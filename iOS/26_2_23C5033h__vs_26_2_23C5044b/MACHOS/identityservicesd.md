## identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

-1968.300.22.0.0
-  __TEXT.__text: 0x93f258
+1968.300.31.0.0
+  __TEXT.__text: 0x93fb3c
   __TEXT.__auth_stubs: 0x5ba0
-  __TEXT.__objc_stubs: 0x46a00
-  __TEXT.__objc_methlist: 0x297dc
-  __TEXT.__const: 0x64e90
-  __TEXT.__gcc_except_tab: 0x29ea4
-  __TEXT.__objc_methname: 0x73692
-  __TEXT.__cstring: 0x59bd7
-  __TEXT.__oslogstring: 0x7b3bb
-  __TEXT.__objc_classname: 0x4410
-  __TEXT.__objc_methtype: 0x1247f
+  __TEXT.__objc_stubs: 0x46c20
+  __TEXT.__objc_methlist: 0x298cc
+  __TEXT.__const: 0x64ef0
+  __TEXT.__gcc_except_tab: 0x29ddc
+  __TEXT.__objc_methname: 0x737f0
+  __TEXT.__cstring: 0x59ac7
+  __TEXT.__oslogstring: 0x7b2db
+  __TEXT.__objc_classname: 0x440c
+  __TEXT.__objc_methtype: 0x124cd
   __TEXT.__ustring: 0x4ca
   __TEXT.__dlopen_cstrs: 0xea
-  __TEXT.__swift5_typeref: 0x6088
-  __TEXT.__swift5_capture: 0x1358
-  __TEXT.__constg_swiftt: 0x5310
-  __TEXT.__swift5_reflstr: 0x5084
-  __TEXT.__swift5_fieldmd: 0x5390
-  __TEXT.__swift5_builtin: 0xb4
+  __TEXT.__swift5_typeref: 0x60b2
+  __TEXT.__swift5_capture: 0x136c
+  __TEXT.__constg_swiftt: 0x53dc
+  __TEXT.__swift5_reflstr: 0x50f4
+  __TEXT.__swift5_fieldmd: 0x53dc
+  __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_proto: 0x9b8
-  __TEXT.__swift5_types: 0x4d4
+  __TEXT.__swift5_types: 0x4dc
   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift5_assocty: 0xfc0
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x122d0
+  __TEXT.__unwind_info: 0x12330
   __TEXT.__eh_frame: 0x9ae4
   __DATA_CONST.__auth_got: 0x2de0
-  __DATA_CONST.__got: 0x38c8
-  __DATA_CONST.__auth_ptr: 0x7b0
-  __DATA_CONST.__const: 0x2e018
-  __DATA_CONST.__cfstring: 0x34a40
-  __DATA_CONST.__objc_classlist: 0x1128
+  __DATA_CONST.__got: 0x38b8
+  __DATA_CONST.__auth_ptr: 0x7a8
+  __DATA_CONST.__const: 0x2e068
+  __DATA_CONST.__cfstring: 0x34900
+  __DATA_CONST.__objc_classlist: 0x1130
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x760
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x482b0
-  __DATA.__objc_selrefs: 0x15eb8
-  __DATA.__objc_ivar: 0x32d4
-  __DATA.__objc_data: 0xd638
-  __DATA.__data: 0xebe0
+  __DATA.__objc_const: 0x483a0
+  __DATA.__objc_selrefs: 0x15f48
+  __DATA.__objc_ivar: 0x32b0
+  __DATA.__objc_data: 0xd788
+  __DATA.__data: 0xec30
   __DATA.__bss: 0x17158
-  __DATA.__common: 0xf30
+  __DATA.__common: 0xf38
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 54CD0FA1-BDC4-359A-A544-8A03600EC361
-  Functions: 25393
+  UUID: 1804835B-0906-36FB-965F-D0F4CC998CB8
+  Functions: 25439
   Symbols:   2753
   CStrings:  41611
 
