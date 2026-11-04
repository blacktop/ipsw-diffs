## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-448.125.10.0.0
-  __TEXT.__text: 0x8e4ec
-  __TEXT.__objc_methlist: 0x5804
+448.250.2.0.0
+  __TEXT.__text: 0x8f64c
+  __TEXT.__objc_methlist: 0x586c
   __TEXT.__const: 0x888
-  __TEXT.__oslogstring: 0x1510e
-  __TEXT.__cstring: 0xe6b5
+  __TEXT.__oslogstring: 0x1549e
+  __TEXT.__cstring: 0xef45
   __TEXT.__gcc_except_tab: 0xb94
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x3b7

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift_as_cont: 0x68
-  __TEXT.__unwind_info: 0x2f28
+  __TEXT.__unwind_info: 0x2f70
   __TEXT.__eh_frame: 0x918
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x26d8
+  __DATA_CONST.__const: 0x2728
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a18
+  __DATA_CONST.__objc_selrefs: 0x3a80
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x160
-  __DATA_CONST.__objc_arraydata: 0x220
-  __DATA_CONST.__got: 0x1148
-  __AUTH_CONST.__const: 0xb10
-  __AUTH_CONST.__cfstring: 0x9960
-  __AUTH_CONST.__objc_const: 0x10260
+  __DATA_CONST.__objc_arraydata: 0x230
+  __DATA_CONST.__got: 0x1188
+  __AUTH_CONST.__const: 0xb30
+  __AUTH_CONST.__cfstring: 0x9e20
+  __AUTH_CONST.__objc_const: 0x10290
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x968
   __AUTH.__objc_data: 0x170
-  __DATA.__objc_ivar: 0x3d0
+  __DATA.__objc_ivar: 0x3d4
   __DATA.__data: 0x1220
   __DATA_DIRTY.__objc_data: 0x19b0
   __DATA_DIRTY.__data: 0x200

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3220
-  Symbols:   4235
-  CStrings:  2864
+  Functions: 3238
+  Symbols:   4258
+  CStrings:  2916
 
Symbols:
+ +[CDPDPCSController isRecordPasswordGenerationMismatchError:]
+ +[CDPDPCSController passwordVersionMismatchForValidateTelemetry:]
+ -[CDPDAuthProxyImpl recreatePDPRecordWithFallbackForAltDSID:telemetryFlowID:completion:]
+ -[CDPDPDPRecoveryController recreatePDPRecordWithFallbackWithCompletion:]
+ -[CDPDStateMachine _routePostOctagonPDPSetupFailure:completion:]
+ -[CDPDStateMachine _sendPDPServerRecreationEvent:didSucceed:error:]
+ -[CDPDStateMachine _shouldAttemptPDPServerRecreationAfterSetupError:]
+ _AKAppleIDAuthenticationServerErrorDomain
+ _OBJC_CLASS_$_AKBasicServerRequest
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_IVAR_$_CDPDStateMachine._pdpServerRecreationAlreadyAttempted
+ _OUTLINED_FUNCTION_12
+ ___61+[CDPDPCSController isRecordPasswordGenerationMismatchError:]_block_invoke
+ ___64-[CDPDStateMachine _routePostOctagonPDPSetupFailure:completion:]_block_invoke
+ ___73-[CDPDPDPRecoveryController recreatePDPRecordWithFallbackWithCompletion:]_block_invoke
+ ___88-[CDPDAuthProxyImpl recreatePDPRecordWithFallbackForAltDSID:telemetryFlowID:completion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e43_v24?0"AKBasicServerResponse"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e37_v32?0Q8"NSDictionary"16"NSError"24ls32l8s48l8s40l8
+ _kCDPAnalyticsPDPServerRecreationFinishEvent
+ _kCDPAnalyticsPDPServerRecreationSetupAfterRecreateEvent
+ _kCDPAnalyticsPDPServerRecreationSkippedEvent
+ _kCDPAnalyticsPDPServerRecreationStartEvent
+ _kCDPAnalyticsPDPSetupHealedOnRevalidateEvent
+ _kPCSErrorDomain
- GCC_except_table48
CStrings:
+ "CDPDStateMachine: DBR password-version mismatch, attempting server-side recreation"
+ "CDPDStateMachine: DBR record healthy after the failed setup, skipping escalation"
+ "CDPDStateMachine: DBR record not healthy after server-side recreation (state: %lu), running setup"
+ "CDPDStateMachine: DBR setup failed on auth, skipping server-side recreation"
+ "CDPDStateMachine: DBR setup still failed after server-side recreation: %@"
+ "CDPDStateMachine: Server-side recreation failed: %@"
+ "CDPDStateMachine: Server-side recreation healed the DBR record"
+ "CDPDStateMachine: Server-side recreation healed the DBR record after setup"
+ "CDPDStateMachine: server-side recreation already attempted in this sign-in, skipping"
+ "PDP: server-side recreation did %@ succeed, error=%{public}@"
+ "PDP: server-side recreation needs an altDSID"
+ "Requesting server-side DBR recreation for %{mask.hash}@"
+ "Server-side DBR recreation returned HTTP status %ld"
+ "altDsId"
+ "application/json"
+ "com.apple.authkit.appleSMSSenderCacheRefreshed"
+ "com.apple.authkit.callsignalsRequested"
+ "com.apple.authkit.codeDisplayedWithinvisibleInk"
+ "com.apple.authkit.grayTextDisclosures"
+ "com.apple.authkit.invisibleInkRemovedFromCode"
+ "com.apple.authkit.localAuthentication"
+ "com.apple.authkit.pushReceived"
+ "com.apple.authkit.signIn.2FAApprovalFlowEnd"
+ "com.apple.authkit.signIn.2FAApprovalFlowStart"
+ "com.apple.authkit.signIn.appleSMSSenderDetected"
+ "com.apple.authkit.signIn.check2FACodeLegitimacy"
+ "com.apple.remoteui.appleid_account_manage_approval_signin"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_closeButtonBarItem_1"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_confirm"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_confirm_post_HSA2Code_1"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_confirm_post_PiggybackingCode_1"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_confirm_post_SMSCode_1"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_confirm_post_SkybridgeCode_1"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_confirm_post_closeButtonBarItem_1"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_confirm_post_multiChoice_1"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_confirm_post_page"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_deny"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_deny_multiChoice_1"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_deny_multiChoice_2"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_deny_page"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_labelRow_1"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_labelRow_2"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_multiChoice_1"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_multiChoice_2"
+ "com.apple.remoteui.appleid_account_manage_approval_signin_page"
+ "com.apple.remoteui.appleid_account_manage_security_password"
+ "com.apple.remoteui.auth_header_1"
+ "com.apple.remoteui.auth_navigationBar_1"
+ "com.apple.remoteui.auth_page"
+ "com.apple.remoteui.auth_verify_biometrics"
+ "pdpRecreateWithFallback"
+ "v24@?0@\"AKBasicServerResponse\"8@\"NSError\"16"
```
