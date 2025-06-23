## libsqlite3.dylib

> `/usr/lib/libsqlite3.dylib`

```diff

-349.3.0.0.0
-  __TEXT.__text: 0x1570ac
-  __TEXT.__auth_stubs: 0xa10
-  __TEXT.__const: 0x7aa8
-  __TEXT.__cstring: 0xb856
+350.2.0.0.0
+  __TEXT.__text: 0x167918
+  __TEXT.__auth_stubs: 0xa40
+  __TEXT.__const: 0x7c78
+  __TEXT.__cstring: 0xbd82
   __TEXT.__oslogstring: 0x610
-  __TEXT.__unwind_info: 0x1d5c
+  __TEXT.__unwind_info: 0x1e34
   __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x1c38
-  __AUTH_CONST.__const: 0x1100
-  __AUTH_CONST.__auth_got: 0x508
-  __AUTH.__data: 0x930
-  __DATA.__data: 0x170
+  __DATA_CONST.__const: 0x1ce0
+  __AUTH_CONST.__const: 0x1118
+  __AUTH_CONST.__auth_got: 0x520
+  __AUTH.__data: 0x908
+  __DATA.__data: 0x188
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x2760
+  __DATA.__bss: 0x26f0
   __DATA.__common: 0x10
-  __DATA_DIRTY.__data: 0x2e30
-  __DATA_DIRTY.__bss: 0x32e
+  __DATA_DIRTY.__data: 0x3808
+  __DATA_DIRTY.__bss: 0x2b0
   - /usr/lib/libSystem.B.dylib
-  UUID: 48C19B53-12D5-3A2E-B452-7505022C1B29
-  Functions: 2443
-  Symbols:   541
-  CStrings:  2129
+  UUID: 9275A6EC-A2AD-33A7-A94F-6D528FD9F9FB
+  Functions: 2515
+  Symbols:   566
+  CStrings:  2223
 
Symbols:
+ _acos
+ _acosh
+ _asin
+ _asinh
+ _atan
+ _atan2
+ _atanh
+ _cos
+ _cosh
+ _exp
+ _fmod
+ _log10
+ _log2
+ _memset_pattern16
+ _nanosleep
+ _pow
+ _sin
+ _sinh
+ _sqlite3_is_interrupted
+ _sqlite3_stmt_explain
+ _sqlite3_stmt_scanstatus_v2
+ _sqlite3_value_encoding
+ _sqrt
+ _strspn
+ _tan
+ _tanh
+ _trunc
- _sleep
- _usleep
CStrings:
+ " = ?"
+ " AND (?%d OR ?%d IS %w.%w)"
+ " AND (?6 OR ?3 IS stat)"
+ " WHERE <expr>"
+ " of index "
+ " values differ from index "
+ "%!.*f"
+ "%!0.15g"
+ "%.3f"
+ "%c%04d-%02d-%02d %02d:%02d:%06.3f"
+ "%s is %u but should be %u"
+ "%s)%s"
+ "%z%s\"%w\".\"%w\".\"%w\""
+ "'delete' may not be used with a contentless_delete=1 table"
+ "+- \n\t0123456789"
+ ", 1"
+ ",?"
+ ",origin"
+ "-9.0e999"
+ "-Inf"
+ "2023-10-10 13:08:14 1b37c146ee9ebb7acd0160c0ab1fd11017a419fa8a3187386ed8cb32b709aapl"
+ "2nd reference to page %u"
+ "40f"
+ "40f-20a-20d"
+ "50f"
+ "50f-20a-20d"
+ "9.0e999"
+ "?%d"
+ "?1, (CASE WHEN ?2=X'' THEN NULL ELSE ?2 END)"
+ "Bad ptr map entry key=%u expected=(%u,%u) got=(%u,%u)"
+ "C"
+ "CREATE AUTOMATIC INDEX ON %s("
+ "CREATE TABLE x(addr INT,opcode TEXT,p1 INT,p2 INT,p3 INT,p4 TEXT,p5 INT,comment TEXT,subprog TEXT,nexec INT,ncycle INT,stmt HIDDEN);"
+ "DELETE FROM '%q'.'%q_idx' WHERE (segid, (pgno/2)) = (?1, ?2)"
+ "DQS=3"
+ "ENABLE_MATH_FUNCTIONS"
+ "Failed to read ptrmap key=%u"
+ "Fragmentation of %u bytes reported as %u on page %u"
+ "Freelist: "
+ "IsType"
+ "NUM"
+ "NUMERIC value in %s.%s"
+ "Offset %u out of range %u..%u"
+ "Page %u: never used"
+ "Page %u: pointer map referenced"
+ "QNaN"
+ "REPLACE INTO %Q.'%q_docsize' VALUES(?,?%s)"
+ "RIGHT PART OF "
+ "SELECT %s FROM \"%w\".\"%w\" WHERE NOT EXISTS (  SELECT 1 FROM \"%w\".\"%w\" WHERE %s)"
+ "SELECT %s%s FROM %Q.%Q WHERE (%s) IS (%s)"
+ "SELECT %s,%s FROM \"%w\".\"%w\", \"%w\".\"%w\" WHERE %s AND (%z)"
+ "SELECT sz%s FROM %Q.'%q_docsize' WHERE id=?"
+ "SNaN"
+ "TEXT value in %s.%s"
+ "Tree %u page %u cell %u: "
+ "Tree %u page %u right child: "
+ "Tree %u page %u: "
+ "USE TEMP B-TREE FOR %sORDER BY"
+ "\\u00"
+ "\\u0000"
+ "\\u0009"
+ "_rowid_, *"
+ "acos"
+ "acosh"
+ "asin"
+ "asinh"
+ "atan"
+ "atan2"
+ "atanh"
+ "cannot UPDATE a subset of columns on fts5 contentless-delete table: %s"
+ "ceil"
+ "ceiling"
+ "contentless_delete"
+ "contentless_delete=1 is incompatible with columnsize=0"
+ "contentless_delete=1 requires a contentless table"
+ "cos"
+ "cosh"
+ "database corruption page %u of %s"
+ "degrees"
+ "deletemerge"
+ "exp"
+ "failed to get page %u"
+ "flexnum"
+ "floor"
+ "freelist leaf count too big on page %u"
+ "fts5 expression tree is too large (maximum depth %d)"
+ "fts5: 2023-10-10 13:08:14 1b37c146ee9ebb7acd0160c0ab1fd11017a419fa8a3187386ed8cb32b709a6b1"
+ "id INTEGER PRIMARY KEY, sz BLOB, origin INTEGER"
+ "ieee754_inc"
+ "inf"
+ "infinity"
+ "inity"
+ "invalid fts5 file format (found %d, expected %d or %d) - run 'rebuild'"
+ "invalid page number %u"
+ "json_error_position"
+ "ln"
+ "log10"
+ "log2"
+ "malformed contentless_delete=... directive"
+ "max rootpage (%u) disagrees with header (%u)"
+ "mod"
+ "octet_length"
+ "pi"
+ "pow"
+ "power"
+ "radians"
+ "row not in PRIMARY KEY order for %s"
+ "rowid not at end-of-record for row "
+ "secure-delete"
+ "sin"
+ "sinh"
+ "sqrt"
+ "struct iovec"
+ "subsec"
+ "subsecond"
+ "subst"
+ "tan"
+ "tanh"
+ "tbl, ?2, stat"
+ "tbl, idx"
+ "timediff"
+ "trunc"
+ "unhex"
- "%.*f"
- "%s is %d but should be %d"
- "2022-10-14 20:58:05 554764a6e721fab307c63a4f98cd958c8428a5d9d8edfde951858d6fd02daapl"
- "2nd reference to page %d"
- "Bad ptr map entry key=%d expected=(%d,%d) got=(%d,%d)"
- "CREATE TABLE x(addr INT,opcode TEXT,p1 INT,p2 INT,p3 INT,p4 TEXT,p5 INT,comment TEXT,subprog TEXT,stmt HIDDEN);"
- "Failed to read ptrmap key=%d"
- "Fragmentation of %d bytes reported as %d on page %u"
- "IsNullOrType"
- "Main freelist: "
- "Offset %d out of range %d..%d"
- "On page %u at right child: "
- "On tree page %u cell %d: "
- "Page %d is never used"
- "Page %u: "
- "Pointer map page %d is referenced"
- "RIGHT PART OF ORDER BY"
- "SELECT * FROM "
- "SELECT * FROM \"%w\".\"%w\" WHERE NOT EXISTS (  SELECT 1 FROM \"%w\".\"%w\" WHERE %s)"
- "SELECT * FROM \"%w\".\"%w\", \"%w\".\"%w\" WHERE %s AND (%z)"
- "SELECT sz FROM %Q.'%q_docsize' WHERE id=?"
- "SELECT tbl, ?2, stat FROM %Q.sqlite_stat1 WHERE tbl IS ?1 AND idx IS (CASE WHEN ?2=X'' THEN NULL ELSE ?2 END)"
- "database corruption page %d of %s"
- "failed to get page %d"
- "freelist leaf count too big on page %d"
- "fts5: 2022-10-14 20:58:05 d37c01a120a98bceb5e5ee2f8d7cd0ba0e91ef0908b60f12d7079cb098f611cc"
- "invalid fts5 file format (found %d, expected %d) - run 'rebuild'"
- "invalid page number %d"
- "max rootpage (%d) disagrees with header (%d)"

```
