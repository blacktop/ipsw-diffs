## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

-3610.11.1.0.0
-  __TEXT.__text: 0xcfbac
-  __TEXT.__objc_methlist: 0xe100
-  __TEXT.__const: 0x1078
+3610.19.5.0.0
+  __TEXT.__text: 0xd1568
+  __TEXT.__objc_methlist: 0xe2e0
+  __TEXT.__const: 0x1088
   __TEXT.__dlopen_cstrs: 0x24a
   __TEXT.__constg_swiftt: 0x2cc
   __TEXT.__swift5_typeref: 0x1dc
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x30
-  __TEXT.__cstring: 0x17563
+  __TEXT.__cstring: 0x17805
   __TEXT.__swift5_reflstr: 0x278
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_fieldmd: 0x250
   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x3e84
-  __TEXT.__oslogstring: 0x12d4c
-  __TEXT.__unwind_info: 0x4c88
+  __TEXT.__gcc_except_tab: 0x3eec
+  __TEXT.__oslogstring: 0x131e2
+  __TEXT.__unwind_info: 0x4d10
   __TEXT.__eh_frame: 0x270
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x29f0
-  __DATA_CONST.__objc_classlist: 0x778
+  __DATA_CONST.__objc_classlist: 0x790
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x230
+  __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x78a8
+  __DATA_CONST.__objc_selrefs: 0x79e0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x590
+  __DATA_CONST.__objc_superrefs: 0x598
   __DATA_CONST.__objc_arraydata: 0x1c8
-  __DATA_CONST.__got: 0x1068
-  __AUTH_CONST.__const: 0x1be0
-  __AUTH_CONST.__cfstring: 0x9f60
-  __AUTH_CONST.__objc_const: 0x15920
+  __DATA_CONST.__got: 0x1088
+  __AUTH_CONST.__const: 0x1c20
+  __AUTH_CONST.__cfstring: 0xa0c0
+  __AUTH_CONST.__objc_const: 0x15d08
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_floatobj: 0x1a0
-  __AUTH_CONST.__auth_got: 0xfe8
-  __AUTH.__objc_data: 0x358
-  __DATA.__objc_ivar: 0xe44
-  __DATA.__data: 0x1ac0
+  __AUTH_CONST.__auth_got: 0x1008
+  __AUTH.__objc_data: 0x448
+  __DATA.__objc_ivar: 0xe70
+  __DATA.__data: 0x1b20
   __DATA_DIRTY.__objc_data: 0x4810
   __DATA_DIRTY.__data: 0x2e8
   __DATA_DIRTY.__bss: 0x668

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5410
-  Symbols:   10136
-  CStrings:  3923
+  Functions: 5447
+  Symbols:   10220
+  CStrings:  3952
 
