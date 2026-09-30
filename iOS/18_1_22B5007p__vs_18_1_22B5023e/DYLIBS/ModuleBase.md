## ModuleBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase`

```diff

-1656.0.83.0.0
-  __TEXT.__text: 0x4330
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0x4c4
-  __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x65d
-  __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__oslogstring: 0x2d6
-  __TEXT.__unwind_info: 0x188
+1656.40.15.0.0
+  __TEXT.__text: 0x4c28
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_methlist: 0x51c
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x6b1
+  __TEXT.__gcc_except_tab: 0x74
+  __TEXT.__oslogstring: 0x405
+  __TEXT.__unwind_info: 0x198
   __TEXT.__objc_classname: 0xd1
-  __TEXT.__objc_methname: 0x1534
-  __TEXT.__objc_methtype: 0x763
-  __TEXT.__objc_stubs: 0xdc0
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0xe0
+  __TEXT.__objc_methname: 0x1769
+  __TEXT.__objc_methtype: 0x7be
+  __TEXT.__objc_stubs: 0xf80
+  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x508
+  __DATA_CONST.__objc_selrefs: 0x580
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x230
+  __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x7a0
-  __AUTH_CONST.__objc_const: 0xf20
-  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__cfstring: 0x860
+  __AUTH_CONST.__objc_const: 0xfb0
+  __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x8c
+  __DATA.__objc_ivar: 0x98
   __DATA.__data: 0x180
   __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x140

   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 113
-  Symbols:   225
-  CStrings:  441
+  Functions: 121
+  Symbols:   241
+  CStrings:  478
 
Symbols:
+ _LACErrorCodeInternal
+ _LACErrorCodeTimeout
+ _LACLightweightUIModeNone
+ _OBJC_CLASS_$_LACClientInfoProvider
+ _OBJC_CLASS_$_LACError
+ _OBJC_CLASS_$_NSDateFormatter
+ _getuid
+ _objc_retain_x27
CStrings:
+ "\a2\x11"
+ ", "
+ "<AuthenticationInProgress: %!p(MISSING); pid:%!u(MISSING), %!@(MISSING)>"
+ "@\"<LACEvaluationRequest>\""
+ "@\"LACClientInfo\""
+ "@40@0:8@16@24@32"
+ "@72@0:8@16q24@32@40@48@56@?64"
+ "Enqueued %!@(MISSING) after %!@(MISSING)"
+ "Inconsistent authentication binding, %!@(MISSING) is not enqueued after %!@(MISSING)"
+ "T@\"AuthenticationInProgress\",R,N,V_enqueuedAuthentication"
+ "T@\"LACClientInfo\",R,N"
+ "The enqueued authentication will fail with the same error as %!{(MISSING)public}@ -> %!{(MISSING)public}@"
+ "The enqueued authentication will start because the previous authentication has finished successfully."
+ "Ti,R,N,V_originatorPid"
+ "Will enqueue authentication by '%!{(MISSING)public}@'"
+ "Will not enqueue '%!{(MISSING)public}@', PA is '%!{(MISSING)public}@'"
+ "_clientInfo"
+ "_enqueuedAuthentication"
+ "_handleCompletionOfAuthentication:result:error:"
+ "_isInteractiveEvaluationWithinProtectedAppsEvaluation:"
+ "_request"
+ "authenticateForPolicy:constraintData:internalInfo:uiDelegate:originator:request:mechanism:reply:"
+ "bundleId"
+ "client"
+ "clientInfo"
+ "componentsJoinedByString:"
+ "enqueueAuthentication:"
+ "enqueued: %!@(MISSING)"
+ "enqueuedAuthentication"
+ "errorWithCode:debugDescription:"
+ "i16@0:8"
+ "infoForXPCClient:evaluationOptions:"
+ "initWithMechanism:policy:uiDelegate:originator:request:internalInfo:reply:"
+ "localizedStringFromDate:dateStyle:timeStyle:"
+ "originatorPid"
+ "priority: %!@(MISSING)"
+ "request"
+ "retryingForError"
+ "shouldDequeueAndRunAfterAuthentication:result:error:"
+ "shouldEnqueueAuthentication:"
+ "started: %!@(MISSING)"
+ "uid: %!u(MISSING)"
+ "v40@0:8@16@24@32"
+ "v80@0:8q16@24@32@40@48@56@64@?72"
- "\x03\x12\""
- "<AuthenticationInProgress: %!p(MISSING) [pid:%!@(MISSING), uid:%!@(MISSING), started:%!@(MISSING), priority:%!@(MISSING)]>"
- "@64@0:8@16q24@32@40@48@?56"
- "_handleCompletionOfAuthentication:"
- "authenticateForPolicy:constraintData:internalInfo:uiDelegate:originator:mechanism:reply:"
- "initWithMechanism:policy:uiDelegate:originator:internalInfo:reply:"
- "v72@0:8q16@24@32@40@48@56@?64"

```
