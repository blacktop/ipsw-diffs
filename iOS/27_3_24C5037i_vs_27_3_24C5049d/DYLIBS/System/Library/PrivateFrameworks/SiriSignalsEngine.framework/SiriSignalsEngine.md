## SiriSignalsEngine

> `/System/Library/PrivateFrameworks/SiriSignalsEngine.framework/SiriSignalsEngine`

```diff

-1.8.0.0.0
-  __TEXT.__text: 0x4d05c
-  __TEXT.__const: 0x2cd0
-  __TEXT.__swift5_typeref: 0xd8f
-  __TEXT.__constg_swiftt: 0x7d4
+1.8.5.0.0
+  __TEXT.__text: 0x52f4c
+  __TEXT.__const: 0x2ce0
+  __TEXT.__swift5_typeref: 0xddd
+  __TEXT.__constg_swiftt: 0x7fc
   __TEXT.__swift5_reflstr: 0x6d9
   __TEXT.__swift5_fieldmd: 0xba8
   __TEXT.__swift5_builtin: 0x50

   __TEXT.__swift5_types: 0xc8
   __TEXT.__swift_as_entry: 0xb8
   __TEXT.__swift_as_ret: 0xbc
-  __TEXT.__swift_as_cont: 0x128
-  __TEXT.__cstring: 0x12a55
-  __TEXT.__oslogstring: 0x6fc
+  __TEXT.__swift_as_cont: 0x130
+  __TEXT.__cstring: 0x12cb5
+  __TEXT.__oslogstring: 0x85c
   __TEXT.__swift5_acfuncs: 0x50
-  __TEXT.__swift5_capture: 0x150
+  __TEXT.__swift5_capture: 0x1ec
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x17c8
-  __TEXT.__eh_frame: 0x3298
+  __TEXT.__unwind_info: 0x1880
+  __TEXT.__eh_frame: 0x3518
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x170
+  __DATA_CONST.__objc_selrefs: 0x178
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x3758
+  __AUTH_CONST.__const: 0x3988
   __AUTH_CONST.__objc_const: 0x4b8
-  __AUTH_CONST.__auth_got: 0xc00
+  __AUTH_CONST.__auth_got: 0xc10
   __AUTH.__objc_data: 0x140
-  __AUTH.__data: 0x798
-  __DATA.__data: 0xa40
+  __AUTH.__data: 0x7c0
+  __DATA.__data: 0xa60
   __DATA.__common: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1976
-  Symbols:   659
-  CStrings:  130
+  Functions: 2165
+  Symbols:   683
+  CStrings:  143
 
Symbols:
+ _OUTLINED_FUNCTION_120
+ _OUTLINED_FUNCTION_121
+ _OUTLINED_FUNCTION_122
+ _OUTLINED_FUNCTION_123
+ _OUTLINED_FUNCTION_124
+ _OUTLINED_FUNCTION_125
+ _OUTLINED_FUNCTION_126
+ _OUTLINED_FUNCTION_127
+ _OUTLINED_FUNCTION_128
+ _OUTLINED_FUNCTION_129
+ _OUTLINED_FUNCTION_130
+ _OUTLINED_FUNCTION_131
+ _OUTLINED_FUNCTION_132
+ _OUTLINED_FUNCTION_133
+ _OUTLINED_FUNCTION_134
+ _OUTLINED_FUNCTION_135
+ _OUTLINED_FUNCTION_136
+ _OUTLINED_FUNCTION_137
+ _OUTLINED_FUNCTION_138
+ _sqlite3_last_insert_rowid
+ _swift_release_x10
+ _symbolic _____3iid_SSSg4textt s5Int64V
+ _symbolic _____y_____3iid_SSSg4texttG s23_ContiguousArrayStorageC s5Int64V
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation3URLV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5Int64V
- _objc_retain_x27
CStrings:
+ ");\nINSERT OR IGNORE INTO meta(key, value) VALUES ('store_version', "
+ ";\nPRAGMA secure_delete=ON;\n-- Items get an integer key on first insert (AUTOINCREMENT, so a deleted item's key is\n-- never reused) and the postings and rendered text are keyed by it. A new item's rows\n-- then land on the last pages, and a re-sent item's on its own pages, instead of\n-- scattering across indexes keyed by a random UUID.\nCREATE TABLE IF NOT EXISTS items(\n  iid INTEGER PRIMARY KEY AUTOINCREMENT, item_uuid TEXT NOT NULL UNIQUE,\n  source_type TEXT NOT NULL, recency REAL NOT NULL,\n  lexicon_version INTEGER NOT NULL, write_epoch INTEGER NOT NULL,\n  tombstoned INTEGER NOT NULL DEFAULT 0, mailboxes TEXT, bundle_id TEXT,\n  content_hash INTEGER NOT NULL DEFAULT 0);\nCREATE TABLE IF NOT EXISTS postings(\n  iid INTEGER NOT NULL, ngram TEXT NOT NULL, tf INTEGER NOT NULL,\n  PRIMARY KEY(iid, ngram)) WITHOUT ROWID;\nCREATE INDEX IF NOT EXISTS idx_items_epoch ON items(write_epoch);\nCREATE INDEX IF NOT EXISTS idx_items_recency ON items(recency);\nCREATE INDEX IF NOT EXISTS idx_items_src_recency ON items(source_type, recency);\nCREATE TABLE IF NOT EXISTS meta(key TEXT PRIMARY KEY, value INTEGER NOT NULL);\nINSERT OR IGNORE INTO meta(key, value) VALUES ('write_epoch', 0);\n-- Store-generation token: seeded ONCE per fresh store with a unique random value\n-- (OR IGNORE keeps it stable across reopens). A wipe/rebuild reseeds a new value,\n-- so a writer polling storeGeneration() detects the drop and re-drives all items.\nINSERT OR IGNORE INTO meta(key, value) VALUES ('cookie', "
+ ";\nPRAGMA secure_delete=ON;\nCREATE TABLE IF NOT EXISTS rendered_text(iid INTEGER PRIMARY KEY, text TEXT NOT NULL);"
+ "DELETE FROM items WHERE iid = ?;"
+ "DELETE FROM items WHERE recency < ?;"
+ "DELETE FROM postings WHERE iid = ?;"
+ "DELETE FROM postings WHERE iid IN (SELECT iid FROM items WHERE recency < ?);"
+ "DELETE FROM rendered_text WHERE iid = ?;"
+ "DELETE FROM rendered_text WHERE iid NOT IN (SELECT iid FROM postings_db.items);"
+ "INSERT INTO items(item_uuid, source_type, recency, lexicon_version, write_epoch, tombstoned,\n  mailboxes, bundle_id, content_hash)\nVALUES (?,?,?,?,?,0,?,?,?);"
+ "INSERT INTO rendered_text(iid, text) VALUES (?,?)\nON CONFLICT(iid) DO UPDATE SET text=excluded.text WHERE text <> excluded.text;"
+ "INSERT OR REPLACE INTO postings(iid, ngram, tf) VALUES (?,?,?);"
+ "PRAGMA journal_mode=WAL;\nPRAGMA journal_size_limit="
+ "PRAGMA table_info("
+ "SELECT i.bundle_id, SUM(p.tf), COUNT(DISTINCT p.iid)\nFROM postings p JOIN items i ON i.iid = p.iid\nWHERE p.ngram = ? AND i.tombstoned = 0\nGROUP BY i.bundle_id\nORDER BY 2 DESC;"
+ "SELECT iid FROM items WHERE item_uuid = ?;"
+ "SELECT iid FROM items WHERE recency < ?;"
+ "SELECT iid, content_hash FROM items WHERE item_uuid = ?;"
+ "SELECT ngram, tf FROM postings WHERE iid = ?;"
+ "SELECT text FROM rendered_text WHERE iid = ?;"
+ "SELECT value FROM meta WHERE key = 'store_version';"
+ "UPDATE items SET source_type=?, recency=?, lexicon_version=?, write_epoch=?, tombstoned=0,\n  mailboxes=?, bundle_id=?, content_hash=? WHERE iid=?;"
+ "[siriusergroundingd] expired %{public}ld items older than the window"
+ "[siriusergroundingd] expiry failed: %{public}s"
+ "record: %{public}ld written, %{public}ld unchanged and skipped, %{public}ld out of scope"
+ "rendered_text expiry skipped: %{public}@"
+ "replaced a store with the old schema; the writer will re-send every item"
- "ALTER TABLE items ADD COLUMN bundle_id TEXT;"
- "ALTER TABLE items ADD COLUMN mailboxes TEXT;"
- "DELETE FROM items WHERE item_uuid = ?;"
- "DELETE FROM postings WHERE item_uuid = ?;"
- "DELETE FROM rendered_text WHERE item_uuid = ?;"
- "DELETE FROM rendered_text WHERE item_uuid NOT IN (SELECT item_uuid FROM postings_db.items);"
- "INSERT INTO items(item_uuid, source_type, recency, lexicon_version, write_epoch, tombstoned, mailboxes, bundle_id)\nVALUES (?,?,?,?,?,0,?,?)\nON CONFLICT(item_uuid) DO UPDATE SET\n  source_type=excluded.source_type, recency=excluded.recency,\n  lexicon_version=excluded.lexicon_version, write_epoch=excluded.write_epoch,\n  tombstoned=0, mailboxes=excluded.mailboxes, bundle_id=excluded.bundle_id;"
- "INSERT OR REPLACE INTO postings(item_uuid, ngram, tf) VALUES (?,?,?);"
- "INSERT OR REPLACE INTO rendered_text(item_uuid, text) VALUES (?,?);"
- "PRAGMA journal_mode=WAL;\nPRAGMA secure_delete=ON;\nCREATE TABLE IF NOT EXISTS items(\n  item_uuid TEXT PRIMARY KEY, source_type TEXT NOT NULL, recency REAL NOT NULL,\n  lexicon_version INTEGER NOT NULL, write_epoch INTEGER NOT NULL,\n  tombstoned INTEGER NOT NULL DEFAULT 0, mailboxes TEXT, bundle_id TEXT);\nCREATE TABLE IF NOT EXISTS postings(\n  item_uuid TEXT NOT NULL, ngram TEXT NOT NULL, tf INTEGER NOT NULL,\n  PRIMARY KEY(item_uuid, ngram));\nCREATE INDEX IF NOT EXISTS idx_postings_ngram ON postings(ngram);\nCREATE INDEX IF NOT EXISTS idx_items_epoch ON items(write_epoch);\nCREATE INDEX IF NOT EXISTS idx_items_recency ON items(recency);\nCREATE INDEX IF NOT EXISTS idx_items_src_recency ON items(source_type, recency);\nCREATE TABLE IF NOT EXISTS meta(key TEXT PRIMARY KEY, value INTEGER NOT NULL);\nINSERT OR IGNORE INTO meta(key, value) VALUES ('write_epoch', 0);\n-- Store-generation token: seeded ONCE per fresh store with a unique random value\n-- (OR IGNORE keeps it stable across reopens). A wipe/rebuild reseeds a new value,\n-- so a writer polling storeGeneration() detects the drop and re-drives all items.\nINSERT OR IGNORE INTO meta(key, value) VALUES ('cookie', "
- "PRAGMA journal_mode=WAL;\nPRAGMA secure_delete=ON;\nCREATE TABLE IF NOT EXISTS rendered_text(item_uuid TEXT PRIMARY KEY, text TEXT NOT NULL);"
- "SELECT i.bundle_id, SUM(p.tf), COUNT(DISTINCT p.item_uuid)\nFROM postings p JOIN items i ON i.item_uuid = p.item_uuid\nWHERE p.ngram = ? AND i.tombstoned = 0\nGROUP BY i.bundle_id\nORDER BY 2 DESC;"
- "SELECT ngram, tf FROM postings WHERE item_uuid = ?;"
- "SELECT text FROM rendered_text WHERE item_uuid = ?;"
```
