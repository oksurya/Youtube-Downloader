import streamlit as st
from pytube import YouTube

# Streamlit app header
st.title("YouTube Video Info")

# Input field for the video URL
video_url = st.text_input("Enter YouTube Video URL:")
if not video_url:
    st.warning("Please enter a YouTube Video URL.")
else:
    try:
        yt = YouTube(video_url)
        video_info = {
            "title": yt.title,
            "author": yt.author,
            "length": yt.length,
            "views": yt.views,
            "publish_date": yt.publish_date,
            "thumbnail_url": yt.thumbnail_url,
            "streams": []
        }

        for stream in yt.streams.all():
            stream_info = {
                "resolution": stream.resolution,
                "mime_type": stream.mime_type,
                "filesize": stream.filesize,
                "bitrate": stream.bitrate,
                "type": "progressive" if stream.is_progressive else "adaptive",
                "download_url": stream.url,
                "is_3d": stream.is_3d,
                "is_hdr": stream.is_hdr,
                "is_live": stream.is_live
            }
            video_info["streams"].append(stream_info)

        # Display video info using Streamlit components
        st.header(video_info["title"])
        st.subheader(f"By: {video_info['author']}")
        st.image(video_info["thumbnail_url"])
        st.write(f"Length: {video_info['length']} seconds")
        st.write(f"Views: {video_info['views']}")
        st.write(f"Published on: {video_info['publish_date']}")
        
        # Display video streams in a table
        st.subheader("Available Video Streams")
        st.table(video_info["streams"])

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

