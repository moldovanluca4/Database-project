<?php
ini_set('display_errors', '0');
ini_set('display_startup_errors', '0');

set_exception_handler(function (Throwable $error) {
    error_log('Campus request failed (' . get_class($error) . ')');
    http_response_code(500);
    exit('An unexpected error occurred. Please try again later.');
});

$settings = [];
foreach (['DB_HOST', 'DB_USER', 'DB_PASS', 'DB_NAME'] as $name) {
    $value = getenv($name);
    if ($value === false || $value === '') {
        throw new RuntimeException('Required database configuration is missing');
    }
    $settings[$name] = $value;
}

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$conn = new mysqli(
    $settings['DB_HOST'],
    $settings['DB_USER'],
    $settings['DB_PASS'],
    $settings['DB_NAME']
);
?>
