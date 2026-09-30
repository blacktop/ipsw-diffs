## TextToSpeechVoiceBankingSupport

> `/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/TextToSpeechVoiceBankingSupport`

```diff

-671.1.1.0.0
-  __TEXT.__text: 0x178c54
-  __TEXT.__auth_stubs: 0x2bc0
+673.3.0.0.0
+  __TEXT.__text: 0x179884
+  __TEXT.__auth_stubs: 0x2c00
   __TEXT.__objc_methlist: 0xc1c
-  __TEXT.__const: 0x127e0
+  __TEXT.__const: 0x12af0
   __TEXT.__gcc_except_tab: 0x58
   __TEXT.__cstring: 0xbc7b
   __TEXT.__dlopen_cstrs: 0x170
   __TEXT.__oslogstring: 0x3caf
-  __TEXT.__swift5_typeref: 0x44c6
-  __TEXT.__constg_swiftt: 0x3830
-  __TEXT.__swift5_reflstr: 0x28e2
-  __TEXT.__swift5_fieldmd: 0x37b8
-  __TEXT.__swift5_types: 0x4cc
-  __TEXT.__swift5_capture: 0x16ec
-  __TEXT.__swift5_builtin: 0x1cc
+  __TEXT.__swift5_typeref: 0x4530
+  __TEXT.__constg_swiftt: 0x3868
+  __TEXT.__swift5_reflstr: 0x28f2
+  __TEXT.__swift5_fieldmd: 0x37fc
+  __TEXT.__swift5_types: 0x4d4
+  __TEXT.__swift5_capture: 0x1728
+  __TEXT.__swift5_builtin: 0x1f4
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_assocty: 0x7c8
-  __TEXT.__swift5_proto: 0x11f8
+  __TEXT.__swift5_assocty: 0x828
+  __TEXT.__swift5_proto: 0x1228
   __TEXT.__swift_as_entry: 0x2cc
   __TEXT.__swift_as_ret: 0x2d8
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x5350
+  __TEXT.__unwind_info: 0x5370
   __TEXT.__eh_frame: 0x7d10
   __TEXT.__objc_classname: 0x119
-  __TEXT.__objc_methname: 0x3079
-  __TEXT.__objc_methtype: 0x323
+  __TEXT.__objc_methname: 0x308d
+  __TEXT.__objc_methtype: 0x334
   __TEXT.__objc_stubs: 0xb40
-  __DATA_CONST.__got: 0x968
-  __DATA_CONST.__const: 0xd00
+  __DATA_CONST.__got: 0x970
+  __DATA_CONST.__const: 0xd18
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x15f0
-  __AUTH_CONST.__const: 0xab38
+  __AUTH_CONST.__auth_got: 0x1610
+  __AUTH_CONST.__const: 0xac50
   __AUTH_CONST.__cfstring: 0x480
-  __AUTH_CONST.__objc_const: 0x2830
+  __AUTH_CONST.__objc_const: 0x2850
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xbe0
-  __AUTH.__data: 0x1e70
+  __AUTH.__data: 0x1e68
   __DATA.__objc_ivar: 0x18
-  __DATA.__data: 0x2298
-  __DATA.__bss: 0x24370
+  __DATA.__data: 0x2300
+  __DATA.__bss: 0x24970
   __DATA.__common: 0x3a8
   __DATA_DIRTY.__objc_data: 0x798
-  __DATA_DIRTY.__data: 0xdb0
+  __DATA_DIRTY.__data: 0xda0
   __DATA_DIRTY.__bss: 0x760
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 48B62C96-D712-3E64-A87B-E60A699DEA05
-  Functions: 7531
-  Symbols:   3804
-  CStrings:  2171
+  UUID: C5594896-2EC0-3DF2-A2AE-A3B1ED2A5E5C
+  Functions: 7558
+  Symbols:   3835
+  CStrings:  2173
 
Symbols:
+ -[TTSVBSiriTTSTrainerSession installableTrainingAssetsForLocaleID:name:type:]
+ -[TTSVBSiriTTSTrainerSession installedTrainingAssetsForLocaleID:name:type:]
+ _TTSVBSiriTrainingAssetNameDefault
+ _TTSVBSiriTrainingAssetNameNatural
+ _TTSVBSiriTrainingAssetTypeAsset
+ _TTSVBSiriTrainingAssetTypeScript
+ ___63-[TTSVBSiriTTSTrainerSession installAsset:progress:completion:]_block_invoke.32
+ ___63-[TTSVBSiriTTSTrainerSession installAsset:progress:completion:]_block_invoke.32.cold.1
+ ___68-[TTSVBSiriTTSTrainerSession getAllTasksReplyOnQueue:statusHandler:]_block_invoke.45
+ ___69-[TTSVBSiriTTSTrainerSession getTaskByID:replyOnQueue:statusHandler:]_block_invoke.40
+ ___72-[TTSVBSiriTTSTrainerSession cancelTask:replyOnQueue:completionHandler:]_block_invoke.48
+ ___80-[TTSVBSiriTTSTrainerSession startTraining:replyOnQueue:trainingStartedHandler:]_block_invoke.37
+ ___81-[TTSVBSiriTTSTrainerSession discardTrainingTasksReplyOnQueue:completionHandler:]_block_invoke.47
+ ___98-[TTSVBSiriTTSTrainerSession fetchTrainingScriptsWithLocaleID:scriptType:replyOnQueue:completion:]_block_invoke.34
+ _associated conformance So26TTSVBSiriTrainingAssetNameaSHSCSQ
+ _associated conformance So26TTSVBSiriTrainingAssetNameas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So26TTSVBSiriTrainingAssetNameas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _associated conformance So26TTSVBSiriTrainingAssetTypeaSHSCSQ
+ _associated conformance So26TTSVBSiriTrainingAssetTypeas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So26TTSVBSiriTrainingAssetTypeas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _block_copy_helper.119
+ _block_copy_helper.150
+ _block_copy_helper.173
+ _block_copy_helper.190
+ _block_copy_helper.197
+ _block_copy_helper.217
+ _block_copy_helper.271
+ _block_copy_helper.285
+ _block_copy_helper.291
+ _block_copy_helper.301
+ _block_copy_helper.324
+ _block_copy_helper.334
+ _block_copy_helper.350
+ _block_copy_helper.356
+ _block_copy_helper.366
+ _block_copy_helper.381
+ _block_copy_helper.389
+ _block_copy_helper.396
+ _block_copy_helper.430
+ _block_copy_helper.447
+ _block_copy_helper.453
+ _block_copy_helper.459
+ _block_copy_helper.465
+ _block_copy_helper.471
+ _block_copy_helper.486
+ _block_copy_helper.492
+ _block_copy_helper.498
+ _block_copy_helper.501
+ _block_copy_helper.507
+ _block_copy_helper.517
+ _block_copy_helper.606
+ _block_copy_helper.612
+ _block_copy_helper.618
+ _block_copy_helper.93
+ _block_descriptor.121
+ _block_descriptor.152
+ _block_descriptor.175
+ _block_descriptor.192
+ _block_descriptor.199
+ _block_descriptor.219
+ _block_descriptor.273
+ _block_descriptor.287
+ _block_descriptor.293
+ _block_descriptor.303
+ _block_descriptor.326
+ _block_descriptor.336
+ _block_descriptor.352
+ _block_descriptor.358
+ _block_descriptor.368
+ _block_descriptor.383
+ _block_descriptor.391
+ _block_descriptor.398
+ _block_descriptor.432
+ _block_descriptor.449
+ _block_descriptor.455
+ _block_descriptor.461
+ _block_descriptor.467
+ _block_descriptor.473
+ _block_descriptor.488
+ _block_descriptor.494
+ _block_descriptor.500
+ _block_descriptor.503
+ _block_descriptor.509
+ _block_descriptor.519
+ _block_descriptor.608
+ _block_descriptor.614
+ _block_descriptor.620
+ _block_descriptor.95
+ _block_destroy_helper.120
+ _block_destroy_helper.151
+ _block_destroy_helper.174
+ _block_destroy_helper.191
+ _block_destroy_helper.198
+ _block_destroy_helper.218
+ _block_destroy_helper.272
+ _block_destroy_helper.286
+ _block_destroy_helper.292
+ _block_destroy_helper.302
+ _block_destroy_helper.325
+ _block_destroy_helper.335
+ _block_destroy_helper.351
+ _block_destroy_helper.357
+ _block_destroy_helper.367
+ _block_destroy_helper.382
+ _block_destroy_helper.390
+ _block_destroy_helper.397
+ _block_destroy_helper.431
+ _block_destroy_helper.448
+ _block_destroy_helper.454
+ _block_destroy_helper.460
+ _block_destroy_helper.466
+ _block_destroy_helper.472
+ _block_destroy_helper.487
+ _block_destroy_helper.493
+ _block_destroy_helper.499
+ _block_destroy_helper.502
+ _block_destroy_helper.508
+ _block_destroy_helper.518
+ _block_destroy_helper.607
+ _block_destroy_helper.613
+ _block_destroy_helper.619
+ _block_destroy_helper.94
+ _objectdestroy.136Tm
+ _objectdestroy.148Tm
+ _objectdestroy.171Tm
+ _objectdestroy.269Tm
+ _objectdestroy.307Tm
+ _objectdestroy.410Tm
+ _objectdestroy.413Tm
+ _objectdestroy.436Tm
+ _objectdestroy.610Tm
+ _symbolic SfIegy_
+ _symbolic So8NSNumberC
+ _symbolic _____ So26TTSVBSiriTrainingAssetNamea
+ _symbolic _____ So26TTSVBSiriTrainingAssetTypea
+ _symbolic _____y__________GIegn_ s6ResultOsRi_zRi0_zrlE 31TextToSpeechVoiceBankingSupport13TTSVBResultOKO AC10TTSVBErrorV
+ _type_layout_string So26TTSVBSiriTrainingAssetTypea
- -[TTSVBSiriTTSTrainerSession installableTrainingAssetsForLocaleID:]
- -[TTSVBSiriTTSTrainerSession installedTrainingAssetsForLocaleID:]
- ___63-[TTSVBSiriTTSTrainerSession installAsset:progress:completion:]_block_invoke.29
- ___63-[TTSVBSiriTTSTrainerSession installAsset:progress:completion:]_block_invoke.29.cold.1
- ___68-[TTSVBSiriTTSTrainerSession getAllTasksReplyOnQueue:statusHandler:]_block_invoke.42
- ___69-[TTSVBSiriTTSTrainerSession getTaskByID:replyOnQueue:statusHandler:]_block_invoke.37
- ___72-[TTSVBSiriTTSTrainerSession cancelTask:replyOnQueue:completionHandler:]_block_invoke.45
- ___80-[TTSVBSiriTTSTrainerSession startTraining:replyOnQueue:trainingStartedHandler:]_block_invoke.34
- ___81-[TTSVBSiriTTSTrainerSession discardTrainingTasksReplyOnQueue:completionHandler:]_block_invoke.44
- ___98-[TTSVBSiriTTSTrainerSession fetchTrainingScriptsWithLocaleID:scriptType:replyOnQueue:completion:]_block_invoke.31
- _block_copy_helper.132
- _block_copy_helper.184
- _block_copy_helper.208
- _block_copy_helper.253
- _block_copy_helper.276
- _block_copy_helper.282
- _block_copy_helper.292
- _block_copy_helper.306
- _block_copy_helper.325
- _block_copy_helper.341
- _block_copy_helper.347
- _block_copy_helper.357
- _block_copy_helper.363
- _block_copy_helper.380
- _block_copy_helper.387
- _block_copy_helper.421
- _block_copy_helper.429
- _block_copy_helper.444
- _block_copy_helper.450
- _block_copy_helper.456
- _block_copy_helper.462
- _block_copy_helper.468
- _block_copy_helper.483
- _block_copy_helper.489
- _block_copy_helper.499
- _block_copy_helper.522
- _block_copy_helper.528
- _block_copy_helper.534
- _block_copy_helper.95
- _block_descriptor.134
- _block_descriptor.186
- _block_descriptor.210
- _block_descriptor.255
- _block_descriptor.278
- _block_descriptor.284
- _block_descriptor.294
- _block_descriptor.308
- _block_descriptor.327
- _block_descriptor.343
- _block_descriptor.349
- _block_descriptor.359
- _block_descriptor.365
- _block_descriptor.382
- _block_descriptor.389
- _block_descriptor.423
- _block_descriptor.431
- _block_descriptor.446
- _block_descriptor.452
- _block_descriptor.458
- _block_descriptor.464
- _block_descriptor.470
- _block_descriptor.485
- _block_descriptor.491
- _block_descriptor.501
- _block_descriptor.524
- _block_descriptor.530
- _block_descriptor.536
- _block_descriptor.97
- _block_destroy_helper.133
- _block_destroy_helper.185
- _block_destroy_helper.209
- _block_destroy_helper.254
- _block_destroy_helper.277
- _block_destroy_helper.283
- _block_destroy_helper.293
- _block_destroy_helper.307
- _block_destroy_helper.326
- _block_destroy_helper.342
- _block_destroy_helper.348
- _block_destroy_helper.358
- _block_destroy_helper.364
- _block_destroy_helper.381
- _block_destroy_helper.388
- _block_destroy_helper.422
- _block_destroy_helper.430
- _block_destroy_helper.445
- _block_destroy_helper.451
- _block_destroy_helper.457
- _block_destroy_helper.463
- _block_destroy_helper.469
- _block_destroy_helper.484
- _block_destroy_helper.490
- _block_destroy_helper.500
- _block_destroy_helper.523
- _block_destroy_helper.529
- _block_destroy_helper.535
- _block_destroy_helper.96
- _objectdestroy.120Tm
- _objectdestroy.130Tm
- _objectdestroy.165Tm
- _objectdestroy.260Tm
- _objectdestroy.298Tm
- _objectdestroy.401Tm
- _objectdestroy.404Tm
- _objectdestroy.427Tm
- _objectdestroy.592Tm
- _objectdestroy.73Tm
CStrings:
+ "@40@0:8@16@24q32"
+ "Will query SiriTTSTraining for installable assets language=%@ name=%@ type=%lu"
+ "Will query SiriTTSTraining for installed assets language=%@ name=%@ type=%lu"
+ "assetSize"
+ "installableTrainingAssetsForLocaleID:name:type:"
+ "installedTrainingAssetsForLocaleID:name:type:"
- "Will query SiriTTSTraining for installable assets language=%@ name=default"
- "Will query SiriTTSTraining for installed assets language=%@ name=default"
- "installableTrainingAssetsForLocaleID:"
- "installedTrainingAssetsForLocaleID:"

```
