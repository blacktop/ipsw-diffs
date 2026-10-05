## SCHelper

> `/System/Library/Frameworks/SystemConfiguration.framework/SCHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-1453.0.0.0.0
-  __TEXT.__text: 0x4b70
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__const: 0xa0
-  __TEXT.__oslogstring: 0x4d7
-  __TEXT.__cstring: 0x3b6
+1453.40.1.0.0
+  __TEXT.__text: 0x4d68
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__const: 0xb0
+  __TEXT.__oslogstring: 0x505
+  __TEXT.__cstring: 0x3bd
   __TEXT.__unwind_info: 0x110
   __DATA_CONST.__const: 0x3b0
   __DATA_CONST.__cfstring: 0x380
-  __DATA_CONST.__auth_got: 0x3a0
+  __DATA_CONST.__auth_got: 0x3b0
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__data: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   Functions: 43
-  Symbols:   134
-  CStrings:  100
+  Symbols:   136
+  CStrings:  102
 
Symbols:
+ _close
+ _fdopen
+ _mkstemps
- _fopen
Functions:
~ sub_100004f98 : 492 -> 996
CStrings:
+ "/Library/Logs/CrashReporter/SCHelper-%4d-%02d-%02d-%02d%02d%02d-XXXXXX.log"
+ "fdopen(%s) failed: %s"
+ "mkstemps(%s) failed: %s"
- "/Library/Logs/CrashReporter/SCHelper-%4d-%02d-%02d-%02d%02d%02d.log"
```
