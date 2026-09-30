## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-3283.0.9.501.1
-  __TEXT.__text: 0x56e28
+3283.0.13.501.1
+  __TEXT.__text: 0x57140
   __TEXT.__const: 0x8540
-  __TEXT.__cstring: 0xe9f3
+  __TEXT.__cstring: 0xeae1
   __TEXT.__oslogstring: 0x1467
   __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__unwind_info: 0xa38
+  __TEXT.__unwind_info: 0xa30
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x528
   __DATA_CONST.__got: 0x0

   - /usr/lib/libutil.dylib
   Functions: 930
   Symbols:   1173
-  CStrings:  1444
+  CStrings:  1448
 
Functions:
~ _omap_get : 628 -> 632
~ _spaceman_alloc : 4148 -> 4160
~ _spaceman_alloc_iterate_chunks : 3472 -> 3500
~ _APFSCaptureCreatePreallocFile : 316 -> 408
~ _growCaptureFile : 260 -> 304
~ _APFSCaptureExtendPreallocSizeForFile : 100 -> 212
~ _APFSCaptureSetPreallocSizeForFile : 344 -> 356
~ _nx_check : 10472 -> 10480
~ _apfs_init : 596 -> 640
~ _nx_reaper_checkpoint_traverse : 1200 -> 1636
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t9k12f/Sources/apfs_framework/nx/obj.c"
+ "3283.0.13.501.1"
+ "apfs_sanity_check"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CAjzV9/Sources/apfs_framework/nx/obj.c"
- "3283.0.9.501.1"
```
