## pkgutil

> `/usr/sbin/pkgutil`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`

```diff

-881.0.0.0.0
-  __TEXT.__text: 0x5188
-  __TEXT.__auth_stubs: 0x560
+883.0.0.0.0
+  __TEXT.__text: 0x51a0
+  __TEXT.__auth_stubs: 0x570
   __TEXT.__objc_stubs: 0xec0
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__cstring: 0x1f6e
+  __TEXT.__cstring: 0x1f8e
   __TEXT.__objc_methname: 0x9b3
   __TEXT.__unwind_info: 0xf8
   __DATA_CONST.__const: 0x560
   __DATA_CONST.__cfstring: 0x4a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x2c0
+  __DATA_CONST.__auth_got: 0x2c8
   __DATA_CONST.__got: 0x178
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_selrefs: 0x3b0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxar.1.dylib
   Functions: 39
-  Symbols:   140
-  CStrings:  364
+  Symbols:   141
+  CStrings:  365
 
Symbols:
+ _xar_get_safe_path
Functions:
~ sub_100002d74 : 980 -> 1004
CStrings:
+ "Skipping entry with unsafe name"
```
