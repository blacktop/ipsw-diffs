## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/Contents/MacOS/iMessage`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-1487.100.6.1.2
-  __TEXT.__text: 0x119208
+1491.100.1.1.9
+  __TEXT.__text: 0x11a49c
   __TEXT.__auth_stubs: 0x2170
-  __TEXT.__objc_stubs: 0xe760
-  __TEXT.__objc_methlist: 0x304c
+  __TEXT.__objc_stubs: 0xea40
+  __TEXT.__objc_methlist: 0x327c
   __TEXT.__const: 0x1588
-  __TEXT.__gcc_except_tab: 0x98d8
-  __TEXT.__cstring: 0x3d9d
-  __TEXT.__oslogstring: 0x1bd5b
-  __TEXT.__objc_classname: 0x72f
-  __TEXT.__objc_methname: 0x14b0a
-  __TEXT.__objc_methtype: 0x32a9
+  __TEXT.__gcc_except_tab: 0x9778
+  __TEXT.__cstring: 0x3ded
+  __TEXT.__oslogstring: 0x1becb
+  __TEXT.__objc_classname: 0x7ef
+  __TEXT.__objc_methname: 0x1513a
+  __TEXT.__objc_methtype: 0x353b
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0xe26
   __TEXT.__constg_swiftt: 0x5e0
-  __TEXT.__swift5_reflstr: 0x4e3
-  __TEXT.__swift5_fieldmd: 0x570
+  __TEXT.__swift5_reflstr: 0x503
+  __TEXT.__swift5_fieldmd: 0x57c
   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x68
   __TEXT.__swift_as_entry: 0x9c
   __TEXT.__swift_as_ret: 0xc0
   __TEXT.__swift_as_cont: 0x13c
-  __TEXT.__swift5_capture: 0x9bc
+  __TEXT.__swift5_capture: 0x9d4
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2ca8
+  __TEXT.__unwind_info: 0x2cf0
   __TEXT.__eh_frame: 0x1a80
-  __DATA_CONST.__const: 0x5950
+  __DATA_CONST.__const: 0x5980
   __DATA_CONST.__cfstring: 0x3d00
-  __DATA_CONST.__objc_classlist: 0x108
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_intobj: 0x3c0
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x60

   __DATA_CONST.__auth_got: 0x10c8
   __DATA_CONST.__got: 0x12f8
   __DATA_CONST.__auth_ptr: 0x330
-  __DATA.__objc_const: 0x3878
-  __DATA.__objc_selrefs: 0x40b8
-  __DATA.__objc_ivar: 0x248
-  __DATA.__objc_data: 0xc88
-  __DATA.__data: 0xdd8
+  __DATA.__objc_const: 0x3db8
+  __DATA.__objc_selrefs: 0x4180
+  __DATA.__objc_ivar: 0x274
+  __DATA.__objc_data: 0xdc8
+  __DATA.__data: 0xe98
   __DATA.__bss: 0x1060
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2607
+  Functions: 2651
   Symbols:   920
-  CStrings:  5228
+  CStrings:  5301
 
