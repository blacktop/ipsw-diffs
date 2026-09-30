## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-3402.62.3.1.2
-  __TEXT.__text: 0x1a3e3c
-  __TEXT.__auth_stubs: 0x1540
-  __TEXT.__objc_methlist: 0x19ac4
+3402.71.2.0.0
+  __TEXT.__text: 0x1a6200
+  __TEXT.__auth_stubs: 0x1550
+  __TEXT.__objc_methlist: 0x19c1c
   __TEXT.__const: 0x458
-  __TEXT.__gcc_except_tab: 0x25a4
-  __TEXT.__cstring: 0x3bd57
-  __TEXT.__oslogstring: 0x10085
-  __TEXT.__dlopen_cstrs: 0x42e
-  __TEXT.__unwind_info: 0x7a70
-  __TEXT.__objc_classname: 0x4e2f
-  __TEXT.__objc_methname: 0x3a7da
-  __TEXT.__objc_methtype: 0xa93a
-  __TEXT.__objc_stubs: 0x24080
+  __TEXT.__gcc_except_tab: 0x2670
+  __TEXT.__cstring: 0x3c212
+  __TEXT.__oslogstring: 0x103e2
+  __TEXT.__dlopen_cstrs: 0x484
+  __TEXT.__unwind_info: 0x7ab8
+  __TEXT.__objc_classname: 0x4e65
+  __TEXT.__objc_methname: 0x3a988
+  __TEXT.__objc_methtype: 0xa98c
+  __TEXT.__objc_stubs: 0x241c0
   __DATA_CONST.__got: 0x1610
-  __DATA_CONST.__const: 0x8228
-  __DATA_CONST.__objc_classlist: 0xda8
+  __DATA_CONST.__const: 0x8320
+  __DATA_CONST.__objc_classlist: 0xdb8
   __DATA_CONST.__objc_catlist: 0x290
   __DATA_CONST.__objc_protolist: 0x550
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbf20
+  __DATA_CONST.__objc_selrefs: 0xbfa0
   __DATA_CONST.__objc_protorefs: 0x140
-  __DATA_CONST.__objc_superrefs: 0xdb8
-  __DATA_CONST.__objc_arraydata: 0x1fb8
-  __AUTH_CONST.__auth_got: 0xab0
+  __DATA_CONST.__objc_superrefs: 0xdc8
+  __DATA_CONST.__objc_arraydata: 0x1fa8
+  __AUTH_CONST.__auth_got: 0xab8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3920
-  __AUTH_CONST.__cfstring: 0x26b20
-  __AUTH_CONST.__objc_const: 0x39df8
+  __AUTH_CONST.__const: 0x38a0
+  __AUTH_CONST.__cfstring: 0x26c20
+  __AUTH_CONST.__objc_const: 0x3a008
   __AUTH_CONST.__objc_intobj: 0x2328
   __AUTH_CONST.__objc_dictobj: 0xb90
   __AUTH_CONST.__objc_arrayobj: 0x588
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x73f0
-  __AUTH.__data: 0x2f8
-  __DATA.__objc_ivar: 0x2544
+  __AUTH.__objc_data: 0x7440
+  __AUTH.__data: 0x290
+  __DATA.__objc_ivar: 0x2550
   __DATA.__data: 0x4108
-  __DATA.__bss: 0x1348
+  __DATA.__bss: 0x1280
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x14a0
+  __DATA_DIRTY.__objc_data: 0x14f0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x1a0
+  __DATA_DIRTY.__bss: 0x1b8
   __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11652
-  Symbols:   13849
-  CStrings:  18974
+  Functions: 11668
+  Symbols:   13875
+  CStrings:  19032
 
