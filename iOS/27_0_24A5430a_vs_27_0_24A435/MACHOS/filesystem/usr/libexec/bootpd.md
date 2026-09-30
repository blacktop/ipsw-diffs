## bootpd

> `/usr/libexec/bootpd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

 557.0.0.0.0
-  __TEXT.__text: 0x11288
+  __TEXT.__text: 0x1128c
   __TEXT.__auth_stubs: 0x970
   __TEXT.__const: 0xe8
   __TEXT.__cstring: 0x1f14
Functions:
~ sub_10000d0f4 : 188 -> 192
```
