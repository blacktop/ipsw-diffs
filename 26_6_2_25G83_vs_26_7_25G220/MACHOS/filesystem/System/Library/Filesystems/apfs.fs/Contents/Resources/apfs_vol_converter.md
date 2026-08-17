## apfs_vol_converter

> `System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_vol_converter`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.7.0.4
-  __TEXT.__text: 0x59998
+2811.160.7.701.3
+  __TEXT.__text: 0x59a28
   __TEXT.__auth_stubs: 0xa50
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0xc20
-  __TEXT.__cstring: 0x123c0
+  __TEXT.__cstring: 0x123d4
   __TEXT.__gcc_except_tab: 0x698
   __TEXT.__unwind_info: 0xc38
   __DATA_CONST.__auth_got: 0x530

   - /usr/lib/libutil.dylib
   Functions: 881
   Symbols:   190
-  CStrings:  1626
+  CStrings:  1627
 
Functions:
~ sub_100019084 : 592 -> 640
~ sub_100028398 -> sub_1000283c8 : 488 -> 524
~ sub_1000309e0 -> sub_100030a34 : 496 -> 508
~ sub_100037e7c -> sub_100037edc : 488 -> 516
~ sub_100049a24 -> sub_100049aa0 : 1248 -> 1268
CStrings:
+ "2811.160.7.701.3"
+ "apfs_sanity_check"
- "2811.160.7.0.4"
```
