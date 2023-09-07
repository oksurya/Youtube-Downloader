from flask import Flask, request, jsonify, redirect, url_for
from pytube import YouTube
import random

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage_redirect():
    return redirect("https://www.youtube.com/")

@app.route('/watch', methods=['GET'])
def get_video_info_json():
    video_id = request.args.get('v')
    if not video_id:
        return jsonify({"error": "Missing 'v' parameter"}), 400

    video_url = f'https://www.youtube.com/watch?v={video_id}'
    
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

        return jsonify(video_info), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
