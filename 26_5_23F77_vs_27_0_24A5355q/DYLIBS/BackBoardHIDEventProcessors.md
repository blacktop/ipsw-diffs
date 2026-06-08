## BackBoardHIDEventProcessors

> `/System/Library/PrivateFrameworks/BackBoardHIDEventProcessors.framework/BackBoardHIDEventProcessors`

```diff

-735.5.1.0.0
-  __TEXT.__text: 0x243c
-  __TEXT.__auth_stubs: 0x340
+860.0.1.0.0
+  __TEXT.__text: 0x2164
   __TEXT.__objc_methlist: 0x364
   __TEXT.__const: 0x80
   __TEXT.__oslogstring: 0x2b2
-  __TEXT.__cstring: 0x15d
-  __TEXT.__unwind_info: 0x128
-  __TEXT.__objc_classname: 0x12d
-  __TEXT.__objc_methname: 0x85f
-  __TEXT.__objc_methtype: 0x304
-  __TEXT.__objc_stubs: 0x500
-  __DATA_CONST.__got: 0x50
+  __TEXT.__cstring: 0x177
+  __TEXT.__unwind_info: 0xb8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x250
-  __AUTH_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__got: 0x48
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0xa20
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x30
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/StudyLog.framework/StudyLog
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CC962B58-F8E1-3A9C-AE45-C00458B3B3F9
+  UUID: D225E27D-4DC8-3A46-9FF9-43B65DE0E6D3
   Functions: 60
-  Symbols:   344
-  CStrings:  191
+  Symbols:   346
+  CStrings:  46
 
Symbols:
+ ___block_literal_global.216
+ ___block_literal_global.44
+ ___block_literal_global.47
+ ___block_literal_global.50
+ ___block_literal_global.53
+ ___block_literal_global.56
+ ___block_literal_global.59
+ ___block_literal_global.62
+ ___block_literal_global.65
+ ___block_literal_global.68
+ ___block_literal_global.71
+ ___block_literal_global.74
+ ___block_literal_global.77
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x8
- _BKLoggingSubsystem
- ___block_literal_global.12
- ___block_literal_global.15
- ___block_literal_global.18
- ___block_literal_global.21
- ___block_literal_global.225
- ___block_literal_global.24
- ___block_literal_global.27
- ___block_literal_global.3
- ___block_literal_global.30
- ___block_literal_global.33
- ___block_literal_global.36
- ___block_literal_global.6
- ___block_literal_global.9
- _objc_release
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
- _objc_retain_x26
CStrings:
+ "com.apple.BackBoard"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<BKHIDEventDispatcher>\""
- "@\"<BKHIDEventSenderInfo>\""
- "@\"BSDescriptionBuilder\"16@0:8"
- "@\"BSDescriptionBuilder\"24@0:8@\"NSString\"16"
- "@\"NSMutableDictionary\""
- "@\"NSSet\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"BKHIDEventProcessorCreationContext\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "BKHIDBiometricEventProcessor"
- "BKHIDEventProcessor"
- "BKHIDGameControllerEventProcessor"
- "BKHIDGenericGestureEventProcessor"
- "BKHIDPointerEventProcessor"
- "BKHIDPointerEventRecord"
- "BKHIDScrollEventProcessor"
- "BKHIDVendorDefinedEventProcessor"
- "BKIOHIDServiceDisappearanceObserver"
- "BSDescriptionProviding"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<BKHIDEventDispatcher>\",&,N,V_eventDispatcher"
- "T@\"<BKHIDEventSenderInfo>\",&,N,V_senderInfo"
- "T@\"NSMutableDictionary\",&,N,V_genericGestureTypePerSenderID"
- "T@\"NSMutableDictionary\",&,N,V_pendingDestinationsPerSenderID"
- "T@\"NSSet\",&,N,V_destinations"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,N,V_trackingButtonDown"
- "TB,N,V_trackingPointerMovement"
- "TQ,R"
- "Td,N,V_destinationCaptureTime"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_destinationCaptureTime"
- "_destinations"
- "_didTrackButtonDown"
- "_didTrackPointerMovement"
- "_dispatchEvent:sender:dispatcher:destinations:"
- "_eventDispatcher"
- "_eventRecords"
- "_genericGestureTypePerSenderID"
- "_lock"
- "_pendingDestinationsPerSenderID"
- "_postEvent:toDestination:usingDispatcher:"
- "_senderInfo"
- "_trackingButtonDown"
- "_trackingPointerMovement"
- "addDisappearanceObserver:queue:"
- "appendBool:withName:"
- "appendDouble:withName:decimalPrecision:"
- "appendObject:withName:"
- "autorelease"
- "baseAttributesFromProvider:"
- "bs_map:"
- "build"
- "builderWithObject:"
- "class"
- "conformsToProtocol:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "d16@0:8"
- "debugDescription"
- "description"
- "descriptionBuilderWithMultilinePrefix:"
- "descriptionWithMultilinePrefix:"
- "destinationsForEvent:fromSender:"
- "didInitializeRegistryWithContext:"
- "displayUUID"
- "eventDispatcher"
- "eventSource"
- "genericGestureTypePerSenderID"
- "hash"
- "initWithContext:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "numberWithInt:"
- "numberWithLong:"
- "numberWithUnsignedLongLong:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "pendingDestinationsPerSenderID"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pid"
- "postEvent:toDestination:"
- "processEvent:sender:dispatcher:"
- "q40@0:8N^^{__IOHIDEvent}16@\"<BKHIDEventSenderInfo>\"24@\"<BKHIDEventDispatcher>\"32"
- "q40@0:8N^^{__IOHIDEvent}16@24@32"
- "release"
- "removeDisappearanceObserver:"
- "removeObjectForKey:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "senderID"
- "serviceDidDisappear:"
- "setDestinationCaptureTime:"
- "setDestinations:"
- "setEventDispatcher:"
- "setGenericGestureTypePerSenderID:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPendingDestinationsPerSenderID:"
- "setSenderInfo:"
- "setTrackingButtonDown:"
- "setTrackingPointerMovement:"
- "succinctDescription"
- "succinctDescriptionBuilder"
- "superclass"
- "timeIntervalSinceReferenceDate"
- "unsignedIntValue"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"BKHIDEventProcessorCreationContext\"16"
- "v24@0:8@\"BKIOHIDService\"16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v40@0:8^{__IOHIDEvent=}16@24@32"
- "v48@0:8^{__IOHIDEvent=}16@24@32@40"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
