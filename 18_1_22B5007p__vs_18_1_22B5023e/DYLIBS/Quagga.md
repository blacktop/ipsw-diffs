## Quagga

> `/System/Library/PrivateFrameworks/Quagga.framework/Quagga`

```diff

-192.8.0.0.0
-  __TEXT.__text: 0xe0e40
-  __TEXT.__auth_stubs: 0x1cf0
-  __TEXT.__objc_methlist: 0xe0
-  __TEXT.__gcc_except_tab: 0x92bc
-  __TEXT.__const: 0x20134
-  __TEXT.__cstring: 0x46f9
-  __TEXT.__oslogstring: 0x59c6
+192.11.0.0.0
+  __TEXT.__text: 0xf1c6c
+  __TEXT.__auth_stubs: 0x1e40
+  __TEXT.__objc_methlist: 0x184
+  __TEXT.__gcc_except_tab: 0x9eec
+  __TEXT.__const: 0x25060
+  __TEXT.__cstring: 0x4ece
+  __TEXT.__oslogstring: 0x6690
   __TEXT.__dlopen_cstrs: 0x43
-  __TEXT.__unwind_info: 0x3188
-  __TEXT.__objc_classname: 0x57
-  __TEXT.__objc_methname: 0x1887
+  __TEXT.__unwind_info: 0x3828
+  __TEXT.__objc_classname: 0x86
+  __TEXT.__objc_methname: 0x18f9
   __TEXT.__objc_methtype: 0x1139
-  __TEXT.__objc_stubs: 0x760
-  __DATA_CONST.__got: 0x520
-  __DATA_CONST.__const: 0x13a8
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__objc_stubs: 0x7a0
+  __DATA_CONST.__got: 0x598
+  __DATA_CONST.__const: 0x13e8
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x200
+  __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xe88
+  __AUTH_CONST.__auth_got: 0xf30
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x5fa8
-  __AUTH_CONST.__cfstring: 0x38a0
-  __AUTH_CONST.__objc_const: 0x1610
+  __AUTH_CONST.__const: 0x7ba8
+  __AUTH_CONST.__cfstring: 0x3c60
+  __AUTH_CONST.__objc_const: 0x1748
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x490
   __DATA.__bss: 0x350
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x2b8
-  __DATA_DIRTY.__bss: 0xca8
+  __DATA_DIRTY.__bss: 0xd08
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libiconv.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2831
-  Symbols:   886
-  CStrings:  1626
+  Functions: 3359
+  Symbols:   921
+  CStrings:  1728
 
Symbols:
+ _CFGetRetainCount
+ _CFMakeCollectable
+ _CFStringReplaceAll
+ _MRCContextOptionIsStreaming
+ _MRCContextOptionMaximumBufferAge
+ _VTPixelRotationSessionCreate
+ _VTPixelRotationSessionInvalidate
+ _VTPixelRotationSessionRotateImage
+ _VTPixelRotationSessionRotateSubImage
+ _VTSessionCopyProperty
+ __CFIsDeallocating
+ __CFNonObjCEqual
+ __CFNonObjCHash
+ __CFNonObjCRelease
+ __CFNonObjCRetain
+ __CFRuntimeBridgeClasses
+ __CFTryRetain
+ __os_log_fault_impl
+ _class_getName
+ _kCVPixelBufferPoolMaximumBufferAgeKey
+ _kCVPixelBufferPoolMinimumBufferCountKey
+ _kIOSurfaceIsGlobal
+ _kIOSurfaceName
+ _kVTPixelRotationPropertyKey_EnableHardwareAcceleratedTransfer
+ _kVTPixelRotationPropertyKey_EnableHighSpeedTransfer
+ _kVTPixelRotationPropertyKey_MostRecentChainDescription
+ _kVTPixelRotationPropertyKey_Rotation
+ _kVTPixelRotationPropertyKey_ZeroFillData
+ _kVTPixelTransferPropertyKey_EnableGPUAcceleratedTransfer
+ _kVTPixelTransferPropertyKey_MostRecentChainDescription
+ _kVTPixelTransferPropertyKey_MostRecentConversionType
+ _kVTRotation_CW90
+ _vDSP_vsmul
+ _vImageConvert_ARGB16UtoPlanar16U
+ _vImageConvert_BGRXFFFFToPlanarF
CStrings:
+ "        isStreaming %!s(MISSING)\n"
+ "        maximumBufferAge %!g(MISSING)\n"
+ "        maximumBufferAge <unspecified>\n"
+ "%!@(MISSING) 90CW"
+ "%!{(MISSING)public}s %!{(MISSING)public}p is being prepared"
+ "%!{(MISSING)public}s %!{(MISSING)public}p is ready"
+ "%!{(MISSING)public}s: allocated pyramid %!{(MISSING)public}p with %!{(MISSING)public}ld level(s)"
+ "%!{(MISSING)public}s: at level #%!{(MISSING)public}zu, allocated pixel buffer pool: %!{(MISSING)public}@"
+ "%!{(MISSING)public}s: at level #%!{(MISSING)public}zu, pixelBufferAttributes: %!{(MISSING)public}@"
+ "%!{(MISSING)public}s: at level #%!{(MISSING)public}zu, pixelBufferPoolAttributes: %!{(MISSING)public}@"
+ "%!{(MISSING)public}s: attempting to create a CVPixelBuffer at level #%!{(MISSING)public}zu from pool %!{(MISSING)public}p"
+ "%!{(MISSING)public}s: attempting to create a CVPixelBufferPool at level #%!{(MISSING)public}zu"
+ "%!{(MISSING)public}s: effective pixel buffer pools are not yet ready"
+ "%!{(MISSING)public}s: failed to allocate pyramid"
+ "%!{(MISSING)public}s: failed to create IOSurface-backed pixel buffer at level #%!{(MISSING)public}zu"
+ "%!{(MISSING)public}s: failed to create pixel buffer at level #%!{(MISSING)public}zu from pool %!{(MISSING)public}p"
+ "%!{(MISSING)public}s: failed to create pixel buffer pool at level #%!{(MISSING)public}zu"
+ "%!{(MISSING)public}s: failed to prepare"
+ "%!{(MISSING)public}s: level #%!{(MISSING)public}ld of pyramid %!{(MISSING)public}p: %!{(MISSING)public}@"
+ "<anonymous>"
+ "<redacted>"
+ "<unspecified>"
+ "ANMDImagePreprocessor: rotation is not needed"
+ "ANMDImagePreprocessor: using Accelerate"
+ "ANMDImagePreprocessor: using Video Toolbox"
+ "ANMDImagePreprocessor[Rotation, %!z(MISSING)u, %!z(MISSING)u, %!s(MISSING)]"
+ "ANMDImagePreprocessor[Transfer, %!z(MISSING)u, %!z(MISSING)u, %!s(MISSING)]"
+ "ANMDImagePreprocessor_Accelerate is not ready."
+ "ANMDImagePreprocessor_Accelerate is not ready."
+ "ANMDImagePreprocessor_Accelerate::prepare"
+ "ANMDImagePreprocessor_Accelerate::run"
+ "ANMDImagePreprocessor_Accelerate_32BGRA is not ready."
+ "ANMDImagePreprocessor_Accelerate_32BGRA is not ready."
+ "ANMDImagePreprocessor_Accelerate_32BGRA::prepare"
+ "ANMDImagePreprocessor_Accelerate_32BGRA::resampleAndRotateIfNeeded_"
+ "ANMDImagePreprocessor_Accelerate_32BGRA::run"
+ "ANMDImagePreprocessor_VideoToolbox is not ready."
+ "ANMDImagePreprocessor_VideoToolbox is not ready."
+ "ANMDImagePreprocessor_VideoToolbox::prepare"
+ "ANMDImagePreprocessor_VideoToolbox::run"
+ "ANMDPreprocessingUsingVideoToolbox"
+ "Allocated interleaved pixel buffer: %!{(MISSING)public}@"
+ "Allocated interleaved90CW pixel buffer: %!{(MISSING)public}@"
+ "Attempting to create an IOSurface-backed CVPixelBuffer: width=%!{(MISSING)public}zu, height=%!{(MISSING)public}zu, pixelFormatType=%!{(MISSING)public}.4s"
+ "CFArrayCreateMutable failed"
+ "CFArrayCreateMutable failed."
+ "CachedPyramidAllocator::allocate"
+ "CachedPyramidAllocator::prepare_"
+ "Effective pixel buffer pools are not yet ready."
+ "End decoding: decoderResult=%!{(MISSING)sensitive, signpost.description:attribute}@"
+ "EphemeralPyramidAllocator::allocate"
+ "Failed to allocate image preprocessor."
+ "Failed to allocate pyramid allocator."
+ "Failed to allocate pyramid allocator: %!{(MISSING)public}s"
+ "Failed to lock interleaved pixel buffer for reading"
+ "Invalid interleaved pixel buffer"
+ "Invalid interleaved pixel buffer."
+ "Invalid pixel rotation session."
+ "Invalid pixel rotation session."
+ "Invalid pyramid allocator"
+ "Invalid pyramid allocator."
+ "MRC: ANMD Preprocessor Interleaved"
+ "MRC: Cached Pyramid Level #%!z(MISSING)u"
+ "MRC: Ephemeral Pyramid Level #%!z(MISSING)u"
+ "MRCContextOptionIsStreaming"
+ "MRCContextOptionMaximumBufferAge"
+ "MRCDecoderDecodeSampleWithRegions: decoderResult: %!{(MISSING)sensitive}@"
+ "MRCDescriptorDecodePayloadAndSupplementalPayloadWithOptions: decodedPayloadString: %!{(MISSING)sensitive, mask.hash}@"
+ "MRCDescriptorDecodePayloadAndSupplementalPayloadWithOptions: descriptor: %!{(MISSING)sensitive}@"
+ "MRCDescriptorDecodePayloadAndSupplementalPayloadWithOptions: supplementalPayloadStringValue: %!{(MISSING)sensitive, mask.hash}@"
+ "MRCDescriptorDecodePayloadWithOptions: decodedPayloadString: %!{(MISSING)sensitive, mask.hash}@"
+ "MRCDescriptorDecodePayloadWithOptions: descriptor: %!{(MISSING)sensitive}@"
+ "MostRecentChainDescription"
+ "MostRecentConversionType"
+ "New pyramid allocator: <%!{(MISSING)public}s %!{(MISSING)public}p>"
+ "On-demand pyramid generation: disablesCropping=%!{(MISSING)public, bool}d"
+ "PixelRotationSession::rotateImage"
+ "PixelTransferSession: mostRecentChainDescription: %!{(MISSING)public}@"
+ "PixelTransferSession: mostRecentConversionType: %!{(MISSING)public}@"
+ "PlaceholderPyramidAllocator::allocate should never be invoked."
+ "Pyramid allocator <%!{(MISSING)public}s %!{(MISSING)public}p> can be reused"
+ "Pyramid allocator <%!{(MISSING)public}s %!{(MISSING)public}p>: unable to allocate pyramid"
+ "PyramidGenerationOnDemandWithoutCropping"
+ "Resetting pyramid allocator <%!{(MISSING)public}s %!{(MISSING)public}p>"
+ "T@\"NSString\",R,C,N"
+ "Unable to reset pyramid allocator <%!{(MISSING)public}s %!{(MISSING)public}p>"
+ "Unexpected invocation: %!{(MISSING)public}s"
+ "Unsupported pixel format: %!{(MISSING)public}#x"
+ "VTPixelRotationSessionCreate failed."
+ "VTPixelRotationSessionCreate failed: %!{(MISSING)public}d"
+ "VTPixelRotationSessionRotateImage failed."
+ "VTPixelRotationSessionRotateImage failed: %!{(MISSING)public}d"
+ "VTPixelRotationSessionRotateSubImage failed."
+ "VTPixelRotationSessionRotateSubImage failed: %!{(MISSING)public}d"
+ "VTSessionCopyProperty failed with status %!{(MISSING)public}d, key=%!{(MISSING)public}@"
+ "VTSessionCopyProperty failed."
+ "VTSessionSetProperty failed with status %!{(MISSING)public}d, key=%!{(MISSING)public}@, value=%!{(MISSING)public}@"
+ "VTSessionSetProperty failed."
+ "[PixelRotationSession::create] created <%!{(MISSING)public}s %!{(MISSING)public}p> with underlying session: %!{(MISSING)public}@"
+ "[PixelTransferSession::create] created <%!{(MISSING)public}s %!{(MISSING)public}p> with underlying session: %!{(MISSING)public}@"
+ "__MRCCFType"
+ "__MRCCFTypeWithRedactedDescription"
+ "_cfTypeID"
+ "_isDeallocating"
+ "_tryRetain"
+ "automaticallyNotifiesObserversForKey:"
+ "createNetworkInputPixelBufferFromInterleaved"
+ "masterWidth=%!{(MISSING)public, signpost.description:attribute}zu, masterHeight=%!{(MISSING)public, signpost.description:attribute}zu, pixelFormatType=%!{(MISSING)public, signpost.description:attribute}.4s"
+ "mrc::Context::ConcreteBase<mrc::(anonymous namespace)::PyramidGenerationSessionContext<mrc::PyramidGenerationBehavior::Default>>::ConcreteBase(const Options &, dispatch_queue_t _Nonnull) [_Derived = mrc::(anonymous namespace)::PyramidGenerationSessionContext<mrc::PyramidGenerationBehavior::Default>]"
+ "mrc::Context::ConcreteBase<mrc::(anonymous namespace)::PyramidGenerationSessionContext<mrc::PyramidGenerationBehavior::Legacy>>::ConcreteBase(const Options &, dispatch_queue_t _Nonnull) [_Derived = mrc::(anonymous namespace)::PyramidGenerationSessionContext<mrc::PyramidGenerationBehavior::Legacy>]"
+ "name=%!{(MISSING)public, signpost.description:attribute}@"
+ "pixelFormatType=%!s(MISSING), "
+ "redactedDescription"
+ "temporaryAlpha"
+ "vImageConvert_ARGB16UtoPlanar16U failed: %!{(MISSING)public}zd"
+ "vImageConvert_RGBXFFFFToPlanarF failed."
+ "vImageConvert_RGBXFFFFToPlanarF failed: %!{(MISSING)public}zd"
+ "virtual CFRef<CFArrayRef> mrc::(anonymous namespace)::PlaceholderPyramidAllocator<mrc::PyramidGenerationBehavior::Default>::allocate(std::optional<Error> &, const std::optional<os_signpost_id_t> &) const [_Behavior = mrc::PyramidGenerationBehavior::Default]"
+ "virtual CFRef<CFArrayRef> mrc::(anonymous namespace)::PlaceholderPyramidAllocator<mrc::PyramidGenerationBehavior::Legacy>::allocate(std::optional<Error> &, const std::optional<os_signpost_id_t> &) const [_Behavior = mrc::PyramidGenerationBehavior::Legacy]"
- "ANMDImagePreprocessor is not ready."
- "ANMDImagePreprocessor is not ready."
- "ANMDImagePreprocessor::prepare"
- "ANMDImagePreprocessor::resampleAndRotateIfNeeded_"
- "ANMDImagePreprocessor::run"
- "Attempting to create an IOSurface-backed CVPixelBuffer: width=%!{(MISSING)public}zu, height=%!{(MISSING)public}zu, pixelFormatType=%!{(MISSING)public}c%!{(MISSING)public}c%!{(MISSING)public}c%!{(MISSING)public}c"
- "End decoding: decoderResult=%!{(MISSING)private, signpost.description:attribute}@"
- "Failed to create IOSurface-backed pixel buffer at level #%!{(MISSING)public}ld."
- "MRCDecoderDecodeSampleWithRegions: decoderResult: %!{(MISSING)private}@"
- "MRCDescriptorDecodePayloadAndSupplementalPayloadWithOptions: decodedPayloadString: %!{(MISSING)private}@"
- "MRCDescriptorDecodePayloadAndSupplementalPayloadWithOptions: descriptor: %!{(MISSING)private}@"
- "MRCDescriptorDecodePayloadAndSupplementalPayloadWithOptions: supplementalPayloadStringValue: %!{(MISSING)private}@"
- "MRCDescriptorDecodePayloadWithOptions: decodedPayloadString: %!{(MISSING)private}@"
- "MRCDescriptorDecodePayloadWithOptions: descriptor: %!{(MISSING)private}@"
- "PyramidGenerationSessionContext"
- "mrc::Context::ConcreteBase<mrc::(anonymous namespace)::PyramidGenerationSessionContext>::ConcreteBase(const Options &, dispatch_queue_t _Nonnull) [_Derived = mrc::(anonymous namespace)::PyramidGenerationSessionContext]"
- "pixelFormatType=%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING), "

```
