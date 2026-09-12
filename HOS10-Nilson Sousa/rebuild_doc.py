# -*- coding: utf-8 -*-
import re, sys
from docx import Document
from docx.shared import Pt, RGBColor, Inches, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = __import__('os').path.dirname(__import__('os').path.abspath(__file__))
raw = open(HERE + '/mongodb-results.txt', encoding='utf-8').read()
parts = re.split(r'^===== (.+?) =====$', raw, flags=re.M)
R = {}
for i in range(1, len(parts), 2):
    R[parts[i]] = parts[i + 1].strip()

def res(key):
    for k in R:
        if k.startswith(key):
            return R[k]
    raise SystemExit('missing result: ' + key)

FONT = 'Calibri'
MONO = 'Consolas'

doc = Document()

# US Letter, 1 inch margins
sec = doc.sections[0]
sec.page_width = Inches(8.5)
sec.page_height = Inches(11)
for attr in ('top_margin', 'bottom_margin', 'left_margin', 'right_margin'):
    setattr(sec, attr, Inches(1))

# Base style
st = doc.styles['Normal']
st.font.name = FONT
st.font.size = Pt(11)
st.element.rPr.rFonts.set(qn('w:eastAsia'), FONT)
st.paragraph_format.space_after = Pt(6)
st.paragraph_format.line_spacing = 1.15

for name, size, color in (('Heading 1', 15, '1F3864'), ('Heading 2', 12.5, '2E5496')):
    s = doc.styles[name]
    s.font.name = FONT
    s.font.size = Pt(size)
    s.font.bold = True
    s.font.color.rgb = RGBColor.from_string(color)
    s.paragraph_format.space_before = Pt(14)
    s.paragraph_format.space_after = Pt(7)

def shade(par_or_cell, fill):
    el = par_or_cell._p.get_or_add_pPr() if hasattr(par_or_cell, '_p') else par_or_cell._tc.get_or_add_tcPr()
    sh = OxmlElement('w:shd')
    sh.set(qn('w:val'), 'clear')
    sh.set(qn('w:color'), 'auto')
    sh.set(qn('w:fill'), fill)
    el.append(sh)

def borders(par, color, style='dashed', size='6'):
    pPr = par._p.get_or_add_pPr()
    bd = OxmlElement('w:pBdr')
    for side in ('top', 'left', 'bottom', 'right'):
        e = OxmlElement('w:' + side)
        e.set(qn('w:val'), style)
        e.set(qn('w:sz'), size)
        e.set(qn('w:space'), '4')
        e.set(qn('w:color'), color)
        bd.append(e)
    pPr.append(bd)

