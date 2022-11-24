<!DOCTYPE html>
<html>
<body>

<form action="/" method="post" enctype="multipart/form-data">
	Select image to upload:
	<input type="file" name="fileToUpload" id="fileToUpload">
	<input type="submit" value="Upload Image" name="submit">
</form>

</body>
</html>



<?php
	if(isset($_POST["submit"])) 
	{
		$target_dir = "./";
		// if (!file_exists($target_dir)) mkdir($target_dir, 777, true);
		$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
		$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
		if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
			echo "The file ". htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])). " has been uploaded.";
		} 
		else 
		{
			echo "Sorry, there was an error uploading your file.";
		}
	}

?>
