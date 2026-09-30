## SetupKit

> `/System/Library/PrivateFrameworks/SetupKit.framework/SetupKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-900.48.0.0.0
+900.55.0.0.0
   __TEXT.__text: 0x28f54
   __TEXT.__objc_methlist: 0x2378
   __TEXT.__const: 0x1d2

   __TEXT.__gcc_except_tab: 0xeec
   __TEXT.__cstring: 0x762e
   __TEXT.__oslogstring: 0x113
-  __TEXT.__unwind_info: 0xa28
+  __TEXT.__unwind_info: 0xa18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xaa0
   __AUTH.__data: 0x20
   __DATA.__objc_ivar: 0x4a0
   __DATA.__data: 0xc90
   __DATA.__bss: 0x68
+  __DATA_DIRTY.__objc_data: 0xaa0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
```
