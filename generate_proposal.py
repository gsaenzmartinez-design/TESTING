from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

# ── Márgenes (estilo B) ──────────────────────────────────────────────────────
for section in doc.sections:
    section.top_margin    = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin   = Cm(3.0)
    section.right_margin  = Cm(2.5)

# ── Helpers ──────────────────────────────────────────────────────────────────
FONT = 'Arial'
BODY_SIZE = 11

def para(text='', bold=False, italic=False, size=BODY_SIZE,
         sb=0, sa=6, align=WD_ALIGN_PARAGRAPH.LEFT, underline=False):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(sb)
    p.paragraph_format.space_after  = Pt(sa)
    if text:
        run = p.add_run(text)
        run.bold      = bold
        run.italic    = italic
        run.underline = underline
        run.font.size = Pt(size)
        run.font.name = FONT
    return p

def section_head(text):
    """Estilo cabecera de sección tipo B: negrita, mayúsculas, espacio antes."""
    return para(text, bold=True, sb=12, sa=4)

def sub_head(text):
    """Cabecera de sub-sección tipo B: negrita, espacio moderado."""
    return para(text, bold=True, sb=8, sa=4)

def body(text):
    return para(text, sb=0, sa=4)

def bullet(text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    run = p.add_run(text)
    run.font.size = Pt(BODY_SIZE)
    run.font.name = FONT
    return p

def blank(n=1):
    for _ in range(n):
        para()

# ════════════════════════════════════════════════════════════════════════════
# CABECERA DEL DESTINATARIO (formato B: texto plano, sin negrita)
# ════════════════════════════════════════════════════════════════════════════
para('Mr. Jakub Sobieski', sb=0, sa=2)
para('ALTO Advisory', sa=2)
para('Gdański Business Center, ul. Inflancka 4b | 00-189 Warszawa, Poland', sa=2)
para('jsobieski@altoadvisory.pl', sa=0)

blank()

para('Vigo, 25th May 2026', sa=0)

blank()

para('Dear Mr. Sobieski,', sa=6)

blank()

# ── Párrafo de apertura (contenido de A, prosa de B) ────────────────────────
body('Thank you for reaching out through our colleague María Zabala at ABBANTIA. '
     'We are pleased to submit this proposal in response to your request for VAT '
     'compliance services in Spain on behalf of your client, a Polish company '
     'intending to install its own IT equipment in a Spanish data centre under a '
     'colocation agreement.')

body('Based on the facts and information provided, we have prepared a comprehensive '
     'proposal covering all VAT obligations arising from this operation. We have also '
     'identified certain tax risk areas that we recommend addressing as part of the '
     'engagement.')

body('Our professional services include:')

blank()

# ════════════════════════════════════════════════════════════════════════════
# I.- FACTS AND TAX CONTEXT
# ════════════════════════════════════════════════════════════════════════════
section_head('I.- FACTS AND TAX CONTEXT.')

body('Your client, a Polish company, intends to locate one of its backup server rooms '
     'in a professional data centre in Spain under a colocation arrangement. The key '
     'features of the operation, as described, are the following:')

bullet('The client will rent physical space in a Spanish data centre (colocation '
       'services) and place its own servers, storage systems and network devices therein.')
bullet('Only backup data will be stored on the servers. No commercial or operational '
       'activity will be conducted in Spain.')
bullet('The equipment (servers, switches, etc.) will be purchased from Polish suppliers '
       'not registered for VAT/VAT-EU purposes in Spain.')
bullet('The equipment will be configured and tested in Poland before being physically '
       'transported to Spain at the client\'s own expense.')
bullet('The transport of the equipment from Poland to Spain will be treated as a transfer '
       'of own goods between Member States.')
bullet('Following delivery, the Polish suppliers will install, connect and integrate the '
       'equipment at the data centre in Spain.')

blank()

body('From a Spanish VAT perspective, the transfer of own goods from Poland to Spain '
     'constitutes an intra-Community acquisition of goods (ICA) in Spain, which triggers '
     'a registration obligation and the obligation to declare and self-assess Spanish VAT '
     'on the acquisition value of the transferred assets. The installation services '
     'provided by the Polish suppliers in Spain also require careful analysis under the '
     'supply-with-installation rules.')

# ════════════════════════════════════════════════════════════════════════════
# II.- SCOPE OF SERVICES
# ════════════════════════════════════════════════════════════════════════════
section_head('II.- SCOPE OF SERVICES.')

# A
sub_head('A.- VAT REGISTRATION IN SPAIN (CENSUS REGISTRATION / ROI).')

body('This service covers the full registration of the client for VAT purposes in Spain '
     'with the Spanish Tax Agency (Agencia Estatal de Administración Tributaria – AEAT). '
     'Specifically, ABBANTIA will:')

bullet('Prepare and file the census registration form (Modelo 036) to obtain a Spanish '
       'tax identification number (NIF) as a non-established entity.')
bullet('Register the client in the Register of Intra-Community Operators (Registro de '
       'Operadores Intracomunitarios – ROI) to enable the filing of intra-Community '
       'transaction declarations.')
bullet('Prepare a full list of documents required by the AEAT and provide detailed '
       'instructions to the client for each action required on their part.')
bullet('Liaise directly with the AEAT throughout the registration process until a valid '
       'Spanish VAT/NIF number has been obtained.')
bullet('Advise on the power of attorney (apoderamiento) required to represent the client '
       'before the AEAT.')

# B
sub_head('B.- VAT FILING AND SUBMISSION.')

body('ABBANTIA will prepare and submit all required VAT and associated declarations '
     'arising from the operation. These include, to the extent applicable:')

bullet('Modelo 309 – Non-periodic VAT return for non-established entities, to declare '
       'and self-assess the intra-Community acquisition of goods (transfer of own goods '
       'from Poland to Spain).')
bullet('Modelo 349 – Recapitulative statement of intra-Community transactions, to report '
       'the ICA and any other intra-Community operations.')
bullet('Intrastat (DUA/Estadística) – Statistical declaration of goods movements, if the '
       'value of the transferred equipment exceeds the applicable threshold (currently '
       'EUR 400,000 for arrivals/introductions).')
bullet('Any other form or supplementary declaration required by the AEAT in connection '
       'with the above operations.')

blank()

body('ABBANTIA will calculate the applicable VAT base and the tax due, prepare all '
     'returns and submit them within the legal deadlines, providing the client with full '
     'documentation of each submission.')

# C
sub_head('C.- VAT DEDUCTION ANALYSIS.')

body('The client may be entitled to deduct the Spanish VAT self-assessed on the '
     'intra-Community acquisition, subject to meeting the applicable requirements under '
     'Spanish VAT law (Ley 37/1992). ABBANTIA will:')

bullet('Analyse whether the conditions for deduction of input VAT are met in the specific '
       'circumstances of the client.')
bullet('Advise on the procedure and documentation required to exercise the right of '
       'deduction or, where applicable, to request a VAT refund from the AEAT (Modelo 360/361).')

# D
sub_head('D.- DEREGISTRATION FROM THE SPANISH VAT REGISTER.')

body('Once all equipment has been delivered and installed, all Spanish VAT obligations '
     'have been filed and settled, and no further intra-Community transactions are '
     'anticipated, ABBANTIA will manage the full deregistration process, including:')

bullet('Preparation and submission of the deregistration form (Modelo 036 – baja en el '
       'censo) before the AEAT.')
bullet('Follow-up with the AEAT until the deregistration is formally confirmed.')
bullet('Advising on the conditions and timing required for deregistration (including '
       'clearance of pending tax obligations).')

blank()

body('Note: the deregistration process before the AEAT can take several months. We '
     'recommend allowing sufficient time and not initiating it before all pending '
     'obligations have been fully settled.')

# E
sub_head('E.- REPRESENTATION BEFORE THE SPANISH TAX AUTHORITIES.')

body('Throughout the engagement, ABBANTIA will act as the client\'s representative before '
     'the AEAT in connection with all of the above services. This includes responding to '
     'enquiries, information requests and any formal communications from the tax authorities.')

# F
sub_head('F.- VAT COMPLIANCE ADVISORY.')

body('Any specific VAT compliance questions arising outside the scope of the above '
     'services will be handled individually by one of our VAT specialists and billed at '
     'the agreed hourly rate.')

# Exclusions
blank()
sub_head('MATTERS AND SERVICES EXCLUDED FROM THIS PROPOSAL.')

body('Advice or compliance in respect of taxes other than VAT (e.g. corporate income '
     'tax, transfer pricing, customs duties, etc.).')
body('Legal advice or representation in judicial or administrative proceedings '
     '(Tribunales Económico-Administrativos, ordinary courts).')
body('Attendance at or assistance with tax audits or inspections initiated by the AEAT, '
     'unless separately agreed.')
body('Intrastat declarations when the number of movements exceeds 50 transactions per '
     'reporting period.')
body('Services relating to any permanent establishment analysis beyond the scope '
     'described in Section III below.')

blank()
body('Any of the above services may be discussed and quoted separately upon request.')

# ════════════════════════════════════════════════════════════════════════════
# III.- IMPORTANT TAX RISK: PERMANENT ESTABLISHMENT FOR VAT PURPOSES
# ════════════════════════════════════════════════════════════════════════════
section_head('III.- IMPORTANT TAX RISK: PERMANENT ESTABLISHMENT FOR VAT PURPOSES.')

body('We draw your attention to a material tax risk that must be considered in the '
     'context of this operation. The presence of the client\'s own servers and IT '
     'equipment in a Spanish data centre, under a long-term colocation agreement, may '
     'be construed by the AEAT as constituting a fixed establishment (establecimiento '
     'permanente) for VAT purposes under Article 69.Three of the Spanish VAT Act and '
     'the EU VAT Directive (2006/112/EC).')

body('Recent case law of the Court of Justice of the European Union (in particular '
     'cases C-547/18, C-333/20 and C-155/12) has clarified the conditions under which '
     'a technical infrastructure in another Member State may constitute a fixed '
     'establishment for VAT purposes. The key criteria are the existence of a sufficient '
     'degree of permanence and an adequate technical and human structure capable of '
     'receiving or providing taxable services.')

body('While the client\'s stated intention is that no commercial activity will be carried '
     'out in Spain, the fact that the servers will be present on a permanent basis and '
     'that the colocation services are being received at that location creates a potential '
     'risk that the AEAT could take a different view. If a fixed establishment were found '
     'to exist, additional VAT obligations could arise, including the obligation to '
     'register for VAT in Spain on a regular basis and to account for VAT on services '
     'received through that establishment.')

body('We recommend that a specific fixed establishment risk analysis be carried out '
     'prior to or simultaneously with the registration process. This analysis would '
     'involve a review of the colocation agreement and the technical parameters of the '
     'operation, and would result in a written legal opinion. This service is quoted '
     'separately below.')

# ════════════════════════════════════════════════════════════════════════════
# IV.- PROFESSIONAL FEES
# ════════════════════════════════════════════════════════════════════════════
section_head('IV.- PROFESSIONAL FEES.')

body('All fees are quoted in euros and are exclusive of Spanish VAT (IVA). Fees for '
     'services rendered to a non-established entity are generally zero-rated for Spanish '
     'VAT purposes under the reverse charge mechanism.')

blank()

sub_head('A.- VAT REGISTRATION IN SPAIN (NIF + ROI).')
body('Our fee for full VAT registration in Spain (NIF + ROI) is EUR 1,400 (VAT excluded), '
     'one-time fee.')

sub_head('B.- VAT FILING AND SUBMISSION.')
body('Modelo 309 (non-periodic VAT return): EUR 350 per return.')
body('Modelo 349 (recapitulative statement of intra-Community transactions): EUR 250 per return.')
body('Intrastat declaration (if applicable): EUR 300 per declaration.')

sub_head('C.- VAT DEDUCTION / REFUND ANALYSIS.')
body('Our fee for the VAT deduction/refund analysis is EUR 500 (VAT excluded), one-time fee.')

sub_head('D.- DEREGISTRATION (MODELO 036 – BAJA).')
body('Our fee for the deregistration process is EUR 600 (VAT excluded), one-time fee.')

sub_head('E.- REPRESENTATION / AEAT COMMUNICATIONS.')
body('Included in the above fees.')

sub_head('F.- COMPLIANCE ADVISORY.')
body('Both parties agree to fix an hourly rate of EUR 170 per hour, with a minimum of '
     '0.25 hour per action.')

sub_head('OPTIONAL: FIXED ESTABLISHMENT RISK OPINION.')
body('EUR 800 – 1,200 (to be confirmed depending on scope).')

blank()

body('An advance payment of EUR 1,000 is required prior to commencement of the '
     'registration process. This amount will be deducted from the registration fee invoice.')

# ════════════════════════════════════════════════════════════════════════════
# V.- INVOICING AND PAYMENT CONDITIONS
# ════════════════════════════════════════════════════════════════════════════
section_head('V.- INVOICING AND PAYMENT CONDITIONS.')

body('We shall invoice the proposed fees in the following manner:')

blank()

body('a).- Registration fee (EUR 1,400): EUR 1,000 upon acceptance of this proposal; '
     'EUR 400 upon completion of the registration and issuance of the Spanish NIF.')

body('b).- VAT returns (Modelo 309, 349, Intrastat): invoiced individually upon '
     'submission of each return.')

body('c).- Deregistration fee (EUR 600): 50% upon commencement; 50% upon formal '
     'confirmation of deregistration by the AEAT.')

body('d).- Compliance advisory: invoiced monthly based on time spent.')

body('e).- Fixed establishment opinion (if instructed): 50% upon instruction; 50% upon '
     'delivery of the written opinion.')

blank()

body('Fees are payable within 14 days of invoice date. Any disbursements (notary fees, '
     'official translations, public registry fees, etc.) incurred on the client\'s behalf '
     'will be invoiced separately at cost.')

# ════════════════════════════════════════════════════════════════════════════
# VI.- INDICATIVE TIMELINE
# ════════════════════════════════════════════════════════════════════════════
section_head('VI.- INDICATIVE TIMELINE.')

body('Engagement & KYC / document collection: 1–2 weeks from instruction.')
body('Submission of VAT registration (NIF + ROI): 2–3 weeks from instruction.')
body('AEAT processing of registration: 4–8 weeks (AEAT timescales, may vary).')
body('Filing of Modelo 309 / 349 / Intrastat: within legal deadlines after NIF obtained.')
body('Deregistration process: 3–6 months after final tax settlement.')

# ════════════════════════════════════════════════════════════════════════════
# VII.- INFORMATION AND DOCUMENTS REQUIRED FROM THE CLIENT
# ════════════════════════════════════════════════════════════════════════════
section_head('VII.- INFORMATION AND DOCUMENTS REQUIRED FROM THE CLIENT.')

body('To commence this engagement, we require the following information and documentation:')

blank()

sub_head('CORPORATE AND TAX IDENTIFICATION.')
bullet('Copy of the company\'s deed of incorporation and current articles of association '
       '(or equivalent).')
bullet('Certificate of tax residency in Poland (issued by the Polish tax authorities).')
bullet('Valid VAT/VAT-EU registration certificate in Poland.')
bullet('Copy of the passport or national ID of the legal representative signing the power '
       'of attorney.')
bullet('Power of attorney in favour of ABBANTIA, duly executed (we will provide the template).')

sub_head('INFORMATION RELATING TO THE SPANISH OPERATION.')
bullet('Colocation agreement with the Spanish data centre (for analysis of fixed '
       'establishment risk and to confirm the nature and duration of the arrangement).')
bullet('Total estimated value of the equipment to be transferred from Poland to Spain '
       '(for VAT base and Intrastat threshold assessment).')
bullet('Planned date of equipment transfer and installation.')
bullet('List of Polish suppliers who will install the equipment in Spain, indicating '
       'whether any of them hold a Spanish NIF-IVA or NIF.')
bullet('Description of the equipment to be transferred (type, quantity, estimated value '
       'per item).')
bullet('Confirmation of whether the client has an existing VAT registration in any other '
       'EU Member State.')
bullet('Confirmation of whether any services will be provided from or through the Spanish '
       'servers to third parties (even indirectly), now or in the future.')

# ════════════════════════════════════════════════════════════════════════════
# VIII.- OUR EXPERIENCE
# ════════════════════════════════════════════════════════════════════════════
section_head('VIII.- OUR EXPERIENCE.')

body('ABBANTIA has extensive experience advising foreign entities on VAT compliance '
     'matters in Spain, including registrations, periodic compliance, intra-Community '
     'transactions and deregistration. Our team includes qualified tax advisers (asesores '
     'fiscales) and lawyers (abogados) with specific expertise in cross-border VAT, EU '
     'VAT Directive analysis and litigation before Spanish tax authorities.')

body('We regularly advise clients from across the EU and beyond on VAT obligations '
     'arising from intra-Community transfers of goods, e-commerce, fixed establishment '
     'analysis, and related compliance matters. Our Vigo office, in coordination with '
     'our teams in Bilbao, Madrid and Seville, is well positioned to handle matters '
     'before the AEAT efficiently.')

# ════════════════════════════════════════════════════════════════════════════
# IX.- GENERAL CONDITIONS
# ════════════════════════════════════════════════════════════════════════════
section_head('IX.- GENERAL CONDITIONS.')

body('According to general price levels in Spain, fees will be reviewed annually in '
     'January in line with the CPI (Consumer Price Index) applicable in Spain.')

body('Any significant change in the scope of services (e.g. additional declarations, '
     'extended engagement period, AEAT inspections) will be agreed in writing before '
     'additional work is commenced.')

body('All disbursements and out-of-pocket costs (notary fees, translations, filing fees) '
     'are not included in the above fees and will be invoiced separately at cost.')

body('This proposal is valid for 30 days from the date hereof.')

body('The engagement will be governed by Spanish law. Any disputes shall be subject to '
     'the jurisdiction of the courts of Vigo.')

# ════════════════════════════════════════════════════════════════════════════
# X.- DATA PROTECTION
# ════════════════════════════════════════════════════════════════════════════
section_head('X.- DATA PROTECTION.')

body('PRIVACY POLICY – INFORMATIVE CLAUSE – GENERAL DATA PROTECTION REGULATION.')

blank()

body('In compliance with EU Regulation 2016/679 (GDPR) and Spanish data protection '
     'legislation, we inform you that personal data provided in connection with this '
     'engagement will be processed by ABBANTIA ABOGADOS BILBAO S.L. (CIF B95492799), '
     'solely for the purpose of managing the professional relationship and fulfilling '
     'our legal and fiscal obligations. Data will not be transferred to third parties '
     'except where required by law or necessary for the provision of the services. '
     'Data subjects may exercise their rights of access, rectification, erasure, '
     'restriction, portability and objection by contacting datos@abbantia.com.')

# ════════════════════════════════════════════════════════════════════════════
# CIERRE (estilo B)
# ════════════════════════════════════════════════════════════════════════════
blank()

body('Once again we would like to thank you for reaching out to our firm, and we look '
     'forward to the opportunity to assist you and your client with efficiency and '
     'competence.')

blank()

body('We kindly request that you return this letter of engagement duly signed as proof '
     'of acceptance.')

blank()

body('In proof of conformity as above, the client and the adviser sign in duplicate copy '
     'and to a single effect. In Vigo, 25th May 2026.')

blank()

para('Yours sincerely,', sb=12, sa=2)

blank()

para('Guillermo Sáenz', bold=True, sa=2)
para('Managing Partner – Tax & VAT', sa=2)
para('PS Tributación y Finanzas S.L. / VATONTIME', sa=2)
para('In association with ABBANTIA ABOGADOS', sa=12)

# Línea de firma del cliente
body('THE CLIENT.')

blank()

body('Signature: ______________________________      Date: _______________')
body('Name: __________________________________      Position: _____________')

blank(2)

# ── Footer estilo B ──────────────────────────────────────────────────────────
footer_para = para('BILBAO – MADRID – SEVILLA - VIGO',
                   bold=True, sb=12, sa=0,
                   align=WD_ALIGN_PARAGRAPH.CENTER)

# ── Guardar ──────────────────────────────────────────────────────────────────
output_path = '/home/user/TESTING/2026-05-25__ES__PROPUESTA__ALTO_Advisory__VAT_Compliance_Spain__v01__GS__formatted.docx'
doc.save(output_path)
print(f'Saved: {output_path}')
