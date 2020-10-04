# Density

This repo simply optimizes for the density loss between two or more chords.
Density is implemented using the formula described in http://www.ex-tempore.org/harrington/harrington.htm

In short, given a chord we calculate its density and optimize a second chord to match the density of the first.

The target and the input can have arbitrarily many notes. See the `example.ipynb`

## Requirements

`pip install music21 torch torchvision`

for listening the result:

`pip install synthesizer`