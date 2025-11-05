## lockstat

> `/usr/bin/lockstat`

```diff

 411.0.0.0.0
-  __TEXT.__text: 0x3534
+  __TEXT.__text: 0x3434
   __TEXT.__auth_stubs: 0x430
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x1380
-  __TEXT.__unwind_info: 0xc0
+  __TEXT.__cstring: 0x137d
+  __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__auth_got: 0x218
   __DATA_CONST.__got: 0x28
   __DATA.__data: 0x3484

   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/Versions/A/CoreSymbolication
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libdtrace.dylib
-  UUID: 6CEE5AA0-CD74-3D8B-A9BB-2A4AF70E09E9
+  UUID: A4D60154-7476-3F29-AFCC-9F26D5B38E4F
   Functions: 29
   Symbols:   132
-  CStrings:  162
+  CStrings:  161
 
Functions:
~ _main : 9100 -> 8836
~ _lockstat_mergesort : 312 -> 304
~ _process_aggregate : 300 -> 312
~ _process_trace : 112 -> 116
CStrings:
- "CH"

```
