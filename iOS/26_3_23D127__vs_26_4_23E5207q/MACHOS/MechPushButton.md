## MechPushButton

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPushButton.bundle/MechPushButton`

```diff

-2005.80.10.0.0
-  __TEXT.__text: 0x1514
-  __TEXT.__auth_stubs: 0x200
-  __TEXT.__objc_stubs: 0x740
-  __TEXT.__objc_methlist: 0x238
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x124
-  __TEXT.__objc_methname: 0x7ed
-  __TEXT.__oslogstring: 0x1a3
+2005.100.174.0.0
+  __TEXT.__text: 0x198c
+  __TEXT.__auth_stubs: 0x230
+  __TEXT.__objc_stubs: 0x7a0
+  __TEXT.__objc_methlist: 0x250
+  __TEXT.__const: 0x78
+  __TEXT.__gcc_except_tab: 0x14
+  __TEXT.__cstring: 0xfd
+  __TEXT.__objc_methname: 0x870
+  __TEXT.__oslogstring: 0x1aa
   __TEXT.__objc_classname: 0x32
-  __TEXT.__objc_methtype: 0x190
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0x108
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x180
+  __TEXT.__objc_methtype: 0x1b1
+  __TEXT.__unwind_info: 0xc0
+  __DATA_CONST.__auth_got: 0x128
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__const: 0x28
+  __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x348
-  __DATA.__objc_selrefs: 0x2b8
+  __DATA.__objc_selrefs: 0x2d8
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 483213F8-7EE7-3F9E-9760-C7F0D6637467
+  UUID: E8807BE0-2552-335E-A1B2-2C93611ED7E4
   Functions: 23
-  Symbols:   53
-  CStrings:  172
+  Symbols:   66
+  CStrings:  175
 
Symbols:
+ _LACDarwinNotificationIntentNotWaiting
+ _LACDarwinNotificationIntentWaiting
+ _LACErrorCodeDoublePressRequired
+ _LACEventParamCredentialPresent
+ _LACEventPushButton
+ _LACEventPushButtonSecondary
+ _LACLogEvaluationMechanism
+ _LACPolicyDoublePressBypass
+ _LACPolicyOptionIgnoreExistingDoublePress
+ _LACPolicyOptionSkipDoublePress
+ _OBJC_CLASS_$_LACError
+ _OBJC_CLASS_$_LACMutableEvaluationEventValuePushButtonStatus
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___objc_personality_v0
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_opt_new
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x20
+ _objc_retain_x21
- _LALogForCategory
- _OBJC_CLASS_$_LAErrorHelper
- _OBJC_CLASS_$_NSConstantIntegerNumber
- __NSConcreteGlobalBlock
- _dispatch_once
- _objc_claimAutoreleasedReturnValue
- _objc_release_x1
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "%{public}@ will honor LACPolicyOptionPushButtonUseMaxPreArmAge request"
+ "_runWithHints:"
+ "client decides to not reuse"
+ "errorWithCode:debugDescription:"
+ "handleEvaluationEvent:value:"
+ "runWithHints:eventHandler:activationCompletion:reply:"
+ "setIsCredentialPresent:"
+ "v24@0:8@16"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v48@0:8@16@24@?32@?40"
- "%{public}@ will honor LAOptionPushButtonUseMaxPreArmAge request"
- "com.apple.LocalAuthentication.intent.not-waiting"
- "com.apple.LocalAuthentication.intent.waiting"
- "errorWithCode:message:"
- "q"
- "v8@?0"

```
