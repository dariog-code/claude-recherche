#!/usr/bin/env python3
"""Strong company-domain classifier over harvested Ahrefs outgoing links.
Goal: per Hochschule, list GENUINE external company domains it links to (dofollow)."""
import json, os, re, csv

RAW="_tools/ahrefs/raw"

# --- exclusion blocklists (substring match on domain) ---
PLATFORMS_TOOLS = """facebook. instagram. youtube. youtu.be linkedin. twitter. x.com xing. tiktok.
vimeo. soundcloud. spotify. pinterest. flickr. snapchat. threads.net whatsapp. wa.me t.me
telegram. mastodon. bsky. tumblr. wordpress. blogspot. medium.com myspace. behance. cargo.
dribbble. format.com myportfolio. wix. jimdo. squarespace. weebly. webnode. google. gstatic.
googleapis. googletagmanager. youtube-nocookie. microsoft microsoftonline office.com office365
live.com sharepoint. outlook. apple. adobe. mozilla. browsehappy. github. gitlab. gitea. bitbucket.
sourceforge. zoom.us zoom-x. teams. webex. gotomeeting. slack. discord. miro.com mural.co padlet.
mentimeter. slido. kahoot. sciebo. nextcloud. owncloud. dropbox. wetransfer. cloud.sap academiccloud.
matomo. cookiebot. usercentrics. consentmanager. piwik. hotjar. mailchimp mailchi.mp twingle.
betterplace. bildungsspender. paypal. sumup spreadshop spreadshirt myspreadshop teamshirts.
eventbrite. eventim. reservix. ticketmaster. etermin. terminland. doodle. calendly. sibforms.
typeform. surveymonkey. limesurvey. lamapoll. soscisurvey. jotform. formstack. heavenhr. personio.
jobteaser. joborama. stellenticket. stellenwerk. kununu. stepstone. indeed. jobware. monster.
hochschuljobboerse. myunijobs. myuniboard. bewerbung2go. studycheck. studydrive. studis-online.
studieren.de hochschulkompass. studienwahl. fernstudiumcheck. uninow goo.gl bit.ly tinyurl.
flaticon. fontawesome. jquery. bootstrap. cloudflare. jsdelivr. unpkg. gravatar. zymphonies.
themeware. podigee. letscast. anchor.fm spreaker. omny.fm chatboardapp. enable-javascript.
edgewall. opensource.org creativecommons. gnu.org fsf.org""".split()

DEV_INFRA = """apache. eclipse. jboss. redmine. debian. ubuntu. centos. opensuse. linux. kernel.org
python.org php.net java.com java.net oracle.com mysql. postgresql. mongodb. mariadb. docker.
kubernetes. readthedocs. sphinx-doc. doxygen ctan. tug.org latex- overleaf. r-project. rstudio.
bioconductor. scala-lang. nodejs. npmjs. w3.org schema.org dbpedia. json-ld. xml. rdf. ietf.
rfc-editor. iso.org unicode.org iana. handle.net purl.org openurl. mediawiki. wikidata. wikipedia.
wikimedia. wikiversity. moodle. ilias. studip. instructure. canvas. blackboard. opal- vivoweb.
openproject. mantis. bugzilla. jira. confluence. forgejo. config.de smallrye. quarkus. springframework.
hibernate. log4j. maven. gradle. nginx. iisys.""".split()

PUBLISHERS_ACADEMIC = """springer. wiley. elsevier. sciencedirect. tandfonline. taylorfrancis. sagepub.
nature.com frontiersin. mdpi. plos. cell.com thelancet. bmj.com acm.org ieee. aip.org aps.org
acs.org rsc.org iop.org jstor. doi.org datacite. crossref. orcid. researchgate. academia.edu
arxiv. biorxiv. ssrn. ncbi. pubmed. nih.gov ebi.ac.uk uniprot. rcsb. ensembl. genome. semanticscholar.
dimensions.ai scopus. webofscience. clarivate. publons. mendeley. zotero. zenodo. figshare. osf.io
de.gruyter degruyter. nomos- peterlang. hanser- thieme. beck-shop. boorberg. utb.de vandenhoeck.
mohr.de transcript-verlag. waxmann. juventa. kohlhammer. duncker-humblot. econstor. repec. ideas.repec.
ssoar. base-search. re3data. opendoar. sherpa. lyrasis. duraspace. dspace. eprints. oclc. worldcat.
k10plus. swisscovery. primo. exlibrisgroup. ebsco ebscohost. proquest. gale. emerald. inderscience.
hypotheses. openedition. ojs. dnb.de d-nb.info nbn-resolving. urn: zdb- gbv.de kobv.de bsz-bw. ibs-bw.
hebis. hbz-nrw. digibib. zvdd. dfg-viewer. iiif. rightsstatements. europeana. deutsche-digitale-bibliothek.
digitale-sammlungen. manuscripta- handschriften. propylaeum. perspectivia. recensio. h-net. clio-online.
vifa kxp.""".split()

