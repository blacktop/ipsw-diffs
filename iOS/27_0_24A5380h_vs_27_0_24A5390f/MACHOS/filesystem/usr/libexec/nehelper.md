## nehelper

> `/usr/libexec/nehelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2322.0.0.0.1
-  __TEXT.__text: 0x255e8
+2331.0.0.0.1
+  __TEXT.__text: 0x25624
   __TEXT.__auth_stubs: 0x10b0
   __TEXT.__objc_stubs: 0x2a60
   __TEXT.__objc_methlist: 0x44c
   __TEXT.__const: 0x11c
   __TEXT.__gcc_except_tab: 0x7f8
   __TEXT.__objc_methname: 0x1f9c
-  __TEXT.__cstring: 0x5f44
-  __TEXT.__oslogstring: 0x4a97
+  __TEXT.__cstring: 0x5f37
+  __TEXT.__oslogstring: 0x4ae1
   __TEXT.__objc_classname: 0x190
   __TEXT.__objc_methtype: 0x26e
   __TEXT.__unwind_info: 0x3e8
   __DATA_CONST.__const: 0xd10
-  __DATA_CONST.__cfstring: 0x51a0
+  __DATA_CONST.__cfstring: 0x5180
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
Functions:
~ sub_10001199c : 2152 -> 2312
~ sub_1000147d4 -> sub_100014874 : 8376 -> 8276
CStrings:
+ "%@: not platform entitled and no application ID is set, permission denied"
- "plugin-types"
```
