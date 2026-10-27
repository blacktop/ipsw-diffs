## SCHelper

> `/System/Library/Frameworks/SystemConfiguration.framework/Versions/A/Helpers/SCHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-1446.0.0.0.0
-  __TEXT.__text: 0x5f9c
-  __TEXT.__auth_stubs: 0x8e0
-  __TEXT.__const: 0xb8
-  __TEXT.__oslogstring: 0x7f3
-  __TEXT.__cstring: 0x498
+1453.40.1.0.0
+  __TEXT.__text: 0x6190
+  __TEXT.__auth_stubs: 0x900
+  __TEXT.__const: 0xc8
+  __TEXT.__oslogstring: 0x821
+  __TEXT.__cstring: 0x49f
   __TEXT.__unwind_info: 0x120
   __DATA_CONST.__const: 0x428
   __DATA_CONST.__cfstring: 0x480
-  __DATA_CONST.__auth_got: 0x470
+  __DATA_CONST.__auth_got: 0x480
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__data: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   Functions: 47
-  Symbols:   168
-  CStrings:  125
+  Symbols:   170
+  CStrings:  127
 
Symbols:
+ _close
+ _fdopen
+ _mkstemps
- _fopen
Functions:
~ sub_100002068 : 1708 -> 1704
~ sub_1000061d4 -> sub_1000061d0 : 492 -> 996
CStrings:
+ "/Library/Logs/DiagnosticReports/SCHelper-%4d-%02d-%02d-%02d%02d%02d-XXXXXX.log"
+ "fdopen(%s) failed: %s"
+ "mkstemps(%s) failed: %s"
- "/Library/Logs/DiagnosticReports/SCHelper-%4d-%02d-%02d-%02d%02d%02d.log"
```
