<?php include 'header.php'; ?>
<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

include 'db_connect.php';

if (isset($_POST['submit'])) {

    // Generate new Exam ID
    $stmt = $conn->prepare("SELECT MAX(Exam_ID) AS max_id FROM Exam");
    $stmt->execute();
    $result = $stmt->get_result();
    $row = $result->fetch_assoc();
    $newExamID = $row['max_id'] + 1;

    // Read input
    $examName = $_POST['exam_name'];
    $major = $_POST['major'];
    $duration = $_POST['duration'] . ":00";
    $examDatetime = str_replace('T', ' ', $_POST['exam_datetime']) . ':00';

    // Check for past date
    if (strtotime($examDatetime) < time()) {
        header("Location: Exam_Feedback?status=error&message=" . urlencode("You cannot select a past date/time."));
        exit;
    }

    // Check for conflicts (3-hour window)
    $conflictQuery = "
        SELECT e.Date_ FROM Event e
        JOIN Exam ex ON ex.Event_ID = e.Event_ID
        WHERE ABS(TIMESTAMPDIFF(HOUR, e.Date_, ?)) < 3
        UNION ALL
        SELECT e.Date_ FROM Event e
        JOIN Ceremony c ON c.Event_ID = e.Event_ID
        WHERE ABS(TIMESTAMPDIFF(HOUR, e.Date_, ?)) < 3
    ";
    $stmt = $conn->prepare($conflictQuery);
    $stmt->bind_param('ss', $examDatetime, $examDatetime);
    $stmt->execute();
    $conflicts = $stmt->get_result();

    if ($conflicts->num_rows > 0) {
        header("Location: Exam_Feedback.php?status=error&message=" . urlencode("There is an Exam, Ceremony, or TOS within 3 hours of your selected time."));
        exit;
    }

    // Generate new Event ID
    $stmt = $conn->prepare("SELECT MAX(Event_ID) AS max_id FROM Event");
    $stmt->execute();
    $eventRow = $stmt->get_result()->fetch_assoc();
    $newEventID = $eventRow['max_id'] + 1;

    // Insert Event
    $stmt = $conn->prepare("INSERT INTO Event (Event_ID, Venue_ID, Date_) VALUES (?, NULL, ?)");
    $stmt->bind_param('is', $newEventID, $examDatetime);
    $stmt->execute();

    // Insert Exam
    $stmt = $conn->prepare("INSERT INTO Exam (Exam_ID, Event_ID, Exam_Name, Major, Duration) VALUES (?, ?, ?, ?, ?)");
    $stmt->bind_param('iisss', $newExamID, $newEventID, $examName, $major, $duration);
    if ($stmt->execute()) {
        header("Location: Exam_Feedback.php?status=success&message=" . urlencode("Exam inserted successfully! ID: $newExamID"));
        exit;
    } else {
        header("Location: Exam_Feedback.php?status=error&message=" . urlencode($stmt->error));
        exit;
    }
}
$conn->close();
?>

<h2>Add Exam</h2>
<form method="POST" action="">
    Exam Name: <input type="text" name="exam_name" required><br><br>
    Major: <input type="text" name="major" required><br><br>
    Duration: <input type="time" name="duration" required><br><br>
    Select Date and Time:
    <input type="datetime-local" name="exam_datetime" required min="<?php echo date('Y-m-d\TH:i'); ?>"><br><br>
    <input type="submit" name="submit" value="Add Exam">
</form>

<p><a href="Maintenance.php">Back to Maintenance</a></p>
<?php include 'footer.php'; ?>
