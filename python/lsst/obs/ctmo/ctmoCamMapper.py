from lsst.obs.base import CameraMapper

__all__ = ["CtmoCamMapper"]


class CtmoCamMapper(CameraMapper):
    packageName = "obs_ctmo"

    def __init__(self, inputPolicy=None, **kwargs):
        policyFile = Policy.defaultPolicyFile(
            self.packageName, "CtmoMapper.yaml", "policy"
        )
        policy = Policy(policyFile)
