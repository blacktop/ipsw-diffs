## FitnessCoachingCore

> `/System/Library/PrivateFrameworks/FitnessCoachingCore.framework/FitnessCoachingCore`

```diff

-176.1.0.0.0
-  __TEXT.__text: 0x131f8
+193.0.0.0.0
+  __TEXT.__text: 0x14440
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x1f3c
+  __TEXT.__objc_methlist: 0x1f94
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x12dd
+  __TEXT.__cstring: 0x1351
   __TEXT.__oslogstring: 0x342
-  __TEXT.__unwind_info: 0x628
+  __TEXT.__unwind_info: 0x630
   __TEXT.__objc_classname: 0x5ba
-  __TEXT.__objc_methname: 0x2fb2
-  __TEXT.__objc_methtype: 0x8ed
-  __TEXT.__objc_stubs: 0x1d20
-  __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x350
+  __TEXT.__objc_methname: 0x30d6
+  __TEXT.__objc_methtype: 0x923
+  __TEXT.__objc_stubs: 0x1e20
+  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__const: 0x360
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb10
+  __DATA_CONST.__objc_selrefs: 0xb68
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x168
   __AUTH_CONST.__auth_got: 0x2e0
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x1220
-  __AUTH_CONST.__objc_const: 0x7038
+  __AUTH_CONST.__cfstring: 0x1280
+  __AUTH_CONST.__objc_const: 0x70a8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x224
+  __DATA.__objc_ivar: 0x22c
   __DATA.__data: 0x240
   __DATA_DIRTY.__objc_data: 0xaf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0130C53A-2208-30C5-B23E-3D3387676C28
-  Functions: 643
-  Symbols:   2333
-  CStrings:  965
+  UUID: 59BD74B3-FF25-36FD-AE07-E158F2F8F501
+  Functions: 650
+  Symbols:   2355
+  CStrings:  987
 
Symbols:
+ -[FCCFitnessPlusPlanClient postNotificationForType:force:showTomorrowPlan:completion:]
+ -[FCCFitnessPlusPlanPostNotificationRequest initWithType:force:showTomorrowPlan:]
+ -[FCCFitnessPlusPlanPostNotificationRequest initWithType:showTomorrowPlan:]
+ -[FCCFitnessPlusPlanPostNotificationRequest showTomorrowPlan]
+ -[FCCFitnessPlusPlanPostNotificationRequestProtobuf hasShowTomorrowPlan]
+ -[FCCFitnessPlusPlanPostNotificationRequestProtobuf setHasShowTomorrowPlan:]
+ -[FCCFitnessPlusPlanPostNotificationRequestProtobuf setShowTomorrowPlan:]
+ -[FCCFitnessPlusPlanPostNotificationRequestProtobuf showTomorrowPlan]
+ OBJC_IVAR_$_FCCFitnessPlusPlanPostNotificationRequestProtobuf._showTomorrowPlan
+ _FCCFitnessPlusPlanMostRecentlyNotifiedWorkoutPlanUUIDKey
+ _FCCNotificationUserInfoShowingTomorrowPlan
+ _OBJC_IVAR_$_FCCFitnessPlusPlanPostNotificationRequest._showTomorrowPlan
+ ___35-[FCCXPCClient _setupXPCConnection]_block_invoke.295
+ ___35-[FCCXPCClient _setupXPCConnection]_block_invoke.295.cold.1
+ ___45-[FCCXPCActivityScheduler _runActivity:name:]_block_invoke.290
+ ___45-[FCCXPCActivityScheduler _runActivity:name:]_block_invoke.290.cold.1
+ ___86-[FCCFitnessPlusPlanClient postNotificationForType:force:showTomorrowPlan:completion:]_block_invoke
+ ___block_literal_global.295
+ ___block_literal_global.297
+ _objc_msgSend$_setError
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$hasShowTomorrowPlan
+ _objc_msgSend$initWithType:force:showTomorrowPlan:
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setShowTomorrowPlan:
+ _objc_msgSend$showTomorrowPlan
+ _objc_retain_x5
- -[FCCFitnessPlusPlanClient postNotificationForType:force:completion:]
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- ___35-[FCCXPCClient _setupXPCConnection]_block_invoke.292
- ___35-[FCCXPCClient _setupXPCConnection]_block_invoke.292.cold.1
- ___45-[FCCXPCActivityScheduler _runActivity:name:]_block_invoke.287
- ___45-[FCCXPCActivityScheduler _runActivity:name:]_block_invoke.287.cold.1
- ___69-[FCCFitnessPlusPlanClient postNotificationForType:force:completion:]_block_invoke
- ___block_literal_global.292
- ___block_literal_global.294
- _objc_msgSend$initWithType:force:
- _objc_retain_x4
CStrings:
+ "@32@0:8@16B24B28"
+ "FCCFitnessPlusPlanPostNotificationRequest: type: %@, force: %{BOOL}d, showTomorrowPlan: %{BOOL}d"
+ "FitnessPlusPlanMostRecentlyNotifiedWorkoutPlanUUID"
+ "TB,N,V_showTomorrowPlan"
+ "TB,R,N,V_showTomorrowPlan"
+ "_setError"
+ "_showTomorrowPlan"
+ "getBytes:range:"
+ "hasError"
+ "hasShowTomorrowPlan"
+ "initWithType:force:showTomorrowPlan:"
+ "initWithType:showTomorrowPlan:"
+ "position"
+ "postNotificationForType:force:showTomorrowPlan:completion:"
+ "setHasShowTomorrowPlan:"
+ "setPosition:"
+ "setShowTomorrowPlan:"
+ "showTomorrowPlan"
+ "showingTomorrowPlan"
+ "v40@0:8@16B24B28@?32"
+ "{?=\"force\"b1\"showTomorrowPlan\"b1}"
- "FCCFitnessPlusPlanPostNotificationRequest: type: %@, force: %{BOOL}d"
- "postNotificationForType:force:completion:"
- "v36@0:8@16B24@?28"

```
