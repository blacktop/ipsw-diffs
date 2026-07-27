## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/fsck_apfs`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__bss`

```diff

-2811.160.6.0.0
-  __TEXT.__text: 0x53534
+2811.160.7.0.4
+  __TEXT.__text: 0x53568
   __TEXT.__auth_stubs: 0xb60
-  __TEXT.__cstring: 0x19f6e
+  __TEXT.__cstring: 0x19f84
   __TEXT.__const: 0x8700
-  __TEXT.__unwind_info: 0xb40
+  __TEXT.__unwind_info: 0xb48
   __DATA_CONST.__auth_got: 0x5b0
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x68
   __DATA_CONST.__const: 0x610
   __DATA_CONST.__cfstring: 0x200
-  __DATA.__data: 0xee0
+  __DATA.__data: 0xee8
   __DATA.__bss: 0x1e1c9
   __DATA.__common: 0x7a9
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 965
+  Functions: 966
   Symbols:   199
   CStrings:  1957
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EU55BS/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EU55BS/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EU55BS/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "2811.160.7.0.4"
+ "reap list object 0x%llx first index %u larger than max index %u\n"
+ "reap list object 0x%llx free index %u larger than max index %u\n"
+ "reap list object 0x%llx last index %u larger than max index %u\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PengPR/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PengPR/Sources/AppleKeyStore_libs/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PengPR/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "2811.160.6"
- "reap list object 0x%llx first index %u larger than max %u\n"
- "reap list object 0x%llx free index %u larger than max %u\n"
- "reap list object 0x%llx last index %u larger than max %u\n"
```
