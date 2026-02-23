## identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

-1969.500.52.2.4
-  __TEXT.__text: 0xa5bb5c
-  __TEXT.__auth_stubs: 0x6e30
-  __TEXT.__objc_stubs: 0x48a60
-  __TEXT.__objc_methlist: 0x2b154
-  __TEXT.__const: 0x69c10
-  __TEXT.__gcc_except_tab: 0x27090
-  __TEXT.__objc_methname: 0x78b65
-  __TEXT.__cstring: 0x56cf7
-  __TEXT.__oslogstring: 0x80716
-  __TEXT.__objc_classname: 0x777b
-  __TEXT.__objc_methtype: 0x13bee
+1969.500.75.0.0
+  __TEXT.__text: 0xa4beb4
+  __TEXT.__auth_stubs: 0x6eb0
+  __TEXT.__objc_stubs: 0x48d20
+  __TEXT.__objc_methlist: 0x2b24c
+  __TEXT.__const: 0x6c670
+  __TEXT.__gcc_except_tab: 0x274f4
+  __TEXT.__objc_methname: 0x79055
+  __TEXT.__cstring: 0x574c7
+  __TEXT.__oslogstring: 0x80d36
+  __TEXT.__objc_classname: 0x7c6b
+  __TEXT.__objc_methtype: 0x13c6e
   __TEXT.__ustring: 0x4ca
   __TEXT.__dlopen_cstrs: 0xea
-  __TEXT.__swift5_typeref: 0x8352
-  __TEXT.__swift5_capture: 0x1eb4
-  __TEXT.__constg_swiftt: 0x6228
-  __TEXT.__swift5_reflstr: 0x6c54
-  __TEXT.__swift5_fieldmd: 0x7324
-  __TEXT.__swift5_protos: 0xa8
-  __TEXT.__swift5_proto: 0xb98
-  __TEXT.__swift5_types: 0x740
+  __TEXT.__swift5_typeref: 0x8a1a
+  __TEXT.__swift5_capture: 0x1fac
+  __TEXT.__constg_swiftt: 0x679c
+  __TEXT.__swift5_reflstr: 0x7524
+  __TEXT.__swift5_fieldmd: 0x7c14
+  __TEXT.__swift5_proto: 0xca8
+  __TEXT.__swift5_types: 0x7a8
   __TEXT.__swift_as_entry: 0x284
   __TEXT.__swift_as_ret: 0x2a8
-  __TEXT.__swift5_builtin: 0x21c
-  __TEXT.__swift5_assocty: 0x1148
+  __TEXT.__swift5_builtin: 0x208
+  __TEXT.__swift5_protos: 0x9c
+  __TEXT.__swift5_assocty: 0x1388
   __TEXT.__swift5_acfuncs: 0xa0
   __TEXT.__swift5_mpenum: 0x68
-  __TEXT.__unwind_info: 0x15d38
-  __TEXT.__eh_frame: 0xea2c
-  __DATA_CONST.__auth_got: 0x3728
-  __DATA_CONST.__got: 0x3ff8
+  __TEXT.__unwind_info: 0x16648
+  __TEXT.__eh_frame: 0xfc34
+  __DATA_CONST.__auth_got: 0x3768
+  __DATA_CONST.__got: 0x4038
   __DATA_CONST.__auth_ptr: 0xdc8
-  __DATA_CONST.__const: 0x32568
-  __DATA_CONST.__cfstring: 0x34da0
-  __DATA_CONST.__objc_classlist: 0x1290
+  __DATA_CONST.__const: 0x2f868
+  __DATA_CONST.__cfstring: 0x351c0
+  __DATA_CONST.__objc_classlist: 0x1300
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x808
+  __DATA_CONST.__objc_protolist: 0x810
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x180
+  __DATA_CONST.__objc_protorefs: 0x190
   __DATA_CONST.__objc_superrefs: 0xba8
