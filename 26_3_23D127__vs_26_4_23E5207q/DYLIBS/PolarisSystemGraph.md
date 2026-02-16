## PolarisSystemGraph

> `/System/Library/PrivateFrameworks/PolarisSystemGraph.framework/PolarisSystemGraph`

```diff

-220.0.17.0.0
-  __TEXT.__text: 0xa310
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0x11a8
+220.100.15.0.3
+  __TEXT.__text: 0xb8f0
+  __TEXT.__auth_stubs: 0x3e0
+  __TEXT.__objc_methlist: 0x12d8
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x6b0
-  __TEXT.__oslogstring: 0xdbf
-  __TEXT.__unwind_info: 0x288
-  __TEXT.__objc_classname: 0x72f
-  __TEXT.__objc_methname: 0x20aa
-  __TEXT.__objc_methtype: 0x8c5
-  __TEXT.__objc_stubs: 0x1aa0
+  __TEXT.__cstring: 0x73f
+  __TEXT.__oslogstring: 0xe35
+  __TEXT.__unwind_info: 0x380
+  __TEXT.__objc_classname: 0x748
+  __TEXT.__objc_methname: 0x234f
+  __TEXT.__objc_methtype: 0x932
+  __TEXT.__objc_stubs: 0x1c80
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x1e0
-  __DATA_CONST.__objc_classlist: 0x1c8
+  __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8b8
-  __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x228
+  __DATA_CONST.__objc_selrefs: 0x950
+  __DATA_CONST.__objc_superrefs: 0x50
+  __AUTH_CONST.__auth_got: 0x1f8
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x2cd0
+  __AUTH_CONST.__cfstring: 0x160
+  __AUTH_CONST.__objc_const: 0x2ea8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x11d0
-  __DATA.__objc_ivar: 0xc0
+  __DATA.__objc_ivar: 0xd8
   __DATA.__data: 0x120
   __DATA.__bss: 0x20
+  __DATA_DIRTY.__objc_data: 0x1220
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7C2D253F-6553-3DCD-A6FB-A2FEDCB6B5ED
-  Functions: 291
-  Symbols:   1287
-  CStrings:  628
+  UUID: 7D207611-411C-381A-8998-46DB69934366
+  Functions: 312
+  Symbols:   1352
+  CStrings:  680
 
Symbols:
+ +[PSSGMessageDeRegisterAck messageWithSessionName:]
+ +[PSSGMessageResourceRequestsFailed messageWithResourceRequest:sender:reason:]
+ +[PSSGResourceOptions optionsWithDefaultStride:supportedStrides:setupSupported:baseMSGSyncID:availability:]
+ -[PSSGClient deregisterSelfAfterCrash]
+ -[PSSGClient deregisterSemaphore]
+ -[PSSGClient requestResourcesWithStrides:failedReason:]
+ -[PSSGClient resourceRequestsFailed:reason:]
+ -[PSSGClient resourceRequestsFailedReason]
+ -[PSSGClient setDeregisterSemaphore:]
+ -[PSSGClient setResourceRequestsFailedReason:]
+ -[PSSGComms canDeRegisterSelf]
+ -[PSSGComms canSend]
+ -[PSSGComms deRegisterSelf:]
+ -[PSSGComms disableSend]
+ -[PSSGComms disableSend].cold.1
+ -[PSSGComms isAbleToSend]
+ -[PSSGComms setCanDeRegisterSelf:]
+ -[PSSGComms setCanSend:]
+ -[PSSGMessageResourceRequestsFailed description]
+ -[PSSGMessageResourceRequestsFailed initWithRawMessage:]
+ -[PSSGMessageResourceRequestsFailed initWithType:sender:request:reason:]
+ -[PSSGMessageResourceRequestsFailed reason]
+ -[PSSGMessageResourceRequestsFailed serialize]
+ -[PSSGResourceOptions availability]
+ -[PSSGResourceOptions initWithDefaultStride:supportedStrides:setupSupported:baseMSGSyncID:availability:]
+ -[PSSGResourceOptions setAvailability:]
+ _OBJC_CLASS_$_PSSGMessageDeRegisterAck
+ _OBJC_IVAR_$_PSSGClient._deregisterSemaphore
+ _OBJC_IVAR_$_PSSGClient._resourceRequestsFailedReason
+ _OBJC_IVAR_$_PSSGComms._canDeRegisterSelf
+ _OBJC_IVAR_$_PSSGComms._canSend
+ _OBJC_IVAR_$_PSSGMessageResourceRequestsFailed._reason
+ _OBJC_IVAR_$_PSSGResourceOptions._availability
+ _OBJC_METACLASS_$_PSSGMessageDeRegisterAck
+ __OBJC_$_CLASS_METHODS_PSSGMessageDeRegisterAck
+ __OBJC_$_INSTANCE_METHODS_PSSGMessageResourceRequestsFailed
+ __OBJC_$_INSTANCE_VARIABLES_PSSGMessageResourceRequestsFailed
+ __OBJC_$_PROP_LIST_PSSGMessageResourceRequestsFailed
+ __OBJC_CLASS_RO_$_PSSGMessageDeRegisterAck
+ __OBJC_METACLASS_RO_$_PSSGMessageDeRegisterAck
+ _objc_msgSend$availability
+ _objc_msgSend$canDeRegisterSelf
+ _objc_msgSend$cancel
+ _objc_msgSend$deRegisterSelf:
+ _objc_msgSend$deregisterSemaphore
+ _objc_msgSend$disableSend
+ _objc_msgSend$exit
+ _objc_msgSend$initWithDefaultStride:supportedStrides:setupSupported:baseMSGSyncID:availability:
+ _objc_msgSend$initWithType:sender:request:reason:
+ _objc_msgSend$isAbleToSend
+ _objc_msgSend$messageWithResourceRequest:sender:reason:
+ _objc_msgSend$optionsWithDefaultStride:supportedStrides:setupSupported:baseMSGSyncID:availability:
+ _objc_msgSend$reason
+ _objc_msgSend$resourceRequestsFailedReason
+ _objc_msgSend$setCanDeRegisterSelf:
+ _objc_msgSend$setDeregisterSemaphore:
+ _objc_msgSend$setResourceRequestsFailedReason:
+ _objc_retainAutoreleasedReturnValue
+ _ps_comms_client_send_self
+ _ps_comms_disable_send
- +[PSSGMessageResourceRequestsFailed messageWithResourceRequest:sender:]
- +[PSSGResourceOptions optionsWithDefaultStride:supportedStrides:setupSupported:baseMSGSyncID:]
- -[PSSGClient requestResourcesWithStrides:]
- -[PSSGClient resourceRequestsFailed:]
- -[PSSGResourceOptions initWithDefaultStride:supportedStrides:setupSupported:baseMSGSyncID:]
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$initWithDefaultStride:supportedStrides:setupSupported:baseMSGSyncID:
- _objc_msgSend$optionsWithDefaultStride:supportedStrides:setupSupported:baseMSGSyncID:
- _objc_release_x9
- _objc_retain_x2
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
CStrings:
+ "%s:%d Failed to invalidate PSSGComms"
+ "(%@) <-- SELF_DEREGESTER_ACK"
+ "-[PSSGComms disableSend]"
+ "2"
+ "<%@: %p, sender %@, request %@, reason %@>"
+ "@24@0:8^{pssg_tx_s={?={?=IIIIIi}{?=I}(?={?=IIb16b8b8}{?=^vb8b8b8b8I}{?=^vb8b8b8b8I}{?=IIb24b8}{?=Qb16b8b8I})}Q[256c](?={?=QQQQ}{?=i}{?=^v})}16"
+ "@40@0:8@16@24Q32"
+ "@48@0:8I16@20B28@32Q40"
+ "@48@0:8Q16@24@32Q40"
+ "AB"
+ "B24@0:8@\"<PSSGMessage>\"16"
+ "B32@0:8@16^Q24"
+ "Failed to invalidate PSSGComms"
+ "Failed to send message because polarisd has crashed"
+ "PSSGMessageDeRegisterAck"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_deregisterSemaphore"
+ "TAB,V_canSend"
+ "TB,V_canDeRegisterSelf"
+ "TQ,N,V_availability"
+ "TQ,N,V_resourceRequestsFailedReason"
+ "TQ,R,N,V_reason"
+ "^{?={pssg_tx_s={?={?=IIIIIi}{?=I}(?={?=IIb16b8b8}{?=^vb8b8b8b8I}{?=^vb8b8b8b8I}{?=IIb24b8}{?=Qb16b8b8I})}Q[256c](?={?=QQQQ}{?=i}{?=^v})}iI(?=^v^[256c]^{pssg_stream_entry_s}^{pssg_stream_request_s}^{pssg_stream_availability_entry_s})}16@0:8"
+ "_availability"
+ "_canDeRegisterSelf"
+ "_canSend"
+ "_deregisterSemaphore"
+ "_reason"
+ "_resourceRequestsFailedReason"
+ "availability"
+ "canDeRegisterSelf"
+ "canSend"
+ "cancel"
+ "deRegisterSelf:"
+ "deregisterSelfAfterCrash"
+ "deregisterSemaphore"
+ "disableSend"
+ "entering sleep"
+ "exit"
+ "initWithDefaultStride:supportedStrides:setupSupported:baseMSGSyncID:availability:"
+ "initWithType:sender:request:reason:"
+ "isAbleToSend"
+ "messageWithResourceRequest:sender:reason:"
+ "optionsWithDefaultStride:supportedStrides:setupSupported:baseMSGSyncID:availability:"
+ "reason"
+ "requestResourcesWithStrides:failedReason:"
+ "resource unavailable"
+ "resourceRequestsFailed:reason:"
+ "resourceRequestsFailedReason"
+ "setAvailability:"
+ "setCanDeRegisterSelf:"
+ "setCanSend:"
+ "setDeregisterSemaphore:"
+ "setResourceRequestsFailedReason:"
+ "unknown"
+ "v24@0:8^{?={pssg_tx_s={?={?=IIIIIi}{?=I}(?={?=IIb16b8b8}{?=^vb8b8b8b8I}{?=^vb8b8b8b8I}{?=IIb24b8}{?=Qb16b8b8I})}Q[256c](?={?=QQQQ}{?=i}{?=^v})}{?=II}}16"
+ "v32@0:8@16Q24"
+ "{?=\"message\"{pssg_tx_s=\"header\"{?=\"header\"{?=\"msgh_bits\"I\"msgh_size\"I\"msgh_remote_port\"I\"msgh_local_port\"I\"msgh_voucher_port\"I\"msgh_id\"i}\"body\"{?=\"msgh_descriptor_count\"I}\"ool_port_data\"(?=\"port\"{?=\"name\"I\"pad1\"I\"pad2\"b16\"disposition\"b8\"type\"b8}\"out_of_line\"{?=\"address\"^v\"deallocate\"b8\"copy\"b8\"pad1\"b8\"type\"b8\"size\"I}\"ool_ports\"{?=\"address\"^v\"deallocate\"b8\"copy\"b8\"disposition\"b8\"type\"b8\"count\"I}\"type\"{?=\"pad1\"I\"pad2\"I\"pad3\"b24\"type\"b8}\"guarded_port\"{?=\"context\"Q\"flags\"b16\"disposition\"b8\"type\"b8\"name\"I})}\"type\"Q\"string1\"[256c]\"\"(?=\"\"{?=\"countArray1\"Q\"countArray2\"Q\"dataLength\"Q\"uint1\"Q}\"\"{?=\"pid\"i}\"\"{?=\"notifications\"^v})}\"pid\"i\"oolDataLength\"I\"\"(?=\"oolData\"^v\"strings\"^[256c]\"streamsWithStrides\"^{pssg_stream_entry_s}\"streamRequest\"^{pssg_stream_request_s}\"streamAvailability\"^{pssg_stream_availability_entry_s})}"
+ "\xf0\xf0\xf0$"
- "\""
- "@24@0:8^{pssg_tx_s={?={?=IIIIIi}{?=I}(?={?=IIb16b8b8}{?=^vb8b8b8b8I}{?=^vb8b8b8b8I}{?=IIb24b8}{?=Qb16b8b8I})}Q[256c](?={?=QQQ}{?=i}{?=^v})}16"
- "@40@0:8I16@20B28@32"
- "A"
- "^{?={pssg_tx_s={?={?=IIIIIi}{?=I}(?={?=IIb16b8b8}{?=^vb8b8b8b8I}{?=^vb8b8b8b8I}{?=IIb24b8}{?=Qb16b8b8I})}Q[256c](?={?=QQQ}{?=i}{?=^v})}iI(?=^v^[256c]^{pssg_stream_entry_s}^{pssg_stream_request_s}^{pssg_stream_availability_entry_s})}16@0:8"
- "initWithDefaultStride:supportedStrides:setupSupported:baseMSGSyncID:"
- "optionsWithDefaultStride:supportedStrides:setupSupported:baseMSGSyncID:"
- "requestResourcesWithStrides:"
- "resourceRequestsFailed:"
- "v24@0:8^{?={pssg_tx_s={?={?=IIIIIi}{?=I}(?={?=IIb16b8b8}{?=^vb8b8b8b8I}{?=^vb8b8b8b8I}{?=IIb24b8}{?=Qb16b8b8I})}Q[256c](?={?=QQQ}{?=i}{?=^v})}{?=II}}16"
- "{?=\"message\"{pssg_tx_s=\"header\"{?=\"header\"{?=\"msgh_bits\"I\"msgh_size\"I\"msgh_remote_port\"I\"msgh_local_port\"I\"msgh_voucher_port\"I\"msgh_id\"i}\"body\"{?=\"msgh_descriptor_count\"I}\"ool_port_data\"(?=\"port\"{?=\"name\"I\"pad1\"I\"pad2\"b16\"disposition\"b8\"type\"b8}\"out_of_line\"{?=\"address\"^v\"deallocate\"b8\"copy\"b8\"pad1\"b8\"type\"b8\"size\"I}\"ool_ports\"{?=\"address\"^v\"deallocate\"b8\"copy\"b8\"disposition\"b8\"type\"b8\"count\"I}\"type\"{?=\"pad1\"I\"pad2\"I\"pad3\"b24\"type\"b8}\"guarded_port\"{?=\"context\"Q\"flags\"b16\"disposition\"b8\"type\"b8\"name\"I})}\"type\"Q\"string1\"[256c]\"\"(?=\"\"{?=\"countArray1\"Q\"countArray2\"Q\"dataLength\"Q}\"\"{?=\"pid\"i}\"\"{?=\"notifications\"^v})}\"pid\"i\"oolDataLength\"I\"\"(?=\"oolData\"^v\"strings\"^[256c]\"streamsWithStrides\"^{pssg_stream_entry_s}\"streamRequest\"^{pssg_stream_request_s}\"streamAvailability\"^{pssg_stream_availability_entry_s})}"

```
