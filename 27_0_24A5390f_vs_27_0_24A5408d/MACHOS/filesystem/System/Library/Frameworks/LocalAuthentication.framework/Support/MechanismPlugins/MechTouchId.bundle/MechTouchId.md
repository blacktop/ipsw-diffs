## MechTouchId

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechTouchId.bundle/MechTouchId`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2319.0.46.0.0
-  __TEXT.__text: 0x3244
-  __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_stubs: 0xe80
-  __TEXT.__objc_methlist: 0x2fc
+2319.0.63.0.0
+  __TEXT.__text: 0x3d18
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_stubs: 0x1080
+  __TEXT.__objc_methlist: 0x334
   __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__cstring: 0x10c
-  __TEXT.__objc_methname: 0xde2
-  __TEXT.__oslogstring: 0x271
+  __TEXT.__gcc_except_tab: 0xf4
+  __TEXT.__cstring: 0x127
+  __TEXT.__objc_methname: 0xfa3
+  __TEXT.__oslogstring: 0x33b
   __TEXT.__objc_classname: 0x8d
-  __TEXT.__objc_methtype: 0x23d
-  __TEXT.__unwind_info: 0x148
-  __DATA_CONST.__const: 0x1b8
-  __DATA_CONST.__cfstring: 0x1a0
+  __TEXT.__objc_methtype: 0x261
+  __TEXT.__unwind_info: 0x170
+  __DATA_CONST.__const: 0x260
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0x168
-  __DATA_CONST.__got: 0x180
-  __DATA.__objc_const: 0x380
-  __DATA.__objc_selrefs: 0x4c8
-  __DATA.__objc_ivar: 0x20
+  __DATA_CONST.__auth_got: 0x170
+  __DATA_CONST.__got: 0x1d0
+  __DATA.__objc_const: 0x3e0
+  __DATA.__objc_selrefs: 0x550
+  __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 45
-  Symbols:   101
-  CStrings:  239
+  Functions: 56
+  Symbols:   112
+  CStrings:  267
 
Symbols:
+ _LACErrorCodeDoublePressRequired
+ _LACErrorSubcodeLostFocus
+ _LACEventParamCredentialPresent
+ _LACEventPushButton
+ _LACPolicyOptionSkipDoublePress
+ _LACResultPushButtonPressed
+ _OBJC_CLASS_$_LACACMHelper
+ _OBJC_CLASS_$_LACMutableEvaluationEventValuePushButtonStatus
+ _OBJC_CLASS_$_NSDate
+ ___kCFBooleanFalse
+ __os_log_error_impl
+ _objc_alloc
- _objc_retain_x4
CStrings:
+ "%{public}@ cached match expired while waiting for the double press"
+ "%{public}@ failed to query push button credential: %{public}@"
+ "%{public}@ state changed to %d"
+ "%{public}@ will not restart in biolockout"
+ "@\"NSDate\""
+ "@\"NSDictionary\""
+ "@\"NSUUID\""
+ "Double press is required."
+ "_expireMatchThatStartedAt:"
+ "_hasDoublePressPrecondition"
+ "_matchIdentityUUID"
+ "_matchResult"
+ "_runWithHints:eventHandler:"
+ "_scheduleMatchExpirationWithResult:identityUUID:"
+ "_startedMatching"
+ "acmContext"
+ "biolockout"
+ "canRecoverFromError:"
+ "checkCredentialValid"
+ "companionStateChanged:newState:"
+ "date"
+ "error:hasCode:subcode:"
+ "initWithACMContext:"
+ "isCredentialOfTypeSet:error:"
+ "isLastRestartAttempt"
+ "preCompanion"
+ "prepareForRestart"
+ "runWithHints:eventHandler:reply:"
+ "setIsCredentialPresent:"
- "_runWithHints"
```
