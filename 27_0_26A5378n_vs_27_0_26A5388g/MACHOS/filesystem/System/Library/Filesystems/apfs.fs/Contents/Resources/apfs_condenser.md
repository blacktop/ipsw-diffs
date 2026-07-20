## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_condenser`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3283.0.9.501.1
-  __TEXT.__text: 0x4d598
+3283.0.13.501.1
+  __TEXT.__text: 0x4d7b4
   __TEXT.__auth_stubs: 0x820
-  __TEXT.__cstring: 0xfa83
+  __TEXT.__cstring: 0xfb72
   __TEXT.__const: 0x220
   __TEXT.__unwind_info: 0x850
   __DATA_CONST.__const: 0x8f8

   - /usr/lib/libutil.dylib
   Functions: 688
   Symbols:   144
-  CStrings:  1288
+  CStrings:  1292
 
Functions:
~ sub_10000a908 : 10496 -> 10504
~ sub_10000e934 -> sub_10000e93c : 596 -> 640
~ sub_100011cdc -> sub_100011d10 : 1204 -> 1640
~ sub_10003112c -> sub_100031314 : 276 -> 284
~ sub_10004014c -> sub_10004033c : 632 -> 636
~ sub_1000451b4 -> sub_1000453a8 : 4160 -> 4172
~ sub_100046568 -> sub_100046768 : 3476 -> 3504
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "%s:%d: obj is NULL or not apfs object!\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XQJT3Z/Sources/apfs_executables/nx/jobj_snap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XQJT3Z/Sources/apfs_executables/nx/obj.c"
+ "3283.0.13.501.1"
+ "apfs_sanity_check"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "%s:%d: obj is NULL or not apfs object!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/jobj_snap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/obj.c"
- "3283.0.9.501.1"
```
