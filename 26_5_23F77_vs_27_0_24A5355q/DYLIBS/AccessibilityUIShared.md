## AccessibilityUIShared

> `/System/Library/PrivateFrameworks/AccessibilityUIShared.framework/AccessibilityUIShared`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x3488
-  __TEXT.__auth_stubs: 0x480
+3229.1.6.0.0
+  __TEXT.__text: 0x2fe4
   __TEXT.__objc_methlist: 0x434
-  __TEXT.__cstring: 0x49a
   __TEXT.__const: 0x30
-  __TEXT.__oslogstring: 0x225
   __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__unwind_info: 0x1a8
-  __TEXT.__objc_classname: 0xb1
-  __TEXT.__objc_methname: 0xf17
-  __TEXT.__objc_methtype: 0x3b0
-  __TEXT.__objc_stubs: 0xa40
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x358
+  __TEXT.__cstring: 0x4a7
+  __TEXT.__oslogstring: 0x225
+  __TEXT.__unwind_info: 0x168
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x330
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x378
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x250
+  __DATA_CONST.__got: 0x98
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x2a0
   __AUTH_CONST.__objc_const: 0x7d8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x110
   __DATA_DIRTY.__objc_data: 0x190

   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E0BF4942-16EE-312D-9BBC-54C00253A89D
-  Functions: 99
-  Symbols:   490
-  CStrings:  286
+  UUID: 1117E2CE-318A-3B59-8797-9F92210AAC49
+  Functions: 85
+  Symbols:   462
+  CStrings:  70
 
