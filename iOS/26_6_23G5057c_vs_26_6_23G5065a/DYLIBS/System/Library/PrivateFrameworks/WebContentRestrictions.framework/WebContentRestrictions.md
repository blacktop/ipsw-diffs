## WebContentRestrictions

> `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-  __TEXT.__text: 0xbb10
+  __TEXT.__text: 0xb810
   __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_methlist: 0x7e8
+  __TEXT.__objc_methlist: 0x7e0
   __TEXT.__const: 0x560
-  __TEXT.__cstring: 0x129c
+  __TEXT.__cstring: 0x121c
   __TEXT.__gcc_except_tab: 0xcc
   __TEXT.__oslogstring: 0x1b3
   __TEXT.__swift5_typeref: 0x10c

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x34
-  __TEXT.__unwind_info: 0x3e8
+  __TEXT.__unwind_info: 0x3e0
   __TEXT.__eh_frame: 0x378
   __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methname: 0x1b38
+  __TEXT.__objc_methname: 0x1af8
   __TEXT.__objc_methtype: 0x2f4
-  __TEXT.__objc_stubs: 0x17e0
+  __TEXT.__objc_stubs: 0x17c0
   __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x400
+  __DATA_CONST.__const: 0x3b0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e0
+  __DATA_CONST.__objc_selrefs: 0x6d8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__auth_got: 0x548
   __AUTH_CONST.__const: 0x389
-  __AUTH_CONST.__cfstring: 0x12e0
+  __AUTH_CONST.__cfstring: 0x12a0
   __AUTH_CONST.__objc_const: 0xd28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 312
-  Symbols:   1081
-  CStrings:  528
+  Functions: 309
+  Symbols:   1075
+  CStrings:  525
 
Symbols:
- -[WCRBrowserEngineClient _requestOpenScreenTimeSettingsForAgeVerificationWithCompletion:]
- ___89-[WCRBrowserEngineClient _requestOpenScreenTimeSettingsForAgeVerificationWithCompletion:]_block_invoke
- ___89-[WCRBrowserEngineClient _requestOpenScreenTimeSettingsForAgeVerificationWithCompletion:]_block_invoke_2
- ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_40_e8_32bs_e45_v24?0"_UIRemoteViewController"8"NSError"16ls32l8
- _objc_msgSend$_requestOpenScreenTimeSettingsForAgeVerificationWithCompletion:
CStrings:
- "Failed to connect to WCRUI for age verification Settings navigation: %@"
- "Failed to open Screen Time Settings for age verification: %@"
- "_requestOpenScreenTimeSettingsForAgeVerificationWithCompletion:"
```
