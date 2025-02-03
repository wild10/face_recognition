import cv2

def read_webcam_and_record(video_source=0, output_file=None):

    # Reading the video from webcamp set to "0"    
    cap = cv2.VideoCapture(video_source)

    # Check if it is correctly opened
    if not cap.isOpened():
        print(f"Error: Could not open video source: {video_source}")
        return

    # get the fps, width and height info from the video captured.
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Defining the video format to safe the recorded
    if output_file:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' codec for MP4 files
        out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))
    
    # start the counting on zero
    frame_count = 0

    while True:
        ret, frame = cap.read() # read the frame
        # check if the frame is correctly loaded.
        if not ret:
            print("Error: Could not read a frame.")
            break

        frame_count += 1
        # Show the video frame number
        cv2.imshow("Video Frame", frame)

        # If the writing option is set TRUE safe, otherways just skip
        if output_file:
            print("yes")
            out.write(frame)

        # print the frame number with , share and dtype used in the terminal
        print(f"Frame {frame_count}: Shape = {frame.shape}, Data Type = {frame.dtype}")
        # To "stop" use the key "q"
        delay = int(1000 / fps)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cap.release()
    if output_file:
        out.release()
    cv2.destroyAllWindows()

  

def read_and_display_video(video_path):

    """Reads a video file, displays it frame by frame, and prints frame information.

    Args:
        video_path: The path to the video file.
    """
    

    try:
        # Open the video file
        cap = cv2.VideoCapture(video_path)

        # Get the video's frame per rate (frames per second)
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Check if the video opened successfully
        if not cap.isOpened():
            print(f"Error: Could not open video file: {video_path}")
            return

        frame_count = 0
        while True:
            # Read a frame from the video
            ret, frame = cap.read()

            # Check if a frame was successfully read
            if not ret:
                # Break the loop if no more frames are available
                break

            frame_count += 1

            # Display the frame
            cv2.imshow("Video Frame", frame)

            # Print frame information (you can customize this)
            print(f"Frame {frame_count}: Shape = {frame.shape}, Data Type = {frame.dtype}")

            # Wait for a key press (1 millisecond delay).  Adjust as needed.
            # Press 'q' to exit.
            delay = int(1000/ fps)
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

        # Release the video capture object and destroy all windows
        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Test the laoding with video previosly safe.
    # video_file = "my_video.mp4"  # Replace with the actual path to your video file
    # read_and_display_video(video_file)

    # Test the video using the webcam
    video_source = 0  # Webcam source
    output_file = "output_video_webcam.mp4"  # Save as MP4
    read_webcam_and_record(video_source, output_file)