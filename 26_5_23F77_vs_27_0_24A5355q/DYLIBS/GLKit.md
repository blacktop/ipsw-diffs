## GLKit

> `/System/Library/Frameworks/GLKit.framework/GLKit`

```diff

 129.0.0.0.0
-  __TEXT.__text: 0x1b5a4
-  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__text: 0x1c200
   __TEXT.__objc_methlist: 0x2cc8
   __TEXT.__const: 0x19c
-  __TEXT.__cstring: 0x212d
+  __TEXT.__cstring: 0x213d
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__unwind_info: 0x5c8
-  __TEXT.__objc_classname: 0x295
-  __TEXT.__objc_methname: 0x6b7b
-  __TEXT.__objc_methtype: 0x125d
-  __TEXT.__objc_stubs: 0x3240
-  __DATA_CONST.__got: 0x218
+  __TEXT.__unwind_info: 0x5b8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3a0
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1940
   __DATA_CONST.__objc_superrefs: 0xd0
-  __AUTH_CONST.__auth_got: 0x670
+  __DATA_CONST.__got: 0x218
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x2040
   __AUTH_CONST.__objc_const: 0x5bd0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x548
   __DATA.__data: 0x528
   __DATA.__bss: 0x9e8

   - /System/Library/PrivateFrameworks/TextureIO.framework/TextureIO
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 96883A64-F7DF-3F39-A2A4-E18214469AAF
+  UUID: 264F60B3-4F1B-36CC-B3CF-4F1E73CFA49C
   Functions: 978
-  Symbols:   3268
-  CStrings:  2197
+  Symbols:   3274
+  CStrings:  597
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x4
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[GLKEffect init] : 448 -> 452
~ __modelviewMatrixMask : 488 -> 496
~ __useTexCoordAttribMask : 328 -> 332
~ __texturingEnabledMask : 348 -> 352
~ __normalizedNormalsMask : 304 -> 308
~ __vNormalEyeMask : 336 -> 340
~ __vPositionEyeMask : 508 -> 516
~ -[GLKEffect initWithPropertyArray:] : 984 -> 992
~ __lightStateChanged : 480 -> 484
~ -[GLKEffect setTextureIndices] : 620 -> 632
~ -[GLKEffect useTexCoordAttrib] : 240 -> 244
~ -[GLKEffect createAndUseProgramWithShadingHash:] : 2040 -> 2056
~ -[GLKEffect bind] : 1284 -> 1296
~ -[GLKEffect initializeMasks] : 164 -> 168
~ -[GLKEffect includeShaderTextForRootNode:] : 1396 -> 1412
~ -[GLKMeshBufferZone newBufferWithLength:type:] : 544 -> 528
~ -[GLKMeshBufferZone destroyBuffer:] : 236 -> 216
~ -[GLKMeshBuffer _initWithLength:offset:zone:type:] : 136 -> 128
~ -[GLKMeshBuffer _initWithData:allocator:type:] : 148 -> 152
~ -[GLKMeshBuffer _initWithBytes:length:offset:allocator:zone:type:] : 312 -> 320
~ -[GLKMeshBuffer fillData:offset:] : 176 -> 172
~ -[GLKMeshBuffer copyWithZone:] : 200 -> 192
~ -[GLKMeshBufferAllocator init] : 160 -> 140
~ -[GLKMeshBufferAllocator newZoneForBuffersWithSize:andType:] : 280 -> 276
~ -[GLKMeshBufferAllocator newBufferFromZone:length:type:] : 164 -> 160
~ -[GLKSubmesh initWithMesh:submesh:error:] : 756 -> 740
~ -[GLKMesh initWithMesh:error:] : 980 -> 948
~ +[GLKMesh _createMeshesFromObject:newMeshes:sourceMeshes:error:] : 444 -> 452
~ +[GLKMesh newMeshesFromAsset:sourceMeshes:error:] : 456 -> 452
~ _MDLMeshBufferMapFunction : 60 -> 12
~ _MDLSubmeshFunction : 60 -> 12
~ _MDLMeshFunction : 60 -> 12
~ -[GLKEffectPropertyConstantColor init] : 124 -> 132
~ -[GLKEffectPropertyConstantColor setShaderBindings] : 112 -> 116
~ -[GLKEffectPropertyConstantColor bind] : 84 -> 88
~ -[GLKEffectPropertyConstantColor enabled] : 16 -> 20
~ -[GLKEffectPropertyConstantColor setEnabled:] : 16 -> 20
~ -[GLKEffectPropertyFog init] : 168 -> 188
~ -[GLKEffectPropertyFog initializeMasks] : 264 -> 276
~ __modeMask : 276 -> 304
~ -[GLKEffectPropertyFog setEnabled:] : 256 -> 264
~ -[GLKEffectPropertyFog setMode:] : 144 -> 148
~ -[GLKEffectPropertyFog setDensity:] : 88 -> 92
~ -[GLKEffectPropertyFog setStart:] : 88 -> 92
~ -[GLKEffectPropertyFog setEnd:] : 88 -> 92
~ -[GLKEffectPropertyFog includeVshShaderTextForRootNode:] : 116 -> 120
~ -[GLKEffectPropertyFog includeFshShaderTextForRootNode:] : 116 -> 120
~ +[GLKEffectPropertyFog setStaticMasksWithVshRoot:fshRoot:] : 256 -> 260
~ -[GLKEffectPropertyFog setShaderBindings] : 204 -> 224
~ -[GLKEffectPropertyFog bind] : 280 -> 316
~ -[GLKEffectPropertyFog description] : 368 -> 388
~ -[GLKEffectPropertyFog enabled] : 16 -> 20
~ -[GLKEffectPropertyFog mode] : 16 -> 20
~ -[GLKEffectPropertyFog density] : 16 -> 20
~ -[GLKEffectPropertyFog start] : 16 -> 20
~ -[GLKEffectPropertyFog end] : 16 -> 20
~ -[GLKEffectPropertyFog modeLoc] : 16 -> 20
~ -[GLKEffectPropertyFog setModeLoc:] : 16 -> 20
~ -[GLKEffectPropertyFog colorLoc] : 16 -> 20
~ -[GLKEffectPropertyFog setColorLoc:] : 16 -> 20
~ -[GLKEffectPropertyFog densityLoc] : 16 -> 20
~ -[GLKEffectPropertyFog setDensityLoc:] : 16 -> 20
~ -[GLKEffectPropertyFog startLoc] : 16 -> 20
~ -[GLKEffectPropertyFog setStartLoc:] : 16 -> 20
~ -[GLKEffectPropertyFog endLoc] : 16 -> 20
~ -[GLKEffectPropertyFog setEndLoc:] : 16 -> 20
~ -[GLKEffectPropertyLight initWithTransform:lightingType:firstLight:] : 324 -> 392
~ -[GLKEffectPropertyLight setGLDefaults] : 304 -> 340
~ -[GLKEffectPropertyLight initializeMasks] : 164 -> 176
~ __setMasks : 896 -> 968
~ -[GLKEffectPropertyLight setShaderBindings] : 716 -> 768
~ -[GLKEffectPropertyLight setTransform:] : 84 -> 88
~ -[GLKEffectPropertyLight setSpotDirection:] : 244 -> 248
~ -[GLKEffectPropertyLight setAmbientColor:] : 160 -> 164
~ -[GLKEffectPropertyLight setPosition:] : 972 -> 968
~ __attenuateMask : 424 -> 472
~ -[GLKEffectPropertyLight setNormalize:] : 20 -> 24
~ -[GLKEffectPropertyLight setEnabled:] : 176 -> 184
~ -[GLKEffectPropertyLight setLightingType:] : 140 -> 148
~ -[GLKEffectPropertyLight setSpotExponent:] : 88 -> 92
~ -[GLKEffectPropertyLight setQuadraticAttenuation:] : 120 -> 128
~ -[GLKEffectPropertyLight setLinearAttenuation:] : 120 -> 128
~ -[GLKEffectPropertyLight setConstantAttenuation:] : 120 -> 128
~ -[GLKEffectPropertyLight setSpotCutoff:] : 304 -> 332
~ -[GLKEffectPropertyLight spotCutoff] : 16 -> 20
~ +[GLKEffectPropertyLight setStaticMasksWithVshRoot:fshRoot:] : 368 -> 376
~ -[GLKEffectPropertyLight includeVshShaderTextForRootNode:] : 120 -> 124
~ -[GLKEffectPropertyLight includeFshShaderTextForRootNode:] : 120 -> 124
~ -[GLKEffectPropertyLight isSpot] : 68 -> 72
~ -[GLKEffectPropertyLight bind] : 552 -> 616
~ -[GLKEffectPropertyLight setLightIndex:] : 144 -> 164
~ -[GLKEffectPropertyLight description] : 580 -> 604
~ -[GLKEffectPropertyLight dealloc] : 84 -> 88
~ -[GLKEffectPropertyLight enabled] : 16 -> 20
~ -[GLKEffectPropertyLight spotExponent] : 16 -> 20
~ -[GLKEffectPropertyLight spotCutoffDegrees] : 16 -> 20
~ -[GLKEffectPropertyLight setSpotCutoffDegrees:] : 16 -> 20
~ -[GLKEffectPropertyLight constantAttenuation] : 16 -> 20
~ -[GLKEffectPropertyLight linearAttenuation] : 16 -> 20
~ -[GLKEffectPropertyLight quadraticAttenuation] : 16 -> 20
~ -[GLKEffectPropertyLight effectDirtyUniforms] : 16 -> 20
~ -[GLKEffectPropertyLight setEffectDirtyUniforms:] : 16 -> 20
~ -[GLKEffectPropertyLight transform] : 16 -> 20
~ -[GLKEffectPropertyLight positionEyeStale] : 16 -> 20
~ -[GLKEffectPropertyLight setPositionEyeStale:] : 16 -> 20
~ -[GLKEffectPropertyLight positionEyeLoc] : 16 -> 20
~ -[GLKEffectPropertyLight setPositionEyeLoc:] : 16 -> 20
~ -[GLKEffectPropertyLight ambientLoc] : 16 -> 20
~ -[GLKEffectPropertyLight setAmbientLoc:] : 16 -> 20
~ -[GLKEffectPropertyLight diffuseLoc] : 16 -> 20
~ -[GLKEffectPropertyLight setDiffuseLoc:] : 16 -> 20
~ -[GLKEffectPropertyLight specularLoc] : 16 -> 20
~ -[GLKEffectPropertyLight setSpecularLoc:] : 16 -> 20
~ -[GLKEffectPropertyLight normalizedSpotDirectionEyeLoc] : 16 -> 20
~ -[GLKEffectPropertyLight setNormalizedSpotDirectionEyeLoc:] : 16 -> 20
~ -[GLKEffectPropertyLight spotExponentLoc] : 16 -> 20
~ -[GLKEffectPropertyLight setSpotExponentLoc:] : 16 -> 20
~ -[GLKEffectPropertyLight spotCutoffLoc] : 16 -> 20
~ -[GLKEffectPropertyLight setSpotCutoffLoc:] : 16 -> 20
~ -[GLKEffectPropertyLight constantAttenuationLoc] : 16 -> 20
~ -[GLKEffectPropertyLight setConstantAttenuationLoc:] : 16 -> 20
~ -[GLKEffectPropertyLight linearAttenuationLoc] : 16 -> 20
~ -[GLKEffectPropertyLight setLinearAttenuationLoc:] : 16 -> 20
~ -[GLKEffectPropertyLight quadraticAttenuationLoc] : 16 -> 20
~ -[GLKEffectPropertyLight setQuadraticAttenuationLoc:] : 16 -> 20
~ -[GLKEffectPropertyLight normalizeLoc] : 16 -> 20
~ -[GLKEffectPropertyLight setNormalizeLoc:] : 16 -> 20
~ -[GLKEffectPropertyLight ambientTermLoc] : 16 -> 20
~ -[GLKEffectPropertyLight setAmbientTermLoc:] : 16 -> 20
~ -[GLKEffectPropertyLight lightIndex] : 16 -> 20
~ -[GLKEffectPropertyLight lightingType] : 16 -> 20
~ -[GLKEffectPropertyLight firstLight] : 16 -> 20
~ -[GLKEffectPropertyLight setFirstLight:] : 16 -> 20
~ -[GLKEffectPropertyMaterial init] : 172 -> 196
~ -[GLKEffectPropertyMaterial setEffectDirtyUniforms:] : 44 -> 48
~ -[GLKEffectPropertyMaterial setAmbientColor:] : 160 -> 164
~ -[GLKEffectPropertyMaterial setEmissiveColor:] : 160 -> 164
~ -[GLKEffectPropertyMaterial initializeMasks] : 112 -> 116
~ __specularColorMask : 312 -> 340
~ -[GLKEffectPropertyMaterial setShininess:] : 88 -> 92
~ -[GLKEffectPropertyMaterial setShaderBindings] : 204 -> 224
~ +[GLKEffectPropertyMaterial setStaticMasksWithVshRoot:fshRoot:] : 288 -> 296
~ -[GLKEffectPropertyMaterial includeVshShaderTextForRootNode:] : 116 -> 120
~ -[GLKEffectPropertyMaterial includeFshShaderTextForRootNode:] : 116 -> 120
~ -[GLKEffectPropertyMaterial bind] : 292 -> 316
~ -[GLKEffectPropertyMaterial description] : 324 -> 328
~ -[GLKEffectPropertyMaterial shininess] : 16 -> 20
~ -[GLKEffectPropertyMaterial effectDirtyUniforms] : 16 -> 20
~ -[GLKEffectPropertyMaterial _ambientColorLoc] : 16 -> 20
~ -[GLKEffectPropertyMaterial set_ambientColorLoc:] : 16 -> 20
~ -[GLKEffectPropertyMaterial _diffuseColorLoc] : 16 -> 20
~ -[GLKEffectPropertyMaterial set_diffuseColorLoc:] : 16 -> 20
~ -[GLKEffectPropertyMaterial _specularColorLoc] : 16 -> 20
~ -[GLKEffectPropertyMaterial set_specularColorLoc:] : 16 -> 20
~ -[GLKEffectPropertyMaterial _emissiveColorLoc] : 16 -> 20
~ -[GLKEffectPropertyMaterial set_emissiveColorLoc:] : 16 -> 20
~ -[GLKEffectPropertyMaterial _shininessLoc] : 16 -> 20
~ -[GLKEffectPropertyMaterial set_shininessLoc:] : 16 -> 20
~ -[GLKEffectPropertyTexGen initWithMode:coord:] : 256 -> 284
~ -[GLKEffectPropertyTexGen setMode:] : 188 -> 196
~ -[GLKEffectPropertyTexGen setPlane:] : 160 -> 164
~ -[GLKEffectPropertyTexGen setModeNameString:] : 76 -> 80
~ -[GLKEffectPropertyTexGen setPlaneNameString:] : 76 -> 80
~ -[GLKEffectPropertyTexGen setTextureIndex:] : 16 -> 20
~ -[GLKEffectPropertyTexGen setShaderBindings] : 292 -> 308
~ -[GLKEffectPropertyTexGen initializeMasks] : 116 -> 120
~ -[GLKEffectPropertyTexGen bind] : 160 -> 176
~ -[GLKEffectPropertyTexGen dealloc] : 124 -> 136
~ -[GLKEffectPropertyTexGen mode] : 16 -> 20
~ -[GLKEffectPropertyTexGen plane] : 16 -> 20
~ -[GLKEffectPropertyTexGen coord] : 16 -> 20
~ -[GLKEffectPropertyTexGen eyePlaneByInvModelview] : 16 -> 20
~ -[GLKEffectPropertyTexGen setEyePlaneByInvModelview:] : 16 -> 20
~ -[GLKEffectPropertyTexGen modeLoc] : 16 -> 20
~ -[GLKEffectPropertyTexGen setModeLoc:] : 16 -> 20
~ -[GLKEffectPropertyTexGen planeLoc] : 16 -> 20
~ -[GLKEffectPropertyTexGen setPlaneLoc:] : 16 -> 20
~ -[GLKEffectPropertyTexGen eyePlaneByInvModelviewLoc] : 16 -> 20
~ -[GLKEffectPropertyTexGen setEyePlaneByInvModelviewLoc:] : 16 -> 20
~ -[GLKEffectPropertyTexGen modeNameString] : 16 -> 20
~ -[GLKEffectPropertyTexGen planeNameString] : 16 -> 20
~ -[GLKEffectPropertyTexGen textureIndex] : 16 -> 20
~ -[GLKEffectPropertyTexture init] : 232 -> 272
~ -[GLKEffectPropertyTexture texGenS] : 356 -> 388
~ __texGenSMask : 548 -> 632
~ -[GLKEffectPropertyTexture texGenT] : 356 -> 388
~ __texGenTMask : 548 -> 632
~ -[GLKEffectPropertyTexture texGenR] : 356 -> 388
~ __texGenRMask : 548 -> 632
~ -[GLKEffectPropertyTexture setTextureIndex:] : 524 -> 540
~ __setMasks : 964 -> 1076
~ -[GLKEffectPropertyTexture setShaderBindings] : 332 -> 356
~ +[GLKEffectPropertyTexture setStaticMasksWithVshRoot:fshRoot:] : 328 -> 332
~ -[GLKEffectPropertyTexture includeVshShaderTextForRootNode:] : 112 -> 116
~ -[GLKEffectPropertyTexture includeFshShaderTextForRootNode:] : 120 -> 124
~ -[GLKEffectPropertyTexture setUnit2dNameString:] : 84 -> 88
~ -[GLKEffectPropertyTexture setUnitCubeNameString:] : 84 -> 88
~ -[GLKEffectPropertyTexture setEnabled:] : 492 -> 536
~ -[GLKEffectPropertyTexture initializeMasks] : 288 -> 300
~ -[GLKEffectPropertyTexture setEnvMode:] : 176 -> 196
~ -[GLKEffectPropertyTexture setTarget:] : 440 -> 488
~ -[GLKEffectPropertyTexture setMatrixEnabled:] : 124 -> 132
~ -[GLKEffectPropertyTexture normalizedNormalsMask] : 192 -> 208
~ __reflectionMappingEnabled : 88 -> 96
~ -[GLKEffectPropertyTexture vPositionEyeMask] : 240 -> 256
~ -[GLKEffectPropertyTexture vNormalEyeMask] : 192 -> 208
~ -[GLKEffectPropertyTexture useTexCoordAttribMask] : 204 -> 220
~ -[GLKEffectPropertyTexture description] : 276 -> 292
~ -[GLKEffectPropertyTexture bind] : 388 -> 416
~ -[GLKEffectPropertyTexture dealloc] : 172 -> 196
~ -[GLKEffectPropertyTexture target] : 16 -> 20
~ -[GLKEffectPropertyTexture enabled] : 16 -> 20
~ -[GLKEffectPropertyTexture filePath] : 16 -> 20
~ -[GLKEffectPropertyTexture textureIndex] : 16 -> 20
~ -[GLKEffectPropertyTexture matrixEnabled] : 16 -> 20
~ -[GLKEffectPropertyTexture envMode] : 16 -> 20
~ -[GLKEffectPropertyTexture unit2dNameString] : 16 -> 20
~ -[GLKEffectPropertyTexture unitCubeNameString] : 16 -> 20
~ -[GLKEffectPropertyTexture name] : 16 -> 20
~ -[GLKEffectPropertyTexture setName:] : 16 -> 20
~ -[GLKEffectPropertyTexture unit2dLoc] : 16 -> 20
~ -[GLKEffectPropertyTexture setUnit2dLoc:] : 16 -> 20
~ -[GLKEffectPropertyTexture unitCubeLoc] : 16 -> 20
~ -[GLKEffectPropertyTexture setUnitCubeLoc:] : 16 -> 20
~ -[GLKEffectPropertyTexture texGenArray] : 16 -> 20
~ -[GLKEffectPropertyTransform setShaderBindings] : 148 -> 160
~ -[GLKEffectPropertyTransform bind] : 216 -> 228
~ -[GLKEffectPropertyTransform mvpMatrixLoc] : 16 -> 20
~ -[GLKEffectPropertyTransform setMvpMatrixLoc:] : 16 -> 20
~ -[GLKEffectPropertyTransform modelviewMatrixLoc] : 16 -> 20
~ -[GLKEffectPropertyTransform setModelviewMatrixLoc:] : 16 -> 20
~ -[GLKEffectPropertyTransform projectionMatrixLoc] : 16 -> 20
~ -[GLKEffectPropertyTransform setProjectionMatrixLoc:] : 16 -> 20
~ -[GLKEffectPropertyTransform normalMatrixLoc] : 16 -> 20
~ -[GLKEffectPropertyTransform setNormalMatrixLoc:] : 16 -> 20
~ -[GLKEffectPropertyTransform invModelviewMatrixLoc] : 16 -> 20
~ -[GLKEffectPropertyTransform setInvModelviewMatrixLoc:] : 16 -> 20
~ _GLKMatrix4Invert : 624 -> 628
~ _GLKQuaternionMakeWithMatrix3 : 444 -> 448
~ _GLKQuaternionMakeWithMatrix4 : 432 -> 436
~ _GLKQuaternionRotateVector3Array : 228 -> 216
~ _GLKQuaternionRotateVector4Array : 228 -> 216
~ _GLKMatrixStackCreate : 272 -> 276
~ _GLKMatrixStackGetModifyCount : 64 -> 68
~ _GLKMatrixStackPush : 356 -> 368
~ _GLKMatrixStackLoadMatrix4 : 148 -> 152
~ _GLKMatrixStackGetMatrix4 : 76 -> 80
~ _GLKMatrixStackGetMatrix3 : 108 -> 112
~ _GLKMatrixStackGetMatrix2 : 68 -> 72
~ _GLKMatrixStackGetMatrix4Inverse : 624 -> 628
~ _GLKMatrixStackGetMatrix4InverseTranspose : 656 -> 660
~ _GLKMatrixStackGetMatrix3Inverse : 508 -> 512
~ _GLKMatrixStackGetMatrix3InverseTranspose : 652 -> 676
~ _GLKMatrixStackMultiplyMatrix4 : 232 -> 236
~ _GLKMatrixStackMultiplyMatrixStack : 236 -> 244
~ _GLKMatrixStackTranslate : 120 -> 124
~ _GLKMatrixStackTranslateWithVector3 : 120 -> 124
~ _GLKMatrixStackTranslateWithVector4 : 120 -> 124
~ _GLKMatrixStackScale : 188 -> 192
~ _GLKMatrixStackRotate : 344 -> 348
~ _GLKMatrixStackRotateX : 236 -> 240
~ _GLKMatrixStackRotateY : 232 -> 236
~ _GLKMatrixStackRotateZ : 232 -> 236
~ __GLKMatrixFormatDescription : 308 -> 312
~ -[GLKTextureTXR uploadToGLTexture:error:] : 3200 -> 3212
~ -[GLKTexture uploadToGLTexture:error:] : 984 -> 988
~ -[GLKTexture determinePVRFormat:] : 492 -> 500
~ +[GLKTextureLoader commonCubeMapWithContentsOfURL:options:error:lock:glContext:] : 1588 -> 1612
~ -[GLKReflectionMapEffect init] : 272 -> 284
~ -[GLKReflectionMapEffect setMatrix:] : 48 -> 52
~ -[GLKReflectionMapEffect prepareToDraw] : 180 -> 192
~ -[GLKReflectionMapEffect dealloc] : 84 -> 88
~ -[GLKReflectionMapEffect textureCubeMap] : 16 -> 20
~ -[GLKReflectionMapEffect dirtyUniforms] : 16 -> 20
~ -[GLKReflectionMapEffect setDirtyUniforms:] : 16 -> 20
~ -[GLKReflectionMapEffect matrixLoc] : 16 -> 20
~ -[GLKReflectionMapEffect setMatrixLoc:] : 16 -> 20
~ _GLKMatrix3Invert : 612 -> 616
~ -[GLKHashableBigInt hash] : 88 -> 96
~ -[GLKView _initCommon] : 348 -> 376
~ -[GLKView initWithCoder:] : 328 -> 348
~ -[GLKView encodeWithCoder:] : 212 -> 232
~ -[GLKView dealloc] : 184 -> 188
~ -[GLKView _createFramebuffer] : 1224 -> 1308
~ -[GLKView _deleteFramebuffer] : 336 -> 372
~ -[GLKView _setFramebuffer:] : 252 -> 272
~ -[GLKView _resolveAndDiscard] : 300 -> 324
~ -[GLKView _presentFramebuffer] : 84 -> 92
~ -[GLKView _display:] : 288 -> 304
~ -[GLKView context] : 16 -> 20
~ -[GLKView setContext:] : 156 -> 160
~ -[GLKView drawableColorFormat] : 16 -> 20
~ -[GLKView setDrawableColorFormat:] : 44 -> 52
~ -[GLKView drawableDepthFormat] : 16 -> 20
~ -[GLKView setDrawableDepthFormat:] : 44 -> 52
~ -[GLKView drawableStencilFormat] : 16 -> 20
~ -[GLKView setDrawableStencilFormat:] : 44 -> 52
~ -[GLKView drawableMultisample] : 16 -> 20
~ -[GLKView setDrawableMultisample:] : 44 -> 52
~ -[GLKView snapshot] : 616 -> 632
~ -[GLKView setEnableSetNeedsDisplay:] : 16 -> 20
~ -[GLKView enableSetNeedsDisplay] : 16 -> 20
~ -[GLKView displayLayer:] : 32 -> 36
~ -[GLKView setContentScaleFactor:] : 144 -> 152
~ -[GLKView layoutSubviews] : 240 -> 244
~ -[GLKView inDraw] : 16 -> 20
~ -[GLKView setInDraw:] : 16 -> 20
~ -[GLKView drawableProperties] : 16 -> 20
~ -[GLKView shouldDeleteFramebuffer] : 16 -> 20
~ -[GLKView setShouldDeleteFramebuffer:] : 16 -> 20
~ -[GLKView resolveFramebuffer] : 16 -> 20
~ -[GLKView setResolveFramebuffer:] : 16 -> 20
~ -[GLKView resolveColorRenderbuffer] : 16 -> 20
~ -[GLKView setResolveColorRenderbuffer:] : 16 -> 20
~ -[GLKView multisampleFramebuffer] : 16 -> 20
~ -[GLKView setMultisampleFramebuffer:] : 16 -> 20
~ -[GLKView multisampleColorRenderbuffer] : 16 -> 20
~ -[GLKView setMultisampleColorRenderbuffer:] : 16 -> 20
~ -[GLKView depthRenderbuffer] : 16 -> 20
~ -[GLKView setDepthRenderbuffer:] : 16 -> 20
~ -[GLKView stencilRenderbuffer] : 16 -> 20
~ -[GLKView setStencilRenderbuffer:] : 16 -> 20
~ -[GLKView depthStencilRenderbuffer] : 16 -> 20
~ -[GLKView setDepthStencilRenderbuffer:] : 16 -> 20
~ -[GLKView viewContentScaleFactor] : 16 -> 20
~ -[GLKView setViewContentScaleFactor:] : 16 -> 20
~ -[GLKView delegate] : 16 -> 20
~ -[GLKView setDelegate:] : 16 -> 20
~ -[GLKView drawableWidth] : 16 -> 20
~ -[GLKView drawableHeight] : 16 -> 20
~ -[GLKView drawRectIMP] : 16 -> 20
~ -[GLKView setDrawRectIMP:] : 16 -> 20
~ -[GLKViewController _initCommon] : 308 -> 332
~ -[GLKViewController initWithCoder:] : 240 -> 248
~ -[GLKViewController encodeWithCoder:] : 156 -> 168
~ -[GLKViewController dealloc] : 172 -> 184
~ -[GLKViewController _configureNotifications] : 256 -> 264
~ -[GLKViewController _createDisplayLinkForScreen:] : 216 -> 232
~ -[GLKViewController _updateAndDraw] : 520 -> 592
~ -[GLKViewController _resumeByNotification] : 32 -> 36
~ -[GLKViewController _updateScreenIfChanged] : 256 -> 276
~ -[GLKViewController viewDidUnload] : 84 -> 88
~ -[GLKViewController viewWillAppear:] : 100 -> 104
~ -[GLKViewController viewWillDisappear:] : 92 -> 96
~ -[GLKViewController preferredFramesPerSecond] : 16 -> 20
~ -[GLKViewController setPreferredFramesPerSecond:] : 84 -> 96
~ -[GLKViewController setPaused:] : 300 -> 336
~ -[GLKViewController isPaused] : 16 -> 20
~ -[GLKViewController timeSinceFirstResume] : 80 -> 88
~ -[GLKViewController timeSinceLastResume] : 80 -> 88
~ -[GLKViewController setPauseOnWillResignActive:] : 16 -> 20
~ -[GLKViewController pauseOnWillResignActive] : 16 -> 20
~ -[GLKViewController setResumeOnDidBecomeActive:] : 16 -> 20
~ -[GLKViewController resumeOnDidBecomeActive] : 16 -> 20
~ -[GLKViewController screen] : 16 -> 20
~ -[GLKViewController displayLink] : 16 -> 20
~ -[GLKViewController displayLinkPaused] : 16 -> 20
~ -[GLKViewController setDisplayLinkPaused:] : 16 -> 20
~ -[GLKViewController displayLinkMessenger] : 16 -> 20
~ -[GLKViewController viewIsVisible] : 16 -> 20
~ -[GLKViewController setViewIsVisible:] : 16 -> 20
~ -[GLKViewController firstResumeOccurred] : 16 -> 20
~ -[GLKViewController setFirstResumeOccurred:] : 16 -> 20
~ -[GLKViewController timeSinceFirstResumeStartTime] : 16 -> 20
~ -[GLKViewController setTimeSinceFirstResumeStartTime:] : 16 -> 20
~ -[GLKViewController lastResumeOccurred] : 16 -> 20
~ -[GLKViewController setLastResumeOccurred:] : 16 -> 20
~ -[GLKViewController timeSinceLastResumeStartTime] : 16 -> 20
~ -[GLKViewController setTimeSinceLastResumeStartTime:] : 16 -> 20
~ -[GLKViewController lastUpdateOccurred] : 16 -> 20
~ -[GLKViewController setLastUpdateOccurred:] : 16 -> 20
~ -[GLKViewController timeSinceLastUpdatePreviousTime] : 16 -> 20
~ -[GLKViewController setTimeSinceLastUpdatePreviousTime:] : 16 -> 20
~ -[GLKViewController lastDrawOccurred] : 16 -> 20
~ -[GLKViewController setLastDrawOccurred:] : 16 -> 20
~ -[GLKViewController timeSinceLastDrawPreviousTime] : 16 -> 20
~ -[GLKViewController setTimeSinceLastDrawPreviousTime:] : 16 -> 20
~ -[GLKViewController updateIMP] : 16 -> 20
~ -[GLKViewController setUpdateIMP:] : 16 -> 20
~ -[GLKViewController delegate] : 16 -> 20
~ -[GLKViewController setDelegate:] : 16 -> 20
~ -[GLKViewController screenFramesPerSecond] : 16 -> 20
~ -[GLKViewController setScreenFramesPerSecond:] : 16 -> 20
~ -[GLKViewController framesPerSecond] : 16 -> 20
~ -[GLKViewController framesDisplayed] : 16 -> 20
~ -[GLKViewController timeSinceLastUpdate] : 16 -> 20
~ -[GLKViewController timeSinceLastDraw] : 16 -> 20
CStrings:
- "#16@0:8"
- "(_GLKMatrix3=\"\"{?=\"m00\"f\"m01\"f\"m02\"f\"m10\"f\"m11\"f\"m12\"f\"m20\"f\"m21\"f\"m22\"f}\"m\"[9f])"
- "(_GLKMatrix3={?=fffffffff}[9f])16@0:8"
- "(_GLKMatrix4=\"\"{?=\"m00\"f\"m01\"f\"m02\"f\"m03\"f\"m10\"f\"m11\"f\"m12\"f\"m13\"f\"m20\"f\"m21\"f\"m22\"f\"m23\"f\"m30\"f\"m31\"f\"m32\"f\"m33\"f}\"m\"[16f])"
- "(_GLKMatrix4={?=ffffffffffffffff}[16f])16@0:8"
- "(_GLKVector3=\"\"{?=\"x\"f\"y\"f\"z\"f}\"\"{?=\"r\"f\"g\"f\"b\"f}\"\"{?=\"s\"f\"t\"f\"p\"f}\"v\"[3f])"
- "(_GLKVector3={?=fff}{?=fff}{?=fff}[3f])16@0:8"
- "(_GLKVector4=\"\"{?=\"x\"f\"y\"f\"z\"f\"w\"f}\"\"{?=\"r\"f\"g\"f\"b\"f\"a\"f}\"\"{?=\"s\"f\"t\"f\"p\"f\"q\"f}\"v\"[4f])"
- "(_GLKVector4={?=ffff}{?=ffff}{?=ffff}[4f])16@0:8"
- "*"
- "*16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<GLKViewControllerDelegate>\""
- "@\"<GLKViewDelegate>\""
- "@\"<MDLMeshBuffer>\"32@0:8@\"NSData\"16Q24"
- "@\"<MDLMeshBuffer>\"32@0:8Q16Q24"
- "@\"<MDLMeshBuffer>\"40@0:8@\"<MDLMeshBufferZone>\"16@\"NSData\"24Q32"
- "@\"<MDLMeshBuffer>\"40@0:8@\"<MDLMeshBufferZone>\"16Q24Q32"
- "@\"<MDLMeshBufferAllocator>\"16@0:8"
- "@\"<MDLMeshBufferZone>\"16@0:8"
- "@\"<MDLMeshBufferZone>\"24@0:8Q16"
- "@\"<MDLMeshBufferZone>\"32@0:8@\"NSArray\"16@\"NSArray\"24"
- "@\"CADisplayLink\""
- "@\"EAGLContext\""
- "@\"EAGLSharegroup\""
- "@\"GLKDisplayLinkMessenger\""
- "@\"GLKEffect\""
- "@\"GLKEffectPropertyConstantColor\""
- "@\"GLKEffectPropertyFog\""
- "@\"GLKEffectPropertyLight\""
- "@\"GLKEffectPropertyMaterial\""
- "@\"GLKEffectPropertyTexGen\""
- "@\"GLKEffectPropertyTexture\""
- "@\"GLKEffectPropertyTransform\""
- "@\"GLKMesh\""
- "@\"GLKMeshBuffer\""
- "@\"GLKMeshBufferAllocator\""
- "@\"GLKMeshBufferZone\""
- "@\"GLKShaderBlockNode\""
- "@\"MDLMeshBufferMap\"16@0:8"
- "@\"MDLVertexDescriptor\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSData\"40@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32"
- "@\"NSLock\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableOrderedSet\""
- "@\"NSMutableString\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"TXRTexture\""
- "@\"UIScreen\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{GLKBigInt_s=QQ}16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8i16i20"
- "@28@0:8@16I24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@32@0:8@16i24C28"
- "@32@0:8Q16@24"
- "@32@0:8Q16Q24"
- "@36@0:8I16@20r*28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24Q32"
- "@40@0:8@16@24^@32"
- "@40@0:8@16Q24Q32"
- "@40@0:8@16^@24^@32"
- "@40@0:8Q16@24Q32"
- "@40@0:8^{CGImage=}16@24^@32"
- "@48@0:8@16Q24@32^@40"
- "@48@0:8Q16Q24@32Q40"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@56@0:8@16@24^@32@40@48"
- "@56@0:8@16B24^B28i36@40^@48"
- "@56@0:8@16d24@32@40^@48"
- "@56@0:8^{CGImage=}16@24^@32@40@48"
- "@56@0:8^{CGImage=}16B24^B28i36@40^@48"
- "@56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48"
- "@64@0:8@16I24I28I32@36i44@48^@56"
- "@64@0:8r^v16Q24Q32@40@48Q56"
- "@72@0:8@16d24@32@40^@48@56@64"
- "API"
- "APIs"
- "B"
- "B16@0:8"
- "B20@0:8I16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^{CGImage=}16"
- "B28@0:8I16^@20"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8^{CGImage=}16^{CGImageProvider=}24"
- "B32@0:8i16Q20i28"
- "B40@0:8@16@24^@32"
- "B40@0:8^{CGImage=}16@24^@32"
- "B52@0:8^v16^v24I32I36I40^@44"
- "B56@0:8I16@20i28i32i36i40i44^@48"
- "C"
- "C16@0:8"
- "GLKDisplayLinkMessenger"
- "GLKEffect"
- "GLKEffectProperty"
- "GLKEffectPropertyConstantColor"
- "GLKEffectPropertyFog"
- "GLKEffectPropertyLight"
- "GLKEffectPropertyMaterial"
- "GLKEffectPropertyTexGen"
- "GLKEffectPropertyTexture"
- "GLKEffectPropertyTransform"
- "GLKHashableBigInt"
- "GLKMesh"
- "GLKMeshBuffer"
- "GLKMeshBufferAllocator"
- "GLKMeshBufferHolder"
- "GLKMeshBufferZone"
- "GLKNamedEffect"
- "GLKReflectionMapEffect"
- "GLKShaderBlockNode"
- "GLKShadingHash"
- "GLKSkyboxEffect"
- "GLKSubmesh"
- "GLKTexture"
- "GLKTextureInfo"
- "GLKTextureTXR"
- "GLKView"
- "GLKViewController"
- "GLKViewDelegate"
- "GLTextureName"
- "I"
- "I16@0:8"
- "I32@0:8@16^I24"
- "MDLMeshBuffer"
- "MDLMeshBufferAllocator"
- "MDLMeshBufferZone"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSXMLParserDelegate"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T(_GLKMatrix3={?=fffffffff}[9f]),N,V_matrix"
- "T(_GLKMatrix3={?=fffffffff}[9f]),R,N,V_normalMatrix"
- "T(_GLKMatrix4={?=ffffffffffffffff}[16f]),N,V_invModelviewMatrix"
- "T(_GLKMatrix4={?=ffffffffffffffff}[16f]),N,V_modelviewMatrix"
- "T(_GLKMatrix4={?=ffffffffffffffff}[16f]),N,V_mvpMatrix"
- "T(_GLKMatrix4={?=ffffffffffffffff}[16f]),N,V_projectionMatrix"
- "T(_GLKVector3={?=fff}{?=fff}{?=fff}[3f]),N,V_center"
- "T(_GLKVector3={?=fff}{?=fff}{?=fff}[3f]),N,V_normalizedSpotDirectionEye"
- "T(_GLKVector3={?=fff}{?=fff}{?=fff}[3f]),N,V_spotDirection"
- "T(_GLKVector4={?=ffff}{?=ffff}{?=ffff}[4f]),N,V_ambientColor"
- "T(_GLKVector4={?=ffff}{?=ffff}{?=ffff}[4f]),N,V_baseLightingColor"
- "T(_GLKVector4={?=ffff}{?=ffff}{?=ffff}[4f]),N,V_color"
- "T(_GLKVector4={?=ffff}{?=ffff}{?=ffff}[4f]),N,V_constantColor"
- "T(_GLKVector4={?=ffff}{?=ffff}{?=ffff}[4f]),N,V_diffuseColor"
- "T(_GLKVector4={?=ffff}{?=ffff}{?=ffff}[4f]),N,V_emissiveColor"
- "T(_GLKVector4={?=ffff}{?=ffff}{?=ffff}[4f]),N,V_lightModelAmbientColor"
- "T(_GLKVector4={?=ffff}{?=ffff}{?=ffff}[4f]),N,V_position"
- "T(_GLKVector4={?=ffff}{?=ffff}{?=ffff}[4f]),N,V_positionEye"
- "T(_GLKVector4={?=ffff}{?=ffff}{?=ffff}[4f]),N,V_specularColor"
- "T*,N,V_fshSource"
- "T*,N,V_modeNameString"
- "T*,N,V_nameString"
- "T*,N,V_planeNameString"
- "T*,N,V_unit2dNameString"
- "T*,N,V_unitCubeNameString"
- "T*,N,V_vshSource"
- "T@\"<GLKViewControllerDelegate>\",N,V_delegate"
- "T@\"<GLKViewDelegate>\",N,V_delegate"
- "T@\"<MDLMeshBufferAllocator>\",R,&,N"
- "T@\"<MDLMeshBufferAllocator>\",R,N"
- "T@\"<MDLMeshBufferAllocator>\",R,N,V_allocator"
- "T@\"<MDLMeshBufferZone>\",R,&,N"
- "T@\"<MDLMeshBufferZone>\",R,N,V_zone"
- "T@\"CADisplayLink\",&,N,V_displayLink"
- "T@\"EAGLContext\",&,N,V_context"
- "T@\"EAGLContext\",&,V_glContext"
- "T@\"GLKDisplayLinkMessenger\",&,N,V_displayLinkMessenger"
- "T@\"GLKEffect\",N,V_effect"
- "T@\"GLKEffectPropertyConstantColor\",R,N,V_constantColorProp"
- "T@\"GLKEffectPropertyFog\",R,N,V_fog"
- "T@\"GLKEffectPropertyLight\",R,N,V_light0"
- "T@\"GLKEffectPropertyLight\",R,N,V_light1"
- "T@\"GLKEffectPropertyLight\",R,N,V_light2"
- "T@\"GLKEffectPropertyMaterial\",R,N,V_material"
- "T@\"GLKEffectPropertyTexGen\",R,N,V_texGenR"
- "T@\"GLKEffectPropertyTexGen\",R,N,V_texGenS"
- "T@\"GLKEffectPropertyTexGen\",R,N,V_texGenT"
- "T@\"GLKEffectPropertyTexture\",R,N,V_texture2d0"
- "T@\"GLKEffectPropertyTexture\",R,N,V_texture2d1"
- "T@\"GLKEffectPropertyTexture\",R,N,V_textureCubeMap"
- "T@\"GLKEffectPropertyTransform\",&,N,V_transform"
- "T@\"GLKEffectPropertyTransform\",R,N,V_transform"
- "T@\"GLKMesh\",R,W,N,V_mesh"
- "T@\"GLKMeshBuffer\",R,N,V_elementBuffer"
- "T@\"GLKMeshBuffer\",V_buffer"
- "T@\"GLKMeshBufferAllocator\",R,N,V_allocator"
- "T@\"GLKShaderBlockNode\",N,V_children"
- "T@\"GLKShaderBlockNode\",N,V_next"
- "T@\"GLKShaderBlockNode\",N,V_parent"
- "T@\"GLKShaderBlockNode\",R,N,V_fshRootNode"
- "T@\"GLKShaderBlockNode\",R,N,V_vshRootNode"
- "T@\"MDLVertexDescriptor\",R,N,V_vertexDescriptor"
- "T@\"NSArray\",C,N,V_textureOrder"
- "T@\"NSArray\",R,N,V_submeshes"
- "T@\"NSArray\",R,N,V_vertexBuffers"
- "T@\"NSData\",R,V_imageData"
- "T@\"NSLock\",&,V_nsLock"
- "T@\"NSMutableArray\",&,N,V_lightProperties"
- "T@\"NSMutableArray\",&,N,V_properties"
- "T@\"NSMutableArray\",R,N,V_propertyArray"
- "T@\"NSMutableArray\",R,N,V_texGenArray"
- "T@\"NSMutableDictionary\",&,N,V_drawableProperties"
- "T@\"NSMutableDictionary\",R,N,V_programHash"
- "T@\"NSMutableString\",&,N,V_blockText"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_label"
- "T@\"NSString\",C,N,V_loopVar"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_filePath"
- "T@\"NSString\",R,N,V_name"
- "T@\"UIImage\",R"
- "T@\"UIScreen\",&,N,V_screen"
- "TB,N,GisPaused"
- "TB,N,V_dirtyUniforms"
- "TB,N,V_displayLinkPaused"
- "TB,N,V_enableSetNeedsDisplay"
- "TB,N,V_firstResumeOccurred"
- "TB,N,V_hasAlpha"
- "TB,N,V_inDraw"
- "TB,N,V_indexedMask"
- "TB,N,V_isCubeMap"
- "TB,N,V_isMipmapped"
- "TB,N,V_isPowerOfTwo"
- "TB,N,V_isVerticalFlipped"
- "TB,N,V_lastDrawOccurred"
- "TB,N,V_lastResumeOccurred"
- "TB,N,V_lastUpdateOccurred"
- "TB,N,V_lossyCompressedSource"
- "TB,N,V_pauseOnWillResignActive"
- "TB,N,V_reOrient"
- "TB,N,V_resumeOnDidBecomeActive"
- "TB,N,V_shouldDeleteFramebuffer"
- "TB,N,V_textureOrderStale"
- "TB,N,V_viewIsVisible"
- "TB,R,V_hasPremultipliedAlpha"
- "TB,R,V_requestIssuedForMipmapGeneration"
- "TB,R,VcontainsMipmaps"
- "TB,V_supportsASTC_LDR"
- "TB,V_supportsETC2"
- "TC,N,V_centerChanged"
- "TC,N,V_colorMaterialEnabled"
- "TC,N,V_effectStale"
- "TC,N,V_enabled"
- "TC,N,V_firstLight"
- "TC,N,V_lightModelTwoSided"
- "TC,N,V_masksInitialized"
- "TC,N,V_matrixEnabled"
- "TC,N,V_perPixelLightingEnabled"
- "TC,N,V_perVertexLightingEnabled"
- "TC,N,V_positionEyeStale"
- "TC,N,V_propertyArrayStale"
- "TC,N,V_texturingEnabled"
- "TC,N,V_useConstantColor"
- "TC,R,N"
- "TI,N,V_GLTextureName"
- "TI,N,V_arrayLength"
- "TI,N,V_bindTarget"
- "TI,N,V_bitsPerPixel"
- "TI,N,V_depth"
- "TI,N,V_depthRenderbuffer"
- "TI,N,V_depthStencilRenderbuffer"
- "TI,N,V_format"
- "TI,N,V_fshName"
- "TI,N,V_height"
- "TI,N,V_index"
- "TI,N,V_internalFormat"
- "TI,N,V_mipmapLevelCount"
- "TI,N,V_multisampleColorRenderbuffer"
- "TI,N,V_multisampleFramebuffer"
- "TI,N,V_nComponents"
- "TI,N,V_nPrimarySurfaces"
- "TI,N,V_nSurfaces"
- "TI,N,V_name"
- "TI,N,V_numFshStrings"
- "TI,N,V_numLights"
- "TI,N,V_numMipMapLevels"
- "TI,N,V_numTextures"
- "TI,N,V_numVshStrings"
- "TI,N,V_orientation"
- "TI,N,V_positionVBO"
- "TI,N,V_programName"
- "TI,N,V_resolveColorRenderbuffer"
- "TI,N,V_resolveFramebuffer"
- "TI,N,V_rowBytes"
- "TI,N,V_stencilRenderbuffer"
- "TI,N,V_target"
- "TI,N,V_texCoordVBO"
- "TI,N,V_textureIndex"
- "TI,N,V_textureTarget"
- "TI,N,V_type"
- "TI,N,V_vao"
- "TI,N,V_vshName"
- "TI,N,V_width"
- "TI,R,N,V_glBufferName"
- "TI,R,N,V_mode"
- "TI,R,N,V_type"
- "TI,R,VarrayLength"
- "TI,R,Vdepth"
- "TI,R,Vheight"
- "TI,R,VmimapLevelCount"
- "TI,R,Vname"
- "TI,R,Vtarget"
- "TI,R,Vwidth"
- "TQ,N,V_dirtyUniforms"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_capacity"
- "TQ,R,N,V_length"
- "TQ,R,N,V_offset"
- "TQ,R,N,V_type"
- "TQ,R,N,V_vertexCount"
- "T^*,N,V_fshStrings"
- "T^*,N,V_vshStrings"
- "T^?,N,V_drawRectIMP"
- "T^?,N,V_updateIMP"
- "T^@,N,V_effectShaderArray"
- "T^Q,N,V_effectDirtyUniforms"
- "T^f,N,V_eyePlaneByInvModelview"
- "T^f,N,V_plane"
- "T^f,R,N,V_materialAmbientColor"
- "T^f,R,N,V_materialDiffuseColor"
- "T^{GLKBigInt_s=QQ},N,V_fshMask"
- "T^{GLKBigInt_s=QQ},N,V_vshMask"
- "Td,N,V_timeSinceFirstResumeStartTime"
- "Td,N,V_timeSinceLastDrawPreviousTime"
- "Td,N,V_timeSinceLastResumeStartTime"
- "Td,N,V_timeSinceLastUpdatePreviousTime"
- "Td,N,V_viewContentScaleFactor"
- "Td,R,N,V_timeSinceFirstResume"
- "Td,R,N,V_timeSinceLastDraw"
- "Td,R,N,V_timeSinceLastResume"
- "Td,R,N,V_timeSinceLastUpdate"
- "Tf,N,V_constantAttenuation"
- "Tf,N,V_density"
- "Tf,N,V_end"
- "Tf,N,V_linearAttenuation"
- "Tf,N,V_quadraticAttenuation"
- "Tf,N,V_shininess"
- "Tf,N,V_spotCutoff"
- "Tf,N,V_spotCutoffDegrees"
- "Tf,N,V_spotExponent"
- "Tf,N,V_start"
- "Tf,N,V_xSize"
- "Tf,N,V_ySize"
- "Tf,N,V_zSize"
- "Ti,N,V_aColorLoc"
- "Ti,N,V_ambientColorLoc"
- "Ti,N,V_ambientLoc"
- "Ti,N,V_ambientTermLoc"
- "Ti,N,V_baseLightingColorLoc"
- "Ti,N,V_colorLoc"
- "Ti,N,V_constantAttenuationLoc"
- "Ti,N,V_dataCategory"
- "Ti,N,V_densityLoc"
- "Ti,N,V_diffuseColorLoc"
- "Ti,N,V_diffuseLoc"
- "Ti,N,V_drawableColorFormat"
- "Ti,N,V_drawableDepthFormat"
- "Ti,N,V_drawableMultisample"
- "Ti,N,V_drawableStencilFormat"
- "Ti,N,V_emissiveColorLoc"
- "Ti,N,V_endLoc"
- "Ti,N,V_envMode"
- "Ti,N,V_eyePlaneByInvModelviewLoc"
- "Ti,N,V_invModelviewMatrixLoc"
- "Ti,N,V_lightIndex"
- "Ti,N,V_lightModelAmbientColorLoc"
- "Ti,N,V_lightingType"
- "Ti,N,V_linearAttenuationLoc"
- "Ti,N,V_loadMode"
- "Ti,N,V_location"
- "Ti,N,V_matrixLoc"
- "Ti,N,V_mode"
- "Ti,N,V_modeLoc"
- "Ti,N,V_modelviewMatrixLoc"
- "Ti,N,V_mvpMatrixLoc"
- "Ti,N,V_normalMatrixLoc"
- "Ti,N,V_normalizeLoc"
- "Ti,N,V_normalizedSpotDirectionEyeLoc"
- "Ti,N,V_planeLoc"
- "Ti,N,V_positionEyeLoc"
- "Ti,N,V_projectionMatrixLoc"
- "Ti,N,V_propertyClass"
- "Ti,N,V_quadraticAttenuationLoc"
- "Ti,N,V_shininessLoc"
- "Ti,N,V_specularColorLoc"
- "Ti,N,V_specularLoc"
- "Ti,N,V_spotCutoffLoc"
- "Ti,N,V_spotExponentLoc"
- "Ti,N,V_startLoc"
- "Ti,N,V_texelFormat"
- "Ti,N,V_textureIndex"
- "Ti,N,V_type"
- "Ti,N,V_unit2dLoc"
- "Ti,N,V_unitCubeLoc"
- "Ti,N,V_unrollCt"
- "Ti,R,N,V_coord"
- "Ti,R,N,V_elementCount"
- "Ti,R,ValphaState"
- "Ti,R,VtextureOrigin"
- "Tq,N,V_preferredFramesPerSecond"
- "Tq,N,V_screenFramesPerSecond"
- "Tq,R,N,V_drawableHeight"
- "Tq,R,N,V_drawableWidth"
- "Tq,R,N,V_framesDisplayed"
- "Tq,R,N,V_framesPerSecond"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_viewBounds"
- "T{GLKBigInt_s=QQ},N,V_colorMaterialEnabledMask"
- "T{GLKBigInt_s=QQ},N,V_mask"
- "T{GLKBigInt_s=QQ},N,V_prevFshMask"
- "T{GLKBigInt_s=QQ},N,V_prevVshMask"
- "T{GLKBigInt_s=QQ},R,N,V_allFshMasks"
- "T{GLKBigInt_s=QQ},R,N,V_allVshMasks"
- "UTF8String"
- "Vv16@0:8"
- "^*"
- "^*16@0:8"
- "^?"
- "^?16@0:8"
- "^@"
- "^@16@0:8"
- "^Q"
- "^Q16@0:8"
- "^f"
- "^f16@0:8"
- "^v"
- "^v28@0:8I16r^v20"
- "^{CGImageBlockSet=}"
- "^{GLKBigInt_s=QQ}"
- "^{GLKBigInt_s=QQ}16@0:8"
- "^{GLKEffectPropertyPrv=^{GLKBigInt_s}^{GLKBigInt_s}^{GLKBigInt_s}^{GLKBigInt_s}@}"
- "^{_NSZone=}16@0:8"
- "^{__CFData=}"
- "_API"
- "_GLTextureName"
- "_aColorLoc"
- "_allFshMasks"
- "_allVshMasks"
- "_allocator"
- "_ambientColor"
- "_ambientColorLoc"
- "_ambientLoc"
- "_ambientTermLoc"
- "_arrayLength"
- "_baseLightingColor"
- "_baseLightingColorLoc"
- "_bigInt"
- "_bindTarget"
- "_bitsPerPixel"
- "_blockSet"
- "_blockText"
- "_buffer"
- "_buffers"
- "_calculateScreenFramesPerSecond:"
- "_canDrawContent"
- "_capacity"
- "_center"
- "_centerChanged"
- "_cfData"
- "_children"
- "_color"
- "_colorLoc"
- "_colorMaterialEnabled"
- "_colorMaterialEnabledMask"
- "_compiledFshs"
- "_compiledVshs"
- "_configureNotifications"
- "_constantAttenuation"
- "_constantAttenuationLoc"
- "_constantColor"
- "_constantColorProp"
- "_context"
- "_controlsOwnScaleFactor"
- "_coord"
- "_createDisplayLinkForScreen:"
- "_createFramebuffer"
- "_createMeshesFromObject:newMeshes:sourceMeshes:error:"
- "_dataCategory"
- "_delegate"
- "_deleteFramebuffer"
- "_density"
- "_densityLoc"
- "_depth"
- "_depthRenderbuffer"
- "_depthStencilRenderbuffer"
- "_destroyInvoked"
- "_diffuseColor"
- "_diffuseColorLoc"
- "_diffuseLoc"
- "_dirtyUniforms"
- "_display:"
- "_displayLink"
- "_displayLinkMessenger"
- "_displayLinkPaused"
- "_drawRectIMP"
- "_drawableColorFormat"
- "_drawableDepthFormat"
- "_drawableHeight"
- "_drawableMultisample"
- "_drawableProperties"
- "_drawableStencilFormat"
- "_drawableWidth"
- "_effect"
- "_effectDirtyUniforms"
- "_effectShaderArray"
- "_effectStale"
- "_elementBuffer"
- "_elementCount"
- "_emissiveColor"
- "_emissiveColorLoc"
- "_enableSetNeedsDisplay"
- "_enabled"
- "_end"
- "_endLoc"
- "_envMode"
- "_existingView"
- "_eyePlaneByInvModelview"
- "_eyePlaneByInvModelviewLoc"
- "_filePath"
- "_firstLight"
- "_firstResumeOccurred"
- "_fog"
- "_fogEnabled"
- "_format"
- "_framesDisplayed"
- "_framesPerSecond"
- "_fshMask"
- "_fshName"
- "_fshQueue"
- "_fshRootNode"
- "_fshSource"
- "_fshStrings"
- "_glBufferName"
- "_glContext"
- "_hasAlpha"
- "_hasPremultipliedAlpha"
- "_height"
- "_imageData"
- "_inDraw"
- "_index"
- "_indexedMask"
- "_initCommon"
- "_initWithBytes:length:offset:allocator:zone:type:"
- "_initWithData:allocator:type:"
- "_initWithLength:allocator:type:"
- "_initWithLength:offset:zone:type:"
- "_internalFormat"
- "_invModelviewMatrix"
- "_invModelviewMatrixLoc"
- "_isCubeMap"
- "_isMipmapped"
- "_isPowerOfTwo"
- "_isVerticalFlipped"
- "_label"
- "_lastDrawOccurred"
- "_lastResumeOccurred"
- "_lastUpdateOccurred"
- "_length"
- "_light0"
- "_light1"
- "_light2"
- "_lightIndex"
- "_lightModelAmbientColor"
- "_lightModelAmbientColorLoc"
- "_lightModelTwoSided"
- "_lightProperties"
- "_lightingType"
- "_linearAttenuation"
- "_linearAttenuationLoc"
- "_loadMode"
- "_loadTarget"
- "_location"
- "_loopVar"
- "_lossyCompressedSource"
- "_mapCount"
- "_mapPtr"
- "_mask"
- "_masksInitialized"
- "_material"
- "_materialAmbientColor"
- "_materialDiffuseColor"
- "_matrix"
- "_matrixEnabled"
- "_matrixLoc"
- "_mesh"
- "_mipmapLevelCount"
- "_mode"
- "_modeLoc"
- "_modeNameString"
- "_modelviewMatrix"
- "_modelviewMatrixLoc"
- "_multisampleColorRenderbuffer"
- "_multisampleFramebuffer"
- "_mvpMatrix"
- "_mvpMatrixLoc"
- "_nComponents"
- "_nPrimarySurfaces"
- "_nSurfaces"
- "_name"
- "_nameString"
- "_next"
- "_normalMatrix"
- "_normalMatrixLoc"
- "_normalizeLoc"
- "_normalizedSpotDirectionEye"
- "_normalizedSpotDirectionEyeLoc"
- "_nsLock"
- "_numFshStrings"
- "_numLights"
- "_numMipMapLevels"
- "_numTextures"
- "_numVshStrings"
- "_offset"
- "_orientation"
- "_parent"
- "_pauseByNotification"
- "_pauseOnWillResignActive"
- "_perPixelLightingEnabled"
- "_perVertexLightingEnabled"
- "_plane"
- "_planeLoc"
- "_planeNameString"
- "_position"
- "_positionEye"
- "_positionEyeLoc"
- "_positionEyeStale"
- "_positionVBO"
- "_preferredFramesPerSecond"
- "_presentFramebuffer"
- "_prevFshMask"
- "_prevVshMask"
- "_primarySurfaceLength"
- "_programHash"
- "_programName"
- "_projectionMatrix"
- "_projectionMatrixLoc"
- "_properties"
- "_propertyArray"
- "_propertyArrayStale"
- "_propertyClass"
- "_prv"
- "_quadraticAttenuation"
- "_quadraticAttenuationLoc"
- "_reOrient"
- "_refreshRate"
- "_requestIssuedForAlphaPremultiplication"
- "_requestIssuedForMipmapGeneration"
- "_requestIssuedForSRGB"
- "_requestIssuedToInterpretGrayAsAlpha"
- "_requestIssuedToReorientToGL"
- "_resolveAndDiscard"
- "_resolveColorRenderbuffer"
- "_resolveFramebuffer"
- "_resumeByNotification"
- "_resumeOnDidBecomeActive"
- "_rowBytes"
- "_screen"
- "_screenFramesPerSecond"
- "_setFramebuffer:"
- "_sharegroup"
- "_shininess"
- "_shininessLoc"
- "_shouldDeleteFramebuffer"
- "_specularColor"
- "_specularColorLoc"
- "_specularLoc"
- "_spotCutoff"
- "_spotCutoffDegrees"
- "_spotCutoffLoc"
- "_spotDirection"
- "_spotExponent"
- "_spotExponentLoc"
- "_start"
- "_startLoc"
- "_stencilRenderbuffer"
- "_submeshes"
- "_supportsASTC_LDR"
- "_supportsETC2"
- "_target"
- "_texCoordVBO"
- "_texGenArray"
- "_texGenR"
- "_texGenS"
- "_texGenT"
- "_texelFormat"
- "_texture"
- "_texture2d0"
- "_texture2d1"
- "_textureCubeMap"
- "_textureIndex"
- "_textureOrder"
- "_textureOrderStale"
- "_textureTarget"
- "_textureWithTexture:error:"
- "_textureWithTextureTXR:error:"
- "_texturingEnabled"
- "_timeSinceFirstResume"
- "_timeSinceFirstResumeStartTime"
- "_timeSinceLastDraw"
- "_timeSinceLastDrawPreviousTime"
- "_timeSinceLastResume"
- "_timeSinceLastResumeStartTime"
- "_timeSinceLastUpdate"
- "_timeSinceLastUpdatePreviousTime"
- "_transform"
- "_type"
- "_unit2dLoc"
- "_unit2dNameString"
- "_unitCubeLoc"
- "_unitCubeNameString"
- "_unpackAlignment"
- "_unrollCt"
- "_updateAndDraw"
- "_updateIMP"
- "_updateScreenIfChanged"
- "_uploadToGLTexture:data:width:height:dataCategory:cubeMapIndex:mipMapIndex:error:"
- "_useConstantColor"
- "_vao"
- "_vertexBuffers"
- "_vertexCount"
- "_vertexDescriptor"
- "_viewBounds"
- "_viewContentScaleFactor"
- "_viewIsVisible"
- "_vshMask"
- "_vshName"
- "_vshQueue"
- "_vshRootNode"
- "_vshSource"
- "_vshStrings"
- "_width"
- "_xSize"
- "_ySize"
- "_zSize"
- "_zone"
- "aColorLoc"
- "addObject:"
- "addObserver:selector:name:object:"
- "addToRunLoop:forMode:"
- "addTransformProperty"
- "alignmentFix:data:"
- "allFshMasks"
- "allVshMasks"
- "allocWithZone:"
- "allocator"
- "alphaState"
- "ambientColor"
- "ambientLoc"
- "ambientTermLoc"
- "appendFormat:"
- "appendString:"
- "arrayLength"
- "arrayWithArray:"
- "autorelease"
- "baseLightingColorLoc"
- "bind"
- "bindDrawable"
- "bindTarget"
- "bitsPerPixel"
- "blockText"
- "boolValue"
- "bounds"
- "buffer"
- "buildUnrollNodeArray:array:"
- "bundleWithIdentifier:"
- "bytes"
- "bytesPerImage"
- "bytesPerRow"
- "cStringUsingEncoding:"
- "canHonorSRGBrequest"
- "capacity"
- "center"
- "centerChanged"
- "checkResourceIsReachableAndReturnError:"
- "children"
- "clearAllTexturingMasks:fshMask:"
- "color"
- "colorLoc"
- "colorMaterialEnabled"
- "commonCubeMapWithContentsOfFiles:options:error:lock:glContext:"
- "commonCubeMapWithContentsOfURL:options:error:lock:glContext:"
- "commonTextureWithCGImage:options:error:lock:glContext:"
- "commonTextureWithContentsOfData:options:error:lock:glContext:"
- "commonTextureWithContentsOfURL:options:error:lock:glContext:"
- "commonTextureWithName:scaleFactor:bundle:options:error:lock:glContext:"
- "compiledFshForKey:"
- "compiledVshForKey:"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "constantAttenuation"
- "constantAttenuationLoc"
- "constantColor"
- "constantColorProp"
- "containsMipmaps"
- "containsObject:"
- "containsValueForKey:"
- "contentScaleFactor"
- "context"
- "coord"
- "copyTreeWithRoot:parent:"
- "copyTreeWithRootButNotSiblings:parent:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAndBindVAOWithPositions:texCoords:"
- "createAndUseProgramWithShadingHash:"
- "cubeMapWithContentsOfFile:options:error:"
- "cubeMapWithContentsOfFile:options:queue:completionHandler:"
- "cubeMapWithContentsOfFiles:options:error:"
- "cubeMapWithContentsOfFiles:options:queue:completionHandler:"
- "cubeMapWithContentsOfURL:options:error:"
- "cubeMapWithContentsOfURL:options:queue:completionHandler:"
- "cubemap"
- "currentContext"
- "currentRunLoop"
- "d"
- "d16@0:8"
- "dataCategory"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeCGImage:"
- "decodeCGImageDataProvider:"
- "decodeCGImageImageProvider:CGImageProvider:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "defaultCenter"
- "defaultUICatalogForBundle:"
- "delegate"
- "deleteDrawable"
- "density"
- "densityLoc"
- "depth"
- "depthRenderbuffer"
- "depthStencilRenderbuffer"
- "description"
- "destroyBuffer:"
- "determineCGImageBlockFormatWithComponentType:andPixelSize:andColorModel:"
- "determinePVRFormat:"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "diffuseColor"
- "diffuseLoc"
- "dimensions"
- "dirtyAllUniforms"
- "dirtyUniforms"
- "display"
- "displayLayer:"
- "displayLink"
- "displayLinkMessenger"
- "displayLinkPaused"
- "displayLinkWithTarget:selector:"
- "doesNotRecognizeSelector:"
- "draw"
- "drawRect:"
- "drawRectIMP"
- "drawableColorFormat"
- "drawableDepthFormat"
- "drawableHeight"
- "drawableMultisample"
- "drawableProperties"
- "drawableStencilFormat"
- "drawableWidth"
- "effect"
- "effectDirtyUniforms"
- "effectShaderArray"
- "effectStale"
- "elementBuffer"
- "elementCount"
- "elements"
- "emissiveColor"
- "enableSetNeedsDisplay"
- "enabled"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeWithCoder:"
- "end"
- "endLoc"
- "envMode"
- "errorWithDomain:code:userInfo:"
- "eyePlaneByInvModelview"
- "eyePlaneByInvModelviewLoc"
- "f"
- "f16@0:8"
- "faces"
- "filePath"
- "fileURLWithPath:"
- "fillData:offset:"
- "firstLight"
- "firstResumeOccurred"
- "fog"
- "format"
- "frame"
- "framesDisplayed"
- "framesPerSecond"
- "fshMask"
- "fshMaskCt"
- "fshMaskStr"
- "fshMasks"
- "fshName"
- "fshRootNode"
- "fshSource"
- "fshStrings"
- "geometryType"
- "getBytes:length:"
- "glBufferName"
- "glContext"
- "glkView:drawInRect:"
- "glkViewController:willPause:"
- "glkViewControllerUpdate:"
- "hasAlpha"
- "hasAlpha:"
- "hasPremultipliedAlpha"
- "hash"
- "height"
- "i"
- "i16@0:8"
- "imageData"
- "inDraw"
- "includeFshShaderTextForRootNode:"
- "includeShaderTextForRootNode:"
- "includeVshShaderTextForRootNode:"
- "index"
- "indexBuffer"
- "indexCount"
- "indexType"
- "init"
- "initWithAPI:sharegroup:"
- "initWithBigInt:"
- "initWithBytes:deallocator:"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithCGImage:forceCubeMap:wasCubeMap:cubeMapIndex:options:error:"
- "initWithCapacity:allocator:"
- "initWithCoder:"
- "initWithContentsOfURL:"
- "initWithContentsOfURL:options:error:"
- "initWithData:forceCubeMap:wasCubeMap:cubeMapIndex:options:error:"
- "initWithDecodedData:width:height:rowBytes:texture:cubeMapIndex:options:error:"
- "initWithFrame:"
- "initWithFrame:context:"
- "initWithMDLSubmesh:indexType:geometryType:"
- "initWithMesh:error:"
- "initWithMesh:submesh:error:"
- "initWithMode:coord:"
- "initWithNibName:bundle:"
- "initWithPropertyArray:"
- "initWithSharegroup:"
- "initWithString:"
- "initWithTexture:API:options:error:"
- "initWithTexture:textureName:"
- "initWithTextureTXR:textureName:"
- "initWithTransform:lightingType:firstLight:"
- "initWithUTF8String:"
- "initialize"
- "initializeMasks"
- "initializeStaticMasks"
- "insertNode:afterSibling:"
- "insertObject:atIndex:"
- "instanceMethodForSelector:"
- "intValue"
- "internalFormat"
- "invModelviewMatrix"
- "invModelviewMatrixLoc"
- "invalidate"
- "isASTC:"
- "isAttenuated"
- "isCompressed:"
- "isCubeMap"
- "isETC2:"
- "isEqual:"
- "isEqualToString:"
- "isFileURL"
- "isGammaEncoded:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isMipmapped"
- "isPaused"
- "isPowerOfTwo"
- "isProxy"
- "isSpot"
- "isVerticalFlipped"
- "keyEnumerator"
- "lastDrawOccurred"
- "lastObject"
- "lastPathComponent"
- "lastResumeOccurred"
- "lastUpdateOccurred"
- "layer"
- "layerClass"
- "layoutSubviews"
- "length"
- "light0"
- "light1"
- "light2"
- "lightIndex"
- "lightModelAmbientColorLoc"
- "lightModelTwoSided"
- "lightProperties"
- "lightingType"
- "linearAttenuation"
- "linearAttenuationLoc"
- "loadCGImage:options:error:"
- "loadIdentity:"
- "loadMatrix:matrix:"
- "loadMode"
- "loadPVRTCData:error:"
- "loadView"
- "loadWithData:options:error:"
- "localizedDescription"
- "location"
- "lock"
- "lockAndSwitchContext:glContext:"
- "logSetMasksWithLabel:obj:typeStr:"
- "lossyCompressedSource"
- "mainScreen"
- "map"
- "mask"
- "maskForLabel:root:index:"
- "masksInitialized"
- "material"
- "materialAmbientColor"
- "materialDiffuseColor"
- "matrix"
- "matrixEnabled"
- "matrixLoc"
- "mesh"
- "message"
- "methodForSelector:"
- "mimapLevelCount"
- "mipmapLevelCount"
- "mipmapLevels"
- "mode"
- "modeLoc"
- "modeNameString"
- "modelviewMatrixLoc"
- "multisampleColorRenderbuffer"
- "multisampleFramebuffer"
- "mutableCopyWithZone:"
- "mvpMatrixLoc"
- "nComponents"
- "nPrimarySurfaces"
- "nSurfaces"
- "name"
- "nameString"
- "namedTextureWithName:scaleFactor:"
- "nativeScale"
- "newBuffer:type:"
- "newBufferFromZone:data:type:"
- "newBufferFromZone:length:type:"
- "newBufferWithData:type:"
- "newBufferWithLength:type:"
- "newMeshesFromAsset:sourceMeshes:error:"
- "newZone:"
- "newZoneForBuffersWithSize:andType:"
- "next"
- "nextObject"
- "nibBundle"
- "nibName"
- "nodeCt:nodeCt:"
- "normalMatrixLoc"
- "normalizeLoc"
- "normalizedNormalsMask"
- "normalizedSpotDirectionEye"
- "normalizedSpotDirectionEyeLoc"
- "nsLock"
- "null"
- "numFshStrings"
- "numLights"
- "numMipMapLevels"
- "numTextures"
- "numVshStrings"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKey:"
- "offset"
- "orientation"
- "packedMemoryLayoutForFormat:dimensions:"
- "parent"
- "parse"
- "parseXMLFile:rootNode:"
- "parser:didEndElement:namespaceURI:qualifiedName:"
- "parser:didEndMappingPrefix:"
- "parser:didStartElement:namespaceURI:qualifiedName:attributes:"
- "parser:didStartMappingPrefix:toURI:"
- "parser:foundAttributeDeclarationWithName:forElement:type:defaultValue:"
- "parser:foundCDATA:"
- "parser:foundCharacters:"
- "parser:foundComment:"
- "parser:foundElementDeclarationWithName:model:"
- "parser:foundExternalEntityDeclarationWithName:publicID:systemID:"
- "parser:foundIgnorableWhitespace:"
- "parser:foundInternalEntityDeclarationWithName:value:"
- "parser:foundNotationDeclarationWithName:publicID:systemID:"
- "parser:foundProcessingInstructionWithTarget:data:"
- "parser:foundUnparsedEntityDeclarationWithName:publicID:systemID:notationName:"
- "parser:parseErrorOccurred:"
- "parser:resolveExternalEntityName:systemID:"
- "parser:validationErrorOccurred:"
- "parserDidEndDocument:"
- "parserDidStartDocument:"
- "pathForResource:ofType:"
- "pauseOnWillResignActive"
- "paused"
- "perPixelLightingEnabled"
- "perVertexLightingEnabled"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pixelBytes:"
- "pixelFormat"
- "plane"
- "planeLoc"
- "planeNameString"
- "position"
- "positionEye"
- "positionEyeLoc"
- "positionEyeStale"
- "positionVBO"
- "preferredFramesPerSecond"
- "premultiplyWithAlpha:source:withWidth:withHeight:withRowBytes:error:"
- "prepareToDraw"
- "presentRenderbuffer:"
- "prevFshMask"
- "prevVshMask"
- "printTree:"
- "printTreeVerbose:"
- "programHash"
- "programInfoLogForName:effectLabel:msg:"
- "programName"
- "projectionMatrix"
- "projectionMatrixLoc"
- "properties"
- "propertyArray"
- "propertyArrayStale"
- "propertyClass"
- "purgeAllShaders"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "quadraticAttenuation"
- "quadraticAttenuationLoc"
- "raise:format:"
- "reOrient"
- "reformat:gammaDegamma:bufferAllocator:error:"
- "relativeString"
- "release"
- "removeAllObjects"
- "removeObjectAtIndex:"
- "removeObserver:"
- "removeObserver:name:object:"
- "renderbufferStorage:fromDrawable:"
- "reorientToGL:source:withWidth:withHeight:withRowBytes:error:"
- "replaceOccurrencesOfString:withString:options:range:"
- "requestIssuedForMipmapGeneration"
- "resolveColorRenderbuffer"
- "resolveFramebuffer"
- "respondsToSelector:"
- "resumeOnDidBecomeActive"
- "retain"
- "retainCount"
- "rowBytes"
- "screen"
- "screenFramesPerSecond"
- "self"
- "setAColorLoc:"
- "setAmbientColor:"
- "setAmbientLoc:"
- "setAmbientTermLoc:"
- "setArrayLength:"
- "setAutoresizingMask:"
- "setBaseLightingColor:"
- "setBaseLightingColorLoc:"
- "setBindTarget:"
- "setBitsPerPixel:"
- "setBlockText:"
- "setBuffer:"
- "setCenter:"
- "setCenterChanged:"
- "setChildren:"
- "setColor:"
- "setColorLoc:"
- "setColorMaterialEnabled:"
- "setCompiledFsh:forKey:"
- "setCompiledVsh:forKey:"
- "setConstantAttenuation:"
- "setConstantAttenuationLoc:"
- "setConstantColor:"
- "setContentScaleFactor:"
- "setContext:"
- "setCurrentContext:"
- "setDataCategory:"
- "setDebugLabel:"
- "setDelegate:"
- "setDensity:"
- "setDensityLoc:"
- "setDepth:"
- "setDepthRenderbuffer:"
- "setDepthStencilRenderbuffer:"
- "setDiffuseColor:"
- "setDiffuseLoc:"
- "setDirtyUniforms:"
- "setDisplayLink:"
- "setDisplayLinkMessenger:"
- "setDisplayLinkPaused:"
- "setDrawRectIMP:"
- "setDrawableColorFormat:"
- "setDrawableDepthFormat:"
- "setDrawableMultisample:"
- "setDrawableProperties:"
- "setDrawableStencilFormat:"
- "setEffect:"
- "setEffectDirtyUniforms:"
- "setEffectShaderArray:"
- "setEffectStale:"
- "setEmissiveColor:"
- "setEnableSetNeedsDisplay:"
- "setEnabled:"
- "setEnd:"
- "setEndLoc:"
- "setEnvMode:"
- "setEyePlaneByInvModelview:"
- "setEyePlaneByInvModelviewLoc:"
- "setFSHSource:"
- "setFirstLight:"
- "setFirstResumeOccurred:"
- "setFormat:"
- "setFshMask:"
- "setFshName:"
- "setFshSource:"
- "setFshStrings:"
- "setGLDefaults"
- "setGLTextureName:"
- "setGlContext:"
- "setHasAlpha:"
- "setHeight:"
- "setInDraw:"
- "setIndex:"
- "setIndexedMask:"
- "setIndicesForRoot:andReplaceLoopVar:baseLabel:basePropertyClass:usingIndex:indexString:"
- "setInternalFormat:"
- "setInvModelviewMatrix:"
- "setInvModelviewMatrixLoc:"
- "setIsCubeMap:"
- "setIsMipmapped:"
- "setIsPowerOfTwo:"
- "setIsVerticalFlipped:"
- "setLabel:"
- "setLastDrawOccurred:"
- "setLastResumeOccurred:"
- "setLastUpdateOccurred:"
- "setLightIndex:"
- "setLightModelAmbientColor:"
- "setLightModelAmbientColorLoc:"
- "setLightModelTwoSided:"
- "setLightProperties:"
- "setLightingType:"
- "setLinearAttenuation:"
- "setLinearAttenuationLoc:"
- "setLoadMode:"
- "setLocation:"
- "setLoopVar:"
- "setLossyCompressedSource:"
- "setMask:"
- "setMasks"
- "setMasksInitialized:"
- "setMasksWithRoot:treeRoot:mask:"
- "setMatrix:"
- "setMatrixEnabled:"
- "setMatrixLoc:"
- "setMipmapLevelCount:"
- "setMode:"
- "setModeLoc:"
- "setModeNameString:"
- "setModelviewMatrix:"
- "setModelviewMatrixLoc:"
- "setMultisampleColorRenderbuffer:"
- "setMultisampleFramebuffer:"
- "setMvpMatrix:"
- "setMvpMatrixLoc:"
- "setNComponents:"
- "setNPrimarySurfaces:"
- "setNSurfaces:"
- "setName:"
- "setNameString:"
- "setNext:"
- "setNormalMatrixLoc:"
- "setNormalize:"
- "setNormalizeLoc:"
- "setNormalizedSpotDirectionEye:"
- "setNormalizedSpotDirectionEyeLoc:"
- "setNsLock:"
- "setNumFshStrings:"
- "setNumLights:"
- "setNumMipMapLevels:"
- "setNumTextures:"
- "setNumVshStrings:"
- "setObject:forKey:"
- "setOpaque:"
- "setOrientation:"
- "setParent:"
- "setPauseOnWillResignActive:"
- "setPaused:"
- "setPerPixelLightingEnabled:"
- "setPerVertexLightingEnabled:"
- "setPlane:"
- "setPlaneLoc:"
- "setPlaneNameString:"
- "setPosition:"
- "setPositionEye:"
- "setPositionEyeLoc:"
- "setPositionEyeStale:"
- "setPositionVBO:"
- "setPreferredFramesPerSecond:"
- "setPrevFshMask:"
- "setPrevVshMask:"
- "setProgramName:"
- "setProjectionMatrix:"
- "setProjectionMatrixLoc:"
- "setProperties:"
- "setPropertyArrayStale:"
- "setPropertyClass:"
- "setQuadraticAttenuation:"
- "setQuadraticAttenuationLoc:"
- "setReOrient:"
- "setResolveColorRenderbuffer:"
- "setResolveFramebuffer:"
- "setResumeOnDidBecomeActive:"
- "setRowBytes:"
- "setScreen:"
- "setScreenFramesPerSecond:"
- "setShaderBindings"
- "setShininess:"
- "setShouldDeleteFramebuffer:"
- "setShouldResolveExternalEntities:"
- "setSpecularColor:"
- "setSpecularLoc:"
- "setSpotCutoff:"
- "setSpotCutoffDegrees:"
- "setSpotCutoffLoc:"
- "setSpotDirection:"
- "setSpotExponent:"
- "setSpotExponentLoc:"
- "setStart:"
- "setStartLoc:"
- "setStaticMasksWithVshRoot:fshRoot:"
- "setStencilRenderbuffer:"
- "setSupportsASTC_LDR:"
- "setSupportsETC2:"
- "setTarget:"
- "setTexCoordVBO:"
- "setTexelFormat:"
- "setTextureIndex:"
- "setTextureIndices"
- "setTextureOrder:"
- "setTextureOrderStale:"
- "setTextureTarget:"
- "setTexturingEnabled:"
- "setTimeSinceFirstResumeStartTime:"
- "setTimeSinceLastDrawPreviousTime:"
- "setTimeSinceLastResumeStartTime:"
- "setTimeSinceLastUpdatePreviousTime:"
- "setTransform:"
- "setType:"
- "setUnit2dLoc:"
- "setUnit2dNameString:"
- "setUnitCubeLoc:"
- "setUnitCubeNameString:"
- "setUnrollCt:"
- "setUpdateIMP:"
- "setUseConstantColor:"
- "setVSHSource:"
- "setVao:"
- "setView:"
- "setViewBounds:"
- "setViewContentScaleFactor:"
- "setViewIsVisible:"
- "setVshMask:"
- "setVshName:"
- "setVshSource:"
- "setVshStrings:"
- "setWidth:"
- "setXSize:"
- "setYSize:"
- "setZSize:"
- "set_ambientColorLoc:"
- "set_colorMaterialEnabledMask:"
- "set_diffuseColorLoc:"
- "set_emissiveColorLoc:"
- "set_shininessLoc:"
- "set_specularColorLoc:"
- "shaderInfoLogForName:effectLabel:msg:"
- "sharegroup"
- "shininess"
- "shouldApplyPremultiplication"
- "shouldApplyReorientToGL"
- "shouldDeleteFramebuffer"
- "snapshot"
- "specularColor"
- "specularLoc"
- "spotCutoff"
- "spotCutoffDegrees"
- "spotCutoffLoc"
- "spotDirection"
- "spotExponent"
- "spotExponentLoc"
- "start"
- "startLoc"
- "stencilRenderbuffer"
- "stringWithFormat:"
- "submeshes"
- "superclass"
- "supportsASTC_LDR"
- "supportsETC2"
- "target"
- "texCoordVBO"
- "texGenArray"
- "texGenR"
- "texGenS"
- "texGenT"
- "texelFormat"
- "texture2d0"
- "texture2d1"
- "textureCubeMap"
- "textureIndex"
- "textureOrder"
- "textureOrderStale"
- "textureOrigin"
- "textureTarget"
- "textureWithBufferAllocator:"
- "textureWithCGImage:options:error:"
- "textureWithCGImage:options:queue:completionHandler:"
- "textureWithContentsOfData:options:error:"
- "textureWithContentsOfData:options:queue:completionHandler:"
- "textureWithContentsOfFile:options:error:"
- "textureWithContentsOfFile:options:queue:completionHandler:"
- "textureWithContentsOfURL:options:error:"
- "textureWithContentsOfURL:options:queue:completionHandler:"
- "textureWithName:scaleFactor:bundle:options:error:"
- "textureWithName:scaleFactor:bundle:options:queue:completionHandler:"
- "texturingEnabled"
- "timeSinceFirstResume"
- "timeSinceFirstResumeStartTime"
- "timeSinceLastDraw"
- "timeSinceLastDrawPreviousTime"
- "timeSinceLastResume"
- "timeSinceLastResumeStartTime"
- "timeSinceLastUpdate"
- "timeSinceLastUpdatePreviousTime"
- "transform"
- "unit2dLoc"
- "unit2dNameString"
- "unitCubeLoc"
- "unitCubeNameString"
- "unlock"
- "unlockAndRestoreContext:glContext:"
- "unrollLoopNodesForStaticTreeWithRoot:"
- "unsignedIntegerValue"
- "update"
- "updateBaseEffect"
- "updateFshStringsWithRoot:enabled:"
- "updateIMP"
- "updateRequestedOperationsFromOptions:"
- "updateSkyboxEffect"
- "updateVshStringsWithRoot:enabled:"
- "uploadToGLTexture:error:"
- "useColorAttrib"
- "useConstantColor"
- "useTexCoordAttrib"
- "useTexCoordAttribMask"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8I16"
- "v20@0:8f16"
- "v20@0:8i16"
- "v24@0:8*16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSXMLParser\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8^*16"
- "v24@0:8^?16"
- "v24@0:8^@16"
- "v24@0:8^B16"
- "v24@0:8^Q16"
- "v24@0:8^f16"
- "v24@0:8^{GLKBigInt_s=QQ}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8(_GLKVector3={?=fff}{?=fff}{?=fff}[3f])16"
- "v28@0:8@16B24"
- "v32@0:8(_GLKVector4={?=ffff}{?=ffff}{?=ffff}[4f])16"
- "v32@0:8@\"NSData\"16Q24"
- "v32@0:8@\"NSXMLParser\"16@\"NSData\"24"
- "v32@0:8@\"NSXMLParser\"16@\"NSError\"24"
- "v32@0:8@\"NSXMLParser\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8@16Q24"
- "v32@0:8^f16^f24"
- "v32@0:8^{GLKBigInt_s=QQ}16^{GLKBigInt_s=QQ}24"
- "v32@0:8{GLKBigInt_s=QQ}16"
- "v40@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24^{GLKBigInt_s=QQ}32"
- "v40@0:8@16{GLKBigInt_s=QQ}24"
- "v48@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24@32^@40"
- "v48@0:8^{CGImage=}16@24@32@?40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v52@0:8(_GLKMatrix3={?=fffffffff}[9f])16"
- "v56@0:8@\"GLKView\"16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "v56@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSDictionary\"48"
- "v56@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48"
- "v56@0:8@16@24@32@40@48"
- "v56@0:8@16@24@32i40I44@48"
- "v56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "v64@0:8@16d24@32@40@48@?56"
- "v80@0:8(_GLKMatrix4={?=ffffffffffffffff}[16f])16"
- "v84@0:8i16(_GLKMatrix4={?=ffffffffffffffff}[16f])20"
- "vNormalEyeMask"
- "vPositionEyeMask"
- "valueForKey:"
- "vao"
- "vertexBuffers"
- "vertexCount"
- "vertexDescriptor"
- "view"
- "viewBounds"
- "viewContentScaleFactor"
- "viewDidLoad"
- "viewDidMoveToWindow:shouldAppearOrDisappear:"
- "viewDidUnload"
- "viewIsVisible"
- "viewWillAppear:"
- "viewWillDisappear:"
- "vshMask"
- "vshMaskCt"
- "vshMaskStr"
- "vshMasks"
- "vshName"
- "vshRootNode"
- "vshSource"
- "vshStrings"
- "width"
- "window"
- "xSize"
- "ySize"
- "zSize"
- "zone"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{GLKBigInt_s=\"n0\"Q\"n1\"Q}"
- "{GLKBigInt_s=QQ}16@0:8"
- "{GLKBigInt_s=QQ}36@0:8@16@24i32"

```
