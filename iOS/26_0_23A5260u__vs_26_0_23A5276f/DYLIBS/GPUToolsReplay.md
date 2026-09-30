## GPUToolsReplay

> `/System/Library/PrivateFrameworks/GPUToolsReplay.framework/GPUToolsReplay`

```diff

-310.22.0.0.0
-  __TEXT.__text: 0x313d84
+310.25.0.0.0
+  __TEXT.__text: 0x316440
   __TEXT.__auth_stubs: 0x1e70
   __TEXT.__init_offsets: 0xc
-  __TEXT.__objc_methlist: 0x64fc
-  __TEXT.__const: 0x92c0
-  __TEXT.__oslogstring: 0x1234
-  __TEXT.__cstring: 0xeca42
-  __TEXT.__gcc_except_tab: 0xf2a4
+  __TEXT.__objc_methlist: 0x6dc4
+  __TEXT.__const: 0x9320
+  __TEXT.__oslogstring: 0x124f
+  __TEXT.__cstring: 0xedb81
+  __TEXT.__gcc_except_tab: 0xf2ec
   __TEXT.__ustring: 0x4f6
-  __TEXT.__unwind_info: 0x3a08
-  __TEXT.__objc_classname: 0xc39
-  __TEXT.__objc_methname: 0x174b4
-  __TEXT.__objc_methtype: 0x5672
-  __TEXT.__objc_stubs: 0x14600
-  __DATA_CONST.__got: 0x930
-  __DATA_CONST.__const: 0x32ece8
-  __DATA_CONST.__objc_classlist: 0x268
+  __TEXT.__unwind_info: 0x3b20
+  __TEXT.__objc_classname: 0xcce
+  __TEXT.__objc_methname: 0x177c4
+  __TEXT.__objc_methtype: 0x5645
+  __TEXT.__objc_stubs: 0x14a40
+  __DATA_CONST.__got: 0x928
+  __DATA_CONST.__const: 0x3466e0
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x150
+  __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x61c8
+  __DATA_CONST.__objc_selrefs: 0x62c0
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x250
+  __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0xae8
   __AUTH_CONST.__auth_got: 0xf50
   __AUTH_CONST.__const: 0x1740
-  __AUTH_CONST.__cfstring: 0xe420
-  __AUTH_CONST.__objc_const: 0x9f58
+  __AUTH_CONST.__cfstring: 0xe480
+  __AUTH_CONST.__objc_const: 0xab40
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0x780
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x1810
+  __AUTH.__objc_data: 0x18b0
   __AUTH.__thread_vars: 0x78
   __AUTH.__thread_bss: 0x1088
   __DATA.__objc_ivar: 0x720
-  __DATA.__data: 0x1ff0
+  __DATA.__data: 0x2260
   __DATA.__bss: 0x13f8
   __DATA.__common: 0x4a
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CA10F754-0C17-3A54-A80E-B6B8D885C7B0
-  Functions: 5858
-  Symbols:   15447
-  CStrings:  22865
+  UUID: 82BE9B4C-CD77-30AD-ABBE-39A79C7163EE
+  Functions: 5972
+  Symbols:   15723
+  CStrings:  22973
 
Symbols:
+ +[GTReplayMTLFXTemporalDenoisedScaler wrapperWithDevice:descriptor:]
+ +[GTReplayMTLFXTemporalScaler wrapperWithDevice:descriptor:]
+ -[GTCaptureArchiveFilenameOverride debugDescription]
+ -[GTCaptureArchiveHeapRestoreTextureSliceOverrideKey debugDescription]
+ -[GTCaptureArchiveOverrideKey debugDescription]
+ -[GTCaptureArchiveOverrides copyWithZone:]
+ -[GTReplayMTLFXTemporalDenoisedScaler colorTextureFormat]
+ -[GTReplayMTLFXTemporalDenoisedScaler colorTextureUsage]
+ -[GTReplayMTLFXTemporalDenoisedScaler colorTexture]
+ -[GTReplayMTLFXTemporalDenoisedScaler debugTexture]
+ -[GTReplayMTLFXTemporalDenoisedScaler denoiseStrengthMaskTextureFormat]
+ -[GTReplayMTLFXTemporalDenoisedScaler denoiseStrengthMaskTextureUsage]
+ -[GTReplayMTLFXTemporalDenoisedScaler denoiseStrengthMaskTexture]
+ -[GTReplayMTLFXTemporalDenoisedScaler depthTextureFormat]
+ -[GTReplayMTLFXTemporalDenoisedScaler depthTextureUsage]
+ -[GTReplayMTLFXTemporalDenoisedScaler depthTexture]
+ -[GTReplayMTLFXTemporalDenoisedScaler diffuseAlbedoTextureFormat]
+ -[GTReplayMTLFXTemporalDenoisedScaler diffuseAlbedoTextureUsage]
+ -[GTReplayMTLFXTemporalDenoisedScaler diffuseAlbedoTexture]
+ -[GTReplayMTLFXTemporalDenoisedScaler dilatedMotionVectors]
+ -[GTReplayMTLFXTemporalDenoisedScaler encodeToCommandBuffer:]
+ -[GTReplayMTLFXTemporalDenoisedScaler encodeToCommandQueue:]
+ -[GTReplayMTLFXTemporalDenoisedScaler exposureTexture]
+ -[GTReplayMTLFXTemporalDenoisedScaler fence]
+ -[GTReplayMTLFXTemporalDenoisedScaler initWithDevice:descriptor:]
+ -[GTReplayMTLFXTemporalDenoisedScaler inputContentHeight]
+ -[GTReplayMTLFXTemporalDenoisedScaler inputContentMaxScale]
+ -[GTReplayMTLFXTemporalDenoisedScaler inputContentMinScale]
+ -[GTReplayMTLFXTemporalDenoisedScaler inputContentWidth]
+ -[GTReplayMTLFXTemporalDenoisedScaler inputHeight]
+ -[GTReplayMTLFXTemporalDenoisedScaler inputWidth]
+ -[GTReplayMTLFXTemporalDenoisedScaler isDepthReversed]
+ -[GTReplayMTLFXTemporalDenoisedScaler jitterOffsetX]
+ -[GTReplayMTLFXTemporalDenoisedScaler jitterOffsetY]
+ -[GTReplayMTLFXTemporalDenoisedScaler motionTextureFormat]
+ -[GTReplayMTLFXTemporalDenoisedScaler motionTextureUsage]
+ -[GTReplayMTLFXTemporalDenoisedScaler motionTexture]
+ -[GTReplayMTLFXTemporalDenoisedScaler motionVectorScaleX]
+ -[GTReplayMTLFXTemporalDenoisedScaler motionVectorScaleY]
+ -[GTReplayMTLFXTemporalDenoisedScaler normalTextureFormat]
+ -[GTReplayMTLFXTemporalDenoisedScaler normalTextureUsage]
+ -[GTReplayMTLFXTemporalDenoisedScaler normalTexture]
+ -[GTReplayMTLFXTemporalDenoisedScaler outputHeight]
+ -[GTReplayMTLFXTemporalDenoisedScaler outputTextureFormat]
+ -[GTReplayMTLFXTemporalDenoisedScaler outputTextureUsage]
+ -[GTReplayMTLFXTemporalDenoisedScaler outputTexture]
+ -[GTReplayMTLFXTemporalDenoisedScaler outputWidth]
+ -[GTReplayMTLFXTemporalDenoisedScaler preExposure]
+ -[GTReplayMTLFXTemporalDenoisedScaler reactiveMaskTextureFormat]
+ -[GTReplayMTLFXTemporalDenoisedScaler reactiveMaskTexture]
+ -[GTReplayMTLFXTemporalDenoisedScaler reactiveTextureUsage]
+ -[GTReplayMTLFXTemporalDenoisedScaler reset]
+ -[GTReplayMTLFXTemporalDenoisedScaler roughnessTextureFormat]
+ -[GTReplayMTLFXTemporalDenoisedScaler roughnessTextureUsage]
+ -[GTReplayMTLFXTemporalDenoisedScaler roughnessTexture]
+ -[GTReplayMTLFXTemporalDenoisedScaler setColorTexture:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setDebugTexture:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setDenoiseStrengthMaskTexture:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setDepthReversed:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setDepthTexture:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setDiffuseAlbedoTexture:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setExposureTexture:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setFence:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setInputContentHeight:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setInputContentWidth:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setJitterOffsetX:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setJitterOffsetY:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setMotionTexture:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setMotionVectorScaleX:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setMotionVectorScaleY:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setNormalTexture:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setOutputTexture:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setPreExposure:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setReactiveMaskTexture:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setReset:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setRoughnessTexture:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setShouldResetHistory:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setSpecularAlbedoTexture:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setSpecularHitDistanceTexture:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setTransparencyOverlayTexture:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setViewToClipMatrix:]
+ -[GTReplayMTLFXTemporalDenoisedScaler setWorldToViewMatrix:]
+ -[GTReplayMTLFXTemporalDenoisedScaler shouldResetHistory]
+ -[GTReplayMTLFXTemporalDenoisedScaler specularAlbedoTextureFormat]
+ -[GTReplayMTLFXTemporalDenoisedScaler specularAlbedoTextureUsage]
+ -[GTReplayMTLFXTemporalDenoisedScaler specularAlbedoTexture]
+ -[GTReplayMTLFXTemporalDenoisedScaler specularHitDistanceTextureFormat]
+ -[GTReplayMTLFXTemporalDenoisedScaler specularHitDistanceTextureUsage]
+ -[GTReplayMTLFXTemporalDenoisedScaler specularHitDistanceTexture]
+ -[GTReplayMTLFXTemporalDenoisedScaler transparencyOverlayTextureFormat]
+ -[GTReplayMTLFXTemporalDenoisedScaler transparencyOverlayTextureUsage]
+ -[GTReplayMTLFXTemporalDenoisedScaler transparencyOverlayTexture]
+ -[GTReplayMTLFXTemporalDenoisedScaler viewToClipMatrix]
+ -[GTReplayMTLFXTemporalDenoisedScaler worldToViewMatrix]
+ -[GTReplayMTLFXTemporalScaler colorTextureFormat]
+ -[GTReplayMTLFXTemporalScaler colorTextureUsage]
+ -[GTReplayMTLFXTemporalScaler colorTexture]
+ -[GTReplayMTLFXTemporalScaler currentViewToClipMatrix]
+ -[GTReplayMTLFXTemporalScaler currentWorldToViewMatrix]
+ -[GTReplayMTLFXTemporalScaler debugTexture]
+ -[GTReplayMTLFXTemporalScaler depthTextureFormat]
+ -[GTReplayMTLFXTemporalScaler depthTextureUsage]
+ -[GTReplayMTLFXTemporalScaler depthTexture]
+ -[GTReplayMTLFXTemporalScaler dilatedMotionVectors]
+ -[GTReplayMTLFXTemporalScaler encodeToCommandBuffer:]
+ -[GTReplayMTLFXTemporalScaler encodeToCommandQueue:]
+ -[GTReplayMTLFXTemporalScaler exposureTexture]
+ -[GTReplayMTLFXTemporalScaler fence]
+ -[GTReplayMTLFXTemporalScaler initWithDevice:descriptor:]
+ -[GTReplayMTLFXTemporalScaler inputContentHeight]
+ -[GTReplayMTLFXTemporalScaler inputContentMaxScale]
+ -[GTReplayMTLFXTemporalScaler inputContentMinScale]
+ -[GTReplayMTLFXTemporalScaler inputContentWidth]
+ -[GTReplayMTLFXTemporalScaler inputHeight]
+ -[GTReplayMTLFXTemporalScaler inputWidth]
+ -[GTReplayMTLFXTemporalScaler isDepthReversed]
+ -[GTReplayMTLFXTemporalScaler jitterOffsetX]
+ -[GTReplayMTLFXTemporalScaler jitterOffsetY]
+ -[GTReplayMTLFXTemporalScaler motionTextureFormat]
+ -[GTReplayMTLFXTemporalScaler motionTextureUsage]
+ -[GTReplayMTLFXTemporalScaler motionTexture]
+ -[GTReplayMTLFXTemporalScaler motionVectorScaleX]
+ -[GTReplayMTLFXTemporalScaler motionVectorScaleY]
+ -[GTReplayMTLFXTemporalScaler outputHeight]
+ -[GTReplayMTLFXTemporalScaler outputTextureFormat]
+ -[GTReplayMTLFXTemporalScaler outputTextureUsage]
+ -[GTReplayMTLFXTemporalScaler outputTexture]
+ -[GTReplayMTLFXTemporalScaler outputWidth]
+ -[GTReplayMTLFXTemporalScaler preExposure]
+ -[GTReplayMTLFXTemporalScaler previousJitterOffset]
+ -[GTReplayMTLFXTemporalScaler previousViewToClipMatrix]
+ -[GTReplayMTLFXTemporalScaler previousWorldToViewMatrix]
+ -[GTReplayMTLFXTemporalScaler reactiveMaskTextureFormat]
+ -[GTReplayMTLFXTemporalScaler reactiveMaskTexture]
+ -[GTReplayMTLFXTemporalScaler reactiveTextureUsage]
+ -[GTReplayMTLFXTemporalScaler reset]
+ -[GTReplayMTLFXTemporalScaler setColorTexture:]
+ -[GTReplayMTLFXTemporalScaler setCurrentViewToClipMatrix:]
+ -[GTReplayMTLFXTemporalScaler setCurrentWorldToViewMatrix:]
+ -[GTReplayMTLFXTemporalScaler setDebugTexture:]
+ -[GTReplayMTLFXTemporalScaler setDepthReversed:]
+ -[GTReplayMTLFXTemporalScaler setDepthTexture:]
+ -[GTReplayMTLFXTemporalScaler setExposureTexture:]
+ -[GTReplayMTLFXTemporalScaler setFence:]
+ -[GTReplayMTLFXTemporalScaler setInputContentHeight:]
+ -[GTReplayMTLFXTemporalScaler setInputContentWidth:]
+ -[GTReplayMTLFXTemporalScaler setJitterOffsetX:]
+ -[GTReplayMTLFXTemporalScaler setJitterOffsetY:]
+ -[GTReplayMTLFXTemporalScaler setMotionTexture:]
+ -[GTReplayMTLFXTemporalScaler setMotionVectorScaleX:]
+ -[GTReplayMTLFXTemporalScaler setMotionVectorScaleY:]
+ -[GTReplayMTLFXTemporalScaler setOutputTexture:]
+ -[GTReplayMTLFXTemporalScaler setPreExposure:]
+ -[GTReplayMTLFXTemporalScaler setPreviousJitterOffset:]
+ -[GTReplayMTLFXTemporalScaler setPreviousViewToClipMatrix:]
+ -[GTReplayMTLFXTemporalScaler setPreviousWorldToViewMatrix:]
+ -[GTReplayMTLFXTemporalScaler setReactiveMaskTexture:]
+ -[GTReplayMTLFXTemporalScaler setReset:]
+ -[GTReplayWrapperBase .cxx_destruct]
+ -[GTReplayWrapperBase effectID]
+ -[GTReplayWrapperBase executionMode]
+ -[GTReplayWrapperBase forwardingTargetForSelector:]
+ -[GTReplayWrapperBase setExecutionMode:]
+ -[GTReplayWrapperBase setTracingDelegate:]
+ -[GTReplayWrapperBase tracingDelegate]
+ GCC_except_table1003
+ GCC_except_table1022
+ GCC_except_table1030
+ GCC_except_table1031
+ GCC_except_table1032
+ GCC_except_table1033
+ GCC_except_table1038
+ GCC_except_table1039
+ GCC_except_table1043
+ GCC_except_table1047
+ GCC_except_table1048
+ GCC_except_table1049
+ GCC_except_table1061
+ GCC_except_table1065
+ GCC_except_table1066
+ GCC_except_table1068
+ GCC_except_table1069
+ GCC_except_table1072
+ GCC_except_table1073
+ GCC_except_table1078
+ GCC_except_table1079
+ GCC_except_table1085
+ GCC_except_table1086
+ GCC_except_table1088
+ GCC_except_table1090
+ GCC_except_table1091
+ GCC_except_table1092
+ GCC_except_table1093
+ GCC_except_table1094
+ GCC_except_table1095
+ GCC_except_table1096
+ GCC_except_table1098
+ GCC_except_table1101
+ GCC_except_table1102
+ GCC_except_table1106
+ GCC_except_table1113
+ GCC_except_table1114
+ GCC_except_table1115
+ GCC_except_table1116
+ GCC_except_table1117
+ GCC_except_table1118
+ GCC_except_table1119
+ GCC_except_table1120
+ GCC_except_table1121
+ GCC_except_table1123
+ GCC_except_table1127
+ GCC_except_table1141
+ GCC_except_table1143
+ GCC_except_table1144
+ GCC_except_table1145
+ GCC_except_table1146
+ GCC_except_table1147
+ GCC_except_table1148
+ GCC_except_table1150
+ GCC_except_table1152
+ GCC_except_table1153
+ GCC_except_table1158
+ GCC_except_table1171
+ GCC_except_table1172
+ GCC_except_table1173
+ GCC_except_table1176
+ GCC_except_table1177
+ GCC_except_table1178
+ GCC_except_table1179
+ GCC_except_table1180
+ GCC_except_table1181
+ GCC_except_table1182
+ GCC_except_table1183
+ GCC_except_table1184
+ GCC_except_table1185
+ GCC_except_table1190
+ GCC_except_table1206
+ GCC_except_table1219
+ GCC_except_table1223
+ GCC_except_table1231
+ GCC_except_table1295
+ GCC_except_table1430
+ GCC_except_table1431
+ GCC_except_table1486
+ GCC_except_table1511
+ GCC_except_table1542
+ GCC_except_table1543
+ GCC_except_table1546
+ GCC_except_table1547
+ GCC_except_table1564
+ GCC_except_table1566
+ GCC_except_table1568
+ GCC_except_table1570
+ GCC_except_table1572
+ GCC_except_table1580
+ GCC_except_table1690
+ GCC_except_table1691
+ GCC_except_table1692
+ GCC_except_table1693
+ GCC_except_table1694
+ GCC_except_table1695
+ GCC_except_table1705
+ GCC_except_table1712
+ GCC_except_table1713
+ GCC_except_table1714
+ GCC_except_table1715
+ GCC_except_table1717
+ GCC_except_table1719
+ GCC_except_table1720
+ GCC_except_table1722
+ GCC_except_table1723
+ GCC_except_table1725
+ GCC_except_table1735
+ GCC_except_table1782
+ GCC_except_table1783
+ GCC_except_table1784
+ GCC_except_table1785
+ GCC_except_table1786
+ GCC_except_table1787
+ GCC_except_table1790
+ GCC_except_table1863
+ GCC_except_table1864
+ GCC_except_table1865
+ GCC_except_table1885
+ GCC_except_table1900
+ GCC_except_table1901
+ GCC_except_table1902
+ GCC_except_table1903
+ GCC_except_table1904
+ GCC_except_table1909
+ GCC_except_table1912
+ GCC_except_table1927
+ GCC_except_table1937
+ GCC_except_table1939
+ GCC_except_table1975
+ GCC_except_table1977
+ GCC_except_table1979
+ GCC_except_table1980
+ GCC_except_table1981
+ GCC_except_table1989
+ GCC_except_table200
+ GCC_except_table2011
+ GCC_except_table2014
+ GCC_except_table2030
+ GCC_except_table2033
+ GCC_except_table2035
+ GCC_except_table2040
+ GCC_except_table2043
+ GCC_except_table2050
+ GCC_except_table2052
+ GCC_except_table2053
+ GCC_except_table2054
+ GCC_except_table2057
+ GCC_except_table2058
+ GCC_except_table2063
+ GCC_except_table2070
+ GCC_except_table2071
+ GCC_except_table2072
+ GCC_except_table2074
+ GCC_except_table2075
+ GCC_except_table2080
+ GCC_except_table2081
+ GCC_except_table2082
+ GCC_except_table2083
+ GCC_except_table2084
+ GCC_except_table2085
+ GCC_except_table2086
+ GCC_except_table2087
+ GCC_except_table2088
+ GCC_except_table2089
+ GCC_except_table2090
+ GCC_except_table2092
+ GCC_except_table2093
+ GCC_except_table2094
+ GCC_except_table2095
+ GCC_except_table2096
+ GCC_except_table2097
+ GCC_except_table2098
+ GCC_except_table2099
+ GCC_except_table2100
+ GCC_except_table2106
+ GCC_except_table2107
+ GCC_except_table2112
+ GCC_except_table2114
+ GCC_except_table2117
+ GCC_except_table2119
+ GCC_except_table2123
+ GCC_except_table2124
+ GCC_except_table2125
+ GCC_except_table2126
+ GCC_except_table2128
+ GCC_except_table2131
+ GCC_except_table2133
+ GCC_except_table2134
+ GCC_except_table2135
+ GCC_except_table2142
+ GCC_except_table2496
+ GCC_except_table2520
+ GCC_except_table2591
+ GCC_except_table2595
+ GCC_except_table2599
+ GCC_except_table2601
+ GCC_except_table2620
+ GCC_except_table2627
+ GCC_except_table2634
+ GCC_except_table2636
+ GCC_except_table2638
+ GCC_except_table2640
+ GCC_except_table2641
+ GCC_except_table2643
+ GCC_except_table2644
+ GCC_except_table2645
+ GCC_except_table2646
+ GCC_except_table2647
+ GCC_except_table2649
+ GCC_except_table2660
+ GCC_except_table2663
+ GCC_except_table2666
+ GCC_except_table2673
+ GCC_except_table2676
+ GCC_except_table2685
+ GCC_except_table2689
+ GCC_except_table2693
+ GCC_except_table2703
+ GCC_except_table2707
+ GCC_except_table2741
+ GCC_except_table2764
+ GCC_except_table2772
+ GCC_except_table2773
+ GCC_except_table2775
+ GCC_except_table2776
+ GCC_except_table2777
+ GCC_except_table2798
+ GCC_except_table2799
+ GCC_except_table2801
+ GCC_except_table2802
+ GCC_except_table2803
+ GCC_except_table2815
+ GCC_except_table2845
+ GCC_except_table2848
+ GCC_except_table2849
+ GCC_except_table2850
+ GCC_except_table2851
+ GCC_except_table2852
+ GCC_except_table2853
+ GCC_except_table2858
+ GCC_except_table2862
+ GCC_except_table2867
+ GCC_except_table2872
+ GCC_except_table2903
+ GCC_except_table2906
+ GCC_except_table2907
+ GCC_except_table299
+ GCC_except_table2994
+ GCC_except_table301
+ GCC_except_table304
+ GCC_except_table309
+ GCC_except_table316
+ GCC_except_table317
+ GCC_except_table318
+ GCC_except_table332
+ GCC_except_table343
+ GCC_except_table354
+ GCC_except_table360
+ GCC_except_table361
+ GCC_except_table371
+ GCC_except_table379
+ GCC_except_table381
+ GCC_except_table382
+ GCC_except_table383
+ GCC_except_table389
+ GCC_except_table425
+ GCC_except_table431
+ GCC_except_table462
+ GCC_except_table466
+ GCC_except_table467
+ GCC_except_table477
+ GCC_except_table479
+ GCC_except_table486
+ GCC_except_table506
+ GCC_except_table513
+ GCC_except_table555
+ GCC_except_table559
+ GCC_except_table560
+ GCC_except_table566
+ GCC_except_table567
+ GCC_except_table573
+ GCC_except_table574
+ GCC_except_table575
+ GCC_except_table580
+ GCC_except_table582
+ GCC_except_table583
+ GCC_except_table584
+ GCC_except_table591
+ GCC_except_table592
+ GCC_except_table594
+ GCC_except_table608
+ GCC_except_table611
+ GCC_except_table639
+ GCC_except_table648
+ GCC_except_table655
+ GCC_except_table656
+ GCC_except_table657
+ GCC_except_table660
+ GCC_except_table668
+ GCC_except_table669
+ GCC_except_table678
+ GCC_except_table679
+ GCC_except_table681
+ GCC_except_table682
+ GCC_except_table683
+ GCC_except_table684
+ GCC_except_table691
+ GCC_except_table692
+ GCC_except_table695
+ GCC_except_table697
+ GCC_except_table699
+ GCC_except_table701
+ GCC_except_table703
+ GCC_except_table714
+ GCC_except_table715
+ GCC_except_table716
+ GCC_except_table718
+ GCC_except_table720
+ GCC_except_table725
+ GCC_except_table726
+ GCC_except_table727
+ GCC_except_table728
+ GCC_except_table729
+ GCC_except_table734
+ GCC_except_table735
+ GCC_except_table736
+ GCC_except_table740
+ GCC_except_table741
+ GCC_except_table742
+ GCC_except_table749
+ GCC_except_table750
+ GCC_except_table752
+ GCC_except_table754
+ GCC_except_table763
+ GCC_except_table764
+ GCC_except_table765
+ GCC_except_table767
+ GCC_except_table768
+ GCC_except_table769
+ GCC_except_table771
+ GCC_except_table779
+ GCC_except_table780
+ GCC_except_table781
+ GCC_except_table782
+ GCC_except_table783
+ GCC_except_table784
+ GCC_except_table785
+ GCC_except_table786
+ GCC_except_table787
+ GCC_except_table790
+ GCC_except_table791
+ GCC_except_table793
+ GCC_except_table795
+ GCC_except_table798
+ GCC_except_table802
+ GCC_except_table809
+ GCC_except_table810
+ GCC_except_table811
+ GCC_except_table825
+ GCC_except_table960
+ GCC_except_table985
+ GCC_except_table996
+ GCC_except_table997
+ _AppendString.13693
+ _CleanupSandboxExtensionURL.883
+ _CreateEncoderStream
+ _CreateScalersWithBlock
+ _CreateStream
+ _DYTraceDecode_MTL4ArgumentTable_setAddress_attributeStride_atIndex
+ _DYTraceDecode_MTLCommandBuffer___waitUntilCompletedAsync
+ _DYTraceDecode_MTLCommandBuffer___waitUntilScheduledAsync
+ _DYTraceDecode_MTLDevice_newArgumentEncoderWithArguments
+ _DYTraceDecode_MTLDevice_setRequiresLegacyCompilerProcessesCount
+ _DYTraceDecode_MTLFXTemporalDenoisedScaler_executionMode
+ _GTTraceFbufToFunc_createStream
+ _GTTraceFunc_getFuncStreamRef
+ _GetOpenStream
+ _GetStream.13248
+ _GetStreamAtIndex
+ _GroupBuilder_getCommandEncoder.5195
+ _NewCommandBuffer.5657
+ _OBJC_CLASS_$_GTReplayMTLFXTemporalDenoisedScaler
+ _OBJC_CLASS_$_GTReplayMTLFXTemporalScaler
+ _OBJC_CLASS_$_GTReplayWrapperBase
+ _OBJC_IVAR_$_GTReplayWrapperBase._aneScaler
+ _OBJC_IVAR_$_GTReplayWrapperBase._effectID
+ _OBJC_IVAR_$_GTReplayWrapperBase._executionMode
+ _OBJC_IVAR_$_GTReplayWrapperBase._gpuScaler
+ _OBJC_METACLASS_$_GTReplayMTLFXTemporalDenoisedScaler
+ _OBJC_METACLASS_$_GTReplayMTLFXTemporalScaler
+ _OBJC_METACLASS_$_GTReplayWrapperBase
+ __OBJC_$_CLASS_METHODS_GTReplayMTLFXTemporalDenoisedScaler
+ __OBJC_$_CLASS_METHODS_GTReplayMTLFXTemporalScaler
+ __OBJC_$_INSTANCE_METHODS_GTReplayMTLFXTemporalDenoisedScaler
+ __OBJC_$_INSTANCE_METHODS_GTReplayMTLFXTemporalScaler
+ __OBJC_$_INSTANCE_METHODS_GTReplayWrapperBase
+ __OBJC_$_INSTANCE_VARIABLES_GTReplayWrapperBase
+ __OBJC_$_PROP_LIST_GTReplayMTLFXTemporalDenoisedScaler
+ __OBJC_$_PROP_LIST_GTReplayMTLFXTemporalScaler
+ __OBJC_$_PROP_LIST_GTReplayWrapperBase
+ __OBJC_$_PROP_LIST_MTLFXTemporalDenoisedScalerBase
+ __OBJC_$_PROP_LIST_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXTemporalDenoisedScaler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXTemporalDenoisedScalerBase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXTemporalDenoisedScaler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXTemporalDenoisedScalerBase
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_$_PROTOCOL_REFS_MTLFXTemporalDenoisedScaler
+ __OBJC_$_PROTOCOL_REFS_MTLFXTemporalDenoisedScalerBase
+ __OBJC_$_PROTOCOL_REFS_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_CLASS_PROTOCOLS_$_GTReplayMTLFXTemporalDenoisedScaler
+ __OBJC_CLASS_PROTOCOLS_$_GTReplayMTLFXTemporalScaler
+ __OBJC_CLASS_RO_$_GTReplayMTLFXTemporalDenoisedScaler
+ __OBJC_CLASS_RO_$_GTReplayMTLFXTemporalScaler
+ __OBJC_CLASS_RO_$_GTReplayWrapperBase
+ __OBJC_LABEL_PROTOCOL_$_MTLFXTemporalDenoisedScaler
+ __OBJC_LABEL_PROTOCOL_$_MTLFXTemporalDenoisedScalerBase
+ __OBJC_LABEL_PROTOCOL_$_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_METACLASS_RO_$_GTReplayMTLFXTemporalDenoisedScaler
+ __OBJC_METACLASS_RO_$_GTReplayMTLFXTemporalScaler
+ __OBJC_METACLASS_RO_$_GTReplayWrapperBase
+ __OBJC_PROTOCOL_$_MTLFXTemporalDenoisedScaler
+ __OBJC_PROTOCOL_$_MTLFXTemporalDenoisedScalerBase
+ __OBJC_PROTOCOL_$_MTLFXTemporalDenoisedScalerSPI
+ __ZL16DispatchFunctionP21GTMTLReplayControllerPK11GTTraceFuncRb.1365
+ __ZL23GetRenderPassDescriptorPK11GTTraceFuncP10apr_hash_t.1366
+ __ZL31DisableComputeEncoderCoalescingP21GTMTLReplayControllerb.1313
+ ___57-[GTReplayMTLFXTemporalScaler initWithDevice:descriptor:]_block_invoke
+ ___65-[GTReplayMTLFXTemporalDenoisedScaler initWithDevice:descriptor:]_block_invoke
+ ___Block_byref_object_copy_.1521
+ ___Block_byref_object_copy_.1877
+ ___Block_byref_object_copy_.455
+ ___Block_byref_object_copy_.5845
+ ___Block_byref_object_copy_.7156
+ ___Block_byref_object_copy_.827
+ ___Block_byref_object_copy_.9138
+ ___Block_byref_object_copy_.9755
+ ___Block_byref_object_copy_.9787
+ ___Block_byref_object_dispose_.1522
+ ___Block_byref_object_dispose_.1878
+ ___Block_byref_object_dispose_.456
+ ___Block_byref_object_dispose_.5846
+ ___Block_byref_object_dispose_.7157
+ ___Block_byref_object_dispose_.828
+ ___Block_byref_object_dispose_.9139
+ ___Block_byref_object_dispose_.9756
+ ___Block_byref_object_dispose_.9788
+ ___block_descriptor_48_e8_32s40s_e28_"<MTLFXTemporalScaler>"8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e36_"<MTLFXTemporalDenoisedScaler>"8?0ls32l8s40l8
+ ___block_literal_global.100
+ ___block_literal_global.10758
+ ___block_literal_global.10846
+ ___block_literal_global.11339
+ ___block_literal_global.1474
+ ___block_literal_global.1582
+ ___block_literal_global.1726
+ ___block_literal_global.19
+ ___block_literal_global.2472
+ ___block_literal_global.2606
+ ___block_literal_global.2924
+ ___block_literal_global.3003
+ ___block_literal_global.4332
+ ___block_literal_global.5407
+ ___block_literal_global.5892
+ ___block_literal_global.6329
+ ___block_literal_global.6692
+ ___block_literal_global.6713
+ ___block_literal_global.6872
+ ___block_literal_global.722
+ ___block_literal_global.7529
+ ___block_literal_global.90
+ ___block_literal_global.955
+ ___block_literal_global.98
+ _g_null_string_token.13694
+ _objc_msgSend$denoiseStrengthMaskTexture
+ _objc_msgSend$denoiseStrengthMaskTextureFormat
+ _objc_msgSend$denoiseStrengthMaskTextureUsage
+ _objc_msgSend$diffuseAlbedoTexture
+ _objc_msgSend$diffuseAlbedoTextureFormat
+ _objc_msgSend$diffuseAlbedoTextureUsage
+ _objc_msgSend$initWithDevice:descriptor:
+ _objc_msgSend$normalTexture
+ _objc_msgSend$normalTextureFormat
+ _objc_msgSend$normalTextureUsage
+ _objc_msgSend$roughnessTexture
+ _objc_msgSend$roughnessTextureFormat
+ _objc_msgSend$roughnessTextureUsage
+ _objc_msgSend$setAddress:attributeStride:atIndex:
+ _objc_msgSend$setFilenameOverrides:
+ _objc_msgSend$setHeapExtractedTextures:
+ _objc_msgSend$setHeapTextureRestoreOverrides:
+ _objc_msgSend$setMaxMeshBufferBindCount:
+ _objc_msgSend$setMaxObjectBufferBindCount:
+ _objc_msgSend$setMaxObjectThreadgroupMemoryBindCount:
+ _objc_msgSend$setRequiresLegacyCompilerProcessesCount:
+ _objc_msgSend$setReverseAliasMap:
+ _objc_msgSend$shouldResetHistory
+ _objc_msgSend$specularAlbedoTexture
+ _objc_msgSend$specularAlbedoTextureFormat
+ _objc_msgSend$specularAlbedoTextureUsage
+ _objc_msgSend$specularHitDistanceTexture
+ _objc_msgSend$specularHitDistanceTextureFormat
+ _objc_msgSend$specularHitDistanceTextureUsage
+ _objc_msgSend$transparencyOverlayTexture
+ _objc_msgSend$transparencyOverlayTextureFormat
+ _objc_msgSend$transparencyOverlayTextureUsage
+ _objc_msgSend$viewToClipMatrix
+ _objc_msgSend$worldToViewMatrix
+ _objc_msgSend$wrapperWithDevice:descriptor:
- -[GTMTLReplayTemporalScaler .cxx_destruct]
- -[GTMTLReplayTemporalScaler colorTextureFormat]
- -[GTMTLReplayTemporalScaler colorTextureUsage]
- -[GTMTLReplayTemporalScaler colorTexture]
- -[GTMTLReplayTemporalScaler currentViewToClipMatrix]
- -[GTMTLReplayTemporalScaler currentWorldToViewMatrix]
- -[GTMTLReplayTemporalScaler debugTexture]
- -[GTMTLReplayTemporalScaler depthTextureFormat]
- -[GTMTLReplayTemporalScaler depthTextureUsage]
- -[GTMTLReplayTemporalScaler depthTexture]
- -[GTMTLReplayTemporalScaler dilatedMotionVectors]
- -[GTMTLReplayTemporalScaler effectID]
- -[GTMTLReplayTemporalScaler encodeToCommandBuffer:]
- -[GTMTLReplayTemporalScaler encodeToCommandQueue:]
- -[GTMTLReplayTemporalScaler executionMode]
- -[GTMTLReplayTemporalScaler exposureTexture]
- -[GTMTLReplayTemporalScaler fence]
- -[GTMTLReplayTemporalScaler forwardingTargetForSelector:]
- -[GTMTLReplayTemporalScaler initWithGPUScaler:ANEScaler:executionMode:]
- -[GTMTLReplayTemporalScaler inputContentHeight]
- -[GTMTLReplayTemporalScaler inputContentMaxScale]
- -[GTMTLReplayTemporalScaler inputContentMinScale]
- -[GTMTLReplayTemporalScaler inputContentWidth]
- -[GTMTLReplayTemporalScaler inputHeight]
- -[GTMTLReplayTemporalScaler inputWidth]
- -[GTMTLReplayTemporalScaler isDepthReversed]
- -[GTMTLReplayTemporalScaler jitterOffsetX]
- -[GTMTLReplayTemporalScaler jitterOffsetY]
- -[GTMTLReplayTemporalScaler motionTextureFormat]
- -[GTMTLReplayTemporalScaler motionTextureUsage]
- -[GTMTLReplayTemporalScaler motionTexture]
- -[GTMTLReplayTemporalScaler motionVectorScaleX]
- -[GTMTLReplayTemporalScaler motionVectorScaleY]
- -[GTMTLReplayTemporalScaler outputHeight]
- -[GTMTLReplayTemporalScaler outputTextureFormat]
- -[GTMTLReplayTemporalScaler outputTextureUsage]
- -[GTMTLReplayTemporalScaler outputTexture]
- -[GTMTLReplayTemporalScaler outputWidth]
- -[GTMTLReplayTemporalScaler preExposure]
- -[GTMTLReplayTemporalScaler previousJitterOffset]
- -[GTMTLReplayTemporalScaler previousViewToClipMatrix]
- -[GTMTLReplayTemporalScaler previousWorldToViewMatrix]
- -[GTMTLReplayTemporalScaler reactiveMaskTextureFormat]
- -[GTMTLReplayTemporalScaler reactiveMaskTexture]
- -[GTMTLReplayTemporalScaler reactiveTextureUsage]
- -[GTMTLReplayTemporalScaler reset]
- -[GTMTLReplayTemporalScaler setColorTexture:]
- -[GTMTLReplayTemporalScaler setCurrentViewToClipMatrix:]
- -[GTMTLReplayTemporalScaler setCurrentWorldToViewMatrix:]
- -[GTMTLReplayTemporalScaler setDebugTexture:]
- -[GTMTLReplayTemporalScaler setDepthReversed:]
- -[GTMTLReplayTemporalScaler setDepthTexture:]
- -[GTMTLReplayTemporalScaler setExecutionMode:]
- -[GTMTLReplayTemporalScaler setExposureTexture:]
- -[GTMTLReplayTemporalScaler setFence:]
- -[GTMTLReplayTemporalScaler setInputContentHeight:]
- -[GTMTLReplayTemporalScaler setInputContentWidth:]
- -[GTMTLReplayTemporalScaler setJitterOffsetX:]
- -[GTMTLReplayTemporalScaler setJitterOffsetY:]
- -[GTMTLReplayTemporalScaler setMotionTexture:]
- -[GTMTLReplayTemporalScaler setMotionVectorScaleX:]
- -[GTMTLReplayTemporalScaler setMotionVectorScaleY:]
- -[GTMTLReplayTemporalScaler setOutputTexture:]
- -[GTMTLReplayTemporalScaler setPreExposure:]
- -[GTMTLReplayTemporalScaler setPreviousJitterOffset:]
- -[GTMTLReplayTemporalScaler setPreviousViewToClipMatrix:]
- -[GTMTLReplayTemporalScaler setPreviousWorldToViewMatrix:]
- -[GTMTLReplayTemporalScaler setReactiveMaskTexture:]
- -[GTMTLReplayTemporalScaler setReset:]
- -[GTMTLReplayTemporalScaler setTracingDelegate:]
- -[GTMTLReplayTemporalScaler tracingDelegate]
- GCC_except_table1007
- GCC_except_table1008
- GCC_except_table1012
- GCC_except_table1013
- GCC_except_table1014
- GCC_except_table1015
- GCC_except_table1016
- GCC_except_table1017
- GCC_except_table1018
- GCC_except_table1019
- GCC_except_table1020
- GCC_except_table1021
- GCC_except_table1026
- GCC_except_table1042
- GCC_except_table1055
- GCC_except_table1059
- GCC_except_table1131
- GCC_except_table1244
- GCC_except_table1266
- GCC_except_table1267
- GCC_except_table1322
- GCC_except_table1347
- GCC_except_table135
- GCC_except_table137
- GCC_except_table1378
- GCC_except_table1379
- GCC_except_table138
- GCC_except_table1382
- GCC_except_table1383
- GCC_except_table1384
- GCC_except_table1385
- GCC_except_table1386
- GCC_except_table1387
- GCC_except_table1389
- GCC_except_table139
- GCC_except_table140
- GCC_except_table1400
- GCC_except_table1402
- GCC_except_table1404
- GCC_except_table1406
- GCC_except_table1416
- GCC_except_table145
- GCC_except_table152
- GCC_except_table1526
- GCC_except_table1527
- GCC_except_table1528
- GCC_except_table1529
- GCC_except_table153
- GCC_except_table1530
- GCC_except_table1531
- GCC_except_table1536
- GCC_except_table1537
- GCC_except_table154
- GCC_except_table1541
- GCC_except_table1555
- GCC_except_table1556
- GCC_except_table1558
- GCC_except_table1559
- GCC_except_table156
- GCC_except_table1561
- GCC_except_table1571
- GCC_except_table1601
- GCC_except_table1618
- GCC_except_table1619
- GCC_except_table1620
- GCC_except_table1621
- GCC_except_table1622
- GCC_except_table1623
- GCC_except_table1626
- GCC_except_table168
- GCC_except_table1699
- GCC_except_table1702
- GCC_except_table1721
- GCC_except_table1736
- GCC_except_table1737
- GCC_except_table1738
- GCC_except_table1739
- GCC_except_table1740
- GCC_except_table1745
- GCC_except_table1747
- GCC_except_table1748
- GCC_except_table1759
- GCC_except_table1760
- GCC_except_table1762
- GCC_except_table1763
- GCC_except_table1764
- GCC_except_table1766
- GCC_except_table1773
- GCC_except_table1775
- GCC_except_table179
- GCC_except_table1811
- GCC_except_table1813
- GCC_except_table1814
- GCC_except_table1815
- GCC_except_table1816
- GCC_except_table1817
- GCC_except_table1825
- GCC_except_table1847
- GCC_except_table1850
- GCC_except_table1869
- GCC_except_table1871
- GCC_except_table1876
- GCC_except_table1879
- GCC_except_table1886
- GCC_except_table1888
- GCC_except_table1889
- GCC_except_table1890
- GCC_except_table1893
- GCC_except_table1894
- GCC_except_table1899
- GCC_except_table190
- GCC_except_table1906
- GCC_except_table1907
- GCC_except_table1908
- GCC_except_table191
- GCC_except_table1910
- GCC_except_table1916
- GCC_except_table1917
- GCC_except_table1918
- GCC_except_table1919
- GCC_except_table1920
- GCC_except_table1921
- GCC_except_table1922
- GCC_except_table1925
- GCC_except_table1931
- GCC_except_table1932
- GCC_except_table1933
- GCC_except_table1934
- GCC_except_table1935
- GCC_except_table1936
- GCC_except_table1942
- GCC_except_table1943
- GCC_except_table1948
- GCC_except_table1950
- GCC_except_table1953
- GCC_except_table1955
- GCC_except_table1959
- GCC_except_table196
- GCC_except_table1960
- GCC_except_table1961
- GCC_except_table1962
- GCC_except_table1964
- GCC_except_table1967
- GCC_except_table1969
- GCC_except_table197
- GCC_except_table1970
- GCC_except_table1971
- GCC_except_table207
- GCC_except_table215
- GCC_except_table217
- GCC_except_table218
- GCC_except_table219
- GCC_except_table225
- GCC_except_table232
- GCC_except_table239
- GCC_except_table2403
- GCC_except_table2409
- GCC_except_table2427
- GCC_except_table2434
- GCC_except_table2498
- GCC_except_table2506
- GCC_except_table2508
- GCC_except_table2534
- GCC_except_table2541
- GCC_except_table2543
- GCC_except_table2545
- GCC_except_table2547
- GCC_except_table2548
- GCC_except_table2550
- GCC_except_table2551
- GCC_except_table2552
- GCC_except_table2553
- GCC_except_table2554
- GCC_except_table2556
- GCC_except_table2567
- GCC_except_table2570
- GCC_except_table2573
- GCC_except_table2580
- GCC_except_table2583
- GCC_except_table2592
- GCC_except_table2596
- GCC_except_table2600
- GCC_except_table261
- GCC_except_table2610
- GCC_except_table2614
- GCC_except_table2628
- GCC_except_table2629
- GCC_except_table2648
- GCC_except_table266
- GCC_except_table267
- GCC_except_table2671
- GCC_except_table2679
- GCC_except_table2680
- GCC_except_table2682
- GCC_except_table2683
- GCC_except_table2684
- GCC_except_table2705
- GCC_except_table2706
- GCC_except_table2708
- GCC_except_table2709
- GCC_except_table271
- GCC_except_table2710
- GCC_except_table2720
- GCC_except_table2752
- GCC_except_table2755
- GCC_except_table2756
- GCC_except_table2757
- GCC_except_table2758
- GCC_except_table2759
- GCC_except_table2760
- GCC_except_table2765
- GCC_except_table2769
- GCC_except_table2774
- GCC_except_table2779
- GCC_except_table2810
- GCC_except_table2901
- GCC_except_table298
- GCC_except_table313
- GCC_except_table315
- GCC_except_table322
- GCC_except_table342
- GCC_except_table349
- GCC_except_table390
- GCC_except_table391
- GCC_except_table395
- GCC_except_table397
- GCC_except_table398
- GCC_except_table400
- GCC_except_table402
- GCC_except_table406
- GCC_except_table407
- GCC_except_table408
- GCC_except_table409
- GCC_except_table410
- GCC_except_table411
- GCC_except_table416
- GCC_except_table418
- GCC_except_table419
- GCC_except_table420
- GCC_except_table424
- GCC_except_table427
- GCC_except_table428
- GCC_except_table436
- GCC_except_table437
- GCC_except_table440
- GCC_except_table444
- GCC_except_table447
- GCC_except_table451
- GCC_except_table452
- GCC_except_table455
- GCC_except_table457
- GCC_except_table475
- GCC_except_table483
- GCC_except_table491
- GCC_except_table492
- GCC_except_table493
- GCC_except_table496
- GCC_except_table504
- GCC_except_table505
- GCC_except_table514
- GCC_except_table515
- GCC_except_table517
- GCC_except_table518
- GCC_except_table520
- GCC_except_table527
- GCC_except_table528
- GCC_except_table531
- GCC_except_table533
- GCC_except_table535
- GCC_except_table537
- GCC_except_table539
- GCC_except_table550
- GCC_except_table551
- GCC_except_table552
- GCC_except_table556
- GCC_except_table563
- GCC_except_table565
- GCC_except_table576
- GCC_except_table577
- GCC_except_table578
- GCC_except_table585
- GCC_except_table586
- GCC_except_table590
- GCC_except_table603
- GCC_except_table605
- GCC_except_table607
- GCC_except_table617
- GCC_except_table618
- GCC_except_table620
- GCC_except_table622
- GCC_except_table623
- GCC_except_table625
- GCC_except_table626
- GCC_except_table627
- GCC_except_table629
- GCC_except_table631
- GCC_except_table632
- GCC_except_table634
- GCC_except_table638
- GCC_except_table645
- GCC_except_table646
- GCC_except_table661
- GCC_except_table818
- GCC_except_table820
- GCC_except_table821
- GCC_except_table824
- GCC_except_table832
- GCC_except_table833
- GCC_except_table839
- GCC_except_table845
- GCC_except_table858
- GCC_except_table866
- GCC_except_table867
- GCC_except_table868
- GCC_except_table869
- GCC_except_table874
- GCC_except_table875
- GCC_except_table879
- GCC_except_table883
- GCC_except_table884
- GCC_except_table885
- GCC_except_table897
- GCC_except_table901
- GCC_except_table902
- GCC_except_table903
- GCC_except_table904
- GCC_except_table905
- GCC_except_table908
- GCC_except_table909
- GCC_except_table914
- GCC_except_table915
- GCC_except_table921
- GCC_except_table922
- GCC_except_table924
- GCC_except_table926
- GCC_except_table927
- GCC_except_table928
- GCC_except_table929
- GCC_except_table930
- GCC_except_table931
- GCC_except_table932
- GCC_except_table934
- GCC_except_table937
- GCC_except_table938
- GCC_except_table942
- GCC_except_table949
- GCC_except_table950
- GCC_except_table951
- GCC_except_table952
- GCC_except_table954
- GCC_except_table955
- GCC_except_table956
- GCC_except_table957
- GCC_except_table959
- GCC_except_table963
- GCC_except_table977
- GCC_except_table979
- GCC_except_table980
- GCC_except_table981
- GCC_except_table983
- GCC_except_table986
- GCC_except_table989
- GCC_except_table994
- _AppendString.13431
- _CleanupSandboxExtensionURL.769
- _GetStream.13066
- _GetStream.13127
- _GroupBuilder_getCommandEncoder.5014
- _LastStream
- _MakeMTLLogicalToPhysicalColorAttachmentMapSPI
- _NewCommandBuffer.5477
- _OBJC_CLASS_$_GTMTLReplayTemporalScaler
- _OBJC_CLASS_$_MTLLogicalToPhysicalColorAttachmentMapSPI
- _OBJC_IVAR_$_GTMTLReplayTemporalScaler._aneScaler
- _OBJC_IVAR_$_GTMTLReplayTemporalScaler._effectID
- _OBJC_IVAR_$_GTMTLReplayTemporalScaler._executionMode
- _OBJC_IVAR_$_GTMTLReplayTemporalScaler._gpuScaler
- _OBJC_METACLASS_$_GTMTLReplayTemporalScaler
- _OpenEncoderStream
- __OBJC_$_INSTANCE_METHODS_GTMTLReplayTemporalScaler
- __OBJC_$_INSTANCE_VARIABLES_GTMTLReplayTemporalScaler
- __OBJC_$_PROP_LIST_GTMTLReplayTemporalScaler
- __OBJC_CLASS_PROTOCOLS_$_GTMTLReplayTemporalScaler
- __OBJC_CLASS_RO_$_GTMTLReplayTemporalScaler
- __OBJC_METACLASS_RO_$_GTMTLReplayTemporalScaler
- __ZL16DispatchFunctionP21GTMTLReplayControllerPK11GTTraceFuncRb.1247
- __ZL23GetRenderPassDescriptorPK11GTTraceFuncP10apr_hash_t.1248
- __ZL31DisableComputeEncoderCoalescingP21GTMTLReplayControllerb.1196
- ___Block_byref_object_copy_.1401
- ___Block_byref_object_copy_.1745
- ___Block_byref_object_copy_.367
- ___Block_byref_object_copy_.5660
- ___Block_byref_object_copy_.6969
- ___Block_byref_object_copy_.711
- ___Block_byref_object_copy_.8965
- ___Block_byref_object_copy_.9582
- ___Block_byref_object_copy_.9614
- ___Block_byref_object_dispose_.1402
- ___Block_byref_object_dispose_.1746
- ___Block_byref_object_dispose_.368
- ___Block_byref_object_dispose_.5661
- ___Block_byref_object_dispose_.6970
- ___Block_byref_object_dispose_.712
- ___Block_byref_object_dispose_.8966
- ___Block_byref_object_dispose_.9583
- ___Block_byref_object_dispose_.9615
- ___block_literal_global.104
- ___block_literal_global.10586
- ___block_literal_global.106
- ___block_literal_global.10674
- ___block_literal_global.11147
- ___block_literal_global.1356
- ___block_literal_global.1461
- ___block_literal_global.1598
- ___block_literal_global.2325
- ___block_literal_global.2458
- ___block_literal_global.2761
- ___block_literal_global.2836
- ___block_literal_global.4174
- ___block_literal_global.46
- ___block_literal_global.5226
- ___block_literal_global.5707
- ___block_literal_global.608
- ___block_literal_global.6141
- ___block_literal_global.6505
- ___block_literal_global.6527
- ___block_literal_global.6686
- ___block_literal_global.7344
- ___block_literal_global.839
- ___block_literal_global.94
- _agxps_gpu_variant_to_string
- _g_null_string_token.13432
- _objc_msgSend$initWithGPUScaler:ANEScaler:executionMode:
CStrings:
+ "%s:%u: WARNING: Could not find matching GPU revision. Falling back to an earlier revision because agxps_gpu_flags_allow_aps_revision_fallback was specified"
+ "@\"<MTLFXTemporalDenoisedScaler>\"8@?0"
+ "@\"<MTLFXTemporalScaler>\"8@?0"
+ "GTReplayMTLFXTemporalDenoisedScaler"
+ "GTReplayMTLFXTemporalScaler"
+ "GTReplayWrapperBase"
+ "MTLFXTemporalDenoisedScalerBase"
+ "MTLFXTemporalDenoisedScalerSPI"
+ "Original = %@, Override = %@, Tool version = %llu"
+ "Platform = %@, RIA Gen = %@"
+ "Slice = %lu, Mip level = %lu, Depth plane = %lu, Plane = %@"
+ "TextureBytesReadCompressedFromMainMemory"
+ "TextureBytesReadCompressedFromMainMemory description"
+ "ZAndTextureBytesUncompressedaReadFromMainMemory"
+ "ZTextureBytesCompressedReadFromMainMemory"
+ "_0d052856f8b7f1e2923c0833d57ea7d305e75bc097c55b4219a61201fcbf7d41"
+ "_0d2a03e2e74b0f1a2cd14c6d1aa1aa8030bf42edf16b18ef835ea7d0c4af3e19"
+ "_1137ef97a3cec2b87836ea53883fa98f7d35030d603bf1b63eef7e97de636715"
+ "_1cd7690f501bce6e82955d3fe3998ec804d1ef190da99c215acb31403f8979a2"
+ "_28a0d838a6a5e0be5091f96529779170e8be3bb0a616c5ee059f274f06ee0ae0"
+ "_2dfce7695dda0e0fca2e4efa85dd03dc0116f75756e519fb4849ee1da035acd3"
+ "_2f8eb09a92ac04686362dc932194463ac494ba9fa0a11d8278430da839c9dfe0"
+ "_354160ae671773aeaa31cf66534b089488a9d3b35daa36be8163e0d619ececc6"
+ "_3dfdf82f1c79b4a58513a034cbbc768843b7dac7d7a329682b6db0b750f02858"
+ "_3e75681c068835f1630f1e61584ef847028448c4e11651b89c4cfffd3131d08e"
+ "_470fad2e0fc12bb26ac7ad41f1089d912d4c74ed3c9f47913968e35d78a207da"
+ "_47a391fcd4cf212c3ced5df81581c29087d65e1ca3b76041e5fd28d83947005b"
+ "_525e6837d3d004074e798545e71230b5b87df7663463cac26bfa239463302b99"
+ "_576f1719d6e566883126e3d61afc134679e2d5af746394443adeaf33ff0ee696"
+ "_5c4d54ef3a16fcc9724b00a57a766bd25a5069bb631deda9563a30a5a36d25ba"
+ "_5d8752d21b3c837462d336a319b139824f311944421036cda71193f3181d0f76"
+ "_5decb725dba9715f86df169e04e39409e88cf34fc279b90c0ab0a929d4af8c65"
+ "_68eee53849ad570efe2789714b398f4f2aec1f739867b73b34a1ee930b25c6d2"
+ "_6b12cf25531e582ee88d8f9759e526f16a43a3a11332ec45888e1910006705ba"
+ "_6b142fabf80e03ad694ac6373c432f4158f351a6b5b07e8c919581bfa9f74725"
+ "_7248586b9d9e3e05a15775f0b4dc2e311266c4458d0fc358e724ed4179def848"
+ "_7578245048476e55c80c50d2f395352b5d6408a598786a7db8a3ab4ba092a748"
+ "_84ed11582ed945abeaf0c547d465faa8dec84ced5b70a6d013d4cc04a98d351a"
+ "_86cbb5e815198306f885ae8966758c213178f734b4b5969c1ee0a65ef628fd86"
+ "_907395c09cc0738417992172a118f18e211c4e31604b7cfa627a4299e8193ab0"
+ "_94b244c3fdf54affbfe4a26e17e562252e31ddb3340272290815727e620c033c"
+ "_a0cfeb45fbd689763e1e48f05633f3c83b72fc80cdb2518fc52e176d7eef5fcb"
+ "_a110e9914d1de833f8eb90a5e638cafcdd727e4794c1f26af7b65921e5a63867"
+ "_a337144934e84750987913c781c7581640c7f750af9abf407e60453f1bb13c20"
+ "_a5bee0d2a278e80f002ff94b10cd259008565079b77fd084e6d1eea0192d0269"
+ "_a60e51c3412b9e7d1d2fadea6422a0527f35626e75d98d31fd6614f1f575afe4"
+ "_acce06635a6ad56f3772d604f60d24ba07eefd59b8decbf6d8110f0731150009"
+ "_acdabf3d1a7bc585e8fe8efd383ce684e79df3341df4c3e358b125dfea901a50"
+ "_b209dcf8e2830ee1f19d59047f4710ce2224745d55bb75b3eaad5e701644aa0a"
+ "_b9a26adf6863da7bf6981ba1945e72472b5b428286b1a57961f3055e5a62b172"
+ "_bdc443d1b90953c048630dc293ccc4b1cb090f90b30ce7e000b005e5fc927a84"
+ "_bf16c8266844cd8dcb42338abfcf14c661cc38b51f17ea88948cf152e9884578"
+ "_c0fddd8a9428afe6678ff9a9f7b5cae61346ac8f19f00c2e86e549e272b201fb"
+ "_c212438221a1770ca4044339ce776d8934005885917f6f2d0002883299788881"
+ "_c35059b308ea6ce17f9696ae98c6c20c4bb855730e58d6229c80ea888ee1df0e"
+ "_c483efb3110f4d191986b31534a192dd2e089037244dd1ca09a249ad35210f83"
+ "_c660e9fd8c4bac562c5fc61fe2d5fa6288bc1300bdc37921468676e86fbfb4d8"
+ "_c9fdaa68d636601dc5a6c2f4f768df3b9687cce02b45e270d78f6e53850cbd4b"
+ "_cab63dc46bde0cb1eb7d614c0706aaa6cbf0970bd58451f7d77daf30479eb22e"
+ "_cb5103117d69dbbbe1994ac9aac6ea60e3fa8e692f9b6dcd3ecdb1e0243b8f7c"
+ "_cddfe5acb18962cd2de7ebff0a9b2b736f787e61a9083d00d306b0e164a1c435"
+ "_cf18cbffa2404d9a5c38446f1117768eb24d2cd43a741d5e0b8da91d768e39b2"
+ "_d7c3bf2e23158c12ae08b92b6cee2ae8ff53b890b1cec9f531c6fc7327525997"
+ "_da01c1481b1f0f16b8ac4addba5b41c1c8fcc9caf8522b8410f966af02ddf6a6"
+ "_e9257b2bf1aa968f73328efa48d9a05e8bf1cf337e7e039a01b5986c5bcbe2d7"
+ "_ec2e343ce0abe20314003df42c80d60bda92ac939a275814a6c22e79865148ea"
+ "_ef2f8e4bebd7da952ddb8c07b077af12ef71ade6bd97713366ac0a439a22f90f"
+ "_f36dadd175dfbd1e5aeef21d1c4cad59c66695545b020160f89942aaf3bd2bf2"
+ "_fa13af69162fb6187e78b7531f36b39f6b98cfab065fa45dcb5128fbf2408065"
+ "denoiseStrengthMaskTexture"
+ "denoiseStrengthMaskTextureUsage"
+ "diffuseAlbedoTexture"
+ "diffuseAlbedoTextureFormat"
+ "diffuseAlbedoTextureUsage"
+ "drawableStream != ((void*)0)"
+ "initWithDevice:descriptor:"
+ "kDYFEMTL4CommandBuffer_resolveCounterHeap_withRange_intoBuffer_waitFence_updateFence"
+ "kDYFEMTLCommandBuffer___waitUntilCompletedAsync"
+ "kDYFEMTLCommandBuffer___waitUntilScheduledAsync"
+ "kDYFEMTLDevice_defaultCompilerProcessesCount"
+ "kDYFEMTLDevice_maximumCompilerProcessesCount"
+ "kDYFEMTLDevice_setRequiresLegacyCompilerProcessesCount"
+ "kDYFEMTLDevice_threadsPerCompilerProcess"
+ "kDYFEMTLFXTemporalDenoisedScaler_executionMode"
+ "maxMeshBufferBindCount"
+ "maxObjectBufferBindCount"
+ "maxObjectThreadgroupMemoryBindCount"
+ "memcmp((const char*)bytes + offset, (\"Cuwulul\"), sizeof(\"Cuwulul\")) == 0"
+ "normalTexture"
+ "normalTextureFormat"
+ "normalTextureUsage"
+ "roughnessTexture"
+ "roughnessTextureFormat"
+ "roughnessTextureUsage"
+ "setAddress:attributeStride:atIndex:"
+ "setMaxMeshBufferBindCount:"
+ "setMaxObjectBufferBindCount:"
+ "setMaxObjectThreadgroupMemoryBindCount:"
+ "setRequiresLegacyCompilerProcessesCount:"
+ "shouldResetHistory"
+ "specularAlbedoTexture"
+ "specularAlbedoTextureFormat"
+ "specularAlbedoTextureUsage"
+ "specularHitDistanceTexture"
+ "specularHitDistanceTextureUsage"
+ "supportMTLEvent"
+ "transparencyOverlayTexture"
+ "transparencyOverlayTextureUsage"
+ "viewToClipMatrix"
+ "worldToViewMatrix"
+ "wrapperWithDevice:descriptor:"
- "%s:%u: WARNING: %s falling back to revision %s for GPU %s%s %s because agxps_gpu_flags_allow_aps_revision_fallback was specified"
- "@\"<MTLFXTemporalScalerSPI>\""
- "@36@0:8@16@24C32"
- "GTMTLReplayTemporalScaler"
- "agxps_gpu_create"
- "deviceObject == 0 || object != NULL"
- "initWithGPUScaler:ANEScaler:executionMode:"

```
