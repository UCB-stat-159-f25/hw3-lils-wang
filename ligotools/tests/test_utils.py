import pytest
import numpy as np
from ligotools.utils import whiten, reqshift, generate_plot, write_wavfile




def test_whiten_output():
    fs = 4096
    dt = 1.0 / fs
    freq = 50
    time = np.linspace(0,1,int(1/dt))
    expected = np.sin(2*np.pi*50*time) +0.1*np.random.randn(len(time))
    def interp_psd(freqs):
        return np.ones_like(freqs)*1e-45
    whitened = whiten(expected,interp_psd,dt)
    assert len(expected) == len(whitened)


def test_reqshift_output():
    fs = 4096
    time = np.linspace(0,1,fs,endpoint=False)
    freq = 50
    expected = np.sin(2*np.pi*freq*time)
    sample_rate = fs
    shift = 100
    shifted = reqshift(expected, shift, sample_rate)
    assert len(shifted) == len(expected)