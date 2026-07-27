## libspindump.dylib

> `/usr/lib/libspindump.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`

```diff

 419.11.0.0.0
-  __TEXT.__text: 0x464c
+  __TEXT.__text: 0x4648
   __TEXT.__auth_stubs: 0x3f0
   __TEXT.__const: 0xc0
   __TEXT.__cstring: 0x4ca
Functions:
~ ___SPNotifyLeavingFullWake_block_invoke : 44 -> 40
```
