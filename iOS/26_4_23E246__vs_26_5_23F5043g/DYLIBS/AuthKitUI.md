## AuthKitUI

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI`

```diff

-525.475.19.0.0
-  __TEXT.__text: 0xca118
+525.575.4.0.0
+  __TEXT.__text: 0xcb57c
   __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_methlist: 0x84ec
+  __TEXT.__objc_methlist: 0x8524
   __TEXT.__const: 0x286
-  __TEXT.__gcc_except_tab: 0x14fc
-  __TEXT.__cstring: 0x520f
-  __TEXT.__oslogstring: 0x4e7a
+  __TEXT.__gcc_except_tab: 0x158c
+  __TEXT.__cstring: 0x526c
+  __TEXT.__oslogstring: 0x4fa4
   __TEXT.__dlopen_cstrs: 0x179
   __TEXT.__ustring: 0x2c
   __TEXT.__constg_swiftt: 0xac

   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1620
+  __TEXT.__unwind_info: 0x1630
   __TEXT.__objc_classname: 0x1628
-  __TEXT.__objc_methname: 0x17a3a
+  __TEXT.__objc_methname: 0x17b2a
   __TEXT.__objc_methtype: 0x4841
-  __TEXT.__objc_stubs: 0x126c0
+  __TEXT.__objc_stubs: 0x12760
   __DATA_CONST.__got: 0xd20
-  __DATA_CONST.__const: 0x2570
+  __DATA_CONST.__const: 0x25f0
   __DATA_CONST.__objc_classlist: 0x398
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d30
+  __DATA_CONST.__objc_selrefs: 0x5d60
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0x2b8
   __AUTH_CONST.__auth_got: 0x548
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x4ea0
-  __AUTH_CONST.__objc_const: 0x17908
+  __AUTH_CONST.__cfstring: 0x4f20
+  __AUTH_CONST.__objc_const: 0x17a70
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1CC21BAB-A674-3C51-9DBB-4DB709236D4E
-  Functions: 2781
-  Symbols:   11262
-  CStrings:  6243
+  UUID: AFF7AA74-7AD4-3B78-95D2-0865DA1DB48F
+  Functions: 2788
+  Symbols:   11285
+  CStrings:  6264
 
Symbols:
+ -[AKPDPBlobGenerationHook _displayPasswordChangeFailedAlertWithError:completion:]
+ -[AKPDPBlobGenerationHook _injectPDPPayloadWithContext:pdpBlob:objectModel:]
+ -[AKPDPBlobGenerationHook _processPasswordCollectionFromObjectModel:completion:]
+ -[AKPDPBlobGenerationHook _shouldProceedWithPDPFlowWithCompletion:]
+ -[AKPDPBlobGenerationHook requiresAsyncCompletion]
+ _AKPDPBlobGenerationButtonName
+ ___76-[AKPDPBlobGenerationHook processElement:attributes:objectModel:completion:]_block_invoke
+ ___81-[AKPDPBlobGenerationHook _displayPasswordChangeFailedAlertWithError:completion:]_block_invoke
+ ___81-[AKPDPBlobGenerationHook _displayPasswordChangeFailedAlertWithError:completion:]_block_invoke.48
+ ___block_descriptor_48_e8_32s40bs_e23_v16?0"UIAlertAction"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e28_v24?0"NSData"8"NSError"16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
+ _objc_msgSend$_displayPasswordChangeFailedAlertWithError:completion:
+ _objc_msgSend$_injectPDPPayloadWithContext:pdpBlob:objectModel:
+ _objc_msgSend$_processPasswordCollectionFromObjectModel:completion:
+ _objc_msgSend$_shouldProceedWithPDPFlowWithCompletion:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$isPDPEligibleForAccount:
- -[AKPDPBlobGenerationHook _setResponsePayloadWithContext:pdpBlob:]
- ___block_descriptor_56_e8_32s40s48bs_e28_v24?0"NSData"8"NSError"16ls48l8s32l8s40l8
- _objc_msgSend$_setResponsePayloadWithContext:pdpBlob:
CStrings:
+ "AUTH_ERROR_ALERT_BUTTON_OK"
+ "B24@0:8@?16"
+ "No presentation context available for password change failed alert"
+ "PDPBlobGenerationHook processing - Account is PDP eligible"
+ "PDPBlobGenerationHook skipped - Account not PDP eligible (state: %lu)"
+ "PDPBlobGenerationHook skipped - action '%{public}@' is not ak:collectPassword"
+ "PDPBlobGenerationHook skipped - no AuthKit account: %@"
+ "PDPBlobGenerationHook triggered by button element: %@"
+ "PDP_BLOB_ERROR_ALERT_MESSAGE"
+ "PDP_BLOB_ERROR_ALERT_TITLE"
+ "Password extraction returned nil"
+ "TB,?,R,N"
+ "_displayPasswordChangeFailedAlertWithError:completion:"
+ "_injectPDPPayloadWithContext:pdpBlob:objectModel:"
+ "_processPasswordCollectionFromObjectModel:completion:"
+ "_shouldProceedWithPDPFlowWithCompletion:"
+ "addEntriesFromDictionary:"
+ "ak-button"
+ "isPDPEligibleForAccount:"
+ "requiresAsyncCompletion"
- "PDPBlobGenerationHook skipped - PDP state is not Active (state: %lu)"
- "Successfully generated password collection hook."
- "_setResponsePayloadWithContext:pdpBlob:"

```
