## AuthKitUI

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI`

```diff

-525.125.2.1.0
-  __TEXT.__text: 0xc3a90
+525.126.1.1.0
+  __TEXT.__text: 0xc41f8
   __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_methlist: 0x827c
+  __TEXT.__objc_methlist: 0x82ac
   __TEXT.__const: 0x276
-  __TEXT.__gcc_except_tab: 0x12a4
+  __TEXT.__gcc_except_tab: 0x1348
   __TEXT.__cstring: 0x50c8
-  __TEXT.__oslogstring: 0x4847
+  __TEXT.__oslogstring: 0x4963
   __TEXT.__dlopen_cstrs: 0x163
   __TEXT.__ustring: 0x2c
   __TEXT.__constg_swiftt: 0xac

   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x14e8
-  __TEXT.__objc_classname: 0x1534
-  __TEXT.__objc_methname: 0x1727b
+  __TEXT.__unwind_info: 0x14f8
+  __TEXT.__objc_classname: 0x1536
+  __TEXT.__objc_methname: 0x172d1
   __TEXT.__objc_methtype: 0x472b
-  __TEXT.__objc_stubs: 0x120a0
+  __TEXT.__objc_stubs: 0x120e0
   __DATA_CONST.__got: 0xca8
-  __DATA_CONST.__const: 0x2478
+  __DATA_CONST.__const: 0x24a0
   __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b88
+  __DATA_CONST.__objc_selrefs: 0x5b98
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x2b8
   __AUTH_CONST.__auth_got: 0x548
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0x4e00
-  __AUTH_CONST.__objc_const: 0x17088
+  __AUTH_CONST.__objc_const: 0x170b8
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0x2068
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x73c
+  __DATA.__objc_ivar: 0x740
   __DATA.__data: 0x19d0
   __DATA.__bss: 0x160
   __DATA_DIRTY.__objc_data: 0x320

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AC7E5A67-F7ED-3E90-8BB6-09E64ACB82F9
-  Functions: 2694
-  Symbols:   10985
-  CStrings:  6130
+  UUID: 0CFA4536-6274-3B45-8776-49D1F7848CB1
+  Functions: 2699
+  Symbols:   11000
+  CStrings:  6134
 
Symbols:
+ -[AKAppleIDFollowUpServerUIPresenter _authContextWithAltDSID:account:]
+ -[AKAppleIDFollowUpServerUIPresenter _presentServerUIWithCompletion:]
+ -[AKAppleIDFollowUpServerUIPresenter _urlAtKey:completion:]
+ -[AKExtensionlessFollowUpHelperContext forceInlinePresentation]
+ -[AKExtensionlessFollowUpHelperContext setForceInlinePresentation:]
+ GCC_except_table4
+ _OBJC_IVAR_$_AKExtensionlessFollowUpHelperContext._forceInlinePresentation
+ ___69-[AKAppleIDFollowUpServerUIPresenter _presentServerUIWithCompletion:]_block_invoke
+ ___93-[AKAppleIDFollowUpServerUIPresenter _performAuthKitActionWithResponse:additionalData:error:]_block_invoke.59
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e27_v24?0"NSURL"8"NSError"16lw64l8s56l8s32l8s40l8s48l8
+ _objc_msgSend$_authContextWithAltDSID:account:
+ _objc_msgSend$_presentServerUIWithCompletion:
+ _objc_msgSend$_urlAtKey:completion:
+ _objc_msgSend$urlForKey:completion:
- -[AKAppleIDFollowUpServerUIPresenter _urlAtKey:]
- ___93-[AKAppleIDFollowUpServerUIPresenter _performAuthKitActionWithResponse:additionalData:error:]_block_invoke.57
- _objc_msgSend$_urlAtKey:
- _objc_msgSend$imageNamed:
CStrings:
+ "Failed to fetch follow up items with id: %@\nfetchError: %@"
+ "T@\"AKExtensionlessFollowUpHelperContext\",&,N,V_followupHelperContext"
+ "_authContextWithAltDSID:account:"
+ "_prepareServerUIContext with altDSID=%{mask.hash}@"
+ "_presentServerUIWithCompletion - altDSID not found in follow up _item, checking _followupHelperContext instead."
+ "_presentServerUIWithCompletion - failed to find URL key: %@ in bag, cannot present server UI"
+ "_presentServerUIWithCompletion - no altDSID provided in FollowUp or context, cannot present server UI."
+ "_presentServerUIWithCompletion with urlKey: %@"
+ "_presentServerUIWithCompletion:"
+ "_signRequestAndPrepareServerConfig for initialURL: %@"
+ "_urlAtKey:completion:"
+ "urlForKey:completion:"
- "Failed to fetch follow up items with id: %@"
- "Failed to find Url key: %@ in bag, cannot present server UI"
- "No altDSID provided in FollowUp, cannot present server UI."
- "Preparing server configuration..."
- "Preparing the server UI Load Delegate"
- "T@\"AKExtensionlessFollowUpHelperContext\",C,N,V_followupHelperContext"
- "_urlAtKey:"
- "imageNamed:"

```
