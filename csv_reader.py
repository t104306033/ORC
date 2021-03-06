#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 00:07:47 2018

@author: wei
"""

import csv
from node import Node
from tabulate_text import ORC_status
import matplotlib.pyplot as plt 
from ORC_plot import ProcessPlot, calc_SaturationofCurve, calc_StatusofORC, clear_plot, set_windows

class Paser_data():
    
    def __init__(self, file):
        self.file = file
        self.header = None
        
    def parser_csv(self):
        with open(self.file, 'r', newline='', encoding='utf-16') as file:
            reader = csv.reader(file, delimiter=',')
            data = (row for row in reader)
            for row_index, index in enumerate(data):
                if index[0] == 'Scan':
                    self.header = index
                    self.index = row_index
    
    def read_csv(self):
        with open(self.file, 'r', newline='', encoding='utf-16') as file:
            reader = csv.reader(file, delimiter=',')
            for row in (row for row in reader):
                yield row

def data_gen(filename):
    Data = Paser_data(filename)
    Data.parser_csv()
    header = Data.header
    data = Data.read_csv()
#    head, data = data_gen()
    _cont = 0
    while 1:
        if next(data) == header:
            return header, data
        elif _cont > 10:
            raise Exception("data error") 
        else:
            _cont += 1
            continue

                
def csv_data(data, header,
             pumpi_p='112 <pump inlet> (BAR)',       pumpi_t='101 <pump inlet> (C)',
             pumpo_p='113 <pump outlet> (BAR)',      pumpo_t='102 <pump outlet> (C)',
             EVPo_p ='114 <HX outlet> (BAR)',        EVPo_t='103 <HX outlet> (C)',
             EXPi_p ='115 <expander inlet> (BAR)',   EXPi_t='104 <expander inlet> (C)',
             EXPo_p ='116 <expander outlet> (BAR)',  EXPo_t='105 <expander outlet> (C)',
             CDSi_p ='117 <condenser inlet> (BAR)',  CDSi_t='106 <condenser inlet> (C)',
             CDSo_p ='118 <condenser outlet> (BAR)', CDSo_t='107 <condenser outlet> (C)'):
        pumpi = {'name' : 'pump_inlet',
                 'nid' : 1,
                 'P' : data[header.index(pumpi_p)],
                 'T' : data[header.index(pumpi_t)]}
        pumpo = {'name' : 'pump_ioutlet',
                 'nid' : 2,
                 'P' : data[header.index(pumpo_p)],
                 'T' : data[header.index(pumpo_t)]}
        EVPo = {'name' : 'evaparator_outlet',
                'nid' : 3,
                 'P' : data[header.index(EVPo_p)],
                 'T' : data[header.index(EVPo_t)]}
        EXPi = {'name' : 'expander_inlet',
                'nid' : 4,
                 'P' : data[header.index(EXPi_p)],
                 'T' : data[header.index(EXPi_t)]}
        EXPo = {'name' : 'expander_outlet',
                'nid' : 5,
                 'P' : data[header.index(EXPo_p)],
                 'T' : data[header.index(EXPo_t)]}
        CDSi = {'name' : 'condenser_inlet',
                'nid' : 6,
                 'P' : data[header.index(CDSi_p)],
                 'T' : data[header.index(CDSi_t)]}
        CDSo = {'name' : 'condenser_outlet',
                'nid' : 7,
                 'P' : data[header.index(CDSo_p)],
                 'T' : data[header.index(CDSo_t)]}
        return [pumpi, pumpo, EVPo, EXPi, EXPo, CDSi, CDSo]

def csv_data500(data, header,
                pumpi_p='101 <pump inlet> (BAR)',       pumpi_t='102 <pump inlet> (C)',
                pumpo_p='103 <pump outlet> (BAR)',      pumpo_t='104 <pump outlet> (C)',
                EVPo_p ='105 <evaporater outlet> (BAR)',EVPo_t='106 <evaporalet outlet> (C)',
                EXPi_p ='201 <expander2 inlet> (BAR)',   EXPi_t='202 <expander2 inlet> (C)',
                EXPo_p ='203 <expander2 outlet> (BAR)',  EXPo_t='204 <expander2 outlet> (C)',
                CDSi_p ='111 <condenser inlet> (BAR)',  CDSi_t='112 <condenser inlet> (C)',
                CDSo_p ='113 <condenser outlet> (BAR)', CDSo_t='114 <condenser outlet> (C)'):
        pumpi = {'name' : 'pump_inlet',
                 'nid' : 1,
                 'P' : data[header.index(pumpi_p)],
                 'T' : data[header.index(pumpi_t)]}
        pumpo = {'name' : 'pump_ioutlet',
                 'nid' : 2,
                 'P' : data[header.index(pumpo_p)],
                 'T' : data[header.index(pumpo_t)]}
        EVPo = {'name' : 'evaparator_outlet',
                'nid' : 3,
                 'P' : data[header.index(EVPo_p)],
                 'T' : data[header.index(EVPo_t)]}
        EXPi = {'name' : 'expander_inlet',
                'nid' : 4,
                 'P' : data[header.index(EXPi_p)],
                 'T' : data[header.index(EXPi_t)]}
        EXPo = {'name' : 'expander_outlet',
                'nid' : 5,
                 'P' : data[header.index(EXPo_p)],
                 'T' : data[header.index(EXPo_t)]}
        CDSi = {'name' : 'condenser_inlet',
                'nid' : 6,
                 'P' : data[header.index(CDSi_p)],
                 'T' : data[header.index(CDSi_t)]}
        CDSo = {'name' : 'condenser_outlet',
                'nid' : 7,
                 'P' : data[header.index(CDSo_p)],
                 'T' : data[header.index(CDSo_t)]}
        return [pumpi, pumpo, EVPo, EXPi, EXPo, CDSi, CDSo]
    

def main():
    Data = Paser_data('Data 0x2007 0x0957 2_22_2018 19_05_07.csv')
    Data.parser_csv()
    header = Data.header
    data = Data.read_csv()
    for i in data:
        if i[0] == 'Scan':
            order = i[0]
            print(order)
            break
    for i in data:
        if i[0] == '300':
            for i in data:
                order = i[0]
                dev_list = [pumpi, pumpo, EVPo, EXPi, EXPo, CDSi, CDSo] = csv_data(i, header)
                    
                nodes = []
                for index, obj in enumerate(dev_list):
                    nodes.append(Node(obj['name'], index))
                for index, obj in enumerate(dev_list):
                    nodes[index].set_tp(float(obj['T']), float(obj['P']))
                    nodes[index].pt()
                    
                print(order)
                ORC_status([nodes[a] for a in range(7)])
                
                set_windows()
                plot_SaturationofCurve() 
                plot_StatusofORC(nodes)
        
                # plot process of ORC
                process = [ProcessPlot(0, 1, 'isos'),
                           ProcessPlot(1, 2, 'isop'),
                           ProcessPlot(2, 3, 'isop'),
                           ProcessPlot(3, 4, 'isos'),
                           ProcessPlot(4, 5, 'isop'),
                           ProcessPlot(5, 6, 'isop'),
                           ProcessPlot(6, 0, 'isop')]
                [plot.plot_process(nodes) for plot in process]
                
                ''' 測試
                process = [ProcessPlot(0, 1, 'isos'),
                           ProcessPlot(1, 2, 'isop'),
#                           ProcessPlot(2, 3, 'isop'),
                           ProcessPlot(2, 4, 'isos'),
#                           ProcessPlot(4, 5, 'isop'),
                           ProcessPlot(4, 6, 'isop')]
#                            ProcessPlot(6, 0, 'isop')]
                [plot.plot_process(nodes) for plot in process]
                '''
                plt.pause(0.0000005)
                if order == '':
                    break
                
#    def parser_data(self):
#        [i for i in range(50) if]
#
#def dealwith_csv():
#
#def paser_data():
'''
                pumpi = {'name' : 'pump_inlet',
                         'nid' : 1,
                         'P' : i[24],
                         'T' : i[2]}
                pumpo = {'name' : 'pump_ioutlet',
                         'nid' : 2,
                         'P' : i[26],
                         'T' : i[4]}
                EVPo = {'name' : 'evaparator_outlet',
                        'nid' : 3,
                        'P' : i[28],
                        'T' : i[6]}
                EXPi = {'name' : 'expander_inlet',
                        'nid' : 4,
                        'P' : i[30],
                        'T' : i[8]}
                EXPo = {'name' : 'expander_outlet',
                        'nid' : 5,
                        'P' : i[32],
                        'T' : i[10]}
                CDSi = {'name' : 'condenser_inlet',
                        'nid' : 6,
                        'P' : i[34],
                        'T' : i[12]}
                CDSo = {'name' : 'condenser_outlet',
                        'nid' : 7,
                        'P' : i[36],
                        'T' : i[14]}
'''

    
if __name__=='__main__':
    header, data = data_gen(r'./data/Data 8199 2391 2_13_2018 09_48_30.csv')
#    file = 'Data 8199 2391 2_12_2018 14_23_36.csv'
#    with open(file, 'r', newline='', encoding='utf-16') as file:
#        reader = csv.reader(file, delimiter='\t')
#        data = [row for row in reader]
#        print(data[4][0])

    dia = set_windows()
    sat_line = calc_SaturationofCurve()
    dia.add_line(sat_line[0])
    dia.add_line(sat_line[1])
    for i in data:
        if i[0] == '1500':
            for i in data:
                order = i[0]
                dev_list = [pumpi, pumpo, EVPo, EXPi, EXPo, CDSi, CDSo] = csv_data500(i, header)
                    
                nodes = []
                for index, obj in enumerate(dev_list):
                    nodes.append(Node(obj['name'], index))
                for index, obj in enumerate(dev_list):
                    nodes[index].set_tp(float(obj['T']), float(obj['P']))
                    nodes[index].pt()
                    
                print('index:{}'.format(i[0]))
                ORC_status([nodes[a] for a in range(7)])
                if nodes[3].d < 200 and nodes[4].d < 200:
                    ORC_eff = ((nodes[4].h-nodes[3].h)+(nodes[1].h-nodes[0].h))/(nodes[1].h-nodes[2].h)
                    print('eff:{}'.format(ORC_eff))
                else:
                    print('None')
                
#                globals state_point
                state_point = calc_StatusofORC(nodes, [0, 1, 2, 5])
                dia.add_line(state_point)
                process = [ProcessPlot(0, 1, 'isos'),
                           ProcessPlot(1, 2, 'isop'),
#                           ProcessPlot(2, 3, 'isop'),
                           ProcessPlot(2, 5, 'isos'),
#                           ProcessPlot(4, 5, 'isop'),
                           ProcessPlot(5, 6, 'isop'),
                           ProcessPlot(6, 0, 'isop')]
                good = [plot.plot_process(nodes) for plot in process]
                for i in good:
                    dia.add_line(i[0])
                    dia.add_line(i[1])
                

#                plt.show()
                plt.pause(0.1)
#                plt.close('all')
#                plt.close()
                clear_plot(dia)
                
                if order == '':
                    break

'''
#    for i in data.read_csv():
#        print(i)
#        if i == 0:
#            break
    
#    for i in table:
#        print(i)
#        print(table[i][0])
#        if table[i][0] == 'Scan':
#            print(table[i][0])
#            x = i
#    print(x)
    header_index = table[x]
#    print(header_index)
    
    table_new = []
#    for x in range(x, reader.line_num - 1): 
    for x in range(270, 273):
        table_new.append(table[x + 1])
    
    dev_list = ['<pump inlet>', '<pump outlet>', '<HX outlet>', '<expander inlet>'
                , '<expander outlet>', '<condenser inlet>' , '<condenser outlet>']
    for indexe, i in enumerate(table_new):
        print(indexe)
        pumpi = {'name' : 'pump_inlet',
#                 'nid' : 1,
                 'P' : i[24],
                 'T' : i[2]}
        pumpo = {'name' : 'pump_ioutlet',
#                 'nid' : 2,
                 'P' : i[26],
                 'T' : i[4]}
        EVPo = {'name' : 'evaparator_outlet',
#                'nid' : 3,
                'P' : i[28],
                'T' : i[6]}
        EXPi = {'name' : 'expander_inlet',
#                'nid' : 4,
                'P' : i[30],
                'T' : i[8]}
        EXPo = {'name' : 'expander_outlet',
#                'nid' : 5,
                'P' : i[32],
                'T' : i[10]}
        CDSi = {'name' : 'condenser_inlet',
#                'nid' : 6,
                'P' : i[34],
                'T' : i[12]}
        CDSo = {'name' : 'condenser_outlet',
#                'nid' : 7,
                'P' : i[36],
                'T' : i[14]}
        dev_list = [pumpi, pumpo, EVPo, EXPi, EXPo, CDSi, CDSo]
'''
'''
        nodes = []
        for index, j in enumerate(dev_list):
            nodes.append(Node(j['name'], index))
        for index, j in enumerate(dev_list):
            nodes[index].set_tp(float(j['T']), float(j['P']))
            nodes[index].pt()
            
            
        
        ORC_status([nodes[a] for a in range(7)])
        
        set_windows()
        plot_SaturationofCurve()   
        plot_StatusofORC(nodes)

        # plot process of ORC
        process = [ProcessPlot(0, 1, 'isos'),
                   ProcessPlot(1, 2, 'isop'),
                   ProcessPlot(2, 3, 'isop'),
                   ProcessPlot(3, 4, 'isos'),
                   ProcessPlot(4, 5, 'isop'),
                   ProcessPlot(5, 6, 'isop'),
                   ProcessPlot(6, 0, 'isop')]
        [plot.plot_process(nodes) for plot in process]
        plt.pause(0.00005)
'''     

#        [nodes[k] for k in range(7)]
#        print(i)


#    table_new.reverse()
#    for i in table_new:
#        print(i)


#    reader = csv.DictReader(f)
#    table = []
#    for row in reader:
#        table.append(row)
#        print(row.values())
    
#    for i in range(150):
#        print(table[i])
    