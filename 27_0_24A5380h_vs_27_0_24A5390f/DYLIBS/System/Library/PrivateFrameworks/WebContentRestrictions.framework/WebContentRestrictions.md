## WebContentRestrictions

> `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__oslogstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-67.0.0.0.0
-  __TEXT.__text: 0xf8fc
-  __TEXT.__objc_methlist: 0xf58
+70.0.0.0.0
+  __TEXT.__text: 0xfdcc
+  __TEXT.__objc_methlist: 0xfa0
   __TEXT.__const: 0x5b0
   __TEXT.__cstring: 0x16fc
   __TEXT.__gcc_except_tab: 0x250

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x34
-  __TEXT.__unwind_info: 0x4b8
+  __TEXT.__unwind_info: 0x4d0
   __TEXT.__eh_frame: 0x2a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x550
+  __DATA_CONST.__const: 0x5a0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa60
+  __DATA_CONST.__objc_selrefs: 0xa88
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__got: 0x1d8
   __AUTH_CONST.__const: 0x389
   __AUTH_CONST.__cfstring: 0x19e0
-  __AUTH_CONST.__objc_const: 0x1cf0
+  __AUTH_CONST.__objc_const: 0x1d50
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x5b0
   __AUTH.__objc_data: 0x4a0
   __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0xe4
+  __DATA.__objc_ivar: 0xe8
   __DATA.__data: 0x488
   __DATA.__bss: 0x690
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 443
-  Symbols:   1430
+  Functions: 452
+  Symbols:   1445
   CStrings:  287
 
Symbols:
+ +[WCRBrowserEngineClient _askToBrowsePopoverSourceRectForBounds:safeAreaInsets:isPad:]
+ -[WCRBrowserEngineClient presentingViewController]
+ -[WCRBrowserEngineClient setPresentingViewController:]
+ -[WCRPopoverPresentationControllerDelegate popoverPresentationController:willRepositionPopoverToRect:inView:]
+ -[WCRRemoteAskToViewController hasPasscodeWithCompletion:]
+ GCC_except_table44
+ GCC_except_table50
+ GCC_except_table77
+ GCC_except_table79
+ GCC_except_table81
+ _CGRectGetMidX
+ _OBJC_IVAR_$_WCRBrowserEngineClient._presentingViewController
+ _WCROverridePolicyStringForValue
+ _WCROverridePolicyValueForString
+ ___85-[WCRBrowserEngineClient askToBrowseContextMenu:presentingView:state:withCompletion:]_block_invoke_3
+ ___block_descriptor_64_e8_32s40s48s56bs_e8_v12?0B8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e8_v12?0B8ls32l8s40l8s48l8s56l8s72l8s64l8
+ _objc_msgSend$_askToBrowsePopoverSourceRectForBounds:safeAreaInsets:isPad:
+ _objc_msgSend$hasPasscodeWithCompletion:
+ _objc_msgSend$safeAreaInsets
+ _objc_msgSend$setPresentingViewController:
+ _objc_msgSend$traitCollection
- GCC_except_table43
- GCC_except_table49
- GCC_except_table74
- GCC_except_table76
- GCC_except_table78
- _CGRectGetWidth
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e8_v12?0B8ls32l8s40l8s48l8s72l8s56l8s64l8
CStrings:
+ "%{sensitive}@ -> Not Allowed"
+ "Bloom filter: %{sensitive}@ -> Allowed"
+ "Transitive trust bloom filter: %{sensitive}@ -> Not Allowed"
+ "Transitive trust via authentication sites: %{sensitive}@ -> Allowed"
+ "overridePolicy from DC: %s"
- "overridePolicy from DC: askForPermission"
- "overridePolicy from DC: localApprovalOnly"
- "overridePolicy from DC: notAllowed"
- "overridePolicy from DC: unverifiedAdultLegacyScreenTime"
- "overridePolicy from DC: unverifiedAdultScreenTime"
```
