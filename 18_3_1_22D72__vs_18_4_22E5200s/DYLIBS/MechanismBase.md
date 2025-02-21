## MechanismBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase`

```diff

-1656.80.6.0.0
-  __TEXT.__text: 0x1591c
+1656.100.213.0.1
+  __TEXT.__text: 0x16434
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x1624
-  __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0x370
-  __TEXT.__cstring: 0x1004
-  __TEXT.__oslogstring: 0x1360
-  __TEXT.__unwind_info: 0x6e0
-  __TEXT.__objc_classname: 0x3e2
-  __TEXT.__objc_methname: 0x47f1
-  __TEXT.__objc_methtype: 0xe8c
-  __TEXT.__objc_stubs: 0x3540
-  __DATA_CONST.__got: 0x230
+  __TEXT.__objc_methlist: 0x1c68
+  __TEXT.__const: 0x118
+  __TEXT.__gcc_except_tab: 0x3a4
+  __TEXT.__cstring: 0xfc3
+  __TEXT.__oslogstring: 0x1393
+  __TEXT.__unwind_info: 0x708
+  __TEXT.__objc_classname: 0x3f3
+  __TEXT.__objc_methname: 0x49a0
+  __TEXT.__objc_methtype: 0xeb9
+  __TEXT.__objc_stubs: 0x3600
+  __DATA_CONST.__got: 0x270
   __DATA_CONST.__const: 0x818
-  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfe0
+  __DATA_CONST.__objc_selrefs: 0x1138
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0xfc0
-  __AUTH_CONST.__objc_const: 0x5800
-  __AUTH_CONST.__objc_intobj: 0x360
+  __AUTH_CONST.__cfstring: 0xfa0
+  __AUTH_CONST.__objc_const: 0x4eb8
+  __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x4b0
+  __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x244
   __DATA.__data: 0x780
-  __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0x320
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__objc_data: 0x550
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 582
-  Symbols:   795
-  CStrings:  1286
+  Functions: 598
+  Symbols:   822
+  CStrings:  1305
 
Symbols:
+ _LACErrorCodeInternal
+ _LACErrorSubcodeRequestMismatch
+ _LACEvaluationRequestPayloadKeyConcurrentIdleUIListener
+ _LACPolicyDeviceOwnerAuthenticationWithBiometrics
+ _LACPolicyOptionBiometryLockoutRecovery
+ _LACPolicyOptionBiometryLockoutRecoveryRetries
+ _LACPolicyOptionFallbackVisible
+ _LACPolicyOptionPasscodeFirst
+ _LACPolicyOptionUserFallback
+ _OBJC_CLASS_$_LACBiometryHelper
+ _OBJC_CLASS_$_LACPolicyUtilities
+ _OBJC_CLASS_$_MechanismBaseComposite
+ _OBJC_METACLASS_$_MechanismBaseComposite
- _OBJC_CLASS_$_BiometryHelper
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_Request
CStrings:
+ "\x05\x13A\x11\x12\x115"
+ "\x06$\x11\x11\x11"
+ "$"
+ "%@://%@?%@=%u"
+ "%u-%u"
+ "@\"<LACBackoffCounter>\""
+ "@\"<LACContextExternalizing>\""
+ "@\"<LACRemoteUI>\""
+ "@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\""
+ "@\"RemoteUIParams\""
+ "@56@0:8q16q24Q32@40@48"
+ "Connection failed with error %{public}@"
+ "Current request identifier: %u is different from the connection identifier: %@"
+ "LACContextExternalizing"
+ "LACRemoteUIHost"
+ "LACUIMechanism"
+ "MechanismBaseComposite"
+ "Q\x81A\""
+ "Request mismatch: %@ != %@"
+ "T@\"<LACBackoffCounter>\",&,N,V_backoffCounter"
+ "T@\"<LACContextExternalizing>\",R,W,N,V_cachedExternalizationDelegate"
+ "T@\"<LACRemoteUI>\",W,N,V_remoteUiDelegate"
+ "T@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\",&,N,V_uiMechanism"
+ "T@\"NSArray\",&,N,V_submechanisms"
+ "TB,N,GisAND,V_AND"
+ "TB,N,GisOR,V_OR"
+ "TI,N,V_requestID"
+ "TI,R,N,V_instanceId"
+ "TQ,N,V_k"
+ "TQ,N,V_n"
+ "_AND"
+ "_OR"
+ "_assignPendingRequest:reply:"
+ "_n"
+ "_requestID"
+ "_submechanisms"
+ "analyticsData"
+ "anonymousListenerWithIdentifier:"
+ "canRecoverFromAvailabilityError:request:"
+ "checkHasPendingUIRequestsWithCompletion:"
+ "checkLockoutState:isEffectiveLockoutForMatchWithPurpose:"
+ "connectRemoteUI:requestID:reply:"
+ "connectionToViewServiceInvalidatedForIdentifier: %@"
+ "connectionToViewServiceInvalidatedForIdentifier:reply:"
+ "dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:"
+ "dismissRemoteUIWithIdleEndpoint:wasInvalidated:completionHandler:"
+ "endpoint"
+ "errorWithCode:subcode:debugDescription:"
+ "identifier"
+ "initWithEventIdentifier:remoteViewController:k:ofSubmechanisms:request:"
+ "instanceId"
+ "numberWithUnsignedInt:"
+ "passcodeShouldBeFirstMechanism"
+ "payload"
+ "requestID"
+ "resume"
+ "setAND:"
+ "setK:"
+ "setN:"
+ "setOR:"
+ "setRequestID:"
+ "setSubmechanisms:"
+ "v24@0:8@?<v@?@\"NSArray\">16"
+ "v32@0:8@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?>24"
+ "v32@?0@\"<LACUIMechanism>\"8@\"<LACBackoffCounter>\"16@\"NSError\"24"
+ "v40@0:8@\"<LACRemoteUI>\"16@\"NSNumber\"24@?<v@?@\"<LACUIMechanism>\"@\"<LACBackoffCounter>\"@\"NSError\">32"
+ "v48@0:8@\"<LACRemoteUI>\"16@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\"24B32B36@?<v@?>40"
+ "v48@0:8@16@24B32B36@?40"
- "\x011"
- "\x05#1\x11\x12\x115"
- "\x06%\x11\x11\x11"
- "\x14"
- "%@ is pending"
- "%@ is running"
- "%@://%@"
- "@\"<LABackoffCounter>\""
- "@\"<LACEvaluationRequest>\""
- "@\"<LAContextExternalizationProt>\""
- "@\"<LARemoteUI>\""
- "@\"MechanismUI<LAUIMechanism><LARemoteUIHost>\""
- "@\"NSError\"8@?0"
- "LAContextExternalizationProt"
- "LARemoteUIHost"
- "LAUIMechanism"
- "Not clear for idle exit because %@."
- "T@\"<LABackoffCounter>\",&,N,V_backoffCounter"
- "T@\"<LAContextExternalizationProt>\",R,W,N,V_cachedExternalizationDelegate"
- "T@\"<LARemoteUI>\",W,N,V_remoteUiDelegate"
- "T@\"MechanismUI<LAUIMechanism><LARemoteUIHost>\",&,N,V_uiMechanism"
- "T@\"NSArray\",R,N,Vsubmechanisms"
- "TB,R,N,GisAND,VAND"
- "TB,R,N,GisOR,VOR"
- "TQ,R,N,Vk"
- "TQ,R,N,Vn"
- "UI idle-exit check failed: %{public}@"
- "UI idle-exit check: clear for %.0f ms (%@, %@)"
- "_assignPendingMechanism:reply:"
- "aqA\""
- "caller"
- "canRecoverFromError:request:"
- "checkClearForIdleExitWithCompletion:"
- "connectRemoteUI:reply:"
- "connectionToViewServiceInvalidated"
- "connectionToViewServiceInvalidated:"
- "current"
- "dateWithTimeIntervalSinceNow:"
- "deviceIsInBioLockout"
- "dismissRemoteUI:uiMechanism:uiDisappeared:reply:"
- "dismissRemoteUIWasInvalidated:completionHandler:"
- "errorNotSupported"
- "interactive"
- "of a new interactive request from %@"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"NSDate\"@\"NSError\">16"
- "v32@0:8@\"<LARemoteUI>\"16@?<v@?@\"<LAUIMechanism>\"@\"<LABackoffCounter>\"@\"NSError\">24"
- "v32@0:8@\"MechanismUI<LAUIMechanism><LARemoteUIHost>\"16@?<v@?B@\"NSError\">24"
- "v32@?0@\"<LAUIMechanism>\"8@\"<LABackoffCounter>\"16@\"NSError\"24"
- "v44@0:8@\"<LARemoteUI>\"16@\"MechanismUI<LAUIMechanism><LARemoteUIHost>\"24B32@?<v@?>36"
- "v44@0:8@16@24B32@?36"

```
