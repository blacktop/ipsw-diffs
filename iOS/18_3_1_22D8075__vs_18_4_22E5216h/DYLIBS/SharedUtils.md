## SharedUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils`

```diff

-1656.80.6.0.0
-  __TEXT.__text: 0x1fc54
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0xc08
-  __TEXT.__const: 0x218
-  __TEXT.__cstring: 0x28b8
-  __TEXT.__oslogstring: 0xbae
-  __TEXT.__gcc_except_tab: 0x2ac
-  __TEXT.__unwind_info: 0x830
-  __TEXT.__objc_classname: 0x451
-  __TEXT.__objc_methname: 0x295a
-  __TEXT.__objc_methtype: 0x114b
-  __TEXT.__objc_stubs: 0x1900
-  __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0x7b0
-  __DATA_CONST.__objc_classlist: 0xd0
-  __DATA_CONST.__objc_protolist: 0xf0
+1656.100.222.0.0
+  __TEXT.__text: 0x1d48c
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_methlist: 0x102c
+  __TEXT.__const: 0x220
+  __TEXT.__cstring: 0x2566
+  __TEXT.__oslogstring: 0xa74
+  __TEXT.__gcc_except_tab: 0x274
+  __TEXT.__unwind_info: 0x7a8
+  __TEXT.__objc_classname: 0x3fa
+  __TEXT.__objc_methname: 0x25a5
+  __TEXT.__objc_methtype: 0x10e2
+  __TEXT.__objc_stubs: 0x1680
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__const: 0x628
+  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9d0
-  __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x338
+  __DATA_CONST.__objc_selrefs: 0xa78
+  __DATA_CONST.__objc_protorefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x68
+  __AUTH_CONST.__auth_got: 0x2e0
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x1240
-  __AUTH_CONST.__objc_const: 0x29a8
-  __AUTH_CONST.__objc_intobj: 0x9c0
+  __AUTH_CONST.__const: 0x340
+  __AUTH_CONST.__cfstring: 0xca0
+  __AUTH_CONST.__objc_const: 0x1ce8
+  __AUTH_CONST.__objc_intobj: 0x900
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xa4
-  __DATA.__data: 0xb51
-  __DATA.__bss: 0xf0
+  __DATA.__objc_ivar: 0x8c
+  __DATA.__data: 0xa91
+  __DATA.__bss: 0xd8
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x780
+  __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0xb0
+  __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 630
-  Symbols:   849
-  CStrings:  1119
+  Functions: 691
+  Symbols:   894
+  CStrings:  1012
 
Symbols:
+ _LACLogService
+ _OBJC_CLASS_$_LACPolicyUtilities
+ _OBJC_CLASS_$_LACXPCInterface
+ _objc_retain_x6
- _LACErrorCodeInternal
- _LACLogContext
- _LACPolicyIsLocationBasedPolicy
- _MKBGetDeviceLockStateInfo
- _MKBKeyBagKeyStashCreateWithManifest
- _MKBKeyBagKeyStashCreateWithMode
- _MKBUnlockDevice
- _MKBVerifyPasswordWithContext
- _NSStringFromMechanismEvent
- _NSStringFromMechanismEventAndValue
- _NSStringFromRemoteUIEvent
- _NSStringFromRemoteUIEventAndOptions
- _OBJC_CLASS_$_LACError
- _OBJC_CLASS_$_LACKeyBagProvider
- _OBJC_CLASS_$_LACachedExternalizedContext
- _OBJC_CLASS_$_LALocalBackoffCounter
- _OBJC_CLASS_$_NSDate
- _OBJC_METACLASS_$_LACachedExternalizedContext
- _OBJC_METACLASS_$_LALocalBackoffCounter
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _getuid
- _kMKBInfoBackOff
- _objc_opt_respondsToSelector
- _objc_retain_x28
CStrings:
+ "LACContextCallbackXPC"
+ "LACContextExternalizing"
+ "LACRemoteUI"
+ "LACRemoteUIHost"
+ "LACUIMechanism"
+ "LocationBasedTrustComputer"
+ "analyticsAction:dismissing:reply:"
+ "analyticsMechanism:result:reply:"
+ "analyticsMechanism:starting:reply:"
+ "analyticsSessionStarting:dialogID:bundleID:reply:"
+ "checkHasPendingUIRequestsWithCompletion:"
+ "connectRemoteUI:requestID:reply:"
+ "dismissRemoteUIWithIdleEndpoint:wasInvalidated:completionHandler:"
+ "interfaceForXPCProtocol:"
+ "v24@0:8@?<v@?@\"NSArray\">16"
+ "v36@0:8@\"NSXPCListenerEndpoint\"16B24@?<v@?>28"
+ "v36@0:8@16B24@?28"
+ "v40@0:8@\"<LACRemoteUI>\"16@\"NSNumber\"24@?<v@?@\"<LACUIMechanism>\"@\"<LACBackoffCounter>\"@\"NSError\">32"
+ "v44@0:8B16@\"NSString\"20@\"NSString\"28@?<v@?B@\"NSError\">36"
+ "v44@0:8B16@20@28@?36"
+ "v48@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
+ "v64@0:8@\"NSUUID\"16@\"<LACContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"
+ "verifyPasscodeUsingAKS:acmContext:userId:policy:options:bioLockoutRecovery:"
+ "verifyPasscodeUsingPAM:userID:pamService:pamUser:pamToken:"
- "%{public}@ has %d failed passcode attempts out of %d"
- ", options: %@"
- ", value: %@"
- "@\"<LAContextExternalizationObserverProt>\""
- "@\"<LAContextExternalizationProt>\""
- "@\"LACKeyBagProvider\""
- "@\"NSData\""
- "@24@0:8@?<v@?@\"NSError\">16"
- "@32@0:8@16q24"
- "B24@0:8q16"
- "B28@0:8q16B24"
- "BiometryLockout"
- "BiometryMatch"
- "BiometryNoMatch"
- "BiometryPresenceDetectionIn"
- "BiometryPresenceDetectionOut"
- "BiometrySensorActive"
- "BiometrySensorInactive"
- "Bootstrap"
- "CancelButtonPressed"
- "CoachingFeedback"
- "ContinueButtonPressed"
- "DeviceHandle"
- "DidAppear"
- "DidDisappear"
- "DismissButtonPressed"
- "FaceIdHighTemperature"
- "FaceIdLowPower"
- "FaceIdLowTemperature"
- "FaceIdSilentFallback"
- "Failed to fetch ratchet state and config (stat: %d)"
- "Failed to get externalized context: %{public}@"
- "Failure"
- "FallbackButtonPressed"
- "GotFocus"
- "HomeGestureInJindoForStockholm"
- "I24@0:8@16"
- "Invalid LAMechanismEvent: %d"
- "Invalid LARemoteUIEvent: %d"
- "Invalid string (%@)"
- "LABackoffCounter"
- "LACachedExternalizedContext"
- "LAContextCallbackXPC"
- "LAContextExternalizationProt"
- "LALocalBackoffCounter"
- "LARemoteUI"
- "LARemoteUIHost"
- "LAServiceKit"
- "LAUIMechanism"
- "LostFocus"
- "MKB device unlock for keybag %d returned %d"
- "MKB password verification for keybag %d returned %d"
- "Missing ACM context"
- "Missing externalizationDelegate"
- "NSXPCProxyCreating"
- "None"
- "Passcode backoff"
- "PasscodeRejected"
- "PasscodeVerified"
- "PushButtonDoubleClicked"
- "PushButtonExpired"
- "RetryButtonPressed"
- "RetryTime"
- "SecureUIMoved"
- "SecurityDelayBegan"
- "SecurityDelayEnded"
- "StartedTypingPasscode"
- "T@\"<LAContextExternalizationObserverProt>\",W,N,V_externalizationObserver"
- "T@\"NSData\",&,V_cachedExternalizedContext"
- "T@\"NSData\",R,N"
- "WatchApproved"
- "_backoffEndTimeDictionary"
- "_cachedExternalizedContext"
- "_currentUserID"
- "_errorFromACMStatus:"
- "_externalizationDelegate"
- "_externalizationObserver"
- "_failedAttemptsDictionary"
- "_increaseFailedAttemptCountForUserID:"
- "_keyBagProvider"
- "_keybagHandleForUserId:"
- "_passwordPolicyStatusForUserID:"
- "_resetFailedAttemptCountForUserID:"
- "_verifyPasswordUsingMKB:acmContext:userId:options:log:"
- "actionBackoffWithReply:"
- "actionFailureWithReply:"
- "actionSuccess"
- "backoff: %{public}@"
- "cachedExternalizedContext"
- "checkClearForIdleExitWithCompletion:"
- "connectRemoteUI:reply:"
- "contextWasExternalized:"
- "create stash with manifest: %d"
- "create stash with mode: %d"
- "current user"
- "currentBackoffErrorWithReply:"
- "date"
- "dateByAddingTimeInterval:"
- "dateWithTimeIntervalSinceNow:"
- "dismissRemoteUIWasInvalidated:completionHandler:"
- "doubleValue"
- "errorWithCode:debugDescription:"
- "externalizationObserver"
- "externalizedContext"
- "externalizedContextWithError:"
- "i56@0:8@16@24@32@40@48"
- "initWithExternalizationDelegate:"
- "invalidateBecauseOfInvalidConnection:"
- "isApplePayPolicy:inApp:"
- "isBiometricOnlyPolicy:"
- "isLocationBasedPolicy:"
- "isPolicyAcceptingEmptyPassword:"
- "q20@0:8i16"
- "rangeOfComposedCharacterSequencesForRange:"
- "ratchetStatusWithConfig:"
- "remoteObjectProxy"
- "removeObjectForKey:"
- "setCachedExternalizedContext:"
- "setExternalizationObserver:"
- "substringWithRange:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "truncateString:maxLength:"
- "updatePasscodeSuccessAgeWithCurrentSystemUptime"
- "user %d"
- "v20@0:8B16"
- "v24@0:8@?<v@?@\"NSDate\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@?0@\"NSData\"8@\"NSError\"16"
- "v32@0:8@\"<LARemoteUI>\"16@?<v@?@\"<LAUIMechanism>\"@\"<LABackoffCounter>\"@\"NSError\">24"
- "v48@0:8@\"NSData\"16@\"<LAContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
- "v64@0:8@\"NSUUID\"16@\"<LAContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"

```
