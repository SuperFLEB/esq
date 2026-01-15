"""
Clever docstring goes here.
"""
import typing
from . import ESQ

ESQ = ESQ.ESQ
ESQStyle: typing.TypeAlias = typing.Callable[[typing.Any], ESQ._ESQBlock]

if __name__ == "__main__":
    emph = ESQ.bright.yellow
    print(
        ESQ.yellow("⠕") +
        ESQ.bright.red("⪫") +
        ESQ.bright.yellow.ESQ("⁓ESQ⁓") +
        ESQ.bright.red("⪪") +
        ESQ.yellow("⠪") +
        ESQ.bright.cyan.italic(
            emph(" E") + "scape " +
            emph("S") + "e" + emph("Q") + "uence... " +
            ESQ.no.italic.white("Uhh...") +
            " Generator"
        ))
    print(__doc__)
