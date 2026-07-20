## AppRestrictions

> `/System/Library/PrivateFrameworks/AppRestrictions.framework/AppRestrictions`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__data`

```diff

-19.0.0.0.0
+21.0.0.0.0
   __TEXT.__text: 0x106e4
   __TEXT.__objc_methlist: 0x44c
   __TEXT.__const: 0x948

   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x2b08
   __AUTH_CONST.__auth_got: 0x650
-  __AUTH.__objc_data: 0x158
+  __AUTH.__objc_data: 0x108
   __AUTH.__data: 0xd0
-  __DATA.__data: 0x540
-  __DATA.__bss: 0x1c8
-  __DATA_DIRTY.__objc_data: 0x360
-  __DATA_DIRTY.__data: 0x560
-  __DATA_DIRTY.__bss: 0x510
+  __DATA.__data: 0x4e0
+  __DATA.__bss: 0x148
+  __DATA_DIRTY.__objc_data: 0x3b0
+  __DATA_DIRTY.__data: 0x5b0
+  __DATA_DIRTY.__bss: 0x590
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
```
