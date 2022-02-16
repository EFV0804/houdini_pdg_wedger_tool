"""
INPUT
user_wedgecount = wedge node wedgecount parm // number of work items to create
user_attribute_names = name of the attributes to wedge
user_attribute_types = type of the attribute (float, int, etc)
user_attribute_wedgetypes = type of wedge (range, list etc.)
number_attributes = number of attributes duh




geo = geo to sample from
batch size = how many work item to process at once

geo_cache = cache generated after cooking 


OUTPUT

sim_cache = simulation cache created by TOP network

"""
'''
user_settings = {
    'wedge' : { 'num_wedge_nodes' : 1,
                'wedge_count' : 1,
                'wedge_name': 'wedge_01',
                'num_attributes' : 0,
                'attributes' : {'attrib_01' : { 'name': "heat",
                                                'type': 'float',
                                                'type_index': 0},
                            'attrib_02' : { 'name': "particles",
                                                'type': 'int',
                                                'type_index': 1}  
                                },
    'geo_src': { 'frame_range' : ('$FSTART', '$FEND'),
                 'SOP_path' : 'obj/',
                 'output' : '$HIP/geo',
                 'frames_batch' : 0,
                 'one_batch' : False
                },
    'sim' : {    'SOP_path' : 'obj/',
                 'output' : '$HIP/geo'
    },
    'prev' : {

    }
}
'''
#
# import pdg
# import hou
def data_parser():
    # Gets data from UI sets it into a dict and returns it for main to handle

    # User defined settings: should be retrieved from UI
    user_wedgecount = 2
    user_attribute_names = ['heat', 'particles']
    user_attribute_types = [0, 2]
    user_attribute_wedgetypes = [0, 2]
    number_attributes = len(user_attribute_names)
    num_variations = 4
    variation_values = [10, 2, 6, 3]

    # consts
    ATTRIBUTE_TYPES = ['float', 'floatvector', 'int', 'intvector', 'str', 'color']
    WEDGE_TYPES = ['range', 'value', 'values', 'bracket']

    # dict to return
    user_settings = {
        'wedge': {'wedge_count': user_wedgecount,
                  'wedge_name': 'wedge_01',
                  'num_attributes': len(user_attribute_names),
                  'attributes': {}}}

    # add attrib to dict
    for i in range(user_settings['wedge']['num_attributes']):
        user_settings['wedge']['attributes']['attribute_{}'.format(i + 1)] = {}
        user_settings['wedge']['attributes']['attribute_{}'.format(i + 1)]['name'] = user_attribute_names[i]
        user_settings['wedge']['attributes']['attribute_{}'.format(i + 1)]['type'] = ATTRIBUTE_TYPES[
            user_attribute_types[i]]
        user_settings['wedge']['attributes']['attribute_{}'.format(i + 1)]['type_index'] = user_attribute_types[i]

    #print(user_settings)
    #for attribute in user_settings['wedge']['attributes'].keys():
        #print(user_settings['wedge']['attributes'][attribute]['name'])

    return user_settings

class Wedger():
    def __init__(self):
        self.data = data_parser()

    @property
    def attributes(self):
        return self.data['wedge']['attributes']

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


if __name__ == "__main__":
    wedger = Wedger()
    #print(wedger.attributes)
    for attrib in wedger.attributes.keys():
        print(attrib)