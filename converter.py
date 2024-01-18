import subprocess


def convert_video_to_mp4(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Successfully Converted!")
    except subprocess.CalledProcessError as e:
        print("Coversion Failed! Error: " + e)

