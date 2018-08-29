# -*- coding:utf-8 -*-
import re, os, errno, cgi, json, xml, logging, numpy
import sys, codecs, locale, getopt
import xml.etree.ElementTree as ET
from subprocess import Popen, PIPE
from operator import itemgetter
from xml.dom.minidom import parse, parseString
from imp import reload
from collections import defaultdict

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def main():
    # to be adjusted as needed
    pos='Prop'
    in_dir = '01_txt'
    out_dir = '02_xml'
    cwd = os.getcwd()
    out_dir_path = os.path.join(cwd,out_dir)
    if not os.path.exists(out_dir_path):
        os.mkdir(out_dir_path)
        
    if fst_type == 'xfst':
        plup = Popen('which lookup', shell=True, stdout=PIPE, stderr=PIPE)
        olup, elup = plup.communicate()
        #print("___ lookup is ",olup.decode())
    if fst_type == 'hfstol':
        plup = Popen('which hfst-optimised-lookup', shell=True, stdout=PIPE, stderr=PIPE)
        olup, elup = plup.communicate()
        #print("___ lookup is ",olup.decode())
    if not olup.decode():
        print('No lookup found, please install it!')
        sys.exit('Error')
    lookup = olup.decode().strip()
    
    
    
    
    
    # parameters to be adjusted as needed
    plup = Popen('which lookup', shell=True, stdout=PIPE, stderr=PIPE)
    olup, elup = plup.communicate()
    print("___ lookup is ",olup.decode())
    if not olup.decode():
        print('No lookup found, please install it!')
        sys.exit()
    
    lookup = olup.decode().strip()
    langs_dir = '$GTHOME/langs/'
    xfst_file = '/src/analyser-gt-'
    
    for root, dirs, files in os.walk(in_dir):
    
        for f in files:
            if f.endswith('txt'):
                print('... processing ', str(f))
                file_name = f[:-4]
                tree = ET.ElementTree(ET.fromstring('<text id="' + file_name + '"></text>'))
                f_root = tree.getroot()
                
                with open(in_dir+'/'+f, encoding='utf-8-sig') as cf:
                    file_content = cf.read() # Read whole file in the file_content string
                    
                pages = numpy.asarray(file_content.split(''))
                print('_PAGES_ ', len(pages))
                page_counter = 0
                for page in pages:
                    #print('-+- ', page)
                    if not page == '\n':
                        page_counter += 1
                        pEl = ET.SubElement(f_root, 'page')
                        pEl.set('id', str(page_counter))
                        # pEl.text = '\n'+page
                        
                        lines = numpy.asarray(page.split('\n'))
                        line_counter = 0
                        for line in lines:
                            line.strip()
                            if line:
                                line_counter += 1
                                lEl = ET.SubElement(pEl, 'line')
                                lEl.set('id', str(line_counter))
                                # lEl.text = line
                        
                        
        indent(f_root)
        
        tree.write(os.path.join(out_dir_path,str(file_name+'.xml')),
                       xml_declaration=True,encoding='utf-8',
                       method="xml")
        print('DONE ', f)


def checkAnalysis(fst_type, fst, name, lang_code):
    
    _fst_type = fst_type
    _fst = fst
    _name = name
    _lang_code = lang_code
    
    spelling=_name.find('spelling').text
    
    print('... lemma ', str(spelling))
    
    cmd = " | lookup -q -flags mbTT " + _fst
    
    p = Popen('echo "'+spelling+'"'+cmd, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    c_analysis = ''
    filtered_analysis = ''
    print("|", out.decode().split('\n', 1 ),"|")
    current_analysis = filter(None,out.decode().split('\n\n'))
    
    for current_cohort in current_analysis:
        cc_list = current_cohort.split('\n')
        # set default analysis value to 'no'
        _name.find('spelling').set(_fst_type+'_fst', 'no')
        for analysis in cc_list:
            analysis = analysis.partition('\t')[2]
            if '+Prop+' in analysis:
                # due to tags in nob output
                if _lang_code is 'nob':
                    _name.find('spelling').set(_fst_type+'_fst', 'yes')
                    break
                # due to tags in non-nob output
                if analysis.endswith('+Nom') and not _lang_code is 'nob':
                    _name.find('spelling').set(_fst_type+'_fst', 'yes')
                    break
                    
            # refine analysis: check with Nåebrie, Storfjellet and kommunenavn Lierne
            # this is easier done via xsl: both files are xml-files
            
    return _name
        
        
if __name__ == "__main__":
    reload(sys)
    main()



