## newfs_apfs

> `System/Library/Filesystems/apfs.fs/Contents/Resources/newfs_apfs`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.7.0.4
-  __TEXT.__text: 0x5461c
+2811.160.7.701.3
+  __TEXT.__text: 0x5468c
   __TEXT.__auth_stubs: 0x900
-  __TEXT.__cstring: 0x10821
+  __TEXT.__cstring: 0x10835
   __TEXT.__const: 0x84c1
   __TEXT.__oslogstring: 0x125
   __TEXT.__unwind_info: 0x8d0

   - /usr/lib/libutil.dylib
   Functions: 806
   Symbols:   161
-  CStrings:  1405
+  CStrings:  1406
 
Functions:
~ sub_1000189ec : 488 -> 516
~ sub_100026ddc -> sub_100026df8 : 488 -> 524
~ sub_10002e8fc -> sub_10002e93c : 592 -> 640
CStrings:
+ "2811.160.7.701.3"
+ "apfs_sanity_check"
- "2811.160.7.0.4"
```
