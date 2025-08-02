import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

def create_posts():
    # Replace 'admin' with your admin username, if different
    author = User.objects.get(username='divya')

    post_data = [
        {
            'title': 'My First Django Project',
            'content': (
                "Navigating the world of Django for the first time was both exciting and challenging. "
                "Setting up the project, configuring apps, and finally seeing my first “Hello, World!” page gave me tremendous satisfaction. "
                "This post details the steps I took, resources that helped, and lessons learned along the way."
            ),
        },
        {
            'title': 'Why I Chose Python',
            'content': (
                "Python’s readability, versatility, and vast ecosystem made it my top choice for web and software development. "
                "From web apps to automation scripts, Python’s approachable syntax has accelerated my programming journey and made learning new concepts much easier."
            ),
        },
        {
            'title': 'A Day in the Life of a Self-Taught Coder',
            'content': (
                "Every coder’s journey is unique, especially for those who are self-taught. "
                "My day starts with reviewing code, tackling new bugs, and exploring new frameworks. "
                "Here, I share my tips for structuring learning and maintaining motivation without a traditional classroom."
            ),
        },
        {
            'title': 'Overcoming Errors: Debugging in Django',
            'content': (
                "Facing bugs is inevitable in coding, but Django provides excellent tools for debugging and troubleshooting. "
                "In this post, I highlight common errors I’ve faced and share the strategies and resources that helped me debug and resolve them efficiently."
            ),
        },
        {
            'title': 'How I Organize My Coding Projects',
            'content': (
                "Keeping projects organized is essential for productivity and scalability. "
                "I use version control, systematic folder structures, and clear documentation. "
                "This habit has improved my workflow and made it easier to revisit and maintain my projects in the long term."
            ),
        },
        # Add more posts if needed
        
    {
        'title': "Why I Can't Stop Binging Anime: My Favorite Must-Watch 'Naruto'",
        'content': (
            "Anime has always been a huge part of my life, and there's one show that stands out above all: 'Naruto'. "
            "It's a story of perseverance, friendship, and growth that resonates deeply. "
            "From epic battles to heartfelt moments, Naruto's characters and world have inspired me in so many ways. "
            "Whether I'm relaxing after a long day or seeking motivation, returning to Naruto is always comforting and energizing."
        ),
    },
    {
        'title': "Why I'm Team Twitter: The Power of a United Community",
        'content': (
            "I really like Twitter because unlike other platforms, it's a place where the whole community "
            "can come together, whether to support a cause or push against something collectively. "
            "This collective energy, despite disagreements, creates a dynamic and vibrant environment that I find fascinating. "
            "It's this communal spirit that keeps me coming back and engaging actively on Twitter."
        ),
    },
    {
        'title': "The Power of Memes: Why Humor Makes Life Easier",
        'content': (
            "Memes and humor are essential to me. In a world that can be stressful, memes offer a quick "
            "breath of fresh air and connection. They make difficult days lighter and help people bond across distances. "
            "I believe that humor humanizes us and brings a sense of community that is truly invaluable. "
            "Keeping laughter alive through memes has been a personal remedy for me."
        ),
    },
    {
        'title': "My Tech Gadget Journey: From Basics to Must-Haves",
        'content': (
            "Technology is constantly evolving, and so has my collection of gadgets. "
            "Starting with just the basics, I have gradually added tools that boost my productivity and enjoyment. "
            "From a reliable laptop to noise-cancelling headphones, these gadgets shape how I work and relax. "
            "Finding the right tech essentials is all about understanding your needs and staying curious."
        ),
    },
]



    for data in post_data:
        Post.objects.create(
            title=data['title'],
            content=data['content'],
            author=author,
            published_date=timezone.now()
        )
    print("Database populated with new blog posts!")

if __name__ == '__main__':
    create_posts()