Symbols:
+ _AFBluetoothStreamName
+ _AFDeviceSupportsBackgroundSession
+ _AFSiriServiceStreamName
+ _BiomeLibrary
+ _OBJC_CLASS_$_AFLocationFetchRequest
+ _OBJC_CLASS_$_AFSiriServiceEvent
+ _OBJC_METACLASS_$_AFLocationFetchRequest
+ _OBJC_METACLASS_$_AFSiriServiceEvent
+ _kAFSiriServiceEventDismissalReasonKey
+ _kAFSiriServiceEventDomainKey
+ _kAFSiriServiceEventRequestSourceKey
+ _kAFSiriServiceEventUnintendedKey
- _OBJC_CLASS_$_NSSortDescriptor
CStrings:
+ "%!s(MISSING) Biome Store APIs does not support end time for events"
+ "%!s(MISSING) Biome base event unavailable for AFBTEvent"
+ "%!s(MISSING) Biome event stream unavailable"
+ "%!s(MISSING) Biome event stream unavailable for bluetooth device"
+ "%!s(MISSING) Biome stream unavailable"
+ "%!s(MISSING) Dispatching event %!@(MISSING) to event source"
+ "%!s(MISSING) Error creating Biome publisher"
+ "%!s(MISSING) Error creating Biome stream"
+ "%!s(MISSING) Error creating biome event"
+ "%!s(MISSING) Error creating biome event store"
+ "%!s(MISSING) Error deleting BT event: %!@(MISSING)"
+ "%!s(MISSING) Error deleting SiriService event: %!@(MISSING)"
+ "%!s(MISSING) Error fetching notification event: %!@(MISSING)"
+ "%!s(MISSING) Error recoding events: %!@(MISSING)"
+ "%!s(MISSING) Fetching SiriServices Biome events between startData: %!@(MISSING), endDate: %!@(MISSING)"
+ "%!s(MISSING) Filtering event:`%!@(MISSING)` with timestamp: %!@(MISSING)"
+ "%!s(MISSING) Received event %!@(MISSING) {dismissal reason:%!d(MISSING)}"
+ "%!s(MISSING) Received event '%!@(MISSING)' with no product id"
+ "%!s(MISSING) Recording context event with {key: %!@(MISSING), domain: %!@(MISSING), command: %!@(MISSING)}"
+ "%!s(MISSING) Sending event %!@(MISSING) to event source"
+ "%!s(MISSING) Sent event %!@(MISSING) to stream %!@(MISSING)"
+ "%!s(MISSING) Sent event %!@(MISSING) to stream Device.Wireless.Bluetooth"
+ "%!s(MISSING) Unable to store invalid biome event of type `%!@(MISSING)`"
+ "%!s(MISSING) Unknown Biome stream: %!@(MISSING)"
+ "%!s(MISSING) Unsupported BMSiriServiceDismissalReason %!u(MISSING)"
+ "%!s(MISSING) Unsupported BMSiriServiceRequestSource %!u(MISSING)"
+ "%!s(MISSING) Unsupported Biome stream %!@(MISSING)"
+ "%!s(MISSING) Unsupported metadata in {%!@(MISSING)}"
+ "-[AFEventStore(BluetoothEvent) _getPublisher]"
+ "-[AFEventStore(BluetoothEvent) deleteAllBTEventsWithQueue:withCompletionHandler:]"
+ "-[AFEventStore(BluetoothEvent) fetchAppleAudioDeviceConnectedInLast24HoursWithCompletionHandler:]"
+ "-[AFEventStore(BluetoothEvent) fetchAppleAudioDeviceConnectedInLast24HoursWithCompletionHandler:]_block_invoke"
+ "-[AFEventStore(BluetoothEvent) fetchAppleAudioDeviceConnectedInLast24HoursWithCompletionHandler:]_block_invoke_2"
+ "-[AFEventStore(BluetoothEvent) fetchHeadunitsConnectedInLast24HoursWithCompletionHandler:]"
+ "-[AFEventStore(BluetoothEvent) storeBTEvent:withQueue:withCompletionHandler:]"
+ "-[AFEventStore(BluetoothEvent) storeBTEvent:withQueue:withCompletionHandler:]_block_invoke"
+ "-[AFEventStore(SiriService) deleteAllSiriServiceEventsWithQueue:withCompletionHandler:]"
+ "-[AFEventStore(SiriService) fetchEventsBetweenStartDate:endDate:withQueue:withCompletionHandler:]"
+ "-[AFEventStore(SiriService) fetchEventsBetweenStartDate:endDate:withQueue:withCompletionHandler:]_block_invoke"
+ "-[AFEventStore(SiriService) fetchEventsBetweenStartDate:endDate:withQueue:withCompletionHandler:]_block_invoke_2"
+ "-[AFEventStore(SiriService) storeSiriServiceEvent:withQueue:atTime:withCompletionHandler:]"
+ "-[AFEventStore(SiriService) storeSiriServiceEvent:withQueue:atTime:withCompletionHandler:]_block_invoke"
+ "-[AFOpportuneSpeakingModelFeedbackManager fetchNotificationUsageForSpeakableId:withStartDate:withEndDate:withHandler:]_block_invoke_2"
+ "-[AFSiriServiceEvent initWithMetadata:identifier:]"
+ "/bluetooth/dataDictionary"
+ "/siri/service"
+ "AFAppleAudioDeviceConnectedInLast24Hours_block_invoke"
+ "AFBTHeadunitsConnectedInLast24Hours_block_invoke"
+ "AFEvents_Internal.h"
+ "AFLocationFetchRequest"
+ "AFRecordCoreDuetContext_block_invoke"
+ "AFSiriServiceEvent"
+ "B24@?0@\"BMStoreEvent\"8^B16"
+ "B32@0:8@16q24"
+ "BMSiriService"
+ "CLOUDKIT_CLIENT_EVENT"
+ "GMS_CLIENT_EVENT"
+ "Notification"
+ "ODFUNNEL_SIRI_CLIENT_EVENT"
+ "SiriService"
+ "T@,C,N,V_bmEvent"
+ "TQ,N,V_style"
+ "Td,N,V_desiredAccuracy"
+ "Td,N,V_timeout"
+ "Usage"
+ "Vv32@0:8@\"AFLocationFetchRequest\"16@?<v@?@\"CLLocation\"@\"NSError\">24"
+ "_AFRecordCoreDuetEventAtTimestamps"
+ "_desiredAccuracy"
+ "_filterAppleAudioEventsMoreThanADayOld:"
+ "_filterHeadUnitEventsMoreThanADayOld:"
+ "_getPublisher"
+ "_isEvent:olderThan:"
+ "_mapIDsToProduct:"
+ "_timeout"
+ "absoluteTimestamp"
+ "assistant.device.bt.delete"
+ "assistant.siriservice.delete"
+ "background_session"
+ "com.apple.Siri.NLRouter"
+ "currentLocationWithFetchRequest:completion:"
+ "deleteAllBTEventsWithQueue:withCompletionHandler:"
+ "deleteAllSiriServiceEventsWithQueue:withCompletionHandler:"
+ "deleteWithPolicy:eventsPassingTest:"
+ "desiredAccuracy"
+ "dismissalReason"
+ "fetchAppleAudioDeviceConnectedInLast24HoursWithCompletionHandler:"
+ "fetchEventsBetweenStartDate:endDate:withQueue:withCompletionHandler:"
+ "initWithDismissalReason:unintended:requestSource:identifier:domain:command:"
+ "initWithDomain:identifier:command:"
+ "initWithMetadata:identifier:"
+ "initWithTimeIntervalSinceReferenceDate:"
+ "isSiriBackgroundSessionEnabled"
+ "isSubsetOfSet:"
+ "pruner"
+ "publisherWithUseCase:"
+ "publisherWithUseCase:options:"
+ "requestSource"
+ "sendEvent:timestamp:"
+ "setBmEvent:"
+ "setDesiredAccuracy:"
+ "setTimeout:"
+ "storeBTEvent:withQueue:withCompletionHandler:"
+ "storeSiriServiceEvent:withQueue:atTime:withCompletionHandler:"
+ "storeSiriServiceEvent:withQueue:withCompletionHandler:"
+ "timeout"
+ "unintended"
+ "uniqueID"
+ "usageType"
+ "v16@?0@\"BMStoreEvent\"8"
+ "v24@?0@\"NSSet\"8@\"NSError\"16"
- "%!s(MISSING) Error deleting from duet: %!@(MISSING)"
- "%!s(MISSING) Error obtaining notificationUsageStream from CoreDuet."
- "%!s(MISSING) Error querying CoreDuet with %!@(MISSING): %!@(MISSING)"
- "%!s(MISSING) Error saving to duet: %!@(MISSING)"
- "%!s(MISSING) Queue and key must be non-nil: %!@(MISSING), %!@(MISSING)"
- "%!s(MISSING) Queue and stream must be non-nil: %!@(MISSING), %!@(MISSING)"
- "%!s(MISSING) Unable to get an instance of _DKKnowledgeStore."
- "(startDate > %!@(MISSING) AND startDate < %!@(MISSING)) OR (endDate > %!@(MISSING) AND endDate < %!@(MISSING))"
- "-[AFOpportuneSpeakingModelFeedbackManager fetchNotificationUsageForSpeakableId:withStartDate:withEndDate:withHandler:]"
- "/System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext"
- "AFAppleAudioDeviceConnectedInLast24Hours"
- "AFBTHeadunitsConnectedInLast24Hours"
- "AFEventDefs.h"
- "Confidence"
- "EndDate"
- "IndirectClear"
- "T@,R,N,V_bmEvent"
- "_AFFetchCoreDuetEventsWithStream"
- "_CDClientContext"
- "_CDContextualKeyPath"
- "_DKBluetoothMetadataKey"
- "_DKEvent"
- "_DKEventQuery"
- "_DKEventStream"
- "_DKNotificationUsageMetadataKey"
- "_DKQuery"
- "_DKSystemEventStreams"
- "_filterEventsMoreThanADayOld:"
- "bluetoothIsConnectedStream"
- "class_DKEventQuery"
- "class_DKNotificationUsageMetadataKey"
- "class_DKQuery"
- "class_DKSystemEventStreams"
- "deleteObjects:error:"
- "eventQueryWithPredicate:eventStreams:offset:limit:sortDescriptors:"
- "eventStreamWithName:"
- "eventWithStream:startDate:endDate:identifierStringValue:metadata:"
- "executeQuery:error:"
- "initWithAddress:name:productID:starting:deviceType:batteryLevelHeadphoneCase:batteryLevelHeadphoneRight:batteryLevelHeadphoneLeft:appleAudioDevice:userWearing:"
- "init_DKEventQuery_block_invoke"
- "init_DKNotificationUsageMetadataKey_block_invoke"
- "init_DKQuery_block_invoke"
- "init_DKSystemEventStreams_block_invoke"
- "isAppleAudioDevice"
- "keyPathWithKey:"
- "localizedDescription"
- "notificationUsageStream"
- "predicateForEventsWithStartInDateRangeFrom:to:"
- "predicateForEventsWithStreamName:"
- "predicateWithFormat:"
- "publisherWithOptions:"
- "saveObjects:error:"
- "setObject:forContextualKeyPath:"
- "sortDescriptorWithKey:ascending:"
- "userContext"
- "vi-VN-u-sd-vnct"

```
