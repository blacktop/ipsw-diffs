## libsqlite3.dylib

> `/usr/lib/libsqlite3.dylib`

```diff

-360.1.0.0.0
-  __TEXT.__text: 0x169320
-  __TEXT.__auth_stubs: 0xa70
-  __TEXT.__const: 0x7e54
-  __TEXT.__cstring: 0xbda9
-  __TEXT.__oslogstring: 0x6d8
-  __TEXT.__unwind_info: 0x1d68
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x1d00
-  __AUTH_CONST.__auth_got: 0x538
-  __AUTH_CONST.__const: 0x1138
-  __AUTH.__data: 0x930
-  __DATA.__data: 0x170
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x26f0
+371.0.0.0.0
+  __TEXT.__text: 0x190b24
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__const: 0x813c
+  __TEXT.__cstring: 0xc546
+  __TEXT.__oslogstring: 0x777
+  __TEXT.__unwind_info: 0x1d40
+  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__const: 0x1dc8
+  __AUTH_CONST.__auth_got: 0x560
+  __AUTH_CONST.__const: 0x11a0
+  __AUTH.__data: 0x968
+  __DATA.__data: 0x1c0
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x2708
   __DATA.__common: 0x10
-  __DATA_DIRTY.__data: 0x3970
+  __DATA_DIRTY.__data: 0x3e80
   __DATA_DIRTY.__bss: 0x2d0
   - /usr/lib/libSystem.B.dylib
-  UUID: 7B66E49D-0FE5-394B-ADCA-F5731B03DFDA
-  Functions: 2436
-  Symbols:   569
-  CStrings:  2223
+  UUID: 3FE564CD-732A-33EA-9407-E4CCB870F990
+  Functions: 2449
+  Symbols:   580
+  CStrings:  2309
 
Symbols:
+ ___memmove_chk
+ __os_feature_enabled_impl
+ __xpc_type_bool
+ __xpc_type_int64
+ _memchr
+ _sqlite3_get_clientdata
+ _sqlite3_set_clientdata
+ _sqlite3changegroup_add_change
+ _sqlite3changegroup_schema
+ _xpc_bool_get_value
+ _xpc_get_type
+ _xpc_int64_get_value
- _memset_pattern16
CStrings:
+ "    "
+ " VIRTUAL TABLE INDEX "
+ "\""
+ "\"\\/bfnrt"
+ "%!0.20e"
+ "%02d:%02d"
+ "%02d:%02d:%02d"
+ "%04d-%02d-%02d"
+ "%2d"
+ "%d:%s"
+ "%s a subset of columns on fts5 contentless-delete table: %s"
+ "%s contentless fts5 table: %s"
+ "%s: \"%s\" - should this be a string literal in single-quotes?"
+ "%u-ROW VALUES CLAUSE"
+ "%z%s?%d"
+ "%z,?%d"
+ ",\n"
+ ", NULL"
+ ", T.l%d"
+ ", l%d"
+ "-9e999"
+ ".\""
+ ".\"%.*s\""
+ "0x%x:%s"
+ "200"
+ "2024-12-16 18:27:27 86c6d40764d2dee83f92215a40179af621c5b28277b3b87a577cbdb69b53aapl"
+ "9e999"
+ ": "
+ "@"
+ "AM"
+ "ATTACH %Q AS %s"
+ "BEGIN IMMEDIATE; COMMIT;"
+ "CODEC=see-cccrypt"
+ "CREATE BLOOM FILTER"
+ "DELETE FROM %Q.'%q_content';"
+ "DIRECT_OVERFLOW_READ"
+ "ExpensiveQueryTelemetry"
+ "FLAGS parameter to json_valid() must be between 1 and 15"
+ "GetSubtype"
+ "INSERT INTO %Q.%Q(%Q) VALUES('flush')"
+ "INSERT INTO %s.sqlite_schema SELECT*FROM \"%w\".sqlite_schema WHERE type IN('view','trigger') OR(type='table'AND rootpage=0)"
+ "IfSizeBetween"
+ "In RTree %s.%s:\n%z"
+ "LAST TERM OF "
+ "ORDER BY may not be used with non-aggregate %#T()"
+ "PM"
+ "PRAGMA '%q'.table_xinfo('%q')"
+ "REPLACE INTO %Q.'%q_config' VALUES ('version', %d)"
+ "SCAN %S"
+ "SELECT"
+ "SELECT 0, 'tbl',  '', 0, '', 1, 0     UNION ALL SELECT 1, 'idx',  '', 0, '', 2, 0     UNION ALL SELECT 2, 'stat', '', 0, '', 0, 0"
+ "SELECT CASE WHEN quick_check GLOB 'CHECK*' THEN raise(ABORT,'CHECK constraint failed') WHEN quick_check GLOB 'non-* value in*' THEN raise(ABORT,'type mismatch on DEFAULT') ELSE raise(ABORT,'NOT NULL constraint failed') END  FROM pragma_quick_check(%Q,%Q) WHERE quick_check GLOB 'CHECK*' OR quick_check GLOB 'NULL*' OR quick_check GLOB 'non-* value in*'"
+ "SELECT pgno FROM '%q'.'%q_idx' WHERE segid=? AND term>? ORDER BY term ASC LIMIT 1"
+ "SELECT'INSERT INTO %s.'||quote(name)||' SELECT*FROM\"%w\".'||quote(name)FROM %s.sqlite_schema WHERE type='table'AND coalesce(rootpage,1)>0"
+ "SELECT*FROM\"%w\".\"%w\""
+ "SQLITE_ACCEPTABLE_PAGES_PER_STEP"
+ "SQLite"
+ "SetSubtype"
+ "USE TEMP B-TREE FOR %s(ORDER BY)"
+ "USE TEMP B-TREE FOR LAST %d TERMS OF ORDER BY"
+ "VCheck"
+ "[%lld]"
+ "\\\""
+ "_node"
+ "am"
+ "bad JSON path: %Q"
+ "cannot DELETE from contentless fts5 table: %s"
+ "cannot UPDATE"
+ "cannot create triggers on shadow tables"
+ "cannot open table with generated columns: %s"
+ "com.apple.private.sqlite.defensive"
+ "contentless_unindexed"
+ "contentless_unindexed=1 requires a contentless table"
+ "enableTelemetry=%s nSpill=%{public,signpost.telemetry:number1,name=rc}d writes=%{public,public,signpost.telemetry:number2}d"
+ "enableTelemetry=%s rc=%{public,signpost.telemetry:number1,name=rc}d runCount=%{public}d nScan=%{public}d nAutoindex=%{public}d nSort=%{public}d nSpill=%{public}d nStep=%{public}d errMsg=%{public}s nVmStep=%{public,signpost.telemetry:number2,name=nVmStep}d hits=%{public}d misses=%{public}d writes=%{public}d bytesPerRow=%{public}d"
+ "flush"
+ "fts5: 2024-12-16 18:27:27 86c6d40764d2dee83f92215a40179af621c5b28277b3b87a577cbdb69b53c0f5"
+ "fts5: missing row %lld from content table %s"
+ "fts5_get_locale"
+ "fts5_insttoken"
+ "fts5_locale"
+ "fts5_locale() requires locale=1"
+ "if"
+ "insttoken"
+ "internal query planner error"
+ "json_pretty"
+ "jsonb"
+ "jsonb_array"
+ "jsonb_extract"
+ "jsonb_group_array"
+ "jsonb_group_object"
+ "jsonb_insert"
+ "jsonb_object"
+ "jsonb_patch"
+ "jsonb_remove"
+ "jsonb_replace"
+ "jsonb_set"
+ "malformed inverted index for FTS%d table %s.%s"
+ "malformed inverted index for FTS5 table %s.%s"
+ "malformed locale=... directive"
+ "malformed tokendata=... directive"
+ "non-integer argument passed to function fts5_get_locale()"
+ "pm"
+ "sqlite_returning_%p"
+ "string_agg"
+ "subrtnsig:%d,%s"
+ "syntax error"
+ "unable to validate the inverted index for FTS%d table %s.%s: %s"
+ "unable to validate the inverted index for FTS5 table %s.%s: %s"
+ "unrecognized token: \"%s\""
+ "vacuum_%016llx"
+ "wrong number of arguments to function fts5_get_locale()"
- " = ?"
- " VIRTUAL TABLE INDEX %d:%s"
- "$."
- "$["
- "%!.20e"
- "%s_node"
- "-9.0e999"
- "2023-10-10 13:08:14 1b37c146ee9ebb7acd0160c0ab1fd11017a419fa8a3187386ed8cb32b709aapl"
- "ATTACH %Q AS vacuum_db"
- "DELETE from"
- "END"
- "INSERT INTO vacuum_db.sqlite_schema SELECT*FROM \"%w\".sqlite_schema WHERE type IN('view','trigger') OR(type='table'AND rootpage=0)"
- "IfSmaller"
- "JSON path error near '%q'"
- "PRAGMA '%q'.table_info('%q')"
- "RIGHT PART OF "
- "SELECT 0, 'tbl',  '', 0, '', 1     UNION ALL SELECT 1, 'idx',  '', 0, '', 2     UNION ALL SELECT 2, 'stat', '', 0, '', 0"
- "SELECT CASE WHEN quick_check GLOB 'CHECK*' THEN raise(ABORT,'CHECK constraint failed') ELSE raise(ABORT,'NOT NULL constraint failed') END  FROM pragma_quick_check(%Q,%Q) WHERE quick_check GLOB 'CHECK*' OR quick_check GLOB 'NULL*'"
- "SELECT'INSERT INTO vacuum_db.'||quote(name)||' SELECT*FROM\"%w\".'||quote(name)FROM vacuum_db.sqlite_schema WHERE type='table'AND coalesce(rootpage,1)>0"
- "[%d]"
- "cannot %s contentless fts5 table: %s"
- "cannot UPDATE a subset of columns on fts5 contentless-delete table: %s"
- "enableTelemetry=%s rc=%{public,signpost.telemetry:number1,name=rc}d runCount=%{public}d nScan=%{public}d nAutoindex=%{public}d nSort=%{public}d nSpill=%{public}d nStep=%{public}d errMsg=%{public}s nVmStep=%{public,signpost.telemetry:number2,name=nVmStep}d hits=%{public}d misses=%{public}d writes=%{public}d"
- "fts5: 2023-10-10 13:08:14 1b37c146ee9ebb7acd0160c0ab1fd11017a419fa8a3187386ed8cb32b709a6b1"
- "sqlite_returning"
- "subst"
- "tbl, idx"

```
