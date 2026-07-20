## Anvil

> `/System/Library/PrivateFrameworks/Anvil.framework/Versions/A/Anvil`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`

```diff

-107.0.0.0.0
+108.0.0.0.0
   __TEXT.__text: 0x123ebc
   __TEXT.__objc_methlist: 0x33c
   __TEXT.__const: 0x10190

   __AUTH_CONST.__const: 0xb6e1
   __AUTH_CONST.__objc_const: 0x1278
   __AUTH_CONST.__auth_got: 0x1828
-  __AUTH.__objc_data: 0x300
-  __AUTH.__data: 0x19d0
-  __DATA.__data: 0x2858
+  __AUTH.__objc_data: 0x90
+  __AUTH.__data: 0xfe0
+  __DATA.__data: 0x27e0
   __DATA.__bss: 0x1d170
-  __DATA.__common: 0xb8
-  __DATA_DIRTY.__data: 0x869
+  __DATA.__common: 0xa8
+  __DATA_DIRTY.__objc_data: 0x270
+  __DATA_DIRTY.__data: 0x12e0
   __DATA_DIRTY.__bss: 0x180
-  __DATA_DIRTY.__common: 0xa9
+  __DATA_DIRTY.__common: 0xb9
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/Versions/A/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
```
