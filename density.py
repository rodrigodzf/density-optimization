import torch


def density(freqs, mode='d'):
    '''
      Get the desity of a 1D tensor chord
    '''
    if mode == 'b':
        return torch.log10(torch.sum(freqs)) + freqs.shape[0]

    combs = torch.combinations(freqs, 2)
    density = (combs[:, 0] / combs[:, 1])
    density = torch.sum(density) / combs.shape[0]

    if mode == 'd':
        return 1.0 / density
    else:
        return (1.0 / density) + combs.shape[0]
