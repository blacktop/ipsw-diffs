## MobileMulticastTransfer

> `/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer`

```diff

-153.80.10.0.0
-  __TEXT.__text: 0x2e5a4
-  __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_methlist: 0x1580
-  __TEXT.__const: 0x4908
-  __TEXT.__cstring: 0xe9b
-  __TEXT.__oslogstring: 0x38cc
-  __TEXT.__gcc_except_tab: 0x6d0
-  __TEXT.__unwind_info: 0xd00
-  __TEXT.__objc_classname: 0x31a
-  __TEXT.__objc_methname: 0x3787
-  __TEXT.__objc_methtype: 0x1517
-  __TEXT.__objc_stubs: 0x2a80
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__const: 0x868
-  __DATA_CONST.__objc_classlist: 0x98
+176.100.32.0.0
+  __TEXT.__text: 0x36a18
+  __TEXT.__auth_stubs: 0xc20
+  __TEXT.__objc_methlist: 0x1620
+  __TEXT.__const: 0x4930
+  __TEXT.__cstring: 0xfd0
+  __TEXT.__oslogstring: 0x4d30
+  __TEXT.__gcc_except_tab: 0x884
+  __TEXT.__unwind_info: 0xe48
+  __TEXT.__objc_classname: 0x332
+  __TEXT.__objc_methname: 0x3c2c
+  __TEXT.__objc_methtype: 0x159e
+  __TEXT.__objc_stubs: 0x2da0
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__const: 0x908
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd20
+  __DATA_CONST.__objc_selrefs: 0xe20
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x650
-  __AUTH_CONST.__const: 0x2360
-  __AUTH_CONST.__cfstring: 0x9a0
-  __AUTH_CONST.__objc_const: 0x4980
-  __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x274
+  __AUTH_CONST.__auth_got: 0x620
+  __AUTH_CONST.__const: 0x2ec0
+  __AUTH_CONST.__cfstring: 0xae0
+  __AUTH_CONST.__objc_const: 0x4be8
+  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__objc_doubleobj: 0x20
+  __AUTH.__objc_data: 0x640
+  __DATA.__objc_ivar: 0x2a0
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x38
   __DATA.__common: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 195DDBDC-AB81-3A2C-AC41-CC229D9C4413
-  Functions: 1278
-  Symbols:   4497
-  CStrings:  1308
+  UUID: 9CFA762D-89D8-3C68-8B13-132FD9A8AF88
+  Functions: 1509
+  Symbols:   5339
+  CStrings:  1477
 
Symbols:
+ -[MIBUEncodedFileInfo .cxx_destruct]
+ -[MIBUEncodedFileInfo fileHandle]
+ -[MIBUEncodedFileInfo fileNumber]
+ -[MIBUEncodedFileInfo setFileHandle:]
+ -[MIBUEncodedFileInfo setFileNumber:]
+ -[MIBUEncodedFileInfo setSourceBlockNumber:]
+ -[MIBUEncodedFileInfo sourceBlockNumber]
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.1
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.2
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.3
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.4
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.5
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.6
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.7
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.8
+ -[MIBUNWClientController _createNANTCPConnectionUsingInterface:].cold.4
+ -[MIBUNWClientController _disableFirewall].cold.4
+ -[MIBUNWClientController _handlePacketConsumerCompletion].cold.2
+ -[MIBUNWClientController _pingThroughMulticast:]
+ -[MIBUNWClientController _pingThroughMulticast:].cold.1
+ -[MIBUNWClientController _receivedVeryFirstPacketArray].cold.2
+ -[MIBUNWClientController _startMulticastReceiverUsingInterface:].cold.4
+ -[MIBUNWClientController _stopMulticastReceiver].cold.2
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:].cold.1
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:].cold.2
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:].cold.3
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:].cold.4
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:].cold.5
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:].cold.6
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:].cold.7
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:].cold.8
+ -[MIBUNWClientController multicastSocketDidStop:withError:].cold.2
+ -[MIBUNWClientController multicastSocketDidStop:withError:].cold.3
+ -[MIBUNWClientController multicastSocketDidStop:withError:].cold.4
+ -[MIBUNWClientController nanSubscriber:didReceiveData:].cold.1
+ -[MIBUNWClientController nanSubscriber:didReceiveData:].cold.2
+ -[MIBUNWClientController nanSubscriberDetectedMulticastError:].cold.1
+ -[MIBUNWClientController nanSubscriberDetectedMulticastError:].cold.2
+ -[MIBUNWClientController nanSubscriberDidStart:withPeerIPAddress:usingInterface:forRetry:].cold.1
+ -[MIBUNWClientController nanSubscriberDidStop:withError:willRetry:].cold.1
+ -[MIBUNWClientController nanSubscriberDidTerminateDataSession:].cold.1
+ -[MIBUNWClientController pingThroughMulticast:].cold.2
+ -[MIBUNWClientController stopMulticast].cold.1
+ -[MIBUNWClientController stopMulticast].cold.2
+ -[MIBUNWClientController stopMulticast].cold.3
+ -[MIBUNWServerController _handleFetchCompletionWithResult:atEOF:packets:].cold.3
+ -[MIBUNWServerController _handleFetchCompletionWithResult:atEOF:packets:].cold.4
+ -[MIBUNWServerController _handleFetchCompletionWithResult:atEOF:packets:].cold.5
+ -[MIBUNWServerController _setupFileSenderLoop].cold.2
+ -[MIBUNWServerController _startMulticastUsingInterface:]
+ -[MIBUNWServerController _startMulticastUsingInterface:].cold.1
+ -[MIBUNWServerController _startMulticastUsingInterface:].cold.2
+ -[MIBUNWServerController _startMulticastUsingInterface:].cold.3
+ -[MIBUNWServerController _startMulticastUsingInterface:].cold.4
+ -[MIBUNWServerController _startMulticastUsingInterface:].cold.5
+ -[MIBUNWServerController _startMulticastUsingInterface:].cold.6
+ -[MIBUNWServerController _stopWithReason:].cold.10
+ -[MIBUNWServerController _stopWithReason:].cold.2
+ -[MIBUNWServerController _stopWithReason:].cold.3
+ -[MIBUNWServerController _stopWithReason:].cold.4
+ -[MIBUNWServerController _stopWithReason:].cold.5
+ -[MIBUNWServerController _stopWithReason:].cold.6
+ -[MIBUNWServerController _stopWithReason:].cold.7
+ -[MIBUNWServerController _stopWithReason:].cold.8
+ -[MIBUNWServerController _stopWithReason:].cold.9
+ -[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:]
+ -[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:].cold.1
+ -[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:].cold.2
+ -[MIBUNWServerController multicastSocketDidStart:].cold.1
+ -[MIBUNWServerController multicastSocketDidStop:withError:].cold.1
+ -[MIBUNWServerController multicastSocketDidStop:withError:].cold.2
+ -[MIBUNWServerController multicastSocketDidStop:withError:].cold.3
+ -[MIBUNWServerController nanPublisher:didCreateDataSessionWithPeer:usingInterface:].cold.1
+ -[MIBUNWServerController nanPublisher:didDestoryDataSessionWithPeer:].cold.1
+ -[MIBUNWServerController nanPublisherDidStart:usingInterface:forRetry:]
+ -[MIBUNWServerDevice _checkOutWithError:withSummary:]
+ -[MIBUNWServerDevice checkOutWithError:withSummary:].cold.1
+ -[MIBUNWServerDevice checkOutWithError:withSummary:].cold.2
+ -[MIBUNWServerDevice checkOutWithError:withSummary:].cold.3
+ -[MIBUNWServerDevice checkOutWithError:withSummary:].cold.4
+ -[MIBUNWServerDevice checkOutWithError:withSummary:].cold.5
+ -[MIBURaptorQPacketConsumer _assembleWithCompletion:]
+ -[MIBURaptorQPacketConsumer _assembleWithCompletion:].cold.1
+ -[MIBURaptorQPacketConsumer _assembleWithCompletion:].cold.10
+ -[MIBURaptorQPacketConsumer _assembleWithCompletion:].cold.11
+ -[MIBURaptorQPacketConsumer _assembleWithCompletion:].cold.2
+ -[MIBURaptorQPacketConsumer _assembleWithCompletion:].cold.3
+ -[MIBURaptorQPacketConsumer _assembleWithCompletion:].cold.4
+ -[MIBURaptorQPacketConsumer _assembleWithCompletion:].cold.5
+ -[MIBURaptorQPacketConsumer _assembleWithCompletion:].cold.6
+ -[MIBURaptorQPacketConsumer _assembleWithCompletion:].cold.7
+ -[MIBURaptorQPacketConsumer _assembleWithCompletion:].cold.8
+ -[MIBURaptorQPacketConsumer _assembleWithCompletion:].cold.9
+ -[MIBURaptorQPacketConsumer _bootstrap].cold.5
+ -[MIBURaptorQPacketConsumer _bootstrap].cold.6
+ -[MIBURaptorQPacketConsumer _bootstrap].cold.7
+ -[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:].cold.10
+ -[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:].cold.11
+ -[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:].cold.12
+ -[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:].cold.13
+ -[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:].cold.4
+ -[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:].cold.5
+ -[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:].cold.6
+ -[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:].cold.7
+ -[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:].cold.8
+ -[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:].cold.9
+ -[MIBURaptorQPacketConsumer assembleWithCompletion:]
+ -[MIBURaptorQPacketConsumer initWithBasicParametersArray:extendedParametersArray:threshold:fileRanges:outputFiles:]
+ -[MIBURaptorQPacketConsumer initWithBasicParametersArray:extendedParametersArray:threshold:fileRanges:outputFiles:].cold.1
+ -[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]
+ -[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:].cold.1
+ -[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:].cold.10
+ -[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:].cold.11
+ -[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:].cold.2
+ -[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:].cold.3
+ -[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:].cold.4
+ -[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:].cold.5
+ -[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:].cold.6
+ -[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:].cold.7
+ -[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:].cold.8
+ -[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:].cold.9
+ -[MIBURaptorQPacketProvider _bootstrap].cold.7
+ -[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]
+ -[MIBURaptorQPacketProvider _splitInputFileIfNeeded:].cold.1
+ -[MIBURaptorQPacketProvider _splitInputFileIfNeeded:].cold.2
+ -[MIBURaptorQPacketProvider _splitInputFileIfNeeded:].cold.3
+ -[MIBURaptorQPacketProvider _splitInputFileIfNeeded:].cold.4
+ -[MIBURaptorQPacketProvider _splitInputFileIfNeeded:].cold.5
+ -[MIBURaptorQPacketProvider _splitInputFileIfNeeded:].cold.6
+ -[MIBURaptorQPacketProvider _splitInputFileIfNeeded:].cold.7
+ -[MIBURaptorQPacketProvider _splitInputFileIfNeeded:].cold.8
+ -[MIBURaptorQPacketProvider fileRangeTable]
+ -[MIBURaptorQPacketProvider initWithPayloadSize:repairFactor:inputFiles:]
+ -[MIBURaptorQPacketProvider initWithPayloadSize:repairFactor:inputFiles:].cold.1
+ -[MIBURaptorQPacketProvider initWithPayloadSize:repairFactor:inputFiles:].cold.2
+ -[MIBURaptorQPacketProvider rqBasicParametersArray]
+ -[MIBURaptorQPacketProvider rqExtendedParametersArray]
+ -[SKRaptorQDecoder fileSize]
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table33
+ GCC_except_table61
+ GCC_except_table8
+ _NSCocoaErrorDomain
+ _NSFileSize
+ _NSStringFromRange
+ _OBJC_CLASS_$_MIBUEncodedFileInfo
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$_WiFiAwareDeviceCapabilities
+ _OBJC_IVAR_$_MIBUEncodedFileInfo._fileHandle
+ _OBJC_IVAR_$_MIBUEncodedFileInfo._fileNumber
+ _OBJC_IVAR_$_MIBUEncodedFileInfo._sourceBlockNumber
+ _OBJC_IVAR_$_MIBURaptorQPacketConsumer._basicParametersArray
+ _OBJC_IVAR_$_MIBURaptorQPacketConsumer._extendedParametersArray
+ _OBJC_IVAR_$_MIBURaptorQPacketConsumer._fileCompletionStatus
+ _OBJC_IVAR_$_MIBURaptorQPacketConsumer._fileRanges
+ _OBJC_IVAR_$_MIBURaptorQPacketConsumer._multiFileMode
+ _OBJC_IVAR_$_MIBURaptorQPacketConsumer._outputFiles
+ _OBJC_IVAR_$_MIBURaptorQPacketConsumer._packetCountsPerFile
+ _OBJC_IVAR_$_MIBURaptorQPacketConsumer._partOutputFiles
+ _OBJC_IVAR_$_MIBURaptorQPacketConsumer._partOutputFilesSizes
+ _OBJC_IVAR_$_MIBURaptorQPacketConsumer._raptorQDecoders
+ _OBJC_IVAR_$_MIBURaptorQPacketProvider._encoderSummaries
+ _OBJC_IVAR_$_MIBURaptorQPacketProvider._fileRangeTable
+ _OBJC_IVAR_$_MIBURaptorQPacketProvider._inputFiles
+ _OBJC_IVAR_$_MIBURaptorQPacketProvider._rqBasicParametersArray
+ _OBJC_IVAR_$_MIBURaptorQPacketProvider._rqExtendedParametersArray
+ _OBJC_METACLASS_$_MIBUEncodedFileInfo
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ __OBJC_$_INSTANCE_METHODS_MIBUEncodedFileInfo
+ __OBJC_$_INSTANCE_VARIABLES_MIBUEncodedFileInfo
+ __OBJC_$_PROP_LIST_MIBUEncodedFileInfo
+ __OBJC_CLASS_RO_$_MIBUEncodedFileInfo
+ __OBJC_METACLASS_RO_$_MIBUEncodedFileInfo
+ ___115-[MIBURaptorQPacketConsumer initWithBasicParametersArray:extendedParametersArray:threshold:fileRanges:outputFiles:]_block_invoke
+ ___115-[MIBURaptorQPacketConsumer initWithBasicParametersArray:extendedParametersArray:threshold:fileRanges:outputFiles:]_block_invoke.cold.1
+ ___128-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke
+ ___128-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.57
+ ___128-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.57.cold.1
+ ___128-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.62
+ ___128-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.62.cold.1
+ ___128-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.67
+ ___128-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.67.cold.1
+ ___128-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.cold.1
+ ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke
+ ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.22
+ ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.22.cold.1
+ ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.25
+ ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.25.cold.1
+ ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.28
+ ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.28.cold.1
+ ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.32
+ ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.32.cold.1
+ ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.35
+ ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.35.cold.1
+ ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.39
+ ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.39.cold.1
+ ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.cold.1
+ ___189-[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:]_block_invoke
+ ___189-[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:]_block_invoke.5
+ ___189-[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:]_block_invoke.5.cold.1
+ ___189-[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:]_block_invoke.cold.1
+ ___34-[MIBUNWClientController progress]_block_invoke
+ ___35-[MIBUNANPublisher _startPublisher]_block_invoke.78
+ ___35-[MIBUNANPublisher _startPublisher]_block_invoke.78.cold.1
+ ___39-[MIBUNWClientController stopMulticast]_block_invoke.44
+ ___39-[MIBUNWClientController stopMulticast]_block_invoke.47
+ ___39-[MIBUNWClientController stopMulticast]_block_invoke.47.cold.1
+ ___39-[MIBUNWClientController stopMulticast]_block_invoke.cold.1
+ ___39-[MIBUNWClientController stopMulticast]_block_invoke_2
+ ___39-[MIBUNWClientController stopMulticast]_block_invoke_2.cold.1
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.13
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.13.cold.1
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.16
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.16.cold.1
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.21
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.21.cold.1
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.26
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.26.cold.1
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.29
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.29.cold.1
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.32
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.32.cold.1
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.39
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.39.cold.1
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.42
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.46
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.46.cold.1
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.51
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.51.cold.1
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.55
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.55.cold.1
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.58
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.58.cold.1
+ ___42-[MIBUNWClientController _disableFirewall]_block_invoke.173
+ ___42-[MIBUNWClientController _disableFirewall]_block_invoke.173.cold.1
+ ___42-[MIBUNWClientController _disableFirewall]_block_invoke.176
+ ___42-[MIBUNWClientController _disableFirewall]_block_invoke.176.cold.1
+ ___42-[MIBUNWServerController _startNANService]_block_invoke.67
+ ___42-[MIBUNWServerController _startNANService]_block_invoke.67.cold.1
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.17
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.17.cold.1
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.20
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.20.cold.1
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.23
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.23.cold.1
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.26
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.26.cold.1
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.29
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.29.cold.1
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.32
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.32.cold.1
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.35
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.35.cold.1
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.38
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.38.cold.1
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.41
+ ___42-[MIBUNWServerController _stopWithReason:]_block_invoke.41.cold.1
+ ___43-[MIBUNWServerController _startTCPListener]_block_invoke.57
+ ___43-[MIBUNWServerController _startTCPListener]_block_invoke.57.cold.1
+ ___43-[MIBUNWServerController _startTCPListener]_block_invoke.61
+ ___43-[MIBUNWServerController _startTCPListener]_block_invoke.61.cold.1
+ ___44-[MIBUNANPublisher _stopPublisherForReason:]_block_invoke.84
+ ___44-[MIBUNANPublisher _stopPublisherForReason:]_block_invoke.84.cold.1
+ ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.135
+ ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.135.cold.1
+ ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.138
+ ___45-[MIBUNWServerDevice _handleIncomingMessage:]_block_invoke.54
+ ___45-[MIBUNWServerDevice _handleIncomingMessage:]_block_invoke.54.cold.1
+ ___46-[MIBUNWServerController _setupFileSenderLoop]_block_invoke.101
+ ___46-[MIBUNWServerController _setupFileSenderLoop]_block_invoke.101.cold.1
+ ___46-[MIBUNWServerController _setupFileSenderLoop]_block_invoke.104
+ ___47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.52
+ ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke
+ ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke.116
+ ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke.116.cold.1
+ ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke.116.cold.2
+ ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke.cold.1
+ ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke_2
+ ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke_2.cold.1
+ ___48-[MIBUNWClientController _stopMulticastReceiver]_block_invoke.86
+ ___48-[MIBUNWClientController _stopMulticastReceiver]_block_invoke.86.cold.1
+ ___49-[MIBUNWServerController _tearDownFileSenderLoop]_block_invoke.107
+ ___49-[MIBUNWServerController _tearDownFileSenderLoop]_block_invoke.107.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.187
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.187.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.190
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.190.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.193
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.193.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.193.cold.2
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.193.cold.3
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.197
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.197.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.200
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.200.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.203
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.203.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.206
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.206.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.209
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.209.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.212
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.212.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.217
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.217.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.cold.5
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.cold.6
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.cold.7
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.cold.8
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.cold.9
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke_2.194
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke_2.194.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidConnect:]_block_invoke.167
+ ___49-[MIBUNWServerController clientDeviceDidConnect:]_block_invoke.167.cold.1
+ ___49-[MIBUNWServerController clientListenerDidStart:]_block_invoke.152
+ ___49-[MIBUNWServerController clientListenerDidStart:]_block_invoke.152.cold.1
+ ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.124
+ ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.124.cold.1
+ ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.124.cold.2
+ ___50-[MIBUNWServerController multicastSocketDidStart:]_block_invoke
+ ___50-[MIBUNWServerController multicastSocketDidStart:]_block_invoke.cold.1
+ ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.100
+ ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.100.cold.1
+ ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.103
+ ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.103.cold.1
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.172
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.172.cold.1
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.175
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.175.cold.1
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.175.cold.2
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.175.cold.3
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.179
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.179.cold.1
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.182
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.182.cold.1
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.cold.3
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke_2.176
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke_2.176.cold.1
+ ___52-[MIBUNWServerDevice checkOutWithError:withSummary:]_block_invoke
+ ___52-[MIBUNWServerDevice checkOutWithError:withSummary:]_block_invoke.29
+ ___52-[MIBUNWServerDevice checkOutWithError:withSummary:]_block_invoke.29.cold.1
+ ___52-[MIBUNWServerDevice checkOutWithError:withSummary:]_block_invoke.32
+ ___52-[MIBUNWServerDevice checkOutWithError:withSummary:]_block_invoke.32.cold.1
+ ___52-[MIBUNWServerDevice checkOutWithError:withSummary:]_block_invoke.cold.1
+ ___52-[MIBUNWServerDevice checkOutWithError:withSummary:]_block_invoke_2
+ ___52-[MIBUNWServerDevice checkOutWithError:withSummary:]_block_invoke_2.cold.1
+ ___52-[MIBURaptorQPacketConsumer assembleWithCompletion:]_block_invoke
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.102
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.102.cold.1
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.81
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.81.cold.1
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.84
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.84.cold.1
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.87
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.87.cold.1
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.90
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.90.cold.1
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.93
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.93.cold.1
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.96
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.96.cold.1
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.99
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.99.cold.1
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.cold.1
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.82
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.82.cold.1
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.85
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.85.cold.1
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.90
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.90.cold.1
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.93
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.93.cold.1
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.96
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.96.cold.1
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.cold.1
+ ___54-[MIBUNWServerController _calculateEffectiveBandwidth]_block_invoke.112
+ ___54-[MIBUNWServerController _calculateEffectiveBandwidth]_block_invoke.112.cold.1
+ ___55-[MIBUNWClientController _receivedVeryFirstPacketArray]_block_invoke.133
+ ___55-[MIBUNWClientController _receivedVeryFirstPacketArray]_block_invoke.133.cold.1
+ ___55-[MIBUNWClientController nanSubscriber:didReceiveData:]_block_invoke
+ ___55-[MIBUNWClientController nanSubscriber:didReceiveData:]_block_invoke.cold.1
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.141
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.141.cold.1
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.141.cold.2
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.142
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.142.cold.1
+ ___56-[MIBUNWServerController _startMulticastUsingInterface:]_block_invoke
+ ___56-[MIBUNWServerController _startMulticastUsingInterface:]_block_invoke.81
+ ___56-[MIBUNWServerController _startMulticastUsingInterface:]_block_invoke.81.cold.1
+ ___56-[MIBUNWServerController _startMulticastUsingInterface:]_block_invoke.84
+ ___56-[MIBUNWServerController _startMulticastUsingInterface:]_block_invoke.84.cold.1
+ ___56-[MIBUNWServerController _startMulticastUsingInterface:]_block_invoke.87
+ ___56-[MIBUNWServerController _startMulticastUsingInterface:]_block_invoke.87.cold.1
+ ___56-[MIBUNWServerController _startMulticastUsingInterface:]_block_invoke.91
+ ___56-[MIBUNWServerController _startMulticastUsingInterface:]_block_invoke.91.cold.1
+ ___56-[MIBUNWServerController _startMulticastUsingInterface:]_block_invoke.94
+ ___56-[MIBUNWServerController _startMulticastUsingInterface:]_block_invoke.94.cold.1
+ ___56-[MIBUNWServerController _startMulticastUsingInterface:]_block_invoke.cold.1
+ ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.107
+ ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.107.cold.1
+ ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.110
+ ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.110.cold.1
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.37
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.48
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.48.cold.1
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.51
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.55
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.55.cold.1
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.58
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.58.cold.1
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.67
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.67.cold.1
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.70
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.70.cold.1
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.73
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.73.cold.1
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.76
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.76.cold.1
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke_2
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke_2.52
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke_2.52.cold.1
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke_2.cold.1
+ ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.148
+ ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.148.cold.1
+ ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.151
+ ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.151.cold.1
+ ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.154
+ ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.93
+ ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.93.cold.1
+ ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.96
+ ___58-[MIBUNWServerController clientListenerDidStop:withError:]_block_invoke.157
+ ___58-[MIBUNWServerController clientListenerDidStop:withError:]_block_invoke.157.cold.1
+ ___59-[MIBUNWClientController multicastSocketDidStop:withError:]_block_invoke.191
+ ___59-[MIBUNWClientController multicastSocketDidStop:withError:]_block_invoke.191.cold.1
+ ___59-[MIBUNWClientController multicastSocketDidStop:withError:]_block_invoke.194
+ ___59-[MIBUNWClientController multicastSocketDidStop:withError:]_block_invoke.194.cold.1
+ ___59-[MIBUNWServerController multicastSocketDidStop:withError:]_block_invoke
+ ___59-[MIBUNWServerController multicastSocketDidStop:withError:]_block_invoke.246
+ ___59-[MIBUNWServerController multicastSocketDidStop:withError:]_block_invoke.246.cold.1
+ ___59-[MIBUNWServerController multicastSocketDidStop:withError:]_block_invoke.cold.1
+ ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.124
+ ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.124.cold.1
+ ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.127
+ ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.127.cold.1
+ ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.cold.2
+ ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.cold.3
+ ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.cold.4
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.64
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.64.cold.1
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.67
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.67.cold.1
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.70
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.70.cold.1
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.74
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.74.cold.1
+ ___62-[MIBUNWClientController nanSubscriberDetectedMulticastError:]_block_invoke
+ ___62-[MIBUNWClientController nanSubscriberDetectedMulticastError:]_block_invoke.cold.1
+ ___63-[MIBUNWClientController nanSubscriberDidTerminateDataSession:]_block_invoke.205
+ ___63-[MIBUNWClientController nanSubscriberDidTerminateDataSession:]_block_invoke.cold.1
+ ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.162
+ ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.162.cold.1
+ ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.165
+ ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.165.cold.1
+ ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.78
+ ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.78.cold.1
+ ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.81
+ ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.81.cold.1
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.92
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.92.cold.1
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.98
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.98.cold.1
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.98.cold.2
+ ___67-[MIBUNWClientController nanSubscriberDidStop:withError:willRetry:]_block_invoke.202
+ ___67-[MIBUNWClientController nanSubscriberDidStop:withError:willRetry:]_block_invoke.cold.1
+ ___67-[MIBUNWServerController clientListener:didReceiveNewClientDevice:]_block_invoke.162
+ ___67-[MIBUNWServerController clientListener:didReceiveNewClientDevice:]_block_invoke.162.cold.1
+ ___69-[MIBUNWServerController nanPublisher:didDestoryDataSessionWithPeer:]_block_invoke
+ ___69-[MIBUNWServerController nanPublisher:didDestoryDataSessionWithPeer:]_block_invoke.cold.1
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.107
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.107.cold.1
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.113
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.113.cold.1
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.113.cold.2
+ ___71-[MIBUNWServerController nanPublisherDidStart:usingInterface:forRetry:]_block_invoke
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.224
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.224.cold.1
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.228
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.228.cold.1
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.231
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.231.cold.1
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.234
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.234.cold.1
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.cold.3
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.cold.4
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke_2.225
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke_2.225.cold.1
+ ___73-[MIBUNWServerController _handleFetchCompletionWithResult:atEOF:packets:]_block_invoke.133
+ ___73-[MIBUNWServerController _handleFetchCompletionWithResult:atEOF:packets:]_block_invoke.133.cold.1
+ ___73-[MIBUNWServerController _handleFetchCompletionWithResult:atEOF:packets:]_block_invoke.136
+ ___73-[MIBUNWServerController _handleFetchCompletionWithResult:atEOF:packets:]_block_invoke.140
+ ___73-[MIBUNWServerController _handleFetchCompletionWithResult:atEOF:packets:]_block_invoke.140.cold.1
+ ___73-[MIBURaptorQPacketProvider initWithPayloadSize:repairFactor:inputFiles:]_block_invoke
+ ___73-[MIBURaptorQPacketProvider initWithPayloadSize:repairFactor:inputFiles:]_block_invoke.32
+ ___73-[MIBURaptorQPacketProvider initWithPayloadSize:repairFactor:inputFiles:]_block_invoke.32.cold.1
+ ___73-[MIBURaptorQPacketProvider initWithPayloadSize:repairFactor:inputFiles:]_block_invoke.cold.1
+ ___74-[MIBUNWServerController _adjustBatchSizeWithPacketDroppedInLastInterval:]_block_invoke.124
+ ___74-[MIBUNWServerController _adjustBatchSizeWithPacketDroppedInLastInterval:]_block_invoke.124.cold.1
+ ___83-[MIBUNWServerController nanPublisher:didCreateDataSessionWithPeer:usingInterface:]_block_invoke
+ ___83-[MIBUNWServerController nanPublisher:didCreateDataSessionWithPeer:usingInterface:]_block_invoke.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.124
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.124.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.130
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.130.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.136
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.136.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.139
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.139.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.145
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.145.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.148
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.148.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.151
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.151.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.154
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.154.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.cold.1
+ ___90-[MIBUNWClientController nanSubscriberDidStart:withPeerIPAddress:usingInterface:forRetry:]_block_invoke.199
+ ___90-[MIBUNWClientController nanSubscriberDidStart:withPeerIPAddress:usingInterface:forRetry:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32r_e47_B40?0"NSObject<OS_dispatch_data>"8Q16r^v24Q32lr32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e8_v12?0B8ls32l8s40l8
+ ___block_literal_global.100
+ ___block_literal_global.102
+ ___block_literal_global.103
+ ___block_literal_global.105
+ ___block_literal_global.112
+ ___block_literal_global.115
+ ___block_literal_global.122
+ ___block_literal_global.153
+ ___block_literal_global.159
+ ___block_literal_global.160
+ ___block_literal_global.164
+ ___block_literal_global.167
+ ___block_literal_global.174
+ ___block_literal_global.175
+ ___block_literal_global.178
+ ___block_literal_global.180
+ ___block_literal_global.181
+ ___block_literal_global.184
+ ___block_literal_global.186
+ ___block_literal_global.189
+ ___block_literal_global.192
+ ___block_literal_global.193
+ ___block_literal_global.196
+ ___block_literal_global.198
+ ___block_literal_global.199
+ ___block_literal_global.201
+ ___block_literal_global.202
+ ___block_literal_global.204
+ ___block_literal_global.205
+ ___block_literal_global.207
+ ___block_literal_global.208
+ ___block_literal_global.209
+ ___block_literal_global.211
+ ___block_literal_global.214
+ ___block_literal_global.219
+ ___block_literal_global.221
+ ___block_literal_global.227
+ ___block_literal_global.230
+ ___block_literal_global.233
+ ___block_literal_global.236
+ ___block_literal_global.241
+ ___block_literal_global.243
+ ___block_literal_global.245
+ ___block_literal_global.248
+ ___block_literal_global.250
+ ___block_literal_global.252
+ ___block_literal_global.255
+ ___block_literal_global.57
+ ___block_literal_global.58
+ ___block_literal_global.63
+ ___block_literal_global.85
+ ___block_literal_global.88
+ ___block_literal_global.92
+ ___block_literal_global.94
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ __os_log_debug_impl
+ _oalloc.cold.1
+ _objc_msgSend$_assembleWithCompletion:
+ _objc_msgSend$_checkOutWithError:withSummary:
+ _objc_msgSend$_pingThroughMulticast:
+ _objc_msgSend$_splitInputFileIfNeeded:
+ _objc_msgSend$_startMulticastUsingInterface:
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$appendData:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$assembleWithCompletion:
+ _objc_msgSend$boolValue
+ _objc_msgSend$currentDeviceCapabilities
+ _objc_msgSend$dataWithCapacity:
+ _objc_msgSend$discoveryInterfaceName
+ _objc_msgSend$doubleValue
+ _objc_msgSend$fileHandle
+ _objc_msgSend$fileHandleForReadingAtPath:
+ _objc_msgSend$fileHandleForWritingAtPath:
+ _objc_msgSend$fileNumber
+ _objc_msgSend$firstObject
+ _objc_msgSend$initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:
+ _objc_msgSend$nanPublisherDidStart:usingInterface:forRetry:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$rangeValue
+ _objc_msgSend$readDataOfLength:
+ _objc_msgSend$reassembleFileFromParts:toOutputFile:maxBytesToRead:error:
+ _objc_msgSend$setFileHandle:
+ _objc_msgSend$setFileNumber:
+ _objc_msgSend$setSourceBlockNumber:
+ _objc_msgSend$sourceBlockNumber
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$valueWithRange:
+ _objc_msgSend$writeData:
- -[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]
- -[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.1
- -[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.2
- -[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.3
- -[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.4
- -[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.5
- -[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.6
- -[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.7
- -[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.8
- -[MIBUNWClientController _checkOutWithError:]
- -[MIBUNWClientController _checkOutWithError:].cold.1
- -[MIBUNWClientController _checkOutWithError:].cold.2
- -[MIBUNWClientController _checkOutWithError:].cold.3
- -[MIBUNWClientController _checkOutWithError:].cold.4
- -[MIBUNWClientController _createTCPConnectionWithAddr:andPort:]
- -[MIBUNWClientController _createTCPConnectionWithAddr:andPort:].cold.1
- -[MIBUNWClientController _createTCPConnectionWithAddr:andPort:].cold.2
- -[MIBUNWClientController _createTCPConnectionWithAddr:andPort:].cold.3
- -[MIBUNWClientController checkOutWithError:]
- -[MIBUNWClientController initWithPacketConsumer:hostPort:tcpAddress:tcpPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]
- -[MIBUNWClientController setPingInterval:]
- -[MIBUNWClientController setPingInterval:].cold.1
- -[MIBUNWServerController _startMulticast]
- -[MIBUNWServerController _startMulticast].cold.1
- -[MIBUNWServerController _startMulticast].cold.2
- -[MIBUNWServerController _startMulticast].cold.3
- -[MIBUNWServerController _startMulticast].cold.4
- -[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:]
- -[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:].cold.1
- -[MIBUNWServerController nanPublisherDidStart:forRetry:]
- -[MIBURaptorQPacketConsumer _assemble]
- -[MIBURaptorQPacketConsumer _assemble].cold.1
- -[MIBURaptorQPacketConsumer assemble]
- -[MIBURaptorQPacketProvider initWithPayloadSize:repairFactor:inputFile:]
- -[MIBURaptorQPacketProvider initWithPayloadSize:repairFactor:inputFile:].cold.1
- GCC_except_table13
- GCC_except_table18
- GCC_except_table23
- GCC_except_table31
- GCC_except_table42
- GCC_except_table49
- _OBJC_IVAR_$_MIBUNWClientController._tcpPingInterval
- _OBJC_IVAR_$_MIBUNWClientController._tcpUnicastDevice
- _OBJC_IVAR_$_MIBUNWClientController._timerQueue
- _OBJC_IVAR_$_MIBUNWServerController._interfaceName
- _OBJC_IVAR_$_MIBURaptorQPacketConsumer._outputFile
- _OBJC_IVAR_$_MIBURaptorQPacketProvider._encoderSummary
- _OBJC_IVAR_$_MIBURaptorQPacketProvider._inputFile
- ___138-[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke
- ___138-[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.58
- ___138-[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.58.cold.1
- ___138-[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.63
- ___138-[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.63.cold.1
- ___138-[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.68
- ___138-[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.68.cold.1
- ___138-[MIBUNANPublisher initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.cold.1
- ___203-[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:]_block_invoke
- ___203-[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:]_block_invoke.cold.1
- ___35-[MIBUNANPublisher _startPublisher]_block_invoke.79
- ___35-[MIBUNANPublisher _startPublisher]_block_invoke.79.cold.1
- ___37-[MIBURaptorQPacketConsumer assemble]_block_invoke
- ___38-[MIBURaptorQPacketConsumer _assemble]_block_invoke
- ___38-[MIBURaptorQPacketConsumer _assemble]_block_invoke.cold.1
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.10
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.10.cold.1
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.15
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.15.cold.1
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.7
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.7.cold.1
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.10
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.16
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.16.cold.1
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.19
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.19.cold.1
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.22
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.22.cold.1
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.7
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.7.cold.1
- ___41-[MIBUNWServerController _startMulticast]_block_invoke
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.51
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.51.cold.1
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.54
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.54.cold.1
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.58
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.58.cold.1
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.cold.1
- ___42-[MIBUNWClientController _disableFirewall]_block_invoke.142
- ___42-[MIBUNWClientController _disableFirewall]_block_invoke.142.cold.1
- ___42-[MIBUNWClientController setPingInterval:]_block_invoke
- ___42-[MIBUNWClientController setPingInterval:]_block_invoke.cold.1
- ___42-[MIBUNWServerController _startNANService]_block_invoke.37
- ___42-[MIBUNWServerController _startNANService]_block_invoke.37.cold.1
- ___43-[MIBUNWServerController _startTCPListener]_block_invoke.27
- ___43-[MIBUNWServerController _startTCPListener]_block_invoke.27.cold.1
- ___43-[MIBUNWServerController _startTCPListener]_block_invoke.31
- ___43-[MIBUNWServerController _startTCPListener]_block_invoke.31.cold.1
- ___44-[MIBUNANPublisher _stopPublisherForReason:]_block_invoke.85
- ___44-[MIBUNANPublisher _stopPublisherForReason:]_block_invoke.85.cold.1
- ___44-[MIBUNWClientController checkOutWithError:]_block_invoke
- ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.136
- ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.136.cold.1
- ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.139
- ___45-[MIBUNWClientController _checkOutWithError:]_block_invoke
- ___45-[MIBUNWClientController _checkOutWithError:]_block_invoke.46
- ___45-[MIBUNWClientController _checkOutWithError:]_block_invoke.46.cold.1
- ___45-[MIBUNWClientController _checkOutWithError:]_block_invoke.cold.1
- ___45-[MIBUNWClientController _checkOutWithError:]_block_invoke_2
- ___45-[MIBUNWClientController _checkOutWithError:]_block_invoke_2.cold.1
- ___45-[MIBUNWServerDevice _handleIncomingMessage:]_block_invoke.39
- ___45-[MIBUNWServerDevice _handleIncomingMessage:]_block_invoke.39.cold.1
- ___46-[MIBUNWServerController _setupFileSenderLoop]_block_invoke.65
- ___47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.94
- ___47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.94.cold.1
- ___47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.94.cold.2
- ___49-[MIBUNWServerController _tearDownFileSenderLoop]_block_invoke.68
- ___49-[MIBUNWServerController _tearDownFileSenderLoop]_block_invoke.68.cold.1
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.136
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.136.cold.1
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.139
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.139.cold.1
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.139.cold.2
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.143
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.143.cold.1
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.148
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.148.cold.1
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke_2.140
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke_2.140.cold.1
- ___49-[MIBUNWServerController clientDeviceDidConnect:]_block_invoke.122
- ___49-[MIBUNWServerController clientDeviceDidConnect:]_block_invoke.122.cold.1
- ___49-[MIBUNWServerController clientListenerDidStart:]_block_invoke.107
- ___49-[MIBUNWServerController clientListenerDidStart:]_block_invoke.107.cold.1
- ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.125
- ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.125.cold.1
- ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.125.cold.2
- ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.78
- ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.78.cold.1
- ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.81
- ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.81.cold.1
- ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.127
- ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.127.cold.1
- ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.130
- ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.130.cold.1
- ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.130.cold.2
- ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke_2.131
- ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke_2.131.cold.1
- ___54-[MIBUNWServerController _calculateEffectiveBandwidth]_block_invoke.73
- ___54-[MIBUNWServerController _calculateEffectiveBandwidth]_block_invoke.73.cold.1
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.142
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.142.cold.1
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.142.cold.2
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.143
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.143.cold.1
- ___56-[MIBUNWServerController nanPublisherDidStart:forRetry:]_block_invoke
- ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.27
- ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.27.cold.1
- ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.30
- ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.30.cold.1
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.20
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.20.cold.1
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.116
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.116.cold.1
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.116.cold.2
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.119
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.119.cold.1
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.122
- ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.71
- ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.71.cold.1
- ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.74
- ___58-[MIBUNWServerController clientListenerDidStop:withError:]_block_invoke.112
- ___58-[MIBUNWServerController clientListenerDidStop:withError:]_block_invoke.112.cold.1
- ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.28
- ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.28.cold.1
- ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.31
- ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.31.cold.1
- ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.34
- ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.34.cold.1
- ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.37
- ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.37.cold.1
- ___63-[MIBUNWClientController _createTCPConnectionWithAddr:andPort:]_block_invoke
- ___63-[MIBUNWClientController _createTCPConnectionWithAddr:andPort:]_block_invoke.136
- ___63-[MIBUNWClientController _createTCPConnectionWithAddr:andPort:]_block_invoke.136.cold.1
- ___63-[MIBUNWClientController _createTCPConnectionWithAddr:andPort:]_block_invoke.cold.1
- ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.129
- ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.129.cold.1
- ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.62
- ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.62.cold.1
- ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.93
- ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.93.cold.1
- ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.99
- ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.99.cold.1
- ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.99.cold.2
- ___67-[MIBUNWServerController clientListener:didReceiveNewClientDevice:]_block_invoke.117
- ___67-[MIBUNWServerController clientListener:didReceiveNewClientDevice:]_block_invoke.117.cold.1
- ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.108
- ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.108.cold.1
- ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.114
- ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.114.cold.1
- ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.114.cold.2
- ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.155
- ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.155.cold.1
- ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.159
- ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.159.cold.1
- ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke_2.156
- ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke_2.156.cold.1
- ___72-[MIBURaptorQPacketProvider initWithPayloadSize:repairFactor:inputFile:]_block_invoke
- ___72-[MIBURaptorQPacketProvider initWithPayloadSize:repairFactor:inputFile:]_block_invoke.cold.1
- ___73-[MIBUNWServerController _handleFetchCompletionWithResult:atEOF:packets:]_block_invoke.94
- ___74-[MIBUNWServerController _adjustBatchSizeWithPacketDroppedInLastInterval:]_block_invoke.85
- ___74-[MIBUNWServerController _adjustBatchSizeWithPacketDroppedInLastInterval:]_block_invoke.85.cold.1
- ___block_literal_global.107
- ___block_literal_global.116
- ___block_literal_global.119
- ___block_literal_global.124
- ___block_literal_global.127
- ___block_literal_global.133
- ___block_literal_global.145
- ___block_literal_global.146
- ___block_literal_global.152
- ___block_literal_global.67
- ___block_literal_global.97
- ___block_literal_global.99
- _dispatch_get_global_queue
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_assemble
- _objc_msgSend$_checkOutWithError:
- _objc_msgSend$_createTCPConnectionWithAddr:andPort:
- _objc_msgSend$_startMulticast
- _objc_msgSend$assemble
- _objc_msgSend$checkOutWithError:withSummary:
- _objc_msgSend$devicePingPayload
- _objc_msgSend$initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:
- _objc_msgSend$nanPublisherDidStart:forRetry:
- _objc_msgSend$pingThroughMulticast:
- _objc_msgSend$pingWithPayload:
- _objc_msgSend$summaryReport
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "  channelName: %lu, band: %lu, bandwidth: %lu, enableRA: %d"
+ "  hostPort: %{public}@, groupAddr: %{public}@, groupPort: %{public}@"
+ "  serviceName: %{public}@, countryCode: %{public}@"
+ "%@"
+ "%@.part%03lu"
+ "%{public}@: All packets received, transitioning to assembling state"
+ "%{public}@: Client checkout failed after all retries!"
+ "%{public}@: Establishing NAN TCP connection with sender %{public}@ on interface %{public}@"
+ "%{public}@: Failed to bind socket to address: %s"
+ "%{public}@: Ignoring extra packet reception completion"
+ "%{public}@: Initial state - expected packets: %lu"
+ "%{public}@: Multicast receiver already stopped (socket is nil)"
+ "%{public}@: Multicast semaphore signaled, stopMulticast complete"
+ "%{public}@: Multicast socket created successfully"
+ "%{public}@: Multicast socket stopped cleanly"
+ "%{public}@: NAN publisher started using interface: %{public}@"
+ "%{public}@: NAN subscriber detected multicast error"
+ "%{public}@: NAN subscriber received %lu bytes (no action taken)"
+ "%{public}@: NAN subscriber started with peer IP: %{public}@, interface: %{public}@, retry: %d"
+ "%{public}@: NAN subscriber stopped with error: %{public}@, willRetry: %d"
+ "%{public}@: NAN subscriber terminated data session"
+ "%{public}@: NAN unicast device created successfully"
+ "%{public}@: No packets consumed from batch"
+ "%{public}@: Received the very first array of packets! Transitioning to receiving state."
+ "%{public}@: Signaling multicast socket semaphore"
+ "%{public}@: Waiting on multicast semaphore..."
+ "%{public}@: device checked out: %{public}@"
+ "%{public}@: pingThroughMulticast called with payload: %{public}@"
+ "%{public}@: pingThroughMulticast completed"
+ "%{public}@: stopMulticast called, waiting for multicast to stop..."
+ "/Library/Caches/com.apple.xbs/C913B9B7-33E5-435D-90A9-395071BD0A5E/TemporaryDirectory.KMrRKZ/Sources/MobileInBoxUpdater/External/nanorq/wrkmat.c"
+ "@\"NSFileHandle\""
+ "@108@0:8@16@24@32@40@48@56Q64Q72Q80B88@92@100"
+ "@116@0:8@16@24@32@40@48@56@64@72Q80Q88Q96B104@108"
+ "@56@0:8@16@24Q32@40@48"
+ "@76@0:8@16@24@32Q40Q48Q56B64@68"
+ "All %lu expected clients have checked in, starting file sender loop"
+ "All %lu files have received enough encoded symbols! Cycle time: %f"
+ "All TCP devices have checked out, stopping server controller"
+ "B48@0:8@16@24@32^@40"
+ "Bootstrap complete: %lu input files, %lu encoded files total"
+ "C"
+ "C16@0:8"
+ "Clearing %lu NAN devices"
+ "Clearing %lu TCP devices"
+ "Client controller initialization complete"
+ "Completed part %lu: %lu bytes read"
+ "Created %lu decoders for multi-file transfer"
+ "Creating decoder for file %lu , partFile %lu with basicParam=%llu, extendedParam=%u, output=%{public}@"
+ "Creating part file %{public}@ (%.2f GB)"
+ "Current device counts - NAN: %lu, TCP: %lu"
+ "Decoding %lu part files..."
+ "Failed to add symbol to RaptorQ decoder for file %u: %{public}@"
+ "Failed to create output file: %@"
+ "Failed to create output file: %{public}@"
+ "Failed to create part file: %{public}@"
+ "Failed to decode part file %lu: %{public}@"
+ "Failed to get file attributes for %{public}@: %{public}@"
+ "Failed to initialize NAN subscriber"
+ "Failed to initialize RaptorQ decoder for file %lu part file %lu: %{public}@"
+ "Failed to open encoded file: %{public}@ error: %{public}@"
+ "Failed to open input file for reading: %{public}@"
+ "Failed to open part file for reading: %{public}@"
+ "Failed to open part file: %@"
+ "Failed to read encoded file %{public}@ (file %u, block %u): %{public}@"
+ "Failed to reassemble part files: %{public}@"
+ "Failed to seek to offset 0 for file %u, block %u: %{public}@"
+ "Failed to set sysctl kern.ipc.sorestrictrecv to 0 with ret: %d, errno: %d (%s)"
+ "Fetched %lu packets from provider (EOF: %d)"
+ "File %lu received %lu packets total"
+ "File %lu: rqBasicParameters=%llu, rqExtendedParameters=%u"
+ "File %u has received enough encoded symbols! Total packets received: %lu"
+ "File %{public}@ is %{public}@ bytes, splitting into parts"
+ "File sender loop already running, skipping setup"
+ "Final packet distribution: "
+ "Final statistics - Total packets sent: %lu, dropped: %lu, fetched: %lu, checked-in clients: %lu"
+ "Firewall disabled successfully"
+ "Found NAN IPv6 address %{public}@ for TCP device %{public}@, terminating multicast session"
+ "Initialize packet consumer for multi-file transfer with %lu files, threshold: %lu, file ranges: %{public}@ output files: %{public}@"
+ "Initialize packet provider with payload size: %lu, repair factor: %lu, input files: %{public}@"
+ "Initializing MIBUNWServerController with TCP host: %{public}@:%{public}@, NAN port: %{public}@, multicast group: %{public}@:%{public}@, service: %{public}@, country: %{public}@, channel: %lu, band: %lu, bandwidth: %lu, RA enabled: %d"
+ "Initializing client controller with parameters:"
+ "Input file '%{public}@' assigned with range '%{public}@'"
+ "Invalid fileNumber %u (expected 0-%lu)"
+ "Invalidating packet provider"
+ "MIBUEncodedFileInfo"
+ "Multicast socket started successfully"
+ "Multicast socket stopped"
+ "Multicast socket stopped with error: %{public}@"
+ "NAN device %{public}@ checked out"
+ "NAN device disconnected: %{public}@, initiating cleanup"
+ "NAN publisher created data session with peer %{public}@ on interface %{public}@"
+ "NAN publisher destroyed data session with peer %{public}@"
+ "NAN subscriber initialized successfully"
+ "No NAN IPv6 address found for TCP device %{public}@. Device may have connected directly via infra WiFi."
+ "No part files provided"
+ "Packet distribution: "
+ "Packet too small: %zu bytes"
+ "Parameter arrays: basicParamsArray has %lu elements, extendedParamsArray has %lu elements"
+ "Part file does not exist: %@"
+ "Part file does not exist: %{public}@"
+ "Processing part %lu/%lu: %{public}@ (%.2f MB)"
+ "Reached end of file for file %u, block %u, will start from beginning."
+ "Reassembling %lu part files to %{public}@"
+ "Reassembling part files %{public}@ into %{public}@"
+ "Recorded NAN IPv6 address %{public}@ for device %{public}@"
+ "Removed NAN device from active set. Remaining NAN devices: %lu"
+ "Retrieved IPv6 address %{public}@ for interface %{public}@"
+ "Sample packet for file %u: tag=0x%08x (SBN=%u, ESI=%u), rqPacket size=%zu"
+ "Server controller cleanup complete"
+ "Split file %{public}@ into %lu parts, total bytes: %lu"
+ "Starting NAN client listener with config: %{public}@"
+ "Starting decode for file %lu (received %lu packets)..."
+ "Starting file sender loop (no expected client count set)"
+ "Starting file sending loop with batch size: %lu, packet size: %lu bytes"
+ "Stopping NAN listener"
+ "Stopping NAN publisher"
+ "Stopping TCP listener"
+ "Stopping multicast socket"
+ "Successfully decoded part file %lu to %{public}@, discarded %lu packets"
+ "Successfully reassembled file %{public}@: %lu total bytes from %lu parts"
+ "Successfully reassembled final file %{public}@"
+ "Successfully started NAN listener and multicast socket on interface %{public}@"
+ "Successfully terminated NAN data session for device: %{public}@"
+ "Successfully terminated multicast session for device: %{public}@"
+ "T@\"NSArray\",R,N,V_rqBasicParametersArray"
+ "T@\"NSArray\",R,N,V_rqExtendedParametersArray"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSFileHandle\",&,N,V_fileHandle"
+ "TC,N,V_sourceBlockNumber"
+ "TCP device %{public}@ checked out with error: %@, summary: %@"
+ "TI,N,V_fileNumber"
+ "Unexpected number of files in work directory: %lu!"
+ "Unexpected size of data read from socket: %ld (expected 1032)"
+ "Waiting for more clients to check in (%lu/%lu)"
+ "Warning: Received 0 packets from provider but not at EOF"
+ "[file%lu=%lu done=%d] "
+ "_assembleWithCompletion:"
+ "_basicParametersArray"
+ "_checkOutWithError:withSummary:"
+ "_encoderSummaries"
+ "_extendedParametersArray"
+ "_fileCompletionStatus"
+ "_fileHandle"
+ "_fileNumber"
+ "_fileRangeTable"
+ "_fileRanges"
+ "_inputFiles"
+ "_multiFileMode"
+ "_outputFiles"
+ "_packetCountsPerFile"
+ "_partOutputFiles"
+ "_partOutputFilesSizes"
+ "_pingThroughMulticast:"
+ "_raptorQDecoders"
+ "_rqBasicParametersArray"
+ "_rqExtendedParametersArray"
+ "_sourceBlockNumber"
+ "_splitInputFileIfNeeded:"
+ "_startMulticastUsingInterface:"
+ "appendBytes:length:"
+ "appendData:"
+ "appendFormat:"
+ "arrayWithCapacity:"
+ "arrayWithObjects:count:"
+ "assembleWithCompletion:"
+ "boolValue"
+ "currentDeviceCapabilities"
+ "dataWithCapacity:"
+ "discoveryInterfaceName"
+ "doubleValue"
+ "file%lu=%lu "
+ "fileHandle"
+ "fileHandleForReadingAtPath:"
+ "fileHandleForWritingAtPath:"
+ "fileNumber"
+ "fileRangeTable"
+ "firstObject"
+ "initWithBasicParametersArray:extendedParametersArray:threshold:fileRanges:outputFiles:"
+ "initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:"
+ "initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:"
+ "initWithPayloadSize:repairFactor:inputFiles:"
+ "initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:"
+ "nanPublisherDidStart:usingInterface:forRetry:"
+ "number of byte read limits does not match number of part files to read"
+ "objectForKeyedSubscript:"
+ "partBytesRead: %lu totalBytesWritten: %lu remainingBytes: %lu"
+ "publisher:getKeysBlobForMulticastSession:"
+ "rangeValue"
+ "readDataOfLength:"
+ "reassembleFileFromParts:toOutputFile:maxBytesToRead:error:"
+ "rqBasicParametersArray"
+ "rqExtendedParametersArray"
+ "setFileHandle:"
+ "setFileNumber:"
+ "setSourceBlockNumber:"
+ "sourceBlockNumber"
+ "stringByDeletingPathExtension"
+ "stringWithString:"
+ "subarrayWithRange:"
+ "unsignedLongLongValue"
+ "v20@0:8C16"
+ "v24@0:8@?<v@?B>16"
+ "v32@0:8@\"WiFiAwarePublisher\"16@\"NSData\"24"
+ "v36@0:8@\"MIBUNANPublisher\"16@\"NSString\"24B32"
+ "valueWithRange:"
+ "writeData:"
- "\n("
- "%@: Received the very first array of packets!"
- "%{pubilc}@: Failed to create dispatch source from socket."
- "%{pubilic}@: Failed to bind socket to address: %s"
- "%{public}@: Establishing NAN TCP connection with sender %{public}@"
- "%{public}@: Failed to create server device over infra."
- "%{public}@: NAN publisher started!"
- "%{public}@: TCP device checked out: %{public}@"
- "%{public}@: creating TCP connection to address: %{public}@; port: %{public}@"
- "/Library/Caches/com.apple.xbs/Sources/MobileInBoxUpdater/External/nanorq/wrkmat.c"
- ">> rqBasicParameters=%llu, rqExtendedParameters=%u"
- "@124@0:8@16@24@32@40@48@56@64@72@80Q88Q96Q104B112@116"
- "@132@0:8@16@24@32@40@48@56@64@72@80Q88Q96Q104B112@116@124"
- "@84@0:8@16@24@32@40Q48Q56Q64B72@76"
- "Failed to read encoded file: %{public}@ error: %{public}@"
- "Failed to seek to offset 0 for file handle %{public}@: %{public}@"
- "Failed to set sysctl kern.ipc.sorestrictrecv to 0 with ret: %d"
- "Ignoring extra packet reception"
- "Initialize packet provider with payload size: %lu, repair factor: %lu , input file: %{public}@"
- "NAN device %{public}@ checkout out"
- "NAN device disconnected: %{public}@"
- "No NAN IPv6 address found for TCP device."
- "RaptorQ encoder summary report:"
- "Reached end of file for %{public}@, will start from beginning."
- "Setting client controller ping interval to %{public}@"
- "Starting NAN client with listener config: %{public}@"
- "Starting file sending loop"
- "TCP device %{public}@ checked out with error: %@"
- "Unexpected size of data read from socket: %ld"
- "Unexpetced number of files in work directory: %lu!"
- "_assemble"
- "_checkOutWithError:"
- "_createTCPConnectionWithAddr:andPort:"
- "_startMulticast"
- "_tcpPingInterval"
- "_tcpUnicastDevice"
- "_timerQueue"
- "checkOutWithError:"
- "com.apple.MIBUNWClientControllerTimer"
- "devicePingPayload"
- "initWithPacketConsumer:hostPort:tcpAddress:tcpPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:"
- "initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:"
- "initWithPayloadSize:repairFactor:inputFile:"
- "initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:"
- "nanPublisherDidStart:forRetry:"
- "setPingInterval:"
- "summaryReport"
- "v28@0:8@\"MIBUNANPublisher\"16B24"

```
