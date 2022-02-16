import hou

class Wedger():
    def __init__(self):
        self.user_settings = data_parser()

    @property
    def user_settings(self):
        return self.user_settings

    @property
    def attributes(self):
        return self.user_settings['wedge']['attributes']

    def run():
        # #User defined settings
        # user_wedgecount = 2
        # user_attribute_names = ['attribute_01', 'attribute_02']
        # user_attribute_types = [0, 2]
        # user_attribute_wedgetypes = [0, 2]
        # number_attributes = len(user_attribute_names)
        # num_variations = 4
        # variation_values = [10,2,6,3]
        #
        # #consts
        # attribute_types = ['float', 'floatvector', 'int', 'intvector', 'str', 'color']
        # wedge_types = ['range', 'value', 'values', 'bracket']


        #obj/topnet
        obj_context = hou.node('obj/')
        topnet = obj_context.createNode('topnet')

        #wedge nodehou
        wedge = topnet.createNode('wedge', 'wedge_01')
        wedge.parm('wedgecount').set(user_wedgecount)
        wedge.parm('wedgeattributes').set(number_attributes)

        for index in range(number_attributes):
            attrib_type = attribute_types[user_attribute_types[index]]
            wedge_type = wedge_types[user_attribute_wedgetypes[index]]


            wedge.parm('name{0}'.format(index+1)).set(user_attribute_names[index])
            wedge.parm('type{0}'.format(index+1)).set(user_attribute_types[index])
            wedge.parm('wedgetype{0}'.format(index+1)).set(user_attribute_wedgetypes[index])
            if user_attribute_wedgetypes[index] == 2:
                attrib_num = index + 1
                wedge.parm('{wedge_type}{attrib_num}').set(num_variations)
                for num in range(num_variations):

                    wedge.parm('{0}value{1}_{2}'.format(attribute_types[attrib_type],index+1, num+1)).set(variation_values[num])

