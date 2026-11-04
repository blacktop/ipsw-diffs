## nehelper

> `/usr/libexec/nehelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2365.40.3.0.2
-  __TEXT.__text: 0x262f4
+2365.60.12.0.0
+  __TEXT.__text: 0x26430
   __TEXT.__auth_stubs: 0x10c0
   __TEXT.__objc_stubs: 0x2aa0
   __TEXT.__objc_methlist: 0x44c
   __TEXT.__const: 0x11c
   __TEXT.__gcc_except_tab: 0x894
   __TEXT.__objc_methname: 0x1fed
-  __TEXT.__cstring: 0x606f
-  __TEXT.__oslogstring: 0x4d0a
+  __TEXT.__cstring: 0x6082
+  __TEXT.__oslogstring: 0x4d38
   __TEXT.__objc_classname: 0x190
   __TEXT.__objc_methtype: 0x26e
   __TEXT.__unwind_info: 0x4d8
   __DATA_CONST.__const: 0xd90
-  __DATA_CONST.__cfstring: 0x51e0
+  __DATA_CONST.__cfstring: 0x5200
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__objc_arraydata: 0x1350
-  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA_CONST.__objc_arraydata: 0x1358
+  __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__auth_got: 0x870
   __DATA_CONST.__got: 0x3c0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 254
+  Functions: 255
   Symbols:   384
-  CStrings:  1725
+  CStrings:  1727
 
CStrings:
+ "Removing rule for %@, not allowed in the list"
+ "com.apple.rapportd"
```
