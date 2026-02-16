## MechTouchId

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechTouchId.bundle/MechTouchId`

```diff

-2005.80.10.0.0
-  __TEXT.__text: 0x2834
-  __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_stubs: 0xd80
+2005.100.174.0.0
+  __TEXT.__text: 0x3544
+  __TEXT.__auth_stubs: 0x2b0
+  __TEXT.__objc_stubs: 0xe80
   __TEXT.__objc_methlist: 0x314
-  __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__cstring: 0xdf
-  __TEXT.__objc_methname: 0xd1c
-  __TEXT.__oslogstring: 0x23c
+  __TEXT.__const: 0x90
+  __TEXT.__gcc_except_tab: 0xdc
+  __TEXT.__cstring: 0x109
+  __TEXT.__objc_methname: 0xe1d
+  __TEXT.__oslogstring: 0x271
   __TEXT.__objc_classname: 0x92
-  __TEXT.__objc_methtype: 0x238
-  __TEXT.__unwind_info: 0x120
-  __DATA_CONST.__auth_got: 0x148
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x168
+  __TEXT.__objc_methtype: 0x24e
+  __TEXT.__unwind_info: 0x158
+  __DATA_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x1c8
-  __DATA.__objc_const: 0x3e0
-  __DATA.__objc_selrefs: 0x488
-  __DATA.__objc_ivar: 0x28
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA.__objc_const: 0x3b0
+  __DATA.__objc_selrefs: 0x4c8
+  __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 60D73049-F8BC-3DA6-8C29-0F4DB154D106
-  Functions: 44
-  Symbols:   63
-  CStrings:  247
+  UUID: 8961317A-B743-378E-A8F9-C22686EE7E77
+  Functions: 47
+  Symbols:   101
+  CStrings:  256
 
Symbols:
+ _LACErrorCodeAuthenticationFailed
+ _LACErrorCodeSystemCancel
+ _LACErrorCodeWrongAuthentication
+ _LACErrorSubcodeBiometryFailedToStart
+ _LACEventParamTouchIDLockoutError
+ _LACEventParamTouchIDSimpleStatus
+ _LACEventSimpleStatusTouchIDFingerDetectBegin
+ _LACEventSimpleStatusTouchIDFingerDetectTimeoutExpired
+ _LACEventSimpleStatusTouchIDFingerDetectTimeoutSet
+ _LACEventSimpleStatusTouchIDFingerOff
+ _LACEventSimpleStatusTouchIDFingerOn
+ _LACEventSimpleStatusTouchIDLiftFinger
+ _LACEventSimpleStatusTouchIDMatch
+ _LACEventSimpleStatusTouchIDNoMatch
+ _LACEventSimpleStatusTouchIDSensorActive
+ _LACEventSimpleStatusTouchIDSensorInactive
+ _LACEventSimpleStatusTouchIDUnboundMatch
+ _LACPolicyOptionFingerDetectLength
+ _LACPolicyOptionFingerMustBeOff
+ _LACPolicyOptionMatchForUnlock
+ _LACPolicyOptionMaxBiometryFailures
+ _LACPolicyOptionNoFailureUI
+ _LACPolicyOptionReturnBiometryDatabaseHash
+ _LACPolicyStockholm
+ _LACPurposeNone
+ _LACPurposeUnlock
+ _LACResultBiometryCredentialAdded
+ _LACResultBiometryDatabaseHash
+ _LACResultBiometryKeyBagUnlock
+ _LACResultBiometryLockout
+ _LACResultPassedBiometry
+ _LACResultUserID
+ _OBJC_CLASS_$_LACError
+ _OBJC_CLASS_$_LACFlags
+ _OBJC_CLASS_$_LACMutableEvaluationEventValueBiometricStatus
+ _OBJC_CLASS_$_LACPasscodeHelper
+ _objc_opt_new
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x21
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x27
- _OBJC_CLASS_$_LAErrorHelper
- _OBJC_CLASS_$_LAPasscodeHelper
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "Will not activate %@ at this moment, event is paused"
+ "_runWithHints"
+ "errorWithCode:debugDescription:"
+ "errorWithCode:subcode:underlyingError:debugDescription:"
+ "errorWithCode:underlyingError:debugDescription:"
+ "featureFlagPresentationContextEnabled"
+ "handleBiometricStatusEventWithValue:completion:"
+ "handleEvaluationEvent:value:"
+ "isEventPaused:"
+ "runWithHints:eventHandler:activationCompletion:reply:"
+ "setLockoutError:"
+ "setMatchingStatus:"
+ "setPayload:"
+ "v12@?0B8"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v48@0:8@16@24@?32@?40"
- "TB,N,V_hasUI"
- "_hasUI"
- "errorWithCode:message:"
- "errorWithCode:message:suberror:"
- "errorWithCode:subcode:message:suberror:"
- "setHasUI:"

```
