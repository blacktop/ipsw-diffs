## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/newfs_apfs`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.6.0.0
-  __TEXT.__text: 0x54458
+2811.160.7.0.4
+  __TEXT.__text: 0x5461c
   __TEXT.__auth_stubs: 0x900
-  __TEXT.__cstring: 0x10742
+  __TEXT.__cstring: 0x10821
   __TEXT.__const: 0x84c1
   __TEXT.__oslogstring: 0x125
   __TEXT.__unwind_info: 0x8d0

   - /usr/lib/libutil.dylib
   Functions: 806
   Symbols:   161
-  CStrings:  1402
+  CStrings:  1405
 
Functions:
~ sub_1000063ac : 12056 -> 12064
~ sub_10000f96c -> sub_10000f974 : 1192 -> 1632
~ sub_100040dbc -> sub_100040f7c : 632 -> 636
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2BQrQO/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2BQrQO/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2BQrQO/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Yjd3GC/Sources/apfs_executables/nx/obj.c"
+ "2811.160.7.0.4"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7XiiiP/Sources/apfs_executables/nx/obj.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HwY5nz/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HwY5nz/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HwY5nz/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "2811.160.6"
```
