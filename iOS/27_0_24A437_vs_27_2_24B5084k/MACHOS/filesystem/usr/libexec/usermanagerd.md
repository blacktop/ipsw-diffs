## usermanagerd

> `/usr/libexec/usermanagerd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

 490.0.3.0.0
-  __TEXT.__text: 0xad018
+  __TEXT.__text: 0xad160
   __TEXT.__auth_stubs: 0x18d0
   __TEXT.__objc_stubs: 0x22e0
   __TEXT.__objc_methlist: 0x1a78
-  __TEXT.__const: 0x14fc
+  __TEXT.__const: 0x1554
   __TEXT.__gcc_except_tab: 0x161c
   __TEXT.__cstring: 0x76d7
   __TEXT.__objc_classname: 0x37a

   __DATA.__objc_selrefs: 0xd10
   __DATA.__objc_ivar: 0x1e4
   __DATA.__objc_data: 0xa00
-  __DATA.__data: 0x1318
+  __DATA.__data: 0x1340
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 2405
+  Functions: 2404
   Symbols:   469
   CStrings:  3392
 
```
