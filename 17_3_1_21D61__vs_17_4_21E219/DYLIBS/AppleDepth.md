## AppleDepth

> `/System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth`

```diff

-109.3.0.0.0
-  __TEXT.__text: 0x9e148
-  __TEXT.__auth_stubs: 0x12f0
-  __TEXT.__objc_methlist: 0x44d4
-  __TEXT.__const: 0x10f0
-  __TEXT.__gcc_except_tab: 0x96ec
-  __TEXT.__cstring: 0x46ae
-  __TEXT.__oslogstring: 0x4e81
-  __TEXT.__unwind_info: 0x25dc
+115.0.0.0.0
+  __TEXT.__text: 0xa0248
+  __TEXT.__auth_stubs: 0x1330
+  __TEXT.__objc_methlist: 0x457c
+  __TEXT.__const: 0x1150
+  __TEXT.__gcc_except_tab: 0xa178
+  __TEXT.__cstring: 0x43ab
+  __TEXT.__oslogstring: 0x5181
+  __TEXT.__unwind_info: 0x2668
   __TEXT.__eh_frame: 0xc0
-  __TEXT.__objc_classname: 0x10dfb
-  __TEXT.__objc_methname: 0xd528
-  __TEXT.__objc_methtype: 0x4538
-  __TEXT.__objc_stubs: 0x6e20
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x300
-  __DATA_CONST.__objc_classlist: 0x380
+  __TEXT.__objc_classname: 0x10e56
+  __TEXT.__objc_methname: 0xd870
+  __TEXT.__objc_methtype: 0x461c
+  __TEXT.__objc_stubs: 0x6f00
+  __DATA_CONST.__got: 0x1f8
+  __DATA_CONST.__const: 0x2c8
+  __DATA_CONST.__objc_classlist: 0x390
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x99e0
-  __DATA_CONST.__objc_selrefs: 0x22a0
-  __DATA_CONST.__objc_arraydata: 0xe0
+  __DATA_CONST.__objc_const: 0x9d70
+  __DATA_CONST.__objc_selrefs: 0x2310
+  __DATA_CONST.__objc_classrefs: 0x418
+  __DATA_CONST.__objc_superrefs: 0x308
+  __DATA_CONST.__objc_arraydata: 0x128
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__objc_const: 0x318
-  __AUTH_CONST.__cfstring: 0x4680
-  __AUTH_CONST.__objc_intobj: 0x1e0
-  __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__objc_const: 0x240
+  __AUTH_CONST.__cfstring: 0x4280
+  __AUTH_CONST.__objc_intobj: 0x1f8
+  __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x988
-  __AUTH.__objc_data: 0x320
-  __DATA.__got_weak: 0x58
-  __DATA.__objc_classrefs: 0x3f0
-  __DATA.__objc_superrefs: 0x2e8
-  __DATA.__objc_ivar: 0xb78
-  __DATA.__data: 0x440
+  __AUTH_CONST.__auth_got: 0x9a8
+  __AUTH.__objc_data: 0x230
+  __DATA.__got_weak: 0x60
+  __DATA.__objc_ivar: 0xba0
+  __DATA.__data: 0x3c8
   __DATA.__bss: 0x1a1
   __DATA_DIRTY.__const: 0x3b0
-  __DATA_DIRTY.__objc_const: 0x1f30
-  __DATA_DIRTY.__objc_data: 0x1fe0
+  __DATA_DIRTY.__objc_const: 0x2098
+  __DATA_DIRTY.__objc_data: 0x2170
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: AD81CE9C-8867-3247-8822-FFAF8DA07EE7
-  Functions: 2019
-  Symbols:   7288
-  CStrings:  4226
+  UUID: C119B108-01A6-39C6-92D7-E18229F7AFE0
+  Functions: 2049
+  Symbols:   7377
+  CStrings:  4202
 
Symbols:
+ +[ADNetworkProvider getAlternativePathForNetwork:]
+ +[ADNetworkProvider getConfigFolderForNetwork:]
+ +[ADNetworkProvider getDefaultPathForNetwork:allowPrecompiledModel:]
+ +[ADNetworkProvider providerForNetwork:requestedLayouts:]
+ +[ADNetworkProvider providerForNetwork:requestedLayouts:espressoEngine:]
+ +[ADNetworkProvider supportedSizesForSizesDict:key:expectedPixelFormat:]
+ +[ADNetworkProvider updateSizeForItem:fromShape:forLayout:target:]
+ -[ADDensifiedLiDARFocusAssistPipelineParameters confidenceUnits]
+ -[ADDensifiedLiDARFocusAssistPipelineParameters setConfidenceUnits:]
+ -[ADFlowFrameInput pearl]
+ -[ADFlowFrameInput pointClouds]
+ -[ADFlowFrameInput secondaryColor]
+ -[ADFlowFrameInput setPearl:]
+ -[ADFlowFrameInput setPointClouds:]
+ -[ADFlowFrameInput setSecondaryColor:]
+ -[ADFlowFrameOutput .cxx_destruct]
+ -[ADFlowFrameOutput figuresOfMerit]
+ -[ADFlowFrameOutput normals]
+ -[ADFlowFrameOutput setFiguresOfMerit:]
+ -[ADFlowFrameOutput setNormals:]
+ -[ADJasperColorExecutor executeWithColor:colorCameraCalibration:colorWorldToPlatformTransform:pointClouds:lidarCameraCalibration:pointCloudWorldToPlatformTransforms:outDepthMap:outConfMap:outNormalsMap:]
+ -[ADJasperColorFlow pushColor:pose:calibration:metadata:timestamp:]
+ -[ADJasperColorInFieldCalibrationControllerParameters setThresholdAngularVelocity:]
+ -[ADJasperColorInFieldCalibrationControllerParameters thresholdAngularVelocity]
+ -[ADJasperColorInFieldCalibrationExecutor preprocessInputColorFrame:colorPose:jasperPointClouds:jasperPoses:jasperCameraCalibration:colorCameraCalibration:timestamp:colorMetadata:]
+ -[ADJasperColorInFieldCalibrationPipeline getDeviceFrequency]
+ -[ADJasperColorInFieldCalibrationPipeline isAngularVelocityValid:]
+ -[ADJasperColorInFieldCalibrationResult initWithDictionary:]
+ -[ADJasperColorInFieldCalibrationTelemetryData .cxx_destruct]
+ -[ADJasperColorInFieldCalibrationTelemetryData firedEventTimestampsArray]
+ -[ADJasperColorInFieldCalibrationTelemetryData initEventTimestampsArray]
+ -[ADJasperColorInFieldCalibrationTelemetryData setFiredEventTimestampsArray:]
+ -[ADJasperColorInfieldCalibrationFlow .cxx_destruct]
+ -[ADJasperColorInfieldCalibrationFlow executor]
+ -[ADJasperColorInfieldCalibrationFlow handleMatch:]
+ -[ADJasperColorInfieldCalibrationFlow initWithExecutor:andIntersessionData:]
+ -[ADJasperColorInfieldCalibrationFlow lastExecutionResult]
+ -[ADJasperColorInfieldCalibrationFlow pushColor:pose:calibration:metadata:timestamp:]
+ -[ADJasperColorInfieldCalibrationFlow pushPointCloud:pose:calibration:timestamp:]
+ -[ADNetworkProvider initWithNetwork:requestedLayouts:espressoEngine:]
+ -[ADNetworkProvider supportedSizesForInput:expectedPixelFormat:]
+ -[ADNetworkProvider supportedSizesForOutput:expectedPixelFormat:]
+ -[ADPearlColorInFieldCalibrationResult initWithDictionary:]
+ -[ADPearlColorInFieldCalibrationTelemetryData .cxx_destruct]
+ -[ADPearlColorInFieldCalibrationTelemetryData firedEventTimestampsArray]
+ -[ADPearlColorInFieldCalibrationTelemetryData initEventTimestampsArray]
+ -[ADPearlColorInFieldCalibrationTelemetryData setFiredEventTimestampsArray:]
+ -[ADPearlColorInfieldCalibrationFlow .cxx_destruct]
+ -[ADPearlColorInfieldCalibrationFlow executor]
+ -[ADPearlColorInfieldCalibrationFlow handleMatch:]
+ -[ADPearlColorInfieldCalibrationFlow initWithExecutor:andIntersessionData:]
+ -[ADPearlColorInfieldCalibrationFlow lastExecutionResult]
+ -[ADPearlColorInfieldCalibrationFlow pushColor:pose:calibration:metadata:timestamp:]
+ -[ADPearlColorInfieldCalibrationFlow pushPearlDepth:pose:depthCalibration:irToDepthTransform:timestamp:]
+ GCC_except_table1000
+ GCC_except_table1001
+ GCC_except_table1002
+ GCC_except_table1008
+ GCC_except_table1016
+ GCC_except_table1017
+ GCC_except_table1030
+ GCC_except_table1032
+ GCC_except_table1041
+ GCC_except_table1042
+ GCC_except_table1045
+ GCC_except_table1056
+ GCC_except_table1057
+ GCC_except_table1058
+ GCC_except_table1062
+ GCC_except_table1063
+ GCC_except_table1065
+ GCC_except_table1066
+ GCC_except_table1067
+ GCC_except_table1068
+ GCC_except_table1069
+ GCC_except_table1070
+ GCC_except_table1071
+ GCC_except_table1073
+ GCC_except_table1083
+ GCC_except_table1098
+ GCC_except_table1103
+ GCC_except_table1107
+ GCC_except_table1108
+ GCC_except_table1109
+ GCC_except_table1110
+ GCC_except_table1111
+ GCC_except_table1112
+ GCC_except_table1113
+ GCC_except_table1118
+ GCC_except_table1134
+ GCC_except_table1135
+ GCC_except_table1138
+ GCC_except_table1140
+ GCC_except_table1143
+ GCC_except_table1144
+ GCC_except_table1146
+ GCC_except_table1168
+ GCC_except_table1169
+ GCC_except_table1177
+ GCC_except_table1178
+ GCC_except_table1243
+ GCC_except_table1244
+ GCC_except_table1263
+ GCC_except_table1278
+ GCC_except_table1291
+ GCC_except_table1293
+ GCC_except_table1294
+ GCC_except_table1295
+ GCC_except_table1299
+ GCC_except_table1303
+ GCC_except_table1328
+ GCC_except_table1330
+ GCC_except_table1332
+ GCC_except_table1333
+ GCC_except_table1334
+ GCC_except_table1335
+ GCC_except_table1336
+ GCC_except_table1338
+ GCC_except_table1342
+ GCC_except_table1343
+ GCC_except_table1345
+ GCC_except_table1346
+ GCC_except_table1347
+ GCC_except_table1348
+ GCC_except_table1350
+ GCC_except_table1351
+ GCC_except_table1352
+ GCC_except_table1353
+ GCC_except_table1355
+ GCC_except_table1365
+ GCC_except_table1366
+ GCC_except_table1382
+ GCC_except_table1387
+ GCC_except_table1388
+ GCC_except_table1389
+ GCC_except_table1390
+ GCC_except_table1394
+ GCC_except_table1398
+ GCC_except_table1400
+ GCC_except_table1401
+ GCC_except_table1410
+ GCC_except_table1436
+ GCC_except_table1438
+ GCC_except_table1439
+ GCC_except_table1440
+ GCC_except_table1443
+ GCC_except_table1452
+ GCC_except_table1453
+ GCC_except_table1476
+ GCC_except_table1494
+ GCC_except_table1495
+ GCC_except_table1496
+ GCC_except_table1497
+ GCC_except_table1498
+ GCC_except_table1500
+ GCC_except_table1501
+ GCC_except_table1502
+ GCC_except_table1507
+ GCC_except_table1508
+ GCC_except_table1509
+ GCC_except_table1510
+ GCC_except_table1512
+ GCC_except_table1513
+ GCC_except_table1516
+ GCC_except_table1517
+ GCC_except_table1519
+ GCC_except_table1520
+ GCC_except_table1541
+ GCC_except_table1549
+ GCC_except_table1553
+ GCC_except_table1554
+ GCC_except_table1555
+ GCC_except_table1564
+ GCC_except_table1577
+ GCC_except_table1578
+ GCC_except_table1583
+ GCC_except_table1584
+ GCC_except_table1585
+ GCC_except_table1587
+ GCC_except_table1588
+ GCC_except_table1590
+ GCC_except_table1620
+ GCC_except_table1623
+ GCC_except_table1624
+ GCC_except_table1625
+ GCC_except_table1626
+ GCC_except_table1636
+ GCC_except_table1639
+ GCC_except_table1642
+ GCC_except_table1645
+ GCC_except_table1648
+ GCC_except_table1654
+ GCC_except_table1655
+ GCC_except_table1656
+ GCC_except_table1670
+ GCC_except_table1674
+ GCC_except_table1676
+ GCC_except_table1677
+ GCC_except_table1685
+ GCC_except_table1686
+ GCC_except_table1687
+ GCC_except_table1689
+ GCC_except_table1690
+ GCC_except_table1691
+ GCC_except_table1692
+ GCC_except_table1706
+ GCC_except_table1707
+ GCC_except_table1709
+ GCC_except_table1721
+ GCC_except_table1725
+ GCC_except_table1727
+ GCC_except_table1735
+ GCC_except_table1740
+ GCC_except_table1745
+ GCC_except_table1750
+ GCC_except_table1751
+ GCC_except_table1763
+ GCC_except_table1768
+ GCC_except_table1769
+ GCC_except_table1770
+ GCC_except_table1773
+ GCC_except_table1774
+ GCC_except_table1776
+ GCC_except_table1791
+ GCC_except_table1798
+ GCC_except_table1799
+ GCC_except_table1814
+ GCC_except_table1828
+ GCC_except_table1829
+ GCC_except_table1832
+ GCC_except_table1833
+ GCC_except_table1835
+ GCC_except_table1838
+ GCC_except_table1839
+ GCC_except_table1847
+ GCC_except_table1856
+ GCC_except_table1864
+ GCC_except_table1865
+ GCC_except_table1866
+ GCC_except_table1868
+ GCC_except_table1873
+ GCC_except_table1877
+ GCC_except_table1880
+ GCC_except_table1883
+ GCC_except_table1892
+ GCC_except_table1898
+ GCC_except_table1899
+ GCC_except_table1902
+ GCC_except_table1904
+ GCC_except_table1910
+ GCC_except_table1911
+ GCC_except_table1915
+ GCC_except_table1916
+ GCC_except_table1917
+ GCC_except_table1926
+ GCC_except_table1927
+ GCC_except_table1928
+ GCC_except_table1941
+ GCC_except_table1944
+ GCC_except_table1953
+ GCC_except_table1956
+ GCC_except_table1965
+ GCC_except_table1966
+ GCC_except_table1983
+ GCC_except_table1984
+ GCC_except_table1989
+ GCC_except_table1990
+ GCC_except_table1991
+ GCC_except_table1993
+ GCC_except_table1994
+ GCC_except_table1997
+ GCC_except_table1998
+ GCC_except_table2000
+ GCC_except_table2009
+ GCC_except_table2010
+ GCC_except_table2011
+ GCC_except_table2012
+ GCC_except_table2025
+ GCC_except_table2033
+ GCC_except_table2034
+ GCC_except_table224
+ GCC_except_table225
+ GCC_except_table232
+ GCC_except_table255
+ GCC_except_table263
+ GCC_except_table266
+ GCC_except_table267
+ GCC_except_table278
+ GCC_except_table314
+ GCC_except_table319
+ GCC_except_table322
+ GCC_except_table330
+ GCC_except_table331
+ GCC_except_table343
+ GCC_except_table351
+ GCC_except_table354
+ GCC_except_table357
+ GCC_except_table358
+ GCC_except_table382
+ GCC_except_table387
+ GCC_except_table390
+ GCC_except_table394
+ GCC_except_table404
+ GCC_except_table405
+ GCC_except_table407
+ GCC_except_table408
+ GCC_except_table409
+ GCC_except_table420
+ GCC_except_table424
+ GCC_except_table426
+ GCC_except_table445
+ GCC_except_table449
+ GCC_except_table450
+ GCC_except_table451
+ GCC_except_table453
+ GCC_except_table454
+ GCC_except_table455
+ GCC_except_table463
+ GCC_except_table472
+ GCC_except_table473
+ GCC_except_table491
+ GCC_except_table493
+ GCC_except_table494
+ GCC_except_table496
+ GCC_except_table497
+ GCC_except_table498
+ GCC_except_table548
+ GCC_except_table549
+ GCC_except_table550
+ GCC_except_table561
+ GCC_except_table562
+ GCC_except_table563
+ GCC_except_table564
+ GCC_except_table567
+ GCC_except_table568
+ GCC_except_table583
+ GCC_except_table585
+ GCC_except_table586
+ GCC_except_table587
+ GCC_except_table588
+ GCC_except_table592
+ GCC_except_table593
+ GCC_except_table597
+ GCC_except_table607
+ GCC_except_table634
+ GCC_except_table646
+ GCC_except_table650
+ GCC_except_table653
+ GCC_except_table656
+ GCC_except_table665
+ GCC_except_table673
+ GCC_except_table682
+ GCC_except_table689
+ GCC_except_table694
+ GCC_except_table697
+ GCC_except_table701
+ GCC_except_table711
+ GCC_except_table720
+ GCC_except_table727
+ GCC_except_table731
+ GCC_except_table735
+ GCC_except_table749
+ GCC_except_table756
+ GCC_except_table766
+ GCC_except_table784
+ GCC_except_table786
+ GCC_except_table788
+ GCC_except_table800
+ GCC_except_table801
+ GCC_except_table806
+ GCC_except_table807
+ GCC_except_table809
+ GCC_except_table820
+ GCC_except_table821
+ GCC_except_table822
+ GCC_except_table823
+ GCC_except_table833
+ GCC_except_table834
+ GCC_except_table839
+ GCC_except_table844
+ GCC_except_table845
+ GCC_except_table852
+ GCC_except_table854
+ GCC_except_table855
+ GCC_except_table857
+ GCC_except_table867
+ GCC_except_table878
+ GCC_except_table901
+ GCC_except_table902
+ GCC_except_table908
+ GCC_except_table909
+ GCC_except_table970
+ GCC_except_table972
+ GCC_except_table973
+ GCC_except_table990
+ GCC_except_table999
+ _NSCalendarIdentifierGregorian
+ _OBJC_CLASS_$_ADJasperColorInfieldCalibrationFlow
+ _OBJC_CLASS_$_ADPearlColorInfieldCalibrationFlow
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_IVAR_$_ADDensifiedLiDARFocusAssistPipelineParameters._confidenceUnits
+ _OBJC_IVAR_$_ADFlowFrameInput._pearl
+ _OBJC_IVAR_$_ADFlowFrameInput._pointClouds
+ _OBJC_IVAR_$_ADFlowFrameInput._secondaryColor
+ _OBJC_IVAR_$_ADFlowFrameOutput._figuresOfMerit
+ _OBJC_IVAR_$_ADFlowFrameOutput._normals
+ _OBJC_IVAR_$_ADJasperColorInFieldCalibrationControllerParameters._thresholdAngularVelocity
+ _OBJC_IVAR_$_ADJasperColorInFieldCalibrationExecutor._forceAngularVelocityLogic
+ _OBJC_IVAR_$_ADJasperColorInFieldCalibrationTelemetryData._firedEventTimestampsArray
+ _OBJC_IVAR_$_ADJasperColorInfieldCalibrationFlow._executor
+ _OBJC_IVAR_$_ADJasperColorInfieldCalibrationFlow._intersessionData
+ _OBJC_IVAR_$_ADJasperColorInfieldCalibrationFlow._lastExecutionResult
+ _OBJC_IVAR_$_ADJasperColorInfieldCalibrationFlow._streamSync
+ _OBJC_IVAR_$_ADPearlColorInFieldCalibrationTelemetryData._firedEventTimestampsArray
+ _OBJC_IVAR_$_ADPearlColorInfieldCalibrationFlow._executor
+ _OBJC_IVAR_$_ADPearlColorInfieldCalibrationFlow._intersessionData
+ _OBJC_IVAR_$_ADPearlColorInfieldCalibrationFlow._lastExecutionResult
+ _OBJC_IVAR_$_ADPearlColorInfieldCalibrationFlow._streamSync
+ _OBJC_IVAR_$_ADPearlColorInfieldCalibrationFlow._transformKey
+ _OBJC_METACLASS_$_ADJasperColorInfieldCalibrationFlow
+ _OBJC_METACLASS_$_ADPearlColorInfieldCalibrationFlow
+ __OBJC_$_INSTANCE_METHODS_ADJasperColorInfieldCalibrationFlow
+ __OBJC_$_INSTANCE_METHODS_ADPearlColorInfieldCalibrationFlow
+ __OBJC_$_INSTANCE_VARIABLES_ADJasperColorInfieldCalibrationFlow
+ __OBJC_$_INSTANCE_VARIABLES_ADPearlColorInfieldCalibrationFlow
+ __OBJC_$_PROP_LIST_ADJasperColorInfieldCalibrationFlow
+ __OBJC_$_PROP_LIST_ADPearlColorInfieldCalibrationFlow
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ADFlowPearlConsumer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ADFlowPearlConsumer
+ __OBJC_$_PROTOCOL_REFS_ADFlowPearlConsumer
+ __OBJC_CLASS_PROTOCOLS_$_ADJasperColorInfieldCalibrationFlow
+ __OBJC_CLASS_PROTOCOLS_$_ADPearlColorInfieldCalibrationFlow
+ __OBJC_CLASS_RO_$_ADJasperColorInfieldCalibrationFlow
+ __OBJC_CLASS_RO_$_ADPearlColorInfieldCalibrationFlow
+ __OBJC_LABEL_PROTOCOL_$_ADFlowPearlConsumer
+ __OBJC_METACLASS_RO_$_ADJasperColorInfieldCalibrationFlow
+ __OBJC_METACLASS_RO_$_ADPearlColorInfieldCalibrationFlow
+ __OBJC_PROTOCOL_$_ADFlowPearlConsumer
+ __PromotedConst.5619
+ __PromotedConst.5620
+ __Z11getDateDiffP6NSDateS0_m
+ __Z13waitForFolderP8NSStringd
+ __Z15prepareAneFlagsP12NSDictionaryP8NSStringS2_b
+ __Z24getMaxOneShotEventsCountv
+ __Z29analyzeOneShotExtremeRotationfffP8NSStringP14NSMutableArray
+ __Z39fireOneShotLargeRotationEventIfDetectedPK8NSStringff12OneShotIndexPS_P14NSMutableArray
+ __ZL15INSTRUMENTS_ENDjyyyy.1103
+ __ZL15INSTRUMENTS_ENDjyyyy.1164
+ __ZL15INSTRUMENTS_ENDjyyyy.1199
+ __ZL15INSTRUMENTS_ENDjyyyy.1229
+ __ZL15INSTRUMENTS_ENDjyyyy.1235
+ __ZL15INSTRUMENTS_ENDjyyyy.125
+ __ZL15INSTRUMENTS_ENDjyyyy.1326
+ __ZL15INSTRUMENTS_ENDjyyyy.1458
+ __ZL15INSTRUMENTS_ENDjyyyy.1464
+ __ZL15INSTRUMENTS_ENDjyyyy.1524
+ __ZL15INSTRUMENTS_ENDjyyyy.1665
+ __ZL15INSTRUMENTS_ENDjyyyy.1906
+ __ZL15INSTRUMENTS_ENDjyyyy.197
+ __ZL15INSTRUMENTS_ENDjyyyy.203
+ __ZL15INSTRUMENTS_ENDjyyyy.2135
+ __ZL15INSTRUMENTS_ENDjyyyy.2284
+ __ZL15INSTRUMENTS_ENDjyyyy.2439
+ __ZL15INSTRUMENTS_ENDjyyyy.272
+ __ZL15INSTRUMENTS_ENDjyyyy.2874
+ __ZL15INSTRUMENTS_ENDjyyyy.2930
+ __ZL15INSTRUMENTS_ENDjyyyy.3134
+ __ZL15INSTRUMENTS_ENDjyyyy.3272
+ __ZL15INSTRUMENTS_ENDjyyyy.3323
+ __ZL15INSTRUMENTS_ENDjyyyy.3485
+ __ZL15INSTRUMENTS_ENDjyyyy.3582
+ __ZL15INSTRUMENTS_ENDjyyyy.3749
+ __ZL15INSTRUMENTS_ENDjyyyy.3855
+ __ZL15INSTRUMENTS_ENDjyyyy.3878
+ __ZL15INSTRUMENTS_ENDjyyyy.391
+ __ZL15INSTRUMENTS_ENDjyyyy.4083
+ __ZL15INSTRUMENTS_ENDjyyyy.4131
+ __ZL15INSTRUMENTS_ENDjyyyy.4264
+ __ZL15INSTRUMENTS_ENDjyyyy.4440
+ __ZL15INSTRUMENTS_ENDjyyyy.4591
+ __ZL15INSTRUMENTS_ENDjyyyy.4706
+ __ZL15INSTRUMENTS_ENDjyyyy.472
+ __ZL15INSTRUMENTS_ENDjyyyy.4909
+ __ZL15INSTRUMENTS_ENDjyyyy.5381
+ __ZL15INSTRUMENTS_ENDjyyyy.543
+ __ZL15INSTRUMENTS_ENDjyyyy.5440
+ __ZL15INSTRUMENTS_ENDjyyyy.55
+ __ZL15INSTRUMENTS_ENDjyyyy.5603
+ __ZL15INSTRUMENTS_ENDjyyyy.643
+ __ZL15INSTRUMENTS_ENDjyyyy.675
+ __ZL15INSTRUMENTS_ENDjyyyy.813
+ __ZL15INSTRUMENTS_ENDjyyyy.960
+ __ZL17INSTRUMENTS_EVENTjyyyy.1104
+ __ZL17INSTRUMENTS_EVENTjyyyy.1165
+ __ZL17INSTRUMENTS_EVENTjyyyy.1200
+ __ZL17INSTRUMENTS_EVENTjyyyy.1230
+ __ZL17INSTRUMENTS_EVENTjyyyy.1236
+ __ZL17INSTRUMENTS_EVENTjyyyy.126
+ __ZL17INSTRUMENTS_EVENTjyyyy.1327
+ __ZL17INSTRUMENTS_EVENTjyyyy.1459
+ __ZL17INSTRUMENTS_EVENTjyyyy.1465
+ __ZL17INSTRUMENTS_EVENTjyyyy.1525
+ __ZL17INSTRUMENTS_EVENTjyyyy.1666
+ __ZL17INSTRUMENTS_EVENTjyyyy.1907
+ __ZL17INSTRUMENTS_EVENTjyyyy.198
+ __ZL17INSTRUMENTS_EVENTjyyyy.204
+ __ZL17INSTRUMENTS_EVENTjyyyy.2136
+ __ZL17INSTRUMENTS_EVENTjyyyy.2285
+ __ZL17INSTRUMENTS_EVENTjyyyy.2440
+ __ZL17INSTRUMENTS_EVENTjyyyy.273
+ __ZL17INSTRUMENTS_EVENTjyyyy.2875
+ __ZL17INSTRUMENTS_EVENTjyyyy.2931
+ __ZL17INSTRUMENTS_EVENTjyyyy.3135
+ __ZL17INSTRUMENTS_EVENTjyyyy.3273
+ __ZL17INSTRUMENTS_EVENTjyyyy.3324
+ __ZL17INSTRUMENTS_EVENTjyyyy.3486
+ __ZL17INSTRUMENTS_EVENTjyyyy.3583
+ __ZL17INSTRUMENTS_EVENTjyyyy.3750
+ __ZL17INSTRUMENTS_EVENTjyyyy.3856
+ __ZL17INSTRUMENTS_EVENTjyyyy.3879
+ __ZL17INSTRUMENTS_EVENTjyyyy.392
+ __ZL17INSTRUMENTS_EVENTjyyyy.4084
+ __ZL17INSTRUMENTS_EVENTjyyyy.4132
+ __ZL17INSTRUMENTS_EVENTjyyyy.4265
+ __ZL17INSTRUMENTS_EVENTjyyyy.4441
+ __ZL17INSTRUMENTS_EVENTjyyyy.4592
+ __ZL17INSTRUMENTS_EVENTjyyyy.4707
+ __ZL17INSTRUMENTS_EVENTjyyyy.473
+ __ZL17INSTRUMENTS_EVENTjyyyy.4910
+ __ZL17INSTRUMENTS_EVENTjyyyy.5382
+ __ZL17INSTRUMENTS_EVENTjyyyy.544
+ __ZL17INSTRUMENTS_EVENTjyyyy.5441
+ __ZL17INSTRUMENTS_EVENTjyyyy.56
+ __ZL17INSTRUMENTS_EVENTjyyyy.5604
+ __ZL17INSTRUMENTS_EVENTjyyyy.644
+ __ZL17INSTRUMENTS_EVENTjyyyy.676
+ __ZL17INSTRUMENTS_EVENTjyyyy.814
+ __ZL17INSTRUMENTS_EVENTjyyyy.961
+ __ZL17INSTRUMENTS_STARTjyyyy.1105
+ __ZL17INSTRUMENTS_STARTjyyyy.1166
+ __ZL17INSTRUMENTS_STARTjyyyy.1201
+ __ZL17INSTRUMENTS_STARTjyyyy.1231
+ __ZL17INSTRUMENTS_STARTjyyyy.1237
+ __ZL17INSTRUMENTS_STARTjyyyy.127
+ __ZL17INSTRUMENTS_STARTjyyyy.1328
+ __ZL17INSTRUMENTS_STARTjyyyy.1460
+ __ZL17INSTRUMENTS_STARTjyyyy.1466
+ __ZL17INSTRUMENTS_STARTjyyyy.1526
+ __ZL17INSTRUMENTS_STARTjyyyy.1667
+ __ZL17INSTRUMENTS_STARTjyyyy.1908
+ __ZL17INSTRUMENTS_STARTjyyyy.199
+ __ZL17INSTRUMENTS_STARTjyyyy.205
+ __ZL17INSTRUMENTS_STARTjyyyy.2137
+ __ZL17INSTRUMENTS_STARTjyyyy.2286
+ __ZL17INSTRUMENTS_STARTjyyyy.2441
+ __ZL17INSTRUMENTS_STARTjyyyy.274
+ __ZL17INSTRUMENTS_STARTjyyyy.2876
+ __ZL17INSTRUMENTS_STARTjyyyy.2932
+ __ZL17INSTRUMENTS_STARTjyyyy.3136
+ __ZL17INSTRUMENTS_STARTjyyyy.3274
+ __ZL17INSTRUMENTS_STARTjyyyy.3325
+ __ZL17INSTRUMENTS_STARTjyyyy.3487
+ __ZL17INSTRUMENTS_STARTjyyyy.3584
+ __ZL17INSTRUMENTS_STARTjyyyy.3751
+ __ZL17INSTRUMENTS_STARTjyyyy.3857
+ __ZL17INSTRUMENTS_STARTjyyyy.3880
+ __ZL17INSTRUMENTS_STARTjyyyy.393
+ __ZL17INSTRUMENTS_STARTjyyyy.4085
+ __ZL17INSTRUMENTS_STARTjyyyy.4133
+ __ZL17INSTRUMENTS_STARTjyyyy.4266
+ __ZL17INSTRUMENTS_STARTjyyyy.4442
+ __ZL17INSTRUMENTS_STARTjyyyy.4593
+ __ZL17INSTRUMENTS_STARTjyyyy.4708
+ __ZL17INSTRUMENTS_STARTjyyyy.474
+ __ZL17INSTRUMENTS_STARTjyyyy.4911
+ __ZL17INSTRUMENTS_STARTjyyyy.5383
+ __ZL17INSTRUMENTS_STARTjyyyy.5442
+ __ZL17INSTRUMENTS_STARTjyyyy.545
+ __ZL17INSTRUMENTS_STARTjyyyy.5605
+ __ZL17INSTRUMENTS_STARTjyyyy.57
+ __ZL17INSTRUMENTS_STARTjyyyy.645
+ __ZL17INSTRUMENTS_STARTjyyyy.677
+ __ZL17INSTRUMENTS_STARTjyyyy.815
+ __ZL17INSTRUMENTS_STARTjyyyy.962
+ __ZL27g_streamTrainedCroppRectPad
+ __ZN13ADCommonUtils17calcRotationAngleER13simd_float3x3
+ __ZN13ADCommonUtils17calcRotationAngleER14simd_double3x3
+ __ZN13ADCommonUtils18extrinsicsToStringE13simd_float4x4
+ __ZN13ADCommonUtils21calculatePoseDistanceE13simd_float4x4S0_
+ __ZN13ADCommonUtils27matrixNxMToArrayColumnFirstILm4ELm3E13simd_float4x3EEP7NSArrayRKT1_
+ __ZN13ADCommonUtils27matrixNxMToArrayColumnFirstILm4ELm4E13simd_float4x4EEP7NSArrayRKT1_
+ __ZN13ADCommonUtils29matrixNxMFromArrayColumnFirstILm3ELm4E13simd_float4x3EET1_P7NSArray
+ __ZN13ADCommonUtils29matrixNxMFromArrayColumnFirstILm4ELm4E13simd_float4x4EET1_P7NSArray
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorI31ADDisparityToDepthFitWorldPointNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorI7CGPointNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIDv3_fNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1ELm2ELm3ELm4ELm5EEEEJbffNS_6vectorIfNS_9allocatorIfEEEES6_NS3_I31ADDisparityToDepthFitWorldPointNS4_IS7_EEEEEEC2B8ue170006IJLm0ELm1ELm2ELm3ELm4ELm5EEJbffS6_S6_S9_EJEJEJbiiRS6_SC_RKS9_EEENS1_IJXspT_EEEENS_13__tuple_typesIJDpT0_EEENS1_IJXspT1_EEEENSG_IJDpT2_EEEDpOT3_
+ __ZNSt3__113__nth_elementB8ue170006INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPfEEEEvT1_S8_S8_T0_
+ __ZNSt3__113unordered_setIiNS_4hashIiEENS_8equal_toIiEENS_9allocatorIiEEED1B8ue170006Ev
+ __ZNSt3__119piecewise_constructE
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__125__throw_bad_function_callB8ue170006Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ue170006IPfS5_EEvT_T0_l
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ____Z18bundleE5mlIfNeededP8NSStringS0_S0_b_block_invoke
+ ____Z39fireOneShotLargeRotationEventIfDetectedPK8NSStringff12OneShotIndexPS_P14NSMutableArray_block_invoke
+ ___block_descriptor_64_ea8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.4976
+ __unnamed_array_storage.2057
+ __unnamed_array_storage.209
+ __unnamed_array_storage.2829
+ __unnamed_array_storage.483
+ __unnamed_array_storage.5591
+ __unnamed_array_storage.58
+ __unnamed_array_storage.64
+ _defaultSPGConfig.5610
+ _kADDeviceConfigurationKeyJasperColorInFieldAngularVelocityThreshold
+ _kADDeviceConfigurationKeyJasperColorInFieldForceAngularVelocityLogic
+ _objc_getProperty
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$aggregatePointClouds:calibrations:worldToPlatformTransforms:projectingToCamera:worldToPlatformAtProjectionTime:
+ _objc_msgSend$allValues
+ _objc_msgSend$code
+ _objc_msgSend$components:fromDate:toDate:options:
+ _objc_msgSend$date
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$day
+ _objc_msgSend$distantPast
+ _objc_msgSend$executableURL
+ _objc_msgSend$executeWithColor:colorCameraCalibration:colorWorldToPlatformTransform:pointClouds:lidarCameraCalibration:pointCloudWorldToPlatformTransforms:outDepthMap:outConfMap:outNormalsMap:
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$firedEventTimestampsArray
+ _objc_msgSend$getAlternativePathForNetwork:
+ _objc_msgSend$getAngularVelocityFromMetadataDictionary:deviceClock:
+ _objc_msgSend$getConfigFolderForNetwork:
+ _objc_msgSend$getDefaultPathForNetwork:allowPrecompiledModel:
+ _objc_msgSend$getDeviceFrequency
+ _objc_msgSend$handleMatch:
+ _objc_msgSend$initEventTimestampsArray
+ _objc_msgSend$initWithCalendarIdentifier:
+ _objc_msgSend$initWithNetwork:requestedLayouts:espressoEngine:
+ _objc_msgSend$isAngularVelocityValid:
+ _objc_msgSend$launchAndReturnError:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$metadata
+ _objc_msgSend$moveItemAtPath:toPath:error:
+ _objc_msgSend$path
+ _objc_msgSend$pipeline
+ _objc_msgSend$pointCloudByMergingPointClouds:
+ _objc_msgSend$preprocessInputColorFrame:colorPose:jasperPointClouds:jasperPoses:jasperCameraCalibration:colorCameraCalibration:timestamp:colorMetadata:
+ _objc_msgSend$providerForNetwork:requestedLayouts:
+ _objc_msgSend$providerForNetwork:requestedLayouts:espressoEngine:
+ _objc_msgSend$pushData:streamIndex:timestamp:pose:calibration:meta:
+ _objc_msgSend$readDataToEndOfFileAndReturnError:
+ _objc_msgSend$setExecutableURL:
+ _objc_msgSend$setFiguresOfMerit:
+ _objc_msgSend$setPearl:
+ _objc_msgSend$setPointClouds:
+ _objc_msgSend$sleepForTimeInterval:
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$supportedSizesForInput:expectedPixelFormat:
+ _objc_msgSend$supportedSizesForOutput:expectedPixelFormat:
+ _objc_msgSend$supportedSizesForSizesDict:key:expectedPixelFormat:
+ _objc_msgSend$thresholdAngularVelocity
+ _objc_msgSend$updateSizeForItem:fromShape:forLayout:target:
+ _objc_opt_respondsToSelector
+ _objc_retain_x28
+ _objc_setProperty_atomic
+ _rmdir
- +[ADNetworkProvider getAlternativePathForNetwork:andPriority:]
- +[ADNetworkProvider getConfigFolderForNetwork:andPriority:]
- +[ADNetworkProvider getDefaultPathForNetwork:andPriority:allowPrecompiledModel:]
- +[ADNetworkProvider getEspressoFileNameForNetwork:andPriority:]
- +[ADNetworkProvider providerForNetwork:prioritization:]
- +[ADNetworkProvider providerForNetwork:prioritization:requestedLayouts:]
- +[ADNetworkProvider providerForNetwork:prioritization:requestedLayouts:espressoEngine:]
- +[ADNetworkProvider updateSizeForItem:fromShape:dtype:forLayout:target:]
- -[ADFlowFrameInput pointCloud]
- -[ADFlowFrameInput setPointCloud:]
- -[ADJasperColorFlow pushColor:pose:calibration:timestamp:]
- -[ADJasperColorInFieldCalibrationExecutor executeWithInterSessionData:outResult:]
- -[ADJasperColorInFieldCalibrationExecutor executeWithInterSessionData:result:]
- -[ADJasperColorInFieldCalibrationExecutor preprocessInputColorFrameImpl:colorPose:jasperPointClouds:jasperPoses:jasperCameraCalibration:colorCameraCalibration:timestamp:colorMetadata:]
- -[ADJasperColorInFieldCalibrationExecutor preprocessPushedInputs]
- -[ADJasperColorInFieldCalibrationExecutor pushColorImage:timestamp:metadata:pose:]
- -[ADJasperColorInFieldCalibrationExecutor pushColorImage:timestamp:pose:]
- -[ADJasperColorInFieldCalibrationExecutor pushJasperPointCloud:timestamp:metadata:pose:]
- -[ADJasperColorInFieldCalibrationExecutor pushJasperPointCloud:timestamp:pose:]
- -[ADJasperColorInFieldCalibrationExecutor updatePcAggregator]
- -[ADJasperColorInFieldCalibrationTelemetryData largeRotationStatusBits]
- -[ADJasperColorInFieldCalibrationTelemetryData updateLargeRotationStatusBits:]
- -[ADNetworkProvider initWithNetwork:prioritization:requestedLayouts:allowPrecompiledModel:]
- -[ADNetworkProvider rawConfidenceUnits]
- -[ADNetworkProvider setRawConfidenceUnits:]
- -[ADNetworkProvider sizeFor:isInput:requestedLayout:]
- -[ADNetworkProvider sizeForInput:]
- -[ADNetworkProvider sizeForInput:withLayout:]
- -[ADNetworkProvider sizeForOutput:]
- -[ADNetworkProvider sizeForOutput:withLayout:]
- -[ADNetworkProvider supportedSizesForInput:]
- -[ADNetworkProvider supportedSizesForOutput:]
- -[ADPearlColorInFieldCalibrationExecutor executeWithInterSessionData:outResult:]
- -[ADPearlColorInFieldCalibrationExecutor executeWithInterSessionData:result:]
- -[ADPearlColorInFieldCalibrationExecutor preprocessPushedInputs]
- -[ADPearlColorInFieldCalibrationExecutor pushColorImage:timestamp:metadata:pose:]
- -[ADPearlColorInFieldCalibrationExecutor pushColorImage:timestamp:pose:]
- -[ADPearlColorInFieldCalibrationExecutor pushPearlDepth:timestamp:metadata:pose:]
- -[ADPearlColorInFieldCalibrationExecutor pushPearlDepth:timestamp:pose:]
- -[ADPearlColorInFieldCalibrationTelemetryData updateLargeRotationStatusBits:]
- GCC_except_table1009
- GCC_except_table1011
- GCC_except_table1013
- GCC_except_table1018
- GCC_except_table1019
- GCC_except_table1020
- GCC_except_table1022
- GCC_except_table1025
- GCC_except_table1026
- GCC_except_table1027
- GCC_except_table1029
- GCC_except_table1035
- GCC_except_table1036
- GCC_except_table1043
- GCC_except_table1049
- GCC_except_table1050
- GCC_except_table1051
- GCC_except_table1052
- GCC_except_table1064
- GCC_except_table1079
- GCC_except_table1084
- GCC_except_table1088
- GCC_except_table1089
- GCC_except_table1090
- GCC_except_table1091
- GCC_except_table1092
- GCC_except_table1094
- GCC_except_table1099
- GCC_except_table1100
- GCC_except_table1115
- GCC_except_table1116
- GCC_except_table1121
- GCC_except_table1124
- GCC_except_table1125
- GCC_except_table1127
- GCC_except_table1129
- GCC_except_table1147
- GCC_except_table1157
- GCC_except_table1222
- GCC_except_table1239
- GCC_except_table1245
- GCC_except_table1254
- GCC_except_table1267
- GCC_except_table1268
- GCC_except_table1270
- GCC_except_table1271
- GCC_except_table1273
- GCC_except_table1275
- GCC_except_table1279
- GCC_except_table1302
- GCC_except_table1304
- GCC_except_table1306
- GCC_except_table1308
- GCC_except_table1309
- GCC_except_table1310
- GCC_except_table1311
- GCC_except_table1312
- GCC_except_table1314
- GCC_except_table1318
- GCC_except_table1320
- GCC_except_table1322
- GCC_except_table1324
- GCC_except_table1325
- GCC_except_table1327
- GCC_except_table1329
- GCC_except_table1339
- GCC_except_table1356
- GCC_except_table1361
- GCC_except_table1362
- GCC_except_table1363
- GCC_except_table1367
- GCC_except_table1371
- GCC_except_table1373
- GCC_except_table1374
- GCC_except_table1383
- GCC_except_table1409
- GCC_except_table1411
- GCC_except_table1412
- GCC_except_table1413
- GCC_except_table1416
- GCC_except_table1425
- GCC_except_table1426
- GCC_except_table1446
- GCC_except_table1448
- GCC_except_table1449
- GCC_except_table1458
- GCC_except_table1466
- GCC_except_table1467
- GCC_except_table1468
- GCC_except_table1469
- GCC_except_table1470
- GCC_except_table1471
- GCC_except_table1474
- GCC_except_table1480
- GCC_except_table1481
- GCC_except_table1482
- GCC_except_table1483
- GCC_except_table1486
- GCC_except_table1487
- GCC_except_table1489
- GCC_except_table1490
- GCC_except_table1492
- GCC_except_table1522
- GCC_except_table1526
- GCC_except_table1527
- GCC_except_table1528
- GCC_except_table1529
- GCC_except_table1530
- GCC_except_table1531
- GCC_except_table1533
- GCC_except_table1534
- GCC_except_table1537
- GCC_except_table1542
- GCC_except_table1543
- GCC_except_table1544
- GCC_except_table1550
- GCC_except_table1551
- GCC_except_table1563
- GCC_except_table1568
- GCC_except_table1592
- GCC_except_table1593
- GCC_except_table1594
- GCC_except_table1599
- GCC_except_table1600
- GCC_except_table1602
- GCC_except_table1609
- GCC_except_table1610
- GCC_except_table1611
- GCC_except_table1612
- GCC_except_table1613
- GCC_except_table1614
- GCC_except_table1615
- GCC_except_table1616
- GCC_except_table1617
- GCC_except_table1618
- GCC_except_table1628
- GCC_except_table1633
- GCC_except_table1634
- GCC_except_table1635
- GCC_except_table1647
- GCC_except_table1650
- GCC_except_table1652
- GCC_except_table1658
- GCC_except_table1659
- GCC_except_table1663
- GCC_except_table1666
- GCC_except_table1669
- GCC_except_table1680
- GCC_except_table1681
- GCC_except_table1682
- GCC_except_table1713
- GCC_except_table1714
- GCC_except_table1716
- GCC_except_table1718
- GCC_except_table1724
- GCC_except_table1736
- GCC_except_table1746
- GCC_except_table1764
- GCC_except_table1771
- GCC_except_table1772
- GCC_except_table1786
- GCC_except_table1787
- GCC_except_table1788
- GCC_except_table1800
- GCC_except_table1801
- GCC_except_table1802
- GCC_except_table1803
- GCC_except_table1804
- GCC_except_table1805
- GCC_except_table1807
- GCC_except_table1809
- GCC_except_table1812
- GCC_except_table1816
- GCC_except_table1818
- GCC_except_table1819
- GCC_except_table1820
- GCC_except_table1841
- GCC_except_table1842
- GCC_except_table1843
- GCC_except_table1844
- GCC_except_table1845
- GCC_except_table1846
- GCC_except_table1848
- GCC_except_table1850
- GCC_except_table1853
- GCC_except_table1857
- GCC_except_table1858
- GCC_except_table1859
- GCC_except_table1871
- GCC_except_table1872
- GCC_except_table1884
- GCC_except_table1886
- GCC_except_table1893
- GCC_except_table1895
- GCC_except_table1896
- GCC_except_table1897
- GCC_except_table1907
- GCC_except_table1908
- GCC_except_table1924
- GCC_except_table1925
- GCC_except_table1936
- GCC_except_table1946
- GCC_except_table1950
- GCC_except_table1963
- GCC_except_table1964
- GCC_except_table1969
- GCC_except_table1971
- GCC_except_table1973
- GCC_except_table1974
- GCC_except_table1977
- GCC_except_table1978
- GCC_except_table1980
- GCC_except_table1995
- GCC_except_table2003
- GCC_except_table2004
- GCC_except_table221
- GCC_except_table226
- GCC_except_table253
- GCC_except_table261
- GCC_except_table264
- GCC_except_table265
- GCC_except_table276
- GCC_except_table312
- GCC_except_table313
- GCC_except_table320
- GCC_except_table327
- GCC_except_table328
- GCC_except_table341
- GCC_except_table346
- GCC_except_table347
- GCC_except_table353
- GCC_except_table356
- GCC_except_table380
- GCC_except_table384
- GCC_except_table385
- GCC_except_table392
- GCC_except_table410
- GCC_except_table412
- GCC_except_table423
- GCC_except_table429
- GCC_except_table433
- GCC_except_table434
- GCC_except_table435
- GCC_except_table437
- GCC_except_table438
- GCC_except_table447
- GCC_except_table456
- GCC_except_table457
- GCC_except_table469
- GCC_except_table470
- GCC_except_table471
- GCC_except_table474
- GCC_except_table475
- GCC_except_table476
- GCC_except_table478
- GCC_except_table481
- GCC_except_table482
- GCC_except_table486
- GCC_except_table489
- GCC_except_table540
- GCC_except_table541
- GCC_except_table542
- GCC_except_table544
- GCC_except_table553
- GCC_except_table554
- GCC_except_table555
- GCC_except_table556
- GCC_except_table559
- GCC_except_table571
- GCC_except_table572
- GCC_except_table576
- GCC_except_table579
- GCC_except_table580
- GCC_except_table581
- GCC_except_table591
- GCC_except_table595
- GCC_except_table596
- GCC_except_table600
- GCC_except_table632
- GCC_except_table644
- GCC_except_table649
- GCC_except_table651
- GCC_except_table654
- GCC_except_table663
- GCC_except_table671
- GCC_except_table681
- GCC_except_table686
- GCC_except_table691
- GCC_except_table695
- GCC_except_table699
- GCC_except_table709
- GCC_except_table719
- GCC_except_table726
- GCC_except_table730
- GCC_except_table733
- GCC_except_table748
- GCC_except_table750
- GCC_except_table757
- GCC_except_table780
- GCC_except_table781
- GCC_except_table785
- GCC_except_table795
- GCC_except_table797
- GCC_except_table803
- GCC_except_table805
- GCC_except_table816
- GCC_except_table817
- GCC_except_table818
- GCC_except_table819
- GCC_except_table824
- GCC_except_table826
- GCC_except_table827
- GCC_except_table829
- GCC_except_table841
- GCC_except_table847
- GCC_except_table848
- GCC_except_table850
- GCC_except_table853
- GCC_except_table861
- GCC_except_table866
- GCC_except_table885
- GCC_except_table886
- GCC_except_table893
- GCC_except_table954
- GCC_except_table959
- GCC_except_table964
- GCC_except_table979
- GCC_except_table980
- GCC_except_table981
- GCC_except_table982
- GCC_except_table985
- GCC_except_table989
- _OBJC_CLASS_$_NSConstantFloatNumber
- _OBJC_IVAR_$_ADFlowFrameInput._pointCloud
- _OBJC_IVAR_$_ADJasperColorFlow._pointCloudAggregator
- _OBJC_IVAR_$_ADJasperColorInFieldCalibrationExecutor._lastSyncMatch
- _OBJC_IVAR_$_ADJasperColorInFieldCalibrationExecutor._pcAggregator
- _OBJC_IVAR_$_ADJasperColorInFieldCalibrationExecutor._streamSync
- _OBJC_IVAR_$_ADJasperColorInFieldCalibrationTelemetryData._largeRotationStatusBits
- _OBJC_IVAR_$_ADNetworkProvider._rawConfidenceUnits
- _OBJC_IVAR_$_ADPearlColorInFieldCalibrationExecutor._lastSyncMatch
- _OBJC_IVAR_$_ADPearlColorInFieldCalibrationExecutor._streamSync
- __PromotedConst.5332
- __Z13ADMLModelPathP8NSStringb
- __Z15prepareAneFlagsP12NSDictionaryP8NSStringS2_
- __Z29analyzeOneShotExtremeRotationjfffP8NSStringPj
- __Z39fireOneShotLargeRotationEventIfDetectedPK8NSStringff14OneShotBitMaskjPS_Pj
- __ZL15INSTRUMENTS_ENDjyyyy.1024
- __ZL15INSTRUMENTS_ENDjyyyy.1085
- __ZL15INSTRUMENTS_ENDjyyyy.1120
- __ZL15INSTRUMENTS_ENDjyyyy.1150
- __ZL15INSTRUMENTS_ENDjyyyy.1156
- __ZL15INSTRUMENTS_ENDjyyyy.1240
- __ZL15INSTRUMENTS_ENDjyyyy.127
- __ZL15INSTRUMENTS_ENDjyyyy.1368
- __ZL15INSTRUMENTS_ENDjyyyy.1374
- __ZL15INSTRUMENTS_ENDjyyyy.1424
- __ZL15INSTRUMENTS_ENDjyyyy.1561
- __ZL15INSTRUMENTS_ENDjyyyy.1817
- __ZL15INSTRUMENTS_ENDjyyyy.188
- __ZL15INSTRUMENTS_ENDjyyyy.194
- __ZL15INSTRUMENTS_ENDjyyyy.1995
- __ZL15INSTRUMENTS_ENDjyyyy.2118
- __ZL15INSTRUMENTS_ENDjyyyy.2276
- __ZL15INSTRUMENTS_ENDjyyyy.265
- __ZL15INSTRUMENTS_ENDjyyyy.2715
- __ZL15INSTRUMENTS_ENDjyyyy.2771
- __ZL15INSTRUMENTS_ENDjyyyy.2962
- __ZL15INSTRUMENTS_ENDjyyyy.3093
- __ZL15INSTRUMENTS_ENDjyyyy.3145
- __ZL15INSTRUMENTS_ENDjyyyy.3307
- __ZL15INSTRUMENTS_ENDjyyyy.3405
- __ZL15INSTRUMENTS_ENDjyyyy.3566
- __ZL15INSTRUMENTS_ENDjyyyy.3673
- __ZL15INSTRUMENTS_ENDjyyyy.3696
- __ZL15INSTRUMENTS_ENDjyyyy.374
- __ZL15INSTRUMENTS_ENDjyyyy.3901
- __ZL15INSTRUMENTS_ENDjyyyy.3986
- __ZL15INSTRUMENTS_ENDjyyyy.4077
- __ZL15INSTRUMENTS_ENDjyyyy.4260
- __ZL15INSTRUMENTS_ENDjyyyy.4410
- __ZL15INSTRUMENTS_ENDjyyyy.444
- __ZL15INSTRUMENTS_ENDjyyyy.4523
- __ZL15INSTRUMENTS_ENDjyyyy.4738
- __ZL15INSTRUMENTS_ENDjyyyy.5214
- __ZL15INSTRUMENTS_ENDjyyyy.530
- __ZL15INSTRUMENTS_ENDjyyyy.5316
- __ZL15INSTRUMENTS_ENDjyyyy.54
- __ZL15INSTRUMENTS_ENDjyyyy.560
- __ZL15INSTRUMENTS_ENDjyyyy.709
- __ZL15INSTRUMENTS_ENDjyyyy.865
- __ZL17INSTRUMENTS_EVENTjyyyy.1025
- __ZL17INSTRUMENTS_EVENTjyyyy.1086
- __ZL17INSTRUMENTS_EVENTjyyyy.1121
- __ZL17INSTRUMENTS_EVENTjyyyy.1151
- __ZL17INSTRUMENTS_EVENTjyyyy.1157
- __ZL17INSTRUMENTS_EVENTjyyyy.1241
- __ZL17INSTRUMENTS_EVENTjyyyy.128
- __ZL17INSTRUMENTS_EVENTjyyyy.1369
- __ZL17INSTRUMENTS_EVENTjyyyy.1375
- __ZL17INSTRUMENTS_EVENTjyyyy.1425
- __ZL17INSTRUMENTS_EVENTjyyyy.1562
- __ZL17INSTRUMENTS_EVENTjyyyy.1818
- __ZL17INSTRUMENTS_EVENTjyyyy.189
- __ZL17INSTRUMENTS_EVENTjyyyy.195
- __ZL17INSTRUMENTS_EVENTjyyyy.1996
- __ZL17INSTRUMENTS_EVENTjyyyy.2119
- __ZL17INSTRUMENTS_EVENTjyyyy.2277
- __ZL17INSTRUMENTS_EVENTjyyyy.266
- __ZL17INSTRUMENTS_EVENTjyyyy.2716
- __ZL17INSTRUMENTS_EVENTjyyyy.2772
- __ZL17INSTRUMENTS_EVENTjyyyy.2963
- __ZL17INSTRUMENTS_EVENTjyyyy.3094
- __ZL17INSTRUMENTS_EVENTjyyyy.3146
- __ZL17INSTRUMENTS_EVENTjyyyy.3308
- __ZL17INSTRUMENTS_EVENTjyyyy.3406
- __ZL17INSTRUMENTS_EVENTjyyyy.3567
- __ZL17INSTRUMENTS_EVENTjyyyy.3674
- __ZL17INSTRUMENTS_EVENTjyyyy.3697
- __ZL17INSTRUMENTS_EVENTjyyyy.375
- __ZL17INSTRUMENTS_EVENTjyyyy.3902
- __ZL17INSTRUMENTS_EVENTjyyyy.3987
- __ZL17INSTRUMENTS_EVENTjyyyy.4078
- __ZL17INSTRUMENTS_EVENTjyyyy.4261
- __ZL17INSTRUMENTS_EVENTjyyyy.4411
- __ZL17INSTRUMENTS_EVENTjyyyy.445
- __ZL17INSTRUMENTS_EVENTjyyyy.4524
- __ZL17INSTRUMENTS_EVENTjyyyy.4739
- __ZL17INSTRUMENTS_EVENTjyyyy.5215
- __ZL17INSTRUMENTS_EVENTjyyyy.531
- __ZL17INSTRUMENTS_EVENTjyyyy.5317
- __ZL17INSTRUMENTS_EVENTjyyyy.55
- __ZL17INSTRUMENTS_EVENTjyyyy.561
- __ZL17INSTRUMENTS_EVENTjyyyy.710
- __ZL17INSTRUMENTS_EVENTjyyyy.866
- __ZL17INSTRUMENTS_STARTjyyyy.1026
- __ZL17INSTRUMENTS_STARTjyyyy.1087
- __ZL17INSTRUMENTS_STARTjyyyy.1122
- __ZL17INSTRUMENTS_STARTjyyyy.1152
- __ZL17INSTRUMENTS_STARTjyyyy.1158
- __ZL17INSTRUMENTS_STARTjyyyy.1242
- __ZL17INSTRUMENTS_STARTjyyyy.129
- __ZL17INSTRUMENTS_STARTjyyyy.1370
- __ZL17INSTRUMENTS_STARTjyyyy.1376
- __ZL17INSTRUMENTS_STARTjyyyy.1426
- __ZL17INSTRUMENTS_STARTjyyyy.1563
- __ZL17INSTRUMENTS_STARTjyyyy.1819
- __ZL17INSTRUMENTS_STARTjyyyy.190
- __ZL17INSTRUMENTS_STARTjyyyy.196
- __ZL17INSTRUMENTS_STARTjyyyy.1997
- __ZL17INSTRUMENTS_STARTjyyyy.2120
- __ZL17INSTRUMENTS_STARTjyyyy.2278
- __ZL17INSTRUMENTS_STARTjyyyy.267
- __ZL17INSTRUMENTS_STARTjyyyy.2717
- __ZL17INSTRUMENTS_STARTjyyyy.2773
- __ZL17INSTRUMENTS_STARTjyyyy.2964
- __ZL17INSTRUMENTS_STARTjyyyy.3095
- __ZL17INSTRUMENTS_STARTjyyyy.3147
- __ZL17INSTRUMENTS_STARTjyyyy.3309
- __ZL17INSTRUMENTS_STARTjyyyy.3407
- __ZL17INSTRUMENTS_STARTjyyyy.3568
- __ZL17INSTRUMENTS_STARTjyyyy.3675
- __ZL17INSTRUMENTS_STARTjyyyy.3698
- __ZL17INSTRUMENTS_STARTjyyyy.376
- __ZL17INSTRUMENTS_STARTjyyyy.3903
- __ZL17INSTRUMENTS_STARTjyyyy.3988
- __ZL17INSTRUMENTS_STARTjyyyy.4079
- __ZL17INSTRUMENTS_STARTjyyyy.4262
- __ZL17INSTRUMENTS_STARTjyyyy.4412
- __ZL17INSTRUMENTS_STARTjyyyy.446
- __ZL17INSTRUMENTS_STARTjyyyy.4525
- __ZL17INSTRUMENTS_STARTjyyyy.4740
- __ZL17INSTRUMENTS_STARTjyyyy.5216
- __ZL17INSTRUMENTS_STARTjyyyy.5318
- __ZL17INSTRUMENTS_STARTjyyyy.532
- __ZL17INSTRUMENTS_STARTjyyyy.56
- __ZL17INSTRUMENTS_STARTjyyyy.562
- __ZL17INSTRUMENTS_STARTjyyyy.711
- __ZL17INSTRUMENTS_STARTjyyyy.867
- __ZN13ADCommonUtils26calculateTransformDistanceE13simd_float4x3S0_
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorI31ADDisparityToDepthFitWorldPointNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorI7CGPointNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIDv3_fNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1ELm2ELm3ELm4ELm5EEEEJbffNS_6vectorIfNS_9allocatorIfEEEES6_NS3_I31ADDisparityToDepthFitWorldPointNS4_IS7_EEEEEEC2B7v160006IJLm0ELm1ELm2ELm3ELm4ELm5EEJbffS6_S6_S9_EJEJEJbiiRS6_SC_RKS9_EEENS1_IJXspT_EEEENS_13__tuple_typesIJDpT0_EEENS1_IJXspT1_EEEENSG_IJDpT2_EEEDpOT3_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- __ZNSt3__113__nth_elementB7v160006INS_17_ClassicAlgPolicyERNS_6__lessIffEENS_11__wrap_iterIPfEEEEvT1_S8_S8_T0_
- __ZNSt3__113unordered_setIiNS_4hashIiEENS_8equal_toIiEENS_9allocatorIiEEED1B7v160006Ev
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__125__throw_bad_function_callB7v160006Ev
- __ZNSt3__16vectorIfNS_9allocatorIfEEE6assignIPfLi0EEEvT_S6_
- __ZNSt3__1L19piecewise_constructE
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ____Z39fireOneShotLargeRotationEventIfDetectedPK8NSStringff14OneShotBitMaskjPS_Pj_block_invoke
- ___block_literal_global.4792
- __unnamed_array_storage.1938
- __unnamed_array_storage.204
- __unnamed_array_storage.2656
- __unnamed_array_storage.467
- _defaultSPGConfig.5323
- _kADNetworkIDCinVidPearl
- _kADNetworkIDCinVidStereoTeleWide
- _kADNetworkIDCinVidStereoWideSuperwide
- _kADNetworkIDD3P
- _kADNetworkIDDARP
- _kADNetworkIDDensifiedLiDARFocusAssist
- _kADNetworkIDJasperColor
- _kADNetworkIDJasperColorInFieldCalibrationBackend_iOS
- _kADNetworkIDJasperColorInFieldCalibrationFrontend_iOS
- _kADNetworkIDJasperColorV2
- _kADNetworkIDMonocular
- _kADNetworkIDMonocularV2
- _kADNetworkIDMonocularV2Legacy2021
- _kADNetworkIDMonocularV3
- _kADNetworkIDNMPPeridot
- _kADNetworkIDPearlColorInFieldCalibrationBackend_iOS
- _kADNetworkIDPearlColorInFieldCalibrationFrontend_iOS
- _kADNetworkIDSIJNetBackend
- _kADNetworkIDSIJNetFrontend
- _kADNetworkIDSIPNetBackend
- _kADNetworkIDSIPNetFrontend
- _kADNetworkIDStereoFSD
- _kADNetworkIDStereoFSD60Deg
- _kADNetworkIDStereoFSDV3
- _kADNetworkIDStereoFSDV3_45Deg
- _kADNetworkIDStereoFSDV3_60Deg
- _kADNetworkIDStereoV2RTFSD_0Deg
- _kADNetworkIDStereoV2RTFSD_45Deg
- _kADNetworkIDStillImage
- _objc_msgSend$aggregateForTime:worldToCameraTransform:
- _objc_msgSend$bundleWithIdentifier:
- _objc_msgSend$clear
- _objc_msgSend$colorCameraCalibration
- _objc_msgSend$executeWithColor:pointCloud:outDepthMap:outConfMap:worldToCameraTransform:cameraCalibration:
- _objc_msgSend$executeWithInterSessionData:outResult:
- _objc_msgSend$getAlternativePathForNetwork:andPriority:
- _objc_msgSend$getConfigFolderForNetwork:andPriority:
- _objc_msgSend$getDefaultPathForNetwork:andPriority:allowPrecompiledModel:
- _objc_msgSend$getEspressoFileNameForNetwork:andPriority:
- _objc_msgSend$initWithAggregationParameters:
- _objc_msgSend$initWithAggregationParameters:jasperToColorTransform:colorCamera:
- _objc_msgSend$initWithNetwork:prioritization:requestedLayouts:allowPrecompiledModel:
- _objc_msgSend$largeRotationStatusBits
- _objc_msgSend$launch
- _objc_msgSend$launchPath
- _objc_msgSend$pointCloud
- _objc_msgSend$preprocessInputColorFrameImpl:colorPose:jasperPointClouds:jasperPoses:jasperCameraCalibration:colorCameraCalibration:timestamp:colorMetadata:
- _objc_msgSend$preprocessPushedInputs
- _objc_msgSend$providerForNetwork:prioritization:
- _objc_msgSend$providerForNetwork:prioritization:requestedLayouts:
- _objc_msgSend$providerForNetwork:prioritization:requestedLayouts:espressoEngine:
- _objc_msgSend$pushColorImage:timestamp:metadata:pose:
- _objc_msgSend$pushData:streamIndex:timestamp:pose:
- _objc_msgSend$pushJasperPointCloud:timestamp:metadata:pose:
- _objc_msgSend$pushPearlDepth:timestamp:metadata:pose:
- _objc_msgSend$pushPointCloud:timestamp:worldToCameraTransform:
- _objc_msgSend$pushPointCloud:timestamp:worldToLidarTransform:
- _objc_msgSend$rawConfidenceUnits
- _objc_msgSend$readDataToEndOfFile
- _objc_msgSend$setJasperToCameraTransform:
- _objc_msgSend$setLaunchPath:
- _objc_msgSend$setPointCloud:
- _objc_msgSend$setPointCloudFilterParameters:
- _objc_msgSend$sizeFor:isInput:requestedLayout:
- _objc_msgSend$supportedSizesForInput:
- _objc_msgSend$supportedSizesForOutput:
- _objc_msgSend$updateLargeRotationStatusBits:
- _objc_msgSend$updatePcAggregator
- _objc_msgSend$updateSizeForItem:fromShape:dtype:forLayout:target:
CStrings:
+ "\b"
+ "\x136b\x84"
+ "\x14(\xf0\x14"
+ ".N301"
+ "115.0"
+ "@\"ADJasperColorInFieldCalibrationExecutor\""
+ "@\"ADJasperColorInFieldCalibrationInterSessionData\""
+ "@\"ADJasperColorInFieldCalibrationResult\""
+ "@\"ADPearlColorInFieldCalibrationExecutor\""
+ "@\"ADPearlColorInFieldCalibrationInterSessionData\""
+ "@\"ADPearlColorInFieldCalibrationResult\""
+ "@28@0:8@16I24"
+ "@36@0:8@16@24I32"
+ "@40@0:8@16@24Q32"
+ "ADFlowPearlConsumer"
+ "ADJasperColorInFieldCalibration preprocessInputColorFrameImpl fail for to high angular velocity"
+ "ADJasperColorInfieldCalibrationFlow"
+ "ADJasperColorPipeline only supports speed prioritization"
+ "ADPearlColorInfieldCalibrationFlow"
+ "ARCylon"
+ "CVM"
+ "CVM4"
+ "DAPIBalanced"
+ "DAPIQuality"
+ "DSD"
+ "FSDNetV3_0deg"
+ "FSDNetV3_45deg"
+ "FSDNetV3_60deg"
+ "FSDNet_0deg"
+ "FSDNet_60deg"
+ "High Angular velocity of %f detected against threshold of %f"
+ "J7"
+ "NMP"
+ "PeCoNetBackend"
+ "PeCoNetFrontend"
+ "R:[%.4f, %.4f, %.4f, %.4f],[%.4f, %.4f, %.4f, %.4f],[%.4f, %.4f, %.4f, %.4f]. T:[%.4f, %.4f, %.4f, %.4f]\n"
+ "R:[%.4f, %.4f, %.4f],[%.4f, %.4f, %.4f],[%.4f, %.4f, %.4f]. T:[%.4f, %.4f, %.4f]\n"
+ "RGBPNetSMPBackend"
+ "RGBPNetSMPFrontend"
+ "RTFSD_0deg"
+ "RTFSD_45deg"
+ "SIJNetBackend"
+ "SIJNetFrontend"
+ "SelfieNet"
+ "SelfieNetQuality"
+ "T@\"ADJasperColorInFieldCalibrationExecutor\",R,&,N,V_executor"
+ "T@\"ADJasperColorInFieldCalibrationResult\",R,&,N,V_lastExecutionResult"
+ "T@\"ADPearlColorInFieldCalibrationExecutor\",R,&,N,V_executor"
+ "T@\"ADPearlColorInFieldCalibrationResult\",R,&,N,V_lastExecutionResult"
+ "T@\"NSArray\",R,&,N,V_pointClouds"
+ "T@\"NSDictionary\",R,N,V_figuresOfMerit"
+ "T@\"NSMutableArray\",&,V_firedEventTimestampsArray"
+ "T@\"NSString\",?,R,C"
+ "T^{__CVBuffer=},R,N,V_normals"
+ "T^{__CVBuffer=},R,N,V_pearl"
+ "T^{__CVBuffer=},R,N,V_secondaryColor"
+ "Tf,N,V_thresholdAngularVelocity"
+ "UUID"
+ "UUIDString"
+ "Unknown device frequency (%@). Will use 24MHz..."
+ "_figuresOfMerit"
+ "_firedEventTimestampsArray"
+ "_forceAngularVelocityLogic"
+ "_intersessionData"
+ "_lastExecutionResult"
+ "_normals"
+ "_pearl"
+ "_pointClouds"
+ "_secondaryColor"
+ "_thresholdAngularVelocity"
+ "_transformKey"
+ "aggregatePointClouds:calibrations:worldToPlatformTransforms:projectingToCamera:worldToPlatformAtProjectionTime:"
+ "aggregatedPointCloud"
+ "allValues"
+ "cannot aggregate and project point clouds without color calibration and world transform data"
+ "cannot execute on multiple point clouds without aggregation information"
+ "code"
+ "components:fromDate:toDate:options:"
+ "could not find json file for requested model %{public}@"
+ "could not find network files for requested model:%{public}@"
+ "creating network provider for %@. precompiled model allowed: %d"
+ "date"
+ "dateWithTimeIntervalSince1970:"
+ "day"
+ "did not find network for pipeline ADJasperColorV2Pipeline prioritization %@"
+ "distantPast"
+ "executableURL"
+ "executeWithColor:colorCameraCalibration:colorWorldToPlatformTransform:pointClouds:lidarCameraCalibration:pointCloudWorldToPlatformTransforms:outDepthMap:outConfMap:outNormalsMap:"
+ "failed execute preprocessed stage"
+ "failed preprocessing input stage"
+ "failed to create folder structure needed for compilation. Error: %@"
+ "figuresOfMerit"
+ "fileSystemRepresentation"
+ "fireOneShotLargeRotationEventIfDetected: fail to understand history when tried to fire one shot large tolerance"
+ "fireOneShotLargeRotationEventIfDetected: rotation diff %s > %f compare to factory event failed to be seant"
+ "fireOneShotLargeRotationEventIfDetected: rotation diff %s compare to factory %f > %f fired"
+ "fireOneShotLargeRotationEventIfDetected: this event of large tolerance for %@ is not the first and it wa last sean at %@"
+ "fireOneShotLargeRotationEventIfDetected: time since last large rotation event is >= then 2 monthes, last event time %@, current event time %@"
+ "firedEventTimestampsArray"
+ "found network path: %@"
+ "getAlternativePathForNetwork:"
+ "getAngularVelocityFromMetadataDictionary:deviceClock:"
+ "getConfigFolderForNetwork:"
+ "getDefaultPathForNetwork:allowPrecompiledModel:"
+ "getDeviceFrequency"
+ "handleMatch:"
+ "initEventTimestampsArray"
+ "initWithCalendarIdentifier:"
+ "initWithDictionary:"
+ "initWithExecutor:andIntersessionData:"
+ "initWithNetwork:requestedLayouts:espressoEngine:"
+ "inputColorCalibration"
+ "inputColorMetadata"
+ "inputColorPose"
+ "inputIntersessionData"
+ "inputIrToDepthTransform"
+ "inputPearl"
+ "inputPearlCalibration"
+ "inputPointCloudCalibration"
+ "inputPointCloudPose"
+ "isAngularVelocityValid:"
+ "jasperColorInFieldAngularVelocityThreshold"
+ "jasperColorInFieldForceAngularVelocityLogic"
+ "lastExecutionResult"
+ "launchAndReturnError:"
+ "localizedDescription"
+ "metadata"
+ "model already compiled or being compiled, no need to recompile"
+ "model folder found"
+ "moveItemAtPath:toPath:error:"
+ "no monocular models for prioritization %@"
+ "normals"
+ "path"
+ "pearl"
+ "platform is %@ but compiling to generic platform instead"
+ "pointCloudByMergingPointClouds:"
+ "pointClouds"
+ "preprocessInputColorFrame:colorPose:jasperPointClouds:jasperPoses:jasperCameraCalibration:colorCameraCalibration:timestamp:colorMetadata:"
+ "providerForNetwork:requestedLayouts:"
+ "providerForNetwork:requestedLayouts:espressoEngine:"
+ "pushColor:pose:calibration:metadata:timestamp:"
+ "pushData:streamIndex:timestamp:pose:calibration:meta:"
+ "pushPearlDepth:pose:depthCalibration:irToDepthTransform:timestamp:"
+ "q144@0:8^{__CVBuffer=}16@24{?=[4]}32@96@104^{?=[4]}112^^{__CVBuffer}120^^{__CVBuffer}128^^{__CVBuffer}136"
+ "readDataToEndOfFileAndReturnError:"
+ "secondaryColor"
+ "setExecutableURL:"
+ "setFiguresOfMerit:"
+ "setFiredEventTimestampsArray:"
+ "setNormals:"
+ "setPearl:"
+ "setPointClouds:"
+ "setSecondaryColor:"
+ "setThresholdAngularVelocity:"
+ "sleepForTimeInterval:"
+ "stringWithCString:encoding:"
+ "supportedSizesForInput:expectedPixelFormat:"
+ "supportedSizesForOutput:expectedPixelFormat:"
+ "supportedSizesForSizesDict:key:expectedPixelFormat:"
+ "thresholdAngularVelocity"
+ "timed out waiting for model folder. Consider removing folder %@ and try again."
+ "unable to initialize network provider: nil network name"
+ "unable to support confidence threshold for non aleatoric uncertainty models"
+ "updateSizeForItem:fromShape:forLayout:target:"
+ "v112@0:8^{__CVBuffer=}16{?=[4]}24@\"ADCameraCalibration\"88@\"NSDictionary\"96d104"
+ "v112@0:8^{__CVBuffer=}16{?=[4]}24@88@96d104"
+ "v168@0:8^{__CVBuffer=}16{?=[4]}24@\"ADCameraCalibration\"88{?=[4]}96d160"
+ "v168@0:8^{__CVBuffer=}16{?=[4]}24@88{?=[4]}96d160"
+ "v48@0:8@16@24Q32@40"
+ "waiting for model folder to appear (timeout: %.0f seconds)"
+ "\x91"
- "\a\x11"
- "\x13\x11&c\x84"
- "\x16(q\x84"
- "%@__%@"
- "109.3"
- "@\"ADPointCloudAggregator\""
- "@\"ADStreamSyncMatch\""
- "@32@0:8@16q24"
- "@36@0:8@16q24B32"
- "@40@0:8@16q24@32"
- "@44@0:8@16q24@32B40"
- "@48@0:8@16q24@32Q40"
- "ADJasperColorInFieldCalibration jasper sync not ready"
- "ADJasperColorInFieldCalibration jasper sync pass"
- "ADNetworkIDCinVidStereoTeleWide"
- "ADNetworkIDCinVidStereoWideSuperwide"
- "ADNetworkIDDensifiedLiDARFocusAssist"
- "ADPearlColorInFieldCalibration pearl sync fail"
- "ADPearlColorInFieldCalibration pearl sync pass"
- "AppleDepth"
- "Balanced"
- "FSDNetStill0deg"
- "FSDNetStill60deg"
- "FSDNetV3Still0deg"
- "FSDNetV3Still45deg"
- "FSDNetV3Still60deg"
- "FSDNetVideo60deg"
- "JasperColorInFieldCalibrationBackend_iOS"
- "JasperColorInFieldCalibrationFrontend_iOS"
- "JasperColorSpeed"
- "JasperColorV2Balanced"
- "JasperColorV2Quality"
- "MCAM-J calibration creation failed"
- "MCAM-P calibration creation failed"
- "MaxTDLatencyMicroSec"
- "MonocularBalanced"
- "MonocularQuality"
- "MonocularSpeed"
- "MonocularV2"
- "MonocularV2Legacy2021"
- "MonocularV3"
- "NetworkIDCinVidPearl"
- "NetworkIDD3P"
- "NetworkIDDARP"
- "NetworkIDJasperColor"
- "NetworkIDJasperColorInFieldCalibrationBackend_iOS"
- "NetworkIDJasperColorInFieldCalibrationFrontend_iOS"
- "NetworkIDJasperColorV2"
- "NetworkIDMonocular"
- "NetworkIDMonocularV2"
- "NetworkIDMonocularV2Legacy2021"
- "NetworkIDMonocularV3"
- "NetworkIDNMPPeridot"
- "NetworkIDPearlColorInFieldCalibrationBackend_iOS"
- "NetworkIDPearlColorInFieldCalibrationFrontend_iOS"
- "NetworkIDSIJNetBackend"
- "NetworkIDSIJNetFrontend"
- "NetworkIDSIPNetBackend"
- "NetworkIDSIPNetFrontend"
- "NetworkIDStereoFSD"
- "NetworkIDStereoFSD60deg"
- "NetworkIDStereoFSDV3"
- "NetworkIDStereoFSDV3_45deg"
- "NetworkIDStereoFSDV3_60deg"
- "NetworkIDStereoV2RTFSD_0Deg"
- "NetworkIDStereoV2RTFSD_45Deg"
- "NetworkIDStillImage"
- "PearlColorInFieldCalibrationBackend_iOS"
- "PearlColorInFieldCalibrationFrontend_iOS"
- "Quality"
- "R:[%.3f, %.3f, %.3f],[%.3f, %.3f, %.3f],[%.3f, %.3f, %.3f]. T:[%.3f, %.3f, %.3f]\n"
- "RTFSD0deg"
- "RTFSD45deg"
- "SIJNetBackendQuality"
- "SIJNetFrontendQuality"
- "Speed"
- "StillImageQuality"
- "T@\"ADJasperPointCloud\",R,&,N,V_pointCloud"
- "TQ,V_rawConfidenceUnits"
- "_lastSyncMatch"
- "_pcAggregator"
- "_pointCloud"
- "_pointCloudAggregator"
- "_rawConfidenceUnits"
- "aggregateForTime:worldToCameraTransform:"
- "bundleWithIdentifier:"
- "clear"
- "colorInputMetaData"
- "could not find json file. requested ID:%{public}@ prioritization:%{public}@"
- "could not find network files. requested ID:%{public}@ prioritization:%{public}@"
- "creating network provider for id:%@ prioritization:%@"
- "empty sync match when preprocess pushed inputs"
- "executeWithInterSessionData:outResult:"
- "executeWithInterSessionData:result:"
- "failed aggregating point cloud"
- "failed to push point cloud into aggregator"
- "getAlternativePathForNetwork:andPriority:"
- "getConfigFolderForNetwork:andPriority:"
- "getDefaultPathForNetwork:andPriority:allowPrecompiledModel:"
- "getEspressoFileNameForNetwork:andPriority:"
- "initWithAggregationParameters:"
- "initWithAggregationParameters:jasperToColorTransform:colorCamera:"
- "initWithNetwork:prioritization:requestedLayouts:allowPrecompiledModel:"
- "input"
- "inputJasper"
- "inputJasper_%d"
- "intersessionData"
- "launch"
- "launchPath"
- "model already compiled, no need to recompile"
- "network confidence units:%ld"
- "network does not provide confidence threshold values"
- "no supported size found for %{public}@ %{public}@"
- "pearlColorInFieldCalibrationInputPearl"
- "pointCloud"
- "preprocessInputColorFrameImpl:colorPose:jasperPointClouds:jasperPoses:jasperCameraCalibration:colorCameraCalibration:timestamp:colorMetadata:"
- "preprocessPushedInputs"
- "providerForNetwork:prioritization:"
- "providerForNetwork:prioritization:requestedLayouts:"
- "providerForNetwork:prioritization:requestedLayouts:espressoEngine:"
- "pushColor:pose:calibration:timestamp:"
- "pushColorImage:timestamp:metadata:pose:"
- "pushColorImage:timestamp:pose:"
- "pushData:streamIndex:timestamp:pose:"
- "pushJasperPointCloud:timestamp:metadata:pose:"
- "pushJasperPointCloud:timestamp:pose:"
- "pushPearlDepth:timestamp:metadata:pose:"
- "pushPearlDepth:timestamp:pose:"
- "pushPointCloud:timestamp:worldToCameraTransform:"
- "pushPointCloud:timestamp:worldToLidarTransform:"
- "pushed color frame for ts:%f into streamSync"
- "pushed jasper point cloud for ts:%f into streamSync"
- "pushed pearl depth for ts:%f into streamSync"
- "q104@0:8@16d24@32{?=[4]}40"
- "q104@0:8^{__CVBuffer=}16d24@32{?=[4]}40"
- "q96@0:8@16d24{?=[4]}32"
- "q96@0:8^{__CVBuffer=}16d24{?=[4]}32"
- "raw network name: %@"
- "rawConfidenceUnits"
- "readDataToEndOfFile"
- "rotation diff %s > %f compare to factory event failed to be seant"
- "rotation diff %s compare to factory %f > %f fired"
- "setJasperToCameraTransform:"
- "setLaunchPath:"
- "setPointCloud:"
- "setRawConfidenceUnits:"
- "sizeFor:isInput:requestedLayout:"
- "sizeForInput:"
- "sizeForInput:withLayout:"
- "sizeForOutput:"
- "sizeForOutput:withLayout:"
- "supportedSizesForInput:"
- "supportedSizesForOutput:"
- "updateLargeRotationStatusBits:"
- "updatePcAggregator"
- "updateSizeForItem:fromShape:dtype:forLayout:target:"
- "v104@0:8^{__CVBuffer=}16{?=[4]}24@\"ADCameraCalibration\"88d96"
- "v104@0:8^{__CVBuffer=}16{?=[4]}24@88d96"
- "v56@0:8@16@24@32Q40@48"
- "{CGSize=dd}24@0:8@16"
- "{CGSize=dd}32@0:8@16Q24"
- "{CGSize=dd}36@0:8@16B24Q28"

```