Symbols:
+ +[CSConfig audioProviderRetainedChannelBitsetForNumChannels:]
+ +[CSConfig audioProviderRetainedChannelBitsetForNumChannels:isHorseman:isPebble:horsemanDeviceType:pruningDisabled:fullRingDumpEnabled:]
+ +[CSFOnDeviceCachedIrPurgingUtils purgeCachedIrForAssetExcludingCurrentAsset:baseCachedIrDir:]
+ +[CSFOnDeviceCachedIrPurgingUtils removeCachedIrsForModelType:]
+ +[CSOnDeviceCompilationUtils onDeviceCompilationQueue]
+ +[CSUtils isAttendingOSDQuietModeEnabled]
+ +[CSUtils shouldReuseLiveEmbeddingForCCProfile]
+ -[CSAsset _optimizedOSDConfigPath]
+ -[CSAsset _osdConfigPathForLinwoodEnabled:]
+ -[CSAsset osdConfigPath]
+ -[CSAudioCircularBuffer initWithNumChannels:recordingDuration:samplingRate:audioTimeConverter:retainedChannelMask:]
+ -[CSAudioCircularBuffer numRetainedChannels]
+ -[CSAudioCircularBuffer prunedChannelReadCount]
+ -[CSAudioProvider isExclaveCursorRewindPending]
+ -[CSAudioProvider setIsExclaveCursorRewindPending:]
+ -[CSExclaveRecordClient setRaiseToSpeakDeviceOrientation:]
+ -[CSFMil2bnnsCompilationConfig _setOptionsFromDictionary:]
+ -[CSFPreferences isAudioProviderRingBufferPruningDisabled]
+ -[CSRequestMutex acquisitionTime]
+ -[CSRequestMutexAnalyticsEventManager .cxx_destruct]
+ -[CSRequestMutexAnalyticsEventManager _mhIdForTrackedRequest:requestId:mhId:requester:]
+ -[CSRequestMutexAnalyticsEventManager _trackedRequestForRequestId:]
+ -[CSRequestMutexAnalyticsEventManager acquisitionRefusedForRequestId:mhId:requester:resourceType:snapshot:]
+ -[CSRequestMutexAnalyticsEventManager acquisitionSucceededForRequestId:mhId:requester:resourceType:]
+ -[CSRequestMutexAnalyticsEventManager initWithEmitter:capacity:]
+ -[CSRequestMutexAnalyticsEventManager init]
+ -[CSRequestMutexAnalyticsSELFEmitter _emitMutexRequested:forMhId:]
+ -[CSRequestMutexAnalyticsSELFEmitter _mutexRequestedForRequester:requestedResourceType:successfullyAcquired:]
+ -[CSRequestMutexAnalyticsSELFEmitter emitFirstAcquisitionForMhId:requester:requestedResourceType:]
+ -[CSRequestMutexAnalyticsSELFEmitter emitFirstRefusalForMhId:requester:requestedResourceType:snapshot:]
+ -[CSRequestMutexController _acquisitionSnapshotAtHostTime:]
+ -[CSRequestMutexController _reportAcquisitionForOwner:requestId:mhId:resourceType:succeeded:snapshot:]
+ -[CSRequestMutexController initWithSingleTenancyEnforced:analyticsEventManager:]
+ -[CSRequestMutexController tryAcquireForLocalWithRequestId:mhId:resourceType:]
+ -[CSRequestMutexController tryAcquireForOwner:requestId:mhId:resourceType:]
+ -[CSRequestMutexTrackedRequest .cxx_destruct]
+ -[CSRequestMutexTrackedRequest acquired]
+ -[CSRequestMutexTrackedRequest mhId]
+ -[CSRequestMutexTrackedRequest refused]
+ -[CSRequestMutexTrackedRequest setAcquired:]
+ -[CSRequestMutexTrackedRequest setMhId:]
+ -[CSRequestMutexTrackedRequest setRefused:]
+ -[CSUncompressedAudioLogging _removeAudioFile]
+ GCC_except_table1382
+ GCC_except_table1413
+ GCC_except_table1503
+ GCC_except_table1504
+ GCC_except_table1505
+ GCC_except_table1506
+ GCC_except_table1507
+ GCC_except_table1508
+ GCC_except_table1517
+ GCC_except_table1520
+ GCC_except_table1528
+ GCC_except_table1532
+ GCC_except_table1534
+ GCC_except_table1536
+ GCC_except_table1540
+ GCC_except_table1552
+ GCC_except_table1945
+ GCC_except_table1946
+ GCC_except_table1950
+ GCC_except_table1953
+ GCC_except_table1956
+ GCC_except_table1962
+ GCC_except_table1971
+ GCC_except_table1972
+ GCC_except_table1987
+ GCC_except_table1993
+ GCC_except_table2081
+ GCC_except_table2086
+ GCC_except_table2151
+ GCC_except_table2163
+ GCC_except_table2205
+ GCC_except_table2208
+ GCC_except_table2209
+ GCC_except_table2217
+ GCC_except_table2229
+ GCC_except_table2236
+ GCC_except_table2279
+ GCC_except_table2297
+ GCC_except_table2380
+ GCC_except_table2492
+ GCC_except_table2527
+ GCC_except_table2700
+ GCC_except_table2704
+ GCC_except_table2783
+ GCC_except_table2796
+ GCC_except_table2801
+ GCC_except_table2803
+ GCC_except_table2823
+ GCC_except_table2825
+ GCC_except_table2843
+ GCC_except_table2864
+ GCC_except_table2911
+ GCC_except_table2915
+ GCC_except_table2968
+ GCC_except_table2970
+ GCC_except_table2971
+ GCC_except_table3141
+ GCC_except_table3282
+ GCC_except_table3290
+ GCC_except_table3298
+ GCC_except_table3308
+ GCC_except_table3312
+ GCC_except_table3314
+ GCC_except_table3315
+ GCC_except_table3351
+ GCC_except_table3357
+ GCC_except_table3421
+ GCC_except_table3425
+ GCC_except_table3480
+ GCC_except_table3496
+ GCC_except_table3503
+ GCC_except_table3515
+ GCC_except_table3539
+ GCC_except_table3540
+ GCC_except_table3541
+ GCC_except_table3542
+ GCC_except_table3567
+ GCC_except_table3580
+ GCC_except_table3775
+ GCC_except_table3849
+ GCC_except_table3891
+ GCC_except_table3892
+ GCC_except_table3921
+ GCC_except_table3922
+ GCC_except_table3924
+ GCC_except_table3927
+ GCC_except_table3928
+ GCC_except_table3929
+ GCC_except_table3953
+ GCC_except_table3960
+ GCC_except_table3961
+ GCC_except_table3962
+ GCC_except_table3970
+ GCC_except_table3996
+ GCC_except_table4022
+ GCC_except_table4043
+ GCC_except_table4063
+ GCC_except_table4064
+ GCC_except_table4065
+ GCC_except_table4066
+ GCC_except_table4076
+ GCC_except_table4168
+ GCC_except_table4189
+ GCC_except_table4190
+ GCC_except_table4191
+ GCC_except_table4194
+ GCC_except_table4196
+ GCC_except_table4207
+ GCC_except_table4215
+ GCC_except_table4223
+ GCC_except_table4224
+ GCC_except_table4225
+ GCC_except_table4227
+ GCC_except_table4228
+ GCC_except_table4229
+ GCC_except_table4231
+ GCC_except_table4232
+ GCC_except_table4234
+ GCC_except_table4235
+ GCC_except_table4236
+ GCC_except_table4237
+ GCC_except_table4265
+ GCC_except_table427
+ GCC_except_table4315
+ GCC_except_table4319
+ GCC_except_table4370
+ GCC_except_table4371
+ GCC_except_table4378
+ GCC_except_table4379
+ GCC_except_table4380
+ GCC_except_table4381
+ GCC_except_table4383
+ GCC_except_table4384
+ GCC_except_table4405
+ GCC_except_table4407
+ GCC_except_table4408
+ GCC_except_table4409
+ GCC_except_table4411
+ GCC_except_table4412
+ GCC_except_table4413
+ GCC_except_table4414
+ GCC_except_table4416
+ GCC_except_table4417
+ GCC_except_table4418
+ GCC_except_table4442
+ GCC_except_table4444
+ GCC_except_table4447
+ GCC_except_table4449
+ GCC_except_table4451
+ GCC_except_table4453
+ GCC_except_table4455
+ GCC_except_table4456
+ GCC_except_table4458
+ GCC_except_table4460
+ GCC_except_table4463
+ GCC_except_table4465
+ GCC_except_table4467
+ GCC_except_table4469
+ GCC_except_table4476
+ GCC_except_table4490
+ GCC_except_table4492
+ GCC_except_table4493
+ GCC_except_table4497
+ GCC_except_table4498
+ GCC_except_table4499
+ GCC_except_table4504
+ GCC_except_table4506
+ GCC_except_table4510
+ GCC_except_table4511
+ GCC_except_table4541
+ GCC_except_table4702
+ GCC_except_table4709
+ GCC_except_table4792
+ GCC_except_table4870
+ GCC_except_table4880
+ GCC_except_table4936
+ GCC_except_table4937
+ GCC_except_table4938
+ GCC_except_table4940
+ GCC_except_table4941
+ GCC_except_table4942
+ GCC_except_table4943
+ GCC_except_table4944
+ GCC_except_table4946
+ GCC_except_table4948
+ GCC_except_table4949
+ GCC_except_table4951
+ GCC_except_table4953
+ GCC_except_table4954
+ GCC_except_table4956
+ GCC_except_table4992
+ GCC_except_table5058
+ GCC_except_table5063
+ GCC_except_table5104
+ GCC_except_table512
+ GCC_except_table513
+ GCC_except_table5170
+ GCC_except_table548
+ GCC_except_table588
+ GCC_except_table593
+ GCC_except_table611
+ GCC_except_table679
+ GCC_except_table683
+ GCC_except_table688
+ GCC_except_table690
+ GCC_except_table853
+ GCC_except_table860
+ GCC_except_table923
+ GCC_except_table924
+ GCC_except_table931
+ GCC_except_table932
+ GCC_except_table947
+ GCC_except_table948
+ GCC_except_table954
+ GCC_except_table959
+ GCC_except_table968
+ GCC_except_table969
+ GCC_except_table970
+ GCC_except_table984
+ _OBJC_CLASS_$_CSRequestMutexAnalyticsEventManager
+ _OBJC_CLASS_$_CSRequestMutexAnalyticsSELFEmitter
+ _OBJC_CLASS_$_CSRequestMutexTrackedRequest
+ _OBJC_CLASS_$_MHSchemaMHMutexRequested
+ _OBJC_IVAR_$_CSAsset._didResolveOptimizedOSDConfigPath
+ _OBJC_IVAR_$_CSAsset._optimizedOSDConfigPath
+ _OBJC_IVAR_$_CSAudioProvider._isExclaveCursorRewindPending
+ _OBJC_IVAR_$_CSRequestMutex._acquisitionTime
+ _OBJC_IVAR_$_CSRequestMutexAnalyticsEventManager._capacity
+ _OBJC_IVAR_$_CSRequestMutexAnalyticsEventManager._emitter
+ _OBJC_IVAR_$_CSRequestMutexAnalyticsEventManager._lock
+ _OBJC_IVAR_$_CSRequestMutexAnalyticsEventManager._trackedRequestIdsInInsertionOrder
+ _OBJC_IVAR_$_CSRequestMutexAnalyticsEventManager._trackedRequests
+ _OBJC_IVAR_$_CSRequestMutexController._analyticsEventManager
+ _OBJC_IVAR_$_CSRequestMutexTrackedRequest._acquired
+ _OBJC_IVAR_$_CSRequestMutexTrackedRequest._mhId
+ _OBJC_IVAR_$_CSRequestMutexTrackedRequest._refused
+ _OBJC_METACLASS_$_CSRequestMutexAnalyticsEventManager
+ _OBJC_METACLASS_$_CSRequestMutexAnalyticsSELFEmitter
+ _OBJC_METACLASS_$_CSRequestMutexTrackedRequest
+ __OBJC_$_INSTANCE_METHODS_CSRequestMutexAnalyticsEventManager
+ __OBJC_$_INSTANCE_METHODS_CSRequestMutexAnalyticsSELFEmitter
+ __OBJC_$_INSTANCE_METHODS_CSRequestMutexTrackedRequest
+ __OBJC_$_INSTANCE_VARIABLES_CSRequestMutexAnalyticsEventManager
+ __OBJC_$_INSTANCE_VARIABLES_CSRequestMutexTrackedRequest
+ __OBJC_$_PROP_LIST_CSRequestMutexAnalyticsSELFEmitter
+ __OBJC_$_PROP_LIST_CSRequestMutexTrackedRequest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSRequestMutexAnalyticsEmitting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSRequestMutexAnalyticsEmitting
+ __OBJC_$_PROTOCOL_REFS_CSRequestMutexAnalyticsEmitting
+ __OBJC_CLASS_PROTOCOLS_$_CSRequestMutexAnalyticsSELFEmitter
+ __OBJC_CLASS_RO_$_CSRequestMutexAnalyticsEventManager
+ __OBJC_CLASS_RO_$_CSRequestMutexAnalyticsSELFEmitter
+ __OBJC_CLASS_RO_$_CSRequestMutexTrackedRequest
+ __OBJC_LABEL_PROTOCOL_$_CSRequestMutexAnalyticsEmitting
+ __OBJC_METACLASS_RO_$_CSRequestMutexAnalyticsEventManager
+ __OBJC_METACLASS_RO_$_CSRequestMutexAnalyticsSELFEmitter
+ __OBJC_METACLASS_RO_$_CSRequestMutexTrackedRequest
+ __OBJC_PROTOCOL_$_CSRequestMutexAnalyticsEmitting
+ ___46-[CSUncompressedAudioLogging _removeAudioFile]_block_invoke
+ ___54+[CSOnDeviceCompilationUtils onDeviceCompilationQueue]_block_invoke
+ ___58-[CSFPreferences isAudioProviderRingBufferPruningDisabled]_block_invoke
+ ___94+[CSFOnDeviceCachedIrPurgingUtils purgeCachedIrForAssetExcludingCurrentAsset:baseCachedIrDir:]_block_invoke
+ _arc4random
+ _isAudioProviderRingBufferPruningDisabled.disabled
+ _isAudioProviderRingBufferPruningDisabled.onceToken
+ _objc_sync_enter
+ _objc_sync_exit
+ _onDeviceCompilationQueue.onceToken
+ _onDeviceCompilationQueue.queue
+ _os_unfair_recursive_lock_lock
+ _rename
- +[CSFOnDeviceCachedIrPurgingUtils purgeCachedIrForTrialAssetExcludingCurrentAsset:baseCachedIrDir:]
- -[CSRequestMutexController tryAcquireForOwner:requestId:resourceType:]
- -[CSUncompressedAudioLogging _moveAudioLoggingToCollectionDirectory:]
- -[CSUncompressedAudioLogging _removeTmpAudioFile]
- -[CSUncompressedAudioLogging setTmpAudioFilePath:]
- -[CSUncompressedAudioLogging setTmpDirectory:]
- -[CSUncompressedAudioLogging tmpAudioFilePath]
- -[CSUncompressedAudioLogging tmpDirectory]
- GCC_except_table1376
- GCC_except_table1407
- GCC_except_table1490
- GCC_except_table1494
- GCC_except_table1495
- GCC_except_table1497
- GCC_except_table1498
- GCC_except_table1499
- GCC_except_table1510
- GCC_except_table1513
- GCC_except_table1514
- GCC_except_table1519
- GCC_except_table1522
- GCC_except_table1525
- GCC_except_table1527
- GCC_except_table1545
- GCC_except_table1940
- GCC_except_table1941
- GCC_except_table1948
- GCC_except_table1951
- GCC_except_table1952
- GCC_except_table1960
- GCC_except_table1967
- GCC_except_table1970
- GCC_except_table1985
- GCC_except_table1991
- GCC_except_table2079
- GCC_except_table2084
- GCC_except_table2149
- GCC_except_table2161
- GCC_except_table2203
- GCC_except_table2204
- GCC_except_table2207
- GCC_except_table2213
- GCC_except_table2224
- GCC_except_table2231
- GCC_except_table2274
- GCC_except_table2292
- GCC_except_table2373
- GCC_except_table2485
- GCC_except_table2520
- GCC_except_table2691
- GCC_except_table2695
- GCC_except_table2774
- GCC_except_table2785
- GCC_except_table2787
- GCC_except_table2792
- GCC_except_table2807
- GCC_except_table2814
- GCC_except_table2834
- GCC_except_table2855
- GCC_except_table2902
- GCC_except_table2906
- GCC_except_table2959
- GCC_except_table2961
- GCC_except_table2962
- GCC_except_table3130
- GCC_except_table3271
- GCC_except_table3279
- GCC_except_table3287
- GCC_except_table3297
- GCC_except_table3301
- GCC_except_table3303
- GCC_except_table3304
- GCC_except_table3340
- GCC_except_table3346
- GCC_except_table3410
- GCC_except_table3414
- GCC_except_table3469
- GCC_except_table3481
- GCC_except_table3485
- GCC_except_table3504
- GCC_except_table3528
- GCC_except_table3529
- GCC_except_table3530
- GCC_except_table3531
- GCC_except_table3556
- GCC_except_table3569
- GCC_except_table3761
- GCC_except_table3821
- GCC_except_table3877
- GCC_except_table3878
- GCC_except_table3907
- GCC_except_table3908
- GCC_except_table3910
- GCC_except_table3913
- GCC_except_table3914
- GCC_except_table3915
- GCC_except_table3938
- GCC_except_table3940
- GCC_except_table3945
- GCC_except_table3946
- GCC_except_table3947
- GCC_except_table3981
- GCC_except_table4007
- GCC_except_table4028
- GCC_except_table4048
- GCC_except_table4049
- GCC_except_table4050
- GCC_except_table4051
- GCC_except_table4061
- GCC_except_table4152
- GCC_except_table4153
- GCC_except_table4162
- GCC_except_table4164
- GCC_except_table4165
- GCC_except_table4166
- GCC_except_table4170
- GCC_except_table4171
- GCC_except_table4174
- GCC_except_table4175
- GCC_except_table4176
- GCC_except_table4178
- GCC_except_table4198
- GCC_except_table4204
- GCC_except_table4205
- GCC_except_table4209
- GCC_except_table4214
- GCC_except_table4217
- GCC_except_table4221
- GCC_except_table4222
- GCC_except_table4250
- GCC_except_table4300
- GCC_except_table4304
- GCC_except_table4355
- GCC_except_table4356
- GCC_except_table4363
- GCC_except_table4364
- GCC_except_table4365
- GCC_except_table4366
- GCC_except_table4368
- GCC_except_table4369
- GCC_except_table4390
- GCC_except_table4392
- GCC_except_table4393
- GCC_except_table4394
- GCC_except_table4396
- GCC_except_table4397
- GCC_except_table4398
- GCC_except_table4399
- GCC_except_table4400
- GCC_except_table4401
- GCC_except_table4402
- GCC_except_table4403
- GCC_except_table4424
- GCC_except_table4426
- GCC_except_table4427
- GCC_except_table4428
- GCC_except_table4429
- GCC_except_table4431
- GCC_except_table4432
- GCC_except_table4434
- GCC_except_table4436
- GCC_except_table4437
- GCC_except_table4438
- GCC_except_table4440
- GCC_except_table4448
- GCC_except_table4450
- GCC_except_table4474
- GCC_except_table4475
- GCC_except_table4477
- GCC_except_table4478
- GCC_except_table4480
- GCC_except_table4482
- GCC_except_table4483
- GCC_except_table4484
- GCC_except_table4491
- GCC_except_table4496
- GCC_except_table4526
- GCC_except_table4665
- GCC_except_table4672
- GCC_except_table4755
- GCC_except_table4833
- GCC_except_table4843
- GCC_except_table4899
- GCC_except_table4900
- GCC_except_table4901
- GCC_except_table4903
- GCC_except_table4904
- GCC_except_table4905
- GCC_except_table4906
- GCC_except_table4907
- GCC_except_table4909
- GCC_except_table4911
- GCC_except_table4912
- GCC_except_table4914
- GCC_except_table4916
- GCC_except_table4917
- GCC_except_table4919
- GCC_except_table4955
- GCC_except_table5021
- GCC_except_table5026
- GCC_except_table5067
- GCC_except_table509
- GCC_except_table510
- GCC_except_table5133
- GCC_except_table545
- GCC_except_table582
- GCC_except_table590
- GCC_except_table608
- GCC_except_table676
- GCC_except_table680
- GCC_except_table685
- GCC_except_table687
- GCC_except_table850
- GCC_except_table857
- GCC_except_table920
- GCC_except_table921
- GCC_except_table928
- GCC_except_table943
- GCC_except_table944
- GCC_except_table945
- GCC_except_table950
- GCC_except_table951
- GCC_except_table952
- GCC_except_table962
- GCC_except_table980
- _OBJC_IVAR_$_CSUncompressedAudioLogging._tmpAudioFilePath
- _OBJC_IVAR_$_CSUncompressedAudioLogging._tmpDirectory
- ___49-[CSUncompressedAudioLogging _removeTmpAudioFile]_block_invoke
- ___99+[CSFOnDeviceCachedIrPurgingUtils purgeCachedIrForTrialAssetExcludingCurrentAsset:baseCachedIrDir:]_block_invoke
- _os_unfair_recursive_lock_lock_with_options
CStrings:
+ "%s #requestLock #analytics MHMutexRequested mhId: %@ { requester: %c, requestedResourceType: %s, successfullyAcquired: 0, currentOwner: %c, holdTimeOfUnspecifiedResourceInMs: %u, holdTimeOfAudioResourceInMs: %u, holdTimeOfASRResourceInMs: %u }"
+ "%s #requestLock #analytics MHMutexRequested mhId: %@ { requester: %c, requestedResourceType: %s, successfullyAcquired: 1 }"
+ "%s #requestLock #analytics mhId %@ isn't a UUID, skipping MHMutexRequested"
+ "%s #requestLock #analytics no mhId yet for local requestId %@, not reporting its acquire"
+ "%s #requestLock #analytics no mhId yet for local requestId %@, not reporting its refusal"
+ "%s %@: Audio sample does not exist : %@"
+ "%s %@: Failed to remove audio logging : %@"
+ "%s CSAudioProvider[%{public}@]:Circular buffer keeps %{public}lu of %{public}lu channels (retainedMask = 0x%{public}llx)"
+ "%s Invalid channel request: channelIdx=%{public}lu, numChannels=%{public}lu"
+ "%s Optimized OSD config not in asset, falling back to %{public}@"
+ "%s Read of pruned channel %{public}lu (retainedMask=0x%{public}llx, reads so far=%{public}llu)"
+ "%s asset specified as nil for purging"
+ "%s mil2bnns model config not found, using default options: %@"
+ "%s no cached ir directory for model type: %lu"
+ "%s numChannels: %{public}lu, retainedChannels: %{public}lu, retainedMask: 0x%{public}llx, recordingDuration: %{public}f, sampleRate: %{public}f"
+ "+[CSFOnDeviceCachedIrPurgingUtils purgeCachedIrForAssetExcludingCurrentAsset:baseCachedIrDir:]"
+ "+[CSFOnDeviceCachedIrPurgingUtils removeCachedIrsForModelType:]"
+ "-[CSAsset _optimizedOSDConfigPath]"
+ "-[CSAudioCircularBuffer initWithNumChannels:recordingDuration:samplingRate:audioTimeConverter:retainedChannelMask:]"
+ "-[CSRequestMutexAnalyticsEventManager acquisitionRefusedForRequestId:mhId:requester:resourceType:snapshot:]"
+ "-[CSRequestMutexAnalyticsEventManager acquisitionSucceededForRequestId:mhId:requester:resourceType:]"
+ "-[CSRequestMutexAnalyticsSELFEmitter _emitMutexRequested:forMhId:]"
+ "-[CSRequestMutexAnalyticsSELFEmitter emitFirstAcquisitionForMhId:requester:requestedResourceType:]"
+ "-[CSRequestMutexAnalyticsSELFEmitter emitFirstRefusalForMhId:requester:requestedResourceType:snapshot:]"
+ "-[CSRequestMutexController tryAcquireForOwner:requestId:mhId:resourceType:]"
+ "-[CSUncompressedAudioLogging _removeAudioFile]_block_invoke"
+ ".%u"
+ ".bnnsir"
+ "CSOnDeviceCompilationQueue"
+ "CoreSpeechMil2BnnsCache"
+ "Could not move compiled BNNSIR to %@: %s"
+ "Disable Audio Provider Ring Buffer Channel Pruning"
+ "_optimized"
+ "es-CL"
+ "es-ES"
+ "es-MX"
+ "es-US"
+ "pt-BR"
+ "pt-PT"
- "%s %@: Failed to move audio logging %@"
- "%s %@: Failed to remove audio logging in the tmp : %@"
- "%s numChannels: %{public}lu, recordingDuration: %{public}f, sampleRate: %{public}f"
- "+[CSFOnDeviceCachedIrPurgingUtils purgeCachedIrForTrialAssetExcludingCurrentAsset:baseCachedIrDir:]"
- "-[CSAudioCircularBuffer initWithNumChannels:recordingDuration:samplingRate:audioTimeConverter:]"
- "-[CSRequestMutexController tryAcquireForOwner:requestId:resourceType:]"
- "-[CSUncompressedAudioLogging _moveAudioLoggingToCollectionDirectory:]"
- "-[CSUncompressedAudioLogging _removeTmpAudioFile]_block_invoke"
- "CSOnDeviceCompilationHanlder"
- "config file not found for %@"
```
