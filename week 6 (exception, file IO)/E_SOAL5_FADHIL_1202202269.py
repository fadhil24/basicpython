blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
{'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5,
'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4,
'Shares': 2},]
total_likes = 0
postn = 1

for post in blog_posts:
    try:
        print("Post ke - ",postn)
        print(f"Post ini memiliki {post['Likes']} likes")
        postn+=1
        total_likes = total_likes + post['Likes']
    #Tambahkan code disini
    except KeyError:
        post['Likes'] = 0
        print("Post ini tidak memiliki likes")
        
print("Jumlah total likes adalah ", total_likes)
