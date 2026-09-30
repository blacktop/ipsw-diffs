## avbdiagnose

> `/usr/bin/avbdiagnose`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-1500.16.0.0.0
+1510.1.0.0.0
   __TEXT.__text: 0x6af0
   __TEXT.__auth_stubs: 0x200
   __TEXT.__objc_stubs: 0x18a0
   __TEXT.__objc_methlist: 0x134
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x2520
+  __TEXT.__cstring: 0x251f
   __TEXT.__objc_methname: 0xf79
   __TEXT.__objc_classname: 0x2a
   __TEXT.__objc_methtype: 0xba
CStrings:
+ "1510.1"
- "1500.16"
```