def P(text='', size=11, bold=False, italic=False, color=None, align=None, after=6, before=0,
      space_line=None, indent=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.space_before = Pt(before)
    if align is not None:
        p.alignment = align
    if indent:
        p.paragraph_format.left_indent = Inches(indent)
    r = p.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(size)
    r.bold = bold
    r.italic = italic
    if color:
        r.font.color.rgb = RGBColor.from_string(color)
    return p

def H(text, level):
    p = doc.add_heading(text, level=level)
    for r in p.runs:
        r.font.name = FONT
    return p

def bullet(text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(11)
    return p

def code(text, label=None):
    if label:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(label)
        r.font.name = FONT
        r.font.size = Pt(9.5)
        r.bold = True
        r.font.color.rgb = RGBColor.from_string('555555')
    lines = str(text).split('\n')
    for i, ln in enumerate(lines):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6 if i == len(lines) - 1 else 0)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.left_indent = Inches(0.15)
        p.paragraph_format.right_indent = Inches(0.15)
        p.paragraph_format.line_spacing = 1.0
        shade(p, 'F2F2F2')
        r = p.add_run(ln if ln.strip() else ' ')
        r.font.name = MONO
        r.font.size = Pt(9)
        r._element.rPr.rFonts.set(qn('w:eastAsia'), MONO)

import os, glob

SHOT_DIR = os.path.join(HERE, 'screenshots')

SHOT_KEYS = [
    's01-codespace',
    's02-atlas-signup',
    's03-atlas-welcome',
    's04-create-deployment',
    's05-database-user',
    's06-ip-access-list',
    's07-vscode-extension',
    's08-connect-string',
    's09-paste-string',
    's10-connected',
    's11-playground-saved',
] + ['step%02d' % i for i in range(1, 24)] + [
    's12-source-control',
    's13-pushed-commit',
]
_shot_i = [0]
FOUND = []
MISSING = []

def _find_image(key):
    for ext in ('png', 'PNG', 'jpg', 'JPG', 'jpeg', 'JPEG'):
        hits = sorted(glob.glob(os.path.join(SHOT_DIR, key + '.' + ext)))
        if hits:
            return hits[0]
    return None

def shot(caption):
    key = SHOT_KEYS[_shot_i[0]] if _shot_i[0] < len(SHOT_KEYS) else 'extra%d' % _shot_i[0]
    _shot_i[0] += 1
    path = _find_image(key)
    if path:
        FOUND.append(key)
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(7)
        p.paragraph_format.space_after = Pt(3)
        run = p.add_run()
        pic = run.add_picture(path, width=Inches(6.4))
        if pic.height > Inches(7.5):
            ratio = Inches(7.5) / pic.height
            pic.height = int(pic.height * ratio)
            pic.width = int(pic.width * ratio)
        cap = doc.add_paragraph()
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap.paragraph_format.space_after = Pt(10)
        cr = cap.add_run(caption[0].upper() + caption[1:])
        cr.font.name = FONT
        cr.font.size = Pt(9)
        cr.italic = True
        cr.font.color.rgb = RGBColor.from_string('595959')
        return
    MISSING.append((key, caption))
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(7)
    p.paragraph_format.space_after = Pt(9)
    shade(p, 'FFF6E5')
    borders(p, 'D9A441')
    r = p.add_run('SCREENSHOT [' + key + ']: ' + caption)
    r.font.name = FONT
    r.font.size = Pt(10)
    r.italic = True
    r.font.color.rgb = RGBColor.from_string('8A5A00')

def table(widths_in, rows):
    t = doc.add_table(rows=0, cols=len(widths_in))
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for ri, row in enumerate(rows):
        cells = t.add_row().cells
        for ci, txt in enumerate(row):
            c = cells[ci]
            c.width = Inches(widths_in[ci])
            c.text = ''
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.1
            r = p.add_run(txt)
            r.font.name = FONT
            r.font.size = Pt(10)
            if ri == 0:
                r.bold = True
                shade(c, 'D9E2F3')
    # lock column widths on every cell
    for row in t.rows:
        for ci, c in enumerate(row.cells):
            c.width = Inches(widths_in[ci])
    P('', after=8)
    return t

def page_break():
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

steps = [
 (1, 'List the databases on the server',
  "show dbs\n\n// playground equivalent\ndb.getMongo().getDBs();",
  'Lists every database the connected MongoDB server instance is holding. On a bare cluster only the internal databases admin, config and local appear, because a database is not really created until something is written into it. This cluster was deployed with the Preload sample dataset option enabled, so the sample_ databases that Atlas loads appear in the list as well.',
  'Step 1 show dbs', None, None),
 (2, 'Switch to the practice database',
  "use('CS628Practice');",
  'Switches the active database to CS628Practice. If that database does not exist yet, MongoDB creates it lazily on the first write rather than immediately.',
  None, None, 'The playground reports the switch in its output pane. Nothing is written to disk yet.'),
 (3, 'Confirm the current database',
  "db\n\n// playground equivalent\ndb.getName();",
  'Displays the name of the database currently selected, which confirms that the previous step took effect.',
  'Step 3 db', None, None),
 (4, 'Create the users collection',
  "db.createCollection('users');",
  'Creates a collection named users inside CS628Practice. A collection is the MongoDB counterpart of a table in a relational database, except that the documents inside it are not forced to share one schema.',
  'Step 4 createCollection', None, None),
 (5, 'Insert several user profiles',
  "db.users.insertMany([\n  { name: 'user1', age: 25, email: 'user1@cityuniversity.edu' },\n  { name: 'user2', age: 32, email: 'user2@cityuniversity.edu' },\n  { name: 'user3', age: 28, email: 'user3@cityuniversity.edu' },\n  { name: 'user4', age: 41, email: 'user4@cityuniversity.edu' },\n  { name: 'CityUser5', age: 22, email: 'cityuser5@cityuniversity.edu' }\n]);",
  'Inserts five documents in one call. Each document carries the fields name, age and email. MongoDB assigns every document a unique _id of type ObjectId automatically, and those values are returned in insertedIds.',
  'Step 5 insertMany', None, None),
 (6, 'Read every document in the collection',
  "db.users.find();",
  'Retrieves all documents in the users collection. Calling find with no filter is the equivalent of SELECT * FROM users in SQL.',
  'Step 6 find all', None, None),
 (7, 'Filter with a comparison operator',
  "db.users.find({ age: { $lt: 30 } });",
  'Returns only the users whose age is strictly below 30. $lt is one of a family of comparison operators, listed in the table at the end of this section.',
  'Step 7 age lt 30', None, None),
 (8, 'Update a single document',
  "db.users.updateOne({ name: 'user1' }, { $set: { age: 31 } });",
  'Finds the first document whose name is user1 and sets its age field to 31. The response reports matchedCount and modifiedCount, so the effect of the write can be confirmed.',
  'Step 8 updateOne', None, None),
 (9, 'Verify the update',
  "db.users.find({ name: 'user1' });",
  'Reads user1 back to confirm that the age really did change from 25 to 31.',
  'Step 9 verify update', None, None),
 (10, 'Delete a single document',
  "db.users.deleteOne({ name: 'user2' });",
  'Removes the first document whose name is user2. The response reports deletedCount.',
  'Step 10 deleteOne', None, None),
 (11, 'Verify the delete',
  "db.users.find();",
  'Reads the collection again. Four documents remain and user2 is gone.',
  'Step 11 verify delete', None, None),
 (12, 'Aggregate the average age',
  "db.users.aggregate([\n  { $group: { _id: null, averageAge: { $avg: '$age' } } }\n]);",
  'Runs an aggregation pipeline with a single $group stage. Using _id: null collapses every document into one bucket, so $avg produces one average across the whole collection. The remaining ages are 31, 28, 41 and 22, which average to 30.5.',
  'Step 12 avg age', None, None),
 (13, 'Index the email field',
  "db.users.createIndex({ email: 1 });",
  'Builds an ascending index on email, where 1 means ascending and -1 would mean descending. An index lets MongoDB seek straight to matching documents instead of scanning the whole collection, which speeds up reads at the cost of a little extra work on every write. The command returns the generated index name.',
  'Step 13 createIndex email', None, None),
 (14, 'Create a text index and run a text search',
  "db.users.createIndex({ name: 'text', email: 'text' });\n\ndb.users.find({ $text: { $search: 'user1' } });",
  'A text index covers both name and email, so one $text search can look across both fields at once. A collection may hold only one text index, which is why the two fields are declared together. The search for user1 matches a single document.',
  'Step 14a text index', 'Step 14b text search user1', None),
 (15, 'Sort by age, highest first',
  "db.users.find().sort({ age: -1 });",
  'Returns every user ordered by age in descending order, since -1 means descending.',
  'Step 15 sort age desc', None, None),
 (16, 'Paginate with limit and skip',
  "db.users.find().limit(2).skip(1);",
  'Combining skip and limit is the usual way to build pagination, where skip is the offset and limit is the page size. This step is worth reading carefully, because the two ways of running it do not agree. Run in mongosh, the server applies the skip before the limit and two documents come back, user3 and user4. Run as a selection inside the VS Code playground against the Atlas cluster, a single document came back, user3, which is what the screenshot below shows. The lesson is that chaining limit and skip leaves the order of application ambiguous, so a query that needs a guaranteed order should state it explicitly rather than relying on the chain.',
  'Step 16 playground', None, None),
 (17, 'Group and count users by age',
  "db.users.aggregate([\n  { $group: { _id: '$age', count: { $sum: 1 } } },\n  { $sort: { _id: 1 } }\n]);",
  'Groups the documents by their age value and counts how many fall into each group with $sum: 1. A second $sort stage puts the resulting groups in ascending order of age.',
  'Step 17 group count by age', None, None),
 (18, 'Find the oldest and the youngest user',
  "db.users.aggregate([\n  { $group: { _id: null, oldest: { $max: '$age' }, youngest: { $min: '$age' } } }\n]);",
  'One $group stage over the whole collection computes both extremes at once using $max and $min, and returns them in a single result document.',
  'Step 18 max min age', None, None),
 (19, 'Store geospatial data and index it',
  "db.places.insertMany([\n  { name: 'CityU Seattle', location: { type: 'Point', coordinates: [-122.2015, 47.6101] } },\n  { name: 'Pike Place Market', location: { type: 'Point', coordinates: [-122.3421, 47.6097] } },\n  { name: 'Space Needle', location: { type: 'Point', coordinates: [-122.3493, 47.6205] } },\n  { name: 'Portland OR', location: { type: 'Point', coordinates: [-122.6765, 45.5152] } }\n]);\n\ndb.places.createIndex({ location: '2dsphere' });",
  'Locations are stored as GeoJSON Point objects. The coordinates array is in longitude, latitude order, which is the reverse of the order most mapping websites display. A 2dsphere index models the Earth as a sphere and is required before any geospatial query will run.',
  'Step 19b 2dsphere index', None, None),
 (20, 'Find places within a radius',
  "db.places.find({\n  location: {\n    $geoWithin: {\n      $centerSphere: [[-122.3321, 47.6062], 20 / 6378.1]\n    }\n  }\n});\n\ndb.places.find({\n  location: {\n    $near: {\n      $geometry: { type: 'Point', coordinates: [-122.3321, 47.6062] },\n      $maxDistance: 20000\n    }\n  }\n});",
  'Both queries search a 20 kilometre circle centred on downtown Seattle. $centerSphere takes its radius in radians, so the distance in kilometres is divided by the radius of the Earth, 6378.1 kilometres. $near takes metres instead and returns the same three places sorted from nearest to farthest. Portland is roughly 230 kilometres away and is correctly excluded by both.',
  'Step 20a geoWithin centerSphere 20km', 'Step 20b near 20000m', None),
 (21, 'Advanced query with $or and regular expressions',
  "db.users.find({\n  $or: [\n    { name: { $regex: '^u', $options: 'i' } },\n    { name: { $regex: '^C', $options: 'i' } }\n  ]\n});",
  'The $or operator accepts an array of conditions and matches a document if any one of them holds. Each condition is a regular expression anchored with ^ so it matches only at the start of the name, and the i option makes the match case insensitive.',
  'Step 21 or regex', None, None),
 (22, 'Total age of all users',
  "db.users.aggregate([\n  { $group: { _id: null, totalAge: { $sum: '$age' } } }\n]);",
  'Grouping on null again collapses everything into one bucket, and $sum applied to the age field adds the values instead of counting documents. The four remaining ages, 31, 28, 41 and 22, add up to 122.',
  'Step 22 total age', None, None),
 (23, 'Clean up',
  "show collections\n// playground equivalent\ndb.getCollectionNames();\n\ndb.users.drop();\ndb.places.drop();\n\ndb.getCollectionNames();",
  'Lists the collections in the current database, drops both collections that were created during this exercise, then lists them once more to confirm the database is empty again. Each drop returns true when it succeeds.',
  'Step 23a show collections', 'Step 23d show collections', None),
]

C = WD_ALIGN_PARAGRAPH.CENTER

# Title block
P('CS11A: Technology & Computing Components I', size=13, bold=True, align=C, after=4)
P('HOS10A: MongoDB Atlas', size=20, bold=True, color='1F3864', align=C, after=12)
P('Nilson Sousa', size=12, align=C, after=2)
P('Module 10: NoSQL Database', size=11, color='595959', align=C, after=2)
P('School of Technology & Computing, City University of Seattle', size=10, color='595959', align=C, after=18)

H('Overview', 1)
P('This hands on exercise covers the difference between relational and non relational databases, sets up a free MongoDB Atlas cluster, connects that cluster to GitHub Codespaces through the MongoDB for VS Code extension, and then works through a full set of MongoDB commands in a playground file. Every command in Section 7 appears below with an explanation of what it does and the result it produces, followed by a space for the screenshot of that command running in the playground.')
P('The playground file used for Section 7 is included with this submission as dbserver/hos10.mongodb.js.')
page_break()

H('Section 1: Accessing GitHub Codespaces', 1)
P('The module was opened in GitHub Codespaces following the steps in the Student Resource Center. The codespace provides a browser based VS Code environment with the course repository already cloned, so no local installation is needed.')
shot('the running GitHub Codespace showing the course repository')

H('Section 2: Differentiating SQL and NoSQL', 1)
P('Both families store data and both are queried, but they make opposite trade offs. A relational database fixes the shape of the data in advance and guarantees strict consistency. A document database leaves the shape open and trades some of that strictness for flexibility and easier horizontal scaling.')
table([1.45, 2.5, 2.5], [
 ['Aspect', 'SQL (relational)', 'NoSQL (document)'],
 ['Schema', 'Fixed and declared in advance. Changing it needs a migration.', 'Flexible. Documents in one collection may carry different fields.'],
 ['Data model', 'Tables made of rows and columns.', 'Collections of JSON like documents, stored internally as BSON.'],
 ['Relationships', 'Foreign keys and joins across normalised tables.', 'Related data is often embedded in the same document instead.'],
 ['Transactions', 'ACID by default, which protects integrity across multiple tables.', 'Atomic at the document level. Multi document transactions exist but are used more sparingly.'],
 ['Scaling', 'Usually vertical, by giving one server more resources.', 'Designed for horizontal scaling across many nodes.'],
 ['Best suited for', 'Structured data with well defined relationships, such as finance and inventory.', 'Unstructured or semi structured data, and workloads whose shape keeps changing.'],
 ['Examples', 'MySQL, PostgreSQL, Microsoft SQL Server, SQLite, Oracle.', 'MongoDB, Amazon DynamoDB, Cassandra, Redis, Couchbase.'],
])

H('Section 3: Introducing MongoDB', 1)
P('MongoDB is a document oriented NoSQL database. It stores records as JSON like documents, which means a record can hold nested objects and arrays directly instead of being spread across several tables.')
H('Key concepts', 2)
table([1.6, 4.85], [
 ['Term', 'What it is'],
 ['Database', 'A container for collections, equivalent to a schema in SQL.'],
 ['Collection', 'A group of related documents, equivalent to a table.'],
 ['Document', 'One record, stored in BSON, which is a binary encoding of JSON.'],
 ['Field', 'A single data element inside a document, equivalent to a column.'],
 ['_id', 'The primary key. MongoDB adds one automatically as an ObjectId if none is supplied.'],
])
H('What MongoDB gives you', 2)
bullet('CRUD operations that mirror SQL in intent but use a JSON style syntax.')
bullet('A query language that supports filtering, projection, sorting and pagination.')
bullet('An aggregation framework that chains stages such as $group, $sort and $match to reshape data.')
bullet('Indexes, including text indexes for search and 2dsphere indexes for location data.')
bullet('Geospatial queries for anything that needs to answer what is near this point.')
P('Typical use cases include web applications, content management, product catalogues and real time analytics.', after=10)
page_break()

H('Section 4: Signing up for MongoDB Atlas', 1)
P('MongoDB Atlas is the managed cloud service for MongoDB. An account was created from the Try Free option on the MongoDB website, the email address was verified, and the short welcome questionnaire was completed.')
shot('the MongoDB Atlas sign up page')
shot('the verified account and the completed welcome questionnaire')

H('Section 5: Setting up the first MongoDB database', 1)
P('The free tier cluster was deployed with the settings the exercise calls for.')
table([1.9, 4.55], [
 ['Setting', 'Value used'],
 ['Cluster tier', 'M0 Free'],
 ['Cloud provider', 'AWS'],
 ['Region', 'Oregon (us-west-2)'],
 ['Cluster name', 'CS11A'],
 ['MongoDB version', '8.0.32'],
 ['Topology', 'Replica set, 3 nodes'],
])
shot('the CS11A cluster in the Atlas project overview, deployed on the Free tier')
P('The deployment was created with the Automate security setup option enabled, so Atlas ran its Auto Setup process and created both the database user and the network access entry in one pass rather than prompting for them separately.')
table([1.9, 4.55], [
 ['Security item', 'Value created by Auto Setup'],
 ['Database user', 'nilsonalvessousa_db_user'],
 ['Authentication', 'SCRAM'],
 ['Role', 'atlasAdmin on admin, over all resources'],
 ['IP access list', 'A single /32 entry for the current IP address, status Active'],
])
shot('the database user listed under Database Access')
P('The password for this user is generated once during Auto Setup and is not shown again. It is the value that replaces the placeholder in the connection string, so it has to be captured at creation time or the user has to be edited to set a new one.')
shot('the IP Access List showing the entry created by Auto Setup')
H('A note on the access list', 2)
P('Auto Setup adds only the IP address of the machine that created the cluster. That is the safer default and it is enough to connect from a laptop, but it is not enough to connect from GitHub Codespaces, because a codespace runs in the cloud and reaches Atlas from a completely different address that also changes between sessions. Connecting from a codespace therefore needs an entry of 0.0.0.0/0, which is the Allow Access from Anywhere option the exercise describes. That setting opens the cluster to every address on the internet, so it is acceptable for a throwaway practice cluster and should not be used for anything real.')

H('Section 6: Connecting Atlas to VS Code on GitHub Codespaces', 1)
P('In the codespace, the MongoDB for VS Code extension was installed from the Extensions panel. After installation a leaf icon appears in the activity bar.')
shot('the MongoDB for VS Code extension installed in the codespace')
P('Choosing Add Connection asks for a connection string. That string comes from Atlas, under Connect on the cluster overview, by picking the MongoDB for VS Code option.')
shot('the Connect dialog in Atlas showing the connection string for VS Code')
P('The string is pasted into the codespace prompt and the placeholder for the password is replaced with the real password, angle brackets included. If the password contains special characters they must be percent encoded first, otherwise the string is parsed incorrectly and the connection fails.')
shot('the connection string pasted into the codespace prompt')
shot('the successful connection to the Atlas cluster')
P('With the connection established, Create Playground opens a new file. The generated sample script was cleared to start from a blank file, which was then saved as hos10.mongodb.js under the HOS10/dbserver directory. A playground is recognised by the .mongodb.js extension and runs with the run triangle in the top right corner.')
shot('hos10.mongodb.js saved under HOS10/dbserver and visible in PLAYGROUNDS')
page_break()

H('Section 7: Learning MongoDB step by step', 1)
P('Each command below was run on its own in the playground so that its own result could be captured. A playground file is JavaScript, so the mongosh helpers show dbs and show collections are not valid inside it. Where the exercise asks for one of those, the JavaScript equivalent is used and the helper form is kept beside it as a comment.')
P('Every command below was executed twice. The text results were captured first against a local MongoDB 7 server while the playground was being written, and the screenshots were then taken while running the same file in GitHub Codespaces against the CS11A Atlas cluster on MongoDB 8.0.32. The two agree throughout except at step 16, which is noted there. ObjectId values differ between the two runs because they are generated per insert.')

for n, title, cmd, exp, k1, k2, note in steps:
    H('Step %d: %s' % (n, title), 2)
    code(cmd, 'Command')
    P(exp)
    if k1:
        code(res(k1), 'Result')
    if k2:
        code(res(k2), 'Result')
    if note:
        P(note, italic=True, color='595959')
    shot('Playground Result pane for step %d' % n)

H('Comparison operators related to $lt', 2)
P('Step 7 used $lt. The rest of the comparison family works the same way.')
table([1.2, 5.25], [
 ['Operator', 'Matches'],
 ['$gt', 'Values greater than the one given.'],
 ['$lt', 'Values less than the one given.'],
 ['$gte', 'Values greater than or equal to the one given.'],
 ['$lte', 'Values less than or equal to the one given.'],
 ['$eq', 'Values equal to the one given.'],
 ['$ne', 'Values not equal to the one given.'],
 ['$in', 'Values present in a given array.'],
 ['$nin', 'Values not present in a given array.'],
 ['$exists', 'Documents that have the specified field at all.'],
 ['$type', 'Documents where the field holds a specific BSON data type.'],
])
page_break()

H('Section 8: Pushing the work to GitHub', 1)
P('The finished work was committed from the Source Control panel in the codespace. The pending changes were reviewed, a commit message was entered, and Commit and Push was chosen from the dropdown beside the commit button so the changes went straight to the main branch of the repository.')
code('Submission for Module10, Nilson Sousa', 'Commit message')
shot('the Source Control panel with the pending changes and the commit message')
shot('the pushed commit visible on the GitHub repository')

H('Reflection', 1)
P('The part of this exercise that took the most care was the connection string. The password has to replace the whole placeholder including the angle brackets, and any special character in it has to be percent encoded, otherwise the driver misreads the string and the connection fails without saying why.')
P('The other thing worth noting is coordinate order. GeoJSON stores points as longitude first and latitude second, which is the reverse of how almost every map application presents them. Getting that backwards does not raise an error, it just quietly returns the wrong places, which makes it an easy mistake to miss.')
P('Comparing the two models directly, the aggregation pipeline felt closer to writing a series of small transformations than to writing one declarative SQL statement. Each stage hands its output to the next, so a complicated result can be built up and checked one stage at a time.')

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE + '/HOS10A-Nilson Sousa.docx'
doc.save(OUT)
print('wrote', OUT)
print('screenshots embedded: %d of %d' % (len(FOUND), len(FOUND) + len(MISSING)))
if MISSING:
    print('still missing (drop these into %s):' % SHOT_DIR)
    for k, c in MISSING:
        print('  %-22s %s' % (k + '.png', c))
