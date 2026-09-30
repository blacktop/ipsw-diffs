## SystemConfiguration

> `/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration`

```diff

-1385.40.6.0.0
-  __TEXT.__text: 0x79a08
+1385.40.9.0.0
+  __TEXT.__text: 0x79c64
   __TEXT.__auth_stubs: 0x1f10
   __TEXT.__const: 0x2b0
   __TEXT.__cstring: 0x64bf
-  __TEXT.__oslogstring: 0x58b0
+  __TEXT.__oslogstring: 0x58f5
   __TEXT.__unwind_info: 0xcc0
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__const: 0x2cc0

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: C5EC3974-40DD-395D-B2CD-CFD62321CCEB
-  Functions: 1283
-  Symbols:   3748
-  CStrings:  2911
+  UUID: D97F1175-1463-3589-BFC2-D28BD8B3C22B
+  Functions: 1284
+  Symbols:   3749
+  CStrings:  2914
 
Symbols:
+ _SC_create_file_safely
Functions:
+ _SC_create_file_safely
~ _SCPreferencesCommitChanges : 4012 -> 3764
CStrings:
+ "open(%s) failed with ELOOP"
+ "open(%s) failed: %s"
+ "unlink(%s) failed: %s"

```
