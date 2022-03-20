

from gcmpy.joint_degree.joint_degree_types import JointDegreeType
from gcmpy.joint_degree.joint_degree import JointDegree
from gcmpy.joint_degree.joint_degree_factory import JointDegreeFactory


class JointDegreeDistribution:
    """
    Determines the type of JointDegree subclass to return. Expects `params` 
    dict to contain key `joint_degree_type'. 
    :method load_joint_degree: returns a subclass of ABC `JointDegree`. This 
    will raise an error if the params dict does not contain the required keys.
    """
    @staticmethod
    def load_joint_degree(params: dict) -> JointDegree:
        try:
            input_type = JointDegreeType(params["joint_degree_type"])
        except Exception as e:
            raise(f"Error instantiating JointDegreeDistribution: {e}")
        loader: JointDegree = JointDegreeFactory.resolve_joint_degree(input_type,params)
        loader.create_jdd()
        return loader