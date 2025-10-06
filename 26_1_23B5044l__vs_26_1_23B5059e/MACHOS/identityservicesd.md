## identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

-1968.200.31.2.1
-  __TEXT.__text: 0x927f38
-  __TEXT.__auth_stubs: 0x5a70
-  __TEXT.__objc_stubs: 0x46220
-  __TEXT.__objc_methlist: 0x2936c
+1968.200.61.2.1
+  __TEXT.__text: 0x92a0d0
+  __TEXT.__auth_stubs: 0x5a80
+  __TEXT.__objc_stubs: 0x46620
+  __TEXT.__objc_methlist: 0x29514
   __TEXT.__const: 0x63910
-  __TEXT.__gcc_except_tab: 0x29c80
-  __TEXT.__objc_methname: 0x72985
-  __TEXT.__cstring: 0x593a7
-  __TEXT.__oslogstring: 0x7a82b
-  __TEXT.__objc_classname: 0x43a8
-  __TEXT.__objc_methtype: 0x1232c
+  __TEXT.__gcc_except_tab: 0x29d1c
+  __TEXT.__objc_methname: 0x72fae
+  __TEXT.__cstring: 0x594f7
+  __TEXT.__oslogstring: 0x7aa1b
+  __TEXT.__objc_classname: 0x43ad
+  __TEXT.__objc_methtype: 0x1232d
   __TEXT.__ustring: 0x4ca
   __TEXT.__dlopen_cstrs: 0xea
   __TEXT.__swift5_typeref: 0x5db8
   __TEXT.__swift5_capture: 0x12f8
-  __TEXT.__constg_swiftt: 0x50a0
+  __TEXT.__constg_swiftt: 0x50b8
   __TEXT.__swift5_reflstr: 0x4ef4
   __TEXT.__swift5_fieldmd: 0x5208
   __TEXT.__swift5_builtin: 0xa0

   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift5_assocty: 0xfa8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x12210
-  __TEXT.__eh_frame: 0x99d4
-  __DATA_CONST.__auth_got: 0x2d48
-  __DATA_CONST.__got: 0x3860
+  __TEXT.__unwind_info: 0x12270
+  __TEXT.__eh_frame: 0x9a2c
+  __DATA_CONST.__auth_got: 0x2d50
+  __DATA_CONST.__got: 0x3870
   __DATA_CONST.__auth_ptr: 0x780
-  __DATA_CONST.__const: 0x2dca8
-  __DATA_CONST.__cfstring: 0x34760
+  __DATA_CONST.__const: 0x2dcb8
+  __DATA_CONST.__cfstring: 0x348a0
   __DATA_CONST.__objc_classlist: 0x1110
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x750
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0xb90
-  __DATA_CONST.__objc_intobj: 0x1b18
+  __DATA_CONST.__objc_intobj: 0x1b30
   __DATA_CONST.__objc_arraydata: 0x5b0
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x47b08
-  __DATA.__objc_selrefs: 0x15c10
-  __DATA.__objc_ivar: 0x3294
-  __DATA.__objc_data: 0xd260
+  __DATA.__objc_const: 0x47c90
+  __DATA.__objc_selrefs: 0x15d40
+  __DATA.__objc_ivar: 0x32b4
+  __DATA.__objc_data: 0xd278
   __DATA.__data: 0xead0
   __DATA.__bss: 0x16de8
   __DATA.__common: 0xf18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 65D2060E-5CF4-39DE-B33B-71C719C30272
-  Functions: 25165
-  Symbols:   2739
-  CStrings:  41367
+  UUID: CBA8D47C-F060-38EC-9A31-1E274D43F2D9
+  Functions: 25206
+  Symbols:   2742
+  CStrings:  41447
 
