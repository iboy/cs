<?php
// Connect to database
$conn = mysqli_connect('localhost', 'root', '', 'booking_system');

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Get all events
$sql = "SELECT * FROM events";
$result = mysqli_query($conn, $sql);

// Display events in a table
echo "<h2>Events</h2>";
echo "<a href='create.php'>Create New Event</a>";
echo "<table>";
echo "<tr><th>ID</th><th>Name</th><th>Date</th><th>Time</th><th>Location</th><th>Capacity</th><th>Description</th><th>Image</th><th>Actions</th></tr>";
while ($row = mysqli_fetch_assoc($result)) {
    echo "<tr>";
    echo "<td>".$row['EventID']."</td>";
    echo "<td>".$row['EventName']."</td>";
    echo "<td>".$row['EventDate']."</td>";
    echo "<td>".$row['EventTime']."</td>";
    echo "<td>".$row['Location']."</td>";
    echo "<td>".$row['Capacity']."</td>";
    echo "<td>".$row['Description']."</td>";
    echo "<td><img src='".$row['ImageURL']."' width='100'></td>";
    echo "<td>";
    echo "<a href='read.php?id=".$row['EventID']."'>Read</a> ";
    echo "<a href='update.php?id=".$row['EventID']."'>Update</a> ";
    echo "<a href='delete.php?id=".$row['EventID']."'>Delete</a>";
    echo "</td>";
    echo "</tr>";
}
echo "</table>";

// Close connection
mysqli_close($conn);
?>