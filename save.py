import pickle
import pandas as pd
import argparse
import matplotlib.pyplot as plt
import os


def readParser():
    parser = argparse.ArgumentParser(description='MBPO')
    parser.add_argument('--csv_path', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    # 从readParser()函数返回的参数对象中获取csv_path，读出dataframe，去除表头，转换为numpy然后存储为pkl文件
    args = readParser()
    df = pd.read_csv(args.csv_path)
    # df = pd.read_csv(args.csv_path)
    # df = df.drop(df.columns[0], axis=1)
    df = df.to_numpy().reshape(-1)
    with open(args.csv_path.split('.')[0] + '.pkl', 'wb') as f:
        pickle.dump(df, f)
        print('save',)
        print(args.csv_path.split('.')[0] + '.pkl')
        f.close()
        
    # data = pickle.load(open(os.path.join('./data/mbpo_original/', fname), 'rb'))
    data = df
        ## plot trial mean
    plt.plot(data['x'], data['y'], linewidth=1.5)
    ## plot error bars
    # plt.fill_between(data['x'], data['y'] - data['std'], data['y'] + data['std'], alpha=0.25)

    plt.legend()

    savepath = args.csv_path.split('.')[0] + '.png'
    plt.savefig(savepath)