Symbols:
+ _IDSRegistrationPropertySupportsQueueOneReadReceiptsV2
+ _OBJC_CLASS_$_IDSMessageSendResponseMetric
+ __IDSStorageCheckVersionNumber
CStrings:
+ "%@-%@-%d"
+ "%@-client-ack-timeout"
+ "%@-extend-client-ack-timeout"
+ "1a"
+ "21:28:16"
+ "Caching decrypted read receipt data { key: %@, dataLength: %ld }"
+ "Could not find publicDeviceIdentity for {deviceID: %@}, {pushToken: %@}"
+ "Found cached decrypted read receipt data { key: %@, dataLength: %ld }"
+ "Given message list {guid: %@, ssm: %@, label: %@/%@, LFS: %@} from server. Dissecting into %ld individual messages"
+ "Given single message with ssm {guid: %@, ssm: %@, label: %@/%@, LFS: %@} from server. Handling as message list with single item"
+ "Logged message send response metric: responseCode=%ld service=%@ messageGUID=%@"
+ "Logged server message send response metric: responseCode=%ld service=%@"
+ "Nil parameter given to holdDecryptedReadReceiptData. Key: %@, Data: %@"
+ "No cached decrypted read receipt data found { key: %@ }"
+ "Not all connections are idle."
+ "Oct  1 2025"
+ "Starting client ack timeout timer for topic %@, timeout in %ld seconds"
+ "Starting extended client ack timeout timer for topic %@, timeout in %ld seconds"
+ "T@\"NSMutableDictionary\",&,N,V_clientAckTimerToTopicMap"
+ "T@\"NSMutableDictionary\",&,N,V_readReceiptCache"
+ "T@\"NSNumber\",&,N,V_storageCheckVersion"
+ "Topic %@, has timed out waiting for client ack"
+ "Tq,N,V_clientTimeoutCount"
+ "Tq,N,V_roundCount"
+ "Tq,N,V_serverTimeoutCount"
+ "Tq,N,V_terminationReason"
+ "Triggered Auto Bug Capture for client time out {session : %@, error: %@}"
+ "We are told to send batch processed however storageFetchContext is missing, ignoring..."
+ "We received LFS but still have ssm in progress: {%@} - letting that finish"
+ "_clientAckTimeoutIntervalForTopic:"
+ "_clientAckTimerToTopicMap"
+ "_clientTimeoutCount"
+ "_extendedClientAckTimeoutIntervalForTopic:"
+ "_extendedServerResponseTimeoutIntervalForTopic:"
+ "_hasExceededMaxRequestsWithSSMForTopic:retryCount:ssm:"
+ "_incrementClientTimeoutCountForTopic:"
+ "_incrementRoundCountForTopic:"
+ "_incrementServerTimeoutCountForTopic:"
+ "_invalidateClientAckTimerForTopic:"
+ "_invalidateServerResponseTimerForTopic:"
+ "_invalidateTimeoutTimersForTopic:"
+ "_readReceiptCache"
+ "_roundCount"
+ "_serverDisabledDupeReadReceipts"
+ "_serverResponseTimeoutIntervalForTopic:"
+ "_serverTimeoutCount"
+ "_setStorageCheckVersion:forTopic:"
+ "_setTerminationReasonForTopic:reason:"
+ "_shouldExtendServerResponseTimeoutForTopic:"
+ "_startClientAckTimeoutTimerForTopic:"
+ "_startExtendedServerResponseTimeoutTimerForTopic:ssm:"
+ "_startServerResponseTimeoutTimerForTopic:ssm:"
+ "_stateMachineTimedOutWaitingForClientAck:"
+ "_stateMachineTimedOutWaitingForServerResponse:"
+ "_storageCheckVersion"
+ "_terminationReason"
+ "clientAckTimerToTopicMap"
+ "clientTimeoutCount"
+ "could not find the push token for {deviceID: %@}"
+ "decryptMessageData:guid:localURI:remoteURI:pushToken:groupID:command:encryptionType:isLiveRetry:replayKey:incomingMetric:completionBlock:"
+ "decryptedReadReceiptDataForKey:"
+ "didLeave"
+ "disable-dupe-read-receipts"
+ "endWithReason:"
+ "extendClientAckTimeoutTimerForTopic:"
+ "holdDecryptedReadReceiptData:forKey:"
+ "incomingStorageRequestForTopic:primary:messageContext:sendReasonPathID:"
+ "incrementClientTimeoutCount"
+ "incrementRoundCount"
+ "incrementServerTimeoutCount"
+ "initWithResponseCode:service:messageType:"
+ "initWithService:linkType:wasPrimary:timeTaken:messagesProcessed:roundsProcessed:serverTimeoutCount:clientTimeoutCount:terminationReason:storageCheckVersion:"
+ "leave"
+ "linkedURIs"
+ "messagesProcessed"
+ "readReceiptCache"
+ "registeredDevicesOnService:withLinkedURI:"
+ "reinitFinish"
+ "reinitStart"
+ "requestAllocation"
+ "roundCount"
+ "roundsProcessed"
+ "sendServerStorageProcessedForService:withCompletion:"
+ "serverTimeoutCount"
+ "setClientAckTimerToTopicMap:"
+ "setClientTimeoutCount:"
+ "setReadReceiptCache:"
+ "setRoundCount:"
+ "setServerTimeoutCount:"
+ "setStorageCheckVersion:"
+ "setTerminationReason:"
+ "storageCheckVersion"
+ "terminateStateMachineForTopic:withReason:"
+ "terminationReason"
+ "v108@0:8@16@24@32@40@48@56@64q72B80@84@92@?100"
+ "v44@0:8@16B24@28q36"
- "       found push token in: %@"
- "23:17:22"
- "AWDIDSServerStorageStateMachineCompleted"
- "Given message list {guid: %@, ssm: %@} from server. Dissecting into %ld individual messages"
- "Given single message with ssm {guid: %@, ssm: %@} from server. Handling as message list with single item"
- "NotedReceivedSSM"
- "Noting batch received with ssm: %@ from server storage for topic: %@"
- "Processed 0 messages in message list {identifier: %@} for topic: %@ - not broadcasting batch message"
- "Received batch with invalid ssm: %@ from server storage for topic: %@ - aborting"
- "Sep 16 2025"
- "Told to terminate state machine but we have an ssm in progress for topic: %@, sending"
- "Unable to find a topic timeout timer, This will likely cause a bug"
- "We are still delivering messages on topic %@. Extending timeout."
- "We haven't delivered messages on topic %@. Extending timeout."
- "_extendedTimeoutIntervalForTopic:"
- "_hasExceededMaxRequestsForTopic:retryCount:ssm:"
- "_invalidateTimerForTopic:"
- "_shouldExtendTimeoutForTopic:"
- "_startExtendedTimeoutTimerForTopic:ssm:"
- "_startTimeoutTimerForTopic:ssm:"
- "_stateMachineTimedOut:"
- "_timeoutIntervalForTopic:"
- "decryptMessageData:guid:localURI:remoteURI:pushToken:groupID:encryptionType:isLiveRetry:replayKey:incomingMetric:completionBlock:"
- "incomingStorageRequestForTopic:primary:messageContext:"
- "initWithService:linkType:wasPrimary:timeTaken:numberProcessed:"
- "noteBatchReceivedFromServerStorageForTopic:ssm:"
- "noteServerStorageStateMachineEndedFor:linkType:wasPrimary:timeTaken:numberProcessed:"
- "setTimeTaken:"
- "setTotalMessages:"
- "terminateStateMachineForTopic:"
- "totalProcessed"
- "v100@0:8@16@24@32@40@48@56q64B72@76@84@?92"
- "v52@0:8@16q24B32d36q44"

```
