## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

-  __TEXT.__text: 0x53d5c
+  __TEXT.__text: 0x53e1c
   __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__cstring: 0x19e3f
+  __TEXT.__cstring: 0x19ef1
   __TEXT.__const: 0x8710
   __TEXT.__unwind_info: 0xb50
   __DATA_CONST.__auth_got: 0x5e8

   __DATA_CONST.__const: 0x610
   __DATA_CONST.__cfstring: 0x200
   __DATA.__data: 0xee8
-  __DATA.__bss: 0x1e1f1
-  __DATA.__common: 0xac9
+  __DATA.__bss: 0x1e1f9
+  __DATA.__common: 0x7a9
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit

   - /usr/lib/libutil.dylib
   Functions: 962
   Symbols:   206
-  CStrings:  1975
+  CStrings:  1977
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_10002377c : 404 -> 56
~ sub_100023910 -> sub_1000237b4 : 744 -> 404
~ sub_100023bf8 -> sub_100023948 : 1656 -> 932
~ sub_100024270 -> sub_100023cec : 56 -> 1656
~ sub_10003e7b0 -> sub_10003e86c : 1168 -> 1172
CStrings:
+ "2811.122.1"
+ "could not allocate array of %u entries for tracking omap objects in reap list; skipping subsequent ones\n"
+ "encountered more than %u omap objects in reap list; skipping subsequent ones\n"
- "2811.120.14.0.1"

```
