## tailspind

> `/usr/libexec/tailspind`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

 268.0.0.0.0
-  __TEXT.__text: 0xedfc
+  __TEXT.__text: 0xeec0
   __TEXT.__auth_stubs: 0xcb0
   __TEXT.__objc_stubs: 0xc20
   __TEXT.__objc_methlist: 0x254
   __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x1390
+  __TEXT.__cstring: 0x139c
   __TEXT.__gcc_except_tab: 0x318
-  __TEXT.__oslogstring: 0x2b90
+  __TEXT.__oslogstring: 0x2bdd
   __TEXT.__dlopen_cstrs: 0x5c
   __TEXT.__objc_methname: 0xf20
   __TEXT.__objc_classname: 0x14

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 293
+  Functions: 294
   Symbols:   262
-  CStrings:  526
+  CStrings:  528
 
CStrings:
+ "client %s [%d] requested for tailspin data but was rejected by the allowlist"
+ "hangtracerd"
```