CStrings:
+ "@\"<IMDMessageStoring>\"16@0:8"
+ "@\"<IMPowerLogging>\"16@0:8"
+ "@\"<MessageSendControllerDelegate>\""
+ "@\"<MessageSendControllerDependencyProviding>\""
+ "@\"IMDAppleServiceSession\""
+ "@128@0:8@16@24@32@40@48B56@60@68@76@84@92B100B104B108@112@120"
+ "@28@0:8B16@?20"
+ "@32@0:8B16I20B24B28"
+ "Failed sending message withGUID: %@  to people: %@   error: %d"
+ "Finished sending message: (guid: %@) people: %@ error: %d is chat: %{bool}d from me - to me: %{bool}d"
+ "Got error %@ while replicating, suppressing"
+ "Ignoring stale transcript background %llu < current %llu for chat %s."
+ "Incoming background version: %llu is lower than current chat background version: %llu."
+ "MessageSendCompletionHandler"
+ "MessageSendController"
+ "MessageSendControllerDelegate"
+ "MessageSendControllerDependencyProvider"
+ "MessageSendControllerDependencyProviding"
+ "MessageSendNotificationContext"
+ "PendingUpdate - needsDeliveryReceipt is %{BOOL}d for %@"
+ "PrepareMessage %s: %s failure, failing message"
+ "Requesting delivery status for message GUID %@ for attachment update, not a group chat"
+ "T@\"<IMDMessageStoring>\",R,N"
+ "T@\"<IMPowerLogging>\",R,N"
+ "T@\"<MessageSendControllerDelegate>\",R,N,V_delegate"
+ "T@\"<MessageSendControllerDependencyProviding>\",R,N,V_dependencies"
+ "T@\"IMDAppleServiceSession\",R,N,V_serviceSession"
+ "T@\"NSMutableDictionary\",&,N,V_transcriptBackgroundInFlightVersionByChatGUID"
+ "T@?,R,N,V_notificationHandler"
+ "TB,N,V_needsDeliveryReceipt"
+ "TB,R,N,GisLastCall,V_lastCall"
+ "TB,R,N,V_replicating"
+ "TB,R,N,V_sendSuccess"
+ "TI,R,N,V_errorType"
+ "Unrecoverable acquisition"
+ "Unrecoverable acquisition failure for message %@; failing send."
+ "_dependencies"
+ "_errorType"
+ "_handleDelayedSendFailureForMessage:withContext:"
+ "_lastCall"
+ "_needsDeliveryReceipt"
+ "_notificationHandler"
+ "_postPopulateFileTransferUpdates:message:indexForTransferGUID:"
+ "_prePopulateFileTransferUpdates:message:reason:indexForTransferGUID:"
+ "_replicating"
+ "_sendMessage:context:deliveryContext:fromID:fromAccount:toID:chatIdentifier:chatStyle:toSessionToken:toGroup:toParticipants:originallyToParticipants:requiredRegProperties:interestingRegProperties:requiresLackOfRegProperties:canInlineAttachments:flushingPLAS:sendAsAttachmentUpdate:suppressDeliveryReceipt:isPreAsyncFallback:type:msgPayloadUploadDictionary:originalPayload:replyToMessageGUID:fallbackCount:willSendBlock:placeholderSentBlock:completionBlock:"
+ "_sendSuccess"
+ "_transcriptBackgroundInFlightVersionByChatGUID"
+ "areMySelectedAliases:forService:"
+ "dependencies"
+ "errorType"
+ "handleDeliveryCompletion:withSendContext:message:"
+ "handleIDSCompletionCall error: %d hasNotifiedClient: %{bool}d lastCall: %{bool}d"
+ "handleIDSCompletionCallWithError:isLastCall:"
+ "hasNotifiedClient: %{bool}d sendSuccess: %{bool}d "
+ "idsOptionsForAttachmentUpdateWithMessageItem:toID:fromID:sendGUIDData:alternateCallbackID:isBusinessMessage:chatIdentifier:requiredRegProperties:interestingRegProperties:requiresLackOfRegProperties:deliveryContext:isGroupChat:suppressDeliveryReceipt:canInlineAttachments:msgPayloadUploadDictionary:messageDictionary:"
+ "idsOptionsWithMessageItem:toID:fromID:sendGUIDData:alternateCallbackID:isBusinessMessage:chatIdentifier:requiredRegProperties:interestingRegProperties:requiresLackOfRegProperties:deliveryContext:isGroupChat:suppressDeliveryReceipt:canInlineAttachments:msgPayloadUploadDictionary:messageDictionary:"
+ "initWithDelegate:"
+ "initWithDelegate:dependencies:"
+ "initWithReplicating:notificationHandler:"
+ "initWithSendSuccess:errorType:hasNotifiedClient:lastCall:"
+ "isOneOfMySelectedAliases:forService:"
+ "lastCall"
+ "needsDeliveryReceipt"
+ "normalizeUpdateUserInfoOrder:"
+ "notificationHandler"
+ "powerLog"
+ "replicating"
+ "sendController:FTAWDLogForMessage:withContext:"
+ "sendController:deactivateAccountDueToInvalidState:imdAccount:"
+ "sendController:didHandleDeliveryFailureForMessageNeedingRelay:"
+ "sendController:didSendMessage:withContext:forceDate:fromStorage:"
+ "sendController:handleScheduledMessageSendFailure:"
+ "sendController:trackFinishedSentMessage:"
+ "sendController:trackIDSTokenURI:forChatIdentifier:chatStyle:messageGUID:"
+ "sendControllerDidStopTimingMessageSend:"
+ "sendSuccess"
+ "setNeedsDeliveryReceipt:"
+ "setTranscriptBackgroundInFlightVersionByChatGUID:"
+ "transcriptBackgroundInFlightVersionByChatGUID"
+ "v16@?0@\"MessageSendNotificationContext\"8"
+ "v220@0:8@16@24@32@40@48@56@64C72@76@84@92@100@108@116@124B132@136B144B148B152q156@164@172@180Q188@?196@?204@?212"
+ "v24@0:8@\"MessageSendController\"16"
+ "v24@0:8I16B20"
+ "v32@0:8@\"MessageSendController\"16@\"IMMessageItem\"24"
+ "v40@0:8@\"MessageSendController\"16@\"IDSAccount\"24@\"IMDAccount\"32"
+ "v40@0:8@\"MessageSendController\"16@\"IMMessageItem\"24@\"SendMessageContext\"32"
+ "v48@0:8@16@24q32@40"
+ "v52@0:8@\"MessageSendController\"16@\"IMMessageItem\"24@\"SendMessageContext\"32@\"NSDate\"40B48"
+ "v52@0:8@\"MessageSendController\"16@\"NSString\"24@\"NSString\"32C40@\"NSString\"44"
+ "v52@0:8@16@24@32@40B48"
- "@124@0:8@16@24@32@40@48B56@60@68@76@84@92B100B104@108@116"
- "Finished sending message: (guid: %@) %@ to people: %@ error: %d is chat: %@ from me - to me: %@"
- "Got error %@ while replicating %@, suppressing"
- "Incoming background version: %llu is lower than current chat background version: %@."
- "PrepareMessage %s: Comm safety failure, failing message"
- "T@\"MessageServiceSession\",R,N,V_serviceSession"
- "_postPopulateFileTransferUpdates:message:"
- "_prePopulateFileTransferUpdates:message:reason:"
- "_sendMessage:context:deliveryContext:fromID:fromAccount:toID:chatIdentifier:chatStyle:toSessionToken:toGroup:toParticipants:originallyToParticipants:requiredRegProperties:interestingRegProperties:requiresLackOfRegProperties:canInlineAttachments:flushingPLAS:sendAsAttachmentUpdate:isPreAsyncFallback:type:msgPayloadUploadDictionary:originalPayload:replyToMessageGUID:fallbackCount:willSendBlock:placeholderSentBlock:completionBlock:"
- "areMyAliases:forService:"
- "hasNotifiedClient: %@ sendSuccess: %@ "
- "idsCompletionBlock returned with error: %d guid: %@ hasNotifiedClient: %@ block: %@"
- "idsOptionsForAttachmentUpdateWithMessageItem:toID:fromID:sendGUIDData:alternateCallbackID:isBusinessMessage:chatIdentifier:requiredRegProperties:interestingRegProperties:requiresLackOfRegProperties:deliveryContext:isGroupChat:canInlineAttachments:msgPayloadUploadDictionary:messageDictionary:"
- "idsOptionsWithMessageItem:toID:fromID:sendGUIDData:alternateCallbackID:isBusinessMessage:chatIdentifier:requiredRegProperties:interestingRegProperties:requiresLackOfRegProperties:deliveryContext:isGroupChat:canInlineAttachments:msgPayloadUploadDictionary:messageDictionary:"
- "isOneOfMyAliases:forService:"
- "subarrayWithRange:"
- "v216@0:8@16@24@32@40@48@56@64C72@76@84@92@100@108@116@124B132@136B144B148q152@160@168@176Q184@?192@?200@?208"
- "v40@0:8@16@24q32"
```
