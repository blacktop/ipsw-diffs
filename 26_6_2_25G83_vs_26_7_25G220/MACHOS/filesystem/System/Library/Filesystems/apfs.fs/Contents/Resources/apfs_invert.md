## apfs_invert

> `System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_invert`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.7.0.4
-  __TEXT.__text: 0x51638
+2811.160.7.701.3
+  __TEXT.__text: 0x516c8
   __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__cstring: 0x10e9e
+  __TEXT.__cstring: 0x10eb2
   __TEXT.__const: 0x8440
   __TEXT.__unwind_info: 0x8f8
   __DATA_CONST.__auth_got: 0x3f8

   - /usr/lib/libutil.dylib
   Functions: 734
   Symbols:   142
-  CStrings:  1395
+  CStrings:  1396
 
Functions:
~ sub_100000b44 : 1248 -> 1268
~ sub_100013074 -> sub_100013088 : 592 -> 640
~ sub_10001e16c -> sub_10001e1b0 : 488 -> 516
~ sub_10002ff20 -> sub_10002ff80 : 488 -> 524
~ sub_100036ab4 -> sub_100036b38 : 252 -> 264
CStrings:
+ "2811.160.7.701.3"
+ "apfs_sanity_check"
- "2811.160.7.0.4"
```
