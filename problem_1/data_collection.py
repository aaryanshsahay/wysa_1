import time
import praw

import pandas as pd

import os
from dotenv import load_dotenv
 


def load_data(relevant_posts):
	'''
	Creates a dataframe and saves it as a csv file containing relevant information from posts made on the subreddit r/India.

	:relevant_posts: praw object

	:return: None // Saves a csv file.
	'''
	try:
		posts = []
		
		for post in relevant_posts:	
			posts.append([post.num_comments,post.link_flair_css_class,post.ups,post.upvote_ratio,post.over_18,post.media,post.selftext,post.title,post.url,post.id])

		
		posts = pd.DataFrame(posts,columns=['NumComments','Flair','Upvotes','UpvoteRatio','Over18','Media','Body','Title','URL','ID'])
		posts.to_csv('datacollection.csv',index=False)
		
		print('Data Collection Complete!')
	
	except:
		print('Error occured.')


if __name__ == "__main__":
	try:
		# starting counter
		start = time.time()

		# loading variables
		load_dotenv()
		secret_key = os.environ.get('secret_key')
		client_id = os.environ.get('client_id')
		user_agent = os.environ.get('user_agent')
		
		# initializing praw object
		reddit = praw.Reddit(client_id = client_id, client_secret = secret_key, user_agent = user_agent)
		# getting relevant posts
		relevant_posts = reddit.subreddit('India').top("week",limit = 5000)

		# formatting and saving as csv
		load_data(relevant_posts)

		# ending counter
		end = time.time()

		print(f'Completed!\nTime Taken : {end-start} seconds')

	except:
		print('Error occured.')