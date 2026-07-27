## apfs_diskimage_map

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_diskimage_map`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.6.0.0
-  __TEXT.__text: 0x4afec
+2811.160.7.0.4
+  __TEXT.__text: 0x4b1b0
   __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__cstring: 0xeeeb
+  __TEXT.__cstring: 0xefc6
   __TEXT.__const: 0x248
   __TEXT.__unwind_info: 0x850
   __DATA_CONST.__auth_got: 0x3e0

   - /usr/lib/libutil.dylib
   Functions: 678
   Symbols:   138
-  CStrings:  1223
+  CStrings:  1226
 
Functions:
~ sub_100026558 : 1192 -> 1632
~ sub_100028bf4 -> sub_100028dac : 12056 -> 12064
~ sub_10003a878 -> sub_10003aa38 : 632 -> 636
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Yjd3GC/Sources/apfs_executables/nx/jobj_snap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Yjd3GC/Sources/apfs_executables/nx/obj.c"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7XiiiP/Sources/apfs_executables/nx/jobj_snap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7XiiiP/Sources/apfs_executables/nx/obj.c"
```
