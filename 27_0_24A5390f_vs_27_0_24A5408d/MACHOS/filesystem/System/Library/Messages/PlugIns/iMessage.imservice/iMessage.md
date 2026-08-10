## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

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

-1487.100.6.2.2
-  __TEXT.__text: 0x10a50c
+1491.100.1.2.11
+  __TEXT.__text: 0x10b510
   __TEXT.__auth_stubs: 0x2590
-  __TEXT.__objc_stubs: 0xeb20
-  __TEXT.__objc_methlist: 0x3074
+  __TEXT.__objc_stubs: 0xee00
+  __TEXT.__objc_methlist: 0x32a4
   __TEXT.__const: 0x15f8
-  __TEXT.__gcc_except_tab: 0x9a84
-  __TEXT.__cstring: 0x3e7d
-  __TEXT.__oslogstring: 0x1c51b
-  __TEXT.__objc_classname: 0x72f
-  __TEXT.__objc_methname: 0x14e7e
-  __TEXT.__objc_methtype: 0x32a9
+  __TEXT.__gcc_except_tab: 0x9918
+  __TEXT.__cstring: 0x3ebd
+  __TEXT.__oslogstring: 0x1c65b
+  __TEXT.__objc_classname: 0x7ef
+  __TEXT.__objc_methname: 0x1548e
+  __TEXT.__objc_methtype: 0x355e
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
-  __TEXT.__swift5_capture: 0x9b8
+  __TEXT.__swift5_capture: 0x9d0
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2bd8
+  __TEXT.__unwind_info: 0x2c08
   __TEXT.__eh_frame: 0x1a80
-  __DATA_CONST.__const: 0x5458
+  __DATA_CONST.__const: 0x5480
   __DATA_CONST.__cfstring: 0x3e80
-  __DATA_CONST.__objc_classlist: 0x108
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_intobj: 0x3f0
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x60

   __DATA_CONST.__auth_got: 0x12d8
   __DATA_CONST.__got: 0x1360
   __DATA_CONST.__auth_ptr: 0x330
-  __DATA.__objc_const: 0x3878
-  __DATA.__objc_selrefs: 0x4188
-  __DATA.__objc_ivar: 0x248
-  __DATA.__objc_data: 0xc88
-  __DATA.__data: 0xdd8
+  __DATA.__objc_const: 0x3db0
+  __DATA.__objc_selrefs: 0x4248
+  __DATA.__objc_ivar: 0x270
+  __DATA.__objc_data: 0xdc8
+  __DATA.__data: 0xe98
   __DATA.__bss: 0x1070
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2417
+  Functions: 2455
   Symbols:   1000
-  CStrings:  5302
+  CStrings:  5373
 
CStrings:
+ "@\"<IMDChorosFringeDetecting>\"16@0:8"
+ "@\"<IMDMessageStoring>\"16@0:8"
+ "@\"<IMPowerLogging>\"16@0:8"
+ "@\"<MessageSendControllerDelegate>\""
+ "@\"<MessageSendControllerDependencyProviding>\""
+ "@\"IMDAppleServiceSession\""
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
+ "PrepareMessage %s: %s failure, failing message"
+ "Setting needsDeliveryReceipt to %{BOOL}d since allExistingTransfersAreGradients = %{BOOL}d for transfers on message guid %@"
+ "T@\"<IMDChorosFringeDetecting>\",R,N"
+ "T@\"<IMDMessageStoring>\",R,N"
+ "T@\"<IMPowerLogging>\",R,N"
+ "T@\"<MessageSendControllerDelegate>\",R,N,V_delegate"
+ "T@\"<MessageSendControllerDependencyProviding>\",R,N,V_dependencies"
+ "T@\"IMDAppleServiceSession\",R,N,V_serviceSession"
+ "T@\"NSMutableDictionary\",&,N,V_transcriptBackgroundInFlightVersionByChatGUID"
+ "T@?,R,N,V_notificationHandler"
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
+ "_notificationHandler"
+ "_postPopulateFileTransferUpdates:message:indexForTransferGUID:"
+ "_prePopulateFileTransferUpdates:message:reason:indexForTransferGUID:"
+ "_replicating"
+ "_sendSuccess"
+ "_transcriptBackgroundInFlightVersionByChatGUID"
+ "areMySelectedAliases:forService:"
+ "dependencies"
+ "errorType"
+ "fringeMessageDetector"
+ "handleDeliveryCompletion:withSendContext:message:"
+ "handleIDSCompletionCall error: %d hasNotifiedClient: %{bool}d lastCall: %{bool}d"
+ "handleIDSCompletionCallWithError:isLastCall:"
+ "hasNotifiedClient: %{bool}d sendSuccess: %{bool}d "
+ "initWithDelegate:"
+ "initWithDelegate:dependencies:"
+ "initWithReplicating:notificationHandler:"
+ "initWithSendSuccess:errorType:hasNotifiedClient:lastCall:"
+ "isOneOfMySelectedAliases:forService:"
+ "lastCall"
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
+ "setTranscriptBackgroundInFlightVersionByChatGUID:"
+ "transcriptBackgroundInFlightVersionByChatGUID"
+ "v16@?0@\"MessageSendNotificationContext\"8"
+ "v24@0:8@\"MessageSendController\"16"
+ "v24@0:8I16B20"
+ "v32@0:8@\"MessageSendController\"16@\"IMMessageItem\"24"
+ "v40@0:8@\"MessageSendController\"16@\"IDSAccount\"24@\"IMDAccount\"32"
+ "v40@0:8@\"MessageSendController\"16@\"IMMessageItem\"24@\"SendMessageContext\"32"
+ "v48@0:8@16@24q32@40"
+ "v52@0:8@\"MessageSendController\"16@\"IMMessageItem\"24@\"SendMessageContext\"32@\"NSDate\"40B48"
+ "v52@0:8@\"MessageSendController\"16@\"NSString\"24@\"NSString\"32C40@\"NSString\"44"
+ "v52@0:8@16@24@32@40B48"
- "Finished sending message: (guid: %@) %@ to people: %@ error: %d is chat: %@ from me - to me: %@"
- "Got error %@ while replicating %@, suppressing"
- "Incoming background version: %llu is lower than current chat background version: %@."
- "PrepareMessage %s: Comm safety failure, failing message"
- "T@\"MessageServiceSession\",R,N,V_serviceSession"
- "_postPopulateFileTransferUpdates:message:"
- "_prePopulateFileTransferUpdates:message:reason:"
- "areMyAliases:forService:"
- "hasNotifiedClient: %@ sendSuccess: %@ "
- "idsCompletionBlock returned with error: %d guid: %@ hasNotifiedClient: %@ block: %@"
- "isOneOfMyAliases:forService:"
- "subarrayWithRange:"
- "v40@0:8@16@24q32"
```
