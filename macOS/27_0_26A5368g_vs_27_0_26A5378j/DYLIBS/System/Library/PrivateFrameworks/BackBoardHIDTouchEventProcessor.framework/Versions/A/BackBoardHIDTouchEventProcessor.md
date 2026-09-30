## BackBoardHIDTouchEventProcessor

> `/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/Versions/A/BackBoardHIDTouchEventProcessor`

```diff

-  __TEXT.__text: 0x3b6a8
-  __TEXT.__objc_methlist: 0x2888
+  __TEXT.__text: 0x3c180
+  __TEXT.__objc_methlist: 0x27b8
   __TEXT.__const: 0x400
   __TEXT.__constg_swiftt: 0x124
   __TEXT.__swift5_typeref: 0x164

   __TEXT.__swift5_fieldmd: 0xfc
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__cstring: 0x1e3f
+  __TEXT.__cstring: 0x1e1e
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x3be0
-  __TEXT.__oslogstring: 0x291f
+  __TEXT.__gcc_except_tab: 0x3cd0
+  __TEXT.__oslogstring: 0x2c0d
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1300
+  __TEXT.__unwind_info: 0x1308
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x558
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x118
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a98
-  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_selrefs: 0x1ab0
+  __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x530
-  __AUTH_CONST.__const: 0x1880
-  __AUTH_CONST.__cfstring: 0x2040
-  __AUTH_CONST.__objc_const: 0x6fe8
+  __DATA_CONST.__got: 0x560
+  __AUTH_CONST.__const: 0x18e0
+  __AUTH_CONST.__cfstring: 0x1fe0
+  __AUTH_CONST.__objc_const: 0x6ef8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x6b8
   __AUTH.__objc_data: 0xa28
   __AUTH.__data: 0xb8
-  __DATA.__objc_ivar: 0x554
-  __DATA.__data: 0xd28
+  __DATA.__objc_ivar: 0x548
+  __DATA.__data: 0xcc8
   __DATA.__bss: 0xf8
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0xbe0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1111
-  Symbols:   3515
-  CStrings:  818
+  Functions: 1118
+  Symbols:   3526
+  CStrings:  822
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ +[BKTouchDestination destinationWithHitTestTargetID:clientTaskName:clientConnectionIdentifier:]
+ -[BKDirectTouchState ensureHitTestDestinationExistsForTargetID:clientTaskName:clientConnectionIdentifier:]
+ -[BKDirectTouchStateHitTester _addDestinationForTargetID:clientTaskName:clientConnectionIdentifier:toHostingChain:]
+ -[BKHIDEventHitTestDispatcher sendEvent:forTargetID:toClientConnectionIdentifier:]
+ -[BKTargetDestination clientConnectionIdentifier]
+ -[BKTargetDestination initWithTargetID:clientTaskName:clientConnectionIdentifier:]
+ -[BKTargetDestination setClientConnectionIdentifier:]
+ -[BKTouchDeliveryObservationManagerServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:]
+ -[BKTouchDestination initWithHitTestTargetID:clientTaskName:clientConnectionIdentifier:]
+ -[BKTouchEventServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:]
+ -[BKTouchStreamServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:]
+ -[_BKTouchServerClientRecord init]
+ GCC_except_table1027
+ GCC_except_table1032
+ GCC_except_table1035
+ GCC_except_table1036
+ GCC_except_table1037
+ GCC_except_table1038
+ GCC_except_table1040
+ GCC_except_table210
+ GCC_except_table211
+ GCC_except_table212
+ GCC_except_table222
+ GCC_except_table223
+ GCC_except_table224
+ GCC_except_table228
+ GCC_except_table234
+ GCC_except_table235
+ GCC_except_table242
+ GCC_except_table244
+ GCC_except_table256
+ GCC_except_table257
+ GCC_except_table270
+ GCC_except_table272
+ GCC_except_table277
+ GCC_except_table278
+ GCC_except_table279
+ GCC_except_table331
+ GCC_except_table332
+ GCC_except_table339
+ GCC_except_table340
+ GCC_except_table341
+ GCC_except_table362
+ GCC_except_table364
+ GCC_except_table366
+ GCC_except_table371
+ GCC_except_table372
+ GCC_except_table379
+ GCC_except_table383
+ GCC_except_table390
+ GCC_except_table394
+ GCC_except_table401
+ GCC_except_table402
+ GCC_except_table403
+ GCC_except_table407
+ GCC_except_table415
+ GCC_except_table417
+ GCC_except_table425
+ GCC_except_table427
+ GCC_except_table436
+ GCC_except_table438
+ GCC_except_table443
+ GCC_except_table445
+ GCC_except_table450
+ GCC_except_table458
+ GCC_except_table462
+ GCC_except_table463
+ GCC_except_table470
+ GCC_except_table471
+ GCC_except_table472
+ GCC_except_table484
+ GCC_except_table486
+ GCC_except_table488
+ GCC_except_table559
+ GCC_except_table603
+ GCC_except_table631
+ GCC_except_table647
+ GCC_except_table648
+ GCC_except_table651
+ GCC_except_table679
+ GCC_except_table734
+ GCC_except_table742
+ GCC_except_table745
+ GCC_except_table750
+ GCC_except_table753
+ GCC_except_table755
+ GCC_except_table758
+ GCC_except_table764
+ GCC_except_table770
+ GCC_except_table773
+ GCC_except_table777
+ GCC_except_table783
+ GCC_except_table785
+ GCC_except_table789
+ GCC_except_table808
+ GCC_except_table936
+ OBJC_IVAR_$_BKTargetDestination._clientConnectionIdentifier
+ OBJC_IVAR_$__BKTouchDeliveryObservationConnectionRecord._domainServiceServer
+ _BKGetCurrentDirectTouchEventProcessor
+ _BKGetCurrentDisplayRenderSpace
+ _BKGetCurrentTouchDeliveryObservationManager
+ _BKSetCurrentDirectTouchEventProcessor
+ _BKSetCurrentDisplayRenderSpace
+ _BKSetCurrentTouchDeliveryObservationManager
+ _OBJC_CLASS_$_BKHIDDomainClientCalloutContextualizer
+ __95-[BKTouchEventServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:]_block_invoke
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKHIDEventHitTestDispatcher
+ ___95-[BKTouchEventServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:]_block_invoke
+ ___block_descriptor_72_e8_32bs40bs48r56r64r_e5_8?0l
+ ___block_descriptor_72_e8_32s40bs48r56r64r_e8_v16?08l
+ ___copy_helper_block_e8_32b40b48r56r64r
+ ___copy_helper_block_e8_32s40b48r56r64r
+ ___destroy_helper_block_e8_32s40s48r56r64r
+ _objc_msgSend$_contextualizerWrappingClientProvidedContextualizer:connection:getCurrent:setCurrent:
+ _objc_msgSend$acceptConnectionUsingServiceQueue:clientCalloutContextualizer:
+ _objc_msgSend$clientConnectionIdentifier
+ _objc_msgSend$contextualizedMappedObjectFetcher
+ _objc_msgSend$getClientTaskNamePort:clientConnectionIdentifier:forTargetID:displayUUID:
+ _objc_msgSend$initWithTargetID:clientTaskName:clientConnectionIdentifier:
+ _objc_msgSend$sendEvent:forTargetID:toClientConnectionIdentifier:
+ _objc_msgSend$setSetupBlock:
+ _objc_msgSend$setTeardownBlock:
+ _objc_msgSend$setupBlock
+ _objc_msgSend$teardownBlock
- +[BKTouchDestination destinationWithHitTestTargetID:clientTaskName:]
- -[BKDirectTouchState ensureHitTestDestinationExistsForTargetID:clientTaskName:]
- -[BKDirectTouchStateHitTester _addDestinationForTargetID:clientTaskName:toHostingChain:]
- -[BKHIDEventHitTestDispatcher sendEvent:toClientTaskName:toTargetID:]
- -[BKTouchDeliveryObservationManagerServer _managerForConnection:]
- -[BKTouchDeliveryObservationManagerServer acceptIncomingServiceConnection:mappedObject:]
- -[BKTouchDestination initWithHitTestTargetID:clientTaskName:]
- -[BKTouchEventServer acceptIncomingServiceConnection:mappedObject:]
- -[BKTouchStreamClientRecord .cxx_destruct]
- -[BKTouchStreamClientRecord setTouchProcessor:]
- -[BKTouchStreamClientRecord touchProcessor]
- -[BKTouchStreamServer acceptIncomingServiceConnection:mappedObject:]
- GCC_except_table1020
- GCC_except_table1025
- GCC_except_table1028
- GCC_except_table1029
- GCC_except_table1030
- GCC_except_table1031
- GCC_except_table1033
- GCC_except_table214
- GCC_except_table215
- GCC_except_table216
- GCC_except_table225
- GCC_except_table226
- GCC_except_table231
- GCC_except_table238
- GCC_except_table239
- GCC_except_table248
- GCC_except_table249
- GCC_except_table250
- GCC_except_table260
- GCC_except_table262
- GCC_except_table273
- GCC_except_table275
- GCC_except_table282
- GCC_except_table284
- GCC_except_table286
- GCC_except_table334
- GCC_except_table335
- GCC_except_table348
- GCC_except_table352
- GCC_except_table356
- GCC_except_table368
- GCC_except_table369
- GCC_except_table376
- GCC_except_table377
- GCC_except_table384
- GCC_except_table386
- GCC_except_table388
- GCC_except_table393
- GCC_except_table400
- GCC_except_table404
- GCC_except_table409
- GCC_except_table414
- GCC_except_table418
- GCC_except_table419
- GCC_except_table420
- GCC_except_table433
- GCC_except_table434
- GCC_except_table439
- GCC_except_table444
- GCC_except_table449
- GCC_except_table456
- GCC_except_table457
- GCC_except_table461
- GCC_except_table465
- GCC_except_table466
- GCC_except_table474
- GCC_except_table478
- GCC_except_table482
- GCC_except_table489
- GCC_except_table491
- GCC_except_table493
- GCC_except_table561
- GCC_except_table605
- GCC_except_table633
- GCC_except_table649
- GCC_except_table658
- GCC_except_table663
- GCC_except_table681
- GCC_except_table729
- GCC_except_table735
- GCC_except_table744
- GCC_except_table746
- GCC_except_table751
- GCC_except_table754
- GCC_except_table756
- GCC_except_table760
- GCC_except_table765
- GCC_except_table771
- GCC_except_table775
- GCC_except_table779
- GCC_except_table784
- GCC_except_table786
- GCC_except_table807
- GCC_except_table821
- OBJC_IVAR_$_BKTouchStreamClientRecord._touchProcessor
- OBJC_IVAR_$__BKTouchDeliveryObservationConnectionRecord._observationManager
- OBJC_IVAR_$__BKTouchServerClientRecord._clientManager
- OBJC_IVAR_$__BKTouchServerClientRecord._renderSpace
- OBJC_IVAR_$__BKTouchServerClientRecord._touchProcessor
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKDisplayRenderSpace
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKHIDEventHitTestDispatcher
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKDisplayRenderSpace
- __OBJC_$_PROTOCOL_METHOD_TYPES_BKDisplayRenderSpace
- __OBJC_$_PROTOCOL_REFS_BKDisplayRenderSpace
- __OBJC_LABEL_PROTOCOL_$_BKDisplayRenderSpace
- __OBJC_PROTOCOL_$_BKDisplayRenderSpace
- __OBJC_PROTOCOL_REFERENCE_$_BKDisplayRenderSpace
- _objc_msgSend$_managerForConnection:
- _objc_msgSend$acceptConnection
- _objc_msgSend$conformsToProtocol:
- _objc_msgSend$domainServiceServer
- _objc_msgSend$setTouchProcessor:
- _objc_msgSend$touchProcessor
CStrings:
+ "\""
+ "-[BKTouchEventServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:]_block_invoke"
+ "BKHIDClientCalloutContextualizerSetupBlock for %@ stashed info with no teardownBlock to clean it up!"
+ "Failed to create touch stream for for client: %{public}@ - no current touch processor"
+ "Failed to update dispatch mode for client: %{public}@ - no current touch processor"
+ "clientConnectionIdentifier"
+ "not sending queued updates to: %{public}@ - server is gone"
+ "pid:%d failed to observe kinds:%{public}@ identifier:%X - no manager available"
+ "post updates: %{public}@ and bg update: %{public}@ to: %{public}@"
+ "process '%{public}@' failed to look up CA transforms - no render space available"
+ "process:%{public}@ (ctx:%{public}@) failed to observe background touches - token:%llu contexts:%{public}@ timestamp:%f - no manager available"
+ "process:%{public}@ (ctx:%{public}@) failed to observe general kinds:%{public}@ - no manager available"
+ "process:%{public}@ (ctx:%{public}@) failed to stop observing background touches - token:%llu - no manager available"
- "connection %@ is missing touch event processor"
- "failed to find touch observation manager for existing connection: %@"
- "failed to provide touch observation manager for incoming connection: %@"
- "failed to provide touch processor for incoming connection: %@"
- "post updates:%{public}@ and bg update:@{public}%@ to:%{public}@"
- "renderSpace != nil"

```
