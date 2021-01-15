import sys


class NodeData:

    def __init__(self, node_id: int, pos: tuple = None):
        self.__node_id = node_id
        self.info = ""
        self.weight = 0
        self.tag = 0
        self.pos = pos
        self.inside = 0
        self.outside = 0

    def get_id(self):
        """
        :return: the node id value.
        """
        return self.__node_id

    def get_weight(self):
        """

        :return: the node weight value.
        """
        return self.weight

    def set_weight(self, weight_value: float):
        """
         weight setter
        :param weight_value:
        :return:
        """
        self.weight = weight_value

    def get_tag(self):
        """

         the node tag value.
        """
        return self.tag

    def set_tag(self, tag_value: str):
        """
        tag setter.
        :param tag_value:
        """
        self.tag = tag_value

    def get_info(self):
        """

        :return: the node info value.
        """
        return self.info

    def set_info(self, info_value: str):
        """
        info setter.
        :param info_value:
        """
        self.info = info_value

    def get_pos(self):
        """

        :return: the node position.
        """
        return self.pos

    def set_pos(self, x: float, y: float, z: float):
        """
        position setter.
        :param x:
        :param y:
        :param z:
        """
        self.pos = [x, y, z]

    def __lt__(self, other):

        if self.weight == other.weight:
            return True
        else:
            return self.weight < other.weight

    def __repr__(self):

        return "%s: |edges out| %s |edges in| %s"%(self.__node_id, self.outside, self.inside)