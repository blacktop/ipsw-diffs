## nvram

> `/usr/sbin/nvram`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

-1070.0.0.0.0
+1071.0.1.0.0
   __TEXT.__text: 0x21b4
   __TEXT.__auth_stubs: 0x470
-  __TEXT.__const: 0x40
+  __TEXT.__const: 0x48
   __TEXT.__cstring: 0x9fa
   __TEXT.__unwind_info: 0xd0
   __DATA_CONST.__const: 0x20
```
