
from gcmpy.joint_degree.joint_degree import JointDegree
from gcmpy.joint_degree.joint_degree_types import JointDegreeType

class JointDegreeCover(JointDegree):
    
    _type: str = JointDegreeType.COVER

    @property
    def cover(self) -> list:
        return self._cover 
    @cover.setter
    def cover(self, value: list) -> None:
        self._cover = value

    def __init__(self, params: dict):
        self._cover = params["cover"]
        self._motif_sizes = sorted(
            list(set([len(c) for c in self._cover]))
        )
        self.create_jdd()

    def create_jdd(self) -> None:

        node_ids = list(set([node for clique in self._cover for node in clique]))

        zero_index = 0
        if min(node_ids) != zero_index:
            zero_index = 1

        largest_clique = len(max(self._cover, key = len))

        jds = []
        for _ in range(len(node_ids)):
            jd = [0] * largest_clique
            jds.append(jd)

        for c in self._cover:
            clique_size = len(c)
            for node in c:
                jds[node - zero_index][clique_size-1] += 1

        # iterate each column of the jds and record the index if all zeros
        indxs = [i for i, top in enumerate(zip(*jds)) if not any(top)]
        
        # use the indexes of the zero columns to remove
        for i in indxs:
            for jd in jds:
                del jd[i]

        # convert jds to jdd
        self.convert_jds_to_jdd(jds)
        