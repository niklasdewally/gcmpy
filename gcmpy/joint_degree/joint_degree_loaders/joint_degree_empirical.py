

from gcmpy.joint_degree.joint_degree import JointDegree
from gcmpy.joint_degree.joint_degree_types import JointDegreeType

class JointDegreeEmpirical(JointDegree):
    
    _type: str = JointDegreeType.EMPIRICAL
    _empirical_jds: list = []

    @property
    def empirical_jds(self) -> list:
        return self._empirical_jds
    @empirical_jds.setter
    def empirical_jds(self, value: list) -> None:
        self._empirical_jds = value

    def __init__(self, params: dict):
        self._motif_sizes = params['motif_sizes']
        self._empirical_jds = params['empirical_jds']
        self.create_jdd()

    def create_jdd(self) -> None:
        self.convert_jds_to_jdd(self._empirical_jds)