-  __DATA_CONST.__objc_intobj: 0x1ae8
+  __DATA_CONST.__objc_intobj: 0x1ab8
   __DATA_CONST.__objc_arraydata: 0x5b0
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x4b458
-  __DATA.__objc_selrefs: 0x16708
-  __DATA.__objc_ivar: 0x33ac
-  __DATA.__objc_data: 0xdb28
-  __DATA.__data: 0x121c0
+  __DATA.__objc_const: 0x4c900
+  __DATA.__objc_selrefs: 0x167a0
+  __DATA.__objc_ivar: 0x338c
+  __DATA.__objc_data: 0xe0c8
+  __DATA.__data: 0x13068
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1a768
+  __DATA.__bss: 0x1cf98
   __DATA.__common: 0xf58
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libsqlite3.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCallKit.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 022916D4-5433-32BD-9254-9F17386B5F38
-  Functions: 28159
-  Symbols:   2840
-  CStrings:  42526
+  UUID: E4E1D05A-8EE3-3B51-8CF7-E813135CA1D9
+  Functions: 29071
+  Symbols:   2846
+  CStrings:  42672
 
Symbols:
+ _CFStringGetCStringPtr
+ _CFStringGetMaximumSizeForEncoding
+ _IDSIncomingMessageErrorDomain
+ _IDSNormalizedID
+ _objc_retain_x11
+ _sqlite3_bind_null
+ _sqlite3_bind_text
- _CFDataCreateCopy
CStrings:
+ "%s: GUIDs count %lu ignoringGUIDs count %lu {repeatedAttempt: %@}"
+ "%s: Invalid transition: Received %s while in state %s"
+ ") ORDER BY ROWID DESC"
+ "-[IDSDaemon(Messaging) _processStoredIncomingRemoteBatchMessages]"
+ "/Library/Caches/com.apple.xbs/116D1FB6-3A8B-4237-B623-E90D21AEA7BA/TemporaryDirectory.sXWGZI/Sources/IdentityServices_Swift/IDSAgent/IDSBTDatagramLink.m"
+ "/Library/Caches/com.apple.xbs/116D1FB6-3A8B-4237-B623-E90D21AEA7BA/TemporaryDirectory.sXWGZI/Sources/IdentityServices_Swift/IDSAgent/IDSBTLELink.m"
+ "/Library/Caches/com.apple.xbs/116D1FB6-3A8B-4237-B623-E90D21AEA7BA/TemporaryDirectory.sXWGZI/Sources/IdentityServices_Swift/IDSAgent/IDSBTLink.m"
+ "/Library/Caches/com.apple.xbs/116D1FB6-3A8B-4237-B623-E90D21AEA7BA/TemporaryDirectory.sXWGZI/Sources/IdentityServices_Swift/IDSAgent/IDSClientChannelManager.m"
+ "/Library/Caches/com.apple.xbs/116D1FB6-3A8B-4237-B623-E90D21AEA7BA/TemporaryDirectory.sXWGZI/Sources/IdentityServices_Swift/IDSAgent/IDSLinkManager.m"
+ "/Library/Caches/com.apple.xbs/116D1FB6-3A8B-4237-B623-E90D21AEA7BA/TemporaryDirectory.sXWGZI/Sources/IdentityServices_Swift/IDSAgent/IDSMultiplexer.m"
+ "/Library/Caches/com.apple.xbs/116D1FB6-3A8B-4237-B623-E90D21AEA7BA/TemporaryDirectory.sXWGZI/Sources/IdentityServices_Swift/IDSAgent/IDSMultiplexerUtils.m"
+ "/Library/Caches/com.apple.xbs/116D1FB6-3A8B-4237-B623-E90D21AEA7BA/TemporaryDirectory.sXWGZI/Sources/IdentityServices_Swift/IDSAgent/IDSSessionMultiplexer.m"
+ "/Library/Caches/com.apple.xbs/116D1FB6-3A8B-4237-B623-E90D21AEA7BA/TemporaryDirectory.sXWGZI/Sources/IdentityServices_Swift/IDSAgent/IDSSockAddrPairTable.m"
+ "/Library/Caches/com.apple.xbs/116D1FB6-3A8B-4237-B623-E90D21AEA7BA/TemporaryDirectory.sXWGZI/Sources/IdentityServices_Swift/IDSAgent/IDSUDPGlobalLink.m"
+ "/Library/Caches/com.apple.xbs/116D1FB6-3A8B-4237-B623-E90D21AEA7BA/TemporaryDirectory.sXWGZI/Sources/IdentityServices_Swift/IDSAgent/IDSUTunControlChannel.m"
+ "/Library/Caches/com.apple.xbs/116D1FB6-3A8B-4237-B623-E90D21AEA7BA/TemporaryDirectory.sXWGZI/Sources/IdentityServices_Swift/IDSAgent/IDSUTunControlMessage.m"
+ "/Library/Caches/com.apple.xbs/116D1FB6-3A8B-4237-B623-E90D21AEA7BA/TemporaryDirectory.sXWGZI/Sources/IdentityServices_Swift/IDSAgent/IDSUTunController.m"
+ "/Library/Caches/com.apple.xbs/116D1FB6-3A8B-4237-B623-E90D21AEA7BA/TemporaryDirectory.sXWGZI/Sources/IdentityServices_Swift/IDSAgent/Session/IDSDSession.m"
+ "01:00:01"
+ "<%@: %p; identifier = %@; domain = %@>"
+ "<%@: %p; identifier = %@; persisters = %@>"
+ "@\"<NSCacheDelegate>\""
+ "@\"IDSPeerIDCache\""
+ "@\"IDSPeerIDValue\"20@?0@\"IDSPeerIDKey\"8B16"
+ "@\"NSArray\"24@?0@\"NSString\"8@\"IDSURI\"16"
+ "@32@0:8@?16@?24"
+ "@36@0:8@16B24^B28"
+ "@40@0:8@16B24B28^B32"
+ "@40@0:8@16I24C28^B32"
+ "@40@0:8@?16@24@?32"
+ "@80@0:8@16q24q32@40q48@56@64@72"
+ "Adding sentinel alias to existing account for repair {uniqueIdentifier: %@, account: %@}"
+ "Already processing batch messages"
+ "Cache Eviction { cache: %@, value: %@ }"
+ "Clearing preferences data {identifier: %@, domain: %@}"
+ "Composite persister found no data {identifier: %@}"
+ "Composite persister read from {identifier: %@, persister: %@}"
+ "DB Cache Bypassed, loaded from disk { service: %@, fromURI: %@, toURI: %@ }"
+ "DB Cache Miss, loaded from disk { service: %@, fromURI: %@, toURI: %@ }"
+ "DB Cache Miss, not found on disk { service: %@, fromURI: %@, toURI: %@ }"
+ "Deleted batchset with ssm: %@ { success: %@, error: %@ }"
+ "Error checking for pending batch contexts: %@"
+ "Error fetching all batch GUIDs: %@"
+ "Error fetching all batch message contexts: %@"
+ "Error fetching next batchset contexts: %@"
+ "Existing madrid account has no aliases, marking for sentinel alias repair"
+ "Failed to compress data for preferences {identifier: %@}"
+ "Failed to decompress preferences data {identifier: %@}"
+ "Failed to delete batchset contexts: %@"
+ "Failed to save batch message context %s: %@"
+ "Feb 16 2026"
+ "Finished processing stored messages from batch { topic: %@, batchIdentifier: %@, processed count: %ld }"
+ "Finished storing batch message { batchIdentifier: %@ } before first unlock. Stored %ld/%ld messages"
+ "Handling batch message { batchIdentifier: %@ } before first unlock"
+ "IDSPeerIDCache"
+ "IDSPeerIDCache %@, loading from disk { key: %@ }"
+ "IDSPeerIDCache eviction { value: %@ }"
+ "IDSPeerIDCache loaded from disk and cached { key: %@, endpointCount: %lu }"
+ "IDSPeerIDCache miss, no disk fallback (in-memory mode) { key: %@ }"
+ "IDSPeerIDCache.m"
+ "IDSPersistentMapCompositePersister"
+ "IDSPersistentMapPreferencesPersister"
+ "IDSServerBatchMessageContextWrapper"
+ "More batches to drain for topic %@, delivering next stored batch"
+ "No data found in preferences {identifier: %@, domain: %@}"
+ "No more batch messages to process"
+ "Not an internal install, not using Apple ID account synchronizer"
+ "PNR request is for Encrypted RCS -- ignoring consent prompt. {self: %@, uniqueIdentifier: %@}"
+ "PeerIDCache"
+ "Processing batchset with %ld batches for service: %@"
+ "Received complete batchset { batchIdentifier: %@, totalBatchCount: %@ } before first unlock. Signaling server to send next batchset"
+ "Received complete batchset { batchIdentifier: %@, totalBatchCount: %@ } for service without batch support. Signaling server to send next batchset"
+ "RestrictedIDStatusCache"
+ "Retrieved %ld messages for batch { batchIdentifier: %@ }"
+ "SELECT ROWID, guid, topic, from_id, message_data, date, is_local, message_identifier, expiration_date, control_category FROM incoming_message "
+ "Saving preferences data {identifier: %@, domain: %@, uncompressedSize: %lu, compressedSize: %lu}"
+ "Server bag key set for apple ID account synchronizer: %@"
+ "StandardIDStatusCache"
+ "Successfully deleted batchset contexts"
+ "Successfully saved batch message context %s"
+ "T@\"<NSCacheDelegate>\",W,N"
+ "T@\"<NSCacheDelegate>\",W,N,V_externalDelegate"
+ "T@\"<_TtP17identityservicesd47IDSGroupEncryptionKeyMaterialControllerDelegate_>\",N,R,Vdelegate"
+ "T@\"IDSDaemon\",&,N,V_daemon"
+ "T@\"IDSPeerIDCache\",&,N,V_peerIDCache"
+ "T@\"NSArray\",&,N,V_persisters"
+ "T@\"NSCache\",&,N,V_internalCache"
+ "T@\"NSDate\",N,R"
+ "T@\"NSMutableSet\",&,N,V_inMemoryKeys"
+ "T@\"NSString\",&,N,V_preferencesDomain"
+ "T@?,C,N,V_allKeysBlock"
+ "T@?,C,N,V_diskLoadBlock"
+ "TB,N,VrequiresSentinelAlias"
+ "TB,V_processingStoredIncomingRemoteBatchMessages"
+ "Timeout: More batches to drain for topic %@, delivering next stored batch set"
+ "Topic %@ has recently received/processed a message from storage.  Starting a new extended timer for retry."
+ "Tq,N,R,VbatchNumber"
+ "Tq,N,R,VserverStorageFlags"
+ "Tq,N,R,VtotalBatchCount"
+ "Tried to purge preferences before available -- returning {self: %@}"
+ "U2DEnabled: %@ [%@] State: %@ ssm: %@ last received: %@ last processed: %@ last delivered: %@ retry: %@"
+ "WHERE is_local = ? AND "
+ "We have %ld GUIDs in this batch { batchIdentifier: %@ } to retrieve"
+ "We're under first data protection lock - not broadcasting batch message."
+ "We've delivered the batch with ssm: %@ from local storage for topic %@"
+ "We've persisted the batch with ssm: %@ from server storage for topic %@"
+ "Will broadcast batchMessage: %@ (topic: %{public}@, isFromLocalStorage: %@)"
+ "_TtC17identityservicesd13SecKeyWrapper"
+ "_TtCO17identityservicesd21SDPersistenceSchemaV716IDSQuerySDDevice"
+ "_TtCO17identityservicesd21SDPersistenceSchemaV716IDSQuerySDStatus"
+ "_TtCO17identityservicesd21SDPersistenceSchemaV717IDSQuerySDSession"
+ "_TtCO17identityservicesd21SDPersistenceSchemaV720IDSRegistrationEvent"
+ "_TtCO17identityservicesd21SDPersistenceSchemaV721IDSQuerySDAddressable"
+ "_TtCO17identityservicesd21SDPersistenceSchemaV721IDSQuerySDShortHandle"
+ "_TtCO17identityservicesd21SDPersistenceSchemaV724IDSQuerySDPublicIdentity"
+ "_TtCO17identityservicesd21SDPersistenceSchemaV725IDSQualifiedContactsCount"
+ "_TtCO17identityservicesd21SDPersistenceSchemaV728IDSServerBatchMessageContext"
+ "_TtCO17identityservicesd21SDPersistenceSchemaV730IDSGroupEncryptionKeyRollIndex"
+ "_TtCO17identityservicesd21SDPersistenceSchemaV731IDSOffGridDeliveryDonatedHandle"
+ "_TtCO17identityservicesd21SDPersistenceSchemaV731IDSQuerySDSenderKeyDistribution"
+ "_TtP17identityservicesd38IDSGlobalLinkP2PKeyNegotiationDelegate_"
+ "_TtP17identityservicesd47IDSGroupEncryptionKeyMaterialControllerDelegate_"
+ "_allKeysBlock"
+ "_batchIdentifier"
+ "_batchNumber"
+ "_batchsetTracker"
+ "_daemon"
+ "_deleteProcessedBatchsetContextsForTopic:ssm:"
+ "_deliverNextStoredBatchsetForTopic:"
+ "_diskLoadBlock"
+ "_externalDelegate"
+ "_handleBatchMessageBeforeFirstUnlock:messageList:forTopic:serverStorageSSM:storageFlags:"
+ "_hasBatchesToDrainFromLocalStorageForTopic:"
+ "_inMemoryKeys"
+ "_initWithDiskLoadBlock:internalCache:allKeysBlock:"
+ "_internalCache"
+ "_isBatchsetComplete:totalBatchCount:forTopic:serverStorageSSM:"
+ "_lastProcessedMessageTimePerTopic"
+ "_peerIDCache"
+ "_persisters"
+ "_preferencesDomain"
+ "_processStoredIncomingRemoteBatchMessages"
+ "_processingStoredIncomingRemoteBatchMessages"
+ "_receivedAt"
+ "_serverStorageFlags"
+ "_serverStorageSSM"
+ "_serverStorageSSMString"
+ "_startClientAckTimeoutTimerForTopic:ssm:"
+ "_storedGUIDs"
+ "_totalBatchCount"
+ "allKeysBlock"
+ "allKeysForService:"
+ "allKeysForService:fromURI:"
+ "broadcastBatchMessage:topic:isFromLocalStorage:"
+ "bypassing cache"
+ "control_category = ? AND "
+ "countLimit"
+ "deleteBatchsetContextsWithServerStorageSSM:service:completion:"
+ "deliveredBatchFromLocalStorageForTopic:ssm:"
+ "didUpdateMaterialsForKeyMaterialController:"
+ "diskLoadBlock"
+ "enumerateAllEndpointsWithBlock:"
+ "enumerateEndpointsForService:withBlock:"
+ "externalDelegate"
+ "fetchAllBatchMessageContexts"
+ "fetchNextBatchsetContexts"
+ "guid IN ("
+ "hasAnyPendingBatchContextsForService:"
+ "identityservicesd.IDSServerBatchMessageContextWrapper"
+ "identityservicesd.WeakDelegate"
+ "identityservicesd6"
+ "inMemoryKeys"
+ "incomingMessagesWithGUIDs:controlCategory:messageTransportType:success:"
+ "initWithBatchIdentifier:batchNumber:totalBatchCount:serverStorageSSM:serverStorageFlags:service:storedGUIDs:receivedAt:"
+ "initWithDeliveryController:userDefaults:idsServerBag:daemon:"
+ "initWithDiskLoadBlock:allKeysBlock:"
+ "initWithIdentifier:persisters:"
+ "initWithIdentifier:preferencesDomain:userDefaults:systemMonitor:"
+ "initWithInternalCache:allKeysBlock:"
+ "initWithPushHandler:queryHandler:restrictedPersistenceManager:keyTransparencyVerifier:userDefaults:peerIDCache:standardIDStatusCache:restrictedIDStatusCache:"
+ "internalCache"
+ "kt-enforcement-repair"
+ "lastProcessedMessageTimeForTopic:"
+ "miss"
+ "objectForKey:ignoreExpiration:"
+ "objectForKey:ignoreExpiration:ignoreCache:wasInMemoryCacheHit:"
+ "objectForKey:ignoreExpiration:wasInMemoryCacheHit:"
+ "peerIDCache"
+ "pendingBatchedGUIDs"
+ "persistedBatchFromServerStorageForTopic:ssm:"
+ "persisters"
+ "processedMessageFromStorageForTopic:"
+ "processingStoredIncomingRemoteBatchMessages"
+ "receiveWithCounter:"
+ "receivedAt"
+ "requiresSentinelAlias"
+ "saveBatchMessageContext:completion:"
+ "secKeyMutex"
+ "sendDesiredMaterialsIfNeeded()"
+ "serverStorageFlags"
+ "serverStorageSSMString"
+ "sessionExists"
+ "setAllKeysBlock:"
+ "setDaemon:"
+ "setDiskLoadBlock:"
+ "setExternalDelegate:"
+ "setInMemoryKeys:"
+ "setInternalCache:"
+ "setPeerIDCache:"
+ "setPersisters:"
+ "setPreferencesDomain:"
+ "setProcessingStoredIncomingRemoteBatchMessages:"
+ "setRequiresSentinelAlias:"
+ "storedGUIDs"
+ "totalCostLimit"
+ "v24@0:8@\"_TtC17identityservicesd39IDSGroupEncryptionKeyMaterialController\"16"
+ "v24@?0@\"IDSEndpoint\"8^B16"
+ "v32@?0@\"IDSDIncomingMessage\"8Q16^B24"
- "%p: Couldn't the public key data for the group %{private}@ (error: %@)"
- "%p: Returned the random publicKeyData %@ for the simulator"
- "%p: This IDSRealTimeEncryptionIdentity is expired. (now: %@, expirationDate: %@)"
- "%s: GUIDs count %lu {repeatedAttempt: %@}"
- "%s: could not get external representation of local identity: %s"
- "%s: could not get external representation of remote identity: %s"
- "%s: failed exporting local public key: %s"
- "%s: failed exporting remote public key: %s"
- "%s: failed importing local private key: %s"
- "%s: failed importing local public key: %s"
- "%s: failed importing remote public key: %s"
- "%s: groupID doesn't match: %s, %s"
- "/Library/Caches/com.apple.xbs/6314950F-86CD-42FA-B5DE-97A35B15E55B/TemporaryDirectory.XfOYTD/Sources/IdentityServices_Swift/IDSAgent/IDSBTDatagramLink.m"
- "/Library/Caches/com.apple.xbs/6314950F-86CD-42FA-B5DE-97A35B15E55B/TemporaryDirectory.XfOYTD/Sources/IdentityServices_Swift/IDSAgent/IDSBTLELink.m"
- "/Library/Caches/com.apple.xbs/6314950F-86CD-42FA-B5DE-97A35B15E55B/TemporaryDirectory.XfOYTD/Sources/IdentityServices_Swift/IDSAgent/IDSBTLink.m"
- "/Library/Caches/com.apple.xbs/6314950F-86CD-42FA-B5DE-97A35B15E55B/TemporaryDirectory.XfOYTD/Sources/IdentityServices_Swift/IDSAgent/IDSClientChannelManager.m"
- "/Library/Caches/com.apple.xbs/6314950F-86CD-42FA-B5DE-97A35B15E55B/TemporaryDirectory.XfOYTD/Sources/IdentityServices_Swift/IDSAgent/IDSLinkManager.m"
- "/Library/Caches/com.apple.xbs/6314950F-86CD-42FA-B5DE-97A35B15E55B/TemporaryDirectory.XfOYTD/Sources/IdentityServices_Swift/IDSAgent/IDSMultiplexer.m"
- "/Library/Caches/com.apple.xbs/6314950F-86CD-42FA-B5DE-97A35B15E55B/TemporaryDirectory.XfOYTD/Sources/IdentityServices_Swift/IDSAgent/IDSMultiplexerUtils.m"
- "/Library/Caches/com.apple.xbs/6314950F-86CD-42FA-B5DE-97A35B15E55B/TemporaryDirectory.XfOYTD/Sources/IdentityServices_Swift/IDSAgent/IDSSessionMultiplexer.m"
- "/Library/Caches/com.apple.xbs/6314950F-86CD-42FA-B5DE-97A35B15E55B/TemporaryDirectory.XfOYTD/Sources/IdentityServices_Swift/IDSAgent/IDSSockAddrPairTable.m"
- "/Library/Caches/com.apple.xbs/6314950F-86CD-42FA-B5DE-97A35B15E55B/TemporaryDirectory.XfOYTD/Sources/IdentityServices_Swift/IDSAgent/IDSUDPGlobalLink.m"
- "/Library/Caches/com.apple.xbs/6314950F-86CD-42FA-B5DE-97A35B15E55B/TemporaryDirectory.XfOYTD/Sources/IdentityServices_Swift/IDSAgent/IDSUTunControlChannel.m"
- "/Library/Caches/com.apple.xbs/6314950F-86CD-42FA-B5DE-97A35B15E55B/TemporaryDirectory.XfOYTD/Sources/IdentityServices_Swift/IDSAgent/IDSUTunControlMessage.m"
- "/Library/Caches/com.apple.xbs/6314950F-86CD-42FA-B5DE-97A35B15E55B/TemporaryDirectory.XfOYTD/Sources/IdentityServices_Swift/IDSAgent/IDSUTunController.m"
- "/Library/Caches/com.apple.xbs/6314950F-86CD-42FA-B5DE-97A35B15E55B/TemporaryDirectory.XfOYTD/Sources/IdentityServices_Swift/IDSAgent/Session/IDSDSession.m"
- "21:43:52"
- "<%@: %p forParticipantID: %llu forPublicIdentity: %@ encryptedData: %@>"
- "<%@: %p forParticipantID:%llu forPublicIdentity:%@ materials:%@ hash:%llu>"
- "<IDSRealTimeEncryptionIdentity\n  publicIdentity=%@\n  fullIdentity=%@\n>"
- "@\"NSSet\"24@0:8@\"NSString\"16"
- "@44@0:8@16i24^{__SecKey=}28Q36"
- "B16@?0@\"IDSPeerIDKey\"8"
- "DB Cache Eviction { peerIDValue: %@ }"
- "DB Cache Miss { service: %@, fromURI: %@, toURI: %@ }"
- "Feb  5 2026"
- "IDSRTEncryptionController"
- "IDSRealTimeEncryptionIdentity"
- "IDSServerDesiredEncryptedDataSet"
- "IDSServerDesiredEncryptedDataSet materialDataByID: encrypted the data for participantID: %llu, remote pub key: %@, data: %@, protectedData: %@"
- "IDSServerDesiredEncryptedDataSet materialDataByID: error: %@"
- "IDSServerDesiredEncryptedDataSet: disableEncryptionForData, use plain data: %@"
- "IDSServerDesiredKeyMaterialSet"
- "IDSServerDesiredKeyMaterialSet materialDataByID: could not encrypt the key material for participantID: %llu, remote pub key: %@, mki: %@"
- "IDSServerDesiredKeyMaterialSet materialDataByID: encrypted the key material for participantID: %llu, remote pub key: %@, mki: %@"
- "IDSServerDesiredKeyMaterialSet wrapMaterialOrError"
- "IDSServerDesiredMaterialSet"
- "Invalid transition: Received %s while in state %s"
- "SecKeyCopyExternalRepresentation"
- "ServerMaterialExchange"
- "T@\"IDSPushToken\",C,N,V_pushToken"
- "T@\"IDSRealTimeEncryptionIdentity\",N,R"
- "T@\"IDSRealTimeEncryptionIdentity\",R,N"
- "T@\"NSArray\",R,C,V_kms"
- "T@\"NSCache\",&,N,V_dbCache"
- "T@\"NSData\",C,N,V_publicIdentityData"
- "T@\"NSData\",R,C,V_encryptedData"
- "T@\"NSDate\",C,N,V_expirationDate"
- "T@\"NSString\",C,N,V_groupID"
- "T@\"NSString\",C,N,V_participantID"
- "T@\"NSString\",C,N,V_sessionID"
- "TB,N,V_isPublicKeyDistributed"
- "TB,R,V_requireSignature"
- "TQ,R,V_forParticipantID"
- "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,R"
- "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,V_fullIdentity"
- "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,V_publicIdentity"
- "T^{__SecKey=},R,V_forPublicIdentity"
- "Ti,R"
- "Ti,R,V_type"
- "Topic %@ has recently received a message from storage.  Starting a new extended timer for retry."
- "Tq,N,V_wrapMode"
- "Will broadcast batchMessage: %@ (topic: %{public}@)"
- "[%@] State: %@ ssm: %@ last msg: %@ last delivered: %@ retry: %@"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24@0:8@16"
- "_dbCache"
- "_forParticipantID"
- "_forPublicIdentity"
- "_fullIdentity"
- "_isPublicKeyDistributed"
- "_kms"
- "_loadCachedPeerIDValueForKey:ignoreExpiration:"
- "_requireSignature"
- "_sendDesiredMaterialsIfNeeded()"
- "_startClientAckTimeoutTimerForTopic:"
- "_type"
- "_wrapData: Couldn't protect the data for _forParticipantID: %llu _forPublicIdentity: %@ (error: %@), data: %@"
- "_wrapData:error:"
- "_wrapMode"
- "broadcastBatchMessage:topic:"
- "dbCache"
- "disableEncryptionForData"
- "forParticipantID"
- "forPublicIdentity"
- "fullIdentityKey"
- "getAllKeyValueDeliveryLocalMaterialSet(forGroupID:)"
- "getAllKeyValueDeliveryLocalMaterialSetForGroupID:"
- "getDesiredMaterialSetForEncryptedData"
- "identityForDevice"
- "idsGlobalLinkP2PKeyNegotiationMakeBlob(logger:counter:localIdentity:remoteIdentity:)"
- "initWithDeliveryController:userDefaults:idsServerBag:"
- "initWithEncryptedData:type:forPublicIdentity:forParticipantID:"
- "initWithKMs:type:forPublicIdentity:forParticipantID:"
- "initWithPushHandler:queryHandler:restrictedPersistenceManager:keyTransparencyVerifier:userDefaults:dbCache:standardIDStatusCache:restrictedIDStatusCache:"
- "isPublicKeyDistributed"
- "kms"
- "localPrivatePreKey"
- "localPublicPreKey"
- "materialDataByID"
- "objcIdentity"
- "objcMaterials"
- "objcPreviousIdentity"
- "objcPreviousPublicIdentity"
- "objcPublicIdentity"
- "objcPublicIdentityForPushToken:"
- "previousFullIdentityKey"
- "previousIdentityForDevice"
- "previousLocalPrivatePreKey"
- "previousLocalPublicPreKey"
- "previousPublicIdentityKey"
- "protectedData is nil, return"
- "publicIdentityKey"
- "publicKeyForPushToken:"
- "realTimeEncryptionPublicKeyForDevice:"
- "receivePublicIdentity:"
- "requireSignature"
- "setDbCache:"
- "setFullIdentity:"
- "setIsPublicKeyDistributed:"
- "setPublicIdentityData:"
- "setWrapMode:"
- "wrapMaterial:error:"

```
