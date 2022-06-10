'''
Description: 
Author: JinShiyin
Email: shiyinjin@foxmail.com
Date: 2022-03-04 17:21:08
'''
def get_parameter_number(model):
    total_num = sum(p.numel() for p in model.parameters())
    trainable_num = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f'Total: {total_num}, Trainable: {trainable_num}')
    return {'Total': total_num, 'Trainable': trainable_num}


from components.Conditional_Generator_asm import Generator

generator = Generator(class_num=1)
get_parameter_number(generator)