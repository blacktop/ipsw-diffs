## livefiles_apfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib`

```diff

-  __TEXT.__text: 0xb4c18
+  __TEXT.__text: 0xb4c4c
   __TEXT.__auth_stubs: 0x8f0
   __TEXT.__const: 0x8690
   __TEXT.__oslogstring: 0x15dd3
   __TEXT.__cstring: 0x59bf
-  __TEXT.__unwind_info: 0x1018
+  __TEXT.__unwind_info: 0x1020
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x3c8
   __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__const: 0x470
   __AUTH_CONST.__cfstring: 0x120
-  __AUTH.__data: 0x248
+  __AUTH.__data: 0x250
   __DATA.__data: 0x9c
   __DATA.__common: 0x438
   __DATA.__bss: 0x89

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 2540
-  Symbols:   5802
+  Functions: 2541
+  Symbols:   5804
   CStrings:  2216
 
Sections:
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Symbols:
+ _fv_unwrap_and_migrate_vek
Functions:
~ _fv_unwrap_vek : 1008 -> 8
+ _fv_unwrap_and_migrate_vek
~ _fv_get_blob_state : 924 -> 952
CStrings:
+ "2811.160.7"
- "2811.160.6"

```
