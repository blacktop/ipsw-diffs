## IOKitten

> `/System/Library/PrivateFrameworks/IOKitten.framework/IOKitten`

```diff

-440.2.0.0.0
-  __TEXT.__text: 0x54c0
-  __TEXT.__auth_stubs: 0x770
+500.2.0.0.0
+  __TEXT.__text: 0x506c
   __TEXT.__objc_methlist: 0x7e0
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x8ad
+  __TEXT.__cstring: 0x8b7
   __TEXT.__oslogstring: 0x7e
-  __TEXT.__unwind_info: 0x250
-  __TEXT.__objc_classname: 0x116
-  __TEXT.__objc_methname: 0x10eb
-  __TEXT.__objc_methtype: 0x4f0
-  __TEXT.__objc_stubs: 0x6a0
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__unwind_info: 0x258
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xf8
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x410
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x3c0
+  __DATA_CONST.__got: 0xa8
   __AUTH_CONST.__cfstring: 0x2e0
   __AUTH_CONST.__objc_const: 0xcc8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x5c
   __DATA_DIRTY.__objc_data: 0x460
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 87A57C8A-7EC3-3E5D-B86D-522FD11EEC9D
-  Functions: 205
-  Symbols:   777
-  CStrings:  318
+  UUID: 4255EB53-54AE-3C1D-A0A1-FE9ACDBDB4AE
+  Functions: 198
+  Symbols:   774
+  CStrings:  79
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x26
+ _objc_retain_x1
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
CStrings:
- "#20@0:8I16"
- ".cxx_destruct"
- "@\"<IOKPowerNotifierDelegate>\""
- "@\"IOKInterestNotification\""
- "@\"IOKInterestNotificationRef\""
- "@\"IOKIterator\""
- "@\"IOKMatchingNotification\""
- "@\"IOKMatchingNotificationRef\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@28@0:8@16I24"
- "@28@0:8I16@20"
- "@28@0:8I16@?20"
- "@28@0:8I16^@20"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8^@16@?24"
- "@36@0:8@16@24I32"
- "@36@0:8@16@24i32"
- "@36@0:8@16I24^@28"
- "@40@0:8@16^@24@?32"
- "@48@0:8@16@24^@32@?40"
- "@56@0:8@16@24@32^@40@?48"
- "@?"
- "@?16@0:8"
- "B104@0:8I16I20^Q24I32r^Q36I44r^v48Q56^Q64^I72^v80^Q88^@96"
- "B16@0:8"
- "B20@0:8B16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B28@0:8I16^@20"
- "B32@0:8@16^@24"
- "B36@0:8I16Q20^@28"
- "B40@0:8@16@24^@32"
- "B44@0:8@16I24Q28^@36"
- "B44@0:8I16Q20Q28^@36"
- "B48@0:8I16I20^Q24^Q32^@40"
- "B52@0:8I16Q20Q28Q36^@44"
- "B56@0:8I16r^Q20I28^Q32^I40^@48"
- "B60@0:8I16Q20Q28Q36Q44^@52"
- "B60@0:8I16r^v20Q28^v36^Q44^@52"
- "B68@0:8I16Q20Q28Q36Q44Q52^@60"
- "B72@0:8I16I20^Q24I32r^Q36I44^Q48^I56^@64"
- "B76@0:8I16I20^Q24I32r^v36Q44^v52^Q60^@68"
- "B76@0:8I16Q20Q28Q36Q44Q52Q60^@68"
- "B88@0:8I16r^Q20I28r^v32Q40^Q48^I56^v64^Q72^@80"
- "I"
- "I16@0:8"
- "IOKConnection"
- "IOKInterestNotification"
- "IOKInterestNotificationRef"
- "IOKIterator"
- "IOKMatchingNotification"
- "IOKMatchingNotificationRef"
- "IOKNotificationPort"
- "IOKObject"
- "IOKPowerManager"
- "IOKPowerManagerPowerAssertion"
- "IOKPowerNotifier"
- "IOKRegistryEntry"
- "IOKService"
- "IORegistryIterator"
- "Q16@0:8"
- "T@\"<IOKPowerNotifierDelegate>\",W,N,V_delegate"
- "T@\"IOKInterestNotification\",N,V_notification"
- "T@\"IOKInterestNotificationRef\",R,N,V_notificationRef"
- "T@\"IOKIterator\",&,N,V_iterator"
- "T@\"IOKMatchingNotification\",N,V_notification"
- "T@\"IOKMatchingNotificationRef\",R,N,V_notificationRef"
- "T@\"IOKService\",R,C,N"
- "T@\"NSDictionary\",C,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSString\",R,C,N"
- "T@?,C,N,V_handler"
- "TB,R,N,GisValid"
- "TI,N,V_object"
- "TI,R,N"
- "TI,R,N,V_connection"
- "TI,R,N,V_object"
- "TQ,R,N"
- "T^{IONotificationPort=},R,N,V_port"
- "UTF8String"
- "^{IONotificationPort=}"
- "^{IONotificationPort=}16@0:8"
- "_connection"
- "_delegate"
- "_enumerationBlock"
- "_handlePowerNotificationWithMessageType:andArgument:"
- "_handler"
- "_iterator"
- "_lock"
- "_notification"
- "_notificationPort"
- "_notificationRef"
- "_notifier"
- "_object"
- "_pmAssertionID"
- "_port"
- "_queue"
- "addInterestNotifcationOfType:usingNotificationPort:error:withHandler:"
- "addNotificationOfType:forMatching:usingNotificationPort:error:withEnumerationBlock:"
- "addNotificationOfType:forMatching:usingNotificationPort:error:withHandler:"
- "bsdNameMatching:"
- "bundleIdentifierForClassName:"
- "busyState"
- "callAsyncMethodWithSelector:wakePort:reference:referenceCount:scalarInputs:scalarInputCount:scalarOutputs:scalarOutputCount:error:"
- "callAsyncMethodWithSelector:wakePort:reference:referenceCount:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:structOutput:structOutputSize:error:"
- "callAsyncMethodWithSelector:wakePort:reference:referenceCount:structInput:structInputSize:structOutput:structOutputSize:error:"
- "callMethodWithSelector:scalarInputs:scalarInputCount:scalarOutputs:scalarOutputCount:error:"
- "callMethodWithSelector:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:structOutput:structOutputSize:error:"
- "callMethodWithSelector:structInput:structInputSize:structOutput:structOutputSize:error:"
- "childInPlane:error:"
- "childInServicePlaneWithError:"
- "childIteratorInPlane:error:"
- "childIteratorInPlane:error:withEnumerationBlock:"
- "childIteratorInServicePlaneWithError:"
- "childIteratorInServicePlaneWithError:enumerationBlock:"
- "classForRegistryEntry:"
- "conformsToIOClassName:"
- "connectToServiceOfType:"
- "connection"
- "copy"
- "dealloc"
- "delegate"
- "enterEntry"
- "entryFromPath:"
- "entryID"
- "entryIDMatching:"
- "enumerate"
- "enumerateWithBlock:"
- "errorWithDomain:code:userInfo:"
- "exitEntry"
- "hash"
- "init"
- "initOnDispatchQueue:"
- "initWithDispatchQueue:"
- "initWithIOObject:"
- "initWithIterator:"
- "initWithIterator:enumerationBlock:"
- "initWithMasterPort:onDispatchQueue:"
- "initWithName:assertionTyoe:assertionLevel:"
- "initWithRegistryEntry:"
- "initWithService:"
- "initWithService:andType:"
- "initWithServiceEntry:"
- "initWithUTF8String:"
- "ioClassName"
- "ioSuperClassNameForClassName:"
- "isAttachedToPlane:"
- "isEqual:"
- "isMemberOfClass:"
- "isServiceAuthorizedForOpenAllowInteraction:"
- "isSleepEnabled"
- "isValid"
- "iterator"
- "locationInPlane:error:"
- "locationInServicePlaneWithError:"
- "lock"
- "machPort"
- "mapMemory64OfType:withOptions:atAddress:ofSize:error:"
- "matchesPropertyTable:error:"
- "matchingService:"
- "matchingServices:error:"
- "name"
- "nameInPlane:error:"
- "nameInServicePlaneWithError:"
- "nameMatching:"
- "nextObject"
- "notification"
- "notificationRef"
- "object"
- "parentEntryInPlane:error:"
- "parentEntryInServicePlaneWithError:"
- "parentIteratorInPlane:error:"
- "parentIteratorInPlane:error:withEnumerationBlock:"
- "parentIteratorInServicePlaneWithError:"
- "parentIteratorInServicePlaneWithError:enumerationBlock:"
- "pathInPlane:"
- "pathInServicePlane"
- "port"
- "powerManager"
- "primeNotification"
- "properties"
- "propertyForKey:"
- "queue"
- "raise:format:"
- "registryIteratorForPlane:withOptions:error:"
- "registryIteratorForServicePlaneWithOptions:error:"
- "requestProbeWithOptions:error:"
- "reset"
- "rootEntry"
- "searchForPropertyWithKey:inPlane:"
- "searchForPropertyWithKey:inPlane:withOptions:"
- "service"
- "serviceMatching:"
- "setDelegate:"
- "setHandler:"
- "setIterator:"
- "setNotification:"
- "setNotificationPort:ofType:withReference:error:"
- "setObject:"
- "setProperties:"
- "setProperties:error:"
- "setProperty:forKey:"
- "setProperty:withKey:error:"
- "setQueue:"
- "sleepSystemWithError:"
- "stringWithUTF8String:"
- "systemHasPoweredOn"
- "systemHasPoweredOnWithNotifier:"
- "systemWillNotSleep"
- "systemWillNotSleepWithNotifier:"
- "systemWillPowerOn"
- "systemWillPowerOnWithNotifier:"
- "systemWillSleep"
- "systemWillSleepWithNotifier:"
- "trap:error:"
- "trap:p1:error:"
- "trap:p1:p2:error:"
- "trap:p1:p2:p3:error:"
- "trap:p1:p2:p3:p4:error:"
- "trap:p1:p2:p3:p4:p5:error:"
- "trap:p1:p2:p3:p4:p5:p6:error:"
- "unlock"
- "unmapMemory64OfType:atAddress:error:"
- "v16@0:8"
- "v20@0:8I16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v28@0:8I16q20"
- "v32@0:8@16@24"
- "valid"
- "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"

```
