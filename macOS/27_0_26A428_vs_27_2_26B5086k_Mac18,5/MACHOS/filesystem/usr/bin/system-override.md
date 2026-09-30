## system-override

> `/usr/bin/system-override`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-87.0.3.0.0
-  __TEXT.__text: 0x13698
+87.40.2.0.0
+  __TEXT.__text: 0x136b8
   __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_stubs: 0x960
   __TEXT.__objc_methlist: 0x10c
   __TEXT.__const: 0x129
-  __TEXT.__cstring: 0x2805
+  __TEXT.__cstring: 0x289b
   __TEXT.__gcc_except_tab: 0x19c
   __TEXT.__objc_classname: 0x1d
   __TEXT.__objc_methname: 0x91a

   __TEXT.__oslogstring: 0x1af
   __TEXT.__unwind_info: 0x5a0
   __DATA_CONST.__const: 0x200
-  __DATA_CONST.__cfstring: 0x3a0
+  __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x60

   - /usr/lib/libobjc.A.dylib
   Functions: 502
   Symbols:   146
-  CStrings:  436
+  CStrings:  438
 
Functions:
~ sub_100001120 : 756 -> 788
CStrings:
+ "tcc-dev-mode-modification"
+ "⚠️ Applications may be granted access to your camera, microphone, contacts, and files without showing a consent prompt."
```
