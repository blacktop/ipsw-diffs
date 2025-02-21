## FinHealthCore

> `/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore`

```diff

-1.7.3.3.0
-  __TEXT.__text: 0x2c28c
+1.7.4.1.0
+  __TEXT.__text: 0x2c0c8
   __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0x28cc
+  __TEXT.__objc_methlist: 0x2a74
   __TEXT.__const: 0x318
-  __TEXT.__cstring: 0x712b
-  __TEXT.__gcc_except_tab: 0x884
+  __TEXT.__cstring: 0x7216
+  __TEXT.__gcc_except_tab: 0x8a0
   __TEXT.__oslogstring: 0x107c
-  __TEXT.__unwind_info: 0x978
+  __TEXT.__unwind_info: 0x960
   __TEXT.__objc_classname: 0x593
   __TEXT.__objc_methname: 0x6fa3
   __TEXT.__objc_methtype: 0x7e4
   __TEXT.__objc_stubs: 0x5040
   __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x1450
+  __DATA_CONST.__const: 0x1460
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19c0
+  __DATA_CONST.__objc_selrefs: 0x1a40
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x308
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x5300
-  __AUTH_CONST.__objc_const: 0x5498
+  __AUTH_CONST.__cfstring: 0x5340
+  __AUTH_CONST.__objc_const: 0x51a8
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x5f0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 959
-  Symbols:   1638
-  CStrings:  2188
+  Functions: 973
+  Symbols:   1660
+  CStrings:  2190
 
Symbols:
+ _FHDeleteGroupsByType
+ _FHRetrieveGroupForTransaction
CStrings:
+ "(g_id integer primary key autoincrement,t_identifier text, group_id integer, similarity_score text, group_type integer, UNIQUE(t_identifier, group_type))"
+ "10.73"
+ "CREATE TRIGGER transactions_ai AFTER INSERT ON transactions BEGIN INSERT INTO fts_transactions(rowid, t_identifier, t_source_identifier, a_type, t_date, t_description) VALUES (new.t_tid, new.t_identifier, new.t_source_identifier, new.a_type, new.t_date, new.t_description); END;"
+ "CREATE TRIGGER transactions_au AFTER UPDATE ON transactions BEGIN INSERT INTO fts_transactions(rowid, t_identifier, t_source_identifier, a_type, t_date, t_description) VALUES (new.t_tid, new.t_identifier, new.t_source_identifier, new.a_type, new.t_date, new.t_description); END;"
+ "CREATE TRIGGER transactions_bd BEFORE DELETE ON transactions BEGIN INSERT INTO fts_transactions(fts_transactions, rowid, t_identifier, t_source_identifier, a_type, t_date, t_description) VALUES('delete', old.t_tid, old.t_identifier, old.t_source_identifier, old.a_type, old.t_date, old.t_description); END;"
+ "CREATE TRIGGER transactions_bu BEFORE UPDATE ON transactions BEGIN INSERT INTO fts_transactions(fts_transactions, rowid, t_identifier, t_source_identifier, a_type, t_date, t_description) VALUES('delete', old.t_tid, old.t_identifier, old.t_source_identifier, old.a_type, old.t_date, old.t_description); END;"
+ "CREATE VIRTUAL TABLE fts_transactions USING fts5(t_identifier UNINDEXED, t_source_identifier UNINDEXED, a_type UNINDEXED, t_date UNINDEXED, t_description, content=transactions, content_rowid=t_tid);"
+ "delete from fh_grouping where group_type == %d"
+ "select group_id from fh_grouping where t_identifier == %@"
+ "select t_identifier, t_description from fts_transactions where a_type == %d AND t_description IS NOT NULL order by t_date"
- "(g_id integer primary key autoincrement,t_identifier text, group_id integer, similarity_score text, group_type integer, UNIQUE(t_identifier, group_id))"
- "10.72"
- "CREATE TRIGGER transactions_ai AFTER INSERT ON transactions BEGIN INSERT INTO fts_transactions(rowid, t_identifier, t_source_identifier, a_type, t_description) VALUES (new.t_tid, new.t_identifier, new.t_source_identifier, new.a_type, new.t_description); END;"
- "CREATE TRIGGER transactions_au AFTER UPDATE ON transactions BEGIN INSERT INTO fts_transactions(rowid, t_identifier, t_source_identifier, a_type, t_description) VALUES (new.t_tid, new.t_identifier, new.t_source_identifier, new.a_type, new.t_description); END;"
- "CREATE TRIGGER transactions_bd BEFORE DELETE ON transactions BEGIN INSERT INTO fts_transactions(fts_transactions, rowid, t_identifier, t_source_identifier, a_type, t_description) VALUES('delete', old.t_tid, old.t_identifier, old.t_source_identifier, old.a_type, old.t_description); END;"
- "CREATE TRIGGER transactions_bu BEFORE UPDATE ON transactions BEGIN INSERT INTO fts_transactions(fts_transactions, rowid, t_identifier, t_source_identifier, a_type, t_description) VALUES('delete', old.t_tid, old.t_identifier, old.t_source_identifier, old.a_type, old.t_description); END;"
- "CREATE VIRTUAL TABLE fts_transactions USING fts5(t_identifier UNINDEXED, t_source_identifier UNINDEXED, a_type UNINDEXED, t_description, content=transactions, content_rowid=t_tid);"
- "select t_description from fts_transactions where a_type == %d AND t_description IS NOT NULL"

```
