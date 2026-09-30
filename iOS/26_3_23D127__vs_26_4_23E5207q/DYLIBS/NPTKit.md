## NPTKit

> `/System/Library/PrivateFrameworks/NPTKit.framework/NPTKit`

```diff

-192.0.1.0.0
-  __TEXT.__text: 0x4dd80
-  __TEXT.__auth_stubs: 0x11d0
-  __TEXT.__objc_methlist: 0x4c7c
-  __TEXT.__const: 0x628
-  __TEXT.__cstring: 0x4078
-  __TEXT.__gcc_except_tab: 0xab8
-  __TEXT.__oslogstring: 0x1065
+200.0.0.0.0
+  __TEXT.__text: 0x55620
+  __TEXT.__auth_stubs: 0x11e0
+  __TEXT.__objc_methlist: 0x4b4c
+  __TEXT.__const: 0x638
+  __TEXT.__cstring: 0x3c89
+  __TEXT.__gcc_except_tab: 0xb28
+  __TEXT.__oslogstring: 0x1645
   __TEXT.__swift5_typeref: 0x64f
   __TEXT.__swift5_capture: 0x450
   __TEXT.__constg_swiftt: 0x124

   __TEXT.__swift_as_ret: 0x54
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0xd40
-  __TEXT.__eh_frame: 0x898
-  __TEXT.__objc_classname: 0x3b2
-  __TEXT.__objc_methname: 0xe08e
-  __TEXT.__objc_methtype: 0x1967
-  __TEXT.__objc_stubs: 0x8720
-  __DATA_CONST.__got: 0x398
-  __DATA_CONST.__const: 0xaa8
-  __DATA_CONST.__objc_classlist: 0xf8
+  __TEXT.__unwind_info: 0x1590
+  __TEXT.__eh_frame: 0x890
+  __TEXT.__objc_classname: 0x443
+  __TEXT.__objc_methname: 0xe101
+  __TEXT.__objc_methtype: 0x1d0f
+  __TEXT.__objc_stubs: 0x89a0
+  __DATA_CONST.__got: 0x388
+  __DATA_CONST.__const: 0xc10
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x70
-  __DATA_CONST.__objc_protolist: 0x80
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35f8
+  __DATA_CONST.__objc_selrefs: 0x35d0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x2c8
-  __AUTH_CONST.__auth_got: 0x8f8
-  __AUTH_CONST.__const: 0xef8
-  __AUTH_CONST.__cfstring: 0x6240
-  __AUTH_CONST.__objc_const: 0xc4f8
+  __AUTH_CONST.__auth_got: 0x900
+  __AUTH_CONST.__const: 0xed8
+  __AUTH_CONST.__cfstring: 0x6380
+  __AUTH_CONST.__objc_const: 0xbfe0
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x258
   __DATA.__objc_ivar: 0x744
-  __DATA.__data: 0x718
+  __DATA.__data: 0x6b8
   __DATA.__bss: 0x180
   __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA_DIRTY.__objc_data: 0x780
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0C800107-6579-3D0F-97CE-9EEF4D2662CF
-  Functions: 2016
-  Symbols:   5883
-  CStrings:  4512
+  UUID: 95A4819D-BB88-3839-95F3-510DBF349E96
+  Functions: 2004
+  Symbols:   5881
+  CStrings:  4554
 
Symbols:
+ +[NPTCellularCollector antennaPositionEnumToString:]
+ -[NPTCellularCollector antennaSelectionAPIIsAvailable]
+ -[NPTCellularCollector antennaSelectionAPIIsAvailable].cold.1
+ -[NPTCellularCollector currentAntennaState]
+ -[NPTCellularCollector dealloc]
+ -[NPTCellularCollector periodicActiveAntennaUpdate]
+ -[NPTCellularCollector periodicActiveAntennaUpdate].cold.1
+ -[NPTCellularCollector periodicActiveAntennaUpdate].cold.2
+ -[NPTCellularCollector periodicCollectionTimer]
+ -[NPTCellularCollector serverConnection]
+ -[NPTCellularCollector setCurrentAntennaState:]
+ -[NPTCellularCollector setPeriodicCollectionTimer:]
+ -[NPTCellularCollector setServerConnection:]
+ -[NPTCellularCollector setupPeriodicCollectionTimer]
+ -[NPTCellularCollector setupPeriodicCollectionTimer].cold.1
+ -[NPTCellularCollector setupPeriodicCollectionTimer].cold.2
+ -[NPTPing _cancelTimer]
+ -[NPTPing _completePingWithError:]
+ -[NPTPing _receiveReply]
+ -[NPTPing _sendPing]
+ -[NPTPing _setupDNSResolverForHostname:]
+ -[NPTPing _setupSocketAndConnection]
+ -[NPTPing _setupTimerWithCurrentSequenceNumber:]
+ -[NPTPing _startPinging:withNumberOfPings:forceipv6:completion:]
+ -[NPTPing _stop]
+ -[NPTPing checksumForData:]
+ -[NPTPing createPingErrorWithCode:message:]
+ -[NPTPing forceIPv6]
+ -[NPTPing hostname]
+ -[NPTPing init]
+ -[NPTPing intermediateResult]
+ -[NPTPing maxPings]
+ -[NPTPing parseICMP4Reply:identifier:]
+ -[NPTPing parseICMP6Reply:identifier:]
+ -[NPTPing pings]
+ -[NPTPing processIPv4Address:forHostname:]
+ -[NPTPing processIPv6Address:forHostname:]
+ -[NPTPing resolvedAddress]
+ -[NPTPing setForceIPv6:]
+ -[NPTPing setHostname:]
+ -[NPTPing setMaxPings:]
+ -[NPTPing setPings:]
+ -[NPTPing setResolvedAddress:]
+ -[NPTPing setStopped:]
+ -[NPTPing startPingingToHost:withNumberOfPings:forceipv6:completion:]
+ -[NPTPing stopped]
+ -[NPTPing updatePingObjectWithReplyInfo:]
+ GCC_except_table14
+ GCC_except_table16
+ GCC_except_table19
+ GCC_except_table21
+ GCC_except_table22
+ GCC_except_table26
+ GCC_except_table30
+ GCC_except_table31
+ GCC_except_table32
+ GCC_except_table34
+ GCC_except_table35
+ GCC_except_table83
+ GCC_except_table89
+ _CFDictionaryGetValue
+ _CFNumberGetValue
+ _OBJC_IVAR_$_NPTCellularCollector._currentAntennaState
+ _OBJC_IVAR_$_NPTCellularCollector._periodicCollectionTimer
+ _OBJC_IVAR_$_NPTCellularCollector._serverConnection
+ _OBJC_IVAR_$_NPTPing._forceIPv6
+ _OBJC_IVAR_$_NPTPing._hostname
+ _OBJC_IVAR_$_NPTPing._maxPings
+ _OBJC_IVAR_$_NPTPing._pings
+ _OBJC_IVAR_$_NPTPing._resolvedAddress
+ _OBJC_IVAR_$_NPTPing._stopped
+ _OBJC_IVAR_$_NPTPing.connection
+ _OBJC_IVAR_$_NPTPing.destAddr
+ _OBJC_IVAR_$_NPTPing.networkQueue
+ _OBJC_IVAR_$_NPTPing.rawSocket
+ _OBJC_IVAR_$_NPTPing.resolver
+ _OBJC_IVAR_$_NPTPing.sequenceNumber
+ _OBJC_IVAR_$_NPTPing.timeoutTimer
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ __CTServerConnectionCopyAntennaSelectionInfo
+ ___20-[NPTPing _sendPing]_block_invoke
+ ___24-[NPTPing _receiveReply]_block_invoke
+ ___24-[NPTPing _receiveReply]_block_invoke.49
+ ___29-[NPTPing intermediateResult]_block_invoke
+ ___34-[NPTPing _completePingWithError:]_block_invoke
+ ___36-[NPTPing _setupSocketAndConnection]_block_invoke
+ ___40-[NPTPing _setupDNSResolverForHostname:]_block_invoke
+ ___40-[NPTPing _setupDNSResolverForHostname:]_block_invoke.16
+ ___48-[NPTPing _setupTimerWithCurrentSequenceNumber:]_block_invoke
+ ___52-[NPTCellularCollector setupPeriodicCollectionTimer]_block_invoke
+ ___54-[NPTCellularCollector startCollectingWithCompletion:]_block_invoke.253
+ ___64-[NPTPing _startPinging:withNumberOfPings:forceipv6:completion:]_block_invoke
+ ___69-[NPTPing startPingingToHost:withNumberOfPings:forceipv6:completion:]_block_invoke
+ ___Block_byref_object_copy_.251
+ ___Block_byref_object_dispose_.252
+ ___block_descriptor_40_e8_32s_e101_v36?0"NSObject<OS_dispatch_data>"8"NSObject<OS_nw_content_context>"16B24"NSObject<OS_nw_error>"28ls32l8
+ ___block_descriptor_40_e8_32s_e31_v16?0"NSObject<OS_nw_error>"8ls32l8
+ ___block_descriptor_40_e8_32s_e34_v20?0i8"NSObject<OS_nw_error>"12ls32l8
+ ___block_descriptor_40_e8_32s_e47_B40?0"NSObject<OS_dispatch_data>"8Q16r^v24Q32ls32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_43_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e34_v20?0i8"NSObject<OS_nw_array>"12ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48r_e35_B24?0Q8"NSObject<OS_nw_object>"16ls32l8s40l8r48l8
+ ___block_descriptor_65_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ __nw_content_context_default_message
+ _block_copy_helper.19
+ _block_copy_helper.72
+ _block_copy_helper.82
+ _block_copy_helper.86
+ _block_copy_helper.90
+ _block_descriptor.21
+ _block_descriptor.74
+ _block_descriptor.84
+ _block_descriptor.88
+ _block_descriptor.92
+ _block_destroy_helper.20
+ _block_destroy_helper.73
+ _block_destroy_helper.83
+ _block_destroy_helper.87
+ _block_destroy_helper.91
+ _connect
+ _dispatch_data_apply
+ _dispatch_data_create
+ _dispatch_data_get_size
+ _dispatch_resume
+ _dispatch_sync
+ _getpid
+ _inet_ntop
+ _kCTAntennaSelectionPort
+ _kCTAntennaSelectionPrimary
+ _kCTAntennaSelectionPrimaryLocation
+ _kCTAntennaSelectionSecondary
+ _kCTAntennaSelectionSecondaryLocation
+ _nw_array_apply
+ _nw_connection_cancel
+ _nw_connection_create_with_connected_socket
+ _nw_connection_receive
+ _nw_connection_send
+ _nw_connection_set_queue
+ _nw_connection_set_state_changed_handler
+ _nw_connection_start
+ _nw_endpoint_create_host
+ _nw_endpoint_get_address
+ _nw_endpoint_get_type
+ _nw_ip_options_set_version
+ _nw_parameters_copy_default_protocol_stack
+ _nw_parameters_create
+ _nw_protocol_stack_copy_internet_protocol
+ _nw_resolver_cancel
+ _nw_resolver_create_with_endpoint
+ _nw_resolver_set_update_handler
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_cancelTimer
+ _objc_msgSend$_completePingWithError:
+ _objc_msgSend$_receiveReply
+ _objc_msgSend$_sendPing
+ _objc_msgSend$_setupDNSResolverForHostname:
+ _objc_msgSend$_setupSocketAndConnection
+ _objc_msgSend$_setupTimerWithCurrentSequenceNumber:
+ _objc_msgSend$_startPinging:withNumberOfPings:forceipv6:completion:
+ _objc_msgSend$_stop
+ _objc_msgSend$activateWithCompletion:
+ _objc_msgSend$activeDevices
+ _objc_msgSend$antennaPositionEnumToString:
+ _objc_msgSend$antennaSelectionAPIIsAvailable
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$checksumForData:
+ _objc_msgSend$createPingErrorWithCode:message:
+ _objc_msgSend$currentAntennaState
+ _objc_msgSend$date
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$getPrivilegedFileHandleForPacketCaptureWithCompletionHandler:
+ _objc_msgSend$getPrivilegedFileHandleForPath:completionHandler:
+ _objc_msgSend$hostname
+ _objc_msgSend$idsDeviceIdentifier
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$lastObject
+ _objc_msgSend$localizedFailureReason
+ _objc_msgSend$maxPings
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$parseICMP4Reply:identifier:
+ _objc_msgSend$parseICMP6Reply:identifier:
+ _objc_msgSend$periodicActiveAntennaUpdate
+ _objc_msgSend$periodicCollectionTimer
+ _objc_msgSend$processIPv4Address:forHostname:
+ _objc_msgSend$processIPv6Address:forHostname:
+ _objc_msgSend$registerEventID:options:handler:
+ _objc_msgSend$registerRequestID:options:handler:
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$replaceBytesInRange:withBytes:
+ _objc_msgSend$sendEventID:event:options:completion:
+ _objc_msgSend$sendRequestID:request:options:responseHandler:
+ _objc_msgSend$serverConnection
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setControlFlags:
+ _objc_msgSend$setCurrentAntennaState:
+ _objc_msgSend$setDestinationDevice:
+ _objc_msgSend$setDeviceChangedHandler:
+ _objc_msgSend$setDeviceFoundHandler:
+ _objc_msgSend$setDeviceLostHandler:
+ _objc_msgSend$setDisconnectHandler:
+ _objc_msgSend$setForceIPv6:
+ _objc_msgSend$setHostname:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setMaxPings:
+ _objc_msgSend$setPeriodicCollectionTimer:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setServerConnection:
+ _objc_msgSend$setServiceType:
+ _objc_msgSend$setStopped:
+ _objc_msgSend$setupPeriodicCollectionTimer
+ _objc_msgSend$startLocalPerformanceTestWith:completionHandler:
+ _objc_msgSend$startPingingToHost:withNumberOfPings:forceipv6:completion:
+ _objc_msgSend$stopLocalPerformanceTest:
+ _objc_msgSend$stopped
+ _objc_msgSend$testServiceWithArguments:completionHandler:
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$updatePingObjectWithReplyInfo:
+ _objectdestroy.3Tm
+ _strerror
- +[SimplePing icmpHeaderOffsetInIPv4Packet:]
- -[NPTPing cancel]
- -[NPTPing canceled]
- -[NPTPing initWithNetworkActivityParent:pingTarget:]
- -[NPTPing sendPing]
- -[NPTPing setCanceled:]
- -[NPTPing simplePing:didFailToSendPacket:sequenceNumber:error:]
- -[NPTPing simplePing:didFailToSendPacket:sequenceNumber:error:].cold.1
- -[NPTPing simplePing:didFailWithError:]
- -[NPTPing simplePing:didFailWithError:].cold.1
- -[NPTPing simplePing:didReceivePingResponsePacket:sequenceNumber:]
- -[NPTPing simplePing:didReceiveUnexpectedPacket:]
- -[NPTPing simplePing:didReceiveUnexpectedPacket:].cold.1
- -[NPTPing simplePing:didSendPacket:sequenceNumber:]
- -[NPTPing simplePing:didStartWithAddress:]
- -[NPTPing simplePing:didTimeOut:sequenceNumber:error:]
- -[NPTPing simplePing:didTimeOut:sequenceNumber:error:].cold.1
- -[NPTPing startWithNumberOfPings:forcingIPv4:forcingIPv6:]
- -[NPTPing startWithNumberOfPings:forcingIPv4:forcingIPv6:completion:]
- -[SimplePing .cxx_destruct]
- -[SimplePing addressStyle]
- -[SimplePing copyWithZone:]
- -[SimplePing dealloc]
- -[SimplePing delegate]
- -[SimplePing didFailWithError:]
- -[SimplePing didFailWithHostStreamError:]
- -[SimplePing hostAddressFamily]
- -[SimplePing hostAddress]
- -[SimplePing hostName]
- -[SimplePing hostResolutionDone]
- -[SimplePing host]
- -[SimplePing identifier]
- -[SimplePing initWithHostName:]
- -[SimplePing isInvalidated]
- -[SimplePing nextSequenceNumberHasWrapped]
- -[SimplePing nextSequenceNumber]
- -[SimplePing packetDidFailToSendDelegate:error:]
- -[SimplePing pingPacketWithType:payload:requiresChecksum:]
- -[SimplePing readData]
- -[SimplePing sendPingWithData:]
- -[SimplePing setAddressStyle:]
- -[SimplePing setDelegate:]
- -[SimplePing setHost:]
- -[SimplePing setHostAddress:]
- -[SimplePing setIsInvalidated:]
- -[SimplePing setNextSequenceNumber:]
- -[SimplePing setNextSequenceNumberHasWrapped:]
- -[SimplePing setSocket:]
- -[SimplePing setTimeoutTimer:]
- -[SimplePing setupTimer:currentSequenceNumber:]
- -[SimplePing socket]
- -[SimplePing startWithHostAddress]
- -[SimplePing startWithHostAddress].cold.1
- -[SimplePing start]
- -[SimplePing stopHostResolution]
- -[SimplePing stopSocket]
- -[SimplePing stop]
- -[SimplePing timeOutHandler:sequenceNumber:]
- -[SimplePing timeoutTimer]
- -[SimplePing validatePing4ResponsePacket:sequenceNumber:]
- -[SimplePing validatePing6ResponsePacket:sequenceNumber:]
- -[SimplePing validatePingResponsePacket:sequenceNumber:]
- -[SimplePing validateSequenceNumber:]
- GCC_except_table23
- GCC_except_table27
- GCC_except_table28
- GCC_except_table29
- GCC_except_table6
- GCC_except_table69
- GCC_except_table7
- GCC_except_table72
- _CFAutorelease
- _CFHostCreateWithName
- _CFHostGetAddressing
- _CFHostScheduleWithRunLoop
- _CFHostSetClient
- _CFHostStartInfoResolution
- _CFHostUnscheduleFromRunLoop
- _CFRetain
- _CFRunLoopAddSource
- _CFRunLoopPerformBlock
- _CFRunLoopWakeUp
- _CFSocketCreateRunLoopSource
- _CFSocketCreateWithNative
- _CFSocketGetNative
- _CFSocketGetSocketFlags
- _CFSocketInvalidate
- _HostResolveCallback
- _NSPOSIXErrorDomain
- _OBJC_CLASS_$_NSData
- _OBJC_CLASS_$_NSURLConnection
- _OBJC_CLASS_$_SimplePing
- _OBJC_IVAR_$_NPTPing._canceled
- _OBJC_IVAR_$_NPTPing.activityParent
- _OBJC_IVAR_$_NPTPing.pingCount
- _OBJC_IVAR_$_NPTPing.pinger
- _OBJC_IVAR_$_NPTPing.pings
- _OBJC_IVAR_$_SimplePing._addressStyle
- _OBJC_IVAR_$_SimplePing._delegate
- _OBJC_IVAR_$_SimplePing._host
- _OBJC_IVAR_$_SimplePing._hostAddress
- _OBJC_IVAR_$_SimplePing._hostName
- _OBJC_IVAR_$_SimplePing._identifier
- _OBJC_IVAR_$_SimplePing._isInvalidated
- _OBJC_IVAR_$_SimplePing._nextSequenceNumber
- _OBJC_IVAR_$_SimplePing._nextSequenceNumberHasWrapped
- _OBJC_IVAR_$_SimplePing._socket
- _OBJC_IVAR_$_SimplePing._timeoutTimer
- _OBJC_METACLASS_$_SimplePing
- _SocketReadCallback
- __OBJC_$_CLASS_METHODS_SimplePing
- __OBJC_$_CLASS_PROP_LIST_NPTPing
- __OBJC_$_INSTANCE_METHODS_SimplePing
- __OBJC_$_INSTANCE_VARIABLES_SimplePing
- __OBJC_$_PROP_LIST_SimplePing
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SimplePingDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_SimplePingDelegate
- __OBJC_$_PROTOCOL_REFS_SimplePingDelegate
- __OBJC_CLASS_PROTOCOLS_$_SimplePing
- __OBJC_CLASS_RO_$_SimplePing
- __OBJC_LABEL_PROTOCOL_$_SimplePingDelegate
- __OBJC_METACLASS_RO_$_SimplePing
- __OBJC_PROTOCOL_$_SimplePingDelegate
- ___19-[SimplePing start]_block_invoke
- ___24-[SimplePing stopSocket]_block_invoke
- ___32-[SimplePing stopHostResolution]_block_invoke
- ___39-[NPTPing simplePing:didFailWithError:]_block_invoke
- ___47-[SimplePing setupTimer:currentSequenceNumber:]_block_invoke
- ___47-[SimplePing setupTimer:currentSequenceNumber:]_block_invoke_2
- ___54-[NPTCellularCollector startCollectingWithCompletion:]_block_invoke.251
- ___Block_byref_object_copy_.249
- ___Block_byref_object_dispose_.250
- ___assert_rtn
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_50_e8_32s40w_e5_v8?0lw40l8s32l8
- _arc4random
- _block_copy_helper.15
- _block_copy_helper.22
- _block_copy_helper.75
- _block_copy_helper.8
- _block_copy_helper.81
- _block_copy_helper.85
- _block_copy_helper.89
- _block_copy_helper.93
- _block_copy_helper.97
- _block_descriptor.10
- _block_descriptor.17
- _block_descriptor.24
- _block_descriptor.77
- _block_descriptor.83
- _block_descriptor.87
- _block_descriptor.91
- _block_descriptor.95
- _block_descriptor.99
- _block_destroy_helper.16
- _block_destroy_helper.23
- _block_destroy_helper.76
- _block_destroy_helper.82
- _block_destroy_helper.86
- _block_destroy_helper.9
- _block_destroy_helper.90
- _block_destroy_helper.94
- _block_destroy_helper.98
- _free
- _kCFErrorDomainCFNetwork
- _kCFGetAddrInfoFailureKey
- _kCFRunLoopDefaultMode
- _kCFStreamErrorDomainNetDB
- _malloc_type_malloc
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$addressStyle
- _objc_msgSend$canceled
- _objc_msgSend$didFailWithError:
- _objc_msgSend$didFailWithHostStreamError:
- _objc_msgSend$host
- _objc_msgSend$hostAddress
- _objc_msgSend$hostAddressFamily
- _objc_msgSend$hostName
- _objc_msgSend$hostResolutionDone
- _objc_msgSend$icmpHeaderOffsetInIPv4Packet:
- _objc_msgSend$initWithData:
- _objc_msgSend$initWithHostName:
- _objc_msgSend$initWithNetworkActivityParent:pingTarget:
- _objc_msgSend$isInvalidated
- _objc_msgSend$nextSequenceNumber
- _objc_msgSend$nextSequenceNumberHasWrapped
- _objc_msgSend$packetDidFailToSendDelegate:error:
- _objc_msgSend$pingPacketWithType:payload:requiresChecksum:
- _objc_msgSend$readData
- _objc_msgSend$replaceBytesInRange:withBytes:length:
- _objc_msgSend$resourceLoaderRunLoop
- _objc_msgSend$sendPing
- _objc_msgSend$sendPingWithData:
- _objc_msgSend$setAddressStyle:
- _objc_msgSend$setCanceled:
- _objc_msgSend$setHost:
- _objc_msgSend$setHostAddress:
- _objc_msgSend$setIsInvalidated:
- _objc_msgSend$setNextSequenceNumber:
- _objc_msgSend$setNextSequenceNumberHasWrapped:
- _objc_msgSend$setSocket:
- _objc_msgSend$setTimeoutTimer:
- _objc_msgSend$setupTimer:currentSequenceNumber:
- _objc_msgSend$simplePing:didFailToSendPacket:sequenceNumber:error:
- _objc_msgSend$simplePing:didFailWithError:
- _objc_msgSend$simplePing:didReceivePingResponsePacket:sequenceNumber:
- _objc_msgSend$simplePing:didReceiveUnexpectedPacket:
- _objc_msgSend$simplePing:didSendPacket:sequenceNumber:
- _objc_msgSend$simplePing:didStartWithAddress:
- _objc_msgSend$simplePing:didTimeOut:sequenceNumber:error:
- _objc_msgSend$socket
- _objc_msgSend$start
- _objc_msgSend$startWithHostAddress
- _objc_msgSend$startWithNumberOfPings:forcingIPv4:forcingIPv6:completion:
- _objc_msgSend$stopHostResolution
- _objc_msgSend$stopSocket
- _objc_msgSend$timeOutHandler:sequenceNumber:
- _objc_msgSend$timeoutTimer
- _objc_msgSend$validatePing4ResponsePacket:sequenceNumber:
- _objc_msgSend$validatePing6ResponsePacket:sequenceNumber:
- _objc_msgSend$validatePingResponsePacket:sequenceNumber:
- _objc_msgSend$validateSequenceNumber:
- _objc_release_x1
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_setProperty_nonatomic
- _objectdestroy.6Tm
- _recvfrom
- _sendto
- _setsockopt
CStrings:
+ "(?=\"ipv4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"ipv6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})"
+ "0"
+ "@\"NSObject<OS_nw_connection>\""
+ "@\"NSObject<OS_nw_resolver>\""
+ "@20@0:8C16"
+ "@32@0:8q16@24"
+ "AntennaSelection API not supported"
+ "B24@?0Q8@\"NSObject<OS_nw_object>\"16"
+ "B40@?0@\"NSObject<OS_dispatch_data>\"8Q16r^v24Q32"
+ "Completed %lu pings, stopping."
+ "Connected %@ ICMP socket successfully"
+ "Connection failed"
+ "Created %@ ICMP socket successfully (fd: %d)"
+ "Created Network.framework resolver for %@ hostname resolution"
+ "DNS resolution completed successfully"
+ "DNS resolution failed for hostname: %@"
+ "DNS resolution in progress for hostname: %@"
+ "Failed to connect %@ ICMP socket: %s"
+ "Failed to connect %@ ICMP socket: %s (errno: %d)"
+ "Failed to create %@ ICMP socket: %s"
+ "Failed to create %@ ICMP socket: %s (errno: %d)"
+ "Failed to create CT server connection for antenna selection"
+ "Failed to create Network framework connection from socket"
+ "Failed to create Network.framework resolver"
+ "Failed to create nw_connection from socket"
+ "Failed to create periodic collection timer"
+ "Failed to get antenna selection info: domain=%d, error=%d"
+ "Failed to send ping packet"
+ "ICMP reply too large: %zu bytes (max %zu)"
+ "ICMPv4 packet too short after IP header: %zu bytes"
+ "ICMPv4 packet too short: %zu bytes (minimum %zu)"
+ "ICMPv4 packet type or identifier incorrect"
+ "ICMPv6 packet too short: %zu bytes (minimum %zu)"
+ "ICMPv6 packet type or identifier incorrect"
+ "Invalid reply info or sequence number"
+ "NPTPing Connection cancelled"
+ "NPTPing Connection failed: %@"
+ "NPTPing Connection ready, starting to ping..."
+ "NPTPing Connection state changed to: %d"
+ "NPTPing Connection state: preparing"
+ "NPTPing Connection state: waiting"
+ "NPTPinger has been stopped, no longer have connection"
+ "No %@ address found for hostname: %@"
+ "Parsed ICMPv4 reply: seq=%d"
+ "Parsed ICMPv6 reply: seq=%d"
+ "Periodic collection timer started successfully"
+ "Ping already in progress"
+ "Ping timeout for sequence number %d"
+ "Receive error: %@"
+ "Resolved %@ to IPv4 %s"
+ "Resolved %@ to IPv6 %s"
+ "S24@0:8@16"
+ "Send error: %@"
+ "Sending %@ ping #%lu/%lu to %@ (%lu bytes)"
+ "Started DNS resolution for hostname: %@"
+ "Started NPTPing connection"
+ "T@\"NPTPingResult\",&,V_results"
+ "T@\"NPTPingResult\",R"
+ "T@\"NSMutableArray\",&,V_pings"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_periodicCollectionTimer"
+ "T@\"NSString\",C,V_hostname"
+ "T@\"NSString\",C,V_resolvedAddress"
+ "T@?,C,V_completion"
+ "TB,V_forceIPv6"
+ "TB,V_stopped"
+ "TQ,V_currentAntennaState"
+ "TQ,V_maxPings"
+ "T^{__CTServerConnection=},V_serverConnection"
+ "UTF8String"
+ "Unknown connection state: %d"
+ "Unknown error"
+ "Updated ping object for sequence %d: RTT=%.2fms, protocol=%@"
+ "Will test %@ ping latency by sending %lu pings to Apple CDN Server"
+ "^{__CTServerConnection=}"
+ "^{__CTServerConnection=}16@0:8"
+ "_cancelTimer"
+ "_completePingWithError:"
+ "_currentAntennaState"
+ "_forceIPv6"
+ "_hostname"
+ "_maxPings"
+ "_periodicCollectionTimer"
+ "_receiveReply"
+ "_resolvedAddress"
+ "_sendPing"
+ "_serverConnection"
+ "_setupDNSResolverForHostname:"
+ "_setupSocketAndConnection"
+ "_setupTimerWithCurrentSequenceNumber:"
+ "_startPinging:withNumberOfPings:forceipv6:completion:"
+ "_stop"
+ "_stopped"
+ "antennaPositionEnumToString:"
+ "antennaSelectionAPIIsAvailable"
+ "appendBytes:length:"
+ "cellular_active_antenna_changed"
+ "cellular_antenna_port"
+ "cellular_antenna_primary"
+ "cellular_antenna_primary_location"
+ "cellular_antenna_secondary"
+ "cellular_antenna_secondary_location"
+ "checksumForData:"
+ "com.apple.nptkit.ping"
+ "createPingErrorWithCode:message:"
+ "currentAntennaState"
+ "date"
+ "destAddr"
+ "forceIPv6"
+ "getBytes:length:"
+ "hostname"
+ "idleLatencyProbeCompleted:"
+ "intermediateResult"
+ "invalid"
+ "lastObject"
+ "lower left"
+ "lower right"
+ "maxPings"
+ "networkQueue"
+ "numberWithUnsignedChar:"
+ "parseICMP4Reply:identifier:"
+ "parseICMP6Reply:identifier:"
+ "periodicActiveAntennaUpdate"
+ "periodicCollectionTimer"
+ "processIPv4Address:forHostname:"
+ "processIPv6Address:forHostname:"
+ "rawSocket"
+ "removeAllObjects"
+ "replaceBytesInRange:withBytes:"
+ "resolvedAddress"
+ "resolver"
+ "sequenceNumber"
+ "serverConnection"
+ "setCurrentAntennaState:"
+ "setForceIPv6:"
+ "setHostname:"
+ "setMaxPings:"
+ "setPeriodicCollectionTimer:"
+ "setResolvedAddress:"
+ "setServerConnection:"
+ "setStopped:"
+ "setupPeriodicCollectionTimer"
+ "startPingingToHost:withNumberOfPings:forceipv6:completion:"
+ "stopped"
+ "timeIntervalSince1970"
+ "updatePingObjectWithReplyInfo:"
+ "upper left"
+ "upper right"
+ "v16@?0@\"NSObject<OS_nw_error>\"8"
+ "v20@?0i8@\"NSObject<OS_nw_array>\"12"
+ "v20@?0i8@\"NSObject<OS_nw_error>\"12"
+ "v24@0:8@\"NSDictionary\"16"
+ "v24@0:8^{__CTServerConnection=}16"
+ "v32@0:8r^{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}16@24"
+ "v32@0:8r^{sockaddr_in=CCS{in_addr=I}[8c]}16@24"
+ "v32@0:8{?=BS@}16"
+ "v36@?0@\"NSObject<OS_dispatch_data>\"8@\"NSObject<OS_nw_content_context>\"16B24@\"NSObject<OS_nw_error>\"28"
+ "v44@0:8@16Q24B32@?36"
+ "{?=BS@}28@0:8@16S24"
+ "\xb1"
- "!"
- "%28zd bottles of beer on the wall"
- "%@. Sent: %ld Received: %ld Expected: %lu Percent Lost: %.02f"
- "-[SimplePing startWithHostAddress]"
- "@\"<SimplePingDelegate>\""
- "@\"NSData\""
- "@\"SimplePing\""
- "@32@0:8C16@20B28"
- "B20@0:8S16"
- "B32@0:8@16^S24"
- "C16@0:8"
- "CFSocketGetSocketFlags(self.socket) & kCFSocketCloseOnInvalidate"
- "Errors encountered with ping. Sent: %ld Received: %ld Expected: %lu Percent Lost: %f"
- "Failed to allocate buffer"
- "Failed to create CFHost"
- "Failed to create Socket"
- "Failed to create packet"
- "Failed to read packet data"
- "Failed to send packet with error: %{public}@"
- "Failed to send pings with error: %{public}@"
- "Ping not successful: Did receive unexpected packet"
- "Ping timed out"
- "Q24@0:8@16"
- "S16@0:8"
- "SimplePing"
- "SimplePing.m"
- "SimplePingDelegate"
- "T@\"<SimplePingDelegate>\",W,N,V_delegate"
- "T@\"NPTPingResult\",&,N,V_results"
- "T@\"NSData\",C,V_hostAddress"
- "T@\"NSObject<OS_dispatch_source>\",&,V_timeoutTimer"
- "T@\"NSString\",R,C,V_hostName"
- "TB,N,V_canceled"
- "TB,N,V_nextSequenceNumberHasWrapped"
- "TB,V_isInvalidated"
- "TC,R"
- "TS,R,N,V_identifier"
- "TS,V_nextSequenceNumber"
- "T^{__CFHost=},&,N,V_host"
- "T^{__CFSocket=},&,N,V_socket"
- "Time out with error: %{public}@ , Sequence Number %hu"
- "Tq,N,V_addressStyle"
- "Unknown error occurred"
- "Will test ping latency by sending %lu pings to Apple CDN Server"
- "^{__CFHost=}"
- "^{__CFHost=}16@0:8"
- "^{__CFSocket=}"
- "^{__CFSocket=}16@0:8"
- "_addressStyle"
- "_canceled"
- "_host"
- "_hostAddress"
- "_hostName"
- "_identifier"
- "_isInvalidated"
- "_nextSequenceNumber"
- "_nextSequenceNumberHasWrapped"
- "_socket"
- "_timeoutTimer"
- "a"
- "addressStyle"
- "canceled"
- "didFailWithError:"
- "didFailWithHostStreamError:"
- "host"
- "hostAddress"
- "hostAddress is nil"
- "hostAddressFamily"
- "hostAddressFamily is not compatible"
- "hostName"
- "hostResolutionDone"
- "icmpHeaderOffsetInIPv4Packet:"
- "initWithData:"
- "initWithHostName:"
- "initWithNetworkActivityParent:pingTarget:"
- "isInvalidated"
- "nextSequenceNumber"
- "nextSequenceNumberHasWrapped"
- "packetDidFailToSendDelegate:error:"
- "pingPacketWithType:payload:requiresChecksum:"
- "pinger"
- "readData"
- "replaceBytesInRange:withBytes:length:"
- "resourceLoaderRunLoop"
- "sendPing"
- "sendPingWithData:"
- "setAddressStyle:"
- "setCanceled:"
- "setHost:"
- "setHostAddress:"
- "setIsInvalidated:"
- "setNextSequenceNumber:"
- "setNextSequenceNumberHasWrapped:"
- "setSocket:"
- "setTimeoutTimer:"
- "setupTimer:currentSequenceNumber:"
- "simplePing:didFailToSendPacket:sequenceNumber:error:"
- "simplePing:didFailWithError:"
- "simplePing:didReceivePingResponsePacket:sequenceNumber:"
- "simplePing:didReceiveUnexpectedPacket:"
- "simplePing:didSendPacket:sequenceNumber:"
- "simplePing:didStartWithAddress:"
- "simplePing:didTimeOut:sequenceNumber:error:"
- "socket"
- "start"
- "startWithHostAddress"
- "startWithNumberOfPings:forcingIPv4:forcingIPv6:"
- "startWithNumberOfPings:forcingIPv4:forcingIPv6:completion:"
- "stopHostResolution"
- "stopSocket"
- "timeOutHandler:sequenceNumber:"
- "v24@0:8^{__CFHost=}16"
- "v24@0:8^{__CFSocket=}16"
- "v28@0:8@16S24"
- "v32@0:8@\"SimplePing\"16@\"NSData\"24"
- "v32@0:8@\"SimplePing\"16@\"NSError\"24"
- "v32@0:8Q16B24B28"
- "v32@0:8{?=qi}16"
- "v36@0:8@\"SimplePing\"16@\"NSData\"24S32"
- "v36@0:8@16@24S32"
- "v40@0:8Q16B24B28@?32"
- "v44@0:8@\"SimplePing\"16@\"NSData\"24S32@\"NSError\"36"
- "v44@0:8@16@24S32@36"
- "validatePing4ResponsePacket:sequenceNumber:"
- "validatePing6ResponsePacket:sequenceNumber:"
- "validatePingResponsePacket:sequenceNumber:"
- "validateSequenceNumber:"

```
