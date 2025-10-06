## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

-3305.27.1.0.0
-  __TEXT.__text: 0x80904
+3306.8.1.0.0
+  __TEXT.__text: 0x80f5c
   __TEXT.__auth_stubs: 0x17c0
-  __TEXT.__objc_methlist: 0x7ac8
+  __TEXT.__objc_methlist: 0x7b30
   __TEXT.__const: 0x388
   __TEXT.__gcc_except_tab: 0x1a84
-  __TEXT.__cstring: 0xd025
-  __TEXT.__oslogstring: 0x9c3b
+  __TEXT.__cstring: 0xd1ed
+  __TEXT.__oslogstring: 0x9d1e
   __TEXT.__dlopen_cstrs: 0x114
-  __TEXT.__unwind_info: 0x215c
+  __TEXT.__unwind_info: 0x2174
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x112e
-  __TEXT.__objc_methname: 0x18129
+  __TEXT.__objc_classname: 0x1147
+  __TEXT.__objc_methname: 0x1830d
   __TEXT.__objc_methtype: 0x3524
-  __TEXT.__objc_stubs: 0xcd60
+  __TEXT.__objc_stubs: 0xce40
   __DATA_CONST.__got: 0x308
   __DATA_CONST.__const: 0x14e8
-  __DATA_CONST.__objc_classlist: 0x448
+  __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xcbb0
-  __DATA_CONST.__objc_selrefs: 0x4ee8
+  __DATA_CONST.__objc_const: 0xcbc8
+  __DATA_CONST.__objc_selrefs: 0x4f40
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_classrefs: 0x7b0
+  __DATA_CONST.__objc_classrefs: 0x7c0
   __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__const: 0xea0
-  __AUTH_CONST.__objc_const: 0x34e0
-  __AUTH_CONST.__cfstring: 0x6480
+  __AUTH_CONST.__const: 0xec0
+  __AUTH_CONST.__objc_const: 0x3570
+  __AUTH_CONST.__cfstring: 0x64c0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_floatobj: 0x150
   __AUTH_CONST.__auth_got: 0xbf8
-  __AUTH.__objc_data: 0x10e0
+  __AUTH.__objc_data: 0x1130
   __DATA.__objc_ivar: 0x918
   __DATA.__data: 0xc50
-  __DATA.__bss: 0x4b0
+  __DATA.__bss: 0x4b8
   __DATA_DIRTY.__objc_data: 0x19f0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0x18
-  __DATA_DIRTY.__bss: 0x2f8
+  __DATA_DIRTY.__bss: 0x308
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9BB25532-10A2-3300-8F68-65A6042733C7
-  Functions: 3154
-  Symbols:   11054
-  CStrings:  7142
+  UUID: C3A9FF5A-13C5-32DD-9194-EA044F98B6C3
+  Functions: 3162
+  Symbols:   11089
+  CStrings:  7168
 
