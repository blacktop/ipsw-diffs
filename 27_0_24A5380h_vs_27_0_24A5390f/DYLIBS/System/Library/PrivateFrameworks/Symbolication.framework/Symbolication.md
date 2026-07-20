## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
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
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__thread_vars`
- `__DATA.__data`

```diff

   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0x10d8
-  __AUTH.__objc_data: 0x1238
-  __AUTH.__data: 0x28
+  __AUTH.__objc_data: 0x680
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0xd9c
   __DATA.__data: 0xd18
   __DATA.__bss: 0x610
-  __DATA.__common: 0x108
-  __DATA_DIRTY.__objc_data: 0xc08
-  __DATA_DIRTY.__data: 0x28
+  __DATA.__common: 0x101
+  __DATA_DIRTY.__objc_data: 0x17c0
+  __DATA_DIRTY.__data: 0x50
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
```
