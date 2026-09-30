## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3283.0.9.502.1
-  __TEXT.__text: 0x5a594
+3283.0.13.0.0
+  __TEXT.__text: 0x5a7a8
   __TEXT.__auth_stubs: 0xa10
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x750
-  __TEXT.__cstring: 0x11f54
+  __TEXT.__cstring: 0x1203d
   __TEXT.__gcc_except_tab: 0x6a4
   __TEXT.__unwind_info: 0xcb0
   __DATA_CONST.__const: 0xb20

   - /usr/lib/libutil.dylib
   Functions: 906
   Symbols:   187
-  CStrings:  1610
+  CStrings:  1614
 
Functions:
~ sub_10001974c : 596 -> 640
~ sub_1000312a4 -> sub_1000312d0 : 508 -> 512
~ sub_10003e180 -> sub_10003e1b0 : 1204 -> 1640
~ sub_100040850 -> sub_100040a34 : 10472 -> 10480
~ sub_10004956c -> sub_100049758 : 632 -> 636
~ sub_10004e730 -> sub_10004e920 : 4156 -> 4168
~ sub_10004fae0 -> sub_10004fcdc : 3496 -> 3520
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "%s:%d: obj is NULL or not apfs object!\n"
+ "3283.0.13"
+ "apfs_sanity_check"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "%s:%d: obj is NULL or not apfs object!"
- "3283.0.9.502.1"
```
