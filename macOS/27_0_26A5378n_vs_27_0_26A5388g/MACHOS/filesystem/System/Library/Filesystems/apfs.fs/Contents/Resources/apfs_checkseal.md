## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_checkseal`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3283.0.9.501.1
-  __TEXT.__text: 0x4fd38
+3283.0.13.501.1
+  __TEXT.__text: 0x4ff50
   __TEXT.__auth_stubs: 0x790
   __TEXT.__const: 0x4c0
-  __TEXT.__cstring: 0x102d6
+  __TEXT.__cstring: 0x103c4
   __TEXT.__unwind_info: 0x908
   __DATA_CONST.__const: 0x7b8
   __DATA_CONST.__cfstring: 0x160

   - /usr/lib/libutil.dylib
   Functions: 750
   Symbols:   136
-  CStrings:  1303
+  CStrings:  1307
 
Functions:
~ sub_100004be8 : 596 -> 640
~ sub_10001d0fc -> sub_10001d128 : 516 -> 520
~ sub_10002a0d4 -> sub_10002a104 : 1204 -> 1640
~ sub_10002c7b0 -> sub_10002c994 : 10496 -> 10504
~ sub_10003e4c8 -> sub_10003e6b4 : 632 -> 636
~ sub_100043c80 -> sub_100043e70 : 4160 -> 4172
~ sub_100045034 -> sub_100045230 : 3476 -> 3504
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
+ "apfs_sanity_check"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "%s:%d: obj is NULL or not apfs object!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/jobj.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/jobj_snap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/obj.c"
```
