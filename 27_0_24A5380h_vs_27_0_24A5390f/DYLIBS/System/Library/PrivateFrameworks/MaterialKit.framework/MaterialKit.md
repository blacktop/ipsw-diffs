## MaterialKit

> `/System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__DATA.__data`

```diff

-223.0.0.0.0
-  __TEXT.__text: 0xe580
+224.0.0.0.0
+  __TEXT.__text: 0xe578
   __TEXT.__objc_methlist: 0x161c
   __TEXT.__const: 0x250
   __TEXT.__cstring: 0xf23

   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0x138
   __DATA.__data: 0x428
   __DATA.__bss: 0x50
-  __DATA_DIRTY.__objc_data: 0x280
+  __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0x20
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 490
-  Symbols:   1466
+  Symbols:   1468
   CStrings:  204
 
Symbols:
+ __UIClamp
+ __UILerp
Functions:
~ -[MTMaterialView setWeighting:] : 216 -> 224
~ ___40-[MTMaterialView _setupAlphaTransformer]_block_invoke.77 : 48 -> 32
```
