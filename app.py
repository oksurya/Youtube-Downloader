import streamlit as st
from pytube import YouTube

st.title("YouTube Video Information")

video_url = st.text_input("Enter YouTube Video URL")
if not video_url:
    st.error("Please enter a YouTube Video URL")
else:
    # Check if the URL contains 'youtube.com/watch?v=' and extract the video ID
    video_id = None
    if 'youtube.com/watch?v=' in video_url:
        video_id = video_url.split('youtube.com/watch?v=')[1]

    if video_id:
        try:
            yt = YouTube(video_url)
            st.subheader("Video Information")
            st.write(f"Title: {yt.title}")
            st.write(f"Author: {yt.author}")
            st.write(f"Length: {yt.length} seconds")
            st.write(f"Views: {yt.views}")
            st.write(f"Publish Date: {yt.publish_date}")
            st.image(yt.thumbnail_url)

            st.subheader("Available Streams")
            streams = yt.streams.all()
            for i, stream in enumerate(streams):
                st.write(f"Stream {i+1}:")
                st.write(f"Resolution: {stream.resolution}")
                st.write(f"MIME Type: {stream.mime_type}")
                st.write(f"Filesize: {stream.filesize}")
                st.write(f"Bitrate: {stream.bitrate}")
                st.write(f"Type: {'progressive' if stream.is_progressive else 'adaptive'}")
                st.write(f"Download URL: {stream.url}")
                st.write(f"Is 3D: {stream.is_3d}")
                st.write(f"Is HDR: {stream.is_hdr}")
                st.write(f"Is Live: {stream.is_live}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Invalid YouTube Video URL. Please use a URL in the format 'https://www.youtube.com/watch?v=VIDEO_ID'.")
