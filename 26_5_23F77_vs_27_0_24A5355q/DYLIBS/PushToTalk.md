## PushToTalk

> `/System/Library/Frameworks/PushToTalk.framework/PushToTalk`

```diff

-106.600.51.2.2
-  __TEXT.__text: 0x461c
-  __TEXT.__auth_stubs: 0x400
+139.100.27.2.9
+  __TEXT.__text: 0x416c
   __TEXT.__objc_methlist: 0x664
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x3f1
-  __TEXT.__gcc_except_tab: 0x74
+  __TEXT.__cstring: 0x3fe
+  __TEXT.__gcc_except_tab: 0x54
   __TEXT.__oslogstring: 0x74d
-  __TEXT.__unwind_info: 0x1c0
-  __TEXT.__objc_classname: 0x99
-  __TEXT.__objc_methname: 0x19aa
-  __TEXT.__objc_methtype: 0x5c6
-  __TEXT.__objc_stubs: 0xdc0
-  __DATA_CONST.__got: 0xd8
+  __TEXT.__unwind_info: 0x190
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x558
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0xd8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x260
   __AUTH_CONST.__objc_const: 0xa20
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x120

   - /usr/lib/libBASupport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9BEB75BA-29F9-31D2-A1D2-B0E11F6E35E3
-  Functions: 133
-  Symbols:   574
-  CStrings:  378
+  UUID: E1EBCA1D-E6D6-3AF5-A2B8-661177A23C41
+  Functions: 131
+  Symbols:   576
+  CStrings:  77
 
Symbols:
+ ___41-[PTChannelManager leaveChannelWithUUID:]_block_invoke.63
+ ___88-[PTChannelManager _requestJoinChannelWithUUID:channelDescriptor:originator:completion:]_block_invoke.61
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x26
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- ___41-[PTChannelManager leaveChannelWithUUID:]_block_invoke.64
- ___88-[PTChannelManager _requestJoinChannelWithUUID:channelDescriptor:originator:completion:]_block_invoke.62
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<PTChannelManagerDelegate>\""
- "@\"<PTChannelRestorationDelegate>\""
- "@\"CXCallController\""
- "@\"CXChannelProvider\""
- "@\"CXParticipant\""
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"PTParticipant\""
- "@\"UIImage\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@?32"
- "@?"
- "@?16@0:8"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"<CXAbstractProvider>\"16@\"CXTransaction\"24"
- "B32@0:8@16@24"
- "CXAbstractProviderDelegate"
- "CXChannelProviderDelegate"
- "NSObject"
- "PTChannelDescriptor"
- "PTChannelManager"
- "PTParticipant"
- "PTPendingPush"
- "PTPushResult"
- "Q16@0:8"
- "T#,R"
- "T@\"<PTChannelManagerDelegate>\",W,N,V_channelEventDelegate"
- "T@\"<PTChannelRestorationDelegate>\",W,N,V_channelRestorationDelegate"
- "T@\"CXCallController\",R,N,V_callController"
- "T@\"CXChannelProvider\",R,N,V_underlyingProvider"
- "T@\"CXParticipant\",R,N,V_underlyingParticipant"
- "T@\"NSDictionary\",&,N,V_payload"
- "T@\"NSMutableArray\",&,N,V_pendingPushes"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_callbackQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_name"
- "T@\"NSURL\",R,C,N,V_imageFileURL"
- "T@\"NSUUID\",&,N,V_suppressRejoinForRecentlyDisconnectedChannelUUID"
- "T@\"NSUUID\",&,N,V_uuid"
- "T@\"NSUUID\",&,V_waitingForPushResultChannelUUID"
- "T@\"NSUUID\",R,N,V_activeChannelUUID"
- "T@\"PTParticipant\",&,N,V_participant"
- "T@\"PTPushResult\",R,N"
- "T@\"UIImage\",R,C,N,V_image"
- "T@?,C,N,V_reply"
- "T@?,C,V_instantiationCompletionBlock"
- "TB,N,V_attemptingChannelRestoration"
- "TB,N,V_isHighPriority"
- "TB,N,V_isServiceUpdateMessage"
- "TB,V_isWaitingForPushResult"
- "TB,V_stopTransmitRequestedWhileWaitingForPushResult"
- "TQ,R"
- "Tq,N,V_remainingHighPriorityBudget"
- "Tq,R,N,V_type"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_activeChannelUUID"
- "_appendPendingPushForUUID:payload:reply:isServiceUpdateMessage:isHighPriority:remainingHighPriorityBudget:"
- "_attemptingChannelRestoration"
- "_callController"
- "_callbackQueue"
- "_channelEventDelegate"
- "_channelRestorationDelegate"
- "_deliverChannelManagerInstanceToClientIfNeeded"
- "_deliverPendingPushes"
- "_ensureDelegateIsReadyToReceiveActions:joinReason:"
- "_handleLeaveCheckinResult:"
- "_handlePushResult:pendingPush:"
- "_image"
- "_imageFileURL"
- "_initWithEventDelegate:restorationDelegate:instantiationCompletion:"
- "_initWithResultType:participant:"
- "_instantiationCompletionBlock"
- "_isHighPriority"
- "_isServiceUpdateMessage"
- "_isWaitingForPushResult"
- "_name"
- "_participant"
- "_payload"
- "_pendingPushes"
- "_performChannelRestorationAndUpdateChannelDescriptor:pushPayload:"
- "_remainingHighPriorityBudget"
- "_reply"
- "_requestJoinChannelWithUUID:channelDescriptor:originator:completion:"
- "_setActiveRemoteParticipant:forChannelUUID:shouldReplaceOutgoingTransmission:completionHandler:"
- "_stopTransmitRequestedWhileWaitingForPushResult"
- "_suppressRejoinForRecentlyDisconnectedChannelUUID"
- "_type"
- "_underlyingParticipant"
- "_underlyingProvider"
- "_uuid"
- "_waitingForPushResultChannelUUID"
- "activeChannelUUID"
- "addObject:"
- "array"
- "attemptingChannelRestoration"
- "autorelease"
- "callController"
- "callbackQueue"
- "channelDescriptorForRestoredChannelUUID:"
- "channelEventDelegate"
- "channelManager:channelUUID:didBeginTransmittingFromSource:"
- "channelManager:channelUUID:didEndTransmittingFromSource:"
- "channelManager:didActivateAudioSession:"
- "channelManager:didDeactivateAudioSession:"
- "channelManager:didJoinChannelWithUUID:reason:"
- "channelManager:didLeaveChannelWithUUID:reason:"
- "channelManager:failedToBeginTransmittingInChannelWithUUID:error:"
- "channelManager:failedToJoinChannelWithUUID:error:"
- "channelManager:failedToLeaveChannelWithUUID:error:"
- "channelManager:failedToStopTransmittingInChannelWithUUID:error:"
- "channelManager:receivedEphemeralPushToken:"
- "channelManagerWithDelegate:restorationDelegate:completionHandler:"
- "channelRestorationDelegate"
- "channelUUID"
- "class"
- "code"
- "conformsToProtocol:"
- "containsObject:"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "currentHandler"
- "date"
- "debugDescription"
- "description"
- "domain"
- "errorWithDomain:code:userInfo:"
- "fileURLWithPath:"
- "fulfill"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hash"
- "image"
- "imageByPreparingThumbnailOfSize:"
- "imageFileURL"
- "imageURL"
- "incomingPushResultForChannelManager:channelUUID:pushPayload:"
- "incomingServiceUpdatePushForChannelManager:channelUUID:pushPayload:isHighPriority:remainingHighPriorityBudget:withCompletionHandler:"
- "infoDictionary"
- "init"
- "initWithChannelUUID:"
- "initWithChannelUUID:name:"
- "initWithConfiguration:"
- "initWithName:image:"
- "initWithName:imageURL:"
- "instantiationCompletionBlock"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isHighPriority"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isServiceUpdateMessage"
- "isWaitingForPushResult"
- "isiOSAppOnMac"
- "leaveChannelPushResult"
- "leaveChannelWithUUID:"
- "length"
- "mainBundle"
- "name"
- "objectForKeyedSubscript:"
- "originator"
- "payload"
- "pendingPushes"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processInfo"
- "provider:didActivateAudioSession:"
- "provider:didDeactivateAudioSession:"
- "provider:didReceiveChannelPushToken:"
- "provider:didReceiveCheckInResult:channelUUID:"
- "provider:didReceivePushPayload:"
- "provider:didReceivePushPayload:channelUUID:"
- "provider:didReceivePushPayload:channelUUID:reply:isServiceUpdateMessage:isHighPriority:remainingHighPriorityBudget:"
- "provider:executeTransaction:"
- "provider:performChannelJoinAction:"
- "provider:performChannelLeaveAction:"
- "provider:performChannelTransmitStartAction:"
- "provider:performChannelTransmitStopAction:"
- "provider:timedOutPerformingAction:"
- "providerDidBegin:"
- "providerDidReset:"
- "pushResultForActiveRemoteParticipant:"
- "q"
- "q16@0:8"
- "raise:format:"
- "release"
- "remainingHighPriorityBudget"
- "removeAllObjects"
- "reply"
- "reportChannelWithUUID:disconnectedAtDate:disconnectedReason:"
- "reportChannelWithUUID:updated:completionHandler:"
- "reportIncomingTransmissionEndedForChannelWithUUID:reason:completionHandler:"
- "reportIncomingTransmissionStartedForChannelWithUUID:update:shouldReplaceOutgoingTransmission:completionHandler:"
- "requestBeginTransmittingWithChannelUUID:"
- "requestChannelPushToken"
- "requestJoinChannelWithUUID:descriptor:"
- "requestTransactionWithAction:completion:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "serviceUpdatePushResult"
- "setAccessoryButtonEventsEnabled:"
- "setAccessoryButtonEventsEnabled:forChannelUUID:completionHandler:"
- "setActiveRemoteParticipant:"
- "setActiveRemoteParticipant:forChannelUUID:completionHandler:"
- "setAttemptingChannelRestoration:"
- "setCallbackQueue:"
- "setChannelDescriptor:forChannelUUID:completionHandler:"
- "setChannelEventDelegate:"
- "setChannelRestorationDelegate:"
- "setDelegate:queue:"
- "setImageURL:"
- "setInstantiationCompletionBlock:"
- "setIsHighPriority:"
- "setIsServiceUpdateMessage:"
- "setIsWaitingForPushResult:"
- "setName:"
- "setOriginator:"
- "setParticipant:"
- "setPayload:"
- "setPendingPushes:"
- "setRemainingHighPriorityBudget:"
- "setReply:"
- "setServiceStatus:"
- "setServiceStatus:forChannelUUID:completionHandler:"
- "setStopTransmitRequestedWhileWaitingForPushResult:"
- "setSuppressRejoinForRecentlyDisconnectedChannelUUID:"
- "setTransmissionMode:"
- "setTransmissionMode:forChannelUUID:completionHandler:"
- "setUuid:"
- "setWaitingForPushResultChannelUUID:"
- "setWrappedByObject:"
- "stopTransmitRequestedWhileWaitingForPushResult"
- "stopTransmittingWithChannelUUID:"
- "stringByAppendingPathComponent:"
- "stringWithFormat:"
- "superclass"
- "suppressRejoinForRecentlyDisconnectedChannelUUID"
- "type"
- "underlyingParticipant"
- "underlyingProvider"
- "unregisterChannelPushToken"
- "userInfo"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<CXAbstractProvider>\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8q16"
- "v32@0:8@\"<CXAbstractProvider>\"16@\"CXAction\"24"
- "v32@0:8@\"CXChannelProvider\"16@\"AVAudioSession\"24"
- "v32@0:8@\"CXChannelProvider\"16@\"CXChannelJoinAction\"24"
- "v32@0:8@\"CXChannelProvider\"16@\"CXChannelLeaveAction\"24"
- "v32@0:8@\"CXChannelProvider\"16@\"CXChannelTransmitStartAction\"24"
- "v32@0:8@\"CXChannelProvider\"16@\"CXChannelTransmitStopAction\"24"
- "v32@0:8@\"CXChannelProvider\"16@\"NSData\"24"
- "v32@0:8@\"CXChannelProvider\"16@\"NSDictionary\"24"
- "v32@0:8@16@24"
- "v32@0:8@16q24"
- "v36@0:8B16@20@?28"
- "v40@0:8@\"CXChannelProvider\"16@\"NSDictionary\"24@\"NSUUID\"32"
- "v40@0:8@\"CXChannelProvider\"16q24@\"NSUUID\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16q24@32"
- "v40@0:8q16@24@?32"
- "v44@0:8@16@24B32@?36"
- "v48@0:8@16@24q32@?40"
- "v56@0:8@16@24@?32B40B44q48"
- "v64@0:8@\"CXChannelProvider\"16@\"NSDictionary\"24@\"NSUUID\"32@?<v@?q@\"CXParticipant\">40B48B52q56"
- "v64@0:8@16@24@32@?40B48B52q56"
- "waitingForPushResultChannelUUID"
- "writeToFile:atomically:"
- "zone"

```
