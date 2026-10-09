<?php include 'header.php'; ?>
<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

include 'db_connect.php';

if (isset($_POST['submit'])) {

    // Generate Ceremony ID
    $stmt = $conn->prepare("SELECT MAX(Ceremony_ID) AS max_id FROM Ceremony");
    $stmt->execute();
    $newCeremonyID = $stmt->get_result()->fetch_assoc()['max_id'] + 1;

    $ceremonyName = $_POST['ceremony_name'];

    // Generate new Event ID
    $stmt = $conn->prepare("SELECT MAX(Event_ID) AS max_id FROM Event");
    $stmt->execute();
    $newEventID = $stmt->get_result()->fetch_assoc()['max_id'] + 1;

    // Insert Event
    $stmt = $conn->prepare("INSERT INTO Event (Event_ID, Venue_ID, Date_) VALUES (?, NULL, NULL)");
    $stmt->bind_param('i', $newEventID);
    $stmt->execute();

    // Insert Ceremony
    $stmt = $conn->prepare("INSERT INTO Ceremony (Ceremony_ID, Event_ID, Name_) VALUES (?, ?, ?)");
    $stmt->bind_param('iis', $newCeremonyID, $newEventID, $ceremonyName);
    if ($stmt->execute()) {
        header("Location: Ceremony_Feedback.php?status=success&message=" . urlencode("Ceremony inserted successfully! ID: $newCeremonyID"));
        exit;
    } else {
        header("Location: Ceremony_Feedback.php?status=error&message=" . urlencode($stmt->error));
        exit;
    }
}
$conn->close();
?>

<h2>Add Ceremony</h2>
<form method="POST" action="">
    Ceremony Name: <input type="text" name="ceremony_name" required><br><br>
    <input type="submit" name="submit" value="Add Ceremony">
</form>

<p><a href="Maintenance.php">Back to Maintenance</a></p>
<?php include 'footer.php'; ?>
