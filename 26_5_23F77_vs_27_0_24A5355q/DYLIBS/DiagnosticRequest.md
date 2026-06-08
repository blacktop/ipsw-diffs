## DiagnosticRequest

> `/System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest`

```diff

-411.120.4.0.0
-  __TEXT.__text: 0x11028
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x470
+460.0.0.0.0
+  __TEXT.__text: 0xfca4
+  __TEXT.__objc_methlist: 0x468
   __TEXT.__const: 0xd8
   __TEXT.__cstring: 0x14c3
-  __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__oslogstring: 0x1ff2
-  __TEXT.__unwind_info: 0x4d0
-  __TEXT.__objc_classname: 0x8c
-  __TEXT.__objc_methname: 0xf31
-  __TEXT.__objc_methtype: 0x1fb
-  __TEXT.__objc_stubs: 0xd80
-  __DATA_CONST.__got: 0xf8
+  __TEXT.__gcc_except_tab: 0x98
+  __TEXT.__oslogstring: 0x1cea
+  __TEXT.__unwind_info: 0x2a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x4b8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3d8
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__got: 0xf8
   __AUTH_CONST.__const: 0x980
   __AUTH_CONST.__cfstring: 0xa80
   __AUTH_CONST.__objc_const: 0x988
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x70
   __DATA.__data: 0xd8
   __DATA.__bss: 0x400

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 975E0396-8210-3BBF-82B3-C5524B3A118D
-  Functions: 392
-  Symbols:   1410
-  CStrings:  735
+  UUID: 34DEEE32-E631-3B04-8955-9C804FFA8C6C
+  Functions: 390
+  Symbols:   1412
+  CStrings:  505
 
Symbols:
+ __handleRequestReply
+ _kDRBaseClientMessageKey_type
+ _kDRBaseRequestReplyKey_failureReason
+ _kDRSRequestReplyMessageKey_didSucceed
+ _kDRSRequestReplyMessageKey_failureReason
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x7
- -[_DRCConnectionState sendMessage:]
- __DPClientXPCSendMessage
- ___35-[_DRCConnectionState sendMessage:]_block_invoke
- _kDRClientMessageKey_type
- _kDRSTaskingServiceKey_ReplyType
- _kDRSubmitLogReplyMessageKey_didSucceed
- _kDRSubmitLogReplyMessageKey_failureReason
- _objc_msgSend$sendMessage:
CStrings:
+ "FailureReason"
+ "RequestFailed"
+ "RequestMessageSendFailure"
+ "ShouldEnableDataGatheringRequestFailed"
+ "Team: %{public}@, Issue Category: %{public}@, Issue Description: %{public}@: %{public}s"
+ "Team: %{public}@, Issue Category: %{public}@: %{public}s"
- ".cxx_destruct"
- "@\"DRConfig\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\""
- "@\"NSUUID\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@28@0:8@16B24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@36@0:8@16B24^@28"
- "@40@0:8@16@24@?32"
- "@88@0:8@16@24@32@40@48@56@64@72B80B84"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16^@24"
- "B36@0:8@16B24^@28"
- "B40@0:8@16^@24^@32"
- "DRClientLog"
- "DRConfig"
- "DRConfigMonitor"
- "DRSubscriptionManager"
- "InvalidBroadcastRequestMessageReply"
- "InvalidClearTaskingStateMessageReply"
- "InvalidConfigCompletionMessageReply"
- "InvalidGetCloudChannelConfigReply"
- "InvalidGetConfigStateReply"
- "InvalidJSONMessageReply"
- "InvalidResetCloudChannelConfigReply"
- "InvalidSetCloudChannelConfigReply"
- "JSONObjectWithData:options:error:"
- "NSCoding"
- "NSSecureCoding"
- "Received an invalid reply a config state request from the tasking service: %{public}s"
- "Received an invalid reply for a JSON message from the tasking service"
- "Received an invalid reply for a broadcast request message from the tasking service"
- "Received an invalid reply for a clear tasking state message from the tasking service"
- "Received an invalid reply for a cloud channel config request message from the tasking service"
- "Received an invalid reply for a set cloud channel config message from the tasking service"
- "Received an invalid reply for marking config %{public}@ %{public}@ message from the tasking service"
- "Request failed due to reason: %{public}s"
- "SubmitLogMessageSendFailure"
- "SubmitLogRequestRejected"
- "T@\"DRConfig\",&,N,V_currentConfig"
- "T@\"NSData\",R,N,V_payload"
- "T@\"NSDate\",R,N,V_endDate"
- "T@\"NSDate\",R,N,V_receivedDate"
- "T@\"NSDate\",R,N,V_startDate"
- "T@\"NSDictionary\",R,N,V_payloadDictionaryRepresentation"
- "T@\"NSMutableDictionary\",R,N,V_perTeamIdConfigState"
- "T@\"NSMutableDictionary\",R,N,V_perTeamIdMonitors"
- "T@\"NSMutableSet\",R,N,V_inFlightSubscriptionRequests"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_accessQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_connectionQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_targetQueue"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_connection"
- "T@\"NSObject<OS_xpc_object>\",R,N,V_connection"
- "T@\"NSString\",&,N,V_build"
- "T@\"NSString\",R,N,V_configDescription"
- "T@\"NSString\",R,N,V_path"
- "T@\"NSString\",R,N,V_sandboxExtension"
- "T@\"NSString\",R,N,V_teamID"
- "T@\"NSUUID\",R,N,V_configUUID"
- "T@?,R,N,V_processingBlock"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_isClosed"
- "TB,R,N,V_payloadIsJSON"
- "TB,R,N,V_skippedHysteresis"
- "TB,R,N,V_transferOwnership"
- "TailspinRequestMessageSendFailure"
- "TaskingServiceReplyType"
- "UTF8String"
- "UUIDString"
- "_DRCConnectionState"
- "_DRCTaskingConnectionState"
- "_accessQueue"
- "_broadcastErrorForTeamID:error:"
- "_build"
- "_checkPath"
- "_completeSubscriptionRequestForTeamID:config:event:"
- "_configDescription"
- "_configFromEvent:teamIdOut:"
- "_configUUID"
- "_connection"
- "_connectionQueue"
- "_currentConfig"
- "_endDate"
- "_handleCurrentConfig:error:forceBroadcast:"
- "_hasInitializedSubscriptionForTeamID:cachedConfigOut:errorOut:"
- "_inFlightSubscriptionRequests"
- "_isClosed"
- "_markConfigUUID:isRejected:errorOut:"
- "_notifyClientOfConfig:error:"
- "_path"
- "_payload"
- "_payloadDictionaryRepresentation"
- "_payloadIsJSON"
- "_perTeamIdConfigState"
- "_perTeamIdMonitors"
- "_processNewEvent:"
- "_processingBlock"
- "_receivedDate"
- "_requestSubscriptionToTeamIDStream:"
- "_sandboxExtension"
- "_skippedHysteresis"
- "_startDate"
- "_targetQueue"
- "_teamID"
- "_transferOwnership"
- "_unsubscribeFromStreamWithTeamID:"
- "accessQueue"
- "addMonitor:"
- "addObject:"
- "allKeys"
- "allObjects"
- "arrayWithObjects:count:"
- "attributesOfItemAtPath:error:"
- "base64EncodedStringWithOptions:"
- "boolValue"
- "bytes"
- "cleanupState"
- "compare:"
- "connection"
- "connectionQueue"
- "containsObject:"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentConfig"
- "currentConfigSnapshotWithErrorOut:"
- "dataWithBytes:length:"
- "dataWithPropertyList:format:options:error:"
- "date"
- "dateWithTimeIntervalSince1970:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeObjectOfClass:forKey:"
- "defaultManager"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "doubleValue"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "fileExistsAtPath:isDirectory:"
- "fileSize"
- "hasConnection"
- "inFlightSubscriptionRequests"
- "init"
- "initFileURLWithPath:"
- "initWithBase64EncodedString:options:"
- "initWithBuild:teamID:configDescription:configUUID:receivedDate:startDate:endDate:payload:payloadIsJSON:skipHysteresis:"
- "initWithCoder:"
- "initWithFormat:"
- "initWithJSONDict:receivedDate:"
- "initWithPath:transferOwnership:errorOut:"
- "initWithTeamID:targetQueue:configProcessingBlock:"
- "initWithUUIDString:"
- "isClosed"
- "isEqual:"
- "isEqualToConfig:"
- "isEqualToString:"
- "jsonDictRepresentation"
- "length"
- "localizedDescription"
- "markCompletedConfigUUID:errorOut:"
- "null"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithUnsignedLongLong:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "path"
- "payloadDictionaryRepresentation"
- "perTeamIdConfigState"
- "perTeamIdMonitors"
- "processingBlock"
- "rejectConfigUUID:errorOut:"
- "removeAllObjects"
- "removeMonitor:"
- "removeObject:"
- "removeObjectForKey:"
- "sandboxExtension"
- "sandboxExtensionForLog:transferOwnership:"
- "sendMessage:"
- "sendMessageWithReplySync:"
- "set"
- "setBuild:"
- "setConnection:"
- "setCurrentConfig:"
- "setObject:forKeyedSubscript:"
- "sharedConnectionState"
- "sharedInstance"
- "skippedHysteresis"
- "startMonitoring"
- "stopMonitoring"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "supportsSecureCoding"
- "targetQueue"
- "timeIntervalSince1970"
- "transferOwnership"
- "unarchivedObjectOfClass:fromData:error:"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v32@0:8@16@24"
- "v36@0:8@16@24B32"
- "v40@0:8@16@24@32"
- "weakObjectsHashTable"

```
