## SoundAutoConfig

> `/System/Library/PrivateFrameworks/SoundAutoConfig.framework/SoundAutoConfig`

```diff

 109.27.0.0.0
-  __TEXT.__text: 0x2464
-  __TEXT.__auth_stubs: 0x240
+  __TEXT.__text: 0x2288
   __TEXT.__objc_methlist: 0x42c
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x5ec
+  __TEXT.__gcc_except_tab: 0x5a4
   __TEXT.__oslogstring: 0x53
-  __TEXT.__cstring: 0x2a1
+  __TEXT.__cstring: 0x2a8
   __TEXT.__unwind_info: 0x1b8
-  __TEXT.__objc_classname: 0xb8
-  __TEXT.__objc_methname: 0x75a
-  __TEXT.__objc_methtype: 0x249
-  __TEXT.__objc_stubs: 0x6e0
-  __DATA_CONST.__got: 0x68
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_selrefs: 0x290
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x130
+  __DATA_CONST.__got: 0x68
   __AUTH_CONST.__cfstring: 0x440
   __AUTH_CONST.__objc_const: 0xf18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x2a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 87591CCA-F67F-3B28-9EFF-819F543F3D2F
+  UUID: 562266CD-3858-3A98-8EEA-B55465289BA9
   Functions: 63
   Symbols:   64
-  CStrings:  234
+  CStrings:  74
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
Functions:
~ sub_2759a0d9c -> sub_2a499cd9c : 708 -> 636
~ sub_2759a1254 -> sub_2a499d20c : 188 -> 180
~ sub_2759a1310 -> sub_2a499d2c0 : 268 -> 260
~ sub_2759a1508 -> sub_2a499d4b0 : 572 -> 560
~ sub_2759a1950 -> sub_2a499d8ec : 188 -> 180
~ sub_2759a1a14 -> sub_2a499d9a8 : 64 -> 12
~ sub_2759a1b28 -> sub_2a499da88 : 708 -> 636
~ sub_2759a1fe0 -> sub_2a499def8 : 188 -> 180
~ sub_2759a2134 -> sub_2a499e044 : 604 -> 572
~ sub_2759a2390 -> sub_2a499e280 : 820 -> 780
~ sub_2759a26c4 -> sub_2a499e58c : 480 -> 448
~ sub_2759a2900 -> sub_2a499e7a8 : 180 -> 164
~ sub_2759a29b4 -> sub_2a499e84c : 1692 -> 1576
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<SACDSPDelegate>\""
- "@\"<SACInfoDelegate>\""
- "@\"<SACSYSDelegate>\""
- "@\"<SACServiceDSPDelegate>\""
- "@\"<SACServiceDelegate>\""
- "@\"<SACServiceSYSDelegate>\""
- "@\"NSArray\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "SACDSPController"
- "SACInfo"
- "SACInfoListener"
- "SACSYSController"
- "SACServiceDSPDelegate"
- "SACServiceDelegate"
- "SACServiceInfoDelegate"
- "SACServiceSYSDelegate"
- "T#,R"
- "T@\"<SACDSPDelegate>\",N,V_delegate"
- "T@\"<SACInfoDelegate>\",&,N,V_delegate"
- "T@\"<SACSYSDelegate>\",N,V_delegate"
- "T@\"NSArray\",&,V_companionInfo"
- "T@\"NSArray\",&,V_lfeqIR"
- "T@\"NSNumber\",&,V_angle"
- "T@\"NSNumber\",&,V_calibrationMode"
- "T@\"NSNumber\",&,V_roomGain"
- "T@\"NSNumber\",&,V_spatialAudio"
- "T@\"NSString\",&,V_position"
- "T@\"NSString\",&,V_role"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,R"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_angle"
- "_calibrationMode"
- "_companionInfo"
- "_delegate"
- "_lfeqIR"
- "_position"
- "_role"
- "_roomGain"
- "_spatialAudio"
- "allocWithZone:"
- "appendFormat:"
- "appendString:"
- "autorelease"
- "calibrationModeDescription:"
- "class"
- "conformsToProtocol:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "debugDescription"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "delegate"
- "description"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "floatValue"
- "getDSPInfoByKey:"
- "getDSPInfoByKey:withReply:"
- "handleSACInfo:"
- "handleServiceCrash"
- "hash"
- "init"
- "initWithArray:copyItems:"
- "initWithCoder:"
- "initWithServiceName:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSoundAutoConfigAvailable"
- "lfeqIR"
- "mProxyInterface"
- "mSACDSPDelegate"
- "mSACSYSDelegate"
- "mServiceConnection"
- "mVerbosity"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "registerAsClientWithConnectionType:"
- "registerAsInfoListener"
- "release"
- "remoteObjectProxy"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setAngle:"
- "setCalibrationMode:"
- "setCompanionInfo:"
- "setDSPConfig:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLfeqIR:"
- "setListenerVerbosity:"
- "setPosition:"
- "setRemoteObjectInterface:"
- "setRole:"
- "setRoomGain:"
- "setSYSConfig:"
- "setSpatialAudio:"
- "setVerbosityForClient:"
- "setWithObjects:"
- "startServiceConnection"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "unsignedIntegerValue"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"SACInfo\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@16@?24"
- "zone"

```
