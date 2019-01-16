"""
Various exceptions for working with stereovision.

Classes:

    * ``ChessboardNotFoundError``

    * ``BadBlockMatcherArgumentError``

        * ``StereoBMError``

            * ``InvalidBMPresetError``
            * ``InvalidSearchRangeError``
            * ``InvalidWindowSizeError``

        * ``StereoSGBMError``

            * ``InvalidNumDisparitiesError``
            * ``InvalidSADWindowSizeError``
            * ``InvalidFirstDisparityChangePenaltyError``
            * ``InvalidSecondDisparityChangePenaltyError``
            * ``InvalidUniquenessRatioError``
            * ``InvalidSpeckleWindowSizeError``
            * ``InvalidSpeckleRangeError``

.. image:: classes_exceptions.svg
    :width: 100%
"""

class ChessboardNotFoundError(Exception):
    """No chessboard could be found in searched image."""


class BadBlockMatcherArgumentError(Exception):
    """Bad argument supplied for a ``BlockMatcher``."""

class StereoBMError(BadBlockMatcherArgumentError):
    """Bad argument supplied for a ``StereoBM``."""

class StereoSGBMError(BadBlockMatcherArgumentError):
    """Bad argument supplied for a ``StereoSGBM``."""

class InvalidBMPresetError(StereoBMError):
    """Invalid BM preset."""

class InvalidSearchRangeError(StereoBMError):
    """Invalid search range."""

class InvalidWindowSizeError(StereoBMError):
    """Invalid search range."""

class InvalidNumDisparitiesError(StereoSGBMError):
    """Invalid number of disparities."""

class InvalidSADWindowSizeError(StereoSGBMError):
    """Invalid search window size."""

class InvalidFirstDisparityChangePenaltyError(StereoSGBMError):
    """Invalid first disparity change penalty."""

class InvalidSecondDisparityChangePenaltyError(StereoSGBMError):
    """Invalid second disparity change penalty."""

class InvalidUniquenessRatioError(StereoSGBMError):
    """Invalid uniqueness ratio."""

class InvalidSpeckleWindowSizeError(StereoSGBMError):
    """Invalid speckle window size."""

class InvalidSpeckleRangeError(StereoSGBMError):
    """Invalid speckle range."""