Symbols:
+ _OBJC_CLASS_$_IDSDeliveryPipelineMetricContext
+ _OBJC_METACLASS_$_IDSDeliveryPipelineMetricContext
+ _nw_connection_create_with_connected_socket
- __dispatch_source_type_read
- __dispatch_source_type_write
- _dispatch_suspend
CStrings:
+ ")*"
+ ", appliedEnforcment: "
+ ", enforcementCode: "
+ ", enforcementMetricType: "
+ "22:03:26"
+ "<DeliveryPipelineMetricContext ckv {optIn: "
+ "@\"IDSDeliveryPipelineMetricContext\""
+ "@\"IDSDeliveryPipelineMetricContext\"16@0:8"
+ "IDSDeliveryControllerPipelineMetricContextKey"
+ "IDSDeliveryPipelineMetricContext"
+ "IDSDirectDataPathSocket: (%d, %p) network nw_connection state: %d"
+ "IDSDirectDataPathSocket: (%d, %p) pipe nw_connection state: %d"
+ "IDSDirectDataPathSocket: failed to start network nw_connection:(%d, %p), state: %d error: %@"
+ "IDSDirectDataPathSocket: failed to start pipe nw_connection:(%d, %p), state: %d error: %@"
+ "IDSDirectDataPathSocket: network nw_connection ready: (%d, %p) connection_time: %fs"
+ "IDSDirectDataPathSocket: pipe nw_connection ready: (%d, %p) connection_time: %fs"
+ "IDSDirectDataPathSocket:readFromDatagramNWConnection error (%@) is_complete (%@) nw_connection (%p)"
+ "IDSDirectDataPathSocket:readFromDatagramNWConnection received data (%lu) bytes on nw_connection (%p)"
+ "IDSDirectDataPathSocket:readFromDatagramPipe error (%@) is_complete (%@) nw_connection (%p)"
+ "IDSDirectDataPathSocket:readFromDatagramPipe received data (%lu) bytes on nw_connection (%p)"
+ "IDSDirectDataPathSocket:readFromStreamNWConnection error (%@) is_complete (%@) nw_connection (%p)"
+ "IDSDirectDataPathSocket:readFromStreamNWConnection received data (%lu) bytes on nw_connection (%p)"
+ "IDSDirectDataPathSocket:readFromStreamPipe error (%@) is_complete (%@) nw_connection (%p)"
+ "IDSDirectDataPathSocket:readFromStreamPipe received data (%lu) bytes on nw_connection (%p)"
+ "IDSDirectDataPathSocket:shutdownSocketInternal (%d, %p, %p)"
+ "IDSDirectDataPathSocket:startIfBothReady (%d, %p, %p)"
+ "IDSDirectDataPathSocket:startSocket: failed to get pipe connection"
+ "IDSDirectDataPathSocket:writeDataToNWConnection failed send on nw_connection (%p) with fatal error"
+ "IDSDirectDataPathSocket:writeDataToPipe failed send on nw_connection (%p) with fatal error"
+ "Logged message send response metric: responseCode=%ld service=%@ command=%@ hasDataToEncrypt=%@ messageGUID=%@ metricContext=%@"
+ "Nov 12 2025"
+ "T@\"IDSDeliveryPipelineMetricContext\",&,N,V_metricContext"
+ "TB,N,VckvAppliedEnforcment"
+ "TB,N,VckvOptedIn"
+ "Tq,N,VckvEnforcementCode"
+ "Tq,N,VckvEnforcementMetricType"
+ "_isNwConnectionReady"
+ "_isPipeConnectionReady"
+ "_isServiceConnectorConnection"
+ "_isShutdownCalled"
+ "_isStreamSocket"
+ "_metricContext"
+ "_pipeConnection"
+ "ckvAppliedEnforcment"
+ "ckvEnforcementCode"
+ "ckvEnforcementMetricType"
+ "ckvOptedIn"
+ "initWithResponseCode:service:command:hasDataToEncrypt:messageType:ckvOptedIn:ckvAppliedEnforcment:ckvEnforcementMetricType:ckvEnforcementCode:"
+ "initWithTransparencyDaemon:delegate:queryID:coreAnalyticsLogger:queue:"
+ "metricContext"
+ "metricInfo"
+ "readFromDatagramNWConnection"
+ "readFromDatagramPipe"
+ "readFromPipe"
+ "readFromStreamNWConnection"
+ "readFromStreamPipe"
+ "sendCompletionFailure"
+ "setCkvAppliedEnforcment:"
+ "setCkvEnforcementCode:"
+ "setCkvEnforcementMetricType:"
+ "setCkvOptedIn:"
+ "setMetricContext:"
+ "setMetricInfo:"
+ "shutdownSocketInternal"
+ "startIfBothReady"
+ "startSocketInternal:"
+ "v32@?0@\"NSArray\"8@\"NSArray\"16@\"IDSDeliveryPipelineMetricContext\"24"
+ "writeDataToNWConnection:"
+ "writeDataToPipe:"
- "))"
- "23:03:47"
- "IDSDaemon_directDataPathSocketQueue"
- "IDSDirectDataPathSocket:  (%d, %p) writeMessageToSocket failed, cleaning up"
- "IDSDirectDataPathSocket: (%d, %p) connection state: %d"
- "IDSDirectDataPathSocket: (%d, %p) nw_connection_send sent data: %u bytes"
- "IDSDirectDataPathSocket: (%d, %p) resetting _canSendOverNWConnection to yes"
- "IDSDirectDataPathSocket: (%d, %p) sending: %u bytes"
- "IDSDirectDataPathSocket: (%d, %p) writeMessageToNWConnection nw_connection busy, retrying.."
- "IDSDirectDataPathSocket: (%d, %p) writeMessageToNWConnection recv failed, cleaning up"
- "IDSDirectDataPathSocket: (%d, %p) writeMessageToNWConnection recv failed, retrying..."
- "IDSDirectDataPathSocket: (%d, %p) writeMessageToNWConnection recv failed, socket closed"
- "IDSDirectDataPathSocket: (%d, %p) writeMessageToSocket sentSize is 0!"
- "IDSDirectDataPathSocket: (%d, %p) writeToNWConnection recv failed, cleaning up"
- "IDSDirectDataPathSocket: (%d, %p) writeToNWConnection recv failed, retrying..."
- "IDSDirectDataPathSocket: (%d, %p) writeToNWConnection recv failed, socket closed"
- "IDSDirectDataPathSocket: (%d, %p) writeToSocket failed, cleaning up"
- "IDSDirectDataPathSocket: (%d, %p) writeToSocket sentSize is 0!"
- "IDSDirectDataPathSocket: failed to start connection:(%d, %p), connection state: %d error: %@"
- "IDSDirectDataPathSocket: nw connection ready: (%d, %p) connection_time: %fs"
- "IDSDirectDataPathSocket: writeToSocket invalid sd"
- "IDSDirectDataPathSocket:readFromNWConnection received data (%lu) bytes on nw_connection (%p)"
- "IDSDirectDataPathSocket:shutdownSocket (%d, %p)"
- "IDSDirectDataPathSocket:writeMessageToNWConnection failed send on nw_connection (%p) with fatal error"
- "IDSDirectDataPathSocket:writeMessageToNWConnection invalid sd"
- "IDSDirectDataPathSocket:writeMessageToSocket invalid sd"
- "IDSDirectDataPathSocket:writeToNWConnection failed send on nw_connection (%p) with fatal error"
- "IDSDirectDataPathSocket:writeToNWConnection invalid sd"
- "Logged message send response metric: responseCode=%ld service=%@ command=%@ hasDataToEncrypt=%@ messageGUID=%@"
- "Nov  2 2025"
- "_canSendOverNWConnection"
- "_completionSent"
- "_incomingNWData"
- "_incomingNWMessages"
- "_outgoingNWData"
- "_outgoingNWMessages"
- "_readFromSocketSource"
- "_readSourceSuspended"
- "_serviceConnectorConnection"
- "_shutdownCalled"
- "_socket"
- "_socketQueue"
- "_streamSocket"
- "_writeSourceSuspended"
- "_writeToSocketSource"
- "initWithResponseCode:service:command:hasDataToEncrypt:messageType:"
- "initWithTransparencyDaemon:delegate:queryID:coreAnalyticsLogger:"
- "readMessageFromNWConnection"
- "writeMessageToNWConnection"
- "writeMessageToSocket"
- "writeToNWConnection"
- "writeToSocket"

```
