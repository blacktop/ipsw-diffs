## apfs_checkseal

> `System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_checkseal`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.7.0.4
-  __TEXT.__text: 0x4f008
+2811.160.7.701.3
+  __TEXT.__text: 0x4f088
   __TEXT.__auth_stubs: 0x790
   __TEXT.__const: 0x4f0
-  __TEXT.__cstring: 0x102ab
+  __TEXT.__cstring: 0x102bd
   __TEXT.__unwind_info: 0x8e0
   __DATA_CONST.__auth_got: 0x3c8
   __DATA_CONST.__got: 0x50

   - /usr/lib/libutil.dylib
   Functions: 732
   Symbols:   136
-  CStrings:  1301
+  CStrings:  1302
 
Functions:
~ sub_100004bdc : 592 -> 640
~ sub_100013ea0 -> sub_100013ed0 : 488 -> 524
~ sub_10001cf9c -> sub_10001cff0 : 500 -> 496
~ sub_100024538 -> sub_100024588 : 488 -> 516
~ sub_10003eee4 -> sub_10003ef50 : 1248 -> 1268
CStrings:
+ "apfs_sanity_check"
```
