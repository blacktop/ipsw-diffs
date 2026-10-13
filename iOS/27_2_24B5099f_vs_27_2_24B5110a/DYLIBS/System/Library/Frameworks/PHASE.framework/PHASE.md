## PHASE

> `/System/Library/Frameworks/PHASE.framework/PHASE`

```diff

-400.0.0.0.0
-  __TEXT.__text: 0x24cd44
+400.101.0.0.0
+  __TEXT.__text: 0x252998
   __TEXT.__realtime: 0x16f08
   __TEXT.__objc_methlist: 0x5084
-  __TEXT.__const: 0x47b1c
+  __TEXT.__const: 0x47b5c
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__gcc_except_tab: 0x268b8
-  __TEXT.__oslogstring: 0x21da3
-  __TEXT.__cstring: 0x163a9
-  __TEXT.__unwind_info: 0xd1f0
+  __TEXT.__gcc_except_tab: 0x2701c
+  __TEXT.__oslogstring: 0x22817
+  __TEXT.__cstring: 0x169b7
+  __TEXT.__unwind_info: 0xd350
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2720
+  __DATA_CONST.__objc_selrefs: 0x2730
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x3c0
   __DATA_CONST.__objc_arraydata: 0x48
-  __DATA_CONST.__got: 0x6d0
-  __AUTH_CONST.__const: 0xe310
-  __AUTH_CONST.__cfstring: 0x5e40
+  __DATA_CONST.__got: 0x6d8
+  __AUTH_CONST.__const: 0xe458
+  __AUTH_CONST.__cfstring: 0x5fe0
   __AUTH_CONST.__objc_const: 0xa510
   __AUTH_CONST.__weak_auth_got: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0xdd0
+  __AUTH_CONST.__auth_got: 0xe58
   __AUTH.__objc_data: 0x28f0
   __AUTH.__data: 0x50
   __DATA.__objc_ivar: 0x720

   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders
   - /System/Library/Frameworks/ModelIO.framework/ModelIO

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9893
-  Symbols:   13652
-  CStrings:  4595
+  Functions: 9947
+  Symbols:   13731
+  CStrings:  4673
 
Symbols:
+ _CFArrayGetCount
+ _CFArrayGetTypeID
+ _CFArrayGetValueAtIndex
+ _CFDataGetBytePtr
+ _CFDataGetLength
+ _CFDictionaryContainsKey
+ _CFDictionaryGetValue
+ _CFNumberGetType
+ _CFNumberGetTypeID
+ _CFNumberGetValue
+ _OBJC_CLASS_$_CMDeviceStateManager
+ __ZN10applesauce2CF7details11find_at_keyINSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPK10__CFStringEET_PK14__CFDictionaryOT0_NS1_15counterpart_tagE
+ __ZN10applesauce2CF7details11find_at_keyIfPK10__CFStringEET_PK14__CFDictionaryOT0_NS1_15counterpart_tagE
+ __ZN10applesauce2CF7details11find_at_keyIiPK10__CFStringEET_PK14__CFDictionaryOT0_NS1_15counterpart_tagE
+ __ZN10applesauce2CF7details6at_keyIPK10__CFStringEEPKvPK14__CFDictionaryOT_NS1_10raw_cf_tagE
+ __ZN10applesauce2CF7details7has_keyIPK10__CFStringEEbPK14__CFDictionaryOT_NS1_10raw_cf_tagE
+ __ZN10applesauce2CF8ArrayRefD1Ev
+ __ZN10applesauce2CF9not_foundEv
+ __ZN5Phase10Controller24XTCBinauralEncoderLegacy10InitializeEv
+ __ZN5Phase10Controller24XTCBinauralEncoderLegacy14FilterMetadataD0Ev
+ __ZN5Phase10Controller24XTCBinauralEncoderLegacy14FilterMetadataD1Ev
+ __ZN5Phase10Controller24XTCBinauralEncoderLegacy20SetDeviceOrientationE13CAOrientation
+ __ZN5Phase10Controller24XTCBinauralEncoderLegacyD0Ev
+ __ZN5Phase10Controller24XTCBinauralEncoderLegacyD1Ev
+ __ZN5Phase10Controller24XTCBinauralEncoderLegacyD2Ev
+ __ZN5Phase10Controller28XTCBinauralSpatializerLegacy10InitializeEv
+ __ZN5Phase10Controller28XTCBinauralSpatializerLegacy20SetDeviceOrientationE13CAOrientation
+ __ZN5Phase10Controller28XTCBinauralSpatializerLegacyC2ERKNS0_11Spatializer14InitParametersERKNS0_9HrirAsset10LoadParamsEPKNS0_15BinauralUtilityE
+ __ZN5Phase10Controller28XTCBinauralSpatializerLegacyD0Ev
+ __ZN5Phase10Controller28XTCBinauralSpatializerLegacyD1Ev
+ __ZN5Phase10Controller28XTCBinauralSpatializerLegacyD2Ev
+ __ZN5Phase10Controller30InitializeXTCSpatializerLegacyEPPNS0_11SpatializerERKNS1_14InitParametersEPKNS0_15BinauralUtilityE
+ __ZN5Phase10Controller9HrirAsset10LoadParamsD1Ev
+ __ZN5Phase10Controller9HrirAsset14Implementation4NodeD1Ev
+ __ZN5Phase10Controller9HrirAsset17InterpolationDataD2Ev
+ __ZN5Phase10Controller9HrirAsset4LoadERKNS1_10LoadParamsE
+ __ZN5Phase10Controller9HrirAssetC2ERKNS1_10LoadParamsE
+ __ZNK5Phase10Controller24XTCBinauralEncoderLegacy14AcquireFiltersEv
+ __ZNK5Phase10Controller24XTCBinauralEncoderLegacy14GetDescriptionEv
+ __ZNK5Phase10Controller24XTCBinauralEncoderLegacy16GetNearestFilterERKNS0_23SpatializerFilterHandleERKNS_6VectorIfLm3EEEPv
+ __ZNK5Phase10Controller24XTCBinauralEncoderLegacy18GetCoordinateCountERKNS0_23SpatializerFilterHandleE
+ __ZNK5Phase10Controller24XTCBinauralEncoderLegacy19GetFiltersAndDelaysERKNS_6VectorIfLm3EEEjPPfS6_
+ __ZNK5Phase10Controller24XTCBinauralEncoderLegacy21GetOutputChannelCountEv
+ __ZNK5Phase10Controller24XTCBinauralEncoderLegacy24GetFilterLengthInSamplesERKNS0_23SpatializerFilterHandleE
+ __ZNK5Phase10Controller24XTCBinauralEncoderLegacy24GetWorkBufferSizeInBytesERKNS0_23SpatializerFilterHandleERKNS_6VectorIfLm3EEE
+ __ZNK5Phase10Controller9HrirAsset11InterpolateERKNSt3__16vectorIfNS2_9allocatorIfEEEE
+ __ZNK5Phase10Controller9HrirAsset14Implementation11InterpolateERKNSt3__16vectorIfNS3_9allocatorIfEEEEifRKNS4_INS2_4NodeENS5_ISA_EEEERNS1_17InterpolationDataE
+ __ZNK5Phase10Controller9HrirAsset28IsDeviceOrientationSupportedE13CAOrientation
+ __ZNSt3__114__split_bufferIN5Phase10Controller9HrirAsset14Implementation4NodeERNS_9allocatorIS5_EEED2Ev
+ __ZNSt3__116allocator_traitsINS_9allocatorIN5Phase10Controller9HrirAsset14Implementation4NodeEEEE7destroyB9nqe220106IS6_Li0EEEvRS7_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN5Phase10Controller9HrirAsset14Implementation4NodeEEEE9constructB9nqe220106IS6_JS6_ELi0EEEvRS7_PT_DpOT0_
+ __ZNSt3__120__shared_ptr_emplaceIN5Phase10Controller24XTCBinauralEncoderLegacy14FilterMetadataENS_9allocatorIS4_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIN5Phase10Controller24XTCBinauralEncoderLegacy14FilterMetadataENS_9allocatorIS4_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIN5Phase10Controller24XTCBinauralEncoderLegacy14FilterMetadataENS_9allocatorIS4_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIN5Phase10Controller24XTCBinauralEncoderLegacy14FilterMetadataENS_9allocatorIS4_EEED1Ev
+ __ZNSt3__120__shared_ptr_emplaceIN5Phase10Controller24XTCBinauralEncoderLegacyENS_9allocatorIS3_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIN5Phase10Controller24XTCBinauralEncoderLegacyENS_9allocatorIS3_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIN5Phase10Controller24XTCBinauralEncoderLegacyENS_9allocatorIS3_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIN5Phase10Controller24XTCBinauralEncoderLegacyENS_9allocatorIS3_EEED1Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB9nqe220106INS_9allocatorIN5Phase10Controller9HrirAsset14Implementation4NodeEEEPS6_EEvRT_T0_SB_SB_
+ __ZNSt3__16vectorIN5Phase10Controller9HrirAsset14Implementation4NodeENS_9allocatorIS5_EEE13__vdeallocateEv
+ __ZNSt3__16vectorIN5Phase10Controller9HrirAsset14Implementation4NodeENS_9allocatorIS5_EEE20__throw_length_errorB9nqe220106Ev
+ __ZNSt3__16vectorIN5Phase10Controller9HrirAsset14Implementation4NodeENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJS5_EEEPS5_DpOT_
+ __ZNSt3__16vectorIN5Phase10Controller9HrirAsset14Implementation4NodeENS_9allocatorIS5_EEE9push_backB9nqe220106EOS5_
+ __ZNSt3__16vectorIN5Phase10Controller9HrirAsset14Implementation9DimensionENS_9allocatorIS5_EEE20__throw_length_errorB9nqe220106Ev
+ __ZNSt3__16vectorIsNS_9allocatorIsEEE20__throw_length_errorB9nqe220106Ev
+ __ZNSt3__19allocatorIN5Phase10Controller9HrirAsset14Implementation4NodeEE17allocate_at_leastB9nqe220106Em
+ __ZTVN5Phase10Controller24XTCBinauralEncoderLegacy14FilterMetadataE
+ __ZTVN5Phase10Controller24XTCBinauralEncoderLegacyE
+ __ZTVN5Phase10Controller28XTCBinauralSpatializerLegacyE
+ __ZTVNSt3__120__shared_ptr_emplaceIN5Phase10Controller24XTCBinauralEncoderLegacy14FilterMetadataENS_9allocatorIS4_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceIN5Phase10Controller24XTCBinauralEncoderLegacyENS_9allocatorIS3_EEEE
+ _fclose
+ _fmemopen
+ _fopen
+ _fread
+ _fseek
+ _ftell
+ _rewind
CStrings:
+ "%25s:%-5d %s Initialized XTC binaural spatializer, with no orientation information."
+ "%25s:%-5d %s Initialized XTC binaural spatializer, with supported orientations { %s }"
+ "%25s:%-5d EXCEPTION (std::runtime_error) [dimensionCount == 0 is true]: \"Zero dimension count in hrtf file.\""
+ "%25s:%-5d EXCEPTION (std::runtime_error) [file.get() == nullptr is true]: \"Failed to open hrir file: %s (errno: %d)\""
+ "%25s:%-5d EXCEPTION (std::runtime_error) [objectsRead != 1 is true]: \"std::fread() failed\""
+ "%25s:%-5d EXCEPTION (std::runtime_error) [objectsRead != fileFilterLengthInSamples is true]: \"std::fread() failed\""
+ "%25s:%-5d EXCEPTION (std::runtime_error) [objectsRead != propertyListLengthInBytes is true]: \"std::fread() failed\""
+ "%25s:%-5d EXCEPTION (std::runtime_error) [std::ftell(file.get()) != fileSize is true]: \"Failed to parse entire hrtf file. Is this a version mismatch?\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Invalid CoefficientFormat\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Invalid DelayFormat\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Unknown CoefficientFormat\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Unknown DelayFormat\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Unknown Dimension DefaultValue\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Unknown Dimension Interpolation: %d\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Unknown Dimension Name\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Unknown Dimension Periodicity\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Unknown Dimensions\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Unknown FilterLength\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Unknown NumChannels\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Unknown SampleRate\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Unknown TotalNumCoordinates\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"[XTCBinauralSpatializerLegacy] No valid HRIR filter database for current orientation.\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"fade in/out ranges overlap\""
+ "%25s:%-5d Loading file HRIR asset"
+ "%25s:%-5d Loading personalized HRIR asset"
+ "%25s:%-5d PRECONDITION: IsDeviceOrientationSupported(static_cast<CAOrientation>(inDimensionValueVector[0])) is false."
+ "%25s:%-5d PRECONDITION: inDimension < inDimensionValueVector.size() is false."
+ "%25s:%-5d PRECONDITION: inDimensionValueVector.size() == mpImplementation->mDimensions.size() is false."
+ "%25s:%-5d PRECONDITION: mHRIRAsset->GetChannelsPerCoordinate() == 2 is false."
+ "%25s:%-5d PRECONDITION: mHRIRAsset->GetSampleRateInHertz() == mSpatializer->mInitParameters.mSampleRate is false."
+ "%25s:%-5d PRECONDITION: mpImplementation->mDimensions.begin() == lDimension is false."
+ "%25s:%-5d PRECONDITION: nullptr != mHRIRAsset.get() is false."
+ "<Encoder Type: XTCBinaural Legacy, Filter Length: %d, Output Channel Count: %d, Device Orientation: %s>"
+ "CoefficientFormat"
+ "Could not find item"
+ "DelayFormat"
+ "DelayScaleFactor"
+ "Description"
+ "Dimensions"
+ "Failed to open hrir file: %s (errno: %d)"
+ "Failed to parse entire hrtf file. Is this a version mismatch?"
+ "FilterLength"
+ "FilterScaleFactor"
+ "HRIR_XTC_default_wOrientation"
+ "HrirAsset.cpp"
+ "Interpolation"
+ "Invalid CoefficientFormat"
+ "Invalid DelayFormat"
+ "NumChannels"
+ "PRECONDITION: IsDeviceOrientationSupported(static_cast<CAOrientation>(inDimensionValueVector[0])) is false."
+ "PRECONDITION: inDimension < inDimensionValueVector.size() is false."
+ "PRECONDITION: inDimensionValueVector.size() == mpImplementation->mDimensions.size() is false."
+ "PRECONDITION: mHRIRAsset->GetChannelsPerCoordinate() == 2 is false."
+ "PRECONDITION: mHRIRAsset->GetSampleRateInHertz() == mSpatializer->mInitParameters.mSampleRate is false."
+ "PRECONDITION: mpImplementation->mDimensions.begin() == lDimension is false."
+ "PRECONDITION: nullptr != mHRIRAsset.get() is false."
+ "Periodicity"
+ "SampleRate"
+ "TotalNumCoordinates"
+ "Unknown CoefficientFormat"
+ "Unknown DelayFormat"
+ "Unknown Dimension DefaultValue"
+ "Unknown Dimension Interpolation: %d"
+ "Unknown Dimension Name"
+ "Unknown Dimension Periodicity"
+ "Unknown Dimensions"
+ "Unknown FilterLength"
+ "Unknown NumChannels"
+ "Unknown SampleRate"
+ "Unknown TotalNumCoordinates"
+ "XTCBinauralSpatializerLegacy.mm"
+ "Zero dimension count in hrtf file."
+ "[XTCBinauralSpatializerLegacy] No valid HRIR filter database for current orientation."
+ "fade in/out ranges overlap"
+ "ir"
+ "r"
+ "rb"
+ "std::fread() failed"
```
