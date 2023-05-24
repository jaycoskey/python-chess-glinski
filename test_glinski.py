#!/usr/bin/env python

import logging
import sys
import unittest

from test_utils import RaiseLogHandler, catchAndSkip


# Compare with parent repo's SquareTestCase
class BoardGeometryTestCase(unittest.TestCase):
    def test_cell_coords(self):  # Coordinates of corner & center cells.
        raise NotImplementedError

    def test_cell_distances(self):
        raise NotImplementedError

    def test_cell_sets(self):
        raise NotImplementedError

    def test_conversion_hex(self):  # ID => hex coords => ID
        raise NotImplementedError

    def test_conversion_rank_file(self):  # ID => rank & file => ID
        raise NotImplementedError

    def test_hex_coordinates(self):  # classes HexPos and HexVec
        raise NotImplementedError


class BoardTestCase(unittest.TestCase):
    def test_board_constructor_empty(self):  # Assert zero pieces.
        raise NotImplementedError

    def test_board_constructor_default(self):  # Assert correct placement.
        raise NotImplementedError

    def test_board_constructor_fen(self):
        raise NotImplementedError

    def test_board_zobrist_hash(self):
        raise NotImplementedError


class ConsistencyTestCase(unittest.TestCase):
    def test_consistency_of_bitvector_contants(self):
        raise NotImplementedError


class GameEndTestCase(unittest.TestCase):
    def test_check_detection(self):
        raise NotImplementedError

    def test_checkmate_detection(self):
        raise NotImplementedError

    def test_stalemate_from_inactivity(self):  # 50 and 75 move rules
        raise NotImplementedError

    def test_stalemate_from_insufficient_resources(self):
        raise NotImplementedError

    def test_stalemate_from_lack_of_moves(self):
        raise NotImplementedError

    def test_stalemate_from_repetition(self):
        """x3 and x5, Zobrist hash used for detection"""
        raise NotImplementedError


class GameRecordsTestCase(unittest.TestCase):
    def test_pgn_logs(self):
        raise NotImplementedError

    def test_uci(self):
        raise NotImplementedError


class GameTreeTestCase(unittest.TestCase):
    def test_endgame_search(self):  # Mate in 1, mate in 2, mate in 3
        raise NotImplementedError


class PieceTestCase(unittest.TestCase):
    def test_en_passant(self):
        # Cases where en passant is available; case where it is unavailable.
        raise NotImplementedError

    def test_legal_moves_obstructed(self):
        # Sliders and leapers, obstructed by both own and opponent pieces.
        raise NotImplementedError

    def test_legal_moves_singletons(self):
        # For all piece types and positions on otherwise empty board.
        # Test pawns only for cells they can possibly occupy.
        raise NotImplementedError

    def test_legal_moves_starting_positions(self):
        # Test legal move counts of all pieces in starting position.
        # K:2, Q:6, R:6, B:12, N:6, P:17. Total = 55 per player.
        raise NotImplementedError


if __name__ == "__main__":
    verbosity = sum(arg.count("v") for arg in sys.argv if all(c == "v" for c in arg.lstrip("-")))
    verbosity += sys.argv.count("--verbose")

    if verbosity >= 2:
        logging.basicConfig(level=logging.DEBUG)

    raise_log_handler = RaiseLogHandler()
    raise_log_handler.setLevel(logging.ERROR)
    logging.getLogger().addHandler(raise_log_handler)

    unittest.main()
