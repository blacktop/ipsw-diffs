## EyeRelief

> `/System/Library/PrivateFrameworks/EyeRelief.framework/EyeRelief`

```diff

-32.0.0.0.0
-  __TEXT.__text: 0x2f34
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x53c
+34.0.0.0.0
+  __TEXT.__text: 0x2c88
+  __TEXT.__objc_methlist: 0x554
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__cstring: 0x5ce
+  __TEXT.__cstring: 0x5f4
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x1c0
-  __TEXT.__objc_classname: 0xbe
-  __TEXT.__objc_methname: 0xe12
-  __TEXT.__objc_methtype: 0x2ac
-  __TEXT.__objc_stubs: 0x9a0
-  __DATA_CONST.__got: 0x90
+  __TEXT.__unwind_info: 0x198
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x208
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b8
+  __DATA_CONST.__objc_selrefs: 0x3c0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0x90
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x460
+  __AUTH_CONST.__cfstring: 0x480
   __AUTH_CONST.__objc_const: 0x9b8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x4c
   __DATA.__data: 0x124

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 76070EAF-5FB8-3BC8-909A-13ECFE675E17
+  UUID: B74B6EE5-A23A-3054-821B-B03672030E3F
   Functions: 111
-  Symbols:   488
-  CStrings:  300
+  Symbols:   492
+  CStrings:  87
 
Symbols:
+ -[ERAttentionAwarenessClient dealloc]
+ -[EREyeReliefEngine dealloc]
+ GCC_except_table10
+ GCC_except_table5
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x25
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x21
+ _objc_retain_x8
- GCC_except_table9
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
CStrings:
+ "Failed to invalidate AA: %@"
- "#16@0:8"
- ".cxx_destruct"
- "@\"AWAttentionAwarenessClient\""
- "@\"AWAttentionAwarenessConfiguration\""
- "@\"ERAttentionAwarenessClient\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSUserDefaults\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@?16"
- "@32@0:8:16@24"
- "@32@0:8f16q20B28"
- "@40@0:8:16@24@32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "ERAttentionAwarenessClient"
- "ERDistanceEvent"
- "EREyeReliefClient"
- "EREyeReliefConnection"
- "EREyeReliefEngine"
- "EREyeReliefProtocol"
- "EREyeReliefServer"
- "ERLogging"
- "NSObject"
- "NSXPCListenerDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"AWAttentionAwarenessClient\",&,N,V_attentionAwarenessClient"
- "T@\"AWAttentionAwarenessConfiguration\",&,N,V_attentionAwarenessConfiguration"
- "T@\"ERAttentionAwarenessClient\",&,V_attentionAwarenessClient"
- "T@\"NSMutableArray\",&,N,V_clientConnections"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_connectionQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSUserDefaults\",&,N,V_userDefaults"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@\"NSXPCListener\",&,N,V_listener"
- "T@?,C,N,V_distanceSamplingToggleHandler"
- "T@?,C,N,V_interruptHandler"
- "T@?,C,N,V_isDistanceSamplingEnabledHandler"
- "TB,N,V_didDetectAttention"
- "TQ,R"
- "Tf,N,V_distance"
- "Tf,V_tooCloseCount"
- "Tq,N,V_distanceCategory"
- "Tq,N,V_tooCloseDistanceThreshold"
- "Tq,V_interventionType"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_attentionAwarenessClient"
- "_attentionAwarenessConfiguration"
- "_categoryForDistance:withFaceState:"
- "_categoryForDistance:withTooCloseDistanceThreshold:withFaceState:"
- "_clientConnections"
- "_connection"
- "_connectionQueue"
- "_countReductionForInactiveTime:forSamplingInterval:"
- "_didDetectAttention"
- "_distance"
- "_distanceCategory"
- "_distanceSamplingToggleHandler"
- "_initFromUserDefaults:"
- "_interruptHandler"
- "_interventionType"
- "_isDistanceSamplingEnabledHandler"
- "_listener"
- "_pollForDistanceWithCompletion:"
- "_processDistanceEvent:"
- "_queue"
- "_resumeStreamingWithCompletion:"
- "_sendDistanceEvent:"
- "_tooCloseCount"
- "_tooCloseDistanceThreshold"
- "_userDefaults"
- "addObject:"
- "attentionAwarenessClient"
- "attentionAwarenessConfiguration"
- "autorelease"
- "boolForKey:"
- "boolValue"
- "cancelFaceDetectStreamWithError:"
- "cancelWithError:"
- "class"
- "clientConnections"
- "conformsToProtocol:"
- "connection"
- "connectionQueue"
- "connectionWithErrorHandler:"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "didDetectAttention"
- "distance"
- "distanceCategory"
- "distanceSamplingToggleHandler"
- "eventMask"
- "f"
- "f16@0:8"
- "f32@0:8d16d24"
- "faceState"
- "floatForKey:"
- "hash"
- "init"
- "initWithDistance:distanceCategory:andAttention:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithSuiteName:"
- "integerForKey:"
- "interfaceWithProtocol:"
- "interruptHandler"
- "interventionType"
- "invalidateWithError:"
- "isDistanceSamplingEnabled:"
- "isDistanceSamplingEnabledHandler"
- "isDistanceSamplingEnabledWithError:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "listener"
- "listener:shouldAcceptNewConnection:"
- "log:withType:"
- "numberWithDouble:"
- "numberWithUnsignedLongLong:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pollWithCompletion:"
- "processIdentifier"
- "processInactivity:forSamplingInterval:"
- "processInterventionOutcome:"
- "q"
- "q16@0:8"
- "q28@0:8f16Q20"
- "q36@0:8f16q20Q28"
- "queue"
- "release"
- "removeObject:"
- "reportAnalyticsFaceDetectAttentionEvent:"
- "respondsToSelector:"
- "resume"
- "resumeWithError:"
- "retain"
- "retainCount"
- "self"
- "setActivateAttentionDetection:"
- "setActivateEyeRelief:"
- "setAttentionAwarenessClient:"
- "setAttentionAwarenessConfiguration:"
- "setClientConnections:"
- "setConfiguration:"
- "setConnection:"
- "setConnectionQueue:"
- "setContinuousFaceDetectMode:"
- "setDelegate:"
- "setDidDetectAttention:"
- "setDistance:"
- "setDistanceCategory:"
- "setDistanceSamplingToggleHandler:"
- "setEventStreamerWithQueue:block:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFloat:forKey:"
- "setIdentifier:"
- "setInterruptHandler:"
- "setInterruptionHandler:"
- "setInterventionType:"
- "setInvalidationHandler:"
- "setIsDistanceSamplingEnabledHandler:"
- "setListener:"
- "setNotificationHandlerWithQueue:block:"
- "setNotificationMask:"
- "setQueue:"
- "setRemoteObjectInterface:"
- "setTooCloseCount:"
- "setTooCloseDistanceThreshold:"
- "setUnityStream:"
- "setUserDefaults:"
- "sharedConnection"
- "sharedServer"
- "startServer"
- "stringWithFormat:"
- "superclass"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "takeDistanceSampleWithCompletion:"
- "toggleDistanceSampling:"
- "tooCloseCount"
- "tooCloseDistanceThreshold"
- "userDefaults"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8q16"
- "v32@0:8@16Q24"
- "v32@0:8d16d24"
- "valueForEntitlement:"
- "zone"

```
