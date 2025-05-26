## keybagd

> `/usr/libexec/keybagd`

```diff

-621.40.2.0.0
-  __TEXT.__text: 0x1c7a8
-  __TEXT.__auth_stubs: 0x13c0
+625.100.7.0.0
+  __TEXT.__text: 0x1ce64
+  __TEXT.__auth_stubs: 0x13d0
   __TEXT.__objc_stubs: 0xfa0
   __TEXT.__objc_methlist: 0x480
-  __TEXT.__cstring: 0x77fb
+  __TEXT.__cstring: 0x7cdb
   __TEXT.__const: 0xd1
   __TEXT.__gcc_except_tab: 0x468
-  __TEXT.__objc_methname: 0x173b
+  __TEXT.__objc_methname: 0x175b
   __TEXT.__objc_classname: 0xa7
-  __TEXT.__objc_methtype: 0x917
+  __TEXT.__objc_methtype: 0x925
   __TEXT.__dlopen_cstrs: 0x16a
   __TEXT.__oslogstring: 0x16a
-  __TEXT.__unwind_info: 0x5f8
-  __DATA_CONST.__auth_got: 0x9f0
+  __TEXT.__unwind_info: 0x608
+  __DATA_CONST.__auth_got: 0x9f8
   __DATA_CONST.__got: 0x108
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0xe00
-  __DATA_CONST.__cfstring: 0x4ba0
+  __DATA_CONST.__const: 0xe40
+  __DATA_CONST.__cfstring: 0x4bc0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x90
   __DATA.__objc_const: 0xef0
   __DATA.__objc_selrefs: 0x570
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0xa0
-  __DATA.__objc_superrefs: 0x18
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x1e8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 441
-  Symbols:   375
-  CStrings:  1299
+  Functions: 449
+  Symbols:   376
+  CStrings:  1326
 
Symbols:
+ _CFErrorCreate
+ _objc_release_x25
+ _objc_retain_x25
- _objc_release_x24
- _objc_retain_x24
CStrings:
+ "-[KBXPCService SeshatUnlockWithSecret:secretSize:withMemento:verifyOnly:withACMRef:withReply:]"
+ "ALTER TABLE WrappedKeys ADD COLUMN AddTime TIMESTAMP DEFAULT 0;ALTER TABLE WrappedKeys ADD COLUMN AccessTime TIMESTAMP DEFAULT 0;ALTER TABLE WrappedKeys ADD COLUMN ClearTime TIMESTAMP DEFAULT 0;PRAGMA user_version = 3;"
+ "AnalyticsEvent: status: %llu"
+ "CFDictionaryAddInt"
+ "CFDictionaryAddSQLStringIfNotNull"
+ "Cannot bind age: %s\n"
+ "Cleared Key"
+ "DELETE FROM WrappedKeys WHERE Flagged = 1 AND Key IS NULL AND unixepoch('now') - unixepoch(ClearTime) > ? ;"
+ "DROP TABLE IF EXISTS WrappedKeys;CREATE TABLE WrappedKeys(Inode INT, Uuid BLOB, Key BLOB, Flagged BOOLEAN DEFAULT 0, AddTime TIMESTAMP DEFAULT 0, ClearTime TIMESTAMP DEFAULT 0, AccessTime TIMESTAMP DEFAULT 0, unique(Inode, Uuid));CREATE INDEX Inode ON WrappedKeys(Inode);CREATE INDEX InodeUuid ON WrappedKeys(Inode, Uuid);PRAGMA user_version = 3;"
+ "Failed to prepare get statement: %s\n"
+ "Internal error: could not create CFNumber from int"
+ "Internal error: could not create CFString from C string %s"
+ "Invalid Key"
+ "Migrating backup db from v2"
+ "MobileKeyBagError.DbGetError"
+ "REPLACE INTO WrappedKeys (Inode, Uuid, Key, AddTime) VALUES(?, ?, ?, datetime('now', 'subsec'))"
+ "SELECT Key, AddTime, AccessTime, ClearTime FROM WrappedKeys WHERE Inode = ? AND Uuid = ?"
+ "SeshatUnlockWithSecret:secretSize:withMemento:verifyOnly:withACMRef:withReply:"
+ "Step failed rc=%d, %s"
+ "T@\"NSString\",?,R,C"
+ "UPDATE WrappedKeys SET Key = NULL, ClearTime = datetime('now', 'subsec') WHERE Flagged = 1 AND Key NOT NULL;"
+ "UPDATE WrappedKeys SET Key = NULL, Flagged = 0, ClearTime = datetime('now', 'subsec') WHERE Flagged = 1 AND Key NOT NULL AND Uuid = ?"
+ "accessed"
+ "added"
+ "analytics_send_db_add"
+ "analytics_send_db_get"
+ "cleared"
+ "com.apple.mobile.keybagd.db.add"
+ "com.apple.mobile.keybagd.db.get"
+ "db_clear_flagged"
+ "db_clear_flagged_volume"
+ "db_delete_flagged_old"
+ "db_migrate_from_v2"
+ "sqlError"
+ "status"
+ "v56@0:8@\"NSFileHandle\"16Q24B32B36@\"NSData\"40@?<v@?i@\"NSError\">48"
+ "v56@0:8@16Q24B32B36@40@?48"
- "-[KBXPCService SeshatUnlockWithSecret:secretSize:withMemento:verifyOnly:withReply:]"
- "DELETE FROM WrappedKeys WHERE Flagged = 1"
- "DROP TABLE IF EXISTS WrappedKeys;CREATE TABLE WrappedKeys(Inode INT, Uuid BLOB, Key BLOB, Flagged BOOLEAN DEFAULT 0, unique(Inode, Uuid));CREATE INDEX Inode ON WrappedKeys(Inode);CREATE INDEX InodeUuid ON WrappedKeys(Inode, Uuid);PRAGMA user_version = 2;"
- "REPLACE INTO WrappedKeys VALUES(?, ?, ?, 0)"
- "SELECT Key FROM WrappedKeys WHERE Inode = ? AND Uuid = ?"
- "SeshatUnlockWithSecret:secretSize:withMemento:verifyOnly:withReply:"
- "db_delete_flagged"
- "unexpected number of bytes %d\n"
- "v48@0:8@\"NSFileHandle\"16Q24B32B36@?<v@?i@\"NSError\">40"
- "v48@0:8@16Q24B32B36@?40"

```
