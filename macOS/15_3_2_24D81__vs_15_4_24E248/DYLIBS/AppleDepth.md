## AppleDepth

> `/System/Library/PrivateFrameworks/AppleDepth.framework/Versions/A/AppleDepth`

```diff

-132.0.0.0.0
-  __TEXT.__text: 0xad164
-  __TEXT.__auth_stubs: 0x11a0
-  __TEXT.__objc_methlist: 0x46cc
-  __TEXT.__const: 0x11c0
-  __TEXT.__gcc_except_tab: 0xb3e8
-  __TEXT.__oslogstring: 0x54a0
-  __TEXT.__cstring: 0x45f3
-  __TEXT.__unwind_info: 0x2590
-  __TEXT.__eh_frame: 0x98
-  __TEXT.__objc_classname: 0x10e65
-  __TEXT.__objc_methname: 0xdc48
-  __TEXT.__objc_methtype: 0x4680
-  __TEXT.__objc_stubs: 0x7040
-  __DATA_CONST.__got: 0x628
-  __DATA_CONST.__const: 0x188
-  __DATA_CONST.__objc_classlist: 0x398
+137.3.0.0.0
+  __TEXT.__text: 0xab9a4
+  __TEXT.__auth_stubs: 0x1170
+  __TEXT.__objc_methlist: 0x4784
+  __TEXT.__const: 0x1160
+  __TEXT.__gcc_except_tab: 0xb844
+  __TEXT.__oslogstring: 0x52ed
+  __TEXT.__cstring: 0x4531
+  __TEXT.__unwind_info: 0x25d0
+  __TEXT.__objc_classname: 0x8efe
+  __TEXT.__objc_methname: 0xde9e
+  __TEXT.__objc_methtype: 0x4185
+  __TEXT.__objc_stubs: 0x70e0
+  __DATA_CONST.__got: 0x640
+  __DATA_CONST.__const: 0x1a8
+  __DATA_CONST.__objc_classlist: 0x3b0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23e8
-  __DATA_CONST.__objc_superrefs: 0x310
-  __DATA_CONST.__objc_arraydata: 0x160
-  __AUTH_CONST.__auth_got: 0x8e0
-  __AUTH_CONST.__const: 0x550
-  __AUTH_CONST.__cfstring: 0x46c0
-  __AUTH_CONST.__objc_const: 0xc318
-  __AUTH_CONST.__objc_intobj: 0x1f8
-  __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x23f0
-  __DATA.__objc_ivar: 0xbd4
-  __DATA.__data: 0xe83e8
-  __DATA.__bss: 0x1b1
+  __DATA_CONST.__objc_selrefs: 0x24a8
+  __DATA_CONST.__objc_superrefs: 0x320
+  __DATA_CONST.__objc_arraydata: 0x150
+  __AUTH_CONST.__auth_got: 0x8c8
+  __AUTH_CONST.__const: 0x578
+  __AUTH_CONST.__cfstring: 0x4620
+  __AUTH_CONST.__objc_const: 0xbff0
+  __AUTH_CONST.__objc_intobj: 0x1b0
+  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH.__objc_data: 0x24e0
+  __DATA.__objc_ivar: 0xb70
+  __DATA.__data: 0xe83c8
+  __DATA.__bss: 0x1a1
   - /AppleInternal/Library/Frameworks/VisualLogger.framework/Versions/A/VisualLogger
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: FD826944-1842-35C7-B189-2F18DCFD2082
-  Functions: 1907
-  Symbols:   5670
-  CStrings:  4300
+  UUID: 34D6DA21-40F3-3326-BBFF-DD51B7900409
+  Functions: 1883
+  Symbols:   5665
+  CStrings:  4287
 
Symbols:
+ +[ADDeviceConfiguration registerVerbosityConfigurationUpdate]
+ +[ADFlowFrameOutputPool poolWithDepthDescriptor:confidenceDescriptor:]
+ +[ADFlowFrameOutputPool poolWithDepthDescriptor:confidenceDescriptor:confidenceLevelsDescriptor:normalsDescriptor:uncertaintyDescriptor:depthMaskDescriptor:layout:]
+ +[ADFlowFrameOutputPool poolWithDepthDescriptor:confidenceDescriptor:layout:]
+ +[ADFlowFrameOutputPool poolWithDepthDimensions:depthFormat:confidenceDimensions:confidenceFormat:confidenceLevelsDimensions:confidenceLevelsFormat:normalsDimensions:normalsFormat:uncertaintyDimensions:uncertaintyFormat:depthMaskDimensions:depthMaskFormat:]
+ +[ADNetworkProvider updateSizeForItem:fromShape:customStrides:forLayout:target:]
+ +[ADPearlColorInFieldCalibrationPipeline isPearlMaskExpectedFor:]
+ +[ADPearlColorInFieldCalibrationPipeline isZUsedFor:]
+ -[ADAdaptiveCorrectionPipeline dealloc]
+ -[ADEspressoJasperColorInFieldCalibrationFrontendInferenceDescriptor initWithNetworkProvider:espressoEngine:]
+ -[ADExecutor allocateIOBufferForEspressoDescriptor:]
+ -[ADExecutor deallocInferenceBuffers]
+ -[ADExecutor doesSupportBufferCopyPolicy:]
+ -[ADExecutor executorParameters]
+ -[ADExecutor inferencePixelBufferForDescriptor:inputUserBuffer:]
+ -[ADExecutor inferencePixelBufferForDescriptor:outputUserBuffer:]
+ -[ADExecutor layout]
+ -[ADExecutor preAllocateInferencePixelBufferForDescriptor:]
+ -[ADExecutor setExecutorParameters:]
+ -[ADExecutor setInferencePixelBuffer:forEspressoDescriptor:]
+ -[ADExecutorParameters bufferCopyPolicy]
+ -[ADExecutorParameters setBufferCopyPolicy:]
+ -[ADFlow maximalFrameRate]
+ -[ADFlow setMaximalFrameRate:]
+ -[ADFlow shouldProcessMatch:]
+ -[ADFlowFrameOutputPool bufferFromPool:]
+ -[ADFlowFrameOutputPool dealloc]
+ -[ADFlowFrameOutputPool frameOutput]
+ -[ADFlowFrameOutputPool initWithDepthDimensions:depthFormat:confidenceDimensions:confidenceFormat:confidenceLevelsDimensions:confidenceLevelsFormat:normalsDimensions:normalsFormat:uncertaintyDimensions:uncertaintyFormat:depthMaskDimensions:depthMaskFormat:]
+ -[ADJasperColorExecutor pipeline]
+ -[ADJasperColorInFieldCalibrationPipeline isJasperFrameValid:]
+ -[ADJasperColorInFieldCalibrationPipeline preProcessJasper:referenceCameraCalibration:jasperCameraCalibration:reprojectedPointsBuffer:]
+ -[ADLogManager processConfigurationChange:]
+ -[ADMonocularV2Flow .cxx_destruct]
+ -[ADMonocularV2Flow executor]
+ -[ADMonocularV2Flow initWithExecutor:]
+ -[ADMonocularV2Flow processColor:timestamp:]
+ -[ADMonocularV2Flow pushColor:pose:calibration:metadata:timestamp:]
+ -[ADMonocularV2Flow pushColor:timestamp:]
+ -[ADNetworkProviderLayoutShape .cxx_destruct]
+ -[ADNetworkProviderLayoutShape customStrides]
+ -[ADNetworkProviderLayoutShape layout]
+ -[ADNetworkProviderLayoutShape setCustomStrides:]
+ -[ADNetworkProviderLayoutShape setLayout:]
+ -[ADNetworkProviderLayoutShape setShape:]
+ -[ADNetworkProviderLayoutShape shape]
+ -[ADPearlColorInFieldCalibrationPipeline isPearlFrameValid:]
+ -[ADPearlColorInFieldCalibrationPipeline preProcessPearl:referenceCameraCalibration:pearlCameraCalibration:reprojectedPointsBuffer:reprojectedPointsMaskBuffer:]
+ -[ADPearlColorInFieldCalibrationPipelineParameters getDefaultsForFlow:]
+ -[ADPearlColorInFieldCalibrationPipelineParameters getMaxStdForValidResultForFlow:]
+ GCC_except_table1002
+ GCC_except_table1006
+ GCC_except_table1016
+ GCC_except_table1019
+ GCC_except_table1022
+ GCC_except_table1023
+ GCC_except_table1025
+ GCC_except_table1031
+ GCC_except_table1032
+ GCC_except_table1033
+ GCC_except_table1034
+ GCC_except_table1036
+ GCC_except_table1046
+ GCC_except_table1055
+ GCC_except_table1067
+ GCC_except_table1068
+ GCC_except_table1074
+ GCC_except_table1076
+ GCC_except_table1079
+ GCC_except_table1091
+ GCC_except_table1101
+ GCC_except_table1106
+ GCC_except_table1111
+ GCC_except_table1115
+ GCC_except_table1116
+ GCC_except_table1117
+ GCC_except_table1119
+ GCC_except_table1120
+ GCC_except_table1121
+ GCC_except_table1144
+ GCC_except_table1145
+ GCC_except_table1151
+ GCC_except_table1152
+ GCC_except_table1154
+ GCC_except_table1160
+ GCC_except_table1164
+ GCC_except_table1166
+ GCC_except_table1168
+ GCC_except_table1188
+ GCC_except_table1189
+ GCC_except_table1197
+ GCC_except_table1198
+ GCC_except_table1263
+ GCC_except_table1264
+ GCC_except_table1281
+ GCC_except_table1286
+ GCC_except_table1295
+ GCC_except_table1311
+ GCC_except_table1331
+ GCC_except_table1336
+ GCC_except_table1341
+ GCC_except_table1342
+ GCC_except_table1343
+ GCC_except_table1348
+ GCC_except_table1350
+ GCC_except_table1356
+ GCC_except_table1358
+ GCC_except_table1360
+ GCC_except_table1363
+ GCC_except_table1377
+ GCC_except_table1378
+ GCC_except_table1394
+ GCC_except_table1397
+ GCC_except_table1398
+ GCC_except_table1399
+ GCC_except_table1400
+ GCC_except_table1405
+ GCC_except_table1411
+ GCC_except_table1412
+ GCC_except_table1418
+ GCC_except_table1421
+ GCC_except_table1427
+ GCC_except_table1431
+ GCC_except_table1432
+ GCC_except_table1438
+ GCC_except_table1441
+ GCC_except_table1448
+ GCC_except_table1451
+ GCC_except_table1452
+ GCC_except_table1472
+ GCC_except_table1475
+ GCC_except_table1484
+ GCC_except_table1490
+ GCC_except_table1491
+ GCC_except_table1492
+ GCC_except_table1493
+ GCC_except_table1504
+ GCC_except_table1505
+ GCC_except_table1506
+ GCC_except_table1507
+ GCC_except_table1512
+ GCC_except_table1515
+ GCC_except_table1538
+ GCC_except_table1546
+ GCC_except_table1551
+ GCC_except_table1552
+ GCC_except_table1553
+ GCC_except_table1566
+ GCC_except_table1567
+ GCC_except_table1568
+ GCC_except_table1574
+ GCC_except_table1575
+ GCC_except_table1580
+ GCC_except_table1582
+ GCC_except_table1583
+ GCC_except_table1590
+ GCC_except_table1592
+ GCC_except_table1593
+ GCC_except_table1614
+ GCC_except_table1615
+ GCC_except_table1616
+ GCC_except_table1617
+ GCC_except_table1618
+ GCC_except_table1619
+ GCC_except_table1631
+ GCC_except_table1632
+ GCC_except_table1633
+ GCC_except_table1634
+ GCC_except_table1635
+ GCC_except_table1636
+ GCC_except_table1651
+ GCC_except_table1659
+ GCC_except_table1660
+ GCC_except_table1681
+ GCC_except_table1682
+ GCC_except_table1683
+ GCC_except_table1684
+ GCC_except_table1685
+ GCC_except_table1693
+ GCC_except_table1702
+ GCC_except_table1703
+ GCC_except_table1704
+ GCC_except_table1713
+ GCC_except_table1714
+ GCC_except_table1715
+ GCC_except_table1718
+ GCC_except_table1720
+ GCC_except_table1730
+ GCC_except_table1731
+ GCC_except_table1732
+ GCC_except_table1733
+ GCC_except_table1734
+ GCC_except_table1738
+ GCC_except_table1740
+ GCC_except_table1754
+ GCC_except_table1757
+ GCC_except_table1758
+ GCC_except_table1759
+ GCC_except_table1760
+ GCC_except_table1761
+ GCC_except_table1762
+ GCC_except_table1763
+ GCC_except_table1765
+ GCC_except_table1780
+ GCC_except_table1787
+ GCC_except_table1788
+ GCC_except_table1802
+ GCC_except_table1803
+ GCC_except_table1804
+ GCC_except_table1813
+ GCC_except_table1817
+ GCC_except_table1818
+ GCC_except_table1819
+ GCC_except_table1820
+ GCC_except_table1822
+ GCC_except_table1823
+ GCC_except_table1824
+ GCC_except_table1831
+ GCC_except_table1835
+ GCC_except_table1842
+ GCC_except_table1843
+ GCC_except_table1847
+ GCC_except_table1851
+ GCC_except_table1853
+ GCC_except_table1855
+ GCC_except_table1871
+ GCC_except_table1873
+ GCC_except_table1875
+ GCC_except_table1891
+ GCC_except_table1904
+ GCC_except_table1906
+ GCC_except_table1908
+ GCC_except_table1910
+ GCC_except_table1914
+ GCC_except_table1918
+ GCC_except_table1933
+ GCC_except_table1934
+ GCC_except_table1942
+ GCC_except_table1945
+ GCC_except_table1954
+ GCC_except_table1956
+ GCC_except_table1960
+ GCC_except_table1973
+ GCC_except_table1974
+ GCC_except_table1977
+ GCC_except_table1978
+ GCC_except_table1979
+ GCC_except_table1981
+ GCC_except_table1982
+ GCC_except_table1983
+ GCC_except_table1984
+ GCC_except_table1988
+ GCC_except_table1997
+ GCC_except_table1998
+ GCC_except_table2021
+ GCC_except_table2022
+ GCC_except_table351
+ GCC_except_table352
+ GCC_except_table358
+ GCC_except_table361
+ GCC_except_table385
+ GCC_except_table389
+ GCC_except_table390
+ GCC_except_table397
+ GCC_except_table407
+ GCC_except_table408
+ GCC_except_table421
+ GCC_except_table425
+ GCC_except_table440
+ GCC_except_table446
+ GCC_except_table450
+ GCC_except_table451
+ GCC_except_table455
+ GCC_except_table464
+ GCC_except_table473
+ GCC_except_table474
+ GCC_except_table482
+ GCC_except_table485
+ GCC_except_table486
+ GCC_except_table487
+ GCC_except_table488
+ GCC_except_table491
+ GCC_except_table493
+ GCC_except_table543
+ GCC_except_table544
+ GCC_except_table545
+ GCC_except_table548
+ GCC_except_table557
+ GCC_except_table558
+ GCC_except_table559
+ GCC_except_table560
+ GCC_except_table563
+ GCC_except_table580
+ GCC_except_table585
+ GCC_except_table599
+ GCC_except_table604
+ GCC_except_table606
+ GCC_except_table608
+ GCC_except_table640
+ GCC_except_table652
+ GCC_except_table657
+ GCC_except_table659
+ GCC_except_table662
+ GCC_except_table671
+ GCC_except_table679
+ GCC_except_table689
+ GCC_except_table694
+ GCC_except_table698
+ GCC_except_table702
+ GCC_except_table704
+ GCC_except_table713
+ GCC_except_table728
+ GCC_except_table732
+ GCC_except_table736
+ GCC_except_table750
+ GCC_except_table752
+ GCC_except_table754
+ GCC_except_table761
+ GCC_except_table784
+ GCC_except_table785
+ GCC_except_table789
+ GCC_except_table799
+ GCC_except_table801
+ GCC_except_table803
+ GCC_except_table807
+ GCC_except_table808
+ GCC_except_table821
+ GCC_except_table823
+ GCC_except_table825
+ GCC_except_table830
+ GCC_except_table832
+ GCC_except_table834
+ GCC_except_table842
+ GCC_except_table846
+ GCC_except_table847
+ GCC_except_table851
+ GCC_except_table852
+ GCC_except_table854
+ GCC_except_table855
+ GCC_except_table867
+ GCC_except_table880
+ GCC_except_table893
+ GCC_except_table894
+ GCC_except_table895
+ GCC_except_table897
+ GCC_except_table900
+ GCC_except_table918
+ GCC_except_table925
+ GCC_except_table926
+ GCC_except_table984
+ GCC_except_table985
+ OBJC_IVAR_$_ADExecutor._executorParameters
+ OBJC_IVAR_$_ADExecutor._ownedInferenceBuffers
+ OBJC_IVAR_$_ADExecutorParameters._bufferCopyPolicy
+ OBJC_IVAR_$_ADFlow._lastFrameTimestamp
+ OBJC_IVAR_$_ADFlow._maximalFrameRate
+ OBJC_IVAR_$_ADFlowFrameOutputPool._confidenceBufferPool
+ OBJC_IVAR_$_ADFlowFrameOutputPool._confidenceLevelsBufferPool
+ OBJC_IVAR_$_ADFlowFrameOutputPool._depthBufferPool
+ OBJC_IVAR_$_ADFlowFrameOutputPool._depthMaskBufferPool
+ OBJC_IVAR_$_ADFlowFrameOutputPool._normalsBufferPool
+ OBJC_IVAR_$_ADFlowFrameOutputPool._uncertaintyBufferPool
+ OBJC_IVAR_$_ADJasperColorFlow._frameOutputPool
+ OBJC_IVAR_$_ADMonocularV2Flow._executor
+ OBJC_IVAR_$_ADNetworkProviderLayoutShape._customStrides
+ OBJC_IVAR_$_ADNetworkProviderLayoutShape._layout
+ OBJC_IVAR_$_ADNetworkProviderLayoutShape._shape
+ _CVPixelBufferPoolCreate
+ _CVPixelBufferPoolCreatePixelBuffer
+ _CVPixelBufferPoolRelease
+ _OBJC_CLASS_$_ADFlowFrameOutputPool
+ _OBJC_CLASS_$_ADMonocularV2Flow
+ _OBJC_CLASS_$_ADNetworkProviderLayoutShape
+ _OBJC_CLASS_$_ADPreferences
+ _OBJC_METACLASS_$_ADFlowFrameOutputPool
+ _OBJC_METACLASS_$_ADMonocularV2Flow
+ _OBJC_METACLASS_$_ADNetworkProviderLayoutShape
+ _OBJC_METACLASS_$_ADPreferences
+ _ZL15INSTRUMENTS_ENDjyyyy.1144
+ _ZL15INSTRUMENTS_ENDjyyyy.1209
+ _ZL15INSTRUMENTS_ENDjyyyy.1245
+ _ZL15INSTRUMENTS_ENDjyyyy.1275
+ _ZL15INSTRUMENTS_ENDjyyyy.1371
+ _ZL15INSTRUMENTS_ENDjyyyy.1497
+ _ZL15INSTRUMENTS_ENDjyyyy.1503
+ _ZL15INSTRUMENTS_ENDjyyyy.1557
+ _ZL15INSTRUMENTS_ENDjyyyy.1693
+ _ZL15INSTRUMENTS_ENDjyyyy.1988
+ _ZL15INSTRUMENTS_ENDjyyyy.2178
+ _ZL15INSTRUMENTS_ENDjyyyy.2326
+ _ZL15INSTRUMENTS_ENDjyyyy.2517
+ _ZL15INSTRUMENTS_ENDjyyyy.2880
+ _ZL15INSTRUMENTS_ENDjyyyy.2936
+ _ZL15INSTRUMENTS_ENDjyyyy.3135
+ _ZL15INSTRUMENTS_ENDjyyyy.319
+ _ZL15INSTRUMENTS_ENDjyyyy.3357
+ _ZL15INSTRUMENTS_ENDjyyyy.3409
+ _ZL15INSTRUMENTS_ENDjyyyy.3569
+ _ZL15INSTRUMENTS_ENDjyyyy.3655
+ _ZL15INSTRUMENTS_ENDjyyyy.3819
+ _ZL15INSTRUMENTS_ENDjyyyy.3920
+ _ZL15INSTRUMENTS_ENDjyyyy.3943
+ _ZL15INSTRUMENTS_ENDjyyyy.4153
+ _ZL15INSTRUMENTS_ENDjyyyy.4203
+ _ZL15INSTRUMENTS_ENDjyyyy.4336
+ _ZL15INSTRUMENTS_ENDjyyyy.441
+ _ZL15INSTRUMENTS_ENDjyyyy.4518
+ _ZL15INSTRUMENTS_ENDjyyyy.4662
+ _ZL15INSTRUMENTS_ENDjyyyy.4792
+ _ZL15INSTRUMENTS_ENDjyyyy.4990
+ _ZL15INSTRUMENTS_ENDjyyyy.525
+ _ZL15INSTRUMENTS_ENDjyyyy.5463
+ _ZL15INSTRUMENTS_ENDjyyyy.5523
+ _ZL15INSTRUMENTS_ENDjyyyy.5686
+ _ZL15INSTRUMENTS_ENDjyyyy.596
+ _ZL15INSTRUMENTS_ENDjyyyy.696
+ _ZL15INSTRUMENTS_ENDjyyyy.728
+ _ZL15INSTRUMENTS_ENDjyyyy.841
+ _ZL15INSTRUMENTS_ENDjyyyy.986
+ _ZL17INSTRUMENTS_EVENTjyyyy.1145
+ _ZL17INSTRUMENTS_EVENTjyyyy.1210
+ _ZL17INSTRUMENTS_EVENTjyyyy.1246
+ _ZL17INSTRUMENTS_EVENTjyyyy.1276
+ _ZL17INSTRUMENTS_EVENTjyyyy.1372
+ _ZL17INSTRUMENTS_EVENTjyyyy.1498
+ _ZL17INSTRUMENTS_EVENTjyyyy.1504
+ _ZL17INSTRUMENTS_EVENTjyyyy.1558
+ _ZL17INSTRUMENTS_EVENTjyyyy.1694
+ _ZL17INSTRUMENTS_EVENTjyyyy.1989
+ _ZL17INSTRUMENTS_EVENTjyyyy.2179
+ _ZL17INSTRUMENTS_EVENTjyyyy.2327
+ _ZL17INSTRUMENTS_EVENTjyyyy.2518
+ _ZL17INSTRUMENTS_EVENTjyyyy.2881
+ _ZL17INSTRUMENTS_EVENTjyyyy.2937
+ _ZL17INSTRUMENTS_EVENTjyyyy.3136
+ _ZL17INSTRUMENTS_EVENTjyyyy.320
+ _ZL17INSTRUMENTS_EVENTjyyyy.3358
+ _ZL17INSTRUMENTS_EVENTjyyyy.3410
+ _ZL17INSTRUMENTS_EVENTjyyyy.3570
+ _ZL17INSTRUMENTS_EVENTjyyyy.3656
+ _ZL17INSTRUMENTS_EVENTjyyyy.3820
+ _ZL17INSTRUMENTS_EVENTjyyyy.3921
+ _ZL17INSTRUMENTS_EVENTjyyyy.3944
+ _ZL17INSTRUMENTS_EVENTjyyyy.4154
+ _ZL17INSTRUMENTS_EVENTjyyyy.4204
+ _ZL17INSTRUMENTS_EVENTjyyyy.4337
+ _ZL17INSTRUMENTS_EVENTjyyyy.442
+ _ZL17INSTRUMENTS_EVENTjyyyy.4519
+ _ZL17INSTRUMENTS_EVENTjyyyy.4663
+ _ZL17INSTRUMENTS_EVENTjyyyy.4793
+ _ZL17INSTRUMENTS_EVENTjyyyy.4991
+ _ZL17INSTRUMENTS_EVENTjyyyy.526
+ _ZL17INSTRUMENTS_EVENTjyyyy.5464
+ _ZL17INSTRUMENTS_EVENTjyyyy.5524
+ _ZL17INSTRUMENTS_EVENTjyyyy.5687
+ _ZL17INSTRUMENTS_EVENTjyyyy.597
+ _ZL17INSTRUMENTS_EVENTjyyyy.697
+ _ZL17INSTRUMENTS_EVENTjyyyy.729
+ _ZL17INSTRUMENTS_EVENTjyyyy.842
+ _ZL17INSTRUMENTS_EVENTjyyyy.987
+ _ZL17INSTRUMENTS_STARTjyyyy.1146
+ _ZL17INSTRUMENTS_STARTjyyyy.1211
+ _ZL17INSTRUMENTS_STARTjyyyy.1247
+ _ZL17INSTRUMENTS_STARTjyyyy.1277
+ _ZL17INSTRUMENTS_STARTjyyyy.1373
+ _ZL17INSTRUMENTS_STARTjyyyy.1499
+ _ZL17INSTRUMENTS_STARTjyyyy.1505
+ _ZL17INSTRUMENTS_STARTjyyyy.1559
+ _ZL17INSTRUMENTS_STARTjyyyy.1695
+ _ZL17INSTRUMENTS_STARTjyyyy.1990
+ _ZL17INSTRUMENTS_STARTjyyyy.2180
+ _ZL17INSTRUMENTS_STARTjyyyy.2328
+ _ZL17INSTRUMENTS_STARTjyyyy.2519
+ _ZL17INSTRUMENTS_STARTjyyyy.2882
+ _ZL17INSTRUMENTS_STARTjyyyy.2938
+ _ZL17INSTRUMENTS_STARTjyyyy.3137
+ _ZL17INSTRUMENTS_STARTjyyyy.321
+ _ZL17INSTRUMENTS_STARTjyyyy.3359
+ _ZL17INSTRUMENTS_STARTjyyyy.3411
+ _ZL17INSTRUMENTS_STARTjyyyy.3571
+ _ZL17INSTRUMENTS_STARTjyyyy.3657
+ _ZL17INSTRUMENTS_STARTjyyyy.3821
+ _ZL17INSTRUMENTS_STARTjyyyy.3922
+ _ZL17INSTRUMENTS_STARTjyyyy.3945
+ _ZL17INSTRUMENTS_STARTjyyyy.4155
+ _ZL17INSTRUMENTS_STARTjyyyy.4205
+ _ZL17INSTRUMENTS_STARTjyyyy.4338
+ _ZL17INSTRUMENTS_STARTjyyyy.443
+ _ZL17INSTRUMENTS_STARTjyyyy.4520
+ _ZL17INSTRUMENTS_STARTjyyyy.4664
+ _ZL17INSTRUMENTS_STARTjyyyy.4794
+ _ZL17INSTRUMENTS_STARTjyyyy.4992
+ _ZL17INSTRUMENTS_STARTjyyyy.527
+ _ZL17INSTRUMENTS_STARTjyyyy.5465
+ _ZL17INSTRUMENTS_STARTjyyyy.5525
+ _ZL17INSTRUMENTS_STARTjyyyy.5688
+ _ZL17INSTRUMENTS_STARTjyyyy.598
+ _ZL17INSTRUMENTS_STARTjyyyy.698
+ _ZL17INSTRUMENTS_STARTjyyyy.730
+ _ZL17INSTRUMENTS_STARTjyyyy.843
+ _ZL17INSTRUMENTS_STARTjyyyy.988
+ __OBJC_$_CLASS_METHODS_ADFlowFrameOutputPool
+ __OBJC_$_INSTANCE_METHODS_ADFlowFrameOutputPool
+ __OBJC_$_INSTANCE_METHODS_ADMonocularV2Flow
+ __OBJC_$_INSTANCE_METHODS_ADNetworkProviderLayoutShape
+ __OBJC_$_INSTANCE_VARIABLES_ADFlowFrameOutputPool
+ __OBJC_$_INSTANCE_VARIABLES_ADMonocularV2Flow
+ __OBJC_$_INSTANCE_VARIABLES_ADNetworkProviderLayoutShape
+ __OBJC_$_PROP_LIST_ADMonocularV2Flow
+ __OBJC_$_PROP_LIST_ADNetworkProviderLayoutShape
+ __OBJC_CLASS_PROTOCOLS_$_ADMonocularV2Flow
+ __OBJC_CLASS_RO_$_ADFlowFrameOutputPool
+ __OBJC_CLASS_RO_$_ADMonocularV2Flow
+ __OBJC_CLASS_RO_$_ADNetworkProviderLayoutShape
+ __OBJC_METACLASS_RO_$_ADFlowFrameOutputPool
+ __OBJC_METACLASS_RO_$_ADMonocularV2Flow
+ __OBJC_METACLASS_RO_$_ADNetworkProviderLayoutShape
+ __Z27vImageScale_NearestNeighborIDhEiPK13vImage_BufferS2_m
+ __Z27vImageScale_NearestNeighborIfEiPK13vImage_BufferS2_m
+ __Z27vImageScale_NearestNeighborItEiPK13vImage_BufferS2_m
+ __ZL22isJasperFrameValidImplP18ADJasperPointCloudP49ADJasperColorInFieldCalibrationPipelineParametersP51ADJasperColorInFieldCalibrationControllerParametersPDv3_fS6_Ph
+ __ZN16PixelBufferUtils21createPixelBufferPoolE6CGSizejm
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI31ADDisparityToDepthFitWorldPointNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI7CGPointNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIDv3_fNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyNS_4pairIPhiEEEENS_22__unordered_map_hasherIyS5_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS5_SA_S8_Lb1EEENS_9allocatorIS5_EEED1Ev
+ __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1ELm2ELm3ELm4ELm5EEEEJbffNS_6vectorIfNS_9allocatorIfEEEES6_NS3_I31ADDisparityToDepthFitWorldPointNS4_IS7_EEEEEEC2B8ne190102IJLm0ELm1ELm2ELm3ELm4ELm5EEJbffS6_S6_S9_EJEJEJbiiRS6_SC_RKS9_EEENS1_IJXspT_EEEENS_13__tuple_typesIJDpT0_EEENS1_IJXspT1_EEEENSG_IJDpT2_EEEDpOT3_
+ __ZNSt3__113__nth_elementB8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPfEEEEvT1_S8_S8_T0_
+ __ZNSt3__113unordered_setIiNS_4hashIiEENS_8equal_toIiEENS_9allocatorIiEEED1B8ne190102Ev
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__125__throw_bad_function_callB8ne190102Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne190102IPfS5_EEvT_T0_l
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ __ZZ71-[ADPearlColorInFieldCalibrationPipelineParameters getDefaultsForFlow:]E14defaultPerFlow
+ ___33-[ADLogManager initWithHandlers:]_block_invoke
+ ___61+[ADDeviceConfiguration registerVerbosityConfigurationUpdate]_block_invoke
+ ___block_descriptor_32_e18_v16?0"NSString"8l
+ ___block_descriptor_40_ea8_32s_e18_v16?0"NSString"8l
+ __block_literal_global.215
+ __block_literal_global.217
+ __block_literal_global.3636
+ __block_literal_global.5064
+ _kADDeviceConfigurationKeyPearlColorStdThreshold
+ _kADDeviceConfigurationKeyPearlColorStdThresholdNoOverride
+ _kCVPixelBufferHeightKey
+ _kCVPixelBufferPixelFormatTypeKey
+ _kCVPixelBufferPoolMinimumBufferCountKey
+ _kCVPixelBufferWidthKey
+ _objc_msgSend$allocateIOBufferForEspressoDescriptor:
+ _objc_msgSend$bufferCopyPolicy
+ _objc_msgSend$bufferFromPool:
+ _objc_msgSend$conformedByPixelBuffer:forLayout:
+ _objc_msgSend$createWithSize:layout:customStrides:
+ _objc_msgSend$customStrides
+ _objc_msgSend$depth
+ _objc_msgSend$doesSupportBufferCopyPolicy:
+ _objc_msgSend$doubleForKey:
+ _objc_msgSend$espressoRunnerForPath:forEngine:configurationName:
+ _objc_msgSend$executeWithColor:outDisparity:
+ _objc_msgSend$frameOutput
+ _objc_msgSend$getDefaultsForFlow:
+ _objc_msgSend$getMaxStdForValidResultForFlow:
+ _objc_msgSend$inferencePixelBufferForDescriptor:inputUserBuffer:
+ _objc_msgSend$initIsf
+ _objc_msgSend$initWithDepthDimensions:depthFormat:confidenceDimensions:confidenceFormat:confidenceLevelsDimensions:confidenceLevelsFormat:normalsDimensions:normalsFormat:uncertaintyDimensions:uncertaintyFormat:depthMaskDimensions:depthMaskFormat:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$isJasperFrameValid:
+ _objc_msgSend$isPearlFrameValid:
+ _objc_msgSend$isPearlMaskExpectedFor:
+ _objc_msgSend$isZUsedFor:
+ _objc_msgSend$poolWithDepthDescriptor:confidenceDescriptor:confidenceLevelsDescriptor:normalsDescriptor:uncertaintyDescriptor:depthMaskDescriptor:layout:
+ _objc_msgSend$poolWithDepthDescriptor:confidenceDescriptor:layout:
+ _objc_msgSend$preProcessJasper:referenceCameraCalibration:jasperCameraCalibration:reprojectedPointsBuffer:
+ _objc_msgSend$preProcessPearl:referenceCameraCalibration:pearlCameraCalibration:reprojectedPointsBuffer:reprojectedPointsMaskBuffer:
+ _objc_msgSend$processColor:timestamp:
+ _objc_msgSend$processConfigurationChange:
+ _objc_msgSend$processedConfidenceOutputDescriptor
+ _objc_msgSend$registerUpdateHandlerForKeys:invokeOnRegistration:scopeObject:handlerBlock:
+ _objc_msgSend$registerVerbosityConfigurationUpdate
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$setConfidenceLevels:
+ _objc_msgSend$setCustomStrides:
+ _objc_msgSend$setDepthMask:
+ _objc_msgSend$setExecutorParameters:
+ _objc_msgSend$setLayout:
+ _objc_msgSend$setNormals:
+ _objc_msgSend$setShape:
+ _objc_msgSend$setUncertainty:
+ _objc_msgSend$shape
+ _objc_msgSend$shouldProcessMatch:
+ _objc_msgSend$updateSizeForItem:fromShape:customStrides:forLayout:target:
+ _os_parse_boot_arg_int
- +[ADDeviceConfiguration getDefaultConfiguration]
- +[ADJasperColorInFieldCalibrationPipeline isInSupportedFormat:]
- +[ADNetworkProvider updateSizeForItem:fromShape:forLayout:target:]
- -[ADDensifiedLiDARFocusAssistExecutor executorParameters]
- -[ADDensifiedLiDARFocusAssistExecutor setExecutorParameters:]
- -[ADDeviceConfiguration .cxx_destruct]
- -[ADDeviceConfiguration createPropertyForKey:]
- -[ADDeviceConfiguration dealloc]
- -[ADDeviceConfiguration observeValueForKeyPath:ofObject:change:context:]
- -[ADDeviceConfiguration updateValue:forKey:]
- -[ADEspressoJasperColorInFieldCalibrationFrontendInferenceDescriptor initWithNetworkProvider:espressoEngine:networkFlowType:]
- -[ADJasperColorExecutor executorParameters]
- -[ADJasperColorExecutor setExecutorParameters:]
- -[ADJasperColorInFieldCalibrationControllerParameters initWithFlowType:]
- -[ADJasperColorInFieldCalibrationControllerParameters minRotationBetweenFrames]
- -[ADJasperColorInFieldCalibrationControllerParameters setMinRotationBetweenFrames:]
- -[ADJasperColorInFieldCalibrationExecutor executorParameters]
- -[ADJasperColorInFieldCalibrationExecutor rectifyColorCameraExtrinsics:]
- -[ADJasperColorInFieldCalibrationExecutor setExecutorParameters:]
- -[ADJasperColorInFieldCalibrationExecutor setVmcamToWmcamExtrinsics:]
- -[ADJasperColorInFieldCalibrationExecutor setWmcamToMcamExtrinsics:]
- -[ADJasperColorInFieldCalibrationExecutor vmcamToWmcamExtrinsics]
- -[ADJasperColorInFieldCalibrationExecutor wmcamToMcamExtrinsics]
- -[ADJasperColorInFieldCalibrationInterSessionData .cxx_construct]
- -[ADJasperColorInFieldCalibrationInterSessionData initDiagnosticPipelineLogWithFlowType:]
- -[ADJasperColorInFieldCalibrationInterSessionData initIsfWithFlowType:]
- -[ADJasperColorInFieldCalibrationInterSessionData initWithDictionaryRepresentation:andFlowType:]
- -[ADJasperColorInFieldCalibrationInterSessionData initWithFactoryJasperToColorTransform:currentJasperToColorTransform:andFlowType:]
- -[ADJasperColorInFieldCalibrationInterSessionData insertEntryToDiagnosticPipelineLog:]
- -[ADJasperColorInFieldCalibrationPipeline isJasperFrameValid:pose:prevPose:]
- -[ADJasperColorInFieldCalibrationPipeline preProcessJasper:pose:prevPose:referenceCameraCalibration:jasperCameraCalibration:reprojectedPointsBuffer:]
- -[ADJasperColorInFieldCalibrationPipeline updateWmcamToMcamExtrinsics:]
- -[ADJasperColorInFieldCalibrationPipeline validateInternalMemoryStatus:processedColor:]
- -[ADJasperColorStillsExecutor executorParameters]
- -[ADJasperColorStillsExecutor setExecutorParameters:]
- -[ADJasperColorV2Executor executorParameters]
- -[ADJasperColorV2Executor setExecutorParameters:]
- -[ADLogManager dealloc]
- -[ADLogManager observeValueForKeyPath:ofObject:change:context:]
- -[ADMonocularExecutor executorParameters]
- -[ADMonocularExecutor setExecutorParameters:]
- -[ADMonocularV2Executor executorParameters]
- -[ADMonocularV2Executor setExecutorParameters:]
- -[ADPCEDisparityColorExecutor executorParameters]
- -[ADPCEDisparityColorExecutor setExecutorParameters:]
- -[ADPearlColorInFieldCalibrationControllerParameters minRotationBetweenFrames]
- -[ADPearlColorInFieldCalibrationControllerParameters setMinRotationBetweenFrames:]
- -[ADPearlColorInFieldCalibrationExecutor executorParameters]
- -[ADPearlColorInFieldCalibrationExecutor rectifyColorCameraExtrinsics:]
- -[ADPearlColorInFieldCalibrationExecutor setExecutorParameters:]
- -[ADPearlColorInFieldCalibrationExecutor setVmcamToWmcamExtrinsics:]
- -[ADPearlColorInFieldCalibrationExecutor vmcamToWmcamExtrinsics]
- -[ADPearlColorInFieldCalibrationInterSessionData .cxx_construct]
- -[ADPearlColorInFieldCalibrationInterSessionData initDiagnosticPipelineLogWithFlowType:]
- -[ADPearlColorInFieldCalibrationInterSessionData insertEntryToDiagnosticPipelineLog:]
- -[ADPearlColorInFieldCalibrationPipeline isPearlFrameValid:pose:prevPose:]
- -[ADPearlColorInFieldCalibrationPipeline preProcessPearl:pose:prevPose:referenceCameraCalibration:pearlCameraCalibration:reprojectedPointsBuffer:reprojectedPointsMaskBuffer:]
- -[ADPearlColorInFieldCalibrationPipeline undistortColorImage:undistortedImage:calibration:]
- -[ADPearlColorInFieldCalibrationPipeline updateWmcamToMcamExtrinsics:]
- -[ADPearlColorInFieldCalibrationResult motionRotation]
- -[ADPearlColorInFieldCalibrationResult motionTranslation]
- -[ADPearlColorInFieldCalibrationResult setMotionRotation:]
- -[ADPearlColorInFieldCalibrationResult setMotionTranslation:]
- -[ADStereoExecutor executorParameters]
- -[ADStereoExecutor setExecutorParameters:]
- -[ADStereoV2Executor executorParameters]
- -[ADStereoV2Executor setExecutorParameters:]
- GCC_except_table1003
- GCC_except_table1010
- GCC_except_table1011
- GCC_except_table1021
- GCC_except_table1029
- GCC_except_table1038
- GCC_except_table1043
- GCC_except_table1047
- GCC_except_table1052
- GCC_except_table1053
- GCC_except_table1057
- GCC_except_table1059
- GCC_except_table1063
- GCC_except_table1078
- GCC_except_table1081
- GCC_except_table1083
- GCC_except_table1084
- GCC_except_table1085
- GCC_except_table1086
- GCC_except_table1088
- GCC_except_table1089
- GCC_except_table1098
- GCC_except_table1108
- GCC_except_table1113
- GCC_except_table1122
- GCC_except_table1123
- GCC_except_table1124
- GCC_except_table1125
- GCC_except_table1128
- GCC_except_table1133
- GCC_except_table1134
- GCC_except_table1149
- GCC_except_table1150
- GCC_except_table1159
- GCC_except_table1161
- GCC_except_table1183
- GCC_except_table1184
- GCC_except_table1192
- GCC_except_table1193
- GCC_except_table1258
- GCC_except_table1259
- GCC_except_table1278
- GCC_except_table1284
- GCC_except_table1293
- GCC_except_table1310
- GCC_except_table1312
- GCC_except_table1318
- GCC_except_table1335
- GCC_except_table1340
- GCC_except_table1351
- GCC_except_table1354
- GCC_except_table1357
- GCC_except_table1362
- GCC_except_table1367
- GCC_except_table1369
- GCC_except_table1370
- GCC_except_table1371
- GCC_except_table1372
- GCC_except_table1374
- GCC_except_table1384
- GCC_except_table1385
- GCC_except_table1407
- GCC_except_table1408
- GCC_except_table1413
- GCC_except_table1417
- GCC_except_table1419
- GCC_except_table1420
- GCC_except_table1429
- GCC_except_table1433
- GCC_except_table1436
- GCC_except_table1446
- GCC_except_table1447
- GCC_except_table1450
- GCC_except_table1453
- GCC_except_table1454
- GCC_except_table1476
- GCC_except_table1477
- GCC_except_table1486
- GCC_except_table1496
- GCC_except_table1501
- GCC_except_table1502
- GCC_except_table1503
- GCC_except_table1508
- GCC_except_table1511
- GCC_except_table1513
- GCC_except_table1514
- GCC_except_table1516
- GCC_except_table1519
- GCC_except_table1542
- GCC_except_table1556
- GCC_except_table1559
- GCC_except_table1562
- GCC_except_table1565
- GCC_except_table1570
- GCC_except_table1571
- GCC_except_table1572
- GCC_except_table1584
- GCC_except_table1586
- GCC_except_table1588
- GCC_except_table1589
- GCC_except_table1596
- GCC_except_table1597
- GCC_except_table1598
- GCC_except_table1599
- GCC_except_table1623
- GCC_except_table1625
- GCC_except_table1626
- GCC_except_table1627
- GCC_except_table1628
- GCC_except_table1630
- GCC_except_table1642
- GCC_except_table1645
- GCC_except_table1646
- GCC_except_table1647
- GCC_except_table1661
- GCC_except_table1675
- GCC_except_table1677
- GCC_except_table1678
- GCC_except_table1691
- GCC_except_table1694
- GCC_except_table1696
- GCC_except_table1697
- GCC_except_table1699
- GCC_except_table1707
- GCC_except_table1708
- GCC_except_table1709
- GCC_except_table1721
- GCC_except_table1722
- GCC_except_table1723
- GCC_except_table1724
- GCC_except_table1726
- GCC_except_table1743
- GCC_except_table1744
- GCC_except_table1746
- GCC_except_table1748
- GCC_except_table1750
- GCC_except_table1751
- GCC_except_table1752
- GCC_except_table1764
- GCC_except_table1769
- GCC_except_table1770
- GCC_except_table1771
- GCC_except_table1774
- GCC_except_table1775
- GCC_except_table1777
- GCC_except_table1792
- GCC_except_table1799
- GCC_except_table1800
- GCC_except_table1816
- GCC_except_table1828
- GCC_except_table1829
- GCC_except_table1830
- GCC_except_table1833
- GCC_except_table1834
- GCC_except_table1836
- GCC_except_table1837
- GCC_except_table1839
- GCC_except_table1848
- GCC_except_table1858
- GCC_except_table1859
- GCC_except_table1860
- GCC_except_table1878
- GCC_except_table1885
- GCC_except_table1886
- GCC_except_table1887
- GCC_except_table1897
- GCC_except_table1902
- GCC_except_table1905
- GCC_except_table1911
- GCC_except_table1919
- GCC_except_table1921
- GCC_except_table1922
- GCC_except_table1927
- GCC_except_table1929
- GCC_except_table1931
- GCC_except_table1936
- GCC_except_table1943
- GCC_except_table1946
- GCC_except_table1947
- GCC_except_table1958
- GCC_except_table1967
- GCC_except_table1968
- GCC_except_table1972
- GCC_except_table1991
- GCC_except_table1992
- GCC_except_table1993
- GCC_except_table1995
- GCC_except_table1996
- GCC_except_table2002
- GCC_except_table2011
- GCC_except_table2012
- GCC_except_table2014
- GCC_except_table2027
- GCC_except_table2035
- GCC_except_table2036
- GCC_except_table356
- GCC_except_table359
- GCC_except_table362
- GCC_except_table363
- GCC_except_table387
- GCC_except_table392
- GCC_except_table395
- GCC_except_table399
- GCC_except_table411
- GCC_except_table412
- GCC_except_table423
- GCC_except_table429
- GCC_except_table442
- GCC_except_table448
- GCC_except_table453
- GCC_except_table457
- GCC_except_table458
- GCC_except_table466
- GCC_except_table476
- GCC_except_table477
- GCC_except_table494
- GCC_except_table495
- GCC_except_table497
- GCC_except_table498
- GCC_except_table500
- GCC_except_table501
- GCC_except_table502
- GCC_except_table552
- GCC_except_table553
- GCC_except_table554
- GCC_except_table565
- GCC_except_table566
- GCC_except_table567
- GCC_except_table568
- GCC_except_table571
- GCC_except_table572
- GCC_except_table582
- GCC_except_table594
- GCC_except_table602
- GCC_except_table605
- GCC_except_table607
- GCC_except_table615
- GCC_except_table642
- GCC_except_table654
- GCC_except_table658
- GCC_except_table661
- GCC_except_table664
- GCC_except_table673
- GCC_except_table681
- GCC_except_table690
- GCC_except_table697
- GCC_except_table701
- GCC_except_table703
- GCC_except_table706
- GCC_except_table715
- GCC_except_table731
- GCC_except_table738
- GCC_except_table739
- GCC_except_table758
- GCC_except_table768
- GCC_except_table769
- GCC_except_table770
- GCC_except_table788
- GCC_except_table790
- GCC_except_table792
- GCC_except_table804
- GCC_except_table805
- GCC_except_table806
- GCC_except_table811
- GCC_except_table813
- GCC_except_table826
- GCC_except_table827
- GCC_except_table828
- GCC_except_table839
- GCC_except_table840
- GCC_except_table844
- GCC_except_table845
- GCC_except_table849
- GCC_except_table850
- GCC_except_table856
- GCC_except_table859
- GCC_except_table860
- GCC_except_table862
- GCC_except_table872
- GCC_except_table885
- GCC_except_table912
- GCC_except_table913
- GCC_except_table920
- GCC_except_table981
- GCC_except_table982
- GCC_except_table988
- OBJC_IVAR_$_ADDensifiedLiDARFocusAssistExecutor._executorParameters
- OBJC_IVAR_$_ADDeviceConfiguration._appleDepthUserDefaults
- OBJC_IVAR_$_ADDeviceConfiguration._currentDefaults
- OBJC_IVAR_$_ADDeviceConfiguration._globalUserDefaults
- OBJC_IVAR_$_ADDeviceConfiguration._ignoreValueUpdate
- OBJC_IVAR_$_ADJasperColorExecutor._executorParameters
- OBJC_IVAR_$_ADJasperColorInFieldCalibrationControllerParameters._minRotationBetweenFrames
- OBJC_IVAR_$_ADJasperColorInFieldCalibrationExecutor._executorParameters
- OBJC_IVAR_$_ADJasperColorInFieldCalibrationExecutor._prevJasperPose
- OBJC_IVAR_$_ADJasperColorInFieldCalibrationExecutor._vmcamToWmcamExtrinsics
- OBJC_IVAR_$_ADJasperColorInFieldCalibrationExecutor._wmcamToMcamExtrinsics
- OBJC_IVAR_$_ADJasperColorInFieldCalibrationInterSessionData._diagnosticPipelineLog
- OBJC_IVAR_$_ADJasperColorInFieldCalibrationInterSessionData._diagnosticPipelineLogIndex
- OBJC_IVAR_$_ADJasperColorInFieldCalibrationPipeline._networkFlowType
- OBJC_IVAR_$_ADJasperColorInFieldCalibrationPipeline._wmcamToMcamRotation
- OBJC_IVAR_$_ADJasperColorStillsExecutor._executorParameters
- OBJC_IVAR_$_ADJasperColorV2Executor._executorParameters
- OBJC_IVAR_$_ADMonocularExecutor._executorParameters
- OBJC_IVAR_$_ADMonocularV2Executor._executorParameters
- OBJC_IVAR_$_ADPCEDisparityColorExecutor._executorParameters
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationControllerParameters._minRotationBetweenFrames
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationExecutor._executorParameters
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationExecutor._prevPearlPose
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationExecutor._vmcamToWmcamExtrinsics
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationInterSessionData._diagnosticPipelineLog
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationInterSessionData._diagnosticPipelineLogIndex
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationPipeline._colorImageRaw
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationPipeline._distortedImagePixels
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationPipeline._motionRotationAngles
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationPipeline._motionTranslation
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationPipeline._origWorldPoints
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationPipeline._rectifiedPoints
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationPipeline._rectifiedWorldPoints
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationPipeline._referenceCameraNumOfPoints
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationPipeline._undistortedImagePixels
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationPipeline._wmcamToMcamRotation
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationPipeline._zVals
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationResult._motionRotation
- OBJC_IVAR_$_ADPearlColorInFieldCalibrationResult._motionTranslation
- OBJC_IVAR_$_ADStereoExecutor._executorParameters
- OBJC_IVAR_$_ADStereoV2Executor._executorParameters
- _IOObjectRelease
- _IORegistryEntryCreateCFProperty
- _IOServiceGetMatchingService
- _IOServiceNameMatching
- _OBJC_CLASS_$_ADMutableCameraCalibration
- _OBJC_CLASS_$_NSConstantDoubleNumber
- _OBJC_CLASS_$_NSMutableData
- _OBJC_CLASS_$_NSUserDefaults
- _PromotedConst.5728
- _PromotedConst.5729
- _ZL15INSTRUMENTS_ENDjyyyy.1011
- _ZL15INSTRUMENTS_ENDjyyyy.1152
- _ZL15INSTRUMENTS_ENDjyyyy.1215
- _ZL15INSTRUMENTS_ENDjyyyy.1251
- _ZL15INSTRUMENTS_ENDjyyyy.1287
- _ZL15INSTRUMENTS_ENDjyyyy.1377
- _ZL15INSTRUMENTS_ENDjyyyy.1510
- _ZL15INSTRUMENTS_ENDjyyyy.1516
- _ZL15INSTRUMENTS_ENDjyyyy.1572
- _ZL15INSTRUMENTS_ENDjyyyy.1714
- _ZL15INSTRUMENTS_ENDjyyyy.1966
- _ZL15INSTRUMENTS_ENDjyyyy.2199
- _ZL15INSTRUMENTS_ENDjyyyy.2349
- _ZL15INSTRUMENTS_ENDjyyyy.2501
- _ZL15INSTRUMENTS_ENDjyyyy.2971
- _ZL15INSTRUMENTS_ENDjyyyy.3027
- _ZL15INSTRUMENTS_ENDjyyyy.317
- _ZL15INSTRUMENTS_ENDjyyyy.3232
- _ZL15INSTRUMENTS_ENDjyyyy.3368
- _ZL15INSTRUMENTS_ENDjyyyy.3420
- _ZL15INSTRUMENTS_ENDjyyyy.3581
- _ZL15INSTRUMENTS_ENDjyyyy.3666
- _ZL15INSTRUMENTS_ENDjyyyy.3832
- _ZL15INSTRUMENTS_ENDjyyyy.3938
- _ZL15INSTRUMENTS_ENDjyyyy.3961
- _ZL15INSTRUMENTS_ENDjyyyy.4169
- _ZL15INSTRUMENTS_ENDjyyyy.4217
- _ZL15INSTRUMENTS_ENDjyyyy.4354
- _ZL15INSTRUMENTS_ENDjyyyy.439
- _ZL15INSTRUMENTS_ENDjyyyy.4532
- _ZL15INSTRUMENTS_ENDjyyyy.4682
- _ZL15INSTRUMENTS_ENDjyyyy.4810
- _ZL15INSTRUMENTS_ENDjyyyy.5017
- _ZL15INSTRUMENTS_ENDjyyyy.520
- _ZL15INSTRUMENTS_ENDjyyyy.5491
- _ZL15INSTRUMENTS_ENDjyyyy.5551
- _ZL15INSTRUMENTS_ENDjyyyy.5714
- _ZL15INSTRUMENTS_ENDjyyyy.591
- _ZL15INSTRUMENTS_ENDjyyyy.691
- _ZL15INSTRUMENTS_ENDjyyyy.723
- _ZL15INSTRUMENTS_ENDjyyyy.864
- _ZL17INSTRUMENTS_EVENTjyyyy.1012
- _ZL17INSTRUMENTS_EVENTjyyyy.1153
- _ZL17INSTRUMENTS_EVENTjyyyy.1216
- _ZL17INSTRUMENTS_EVENTjyyyy.1252
- _ZL17INSTRUMENTS_EVENTjyyyy.1288
- _ZL17INSTRUMENTS_EVENTjyyyy.1378
- _ZL17INSTRUMENTS_EVENTjyyyy.1511
- _ZL17INSTRUMENTS_EVENTjyyyy.1517
- _ZL17INSTRUMENTS_EVENTjyyyy.1573
- _ZL17INSTRUMENTS_EVENTjyyyy.1715
- _ZL17INSTRUMENTS_EVENTjyyyy.1967
- _ZL17INSTRUMENTS_EVENTjyyyy.2200
- _ZL17INSTRUMENTS_EVENTjyyyy.2350
- _ZL17INSTRUMENTS_EVENTjyyyy.2502
- _ZL17INSTRUMENTS_EVENTjyyyy.2972
- _ZL17INSTRUMENTS_EVENTjyyyy.3028
- _ZL17INSTRUMENTS_EVENTjyyyy.318
- _ZL17INSTRUMENTS_EVENTjyyyy.3233
- _ZL17INSTRUMENTS_EVENTjyyyy.3369
- _ZL17INSTRUMENTS_EVENTjyyyy.3421
- _ZL17INSTRUMENTS_EVENTjyyyy.3582
- _ZL17INSTRUMENTS_EVENTjyyyy.3667
- _ZL17INSTRUMENTS_EVENTjyyyy.3833
- _ZL17INSTRUMENTS_EVENTjyyyy.3939
- _ZL17INSTRUMENTS_EVENTjyyyy.3962
- _ZL17INSTRUMENTS_EVENTjyyyy.4170
- _ZL17INSTRUMENTS_EVENTjyyyy.4218
- _ZL17INSTRUMENTS_EVENTjyyyy.4355
- _ZL17INSTRUMENTS_EVENTjyyyy.440
- _ZL17INSTRUMENTS_EVENTjyyyy.4533
- _ZL17INSTRUMENTS_EVENTjyyyy.4683
- _ZL17INSTRUMENTS_EVENTjyyyy.4811
- _ZL17INSTRUMENTS_EVENTjyyyy.5018
- _ZL17INSTRUMENTS_EVENTjyyyy.521
- _ZL17INSTRUMENTS_EVENTjyyyy.5492
- _ZL17INSTRUMENTS_EVENTjyyyy.5552
- _ZL17INSTRUMENTS_EVENTjyyyy.5715
- _ZL17INSTRUMENTS_EVENTjyyyy.592
- _ZL17INSTRUMENTS_EVENTjyyyy.692
- _ZL17INSTRUMENTS_EVENTjyyyy.724
- _ZL17INSTRUMENTS_EVENTjyyyy.865
- _ZL17INSTRUMENTS_STARTjyyyy.1013
- _ZL17INSTRUMENTS_STARTjyyyy.1154
- _ZL17INSTRUMENTS_STARTjyyyy.1217
- _ZL17INSTRUMENTS_STARTjyyyy.1253
- _ZL17INSTRUMENTS_STARTjyyyy.1289
- _ZL17INSTRUMENTS_STARTjyyyy.1379
- _ZL17INSTRUMENTS_STARTjyyyy.1512
- _ZL17INSTRUMENTS_STARTjyyyy.1518
- _ZL17INSTRUMENTS_STARTjyyyy.1574
- _ZL17INSTRUMENTS_STARTjyyyy.1716
- _ZL17INSTRUMENTS_STARTjyyyy.1968
- _ZL17INSTRUMENTS_STARTjyyyy.2201
- _ZL17INSTRUMENTS_STARTjyyyy.2351
- _ZL17INSTRUMENTS_STARTjyyyy.2503
- _ZL17INSTRUMENTS_STARTjyyyy.2973
- _ZL17INSTRUMENTS_STARTjyyyy.3029
- _ZL17INSTRUMENTS_STARTjyyyy.319
- _ZL17INSTRUMENTS_STARTjyyyy.3234
- _ZL17INSTRUMENTS_STARTjyyyy.3370
- _ZL17INSTRUMENTS_STARTjyyyy.3422
- _ZL17INSTRUMENTS_STARTjyyyy.3583
- _ZL17INSTRUMENTS_STARTjyyyy.3668
- _ZL17INSTRUMENTS_STARTjyyyy.3834
- _ZL17INSTRUMENTS_STARTjyyyy.3940
- _ZL17INSTRUMENTS_STARTjyyyy.3963
- _ZL17INSTRUMENTS_STARTjyyyy.4171
- _ZL17INSTRUMENTS_STARTjyyyy.4219
- _ZL17INSTRUMENTS_STARTjyyyy.4356
- _ZL17INSTRUMENTS_STARTjyyyy.441
- _ZL17INSTRUMENTS_STARTjyyyy.4534
- _ZL17INSTRUMENTS_STARTjyyyy.4684
- _ZL17INSTRUMENTS_STARTjyyyy.4812
- _ZL17INSTRUMENTS_STARTjyyyy.5019
- _ZL17INSTRUMENTS_STARTjyyyy.522
- _ZL17INSTRUMENTS_STARTjyyyy.5493
- _ZL17INSTRUMENTS_STARTjyyyy.5553
- _ZL17INSTRUMENTS_STARTjyyyy.5716
- _ZL17INSTRUMENTS_STARTjyyyy.593
- _ZL17INSTRUMENTS_STARTjyyyy.693
- _ZL17INSTRUMENTS_STARTjyyyy.725
- _ZL17INSTRUMENTS_STARTjyyyy.866
- __OBJC_$_INSTANCE_VARIABLES_ADDeviceConfiguration
- __Z11getterDummyP11objc_objectP13objc_selector
- __Z11setterDummyP11objc_objectP13objc_selectorS0_
- __ZL22isJasperFrameValidImplP18ADJasperPointCloudP49ADJasperColorInFieldCalibrationPipelineParametersP51ADJasperColorInFieldCalibrationControllerParameters13simd_float4x4S5_PDv3_fS7_Ph
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI31ADDisparityToDepthFitWorldPointNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI7CGPointNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIDv3_fNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt9exception4whatEv
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1ELm2ELm3ELm4ELm5EEEEJbffNS_6vectorIfNS_9allocatorIfEEEES6_NS3_I31ADDisparityToDepthFitWorldPointNS4_IS7_EEEEEEC2B8ne180100IJLm0ELm1ELm2ELm3ELm4ELm5EEJbffS6_S6_S9_EJEJEJbiiRS6_SC_RKS9_EEENS1_IJXspT_EEEENS_13__tuple_typesIJDpT0_EEENS1_IJXspT1_EEEENSG_IJDpT2_EEEDpOT3_
- __ZNSt3__113__nth_elementB8ne180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPfEEEEvT1_S8_S8_T0_
- __ZNSt3__113unordered_setIiNS_4hashIiEENS_8equal_toIiEENS_9allocatorIiEEED1B8ne180100Ev
- __ZNSt3__117bad_function_callD0Ev
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__125__throw_bad_function_callB8ne180100Ev
- __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne180100IPfS5_EEvT_T0_l
- __ZNSt9exceptionD2Ev
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __ZZ48+[ADDeviceConfiguration getDefaultConfiguration]E31s_allADDeviceConfigurationItems
- __block_literal_global.209
- __block_literal_global.211
- __block_literal_global.5103
- _class_addMethod
- _class_addProperty
- _kADDeviceConfigurationKeyJasperColorInFieldMinRotationBetweenFrames
- _kADDeviceConfigurationKeyJasperColorInFieldOperationMode
- _kADDeviceConfigurationKeyJasperColorInfieldFrequency
- _kADDeviceConfigurationKeyPearlColorInFieldMinRotationBetweenFrames
- _kADDeviceConfigurationKeyPearlColorInFieldOperationMode
- _kADDeviceConfigurationKeyPearlColorIsfCapacity_iOS
- _kADDeviceConfigurationKeyPearlColorIsfOutliers_iOS
- _kADDeviceConfigurationKeyPearlColorStdThreshold_iOS
- _kIOMainPortDefault
- _objc_msgSend$addObserver:forKeyPath:options:context:
- _objc_msgSend$aggregationParameters
- _objc_msgSend$aggregationSize
- _objc_msgSend$allValues
- _objc_msgSend$appendBytes:length:
- _objc_msgSend$backProject:undistortedPixels:withZ:outPoints:
- _objc_msgSend$centerCrop:
- _objc_msgSend$createPropertyForKey:
- _objc_msgSend$didChangeValueForKey:
- _objc_msgSend$distort:undistortedPixels:outDistorted:
- _objc_msgSend$getDefaultConfiguration
- _objc_msgSend$initDiagnosticPipelineLogWithFlowType:
- _objc_msgSend$initWithFactoryJasperToColorTransform:currentJasperToColorTransform:andFlowType:
- _objc_msgSend$initWithFlowType:
- _objc_msgSend$initWithSuiteName:
- _objc_msgSend$isInSupportedFormat:
- _objc_msgSend$isJasperFrameValid:pose:prevPose:
- _objc_msgSend$isPearlFrameValid:pose:prevPose:
- _objc_msgSend$minRotationBetweenFrames
- _objc_msgSend$pcAggregationParameters
- _objc_msgSend$preProcessJasper:pose:prevPose:referenceCameraCalibration:jasperCameraCalibration:reprojectedPointsBuffer:
- _objc_msgSend$preProcessPearl:pose:prevPose:referenceCameraCalibration:pearlCameraCalibration:reprojectedPointsBuffer:reprojectedPointsMaskBuffer:
- _objc_msgSend$rectifyColorCameraExtrinsics:
- _objc_msgSend$removeObserver:forKeyPath:context:
- _objc_msgSend$resetPerformanceOverrides
- _objc_msgSend$setEmulatedDevice:
- _objc_msgSend$setMinRotationBetweenFrames:
- _objc_msgSend$setPerformanceOverrides:
- _objc_msgSend$setVmcamToWmcamExtrinsics:
- _objc_msgSend$setWmcamToMcamExtrinsics:
- _objc_msgSend$standardUserDefaults
- _objc_msgSend$stringByReplacingCharactersInRange:withString:
- _objc_msgSend$undistortColorImage:undistortedImage:calibration:
- _objc_msgSend$updateSizeForItem:fromShape:forLayout:target:
- _objc_msgSend$updateValue:forKey:
- _objc_msgSend$updateWmcamToMcamExtrinsics:
- _objc_msgSend$validateInternalMemoryStatus:processedColor:
- _objc_msgSend$willChangeValueForKey:
CStrings:
+ "%@/%010.0f_%s"
+ "%@/%010.0f_%s.%s"
+ "%@=0 is %@set"
+ "%s:%d - ERROR - failed creating pixelBufferPool with error %d"
+ "(SELF CONTAINS[c] %@)"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleDepth/AppleDepth/Utils/ADInFieldCalibrationInterSessionData.mm"
+ "137.3"
+ "@\"<ADEspressoRunnerProtocol>\""
+ "@\"ADExecutorParameters\""
+ "@\"ADFlowFrameOutputPool\""
+ "@\"ADMonocularV2Executor\""
+ "@136@0:8{CGSize=dd}16I32{CGSize=dd}36I52{CGSize=dd}56I72{CGSize=dd}76I92{CGSize=dd}96I112{CGSize=dd}116I132"
+ "@72@0:8@16@24@32@40@48@56Q64"
+ "ADFlowFrameOutputPool"
+ "ADMonocularV2Flow"
+ "ADNetworkProviderLayoutShape"
+ "AP"
+ "B20@0:8i16"
+ "B24@0:8Q16"
+ "Buffer copy policy is ForceNoCopy, but user buffer does not match the descriptor"
+ "Cannot prepare executor that requires crop/scale when buffer copy policy is ForceNoCopy"
+ "CustomStrides"
+ "DEV"
+ "Failed allocating a pixel buffer for channel %@"
+ "Missing required boot-arg: %@=0"
+ "Monocular V2 null output returned"
+ "NuCoReNetBackend_V59"
+ "NuCoReNetFrontend_V59"
+ "T@\"ADDensifiedLiDARFocusAssistExecutorParameters\",&,D,N"
+ "T@\"ADExecutorParameters\",&,N,V_executorParameters"
+ "T@\"ADJasperColorExecutorParameters\",&,D,N"
+ "T@\"ADJasperColorInFieldCalibrationExecutorParameters\",&,D,N"
+ "T@\"ADJasperColorPipeline\",R,&,N,V_pipeline"
+ "T@\"ADJasperColorStillsExecutorParameters\",&,D,N"
+ "T@\"ADJasperColorV2ExecutorParameters\",&,D,N"
+ "T@\"ADMonocularExecutorParameters\",&,D,N"
+ "T@\"ADMonocularV2Executor\",R,&,N,V_executor"
+ "T@\"ADMonocularV2ExecutorParameters\",&,D,N"
+ "T@\"ADPCEDisparityColorExecutorParameters\",&,D,N"
+ "T@\"ADPearlColorInFieldCalibrationExecutorParameters\",&,D,N"
+ "T@\"ADStereoExecutorParameters\",&,D,N"
+ "T@\"ADStereoV2ExecutorParameters\",&,D,N"
+ "T@\"NSArray\",&,N,V_customStrides"
+ "T@\"NSArray\",&,N,V_pointClouds"
+ "T@\"NSArray\",&,N,V_shape"
+ "T@\"NSDictionary\",&,N,V_figuresOfMerit"
+ "TQ,N,V_bufferCopyPolicy"
+ "TQ,N,V_layout"
+ "TQ,R,N,V_layout"
+ "T^{__CVBuffer=},N,V_color"
+ "T^{__CVBuffer=},N,V_confidence"
+ "T^{__CVBuffer=},N,V_confidenceLevels"
+ "T^{__CVBuffer=},N,V_depth"
+ "T^{__CVBuffer=},N,V_depthMask"
+ "T^{__CVBuffer=},N,V_normals"
+ "T^{__CVBuffer=},N,V_pearl"
+ "T^{__CVBuffer=},N,V_secondaryColor"
+ "T^{__CVBuffer=},N,V_uncertainty"
+ "Tf,N,V_maximalFrameRate"
+ "V59"
+ "WARNING: found multiple networks matching query. First one will be loaded (might not be what you intended). Found paths: %@"
+ "^{DefaultsForFlow=f}20@0:8i16"
+ "^{__CVBuffer=}24@0:8@16"
+ "^{__CVBuffer=}24@0:8^{__CVPixelBufferPool=}16"
+ "^{__CVBuffer=}32@0:8@16^^{__CVBuffer}24"
+ "^{__CVBuffer=}32@0:8@16^{__CVBuffer=}24"
+ "^{__CVPixelBufferPool=}"
+ "_bufferCopyPolicy"
+ "_confidenceBufferPool"
+ "_confidenceLevelsBufferPool"
+ "_customStrides"
+ "_depthBufferPool"
+ "_depthMaskBufferPool"
+ "_frameOutputPool"
+ "_lastFrameTimestamp"
+ "_maximalFrameRate"
+ "_normalsBufferPool"
+ "_ownedInferenceBuffers"
+ "_shape"
+ "_uncertaintyBufferPool"
+ "a!2"
+ "allocateIOBufferForEspressoDescriptor:"
+ "bufferCopyPolicy"
+ "bufferFromPool:"
+ "conformedByPixelBuffer:forLayout:"
+ "createPixelBufferPool"
+ "createWithSize:layout:customStrides:"
+ "customStrides"
+ "deallocInferenceBuffers"
+ "depth_input_b"
+ "doesSupportBufferCopyPolicy:"
+ "enforceModelSignatureChecks"
+ "espressoRunnerForPath:forEngine:configurationName:"
+ "executor does not support the requested buffer copy policy"
+ "f20@0:8i16"
+ "failed executing Monocular V2"
+ "frameOutput"
+ "getDefaultsForFlow:"
+ "getMaxStdForValidResultForFlow:"
+ "image_b"
+ "inferencePixelBufferForDescriptor:inputUserBuffer:"
+ "inferencePixelBufferForDescriptor:outputUserBuffer:"
+ "initWithDepthDimensions:depthFormat:confidenceDimensions:confidenceFormat:confidenceLevelsDimensions:confidenceLevelsFormat:normalsDimensions:normalsFormat:uncertaintyDimensions:uncertaintyFormat:depthMaskDimensions:depthMaskFormat:"
+ "initWithDomain:defaultValues:"
+ "isEqualToNumber:"
+ "isJasperFrameValid:"
+ "isPearlFrameValid:"
+ "isPearlMaskExpectedFor:"
+ "isZUsedFor:"
+ "mask_b"
+ "maximalFrameRate"
+ "pearlColorStdThreshold"
+ "poolWithDepthDescriptor:confidenceDescriptor:"
+ "poolWithDepthDescriptor:confidenceDescriptor:confidenceLevelsDescriptor:normalsDescriptor:uncertaintyDescriptor:depthMaskDescriptor:layout:"
+ "poolWithDepthDescriptor:confidenceDescriptor:layout:"
+ "poolWithDepthDimensions:depthFormat:confidenceDimensions:confidenceFormat:confidenceLevelsDimensions:confidenceLevelsFormat:normalsDimensions:normalsFormat:uncertaintyDimensions:uncertaintyFormat:depthMaskDimensions:depthMaskFormat:"
+ "preAllocateInferencePixelBufferForDescriptor:"
+ "preProcessJasper:referenceCameraCalibration:jasperCameraCalibration:reprojectedPointsBuffer:"
+ "preProcessPearl:referenceCameraCalibration:pearlCameraCalibration:reprojectedPointsBuffer:reprojectedPointsMaskBuffer:"
+ "processColor:timestamp:"
+ "processConfigurationChange:"
+ "pushColor:timestamp:"
+ "q32@0:8^{__CVBuffer=}16@24"
+ "q48@0:8@16@24@32^{__CVBuffer=}40"
+ "q56@0:8^{__CVBuffer=}16@24@32^{__CVBuffer=}40^{__CVBuffer=}48"
+ "registerUpdateHandlerForKeys:invokeOnRegistration:scopeObject:handlerBlock:"
+ "registerVerbosityConfigurationUpdate"
+ "removeAllObjects"
+ "setBufferCopyPolicy:"
+ "setCustomStrides:"
+ "setInferencePixelBuffer:forEspressoDescriptor:"
+ "setLayout:"
+ "setMaximalFrameRate:"
+ "setShape:"
+ "shape"
+ "shouldProcessMatch:"
+ "updateSizeForItem:fromShape:customStrides:forLayout:target:"
+ "v16@?0@\"NSString\"8"
+ "v32@0:8^{__CVBuffer=}16d24"
+ "v56@0:8@16@24@32Q40@48"
+ "\xf01"
- "%@ is %@set"
- "%@.%@"
- "%@/%010llu_%s"
- "%@/%010llu_%s.%s"
- "%s"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleDepth/AppleDepth/Utils/ADInFieldCalibrationInterSessionData.mm"
- "132.0"
- "@\"ADDensifiedLiDARFocusAssistExecutorParameters\""
- "@\"ADJasperColorExecutorParameters\""
- "@\"ADJasperColorInFieldCalibrationExecutorParameters\""
- "@\"ADJasperColorStillsExecutorParameters\""
- "@\"ADJasperColorV2ExecutorParameters\""
- "@\"ADMonocularExecutorParameters\""
- "@\"ADMonocularV2ExecutorParameters\""
- "@\"ADPCEDisparityColorExecutorParameters\""
- "@\"ADPearlColorInFieldCalibrationExecutorParameters\""
- "@\"ADStereoExecutorParameters\""
- "@\"ADStereoV2ExecutorParameters\""
- "@\"NSUserDefaults\""
- "@\"id\""
- "@@:"
- "A"
- "AD-RGB controller unsupported pixel format"
- "AD-RGBJ controller CVPixelBufferGetPixelFormatType:%c%c%c%c \n"
- "ADDeviceConfiguration: (%@)=>(%@)"
- "ADJasperColorInFieldCalibration jasper controller failed: frame not passing minimum rotation"
- "ADJasperColorInFieldCalibration jasper controller failed: percentage of valid depth is too low"
- "ADPearlColorInFieldCalibration pearl controller failed: frame not passing minimum rotation"
- "B152@0:8@16{?=[4]}24{?=[4]}88"
- "B152@0:8^{__CVBuffer=}16{?=[4]}24{?=[4]}88"
- "B166@0:8{ADJasperColorInFieldCalibrationDiagnosticPipelineEntry=IcCCffff[5[3f]][5[3f]][5C]cc}16"
- "B69@0:8{ADPearlColorInFieldCalibrationDiagnosticPipelineEntry=IccCCffff[3f][3f]Ccccc}16"
- "D"
- "JasperColorInfieldCalibration unable to create VT session"
- "JasperColorInfieldCalibration unfamiliar network flow type %d"
- "Missing required boot-arg: %@"
- "T"
- "T,N,V_motionRotation"
- "T,N,V_motionTranslation"
- "T@\"ADDensifiedLiDARFocusAssistExecutorParameters\",C,N,V_executorParameters"
- "T@\"ADJasperColorExecutorParameters\",&,N,V_executorParameters"
- "T@\"ADJasperColorInFieldCalibrationExecutorParameters\",C,N,V_executorParameters"
- "T@\"ADJasperColorStillsExecutorParameters\",C,N,V_executorParameters"
- "T@\"ADJasperColorV2ExecutorParameters\",C,N,V_executorParameters"
- "T@\"ADMonocularExecutorParameters\",&,N,V_executorParameters"
- "T@\"ADMonocularV2ExecutorParameters\",C,N,V_executorParameters"
- "T@\"ADPCEDisparityColorExecutorParameters\",C,N,V_executorParameters"
- "T@\"ADPearlColorInFieldCalibrationExecutorParameters\",C,N,V_executorParameters"
- "T@\"ADStereoExecutorParameters\",C,N,V_executorParameters"
- "T@\"ADStereoV2ExecutorParameters\",C,N,V_executorParameters"
- "T@\"NSArray\",R,&,N,V_pointClouds"
- "T@\"NSDictionary\",R,N,V_figuresOfMerit"
- "T^{__CVBuffer=},R,N,V_color"
- "T^{__CVBuffer=},R,N,V_confidence"
- "T^{__CVBuffer=},R,N,V_confidenceLevels"
- "T^{__CVBuffer=},R,N,V_depth"
- "T^{__CVBuffer=},R,N,V_depthMask"
- "T^{__CVBuffer=},R,N,V_normals"
- "T^{__CVBuffer=},R,N,V_pearl"
- "T^{__CVBuffer=},R,N,V_secondaryColor"
- "T^{__CVBuffer=},R,N,V_uncertainty"
- "Tf,N,V_minRotationBetweenFrames"
- "T{?=[4]},N,V_vmcamToWmcamExtrinsics"
- "Unable to verify boot-args"
- "_appleDepthUserDefaults"
- "_currentDefaults"
- "_diagnosticPipelineLog"
- "_diagnosticPipelineLogIndex"
- "_globalUserDefaults"
- "_ignoreValueUpdate"
- "_minRotationBetweenFrames"
- "_prevJasperPose"
- "_prevPearlPose"
- "_vmcamToWmcamExtrinsics"
- "_wmcamToMcamRotation"
- "addObserver:forKeyPath:options:context:"
- "aggregationSize"
- "allValues"
- "appendBytes:length:"
- "backProject:undistortedPixels:withZ:outPoints:"
- "boot-args"
- "cannot set configuration. %{public}@ is set in both global domain and in com.apple.appleDepth. please only use one."
- "centerCrop:"
- "colorImageRaw"
- "createPropertyForKey:"
- "diagnosticPipelineLog"
- "didChangeValueForKey:"
- "distort:undistortedPixels:outDistorted:"
- "enforceModelSignatureChecks=0"
- "error getting defaults key"
- "fail to create colorImageRaw"
- "failed setting property for configuration key %{public}@"
- "getDefaultConfiguration"
- "init color image raw buffer and reseting colorInput ProcessingSession"
- "init colorInput ProcessingSession"
- "initDiagnosticPipelineLogWithFlowType:"
- "initWithFactoryJasperToColorTransform:currentJasperToColorTransform:andFlowType:"
- "initWithFlowType:"
- "initWithSuiteName:"
- "insertEntryToDiagnosticPipelineLog:"
- "isInSupportedFormat:"
- "isJasperFrameValid:pose:prevPose:"
- "isPearlFrameValid:pose:prevPose:"
- "jasperColorInFieldMinRotationBetweenFrames"
- "jasperColorInFieldOperationMode"
- "jasperColorInfieldFrequency"
- "minRotationBetweenFrames"
- "motionRotationX"
- "motionRotationY"
- "motionRotationZ"
- "motionTranslationX"
- "motionTranslationY"
- "motionTranslationZ"
- "observeValueForKeyPath:ofObject:change:context:"
- "options"
- "pearlColorInFieldMinRotationBetweenFrames"
- "pearlColorInFieldOperationMode"
- "pearlColorIsfCapacity_iOS"
- "pearlColorIsfOutliers_iOS"
- "pearlColorStdThreshold_iOS"
- "preProcessJasper:pose:prevPose:referenceCameraCalibration:jasperCameraCalibration:reprojectedPointsBuffer:"
- "preProcessPearl:pose:prevPose:referenceCameraCalibration:pearlCameraCalibration:reprojectedPointsBuffer:reprojectedPointsMaskBuffer:"
- "q!"
- "q176@0:8@16{?=[4]}24{?=[4]}88@152@160^{__CVBuffer=}168"
- "q184@0:8^{__CVBuffer=}16{?=[4]}24{?=[4]}88@152@160^{__CVBuffer=}168^{__CVBuffer=}176"
- "rectifyColorCameraExtrinsics:"
- "removeObserver:forKeyPath:context:"
- "resetPerformanceOverrides"
- "setEmulatedDevice:"
- "setMinRotationBetweenFrames:"
- "setPerformanceOverrides:"
- "setVmcamToWmcamExtrinsics:"
- "standardUserDefaults"
- "stringByReplacingCharactersInRange:withString:"
- "updateSizeForItem:fromShape:forLayout:target:"
- "updateValue:forKey:"
- "updateWmcamToMcamExtrinsics:"
- "v48@0:8@16@24@32^v40"
- "v48@0:8@16@24Q32@40"
- "v@:@"
- "validateInternalMemoryStatus:processedColor:"
- "vmcamToWmcamExtrinsics"
- "willChangeValueForKey:"
- "{?=\"columns\"[3]}"
- "{?=[4]}80@0:8{?=[4]}16"
- "{vector<ADJasperColorInFieldCalibrationDiagnosticPipelineEntry, std::allocator<ADJasperColorInFieldCalibrationDiagnosticPipelineEntry>>=\"__begin_\"^{ADJasperColorInFieldCalibrationDiagnosticPipelineEntry}\"__end_\"^{ADJasperColorInFieldCalibrationDiagnosticPipelineEntry}\"__end_cap_\"{__compressed_pair<ADJasperColorInFieldCalibrationDiagnosticPipelineEntry *, std::allocator<ADJasperColorInFieldCalibrationDiagnosticPipelineEntry>>=\"__value_\"^{ADJasperColorInFieldCalibrationDiagnosticPipelineEntry}}}"
- "{vector<ADPearlColorInFieldCalibrationDiagnosticPipelineEntry, std::allocator<ADPearlColorInFieldCalibrationDiagnosticPipelineEntry>>=\"__begin_\"^{ADPearlColorInFieldCalibrationDiagnosticPipelineEntry}\"__end_\"^{ADPearlColorInFieldCalibrationDiagnosticPipelineEntry}\"__end_cap_\"{__compressed_pair<ADPearlColorInFieldCalibrationDiagnosticPipelineEntry *, std::allocator<ADPearlColorInFieldCalibrationDiagnosticPipelineEntry>>=\"__value_\"^{ADPearlColorInFieldCalibrationDiagnosticPipelineEntry}}}"
- "\xf02"

```
