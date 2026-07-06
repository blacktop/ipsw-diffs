## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

-  __TEXT.__text: 0x56834
+  __TEXT.__text: 0x5687c
   __TEXT.__auth_stubs: 0xc00
-  __TEXT.__cstring: 0x1a637
+  __TEXT.__cstring: 0x1a6cc
   __TEXT.__const: 0x8730
-  __TEXT.__unwind_info: 0xb98
+  __TEXT.__unwind_info: 0xba0
   __DATA_CONST.__const: 0x620
   __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__auth_got: 0x600
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA.__data: 0xf30
+  __DATA.__data: 0xf38
   __DATA.__bss: 0x1e251
   __DATA.__common: 0x688
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 987
+  Functions: 988
   Symbols:   209
-  CStrings:  2016
+  CStrings:  2018
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__bss : content changed
CStrings:
+ "%s (id %llu): class %u file references per-file crypto_id (%llu) but is missing INODE_PROT_CLASS_EXPLICIT\n"
+ "3283.0.9.502.1"
+ "Set INODE_PROT_CLASS_EXPLICIT? "
- "3283"

```
