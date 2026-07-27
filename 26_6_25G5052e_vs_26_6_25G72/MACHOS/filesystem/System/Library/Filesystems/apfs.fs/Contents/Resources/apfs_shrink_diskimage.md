## apfs_shrink_diskimage

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_shrink_diskimage`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.6.0.0
-  __TEXT.__text: 0x597d8
+2811.160.7.0.4
+  __TEXT.__text: 0x599a0
   __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__cstring: 0x130a9
+  __TEXT.__cstring: 0x13184
   __TEXT.__const: 0x250
   __TEXT.__unwind_info: 0x930
   __DATA_CONST.__auth_got: 0x3f0

   - /usr/lib/libutil.dylib
   Functions: 761
   Symbols:   140
-  CStrings:  1512
+  CStrings:  1515
 
Functions:
~ sub_100028cfc : 484 -> 488
~ sub_10002adbc -> sub_10002adc0 : 1192 -> 1632
~ sub_100033848 -> sub_100033a04 : 12056 -> 12064
~ sub_100045b64 -> sub_100045d28 : 632 -> 636
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Yjd3GC/Sources/apfs_executables/nx/jobj.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Yjd3GC/Sources/apfs_executables/nx/nx.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Yjd3GC/Sources/apfs_executables/nx/obj.c"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7XiiiP/Sources/apfs_executables/nx/jobj.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7XiiiP/Sources/apfs_executables/nx/nx.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7XiiiP/Sources/apfs_executables/nx/obj.c"
```
