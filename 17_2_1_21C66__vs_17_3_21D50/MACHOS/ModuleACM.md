## ModuleACM

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/ModulePlugins/ModuleACM.bundle/ModuleACM`

```diff

-1394.62.1.0.0
-  __TEXT.__text: 0x13cdc
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_stubs: 0x2d40
-  __TEXT.__objc_methlist: 0x7e0
-  __TEXT.__const: 0xe4
-  __TEXT.__objc_methname: 0x34e9
-  __TEXT.__objc_classname: 0x129
-  __TEXT.__objc_methtype: 0x959
-  __TEXT.__cstring: 0x11d8
-  __TEXT.__gcc_except_tab: 0x3e0
-  __TEXT.__oslogstring: 0xc7d
+1394.82.1.0.0
+  __TEXT.__text: 0x15f38
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_stubs: 0x3320
+  __TEXT.__objc_methlist: 0x978
+  __TEXT.__const: 0x150
+  __TEXT.__objc_methname: 0x3b4b
+  __TEXT.__objc_classname: 0x170
+  __TEXT.__objc_methtype: 0xaf4
+  __TEXT.__cstring: 0x12ec
+  __TEXT.__gcc_except_tab: 0x478
+  __TEXT.__oslogstring: 0xe02
   __TEXT.__ustring: 0x1e
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0x4a0
-  __DATA_CONST.__auth_got: 0x358
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0xd78
-  __DATA_CONST.__cfstring: 0x16e0
-  __DATA_CONST.__objc_classlist: 0x48
+  __TEXT.__unwind_info: 0x578
+  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__const: 0xf40
+  __DATA_CONST.__cfstring: 0x1800
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x510
+  __DATA_CONST.__objc_intobj: 0x600
   __DATA_CONST.__objc_arraydata: 0x68
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x14c0
-  __DATA.__objc_selrefs: 0xc80
-  __DATA.__objc_classrefs: 0x160
-  __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0xa4
-  __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0x2a0
+  __DATA.__objc_const: 0x1af8
+  __DATA.__objc_selrefs: 0xe08
+  __DATA.__objc_protorefs: 0x8
+  __DATA.__objc_classrefs: 0x178
+  __DATA.__objc_superrefs: 0x30
+  __DATA.__objc_ivar: 0xb8
+  __DATA.__objc_data: 0x320
+  __DATA.__data: 0x360
   __DATA.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 47F3F3C3-04C8-3FC6-ABF4-BC9A7A50D0C6
-  Functions: 300
-  Symbols:   170
-  CStrings:  1110
+  UUID: 12968DC9-9A26-382B-95F5-053931552BD1
+  Functions: 349
+  Symbols:   178
+  CStrings:  1224
 
