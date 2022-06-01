from yacs.config import CfgNode as CN
from .shg import HGNETS
from .head import PARSING_HEAD
from .gnn import GNN

MODELS = CN()

MODELS.NAME = "Hourglass"
MODELS.HGNETS = HGNETS
MODELS.DEVICE = "cuda"
MODELS.WEIGHTS = ""
MODELS.HEAD_SIZE  = [[3], [1], [1], [2], [2]]
MODELS.OUT_FEATURE_CHANNELS = 256

MODELS.LINE_CLASS_BIAS = None
MODELS.LOSS_WEIGHTS = CN(new_allowed=True)
MODELS.LINE_LOSS_WEIGHTS = None
MODELS.JUNCTION_LOSS_WEIGHTS = None
MODELS.FALSE_VS_POSITIVE_SAMPLE_RATIO = None
MODELS.USE_GT_JUNCTIONS = False
MODELS.USE_GT_LINES = False

MODELS.PARSING_HEAD   = PARSING_HEAD
MODELS.GNN   = GNN
MODELS.SCALE = 1.0

MODELS.JUNCTION_LABELS = ['invalid', 'valid']
MODELS.LINE_LABELS = ['invalid', 'valid']