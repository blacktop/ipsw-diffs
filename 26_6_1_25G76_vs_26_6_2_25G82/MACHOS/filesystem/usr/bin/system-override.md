## system-override

> `/usr/bin/system-override`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

 85.0.0.0.0
-  __TEXT.__text: 0x13ebc
+  __TEXT.__text: 0x13f20
   __TEXT.__auth_stubs: 0x630
   __TEXT.__objc_stubs: 0x960
   __TEXT.__objc_methlist: 0x10c

   - /System/Library/PrivateFrameworks/SystemOverride.framework/Versions/A/SystemOverride
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 505
+  Functions: 504
   Symbols:   144
   CStrings:  435
 
```
