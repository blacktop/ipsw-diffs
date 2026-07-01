## com.apple.fskit.apfs

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`

```diff

-  __TEXT.__text: 0xdf44c
+  __TEXT.__text: 0xdf52c
   __TEXT.__auth_stubs: 0xf70
   __TEXT.__objc_stubs: 0x11e0
   __TEXT.__objc_methlist: 0x83c
   __TEXT.__const: 0x8ad0
-  __TEXT.__cstring: 0x3a0a8
+  __TEXT.__cstring: 0x3a19d
   __TEXT.__objc_methname: 0x1da3
   __TEXT.__oslogstring: 0x1ca4
   __TEXT.__objc_classname: 0x129
   __TEXT.__objc_methtype: 0x305f
   __TEXT.__gcc_except_tab: 0x484
-  __TEXT.__unwind_info: 0x1b28
+  __TEXT.__unwind_info: 0x1b20
   __DATA_CONST.__auth_got: 0x7c8
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x80

   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x1300
-  __DATA.__common: 0xb00
-  __DATA.__bss: 0x1e239
+  __DATA.__common: 0x7e0
+  __DATA.__bss: 0x1e241
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3168
+  Functions: 3169
   Symbols:   1515
-  CStrings:  5283
+  CStrings:  5288
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Symbols:
+ _is_omap_in_reaper
- _omap_in_reaper
CStrings:
+ "2811.122.1"
+ "could not allocate array of %u entries for tracking omap objects in reap list; skipping subsequent ones\n"
+ "encountered more than %u omap objects in reap list; skipping subsequent ones\n"
+ "fsck_reaper.c"
+ "omap_info.omaps_in_reaper == NULL"
+ "set_omap_in_reaper"
- "2811.120.14.0.1"

```
