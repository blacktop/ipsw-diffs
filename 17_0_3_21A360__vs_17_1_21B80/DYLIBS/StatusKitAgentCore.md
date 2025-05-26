## StatusKitAgentCore

> `/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore`

```diff

-25.100.1.0.0
-  __TEXT.__text: 0xa5030
-  __TEXT.__auth_stubs: 0x1520
+25.200.71.2.2
+  __TEXT.__text: 0xa5368
+  __TEXT.__auth_stubs: 0x1540
   __TEXT.__objc_methlist: 0x55b4
   __TEXT.__const: 0x57c
-  __TEXT.__cstring: 0x3fda
-  __TEXT.__oslogstring: 0xde0e
+  __TEXT.__cstring: 0x400a
+  __TEXT.__oslogstring: 0xdef0
   __TEXT.__gcc_except_tab: 0xaa8
   __TEXT.__swift5_typeref: 0x764
   __TEXT.__swift5_capture: 0x1d0

   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2058
+  __TEXT.__unwind_info: 0x205c
   __TEXT.__eh_frame: 0x1388
   __TEXT.__objc_classname: 0xc72
-  __TEXT.__objc_methname: 0xe98c
-  __TEXT.__objc_methtype: 0x40b6
-  __TEXT.__objc_stubs: 0x85a0
+  __TEXT.__objc_methname: 0xe9f2
+  __TEXT.__objc_methtype: 0x40ea
+  __TEXT.__objc_stubs: 0x8580
   __DATA_CONST.__got: 0x350
-  __DATA_CONST.__const: 0x1780
+  __DATA_CONST.__const: 0x17a8
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x158

   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xaa0
+  __AUTH_CONST.__auth_got: 0xab0
   __AUTH.__objc_data: 0xae8
   __DATA.__objc_protorefs: 0x30
   __DATA.__objc_classrefs: 0x4b0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3303
-  Symbols:   8726
-  CStrings:  3733
+  Functions: 3304
+  Symbols:   8730
+  CStrings:  3739
 
Symbols:
+ -[SKAChannelManager pushManager:didReceiveData:onChannel:identifier:dateReceived:dateExpired:]
+ -[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:withIdentifier:]
+ -[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:withIdentifier:].cold.1
+ -[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:withIdentifier:].cold.2
+ -[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:withIdentifier:].cold.3
+ -[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:withIdentifier:].cold.4
+ -[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:withIdentifier:].cold.5
+ -[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:withIdentifier:].cold.6
+ -[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:withIdentifier:].cold.7
+ -[SKAPresenceManager channelReceivedIncomingPayloadUpdate:channel:withIdentifier:]
+ -[SKAPresenceManager channelReceivedIncomingPayloadUpdate:channel:withIdentifier:].cold.1
+ -[SKAPresenceManager channelReceivedIncomingPayloadUpdate:channel:withIdentifier:].cold.2
+ -[SKAPresenceManager payloadUpdateProcessingQueue]
+ -[SKAPresenceManager setPayloadUpdateProcessingQueue:]
+ -[SKAStatusServer channelManager:didReceiveData:onChannel:identifier:dateReceived:dateExpired:]
+ -[SKAStatusServer channelManager:didReceiveData:onChannel:identifier:dateReceived:dateExpired:].cold.1
+ -[SKAStatusServer channelManager:didReceiveData:onChannel:identifier:dateReceived:dateExpired:].cold.2
+ -[SKAStatusServer channelManager:didReceiveData:onChannel:identifier:dateReceived:dateExpired:].cold.3
+ GCC_except_table85
+ GCC_except_table90
+ _OBJC_IVAR_$_SKAPresenceManager._payloadUpdateProcessingQueue
+ ___113-[SKAPresenceManager retainPresenceAssertionForPresenceIdentifier:withPresencePayload:options:client:completion:]_block_invoke.12
+ ___76-[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:withIdentifier:]_block_invoke
+ ___76-[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:withIdentifier:]_block_invoke.cold.1
+ ___82-[SKAPresenceManager channelReceivedIncomingPayloadUpdate:channel:withIdentifier:]_block_invoke
+ ___82-[SKAPresenceManager channelReceivedIncomingPayloadUpdate:channel:withIdentifier:]_block_invoke_2
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.117
+ _dispatch_resume
+ _dispatch_suspend
+ _objc_msgSend$_handleIncomingPayloadUpdate:onChannel:withIdentifier:
+ _objc_msgSend$channelManager:didReceiveData:onChannel:identifier:dateReceived:dateExpired:
+ _objc_msgSend$channelReceivedIncomingPayloadUpdate:channel:withIdentifier:
+ _objc_msgSend$payloadUpdateProcessingQueue
+ _objc_msgSend$pushManager:didReceiveData:onChannel:identifier:dateReceived:dateExpired:
- -[SKAChannelManager pushManager:didReceiveData:onChannel:dateReceived:dateExpired:]
- -[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:]
- -[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:].cold.1
- -[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:].cold.2
- -[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:].cold.3
- -[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:].cold.4
- -[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:].cold.5
- -[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:].cold.6
- -[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:].cold.7
- -[SKAPresenceManager channelReceivedIncomingPayloadUpdate:channel:]
- -[SKAPresenceManager channelReceivedIncomingPayloadUpdate:channel:].cold.1
- -[SKAPresenceManager channelReceivedIncomingPayloadUpdate:channel:].cold.2
- -[SKAPresenceManager lastAssertionSendTime]
- -[SKAPresenceManager setLastAssertionSendTime:]
- -[SKAStatusServer channelManager:didReceiveData:onChannel:dateReceived:dateExpired:]
- -[SKAStatusServer channelManager:didReceiveData:onChannel:dateReceived:dateExpired:].cold.1
- -[SKAStatusServer channelManager:didReceiveData:onChannel:dateReceived:dateExpired:].cold.2
- -[SKAStatusServer channelManager:didReceiveData:onChannel:dateReceived:dateExpired:].cold.3
- GCC_except_table81
- GCC_except_table89
- _OBJC_IVAR_$_SKAPresenceManager._lastAssertionSendTime
- ___113-[SKAPresenceManager retainPresenceAssertionForPresenceIdentifier:withPresencePayload:options:client:completion:]_block_invoke.10
- ___61-[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:]_block_invoke
- ___61-[SKAPresenceManager _handleIncomingPayloadUpdate:onChannel:]_block_invoke.cold.1
- ___67-[SKAPresenceManager channelReceivedIncomingPayloadUpdate:channel:]_block_invoke
- ___block_descriptor_88_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- ___block_literal_global.116
- _objc_msgSend$_handleIncomingPayloadUpdate:onChannel:
- _objc_msgSend$channelManager:didReceiveData:onChannel:dateReceived:dateExpired:
- _objc_msgSend$channelReceivedIncomingPayloadUpdate:channel:
- _objc_msgSend$lastAssertionSendTime
- _objc_msgSend$pushManager:didReceiveData:onChannel:dateReceived:dateExpired:
- _objc_msgSend$setLastAssertionSendTime:
CStrings:
+ "Handling payload update %lu with lastCheckpoint %lld and previous checkpoint %lld"
+ "Payload last checkpoint is 0 with newer updates -- not polling"
+ "Payload last checkpoint is 0 with older updates -- dropping"
+ "Receieved aps incoming message %lu : %@ -- expiration: %@"
+ "Received data on channel: %@ identifier: %lu"
+ "Received data on channel: %@ with identifier %lu"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_payloadUpdateProcessingQueue"
+ "_handleIncomingPayloadUpdate:onChannel:withIdentifier:"
+ "_payloadUpdateProcessingQueue"
+ "channelManager:didReceiveData:onChannel:identifier:dateReceived:dateExpired:"
+ "channelReceivedIncomingPayloadUpdate:channel:withIdentifier:"
+ "com.apple.StatusKitAgent.PayloadUpdateProcessing"
+ "payloadUpdateProcessingQueue"
+ "payloadUpdateProcessingQueue resumed"
+ "payloadUpdateProcessingQueue suspended. Sending presence assertion message for presence identifier %@ on channel %@"
+ "pushManager:didReceiveData:onChannel:identifier:dateReceived:dateExpired:"
+ "setPayloadUpdateProcessingQueue:"
+ "v40@0:8@\"NSData\"16@\"SKADatabaseChannel\"24Q32"
+ "v40@0:8@16@24Q32"
+ "v64@0:8@\"<SKAChannelManaging>\"16@\"NSData\"24@\"NSString\"32Q40@\"NSDate\"48@\"NSDate\"56"
+ "v64@0:8@\"<SKAPushManaging>\"16@\"NSData\"24@\"NSString\"32Q40@\"NSDate\"48@\"NSDate\"56"
+ "v64@0:8@16@24@32Q40@48@56"
- "Payload last checkpoint is 0 -- not polling"
- "Receieved aps incoming message: %@ -- expiration: %@"
- "Received data on channel: %@"
- "Sending presence assertion message for presence identifier %@ on channel %@"
- "T@\"NSDate\",&,N,V_lastAssertionSendTime"
- "We recently sent an assertion message. Delaying processing of incoming push by %f"
- "_handleIncomingPayloadUpdate:onChannel:"
- "_lastAssertionSendTime"
- "channelManager:didReceiveData:onChannel:dateReceived:dateExpired:"
- "channelReceivedIncomingPayloadUpdate:channel:"
- "lastAssertionSendTime"
- "pushManager:didReceiveData:onChannel:dateReceived:dateExpired:"
- "setLastAssertionSendTime:"
- "v32@0:8@\"NSData\"16@\"SKADatabaseChannel\"24"
- "v56@0:8@\"<SKAChannelManaging>\"16@\"NSData\"24@\"NSString\"32@\"NSDate\"40@\"NSDate\"48"
- "v56@0:8@\"<SKAPushManaging>\"16@\"NSData\"24@\"NSString\"32@\"NSDate\"40@\"NSDate\"48"

```
