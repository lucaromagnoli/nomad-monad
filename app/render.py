import os
from io import BytesIO

from django.contrib.staticfiles import finders
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from project import settings


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = [os.path.realpath(path) for path in result]
        path=result[0]
    else:
        s_url = settings.STATIC_URL        # Typically /static/
        s_root = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        # m_url = settings.MEDIA_URL         # Typically /media/
        # m_root = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        # if uri.startswith(m_url):
        #     path = os.path.join(m_root, uri.replace(m_url, ""))
        if uri.startswith(s_url):
            path = os.path.join(s_root, uri.replace(s_url, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (s_url, m_url)
        )
    return path

def html_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return None
