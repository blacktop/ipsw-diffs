## ktrace

> `/usr/bin/ktrace`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-706.0.2.0.0
-  __TEXT.__text: 0x80a0
+706.40.5.0.0
+  __TEXT.__text: 0x80ac
   __TEXT.__auth_stubs: 0x1010
   __TEXT.__objc_stubs: 0x20
   __TEXT.__const: 0xd0
Functions:
~ sub_100005a08 : 1504 -> 1516
```
