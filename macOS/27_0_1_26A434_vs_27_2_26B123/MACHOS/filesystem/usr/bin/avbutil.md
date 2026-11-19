## avbutil

> `/usr/bin/avbutil`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__data`

```diff

-1500.16.0.0.0
+1510.1.0.0.0
   __TEXT.__text: 0x14c94
   __TEXT.__auth_stubs: 0x2e0
   __TEXT.__objc_stubs: 0x17e0
   __TEXT.__objc_methlist: 0x78c
   __TEXT.__objc_methname: 0x159d
-  __TEXT.__cstring: 0x4415
+  __TEXT.__cstring: 0x4414
   __TEXT.__objc_classname: 0x117
   __TEXT.__objc_methtype: 0x54f
   __TEXT.__const: 0x10
CStrings:
+ "1510.1"
- "1500.16"
```
