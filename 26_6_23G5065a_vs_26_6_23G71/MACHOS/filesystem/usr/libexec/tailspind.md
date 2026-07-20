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

 250.2.0.0.0
-  __TEXT.__text: 0xda30
+  __TEXT.__text: 0xd958
   __TEXT.__auth_stubs: 0xbd0
   __TEXT.__objc_stubs: 0x960
   __TEXT.__objc_methlist: 0x1f4
   __TEXT.__const: 0x134
-  __TEXT.__cstring: 0x10c1
+  __TEXT.__cstring: 0x10b5
   __TEXT.__objc_methname: 0xc42
-  __TEXT.__oslogstring: 0x27e5
+  __TEXT.__oslogstring: 0x2798
   __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methtype: 0xfb
   __TEXT.__gcc_except_tab: 0x238

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 263
+  Functions: 262
   Symbols:   243
-  CStrings:  444
+  CStrings:  442
 
CStrings:
- "client %s [%d] requested for tailspin data but was rejected by the allowlist"
- "hangtracerd"
```
