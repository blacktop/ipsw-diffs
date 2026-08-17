## apfs_diskimage_map

> `System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_diskimage_map`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.7.0.4
-  __TEXT.__text: 0x4b1b0
+2811.160.7.701.3
+  __TEXT.__text: 0x4b1f4
   __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__cstring: 0xefc6
+  __TEXT.__cstring: 0xefd8
   __TEXT.__const: 0x248
   __TEXT.__unwind_info: 0x850
   __DATA_CONST.__auth_got: 0x3e0

   - /usr/lib/libutil.dylib
   Functions: 678
   Symbols:   138
-  CStrings:  1226
+  CStrings:  1227
 
Functions:
~ sub_1000026f0 : 592 -> 640
~ sub_10003b538 -> sub_10003b568 : 1248 -> 1268
CStrings:
+ "apfs_sanity_check"
```
