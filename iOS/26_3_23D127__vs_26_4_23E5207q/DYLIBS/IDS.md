## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/IDS`

```diff

-1968.400.21.0.0
-  __TEXT.__text: 0x146ebc
-  __TEXT.__auth_stubs: 0x1d00
-  __TEXT.__objc_methlist: 0xd244
-  __TEXT.__const: 0x422
-  __TEXT.__gcc_except_tab: 0x47dc
-  __TEXT.__oslogstring: 0x1a22c
-  __TEXT.__cstring: 0x107b2
+1969.500.52.2.4
+  __TEXT.__text: 0x1871a0
+  __TEXT.__auth_stubs: 0x3210
+  __TEXT.__objc_methlist: 0xd5ac
+  __TEXT.__const: 0x2ef8
+  __TEXT.__gcc_except_tab: 0x4664
+  __TEXT.__oslogstring: 0x1a684
+  __TEXT.__cstring: 0x11042
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__ustring: 0xac
-  __TEXT.__swift5_typeref: 0x8
-  __TEXT.__unwind_info: 0x4f38
-  __TEXT.__objc_classname: 0x19e4
-  __TEXT.__objc_methname: 0x201bf
-  __TEXT.__objc_methtype: 0x7b39
-  __TEXT.__objc_stubs: 0x14380
-  __DATA_CONST.__got: 0x12c8
-  __DATA_CONST.__const: 0x5328
-  __DATA_CONST.__objc_classlist: 0x590
+  __TEXT.__constg_swiftt: 0xb54
+  __TEXT.__swift5_typeref: 0x110a
+  __TEXT.__swift5_reflstr: 0x75b
+  __TEXT.__swift5_fieldmd: 0xb50
+  __TEXT.__swift5_proto: 0x174
+  __TEXT.__swift5_types: 0x114
+  __TEXT.__swift5_protos: 0x20
+  __TEXT.__swift5_capture: 0x35c
+  __TEXT.__swift_as_entry: 0x8c
+  __TEXT.__swift_as_ret: 0xa8
+  __TEXT.__swift5_builtin: 0xa0
+  __TEXT.__swift5_mpenum: 0x18
+  __TEXT.__unwind_info: 0x63c0
+  __TEXT.__eh_frame: 0x1580
+  __TEXT.__objc_classname: 0x1b52
+  __TEXT.__objc_methname: 0x207a4
+  __TEXT.__objc_methtype: 0x82c7
+  __TEXT.__objc_stubs: 0x145e0
+  __DATA_CONST.__got: 0x1820
+  __DATA_CONST.__const: 0x5358
+  __DATA_CONST.__objc_classlist: 0x5b8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x220
+  __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6900
-  __DATA_CONST.__objc_protorefs: 0x108
+  __DATA_CONST.__objc_selrefs: 0x69f0
+  __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x460
-  __AUTH_CONST.__auth_got: 0xe90
-  __AUTH_CONST.__const: 0x1b20
-  __AUTH_CONST.__cfstring: 0x73e0
-  __AUTH_CONST.__objc_const: 0x3b418
+  __AUTH_CONST.__auth_got: 0x1918
+  __AUTH_CONST.__const: 0x3b00
+  __AUTH_CONST.__cfstring: 0x7420
+  __AUTH_CONST.__objc_const: 0x3c8e0
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x1a90
-  __DATA.__objc_ivar: 0xd74
-  __DATA.__data: 0x19b8
-  __DATA.__bss: 0x1b60
-  __DATA_DIRTY.__objc_data: 0x1d10
+  __AUTH.__objc_data: 0x1c98
+  __AUTH.__data: 0x9e8
+  __DATA.__objc_ivar: 0xd78
+  __DATA.__data: 0x2230
+  __DATA.__bss: 0x4c90
+  __DATA_DIRTY.__objc_data: 0x1d60
   __DATA_DIRTY.__bss: 0x388
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AsyncAlgorithmsInternal.framework/AsyncAlgorithmsInternal
   - /System/Library/PrivateFrameworks/CommonUtilities.framework/CommonUtilities
   - /System/Library/PrivateFrameworks/Engram.framework/Engram
   - /System/Library/PrivateFrameworks/FTServices.framework/FTServices
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
+  - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B627B291-4891-37E6-9214-B5A0912DA2C3
-  Functions: 6572
-  Symbols:   1584
-  CStrings:  10144
+  UUID: 126125F5-A5A6-3285-BFF7-04D3E552F229
+  Functions: 8038
+  Symbols:   1779
+  CStrings:  10304
 
Symbols:
+ OBJC_IVAR_$_IDSDaemonRequestTimer._requestContextMap
+ OBJC_IVAR_$_IDSDaemonRequestTimer._requestContextMapLock
+ OBJC_IVAR_$_IDSDaemonResponseHandler._block
+ OBJC_IVAR_$_IDSDaemonResponseHandler._isSync
+ OBJC_IVAR_$_IDSDaemonResponseHandler._queue
+ OBJC_IVAR_$_IDSQuickSwitchAcknowledgementTracker._delegateIdentifiers
+ OBJC_IVAR_$_IDSQuickSwitchAcknowledgementTracker._delegateIdentifiersMutex
+ OBJC_IVAR_$_IDSTransactionLogBaseTaskHandler._queue
+ OBJC_IVAR_$_IDSTransactionLogBaseTaskHandler._task
+ OBJC_IVAR_$_IDSTransactionLogSyncTaskHandler._delegate
+ OBJC_IVAR_$_IDSTransactionLogSyncTaskHandler._queue
+ OBJC_IVAR_$_IDSTransactionLogSyncTaskHandler._syncTask
+ OBJC_IVAR_$_IDSTransactionLogTaskHandlerAccountInfo._accountIdentity
+ OBJC_IVAR_$_IDSTransactionLogTaskHandlerAccountInfo._aliasToAccountsMap
+ OBJC_IVAR_$_IDSTransactionLogTaskHandlerAccountInfo._serviceName
+ OBJC_IVAR_$__IDSDeviceConnection._awdMetrics
+ OBJC_IVAR_$__IDSDeviceConnection._clientName
+ OBJC_IVAR_$__IDSDeviceConnection._clientTimeout
+ OBJC_IVAR_$__IDSDeviceConnection._connectionUUID
+ OBJC_IVAR_$__IDSDeviceConnection._hasTimedOut
+ OBJC_IVAR_$__IDSDeviceConnection._inputStreamForSocket
+ OBJC_IVAR_$__IDSDeviceConnection._isDefaultPairedDevice
+ OBJC_IVAR_$__IDSDeviceConnection._mtu
+ OBJC_IVAR_$__IDSDeviceConnection._nsuuid
+ OBJC_IVAR_$__IDSDeviceConnection._openSocketCompletionHandler
+ OBJC_IVAR_$__IDSDeviceConnection._openSocketCompletionHandlerID
+ OBJC_IVAR_$__IDSDeviceConnection._openSocketCompletionHandlerQueue
+ OBJC_IVAR_$__IDSDeviceConnection._outputStreamForSocket
+ OBJC_IVAR_$__IDSDeviceConnection._service
+ OBJC_IVAR_$__IDSDeviceConnection._serviceToken
+ OBJC_IVAR_$__IDSDeviceConnection._socket
+ OBJC_IVAR_$__IDSDeviceConnection._streamName
+ _CopyTLVDefinition
+ _IDSDataChannelAllParticipantsKey
+ _IDSDataChannelAllStreamsKey
+ _IDSDataChannelNoStreamsKey
+ _IDSDataChannelsQueue
+ _IDSDirectMessageACKForSeqNumNBO
+ _IDSDirectMessageClientData
+ _IDSDirectMessageClientMessage
+ _IDSDirectMessageClientProtobuf
+ _IDSDirectMessageIncomingResponseIdentifier
+ _IDSDirectMessageNSSequenceNumber
+ _IDSDirectMessageOutgoingResponseIdentifier
+ _IDSDirectMessageSockPairMessageFlags
+ _IDSDirectMessageTrafficClass
+ _IDSGroupSessionAllParticipantsKey
+ _IDSGroupSessionAllStreamsKey
+ _IDSGroupSessionAllocateParticipantsKey
+ _IDSGroupSessionClientContextDataKey
+ _IDSGroupSessionCommandContextKey
+ _IDSGroupSessionDoNotAutomaticallyAllocateParticipantsKey
+ _IDSGroupSessionIsSignallingProxyKey
+ _IDSGroupSessionJoinTypeKey
+ _IDSGroupSessionMaxConcurrentStreamsKey
+ _IDSGroupSessionMirageProtocolHandshakeBlobKey
+ _IDSGroupSessionNewServerAllocationKey
+ _IDSGroupSessionNoStreamsKey
+ _IDSGroupSessionNotifyJoinKey
+ _IDSGroupSessionNotifyMembershipChangesKey
+ _IDSGroupSessionParticipantAVCPlainBlobKey
+ _IDSGroupSessionShortMKIEnabledKey
+ _IDSGroupSessionSubscribedStreamsKey
+ _IDSSendMessageOptionPolicyKey
+ _OBJC_CLASS_$_IDSDaemonProtocolController
+ _OBJC_CLASS_$_IDSDaemonRequestTimer
+ _OBJC_CLASS_$_IDSDaemonResponseHandler
+ _OBJC_CLASS_$_IDSDeviceStateMonitoring
+ _OBJC_CLASS_$_IDSDirectMessageConnection
+ _OBJC_CLASS_$_IDSGroupContextController
+ _OBJC_CLASS_$_IDSGroupContextDataSource
+ _OBJC_CLASS_$_IDSGroupContextNotifyingObserver
+ _OBJC_CLASS_$_IDSGroupEncryptionKeyMaterialCache
+ _OBJC_CLASS_$_IDSIDQueryMessagePolicyEngine
+ _OBJC_CLASS_$_IDSInternalQueueController
+ _OBJC_CLASS_$_IDSQuickSwitchAcknowledgementTracker
+ _OBJC_CLASS_$_IDSSendMessagePolicy
+ _OBJC_CLASS_$_IDSTransactionLogBaseTaskHandler
+ _OBJC_CLASS_$_IDSTransactionLogSyncTaskHandler
+ _OBJC_CLASS_$_IDSTransactionLogTaskHandler
+ _OBJC_CLASS_$_IDSTransactionLogTaskHandlerAccountInfo
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$__IDSAccount
+ _OBJC_CLASS_$__IDSConnection
+ _OBJC_CLASS_$__IDSDataChannelLinkContext
+ _OBJC_CLASS_$__IDSDatagramChannel
+ _OBJC_CLASS_$__IDSDevice
+ _OBJC_CLASS_$__IDSDeviceConnection
+ _OBJC_CLASS_$__IDSGroupSession
+ _OBJC_CLASS_$__IDSService
+ _OBJC_CLASS_$__IDSSession
+ _OBJC_CLASS_$__TtC3IDS28IDSGroupSessionDelegateProxy
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$_IDSDaemonProtocolController
+ _OBJC_METACLASS_$_IDSDaemonRequestTimer
+ _OBJC_METACLASS_$_IDSDaemonResponseHandler
+ _OBJC_METACLASS_$_IDSDeviceStateMonitoring
+ _OBJC_METACLASS_$_IDSDirectMessageConnection
+ _OBJC_METACLASS_$_IDSGroupContextController
+ _OBJC_METACLASS_$_IDSGroupContextDataSource
+ _OBJC_METACLASS_$_IDSGroupContextNotifyingObserver
+ _OBJC_METACLASS_$_IDSGroupEncryptionKeyMaterialCache
+ _OBJC_METACLASS_$_IDSIDQueryMessagePolicyEngine
+ _OBJC_METACLASS_$_IDSInternalQueueController
+ _OBJC_METACLASS_$_IDSQuickSwitchAcknowledgementTracker
+ _OBJC_METACLASS_$_IDSTransactionLogBaseTaskHandler
+ _OBJC_METACLASS_$_IDSTransactionLogSyncTaskHandler
+ _OBJC_METACLASS_$_IDSTransactionLogTaskHandler
+ _OBJC_METACLASS_$_IDSTransactionLogTaskHandlerAccountInfo
+ _OBJC_METACLASS_$__IDSAccount
+ _OBJC_METACLASS_$__IDSConnection
+ _OBJC_METACLASS_$__IDSDataChannelLinkContext
+ _OBJC_METACLASS_$__IDSDatagramChannel
+ _OBJC_METACLASS_$__IDSDevice
+ _OBJC_METACLASS_$__IDSDeviceConnection
+ _OBJC_METACLASS_$__IDSGroupSession
+ _OBJC_METACLASS_$__IDSService
+ _OBJC_METACLASS_$__IDSSession
+ _OBJC_METACLASS_$__TtC3IDS28IDSGroupSessionDelegateProxy
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __Block_copy
+ __Block_release
+ __IDSServiceCalculatedPseudonymChanges
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftEmptySetSingleton
+ __swiftImmortalRefCount
+ __swift_stdlib_reportUnimplementedInitializer
+ _malloc_size
+ _memcmp
+ _memmove
+ _objc_allocWithZone
+ _parseTLVDictFromNSData
+ _swift_allocBox
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_checkMetadataState
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deallocPartialClassInstance
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getEnumCaseMultiPayload
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getErrorValue
+ _swift_getExistentialTypeMetadata
+ _swift_getForeignTypeMetadata
+ _swift_getGenericMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTupleTypeMetadata2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_runtimeSupportsNoncopyableTypes
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagMultiPayload
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_updateClassMetadata2
+ _swift_willThrow
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ "%s: No body in response"
+ "%s: Received /QR/DelegatedMessage response with status %ld..."
+ "%s: Sending /QR/DelegatedMessage with SDP..."
+ "%s: Unexpected innerMessage in delegatedMessageResponse"
+ "%s: Unexpected innerMessage in response: %s"
+ "%s: Unexpected innerMessage in webMessageResponse"
+ "%s: could not parse delegated message: %s"
+ "%s: error: %u, %s"
+ "%s: materialID=%s, kind=%s, policies=%ld, onBehalfOf=%s"
+ "%s: no SDP and no error in response"
+ "%s: no innerMessage in delegatedMessageResponse"
+ "%s: received SDP Request"
+ "%s: received SDP Update (txnID=%llu"
+ "%s: received event: %s"
+ "%s: received other indication; ignoring: %s"
+ "%s: received putmaterial indication; ignoring (should be handled by daemon)"
+ "%s: received test message: %s"
+ "%s: resuming updateMembers continuation..."
+ "%s: sessionDidReceiveBlob: %s, type: %s, from: %@"
+ "%s: unexpectedly found nil signallessID in a signalless IDSGroupSessionActiveParticipant."
+ "-[_IDSGroupSession session:didReceiveBlobWithType:data:participant:]"
+ "-[_IDSGroupSession updateMembers:withContext:messagingCapabilities:triggeredLocally:requestUUID:]"
+ ".allocateParticipants("
+ ".automaticallyAllocateParticipants("
+ ".conversationID("
+ ".forceNewAllocation("
+ ".maxConcurrentStreams("
+ ".mirageHandshake"
+ ".notifyJoinLeave(to: "
+ ".notifyMembershipChanges(to: "
+ ".participantData"
+ ".participantInfo"
+ ".signallingProxy"
+ ".signallingProxy("
+ ".startedAsUPlusOne("
+ ".subscribeToStreams("
+ ".triggeredLocally("
+ "/Library/Caches/com.apple.xbs/81F30F82-0129-47CF-B19D-BE1609C36C18/TemporaryDirectory.cWLs4t/Sources/IdentityServices/IDS/Client/IDSDataChannels.m"
+ "/Library/Caches/com.apple.xbs/81F30F82-0129-47CF-B19D-BE1609C36C18/TemporaryDirectory.cWLs4t/Sources/IdentityServices/IDS/IDSDataChannelsUtils.m"
+ "/Library/Caches/com.apple.xbs/81F30F82-0129-47CF-B19D-BE1609C36C18/TemporaryDirectory.cWLs4t/Sources/IdentityServices/IDS/IDSDataChannels_Direct.m"
+ "/QR/DelegatedMessage"
+ "@\"IDSIDQueryController\""
+ "@24@0:8^{?=*QqqICBBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@@@@iISQBBBS[0C]}16"
+ "Delegated Message: "
+ "Delegated Message[participantID="
+ "GroupSessionQueue"
+ "IDS.IDSGroupSessionDelegateProxy"
+ "IDS.IDSGroupSessionInternalDelegateWrapper"
+ "IDSGroupSessionDelegate"
+ "IDSIDQueryMessagePolicyEngine"
+ "IDSPhoneNumberCredentialVendor requestPhoneNumberCredentialForService {service: %@, simLabelID: %@, requestOption: %@}"
+ "IDSSendMessageOptionPolicyKey"
+ "IDSXPCInternalTestingXPCInterceptor"
+ "Ignoring group session didReceiveBlobWithType, session doesn't match %@ vs. %@"
+ "Invalid number of keys found, expected one."
+ "Mirage Handshake"
+ "Participant Data"
+ "Participant Info"
+ "Participant Update: "
+ "ParticipantBlob(blob: "
+ "ParticipantBlob(kind: "
+ "RealTimeGroupSession"
+ "StreamSubscription("
+ "T@\"IDSIDQueryController\",N,R,VqueryController"
+ "TC,R,V_localLinkTechnology"
+ "Unexpected nil update"
+ "^{?=*QqqICBBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@@@@iISQBBBS[0C]}20@0:8B16"
+ "^{?=*QqqICBBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@@@@iISQBBBS[0C]}54@0:8r^v16I24C28C32{?=cSCSC}36^{?=IQSCc[12S]CS{?=SSSSS}dQBQ[16C]BB}46"
+ "^{?=*QqqICBBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@@@@iISQBBBS[0C]}62@0:8r^v16I24C28C32{?=cSCSC}36^{?=IQSCc[12S]CS{?=SSSSS}dQBQ[16C]BB}46@54"
+ "^{?=*QqqICBBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@@@@iISQBBBS[0C]}66@0:8r^v16I24C28C32{?=cSCSC}36^{?=IQSCc[12S]CS{?=SSSSS}dQBQ[16C]BB}46@54B62"
+ "_TtC3IDS20RealTimeGroupSession"
+ "_TtC3IDS28IDSGroupSessionDelegateProxy"
+ "_TtC3IDSP33_887F5B905F406C1969C5786FD07F2C6E38IDSGroupSessionInternalDelegateWrapper"
+ "_TtCC3IDSP33_887F5B905F406C1969C5786FD07F2C6E38IDSGroupSessionInternalDelegateWrapper8Listener"
+ "_localLinkTechnology"
+ "actorProvider"
+ "addConferenceAccountWithType:username:uniqueID:dsid:completion:"
+ "allocationData"
+ "apply(_:to:forService:)"
+ "applyPolicy:toURIs:forService:completion:"
+ "clientContextData"
+ "configureXPCInterception:"
+ "continuation"
+ "destinationWithStringURI:isLightWeight:"
+ "disableXPCInterception"
+ "events(forDelegatedMessageData:)"
+ "fromServer"
+ "groupSessionDidConnectUnderlyingLinks"
+ "groupSessionDidDisconnectUnderlyingLinks"
+ "groupSessionDidInitialize("
+ "groupSessionDidTerminate"
+ "groupSessionEnded("
+ "groupUUID"
+ "idsGroupSession"
+ "init()"
+ "init:"
+ "initWithEnableQualityMetrics:"
+ "initWithQueryController:"
+ "internalDelegateWrapper"
+ "isInitiator"
+ "isSignalless"
+ "joinContinuations"
+ "leaveContinuations"
+ "listenToInternalDelegate(_:)"
+ "listenUsingActor(_:)"
+ "localLinkTechnology"
+ "members"
+ "participant(forActiveParticipant:)"
+ "participantDestinationURI"
+ "participantIDs"
+ "participantPushTokenObject"
+ "participantURI"
+ "participantUpdateType"
+ "phoneNumberCredentialVendorTimeout"
+ "pnr-credential-vendor-xpc-timeout"
+ "processInterceptedMessage:type:protocolName:involvedProcesses:completion:"
+ "queryController"
+ "removeConferenceAccountWithType:completion:"
+ "replaceConferenceAccountWithType:newUniqueID:completion:"
+ "serverDate"
+ "serviceParticipantUpdate("
+ "session"
+ "session %@ participant: %@, didReceiveBlobWithType: %d, data: %@"
+ "session:didReceiveBlobWithType:data:participant:"
+ "session:didReceivePluginAllocationInfo:"
+ "sessionDidJoinGroup("
+ "sessionDidLeaveGroup("
+ "sessionDidReceiveBlob("
+ "sessionDidReceiveData("
+ "sessionDidReceiveDataBlob("
+ "sessionDidReceiveParticipantUpdate("
+ "sessionDidReceiveParticipants("
+ "sessionDidReceiveRemoteParticipantUpgrade:remoteParticipantID:participantType:error:"
+ "setSendMessagePolicy:"
+ "setXPCType:forSelector:argumentIndex:ofReply:"
+ "signallessID"
+ "strongReferences"
+ "updateMembers (messagingCapabilities): lightweightStatusDict: %@, _destinationLightweightStatus: %@, requestUUID: %@"
+ "updateMembers(_:options:)"
+ "updateMembers:forGroup:sessionID:withContext:messagingCapabilities:triggeredLocally:lightweightStatusDict:requestUUID:"
+ "updateMembers:withContext:messagingCapabilities:triggeredLocally:requestUUID:"
+ "v24@0:8@\"<IDSXPCInternalTestingXPCInterceptor>\"16"
+ "v24@0:8@\"IDSGroupSession\"16"
+ "v24@0:8^{?=*QqqICBBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@@@@iISQBBBS[0C]}16"
+ "v28@0:8@\"IDSGroupSession\"16I24"
+ "v32@0:8@\"IDSGroupSession\"16@\"NSArray\"24"
+ "v32@0:8@\"IDSGroupSession\"16@\"NSDictionary\"24"
+ "v32@0:8@\"IDSGroupSession\"16@\"NSError\"24"
+ "v32@0:8q16@?<v@?B@\"NSError\">24"
+ "v36@0:8@\"IDSGroupSession\"16@\"IDSURI\"24I32"
+ "v36@0:8@\"IDSGroupSession\"16@\"NSArray\"24B32"
+ "v36@0:8@\"IDSGroupSession\"16I24@\"NSError\"28"
+ "v36@0:8@\"IDSGroupSession\"16S24@\"NSError\"28"
+ "v40@0:8@\"IDSGroupSession\"16@\"IDSGroupSessionParticipantUpdate\"24@\"NSError\"32"
+ "v40@0:8@\"IDSGroupSession\"16@\"NSArray\"24@\"NSError\"32"
+ "v40@0:8@\"IDSGroupSession\"16@\"NSArray\"24I32B36"
+ "v40@0:8@\"IDSGroupSession\"16@\"NSArray\"24I32S36"
+ "v40@0:8@\"IDSGroupSession\"16@\"NSData\"24@\"IDSGroupSessionActiveParticipant\"32"
+ "v40@0:8@\"IDSGroupSession\"16@\"NSDictionary\"24@\"NSError\"32"
+ "v40@0:8@\"IDSGroupSession\"16Q24@\"NSData\"32"
+ "v40@0:8q16@\"NSString\"24@?<v@?B@\"NSString\"@\"NSString\"@\"NSError\">32"
+ "v44@0:8@\"IDSGroupSession\"16@\"NSArray\"24I32S36B40"
+ "v44@0:8@\"IDSGroupSession\"16@\"NSData\"24S32@\"IDSGroupSessionActiveParticipant\"36"
+ "v44@0:8@\"IDSGroupSession\"16@\"NSNumber\"24S32@\"NSError\"36"
+ "v44@0:8@\"IDSGroupSession\"16I24@\"NSData\"28@\"IDSGroupSessionActiveParticipant\"36"
+ "v44@0:8@\"IDSGroupSession\"16S24Q28@\"NSError\"36"
+ "v44@0:8@\"NSString\"16I24@\"NSData\"28@\"NSDictionary\"36"
+ "v44@0:8@16I24@28@36"
+ "v48@0:8@\"IDSSendMessagePolicy\"16@\"NSArray\"24@\"NSString\"32@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"IDSSendMessagePolicyResult\">40"
+ "v56@0:8@\"NSObject<OS_xpc_object>\"16Q24@\"NSString\"32@\"NSArray\"40@?<v@?@\"NSObject<OS_xpc_object>\">48"
+ "v56@0:8@16Q24@32@40@?48"
+ "v56@0:8q16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?B@\"NSError\">48"
+ "v56@0:8q16@24@32@40@?48"
+ "v76@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@\"IDSMessagingCapabilities\"48B56@\"NSDictionary\"60@\"NSUUID\"68"
+ "v76@0:8@16@24@32@40@48B56@60@68"
- "/Library/Caches/com.apple.xbs/Sources/IdentityServices/IDS/Client/IDSDataChannels.m"
- "/Library/Caches/com.apple.xbs/Sources/IdentityServices/IDS/IDSDataChannelsUtils.m"
- "/Library/Caches/com.apple.xbs/Sources/IdentityServices/IDS/IDSDataChannels_Direct.m"
- "5 {curProtocol: %hhu, prevProtocol: %hhu, prevBundleID: %@, curUUID: %{public,uuid_t}.16P, curPktLen: %u, logSeqn: %hhu}"
- "9 {curProtocol: %hhu, nextProtocol: %hhu, curUUID: %{public,uuid_t}.16P, curPktLen: %u, logSeqn: %hhu}"
- "@24@0:8^{?=*QqqICBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@@iISQBBBS[0C]}16"
- "CrossLayerLogging"
- "Warning! Message with guid %@ exceeds size limitations of MPKL_UUID_NEXT macro."
- "^{?=*QqqICBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@@iISQBBBS[0C]}20@0:8B16"
- "^{?=*QqqICBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@@iISQBBBS[0C]}54@0:8r^v16I24C28C32{?=cSCSC}36^{?=IQSCc[12S]CS{?=SSSSS}dQBQ[16C]BB}46"
- "^{?=*QqqICBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@@iISQBBBS[0C]}62@0:8r^v16I24C28C32{?=cSCSC}36^{?=IQSCc[12S]CS{?=SSSSS}dQBQ[16C]BB}46@54"
- "^{?=*QqqICBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@@iISQBBBS[0C]}66@0:8r^v16I24C28C32{?=cSCSC}36^{?=IQSCc[12S]CS{?=SSSSS}dQBQ[16C]BB}46@54B62"
- "d8@?0"
- "initWithTimeFn:"
- "initWithTimeFn:enableQualityMetrics:"
- "longValue"
- "updateMembers:forGroup:sessionID:withContext:messagingCapabilities:triggeredLocally:lightweightStatusDict:"
- "v24@0:8^{?=*QqqICBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@@iISQBBBS[0C]}16"
- "v68@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@\"IDSMessagingCapabilities\"48B56@\"NSDictionary\"60"
- "v68@0:8@16@24@32@40@48B56@60"

```
