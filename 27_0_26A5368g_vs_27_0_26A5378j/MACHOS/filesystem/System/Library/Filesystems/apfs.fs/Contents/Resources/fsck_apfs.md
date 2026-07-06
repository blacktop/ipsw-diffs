## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/fsck_apfs`

```diff

-  __TEXT.__text: 0x55e7c
+  __TEXT.__text: 0x55ee4
   __TEXT.__auth_stubs: 0xb90
-  __TEXT.__cstring: 0x1a6b4
+  __TEXT.__cstring: 0x1a749
   __TEXT.__const: 0x8720
-  __TEXT.__unwind_info: 0xb88
+  __TEXT.__unwind_info: 0xb98
   __DATA_CONST.__const: 0x620
   __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__auth_got: 0x5c8
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA.__data: 0xf28
+  __DATA.__data: 0xf30
   __DATA.__bss: 0x1e221
   __DATA.__common: 0x688
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 990
+  Functions: 991
   Symbols:   202
-  CStrings:  2012
+  CStrings:  2014
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__bss : content changed
CStrings:
+ "%s (id %llu): class %u file references per-file crypto_id (%llu) but is missing INODE_PROT_CLASS_EXPLICIT\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QPzQcM/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QPzQcM/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QPzQcM/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "3283.0.9.501.1"
+ "Set INODE_PROT_CLASS_EXPLICIT? "
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KI8RaQ/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KI8RaQ/Sources/AppleKeyStore_libs/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KI8RaQ/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "3283"

```
