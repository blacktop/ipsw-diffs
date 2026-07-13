## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/apfs_condenser`

```diff

-  __TEXT.__text: 0x4bf60
+  __TEXT.__text: 0x4c124
   __TEXT.__auth_stubs: 0x780
-  __TEXT.__cstring: 0xf5be
+  __TEXT.__cstring: 0xf69d
   __TEXT.__const: 0x210
   __TEXT.__unwind_info: 0x7f0
   __DATA_CONST.__auth_got: 0x3c0

   - /usr/lib/libutil.dylib
   Functions: 663
   Symbols:   134
-  CStrings:  1265
+  CStrings:  1268
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_10000791c : 12056 -> 12064
~ sub_10000f2c0 -> sub_10000f2c8 : 1192 -> 1632
~ sub_10003d0a4 -> sub_10003d264 : 632 -> 636
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
