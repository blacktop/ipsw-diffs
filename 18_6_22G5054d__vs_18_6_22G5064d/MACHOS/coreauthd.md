## coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

-1656.140.3.0.0
-  __TEXT.__text: 0x228e8
+1656.140.4.0.0
+  __TEXT.__text: 0x22704
   __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_stubs: 0x3260
-  __TEXT.__objc_methlist: 0x1944
+  __TEXT.__objc_stubs: 0x31a0
+  __TEXT.__objc_methlist: 0x1994
   __TEXT.__const: 0x158
-  __TEXT.__objc_methname: 0x4241
-  __TEXT.__cstring: 0x259c
-  __TEXT.__objc_classname: 0x6a7
-  __TEXT.__objc_methtype: 0x1eb5
+  __TEXT.__objc_methname: 0x4320
+  __TEXT.__cstring: 0x2577
+  __TEXT.__objc_classname: 0x6fa
+  __TEXT.__objc_methtype: 0x1f94
   __TEXT.__gcc_except_tab: 0x210
   __TEXT.__oslogstring: 0x150a
-  __TEXT.__unwind_info: 0x7a8
+  __TEXT.__unwind_info: 0x7a0
   __DATA_CONST.__auth_got: 0x3c0
-  __DATA_CONST.__got: 0x3e8
+  __DATA_CONST.__got: 0x3d8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0xab8
-  __DATA_CONST.__cfstring: 0xae0
-  __DATA_CONST.__objc_classlist: 0xf0
-  __DATA_CONST.__objc_protolist: 0x180
+  __DATA_CONST.__cfstring: 0xac0
+  __DATA_CONST.__objc_classlist: 0xf8
+  __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_protorefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0xc0
-  __DATA.__objc_const: 0x72f8
-  __DATA.__objc_selrefs: 0x1028
-  __DATA.__objc_ivar: 0x168
-  __DATA.__objc_data: 0x960
-  __DATA.__data: 0x1202
+  __DATA.__objc_const: 0x77d8
+  __DATA.__objc_selrefs: 0x1038
+  __DATA.__objc_ivar: 0x16c
+  __DATA.__objc_data: 0x9b0
+  __DATA.__data: 0x1322
   __DATA.__bss: 0x110
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 30784051-00F0-3734-A98A-65C77C3A6C83
-  Functions: 770
-  Symbols:   257
-  CStrings:  1470
+  UUID: 7E173384-68A3-3A4C-AA7D-1560E9A40CE4
+  Functions: 768
+  Symbols:   255
+  CStrings:  1481
 
Symbols:
+ _OBJC_CLASS_$_LACAnalyticsServiceXPCHost
+ _OBJC_CLASS_$_LACConcurrencyUtilities
- _LACErrorCodeRequestFailed
- _OBJC_CLASS_$_LACAnalyticsData
- _OBJC_CLASS_$_LACAnalyticsSession
- _OBJC_CLASS_$_LACError
CStrings:
+ "\t"
+ "%{public}@ created for %{public}@ uid:%u"
+ "@\"<LACAnalyticsService>\""
+ "@\"<LACAnalyticsServiceXPC>\"16@0:8"
+ "@\"LACAnalyticsServiceXPCHost\""
+ "@\"LACAnalyticsSession\"24@0:8@\"NSUUID\"16"
+ "AnalyticsService"
+ "LACAnalyticsService"
+ "LACAnalyticsServiceXPC"
+ "LACAnalyticsSessionXPC"
+ "T@\"<LACAnalyticsService>\",R,N,V_analytics"
+ "T@\"<LACAnalyticsServiceXPC>\",R,N"
+ "T@\"<LACAnalyticsServiceXPC>\",R,N,V_xpcController"
+ "_analyticsSessionForEvaluationRequest:"
+ "authenticationAction:failing:reply:"
+ "authenticationAttemptFailedForEvent:reply:"
+ "authenticationStartedForEvent:reply:"
+ "authenticationSuccessfulForEvent:reply:"
+ "connectSessionForContext:reply:"
+ "daemonQueue"
+ "finishWithReply:"
+ "initWithAnalyticsSession:"
+ "kLAServiceTypeAnalytics"
+ "serviceLocator"
+ "sessionForContextUUID:"
+ "setInterface:forSelector:argumentIndex:ofReply:"
+ "startSessionForContext:dialogID:bundleID:reply:"
+ "trackEvaluationAnalytics:"
+ "updateContextUUID:reply:"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"<LACAnalyticsSessionXPC>\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?B@\"NSError\">24"
+ "v48@0:8@\"NSUUID\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"<LACAnalyticsSessionXPC>\"@\"NSError\">40"
- "%{public}@ created for %{public}@ uid:%d"
- "@\"LACAnalyticsSession\""
- "No active analytics session."
- "No analytics session to finish."
- "_analyticsSession"
- "analyticsAction:dismissing:reply:"
- "analyticsMechanism:result:reply:"
- "analyticsMechanism:starting:reply:"
- "analyticsSessionStarting:dialogID:bundleID:reply:"
- "authenticationAction:dismissing:"
- "authenticationResult:event:"
- "authenticationStartedForEvent:"
- "errorWithCode:debugDescription:"
- "finish"
- "initWithDialogID:bundleID:"
- "setAnalyticsData:"
- "setDirty:"
- "setSession:"
- "v44@0:8B16@\"NSString\"20@\"NSString\"28@?<v@?B@\"NSError\">36"
- "v44@0:8B16@20@28@?36"

```
