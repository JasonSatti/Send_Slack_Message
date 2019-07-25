#!/usr/bin/env python3
# Jason Satti

import argparse
import json

import requests


def slack_info(data):
    """Set Slack instance and data info.

    :param data: Passed in via CLI.
    """
    webhook_url = 'https://hooks.slack.com/T00000000/T025BHZUZ/B00000000/' \
                  'XXXXXXXXXXXXXXXXXXXXXXXX'
    slack_data = {'text': F"{data}"}

    return webhook_url, slack_data


def post_to_channel(url, data):
    """Post message to slack channel.

    :param url: Set in slack_info() and passed in.
    :param data: Set in slack_info() via CLI and passed in.
    """
    response = requests.post(
        url, data=json.dumps(data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )


def main():
    """Post a message to a slack channel via webhook."""
    parser = argparse.ArgumentParser(description='Send Slack message to a '
                                                 'specific channel.')
    parser.add_argument('-d', '--data', required=True, type=str,
                        help='Data to be sent in the message.')
    args = parser.parse_args()

    url, data = slack_info(args.data)
    post_to_channel(url, data)


if __name__ == '__main__':
    main()
