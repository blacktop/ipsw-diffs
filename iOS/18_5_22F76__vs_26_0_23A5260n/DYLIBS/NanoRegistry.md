## NanoRegistry

> `/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry`

```diff

-989.21.0.0.0
-  __TEXT.__text: 0x51e34
+1027.4.0.0.0
+  __TEXT.__text: 0x53a50
   __TEXT.__auth_stubs: 0x930
-  __TEXT.__objc_methlist: 0x4974
+  __TEXT.__objc_methlist: 0x499c
   __TEXT.__const: 0xd4
-  __TEXT.__cstring: 0x3f14
-  __TEXT.__gcc_except_tab: 0xea8
+  __TEXT.__cstring: 0x40a7
+  __TEXT.__gcc_except_tab: 0xe98
   __TEXT.__oslogstring: 0x1fee
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1900
+  __TEXT.__unwind_info: 0x1938
   __TEXT.__objc_classname: 0x8e3
-  __TEXT.__objc_methname: 0x742f
-  __TEXT.__objc_methtype: 0x1483
-  __TEXT.__objc_stubs: 0x51c0
-  __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x1d88
+  __TEXT.__objc_methname: 0x751e
+  __TEXT.__objc_methtype: 0x145e
+  __TEXT.__objc_stubs: 0x5260
+  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__const: 0x1dc8
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d78
+  __DATA_CONST.__objc_selrefs: 0x1db0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0xc0
   __AUTH_CONST.__auth_got: 0x4b0
   __AUTH_CONST.__const: 0xb20
-  __AUTH_CONST.__cfstring: 0x48e0
-  __AUTH_CONST.__objc_const: 0x6d40
+  __AUTH_CONST.__cfstring: 0x4a40
+  __AUTH_CONST.__objc_const: 0x6d58
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EFCBB2C1-4DAB-3840-AD2E-6E945D91D504
-  Functions: 2049
-  Symbols:   6437
-  CStrings:  2965
+  UUID: E91DBFAC-05B5-3D80-9F45-3FA729095BB9
+  Functions: 2064
+  Symbols:   6472
+  CStrings:  2999
 
Symbols:
+ -[NRPairedDeviceRegistry listWatchStagedForTransferWithCompletion:]
+ -[NRPairedDeviceRegistry stageWatchForGraduationWithDeviceID:completion:]
+ -[NRPairedDeviceRegistry stageWatchForTransferWithDeviceID:completion:]
+ -[NRPairingProxy xpcListWatchStagedForTransferWithCompletion:]
+ -[NRPairingProxy xpcStageWatchForGraduationWithDeviceID:completion:]
+ -[NRPairingProxy xpcStageWatchForTransferWithDeviceID:completion:]
+ GCC_except_table115
+ GCC_except_table215
+ GCC_except_table220
+ GCC_except_table248
+ GCC_except_table289
+ GCC_except_table30
+ GCC_except_table351
+ GCC_except_table361
+ GCC_except_table364
+ GCC_except_table367
+ GCC_except_table388
+ GCC_except_table75
+ GCC_except_table93
+ _NRDevicePropertyIsStagedForTransfer
+ _NRDevicePropertyRunnableArchNames
+ _NRDevicePropertyTransferType
+ _NRWatchTransferredAndGraduatedDarwinNotification
+ _NSPOSIXErrorDomain
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne200100Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZnwmSt19__type_descriptor_t
+ ___45-[NRPairingProxy xpcSetWatchNeedsGraduation:]_block_invoke.192
+ ___50-[NRPairingProxy xpcAbortPairingReason:withBlock:]_block_invoke.206
+ ___51-[NRPairingProxy xpcWatchBuddyCompletedSetupSteps:]_block_invoke.193
+ ___62-[NRPairingProxy xpcListWatchStagedForTransferWithCompletion:]_block_invoke
+ ___62-[NRPairingProxy xpcListWatchStagedForTransferWithCompletion:]_block_invoke_2
+ ___66-[NRPairingProxy xpcStageWatchForTransferWithDeviceID:completion:]_block_invoke
+ ___66-[NRPairingProxy xpcStageWatchForTransferWithDeviceID:completion:]_block_invoke_2
+ ___67-[NRPairedDeviceRegistry listWatchStagedForTransferWithCompletion:]_block_invoke
+ ___67-[NRPairedDeviceRegistry listWatchStagedForTransferWithCompletion:]_block_invoke_2
+ ___68-[NRPairingProxy xpcStageWatchForGraduationWithDeviceID:completion:]_block_invoke
+ ___68-[NRPairingProxy xpcStageWatchForGraduationWithDeviceID:completion:]_block_invoke_2
+ ___71-[NRPairedDeviceRegistry stageWatchForTransferWithDeviceID:completion:]_block_invoke
+ ___71-[NRPairedDeviceRegistry stageWatchForTransferWithDeviceID:completion:]_block_invoke_2
+ ___71-[NRPairedDeviceRegistry stageWatchForTransferWithDeviceID:completion:]_block_invoke_3
+ ___73-[NRPairedDeviceRegistry stageWatchForGraduationWithDeviceID:completion:]_block_invoke
+ ___73-[NRPairedDeviceRegistry stageWatchForGraduationWithDeviceID:completion:]_block_invoke_2
+ ___73-[NRPairedDeviceRegistry stageWatchForGraduationWithDeviceID:completion:]_block_invoke_3
+ ___block_literal_global.172
+ ___block_literal_global.180
+ ___block_literal_global.182
+ ___block_literal_global.353
+ ___block_literal_global.355
+ ___block_literal_global.357
+ ___block_literal_global.359
+ ___block_literal_global.361
+ ___block_literal_global.363
+ ___block_literal_global.423
+ ___block_literal_global.425
+ ___block_literal_global.432
+ ___block_literal_global.435
+ ___block_literal_global.437
+ ___block_literal_global.440
+ ___block_literal_global.620
+ ___block_literal_global.644
+ ___block_literal_global.648
+ ___block_literal_global.699
+ _objc_msgSend$_setError
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
+ _objc_msgSend$xpcListWatchStagedForTransferWithCompletion:
+ _objc_msgSend$xpcStageWatchForGraduationWithDeviceID:completion:
+ _objc_msgSend$xpcStageWatchForTransferWithDeviceID:completion:
- -[NRPairedDeviceRegistry _]
- -[NRRegistryClient _grabRegistryWithWriteBlockAsync:]
- -[NRRegistryClient _queryDataAsyncIfNeededWithBlock:]
- -[NRSecureDevicePropertyID .cxx_destruct]
- GCC_except_table121
- GCC_except_table219
- GCC_except_table222
- GCC_except_table250
- GCC_except_table291
- GCC_except_table342
- GCC_except_table349
- GCC_except_table352
- GCC_except_table355
- GCC_except_table379
- GCC_except_table77
- GCC_except_table80
- GCC_except_table86
- GCC_except_table89
- GCC_except_table97
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___27-[NRPairedDeviceRegistry _]_block_invoke
- ___45-[NRPairingProxy xpcSetWatchNeedsGraduation:]_block_invoke.188
- ___50-[NRPairingProxy xpcAbortPairingReason:withBlock:]_block_invoke.202
- ___51-[NRPairingProxy xpcWatchBuddyCompletedSetupSteps:]_block_invoke.189
- ___block_literal_global.168
- ___block_literal_global.176
- ___block_literal_global.178
- ___block_literal_global.354
- ___block_literal_global.356
- ___block_literal_global.358
- ___block_literal_global.360
- ___block_literal_global.362
- ___block_literal_global.364
- ___block_literal_global.415
- ___block_literal_global.417
- ___block_literal_global.424
- ___block_literal_global.431
- ___block_literal_global.433
- ___block_literal_global.436
- ___block_literal_global.614
- ___block_literal_global.636
- ___block_literal_global.638
- ___block_literal_global.693
- _objc_msgSend$_grabRegistryWithWriteBlockAsync:
- _objc_msgSend$_queryDataAsyncIfNeededWithBlock:
- _objc_msgSend$_warnAboutMissingEntitlement
CStrings:
+ "-[NRPairedDeviceRegistry listWatchStagedForTransferWithCompletion:]"
+ "-[NRPairedDeviceRegistry stageWatchForGraduationWithDeviceID:completion:]"
+ "-[NRPairedDeviceRegistry stageWatchForTransferWithDeviceID:completion:]"
+ "19"
+ "20"
+ "Feature not enabled"
+ "Invalid argument"
+ "UUIDData"
+ "[16C]"
+ "_setError"
+ "com.apple.nanoregistry.watchtransferredandgraduated"
+ "featureNotEnabled"
+ "getBytes:range:"
+ "hasError"
+ "invalidArgument"
+ "isStagedForTransfer"
+ "listWatchStagedForTransferWithCompletion:"
+ "position"
+ "runnableArchNames"
+ "setPosition:"
+ "stageWatchForGraduationWithDeviceID:completion:"
+ "stageWatchForTransferWithDeviceID:completion:"
+ "transferType"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "xpcListWatchStagedForTransferWithCompletion:"
+ "xpcStageWatchForGraduationWithDeviceID:completion:"
+ "xpcStageWatchForTransferWithDeviceID:completion:"
+ "{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}"
- "_"
- "_grabRegistryWithWriteBlockAsync:"
- "_queryDataAsyncIfNeededWithBlock:"
- "_warnAboutMissingEntitlement"
- "{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__end_cap_\"{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=\"__value_\"^I}}"

```
