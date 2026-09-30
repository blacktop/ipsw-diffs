## CoreUtils

> `/System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils`

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
- `__DATA_DIRTY.__data`

```diff

-900.48.0.0.0
-  __TEXT.__text: 0x11cb78
-  __TEXT.__objc_methlist: 0xa1a8
-  __TEXT.__cstring: 0x1e231
+900.55.0.0.0
+  __TEXT.__text: 0x11f6d0
+  __TEXT.__objc_methlist: 0xa318
+  __TEXT.__cstring: 0x1e3fc
   __TEXT.__const: 0x22dc
-  __TEXT.__gcc_except_tab: 0x1a3c
-  __TEXT.__oslogstring: 0x471e
-  __TEXT.__unwind_info: 0x38a8
+  __TEXT.__gcc_except_tab: 0x1ac8
+  __TEXT.__oslogstring: 0x48bd
+  __TEXT.__unwind_info: 0x3910
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1550
-  __DATA_CONST.__objc_classlist: 0x340
+  __DATA_CONST.__const: 0x1510
+  __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x52b0
+  __DATA_CONST.__objc_selrefs: 0x5360
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x238
+  __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x658
-  __AUTH_CONST.__const: 0x4008
-  __AUTH_CONST.__cfstring: 0x3fa0
-  __AUTH_CONST.__objc_const: 0x13af0
+  __DATA_CONST.__got: 0x678
+  __AUTH_CONST.__const: 0x40e8
+  __AUTH_CONST.__cfstring: 0x4020
+  __AUTH_CONST.__objc_const: 0x13ea0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1580
-  __AUTH.__objc_data: 0x1d88
+  __AUTH_CONST.__auth_got: 0x15c0
+  __AUTH.__objc_data: 0x1e28
   __AUTH.__data: 0xa18
-  __DATA.__objc_ivar: 0x14fc
+  __DATA.__objc_ivar: 0x1540
   __DATA.__data: 0x2f50
-  __DATA.__bss: 0x11a0
+  __DATA.__bss: 0x11c8
   __DATA.__common: 0x2a
   __DATA_DIRTY.__objc_data: 0x2f8
   __DATA_DIRTY.__data: 0xa8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5788
-  Symbols:   11551
-  CStrings:  4846
+  Functions: 5827
+  Symbols:   11663
+  CStrings:  4880
 
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
+ GCC_except_table2302
+ GCC_except_table2303
+ GCC_except_table2326
+ GCC_except_table2372
+ GCC_except_table2456
+ GCC_except_table2480
+ GCC_except_table2521
+ GCC_except_table2588
+ GCC_except_table2589
+ GCC_except_table2591
+ GCC_except_table2592
+ GCC_except_table2594
+ GCC_except_table2599
+ GCC_except_table2603
+ GCC_except_table2606
+ GCC_except_table2609
+ GCC_except_table2612
+ GCC_except_table2619
+ GCC_except_table2622
+ GCC_except_table2636
+ GCC_except_table2697
+ GCC_except_table3029
+ GCC_except_table3030
+ GCC_except_table3089
+ GCC_except_table3160
+ GCC_except_table3164
+ GCC_except_table3208
+ GCC_except_table3211
+ GCC_except_table3212
+ GCC_except_table3214
+ GCC_except_table3236
+ GCC_except_table3244
+ GCC_except_table3249
+ GCC_except_table3255
+ GCC_except_table3520
+ GCC_except_table3570
+ GCC_except_table3958
+ GCC_except_table4006
+ GCC_except_table4331
+ GCC_except_table4339
+ GCC_except_table4347
+ GCC_except_table4462
+ GCC_except_table4489
+ GCC_except_table4490
+ GCC_except_table4554
+ GCC_except_table4558
+ GCC_except_table4560
+ GCC_except_table4562
+ GCC_except_table4585
+ GCC_except_table4660
+ GCC_except_table4662
+ GCC_except_table4664
+ GCC_except_table4666
+ GCC_except_table4668
+ GCC_except_table4670
+ GCC_except_table4674
+ GCC_except_table4676
+ GCC_except_table4688
+ GCC_except_table4700
+ GCC_except_table4705
+ GCC_except_table4709
+ GCC_except_table4710
+ GCC_except_table4711
+ GCC_except_table4721
+ GCC_except_table4731
+ GCC_except_table4745
+ GCC_except_table4749
+ GCC_except_table4751
+ GCC_except_table4753
+ GCC_except_table5381
+ GCC_except_table5385
+ GCC_except_table5390
+ GCC_except_table5408
+ GCC_except_table5417
+ GCC_except_table5666
+ GCC_except_table5667
+ GCC_except_table5680
+ OBJC_IVAR_$_CUNANDataSession._pairOnly
+ OBJC_IVAR_$_CUPairingStream._decryptKey
+ OBJC_IVAR_$_CUPairingStream._encryptKey
+ OBJC_IVAR_$_CUPairingStream._keyLen
+ OBJC_IVAR_$_CUPairingStream._streamType
+ OBJC_IVAR_$_CUXPCPublisher._mockConnection
+ OBJC_IVAR_$_CUXPCSubscriber._dispatchQueue
+ OBJC_IVAR_$_CUXPCSubscriber._eventHandler
+ OBJC_IVAR_$_CUXPCSubscriber._mock
+ OBJC_IVAR_$_CUXPCSubscriber._mockAddReported
+ OBJC_IVAR_$_CUXPCSubscriber._mockDescriptor
+ OBJC_IVAR_$_CUXPCSubscriber._mockListener
+ OBJC_IVAR_$_CUXPCSubscriber._mockToken
+ OBJC_IVAR_$_CUXPCSubscriber._started
+ OBJC_IVAR_$_CUXPCSubscriber._streamName
+ OBJC_IVAR_$_CUXPCSubscriberStream._registered
+ OBJC_IVAR_$_CUXPCSubscriberStream._subscribers
+ _OBJC_CLASS_$_CUXPCSubscriber
+ _OBJC_CLASS_$_CUXPCSubscriberStream
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
+ ___block_descriptor_40_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_40_e8_32w_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_48_e8_32s40w_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_64_e8_32s40bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40w
+ ___destroy_helper_block_e8_32s40w
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
- GCC_except_table2298
- GCC_except_table2299
- GCC_except_table2322
- GCC_except_table2368
- GCC_except_table2452
- GCC_except_table2476
- GCC_except_table2513
- GCC_except_table2624
- GCC_except_table2625
- GCC_except_table2627
- GCC_except_table2628
- GCC_except_table2630
- GCC_except_table2635
- GCC_except_table2639
- GCC_except_table2642
- GCC_except_table2645
- GCC_except_table2648
- GCC_except_table2655
- GCC_except_table2658
- GCC_except_table2672
- GCC_except_table2733
- GCC_except_table3063
- GCC_except_table3064
- GCC_except_table3123
- GCC_except_table3194
- GCC_except_table3198
- GCC_except_table3242
- GCC_except_table3245
- GCC_except_table3246
- GCC_except_table3248
- GCC_except_table3271
- GCC_except_table3276
- GCC_except_table3280
- GCC_except_table3547
- GCC_except_table3597
- GCC_except_table3985
- GCC_except_table4033
- GCC_except_table4358
- GCC_except_table4366
- GCC_except_table4374
- GCC_except_table4551
- GCC_except_table4555
- GCC_except_table4557
- GCC_except_table4559
- GCC_except_table4582
- GCC_except_table4656
- GCC_except_table4657
- GCC_except_table4658
- GCC_except_table4663
- GCC_except_table4665
- GCC_except_table4667
- GCC_except_table4671
- GCC_except_table4673
- GCC_except_table4685
- GCC_except_table4692
- GCC_except_table4694
- GCC_except_table4699
- GCC_except_table4703
- GCC_except_table4708
- GCC_except_table4716
- GCC_except_table4718
- GCC_except_table4726
- GCC_except_table4727
- GCC_except_table4734
- GCC_except_table4748
- GCC_except_table5338
- GCC_except_table5342
- GCC_except_table5347
- GCC_except_table5365
- GCC_except_table5374
- GCC_except_table5623
- GCC_except_table5624
- GCC_except_table5637
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
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xb5pO4/Sources/CoreUtils/CoreUtils/TestUtils.c"
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
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.k3OEc7/Sources/CoreUtils/CoreUtils/TestUtils.c"
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
