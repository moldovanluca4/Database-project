<?php include 'header.php'; ?>
<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

include 'db_connect.php';

if (isset($_POST['submit'])) {

  
    $stmt = $conn->prepare("SELECT MAX(Tos_ID) AS max_id FROM TOS");
    $stmt->execute();
    $newTosID = $stmt->get_result()->fetch_assoc()['max_id'] + 1;

    $ticketPrice = $_POST['ticket_price'];
    $theme = $_POST['theme'];

    
    $stmt = $conn->prepare("SELECT MAX(Event_ID) AS max_id FROM Event");
    $stmt->execute();
    $newEventID = $stmt->get_result()->fetch_assoc()['max_id'] + 1;

    
    $stmt = $conn->prepare("INSERT INTO Event (Event_ID, Venue_ID, Date_) VALUES (?, NULL, NULL)");
    $stmt->bind_param('i', $newEventID);
    $stmt->execute();

    
    $stmt = $conn->prepare("INSERT INTO TOS (Tos_ID, Event_ID, Ticket_price, Theme) VALUES (?, ?, ?, ?)");
    $stmt->bind_param('iiss', $newTosID, $newEventID, $ticketPrice, $theme);
    if ($stmt->execute()) {
        header("Location: Tos_Feedback.php?status=success&message=" . urlencode("TOS inserted successfully! ID: $newTosID"));
        exit;
    } else {
        header("Location: Tos_Feedback.php?status=error&message=" . urlencode($stmt->error));
        exit;
    }
}
$conn->close();
?>

<h2>Add TOS</h2>
<form method="POST" action="">
    Ticket Price: <input type="number" name="ticket_price" required><br><br>
    Theme: <input type="text" name="theme" required><br><br>
    <input type="submit" name="submit" value="Add TOS">
</form>

<p><a href="Maintenance.php">Back to Maintenance</a></p>
<?php include 'footer.php'; ?>
