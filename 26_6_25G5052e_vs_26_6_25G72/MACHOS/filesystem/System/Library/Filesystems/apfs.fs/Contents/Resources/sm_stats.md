## sm_stats

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/sm_stats`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.6.0.0
-  __TEXT.__text: 0x42f60
+2811.160.7.0.4
+  __TEXT.__text: 0x4312c
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__cstring: 0xcc9c
+  __TEXT.__cstring: 0xcd77
   __TEXT.__const: 0x1e8
   __TEXT.__unwind_info: 0x6f0
   __DATA_CONST.__auth_got: 0x390

   - /usr/lib/libutil.dylib
   Functions: 577
   Symbols:   129
-  CStrings:  1045
+  CStrings:  1048
 
Functions:
~ sub_100005244 : 1192 -> 1632
~ sub_10002664c -> sub_100026804 : 500 -> 508
~ sub_10002c058 -> sub_10002c218 : 12056 -> 12064
~ sub_10003db70 -> sub_10003dd38 : 632 -> 636
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Yjd3GC/Sources/apfs_executables/nx/obj.c"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7XiiiP/Sources/apfs_executables/nx/obj.c"
```
