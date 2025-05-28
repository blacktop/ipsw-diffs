## findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 422.2.1.1.0
-  __TEXT.__text: 0x239e94
+  __TEXT.__text: 0x23cecc
   __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_stubs: 0x15d80
-  __TEXT.__objc_methlist: 0xd970
+  __TEXT.__objc_stubs: 0x162a0
+  __TEXT.__objc_methlist: 0xdcb0
   __TEXT.__const: 0x2e0e0
   __TEXT.__gcc_except_tab: 0x1f0c
-  __TEXT.__objc_methname: 0x1b50d
-  __TEXT.__oslogstring: 0x10196
-  __TEXT.__cstring: 0x84c7
-  __TEXT.__objc_classname: 0x19df
-  __TEXT.__objc_methtype: 0x2f6b
-  __TEXT.__unwind_info: 0x318c
+  __TEXT.__objc_methname: 0x1bb85
+  __TEXT.__oslogstring: 0x105b1
+  __TEXT.__cstring: 0x8793
+  __TEXT.__objc_classname: 0x1a32
+  __TEXT.__objc_methtype: 0x2fa1
+  __TEXT.__unwind_info: 0x3210
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__auth_got: 0x708
-  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__got: 0x498
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xcf28
-  __DATA_CONST.__cfstring: 0xa300
-  __DATA_CONST.__objc_classlist: 0x698
+  __DATA_CONST.__const: 0xcff8
+  __DATA_CONST.__cfstring: 0xa540
+  __DATA_CONST.__objc_classlist: 0x6b0
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x390
+  __DATA_CONST.__objc_intobj: 0x468
   __DATA_CONST.__objc_doubleobj: 0xd0
   __DATA_CONST.__objc_arraydata: 0x220
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_floatobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__linkguard: 0xe
-  __DATA.__objc_const: 0x1b5e0
-  __DATA.__objc_selrefs: 0x6260
+  __DATA.__objc_const: 0x1bb90
+  __DATA.__objc_selrefs: 0x63b8
   __DATA.__objc_protorefs: 0x38
-  __DATA.__objc_classrefs: 0xa38
-  __DATA.__objc_superrefs: 0x538
-  __DATA.__objc_ivar: 0x1000
-  __DATA.__objc_data: 0x41f0
-  __DATA.__data: 0x2480
-  __DATA.__bss: 0x780
+  __DATA.__objc_classrefs: 0xa68
+  __DATA.__objc_superrefs: 0x550
+  __DATA.__objc_ivar: 0x104c
+  __DATA.__objc_data: 0x42e0
+  __DATA.__data: 0x2488
+  __DATA.__bss: 0x7b0
   __DATA.__common: 0x6c
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5768
-  Symbols:   564
-  CStrings:  8227
+  Functions: 5873
+  Symbols:   568
+  CStrings:  8346
 
