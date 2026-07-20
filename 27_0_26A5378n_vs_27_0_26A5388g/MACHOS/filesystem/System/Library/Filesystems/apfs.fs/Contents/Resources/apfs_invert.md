## apfs_invert

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_invert`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3283.0.9.501.1
-  __TEXT.__text: 0x5233c
+3283.0.13.501.1
+  __TEXT.__text: 0x52558
   __TEXT.__auth_stubs: 0x800
-  __TEXT.__cstring: 0x10ecb
+  __TEXT.__cstring: 0x10fba
   __TEXT.__const: 0x8418
   __TEXT.__unwind_info: 0x928
   __DATA_CONST.__const: 0x838

   - /usr/lib/libutil.dylib
   Functions: 753
   Symbols:   143
-  CStrings:  1397
+  CStrings:  1401
 
Functions:
~ sub_100010c14 : 10496 -> 10504
~ sub_100014c40 -> sub_100014c48 : 596 -> 640
~ sub_100018180 -> sub_1000181b4 : 1204 -> 1640
~ sub_1000211e4 -> sub_1000213cc : 440 -> 452
~ sub_100038a48 -> sub_100038c3c : 328 -> 324
~ sub_100044474 -> sub_100044664 : 632 -> 636
~ sub_100049224 -> sub_100049418 : 4160 -> 4172
~ sub_10004a5d8 -> sub_10004a7d8 : 3476 -> 3504
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "%s:%d: obj is NULL or not apfs object!\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XQJT3Z/Sources/apfs_executables/nx/jobj.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XQJT3Z/Sources/apfs_executables/nx/jobj_snap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XQJT3Z/Sources/apfs_executables/nx/obj.c"
+ "3283.0.13.501.1"
+ "apfs_sanity_check"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "%s:%d: obj is NULL or not apfs object!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/jobj.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/jobj_snap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/obj.c"
- "3283.0.9.501.1"
```
