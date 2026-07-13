## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/newfs_apfs`

```diff

-  __TEXT.__text: 0x515f8
+  __TEXT.__text: 0x517bc
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__cstring: 0xfaab
+  __TEXT.__cstring: 0xfb8a
   __TEXT.__const: 0x8470
   __TEXT.__unwind_info: 0x848
   __DATA_CONST.__auth_got: 0x468

   - /usr/lib/libutil.dylib
   Functions: 710
   Symbols:   156
-  CStrings:  1338
+  CStrings:  1341
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_1000058f0 : 12056 -> 12064
~ sub_10000eed8 -> sub_10000eee0 : 1192 -> 1632
~ sub_100040180 -> sub_100040340 : 632 -> 636
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "2811.160.7.0.4"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "2811.160.7"

```
