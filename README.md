# A Computational Proof of the Highest-Scoring Boggle Board

This repo contains the source for the paper "A Computational Proof of the Highest-Scoring Boggle Board" as well as the code listings.

📝 [A Computational Proof of the Highest-Scoring Boggle Board][pdf] (PDF, 2025)

The code in this repo is slow Python that's designed to be simple and clear. For the code used in the full-scale Boggle searches, check out the [hybrid-boggle] repo, which uses Python, C++ and pybind11.

## Development

To make a PDF of the paper, install [typst] (perhaps `brew install typst`) and then run:

    ./make-pdf.sh

To run the tests, you'll need [uv]:

    uv run pytest

[pdf]: /paper.pdf
[uv]: https://github.com/astral-sh/uv
[typst]: https://typst.app/docs
[hybrid-boggle]: https://github.com/danvk/hybrid-boggle/