GOV_ORG = """.gov .europa.eu europa.eu bund.de bmbf. bmwk. bmbwf bmas. bmel. auswaertiges-amt.
daad. dfg.de daad.de hrk.de stifterverband. wissenschaftsrat. leopoldina. helmholtz. fraunhofer.
max-planck mpg.de leibniz- dlr.de dwih akkreditierung fibaa. aqas. acquin. zeva. ahpgs. evalag.
aacsb. amba efmd. equis. magna-charta. eua.eu yerun. uas7. che.de ranking. bafög. bafoeg.
stipendium stipendien aufstiegsstipendium weiterbildungsstipendium arbeiterkind. esf. foerderdatenbank
exist.de arbeitsagentur. bundesagentur. kmk.org schulministerium. mkw.nrw mwk. mwsk. stmwk. stk.
bayern.de nrw.de sachsen.de sachsen-anhalt. rlp.de rlp.net berlin.de hamburg.de thueringen.de
baden-wuerttemberg. niedersachsen. brandenburg. hessen.de saarland. schleswig-holstein.
mecklenburg-vorpommern. regierung-mv. bremen.de stadt- .kommune .landkreis charta-der-vielfalt.
total-e-quality. familie-in-der-hochschule. berufundfamilie. erfolgsfaktor-familie. gemeinsam-gegen-sexismus.
echte-vielfalt. fairtrade- un.org unesco. who.int oecd. worldbank. unicef. greenpeace. nabu. bund-
amnesty. drk.de diakonie. caritas. paritaet. awo. malteser. johanniter.""".split()

EDU_RE = re.compile(r"(^|\.)(uni-|fh-|hs-|haw-|th-|tu-|hfm|hfmt|hfbk|hfg-|hmt|hmtm|adbk|kunstakademie|"
    r"musikhochschule|hochschule|universit|\.edu$|\.edu\.|\.ac\.|dhbw|fernuni|leuphana|charite|"
    r"mh-freiburg|uniklinik|klinikum|uni-klinik|uniklinika|studierendenwerk|studentenwerk|stw-|"
    r"\.asta|asta-|stura|hochschulkooperation|hochschulallianz)")

FOUND_VEREIN = re.compile(r"(foerder|förder|freunde|stiftung|-stiftung\.|-ev\.de$|-e-v\.|alumni)")

MEDIA = """zeit.de taz.de spiegel. faz.net faz.de sueddeutsche. tagesspiegel. welt.de handelsblat
morgenpost. nmz.de deutschlandfunk. kulturradio. swr. swr3. dasding. ard.de zdf. dw.com rtl. ntv.
heise. golem. t3n. netzpolitik. spektrum. wissenschaft.de nano""".split()

def excluded(d):
    d=d.lower()
    for grp in (PLATFORMS_TOOLS, DEV_INFRA, PUBLISHERS_ACADEMIC, GOV_ORG, MEDIA):
        for s in grp:
            if s and s in d: return True
    return False

def is_company(dom, target):
    d=dom.lower()
    if d==target or d.endswith("."+target): return False
    stem=target.split(".")[0].split("-")[0]
    if len(stem)>=5 and d.split(".")[0].startswith(stem): return False
    if EDU_RE.search(d): return False
    if FOUND_VEREIN.search(d): return False
    if excluded(d): return False
    return True

# meta
def regdom(s):
    m=re.search(r'([a-z0-9-]+(?:\.[a-z0-9-]+)+)',(s or '').lower())
    if not m: return ""
    p=m.group(1).split('/')[0].split('.'); return ".".join(p[-2:]) if len(p)>=2 else ""
r=list(csv.reader(open('recherche_master_foerdervereine.csv')))
meta={}
for x in r[1:]:
    d=regdom(x[7]) or regdom(x[8])
    if d and d not in meta: meta[d]=(x[0],x[1],x[2])

out={}
for fn in os.listdir(RAW):
    if not fn.endswith(".json"): continue
    rec=json.load(open(f"{RAW}/{fn}")); t=rec["domain"]
    comp=[x for x in rec.get("linked",[]) if is_company(x["domain"],t)]
    comp.sort(key=lambda x:-x["dofollow_links"])
    out[t]={"dr":rec.get("dr"),"n":len(comp),"top":comp[:15]}
json.dump(out, open("_tools/ahrefs/company_links.json","w"), ensure_ascii=False)

# validation print
print("VALIDATION (known cases):")
for d in ["popakademie.de","hs-doepfer.de","iu.de","fom.de","kh-berlin.de","uni-stuttgart.de","fh-mittelstand.de","srh-university.de"]:
    if d in out:
        o=out[d]; print(f"\n{d} (DR{o['dr']}, {o['n']} Firmen): "+", ".join(x['domain'] for x in o['top'][:10]))
