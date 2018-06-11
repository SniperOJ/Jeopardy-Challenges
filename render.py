import glob
import json
import os


def render(challenge_type='WEB'):
    template = "## %s\n\n" % (challenge_type.upper())
    challenges = glob.glob("%s/*.json" % (challenge_type))
    for challenge in challenges:
        print challenge
        content = open(challenge).read()
        data = json.loads(content)
        template += "#### %s  \n" % (data['title'])
        template += "* Description: %s  \n" % (data['description'])
        template += "* Points: %s  \n" % (data['points'])
        template += "* References:  \n"
        for reference in data['references']:
            template += "  * %s  \n" % (reference)
        template += "* Attachments:  \n"
        for attachment in data['attachments']:
            template += "  * %s  \n" % (attachment)
        template += "\n"
    with open("%s/README.md" % (challenge_type), "w+") as f:
        f.write(template)


def main():
    types = [x[0].replace("./", "") for x in os.walk(".")][1:]
    for challenge_type in types:
        render(challenge_type=challenge_type)


if __name__ == '__main__':
    main()
