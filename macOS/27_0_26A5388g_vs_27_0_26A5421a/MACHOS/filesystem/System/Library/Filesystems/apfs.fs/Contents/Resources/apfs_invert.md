## apfs_invert

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_invert`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3283.0.13.501.1
-  __TEXT.__text: 0x52558
+3288.1.3.0.0
+  __TEXT.__text: 0x52598
   __TEXT.__auth_stubs: 0x800
-  __TEXT.__cstring: 0x10fba
+  __TEXT.__cstring: 0x10fb3
   __TEXT.__const: 0x8418
   __TEXT.__unwind_info: 0x928
   __DATA_CONST.__const: 0x838
Functions:
~ sub_10001ff18 : 492 -> 520
~ sub_100031e20 -> sub_100031e3c : 488 -> 524
CStrings:
+ "3288.1.3"
- "3283.0.13.501.1"
```
