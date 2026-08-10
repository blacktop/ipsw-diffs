## PerfPowerServicesReader

> `/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3486.0.81.502.4
-  __TEXT.__text: 0x14ae04
+3486.2.4.0.0
+  __TEXT.__text: 0x14b03c
   __TEXT.__init_offsets: 0xdc
   __TEXT.__objc_methlist: 0x12d94
-  __TEXT.__const: 0x5fe2
-  __TEXT.__cstring: 0xd106
-  __TEXT.__gcc_except_tab: 0x4a8c
-  __TEXT.__oslogstring: 0xd5f
-  __TEXT.__unwind_info: 0x49b8
+  __TEXT.__const: 0x5fd2
+  __TEXT.__cstring: 0xd0f4
+  __TEXT.__gcc_except_tab: 0x4adc
+  __TEXT.__oslogstring: 0xda1
+  __TEXT.__unwind_info: 0x49b0
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_arraydata: 0x110
   __DATA_CONST.__got: 0x720
   __AUTH_CONST.__const: 0x3090
-  __AUTH_CONST.__cfstring: 0xf0a0
+  __AUTH_CONST.__cfstring: 0xf0c0
   __AUTH_CONST.__objc_const: 0x16c28
   __AUTH_CONST.__weak_auth_got: 0xb0
   __AUTH_CONST.__objc_intobj: 0x1e0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7904
+  Functions: 7905
   Symbols:   12938
-  CStrings:  2142
+  CStrings:  2144
 
Functions:
~ ___60-[PPSSQLiteTimeSeriesIngester parseDataForRequest:outError:]_block_invoke : 900 -> 1120
- ___87-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:error:]_block_invoke.46
~ -[PPSSQLiteTimeSeriesIngester parseDataForRequest:outError:] : 2824 -> 2840
~ -[PPSSQLiteDatabase _statementForSQL:shouldCache:error:] : 544 -> 812
+ ___87-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:error:]_block_invoke.49
+ -[PPSSQLiteDatabase _statementForSQL:shouldCache:error:].cold.1
CStrings:
+ "Exception during query execution"
+ "SQL string contains more than one statement."
+ "SQL string contains more than one statement; refusing to execute."
- "SQL strings must contain only a single statement; remaining statements will not be executed: %s"
```
