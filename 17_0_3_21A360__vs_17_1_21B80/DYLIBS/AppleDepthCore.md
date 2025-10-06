## AppleDepthCore

> `/System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore`

```diff

-109.2.0.0.0
-  __TEXT.__text: 0x577e0
+109.3.0.0.0
+  __TEXT.__text: 0x58154
   __TEXT.__auth_stubs: 0x1550
-  __TEXT.__objc_methlist: 0x1db4
-  __TEXT.__const: 0x1560
-  __TEXT.__gcc_except_tab: 0x4498
-  __TEXT.__oslogstring: 0x1642
-  __TEXT.__cstring: 0x28b2
-  __TEXT.__unwind_info: 0x1774
+  __TEXT.__objc_methlist: 0x1dd4
+  __TEXT.__const: 0x2160
+  __TEXT.__gcc_except_tab: 0x45bc
+  __TEXT.__oslogstring: 0x1737
+  __TEXT.__cstring: 0x2d06
+  __TEXT.__unwind_info: 0x17a0
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x43b
-  __TEXT.__objc_methname: 0x4cdc
-  __TEXT.__objc_methtype: 0x4010
-  __TEXT.__objc_stubs: 0x3100
+  __TEXT.__objc_methname: 0x4e3a
+  __TEXT.__objc_methtype: 0x40bd
+  __TEXT.__objc_stubs: 0x3160
   __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2ae0
-  __DATA_CONST.__objc_selrefs: 0x10f0
+  __DATA_CONST.__objc_const: 0x2b90
+  __DATA_CONST.__objc_selrefs: 0x1110
   __DATA_CONST.__objc_arraydata: 0x160
-  __AUTH_CONST.__cfstring: 0x1b40
+  __AUTH_CONST.__cfstring: 0x2120
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__auth_got: 0xab8
   __DATA.__got_weak: 0x20
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x180
+  __DATA.__objc_classrefs: 0x188
   __DATA.__objc_superrefs: 0xd0
   __DATA.__objc_ivar: 0x248
   __DATA.__data: 0x1f8
   __DATA.__bss: 0x1d0
-  __DATA_DIRTY.__const: 0x170
+  __DATA_DIRTY.__const: 0x110
   __DATA_DIRTY.__objc_const: 0xdc0
   __DATA_DIRTY.__objc_data: 0xb90
   __DATA_DIRTY.__bss: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EF3B9768-D9CD-337D-A01A-8E4863F89E53
-  Functions: 1064
-  Symbols:   3656
-  CStrings:  1836
+  UUID: C9B00A9E-94D5-3238-8244-DDBEF5EA5366
+  Functions: 1069
+  Symbols:   3675
+  CStrings:  1898
 
Symbols:
+ +[ADFigCameraCalibrationSource calcSensorCrop:onImageWithDimensions:metadataDictionary:negativeCropHandling:]
+ +[ADPointCloudAggregator aggregatePointClouds:calibrations:worldToPlatformTransforms:projectingToCamera:worldToPlatformAtProjectionTime:]
+ +[ADPointCloudAggregator aggregatePointClouds:pointCloudToPlatformTransforms:worldToPlatformTransforms:projectingToCamera:worldToPlatformAtProjectionTime:]
+ GCC_except_table1003
+ GCC_except_table1004
+ GCC_except_table1005
+ GCC_except_table1006
+ GCC_except_table1012
+ GCC_except_table1013
+ GCC_except_table1018
+ GCC_except_table1026
+ GCC_except_table1027
+ GCC_except_table1028
+ GCC_except_table1029
+ GCC_except_table1040
+ GCC_except_table1041
+ GCC_except_table1048
+ GCC_except_table1052
+ GCC_except_table1055
+ GCC_except_table1056
+ GCC_except_table264
+ GCC_except_table268
+ GCC_except_table274
+ GCC_except_table275
+ GCC_except_table280
+ GCC_except_table288
+ GCC_except_table292
+ GCC_except_table302
+ GCC_except_table305
+ GCC_except_table314
+ GCC_except_table343
+ GCC_except_table344
+ GCC_except_table351
+ GCC_except_table370
+ GCC_except_table374
+ GCC_except_table379
+ GCC_except_table380
+ GCC_except_table383
+ GCC_except_table384
+ GCC_except_table398
+ GCC_except_table399
+ GCC_except_table403
+ GCC_except_table407
+ GCC_except_table413
+ GCC_except_table414
+ GCC_except_table422
+ GCC_except_table425
+ GCC_except_table426
+ GCC_except_table441
+ GCC_except_table444
+ GCC_except_table454
+ GCC_except_table455
+ GCC_except_table469
+ GCC_except_table472
+ GCC_except_table473
+ GCC_except_table476
+ GCC_except_table480
+ GCC_except_table481
+ GCC_except_table496
+ GCC_except_table501
+ GCC_except_table504
+ GCC_except_table505
+ GCC_except_table514
+ GCC_except_table519
+ GCC_except_table530
+ GCC_except_table531
+ GCC_except_table535
+ GCC_except_table538
+ GCC_except_table548
+ GCC_except_table557
+ GCC_except_table561
+ GCC_except_table564
+ GCC_except_table568
+ GCC_except_table575
+ GCC_except_table576
+ GCC_except_table581
+ GCC_except_table587
+ GCC_except_table593
+ GCC_except_table605
+ GCC_except_table606
+ GCC_except_table617
+ GCC_except_table621
+ GCC_except_table624
+ GCC_except_table625
+ GCC_except_table629
+ GCC_except_table640
+ GCC_except_table641
+ GCC_except_table650
+ GCC_except_table651
+ GCC_except_table660
+ GCC_except_table665
+ GCC_except_table668
+ GCC_except_table675
+ GCC_except_table676
+ GCC_except_table691
+ GCC_except_table692
+ GCC_except_table704
+ GCC_except_table705
+ GCC_except_table708
+ GCC_except_table709
+ GCC_except_table712
+ GCC_except_table715
+ GCC_except_table716
+ GCC_except_table722
+ GCC_except_table723
+ GCC_except_table726
+ GCC_except_table727
+ GCC_except_table769
+ GCC_except_table775
+ GCC_except_table776
+ GCC_except_table779
+ GCC_except_table809
+ GCC_except_table812
+ GCC_except_table814
+ GCC_except_table815
+ GCC_except_table831
+ GCC_except_table839
+ GCC_except_table850
+ GCC_except_table855
+ GCC_except_table856
+ GCC_except_table857
+ GCC_except_table858
+ GCC_except_table869
+ GCC_except_table875
+ GCC_except_table876
+ GCC_except_table877
+ GCC_except_table878
+ GCC_except_table894
+ GCC_except_table895
+ GCC_except_table896
+ GCC_except_table897
+ GCC_except_table903
+ GCC_except_table905
+ GCC_except_table916
+ GCC_except_table921
+ GCC_except_table924
+ GCC_except_table937
+ GCC_except_table938
+ GCC_except_table939
+ GCC_except_table949
+ GCC_except_table954
+ GCC_except_table956
+ GCC_except_table961
+ GCC_except_table962
+ GCC_except_table963
+ GCC_except_table964
+ GCC_except_table973
+ GCC_except_table975
+ GCC_except_table976
+ GCC_except_table987
+ GCC_except_table989
+ GCC_except_table990
+ GCC_except_table992
+ GCC_except_table998
+ __OBJC_CLASS_PROTOCOLS_$_ADDynamicPolynomialsLensDistortionModel
+ __OBJC_CLASS_PROTOCOLS_$_ADRefinedPolynomialsLensDistortionModel
+ __PromotedConst.1753
+ __PromotedConst.1754
+ __PromotedConst.1755
+ __PromotedConst.1756
+ __PromotedConst.1757
+ __PromotedConst.1758
+ __ZL15INSTRUMENTS_ENDjyyyy.1113
+ __ZL15INSTRUMENTS_ENDjyyyy.1119
+ __ZL15INSTRUMENTS_ENDjyyyy.1359
+ __ZL15INSTRUMENTS_ENDjyyyy.1412
+ __ZL15INSTRUMENTS_ENDjyyyy.1620
+ __ZL15INSTRUMENTS_ENDjyyyy.1732
+ __ZL15INSTRUMENTS_ENDjyyyy.296
+ __ZL15INSTRUMENTS_ENDjyyyy.378
+ __ZL15INSTRUMENTS_ENDjyyyy.452
+ __ZL15INSTRUMENTS_ENDjyyyy.458
+ __ZL15INSTRUMENTS_ENDjyyyy.524
+ __ZL15INSTRUMENTS_ENDjyyyy.603
+ __ZL15INSTRUMENTS_ENDjyyyy.676
+ __ZL15INSTRUMENTS_ENDjyyyy.945
+ __ZL17INSTRUMENTS_EVENTjyyyy.1114
+ __ZL17INSTRUMENTS_EVENTjyyyy.1120
+ __ZL17INSTRUMENTS_EVENTjyyyy.1360
+ __ZL17INSTRUMENTS_EVENTjyyyy.1413
+ __ZL17INSTRUMENTS_EVENTjyyyy.1621
+ __ZL17INSTRUMENTS_EVENTjyyyy.1733
+ __ZL17INSTRUMENTS_EVENTjyyyy.297
+ __ZL17INSTRUMENTS_EVENTjyyyy.379
+ __ZL17INSTRUMENTS_EVENTjyyyy.453
+ __ZL17INSTRUMENTS_EVENTjyyyy.459
+ __ZL17INSTRUMENTS_EVENTjyyyy.525
+ __ZL17INSTRUMENTS_EVENTjyyyy.604
+ __ZL17INSTRUMENTS_EVENTjyyyy.677
+ __ZL17INSTRUMENTS_EVENTjyyyy.946
+ __ZL17INSTRUMENTS_STARTjyyyy.1115
+ __ZL17INSTRUMENTS_STARTjyyyy.1121
+ __ZL17INSTRUMENTS_STARTjyyyy.1361
+ __ZL17INSTRUMENTS_STARTjyyyy.1414
+ __ZL17INSTRUMENTS_STARTjyyyy.1622
+ __ZL17INSTRUMENTS_STARTjyyyy.1734
+ __ZL17INSTRUMENTS_STARTjyyyy.298
+ __ZL17INSTRUMENTS_STARTjyyyy.380
+ __ZL17INSTRUMENTS_STARTjyyyy.454
+ __ZL17INSTRUMENTS_STARTjyyyy.460
+ __ZL17INSTRUMENTS_STARTjyyyy.526
+ __ZL17INSTRUMENTS_STARTjyyyy.605
+ __ZL17INSTRUMENTS_STARTjyyyy.678
+ __ZL17INSTRUMENTS_STARTjyyyy.947
+ __ZN16PixelBufferUtils13getTurboColorEfRfS0_S0_
+ __ZN16PixelBufferUtils22pixelBufferFromRawFileEPKc
+ __ZNSt3__19to_stringEm
+ __ZNSt3__1L19piecewise_constructE.1074
+ __ZNSt3__1L19piecewise_constructE.178
+ __ZNSt3__1L19piecewise_constructE.650
+ __ZNSt3__1L19piecewise_constructE.845
+ __ZZN16PixelBufferUtils13getTurboColorEfRfS0_S0_E6redMap
+ __ZZN16PixelBufferUtils13getTurboColorEfRfS0_S0_E7blueMap
+ __ZZN16PixelBufferUtils13getTurboColorEfRfS0_S0_E8greenMap
+ ___block_literal_global.1150
+ ___block_literal_global.203
+ ___block_literal_global.205
+ ___block_literal_global.207
+ __unnamed_array_storage.1244
+ _objc_msgSend$aggregatePointClouds:pointCloudToPlatformTransforms:worldToPlatformTransforms:projectingToCamera:worldToPlatformAtProjectionTime:
+ _objc_msgSend$getFrameTransformsFromMetadataDictionary:sensorCropRect:rawSensorSize:postReadCropRect:
+ _objc_msgSend$stringByDeletingPathExtension
- GCC_except_table1001
- GCC_except_table1002
- GCC_except_table1008
- GCC_except_table1009
- GCC_except_table1010
- GCC_except_table1015
- GCC_except_table1017
- GCC_except_table1022
- GCC_except_table1024
- GCC_except_table1035
- GCC_except_table1036
- GCC_except_table1037
- GCC_except_table1038
- GCC_except_table1045
- GCC_except_table261
- GCC_except_table266
- GCC_except_table271
- GCC_except_table272
- GCC_except_table278
- GCC_except_table286
- GCC_except_table290
- GCC_except_table300
- GCC_except_table303
- GCC_except_table312
- GCC_except_table334
- GCC_except_table335
- GCC_except_table349
- GCC_except_table368
- GCC_except_table372
- GCC_except_table375
- GCC_except_table376
- GCC_except_table381
- GCC_except_table382
- GCC_except_table395
- GCC_except_table396
- GCC_except_table401
- GCC_except_table402
- GCC_except_table405
- GCC_except_table409
- GCC_except_table420
- GCC_except_table421
- GCC_except_table424
- GCC_except_table439
- GCC_except_table440
- GCC_except_table445
- GCC_except_table448
- GCC_except_table466
- GCC_except_table467
- GCC_except_table471
- GCC_except_table474
- GCC_except_table478
- GCC_except_table479
- GCC_except_table494
- GCC_except_table499
- GCC_except_table502
- GCC_except_table503
- GCC_except_table512
- GCC_except_table513
- GCC_except_table527
- GCC_except_table528
- GCC_except_table533
- GCC_except_table534
- GCC_except_table546
- GCC_except_table555
- GCC_except_table558
- GCC_except_table559
- GCC_except_table566
- GCC_except_table571
- GCC_except_table574
- GCC_except_table579
- GCC_except_table583
- GCC_except_table591
- GCC_except_table602
- GCC_except_table603
- GCC_except_table611
- GCC_except_table612
- GCC_except_table619
- GCC_except_table623
- GCC_except_table627
- GCC_except_table637
- GCC_except_table638
- GCC_except_table643
- GCC_except_table648
- GCC_except_table655
- GCC_except_table656
- GCC_except_table662
- GCC_except_table672
- GCC_except_table673
- GCC_except_table682
- GCC_except_table683
- GCC_except_table702
- GCC_except_table703
- GCC_except_table706
- GCC_except_table707
- GCC_except_table710
- GCC_except_table713
- GCC_except_table714
- GCC_except_table719
- GCC_except_table720
- GCC_except_table724
- GCC_except_table725
- GCC_except_table767
- GCC_except_table768
- GCC_except_table771
- GCC_except_table777
- GCC_except_table803
- GCC_except_table804
- GCC_except_table827
- GCC_except_table835
- GCC_except_table843
- GCC_except_table844
- GCC_except_table845
- GCC_except_table846
- GCC_except_table854
- GCC_except_table865
- GCC_except_table866
- GCC_except_table867
- GCC_except_table872
- GCC_except_table873
- GCC_except_table885
- GCC_except_table886
- GCC_except_table887
- GCC_except_table888
- GCC_except_table899
- GCC_except_table900
- GCC_except_table901
- GCC_except_table913
- GCC_except_table920
- GCC_except_table929
- GCC_except_table930
- GCC_except_table935
- GCC_except_table941
- GCC_except_table942
- GCC_except_table952
- GCC_except_table957
- GCC_except_table958
- GCC_except_table959
- GCC_except_table960
- GCC_except_table967
- GCC_except_table968
- GCC_except_table969
- GCC_except_table979
- GCC_except_table982
- GCC_except_table984
- GCC_except_table985
- GCC_except_table994
- GCC_except_table996
- GCC_except_table999
- __PromotedConst.1723
- __PromotedConst.1724
- __PromotedConst.1725
- __PromotedConst.1726
- __PromotedConst.1727
- __PromotedConst.1728
- __ZL15INSTRUMENTS_ENDjyyyy.1106
- __ZL15INSTRUMENTS_ENDjyyyy.1112
- __ZL15INSTRUMENTS_ENDjyyyy.1342
- __ZL15INSTRUMENTS_ENDjyyyy.1395
- __ZL15INSTRUMENTS_ENDjyyyy.1590
- __ZL15INSTRUMENTS_ENDjyyyy.1702
- __ZL15INSTRUMENTS_ENDjyyyy.274
- __ZL15INSTRUMENTS_ENDjyyyy.352
- __ZL15INSTRUMENTS_ENDjyyyy.442
- __ZL15INSTRUMENTS_ENDjyyyy.448
- __ZL15INSTRUMENTS_ENDjyyyy.522
- __ZL15INSTRUMENTS_ENDjyyyy.601
- __ZL15INSTRUMENTS_ENDjyyyy.674
- __ZL15INSTRUMENTS_ENDjyyyy.940
- __ZL17INSTRUMENTS_EVENTjyyyy.1107
- __ZL17INSTRUMENTS_EVENTjyyyy.1113
- __ZL17INSTRUMENTS_EVENTjyyyy.1343
- __ZL17INSTRUMENTS_EVENTjyyyy.1396
- __ZL17INSTRUMENTS_EVENTjyyyy.1591
- __ZL17INSTRUMENTS_EVENTjyyyy.1703
- __ZL17INSTRUMENTS_EVENTjyyyy.275
- __ZL17INSTRUMENTS_EVENTjyyyy.353
- __ZL17INSTRUMENTS_EVENTjyyyy.443
- __ZL17INSTRUMENTS_EVENTjyyyy.449
- __ZL17INSTRUMENTS_EVENTjyyyy.523
- __ZL17INSTRUMENTS_EVENTjyyyy.602
- __ZL17INSTRUMENTS_EVENTjyyyy.675
- __ZL17INSTRUMENTS_EVENTjyyyy.941
- __ZL17INSTRUMENTS_STARTjyyyy.1108
- __ZL17INSTRUMENTS_STARTjyyyy.1114
- __ZL17INSTRUMENTS_STARTjyyyy.1344
- __ZL17INSTRUMENTS_STARTjyyyy.1397
- __ZL17INSTRUMENTS_STARTjyyyy.1592
- __ZL17INSTRUMENTS_STARTjyyyy.1704
- __ZL17INSTRUMENTS_STARTjyyyy.276
- __ZL17INSTRUMENTS_STARTjyyyy.354
- __ZL17INSTRUMENTS_STARTjyyyy.444
- __ZL17INSTRUMENTS_STARTjyyyy.450
- __ZL17INSTRUMENTS_STARTjyyyy.524
- __ZL17INSTRUMENTS_STARTjyyyy.603
- __ZL17INSTRUMENTS_STARTjyyyy.676
- __ZL17INSTRUMENTS_STARTjyyyy.942
- __ZNSt3__1L19piecewise_constructE.1068
- __ZNSt3__1L19piecewise_constructE.175
- __ZNSt3__1L19piecewise_constructE.648
- __ZNSt3__1L19piecewise_constructE.851
- __ZNSt3__1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
- ___block_literal_global.105
- ___block_literal_global.107
- ___block_literal_global.109
- ___block_literal_global.1143
- __unnamed_array_storage.1231
CStrings:
+ "%s:%d - ERROR - Cannot read extension from file path. Unknown pixel format"
+ "%s:%d - ERROR - Data size does not match dimensions. padding is not supported"
+ "%s:%d - ERROR - Failed opening file %s for write: %s"
+ "%s:%d - ERROR - Failed reading input file"
+ "%s:%d - ERROR - Input and output buffers do not have the same number of planes"
+ "%s:%d - ERROR - Invalid output buffer dimensions"
+ "%s:%d - ERROR - Only up to 3 planes are supported"
+ "%s:%d - ERROR - Region is outside dimensions"
+ "%s:%d - ERROR - Unable to create image rotation session"
+ "%s:%d - ERROR - Unable to create pixel transfer session for image downscaling"
+ "%s:%d - ERROR - VTImageRotationSessionTransferImage operation failed"
+ "%s:%d - ERROR - VTPixelTransferSessionTransferImage operation failed"
+ "%s:%d - ERROR - asVImageBuffer returned null pointer. Did you forget to lock the CVPixelBuffer before use?"
+ "%s:%d - ERROR - bad dimensions provided when reading file"
+ "%s:%d - ERROR - cannot add circles to pixel buffer. illegal argument"
+ "%s:%d - ERROR - cannot add text to pixel buffer. illegal argument"
+ "%s:%d - ERROR - cannot add text to pixel buffer. illegal text location"
+ "%s:%d - ERROR - cannot alpha blend buffers - not same size/format"
+ "%s:%d - ERROR - cannot copy null session"
+ "%s:%d - ERROR - cannot update crop: pixelBufferUtilsSession does not define a transper session"
+ "%s:%d - ERROR - canoot request plane for single-plane image"
+ "%s:%d - ERROR - could not create context"
+ "%s:%d - ERROR - could not create pixel buffer"
+ "%s:%d - ERROR - crop dimensions must be integers"
+ "%s:%d - ERROR - did not find dimensions in file name - extension ill formatted"
+ "%s:%d - ERROR - did not find dimensions in file name - extension missing"
+ "%s:%d - ERROR - did not find dimensions in file name - width/height ill formatted"
+ "%s:%d - ERROR - failed allocating intermediate buffer for session"
+ "%s:%d - ERROR - failed colorizing and overlaying tile"
+ "%s:%d - ERROR - failed setting HW acceleration for pixelTransferSession"
+ "%s:%d - ERROR - failed setting HW acceleration for rotationSession"
+ "%s:%d - ERROR - invalid crop dimensions"
+ "%s:%d - ERROR - mismatching planes number in input buffers"
+ "%s:%d - ERROR - muliplane pixel buffer with nonmatching plane index"
+ "%s:%d - ERROR - muliplane pixel buffers with nonmatching plane index"
+ "%s:%d - ERROR - pixel transfer session failed"
+ "%s:%d - ERROR - pixelBufferUtilsSession failed to update crop"
+ "%s:%d - ERROR - provided pixel buffers size/format do not match those at creation time"
+ "%s:%d - ERROR - reflection not supperted at the moment"
+ "%s:%d - ERROR - rotation session failed"
+ "%s:%d - ERROR - rotation session is not supported for pixel format"
+ "%s:%d - ERROR - session does not support scaling"
+ "%s:%d - ERROR - this conversion is not supported"
+ "%s:%d - ERROR - transfer session is not supported for pixel format"
+ "%s:%d - ERROR - unable to render tiled view. images array not matching expected tile count"
+ "%s:%d - ERROR - unable to render tiled view. top text provided, but instance initialized without text space"
+ "%s:%d - ERROR - unknown scaling mode"
+ "+[ADFigCameraCalibrationSource calcSensorCrop:onImageWithDimensions:metadataDictionary:negativeCropHandling:]"
+ "@112@0:8@16@24^{?=[4]}32@40{?=[4]}48"
+ "@112@0:8@16^{?=[4]}24^{?=[4]}32@40{?=[4]}48"
+ "ADFigCameraCalibrationSource.mm"
+ "aggregatePointClouds:calibrations:worldToPlatformTransforms:projectingToCamera:worldToPlatformAtProjectionTime:"
+ "aggregatePointClouds:pointCloudToPlatformTransforms:worldToPlatformTransforms:projectingToCamera:worldToPlatformAtProjectionTime:"
+ "calcSensorCrop:onImageWithDimensions:metadataDictionary:negativeCropHandling:"
+ "cannot aggregate point cloud. expecting either 1 calibration instance, or one per point cloud. got %lu calibration and %lu point clouds"
+ "cannot aggregate point cloud. no calibration provided"
+ "cannot aggregate point cloud. no point clouds provided"
+ "stringByDeletingPathExtension"
+ "x"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGSize=dd}48@64q72"
- " for write:"
- "%s:%d - ERROR - %s\n"
- "Cannot read extension from file path. Unknown pixel format"
- "Data size does not match dimensions. padding is not supported"
- "Failed opening file "
- "Failed reading input file"
- "Input and output buffers do not have the same number of planes"
- "Invalid output buffer dimensions"
- "Only up to 3 planes are supported"
- "Region is outside dimensions"
- "Unable to create image rotation session"
- "Unable to create pixel transfer session for image downscaling"
- "VTImageRotationSessionTransferImage operation failed"
- "VTPixelTransferSessionTransferImage operation failed"
- "asVImageBuffer returned null pointer. Did you forget to lock the CVPixelBuffer before use?"
- "cannot add circles to pixel buffer. illegal argument"
- "cannot add text to pixel buffer. illegal argument"
- "cannot add text to pixel buffer. illegal text location"
- "cannot alpha blend buffers - not same size/format"
- "cannot copy null session"
- "cannot update crop: pixelBufferUtilsSession does not define a transper session"
- "canoot request plane for single-plane image"
- "could not create context"
- "could not create pixel buffer"
- "crop dimensions must be integers"
- "failed allocating intermediate buffer for session"
- "failed colorizing and overlaying tile"
- "failed setting HW acceleration for pixelTransferSession"
- "failed setting HW acceleration for rotationSession"
- "invalid crop dimensions"
- "mismatching planes number in input buffers"
- "muliplane pixel buffer with nonmatching plane index"
- "muliplane pixel buffers with nonmatching plane index"
- "pixel transfer session failed"
- "pixelBufferUtilsSession failed to update crop"
- "provided pixel buffers size/format do not match those at creation time"
- "reflection not supperted at the moment"
- "rotation session failed"
- "rotation session is not supported for pixel format"
- "session does not support scaling"
- "this conversion is not supported"
- "transfer session is not supported for pixel format"
- "unable to render tiled view. images array not matching expected tile count"
- "unable to render tiled view. top text provided, but instance initialized without text space"
- "unknown scaling mode"

```
