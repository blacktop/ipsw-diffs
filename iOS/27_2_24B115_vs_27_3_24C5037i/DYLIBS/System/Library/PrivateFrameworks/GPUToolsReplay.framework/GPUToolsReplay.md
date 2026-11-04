## GPUToolsReplay

> `/System/Library/PrivateFrameworks/GPUToolsReplay.framework/GPUToolsReplay`

```diff

-2027.1.3.0.0
-  __TEXT.__text: 0x416e40
+2027.2.4.0.0
+  __TEXT.__text: 0x41b034
   __TEXT.__init_offsets: 0x10
-  __TEXT.__objc_methlist: 0x7cbc
-  __TEXT.__const: 0xa560
-  __TEXT.__oslogstring: 0x184f
-  __TEXT.__cstring: 0x10df32
-  __TEXT.__gcc_except_tab: 0x16a9c
+  __TEXT.__objc_methlist: 0x7bcc
+  __TEXT.__const: 0xa610
+  __TEXT.__oslogstring: 0x1884
+  __TEXT.__cstring: 0x10e1ff
+  __TEXT.__gcc_except_tab: 0x173d4
   __TEXT.__ustring: 0x4f6
-  __TEXT.__unwind_info: 0x7818
+  __TEXT.__unwind_info: 0x77b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x33deb0
-  __DATA_CONST.__objc_classlist: 0x298
+  __DATA_CONST.__const: 0x33de70
+  __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x190
+  __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68a0
+  __DATA_CONST.__objc_selrefs: 0x6970
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x270
+  __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0xba0
-  __DATA_CONST.__got: 0x980
+  __DATA_CONST.__got: 0x990
   __AUTH_CONST.__const: 0x1a48
-  __AUTH_CONST.__cfstring: 0xf940
-  __AUTH_CONST.__objc_const: 0xbff8
+  __AUTH_CONST.__cfstring: 0xfa40
+  __AUTH_CONST.__objc_const: 0xbf78
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__objc_intobj: 0x720
+  __AUTH_CONST.__objc_intobj: 0x738
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0x820
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xe70
-  __AUTH.__objc_data: 0x19f0
+  __AUTH_CONST.__auth_got: 0xe78
+  __AUTH.__objc_data: 0x19a0
   __AUTH.__thread_vars: 0x78
   __AUTH.__thread_bss: 0x1088
-  __DATA.__objc_ivar: 0x798
-  __DATA.__data: 0x25a8
+  __DATA.__objc_ivar: 0x79c
+  __DATA.__data: 0x2548
   __DATA.__common: 0x51
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 7381
-  Symbols:   9303
-  CStrings:  18408
+  Functions: 7326
+  Symbols:   9240
+  CStrings:  18424
 
Symbols:
+ +[GTReplayMTLFXFrameInterpolator wrapperWithDevice:descriptor:]
+ -[GTMTLReplayObjectMap mtl4CounterHeapForKey:]
+ -[GTMTLReplayObjectMap removeMTL4CounterHeapForKey:]
+ -[GTMTLReplayObjectMap setMTL4CounterHeap:forKey:]
+ -[GTMTLReplaySharedBufferRange scalesPlaneTensorAlias:dataPlaneOffset:]
+ -[GTReplayMTLFXFrameInterpolator aspectRatio]
+ -[GTReplayMTLFXFrameInterpolator colorTextureFormat]
+ -[GTReplayMTLFXFrameInterpolator colorTextureUsage]
+ -[GTReplayMTLFXFrameInterpolator colorTexture]
+ -[GTReplayMTLFXFrameInterpolator compositedUITexture]
+ -[GTReplayMTLFXFrameInterpolator contentHeight]
+ -[GTReplayMTLFXFrameInterpolator contentWidth]
+ -[GTReplayMTLFXFrameInterpolator debugTexture]
+ -[GTReplayMTLFXFrameInterpolator deltaTime]
+ -[GTReplayMTLFXFrameInterpolator depthContentOffsetX]
+ -[GTReplayMTLFXFrameInterpolator depthContentOffsetY]
+ -[GTReplayMTLFXFrameInterpolator depthTextureFormat]
+ -[GTReplayMTLFXFrameInterpolator depthTextureUsage]
+ -[GTReplayMTLFXFrameInterpolator depthTexture]
+ -[GTReplayMTLFXFrameInterpolator distortionHeight]
+ -[GTReplayMTLFXFrameInterpolator distortionOffsetX]
+ -[GTReplayMTLFXFrameInterpolator distortionOffsetY]
+ -[GTReplayMTLFXFrameInterpolator distortionTexture]
+ -[GTReplayMTLFXFrameInterpolator distortionWidth]
+ -[GTReplayMTLFXFrameInterpolator encodeToCommandBuffer:]
+ -[GTReplayMTLFXFrameInterpolator encodeToCommandQueue:]
+ -[GTReplayMTLFXFrameInterpolator farPlane]
+ -[GTReplayMTLFXFrameInterpolator fence]
+ -[GTReplayMTLFXFrameInterpolator fieldOfView]
+ -[GTReplayMTLFXFrameInterpolator height]
+ -[GTReplayMTLFXFrameInterpolator initWithDevice:descriptor:]
+ -[GTReplayMTLFXFrameInterpolator inputHeight]
+ -[GTReplayMTLFXFrameInterpolator inputWidth]
+ -[GTReplayMTLFXFrameInterpolator isDepthReversed]
+ -[GTReplayMTLFXFrameInterpolator isUITextureComposited]
+ -[GTReplayMTLFXFrameInterpolator jitterOffsetX]
+ -[GTReplayMTLFXFrameInterpolator jitterOffsetY]
+ -[GTReplayMTLFXFrameInterpolator motionContentOffsetX]
+ -[GTReplayMTLFXFrameInterpolator motionContentOffsetY]
+ -[GTReplayMTLFXFrameInterpolator motionTextureFormat]
+ -[GTReplayMTLFXFrameInterpolator motionTextureUsage]
+ -[GTReplayMTLFXFrameInterpolator motionTexture]
+ -[GTReplayMTLFXFrameInterpolator motionVectorScaleX]
+ -[GTReplayMTLFXFrameInterpolator motionVectorScaleY]
+ -[GTReplayMTLFXFrameInterpolator nearPlane]
+ -[GTReplayMTLFXFrameInterpolator outputHeight]
+ -[GTReplayMTLFXFrameInterpolator outputOffsetX]
+ -[GTReplayMTLFXFrameInterpolator outputOffsetY]
+ -[GTReplayMTLFXFrameInterpolator outputTextureFormat]
+ -[GTReplayMTLFXFrameInterpolator outputTextureUsage]
+ -[GTReplayMTLFXFrameInterpolator outputTexture]
+ -[GTReplayMTLFXFrameInterpolator outputWidth]
+ -[GTReplayMTLFXFrameInterpolator prevColorTexture]
+ -[GTReplayMTLFXFrameInterpolator reset]
+ -[GTReplayMTLFXFrameInterpolator setAspectRatio:]
+ -[GTReplayMTLFXFrameInterpolator setColorTexture:]
+ -[GTReplayMTLFXFrameInterpolator setCompositedUITexture:]
+ -[GTReplayMTLFXFrameInterpolator setContentHeight:]
+ -[GTReplayMTLFXFrameInterpolator setContentWidth:]
+ -[GTReplayMTLFXFrameInterpolator setDebugTexture:]
+ -[GTReplayMTLFXFrameInterpolator setDeltaTime:]
+ -[GTReplayMTLFXFrameInterpolator setDepthContentOffsetX:]
+ -[GTReplayMTLFXFrameInterpolator setDepthContentOffsetY:]
+ -[GTReplayMTLFXFrameInterpolator setDepthReversed:]
+ -[GTReplayMTLFXFrameInterpolator setDepthTexture:]
+ -[GTReplayMTLFXFrameInterpolator setDistortionHeight:]
+ -[GTReplayMTLFXFrameInterpolator setDistortionOffsetX:]
+ -[GTReplayMTLFXFrameInterpolator setDistortionOffsetY:]
+ -[GTReplayMTLFXFrameInterpolator setDistortionTexture:]
+ -[GTReplayMTLFXFrameInterpolator setDistortionWidth:]
+ -[GTReplayMTLFXFrameInterpolator setFarPlane:]
+ -[GTReplayMTLFXFrameInterpolator setFence:]
+ -[GTReplayMTLFXFrameInterpolator setFieldOfView:]
+ -[GTReplayMTLFXFrameInterpolator setHeight:]
+ -[GTReplayMTLFXFrameInterpolator setIsUITextureComposited:]
+ -[GTReplayMTLFXFrameInterpolator setJitterOffsetX:]
+ -[GTReplayMTLFXFrameInterpolator setJitterOffsetY:]
+ -[GTReplayMTLFXFrameInterpolator setMotionContentOffsetX:]
+ -[GTReplayMTLFXFrameInterpolator setMotionContentOffsetY:]
+ -[GTReplayMTLFXFrameInterpolator setMotionTexture:]
+ -[GTReplayMTLFXFrameInterpolator setMotionVectorScaleX:]
+ -[GTReplayMTLFXFrameInterpolator setMotionVectorScaleY:]
+ -[GTReplayMTLFXFrameInterpolator setNearPlane:]
+ -[GTReplayMTLFXFrameInterpolator setOutputOffsetX:]
+ -[GTReplayMTLFXFrameInterpolator setOutputOffsetY:]
+ -[GTReplayMTLFXFrameInterpolator setOutputTexture:]
+ -[GTReplayMTLFXFrameInterpolator setPrevColorTexture:]
+ -[GTReplayMTLFXFrameInterpolator setReset:]
+ -[GTReplayMTLFXFrameInterpolator setShouldResetHistory:]
+ -[GTReplayMTLFXFrameInterpolator setUITexture:]
+ -[GTReplayMTLFXFrameInterpolator setViewToClipMatrix:]
+ -[GTReplayMTLFXFrameInterpolator setWidth:]
+ -[GTReplayMTLFXFrameInterpolator setWorldToViewMatrix:]
+ -[GTReplayMTLFXFrameInterpolator shouldResetHistory]
+ -[GTReplayMTLFXFrameInterpolator uiTextureFormat]
+ -[GTReplayMTLFXFrameInterpolator uiTextureUsage]
+ -[GTReplayMTLFXFrameInterpolator uiTexture]
+ -[GTReplayMTLFXFrameInterpolator viewToClipMatrix]
+ -[GTReplayMTLFXFrameInterpolator width]
+ -[GTReplayMTLFXFrameInterpolator worldToViewMatrix]
+ GCC_except_table1000
+ GCC_except_table1001
+ GCC_except_table1156
+ GCC_except_table1159
+ GCC_except_table1162
+ GCC_except_table1164
+ GCC_except_table1189
+ GCC_except_table1191
+ GCC_except_table1192
+ GCC_except_table1195
+ GCC_except_table1204
+ GCC_except_table1210
+ GCC_except_table1216
+ GCC_except_table1229
+ GCC_except_table1237
+ GCC_except_table1238
+ GCC_except_table1239
+ GCC_except_table1240
+ GCC_except_table1246
+ GCC_except_table1254
+ GCC_except_table1255
+ GCC_except_table1256
+ GCC_except_table1268
+ GCC_except_table1273
+ GCC_except_table1278
+ GCC_except_table1279
+ GCC_except_table1281
+ GCC_except_table1284
+ GCC_except_table1285
+ GCC_except_table1290
+ GCC_except_table1291
+ GCC_except_table1297
+ GCC_except_table1298
+ GCC_except_table1300
+ GCC_except_table1302
+ GCC_except_table1303
+ GCC_except_table1304
+ GCC_except_table1305
+ GCC_except_table1306
+ GCC_except_table1307
+ GCC_except_table1308
+ GCC_except_table1310
+ GCC_except_table1315
+ GCC_except_table1319
+ GCC_except_table1327
+ GCC_except_table1328
+ GCC_except_table1329
+ GCC_except_table1332
+ GCC_except_table1333
+ GCC_except_table1334
+ GCC_except_table1337
+ GCC_except_table1356
+ GCC_except_table1359
+ GCC_except_table1360
+ GCC_except_table1361
+ GCC_except_table1368
+ GCC_except_table1374
+ GCC_except_table1394
+ GCC_except_table1396
+ GCC_except_table1397
+ GCC_except_table1398
+ GCC_except_table1401
+ GCC_except_table1406
+ GCC_except_table1435
+ GCC_except_table1452
+ GCC_except_table1460
+ GCC_except_table1524
+ GCC_except_table1637
+ GCC_except_table1659
+ GCC_except_table1660
+ GCC_except_table1715
+ GCC_except_table1740
+ GCC_except_table1771
+ GCC_except_table1772
+ GCC_except_table1773
+ GCC_except_table1774
+ GCC_except_table1775
+ GCC_except_table1776
+ GCC_except_table1777
+ GCC_except_table1778
+ GCC_except_table1780
+ GCC_except_table1792
+ GCC_except_table1794
+ GCC_except_table1796
+ GCC_except_table1798
+ GCC_except_table1809
+ GCC_except_table1836
+ GCC_except_table1837
+ GCC_except_table1838
+ GCC_except_table1841
+ GCC_except_table1843
+ GCC_except_table1949
+ GCC_except_table1952
+ GCC_except_table1954
+ GCC_except_table1955
+ GCC_except_table1956
+ GCC_except_table1957
+ GCC_except_table1962
+ GCC_except_table1963
+ GCC_except_table1967
+ GCC_except_table1973
+ GCC_except_table1974
+ GCC_except_table1975
+ GCC_except_table1976
+ GCC_except_table1978
+ GCC_except_table1980
+ GCC_except_table1981
+ GCC_except_table1982
+ GCC_except_table1983
+ GCC_except_table1985
+ GCC_except_table1990
+ GCC_except_table2027
+ GCC_except_table2049
+ GCC_except_table2050
+ GCC_except_table2051
+ GCC_except_table2053
+ GCC_except_table2054
+ GCC_except_table2057
+ GCC_except_table2125
+ GCC_except_table2140
+ GCC_except_table2141
+ GCC_except_table2163
+ GCC_except_table2164
+ GCC_except_table2182
+ GCC_except_table2183
+ GCC_except_table2184
+ GCC_except_table2185
+ GCC_except_table2186
+ GCC_except_table2191
+ GCC_except_table2193
+ GCC_except_table2194
+ GCC_except_table2205
+ GCC_except_table2206
+ GCC_except_table2209
+ GCC_except_table2211
+ GCC_except_table2212
+ GCC_except_table2213
+ GCC_except_table2214
+ GCC_except_table2215
+ GCC_except_table2221
+ GCC_except_table2260
+ GCC_except_table2262
+ GCC_except_table2264
+ GCC_except_table2265
+ GCC_except_table2266
+ GCC_except_table2273
+ GCC_except_table2274
+ GCC_except_table2284
+ GCC_except_table2303
+ GCC_except_table2312
+ GCC_except_table2321
+ GCC_except_table2324
+ GCC_except_table2326
+ GCC_except_table2331
+ GCC_except_table2334
+ GCC_except_table2341
+ GCC_except_table2343
+ GCC_except_table2344
+ GCC_except_table2357
+ GCC_except_table2363
+ GCC_except_table2364
+ GCC_except_table2379
+ GCC_except_table2380
+ GCC_except_table2381
+ GCC_except_table2383
+ GCC_except_table2384
+ GCC_except_table2389
+ GCC_except_table2390
+ GCC_except_table2391
+ GCC_except_table2392
+ GCC_except_table2393
+ GCC_except_table2394
+ GCC_except_table2395
+ GCC_except_table2396
+ GCC_except_table2399
+ GCC_except_table2402
+ GCC_except_table2403
+ GCC_except_table2404
+ GCC_except_table2406
+ GCC_except_table2411
+ GCC_except_table2413
+ GCC_except_table2414
+ GCC_except_table2415
+ GCC_except_table2418
+ GCC_except_table2419
+ GCC_except_table2424
+ GCC_except_table2425
+ GCC_except_table2432
+ GCC_except_table2434
+ GCC_except_table2435
+ GCC_except_table2447
+ GCC_except_table2448
+ GCC_except_table2452
+ GCC_except_table2453
+ GCC_except_table2454
+ GCC_except_table2457
+ GCC_except_table2458
+ GCC_except_table2459
+ GCC_except_table2801
+ GCC_except_table2806
+ GCC_except_table2878
+ GCC_except_table2882
+ GCC_except_table2886
+ GCC_except_table2888
+ GCC_except_table2905
+ GCC_except_table2912
+ GCC_except_table2921
+ GCC_except_table2923
+ GCC_except_table2925
+ GCC_except_table2927
+ GCC_except_table2928
+ GCC_except_table2929
+ GCC_except_table2930
+ GCC_except_table2931
+ GCC_except_table2932
+ GCC_except_table2933
+ GCC_except_table2935
+ GCC_except_table2947
+ GCC_except_table2962
+ GCC_except_table2972
+ GCC_except_table2980
+ GCC_except_table3018
+ GCC_except_table3019
+ GCC_except_table3021
+ GCC_except_table3022
+ GCC_except_table3023
+ GCC_except_table3045
+ GCC_except_table3047
+ GCC_except_table3048
+ GCC_except_table3049
+ GCC_except_table3050
+ GCC_except_table3060
+ GCC_except_table3062
+ GCC_except_table3092
+ GCC_except_table3095
+ GCC_except_table3096
+ GCC_except_table3097
+ GCC_except_table3098
+ GCC_except_table3107
+ GCC_except_table3114
+ GCC_except_table3119
+ GCC_except_table3152
+ GCC_except_table3157
+ GCC_except_table3158
+ GCC_except_table3290
+ GCC_except_table415
+ GCC_except_table417
+ GCC_except_table418
+ GCC_except_table419
+ GCC_except_table420
+ GCC_except_table421
+ GCC_except_table422
+ GCC_except_table429
+ GCC_except_table436
+ GCC_except_table437
+ GCC_except_table438
+ GCC_except_table440
+ GCC_except_table444
+ GCC_except_table453
+ GCC_except_table464
+ GCC_except_table476
+ GCC_except_table477
+ GCC_except_table479
+ GCC_except_table482
+ GCC_except_table486
+ GCC_except_table488
+ GCC_except_table498
+ GCC_except_table514
+ GCC_except_table525
+ GCC_except_table527
+ GCC_except_table532
+ GCC_except_table549
+ GCC_except_table571
+ GCC_except_table576
+ GCC_except_table577
+ GCC_except_table578
+ GCC_except_table582
+ GCC_except_table609
+ GCC_except_table614
+ GCC_except_table624
+ GCC_except_table626
+ GCC_except_table631
+ GCC_except_table633
+ GCC_except_table653
+ GCC_except_table660
+ GCC_except_table666
+ GCC_except_table701
+ GCC_except_table702
+ GCC_except_table706
+ GCC_except_table707
+ GCC_except_table708
+ GCC_except_table709
+ GCC_except_table711
+ GCC_except_table714
+ GCC_except_table715
+ GCC_except_table718
+ GCC_except_table720
+ GCC_except_table721
+ GCC_except_table722
+ GCC_except_table723
+ GCC_except_table728
+ GCC_except_table730
+ GCC_except_table732
+ GCC_except_table733
+ GCC_except_table734
+ GCC_except_table740
+ GCC_except_table741
+ GCC_except_table743
+ GCC_except_table744
+ GCC_except_table745
+ GCC_except_table747
+ GCC_except_table751
+ GCC_except_table753
+ GCC_except_table754
+ GCC_except_table760
+ GCC_except_table761
+ GCC_except_table762
+ GCC_except_table765
+ GCC_except_table769
+ GCC_except_table772
+ GCC_except_table776
+ GCC_except_table777
+ GCC_except_table780
+ GCC_except_table782
+ GCC_except_table802
+ GCC_except_table811
+ GCC_except_table812
+ GCC_except_table821
+ GCC_except_table823
+ GCC_except_table824
+ GCC_except_table825
+ GCC_except_table850
+ GCC_except_table852
+ GCC_except_table853
+ GCC_except_table871
+ GCC_except_table873
+ GCC_except_table875
+ GCC_except_table886
+ GCC_except_table887
+ GCC_except_table890
+ GCC_except_table892
+ GCC_except_table903
+ GCC_except_table904
+ GCC_except_table916
+ GCC_except_table917
+ GCC_except_table920
+ GCC_except_table931
+ GCC_except_table932
+ GCC_except_table942
+ GCC_except_table950
+ GCC_except_table951
+ GCC_except_table956
+ GCC_except_table963
+ GCC_except_table965
+ GCC_except_table966
+ GCC_except_table968
+ GCC_except_table970
+ GCC_except_table982
+ GCC_except_table994
+ _ApplyMTL4ColorAttachmentSpecialization
+ _CompareArgumentTableUse
+ _DYTraceDecode_MTL4CommandBuffer_resolveCounterHeap_withRange_intoBuffer_atOffset_waitFence_updateFence
+ _DYTraceDecode_MTL4CommandBuffer_resolveCounterHeap_withRange_intoBuffer_waitFence_updateFence
+ _DYTraceDecode_MTL4CommandBuffer_writeTimestampIntoHeap_atIndex
+ _DYTraceDecode_MTL4Compiler_newRenderPipelineStateBySpecializationWithDescriptor_pipeline_completionHandler
+ _DYTraceDecode_MTL4Compiler_newRenderPipelineStateBySpecializationWithDescriptor_pipeline_error
+ _DYTraceDecode_MTL4ComputeCommandEncoder_writeTimestampWithGranularity_intoHeap_atIndex
+ _DYTraceDecode_MTL4CounterHeap_dealloc
+ _DYTraceDecode_MTL4CounterHeap_invalidateCounterRange
+ _DYTraceDecode_MTL4CounterHeap_resolveCounterRange
+ _DYTraceDecode_MTL4CounterHeap_setLabel
+ _DYTraceDecode_MTL4RenderCommandEncoder_writeTimestampWithGranularity_afterStage_intoHeap_atIndex
+ _DYTraceDecode_MTLDevice_newCounterHeapWithDescriptor_error
+ _DecodeDYMTL4CounterHeapDescriptor
+ _GTCaptureArchive_openSeparateFile
+ _GTSMMTL4Context_getFrameInterpolators
+ _GTSMMTL4Context_getSpatialScalers
+ _GTSMMTL4Context_getTemporalDenoisedScalers
+ _GTSMMTL4Context_getTemporalScalers
+ _GTSMMTL4CounterHeap_init
+ _GTSMMTL4CounterHeap_processTraceFuncWithMap
+ _GTSMMTLBuilder_mtl4CounterHeap
+ _GTSMMTLContext_getMTL4CounterHeaps
+ _GTSMMTLRenderPipelineStateResolved_hasFragmentFunction
+ _GTSMMTLRenderPipelineStateResolved_hasObjectFunction
+ _GTSMMTLRenderPipelineStateResolved_mtl4MeshRender
+ _GTSMMTLRenderPipelineStateResolved_mtl4Render
+ _GTSMMTLRenderPipelineStateResolved_rasterSampleCount
+ _GTSMMTLRenderPipelineState_MTL4TilePipelineDescriptor
+ _GTSMMTLRenderPipelineState_resolve
+ _GTTraceContext_cleanup
+ _MakeMTL4CounterHeapDescriptor
+ _MakeScratchTensorDescriptor
+ _OBJC_CLASS_$_GTReplayFetchCounterHeap
+ _OBJC_CLASS_$_GTReplayMTLFXFrameInterpolator
+ _OBJC_CLASS_$_MTL4CounterHeapDescriptor
+ _OBJC_IVAR_$_GTMTLReplayObjectMap._mtl4CounterHeaps
+ _OBJC_METACLASS_$_GTReplayMTLFXFrameInterpolator
+ _ResolveMTL4ColorAttachmentDefaults
+ _StoreMTL4CounterHeapDescriptorUsingDecode
+ __OBJC_$_CLASS_METHODS_GTReplayMTLFXFrameInterpolator
+ __OBJC_$_INSTANCE_METHODS_GTReplayMTLFXFrameInterpolator
+ __OBJC_$_PROP_LIST_GTReplayMTLFXFrameInterpolator
+ __OBJC_$_PROP_LIST_MTLFXFrameInterpolatorBase
+ __OBJC_$_PROP_LIST_MTLFXFrameInterpolatorSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXFrameInterpolator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXFrameInterpolatorBase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXFrameInterpolatorSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXFrameInterpolator
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXFrameInterpolatorBase
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXFrameInterpolatorSPI
+ __OBJC_$_PROTOCOL_REFS_MTLFXFrameInterpolator
+ __OBJC_$_PROTOCOL_REFS_MTLFXFrameInterpolatorBase
+ __OBJC_$_PROTOCOL_REFS_MTLFXFrameInterpolatorSPI
+ __OBJC_CLASS_PROTOCOLS_$_GTReplayMTLFXFrameInterpolator
+ __OBJC_CLASS_RO_$_GTReplayMTLFXFrameInterpolator
+ __OBJC_LABEL_PROTOCOL_$_MTLFXFrameInterpolator
+ __OBJC_LABEL_PROTOCOL_$_MTLFXFrameInterpolatorBase
+ __OBJC_LABEL_PROTOCOL_$_MTLFXFrameInterpolatorSPI
+ __OBJC_METACLASS_RO_$_GTReplayMTLFXFrameInterpolator
+ __OBJC_PROTOCOL_$_MTLFXFrameInterpolator
+ __OBJC_PROTOCOL_$_MTLFXFrameInterpolatorBase
+ __OBJC_PROTOCOL_$_MTLFXFrameInterpolatorSPI
+ __ZL29ShouldInstrumentFragmentStageP21GTMTLReplayControllerRK22GTMTLIndirectResourcesPK11GTTraceFuncyP10apr_pool_t
+ __ZL30ShouldInstrumentICBObjectStageP21GTMTLReplayControllerPK11GTTraceFuncyP10apr_pool_t
+ ___NewResourceData_block_invoke_5
+ _openat
- +[GTReplayMTL4FXTemporalDenoisedScaler wrapperWithDevice:descriptor:compiler:]
- +[GTReplayMTL4FXTemporalScaler wrapperWithDevice:descriptor:compiler:]
- -[GTReplayMTL4FXTemporalDenoisedScaler colorTextureBarrierStages]
- -[GTReplayMTL4FXTemporalDenoisedScaler colorTextureFormat]
- -[GTReplayMTL4FXTemporalDenoisedScaler colorTextureUsage]
- -[GTReplayMTL4FXTemporalDenoisedScaler colorTexture]
- -[GTReplayMTL4FXTemporalDenoisedScaler debugTexture]
- -[GTReplayMTL4FXTemporalDenoisedScaler denoiseStrengthMaskTextureFormat]
- -[GTReplayMTL4FXTemporalDenoisedScaler denoiseStrengthMaskTextureUsage]
- -[GTReplayMTL4FXTemporalDenoisedScaler denoiseStrengthMaskTexture]
- -[GTReplayMTL4FXTemporalDenoisedScaler depthTextureFormat]
- -[GTReplayMTL4FXTemporalDenoisedScaler depthTextureUsage]
- -[GTReplayMTL4FXTemporalDenoisedScaler depthTexture]
- -[GTReplayMTL4FXTemporalDenoisedScaler diffuseAlbedoTextureFormat]
- -[GTReplayMTL4FXTemporalDenoisedScaler diffuseAlbedoTextureUsage]
- -[GTReplayMTL4FXTemporalDenoisedScaler diffuseAlbedoTexture]
- -[GTReplayMTL4FXTemporalDenoisedScaler dilatedMotionVectors]
- -[GTReplayMTL4FXTemporalDenoisedScaler encodeToCommandBuffer:]
- -[GTReplayMTL4FXTemporalDenoisedScaler exposureTexture]
- -[GTReplayMTL4FXTemporalDenoisedScaler fence]
- -[GTReplayMTL4FXTemporalDenoisedScaler initWithDevice:descriptor:compiler:]
- -[GTReplayMTL4FXTemporalDenoisedScaler inputContentHeight]
- -[GTReplayMTL4FXTemporalDenoisedScaler inputContentMaxScale]
- -[GTReplayMTL4FXTemporalDenoisedScaler inputContentMinScale]
- -[GTReplayMTL4FXTemporalDenoisedScaler inputContentWidth]
- -[GTReplayMTL4FXTemporalDenoisedScaler inputHeight]
- -[GTReplayMTL4FXTemporalDenoisedScaler inputWidth]
- -[GTReplayMTL4FXTemporalDenoisedScaler isDepthReversed]
- -[GTReplayMTL4FXTemporalDenoisedScaler jitterOffsetX]
- -[GTReplayMTL4FXTemporalDenoisedScaler jitterOffsetY]
- -[GTReplayMTL4FXTemporalDenoisedScaler motionTextureFormat]
- -[GTReplayMTL4FXTemporalDenoisedScaler motionTextureUsage]
- -[GTReplayMTL4FXTemporalDenoisedScaler motionTexture]
- -[GTReplayMTL4FXTemporalDenoisedScaler motionVectorScaleX]
- -[GTReplayMTL4FXTemporalDenoisedScaler motionVectorScaleY]
- -[GTReplayMTL4FXTemporalDenoisedScaler normalTextureFormat]
- -[GTReplayMTL4FXTemporalDenoisedScaler normalTextureUsage]
- -[GTReplayMTL4FXTemporalDenoisedScaler normalTexture]
- -[GTReplayMTL4FXTemporalDenoisedScaler outputHeight]
- -[GTReplayMTL4FXTemporalDenoisedScaler outputTextureBarrierStages]
- -[GTReplayMTL4FXTemporalDenoisedScaler outputTextureFormat]
- -[GTReplayMTL4FXTemporalDenoisedScaler outputTextureUsage]
- -[GTReplayMTL4FXTemporalDenoisedScaler outputTexture]
- -[GTReplayMTL4FXTemporalDenoisedScaler outputWidth]
- -[GTReplayMTL4FXTemporalDenoisedScaler preExposure]
- -[GTReplayMTL4FXTemporalDenoisedScaler reactiveMaskTextureFormat]
- -[GTReplayMTL4FXTemporalDenoisedScaler reactiveMaskTextureUsage]
- -[GTReplayMTL4FXTemporalDenoisedScaler reactiveMaskTexture]
- -[GTReplayMTL4FXTemporalDenoisedScaler reactiveTextureUsage]
- -[GTReplayMTL4FXTemporalDenoisedScaler reset]
- -[GTReplayMTL4FXTemporalDenoisedScaler roughnessTextureFormat]
- -[GTReplayMTL4FXTemporalDenoisedScaler roughnessTextureUsage]
- -[GTReplayMTL4FXTemporalDenoisedScaler roughnessTexture]
- -[GTReplayMTL4FXTemporalDenoisedScaler setColorTexture:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setColorTextureBarrierStages:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setDebugTexture:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setDenoiseStrengthMaskTexture:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setDepthReversed:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setDepthTexture:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setDiffuseAlbedoTexture:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setExposureTexture:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setFence:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setInputContentHeight:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setInputContentWidth:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setJitterOffsetX:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setJitterOffsetY:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setMotionTexture:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setMotionVectorScaleX:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setMotionVectorScaleY:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setNormalTexture:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setOutputTexture:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setPreExposure:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setReactiveMaskTexture:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setReset:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setRoughnessTexture:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setShouldResetHistory:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setSpecularAlbedoTexture:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setSpecularHitDistanceTexture:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setTransparencyOverlayTexture:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setViewToClipMatrix:]
- -[GTReplayMTL4FXTemporalDenoisedScaler setWorldToViewMatrix:]
- -[GTReplayMTL4FXTemporalDenoisedScaler shouldResetHistory]
- -[GTReplayMTL4FXTemporalDenoisedScaler specularAlbedoTextureFormat]
- -[GTReplayMTL4FXTemporalDenoisedScaler specularAlbedoTextureUsage]
- -[GTReplayMTL4FXTemporalDenoisedScaler specularAlbedoTexture]
- -[GTReplayMTL4FXTemporalDenoisedScaler specularHitDistanceTextureFormat]
- -[GTReplayMTL4FXTemporalDenoisedScaler specularHitDistanceTextureUsage]
- -[GTReplayMTL4FXTemporalDenoisedScaler specularHitDistanceTexture]
- -[GTReplayMTL4FXTemporalDenoisedScaler transparencyOverlayTextureFormat]
- -[GTReplayMTL4FXTemporalDenoisedScaler transparencyOverlayTextureUsage]
- -[GTReplayMTL4FXTemporalDenoisedScaler transparencyOverlayTexture]
- -[GTReplayMTL4FXTemporalDenoisedScaler viewToClipMatrix]
- -[GTReplayMTL4FXTemporalDenoisedScaler worldToViewMatrix]
- -[GTReplayMTL4FXTemporalScaler colorContentOffsetX]
- -[GTReplayMTL4FXTemporalScaler colorContentOffsetY]
- -[GTReplayMTL4FXTemporalScaler colorTextureBarrierStages]
- -[GTReplayMTL4FXTemporalScaler colorTextureFormat]
- -[GTReplayMTL4FXTemporalScaler colorTextureUsage]
- -[GTReplayMTL4FXTemporalScaler colorTexture]
- -[GTReplayMTL4FXTemporalScaler currentViewToClipMatrix]
- -[GTReplayMTL4FXTemporalScaler currentWorldToViewMatrix]
- -[GTReplayMTL4FXTemporalScaler debugTexture]
- -[GTReplayMTL4FXTemporalScaler depthContentOffsetX]
- -[GTReplayMTL4FXTemporalScaler depthContentOffsetY]
- -[GTReplayMTL4FXTemporalScaler depthTextureFormat]
- -[GTReplayMTL4FXTemporalScaler depthTextureUsage]
- -[GTReplayMTL4FXTemporalScaler depthTexture]
- -[GTReplayMTL4FXTemporalScaler dilatedMotionVectors]
- -[GTReplayMTL4FXTemporalScaler encodeToCommandBuffer:]
- -[GTReplayMTL4FXTemporalScaler exposureTexture]
- -[GTReplayMTL4FXTemporalScaler fence]
- -[GTReplayMTL4FXTemporalScaler initWithDevice:descriptor:compiler:]
- -[GTReplayMTL4FXTemporalScaler inputContentHeight]
- -[GTReplayMTL4FXTemporalScaler inputContentMaxScale]
- -[GTReplayMTL4FXTemporalScaler inputContentMinScale]
- -[GTReplayMTL4FXTemporalScaler inputContentWidth]
- -[GTReplayMTL4FXTemporalScaler inputHeight]
- -[GTReplayMTL4FXTemporalScaler inputWidth]
- -[GTReplayMTL4FXTemporalScaler isDepthReversed]
- -[GTReplayMTL4FXTemporalScaler jitterOffsetX]
- -[GTReplayMTL4FXTemporalScaler jitterOffsetY]
- -[GTReplayMTL4FXTemporalScaler motionContentOffsetX]
- -[GTReplayMTL4FXTemporalScaler motionContentOffsetY]
- -[GTReplayMTL4FXTemporalScaler motionTextureFormat]
- -[GTReplayMTL4FXTemporalScaler motionTextureUsage]
- -[GTReplayMTL4FXTemporalScaler motionTexture]
- -[GTReplayMTL4FXTemporalScaler motionVectorScaleX]
- -[GTReplayMTL4FXTemporalScaler motionVectorScaleY]
- -[GTReplayMTL4FXTemporalScaler outputHeight]
- -[GTReplayMTL4FXTemporalScaler outputOffsetX]
- -[GTReplayMTL4FXTemporalScaler outputOffsetY]
- -[GTReplayMTL4FXTemporalScaler outputTextureBarrierStages]
- -[GTReplayMTL4FXTemporalScaler outputTextureFormat]
- -[GTReplayMTL4FXTemporalScaler outputTextureUsage]
- -[GTReplayMTL4FXTemporalScaler outputTexture]
- -[GTReplayMTL4FXTemporalScaler outputWidth]
- -[GTReplayMTL4FXTemporalScaler preExposure]
- -[GTReplayMTL4FXTemporalScaler previousJitterOffset]
- -[GTReplayMTL4FXTemporalScaler previousViewToClipMatrix]
- -[GTReplayMTL4FXTemporalScaler previousWorldToViewMatrix]
- -[GTReplayMTL4FXTemporalScaler reactiveMaskContentOffsetX]
- -[GTReplayMTL4FXTemporalScaler reactiveMaskContentOffsetY]
- -[GTReplayMTL4FXTemporalScaler reactiveMaskTextureFormat]
- -[GTReplayMTL4FXTemporalScaler reactiveMaskTextureUsage]
- -[GTReplayMTL4FXTemporalScaler reactiveMaskTexture]
- -[GTReplayMTL4FXTemporalScaler reactiveTextureUsage]
- -[GTReplayMTL4FXTemporalScaler reset]
- -[GTReplayMTL4FXTemporalScaler setColorContentOffsetX:]
- -[GTReplayMTL4FXTemporalScaler setColorContentOffsetY:]
- -[GTReplayMTL4FXTemporalScaler setColorTexture:]
- -[GTReplayMTL4FXTemporalScaler setColorTextureBarrierStages:]
- -[GTReplayMTL4FXTemporalScaler setCurrentViewToClipMatrix:]
- -[GTReplayMTL4FXTemporalScaler setCurrentWorldToViewMatrix:]
- -[GTReplayMTL4FXTemporalScaler setDebugTexture:]
- -[GTReplayMTL4FXTemporalScaler setDepthContentOffsetX:]
- -[GTReplayMTL4FXTemporalScaler setDepthContentOffsetY:]
- -[GTReplayMTL4FXTemporalScaler setDepthReversed:]
- -[GTReplayMTL4FXTemporalScaler setDepthTexture:]
- -[GTReplayMTL4FXTemporalScaler setExposureTexture:]
- -[GTReplayMTL4FXTemporalScaler setFence:]
- -[GTReplayMTL4FXTemporalScaler setInputContentHeight:]
- -[GTReplayMTL4FXTemporalScaler setInputContentWidth:]
- -[GTReplayMTL4FXTemporalScaler setJitterOffsetX:]
- -[GTReplayMTL4FXTemporalScaler setJitterOffsetY:]
- -[GTReplayMTL4FXTemporalScaler setMotionContentOffsetX:]
- -[GTReplayMTL4FXTemporalScaler setMotionContentOffsetY:]
- -[GTReplayMTL4FXTemporalScaler setMotionTexture:]
- -[GTReplayMTL4FXTemporalScaler setMotionVectorScaleX:]
- -[GTReplayMTL4FXTemporalScaler setMotionVectorScaleY:]
- -[GTReplayMTL4FXTemporalScaler setOutputOffsetX:]
- -[GTReplayMTL4FXTemporalScaler setOutputOffsetY:]
- -[GTReplayMTL4FXTemporalScaler setOutputTexture:]
- -[GTReplayMTL4FXTemporalScaler setPreExposure:]
- -[GTReplayMTL4FXTemporalScaler setPreviousJitterOffset:]
- -[GTReplayMTL4FXTemporalScaler setPreviousViewToClipMatrix:]
- -[GTReplayMTL4FXTemporalScaler setPreviousWorldToViewMatrix:]
- -[GTReplayMTL4FXTemporalScaler setReactiveMaskContentOffsetX:]
- -[GTReplayMTL4FXTemporalScaler setReactiveMaskContentOffsetY:]
- -[GTReplayMTL4FXTemporalScaler setReactiveMaskTexture:]
- -[GTReplayMTL4FXTemporalScaler setReset:]
- GCC_except_table1002
- GCC_except_table1003
- GCC_except_table1006
- GCC_except_table1017
- GCC_except_table1019
- GCC_except_table1023
- GCC_except_table1024
- GCC_except_table1025
- GCC_except_table1027
- GCC_except_table1028
- GCC_except_table1036
- GCC_except_table1037
- GCC_except_table1038
- GCC_except_table1040
- GCC_except_table1042
- GCC_except_table1043
- GCC_except_table1045
- GCC_except_table1049
- GCC_except_table1051
- GCC_except_table1052
- GCC_except_table1054
- GCC_except_table1056
- GCC_except_table1059
- GCC_except_table1068
- GCC_except_table1069
- GCC_except_table1080
- GCC_except_table1086
- GCC_except_table1087
- GCC_except_table1104
- GCC_except_table1242
- GCC_except_table1248
- GCC_except_table1274
- GCC_except_table1289
- GCC_except_table1295
- GCC_except_table1301
- GCC_except_table1322
- GCC_except_table1323
- GCC_except_table1324
- GCC_except_table1325
- GCC_except_table1339
- GCC_except_table1340
- GCC_except_table1353
- GCC_except_table1358
- GCC_except_table1365
- GCC_except_table1370
- GCC_except_table1375
- GCC_except_table1376
- GCC_except_table1382
- GCC_except_table1383
- GCC_except_table1385
- GCC_except_table1390
- GCC_except_table1391
- GCC_except_table1404
- GCC_except_table1412
- GCC_except_table1413
- GCC_except_table1414
- GCC_except_table1415
- GCC_except_table1416
- GCC_except_table1417
- GCC_except_table1418
- GCC_except_table1419
- GCC_except_table1420
- GCC_except_table1422
- GCC_except_table1426
- GCC_except_table1441
- GCC_except_table1444
- GCC_except_table1445
- GCC_except_table1446
- GCC_except_table1447
- GCC_except_table1449
- GCC_except_table1451
- GCC_except_table1453
- GCC_except_table1454
- GCC_except_table1459
- GCC_except_table1472
- GCC_except_table1473
- GCC_except_table1474
- GCC_except_table1477
- GCC_except_table1478
- GCC_except_table1479
- GCC_except_table1480
- GCC_except_table1481
- GCC_except_table1482
- GCC_except_table1483
- GCC_except_table1484
- GCC_except_table1485
- GCC_except_table1486
- GCC_except_table1491
- GCC_except_table1520
- GCC_except_table1533
- GCC_except_table1537
- GCC_except_table1545
- GCC_except_table1609
- GCC_except_table1722
- GCC_except_table1744
- GCC_except_table1745
- GCC_except_table1825
- GCC_except_table1856
- GCC_except_table1857
- GCC_except_table1858
- GCC_except_table1859
- GCC_except_table1860
- GCC_except_table1861
- GCC_except_table1862
- GCC_except_table1863
- GCC_except_table1865
- GCC_except_table1877
- GCC_except_table1879
- GCC_except_table1881
- GCC_except_table1883
- GCC_except_table1885
- GCC_except_table1894
- GCC_except_table1921
- GCC_except_table1922
- GCC_except_table1923
- GCC_except_table1926
- GCC_except_table1928
- GCC_except_table2034
- GCC_except_table2037
- GCC_except_table2039
- GCC_except_table2040
- GCC_except_table2041
- GCC_except_table2042
- GCC_except_table2047
- GCC_except_table2048
- GCC_except_table2058
- GCC_except_table2059
- GCC_except_table2060
- GCC_except_table2061
- GCC_except_table2063
- GCC_except_table2065
- GCC_except_table2066
- GCC_except_table2067
- GCC_except_table2068
- GCC_except_table2070
- GCC_except_table2075
- GCC_except_table2112
- GCC_except_table2134
- GCC_except_table2135
- GCC_except_table2136
- GCC_except_table2137
- GCC_except_table2138
- GCC_except_table2225
- GCC_except_table2226
- GCC_except_table2227
- GCC_except_table2248
- GCC_except_table2249
- GCC_except_table2276
- GCC_except_table2278
- GCC_except_table2279
- GCC_except_table2290
- GCC_except_table2291
- GCC_except_table2294
- GCC_except_table2295
- GCC_except_table2296
- GCC_except_table2297
- GCC_except_table2298
- GCC_except_table2299
- GCC_except_table2306
- GCC_except_table2309
- GCC_except_table2347
- GCC_except_table2349
- GCC_except_table2354
- GCC_except_table2356
- GCC_except_table2358
- GCC_except_table2359
- GCC_except_table2385
- GCC_except_table2401
- GCC_except_table2407
- GCC_except_table2420
- GCC_except_table2427
- GCC_except_table2431
- GCC_except_table2436
- GCC_except_table2437
- GCC_except_table2438
- GCC_except_table2439
- GCC_except_table2443
- GCC_except_table2465
- GCC_except_table2467
- GCC_except_table2469
- GCC_except_table2470
- GCC_except_table2474
- GCC_except_table2475
- GCC_except_table2476
- GCC_except_table2477
- GCC_except_table2478
- GCC_except_table2479
- GCC_except_table2480
- GCC_except_table2481
- GCC_except_table2482
- GCC_except_table2483
- GCC_except_table2485
- GCC_except_table2488
- GCC_except_table2489
- GCC_except_table2490
- GCC_except_table2492
- GCC_except_table2496
- GCC_except_table2497
- GCC_except_table2498
- GCC_except_table2499
- GCC_except_table2500
- GCC_except_table2501
- GCC_except_table2503
- GCC_except_table2504
- GCC_except_table2505
- GCC_except_table2510
- GCC_except_table2511
- GCC_except_table2515
- GCC_except_table2516
- GCC_except_table2518
- GCC_except_table2520
- GCC_except_table2521
- GCC_except_table2527
- GCC_except_table2533
- GCC_except_table2534
- GCC_except_table2535
- GCC_except_table2536
- GCC_except_table2538
- GCC_except_table2539
- GCC_except_table2540
- GCC_except_table2541
- GCC_except_table2543
- GCC_except_table2544
- GCC_except_table2545
- GCC_except_table2552
- GCC_except_table2959
- GCC_except_table2967
- GCC_except_table2969
- GCC_except_table2993
- GCC_except_table3002
- GCC_except_table3004
- GCC_except_table3006
- GCC_except_table3008
- GCC_except_table3010
- GCC_except_table3011
- GCC_except_table3012
- GCC_except_table3013
- GCC_except_table3014
- GCC_except_table3016
- GCC_except_table3028
- GCC_except_table3043
- GCC_except_table3067
- GCC_except_table3090
- GCC_except_table3102
- GCC_except_table3103
- GCC_except_table3104
- GCC_except_table3125
- GCC_except_table3126
- GCC_except_table3128
- GCC_except_table3129
- GCC_except_table3130
- GCC_except_table3131
- GCC_except_table3141
- GCC_except_table3142
- GCC_except_table3143
- GCC_except_table3173
- GCC_except_table3176
- GCC_except_table3177
- GCC_except_table3178
- GCC_except_table3179
- GCC_except_table3180
- GCC_except_table3181
- GCC_except_table3188
- GCC_except_table3195
- GCC_except_table3200
- GCC_except_table3233
- GCC_except_table3238
- GCC_except_table3239
- GCC_except_table3371
- GCC_except_table501
- GCC_except_table503
- GCC_except_table504
- GCC_except_table505
- GCC_except_table506
- GCC_except_table508
- GCC_except_table515
- GCC_except_table523
- GCC_except_table526
- GCC_except_table530
- GCC_except_table550
- GCC_except_table562
- GCC_except_table563
- GCC_except_table565
- GCC_except_table568
- GCC_except_table572
- GCC_except_table574
- GCC_except_table584
- GCC_except_table593
- GCC_except_table600
- GCC_except_table608
- GCC_except_table610
- GCC_except_table611
- GCC_except_table618
- GCC_except_table625
- GCC_except_table635
- GCC_except_table657
- GCC_except_table662
- GCC_except_table663
- GCC_except_table664
- GCC_except_table668
- GCC_except_table695
- GCC_except_table699
- GCC_except_table700
- GCC_except_table710
- GCC_except_table717
- GCC_except_table739
- GCC_except_table787
- GCC_except_table788
- GCC_except_table792
- GCC_except_table793
- GCC_except_table794
- GCC_except_table795
- GCC_except_table797
- GCC_except_table798
- GCC_except_table800
- GCC_except_table801
- GCC_except_table804
- GCC_except_table805
- GCC_except_table806
- GCC_except_table807
- GCC_except_table808
- GCC_except_table809
- GCC_except_table814
- GCC_except_table816
- GCC_except_table818
- GCC_except_table830
- GCC_except_table831
- GCC_except_table832
- GCC_except_table833
- GCC_except_table839
- GCC_except_table840
- GCC_except_table846
- GCC_except_table858
- GCC_except_table906
- GCC_except_table907
- GCC_except_table911
- GCC_except_table912
- GCC_except_table913
- GCC_except_table915
- GCC_except_table923
- GCC_except_table924
- GCC_except_table934
- GCC_except_table936
- GCC_except_table949
- GCC_except_table961
- GCC_except_table972
- GCC_except_table974
- GCC_except_table976
- GCC_except_table978
- GCC_except_table984
- GCC_except_table989
- GCC_except_table990
- GCC_except_table991
- GCC_except_table995
- GCC_except_table996
- _DYTraceDecode_MTL4FXTemporalScaler_executionMode
- _GTCaptureArchive_confinedSeparateFilePath
- _GTFenum_isSetArgumentTable
- _GTFileSystem_open
- _GTSMMTLRenderPipelineState_fragmentFunction
- _GTSMMTLRenderPipelineState_rasterSampleCount
- _GTTraceDispatch_createArgumentTableStateMapFromParams
- _GTTraceDispatch_reconstructArgumentTableState
- _GTTraceDispatch_setArgumentTableStateForGPUCommandStage
- _OBJC_CLASS_$_GTReplayMTL4FXTemporalDenoisedScaler
- _OBJC_CLASS_$_GTReplayMTL4FXTemporalScaler
- _OBJC_METACLASS_$_GTReplayMTL4FXTemporalDenoisedScaler
- _OBJC_METACLASS_$_GTReplayMTL4FXTemporalScaler
- __OBJC_$_CLASS_METHODS_GTReplayMTL4FXTemporalDenoisedScaler
- __OBJC_$_CLASS_METHODS_GTReplayMTL4FXTemporalScaler
- __OBJC_$_INSTANCE_METHODS_GTReplayMTL4FXTemporalDenoisedScaler
- __OBJC_$_INSTANCE_METHODS_GTReplayMTL4FXTemporalScaler
- __OBJC_$_PROP_LIST_GTReplayMTL4FXTemporalDenoisedScaler
- __OBJC_$_PROP_LIST_GTReplayMTL4FXTemporalScaler
- __OBJC_$_PROP_LIST_MTL4FXTemporalDenoisedScalerSPI
- __OBJC_$_PROP_LIST_MTL4FXTemporalScalerSPI
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXTemporalDenoisedScaler
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXTemporalDenoisedScalerSPI
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXTemporalScaler
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXTemporalScalerSPI
- __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXTemporalDenoisedScaler
- __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXTemporalDenoisedScalerSPI
- __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXTemporalScaler
- __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXTemporalScalerSPI
- __OBJC_$_PROTOCOL_REFS_MTL4FXTemporalDenoisedScaler
- __OBJC_$_PROTOCOL_REFS_MTL4FXTemporalDenoisedScalerSPI
- __OBJC_$_PROTOCOL_REFS_MTL4FXTemporalScaler
- __OBJC_$_PROTOCOL_REFS_MTL4FXTemporalScalerSPI
- __OBJC_CLASS_PROTOCOLS_$_GTReplayMTL4FXTemporalDenoisedScaler
- __OBJC_CLASS_PROTOCOLS_$_GTReplayMTL4FXTemporalScaler
- __OBJC_CLASS_RO_$_GTReplayMTL4FXTemporalDenoisedScaler
- __OBJC_CLASS_RO_$_GTReplayMTL4FXTemporalScaler
- __OBJC_LABEL_PROTOCOL_$_MTL4FXTemporalDenoisedScaler
- __OBJC_LABEL_PROTOCOL_$_MTL4FXTemporalDenoisedScalerSPI
- __OBJC_LABEL_PROTOCOL_$_MTL4FXTemporalScaler
- __OBJC_LABEL_PROTOCOL_$_MTL4FXTemporalScalerSPI
- __OBJC_METACLASS_RO_$_GTReplayMTL4FXTemporalDenoisedScaler
- __OBJC_METACLASS_RO_$_GTReplayMTL4FXTemporalScaler
- __OBJC_PROTOCOL_$_MTL4FXTemporalDenoisedScaler
- __OBJC_PROTOCOL_$_MTL4FXTemporalDenoisedScalerSPI
- __OBJC_PROTOCOL_$_MTL4FXTemporalScaler
- __OBJC_PROTOCOL_$_MTL4FXTemporalScalerSPI
- __ZL29ShouldInstrumentFragmentStageP21GTMTLReplayControllerRK22GTMTLIndirectResourcesPK11GTTraceFuncy
- __ZL30ShouldInstrumentICBObjectStageP21GTMTLReplayControllerPK11GTTraceFuncy
- ___67-[GTReplayMTL4FXTemporalScaler initWithDevice:descriptor:compiler:]_block_invoke
- ___75-[GTReplayMTL4FXTemporalDenoisedScaler initWithDevice:descriptor:compiler:]_block_invoke
- ___block_descriptor_56_e8_32s40s48s_e29_"<MTL4FXTemporalScaler>"8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e37_"<MTL4FXTemporalDenoisedScaler>"8?0ls32l8s40l8s48l8
- _apr_pool_terminate
- _apr_terminate
CStrings:
+ "-TimestampFrequency"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GPUToolsDevice/data_source/GTDataSource_load.m:724"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GPUToolsDevice/data_source/GTDataSource_load.m:745"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GPUToolsDevice/data_source/GTDataSource_restores.c:310"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:283"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:413"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:712"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTMTLReplay_accessTracking.mm:6984"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTMTLReplay_accessTracking.mm:7007"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTMTLReplay_argumentBuffers.m:2102"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTMTLReplay_loadArchive.m:2478"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTMTLReplay_shaderDebugger_internal.m:2184"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTMTLReplay_shaderDebugger_internal.m:5991"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func.c:1140"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func.c:1562"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func.c:479"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10030"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10074"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10085"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10107"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10140"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10184"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10195"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10217"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10459"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10492"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10525"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10536"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10558"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10580"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10690"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10701"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10745"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10778"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10789"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10811"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10833"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10932"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10943"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10976"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10987"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:11278"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:11345"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:2519"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:2541"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:2936"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:2958"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:2980"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:3002"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:3041"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:3063"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:3085"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:3107"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:4260"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:4517"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:4550"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:4610"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:471"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:4710"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:482"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:493"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:4959"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:5069"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:5080"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:5146"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:5196"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:5207"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:5262"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:5328"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:5372"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:5394"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:549"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:571"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:6800"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:8611"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:8633"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9551"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9826"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9859"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9892"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9903"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9936"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9958"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/sm/GTSMMTLBuilder.c:2657"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/sm/GTSMMTLRenderPipelineStateResolved.c:28"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trace/GTTraceContext.c:170"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trackers/GTResourceBinding.m:158"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trackers/GTResourceBinding.m:3013"
+ "0xffffc0e9"
+ "0xffffc0ea"
+ "Counter heap not found"
+ "Counter heap resolve returned nil"
+ "Harvest heap"
+ "Harvesting counter heap %llu (%s) range: %llu - %llu"
+ "MTL4CounterHeap"
+ "MTL4CounterHeap-0x%llx-Fetch"
+ "Pre-play for profiling"
+ "Rewind for profiling"
+ "file.fd >= 0"
+ "kDYFEMTL4CounterHeap_dealloc"
+ "kDYFEMTL4CounterHeap_invalidateCounterRange"
+ "kDYFEMTL4CounterHeap_resolveCounterRange"
+ "kDYFEMTL4CounterHeap_setLabel"
+ "memcmp((const char*)bytes + offset, (\"CUtt\"), sizeof(\"CUtt\")) == 0"
+ "memcmp((const char*)bytes + offset, (\"Ct@2ul@2ultt\"), sizeof(\"Ct@2ul@2ultt\")) == 0"
+ "memcmp((const char*)bytes + offset, (\"Ct@2ultultt\"), sizeof(\"Ct@2ultultt\")) == 0"
+ "memcmp((const char*)bytes + offset, (\"Culultul\"), sizeof(\"Culultul\")) == 0"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GPUToolsDevice/data_source/GTDataSource_load.m:726"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GPUToolsDevice/data_source/GTDataSource_load.m:747"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GPUToolsDevice/data_source/GTDataSource_restores.c:314"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:278"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:408"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:719"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTMTLReplay_accessTracking.mm:7100"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTMTLReplay_accessTracking.mm:7123"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTMTLReplay_argumentBuffers.m:2083"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTMTLReplay_loadArchive.m:2452"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTMTLReplay_shaderDebugger_internal.m:2183"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTMTLReplay_shaderDebugger_internal.m:5986"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func.c:1137"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func.c:1559"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func.c:478"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10043"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10054"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10076"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10318"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10351"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10384"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10395"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10417"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10439"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10549"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10560"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10604"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10637"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10648"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10670"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10692"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10791"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10802"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10835"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:10846"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:11137"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:11204"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:2389"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:2411"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:2806"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:2828"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:2850"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:2872"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:2911"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:2933"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:2955"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:2977"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:394"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:4130"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:438"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:4387"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:4420"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:4480"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:4580"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:460"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:4829"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:4939"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:4950"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:5016"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:5066"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:5077"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:5132"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:516"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:5198"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:5242"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:5264"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:538"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:6659"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:8470"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:8492"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9410"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9685"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9718"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9751"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9762"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9795"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9817"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9889"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9933"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9944"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9966"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTTraceFbuf2Func_mtl.c.inl:9999"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/sm/GTSMMTLBuilder.c:2613"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trace/GTTraceContext.c:162"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trackers/GTResourceBinding.m:157"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trackers/GTResourceBinding.m:3012"
- "@\"<MTL4FXTemporalDenoisedScaler>\"8@?0"
- "@\"<MTL4FXTemporalScaler>\"8@?0"
- "fd > 0"
- "kDYFEMTLCommandBuffer_computeCommandEncoderWithParallelExecution"
- "kDYFEMTLComputeCommandEncoder_dispatchBarrier"
```
