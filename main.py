from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

API_KEY = "4b1a0e44-0205-4ad8-9158-3c10c3e87ae9"


class News:
    def __init__(self, title, description, image_filename):
        self.title = title
        self.description = description
        self.image_filename = image_filename


# Create news objects
news1 = News("Iphone 14 Pro",
             "iPhone 14 Pro and iPhone 14 Pro Max are splash, water, and dust resistant and were tested under controlled laboratory conditions with a rating of IP68 under IEC standard 60529(maximum depth of 6 meters up to 30 minutes.",
             "https://netrinoimages.s3.eu-west-2.amazonaws.com/2022/12/08/1373191/426752/iphone_14_pro_max_3d_model_c4d_max_obj_fbx_ma_lwo_3ds_3dm_stl_4402727_o.png")
news2 = News("New iPadOS 17",
             "iPadOS 17 takes iPad even further. With new levels of personalization, beautiful and helpful custom Lock Screens, and features to help you get more done, iPad is more capable than ever.",
             "https://b2c-contenthub.com/wp-content/uploads/2023/06/iPadOS-17-lock-screen-customization.jpg?quality=50&strip=all&w=1200")
news3 = News("New General AI",
             "The ultimate achievement to some in the AI industry is creating a system with artificial general intelligence (AGI), or the ability to understand and learn any task that a human can.",
             "https://rare-gallery.com/thumbs/1170002-white-digital-art-simple-background-robot-vehicle-sculpture-technology-Toy-machine-artificial-intelligence-Hi-Tech-hand-product.jpg")

# Store news objects in a list
news_list = [news1, news2, news3]


@app.route('/')
def index():
    return render_template('index.html', news_list=news_list)


@app.route('/api/news', methods=['GET'])
def get_news():
    api_key = request.args.get('api_key')

    if api_key != API_KEY:
        return jsonify({'error': 'Invalid API key'}), 401

    news_data = []
    for news in news_list:
        news_data.append({
            'title': news.title,
            'description': news.description,
            'image_filename': news.image_filename
        })
    
    return jsonify({'news': news_data})


if __name__ == '__main__':
    app.run(debug=True)