Symbols:
+ -[AXMultiplexConnectionHandler remoteToken]
+ -[AXMultiplexConnectionHandler setRemoteToken:]
+ GCC_except_table41
+ GCC_except_table45
+ GCC_except_table55
+ GCC_except_table65
+ _OBJC_IVAR_$_AXMultiplexConnectionHandler._remoteToken
+ ___block_literal_global.47
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$remoteToken
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x4
- +[AXUIMessageReplyHandler createReplyObject:fromMessage:withError:].cold.1
- -[AXMultiplexConnectionHandler processHandle]
- -[AXMultiplexConnectionHandler setProcessHandle:]
- -[AXUIMessageSender _sendXPCMessage:context:completionBlock:completionRequiresWritingBlock:targetAccessQueue:timeout:].cold.1
- -[AXUIMessageSender sendAsynchronousMessage:withIdentifier:context:targetAccessQueue:completionRequiresWritingBlock:completion:timeout:].cold.1
- -[AXUIMessageSender sendAsynchronousMessage:withIdentifier:context:targetAccessQueue:completionRequiresWritingBlock:completion:timeout:].cold.2
- GCC_except_table1
- GCC_except_table13
- GCC_except_table23
- GCC_except_table25
- _AXUIServiceManagerLaunchAngelInterface.cold.1
- _OBJC_IVAR_$_AXMultiplexConnectionHandler._processHandle
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- ___118-[AXUIMessageSender _sendXPCMessage:context:completionBlock:completionRequiresWritingBlock:targetAccessQueue:timeout:]_block_invoke.34.cold.1
- ___118-[AXUIMessageSender _sendXPCMessage:context:completionBlock:completionRequiresWritingBlock:targetAccessQueue:timeout:]_block_invoke.cold.1
- ___61-[AXUIMessageSendHandler _sendMessage:context:previousError:]_block_invoke.1.cold.1
- ___61-[AXUIMessageSendHandler _sendMessage:context:previousError:]_block_invoke.6.cold.1
- ___61-[AXUIMessageSendHandler _sendMessage:context:previousError:]_block_invoke.cold.1
- ___96-[AXUIMessageSender _sendLaunchAngelMessage:context:remainingAttempts:previousError:completion:]_block_invoke_3.cold.1
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
- _objc_msgSend$auditToken
- _objc_msgSend$processHandle
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<AXUIMessageSenderDelegate>\""
- "@\"AXAccessQueue\""
- "@\"AXDispatchTimer\""
- "@\"AXUIMessageSender\""
- "@\"BSProcessHandle\""
- "@\"BSServiceConnection\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8@16Q24^v32^@40"
- "@?"
- "@?16@0:8"
- "AXMultiplexConnectionHandler"
- "AXUIMessageContext"
- "AXUIMessageReplyHandler"
- "AXUIMessageSendHandler"
- "AXUIMessageSender"
- "AccessibilityBoardServices_ServerProtocol"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<AXUIMessageSenderDelegate>\",W,N,V_delegate"
- "T@\"AXAccessQueue\",&,N,V_messageSchedulingSerializationQueue"
- "T@\"AXAccessQueue\",&,N,V_targetAccessQueue"
- "T@\"AXDispatchTimer\",&,V_sendingTimer"
- "T@\"AXUIMessageSender\",W,N,V_messageSender"
- "T@\"BSProcessHandle\",&,N,V_processHandle"
- "T@\"BSServiceConnection\",&,N,V_serviceConnection"
- "T@\"NSMutableArray\",&,N,V_messageQueue"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_connection"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_xpcMessage"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@?,C,N,V_completion"
- "T@?,C,N,V_xpc_handler"
- "T@?,C,V_completion"
- "TB,N,GisSendingMessage,V_sendingMessage"
- "TB,N,V_completionRequiresWritingBlock"
- "TQ,N,V_remainingAttempts"
- "TQ,R"
- "T^v,N,V_context"
- "Td,N,V_timeout"
- "T{os_unfair_lock_s=I},N,V_delegateAccessLock"
- "UTF8String"
- "Vv16@0:8"
- "Vv32@0:8@\"NSObject<OS_xpc_object>\"16@?<v@?@\"NSObject<OS_xpc_object>\"@\"NSError\">24"
- "Vv32@0:8@16@?24"
- "^v"
- "^v16@0:8"
- "^{_NSZone=}16@0:8"
- "_completion"
- "_completionRequiresWritingBlock"
- "_connection"
- "_context"
- "_delegate"
- "_delegateAccessLock"
- "_didFinishSendingXPCMessage:replyCustomData:"
- "_messageQueue"
- "_messageSchedulingSerializationQueue"
- "_messageSender"
- "_performBlock:inAccessQueue:treatAsWritingBlock:"
- "_processHandle"
- "_remainingAttempts"
- "_sendLaunchAngelMessage:context:remainingAttempts:previousError:completion:"
- "_sendMessage:context:previousError:"
- "_sendXPCMessage:context:completionBlock:completionRequiresWritingBlock:targetAccessQueue:timeout:"
- "_sendXPCMessage:context:remainingAttempts:previousError:completion:"
- "_sendingMessage"
- "_sendingTimer"
- "_serviceConnection"
- "_targetAccessQueue"
- "_timeout"
- "_xpcMessage"
- "_xpc_handler"
- "afterDelay:processBlock:"
- "afterDelay:processReadingBlock:"
- "auditToken"
- "autorelease"
- "ax_dequeueObject"
- "ax_enqueueObject:"
- "ax_errorWithDomain:description:"
- "ax_nonRedundantDescription"
- "backgroundAccessQueue"
- "cancel"
- "class"
- "completion"
- "completionRequiresWritingBlock"
- "conformsToProtocol:"
- "connection"
- "context"
- "copy"
- "copyXPCMessageFromDictionary:inReplyToXPCMessage:error:"
- "count"
- "createReplyObject:fromMessage:withError:"
- "currentThread"
- "d"
- "d16@0:8"
- "debugDescription"
- "delegate"
- "delegateAccessLock"
- "description"
- "dictionaryFromXPCMessage:error:"
- "dictionaryWithObjects:forKeys:count:"
- "domain"
- "errorWithDomain:code:userInfo:"
- "hash"
- "i16@0:8"
- "init"
- "initWithMessageSender:delegate:"
- "initWithParentClass:description:appendUUIDToLabel:"
- "initWithTargetSerialQueue:"
- "initWithUTF8String:"
- "interfaceWithIdentifier:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSendingMessage"
- "localizedDescription"
- "messageQueue"
- "messageSchedulingSerializationQueue"
- "messageSender"
- "messageSender:accessLaunchAngelConnectionForMessageWithContext:usingBlock:"
- "messageSender:extractCustomDataFromXPCReply:numberOfKeyValuePairsForCustomData:"
- "messageSender:processCustomDataFromXPCReply:"
- "messageSender:willSendXPCMessage:context:"
- "numberWithUnsignedInteger:"
- "performAsynchronousReadingBlock:"
- "performAsynchronousWritingBlock:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performSynchronousWritingBlock:"
- "pid"
- "processHandle"
- "protocolForProtocol:"
- "realToken"
- "release"
- "remainingAttempts"
- "remoteTarget"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendAsynchronousMessage:withIdentifier:context:targetAccessQueue:completionRequiresWritingBlock:completion:"
- "sendAsynchronousMessage:withIdentifier:context:targetAccessQueue:completionRequiresWritingBlock:completion:timeout:"
- "sendBoardServiceMessage:callback:"
- "sendReply:withError:andOriginalXPCMessage:usingConnection:customDataAddingBlock:"
- "sendSynchronousMessage:withIdentifier:context:error:"
- "sendXPCMessage:context:completion:"
- "sendingMessage"
- "sendingTimer"
- "serviceConnection"
- "setClient:"
- "setClientMessagingExpectation:"
- "setCompletion:"
- "setCompletionRequiresWritingBlock:"
- "setConnection:"
- "setContext:"
- "setDelegate:"
- "setDelegateAccessLock:"
- "setMessageQueue:"
- "setMessageSchedulingSerializationQueue:"
- "setMessageSender:"
- "setProcessHandle:"
- "setRemainingAttempts:"
- "setSendingMessage:"
- "setSendingTimer:"
- "setServer:"
- "setServiceConnection:"
- "setTargetAccessQueue:"
- "setTimeout:"
- "setXpcMessage:"
- "setXpc_handler:"
- "stopSendingXPCMessage"
- "superclass"
- "targetAccessQueue"
- "timeout"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8{os_unfair_lock_s=I}16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8^v16"
- "v24@0:8d16"
- "v32@0:8@16^v24"
- "v36@0:8@?16@24B32"
- "v40@0:8@16^v24@32"
- "v40@0:8@16^v24@?32"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16^v24Q32@40@?48"
- "v60@0:8@16Q24^v32@40B48@?52"
- "v60@0:8@16^v24@?32B40@44d52"
- "v68@0:8@16Q24^v32@40B48@?52d60"
- "xpcMessage"
- "xpc_handler"
- "zone"
- "{?=[8I]}16@0:8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```
