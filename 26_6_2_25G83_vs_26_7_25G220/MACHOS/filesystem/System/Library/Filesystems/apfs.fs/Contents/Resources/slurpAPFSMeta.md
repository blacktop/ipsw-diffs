## slurpAPFSMeta

> `System/Library/Filesystems/apfs.fs/Contents/Resources/slurpAPFSMeta`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.7.0.4
-  __TEXT.__text: 0x365f8
+2811.160.7.701.3
+  __TEXT.__text: 0x36628
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__cstring: 0x8b6e
+  __TEXT.__cstring: 0x8b80
   __TEXT.__const: 0x1e0
   __TEXT.__unwind_info: 0x680
   __DATA_CONST.__auth_got: 0x418

   - /usr/lib/libSystem.B.dylib
   Functions: 520
   Symbols:   144
-  CStrings:  755
+  CStrings:  756
 
Functions:
~ sub_1000076c8 : 592 -> 640
CStrings:
+ "apfs_sanity_check"
```
