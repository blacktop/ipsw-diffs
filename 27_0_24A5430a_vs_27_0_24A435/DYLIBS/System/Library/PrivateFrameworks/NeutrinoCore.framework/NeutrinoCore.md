## NeutrinoCore

> `/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore`

```diff

-912.0.234.0.0
-  __TEXT.__text: 0x310f64
-  __TEXT.__objc_methlist: 0x20474
+912.0.235.0.0
+  __TEXT.__text: 0x314798
+  __TEXT.__objc_methlist: 0x2083c
   __TEXT.__const: 0x2918
+  __TEXT.__dlopen_cstrs: 0x45
   __TEXT.__swift5_typeref: 0x3e7
   __TEXT.__swift5_reflstr: 0x93
   __TEXT.__swift5_assocty: 0xa8

   __TEXT.__swift5_fieldmd: 0x178
   __TEXT.__swift5_proto: 0x7c
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__cstring: 0x3dae2
+  __TEXT.__cstring: 0x3e181
   __TEXT.__swift5_capture: 0x210
-  __TEXT.__gcc_except_tab: 0x7f8c
-  __TEXT.__oslogstring: 0x5489
+  __TEXT.__gcc_except_tab: 0x8004
+  __TEXT.__oslogstring: 0x5741
   __TEXT.__ustring: 0x2e
-  __TEXT.__unwind_info: 0x84f0
+  __TEXT.__unwind_info: 0x8538
   __TEXT.__eh_frame: 0x448
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3f78
-  __DATA_CONST.__objc_classlist: 0x15b8
+  __DATA_CONST.__const: 0x3fc0
+  __DATA_CONST.__objc_classlist: 0x15c8
   __DATA_CONST.__objc_catlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0x4f0
+  __DATA_CONST.__objc_protolist: 0x500
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb338
+  __DATA_CONST.__objc_selrefs: 0xb488
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0xfe8
   __DATA_CONST.__objc_arraydata: 0xae0
-  __DATA_CONST.__got: 0x2200
+  __DATA_CONST.__got: 0x2220
   __AUTH_CONST.__const: 0x4e80
-  __AUTH_CONST.__cfstring: 0x1ca00
-  __AUTH_CONST.__objc_const: 0x36110
+  __AUTH_CONST.__cfstring: 0x1cf00
+  __AUTH_CONST.__objc_const: 0x36938
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x8d0
   __AUTH_CONST.__objc_dictobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x210
   __AUTH_CONST.__objc_floatobj: 0x70
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x10c8
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x1970
-  __DATA.__data: 0x3898
+  __AUTH_CONST.__auth_got: 0x10e0
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x19c8
+  __DATA.__data: 0x3958
   __DATA.__crash_info: 0x148
   __DATA_DIRTY.__objc_data: 0xd8e0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x1f0
+  __DATA_DIRTY.__bss: 0x1f8
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto
   - /System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11708
-  Symbols:   25161
-  CStrings:  7174
+  Functions: 11773
+  Symbols:   25331
+  CStrings:  7240
 
Symbols:
+ +[NUVideoUtilities metadataTrackContainsTextureStyleData:]
+ +[_NUTextureStylePersonInstanceProperties personInstancePropertiesFromDictionary:error:]
+ +[_NUTextureStyleProperties textureStylePropertiesFromImageMetadata:auxImageMetadata:error:]
+ +[_NUTextureStyleProperties textureStyleVideoPropertiesFromTextureStyleData:faceInfoData:error:]
+ -[NUCGImageSourceNode _loadTextureStylesProperties:error:]
+ -[NUCGImageSourceNode hasProvenanceData]
+ -[NUCGImageSourceNode setHasProvenanceData:]
+ -[NUCGImageSourceNode setTextureStylesProperties:]
+ -[NUCGImageSourceNode textureStylesProperties]
+ -[NUImageExportRequest embedProvenanceData]
+ -[NUImageExportRequest setEmbedProvenanceData:]
+ -[_NUImageProperties hasProvenanceData]
+ -[_NUImageProperties setHasProvenanceData:]
+ -[_NUImageProperties setTextureStyleProperties:]
+ -[_NUImageProperties textureStyleProperties]
+ -[_NUSemanticStyleProperties linearHighKey]
+ -[_NUSemanticStyleProperties revertUsingOriginal]
+ -[_NUSemanticStyleProperties setLinearHighKey:]
+ -[_NUSemanticStyleProperties setRevertUsingOriginal:]
+ -[_NUTextureStylePersonInstanceProperties .cxx_destruct]
+ -[_NUTextureStylePersonInstanceProperties copyWithZone:]
+ -[_NUTextureStylePersonInstanceProperties description]
+ -[_NUTextureStylePersonInstanceProperties instanceMaskReferenceKey]
+ -[_NUTextureStylePersonInstanceProperties maskSize]
+ -[_NUTextureStylePersonInstanceProperties nu_updateDigest:]
+ -[_NUTextureStylePersonInstanceProperties opaquePersonInfo]
+ -[_NUTextureStylePersonInstanceProperties pixelFormat]
+ -[_NUTextureStylePersonInstanceProperties setInstanceMaskReferenceKey:]
+ -[_NUTextureStylePersonInstanceProperties setMaskSize:]
+ -[_NUTextureStylePersonInstanceProperties setOpaquePersonInfo:]
+ -[_NUTextureStylePersonInstanceProperties setPixelFormat:]
+ -[_NUTextureStyleProperties .cxx_destruct]
+ -[_NUTextureStyleProperties captureMode]
+ -[_NUTextureStyleProperties captureType]
+ -[_NUTextureStyleProperties copyWithZone:]
+ -[_NUTextureStyleProperties description]
+ -[_NUTextureStyleProperties filmGrainSeed]
+ -[_NUTextureStyleProperties hardwareModel]
+ -[_NUTextureStyleProperties isVideo]
+ -[_NUTextureStyleProperties nu_updateDigest:]
+ -[_NUTextureStyleProperties numberOfPersons]
+ -[_NUTextureStyleProperties personInstances]
+ -[_NUTextureStyleProperties portType]
+ -[_NUTextureStyleProperties setCaptureMode:]
+ -[_NUTextureStyleProperties setCaptureType:]
+ -[_NUTextureStyleProperties setFilmGrainSeed:]
+ -[_NUTextureStyleProperties setHardwareModel:]
+ -[_NUTextureStyleProperties setIsVideo:]
+ -[_NUTextureStyleProperties setNumberOfPersons:]
+ -[_NUTextureStyleProperties setPersonInstances:]
+ -[_NUTextureStyleProperties setPortType:]
+ -[_NUTextureStyleProperties setVersion:]
+ -[_NUTextureStyleProperties setVideoFacesInfoData:]
+ -[_NUTextureStyleProperties setVideoOpaquePersonsInfo:]
+ -[_NUTextureStyleProperties version]
+ -[_NUTextureStyleProperties videoFacesInfoData]
+ -[_NUTextureStyleProperties videoOpaquePersonsInfo]
+ GCC_except_table10016
+ GCC_except_table10026
+ GCC_except_table10241
+ GCC_except_table10242
+ GCC_except_table10248
+ GCC_except_table10249
+ GCC_except_table10251
+ GCC_except_table10252
+ GCC_except_table10349
+ GCC_except_table10350
+ GCC_except_table10366
+ GCC_except_table10367
+ GCC_except_table10368
+ GCC_except_table10393
+ GCC_except_table10394
+ GCC_except_table10395
+ GCC_except_table10397
+ GCC_except_table10398
+ GCC_except_table10399
+ GCC_except_table10400
+ GCC_except_table10401
+ GCC_except_table10402
+ GCC_except_table10403
+ GCC_except_table10406
+ GCC_except_table10407
+ GCC_except_table10410
+ GCC_except_table10411
+ GCC_except_table10412
+ GCC_except_table10418
+ GCC_except_table10419
+ GCC_except_table10420
+ GCC_except_table10421
+ GCC_except_table10422
+ GCC_except_table10423
+ GCC_except_table10425
+ GCC_except_table10427
+ GCC_except_table10428
+ GCC_except_table10429
+ GCC_except_table10434
+ GCC_except_table10435
+ GCC_except_table10436
+ GCC_except_table10437
+ GCC_except_table10440
+ GCC_except_table10441
+ GCC_except_table10442
+ GCC_except_table10443
+ GCC_except_table10444
+ GCC_except_table10445
+ GCC_except_table10446
+ GCC_except_table10447
+ GCC_except_table10452
+ GCC_except_table10453
+ GCC_except_table10454
+ GCC_except_table10455
+ GCC_except_table10456
+ GCC_except_table10457
+ GCC_except_table10503
+ GCC_except_table10554
+ GCC_except_table10631
+ GCC_except_table10635
+ GCC_except_table11077
+ GCC_except_table11238
+ GCC_except_table11240
+ GCC_except_table11338
+ GCC_except_table11346
+ GCC_except_table11351
+ GCC_except_table11352
+ GCC_except_table11356
+ GCC_except_table1901
+ GCC_except_table2026
+ GCC_except_table2027
+ GCC_except_table2028
+ GCC_except_table2029
+ GCC_except_table2031
+ GCC_except_table2056
+ GCC_except_table2110
+ GCC_except_table2219
+ GCC_except_table2220
+ GCC_except_table2757
+ GCC_except_table2822
+ GCC_except_table2870
+ GCC_except_table2882
+ GCC_except_table3041
+ GCC_except_table3188
+ GCC_except_table3268
+ GCC_except_table3275
+ GCC_except_table3276
+ GCC_except_table3277
+ GCC_except_table3278
+ GCC_except_table3279
+ GCC_except_table3282
+ GCC_except_table3283
+ GCC_except_table3286
+ GCC_except_table3289
+ GCC_except_table3290
+ GCC_except_table3292
+ GCC_except_table3295
+ GCC_except_table3297
+ GCC_except_table3298
+ GCC_except_table3301
+ GCC_except_table3302
+ GCC_except_table3313
+ GCC_except_table3342
+ GCC_except_table3343
+ GCC_except_table3348
+ GCC_except_table3349
+ GCC_except_table3351
+ GCC_except_table3354
+ GCC_except_table3355
+ GCC_except_table3359
+ GCC_except_table3362
+ GCC_except_table3363
+ GCC_except_table3365
+ GCC_except_table3366
+ GCC_except_table3369
+ GCC_except_table3371
+ GCC_except_table3373
+ GCC_except_table3374
+ GCC_except_table3375
+ GCC_except_table3376
+ GCC_except_table3377
+ GCC_except_table3381
+ GCC_except_table3387
+ GCC_except_table3739
+ GCC_except_table3919
+ GCC_except_table3988
+ GCC_except_table3992
+ GCC_except_table3994
+ GCC_except_table4139
+ GCC_except_table4140
+ GCC_except_table4145
+ GCC_except_table4151
+ GCC_except_table4156
+ GCC_except_table4179
+ GCC_except_table4186
+ GCC_except_table4191
+ GCC_except_table4193
+ GCC_except_table4320
+ GCC_except_table4321
+ GCC_except_table4322
+ GCC_except_table4325
+ GCC_except_table4326
+ GCC_except_table4327
+ GCC_except_table4334
+ GCC_except_table4339
+ GCC_except_table4340
+ GCC_except_table4341
+ GCC_except_table4343
+ GCC_except_table4345
+ GCC_except_table4360
+ GCC_except_table4362
+ GCC_except_table4423
+ GCC_except_table4424
+ GCC_except_table4427
+ GCC_except_table4428
+ GCC_except_table4433
+ GCC_except_table4434
+ GCC_except_table4437
+ GCC_except_table4438
+ GCC_except_table4439
+ GCC_except_table4440
+ GCC_except_table4441
+ GCC_except_table4442
+ GCC_except_table4443
+ GCC_except_table4445
+ GCC_except_table4451
+ GCC_except_table4455
+ GCC_except_table4459
+ GCC_except_table4460
+ GCC_except_table4461
+ GCC_except_table4463
+ GCC_except_table4470
+ GCC_except_table4472
+ GCC_except_table4473
+ GCC_except_table4548
+ GCC_except_table4849
+ GCC_except_table4960
+ GCC_except_table4966
+ GCC_except_table4969
+ GCC_except_table4979
+ GCC_except_table4983
+ GCC_except_table4984
+ GCC_except_table4998
+ GCC_except_table5107
+ GCC_except_table5237
+ GCC_except_table5319
+ GCC_except_table5611
+ GCC_except_table5713
+ GCC_except_table5754
+ GCC_except_table5790
+ GCC_except_table5792
+ GCC_except_table5794
+ GCC_except_table5799
+ GCC_except_table5808
+ GCC_except_table5809
+ GCC_except_table5813
+ GCC_except_table5859
+ GCC_except_table5899
+ GCC_except_table5923
+ GCC_except_table5926
+ GCC_except_table5947
+ GCC_except_table5950
+ GCC_except_table5951
+ GCC_except_table5952
+ GCC_except_table5961
+ GCC_except_table5963
+ GCC_except_table5965
+ GCC_except_table5966
+ GCC_except_table5974
+ GCC_except_table5981
+ GCC_except_table5982
+ GCC_except_table5987
+ GCC_except_table5988
+ GCC_except_table5989
+ GCC_except_table5991
+ GCC_except_table5992
+ GCC_except_table5993
+ GCC_except_table5994
+ GCC_except_table5995
+ GCC_except_table6000
+ GCC_except_table6001
+ GCC_except_table6002
+ GCC_except_table6003
+ GCC_except_table6005
+ GCC_except_table6006
+ GCC_except_table6010
+ GCC_except_table6011
+ GCC_except_table6012
+ GCC_except_table6013
+ GCC_except_table6014
+ GCC_except_table6015
+ GCC_except_table6016
+ GCC_except_table6017
+ GCC_except_table6019
+ GCC_except_table6021
+ GCC_except_table6024
+ GCC_except_table6025
+ GCC_except_table6026
+ GCC_except_table6027
+ GCC_except_table6028
+ GCC_except_table6030
+ GCC_except_table6032
+ GCC_except_table6033
+ GCC_except_table6035
+ GCC_except_table6036
+ GCC_except_table6144
+ GCC_except_table6148
+ GCC_except_table6208
+ GCC_except_table6240
+ GCC_except_table6241
+ GCC_except_table6278
+ GCC_except_table6284
+ GCC_except_table6292
+ GCC_except_table6313
+ GCC_except_table6393
+ GCC_except_table6405
+ GCC_except_table6408
+ GCC_except_table6413
+ GCC_except_table6429
+ GCC_except_table6447
+ GCC_except_table6450
+ GCC_except_table6451
+ GCC_except_table6455
+ GCC_except_table6456
+ GCC_except_table6559
+ GCC_except_table6568
+ GCC_except_table6588
+ GCC_except_table6605
+ GCC_except_table6679
+ GCC_except_table6745
+ GCC_except_table6750
+ GCC_except_table6753
+ GCC_except_table6776
+ GCC_except_table6820
+ GCC_except_table6963
+ GCC_except_table7038
+ GCC_except_table7053
+ GCC_except_table7054
+ GCC_except_table7055
+ GCC_except_table7068
+ GCC_except_table7069
+ GCC_except_table7070
+ GCC_except_table7071
+ GCC_except_table7086
+ GCC_except_table7087
+ GCC_except_table7101
+ GCC_except_table7102
+ GCC_except_table7107
+ GCC_except_table7147
+ GCC_except_table7220
+ GCC_except_table7221
+ GCC_except_table7225
+ GCC_except_table7227
+ GCC_except_table7231
+ GCC_except_table7233
+ GCC_except_table7235
+ GCC_except_table7236
+ GCC_except_table7240
+ GCC_except_table7244
+ GCC_except_table7245
+ GCC_except_table7246
+ GCC_except_table7247
+ GCC_except_table7248
+ GCC_except_table7250
+ GCC_except_table7251
+ GCC_except_table7253
+ GCC_except_table7254
+ GCC_except_table7324
+ GCC_except_table7359
+ GCC_except_table7396
+ GCC_except_table7397
+ GCC_except_table7447
+ GCC_except_table8140
+ GCC_except_table8143
+ GCC_except_table8209
+ GCC_except_table8348
+ GCC_except_table8356
+ GCC_except_table8359
+ GCC_except_table8361
+ GCC_except_table8366
+ GCC_except_table8380
+ GCC_except_table8382
+ GCC_except_table8383
+ GCC_except_table8388
+ GCC_except_table8389
+ GCC_except_table8409
+ GCC_except_table8416
+ GCC_except_table8417
+ GCC_except_table8418
+ GCC_except_table8419
+ GCC_except_table8432
+ GCC_except_table8620
+ GCC_except_table8667
+ GCC_except_table9010
+ GCC_except_table9104
+ GCC_except_table9282
+ GCC_except_table9476
+ GCC_except_table9491
+ GCC_except_table9528
+ GCC_except_table9535
+ GCC_except_table9573
+ GCC_except_table9574
+ GCC_except_table9575
+ GCC_except_table9576
+ GCC_except_table9581
+ GCC_except_table9611
+ GCC_except_table9612
+ GCC_except_table9613
+ GCC_except_table9618
+ GCC_except_table9620
+ GCC_except_table9621
+ GCC_except_table9622
+ GCC_except_table9623
+ GCC_except_table9627
+ GCC_except_table9628
+ GCC_except_table9630
+ GCC_except_table9632
+ GCC_except_table9634
+ GCC_except_table9636
+ GCC_except_table9642
+ GCC_except_table9645
+ GCC_except_table9649
+ GCC_except_table9650
+ GCC_except_table9652
+ GCC_except_table9653
+ GCC_except_table9654
+ GCC_except_table9655
+ GCC_except_table9656
+ GCC_except_table9658
+ GCC_except_table9659
+ GCC_except_table9660
+ GCC_except_table9661
+ GCC_except_table9662
+ GCC_except_table9663
+ GCC_except_table9664
+ GCC_except_table9665
+ GCC_except_table9666
+ GCC_except_table9668
+ GCC_except_table9669
+ GCC_except_table9670
+ GCC_except_table9671
+ GCC_except_table9672
+ GCC_except_table9673
+ GCC_except_table9675
+ GCC_except_table9732
+ GCC_except_table9739
+ GCC_except_table9817
+ GCC_except_table9889
+ GCC_except_table9890
+ GCC_except_table9894
+ GCC_except_table9895
+ GCC_except_table9896
+ GCC_except_table9897
+ GCC_except_table9905
+ GCC_except_table9914
+ GCC_except_table9924
+ GCC_except_table9930
+ GCC_except_table9931
+ GCC_except_table9932
+ GCC_except_table9935
+ GCC_except_table9937
+ GCC_except_table9940
+ GCC_except_table9941
+ GCC_except_table9942
+ _ImageIOLibrary
+ _ImageIOLibraryCore
+ _ImageIOLibraryCore.frameworkLibrary
+ _NUAuxiliaryImagesPropertiesKeyFromReferenceKey
+ _NUTextureStyleMetadataKey_FaceAttitude
+ _OBJC_CLASS_$__NUTextureStylePersonInstanceProperties
+ _OBJC_CLASS_$__NUTextureStyleProperties
+ _OBJC_IVAR_$_NUCGImageSourceNode._hasProvenanceData
+ _OBJC_IVAR_$_NUCGImageSourceNode._textureStylesProperties
+ _OBJC_IVAR_$_NUImageExportRequest._embedProvenanceData
+ _OBJC_IVAR_$__NUImageProperties._hasProvenanceData
+ _OBJC_IVAR_$__NUImageProperties._textureStyleProperties
+ _OBJC_IVAR_$__NUSemanticStyleProperties._linearHighKey
+ _OBJC_IVAR_$__NUSemanticStyleProperties._revertUsingOriginal
+ _OBJC_IVAR_$__NUTextureStylePersonInstanceProperties._instanceMaskReferenceKey
+ _OBJC_IVAR_$__NUTextureStylePersonInstanceProperties._maskSize
+ _OBJC_IVAR_$__NUTextureStylePersonInstanceProperties._opaquePersonInfo
+ _OBJC_IVAR_$__NUTextureStylePersonInstanceProperties._pixelFormat
+ _OBJC_IVAR_$__NUTextureStyleProperties._captureMode
+ _OBJC_IVAR_$__NUTextureStyleProperties._captureType
+ _OBJC_IVAR_$__NUTextureStyleProperties._filmGrainSeed
+ _OBJC_IVAR_$__NUTextureStyleProperties._hardwareModel
+ _OBJC_IVAR_$__NUTextureStyleProperties._isVideo
+ _OBJC_IVAR_$__NUTextureStyleProperties._numberOfPersons
+ _OBJC_IVAR_$__NUTextureStyleProperties._personInstances
+ _OBJC_IVAR_$__NUTextureStyleProperties._portType
+ _OBJC_IVAR_$__NUTextureStyleProperties._version
+ _OBJC_IVAR_$__NUTextureStyleProperties._videoFacesInfoData
+ _OBJC_IVAR_$__NUTextureStyleProperties._videoOpaquePersonsInfo
+ _OBJC_METACLASS_$__NUTextureStylePersonInstanceProperties
+ _OBJC_METACLASS_$__NUTextureStyleProperties
+ __OBJC_$_CLASS_METHODS__NUTextureStylePersonInstanceProperties
+ __OBJC_$_CLASS_METHODS__NUTextureStyleProperties
+ __OBJC_$_INSTANCE_METHODS__NUTextureStylePersonInstanceProperties
+ __OBJC_$_INSTANCE_METHODS__NUTextureStyleProperties
+ __OBJC_$_INSTANCE_VARIABLES__NUTextureStylePersonInstanceProperties
+ __OBJC_$_INSTANCE_VARIABLES__NUTextureStyleProperties
+ __OBJC_$_PROP_LIST_NUTextureStylePersonInstanceProperties
+ __OBJC_$_PROP_LIST_NUTextureStyleProperties
+ __OBJC_$_PROP_LIST__NUTextureStylePersonInstanceProperties
+ __OBJC_$_PROP_LIST__NUTextureStyleProperties
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NUTextureStylePersonInstanceProperties
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NUTextureStyleProperties
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NUTextureStylePersonInstanceProperties
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NUTextureStyleProperties
+ __OBJC_$_PROTOCOL_REFS_NUTextureStylePersonInstanceProperties
+ __OBJC_$_PROTOCOL_REFS_NUTextureStyleProperties
+ __OBJC_CLASS_PROTOCOLS_$__NUTextureStylePersonInstanceProperties
+ __OBJC_CLASS_PROTOCOLS_$__NUTextureStyleProperties
+ __OBJC_CLASS_RO_$__NUTextureStylePersonInstanceProperties
+ __OBJC_CLASS_RO_$__NUTextureStyleProperties
+ __OBJC_LABEL_PROTOCOL_$_NUTextureStylePersonInstanceProperties
+ __OBJC_LABEL_PROTOCOL_$_NUTextureStyleProperties
+ __OBJC_METACLASS_RO_$__NUTextureStylePersonInstanceProperties
+ __OBJC_METACLASS_RO_$__NUTextureStyleProperties
+ __OBJC_PROTOCOL_$_NUTextureStylePersonInstanceProperties
+ __OBJC_PROTOCOL_$_NUTextureStyleProperties
+ ___ImageIOLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___getCGImageDestinationSetProvenanceDataSymbolLoc_block_invoke
+ ___getCGImageSourceCopyProvenanceDataAtIndexSymbolLoc_block_invoke
+ __sl_dlopen
+ _audit_stringImageIO
+ _dlerror
+ _dlsym
+ _getCGImageDestinationSetProvenanceDataSymbolLoc.ptr
+ _getCGImageSourceCopyProvenanceDataAtIndexSymbolLoc
+ _getCGImageSourceCopyProvenanceDataAtIndexSymbolLoc.ptr
+ _kCMPhotoCustomMetadataTypeURN_Provenance_ProcessedImage
+ _kCMPhotoCustomMetadataTypeURN_Provenance_UnprocessedImage
+ _kMetadataIdentifier_TextureStyleInfo
+ _objc_msgSend$_loadPersonInstanceMaskMetadata
+ _objc_msgSend$_loadTextureStylesProperties:error:
+ _objc_msgSend$captureMode
+ _objc_msgSend$captureType
+ _objc_msgSend$embedProvenanceData
+ _objc_msgSend$filmGrainSeed
+ _objc_msgSend$hardwareModel
+ _objc_msgSend$hasProvenanceData
+ _objc_msgSend$instanceMaskReferenceKey
+ _objc_msgSend$linearHighKey
+ _objc_msgSend$maskSize
+ _objc_msgSend$metadataTrackContainsTextureStyleData:
+ _objc_msgSend$numberOfPersons
+ _objc_msgSend$opaquePersonInfo
+ _objc_msgSend$personInstancePropertiesFromDictionary:error:
+ _objc_msgSend$personInstances
+ _objc_msgSend$portType
+ _objc_msgSend$revertUsingOriginal
+ _objc_msgSend$setCaptureMode:
+ _objc_msgSend$setCaptureType:
+ _objc_msgSend$setFilmGrainSeed:
+ _objc_msgSend$setHardwareModel:
+ _objc_msgSend$setHasProvenanceData:
+ _objc_msgSend$setInstanceMaskReferenceKey:
+ _objc_msgSend$setLinearHighKey:
+ _objc_msgSend$setMaskSize:
+ _objc_msgSend$setNumberOfPersons:
+ _objc_msgSend$setOpaquePersonInfo:
+ _objc_msgSend$setPersonInstances:
+ _objc_msgSend$setPortType:
+ _objc_msgSend$setRevertUsingOriginal:
+ _objc_msgSend$setTextureStyleProperties:
+ _objc_msgSend$setTextureStylesProperties:
+ _objc_msgSend$setVideoFacesInfoData:
+ _objc_msgSend$setVideoOpaquePersonsInfo:
+ _objc_msgSend$textureStyleProperties
+ _objc_msgSend$textureStylePropertiesFromImageMetadata:auxImageMetadata:error:
+ _objc_msgSend$textureStylesProperties
+ _objc_msgSend$unsignedShortValue
+ _objc_msgSend$videoFacesInfoData
+ _objc_msgSend$videoOpaquePersonsInfo
- GCC_except_table10176
- GCC_except_table10177
- GCC_except_table10183
- GCC_except_table10184
- GCC_except_table10186
- GCC_except_table10187
- GCC_except_table10284
- GCC_except_table10285
- GCC_except_table10288
- GCC_except_table10289
- GCC_except_table10290
- GCC_except_table10291
- GCC_except_table10292
- GCC_except_table10293
- GCC_except_table10295
- GCC_except_table10298
- GCC_except_table10299
- GCC_except_table10301
- GCC_except_table10302
- GCC_except_table10303
- GCC_except_table10305
- GCC_except_table10306
- GCC_except_table10316
- GCC_except_table10317
- GCC_except_table10322
- GCC_except_table10323
- GCC_except_table10324
- GCC_except_table10325
- GCC_except_table10327
- GCC_except_table10328
- GCC_except_table10329
- GCC_except_table10330
- GCC_except_table10332
- GCC_except_table10333
- GCC_except_table10334
- GCC_except_table10335
- GCC_except_table10336
- GCC_except_table10337
- GCC_except_table10338
- GCC_except_table10341
- GCC_except_table10342
- GCC_except_table10345
- GCC_except_table10346
- GCC_except_table10347
- GCC_except_table10362
- GCC_except_table10369
- GCC_except_table10372
- GCC_except_table10373
- GCC_except_table10375
- GCC_except_table10376
- GCC_except_table10377
- GCC_except_table10378
- GCC_except_table10379
- GCC_except_table10380
- GCC_except_table10391
- GCC_except_table10489
- GCC_except_table10566
- GCC_except_table10570
- GCC_except_table11012
- GCC_except_table11173
- GCC_except_table11175
- GCC_except_table11221
- GCC_except_table11273
- GCC_except_table11281
- GCC_except_table11287
- GCC_except_table11291
- GCC_except_table1896
- GCC_except_table2019
- GCC_except_table2020
- GCC_except_table2021
- GCC_except_table2022
- GCC_except_table2023
- GCC_except_table2050
- GCC_except_table2104
- GCC_except_table2209
- GCC_except_table2210
- GCC_except_table2702
- GCC_except_table2767
- GCC_except_table2815
- GCC_except_table2827
- GCC_except_table2986
- GCC_except_table3133
- GCC_except_table3213
- GCC_except_table3220
- GCC_except_table3221
- GCC_except_table3222
- GCC_except_table3223
- GCC_except_table3224
- GCC_except_table3227
- GCC_except_table3228
- GCC_except_table3231
- GCC_except_table3234
- GCC_except_table3235
- GCC_except_table3237
- GCC_except_table3240
- GCC_except_table3241
- GCC_except_table3242
- GCC_except_table3243
- GCC_except_table3244
- GCC_except_table3245
- GCC_except_table3246
- GCC_except_table3247
- GCC_except_table3255
- GCC_except_table3258
- GCC_except_table3259
- GCC_except_table3264
- GCC_except_table3271
- GCC_except_table3287
- GCC_except_table3288
- GCC_except_table3293
- GCC_except_table3294
- GCC_except_table3304
- GCC_except_table3307
- GCC_except_table3308
- GCC_except_table3311
- GCC_except_table3316
- GCC_except_table3318
- GCC_except_table3320
- GCC_except_table3321
- GCC_except_table3322
- GCC_except_table3332
- GCC_except_table3684
- GCC_except_table3864
- GCC_except_table3933
- GCC_except_table3937
- GCC_except_table3939
- GCC_except_table4076
- GCC_except_table4084
- GCC_except_table4085
- GCC_except_table4090
- GCC_except_table4096
- GCC_except_table4101
- GCC_except_table4124
- GCC_except_table4136
- GCC_except_table4138
- GCC_except_table4265
- GCC_except_table4266
- GCC_except_table4267
- GCC_except_table4270
- GCC_except_table4271
- GCC_except_table4272
- GCC_except_table4277
- GCC_except_table4279
- GCC_except_table4284
- GCC_except_table4285
- GCC_except_table4286
- GCC_except_table4288
- GCC_except_table4290
- GCC_except_table4305
- GCC_except_table4307
- GCC_except_table4368
- GCC_except_table4369
- GCC_except_table4372
- GCC_except_table4373
- GCC_except_table4378
- GCC_except_table4379
- GCC_except_table4382
- GCC_except_table4383
- GCC_except_table4384
- GCC_except_table4385
- GCC_except_table4386
- GCC_except_table4388
- GCC_except_table4390
- GCC_except_table4396
- GCC_except_table4400
- GCC_except_table4404
- GCC_except_table4405
- GCC_except_table4406
- GCC_except_table4408
- GCC_except_table4415
- GCC_except_table4417
- GCC_except_table4418
- GCC_except_table4493
- GCC_except_table4792
- GCC_except_table4903
- GCC_except_table4909
- GCC_except_table4912
- GCC_except_table4922
- GCC_except_table4926
- GCC_except_table4927
- GCC_except_table4941
- GCC_except_table5050
- GCC_except_table5180
- GCC_except_table5262
- GCC_except_table5554
- GCC_except_table5656
- GCC_except_table5697
- GCC_except_table5733
- GCC_except_table5735
- GCC_except_table5737
- GCC_except_table5742
- GCC_except_table5751
- GCC_except_table5752
- GCC_except_table5756
- GCC_except_table5802
- GCC_except_table5821
- GCC_except_table5842
- GCC_except_table5847
- GCC_except_table5866
- GCC_except_table5868
- GCC_except_table5869
- GCC_except_table5874
- GCC_except_table5875
- GCC_except_table5877
- GCC_except_table5887
- GCC_except_table5890
- GCC_except_table5891
- GCC_except_table5892
- GCC_except_table5893
- GCC_except_table5894
- GCC_except_table5895
- GCC_except_table5896
- GCC_except_table5897
- GCC_except_table5898
- GCC_except_table5900
- GCC_except_table5901
- GCC_except_table5902
- GCC_except_table5903
- GCC_except_table5905
- GCC_except_table5906
- GCC_except_table5907
- GCC_except_table5908
- GCC_except_table5909
- GCC_except_table5910
- GCC_except_table5911
- GCC_except_table5912
- GCC_except_table5917
- GCC_except_table5918
- GCC_except_table5924
- GCC_except_table5930
- GCC_except_table5936
- GCC_except_table5937
- GCC_except_table5938
- GCC_except_table5943
- GCC_except_table5945
- GCC_except_table5946
- GCC_except_table5956
- GCC_except_table5970
- GCC_except_table5971
- GCC_except_table5973
- GCC_except_table5976
- GCC_except_table5978
- GCC_except_table5979
- GCC_except_table6087
- GCC_except_table6091
- GCC_except_table6151
- GCC_except_table6183
- GCC_except_table6184
- GCC_except_table6221
- GCC_except_table6228
- GCC_except_table6249
- GCC_except_table6329
- GCC_except_table6341
- GCC_except_table6344
- GCC_except_table6349
- GCC_except_table6364
- GCC_except_table6382
- GCC_except_table6385
- GCC_except_table6386
- GCC_except_table6390
- GCC_except_table6391
- GCC_except_table6494
- GCC_except_table6503
- GCC_except_table6523
- GCC_except_table6540
- GCC_except_table6614
- GCC_except_table6680
- GCC_except_table6685
- GCC_except_table6688
- GCC_except_table6711
- GCC_except_table6755
- GCC_except_table6898
- GCC_except_table6973
- GCC_except_table6988
- GCC_except_table6989
- GCC_except_table6990
- GCC_except_table7003
- GCC_except_table7004
- GCC_except_table7005
- GCC_except_table7006
- GCC_except_table7021
- GCC_except_table7022
- GCC_except_table7036
- GCC_except_table7037
- GCC_except_table7042
- GCC_except_table7082
- GCC_except_table7155
- GCC_except_table7156
- GCC_except_table7160
- GCC_except_table7162
- GCC_except_table7166
- GCC_except_table7168
- GCC_except_table7170
- GCC_except_table7171
- GCC_except_table7175
- GCC_except_table7179
- GCC_except_table7180
- GCC_except_table7181
- GCC_except_table7182
- GCC_except_table7183
- GCC_except_table7185
- GCC_except_table7186
- GCC_except_table7188
- GCC_except_table7189
- GCC_except_table7259
- GCC_except_table7294
- GCC_except_table7331
- GCC_except_table7332
- GCC_except_table7382
- GCC_except_table8075
- GCC_except_table8078
- GCC_except_table8144
- GCC_except_table8283
- GCC_except_table8286
- GCC_except_table8291
- GCC_except_table8294
- GCC_except_table8296
- GCC_except_table8301
- GCC_except_table8315
- GCC_except_table8317
- GCC_except_table8318
- GCC_except_table8323
- GCC_except_table8324
- GCC_except_table8344
- GCC_except_table8352
- GCC_except_table8353
- GCC_except_table8354
- GCC_except_table8367
- GCC_except_table8555
- GCC_except_table8602
- GCC_except_table8945
- GCC_except_table9039
- GCC_except_table9217
- GCC_except_table9411
- GCC_except_table9426
- GCC_except_table9463
- GCC_except_table9470
- GCC_except_table9508
- GCC_except_table9509
- GCC_except_table9510
- GCC_except_table9511
- GCC_except_table9516
- GCC_except_table9522
- GCC_except_table9523
- GCC_except_table9530
- GCC_except_table9533
- GCC_except_table9540
- GCC_except_table9542
- GCC_except_table9543
- GCC_except_table9545
- GCC_except_table9546
- GCC_except_table9547
- GCC_except_table9548
- GCC_except_table9553
- GCC_except_table9555
- GCC_except_table9556
- GCC_except_table9557
- GCC_except_table9558
- GCC_except_table9562
- GCC_except_table9563
- GCC_except_table9565
- GCC_except_table9567
- GCC_except_table9569
- GCC_except_table9571
- GCC_except_table9577
- GCC_except_table9580
- GCC_except_table9584
- GCC_except_table9585
- GCC_except_table9589
- GCC_except_table9590
- GCC_except_table9591
- GCC_except_table9593
- GCC_except_table9594
- GCC_except_table9596
- GCC_except_table9597
- GCC_except_table9599
- GCC_except_table9600
- GCC_except_table9601
- GCC_except_table9602
- GCC_except_table9603
- GCC_except_table9604
- GCC_except_table9606
- GCC_except_table9609
- GCC_except_table9752
- GCC_except_table9800
- GCC_except_table9824
- GCC_except_table9825
- GCC_except_table9829
- GCC_except_table9830
- GCC_except_table9831
- GCC_except_table9832
- GCC_except_table9840
- GCC_except_table9849
- GCC_except_table9859
- GCC_except_table9866
- GCC_except_table9867
- GCC_except_table9870
- GCC_except_table9872
- GCC_except_table9875
- GCC_except_table9876
- GCC_except_table9877
- GCC_except_table9951
- GCC_except_table9961
CStrings:
+ "%s"
+ "+[_NUTextureStylePersonInstanceProperties personInstancePropertiesFromDictionary:error:]"
+ "+[_NUTextureStyleProperties textureStylePropertiesFromImageMetadata:auxImageMetadata:error:]"
+ "+[_NUTextureStyleProperties textureStyleVideoPropertiesFromTextureStyleData:faceInfoData:error:]"
+ "<%@:%p referenceKey:%@>"
+ "<%@:%p version=%@ people:%lu hw=%@ port=%@ mode=%@ type=%@ seed=%@>"
+ "<%@:%p> url=%@ fileUTI=%@ size=%@ orientation=%@ colorSpace=%@ headroom=%f raw=%@ aux=%@ semanticStyle=%@ textureStyle=%@ metadata=%@"
+ "Bypassing revert for stills"
+ "CFDataRef  _Nullable soft_CGImageSourceCopyProvenanceDataAtIndex(CGImageSourceRef _Nonnull, size_t, uint32_t * _Nullable)"
+ "CGImageDestinationSetProvenanceData"
+ "CGImageSourceCopyProvenanceDataAtIndex"
+ "CaptureMode"
+ "CaptureType"
+ "Could not deserialize property list from texture metadata"
+ "Failed to extract provenance data, %{public}@"
+ "Failed to load person instance properties (%@), skipping"
+ "Failed to load texture style properties"
+ "FilmGrainSeed"
+ "HardwareModel"
+ "Invalid height value %@, skipping"
+ "Invalid instanceMaskReferenceKey value"
+ "Invalid linearHighKey: %{public}@, ignored"
+ "Invalid people data %@, treating as empty"
+ "Invalid person entry %@, skipping"
+ "Invalid pixel format value %@, skipping"
+ "Invalid revertUsingOriginal: %{public}@, ignored"
+ "Invalid texture style custom metadata"
+ "Invalid texture style version number"
+ "Invalid width value %@, skipping"
+ "LinearImage"
+ "Missing CMPhoto container"
+ "Missing mask metadata for key %@, skipping"
+ "Missing or invalid capture mode in texture style metadata: %@"
+ "Missing or invalid capture type in texture style metadata: %@"
+ "Missing or invalid hardware model in texture style metadata: %@"
+ "Missing or invalid port type in texture style metadata: %@"
+ "Missing texture style version value"
+ "NUImageExportJob.m"
+ "PortType"
+ "TextureStyleFaceAttitudeMetadata"
+ "TextureStylePeopleDataVersion"
+ "TextureStylePostProcessedPeopleData"
+ "_NUTextureStylePersonInstanceProperties<"
+ "_NUTextureStyleProperties<"
+ "captureMode:"
+ "captureType:"
+ "filmGrainSeed:"
+ "hardwareModel:"
+ "highKey"
+ "imageMetadata != nil"
+ "instanceMaskReferenceKey"
+ "instanceMaskReferenceKey:"
+ "kCGImageAuxiliaryDataTypeProvenanceProcessedImage"
+ "kCGImageAuxiliaryDataTypeProvenanceUnprocessedImage"
+ "l"
+ "linearHighKey:"
+ "maskSize:"
+ "mdta/com.apple.quicktime.texturestyle-info"
+ "personIntances:"
+ "pixelFormat:"
+ "portType:"
+ "revertUsingOriginal:"
+ "softlink:r:path:/System/Library/Frameworks/ImageIO.framework/ImageIO"
+ "tag:apple.com,2026:photo:metadata:texture_styles"
+ "textureData != nil"
+ "void *ImageIOLibrary(void)"
+ "void soft_CGImageDestinationSetProvenanceData(CGImageDestinationRef _Nonnull, uint32_t, CFDataRef _Nullable)"
- "<%@:%p> url=%@ fileUTI=%@ size=%@ orientation=%@ colorSpace=%@ headroom=%f raw=%@ aux=%@ semanticStyle=%@ metadata=%@"
```
