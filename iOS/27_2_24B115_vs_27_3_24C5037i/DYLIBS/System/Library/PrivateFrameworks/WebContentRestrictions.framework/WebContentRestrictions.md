## WebContentRestrictions

> `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions`

```diff

-75.0.0.0.0
-  __TEXT.__text: 0x10480
-  __TEXT.__objc_methlist: 0xfe0
+79.0.0.0.0
+  __TEXT.__text: 0x109a0
+  __TEXT.__objc_methlist: 0x1050
   __TEXT.__const: 0x5c0
-  __TEXT.__cstring: 0x180c
+  __TEXT.__cstring: 0x18dc
   __TEXT.__gcc_except_tab: 0x250
-  __TEXT.__oslogstring: 0x803
+  __TEXT.__oslogstring: 0x883
   __TEXT.__ustring: 0x1bc
   __TEXT.__swift5_typeref: 0x102
   __TEXT.__constg_swiftt: 0x220

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x34
-  __TEXT.__unwind_info: 0x600
+  __TEXT.__unwind_info: 0x618
   __TEXT.__eh_frame: 0x2b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad8
+  __DATA_CONST.__objc_selrefs: 0xb28
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__got: 0x1e0
-  __AUTH_CONST.__const: 0x3a9
-  __AUTH_CONST.__cfstring: 0x1b80
-  __AUTH_CONST.__objc_const: 0x1d50
+  __AUTH_CONST.__const: 0x389
+  __AUTH_CONST.__cfstring: 0x1ca0
+  __AUTH_CONST.__objc_const: 0x1de0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__auth_got: 0x5b0
+  __AUTH_CONST.__auth_got: 0x5b8
   __AUTH.__objc_data: 0x4a0
   __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0xe8
+  __DATA.__objc_ivar: 0xf4
   __DATA.__data: 0x488
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 461
-  Symbols:   1192
-  CStrings:  301
+  Functions: 470
+  Symbols:   1205
+  CStrings:  313
 
Symbols:
+ -[WCRBrowserEngineClient _allowListPINEntryWentAwayUnobserved]
+ -[WCRBrowserEngineClient _failAllowListAuthentication:withError:completion:]
+ -[WCRBrowserEngineClient _finishAllowListAuthentication:]
+ -[WCRBrowserEngineClient allowListAuthenticationInFlight]
+ -[WCRBrowserEngineClient allowListPINEntryPresented]
+ -[WCRBrowserEngineClient presentedAllowListPINEntryViewController]
+ -[WCRBrowserEngineClient setAllowListAuthenticationInFlight:]
+ -[WCRBrowserEngineClient setAllowListPINEntryPresented:]
+ -[WCRBrowserEngineClient setPresentedAllowListPINEntryViewController:]
+ GCC_except_table87
+ GCC_except_table89
+ GCC_except_table91
+ _OBJC_IVAR_$_WCRBrowserEngineClient._allowListAuthenticationInFlight
+ _OBJC_IVAR_$_WCRBrowserEngineClient._allowListPINEntryPresented
+ _OBJC_IVAR_$_WCRBrowserEngineClient._presentedAllowListPINEntryViewController
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v20?0B8"NSError"12ls32l8s56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e45_v24?0"_UIRemoteViewController"8"NSError"16ls32l8s56l8s40l8s48l8
+ _objc_storeWeak
- GCC_except_table84
- GCC_except_table86
- GCC_except_table88
- ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12ls48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e45_v24?0"_UIRemoteViewController"8"NSError"16ls56l8s32l8s40l8s48l8
CStrings:
+ "No view controller available to present PIN entry on"
+ "WCRAuthenticationSites-2026-09-25.plist"
+ "allow list authentication already in flight; refusing re-entrant request"
+ "allow list authentication no longer in flight (%{public}@)"
+ "cancelled"
+ "cannot present PIN entry"
+ "connection error"
+ "correct PIN"
+ "isPINPresent error"
+ "no PIN set"
+ "no view controller"
+ "sheet went away unobserved"
+ "\xf0a"
- "WCRAuthenticationSites-2026-07-19.plist"
```
