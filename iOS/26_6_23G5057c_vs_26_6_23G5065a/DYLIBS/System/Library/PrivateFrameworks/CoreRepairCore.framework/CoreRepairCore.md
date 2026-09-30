## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
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
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-  __TEXT.__text: 0x8ef78
+  __TEXT.__text: 0x8f00c
   __TEXT.__auth_stubs: 0x1660
   __TEXT.__objc_methlist: 0x3ecc
   __TEXT.__const: 0x848
   __TEXT.__oslogstring: 0x9810
   __TEXT.__cstring: 0x60d2
-  __TEXT.__gcc_except_tab: 0x1824
+  __TEXT.__gcc_except_tab: 0x183c
   __TEXT.__unwind_info: 0x15f8
   __TEXT.__objc_classname: 0x8af
   __TEXT.__objc_methname: 0x878f
Functions:
~ -[CRCAttestationManager sendChallengeRequestWith:requestID:serverResponse:error:] : 1900 -> 1980
~ -[CRCAttestationManager sendCertIssueRequestWith:requestID:serverCertResponse:error:] : 1612 -> 1680
```
