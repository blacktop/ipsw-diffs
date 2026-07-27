## apfs_prepare_cryptex

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_prepare_cryptex`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.6.0.0
-  __TEXT.__text: 0x6e254
+2811.160.7.0.4
+  __TEXT.__text: 0x6e418
   __TEXT.__auth_stubs: 0x840
   __TEXT.__const: 0xc51a
-  __TEXT.__cstring: 0x18104
+  __TEXT.__cstring: 0x181e3
   __TEXT.__unwind_info: 0xc48
   __DATA_CONST.__auth_got: 0x420
   __DATA_CONST.__got: 0x58

   - /usr/lib/libutil.dylib
   Functions: 1000
   Symbols:   148
-  CStrings:  2076
+  CStrings:  2079
 
Functions:
~ sub_100046ed0 : 1192 -> 1632
~ sub_100049674 -> sub_10004982c : 12056 -> 12064
~ sub_10005d070 -> sub_10005d230 : 632 -> 636
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Yjd3GC/Sources/apfs_executables/fscommon/purging.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Yjd3GC/Sources/apfs_executables/nx/jobj.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Yjd3GC/Sources/apfs_executables/nx/jobj_snap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Yjd3GC/Sources/apfs_executables/nx/obj.c"
+ "2811.160.7.0.4"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7XiiiP/Sources/apfs_executables/fscommon/purging.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7XiiiP/Sources/apfs_executables/nx/jobj.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7XiiiP/Sources/apfs_executables/nx/jobj_snap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7XiiiP/Sources/apfs_executables/nx/obj.c"
- "2811.160.6"
```
