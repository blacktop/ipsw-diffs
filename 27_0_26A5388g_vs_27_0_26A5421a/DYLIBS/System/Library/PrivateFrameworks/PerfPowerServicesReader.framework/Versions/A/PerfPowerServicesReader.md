## PerfPowerServicesReader

> `/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/Versions/A/PerfPowerServicesReader`

```diff

-3486.0.81.501.3
-  __TEXT.__text: 0x15207c
+3486.1.2.0.0
+  __TEXT.__text: 0x1522dc
   __TEXT.__init_offsets: 0xdc
   __TEXT.__objc_methlist: 0x12d94
-  __TEXT.__const: 0x5fea
-  __TEXT.__cstring: 0xd106
-  __TEXT.__gcc_except_tab: 0x4ac0
-  __TEXT.__oslogstring: 0xd5f
+  __TEXT.__const: 0x5fda
+  __TEXT.__cstring: 0xd0f4
+  __TEXT.__gcc_except_tab: 0x4b10
+  __TEXT.__oslogstring: 0xda1
   __TEXT.__unwind_info: 0x4ae0
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_arraydata: 0x110
   __DATA_CONST.__got: 0x720
   __AUTH_CONST.__const: 0x36f0
-  __AUTH_CONST.__cfstring: 0xf0a0
+  __AUTH_CONST.__cfstring: 0xf0c0
   __AUTH_CONST.__objc_const: 0x16c28
   __AUTH_CONST.__weak_auth_got: 0xb0
   __AUTH_CONST.__objc_intobj: 0x1e0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7944
+  Functions: 7945
   Symbols:   13057
-  CStrings:  2142
+  CStrings:  2144
 
Functions:
~ -[PPSSQLiteDatabase _statementForSQL:shouldCache:error:] : 568 -> 860
~ -[PPSSQLiteTimeSeriesIngester parseDataForRequest:outError:] : 2968 -> 2984
~ ___60-[PPSSQLiteTimeSeriesIngester parseDataForRequest:outError:]_block_invoke : 956 -> 1192
+ -[PPSSQLiteDatabase _statementForSQL:shouldCache:error:].cold.1
CStrings:
+ "Exception during query execution"
+ "SQL string contains more than one statement."
+ "SQL string contains more than one statement; refusing to execute."
- "SQL strings must contain only a single statement; remaining statements will not be executed: %s"
```
