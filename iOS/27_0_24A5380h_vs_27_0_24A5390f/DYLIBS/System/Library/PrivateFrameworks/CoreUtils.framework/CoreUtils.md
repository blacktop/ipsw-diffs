## CoreUtils

> `/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-900.48.0.0.0
-  __TEXT.__text: 0x114c48
-  __TEXT.__objc_methlist: 0x9ed0
-  __TEXT.__cstring: 0x1d52c
+900.55.0.0.0
+  __TEXT.__text: 0x117560
+  __TEXT.__objc_methlist: 0xa040
+  __TEXT.__cstring: 0x1d6f7
   __TEXT.__const: 0x229c
-  __TEXT.__gcc_except_tab: 0x1b14
-  __TEXT.__oslogstring: 0x4818
-  __TEXT.__unwind_info: 0x3970
+  __TEXT.__gcc_except_tab: 0x1ba0
+  __TEXT.__oslogstring: 0x49b7
+  __TEXT.__unwind_info: 0x39d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2960
-  __DATA_CONST.__objc_classlist: 0x340
+  __DATA_CONST.__const: 0x29c0
+  __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5070
+  __DATA_CONST.__objc_selrefs: 0x5120
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x238
+  __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x6a0
-  __AUTH_CONST.__const: 0x2808
-  __AUTH_CONST.__cfstring: 0x44c0
-  __AUTH_CONST.__objc_const: 0x13890
+  __DATA_CONST.__got: 0x6c0
+  __AUTH_CONST.__const: 0x2828
+  __AUTH_CONST.__cfstring: 0x4540
+  __AUTH_CONST.__objc_const: 0x13c40
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1818
-  __AUTH.__objc_data: 0x1f90
+  __AUTH_CONST.__auth_got: 0x1858
+  __AUTH.__objc_data: 0x2030
   __AUTH.__data: 0xa00
-  __DATA.__objc_ivar: 0x14cc
+  __DATA.__objc_ivar: 0x1510
   __DATA.__data: 0x2f50
-  __DATA.__bss: 0x13c8
+  __DATA.__bss: 0x13f8
   __DATA.__common: 0x2a
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x1d1
+  __DATA_DIRTY.__bss: 0x1c9
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5752
-  Symbols:   11488
-  CStrings:  4818
+  Functions: 5789
+  Symbols:   11598
+  CStrings:  4852
 
Symbols:
+ +[CUXPCSubscriber handleEventStreamName:event:]
+ +[CUXPCSubscriber mockEndpointForStreamName:]
+ +[CUXPCSubscriber mockPublisherAdd:streamName:]
+ +[CUXPCSubscriber mockPublisherRemove:streamName:]
+ -[CUNANDataSession _activateWithAutoPairing:]
+ -[CUNANDataSession _autoPairWithCompletion:]
+ -[CUNANDataSession _createPairingMetadata]
+ -[CUNANDataSession autoPairWithCompletion:]
+ -[CUPairingStream exportStateAndReturnError:]
+ -[CUPairingStream initWithState:error:]
+ -[CUSerialPort _readMinLength:maxLength:completionHandler:]
+ -[CUSerialPort _writeBytes:length:completionHandler:]
+ -[CUSerialPort readMinLength:maxLength:completionHandler:]
+ -[CUSerialPort writeData:completionHandler:]
+ -[CUXPCPublisher _mockGetConnection]
+ -[CUXPCSubscriber .cxx_destruct]
+ -[CUXPCSubscriber _mockListenerCreate]
+ -[CUXPCSubscriber _mockReportPublisherAction:token:descriptor:]
+ -[CUXPCSubscriber dealloc]
+ -[CUXPCSubscriber eventHandler]
+ -[CUXPCSubscriber initWithStreamName:dispatchQueue:mock:]
+ -[CUXPCSubscriber mockDescriptor]
+ -[CUXPCSubscriber mockToken]
+ -[CUXPCSubscriber setEventHandler:]
+ -[CUXPCSubscriber setMockDescriptor:]
+ -[CUXPCSubscriber start]
+ -[CUXPCSubscriber stop]
+ -[CUXPCSubscriberStream .cxx_destruct]
+ -[CUXPCSubscriberStream registered]
+ -[CUXPCSubscriberStream setRegistered:]
+ -[CUXPCSubscriberStream setSubscribers:]
+ -[CUXPCSubscriberStream subscribers]
+ GCC_except_table2267
+ GCC_except_table2268
+ GCC_except_table2291
+ GCC_except_table2336
+ GCC_except_table2420
+ GCC_except_table2444
+ GCC_except_table2485
+ GCC_except_table2552
+ GCC_except_table2553
+ GCC_except_table2555
+ GCC_except_table2556
+ GCC_except_table2558
+ GCC_except_table2563
+ GCC_except_table2567
+ GCC_except_table2570
+ GCC_except_table2573
+ GCC_except_table2576
+ GCC_except_table2583
+ GCC_except_table2586
+ GCC_except_table2600
+ GCC_except_table2661
+ GCC_except_table2993
+ GCC_except_table2994
+ GCC_except_table3082
+ GCC_except_table3104
+ GCC_except_table3142
+ GCC_except_table3186
+ GCC_except_table3189
+ GCC_except_table3190
+ GCC_except_table3192
+ GCC_except_table3214
+ GCC_except_table3222
+ GCC_except_table3227
+ GCC_except_table3233
+ GCC_except_table3506
+ GCC_except_table3562
+ GCC_except_table3935
+ GCC_except_table3983
+ GCC_except_table4248
+ GCC_except_table4306
+ GCC_except_table4313
+ GCC_except_table4321
+ GCC_except_table4436
+ GCC_except_table4463
+ GCC_except_table4464
+ GCC_except_table4526
+ GCC_except_table4530
+ GCC_except_table4532
+ GCC_except_table4534
+ GCC_except_table4557
+ GCC_except_table4634
+ GCC_except_table4636
+ GCC_except_table4638
+ GCC_except_table4640
+ GCC_except_table4642
+ GCC_except_table4646
+ GCC_except_table4648
+ GCC_except_table4660
+ GCC_except_table4667
+ GCC_except_table4670
+ GCC_except_table4674
+ GCC_except_table4679
+ GCC_except_table4683
+ GCC_except_table4690
+ GCC_except_table4693
+ GCC_except_table4702
+ GCC_except_table4716
+ GCC_except_table4720
+ GCC_except_table4722
+ GCC_except_table5346
+ GCC_except_table5350
+ GCC_except_table5355
+ GCC_except_table5373
+ GCC_except_table5382
+ GCC_except_table5631
+ GCC_except_table5632
+ GCC_except_table5645
+ _OBJC_CLASS_$_CUXPCSubscriber
+ _OBJC_CLASS_$_CUXPCSubscriberStream
+ _OBJC_IVAR_$_CUNANDataSession._pairOnly
+ _OBJC_IVAR_$_CUPairingStream._decryptKey
+ _OBJC_IVAR_$_CUPairingStream._encryptKey
+ _OBJC_IVAR_$_CUPairingStream._keyLen
+ _OBJC_IVAR_$_CUPairingStream._streamType
+ _OBJC_IVAR_$_CUXPCPublisher._mockConnection
+ _OBJC_IVAR_$_CUXPCSubscriber._dispatchQueue
+ _OBJC_IVAR_$_CUXPCSubscriber._eventHandler
+ _OBJC_IVAR_$_CUXPCSubscriber._mock
+ _OBJC_IVAR_$_CUXPCSubscriber._mockAddReported
+ _OBJC_IVAR_$_CUXPCSubscriber._mockDescriptor
+ _OBJC_IVAR_$_CUXPCSubscriber._mockListener
+ _OBJC_IVAR_$_CUXPCSubscriber._mockToken
+ _OBJC_IVAR_$_CUXPCSubscriber._started
+ _OBJC_IVAR_$_CUXPCSubscriber._streamName
+ _OBJC_IVAR_$_CUXPCSubscriberStream._registered
+ _OBJC_IVAR_$_CUXPCSubscriberStream._subscribers
+ _OBJC_METACLASS_$_CUXPCSubscriber
+ _OBJC_METACLASS_$_CUXPCSubscriberStream
+ __OBJC_$_CLASS_METHODS_CUXPCSubscriber
+ __OBJC_$_INSTANCE_METHODS_CUXPCSubscriber
+ __OBJC_$_INSTANCE_METHODS_CUXPCSubscriberStream
+ __OBJC_$_INSTANCE_VARIABLES_CUXPCSubscriber
+ __OBJC_$_INSTANCE_VARIABLES_CUXPCSubscriberStream
+ __OBJC_$_PROP_LIST_CUXPCSubscriber
+ __OBJC_$_PROP_LIST_CUXPCSubscriberStream
+ __OBJC_CLASS_RO_$_CUXPCSubscriber
+ __OBJC_CLASS_RO_$_CUXPCSubscriberStream
+ __OBJC_METACLASS_RO_$_CUXPCSubscriber
+ __OBJC_METACLASS_RO_$_CUXPCSubscriberStream
+ ___24-[CUXPCSubscriber start]_block_invoke
+ ___27-[CUXPCPublisher _activate]_block_invoke
+ ___36-[CUXPCPublisher _mockGetConnection]_block_invoke
+ ___38-[CUXPCSubscriber _mockListenerCreate]_block_invoke
+ ___38-[CUXPCSubscriber _mockListenerCreate]_block_invoke_2
+ ___43-[CUNANDataSession autoPairWithCompletion:]_block_invoke
+ ___44-[CUSerialPort writeData:completionHandler:]_block_invoke
+ ___47+[CUXPCSubscriber handleEventStreamName:event:]_block_invoke
+ ___58-[CUSerialPort readMinLength:maxLength:completionHandler:]_block_invoke
+ ____readCompletion_block_invoke
+ ____writeCompletion_block_invoke
+ ___block_descriptor_40_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
+ ___block_descriptor_40_e8_32w_e33_v16?0"NSObject<OS_xpc_object>"8lw32l8
+ ___block_descriptor_48_e8_32s40w_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8w40l8
+ ___block_descriptor_64_e8_32s40bs_e5_v8?0ls32l8s40l8
+ __readCompletion
+ __writeCompletion
+ __xpc_error_peer_code_signing_requirement
+ __xpc_error_termination_imminent
+ __xpc_type_connection
+ _cfsetispeed
+ _cfsetospeed
+ _gCUXPCPubSubLock
+ _gCUXPCPublishers
+ _gCUXPCSubscribers
+ _objc_msgSend$_activateWithAutoPairing:
+ _objc_msgSend$_autoPairWithCompletion:
+ _objc_msgSend$_createPairingMetadata
+ _objc_msgSend$_mockGetConnection
+ _objc_msgSend$_mockListenerCreate
+ _objc_msgSend$_mockReportPublisherAction:token:descriptor:
+ _objc_msgSend$_readMinLength:maxLength:completionHandler:
+ _objc_msgSend$_writeBytes:length:completionHandler:
+ _objc_msgSend$eventHandler
+ _objc_msgSend$handleEventStreamName:event:
+ _objc_msgSend$mockDescriptor
+ _objc_msgSend$mockEndpointForStreamName:
+ _objc_msgSend$mockPublisherAdd:streamName:
+ _objc_msgSend$mockPublisherRemove:streamName:
+ _objc_msgSend$mockToken
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$registered
+ _objc_msgSend$reportEventAction:token:descriptor:
+ _objc_msgSend$resetBytesInRange:
+ _objc_msgSend$setRegistered:
+ _objc_msgSend$setSubscribers:
+ _objc_msgSend$subscribers
+ _objc_msgSend$unsignedLongValue
+ _objc_msgSend$wfaAutoPairable
+ _objc_msgSend$wfaPairedUUID
+ _xpc_connection_activate
+ _xpc_connection_create
+ _xpc_connection_create_from_endpoint
+ _xpc_connection_set_target_queue
+ _xpc_endpoint_create
+ _xpc_set_event_stream_handler
- -[CUNANDataSession _activateWithAutoPairing:discoveryResult:]
- -[CUSerialPort _writeLine:completionHandler:]
- -[CUXPCPublisher _reportErrorCode:]
- -[CUXPCPublisher _reportEventAction:token:descriptor:]
- GCC_except_table2263
- GCC_except_table2264
- GCC_except_table2287
- GCC_except_table2332
- GCC_except_table2416
- GCC_except_table2440
- GCC_except_table2477
- GCC_except_table2588
- GCC_except_table2589
- GCC_except_table2591
- GCC_except_table2592
- GCC_except_table2594
- GCC_except_table2599
- GCC_except_table2603
- GCC_except_table2606
- GCC_except_table2609
- GCC_except_table2612
- GCC_except_table2619
- GCC_except_table2622
- GCC_except_table2636
- GCC_except_table2697
- GCC_except_table3027
- GCC_except_table3028
- GCC_except_table3116
- GCC_except_table3172
- GCC_except_table3176
- GCC_except_table3220
- GCC_except_table3223
- GCC_except_table3224
- GCC_except_table3226
- GCC_except_table3249
- GCC_except_table3254
- GCC_except_table3258
- GCC_except_table3533
- GCC_except_table3589
- GCC_except_table3962
- GCC_except_table4010
- GCC_except_table4275
- GCC_except_table4333
- GCC_except_table4340
- GCC_except_table4348
- GCC_except_table4525
- GCC_except_table4529
- GCC_except_table4531
- GCC_except_table4533
- GCC_except_table4556
- GCC_except_table4630
- GCC_except_table4635
- GCC_except_table4637
- GCC_except_table4639
- GCC_except_table4641
- GCC_except_table4645
- GCC_except_table4647
- GCC_except_table4659
- GCC_except_table4666
- GCC_except_table4668
- GCC_except_table4671
- GCC_except_table4675
- GCC_except_table4680
- GCC_except_table4689
- GCC_except_table4691
- GCC_except_table4695
- GCC_except_table4703
- GCC_except_table4717
- GCC_except_table4721
- GCC_except_table5305
- GCC_except_table5309
- GCC_except_table5314
- GCC_except_table5332
- GCC_except_table5341
- GCC_except_table5590
- GCC_except_table5591
- GCC_except_table5604
- ____writeLineCompletion_block_invoke
- ___xpc_connection_send_message_with_reply_f_block_invoke
- ___xpc_connection_set_event_handler_f_block_invoke
- __writeLineCompletion
- _objc_msgSend$_activateWithAutoPairing:discoveryResult:
- _objc_msgSend$_reportErrorCode:
- _objc_msgSend$_reportEventAction:token:descriptor:
- _objc_msgSend$_writeLine:completionHandler:
- _xpc_connection_send_message_with_reply_f
- _xpc_connection_set_event_handler_f
CStrings:
+ "### AutoPair failed: %@"
+ "### read failed: err=%d"
+ "### read line setup failed: error=%@"
+ "### read setup failed: error=%@"
+ "### read start failed: err=%d"
+ "### write failed: err=%d"
+ "### write setup failed: error=%@"
+ "### write start failed: err=%d"
+ "Activate: endpoint=%@, controlFlags=%@, trafficFlags=%@, pair=%s autoPair=%s"
+ "AudioAccessory"
+ "AutoPair: already paired"
+ "AutoPair: endpoint=%@, controlFlags=%@"
+ "AutoPairing not enabled"
+ "AutoPairing required but Peer is not auto-pairable"
+ "BadAuthTagLength"
+ "BadKeyLength"
+ "BadNonceLength"
+ "CUXPCSubscriber"
+ "DecodeStateFailed"
+ "EncodeStateFailed"
+ "MissingStateField"
+ "Peer is not auto-pairable"
+ "Read start failed"
+ "Stream not prepared"
+ "Subscriber start can't retry"
+ "Subscriber start failed after invalidate"
+ "Subscriber start failed after retry max"
+ "Write start failed"
+ "XPC peer code signing requirement not met"
+ "XPC termination imminent"
+ "authTagLen"
+ "decryptKey"
+ "decryptNonce"
+ "encryptKey"
+ "encryptNonce"
+ "handleEvent: streamName=%@, event=%@"
+ "keyType"
+ "read start: minLength=%lu, maxLength=%lu"
+ "read success: length=%zu"
+ "start: streamName=%@, mock=%llu"
+ "stop: streamName=%@, mock=%llu"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
+ "write data start: length=%lu"
+ "write success"
+ "\xf0!"
- "### write line failed: err=%d"
- "### write line start failed: err=%d"
- "Activate: endpoint=%@, controlFlags=%@, trafficFlags=%@, pair=%s"
- "AudioAccessory1,"
- "AudioAccessory5,"
- "AudioAccessory6,"
- "AutoPairing required"
- "Subscriber start failed"
- "Write line start failed"
- "write line failed"
- "write line success"
```
