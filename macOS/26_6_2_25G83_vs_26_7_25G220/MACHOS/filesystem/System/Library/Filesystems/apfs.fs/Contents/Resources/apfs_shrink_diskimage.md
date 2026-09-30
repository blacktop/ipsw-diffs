## apfs_shrink_diskimage

> `System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_shrink_diskimage`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.7.0.4
-  __TEXT.__text: 0x599a0
+2811.160.7.701.3
+  __TEXT.__text: 0x59a0c
   __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__cstring: 0x13184
+  __TEXT.__cstring: 0x13196
   __TEXT.__const: 0x250
   __TEXT.__unwind_info: 0x930
   __DATA_CONST.__auth_got: 0x3f0

   - /usr/lib/libutil.dylib
   Functions: 761
   Symbols:   140
-  CStrings:  1515
+  CStrings:  1516
 
Functions:
~ sub_100001cbc : 592 -> 640
~ sub_10001092c -> sub_10001095c : 488 -> 524
~ sub_100019bfc -> sub_100019c50 : 500 -> 496
~ sub_100022f0c -> sub_100022f5c : 488 -> 516
CStrings:
+ "apfs_sanity_check"
```
