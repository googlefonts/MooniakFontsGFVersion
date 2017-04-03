import os

REMAP_FONTS = [
    ('AbhayaLibre-Bold.ttf', 'AbhayaLibre-Bold.ttf.renamed'),
    ('AbhayaLibre-ExtraBold.ttf', 'AbhayaLibre-ExtraBold.ttf.renamed'),
    ('AbhayaLibre-Medium.ttf', 'AbhayaLibre-Medium.ttf.renamed'),
    ('AbhayaLibre-Regular.ttf', 'AbhayaLibre-Regular.ttf.renamed'),
    ('AbhayaLibre-SemiBold.ttf', 'AbhayaLibre-SemiBold.ttf.renamed'),

    ('GemunuLibre-Bold.ttf', 'GemunuLibre-Bold.ttf.renamed'),
    ('GemunuLibre-ExtraBold.ttf', 'GemunuLibre-ExtraBold.ttf.renamed'),
    ('GemunuLibre-ExtraLight.ttf', 'GemunuLibre-ExtraLight.ttf.renamed'),
    ('GemunuLibre-Light.ttf', 'GemunuLibre-Light.ttf.renamed'),
    ('GemunuLibre-Medium.ttf', 'GemunuLibre-Medium.ttf.renamed'),
    ('GemunuLibre-Regular.ttf', 'GemunuLibre-Regular.ttf.renamed'),
    ('GemunuLibre-SemiBold.ttf', 'GemunuLibre-SemiBold.ttf.renamed'),

    ('PostNoBillsColombo-Bold.ttf', 'PostNoBillsColombo-Bold.ttf.renamed'),
    ('PostNoBillsColombo-ExtraBold.ttf', 'PostNoBillsColombo-ExtraBold.ttf.renamed'),
    ('PostNoBillsColombo-Light.ttf', 'PostNoBillsColombo-Light.ttf.renamed'),
    ('PostNoBillsColombo-Medium.ttf', 'PostNoBillsColombo-Medium.ttf.renamed'),
    ('PostNoBillsColombo-Regular.ttf', 'PostNoBillsColombo-Regular.ttf.renamed'),
    ('PostNoBillsColombo-SemiBold.ttf', 'PostNoBillsColombo-SemiBold.ttf.renamed'),

    ('PostNoBillsJaffna-Bold.ttf', 'PostNoBillsJaffna-Bold.ttf.renamed'),
    ('PostNoBillsJaffna-ExtraBold.ttf', 'PostNoBillsJaffna-ExtraBold.ttf.renamed'),
    ('PostNoBillsJaffna-Light.ttf', 'PostNoBillsJaffna-Light.ttf.renamed'),
    ('PostNoBillsJaffna-Medium.ttf', 'PostNoBillsJaffna-Medium.ttf.renamed'),
    ('PostNoBillsJaffna-Regular.ttf', 'PostNoBillsJaffna-Regular.ttf.renamed'),
    ('PostNoBillsJaffna-SemiBold.ttf', 'PostNoBillsJaffna-SemiBold.ttf.renamed'),

    ('YaldeviColombo-Bold.ttf', 'YaldeviColombo-Bold.ttf.renamed'),
    ('YaldeviColombo-ExtraLight.ttf', 'YaldeviColombo-ExtraLight.ttf.renamed'),
    ('YaldeviColombo-Light.ttf', 'YaldeviColombo-Light.ttf.renamed'),
    ('YaldeviColombo-Medium.ttf', 'YaldeviColombo-Medium.ttf.renamed'),
    ('YaldeviColombo-Regular.ttf', 'YaldeviColombo-Regular.ttf.renamed'),
    ('YaldeviColombo-SemiBold.ttf', 'YaldeviColombo-SemiBold.ttf.renamed'),

    ('YaldeviJaffna-Bold.ttf', 'YaldeviJaffna-Bold.ttf.renamed'),
    ('YaldeviJaffna-ExtraLight.ttf', 'YaldeviJaffna-ExtraLight.ttf.renamed'),
    ('YaldeviJaffna-Light.ttf', 'YaldeviJaffna-Light.ttf.renamed'),
    ('YaldeviJaffna-Medium.ttf', 'YaldeviJaffna-Medium.ttf.renamed'),
    ('YaldeviJaffna-Regular.ttf', 'YaldeviJaffna-Regular.ttf.renamed'),
    ('YaldeviJaffna-SemiBold.ttf', 'YaldeviJaffna-SemiBold.ttf.renamed'),

    ('Mina-Bold.ttf', 'Mina-Bold.ttf.renamed'),
    ('Mina-Regular.ttf', 'Mina-Regular.ttf.renamed'),

]

for old_name, new_name in REMAP_FONTS:
    if old_name in os.listdir('.'):
        os.rename(os.path.join('.', old_name), os.path.join('.', new_name))
        print 'renamed %s to %s' % (old_name, new_name)
print 'Done renaming'
