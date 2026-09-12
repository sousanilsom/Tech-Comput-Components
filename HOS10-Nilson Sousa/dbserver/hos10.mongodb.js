/* ============================================================
   CS11A: Technology & Computing Components I
   HOS10A: MongoDB Atlas
   Nilson Sousa
   MongoDB for VS Code Playground (Section 7)

   How to use:
     Run ONE step at a time so each "Playground Result" pane can
     be captured as its own screenshot. Select the lines for a
     step, then press the run (triangle) button.

   Note on shell helpers:
     A playground file is JavaScript, so the mongosh helpers
     "show dbs" and "show collections" are not valid here. The
     JavaScript equivalents are used instead and the helper form
     is kept beside each one as a comment.
   ============================================================ */


/* --- Step 1: list the databases on the server --------------- */
/* mongosh helper: show dbs */
db.getMongo().getDBs();


/* --- Step 2: switch to the practice database ---------------- */
/* Creates CS628Practice on first write if it does not exist. */
use('CS628Practice');


/* --- Step 3: confirm the current database ------------------- */
use('CS628Practice');
/* mongosh helper: db */
db.getName();


/* --- Step 4: create the users collection -------------------- */
use('CS628Practice');
db.createCollection('users');


/* --- Step 5: insert several user profiles ------------------- */
use('CS628Practice');
db.users.insertMany([
  { name: 'user1', age: 25, email: 'user1@cityuniversity.edu' },
  { name: 'user2', age: 32, email: 'user2@cityuniversity.edu' },
  { name: 'user3', age: 28, email: 'user3@cityuniversity.edu' },
  { name: 'user4', age: 41, email: 'user4@cityuniversity.edu' },
  { name: 'CityUser5', age: 22, email: 'cityuser5@cityuniversity.edu' }
]);


/* --- Step 6: read every document in the collection ---------- */
use('CS628Practice');
db.users.find();


/* --- Step 7: filter with a comparison operator -------------- */
use('CS628Practice');
/* $lt matches values strictly less than the one given. */
db.users.find({ age: { $lt: 30 } });


/* --- Step 8: update a single document ----------------------- */
use('CS628Practice');
db.users.updateOne({ name: 'user1' }, { $set: { age: 31 } });


/* --- Step 9: verify the update ------------------------------ */
use('CS628Practice');
db.users.find({ name: 'user1' });


/* --- Step 10: delete a single document ---------------------- */
use('CS628Practice');
db.users.deleteOne({ name: 'user2' });


/* --- Step 11: verify the delete ----------------------------- */
use('CS628Practice');
db.users.find();


/* --- Step 12: aggregate the average age --------------------- */
use('CS628Practice');
/* _id: null groups every document into one bucket. */
db.users.aggregate([
  { $group: { _id: null, averageAge: { $avg: '$age' } } }
]);


/* --- Step 13: index the email field ------------------------- */
use('CS628Practice');
/* 1 means ascending order. */
db.users.createIndex({ email: 1 });


/* --- Step 14: text index, then a text search ---------------- */
use('CS628Practice');
db.users.createIndex({ name: 'text', email: 'text' });

db.users.find({ $text: { $search: 'user1' } });


/* --- Step 15: sort by age, highest first -------------------- */
use('CS628Practice');
/* -1 means descending order. */
db.users.find().sort({ age: -1 });


/* --- Step 16: paginate with limit and skip ------------------ */
use('CS628Practice');
db.users.find().limit(2).skip(1);


/* --- Step 17: group and count users by age ------------------ */
use('CS628Practice');
db.users.aggregate([
  { $group: { _id: '$age', count: { $sum: 1 } } },
  { $sort: { _id: 1 } }
]);


/* --- Step 18: oldest and youngest user ---------------------- */
use('CS628Practice');
db.users.aggregate([
  { $group: { _id: null, oldest: { $max: '$age' }, youngest: { $min: '$age' } } }
]);


/* --- Step 19: geospatial data and a 2dsphere index ---------- */
use('CS628Practice');
/* Coordinates are stored as GeoJSON in [longitude, latitude] order. */
db.places.insertMany([
  { name: 'CityU Seattle', location: { type: 'Point', coordinates: [-122.2015, 47.6101] } },
  { name: 'Pike Place Market', location: { type: 'Point', coordinates: [-122.3421, 47.6097] } },
  { name: 'Space Needle', location: { type: 'Point', coordinates: [-122.3493, 47.6205] } },
  { name: 'Portland OR', location: { type: 'Point', coordinates: [-122.6765, 45.5152] } }
]);

db.places.createIndex({ location: '2dsphere' });


/* --- Step 20: find places within a radius ------------------- */
use('CS628Practice');
/* $centerSphere takes a radius in radians, so divide the
   distance in kilometres by the radius of the Earth (6378.1 km). */
db.places.find({
  location: {
    $geoWithin: {
      $centerSphere: [[-122.3321, 47.6062], 20 / 6378.1]
    }
  }
});

/* $near returns the same area sorted by distance from the point. */
db.places.find({
  location: {
    $near: {
      $geometry: { type: 'Point', coordinates: [-122.3321, 47.6062] },
      $maxDistance: 20000
    }
  }
});


/* --- Step 21: advanced query with $or and regular expressions */
use('CS628Practice');
/* 'i' makes the match case insensitive. */
db.users.find({
  $or: [
    { name: { $regex: '^u', $options: 'i' } },
    { name: { $regex: '^C', $options: 'i' } }
  ]
});


/* --- Step 22: total age of all users ------------------------ */
use('CS628Practice');
db.users.aggregate([
  { $group: { _id: null, totalAge: { $sum: '$age' } } }
]);


/* --- Step 23: clean up -------------------------------------- */
use('CS628Practice');
/* mongosh helper: show dbs */
db.getMongo().getDBs();

/* mongosh helper: db */
db.getName();

/* mongosh helper: show collections */
db.getCollectionNames();

db.users.drop();

db.places.drop();

/* mongosh helper: show collections */
db.getCollectionNames();
