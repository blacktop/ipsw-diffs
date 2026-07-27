## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__auth_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-2811.160.6.0.0
-  __TEXT.__text: 0x58a28
+2811.160.7.0.4
+  __TEXT.__text: 0x58bec
   __TEXT.__auth_stubs: 0xdc0
   __TEXT.__const: 0x85b0
-  __TEXT.__cstring: 0xeba4
+  __TEXT.__cstring: 0xec83
   __TEXT.__oslogstring: 0x17be
   __TEXT.__gcc_except_tab: 0x1c
   __TEXT.__unwind_info: 0x9f0

   - /usr/lib/libutil.dylib
   Functions: 940
   Symbols:   1199
-  CStrings:  1471
+  CStrings:  1474
 
Functions:
~ _omap_get : 628 -> 632
~ _nx_check : 12092 -> 12100
~ _nx_reaper_checkpoint_traverse : 1188 -> 1628
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VmfCBL/Sources/apfs_framework/nx/obj.c"
+ "2811.160.7.0.4"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.l0HulH/Sources/apfs_framework/nx/obj.c"
- "2811.160.6"
```
