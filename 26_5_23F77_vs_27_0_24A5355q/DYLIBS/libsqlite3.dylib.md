## libsqlite3.dylib

> `/usr/lib/libsqlite3.dylib`

```diff

-382.0.0.0.0
-  __TEXT.__text: 0x1917e0
-  __TEXT.__auth_stubs: 0xad0
-  __TEXT.__const: 0x8180
-  __TEXT.__cstring: 0xc68d
-  __TEXT.__oslogstring: 0x777
-  __TEXT.__unwind_info: 0x1d10
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x1df0
-  __AUTH_CONST.__auth_got: 0x568
-  __AUTH_CONST.__const: 0x11c0
-  __AUTH.__data: 0x930
-  __DATA.__data: 0x1b0
+401.0.0.0.0
+  __TEXT.__text: 0x19e19c
+  __TEXT.__const: 0x8774
+  __TEXT.__cstring: 0xcec2
+  __TEXT.__oslogstring: 0x7c0
+  __TEXT.__unwind_info: 0x1df0
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x1e70
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x1230
+  __AUTH_CONST.__auth_got: 0x580
+  __AUTH.__data: 0x878
+  __DATA.__data: 0x190
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x2700
+  __DATA.__bss: 0x2710
   __DATA.__common: 0x10
-  __DATA_DIRTY.__data: 0x3cb0
-  __DATA_DIRTY.__bss: 0x2e0
+  __DATA_DIRTY.__data: 0x3f50
+  __DATA_DIRTY.__bss: 0x2f8
   - /usr/lib/libSystem.B.dylib
-  UUID: 0A0C0FA5-02BB-35B5-9CE5-B702637152A7
-  Functions: 2463
-  Symbols:   583
-  CStrings:  2324
+  UUID: 3A14C004-A1A2-3A04-AD4B-0AF4E19C1107
+  Functions: 2532
+  Symbols:   607
+  CStrings:  2399
 
Symbols:
+ _XPC_COALITION_INFO_KEY_BUNDLE_IDENTIFIER
+ _XPC_COALITION_INFO_KEY_NAME
+ __xpc_type_dictionary
+ _csops
+ _proc_pidinfo
+ _sqlite3_carray_bind_v2
+ _sqlite3_db_status64
+ _sqlite3_incomplete
+ _sqlite3_key_v3
+ _sqlite3_rekey_v3
+ _sqlite3_set_errmsg
+ _sqlite3_str_free
+ _sqlite3_str_truncate
+ _sqlite3changegroup_change_begin
+ _sqlite3changegroup_change_blob
+ _sqlite3changegroup_change_double
+ _sqlite3changegroup_change_finish
+ _sqlite3changegroup_change_int64
+ _sqlite3changegroup_change_null
+ _sqlite3changegroup_change_text
+ _sqlite3changegroup_config
+ _sqlite3changeset_apply_v3
+ _sqlite3changeset_apply_v3_strm
+ _xpc_coalition_copy_info
+ _xpc_dictionary_get_string
- __os_feature_enabled_impl
CStrings:
+ " EXISTS"
+ "%!.*g"
+ "%!0.17g"
+ "%.*s %s%s"
+ "%.*s%s%s"
+ "%.*s, %s%s"
+ "%s %S%s"
+ "%s references tables to its right"
+ "*]"
+ ".0"
+ "/* %s */ "
+ "/* unknown trigger */ "
+ "2026-04-09 12:25:13 8fa8248e303219400c646a885e36dfc52eae33d83f4412e3f369b2be5373aapl"
+ "<Unknown>"
+ "ENABLE_CARRAY"
+ "ENABLE_PERCENTILE"
+ "Error: %{errorMessage,public}s coalition: %{coalition,public}s"
+ "Failed to determine code signing flags"
+ "IFindKey"
+ "IfEmpty"
+ "Inf input to %%s()"
+ "JSON nested too deep"
+ "JSON path too deep"
+ "ON clause"
+ "PerfPowerServices"
+ "Recursion limit"
+ "SELECT sqlite_fail('constraint %q already exists', %d) FROM \"%w\".sqlite_master WHERE type='table' AND tbl_name=%Q COLLATE nocase AND sqlite_find_constraint(sql, %Q)"
+ "SELECT sqlite_fail('constraint failed', %d) FROM %Q.%Q AS x WHERE x.%.*s IS NULL"
+ "SELECT sqlite_fail('constraint failed', %d) FROM %Q.%Q WHERE (%.*s) IS NOT TRUE"
+ "SQL Error"
+ "UPDATE \"%w\".sqlite_master SET sql = sqlite_add_constraint(sql, %.*Q, -1) WHERE type='table' AND tbl_name=%Q COLLATE nocase"
+ "UPDATE \"%w\".sqlite_master SET sql = sqlite_add_constraint(sqlite_drop_constraint(sql, %d), %.*Q, %d) WHERE type='table' AND tbl_name=%Q COLLATE nocase"
+ "UPDATE \"%w\".sqlite_master SET sql = sqlite_drop_constraint(sql, %s) WHERE type='table' AND tbl_name=%Q COLLATE nocase"
+ "\\u000b"
+ "aes128"
+ "aes256"
+ "alg"
+ "array_insert"
+ "com.apple.libsqlite3.telemetry"
+ "constraint may not be dropped: %s"
+ "drop constraint"
+ "edit constraints of"
+ "expressions"
+ "fts5: 2026-04-09 12:25:13 8fa8248e303219400c646a885e36dfc52eae33d83f4412e3f369b2be53737732"
+ "fts5: checksum mismatch for table \"%s\""
+ "fts5: corrupt structure record for table \"%s\""
+ "fts5: corruption found reading blob %lld from table \"%s\""
+ "fts5: corruption in table \"%s\""
+ "fts5: corruption on page %d, segment %d, table \"%s\""
+ "ieee754_from_int"
+ "ieee754_to_int"
+ "index %s stores an imprecise floating-point value for row "
+ "input to %%s() is not numeric"
+ "invalid change: %s value in PK of old.* record"
+ "invalid change: column %d - old.* value is %sdefined but new.* is %sdefined"
+ "invalid change: column %d is undefined"
+ "invalid change: defined value in PK of new.* record"
+ "invalid change: null value in PK"
+ "irb"
+ "json_array_insert"
+ "jsonb_array_insert"
+ "jsonb_each"
+ "jsonb_tree"
+ "median"
+ "no such constraint: %s"
+ "noop"
+ "not an array element: %Q"
+ "percentile"
+ "percentile_cont"
+ "percentile_disc"
+ "perl"
+ "python"
+ "reserve"
+ "ruby"
+ "see-cccrypt"
+ "sql_error"
+ "sqlite_add_constraint"
+ "sqlite_drop_constraint"
+ "sqlite_fail"
+ "sqlite_find_constraint"
+ "statement aborts at %d: %s; [%s%s]"
+ "table-function argument"
+ "tclsh"
+ "the fraction argument to %%s() is not between 0.0 and %.1f"
+ "the fraction argument to %%s() is not the same for all input rows"
+ "un"
+ "undefined"
- "%!0.20e"
- "%s %S"
- "%s USING TEMP B-TREE"
- "2025-06-12 13:14:41 f0ca7bba1c5e232e5d279fad6338121ab55af0c8c68c84cdfb18ba5114dcaapl"
- "ExpensiveQueryTelemetry"
- "ON clause references tables to its right"
- "SQLite"
- "\\u0009"
- "abort at %d: %s; [%s]"
- "fts5: 2025-06-12 13:14:41 f0ca7bba1c5e232e5d279fad6338121ab55af0c8c68c84cdfb18ba5114dcc60c"
- "parser stack overflow"
- "statement aborts at %d: %s; [%s]"

```
