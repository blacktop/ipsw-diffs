## Security

> `/System/Library/Frameworks/Security.framework/Versions/A/Security`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__dof_codesign`
- `__TEXT.__dof_syspolicy`
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
- `__AUTH_CONST.__auth_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-61901.160.42.501.1
-  __TEXT.__text: 0x3534c8
+61901.160.44.0.0
+  __TEXT.__text: 0x353598
   __TEXT.__auth_stubs: 0x4e40
   __TEXT.__delay_helper: 0x264
   __TEXT.__objc_methlist: 0x642c
-  __TEXT.__const: 0x18f48
+  __TEXT.__const: 0x18f40
   __TEXT.__dlopen_cstrs: 0x112
   __TEXT.__cstring: 0x2916c
   __TEXT.__oslogstring: 0x20ff1
Functions:
~ _cert_contains_marker_extension_value : 616 -> 696
~ _SecPolicyCreateProvoloneFDRSigning : 220 -> 348
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ktGQBC/Sources/Security/OSX/libsecurity_transform/lib/SecSignVerifyTransform.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NG4yjK/Sources/Security/OSX/libsecurity_transform/lib/SecSignVerifyTransform.c"
```
