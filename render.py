import glob
import json
import os

dockerfile_repo = "https://github.com/SniperOJ/Challenge-Dockerfiles"


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
        template += "* Dockerfile: [%s](%s)  \n" % (
            name,
            "%s/tree/master/%s/%s" % (
                dockerfile_repo,
                challenge_type,
                name,
            ),
        )
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
        headers = [
            'Competition',
            'Name',
            'Dockerfile',
            'Points',
            'Author',
            'Level',
        ]
        template += '| %s |  \n' % (" | ".join(headers))
        template += '| %s  \n' % (":-: |" * len(headers))
        for challenge in challenges:
            data = json.loads(open(challenge).read())
            competition = "[%s](%s)" % (
                data['competition_name'],
                data['competition_website'],
            )
            challenge_name = challenge.split("/")[1].replace(".json", "")
            name = "[%s](%s#%s)" % (
                challenge_name,
                challenge_type,
                challenge_name,
            )
            points = data['points']
            author = "[%s](%s)" % (
                data['author_name'],
                data['author_blog']
            )
            if data['dockerfile']:
                dockerfile = "[%s](%s)" % (
                    "Dockerfile",
                    "%s/tree/master/%s/%s" % (
                        dockerfile_repo,
                        challenge_type,
                        challenge_name,
                    ),
                )
            else:
                dockerfile = 'RESERVED'
            level = ":star:" * int(data['level'])
            template += "|%s|%s|%s|%s|%s|%s|  \n" % (
                competition,
                name,
                dockerfile,
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
