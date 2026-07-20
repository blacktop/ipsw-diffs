## apfs_iosd

> `/System/Library/Filesystems/apfs.fs/apfs_iosd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3283.0.9.502.1
-  __TEXT.__text: 0x33cf0
+3283.0.13.0.0
+  __TEXT.__text: 0x33d38
   __TEXT.__auth_stubs: 0xa90
   __TEXT.__const: 0x350
-  __TEXT.__cstring: 0x679d
+  __TEXT.__cstring: 0x67af
   __TEXT.__oslogstring: 0x13e0
   __TEXT.__unwind_info: 0x650
   __DATA_CONST.__const: 0x708

   - /usr/lib/libutil.dylib
   Functions: 562
   Symbols:   197
-  CStrings:  751
+  CStrings:  752
 
Functions:
~ sub_100006ff4 : 596 -> 640
~ sub_1000173a8 -> sub_1000173d4 : 520 -> 508
~ sub_100026554 -> sub_100026574 : 632 -> 636
~ sub_10002a868 -> sub_10002a88c : 4156 -> 4168
~ sub_10002bc18 -> sub_10002bc48 : 3496 -> 3520
CStrings:
+ "apfs_sanity_check"
```