Symbols:
+ _CFStringCompare
+ _LACDTBiometryWatchdogGlobalFallbackTime
+ _LACDarwinNotificationRatchetStateDidChange
+ _LACLogDTOUI
+ _NSStringFromProtocol
+ _OBJC_CLASS_$_LACDarwinNotificationCenter
+ _OBJC_CLASS_$_LACLocalizationUtils
+ _OBJC_METACLASS_$_MechanismACM
CStrings:
+ "\x03"
+ "%@ Could not add credential(%d)"
+ "%@ Did finish ratchet state query %{public}@"
+ "%@ Skipping UI presentation"
+ "%@ Will perform ratchet state query"
+ "%@ Will proceed with UI presentation"
+ "%@ could not add credential(%d)"
+ "%@ preflew policy with status: %d, policySatisfied: %d"
+ "; "
+ "<%@ %p; %@>"
+ "@\"<LACDTOEnvironmentProviding>\"16@0:8"
+ "@\"<LACDTOFeatureControlling>\"16@0:8"
+ "@\"<LACDTOPendingPolicyEvaluationController>\"16@0:8"
+ "@\"<LACDTOPolicyEvaluationController>\"16@0:8"
+ "@\"<LACDTORatchetStateProvider>\"16@0:8"
+ "@\"<LACDTOServiceXPC>\"16@0:8"
+ "@\"<LACDarwinNotificationCenter>\""
+ "@\"NSMutableDictionary\"8@?0"
+ "A"
+ "ACMRequirement"
+ "ACMRequirement: %@"
+ "AUTHENTICATE_TO_RETRY_FACE_ID"
+ "AUTHENTICATE_TO_RETRY_TOUCH_ID"
+ "Could not reset ratchet with error: %{public}@"
+ "LACDTOService"
+ "LACDarwinNotificationCenterObserver"
+ "MechanismRatchet"
+ "Missing LACDTOService dependency"
+ "Requirement: %d not handled for policy: %@"
+ "Skipping Cool-off UI as LAOptionNoCoolOffUI is set to YES"
+ "T@\"<LACDTOEnvironmentProviding>\",R,N"
+ "T@\"<LACDTOFeatureControlling>\",R,N"
+ "T@\"<LACDTOPendingPolicyEvaluationController>\",R,N"
+ "T@\"<LACDTOPolicyEvaluationController>\",R,N"
+ "T@\"<LACDTORatchetStateProvider>\",R,N"
+ "T@\"<LACDTOServiceXPC>\",R,N"
+ "T@\"<LARemoteUI>\",W,N,V_remoteUiDelegate"
+ "Td,N,V_coolOffDuration"
+ "Will set DTOConfig"
+ "_addBiometryConfirmationCredentialWithCompletion:"
+ "_beginSecurityDelay"
+ "_cancel"
+ "_coolOffDuration"
+ "_dismiss"
+ "_finishInState:"
+ "_finishInState:error:"
+ "_finishInState:forceRetry:"
+ "_finishInState:result:"
+ "_finishInState:result:error:forceRetry:"
+ "_isStateSatisfiable:"
+ "_ratchetStateWithCompletion:"
+ "_remoteUiDelegate"
+ "_requirement"
+ "_runWithShowUIBlock:"
+ "_shouldAddRatchetCredential"
+ "_shouldShowUIForRatchetState:"
+ "_shouldSkipCountDownUI"
+ "_shouldUpdateCoolOffDurationForState:"
+ "_startObservingRatchetState"
+ "_stopObservingRatchetState"
+ "acmParameterByAppendingACMParameters:"
+ "acmParameterDoNotStartDTOTimers"
+ "addObserver:notification:"
+ "coolOffDuration"
+ "coolOffDuration: %.2f"
+ "d16@0:8"
+ "duration"
+ "encodeLocalizationKey:"
+ "environmentProvider"
+ "errorWithCode:"
+ "featureController"
+ "finishRunWithResult:error:skipReply:"
+ "hasObserver:"
+ "initWithBytes:length:"
+ "initWithDictionary:"
+ "initWithEventIdentifier:remoteViewController:acmContextRecord:request:"
+ "initWithParams:request:"
+ "isLocationBasedPolicy:"
+ "maxGlobalCredentialAge"
+ "mechanismEvent:value:reply:"
+ "mechanismPruningMechanismsWithEventIdentifier:"
+ "notificationCenter:didReceiveNotification:"
+ "numberWithDouble:"
+ "pendingPolicyEvaluationController"
+ "policyController"
+ "queue"
+ "ratchetStateProvider"
+ "ratchetStateWithCompletion:"
+ "rawValue"
+ "remoteUiDelegate"
+ "removeObserver:"
+ "resetRatchet:"
+ "serviceLocator"
+ "serviceWithIdentifier:"
+ "setCoolOffDuration:"
+ "showUIBlock"
+ "startServices"
+ "v24@0:8d16"
+ "v24@?0@\"LACDTORatchetState\"8@\"NSError\"16"
+ "v32@0:8@\"<LACDarwinNotificationCenter>\"16^{__CFString=}24"
+ "v32@0:8@16^{__CFString=}24"
+ "v36@0:8@16@24B32"
+ "v44@0:8@16@24@32B40"
+ "xpcController"

```
