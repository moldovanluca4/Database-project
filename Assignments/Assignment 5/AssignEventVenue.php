<?php include 'header.php'; ?>
<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

include 'db_connect.php';

if (isset($_POST['submit'])) {
    $eventID = $_POST['event_id'];
    $venueID = $_POST['venue_id'];

    $stmt = $conn->prepare("UPDATE Event SET Venue_ID = ? WHERE Event_ID = ?");
    $stmt->bind_param('ii', $venueID, $eventID);
    if ($stmt->execute()) {
        header("Location: AssignEventVenue_Feedback.php?status=success&message=" . urlencode("Event assigned to Venue successfully!"));
        exit;
    } else {
        header("Location: AssignEventVenue_Feedback.php?status=error&message=" . urlencode($stmt->error));
        exit;
    }
}

// Fetch all Events
$eventsResult = $conn->query("SELECT Event_ID, Date_ FROM Event");

// Fetch all Venues
$venuesResult = $conn->query("SELECT id, name FROM Venue");
?>

<h2>Assign Event to Venue</h2>
<form method="POST" action="">
    Select Event:
    <select name="event_id" required>
        <?php while($event = $eventsResult->fetch_assoc()) { ?>
            <option value="<?php echo $event['Event_ID']; ?>">
                <?php echo "Event ID: " . $event['Event_ID'] . " | Date: " . $event['Date_']; ?>
            </option>
        <?php } ?>
    </select><br><br>

    Select Venue:
    <select name="venue_id" required>
        <?php while($venue = $venuesResult->fetch_assoc()) { ?>
            <option value="<?php echo $venue['id']; ?>">
                <?php echo $venue['name']; ?>
            </option>
        <?php } ?>
    </select><br><br>

    <input type="submit" name="submit" value="Assign Venue">
</form>

<p><a href="Maintenance.php">Back to Maintenance</a></p>
<?php include 'footer.php'; ?>
