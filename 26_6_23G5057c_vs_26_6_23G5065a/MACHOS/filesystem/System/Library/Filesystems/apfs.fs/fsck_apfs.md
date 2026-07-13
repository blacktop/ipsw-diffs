## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

   __TEXT.__text: 0x53e64
   __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__cstring: 0x19ef1
+  __TEXT.__cstring: 0x19f07
   __TEXT.__const: 0x8710
   __TEXT.__unwind_info: 0xb58
   __DATA_CONST.__auth_got: 0x5e8
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
~ __DATA.__bss : content changed
CStrings:
+ "2811.160.7.0.4"
+ "reap list object 0x%llx first index %u larger than max index %u\n"
+ "reap list object 0x%llx free index %u larger than max index %u\n"
+ "reap list object 0x%llx last index %u larger than max index %u\n"
- "2811.160.7"
- "reap list object 0x%llx first index %u larger than max %u\n"
- "reap list object 0x%llx free index %u larger than max %u\n"
- "reap list object 0x%llx last index %u larger than max %u\n"

```
