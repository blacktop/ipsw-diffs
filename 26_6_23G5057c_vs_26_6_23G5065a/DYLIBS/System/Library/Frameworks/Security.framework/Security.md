## Security

> `/System/Library/Frameworks/Security.framework/Security`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__dof_codesign`
- `__TEXT.__dof_security_`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-  __TEXT.__text: 0x180d68
+  __TEXT.__text: 0x180e38
   __TEXT.__auth_stubs: 0x3fa0
   __TEXT.__delay_helper: 0x340
   __TEXT.__objc_methlist: 0x642c
-  __TEXT.__const: 0xe2f0
+  __TEXT.__const: 0xe2e8
   __TEXT.__dlopen_cstrs: 0xbc
   __TEXT.__cstring: 0x18528
   __TEXT.__gcc_except_tab: 0x8b8c
Functions:
~ _cert_contains_marker_extension_value : 616 -> 696
~ _SecPolicyCreateProvoloneFDRSigning : 220 -> 348
```
