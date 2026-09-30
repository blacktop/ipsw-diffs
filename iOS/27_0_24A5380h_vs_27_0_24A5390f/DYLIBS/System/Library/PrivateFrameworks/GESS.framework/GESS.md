## GESS

> `/System/Library/PrivateFrameworks/GESS.framework/GESS`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__data`
- `__AUTH.__thread_vars`
- `__DATA.__data`

```diff

   __TEXT.__gcc_except_tab: 0x4fa90
   __TEXT.__cstring: 0x95a6d
   __TEXT.__oslogstring: 0x2e1
-  __TEXT.__unwind_info: 0x13bf8
+  __TEXT.__unwind_info: 0x13bf0
   __TEXT.__eh_frame: 0x490
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__objc_const: 0x47c0
   __AUTH_CONST.__weak_auth_got: 0x38
   __AUTH_CONST.__auth_got: 0xae0
-  __AUTH.__objc_data: 0x1360
   __AUTH.__data: 0x8
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_data: 0x8

   __DATA.__data: 0x1f8
   __DATA.__bss: 0x64f1
   __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0x1360
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
```
