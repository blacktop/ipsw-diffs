## apfs_prepare_cryptex

> `System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_prepare_cryptex`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.7.0.4
-  __TEXT.__text: 0x6e418
+2811.160.7.701.3
+  __TEXT.__text: 0x6e498
   __TEXT.__auth_stubs: 0x840
   __TEXT.__const: 0xc51a
-  __TEXT.__cstring: 0x181e3
+  __TEXT.__cstring: 0x181f7
   __TEXT.__unwind_info: 0xc48
   __DATA_CONST.__auth_got: 0x420
   __DATA_CONST.__got: 0x58

   - /usr/lib/libutil.dylib
   Functions: 1000
   Symbols:   148
-  CStrings:  2079
+  CStrings:  2080
 
Functions:
~ sub_100010064 : 592 -> 640
~ sub_10001f76c -> sub_10001f79c : 488 -> 524
~ sub_100029c64 -> sub_100029cb8 : 508 -> 504
~ sub_1000355ec -> sub_10003563c : 488 -> 516
~ sub_10005ddcc -> sub_10005de38 : 1248 -> 1268
CStrings:
+ "2811.160.7.701.3"
+ "apfs_sanity_check"
- "2811.160.7.0.4"
```
