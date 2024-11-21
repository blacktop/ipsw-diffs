## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-386.227.2.0.0
-  __TEXT.__text: 0x8e7b8
+386.231.0.0.0
+  __TEXT.__text: 0x8ebf8
   __TEXT.__auth_stubs: 0x11d0
   __TEXT.__objc_methlist: 0x44cc
   __TEXT.__const: 0x730
-  __TEXT.__oslogstring: 0x135e8
-  __TEXT.__cstring: 0x76f5
-  __TEXT.__gcc_except_tab: 0xba4
+  __TEXT.__oslogstring: 0x13768
+  __TEXT.__cstring: 0x7705
+  __TEXT.__gcc_except_tab: 0xbac
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x301
   __TEXT.__swift5_fieldmd: 0x8c

   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x20
   __TEXT.__swift5_capture: 0x1b8
-  __TEXT.__unwind_info: 0x1cb0
+  __TEXT.__unwind_info: 0x1cb8
   __TEXT.__eh_frame: 0x8e0
   __TEXT.__objc_classname: 0xc8c
-  __TEXT.__objc_methname: 0xeb41
-  __TEXT.__objc_methtype: 0x2902
-  __TEXT.__objc_stubs: 0xbe80
-  __DATA_CONST.__got: 0xfc0
+  __TEXT.__objc_methname: 0xeb7e
+  __TEXT.__objc_methtype: 0x28e1
+  __TEXT.__objc_stubs: 0xbea0
+  __DATA_CONST.__got: 0x1000
   __DATA_CONST.__const: 0x2588
   __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3528
+  __DATA_CONST.__objc_selrefs: 0x3530
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__auth_got: 0x8f8
   __AUTH_CONST.__auth_ptr: 0x1d8
-  __AUTH_CONST.__const: 0x9a8
+  __AUTH_CONST.__const: 0x9e8
   __AUTH_CONST.__cfstring: 0x4e60
   __AUTH_CONST.__objc_const: 0x11af8
   __AUTH_CONST.__objc_intobj: 0x180

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3022
-  Symbols:   3825
-  CStrings:  4733
+  Functions: 3027
+  Symbols:   3837
+  CStrings:  4738
 
Symbols:
+ _kCDPAnalyticsEDPRecoveryTokenDontHaveKeyAlertEscapeOptionTappedEvent
+ _kCDPAnalyticsEDPRecoveryTokenDontHaveKeyAlertPresentedEvent
+ _kCDPAnalyticsEDPRecoveryTokenEntryScreenEscapeOptionTappedEvent
+ _kCDPAnalyticsEDPRecoveryTokenEntryScreenLandingEvent
+ _kCDPAnalyticsEDPRecoveryTokenInformationalScreenEscapeOptionTappedEvent
+ _kCDPAnalyticsEDPRecoveryTokenInformationalScreenLandingEvent
+ _kCDPAnalyticsEDPSpyglassPaneEmailButtonTappedEvent
+ _kCDPAnalyticsEDPSpyglassPaneLandingEvent
CStrings:
+ "-[CDPDStateMachine _isEligibleForRecoveryTokenWithContext:cdpStateMachineError:completion:]_block_invoke"
+ "Attempting to persist verifier for keyType: %ld for %@"
+ "CDPContext=%@: isProxSignIn, skipping the password and password metadata checks because prox flows does not have password. Calling PCS repair directly..."
+ "Interactive recovery with EDP status - %lu"
+ "Ledger: rpdProbationDuration is not set. Deafulting to CDPRPDProbationTimeInterval"
+ "We just cancelled / cancelled RPD from the token screen. We should not show the token screen again."
+ "_continuePerformEDPRepairWithResult:completion:"
+ "_isEligibleForRecoveryTokenWithContext:cdpStateMachineError:completion:"
+ "cdp_anyDescendantErrorDownToMaxDepth:matchesPredicate:"
+ "createEDPLivenessDictionaryWithContext:completion:"
+ "v32@0:8@\"CDPContext\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "-[CDPDStateMachine _isEligibleForRecoveryTokenWithContext:completion:]_block_invoke"
- "Attempting to persist verifier: %@ with keyType: %ld for %@"
- "_continuePerformEDPRepairWithCDPEnabled:completion:"
- "_isEligibleForRecoveryTokenWithContext:completion:"
- "createEDPLivenessDictionaryWithContext:uiProvider:completion:"
- "v40@0:8@\"CDPContext\"16@\"<CDPStateUIProviderInternal>\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"

```
