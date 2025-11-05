## Hydra

> `/System/Library/PrivateFrameworks/Hydra.framework/Versions/C/Hydra`

```diff

-4.2.4.0.0
-  __TEXT.__text: 0xb134
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0xebc
+4.2.6.0.0
+  __TEXT.__text: 0xb0a4
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_methlist: 0x115c
   __TEXT.__gcc_except_tab: 0xe70
   __TEXT.__cstring: 0x929
-  __TEXT.__const: 0x1a8
+  __TEXT.__const: 0x1c0
   __TEXT.__unwind_info: 0x638
   __TEXT.__objc_classname: 0x15b
   __TEXT.__objc_methname: 0x2792

   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb90
+  __DATA_CONST.__objc_selrefs: 0xc30
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x1c8
+  __AUTH_CONST.__auth_got: 0x1d0
   __AUTH_CONST.__const: 0x420
   __AUTH_CONST.__cfstring: 0x11c0
-  __AUTH_CONST.__objc_const: 0x2840
+  __AUTH_CONST.__objc_const: 0x2358
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0x1e4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DE9CC0B9-D16B-3339-BE2E-861D041BADDF
+  UUID: DF104CC3-60BF-3EB7-AB62-4902FDE0B210
   Functions: 368
-  Symbols:   1146
+  Symbols:   1147
   CStrings:  1012
 
Symbols:
+ _Z20_ticksToMicroSecondsy.cold.1
+ __ZNKSt3__16vectorIU8__strongP12HYDSceneNodeNS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIU8__strongP12HYDSceneNodeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorIU8__strongP12HYDSceneNodeNS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorIU8__strongP12HYDSceneNodeNS_9allocatorIS3_EEE9push_backB8ne190102ERU8__strongKS2_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ _memcpy
- __ZNKSt3__16vectorIU8__strongP12HYDSceneNodeNS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIU8__strongP12HYDSceneNodeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__121__unwrap_and_dispatchB8ne180100INS_10__overloadINS_11__move_loopINS_17_ClassicAlgPolicyEEENS_14__move_trivialEEEPU8__strongP12HYDSceneNodeSA_SA_Li0EEENS_4pairIT0_T2_EESC_T1_SD_
- __ZNSt3__16vectorIU8__strongP12HYDSceneNodeNS_9allocatorIS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorIU8__strongP12HYDSceneNodeNS_9allocatorIS3_EEE9push_backB8ne180100ERU8__strongKS2_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
Functions:
~ -[HYDCamera mutableCopyWithZone:] : 480 -> 472
~ -[HYDCamera setFromParameters:focus:distance:focalLength:standardFocalLength:horizontalAperture:verticalAperture:scaleBias:projection:leftBottomNear:rightTopFar:clipMin:clipMax:isZUp:] : 396 -> 388
~ -[HYDCamera setFromLerp:from:to:] : 1284 -> 1268
~ -[HYDExporter threadLoop] : 296 -> 300
~ -[HYDExporter start] : 152 -> 144
~ -[HYDLoadingProgressRenderer drawInMTKView:] : 1284 -> 1272
~ __Z20_ticksToMicroSecondsy : 104 -> 88
~ -[HYDRenderer requestFrameInternal] : 72 -> 68
~ -[HYDRenderer requestFrame] : 80 -> 76
~ -[HYDRenderer transitionToCamera:] : 300 -> 296
~ -[HYDRenderer exportAnimation:] : 236 -> 244
~ -[HYDRenderer loadAssetsAsync:limitFileSizeTo:complete:] : 364 -> 360
~ -[HYDRenderer assetPathAtPoint:wsPoint:wsNormal:] : 148 -> 168
~ -[HYDRenderer lookAt:size:] : 1380 -> 1400
~ -[HYDRenderer drawInMTKView:] : 1168 -> 1160
~ -[HYDRenderingServiceProxy loadStage:limitFileSizeTo:error:] : 856 -> 844
~ -[HYDRenderingServiceProxy loadStageAsync:limitFileSizeTo:completeCallback:] : 516 -> 512
~ -[HYDRenderingServiceProxy transformStage:] : 768 -> 760
~ -[HYDRenderingServiceProxy optimize:error:] : 460 -> 452
~ ___43-[HYDRenderingServiceProxy optimize:error:]_block_invoke : 68 -> 72
~ -[HYDStageTransformParams bbox] : 12 -> 20
~ -[HYDStageTransformParams rotation] : 12 -> 20
~ -[HYDRenderParams init] : 116 -> 112
~ __ZNSt3__16vectorIU8__strongP12HYDSceneNodeNS_9allocatorIS3_EEE9push_backB8ne180100ERU8__strongKS2_ -> __ZNSt3__16vectorIU8__strongP12HYDSceneNodeNS_9allocatorIS3_EEE9push_backB8ne190102ERU8__strongKS2_ : 292 -> 260
~ __Z23buildHierarchialPathRecP15NSMutableStringP12HYDSceneNode : 252 -> 248
~ -[HYDSceneNode removeChildAt:] : 92 -> 116
~ __ZNSt3__121__unwrap_and_dispatchB8ne180100INS_10__overloadINS_11__move_loopINS_17_ClassicAlgPolicyEEENS_14__move_trivialEEEPU8__strongP12HYDSceneNodeSA_SA_Li0EEENS_4pairIT0_T2_EESC_T1_SD_ -> __ZNSt3__16vectorIU8__strongP12HYDSceneNodeNS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev : 96 -> 128
~ __ZNSt3__16vectorIU8__strongP12HYDSceneNodeNS_9allocatorIS3_EEE16__destroy_vectorclB8ne180100Ev -> _Z20_ticksToMicroSecondsy.cold.1 : 128 -> 20

```
