## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

-664.2.10.0.0
-  __TEXT.__text: 0x287d48
+664.2.11.0.0
+  __TEXT.__text: 0x287e48
   __TEXT.__auth_stubs: 0xf90
   __TEXT.__objc_methlist: 0x11b48
   __TEXT.__const: 0x1027f0
-  __TEXT.__cstring: 0x33305
+  __TEXT.__cstring: 0x33325
   __TEXT.__gcc_except_tab: 0x19b4
   __TEXT.__oslogstring: 0x349c5
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x4dc8
+  __TEXT.__unwind_info: 0x4dd0
   __TEXT.__objc_classname: 0x31f1
   __TEXT.__objc_methname: 0x33d34
-  __TEXT.__objc_methtype: 0x17110
+  __TEXT.__objc_methtype: 0x17123
   __TEXT.__objc_stubs: 0x16200
   __DATA_CONST.__got: 0xc28
   __DATA_CONST.__const: 0x1380

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7490E0F0-1715-3FEB-A880-C3AFE84696FE
-  Functions: 13362
-  Symbols:   39382
-  CStrings:  19267
+  UUID: 9A2769C3-1459-3387-9771-E1D2FDB8FEB8
+  Functions: 13363
+  Symbols:   39384
+  CStrings:  19268
 
Symbols:
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.15
Functions:
~ -[LearnedFusionNetworkPostANEStage processTilePipelineStage:] : 2176 -> 2212
~ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:] : 684 -> 716
~ -[LearnedFusionNetworkStage runLearnedFusionWithParams:outputLumaTexture:outputChromaTexture:processingOptions:] : 2328 -> 2420
~ -[LearnedDemosaicNetworkPreANEStage initWithMetal:].cold.1 : 100 -> 96
~ -[LearnedDemosaicNetworkPostANEStage initWithMetal:].cold.1 : 100 -> 96
~ -[LearnedDemosaicNetworkStage setupNetwork].cold.1 : 100 -> 104
~ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.4 : 100 -> 104
~ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.7 : 132 -> 96
+ -[LearnedDemosaicNetworkStage getNetworkPath].cold.1
CStrings:
+ "^{?=ffBB}16@0:8"
+ "consts->hrGainDownRatio >= 1.0f"
+ "{?=\"outGain\"f\"hrGainDownRatio\"f\"rotateTile180\"B\"isQuadra\"B}"
- "^{?=fBB}16@0:8"
- "{?=\"outGain\"f\"rotateTile180\"B\"isQuadra\"B}"

```