Symbols:
+ +[CSVoiceProfileSELFLogger initialize]
+ +[CSVoiceProfileSELFLogger sharedLogger]
+ +[CSVoiceProfileSELFLogger voiceProfileiCloudSyncIsolatedStreamID]
+ -[CSFPreferences dateWhenEnrollmentIdForVoiceProfileiCloudMetricsWasCreated]
+ -[CSFPreferences enrollmentIdForVoiceProfileiCloudMetrics]
+ -[CSFPreferences setEnrollmentIdForVoiceProfileiCloudMetrics:on:]
+ -[CSVoiceProfileSELFLogger logVoiceProfileICloudSyncFinishedForEnrollmentId:isVoiceProfileiCloudSyncSuccess:failureReasonIfAny:forLocale:]
+ GCC_except_table2113
+ GCC_except_table2226
+ GCC_except_table2234
+ GCC_except_table2242
+ GCC_except_table2249
+ GCC_except_table2254
+ GCC_except_table2256
+ GCC_except_table2258
+ GCC_except_table2262
+ GCC_except_table2282
+ GCC_except_table2337
+ GCC_except_table2341
+ GCC_except_table2410
+ GCC_except_table2441
+ GCC_except_table2442
+ GCC_except_table2443
+ GCC_except_table2465
+ GCC_except_table2528
+ GCC_except_table2588
+ GCC_except_table2598
+ GCC_except_table2603
+ GCC_except_table2604
+ GCC_except_table2605
+ GCC_except_table2719
+ GCC_except_table2720
+ GCC_except_table2728
+ GCC_except_table2732
+ GCC_except_table2733
+ GCC_except_table2746
+ GCC_except_table2750
+ GCC_except_table2751
+ GCC_except_table2752
+ GCC_except_table2757
+ GCC_except_table2759
+ GCC_except_table2763
+ GCC_except_table2764
+ GCC_except_table2782
+ GCC_except_table2786
+ GCC_except_table2884
+ GCC_except_table2891
+ GCC_except_table2933
+ GCC_except_table2970
+ GCC_except_table2986
+ GCC_except_table2991
+ GCC_except_table3037
+ GCC_except_table3126
+ _OBJC_CLASS_$_CSVoiceProfileSELFLogger
+ _OBJC_CLASS_$_MHSchemaMHVoiceProfileICloudSyncFinished
+ _OBJC_METACLASS_$_CSVoiceProfileSELFLogger
+ __OBJC_$_CLASS_METHODS_CSVoiceProfileSELFLogger
+ __OBJC_$_CLASS_PROP_LIST_CSVoiceProfileSELFLogger
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.5497
+ __OBJC_$_INSTANCE_METHODS_CSVoiceProfileSELFLogger
+ __OBJC_$_PROP_LIST_NSObject.5343
+ __OBJC_$_PROP_LIST_NSObject.5954
+ __OBJC_$_PROP_LIST_NSObject.6234
+ __OBJC_$_PROP_LIST_NSObject.7067
+ __OBJC_$_PROP_LIST_NSObject.7453
+ __OBJC_$_PROP_LIST_NSObject.8375
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.5498
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioFileWriter.8376
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.5955
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSFModelComputeBackend.7068
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.5499
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.5500
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.6878
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.8764
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5344
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5956
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6235
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7069
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7454
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8377
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.5957
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5345
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5958
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6236
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7070
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7455
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8378
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioFileWriter.8379
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.5959
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSFModelComputeBackend.7071
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.5501
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.5502
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.6879
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.8765
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5346
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5960
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6237
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7072
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7456
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8380
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.5503
+ __OBJC_$_PROTOCOL_REFS_CSAudioFileWriter.8381
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.5961
+ __OBJC_$_PROTOCOL_REFS_CSFModelComputeBackend.7073
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.5504
+ __OBJC_CLASS_RO_$_CSVoiceProfileSELFLogger
+ __OBJC_METACLASS_RO_$_CSVoiceProfileSELFLogger
+ ___40+[CSVoiceProfileSELFLogger sharedLogger]_block_invoke
+ ___Block_byref_object_copy_.4901
+ ___Block_byref_object_copy_.5551
+ ___Block_byref_object_copy_.7392
+ ___Block_byref_object_copy_.7596
+ ___Block_byref_object_copy_.7880
+ ___Block_byref_object_copy_.8250
+ ___Block_byref_object_copy_.8330
+ ___Block_byref_object_copy_.8908
+ ___Block_byref_object_dispose_.4902
+ ___Block_byref_object_dispose_.5552
+ ___Block_byref_object_dispose_.7393
+ ___Block_byref_object_dispose_.7597
+ ___Block_byref_object_dispose_.7881
+ ___Block_byref_object_dispose_.8251
+ ___Block_byref_object_dispose_.8331
+ ___Block_byref_object_dispose_.8909
+ ___block_literal_global.432.4702
+ ___block_literal_global.455
+ ___block_literal_global.460
+ ___block_literal_global.475
+ ___block_literal_global.480
+ ___block_literal_global.4817
+ ___block_literal_global.491
+ ___block_literal_global.5175
+ ___block_literal_global.5236
+ ___block_literal_global.5317
+ ___block_literal_global.5355
+ ___block_literal_global.5404
+ ___block_literal_global.5576
+ ___block_literal_global.5813
+ ___block_literal_global.7689
+ ___block_literal_global.7792
+ ___block_literal_global.8131
+ ___block_literal_global.8273
+ ___block_literal_global.8477
+ ___block_literal_global.8593
+ ___block_literal_global.8932
+ __unnamed_array_storage.7008
+ __unnamed_array_storage.8122
+ __voiceProfileiCloudSyncIsolatedStreamID
+ _objc_msgSend$defaultMessageStream
+ _objc_msgSend$emitMessage:isolatedStreamUUID:
+ _objc_msgSend$setEnrollmentId:
+ _objc_msgSend$setIsVoiceProfileSyncSuccess:
+ _objc_msgSend$setVoiceProfileICloudSyncFinished:
+ _objc_msgSend$setVoiceProfileSyncFailureReason:
+ _objc_msgSend$voiceProfileiCloudSyncIsolatedStreamID
+ _sharedInstance.onceToken.5235
+ _sharedInstance.onceToken.5354
+ _sharedInstance.onceToken.5403
+ _sharedInstance.onceToken.5812
+ _sharedInstance.onceToken.8476
+ _sharedInstance.onceToken.8592
+ _sharedInstance.onceToken.8931
+ _sharedInstance.sharedInstance.5237
+ _sharedInstance.sharedInstance.5356
+ _sharedInstance.sharedInstance.5405
+ _sharedInstance.sharedInstance.8478
+ _sharedInstance.sharedInstance.8933
+ _sharedLogger.onceToken.7791
+ _sharedLogger.shared
+ _sharedPreferences.onceToken.5174
- GCC_except_table2110
- GCC_except_table2223
- GCC_except_table2231
- GCC_except_table2239
- GCC_except_table2246
- GCC_except_table2251
- GCC_except_table2253
- GCC_except_table2255
- GCC_except_table2259
- GCC_except_table2279
- GCC_except_table2334
- GCC_except_table2338
- GCC_except_table2407
- GCC_except_table2437
- GCC_except_table2438
- GCC_except_table2439
- GCC_except_table2462
- GCC_except_table2525
- GCC_except_table2585
- GCC_except_table2594
- GCC_except_table2595
- GCC_except_table2601
- GCC_except_table2602
- GCC_except_table2716
- GCC_except_table2717
- GCC_except_table2724
- GCC_except_table2725
- GCC_except_table2726
- GCC_except_table2739
- GCC_except_table2740
- GCC_except_table2747
- GCC_except_table2749
- GCC_except_table2754
- GCC_except_table2756
- GCC_except_table2760
- GCC_except_table2761
- GCC_except_table2779
- GCC_except_table2783
- GCC_except_table2876
- GCC_except_table2883
- GCC_except_table2925
- GCC_except_table2962
- GCC_except_table2978
- GCC_except_table2983
- GCC_except_table3029
- GCC_except_table3118
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.5490
- __OBJC_$_PROP_LIST_NSObject.5336
- __OBJC_$_PROP_LIST_NSObject.5947
- __OBJC_$_PROP_LIST_NSObject.6227
- __OBJC_$_PROP_LIST_NSObject.7060
- __OBJC_$_PROP_LIST_NSObject.7446
- __OBJC_$_PROP_LIST_NSObject.8338
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.5491
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioFileWriter.8339
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.5948
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSFModelComputeBackend.7061
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.5492
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.5493
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.6871
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.8727
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5337
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5949
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6228
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7062
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7447
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8340
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.5950
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5338
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5951
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6229
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7063
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7448
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8341
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioFileWriter.8342
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.5952
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSFModelComputeBackend.7064
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.5494
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.5495
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.6872
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.8728
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5339
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5953
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6230
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7065
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7449
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8343
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.5496
- __OBJC_$_PROTOCOL_REFS_CSAudioFileWriter.8344
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.5954
- __OBJC_$_PROTOCOL_REFS_CSFModelComputeBackend.7066
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.5497
- ___Block_byref_object_copy_.4889
- ___Block_byref_object_copy_.5544
- ___Block_byref_object_copy_.7385
- ___Block_byref_object_copy_.7589
- ___Block_byref_object_copy_.7843
- ___Block_byref_object_copy_.8213
- ___Block_byref_object_copy_.8293
- ___Block_byref_object_copy_.8867
- ___Block_byref_object_dispose_.4890
- ___Block_byref_object_dispose_.5545
- ___Block_byref_object_dispose_.7386
- ___Block_byref_object_dispose_.7590
- ___Block_byref_object_dispose_.7844
- ___Block_byref_object_dispose_.8214
- ___Block_byref_object_dispose_.8294
- ___Block_byref_object_dispose_.8868
- ___block_literal_global.432.4690
- ___block_literal_global.449
- ___block_literal_global.454
- ___block_literal_global.469
- ___block_literal_global.474
- ___block_literal_global.4805
- ___block_literal_global.485
- ___block_literal_global.5163
- ___block_literal_global.5224
- ___block_literal_global.5307
- ___block_literal_global.5348
- ___block_literal_global.5397
- ___block_literal_global.5569
- ___block_literal_global.5806
- ___block_literal_global.7682
- ___block_literal_global.8094
- ___block_literal_global.8236
- ___block_literal_global.8440
- ___block_literal_global.8556
- ___block_literal_global.8891
- __unnamed_array_storage.7001
- __unnamed_array_storage.8085
- _sharedInstance.onceToken.5223
- _sharedInstance.onceToken.5347
- _sharedInstance.onceToken.5396
- _sharedInstance.onceToken.5805
- _sharedInstance.onceToken.8439
- _sharedInstance.onceToken.8555
- _sharedInstance.onceToken.8890
- _sharedInstance.sharedInstance.5225
- _sharedInstance.sharedInstance.5349
- _sharedInstance.sharedInstance.5398
- _sharedInstance.sharedInstance.8441
- _sharedInstance.sharedInstance.8892
- _sharedPreferences.onceToken.5162
CStrings:
+ "%s Fetched enrollmentId %@"
+ "%s Setting enrollmentId %@ on %@... "
+ "%s VoiceProfile iCloud Sync SELF Log for enrollment ID %@, isVoiceProfileiCloudSyncSuccess %@, failureReason %@"
+ "%s date found %@"
+ "%s date not found. Return nil... "
+ "-[CSFPreferences dateWhenEnrollmentIdForVoiceProfileiCloudMetricsWasCreated]"
+ "-[CSFPreferences enrollmentIdForVoiceProfileiCloudMetrics]"
+ "-[CSFPreferences setEnrollmentIdForVoiceProfileiCloudMetrics:on:]"
+ "-[CSVoiceProfileSELFLogger logVoiceProfileICloudSyncFinishedForEnrollmentId:isVoiceProfileiCloudSyncSuccess:failureReasonIfAny:forLocale:]"
+ "CSVoiceProfileSELFLogger"
+ "Creation Date of EnrollmentId used in Voice Profile iCloud Enrollment"
+ "EnrollmentId Voice Profile iCloud Enrollment"
+ "T@\"NSUUID\",R,N"
+ "dateWhenEnrollmentIdForVoiceProfileiCloudMetricsWasCreated"
+ "defaultMessageStream"
+ "emitMessage:isolatedStreamUUID:"
+ "enrollmentIdForVoiceProfileiCloudMetrics"
+ "logVoiceProfileICloudSyncFinishedForEnrollmentId:isVoiceProfileiCloudSyncSuccess:failureReasonIfAny:forLocale:"
+ "setEnrollmentId:"
+ "setEnrollmentIdForVoiceProfileiCloudMetrics:on:"
+ "setIsVoiceProfileSyncSuccess:"
+ "setVoiceProfileICloudSyncFinished:"
+ "setVoiceProfileSyncFailureReason:"
+ "voiceProfileiCloudSyncIsolatedStreamID"

```
