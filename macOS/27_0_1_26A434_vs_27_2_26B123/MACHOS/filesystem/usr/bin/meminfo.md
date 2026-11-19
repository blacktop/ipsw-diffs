## meminfo

> `/usr/bin/meminfo`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1071.0.1.0.0
-  __TEXT.__text: 0x1355c
-  __TEXT.__auth_stubs: 0x9c0
+1071.40.9.0.0
+  __TEXT.__text: 0x136a8
+  __TEXT.__auth_stubs: 0x9d0
   __TEXT.__objc_stubs: 0x100
   __TEXT.__const: 0x9b4
   __TEXT.__swift5_entry: 0x8

   __TEXT.__eh_frame: 0x4d0
   __DATA_CONST.__const: 0x8c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x4e8
+  __DATA_CONST.__auth_got: 0x4f0
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__auth_ptr: 0x1b8
   __DATA.__objc_selrefs: 0x40

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   Functions: 351
-  Symbols:   271
+  Symbols:   272
   CStrings:  58
 
Symbols:
+ _host_info
Functions:
~ sub_100001748 : 3212 -> 3428
~ sub_100005db8 -> sub_100005e90 : 3516 -> 3584
~ sub_100009e0c -> sub_100009f28 : 108 -> 112
~ sub_10001018c -> sub_1000102ac : 1000 -> 1016
~ sub_100010ed4 -> sub_100011004 : 1256 -> 1284
CStrings:
+ " requires root to expand zones; showing aggregate zone total\n"
- "meminfo: --zones requires root; showing aggregate zone total\n"
```
