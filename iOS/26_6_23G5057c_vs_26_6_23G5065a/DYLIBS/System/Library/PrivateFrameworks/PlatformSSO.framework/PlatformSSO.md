## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
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
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-  __TEXT.__text: 0x5bcf8
+  __TEXT.__text: 0x5bd28
   __TEXT.__auth_stubs: 0xe00
   __TEXT.__objc_methlist: 0x331c
   __TEXT.__const: 0x2e2
   __TEXT.__cstring: 0x7e96
-  __TEXT.__oslogstring: 0x22c1
+  __TEXT.__oslogstring: 0x22e1
   __TEXT.__gcc_except_tab: 0x1550
   __TEXT.__dlopen_cstrs: 0x110
   __TEXT.__swift5_typeref: 0xc2
Functions:
~ -[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:] : 2684 -> 2696
~ -[POAgentAuthenticationProcess _handleConfigurationChanged:startup:] : 2412 -> 2448
CStrings:
+ "User state is needs registration, key is invalid, or new user pending registration"
- "User state is needs registration or key is invalid"
```
