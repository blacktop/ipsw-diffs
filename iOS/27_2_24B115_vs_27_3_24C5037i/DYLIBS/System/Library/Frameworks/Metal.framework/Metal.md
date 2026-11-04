## Metal

> `/System/Library/Frameworks/Metal.framework/Metal`

```diff

-383.1.2.0.0
-  __TEXT.__text: 0x1e3fc0
+384.5.0.0.0
+  __TEXT.__text: 0x1e43bc
   __TEXT.__objc_methlist: 0x1ee04
   __TEXT.__cstring: 0x237a6
-  __TEXT.__gcc_except_tab: 0xc3fc
+  __TEXT.__gcc_except_tab: 0xc404
   __TEXT.__const: 0x2e620
   __TEXT.__oslogstring: 0x22d7
   __TEXT.__ustring: 0x1be
-  __TEXT.__unwind_info: 0xa190
+  __TEXT.__unwind_info: 0xa198
   __TEXT.__eh_frame: 0x78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13563
-  Symbols:   22588
+  Functions: 13564
+  Symbols:   22597
   CStrings:  4605
 
Symbols:
+ GCC_except_table1003
+ GCC_except_table1006
+ GCC_except_table1015
+ GCC_except_table1019
+ GCC_except_table1025
+ GCC_except_table1041
+ GCC_except_table350
+ GCC_except_table352
+ GCC_except_table361
+ GCC_except_table366
+ GCC_except_table394
+ GCC_except_table425
+ GCC_except_table433
+ GCC_except_table444
+ GCC_except_table466
+ GCC_except_table474
+ GCC_except_table484
+ GCC_except_table487
+ GCC_except_table507
+ GCC_except_table539
+ GCC_except_table556
+ GCC_except_table559
+ GCC_except_table566
+ GCC_except_table571
+ GCC_except_table574
+ GCC_except_table581
+ GCC_except_table589
+ GCC_except_table595
+ GCC_except_table599
+ GCC_except_table602
+ GCC_except_table606
+ GCC_except_table609
+ GCC_except_table623
+ GCC_except_table647
+ GCC_except_table650
+ GCC_except_table655
+ GCC_except_table660
+ GCC_except_table665
+ GCC_except_table680
+ GCC_except_table683
+ GCC_except_table686
+ GCC_except_table691
+ GCC_except_table695
+ GCC_except_table704
+ GCC_except_table724
+ GCC_except_table777
+ GCC_except_table783
+ GCC_except_table790
+ GCC_except_table795
+ GCC_except_table804
+ GCC_except_table807
+ GCC_except_table810
+ GCC_except_table812
+ GCC_except_table820
+ GCC_except_table828
+ GCC_except_table830
+ GCC_except_table849
+ GCC_except_table854
+ GCC_except_table856
+ GCC_except_table861
+ GCC_except_table871
+ GCC_except_table874
+ GCC_except_table879
+ GCC_except_table914
+ GCC_except_table924
+ GCC_except_table935
+ GCC_except_table939
+ GCC_except_table945
+ GCC_except_table949
+ GCC_except_table956
+ GCC_except_table965
+ GCC_except_table976
+ __ZL21enableAIRNTInterfacesP19MTLSchedulerRequestb
- GCC_except_table1001
- GCC_except_table1005
- GCC_except_table1012
- GCC_except_table1018
- GCC_except_table1024
- GCC_except_table1040
- GCC_except_table346
- GCC_except_table355
- GCC_except_table360
- GCC_except_table365
- GCC_except_table393
- GCC_except_table424
- GCC_except_table443
- GCC_except_table465
- GCC_except_table471
- GCC_except_table486
- GCC_except_table506
- GCC_except_table527
- GCC_except_table557
- GCC_except_table572
- GCC_except_table580
- GCC_except_table582
- GCC_except_table587
- GCC_except_table593
- GCC_except_table598
- GCC_except_table600
- GCC_except_table605
- GCC_except_table608
- GCC_except_table622
- GCC_except_table646
- GCC_except_table649
- GCC_except_table652
- GCC_except_table658
- GCC_except_table662
- GCC_except_table678
- GCC_except_table682
- GCC_except_table685
- GCC_except_table689
- GCC_except_table776
- GCC_except_table782
- GCC_except_table789
- GCC_except_table794
- GCC_except_table801
- GCC_except_table805
- GCC_except_table809
- GCC_except_table811
- GCC_except_table827
- GCC_except_table829
- GCC_except_table848
- GCC_except_table853
- GCC_except_table855
- GCC_except_table859
- GCC_except_table870
- GCC_except_table872
- GCC_except_table875
- GCC_except_table912
- GCC_except_table923
- GCC_except_table934
- GCC_except_table938
- GCC_except_table944
- GCC_except_table948
- GCC_except_table953
- GCC_except_table964
- GCC_except_table975
Functions:
~ ____ZN19MTLSchedulerRequest16generateXPCBlockE11qos_class_ti_block_invoke : 3016 -> 3040
~ -[_MTLFunctionInternal newSpecializedFunctionWithDescriptor:destinationArchive:functionCache:sync:compilerTask:completionHandler:] : 2464 -> 2432
~ __ZN20MTLCompilerScheduler24cleanupCancelledRequestsEv : 580 -> 588
~ ____ZN20MTLCompilerScheduler19createBlockWithDataENSt3__110shared_ptrI19MTLSchedulerRequestEE_block_invoke : 464 -> 568
~ -[MTLCompiler compileFunctionRequestInternal:frameworkLinking:linkDataSize:reflectionOnly:compilerTask:completionHandler:] : 9404 -> 9360
~ __ZN20MTLCompilerScheduler12buildRequestEjNSt3__110shared_ptrI18MTLCompilerRequestEEbP11objc_objectU13block_pointerFv16MTLCompilerErrorPU27objcproto16OS_dispatch_data8NSObjectPKcE : 1724 -> 1880
~ __ZN20MTLCompilerScheduler17getBestConnectionERKNSt3__110shared_ptrI19MTLSchedulerRequestEERNS0_11unique_lockINS0_5mutexEEE : 1348 -> 1352
~ __ZNK21MTLCompilerConnection6isIdleEv : 28 -> 32
~ __ZN21MTLCompilerConnection15scheduleRequestEbNSt3__110shared_ptrI19MTLSchedulerRequestEERNS0_11unique_lockINS0_5mutexEEE : 512 -> 672
~ -[MTLCompiler compileBuiltinRequestInternal:compilerTask:completionHandler:] : 1496 -> 1452
~ -[MTLCompiler compileStatelessFunctionRequest:reflectionOnly:compilerTask:completionHandler:] : 3204 -> 3160
~ __ZN17MTLLibraryBuilder17newLibraryWithDAGEP8NSStringP7NSArrayIPU22objcproto11MTLFunction11objc_objectEU13block_pointerFvPU21objcproto10MTLLibrary11objc_objectP7NSErrorEbNSt3__110shared_ptrINSD_6vectorI21stitchedAirDescriptorNSD_9allocatorISG_EEEEEEmPS2_IPU27objcproto16MTLBinaryArchive11objc_objectESM_P11objc_object : 1968 -> 1936
~ __ZN25MTLCompilerBuiltinRequest17serializedRequestEjPPc : 380 -> 408
~ __ZN20MTLCompilerScheduler13insertRequestERKNSt3__110shared_ptrI19MTLSchedulerRequestEE : 108 -> 112
~ __ZN24MTLXPCCompilerConnection8tryBoostERKNSt3__110shared_ptrI19MTLSchedulerRequestEERNS0_11unique_lockINS0_5mutexEEE : 284 -> 392
~ __ZN20MTLCompilerScheduler14RequestCompareclERKNSt3__110shared_ptrI19MTLSchedulerRequestEES6_ : 112 -> 152
~ __ZN20MTLCompilerScheduler32shouldScheduleAfterCompilerBoostERKNSt3__110shared_ptrI19MTLSchedulerRequestEERNS0_11unique_lockINS0_5mutexEEE : 600 -> 680
~ __ZN23MTLCompilerTaskInternal18waitUntilCompletedEv : 404 -> 452
~ -[_MTLBinaryArchive materializeEntryForKey:fileIndex:containsEntry:addEntry:] : 268 -> 264
~ __ZN26MTLLegacyCompilerScheduler12buildRequestEjP18MTLCompilerRequestbP11objc_objectU13block_pointerFv16MTLCompilerErrorPU27objcproto16OS_dispatch_data8NSObjectPKcE : 1320 -> 1360
~ __ZN37MTLLegacyMonolithicCompilerConnection20BuildRequestInternalEP18MTLCompilerRequestPKcPU27objcproto16OS_dispatch_data8NSObjectP11objc_objectU13block_pointerFvjPKvmS3_E : 728 -> 732
~ ____ZN37MTLLegacyMonolithicCompilerConnection20BuildRequestInternalEP18MTLCompilerRequestPKcPU27objcproto16OS_dispatch_data8NSObjectP11objc_objectU13block_pointerFvjPKvmS3_E_block_invoke : 160 -> 164
~ __Z19newLogReplayRequestP18MTLCompilerRequestPKcPU27objcproto16OS_dispatch_data8NSObjecti : 1004 -> 1048
~ __ZN17MTLLibraryBuilder35initLibraryContainerWithRequestDataEP19MTLLibraryContainerR21MTLLibraryRequestDataP11objc_objectU13block_pointerFvvE : 2884 -> 2796
~ __ZL16downgradeRequestPK26MTLCompilerFunctionRequestjPU27objcproto16OS_dispatch_data8NSObjectRK12MTLUINT256_tP11objc_objectU13block_pointerFv16MTLCompilerErrorS4_PKcE : 776 -> 732
+ __ZL21enableAIRNTInterfacesP19MTLSchedulerRequestb
~ -[MTLCompiler generateMachOWithID:binaryEntries:machOSpecializedData:machOType:Path:platform:bitcodeList:compilerTask:completionHandler:] : 4196 -> 4164
~ -[MTLCompiler createBinaryArchiveAsRecompileTarget:compilerTask:completionHandler:] : 640 -> 608
~ -[MTLCompiler compileLibraryRequest:compilerTask:completionHandler:] : 720 -> 676
~ __ZN20MTLCompilerScheduler25handleRequestCancellationERKNSt3__110shared_ptrI19MTLSchedulerRequestEE : 240 -> 336
~ __ZN20MTLCompilerScheduler26tryCancelRequestWithReasonERKNSt3__110shared_ptrI19MTLSchedulerRequestEENS2_12CancelReasonE : 140 -> 148
~ __ZL12boostProcessRKNSt3__110shared_ptrI19MTLSchedulerRequestEERP21MTLCompilerConnectionbbRNS_11unique_lockINS_5mutexEEE : 328 -> 364
~ __ZN30MTLLegacyXPCCompilerConnection20BuildRequestInternalEP18MTLCompilerRequestPKcPU27objcproto16OS_dispatch_data8NSObjectibP11objc_objectU13block_pointerFvjPKvmS3_E : 1408 -> 1420
~ ____ZN30MTLLegacyXPCCompilerConnection20BuildRequestInternalEP18MTLCompilerRequestPKcPU27objcproto16OS_dispatch_data8NSObjectibP11objc_objectU13block_pointerFvjPKvmS3_E_block_invoke : 1152 -> 1156
~ __ZN19MTLSchedulerRequest19newLogReplayRequestERKNSt3__110shared_ptrI18MTLCompilerRequestEEPKcPU27objcproto16OS_dispatch_data8NSObjecti : 1136 -> 1368
~ ____ZN19MTLSchedulerRequest23generateMonolithicBlockE11qos_class_ti_block_invoke : 856 -> 880
~ ____ZN19MTLSchedulerRequest23generateMonolithicBlockE11qos_class_ti_block_invoke.10 : 320 -> 328
```
