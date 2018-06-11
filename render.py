import glob
import json
import os


def render(challenge_type='WEB'):
    template = "## %s\n\n" % (challenge_type.upper())
    challenges = glob.glob("%s/*.json" % (challenge_type))
    for challenge in challenges:
        name = challenge.split("/")[1].replace(".json", "")
        data = json.loads(open(challenge).read())
        template += "#### %s  \n" % (name)
        template += "* Author: [%s](%s)  \n" % (
            data['author_name'],
            data['author_blog']
        )
        template += "* Description: %s  \n" % (data['description'])
        template += "* Level: %s  \n" % (data['level'])
        template += "* Points: %s  \n" % (data['points'])
        template += "* Competition: [%s](%s)  \n" % (
            data['competition_name'],
            data['competition_website'],
        )
        template += "* References:  \n"
        for reference in data['references']:
            template += "  * %s  \n" % (reference)
        template += "* Attachments:  \n"
        for attachment in data['attachments']:
            template += "  * %s  \n" % (attachment)
        template += "\n"
    with open("%s/README.md" % (challenge_type), "w+") as f:
        f.write(template)


'''

| Competition | Name | Type | Author | Level | Writeup |
| :--: | :--: | :-----: | :-----: | :-----: | :-----: |
'''


def render_root():
    template = "## Challenges\n\n"
    types = [x[0].replace("./", "") for x in os.walk(".")][1:]
    for challenge_type in types:
        template += '#### %s\n\n' % (challenge_type.upper())
        template += '| Competition | Name | Points | Author | Level |  \n'
        template += '| :---------: | :--: | :----: | :----: | :---: |  \n'
        challenges = glob.glob("%s/*.json" % (challenge_type))
        for challenge in challenges:
            data = json.loads(open(challenge).read())
            competition = data['competition']
            title = data['title']
            points = data['points']
            author = data['author']
            level = data['level']
            template += "|%s|%s|%s|%s|%s|" % (
                competition,
                title,
                points,
                author,
                level,
            )
    with open("README.md" % (challenge_type), "w+") as f:
        f.write(template)


def main():
    # render_root()
    types = [x[0].replace("./", "") for x in os.walk(".")][1:]
    for challenge_type in types:
        render(challenge_type=challenge_type)


if __name__ == '__main__':
    main()
