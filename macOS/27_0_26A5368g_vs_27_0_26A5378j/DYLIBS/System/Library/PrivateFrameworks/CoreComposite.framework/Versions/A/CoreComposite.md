## CoreComposite

> `/System/Library/PrivateFrameworks/CoreComposite.framework/Versions/A/CoreComposite`

```diff

-  __TEXT.__text: 0xba534
+  __TEXT.__text: 0xba9fc
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0x97c4
   __TEXT.__const: 0x16a0
-  __TEXT.__gcc_except_tab: 0xac90
+  __TEXT.__gcc_except_tab: 0xad08
   __TEXT.__oslogstring: 0x2922
-  __TEXT.__cstring: 0xe656
+  __TEXT.__cstring: 0xe7bc
   __TEXT.__ustring: 0x90
   __TEXT.__unwind_info: 0x2cd8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__got: 0x880
   __AUTH_CONST.__const: 0x1198
-  __AUTH_CONST.__cfstring: 0x9320
+  __AUTH_CONST.__cfstring: 0x9520
   __AUTH_CONST.__objc_const: 0x158a0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xc0

   - /usr/lib/libz.1.dylib
   Functions: 3675
   Symbols:   8455
-  CStrings:  3014
+  CStrings:  3046
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ GCC_except_table467
- GCC_except_table465
Functions:
~ -[CCMetalTextureSerializer deserializeMetalTexture:deviceGroup:] : 2116 -> 2096
~ -[CCMetalTextureSerializer serializeMetalTexture:deviceGroup:] : 1524 -> 1512
~ -[CCIndirectComputeCommands addComputeBlock:] : 568 -> 532
~ -[CCIndirectComputeCommands addRenderBlock:] : 576 -> 540
~ __ZNSt3__16vectorINS_7variantIJU8__strongU13block_pointerFvPU36objcproto25MTLIndirectComputeCommand11objc_objectE22CCIndirectCommandFenceU8__strongU13block_pointerFvPU35objcproto24MTLIndirectRenderCommand11objc_objectEEEENS_9allocatorISD_EEE24__emplace_back_slow_pathIJS7_EEEPSD_DpOT_ : 432 -> 412
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZ29-[CCAggregatePass sortPasses]E3$_0PU8__strongP6CCPassLb0EEEvT1_S8_T0_NS_15iterator_traitsIS8_E15difference_typeEb : 2476 -> 2456
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERZ29-[CCAggregatePass sortPasses]E3$_0PU8__strongP6CCPassEEbT1_S8_T0_ : 516 -> 488
~ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9nqe220106EPKvm : 1108 -> 1096
~ -[CCFeaturePoints2D initWithCoder:] : 472 -> 860
~ -[CCMinMaxDepthBinAlgorithm clearDepthBinsBottomRightBoundary:encoder:computeSize:] : 456 -> 480
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZ83-[CCTAAAlgorithmRasterizedBackward rebuildTileInstanceData:coverageType:frameData:]E3$_0P11PerTileDataLb0EEEvT1_S6_T0_NS_15iterator_traitsIS6_E15difference_typeEb : 2984 -> 2968
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERZ83-[CCTAAAlgorithmRasterizedBackward rebuildTileInstanceData:coverageType:frameData:]E3$_0P11PerTileDataEEbT1_S6_T0_ : 772 -> 748
~ ___34-[CCORFWarpService setDescriptor:]_block_invoke : 11080 -> 12116
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Algorithms/CCDisplayCorrection/CCBlurFastWorldDepthGaussian.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Algorithms/CCDisplayCorrection/CCDisplayCorrectionBoraPipeline.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Algorithms/CCDisplayCorrection/CCDisplayCorrectionWarpProvider.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Algorithms/CCDisplayCorrection/CCPassthroughDepthWarper.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Algorithms/CCFittingPlaneHybridWarpAlgorithm.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Algorithms/CCMinMaxDepthBinAlgorithm.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Algorithms/CCTAAAlgorithmRasterizedBackward.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Algorithms/CCWarpAlgorithmForward.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Algorithms/Descriptors/CCAlgorithmDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/CCAccelerateDeviceGroup.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/CCKey.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Contexts/CCContext.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Contexts/CCContextDeviceGroup.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Contexts/CCContextDeviceGroupPublic.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Contexts/CCContextSnapshot.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Data/CCData.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Data/CCDisplayCorrectionData.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Data/CCMTLData.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Data/CCWarpIntermediateData.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Data/CCXRData.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Debug/CCPipelineWrapper.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Passes/CCAggregatePass.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Passes/CCSimpleRenderPass.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Platform/CCBoraMeshEncoder.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Platform/CCBoraPlatform.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Resources/CCBuffer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Resources/CCLane.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Services/CCAdaptiveRegistrationService.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Services/CCDebugVisualizationService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Services/CCDisplayCorrectionService.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Services/CCGazeBasedDimmingService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Services/CCMultiLayerDisplayService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Services/CCORFWarpService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Services/CCQueryDepthHitService.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Services/CCReprojectedDepthBinService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Services/CCService.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Services/CCSituationalAwarenessService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Services/CCWarpService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Utilities/CCAutoTracer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Utilities/CCCPUMonitor.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Utilities/CCGPUMonitor.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Utilities/CCGraphicTools.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Utilities/CCMTLBufferAllocator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Utilities/CCMetalTextureSerializer.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Utilities/CCPipelineStateLibrary.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Utilities/CCQuicklook.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Utilities/CCRenderContext.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Utilities/CCSnooping.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Utilities/CCSystemTools.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Utilities/CCTextureIO.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreComposite/Utilities/FastClear/FastClear.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x889ay/Sources/CoreComposite/CoreCompositeKext/Userspace/CCDRMServiceConnection.m"
+ "AccumulateIndexCounts"
+ "AccumulateIndexCounts-LargeGroup"
+ "BufferSumReduction"
+ "ClearBoundary-BottomRight"
+ "ClearBoundary-TopLeft"
+ "ClearDepthBinWithValue"
+ "ClearDepthBinsTo0"
+ "CopyVirtualPixelStatsToReadbackTexture"
+ "GenerateVFWIndexBuffer"
+ "GetDepthStatsKernel"
+ "MeanDepthKernel"
+ "MinMaxDepthKernel"
+ "StreamReduceDepthBin-L"
+ "StreamReduceDepthBin-R"
+ "VFWMeshGeneration"
+ "warpPreProcess"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Algorithms/CCDisplayCorrection/CCBlurFastWorldDepthGaussian.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Algorithms/CCDisplayCorrection/CCDisplayCorrectionBoraPipeline.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Algorithms/CCDisplayCorrection/CCDisplayCorrectionWarpProvider.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Algorithms/CCDisplayCorrection/CCPassthroughDepthWarper.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Algorithms/CCFittingPlaneHybridWarpAlgorithm.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Algorithms/CCMinMaxDepthBinAlgorithm.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Algorithms/CCTAAAlgorithmRasterizedBackward.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Algorithms/CCWarpAlgorithmForward.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Algorithms/Descriptors/CCAlgorithmDescriptor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/CCAccelerateDeviceGroup.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/CCKey.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Contexts/CCContext.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Contexts/CCContextDeviceGroup.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Contexts/CCContextDeviceGroupPublic.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Contexts/CCContextSnapshot.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Data/CCData.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Data/CCDisplayCorrectionData.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Data/CCMTLData.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Data/CCWarpIntermediateData.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Data/CCXRData.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Debug/CCPipelineWrapper.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Passes/CCAggregatePass.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Passes/CCSimpleRenderPass.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Platform/CCBoraMeshEncoder.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Platform/CCBoraPlatform.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Resources/CCBuffer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Resources/CCLane.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Services/CCAdaptiveRegistrationService.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Services/CCDebugVisualizationService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Services/CCDisplayCorrectionService.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Services/CCGazeBasedDimmingService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Services/CCMultiLayerDisplayService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Services/CCORFWarpService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Services/CCQueryDepthHitService.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Services/CCReprojectedDepthBinService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Services/CCService.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Services/CCSituationalAwarenessService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Services/CCWarpService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Utilities/CCAutoTracer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Utilities/CCCPUMonitor.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Utilities/CCGPUMonitor.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Utilities/CCGraphicTools.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Utilities/CCMTLBufferAllocator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Utilities/CCMetalTextureSerializer.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Utilities/CCPipelineStateLibrary.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Utilities/CCQuicklook.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Utilities/CCRenderContext.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Utilities/CCSnooping.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Utilities/CCSystemTools.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Utilities/CCTextureIO.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreComposite/Utilities/FastClear/FastClear.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Lv1aqC/Sources/CoreComposite/CoreCompositeKext/Userspace/CCDRMServiceConnection.m"

```
