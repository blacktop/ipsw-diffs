## DynamicPrefetching

> `/System/Library/PrivateFrameworks/DynamicPrefetching.framework/DynamicPrefetching`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__objc_data`

```diff

   __AUTH_CONST.__auth_got: 0x3f0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0xe8
+  __DATA.__data: 0xe0
   __DATA.__bss: 0x248
-  __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
```
