## sqlite3

> `/usr/bin/sqlite3`

```diff

-401.0.0.0.0
-  __TEXT.__text: 0x1443dc sha256:e2f90a2acfb0723647bf63b058e0df034d586ba17a75dc31cc0d8276d8af584a
-  __TEXT.__auth_stubs: 0xeb0 sha256:2a70b559e2781ec152df664edb3350072367d7d11e71b7e514a569203bb217cc
-  __TEXT.__const: 0xafa4 sha256:7bcae1832b11093b3fcd67f10a68265fd3dede7e5c18a7cf4d8a183cac52f9e2
-  __TEXT.__cstring: 0x1fc21 sha256:bedd3c14d3f5a9f376b9c7aaef499a69c6fd55502436a8302618572b9b3e23b4
+402.0.0.0.0
+  __TEXT.__text: 0x143dac sha256:a23b463f871b7f4a9955aae5bb851b9a795abcbf9df6366f6f5a40b33e4bb78c
+  __TEXT.__auth_stubs: 0xeb0 sha256:cab4b96101cb903181d3a588c37eb048c7669d0565dae5d34d955184c0e56abb
+  __TEXT.__const: 0xafa4 sha256:5360ff58d6bc916260e1866f70363331c521e7b0db5c175474cc370deb9c6b10
+  __TEXT.__cstring: 0x1fc6e sha256:10d237659be998c85783ee624fd1a62e51918b0e552b76aafe1d6ead89918b8f
   __TEXT.__oslogstring: 0x7c0 sha256:1145913275574e25ee3b4fbf413b1f0327ccb474cdfb482e960e232a13fc46a8
-  __TEXT.__unwind_info: 0x2900 sha256:6d823a225ee0b6df44e8c388304544c10220e1b68a8b33f73be609364b721840
-  __TEXT.__eh_frame: 0x88 sha256:4ebeba25f756959fed541c60f35bd38fb768ffcc9580a265b0a3958ff234c8c2
-  __DATA_CONST.__const: 0x4b70 sha256:b9996b6b2244de6a6679e2957c723421d744068204fe98cc156c3e7591a50181
+  __TEXT.__unwind_info: 0x2948 sha256:2a85de69cf70f9e46fdbb3911b72e277845dec6868b1cc0b3da08b5d0872f393
+  __TEXT.__eh_frame: 0x88 sha256:0e68abf98f8160ac158f4a1391d63b5e252d4efb1953393aa728fc54f0368dc0
+  __DATA_CONST.__const: 0x4b70 sha256:d287eb7aa2088f901cbf92291c8488110774d2bcb7900eadb54d1969e95cfc6d
   __DATA_CONST.__auth_got: 0x758 sha256:aff5ada7100ecfbb32a66482a313f9665f535e39f02d8a15afbbe77a7bc50c36
   __DATA_CONST.__got: 0xc8 sha256:e0037ee72c1521cbdc79ddf2b477675d4b410ede9330c5e46faaf0749674ef90
   __DATA_CONST.__auth_ptr: 0x18 sha256:a207c91973b323919561b80c13a72e2b225a5800db9689981019db5df14e6544
-  __DATA.__data: 0x5100 sha256:c2293b9b79c2de4875870c4a6544339911332622585c7c8b998e01750d9609bb
+  __DATA.__data: 0x5100 sha256:30976b163938a96a83b377c4561ba45021d98b72e385845aaae6c503f8ee2ec3
   __DATA.__crash_info: 0x148 sha256:6da6349e97370e8d430272961ce52dff296ff7c22208bd465045a16f557b12e4
   __DATA.__bss: 0x2ce0 sha256:0c20d990b8ce28fa7d0b90199a5973688ed45ca02c1bf8cf91e132bcce749698
   __DATA.__common: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb

   - /usr/lib/libedit.3.dylib
   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 99CA4688-C81B-3BE5-9049-5B37D8BC1759
-  Functions: 3466
+  UUID: 4BFAB851-2CB7-3E7E-801F-A7374F88B231
+  Functions: 3471
   Symbols:   281
-  CStrings:  4349
+  CStrings:  4352
 
CStrings:
+ "CREATE TABLE recovery.map(pgno INTEGER PRIMARY KEY, parent INT)"
+ "CREATE TABLE recovery.schema(type, name, tbl_name, rootpage, sql)"
+ "CREATE TABLE t1(a)"
+ "DROP TABLE t1"
+ "PRAGMA writable_schema = 1"
+ "SELECT rootpage, sql FROM recovery.schema   WHERE type!='table' AND (type!='index' OR sql NOT LIKE '%unique%')    AND sql GLOB 'CREATE *'"
+ "SELECT rootpage, sql FROM recovery.schema   WHERE type!='table' AND type!='index'    AND sql GLOB 'CREATE *'"
+ "WITH dbschema(rootpage, name, sql, tbl, isVirtual, isIndex) AS (  SELECT rootpage, name, sql,     type='table',     sql LIKE 'create virtual%',    (type='index' AND (sql LIKE '%unique%' OR ?1))  FROM recovery.schema)SELECT rootpage, tbl, isVirtual, name, sql FROM dbschema   WHERE (tbl OR isIndex) AND sql GLOB 'CREATE *'  ORDER BY tbl DESC, name=='sqlite_sequence' DESC"
- "CREATE TABLE t1(a); DROP TABLE t1;"
- "PRAGMA writable_schema = 1;CREATE TABLE recovery.map(pgno INTEGER PRIMARY KEY, parent INT);CREATE TABLE recovery.schema(type, name, tbl_name, rootpage, sql);"
- "SELECT rootpage, sql FROM recovery.schema   WHERE type!='table' AND (type!='index' OR sql NOT LIKE '%unique%')"
- "SELECT rootpage, sql FROM recovery.schema   WHERE type!='table' AND type!='index'"
- "WITH dbschema(rootpage, name, sql, tbl, isVirtual, isIndex) AS (  SELECT rootpage, name, sql,     type='table',     sql LIKE 'create virtual%',    (type='index' AND (sql LIKE '%unique%' OR ?1))  FROM recovery.schema)SELECT rootpage, tbl, isVirtual, name, sql FROM dbschema   WHERE tbl OR isIndex  ORDER BY tbl DESC, name=='sqlite_sequence' DESC"

```
