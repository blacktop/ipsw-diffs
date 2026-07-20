## Vista

> `/System/Library/PrivateFrameworks/Vista.framework/Vista`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`

```diff

-19.0.0.0.0
+20.0.0.0.0
   __TEXT.__text: 0x826c8
   __TEXT.__objc_methlist: 0x35a4
   __TEXT.__const: 0x1590

   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__auth_got: 0x5f8
-  __AUTH.__objc_data: 0x1770
   __DATA.__objc_ivar: 0x4e0
   __DATA.__data: 0x180
   __DATA.__bss: 0x2f0
+  __DATA_DIRTY.__objc_data: 0x1770
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
```
