import argparse
import random

import numpy as np
import matplotlib.pyplot as plt


def main(args):
    names = np.genfromtxt(args.input, delimiter=',',
                          dtype='U20',
                          names="name",
                          converters={0: lambda x: x.decode()})
    names = np.char.lower(names)
    unique = np.unique(list(''.join(names)), return_counts=True)
    freq = np.zeros((len(unique[0]),) * 2)
    pos = {k: v for v, k in enumerate(unique[0])}  # lookup table for letters' positions
    for name in names:
        for idx, letter in enumerate(name):
            if idx == 0: continue  # skip first letter
            freq[pos[name[idx - 1]]][pos[letter]] += 1
    freq[np.sum(freq, axis=1) == 0] = 1  # set row to 1 if no letters after
    row_sums = freq.sum(axis=1)
    freq = freq / row_sums[:, np.newaxis]  # normalize
    first_chars = np.unique(names.astype('U1'), return_counts=True)  # get first letters
    first_char_freq = first_chars[1] / np.sum(first_chars[1])

    def generate_name():
        first_letter = np.random.choice(first_chars[0], p=first_char_freq)  # choose random first letter
        new_name = first_letter
        for _ in range(random.randint(len(min(names, key=len)) - 1, len(max(names, key=len)) - 1)):  # make new name
            new_name += np.random.choice(unique[0], p=freq[pos[new_name[-1]]])
        return new_name.capitalize()

    for _ in range(args.n):
        print(generate_name())

    def plot_frequencies(values):
        values = values * 100
        np.savetxt('frequencies.csv', values)
        fig, ax = plt.subplots(1, 1)
        ax.matshow(values, cmap='Blues')
        ax.set_xticks(np.arange(0, len(unique[0])))
        ax.set_yticks(np.arange(0, len(unique[0])))
        ax.set_xticklabels(unique[0])
        ax.set_yticklabels(unique[0])
        ax.tick_params(width=1)
        for (i, j), z in np.ndenumerate(values):
            ax.text(j, i, '{:0.1f}'.format(z), ha='center', va='center', size='x-small')
        plt.show()

    if args.plot:
        plot_frequencies(freq)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='n', type=int, help="Number of generated names")
    parser.add_argument('-p',
                        '--plot',
                        help="Show plot representing probability of changing to another letter",
                        action="store_true",
                        default=False)
    parser.add_argument('-i', '--input', help='Path to csv with names', default='names.csv')
    main(parser.parse_args())
