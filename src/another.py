def load_design_from_file(filename):
    xml_file = open('%s/%s' % (settings.PROJECT_ROOT, filename), 'rU')
    xml_string = ''.join([l.strip() for l in xml_file])
    dom1 = parseString(xml_string)
    design_elem = dom1.documentElement
    # design_attrs = parsers.get_attributes_by_element(design_elem)
    design.me = 'tt'
    design_name = design_attrs["id"]
    design = Design.objects.create(name=design_name, xml_file=File(xml_file))
    parsers.load_xml_to_design(design, dom1)
    design.status = Design.STATUS.designed
    design.save()
    return design

def get_workflow_track01():
    wfTrack01 = WorkFlowTrack.objects.create(
        name='wf_name01',
        owner=User.objects.get_or_create(username='default')[0],
        construct_method=settings.APP_WF_CONSTRUCT_METHOD_CONSENSUS,
        bc_prefix='prefix01',
        reuse_oligo=False,
        wf_vendor=Vendor.objects.get_or_create(name='LifeTech')[0])
    wfTrack01.save()
    return wfTrack01



