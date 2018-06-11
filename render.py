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
        template += "* Description: %s  \n" % (data['description'])
        template += "* Author: [%s](%s)  \n" % (
            data['author_name'],
            data['author_blog']
        )
        template += "* Level: %s  \n" % (":star:" * int(data['level']))
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
    types = [x[0].replace("./", "")
             for x in os.walk(".")
             if not x[0].startswith("./.")
             ][1:]
    for challenge_type in types:
        challenges = glob.glob("%s/*.json" % (challenge_type))
        if len(challenges) == 0:
            continue
        template += '#### %s\n\n' % (challenge_type.upper())
        template += '| Competition | Name | Points | Author | Level |  \n'
        template += '| :---------: | :--: | :----: | :----: | :---: |  \n'
        for challenge in challenges:
            data = json.loads(open(challenge).read())
            competition = "[%s](%s)" % (
                data['competition_name'],
                data['competition_website'],
            )
            name = challenge.split("/")[1].replace(".json", "")
            points = data['points']
            author = "[%s](%s)" % (
                data['author_name'],
                data['author_blog']
            )
            level = ":star:" * int(data['level'])
            template += "|%s|%s|%s|%s|%s|  \n" % (
                competition,
                name,
                points,
                author,
                level,
            )
        template += "\n"
    with open("README.md", "w+") as f:
        f.write(template)


def main():
    render_root()
    types = [x[0].replace("./", "")
             for x in os.walk(".")
             if not x[0].startswith("./.")
             ][1:]
    for challenge_type in types:
        render(challenge_type=challenge_type)


if __name__ == '__main__':
    main()
