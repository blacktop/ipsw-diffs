## RemoteCoreML

> `/System/Library/PrivateFrameworks/RemoteCoreML.framework/RemoteCoreML`

```diff

 2.0.0.0.0
-  __TEXT.__text: 0x5c28
-  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__text: 0x53f0
   __TEXT.__objc_methlist: 0x61c
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x367
+  __TEXT.__cstring: 0x372
   __TEXT.__oslogstring: 0x425
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__unwind_info: 0x1f0
-  __TEXT.__objc_classname: 0xa5
-  __TEXT.__objc_methname: 0xcd0
-  __TEXT.__objc_methtype: 0x28b
-  __TEXT.__objc_stubs: 0xd20
-  __DATA_CONST.__got: 0x98
+  __TEXT.__unwind_info: 0x1b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x270
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x410
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x2f0
+  __DATA_CONST.__got: 0x98
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x200
   __AUTH_CONST.__objc_const: 0xb00
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x78
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B6444CC7-A310-33C3-9E6D-9EA1B6043B76
-  Functions: 194
-  Symbols:   750
-  CStrings:  322
+  UUID: 25F60476-CDC3-3FF7-82D3-95BD4D6D3231
+  Functions: 191
+  Symbols:   755
+  CStrings:  94
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _OUTLINED_FUNCTION_6
- _objc_retainAutoreleasedReturnValue
CStrings:
- ".cxx_destruct"
- "@\"NSMutableData\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSObject<OS_nw_connection>\""
- "@\"NSObject<OS_nw_listener>\""
- "@\"NSObject<OS_nw_parameters>\""
- "@\"NSObject<OS_nw_protocol_stack>\""
- "@\"NSObject<OS_os_log>\""
- "@\"_MLNetworkOptions\""
- "@\"_MLNetworkPacket\""
- "@\"_MLNetworking\""
- "@16@0:8"
- "@24@0:8@16"
- "@28@0:8@?16B24"
- "@32@0:8@16Q24"
- "@32@0:8q16@24"
- "@?"
- "@?16@0:8"
- "@?24@0:8@16"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B40@0:8@16@24^@32"
- "B56@0:8@16@24@32@40^@48"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "T@\"NSMutableData\",&,N,V_buffer"
- "T@\"NSMutableData\",&,N,V_doubleBuffer"
- "T@\"NSMutableData\",&,N,V_outputResult"
- "T@\"NSMutableDictionary\",R,N,V_networkOptions"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_q"
- "T@\"NSObject<OS_dispatch_semaphore>\",R,N,V_semaphore"
- "T@\"NSObject<OS_nw_connection>\",&,N,V_connection"
- "T@\"NSObject<OS_nw_connection>\",R,N,V_connection"
- "T@\"NSObject<OS_nw_listener>\",R,N,V_listener"
- "T@\"NSObject<OS_nw_parameters>\",R,N,V_parameters"
- "T@\"NSObject<OS_nw_protocol_stack>\",R,N,V_protocol_stack"
- "T@\"NSObject<OS_os_log>\",R,N,V_logType"
- "T@\"_MLNetworkOptions\",R,N,V_nwOptions"
- "T@\"_MLNetworkPacket\",R,N,V_packet"
- "T@\"_MLNetworking\",R,N,V_nwObj"
- "T@?,C,N,V_loadFunction"
- "T@?,C,N,V_predictFunction"
- "T@?,C,N,V_textFunction"
- "T@?,C,N,V_unLoadFunction"
- "TB,R,N,V_isClient"
- "TQ,N,V_command"
- "TQ,N,V_sizeOfPacket"
- "TQ,R,N,V_jobCount"
- "Tq,R,N,V_receiveTimeout"
- "UTF8String"
- "^v24@0:8@16"
- "_MLLog"
- "_MLNetworkHeaderEncoding"
- "_MLNetworkOptions"
- "_MLNetworkPacket"
- "_MLNetworkUtilities"
- "_MLNetworking"
- "_MLRemoteConnection"
- "_MLRemoteCoreMLErrors"
- "_MLServer"
- "_buffer"
- "_command"
- "_connection"
- "_doubleBuffer"
- "_isClient"
- "_jobCount"
- "_listener"
- "_loadFunction"
- "_logType"
- "_networkOptions"
- "_nwObj"
- "_nwOptions"
- "_outputResult"
- "_packet"
- "_parameters"
- "_predictFunction"
- "_protocol_stack"
- "_q"
- "_receiveTimeout"
- "_semaphore"
- "_sizeOfPacket"
- "_textFunction"
- "_unLoadFunction"
- "acknowledgeFailData"
- "acknowledgeSucessData"
- "appendBytes:length:"
- "appendData:"
- "bindEndPoints:localAddr:localPort:"
- "boolValue"
- "buffer"
- "bytes"
- "cleanupDoubleBuffer"
- "clientFramework"
- "clientTimeoutErrorForMethod:"
- "command"
- "common"
- "configureTLS:"
- "connection"
- "constructDataPacket:HeaderEncoding:"
- "countByEnumeratingWithState:objects:count:"
- "createErrorWithCode:description:"
- "createSecureConnectionParameter:useUDP:"
- "custom:"
- "daemon"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dictionaryWithObjects:forKeys:count:"
- "doInitNetwork:"
- "doReceive:context:isComplete:error:"
- "doubleBuffer"
- "errorWithDomain:code:userInfo:"
- "family"
- "getHeaderDataSize:"
- "getHeaderDataStart:"
- "getHeaderEncoding:"
- "getHeaderEnd:"
- "getHeaderSize"
- "init"
- "initConnection:"
- "initListener:"
- "initWithBytes:length:"
- "initWithData:"
- "initWithOptions:"
- "isClient"
- "isEqualToString:"
- "isHeaderAcknowledgeFailData:"
- "isHeaderAcknowledgeSucessData:"
- "isHeaderCustom:"
- "isHeaderError:"
- "isHeaderIncomingData:"
- "isHeaderLoad:"
- "isHeaderPredictFeature:"
- "isHeaderText:"
- "isHeaderUnLoad:"
- "jobCount"
- "length"
- "listener"
- "loadFromURL:options:error:"
- "loadFunction"
- "loadModel:"
- "localAddr"
- "localPort"
- "logType"
- "mutableCopy"
- "networkNameIdentifier"
- "networkOptions"
- "nwObj"
- "nwOptions"
- "objectForKeyedSubscript:"
- "outputResult"
- "packet"
- "parameters"
- "path"
- "port"
- "predictFeature:"
- "predictFunction"
- "predictionFromURL:features:output:options:error:"
- "protocol_stack"
- "psk"
- "q"
- "q16@0:8"
- "r*16@0:8"
- "receiveLoop:"
- "receiveTimeout"
- "receiveTimeoutValue"
- "reset"
- "resetDoubleBuffer"
- "resetMetadata"
- "restartConnection"
- "semaphore"
- "send:options:"
- "sendData:"
- "sendDataAndWaitForAcknowledgementOrTimeout:"
- "serverFramework"
- "setAWDL:useAWDL:"
- "setBuffer:"
- "setCommand:"
- "setConnection:"
- "setDoubleBuffer:"
- "setLength:"
- "setListenerReceiveDataCallBack:"
- "setLoadCommand:"
- "setLoadFunction:"
- "setObject:forKeyedSubscript:"
- "setOutputResult:"
- "setPredictCommand:"
- "setPredictFunction:"
- "setProtocolStack:family:"
- "setReceiveDataCallBack:"
- "setSizeOfPacket:"
- "setTextCommand:"
- "setTextFunction:"
- "setUnLoadCommand:"
- "setUnLoadFunction:"
- "setupBonjour:name:useBonjour:useUDP:"
- "setupListenerStateChangeHandler:useUDP:"
- "sizeOfPacket"
- "start"
- "startConnection"
- "stop"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "textDebug:"
- "textFunction"
- "tool"
- "unLoadFunction"
- "unLoadModel:"
- "unloadFromURL:options:error:"
- "unsignedIntegerValue"
- "useAWDL"
- "useBonjour"
- "useTLS"
- "useUDP"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v28@0:8@16B24"
- "v32@0:8@16@24"
- "v40@0:8@16r*24B32B36"
- "v40@0:8@16r*24r*32"
- "v44@0:8@16@24B32@36"

```
