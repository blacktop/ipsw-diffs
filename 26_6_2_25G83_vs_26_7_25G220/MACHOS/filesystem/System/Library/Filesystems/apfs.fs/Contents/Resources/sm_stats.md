## sm_stats

> `System/Library/Filesystems/apfs.fs/Contents/Resources/sm_stats`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.7.0.4
-  __TEXT.__text: 0x4312c
+2811.160.7.701.3
+  __TEXT.__text: 0x4315c
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__cstring: 0xcd77
+  __TEXT.__cstring: 0xcd89
   __TEXT.__const: 0x1e8
   __TEXT.__unwind_info: 0x6f0
   __DATA_CONST.__auth_got: 0x390

   - /usr/lib/libutil.dylib
   Functions: 577
   Symbols:   129
-  CStrings:  1048
+  CStrings:  1049
 
Functions:
~ sub_1000142a8 : 592 -> 640
CStrings:
+ "apfs_sanity_check"
```
