
from gcmpy.joint_degree.joint_degree import JointDegree
from gcmpy.joint_degree.joint_degree_types import JointDegreeType

class JointDegreeManual(JointDegree):
    
    _type: str = JointDegreeType.MANUAL

    def __init__(self, params: dict):
        self._jdd = params['jdd']
        self._motif_sizes = params['motif_sizes']
        self.create_jdd()
        
    def create_jdd(self) -> None:
        return