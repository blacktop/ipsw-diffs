## SpringBoardFoundation

> `/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`

```diff

-4416.25.105.0.0
-  __TEXT.__text: 0x90274
+4416.39.103.0.0
+  __TEXT.__text: 0x8c9bc
   __TEXT.__auth_stubs: 0x1800
-  __TEXT.__objc_methlist: 0x70d4
+  __TEXT.__objc_methlist: 0x6cbc
   __TEXT.__const: 0x1d04
-  __TEXT.__cstring: 0xc30a
-  __TEXT.__gcc_except_tab: 0x698
+  __TEXT.__cstring: 0xc1d6
+  __TEXT.__gcc_except_tab: 0x580
   __TEXT.__dlopen_cstrs: 0x4d2
   __TEXT.__oslogstring: 0x2f41
   __TEXT.__ustring: 0x2e4
-  __TEXT.__unwind_info: 0x2084
-  __TEXT.__objc_classname: 0x1972
-  __TEXT.__objc_methname: 0x16d2d
-  __TEXT.__objc_methtype: 0x334e
-  __TEXT.__objc_stubs: 0xd6c0
+  __TEXT.__unwind_info: 0x1ec4
+  __TEXT.__objc_classname: 0x186e
+  __TEXT.__objc_methname: 0x16831
+  __TEXT.__objc_methtype: 0x310d
+  __TEXT.__objc_stubs: 0xd240
   __DATA_CONST.__got: 0x428
-  __DATA_CONST.__const: 0x1a80
-  __DATA_CONST.__objc_classlist: 0x618
+  __DATA_CONST.__const: 0x1880
+  __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x1b8
+  __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x16e28
-  __DATA_CONST.__objc_selrefs: 0x4a40
+  __DATA_CONST.__objc_const: 0x15390
+  __DATA_CONST.__objc_selrefs: 0x48c0
   __DATA_CONST.__objc_arraydata: 0x4f0
-  __AUTH_CONST.__cfstring: 0xa300
-  __AUTH_CONST.__objc_const: 0x4638
+  __AUTH_CONST.__cfstring: 0xa240
+  __AUTH_CONST.__objc_const: 0x4200
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x228
-  __AUTH_CONST.__const: 0xcc0
+  __AUTH_CONST.__const: 0xc00
   __AUTH_CONST.__objc_doubleobj: 0x4d0
   __AUTH_CONST.__auth_got: 0xc10
-  __AUTH.__objc_data: 0x38e0
+  __AUTH.__objc_data: 0x34d0
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x7b0
-  __DATA.__objc_superrefs: 0x360
-  __DATA.__objc_ivar: 0x970
-  __DATA.__data: 0x1942
-  __DATA.__bss: 0x370
+  __DATA.__objc_classrefs: 0x758
+  __DATA.__objc_superrefs: 0x318
+  __DATA.__objc_ivar: 0x910
+  __DATA.__data: 0x17c2
+  __DATA.__bss: 0x340
   __DATA.__common: 0x0
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x160

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0A6C633A-3109-30ED-8EB6-DE47AB2F0500
-  Functions: 3250
-  Symbols:   11695
-  CStrings:  7894
+  UUID: 1E3DA519-CDDD-3EE9-A880-7DEE72489CEC
+  Functions: 3141
+  Symbols:   11244
+  CStrings:  7781
 
Symbols:
- +[SBFCancelationToken tokenWithCancelationBlock:]
- +[SBFCancelationToken tokenWrappingCancelable:]
- +[SBFObservable forkJoin:]
- +[SBFObservable observableWithBlock:]
- +[SBFObserver observerWithResultBlock:]
- +[SBFObserver observerWithResultBlock:completionBlock:failureBlock:]
- +[SBFObserver sendArray:error:toObserver:]
- +[SBFObserver sendObserver:resultsOfBlock:]
- +[SBFScheduler globalAsyncScheduler]
- +[SBFScheduler immediateScheduler]
- +[SBFScheduler mainScheduler]
- -[SBFCancelationToken .cxx_destruct]
- -[SBFCancelationToken addCancelationBlock:]
- -[SBFCancelationToken callCancelationBlocks:]
- -[SBFCancelationToken cancel]
- -[SBFCancelationToken init]
- -[SBFCancelationToken isCanceled]
- -[SBFCancelationToken nts_cancel]
- -[SBFObservable generate:]
- -[SBFObservable map:]
- -[SBFObservable observeOn:]
- -[SBFObservable subscribe:]
- -[SBFObservable subscribeOn:]
- -[SBFObservable subscribeWithResultBlock:]
- -[SBFObservable subscribeWithResultBlock:completionBlock:failureBlock:]
- -[SBFObservable throttle:onScheduler:]
- -[SBFObservable waitForResults:]
- -[SBFSubject .cxx_destruct]
- -[SBFSubject _observers]
- -[SBFSubject init]
- -[SBFSubject observerDidComplete]
- -[SBFSubject observerDidFailWithError:]
- -[SBFSubject observerDidReceiveResult:]
- -[SBFSubject subscribe:]
- -[_SBFAccumulatingObserver .cxx_destruct]
- -[_SBFAccumulatingObserver init]
- -[_SBFAccumulatingObserver observerDidComplete]
- -[_SBFAccumulatingObserver observerDidFailWithError:]
- -[_SBFAccumulatingObserver observerDidReceiveResult:]
- -[_SBFAccumulatingObserver waitForResults:]
- -[_SBFBlockObservable .cxx_destruct]
- -[_SBFBlockObservable initWithBlock:]
- -[_SBFBlockObservable subscribe:]
- -[_SBFBlockObserver .cxx_destruct]
- -[_SBFBlockObserver initWithResultBlock:completionBlock:failureBlock:]
- -[_SBFBlockObserver observerDidComplete]
- -[_SBFBlockObserver observerDidFailWithError:]
- -[_SBFBlockObserver observerDidReceiveResult:]
- -[_SBFForkJoinObservable .cxx_destruct]
- -[_SBFForkJoinObservable _observableFinishedForObserver:]
- -[_SBFForkJoinObservable _setResult:atIndex:]
- -[_SBFForkJoinObservable initWithWithObservables:]
- -[_SBFForkJoinObservable subscribe:]
- -[_SBFImmediateScheduler afterDelay:performBlock:]
- -[_SBFImmediateScheduler performBlock:]
- -[_SBFImmediateScheduler performCancelableBlock:]
- -[_SBFQueueScheduler .cxx_destruct]
- -[_SBFQueueScheduler afterDelay:performBlock:]
- -[_SBFQueueScheduler initWithQueue:]
- -[_SBFQueueScheduler performBlock:]
- -[_SBFQueueScheduler performCancelableBlock:]
- -[_SBFScheduledObservable .cxx_destruct]
- -[_SBFScheduledObservable initWithObservable:scheduler:]
- -[_SBFScheduledObservable subscribe:]
- -[_SBFThrottledObservable .cxx_destruct]
- -[_SBFThrottledObservable _cancel]
- -[_SBFThrottledObservable _clearResult]
- -[_SBFThrottledObservable _sendCompletionToObsever:]
- -[_SBFThrottledObservable _sendResultToObserver:withIdentifier:]
- -[_SBFThrottledObservable _setDelayToken:]
- -[_SBFThrottledObservable _setResult:]
- -[_SBFThrottledObservable dealloc]
- -[_SBFThrottledObservable initWithInterval:observable:scheduler:]
- -[_SBFThrottledObservable subscribe:]
- GCC_except_table17
- GCC_except_table18
- GCC_except_table31
- GCC_except_table33
- GCC_except_table5
- OBJC_IVAR_$__SBFAccumulatingObserver._didComplete
- OBJC_IVAR_$__SBFAccumulatingObserver._error
- OBJC_IVAR_$__SBFAccumulatingObserver._results
- OBJC_IVAR_$__SBFAccumulatingObserver._semaphore
- OBJC_IVAR_$__SBFBlockObservable._block
- OBJC_IVAR_$__SBFBlockObserver._completionBlock
- OBJC_IVAR_$__SBFBlockObserver._failureBlock
- OBJC_IVAR_$__SBFBlockObserver._resultBlock
- OBJC_IVAR_$__SBFForkJoinObservable._observables
- OBJC_IVAR_$__SBFForkJoinObservable._results
- OBJC_IVAR_$__SBFForkJoinObservable._uncompletedObservableCount
- OBJC_IVAR_$__SBFScheduledObservable._observable
- OBJC_IVAR_$__SBFScheduledObservable._scheduler
- OBJC_IVAR_$__SBFThrottledObservable._delayToken
- OBJC_IVAR_$__SBFThrottledObservable._hasResult
- OBJC_IVAR_$__SBFThrottledObservable._interval
- OBJC_IVAR_$__SBFThrottledObservable._observable
- OBJC_IVAR_$__SBFThrottledObservable._result
- OBJC_IVAR_$__SBFThrottledObservable._resultCounter
- OBJC_IVAR_$__SBFThrottledObservable._scheduler
- _OBJC_CLASS_$_SBFCancelationToken
- _OBJC_CLASS_$_SBFObservable
- _OBJC_CLASS_$_SBFObserver
- _OBJC_CLASS_$_SBFScheduler
- _OBJC_CLASS_$_SBFSubject
- _OBJC_CLASS_$__SBFAccumulatingObserver
- _OBJC_CLASS_$__SBFBlockObservable
- _OBJC_CLASS_$__SBFBlockObserver
- _OBJC_CLASS_$__SBFForkJoinObservable
- _OBJC_CLASS_$__SBFImmediateScheduler
- _OBJC_CLASS_$__SBFQueueScheduler
- _OBJC_CLASS_$__SBFScheduledObservable
- _OBJC_CLASS_$__SBFThrottledObservable
- _OBJC_IVAR_$_SBFCancelationToken._cancelationBlocks
- _OBJC_IVAR_$_SBFCancelationToken._isCanceled
- _OBJC_IVAR_$_SBFSubject._observers
- _OBJC_IVAR_$__SBFQueueScheduler._queue
- _OBJC_METACLASS_$_SBFCancelationToken
- _OBJC_METACLASS_$_SBFObservable
- _OBJC_METACLASS_$_SBFObserver
- _OBJC_METACLASS_$_SBFScheduler
- _OBJC_METACLASS_$_SBFSubject
- _OBJC_METACLASS_$__SBFAccumulatingObserver
- _OBJC_METACLASS_$__SBFBlockObservable
- _OBJC_METACLASS_$__SBFBlockObserver
- _OBJC_METACLASS_$__SBFForkJoinObservable
- _OBJC_METACLASS_$__SBFImmediateScheduler
- _OBJC_METACLASS_$__SBFQueueScheduler
- _OBJC_METACLASS_$__SBFScheduledObservable
- _OBJC_METACLASS_$__SBFThrottledObservable
- _SBFNullCompletionBlock_block_invoke_2
- _SBFNullFailureBlock_block_invoke_3
- _SBFNullResultBlock_block_invoke
- __OBJC_$_CLASS_METHODS_SBFCancelationToken
- __OBJC_$_CLASS_METHODS_SBFObservable
- __OBJC_$_CLASS_METHODS_SBFObserver
- __OBJC_$_CLASS_METHODS_SBFScheduler
- __OBJC_$_INSTANCE_METHODS_SBFCancelationToken
- __OBJC_$_INSTANCE_METHODS_SBFObservable
- __OBJC_$_INSTANCE_METHODS_SBFSubject
- __OBJC_$_INSTANCE_METHODS__SBFAccumulatingObserver
- __OBJC_$_INSTANCE_METHODS__SBFBlockObservable
- __OBJC_$_INSTANCE_METHODS__SBFBlockObserver
- __OBJC_$_INSTANCE_METHODS__SBFForkJoinObservable
- __OBJC_$_INSTANCE_METHODS__SBFImmediateScheduler
- __OBJC_$_INSTANCE_METHODS__SBFQueueScheduler
- __OBJC_$_INSTANCE_METHODS__SBFScheduledObservable
- __OBJC_$_INSTANCE_METHODS__SBFThrottledObservable
- __OBJC_$_INSTANCE_VARIABLES_SBFCancelationToken
- __OBJC_$_INSTANCE_VARIABLES_SBFSubject
- __OBJC_$_INSTANCE_VARIABLES__SBFAccumulatingObserver
- __OBJC_$_INSTANCE_VARIABLES__SBFBlockObservable
- __OBJC_$_INSTANCE_VARIABLES__SBFBlockObserver
- __OBJC_$_INSTANCE_VARIABLES__SBFForkJoinObservable
- __OBJC_$_INSTANCE_VARIABLES__SBFQueueScheduler
- __OBJC_$_INSTANCE_VARIABLES__SBFScheduledObservable
- __OBJC_$_INSTANCE_VARIABLES__SBFThrottledObservable
- __OBJC_$_PROP_LIST_SBFCancelationToken
- __OBJC_$_PROP_LIST_SBFObservable
- __OBJC_$_PROP_LIST_SBFSubject
- __OBJC_$_PROP_LIST__SBFAccumulatingObserver
- __OBJC_$_PROP_LIST__SBFBlockObserver
- __OBJC_$_PROP_LIST__SBFImmediateScheduler
- __OBJC_$_PROP_LIST__SBFQueueScheduler
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBFCancelable
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBFObservable
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBFObserver
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBFScheduler
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBFCancelable
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBFObservable
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBFObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBFScheduler
- __OBJC_$_PROTOCOL_REFS_SBFCancelable
- __OBJC_$_PROTOCOL_REFS_SBFObservable
- __OBJC_$_PROTOCOL_REFS_SBFObserver
- __OBJC_$_PROTOCOL_REFS_SBFScheduler
- __OBJC_CLASS_PROTOCOLS_$_SBFCancelationToken
- __OBJC_CLASS_PROTOCOLS_$_SBFObservable
- __OBJC_CLASS_PROTOCOLS_$_SBFSubject
- __OBJC_CLASS_PROTOCOLS_$__SBFAccumulatingObserver
- __OBJC_CLASS_PROTOCOLS_$__SBFBlockObserver
- __OBJC_CLASS_PROTOCOLS_$__SBFImmediateScheduler
- __OBJC_CLASS_PROTOCOLS_$__SBFQueueScheduler
- __OBJC_CLASS_RO_$_SBFCancelationToken
- __OBJC_CLASS_RO_$_SBFObservable
- __OBJC_CLASS_RO_$_SBFObserver
- __OBJC_CLASS_RO_$_SBFScheduler
- __OBJC_CLASS_RO_$_SBFSubject
- __OBJC_CLASS_RO_$__SBFAccumulatingObserver
- __OBJC_CLASS_RO_$__SBFBlockObservable
- __OBJC_CLASS_RO_$__SBFBlockObserver
- __OBJC_CLASS_RO_$__SBFForkJoinObservable
- __OBJC_CLASS_RO_$__SBFImmediateScheduler
- __OBJC_CLASS_RO_$__SBFQueueScheduler
- __OBJC_CLASS_RO_$__SBFScheduledObservable
- __OBJC_CLASS_RO_$__SBFThrottledObservable
- __OBJC_LABEL_PROTOCOL_$_SBFCancelable
- __OBJC_LABEL_PROTOCOL_$_SBFObservable
- __OBJC_LABEL_PROTOCOL_$_SBFObserver
- __OBJC_LABEL_PROTOCOL_$_SBFScheduler
- __OBJC_METACLASS_RO_$_SBFCancelationToken
- __OBJC_METACLASS_RO_$_SBFObservable
- __OBJC_METACLASS_RO_$_SBFObserver
- __OBJC_METACLASS_RO_$_SBFScheduler
- __OBJC_METACLASS_RO_$_SBFSubject
- __OBJC_METACLASS_RO_$__SBFAccumulatingObserver
- __OBJC_METACLASS_RO_$__SBFBlockObservable
- __OBJC_METACLASS_RO_$__SBFBlockObserver
- __OBJC_METACLASS_RO_$__SBFForkJoinObservable
- __OBJC_METACLASS_RO_$__SBFImmediateScheduler
- __OBJC_METACLASS_RO_$__SBFQueueScheduler
- __OBJC_METACLASS_RO_$__SBFScheduledObservable
- __OBJC_METACLASS_RO_$__SBFThrottledObservable
- __OBJC_PROTOCOL_$_SBFCancelable
- __OBJC_PROTOCOL_$_SBFObservable
- __OBJC_PROTOCOL_$_SBFObserver
- __OBJC_PROTOCOL_$_SBFScheduler
- ___21-[SBFObservable map:]_block_invoke
- ___21-[SBFObservable map:]_block_invoke_2
- ___21-[SBFObservable map:]_block_invoke_3
- ___21-[SBFObservable map:]_block_invoke_4
- ___24-[SBFSubject subscribe:]_block_invoke
- ___26-[SBFObservable generate:]_block_invoke
- ___27-[SBFObservable observeOn:]_block_invoke
- ___27-[SBFObservable observeOn:]_block_invoke_2
- ___27-[SBFObservable observeOn:]_block_invoke_3
- ___27-[SBFObservable observeOn:]_block_invoke_4
- ___27-[SBFObservable observeOn:]_block_invoke_5
- ___27-[SBFObservable observeOn:]_block_invoke_6
- ___27-[SBFObservable observeOn:]_block_invoke_7
- ___29+[SBFScheduler mainScheduler]_block_invoke
- ___34+[SBFScheduler immediateScheduler]_block_invoke
- ___35-[_SBFQueueScheduler performBlock:]_block_invoke
- ___36+[SBFScheduler globalAsyncScheduler]_block_invoke
- ___36-[_SBFForkJoinObservable subscribe:]_block_invoke
- ___36-[_SBFForkJoinObservable subscribe:]_block_invoke_2
- ___36-[_SBFForkJoinObservable subscribe:]_block_invoke_3
- ___36-[_SBFForkJoinObservable subscribe:]_block_invoke_4
- ___37-[_SBFScheduledObservable subscribe:]_block_invoke
- ___37-[_SBFScheduledObservable subscribe:]_block_invoke_2
- ___37-[_SBFThrottledObservable subscribe:]_block_invoke
- ___37-[_SBFThrottledObservable subscribe:]_block_invoke_2
- ___37-[_SBFThrottledObservable subscribe:]_block_invoke_3
- ___37-[_SBFThrottledObservable subscribe:]_block_invoke_4
- ___37-[_SBFThrottledObservable subscribe:]_block_invoke_5
- ___37-[_SBFThrottledObservable subscribe:]_block_invoke_6
- ___45-[_SBFQueueScheduler performCancelableBlock:]_block_invoke
- ___46-[_SBFQueueScheduler afterDelay:performBlock:]_block_invoke
- ___47+[SBFCancelationToken tokenWrappingCancelable:]_block_invoke
- ___block_descriptor_32_e8_v16?08l
- ___block_descriptor_40_e8_32bs_e8_16?08ls32l8
- ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_48_e8_32s40bs_e40_"<SBFCancelable>"16?0"<SBFObserver>"8ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e8_v16?08ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e29_v16?0"SBFCancelationToken"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e40_"<SBFCancelable>"16?0"<SBFObserver>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e8_v16?08ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
- ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_48_e8_32w_e8_v16?08lw32l8
- ___block_descriptor_56_e8_32s40s48w_e8_v16?08lw48l8s32l8s40l8
- ___block_literal_global.3
- ___block_literal_global.65
- ___block_literal_global.68
- _globalAsyncScheduler.sbf_once_object_1
- _globalAsyncScheduler.sbf_once_token_1
- _immediateScheduler.sbf_once_object_0
- _immediateScheduler.sbf_once_token_0
- _mainScheduler.sbf_once_object_2
- _mainScheduler.sbf_once_token_2
- _objc_msgSend$_cancel
- _objc_msgSend$_clearResult
- _objc_msgSend$_observableFinishedForObserver:
- _objc_msgSend$_observers
- _objc_msgSend$_sendCompletionToObsever:
- _objc_msgSend$_sendResultToObserver:withIdentifier:
- _objc_msgSend$_setDelayToken:
- _objc_msgSend$_setResult:
- _objc_msgSend$_setResult:atIndex:
- _objc_msgSend$addCancelationBlock:
- _objc_msgSend$afterDelay:performBlock:
- _objc_msgSend$callCancelationBlocks:
- _objc_msgSend$cancel
- _objc_msgSend$initWithBlock:
- _objc_msgSend$initWithInterval:observable:scheduler:
- _objc_msgSend$initWithObservable:scheduler:
- _objc_msgSend$initWithQueue:
- _objc_msgSend$initWithResultBlock:completionBlock:failureBlock:
- _objc_msgSend$initWithWithObservables:
- _objc_msgSend$isCanceled
- _objc_msgSend$map:
- _objc_msgSend$nts_cancel
- _objc_msgSend$observableWithBlock:
- _objc_msgSend$observerDidComplete
- _objc_msgSend$observerDidFailWithError:
- _objc_msgSend$observerDidReceiveResult:
- _objc_msgSend$observerWithResultBlock:completionBlock:failureBlock:
- _objc_msgSend$performBlock:
- _objc_msgSend$performCancelableBlock:
- _objc_msgSend$replaceObjectAtIndex:withObject:
- _objc_msgSend$sendArray:error:toObserver:
- _objc_msgSend$sleepForTimeInterval:
- _objc_msgSend$subscribe:
- _objc_msgSend$subscribeWithResultBlock:completionBlock:failureBlock:
- _objc_msgSend$tokenWithCancelationBlock:
- _objc_msgSend$waitForResults:
CStrings:
- "@\"<SBFCancelable>\""
- "@\"<SBFCancelable>\"16@?0@\"<SBFObserver>\"8"
- "@\"<SBFCancelable>\"24@0:8@\"<SBFObserver>\"16"
- "@\"<SBFCancelable>\"24@0:8@?<v@?>16"
- "@\"<SBFCancelable>\"24@0:8@?<v@?@\"SBFCancelationToken\">16"
- "@\"<SBFCancelable>\"24@0:8@?<v@?@>16"
- "@\"<SBFCancelable>\"32@0:8d16@?<v@?>24"
- "@\"<SBFCancelable>\"40@0:8@?<v@?@>16@?<v@?>24@?<v@?@\"NSError\">32"
- "@\"<SBFObservable>\""
- "@\"<SBFObservable>\"24@0:8@\"<SBFScheduler>\"16"
- "@\"<SBFObservable>\"24@0:8@?<@@?>16"
- "@\"<SBFObservable>\"24@0:8@?<@@?@>16"
- "@\"<SBFObservable>\"32@0:8d16@\"<SBFScheduler>\"24"
- "@\"<SBFScheduler>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@16@?0@8"
- "@24@0:8^@16"
- "@32@0:8d16@24"
- "@32@0:8d16@?24"
- "@40@0:8d16@24@32"
- "ACMRequirement - ACMRequirementDataRatchet"
- "Got result when already complete"
- "Received null generate block"
- "Received null or empty observable array"
- "Received null transform block"
- "SBFCancelable"
- "SBFCancelationToken"
- "SBFObservable"
- "SBFObservable.m"
- "SBFObserver"
- "SBFScheduler"
- "SBFSubject"
- "_SBFAccumulatingObserver"
- "_SBFBlockObservable"
- "_SBFBlockObserver"
- "_SBFForkJoinObservable"
- "_SBFImmediateScheduler"
- "_SBFQueueScheduler"
- "_SBFScheduledObservable"
- "_SBFThrottledObservable"
- "_block"
- "_cancel"
- "_cancelationBlocks"
- "_clearResult"
- "_completionBlock"
- "_delayToken"
- "_didComplete"
- "_failureBlock"
- "_hasResult"
- "_interval"
- "_isCanceled"
- "_observable"
- "_observableFinishedForObserver:"
- "_observables"
- "_resultBlock"
- "_resultCounter"
- "_results"
- "_scheduler"
- "_semaphore"
- "_sendCompletionToObsever:"
- "_sendResultToObserver:withIdentifier:"
- "_setDelayToken:"
- "_setResult:"
- "_setResult:atIndex:"
- "_uncompletedObservableCount"
- "addCancelationBlock:"
- "afterDelay:performBlock:"
- "callCancelationBlocks:"
- "cancel"
- "forkJoin:"
- "generate:"
- "globalAsyncScheduler"
- "immediateScheduler"
- "initWithBlock:"
- "initWithInterval:observable:scheduler:"
- "initWithObservable:scheduler:"
- "initWithQueue:"
- "initWithResultBlock:completionBlock:failureBlock:"
- "initWithWithObservables:"
- "isCanceled"
- "mainScheduler"
- "map:"
- "nts_cancel"
- "observableWithBlock:"
- "observeOn:"
- "observerDidComplete"
- "observerDidFailWithError:"
- "observerDidReceiveResult:"
- "observerWithResultBlock:"
- "observerWithResultBlock:completionBlock:failureBlock:"
- "performBlock:"
- "performCancelableBlock:"
- "replaceObjectAtIndex:withObject:"
- "sendArray:error:toObserver:"
- "sendObserver:resultsOfBlock:"
- "sleepForTimeInterval:"
- "subscribe:"
- "subscribe: must be override"
- "subscribeOn:"
- "subscribeWithResultBlock:"
- "subscribeWithResultBlock:completionBlock:failureBlock:"
- "throttle:onScheduler:"
- "tokenWithCancelationBlock:"
- "tokenWrappingCancelable:"
- "v16@?0@\"SBFCancelationToken\"8"
- "v16@?0@8"
- "waitForResults:"

```
