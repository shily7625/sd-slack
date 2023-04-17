import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', type=str, help='Slack Bot Token')
    parser.add_argument('--channel-id', type=str, help='Slack Channel ID')
    args = parser.parse_args()

    if args.token:
        with open('token.txt', 'w') as f:
            f.write(args.token)
        f.close()
    if args.channel_id:
        with open('channel-id.txt', 'w') as f:
            f.write(args.channel_id)
        f.close()