Symbols:
+ _LARatchetErrorUserInfoKeyState
+ _OBJC_CLASS_$_LAContext
+ _OBJC_CLASS_$_LARatchet
+ _OBJC_CLASS_$_LARatchetManager
CStrings:
+ "\x1b"
+ "${scheme}://${hostname}/fmipservice/${service}/disableLocations"
+ "%@: sending request to disable locations."
+ "@\"LAContext\""
+ "@\"LARatchet\""
+ "Arming ratchet %@ with options %@."
+ "Evaluating location-based owner authentication policy with options %@."
+ "FMDDisableLocationDisplayRequest"
+ "FMDOwnerAuthenticationManager"
+ "FMDRatchetManager"
+ "FM_OWNER_AUTH_REASON_EACS"
+ "FM_RATCHET_BEGIN_SIGNOUT"
+ "FM_RATCHET_BEGIN_TITLE_SIGNOUT"
+ "FM_RATCHET_BEGIN_TITLE_TURN_OFF"
+ "FM_RATCHET_BEGIN_TURN_OFF"
+ "FM_RATCHET_CALLOUT_REASON_SIGNOUT"
+ "FM_RATCHET_CALLOUT_REASON_TURN_OFF"
+ "FM_RATCHET_COUNTDOWN_SIGNOUT"
+ "FM_RATCHET_COUNTDOWN_TURN_OFF"
+ "FM_RATCHET_REASON_SIGNOUT"
+ "FM_RATCHET_REASON_TURN_OFF"
+ "Failed to arm ratchet %@ no stateInfo, error: %@, %@."
+ "Failed to arm ratchet %@ state %li, error: %@."
+ "Failure to arm ratchet %@ with no error and no result."
+ "Failure to arm ratchet %@, no context found."
+ "Failure to evaluate policy %@, %@."
+ "Finished evaluating policy."
+ "LAContext already evaluating."
+ "Localizable-DIMPLEKEY"
+ "No ratchet defined for this context: %lu. Allowing disable FMIP."
+ "Ratchet already initialized %@."
+ "Ratchet armed %@, proceeding with operation."
+ "Ratchet not enabled. Allowing disable FMIP."
+ "SimulateDisableLocationDisplayFailure"
+ "SimulateRequireDisableLocationFailure"
+ "T@\"FMFuture\",&,N,V_currentTask"
+ "T@\"LAContext\",&,N,V_context"
+ "T@\"LARatchet\",&,N,V_ratchet"
+ "T@\"NSString\",&,N,V_localizedBeginBody"
+ "T@\"NSString\",&,N,V_localizedBeginTitle"
+ "T@\"NSString\",&,N,V_localizedCalloutReason"
+ "T@\"NSString\",&,N,V_localizedCountdownBody"
+ "T@\"NSString\",&,N,V_localizedReason"
+ "T@\"NSString\",&,N,V_ratchetIdentifier"
+ "T@\"NSURL\",&,N,V_deepLinkURL"
+ "T@?,C,N,V_deniedOperationBlock"
+ "T@?,C,N,V_permittedOperationBlock"
+ "TB,N,V_fallbackToNoAuthentication"
+ "Unexpected failure to arm ratchet %@ state %li, error: %@."
+ "_currentTask"
+ "_deepLinkURL"
+ "_deniedOperationBlock"
+ "_fallbackToNoAuthentication"
+ "_localizedBeginBody"
+ "_localizedBeginTitle"
+ "_localizedCalloutReason"
+ "_localizedCountdownBody"
+ "_localizedReason"
+ "_permittedOperationBlock"
+ "_ratchet"
+ "_ratchetIdentifier"
+ "accountRatchet"
+ "addSuccessBlock:"
+ "armRatchetIfNeeded"
+ "armWithOptions:completion:"
+ "com.apple.findmydevice.ratchet.error"
+ "com.apple.findmydevice.ratchet.turnOff"
+ "currentTask"
+ "deepLinkURL"
+ "deniedOperationBlock"
+ "disableLocationDisplay"
+ "disableLocationDisplayWithCompletion simulating failure."
+ "disableLocationDisplayWithCompletion:"
+ "evaluateOperation"
+ "evaluatePolicy"
+ "evaluatePolicy:options:reply:"
+ "evaluationOptions"
+ "fallbackToNoAuthentication"
+ "finishWithNoResult"
+ "handleRatchetError:"
+ "isFeatureEnabled"
+ "localizedBeginBody"
+ "localizedBeginTitle"
+ "localizedCalloutReason"
+ "localizedCountdownBody"
+ "localizedReason"
+ "ownerAuthentication"
+ "ownerAuthenticationManagerEraseAllContentsAndSettings"
+ "permittedOperationBlock"
+ "prefs:root=APPLE_ACCOUNT&path=LOCATION_SHARING/FindMyDevice-Settings"
+ "ratchet"
+ "ratchetErrorDeniedWithUnderlyingError:"
+ "ratchetIdentifier"
+ "ratchetManagerTurnOffFMIP"
+ "ratchetManageriCloudSignOut"
+ "ratchetOptions"
+ "rawValue"
+ "requireDisableLocationWithCompletion could not find provider."
+ "requireDisableLocationWithCompletion finished with error %@."
+ "requireDisableLocationWithCompletion finished."
+ "requireDisableLocationWithCompletion result %li, fmip: %i, locationService: %i."
+ "requireDisableLocationWithCompletion simulating failure."
+ "requireDisableLocationWithCompletion:"
+ "setCurrentTask:"
+ "setDeepLinkURL:"
+ "setDeniedOperationBlock:"
+ "setFallbackToNoAuthentication:"
+ "setLocalizedBeginBody:"
+ "setLocalizedBeginTitle:"
+ "setLocalizedCalloutReason:"
+ "setLocalizedCountdownBody:"
+ "setLocalizedReason:"
+ "setPermittedOperationBlock:"
+ "setRatchet:"
+ "setRatchetIdentifier:"
+ "underlyingErrors"
+ "v16@?0@8"
+ "v24@0:8@?<v@?q@\"NSError\">16"
+ "v24@?0@8@\"NSError\"16"

```
