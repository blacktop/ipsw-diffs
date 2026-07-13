## com.apple.fskit.apfs

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`

```diff

-  __TEXT.__text: 0xdf6d0
+  __TEXT.__text: 0xdf880
   __TEXT.__auth_stubs: 0xf70
   __TEXT.__objc_stubs: 0x11e0
   __TEXT.__objc_methlist: 0x83c
   __TEXT.__const: 0x8ad0
-  __TEXT.__cstring: 0x3a321
+  __TEXT.__cstring: 0x3a400
   __TEXT.__objc_methname: 0x1da3
   __TEXT.__oslogstring: 0x1ca4
   __TEXT.__objc_classname: 0x129

   - /usr/lib/libutil.dylib
   Functions: 3170
   Symbols:   1515
-  CStrings:  5294
+  CStrings:  5297
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
~ __DATA.__bss : content changed
Functions:
~ _omap_get : 628 -> 632
~ _nx_reaper_checkpoint_traverse : 1244 -> 1672
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "2811.160.7.0.4"
+ "reap list object 0x%llx first index %u larger than max index %u\n"
+ "reap list object 0x%llx free index %u larger than max index %u\n"
+ "reap list object 0x%llx last index %u larger than max index %u\n"
- "2811.160.7"
- "reap list object 0x%llx first index %u larger than max %u\n"
- "reap list object 0x%llx free index %u larger than max %u\n"
- "reap list object 0x%llx last index %u larger than max %u\n"

```
