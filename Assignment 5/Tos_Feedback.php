<?php include 'header.php'; ?>
<?php
$message = isset($_GET['message']) ? $_GET['message'] : 'No message provided.';
$status = isset($_GET['status']) ? $_GET['status'] : 'info';
?>
<h2>TOS Feedback</h2>
<p class="<?php echo htmlspecialchars($status); ?>"><?php echo htmlspecialchars($message); ?></p>
<a href="Maintenance.php">Back to Maintenance</a>
<?php include 'footer.php'; ?>
