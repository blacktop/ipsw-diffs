## coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

-2005.0.31.0.0
-  __TEXT.__text: 0x3c168
-  __TEXT.__auth_stubs: 0xe60
-  __TEXT.__objc_stubs: 0x36c0
-  __TEXT.__objc_methlist: 0x1a0c
+2005.0.40.0.0
+  __TEXT.__text: 0x3adc0
+  __TEXT.__auth_stubs: 0xe50
+  __TEXT.__objc_stubs: 0x3420
+  __TEXT.__objc_methlist: 0x1954
   __TEXT.__const: 0x1350
-  __TEXT.__objc_methname: 0x4789
-  __TEXT.__cstring: 0x49da
-  __TEXT.__objc_classname: 0x6cc
-  __TEXT.__objc_methtype: 0x1f5b
-  __TEXT.__gcc_except_tab: 0x26c
-  __TEXT.__oslogstring: 0x17b3
-  __TEXT.__unwind_info: 0xc98
-  __DATA_CONST.__auth_got: 0x740
-  __DATA_CONST.__got: 0x4b8
+  __TEXT.__objc_methname: 0x45bb
+  __TEXT.__cstring: 0x493f
+  __TEXT.__objc_classname: 0x6c9
+  __TEXT.__objc_methtype: 0x1f07
+  __TEXT.__gcc_except_tab: 0x1dc
+  __TEXT.__oslogstring: 0x15de
+  __TEXT.__unwind_info: 0xc68
+  __DATA_CONST.__auth_got: 0x738
+  __DATA_CONST.__got: 0x498
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x2220
-  __DATA_CONST.__cfstring: 0xe00
+  __DATA_CONST.__const: 0x2130
+  __DATA_CONST.__cfstring: 0xdc0
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x60
+  __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0xc0
-  __DATA.__objc_const: 0x79e0
-  __DATA.__objc_selrefs: 0x1140
-  __DATA.__objc_ivar: 0x188
+  __DATA.__objc_const: 0x7908
+  __DATA.__objc_selrefs: 0x10b8
+  __DATA.__objc_ivar: 0x178
   __DATA.__objc_data: 0x9b0
   __DATA.__data: 0x1ab8
-  __DATA.__bss: 0x180
+  __DATA.__bss: 0x150
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 78427601-F27D-349E-B89D-5868692DC69C
-  Functions: 1465
-  Symbols:   395
-  CStrings:  1932
+  UUID: 4811CC61-DB90-342E-AF1B-52DDEE61E755
+  Functions: 1435
+  Symbols:   390
+  CStrings:  1888
 
Symbols:
+ _OBJC_CLASS_$_LACAnalyticsServiceXPCHost
- _LACErrorCodeRequestFailed
- _NSStringFromClass
- _OBJC_CLASS_$_LACAnalyticsData
- _OBJC_CLASS_$_LACAnalyticsSession
- _OBJC_CLASS_$_NSHashTable
- _OBJC_CLASS_$_NSPredicate
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
+ "sessionForContextUUID:"
+ "setInterface:forSelector:argumentIndex:ofReply:"
+ "startSessionForContext:dialogID:bundleID:reply:"
+ "trackEvaluationAnalytics:"
+ "updateContextUUID:reply:"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"<LACAnalyticsSessionXPC>\"@\"NSError\">24"
+ "v48@0:8@\"NSUUID\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"<LACAnalyticsSessionXPC>\"@\"NSError\">40"
- "%{public}@ created for %{public}@ uid:%d"
- "%{public}@ has received newValue: %{public}@, oldValue: %{public}@, notifying PID %d"
- "%{public}@ will %{public}s"
- "%{public}@ will suspend"
- "<%@ %p: className:%@, suspended:%d, PID:%d>"
- "@\"<LANotificationObserverXPC>\""
- "@\"LACAnalyticsSession\""
- "@\"NSHashTable\""
- "@36@0:8@16i24@28"
- "Added notification observer from PID %d for notification class %{public}@"
- "B24@?0@\"Notification\"8@\"NSDictionary\"16"
- "Clearing unexpected notification: %{public}@, pending: %{public}@"
- "LACLegacyNotificationPosting"
- "LANotificationObserverXPC"
- "LANotificationXPC"
- "No active analytics session."
- "No analytics session to finish."
- "Notification"
- "Posted notification %{public}@, newValue: %{public}@, oldValue: %{public}@"
- "Posting notification %{public}@, newValue: %{public}@, oldValue: %{public}@"
- "T@\"<LANotificationObserverXPC>\",R,N,V_observer"
- "T@\"NSHashTable\",R,N,V_notifications"
- "T@\"NSString\",R,N,V_className"
- "TB,R,N,V_suspended"
- "Timeout waiting for confirmation from: %@"
- "_analyticsSession"
- "_className"
- "_clearNotification:fromPendingNotifications:finally:"
- "_notifications"
- "_observer"
- "_observerPid"
- "_suspended"
- "addNotificationObserver:className:completionHandler:"
- "allObjects"
- "analyticsAction:dismissing:reply:"
- "analyticsMechanism:result:reply:"
- "analyticsMechanism:starting:reply:"
- "analyticsSessionStarting:dialogID:bundleID:reply:"
- "arrayWithArray:"
- "authenticationAction:dismissing:"
- "authenticationResult:event:"
- "authenticationStartedForEvent:"
- "className"
- "containsObject:"
- "filteredArrayUsingPredicate:"
- "finish"
- "initWithDialogID:bundleID:"
- "initWithObserver:observerPid:className:"
- "newValue:oldValue:completionHandler:"
- "notifications"
- "observer"
- "postNotificationOfClassNamed:newValue:oldValue:completionHandler:"
- "predicateWithBlock:"
- "removeAllObjects"
- "resume and notify observer"
- "resumeAndNotify:completionHandler:"
- "setAnalyticsData:"
- "setDirty:"
- "setNotificationManager:"
- "setSession:"
- "suspendWithCompletionHandler:"
- "suspended"
- "v24@0:8@?<v@?>16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?>20"
- "v40@0:8@\"<LANotificationObserverXPC>\"16@\"NSString\"24@?<v@?@\"<LANotificationXPC>\"@\"NSError\">32"
- "v40@0:8@16@24@?<v@?>32"
- "v44@0:8B16@\"NSString\"20@\"NSString\"28@?<v@?B@\"NSError\">36"
- "v44@0:8B16@20@28@?36"
- "v48@0:8@\"NSString\"16@24@32@?<v@?>40"
- "weakObjectsHashTable"

```
