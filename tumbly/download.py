import argparse
import sqlite3
import sys
import os
import urllib.request


''' Downloading Functions '''


def download_images(username,
                    database_name,
                    downloaded_image_directory,
                    number):

    # Connect to database
    con = sqlite3.connect(database_name)

    with con:
        # Get image urls from photos table
        cur = con.cursor()
        cur.execute("SELECT url FROM photos")

        # Init J
        j = 0
        while j < number:
            for url in cur:
                for i in url:
                    print('Image url: ' + i)
                    os.chdir(downloaded_image_directory)
                    image_name = (username + '_' + str(j) + '.jpg')
                    urllib.request.urlretrieve(i, image_name)
                    print ('Downloaded: {0}'.format(image_name))
                    j += 1

        print('Finished scraping and downloading')


def main():

    # Init argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('-u',
                        '--username',
                        type=str,
                        help='The username of the tumblr user whos '
                             'tumblr you wish to scrape.',
                        required=True)

    parser.add_argument('-n',
                        '--number',
                        type=int,
                        help='The number of images to scrape.',
                        required=True)

    parser.add_argument('-o',
                        '--start',
                        type=int,
                        help='Post number to start from (offset).',
                        required=False)

    args = parser.parse_args()

    # Set variables

    username = args.username
    number = args.number
    offset = args.start


if __name__ == '__main__':
    main()
