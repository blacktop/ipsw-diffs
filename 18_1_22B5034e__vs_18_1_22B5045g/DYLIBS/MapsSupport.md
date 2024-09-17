## MapsSupport

> `/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport`

```diff

-2864.31.7.31.6
-  __TEXT.__text: 0x74ca0
-  __TEXT.__auth_stubs: 0xab0
-  __TEXT.__objc_methlist: 0x6a28
-  __TEXT.__const: 0x278
-  __TEXT.__cstring: 0x5947
-  __TEXT.__oslogstring: 0x76cf
-  __TEXT.__gcc_except_tab: 0x1128
+2864.31.7.31.13
+  __TEXT.__text: 0x7d20c
+  __TEXT.__auth_stubs: 0xad0
+  __TEXT.__objc_methlist: 0x6f78
+  __TEXT.__const: 0x280
+  __TEXT.__cstring: 0x5e36
+  __TEXT.__oslogstring: 0x7fe9
+  __TEXT.__gcc_except_tab: 0x1324
   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__ustring: 0x2b2
-  __TEXT.__unwind_info: 0x1ba0
-  __TEXT.__objc_classname: 0x113c
-  __TEXT.__objc_methname: 0x10e09
-  __TEXT.__objc_methtype: 0x3268
-  __TEXT.__objc_stubs: 0xc440
-  __DATA_CONST.__got: 0x688
-  __DATA_CONST.__const: 0x26c0
-  __DATA_CONST.__objc_classlist: 0x310
+  __TEXT.__unwind_info: 0x1db8
+  __TEXT.__objc_classname: 0x12c8
+  __TEXT.__objc_methname: 0x1185e
+  __TEXT.__objc_methtype: 0x34e1
+  __TEXT.__objc_stubs: 0xcc00
+  __DATA_CONST.__got: 0x6b8
+  __DATA_CONST.__const: 0x2a00
+  __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x220
+  __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ec8
-  __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x328
+  __DATA_CONST.__objc_selrefs: 0x4108
+  __DATA_CONST.__objc_protorefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x568
-  __AUTH_CONST.__const: 0xae0
-  __AUTH_CONST.__cfstring: 0x41a0
-  __AUTH_CONST.__objc_const: 0xeea0
-  __AUTH_CONST.__objc_intobj: 0x1f8
+  __AUTH_CONST.__auth_got: 0x578
+  __AUTH_CONST.__const: 0xbc0
+  __AUTH_CONST.__cfstring: 0x4340
+  __AUTH_CONST.__objc_const: 0xf940
+  __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x14a0
+  __AUTH.__objc_data: 0x1720
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x458
-  __DATA.__data: 0x1c50
-  __DATA.__bss: 0x20
-  __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x34c
-  __DATA_DIRTY.__objc_data: 0xa00
+  __DATA.__objc_ivar: 0x4bc
+  __DATA.__data: 0x1d80
+  __DATA.__bss: 0x30
+  __DATA.__common: 0x20
+  __DATA_DIRTY.__objc_ivar: 0x35c
+  __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x260
   __DATA_DIRTY.__common: 0x30

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
+  - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MapsSync.framework/MapsSync
   - /System/Library/PrivateFrameworks/Navigation.framework/Navigation

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2668
-  Symbols:   3184
-  CStrings:  4675
+  Functions: 2830
+  Symbols:   3352
+  CStrings:  4871
 
Symbols:
+ _GEOConfigMSPShareETACapabilityFetchingServerPurgeInterval
+ _IMServiceNameiMessage
+ _MSPSharedTripServiceiMessage
+ _MSPSharedTripServiceSMS
+ _xpc_connection_copy_invalidation_reason
+ _MSPSharedTripServiceMaps
+ _IMSPICalculateSendingServiceByDestinationsAndChatGUID
+ _IMServiceNameiMessageLite
+ _MSPSharedTripVirtualReceiverHandleGetServiceName
- _IMSPISMSService
- _IMSPIiMessageService
CStrings:
+ "rcsVirtualReceiverWithName:"
+ "_requestedHandles"
+ "[%!{(MISSING)public}@] Virtual Senders are supported"
+ "@56@0:8@16Q24@32@40@48"
+ "[%!{(MISSING)public}@] retrying fetch in response to IDSBatchQueryController back-off"
+ "capabilityLevelForContact returning cached %!{(MISSING)public}@ capability type for %!@(MISSING)"
+ "_verifyCurrentlyUnblockedStatuses"
+ "_purgeTimer"
+ "v64@0:8@16Q24@32@40@48@?56"
+ "keyEnumerator"
+ "v48@0:8@\"NSArray\"16Q24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "MSPSharedTripCapabilityFetchingPeer"
+ "_performBlockOnAllQueues:"
+ "_fetchTextMessageReachability:"
+ "serviceNameForContact virtual receiver %!{(MISSING)public}@ is %!{(MISSING)public}@"
+ "%!{(MISSING)public}@: purging expired status for handle %!{(MISSING)private}@"
+ "capabilityLevelForContact cache miss for handle %!@(MISSING) (%!{(MISSING)public}@)"
+ "\t- Skipping %!{(MISSING)private}@, none of the peer-requested handles have both statues yet"
+ "_updateRequestedHandlesWithAdditions:subtractions:"
+ "[%!{(MISSING)public}@] addLiveParticipants %!{(MISSING)private}@ no live sender"
+ "[%!{(MISSING)public}@] Creating batch ID query controller"
+ "com.apple.Maps.SharedTrip.Capabilities"
+ "restoreFromGroupSessionStorage:"
+ "_processUpdates:"
+ "@20@0:8B16"
+ "- %!{(MISSING)private}@ is now blocked"
+ "[ContactController] shareWithContactValue received capability for pending contact %!{(MISSING)private}@: %!{(MISSING)public}@/%!{(MISSING)public}@"
+ "SharedTripCapabilityFetching"
+ "_serviceNamesByActiveHandle"
+ "_textMessageStatusFetchQueue"
+ "T@\"NSOrderedSet\",R,C,N"
+ "v32@0:8@\"MSPSharedTripCapabilityFetchingQueue\"16@\"NSDictionary\"24"
+ "Q32@0:8@16^@24"
+ "_notifyPeersForIDSHandlesIfNeeded:"
+ "[%!{(MISSING)public}@] addParticipants %!{(MISSING)private}@ to %!{(MISSING)public}@/%!{(MISSING)public}@"
+ "v32@?0@\"NSString\"8@\"NSMutableDictionary\"16^B24"
+ "Fetched service %!{(MISSING)public}@ for %!{(MISSING)private}@, but it was no longer in fetch queue, dropping"
+ "- removing %!l(MISSING)u blocked handles from statuses"
+ "_currentMinimalSenderForServiceName:createIfNeeded:"
+ "_updateGroupSessionStorage:"
+ "[Peer] Updated contacts: %!{(MISSING)private}@\n\tAdded: %!{(MISSING)private}@\n\tRemoved: %!{(MISSING)private}@"
+ "com.apple.Maps.xpc.SharedTrip.Capabilities"
+ "\tSkipping all peer notifications, no handles have all services checked"
+ "processPendingHandles"
+ "1A"
+ "removeParticipant:reason:"
+ "stopSharingWith: %!{(MISSING)public}@ wasSharing: %!{(MISSING)public}@"
+ "[%!{(MISSING)public}@] restoreFromGroupStorage"
+ "will update from controller"
+ "B32@0:8@\"MSPSharedTripCapabilityFetchingQueue\"16@\"NSString\"24"
+ "v24@?0@\"NSString\"8@\"NSArray\"16"
+ "removeLiveParticipant:"
+ "v28@0:8B16@?20"
+ "- %!{(MISSING)private}@ was recorded blocked, record expired, but handle still blocked, will update record"
+ "v48@?0@\"MSPSharedTripSharingIdentity\"8@\"NSArray\"16@\"NSDictionary\"24@\"NSArray\"32Q40"
+ "\x14\x11"
+ "v24@?0@\"MSPSenderStrategy\"8@\"NSString\"16"
+ "-[MSPSharedTripServer startSharingTripWithContacts:capabilityType:serviceName:completion:]"
+ "_senderStrategyController"
+ "_pendingHandles"
+ "updateRequestedHandlesWithAdditions:subtractions:"
+ "RCS"
+ "\r"
+ "capabilityLevelsDidUpdate:"
+ "_currentSendersByServiceName"
+ "countForObject:"
+ "_statusesByIdentifier"
+ "addEntriesFromDictionary:"
+ "\x04\x12"
+ "[Sender] live participant did join %!@(MISSING)"
+ "@40@0:8@16Q24@32"
+ "serviceName"
+ "capabilityLevelForContact nil service name for blocked %!{(MISSING)private}@"
+ "performWithVirtualSenders:block:"
+ "addLiveParticipants:"
+ "[%!{(MISSING)public}@] updateGroupSessionStorage clearing storage, %!s(MISSING)"
+ "[%!{(MISSING)public}@] idStatusUpdatedForDestinations %!{(MISSING)public}@ service: %!{(MISSING)private}@"
+ "initWithDelegate:queue:label:"
+ "SharedTripCapabilityFetchingQueue"
+ "v16@?0@\"MSPSharedTripCapabilityFetchingQueue\"8"
+ "\x01\x15"
+ "@\"MSPSharedTripSenderStrategyController\""
+ "_nestedVirtualReceiverEnablement"
+ "markHandlesInflight:"
+ "requesting %!l(MISSING)u %!{(MISSING)public}@ handles"
+ "TQ,R,N,V_capabilityType"
+ "[Server] Accepting new connection: %!@(MISSING)"
+ "initWithCapabilityType:serviceName:status:"
+ "serviceNamesByActiveHandle"
+ "removeRequestedHandles:"
+ "%!@(MISSING) (%!@(MISSING)) <delegate: %!@(MISSING), %!l(MISSING)u pending: %!@(MISSING), %!l(MISSING)u inflight: %!@(MISSING)>"
+ "stringWithUTF8String:"
+ "capabilityLevelForContact cache hit for handle %!@(MISSING) (%!{(MISSING)public}@)"
+ "@40@0:8#16#24@32"
+ "_connectionInterrupted:"
+ "unionOrderedSet:"
+ "\t- notifying peer %!{(MISSING)public}@ of %!l(MISSING)u resolved statuses: %!{(MISSING)private}@"
+ "performWithAllMinimalSenders:"
+ "_performBlockWithMinimalSenders:"
+ "MSPSharedTripXPCCapabilityFetching"
+ "_purgeExpiredStatuses"
+ "MSPSharedTripFetchedCapabilityStatus"
+ "Fetch contacts: %!{(MISSING)private}@\n\tAdded: %!{(MISSING)private}@,\n\tRemoved: %!{(MISSING)private}@"
+ "MSPSharedTripIDSCapabilityFetchingQueue"
+ "pendingHandles"
+ "initWithGroupSession:messageStrategyDelegate:"
+ "_updateActiveSharingHandles:serviceNames:"
+ "MSPSharedTripMessagesCapabilityFetchingQueue"
+ "_updateTTL"
+ "[Sender] live participant did leave %!@(MISSING)"
+ "-[MSPSharedTripCapabilityFetchingServer dealloc]"
+ "_lock"
+ "@\"MSPSharedTripMessagesCapabilityFetchingQueue\""
+ "_markHandleInflight:"
+ "[%!{(MISSING)public}@] mark handle inflight: %!{(MISSING)private}@"
+ "[%!{(MISSING)public}@] %!{(MISSING)public}@/%!{(MISSING)public}@: no message body generated but we expected to send something to %!{(MISSING)private}@"
+ "serviceName=%!@(MISSING)"
+ "-[MSPSharedTripCapabilityFetchingServer cancelFetchCapabilitiesForContacts:]"
+ "_fetchQueue"
+ "B40@0:8@16@24Q32"
+ "[%!{(MISSING)public}@] updateGroupSessionStorage"
+ "sharedTripDidUpdateRecipients:withServices:"
+ "_verifyCurrentlyBlockedStatuses"
+ "MSPSharedTripCapabilityFetchingQueueDelegate"
+ "[Server] Removing peer %!{(MISSING)public}@"
+ "%!@(MISSING) (%!@(MISSING)) <status: %!l(MISSING)d, expired: %!s(MISSING), failed: %!s(MISSING), blocked: %!s(MISSING)>"
+ "capabilityFetchingQueue:shouldFetchHandle:"
+ "SharedTripVirtualReceiver"
+ "[Server] Checking existing blocked statuses for now-unblocked handles..."
+ "^{os_unfair_lock_s=I}"
+ "\x03\x14"
+ "-[MSPSharedTripCapabilityFetchingServer cleanConnections]"
+ "_handleCheckinWithSharingIdentity:activeRecipients:serviceNamesByHandle:receivedTrips:permissions:"
+ "v24@?0@\"NSArray\"8@\"NSDictionary\"16"
+ "fetchCapabilitiesForContacts:"
+ "minusOrderedSet:"
+ "- %!{(MISSING)private}@ is blocked, will record"
+ "v32@?0Q8@\"NSString\"16@\"NSError\"24"
+ "[Peer] Still waiting for %!{(MISSING)private}@"
+ "[%!{(MISSING)public}@] Got a callback while backing off, fire immediately to trigger updates for both services"
+ "[%!{(MISSING)public}@] %!{(MISSING)public}@/%!{(MISSING)public}@: IMSPISendMessageWithAttachments returned NO"
+ "MSPShareETACapabilityFetchingServerPurgeIntervalKey"
+ "v24@0:8@?<v@?@\"MSPSharedTripSharingIdentity\"@\"NSArray\"@\"NSDictionary\"@\"NSArray\"Q>16"
+ "[Server] Clearing peer's requested handles from queue: %!{(MISSING)private}@"
+ "markHandleInflight:"
+ "startSharingWith:capabilityType:serviceName:error:"
+ "[%!{(MISSING)public}@] removeParticipant %!{(MISSING)private}@ %!s(MISSING) from %!{(MISSING)public}@/%!{(MISSING)public}@"
+ "_xpcConnection"
+ "-[MSPSharedTripCapabilityFetchingServer createXPCListener]"
+ "_markHandlesInflight:"
+ "capabilityTypeForContact:serviceName:isActiveReceiver:"
+ "v24@?0@\"MSPSharedTripSenderStrategyController\"8@\"NSArray\"16"
+ "-[MSPSharedTripService sharedTripDidUpdateRecipients:withServices:]"
+ "_set"
+ "capabilityType"
+ "[Server] Checking blocklist to see if any cached statuses are now blocked..."
+ "stopSharingWith (virtual): %!{(MISSING)public}@ wasSharing: %!{(MISSING)public}@"
+ "_removePeerForConnection:"
+ "MSPSharedTripXPCCapabilityReceiving"
+ "Will notify for update of %!{(MISSING)private}@"
+ "_createMinimalSenderWithMapsClass:messagesClass:serviceName:"
+ "v56@0:8@16@24@32@40Q48"
+ "[%!{(MISSING)public}@] (%!@(MISSING)) updatedDestinationsStatus error %!@(MISSING)"
+ "v16@?0@\"MSPSharedTripSenderStrategyController\"8"
+ "- %!{(MISSING)private}@ already recorded as blocked, not expired"
+ "Text Message"
+ "removeLiveParticipants:"
+ "inflightHandles"
+ "_performBlockOnAllCachedStatus:"
+ "\t- Skipping %!{(MISSING)private}@, no requested handles"
+ "com.apple.Maps.SharedTrip.CapabilityFetching.Queue.%!@(MISSING)"
+ "Fetched service %!{(MISSING)public}@ for %!{(MISSING)private}@"
+ "A"
+ "updateGroupSessionStorage:fromController:"
+ "dictionaryWithValuesForKeys:"
+ "no strategy controller to update from"
+ "[%!{(MISSING)public}@] %!{(MISSING)public}@/%!{(MISSING)public}@: sendMessageIfNeeded will send %!{(MISSING)public}@ to participant %!{(MISSING)private}@"
+ "_counts"
+ "requesting %!l(MISSING)u Text Message handles from IDS"
+ "A!"
+ "serviceNameForContact:"
+ "_currentLiveSender:"
+ "[%!{(MISSING)public}@] removeLiveParticipants %!{(MISSING)private}@ from %!{(MISSING)public}@"
+ "containsHandle:"
+ "_inflightHandles"
+ "@40@0:8Q16@24q32"
+ "[%!{(MISSING)public}@] Releasing batch ID query controller"
+ "startSharingTripWithContacts:capabilityType:serviceName:completion:"
+ "[%!{(MISSING)public}@] removeLiveParticipant %!{(MISSING)private}@ %!s(MISSING) from %!{(MISSING)public}@"
+ "_didStartSharingWithContact:withCapabilityType:serviceName:error:queue:completion:"
+ "[Server] System block list did update, scheduling coalescing check in %!l(MISSING)fs"
+ "_createMinimalSenderForServiceName:"
+ "_capabilityType"
+ "MSPSharedTripCapabilityFetchingServer"
+ "@\"MSPSharedTripIDSCapabilityFetchingQueue\""
+ "[%!{(MISSING)public}@] removeParticipant no sender for %!{(MISSING)public}@"
+ "[Server] Will start monitoring system block list updates"
+ "[%!{(MISSING)public}@] %!{(MISSING)public}@%!{(MISSING)public}@: no necessary notification for %!{(MISSING)private}@"
+ "cancelFetchCapabilitiesForContacts:"
+ "@\"MSPCountedOrderedSet\""
+ "\b"
+ "doubleValue"
+ "@\"NSDictionary\""
+ "T@\"<MSPSharedTripCapabilityFetchingQueueDelegate>\",W,N,V_delegate"
+ "initWithIDSService:capabilityType:delegate:queue:label:"
+ "[Server] will not accept connection due to missing sharing entitlement: %!@(MISSING)"
+ "addParticipants:forServiceName:"
+ "[%!{(MISSING)public}@] addParticipants %!{(MISSING)private}@ no sender for %!{(MISSING)public}@"
+ "_activeCapabilityTypeForContact:serviceName:"
+ "_capabilityFetchingServer"
+ "-[MSPSharedTripCapabilityFetchingServer fetchCapabilitiesForContacts:]"
+ "removeParticipant:forServiceName:reason:"
+ "[%!{(MISSING)public}@] addLiveParticipants %!{(MISSING)private}@ to %!{(MISSING)public}@"
+ "_connectionInvalidated:"
+ "MSPSharedTripXPCPeer"
+ "@\"MSPSharedTripCapabilityFetchingServer\""
+ "Cancel fetch contacts: %!{(MISSING)private}@\n\tRemoved: %!{(MISSING)private}@"
+ "_capabilityTypeForContact:serviceName:isActiveReceiver:"
+ "label"
+ "_senderStrategiesByServiceName"
+ "[ContactController] shareWithContactValue called for handle %!@(MISSING) with %!{(MISSING)public}@/%!{(MISSING)public}@. Will pass to trip service."
+ "_enableVirtualReceivers"
+ "v24@?0@\"NSMutableDictionary\"8@\"NSString\"16"
+ "Q40@0:8@16^@24^B32"
+ "_removeObjectNoLock:"
+ "v32@?0@8@16^B24"
+ "removeObjectsFromArray:"
+ "requestedHandles"
+ "[Peer] Removing requested contacts %!{(MISSING)private}@"
+ "\tSkipping %!{(MISSING)private}@, we haven't fetched both services yet"
+ "v40@0:8@16^@24^@32"
+ "[Server] Will stop monitoring system block list updates"
+ "_messageStrategyDelegate"
+ "@\"<MSPSharedTripCapabilityFetchingQueueDelegate>\""
+ "capabilityFetchingQueue:didFetchStatusForHandles:"
+ "v32@0:8@\"NSArray\"16@\"NSDictionary\"24"
+ "[%!{(MISSING)public}@] mark handles inflight: %!{(MISSING)private}@"
+ "T@\"NSString\",R,N,V_serviceName"
+ "_virtualSenderStrategiesByServiceName"
+ "T@\"NSString\",R,C,N,V_label"
+ "capabilityLevelForContact returning cached service name %!{(MISSING)public}@"
+ "error calling to remote object: %!{(MISSING)public}@"
+ "B48@0:8@16Q24@32^@40"
+ "[%!{(MISSING)public}@] need to back off, will retry in %!l(MISSING)fs"
+ "\tChecking peer %!{(MISSING)public}@"
+ "updateActiveSharingHandles:serviceNames:"
+ "[Service] Connection invalidated: %!@(MISSING), reason: %!{(MISSING)public}@"
+ "_identifierToTextMessageStatus"
+ "Will fetch best text service for %!{(MISSING)private}@"
+ "_batchIDQueryController"
+ "_startSharingTripWithContacts:capabilityType:serviceName:completion:"
+ "MSPCountedOrderedSet"
+ "initWithDelegate:capabilityType:serviceName:"
+ "updateRequestedHandles:added:removed:"
+ "MSPSharedTripCapabilityFetchingQueue"
+ "%!@(MISSING) (%!@(MISSING)) add: %!l(MISSING)u %!{(MISSING)private}@, removed: %!l(MISSING)u %!{(MISSING)private}@"
+ "_addObjectNoLock:"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSDictionary\">16"
+ "[%!{(MISSING)public}@] %!{(MISSING)public}@/%!{(MISSING)public}@: sendMessageIfNeeded called without requisite state (state: %!{(MISSING)public}@, etaInfo: %!{(MISSING)public}@, destinationInfo: %!{(MISSING)public}@)"
+ "[%!{(MISSING)public}@] %!{(MISSING)public}@/%!{(MISSING)public}@: TO %!{(MISSING)public}@: \"%!{(MISSING)public}@\""
+ "activeCapabilityTypeForContact:serviceName:"
+ "MSPSharedTripSenderStrategyController"
+ "_label"
+ "T@\"NSDictionary\",R,N"
+ "v32@?0@\"NSString\"8@\"MSPSharedTripFetchedCapabilityStatus\"16^B24"
+ "textmessage"
+ "[%!{(MISSING)public}@] removeParticipant %!{(MISSING)private}@ from %!{(MISSING)public}@/%!{(MISSING)public}@"
+ "_processResults:"
- "- %!{(MISSING)private}@ is blocked"
- "[%!{(MISSING)public}@] %!{(MISSING)public}@: TO %!{(MISSING)public}@: \"%!{(MISSING)public}@\""
- "_virtualSMSSender"
- "[%!{(MISSING)public}@] %!{(MISSING)public}@: no necessary notification for %!{(MISSING)private}@"
- "@\"MSPSenderVirtualMinimalStrategy\""
- "_minimalSender"
- "v32@?0@\"NSString\"8@\"MSPSharedTripFetchedStatus\"16^B24"
- "_iMessageSender"
- "_processResult:forContainer:fetchQueue:"
- "processing blocked handles..."
- "[Sender] new stream participants %!@(MISSING)"
- "Creating Messages batch ID query controller"
- "sharedTripDidUpdateRecipients:"
- "1\xb1"
- "removeParticipant:"
- "initWithDelegate:capabilityType:"
- "capabilityLevelForContact cache miss for handle %!@(MISSING) (Maps: %!{(MISSING)public}@, iMessage: %!{(MISSING)public}@)"
- "startSharingWith:capabilityType:error:"
- "_smsSender"
- "capabilityLevelForContact returning cached iMessage capability type for %!@(MISSING)"
- "_virtualiMessageSender"
- "\x03\x1b"
- "idStatusUpdatedForDestinations Maps service: %!@(MISSING)"
- "capabilityLevelForContact returning cached Maps capability type for %!@(MISSING)"
- "_handleCheckinWithSharingIdentity:activeRecipients:receivedTrips:permissions:"
- "Got a callback while backing off, fire immediately to trigger updates for both services"
- "v24@0:8@?<v@?@\"MSPSharedTripSharingIdentity\"@\"NSArray\"@\"NSArray\"Q>16"
- "MSPSharedTripPeer"
- "[%!{(MISSING)public}@] %!{(MISSING)public}@: sendMessageIfNeeded called without requisite state (state: %!{(MISSING)public}@, etaInfo: %!{(MISSING)public}@, destinationInfo: %!{(MISSING)public}@)"
- "Releasing iMessage batch ID query controller"
- "(%!@(MISSING)) updatedDestinationsStatus error %!@(MISSING)"
- "_updateActiveSharingHandles:"
- "_startSharingTripWithContacts:capabilityType:completion:"
- "processMessagesDictionary:"
- "checking for blocked handles..."
- "[%!{(MISSING)public}@] %!{(MISSING)public}@: IMSPISendMessageWithAttachments returned NO"
- "retrying fetch in response to IDSBatchQueryController back-off"
- "sms"
- "_mapsBatchController"
- "updated blocked statuses, notifying observers"
- "@\"MSPSenderVirtualMessageStrategy\""
- "-[MSPSharedTripService sharedTripDidUpdateRecipients:]"
- "no updates after processing blocked handles"
- "v48@0:8@16@24@32Q40"
- "[%!{(MISSING)public}@] %!{(MISSING)public}@: sendMessageIfNeeded will send %!{(MISSING)public}@ to participant %!{(MISSING)private}@"
- "v56@0:8@16Q24@32@40@?48"
- "@\"MSPSenderMinimalStrategy\""
- "v40@?0@\"MSPSharedTripSharingIdentity\"8@\"NSArray\"16@\"NSArray\"24Q32"
- "initWithStatus:"
- "\t"
- "[ContactController] shareWithContactValue called for handle %!@(MISSING) with %!{(MISSING)public}@. Will pass to trip service."
- "-[MSPSharedTripServer startSharingTripWithContacts:capabilityType:completion:]"
- "processMapsDictionary:"
- "removing %!l(MISSING)u blocked handles from fetch queues"
- "no blocked handles in fetch queues"
- "_didStartSharingWithContact:withCapabilityType:error:queue:completion:"
- "- removing %!l(MISSING)u blocked handles from %!{(MISSING)public}@ statuses"
- "capabilityLevelForContact cache hit for handle %!@(MISSING) (Maps: %!{(MISSING)public}@, iMessage: %!{(MISSING)public}@)"
- "- %!{(MISSING)private}@ recorded as blocked+expired, but handle still blocked"
- "requesting %!l(MISSING)u Maps and %!l(MISSING)u iMessage handles from IDS"
- "status: %!l(MISSING)d, expired: %!s(MISSING), failed: %!s(MISSING), blocked: %!s(MISSING)"
- "[ContactController] shareWithContactValue received capability for pending contact %!{(MISSING)private}@: %!l(MISSING)u"
- "1!"
- "Creating Maps batch ID query controller"
- "stopSharingWith: %!{(MISSING)public}@ wasInMinimal: %!{(MISSING)public}@, wasInLive: %!{(MISSING)public}@, wasIniMessage: %!{(MISSING)public}@, wasInSMS: %!{(MISSING)public}@"
- "stopSharingWith: %!{(MISSING)private}@ wasInVirtualMinimal: %!{(MISSING)public}@, wasInVirtualLive: %!{(MISSING)public}@, wasInVirtualiMessage: %!{(MISSING)public}@, wasInVirtualSMS: %!{(MISSING)public}@"
- "@\"MSPSenderMessageStrategy\""
- "Releasing Maps batch ID query controller"
- "MSPSharedTripFetchedStatus"
- "recording %!{(MISSING)private}@ as blocked"
- "- %!{(MISSING)private}@ recorded as blocked, not expired"
- "startSharingTripWithContacts:capabilityType:completion:"
- "updateActiveSharingHandles:"
- "\x03\x12"
- "idStatusUpdatedForDestinations iMessage service: %!@(MISSING)"
- "[%!{(MISSING)public}@] no message body generated but we expected to send something"
- "_virtualMinimalSender"
- "SharedTripCapabilityFetcher"
- "need to back off, will retry in %!l(MISSING)fs"

```
