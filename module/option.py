import argparse

def command():
    parser = argparse.ArgumentParser(description='Description setting please')
    parser.add_argument('-arg1', dest='arg1', metavar='<arg1>', help='arg1 input', type=str, required=True)
    parser.add_argument('-arg2', dest='arg2', metavar='<arg2>', help='arg2 input', type=str, required=True)
    parser.add_argument('-arg3', dest='arg3', metavar='<arg3>', help='arg3 input', type=str, required=True)
    args = parser.parse_args()

    print(f'arg1: {args.arg1}')
    print(f'arg2: {args.arg2}')
    print(f'arg2: {args.arg3}')

    return args.arg1 #정확한 입력 값 처리를 하기 위해서는 일부 입력 값 정규식 활용