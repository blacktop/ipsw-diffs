## FeedbackCore

> `/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore`

```diff

-191.8.1.0.0
-  __TEXT.__text: 0x1441d4
+191.12.0.0.0
+  __TEXT.__text: 0x144c18
   __TEXT.__auth_stubs: 0x2c60
-  __TEXT.__objc_methlist: 0xb5f8
-  __TEXT.__const: 0x3694
-  __TEXT.__cstring: 0xc4d1
-  __TEXT.__oslogstring: 0xa3c6
+  __TEXT.__objc_methlist: 0xb660
+  __TEXT.__const: 0x36a4
+  __TEXT.__cstring: 0xc511
+  __TEXT.__oslogstring: 0xa3f6
   __TEXT.__gcc_except_tab: 0x1cbc
   __TEXT.__ustring: 0xe6
   __TEXT.__dlopen_cstrs: 0x62

   __TEXT.__swift5_assocty: 0x2a0
   __TEXT.__swift5_proto: 0x158
   __TEXT.__swift5_types: 0x13c
-  __TEXT.__swift5_capture: 0xcec
+  __TEXT.__swift5_capture: 0xd08
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x4b00
+  __TEXT.__unwind_info: 0x4b20
   __TEXT.__eh_frame: 0x1580
-  __TEXT.__objc_classname: 0x11e1
-  __TEXT.__objc_methname: 0x1d12f
+  __TEXT.__objc_classname: 0x11e2
+  __TEXT.__objc_methname: 0x1d1d8
   __TEXT.__objc_methtype: 0x3dc8
-  __TEXT.__objc_stubs: 0x14d60
-  __DATA_CONST.__got: 0x11a8
+  __TEXT.__objc_stubs: 0x14dc0
+  __DATA_CONST.__got: 0x11b0
   __DATA_CONST.__const: 0x4018
-  __DATA_CONST.__objc_classlist: 0x538
+  __DATA_CONST.__objc_classlist: 0x540
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7578
+  __DATA_CONST.__objc_selrefs: 0x7598
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x4d0
   __AUTH_CONST.__auth_got: 0x1640
-  __AUTH_CONST.__const: 0x4740
-  __AUTH_CONST.__cfstring: 0x9060
-  __AUTH_CONST.__objc_const: 0x1d598
+  __AUTH_CONST.__const: 0x47b8
+  __AUTH_CONST.__cfstring: 0x9080
+  __AUTH_CONST.__objc_const: 0x1d648
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x498
-  __AUTH.__objc_data: 0x4e58
-  __AUTH.__data: 0xd50
-  __DATA.__objc_ivar: 0x700
+  __AUTH.__objc_data: 0x4ec8
+  __AUTH.__data: 0xd70
+  __DATA.__objc_ivar: 0x704
   __DATA.__data: 0x2cb0
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x3038

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 55EE2A68-A688-3D3D-8ABC-88AE9F61260C
-  Functions: 7328
-  Symbols:   15700
-  CStrings:  9410
+  UUID: 205A61C7-B039-3F26-9D6D-55894C9244EE
+  Functions: 7345
+  Symbols:   15726
+  CStrings:  9424
 
Symbols:
+ +[FBKLoginManager hasSignedInSystemAccount]
+ -[FBKDeviceDiagnosticsController deConsentTextsForGatheringAttachments]
+ _OBJC_CLASS_$_FBKConsentAlertStrings
+ _OBJC_IVAR_$_FBKDeviceDiagnosticsController._deConsentTextsForGatheringAttachments
+ _OBJC_METACLASS_$_FBKConsentAlertStrings
+ __CLASS_METHODS_FBKConsentAlertStrings
+ __CLASS_PROPERTIES_FBKConsentAlertStrings
+ __DATA_FBKConsentAlertStrings
+ __INSTANCE_METHODS_FBKConsentAlertStrings
+ __METACLASS_DATA_FBKConsentAlertStrings
+ __OBJC_$_CLASS_METHODS_FBKLoginManager
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.253
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.253.cold.1
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.260
+ ___42-[FBKBugFormTableViewController legalText]_block_invoke.295
+ ___57-[FBKLoginManager loginWithAppleConnectToken:completion:]_block_invoke.91
+ ___71-[FBKLoginManager _loginWithUsername:authenticationResults:completion:]_block_invoke.90
+ ___75-[FBKBugFormTableViewController alertControllerForDismissWithLaunchAction:]_block_invoke.312
+ ___89-[FBKLoginManager autoLoginWithUserID:userName:deviceToken:usesSystemAccount:completion:]_block_invoke.88
+ ___89-[FBKLoginManager autoLoginWithUserID:userName:deviceToken:usesSystemAccount:completion:]_block_invoke_2.89
+ ___block_literal_global.212
+ ___block_literal_global.293
+ ___block_literal_global.297
+ ___block_literal_global.316
+ ___block_literal_global.94
+ _legalText.onceToken.294
+ _objc_msgSend$alertTitle
+ _objc_msgSend$cancelActionTitle
+ _objc_msgSend$submitActionTitle
- ___39-[FBKBugFormTableViewController submit]_block_invoke.255
- ___39-[FBKBugFormTableViewController submit]_block_invoke.255.cold.1
- ___39-[FBKBugFormTableViewController submit]_block_invoke.264
- ___42-[FBKBugFormTableViewController legalText]_block_invoke.297
- ___57-[FBKLoginManager loginWithAppleConnectToken:completion:]_block_invoke.85
- ___71-[FBKLoginManager _loginWithUsername:authenticationResults:completion:]_block_invoke.84
- ___75-[FBKBugFormTableViewController alertControllerForDismissWithLaunchAction:]_block_invoke.316
- ___89-[FBKLoginManager autoLoginWithUserID:userName:deviceToken:usesSystemAccount:completion:]_block_invoke.82
- ___89-[FBKLoginManager autoLoginWithUserID:userName:deviceToken:usesSystemAccount:completion:]_block_invoke_2.83
- ___block_literal_global.205
- ___block_literal_global.295
- ___block_literal_global.299
- ___block_literal_global.318
- ___block_literal_global.88
- _legalText.onceToken.296
CStrings:
+ "Cancel button in alert asking user to agree to consent text"
+ "FBKConsentAlertStrings"
+ "Sending information to Apple"
+ "Showing DE consent \n%s"
+ "System account check: %{public}@"
+ "T@\"NSArray\",R,C,N,V_deConsentTextsForGatheringAttachments"
+ "_deConsentTextsForGatheringAttachments"
+ "alertTitle"
+ "cancelActionTitle"
+ "hasSignedInSystemAccount"
+ "not signed in"
+ "signed in"
+ "submitActionTitle"
- "Cancel button in alert asking user to agree to consent text. If user choses to go back they will be brought back to the feedback editing UI"
- "SUBMISSION_PII_TITLE"
- "Showing DE consent"

```
