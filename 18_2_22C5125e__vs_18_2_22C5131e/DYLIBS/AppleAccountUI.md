## AppleAccountUI

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI`

```diff

-520.226.0.0.0
-  __TEXT.__text: 0x1735e0
+520.227.1.0.0
+  __TEXT.__text: 0x1735f0
   __TEXT.__auth_stubs: 0x2f00
   __TEXT.__delay_helper: 0x110
-  __TEXT.__objc_methlist: 0x81fc
+  __TEXT.__objc_methlist: 0x8254
   __TEXT.__const: 0x5c34
-  __TEXT.__gcc_except_tab: 0x1490
-  __TEXT.__cstring: 0x6b4e
-  __TEXT.__oslogstring: 0xbc2c
+  __TEXT.__gcc_except_tab: 0x14e8
+  __TEXT.__cstring: 0x6b5e
+  __TEXT.__oslogstring: 0xbbec
   __TEXT.__dlopen_cstrs: 0x428
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0xad14

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x3a80
+  __TEXT.__unwind_info: 0x3a98
   __TEXT.__eh_frame: 0x808
   __TEXT.__objc_classname: 0x1e9f
-  __TEXT.__objc_methname: 0x18ff6
-  __TEXT.__objc_methtype: 0x48e1
-  __TEXT.__objc_stubs: 0x126e0
-  __DATA_CONST.__got: 0x1810
-  __DATA_CONST.__const: 0x2998
+  __TEXT.__objc_methname: 0x19096
+  __TEXT.__objc_methtype: 0x4903
+  __TEXT.__objc_stubs: 0x12680
+  __DATA_CONST.__got: 0x1828
+  __DATA_CONST.__const: 0x29f8
   __DATA_CONST.__objc_classlist: 0x6a8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x290
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5a78
+  __DATA_CONST.__objc_selrefs: 0x5a88
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x418
+  __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0xd0
   __AUTH_CONST.__auth_got: 0x1790
-  __AUTH_CONST.__auth_ptr: 0xa58
+  __AUTH_CONST.__auth_ptr: 0xa20
   __AUTH_CONST.__const: 0x3d98
-  __AUTH_CONST.__cfstring: 0x4760
-  __AUTH_CONST.__objc_const: 0x32b90
+  __AUTH_CONST.__cfstring: 0x46e0
+  __AUTH_CONST.__objc_const: 0x32c40
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x4958
   __AUTH.__data: 0x15a8
-  __DATA.__objc_ivar: 0xb1c
+  __DATA.__objc_ivar: 0xb30
   __DATA.__data: 0x3d58
   __DATA.__bss: 0x6a80
   __DATA.__common: 0x3e0

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 7388
-  Symbols:   4799
-  CStrings:  6518
+  Symbols:   4804
+  CStrings:  6519
 
Symbols:
+ _kAAAnalyticEventRecoveryContactCodeEntryLanding
+ _kAAAnalyticEventRecoveryContactRecoveryLanding
+ _kCDPAnalyticsValidateRecoveryCodeEvent
+ _kDataAccessContinue
+ _kDataAccessRecoveryContactCodeCantGet
CStrings:
+ "\n\x11\x12\x11"
+ "%!@(MISSING) - Unable to fetch EDP token after repair. Stopping flow with error %!@(MISSING)"
+ "%!@(MISSING) - Unable to repair EDP state. Stopping flow with error %!@(MISSING)"
+ "@\"AKAppleIDAuthenticationContext\""
+ "Attempting to repair EDP state."
+ "RC Upsell: No RCUpsellMiniBuddy flag found. is OS FeatureFlag Enabled %!d(MISSING)"
+ "RCUpsellMiniBuddy"
+ "T@\"UINavigationController\",&,N,V_rcUpsellNavigationController"
+ "Unable to show EDP token screen because strongCDPController is nil."
+ "Unable to show EDP token screen because strongSelf is nil."
+ "_launchEDPTokenPane:completion:"
+ "_rcUpsellNavigationController"
+ "_sendAnalyticsEventWithSelectedOffer:"
+ "_showEDPTokenPaneWithToken:onViewController:sender:completion:"
+ "approvalControllerWithPresenter:recoverySessionID:telemetryFlowID:"
+ "attachAllHandlersWithTelemetryFlowID:"
+ "com.apple.appleAccount.recoveryContactCodeEntryLanding"
+ "com.apple.appleAccount.recoveryContactRecoveryLanding"
+ "initWithTelemetryFlowID:"
+ "isRCUpsellEnabled"
+ "navController"
+ "rcUpsellNavigationController"
+ "setRcUpsellNavigationController:"
+ "\xf1!"
- "\n\x11\x11\x11"
- "%!@(MISSING) - Unable to fetch EDP token. Stopping flow with error %!@(MISSING)"
- "%!@(MISSING) - Unable to validate EDP state. Stopping flow with error %!@(MISSING)"
- "Beginning add recovery contact upsell flow"
- "Fetching suggested contacts for upsell..."
- "In recovery contact upsell flow Device needs update error %!@(MISSING)"
- "In recovery contact upsell flow user cancelled error %!@(MISSING)"
- "RC_UPSELL_PRIMARY_BUTTON"
- "RC_UPSELL_SECONDARY_BUTTON"
- "RC_UPSELL_SUBTITLE"
- "RC_UPSELL_TITLE"
- "Skip showing invitation message sent UI..."
- "User is not in manatee, we will be unable to perform one tap repair"
- "_beginAddRecoveryContactUpsellFlow"
- "_fetchSuggestedContactsForUpsell"
- "_hasManatee"
- "_showEDPTokenSpyglassPane:completion:"
- "approvalControllerWithPresenter:recoverySessionID:"
- "fetchSuggestedCustodiansForUpsell:"
- "fetchSuggestedCustodiansForUpsellWithImagesOfSize:andCompletion:"
- "isManateeAvailable:"
- "rcUpsell"
- "\xe1!"

```
