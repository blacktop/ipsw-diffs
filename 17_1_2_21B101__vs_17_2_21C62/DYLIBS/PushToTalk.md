## PushToTalk

> `/System/Library/Frameworks/PushToTalk.framework/PushToTalk`

```diff

-1228.200.71.2.1
-  __TEXT.__text: 0x4048
+1228.300.81.0.0
+  __TEXT.__text: 0x42ec
   __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_methlist: 0x42c
+  __TEXT.__objc_methlist: 0x484
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x3f1
   __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__oslogstring: 0x69d
-  __TEXT.__unwind_info: 0x184
-  __TEXT.__objc_classname: 0x97
-  __TEXT.__objc_methname: 0x1771
-  __TEXT.__objc_methtype: 0x58e
-  __TEXT.__objc_stubs: 0xcc0
+  __TEXT.__oslogstring: 0x74d
+  __TEXT.__unwind_info: 0x188
+  __TEXT.__objc_classname: 0x99
+  __TEXT.__objc_methname: 0x19bd
+  __TEXT.__objc_methtype: 0x5c6
+  __TEXT.__objc_stubs: 0xdc0
   __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x168
+  __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xaf8
-  __DATA_CONST.__objc_selrefs: 0x470
+  __DATA_CONST.__objc_const: 0xb98
+  __DATA_CONST.__objc_selrefs: 0x4b0
   __AUTH_CONST.__cfstring: 0x260
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__objc_const: 0x1f8

   __AUTH.__objc_data: 0x190
   __DATA.__objc_classrefs: 0xc0
   __DATA.__objc_superrefs: 0x20
-  __DATA.__objc_ivar: 0x5c
+  __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x120
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /usr/lib/libBASupport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 123
-  Symbols:   545
-  CStrings:  345
+  Functions: 131
+  Symbols:   573
+  CStrings:  363
 
Symbols:
+ +[PTPushResult serviceUpdatePushResult]
+ -[PTChannelManager _appendPendingPushForUUID:payload:reply:isServiceUpdateMessage:isHighPriority:remainingHighPriorityBudget:]
+ -[PTChannelManager provider:didReceivePushPayload:channelUUID:reply:isServiceUpdateMessage:isHighPriority:remainingHighPriorityBudget:]
+ -[PTPendingPush isHighPriority]
+ -[PTPendingPush isServiceUpdateMessage]
+ -[PTPendingPush remainingHighPriorityBudget]
+ -[PTPendingPush setIsHighPriority:]
+ -[PTPendingPush setIsServiceUpdateMessage:]
+ -[PTPendingPush setRemainingHighPriorityBudget:]
+ GCC_except_table14
+ GCC_except_table24
+ GCC_except_table46
+ _OBJC_IVAR_$_PTPendingPush._isHighPriority
+ _OBJC_IVAR_$_PTPendingPush._isServiceUpdateMessage
+ _OBJC_IVAR_$_PTPendingPush._remainingHighPriorityBudget
+ ___41-[PTChannelManager _deliverPendingPushes]_block_invoke
+ ___41-[PTChannelManager leaveChannelWithUUID:]_block_invoke.64
+ ___88-[PTChannelManager _requestJoinChannelWithUUID:channelDescriptor:originator:completion:]_block_invoke.62
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ _objc_msgSend$_appendPendingPushForUUID:payload:reply:isServiceUpdateMessage:isHighPriority:remainingHighPriorityBudget:
+ _objc_msgSend$incomingServiceUpdatePushForChannelManager:channelUUID:pushPayload:isHighPriority:remainingHighPriorityBudget:withCompletionHandler:
+ _objc_msgSend$isHighPriority
+ _objc_msgSend$isServiceUpdateMessage
+ _objc_msgSend$remainingHighPriorityBudget
+ _objc_msgSend$serviceUpdatePushResult
+ _objc_msgSend$setIsHighPriority:
+ _objc_msgSend$setIsServiceUpdateMessage:
+ _objc_msgSend$setRemainingHighPriorityBudget:
+ _objc_release_x27
- -[PTChannelManager _appendPendingPushForUUID:payload:reply:]
- -[PTChannelManager provider:didReceivePushPayload:channelUUID:reply:]
- GCC_except_table18
- GCC_except_table40
- GCC_except_table8
- ___41-[PTChannelManager leaveChannelWithUUID:]_block_invoke.43
- ___88-[PTChannelManager _requestJoinChannelWithUUID:channelDescriptor:originator:completion:]_block_invoke.41
- _objc_msgSend$_appendPendingPushForUUID:payload:reply:
- _objc_release_x28
CStrings:
+ "\x13"
+ "PTChannelManager received a Service Update push message but the PTChannelManagerDelegate has not implemented the delegate protocol required to receive Service Update messages."
+ "TB,N,V_isHighPriority"
+ "TB,N,V_isServiceUpdateMessage"
+ "Tq,N,V_remainingHighPriorityBudget"
+ "_appendPendingPushForUUID:payload:reply:isServiceUpdateMessage:isHighPriority:remainingHighPriorityBudget:"
+ "_isHighPriority"
+ "_isServiceUpdateMessage"
+ "_remainingHighPriorityBudget"
+ "incomingServiceUpdatePushForChannelManager:channelUUID:pushPayload:isHighPriority:remainingHighPriorityBudget:withCompletionHandler:"
+ "isHighPriority"
+ "isServiceUpdateMessage"
+ "provider:didReceivePushPayload:channelUUID:reply:isServiceUpdateMessage:isHighPriority:remainingHighPriorityBudget:"
+ "remainingHighPriorityBudget"
+ "serviceUpdatePushResult"
+ "setIsHighPriority:"
+ "setIsServiceUpdateMessage:"
+ "setRemainingHighPriorityBudget:"
+ "v24@0:8q16"
+ "v56@0:8@16@24@?32B40B44q48"
+ "v64@0:8@\"CXChannelProvider\"16@\"NSDictionary\"24@\"NSUUID\"32@?<v@?q@\"CXParticipant\">40B48B52q56"
+ "v64@0:8@16@24@32@?40B48B52q56"
- "_appendPendingPushForUUID:payload:reply:"
- "provider:didReceivePushPayload:channelUUID:reply:"
- "v48@0:8@\"CXChannelProvider\"16@\"NSDictionary\"24@\"NSUUID\"32@?<v@?q@\"CXParticipant\">40"
- "v48@0:8@16@24@32@?40"

```
