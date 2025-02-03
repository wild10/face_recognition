import cv2

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
    video_file = "my_video.mp4"  # Replace with the actual path to your video file
    read_and_display_video(video_file)