## Cinematic

> `/System/Library/Frameworks/Cinematic.framework/Cinematic`

```diff

-436.120.4.0.0
-  __TEXT.__text: 0x1032c
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_methlist: 0xd1c
-  __TEXT.__const: 0x810
-  __TEXT.__cstring: 0x527
+478.0.0.0.0
+  __TEXT.__text: 0x12b28
+  __TEXT.__auth_stubs: 0x910
+  __TEXT.__objc_methlist: 0xdc4
+  __TEXT.__const: 0x960
+  __TEXT.__cstring: 0x617
+  __TEXT.__oslogstring: 0x6c6
   __TEXT.__gcc_except_tab: 0x25c
-  __TEXT.__oslogstring: 0x4c8
-  __TEXT.__constg_swiftt: 0x524
-  __TEXT.__swift5_typeref: 0x2e4
-  __TEXT.__swift5_reflstr: 0x203
-  __TEXT.__swift5_fieldmd: 0x31c
+  __TEXT.__constg_swiftt: 0x5b0
+  __TEXT.__swift5_typeref: 0x332
+  __TEXT.__swift5_reflstr: 0x22d
+  __TEXT.__swift5_fieldmd: 0x338
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x38
-  __TEXT.__swift5_types: 0x5c
-  __TEXT.__swift_as_entry: 0x20
-  __TEXT.__swift_as_ret: 0x18
+  __TEXT.__swift5_types: 0x60
+  __TEXT.__swift_as_entry: 0x2c
+  __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x730
-  __TEXT.__eh_frame: 0x338
-  __TEXT.__objc_classname: 0x172
-  __TEXT.__objc_methname: 0x2374
-  __TEXT.__objc_methtype: 0x806
-  __TEXT.__objc_stubs: 0x19c0
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x630
-  __DATA_CONST.__objc_classlist: 0xb8
+  __TEXT.__unwind_info: 0x7e0
+  __TEXT.__eh_frame: 0x448
+  __TEXT.__objc_classname: 0x18a
+  __TEXT.__objc_methname: 0x2777
+  __TEXT.__objc_methtype: 0x81e
+  __TEXT.__objc_stubs: 0x1dc0
+  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__const: 0x708
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a8
+  __DATA_CONST.__objc_selrefs: 0xae8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x438
-  __AUTH_CONST.__const: 0x638
-  __AUTH_CONST.__cfstring: 0x140
-  __AUTH_CONST.__objc_const: 0x1980
+  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_arraydata: 0x58
+  __AUTH_CONST.__auth_got: 0x498
+  __AUTH_CONST.__const: 0x6d0
+  __AUTH_CONST.__cfstring: 0x180
+  __AUTH_CONST.__objc_const: 0x1b10
+  __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x4b0
-  __AUTH.__data: 0x758
-  __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0x310
+  __AUTH.__objc_data: 0x500
+  __AUTH.__data: 0x840
+  __DATA.__objc_ivar: 0x6c
+  __DATA.__data: 0x2c8
   __DATA.__bss: 0x730
+  - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 76675DC0-F5C7-3C47-8F59-303ED62DACC8
-  Functions: 652
-  Symbols:   1435
-  CStrings:  579
+  UUID: 995DED1C-5888-3A00-8B4A-1F41096F9332
+  Functions: 724
+  Symbols:   1598
+  CStrings:  643
 
Symbols:
+ +[CNAssetSpatialAudioInfo checkIfContainsSpatialAudio:completionHandler:]
+ +[CNAssetSpatialAudioInfo findAssociatedRemixMetadata:completionHandler:]
+ +[CNAssetSpatialAudioInfo loadFromAsset:completionHandler:]
+ +[CNAssetSpatialAudioInfo loadFromAsset:completionHandler:].cold.1
+ -[CNAssetSpatialAudioInfo .cxx_destruct]
+ -[CNAssetSpatialAudioInfo assetReaderOutputSettingsForContentType:]
+ -[CNAssetSpatialAudioInfo assetWriterInputSettingsForContentType:]
+ -[CNAssetSpatialAudioInfo audioMixWithEffectIntensity:renderingStyle:]
+ -[CNAssetSpatialAudioInfo defaultEffectIntensity]
+ -[CNAssetSpatialAudioInfo defaultRenderingStyle]
+ -[CNAssetSpatialAudioInfo defaultSpatialAudioTrack]
+ -[CNAssetSpatialAudioInfo initWithSpatialAudioTrack:metadataBlob:]
+ -[CNAssetSpatialAudioInfo spatialAudioMixMetadata]
+ _AVChannelLayoutKey
+ _AVEncoderBitRateKey
+ _AVEncoderContentSourceKey
+ _AVFormatIDKey
+ _AVLinearPCMBitDepthKey
+ _AVLinearPCMIsFloatKey
+ _AVMediaTypeAudio
+ _AVSampleRateKey
+ _CFArrayContainsValue
+ _CFArrayGetCount
+ _CMAudioFormatDescriptionGetRichestDecodableFormat
+ _CMAudioFormatDescriptionGetStreamBasicDescription
+ _CMFormatDescriptionGetMediaSubType
+ _CMFormatDescriptionGetMediaType
+ _CMTimeGetSeconds
+ _FOAPlusDialogChannelLayoutAsData
+ _FigAudioFormatDescriptionGetEligibleCinematicAudioEffectVersion
+ _OBJC_CLASS_$_AVAudioMixCinematicAudioEffect
+ _OBJC_CLASS_$_AVMutableAudioMix
+ _OBJC_CLASS_$_AVMutableAudioMixInputParameters
+ _OBJC_CLASS_$_AVSampleBufferGenerator
+ _OBJC_CLASS_$_AVSampleBufferRequest
+ _OBJC_CLASS_$_AVURLAsset
+ _OBJC_CLASS_$_CNAssetSpatialAudioInfo
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_IVAR_$_CNAssetSpatialAudioInfo._metadataBlob
+ _OBJC_IVAR_$_CNAssetSpatialAudioInfo._spatialAudioTrack
+ _OBJC_METACLASS_$_CNAssetSpatialAudioInfo
+ __Block_copy
+ __Block_release
+ __DATA__TtC9Cinematic23CNAssetSpatialAudioInfo
+ __IVARS__TtC9Cinematic23CNAssetSpatialAudioInfo
+ __METACLASS_DATA__TtC9Cinematic23CNAssetSpatialAudioInfo
+ __OBJC_$_CLASS_METHODS_CNAssetSpatialAudioInfo
+ __OBJC_$_INSTANCE_METHODS_CNAssetSpatialAudioInfo
+ __OBJC_$_INSTANCE_VARIABLES_CNAssetSpatialAudioInfo
+ __OBJC_CLASS_RO_$_CNAssetSpatialAudioInfo
+ __OBJC_METACLASS_RO_$_CNAssetSpatialAudioInfo
+ ___59+[CNAssetSpatialAudioInfo loadFromAsset:completionHandler:]_block_invoke
+ ___59+[CNAssetSpatialAudioInfo loadFromAsset:completionHandler:]_block_invoke.6
+ ___59+[CNAssetSpatialAudioInfo loadFromAsset:completionHandler:]_block_invoke.6.cold.1
+ ___59+[CNAssetSpatialAudioInfo loadFromAsset:completionHandler:]_block_invoke.6.cold.2
+ ___59+[CNAssetSpatialAudioInfo loadFromAsset:completionHandler:]_block_invoke.cold.1
+ ___59+[CNAssetSpatialAudioInfo loadFromAsset:completionHandler:]_block_invoke.cold.2
+ ___59+[CNAssetSpatialAudioInfo loadFromAsset:completionHandler:]_block_invoke_2
+ ___73+[CNAssetSpatialAudioInfo checkIfContainsSpatialAudio:completionHandler:]_block_invoke
+ ___73+[CNAssetSpatialAudioInfo findAssociatedRemixMetadata:completionHandler:]_block_invoke
+ ___73+[CNAssetSpatialAudioInfo findAssociatedRemixMetadata:completionHandler:]_block_invoke.1
+ ___73+[CNAssetSpatialAudioInfo findAssociatedRemixMetadata:completionHandler:]_block_invoke.1.cold.1
+ ___73+[CNAssetSpatialAudioInfo findAssociatedRemixMetadata:completionHandler:]_block_invoke.cold.1
+ ___73+[CNAssetSpatialAudioInfo findAssociatedRemixMetadata:completionHandler:]_block_invoke.cold.2
+ ___73+[CNAssetSpatialAudioInfo findAssociatedRemixMetadata:completionHandler:]_block_invoke.cold.3
+ ___73+[CNAssetSpatialAudioInfo findAssociatedRemixMetadata:completionHandler:]_block_invoke.cold.4
+ ___73+[CNAssetSpatialAudioInfo findAssociatedRemixMetadata:completionHandler:]_block_invoke.cold.5
+ ___block_descriptor_32_e31_B32?0"AVMetadataItem"8Q16^B24l
+ ___block_descriptor_40_e8_32bs_e45_v24?0"CNAssetSpatialAudioInfo"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e16_v16?0"NSData"8ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_60_e8_32s40s48bs_e29_v24?0"NSArray"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s56l8s48l8
+ ___retrieveCinematicAudioRemixMetadataFromTrack_block_invoke
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_Cinematic
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_Cinematic
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_Cinematic
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_Cinematic
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_Cinematic
+ _block_copy_helper.1
+ _block_copy_helper.6
+ _block_descriptor.3
+ _block_descriptor.8
+ _block_destroy_helper.2
+ _block_destroy_helper.7
+ _getEligibleCinematicAudioVersion
+ _kCMTimeZero
+ _objc_msgSend$addEffect:
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$audioMix
+ _objc_msgSend$cinematicAudioEffectWithData:
+ _objc_msgSend$createSampleBufferForRequest:error:
+ _objc_msgSend$dataValue
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dictionary
+ _objc_msgSend$findAssociatedRemixMetadata:completionHandler:
+ _objc_msgSend$identifier
+ _objc_msgSend$indexOfObjectPassingTest:
+ _objc_msgSend$initWithAsset:timebase:
+ _objc_msgSend$initWithSpatialAudioTrack:metadataBlob:
+ _objc_msgSend$initWithStartCursor:
+ _objc_msgSend$isPlayable
+ _objc_msgSend$loadValuesAsynchronouslyForKeys:completionHandler:
+ _objc_msgSend$makeSampleCursorWithPresentationTimeStamp:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$setDialogMixBias:atTime:
+ _objc_msgSend$setDirection:
+ _objc_msgSend$setInputParameters:
+ _objc_msgSend$setMaxSampleCount:
+ _objc_msgSend$setPreferredMinSampleCount:
+ _objc_msgSend$setRenderingStyle:atTime:
+ _objc_msgSend$setTrackID:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$statusOfValueForKey:error:
+ _swift_retain
+ _symbolic SccySo23CNAssetSpatialAudioInfoC______pG s5ErrorP
+ _symbolic So23CNAssetSpatialAudioInfoC
+ _symbolic _____ 9Cinematic23CNAssetSpatialAudioInfoC
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_Cinematic
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_Cinematic
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_Cinematic
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_Cinematic
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_Cinematic
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_Cinematic
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_Cinematic
CStrings:
+ "@\"NSData\""
+ "@28@0:8f16q20"
+ "B32@?0@\"AVMetadataItem\"8Q16^B24"
+ "CNAssetSpatialAudioInfo"
+ "Error: (%@) failed to load playable property of asset %@"
+ "Error: (%@) no eligible audio tracks in asset %@"
+ "Error: (%@) no eligible referent tracks found for metadata track %@"
+ "Error: failed to load metadata tracks with error (%@)"
+ "Error: no metadata track found with required identifier"
+ "Error: no metadata track in asset %@ with metadata blob"
+ "Error: no metadata tracks found"
+ "Error: spatial audio track of asset %@ is not playable"
+ "Error: unsupported asset %@"
+ "_TtC9Cinematic23CNAssetSpatialAudioInfo"
+ "_metadataBlob"
+ "_spatialAudioTrack"
+ "addEffect:"
+ "appendBytes:length:"
+ "assetReaderOutputSettingsForContentType:"
+ "assetWriterInputSettingsForContentType:"
+ "audioMix"
+ "audioMixWithEffectIntensity:renderingStyle:"
+ "checkIfContainsSpatialAudio:completionHandler:"
+ "cinematicAudioEffectWithData:"
+ "createSampleBufferForRequest:error:"
+ "dataValue"
+ "dataWithBytes:length:"
+ "defaultEffectIntensity"
+ "defaultRenderingStyle"
+ "defaultSpatialAudioTrack"
+ "dictionary"
+ "failed to create cursor at cursorTime %0.3f, bad movie"
+ "findAssociatedRemixMetadata:completionHandler:"
+ "identifier"
+ "indexOfObjectPassingTest:"
+ "initWithAsset:timebase:"
+ "initWithSpatialAudioTrack:metadataBlob:"
+ "initWithStartCursor:"
+ "internalCNAssetSpatialAudioInfo"
+ "isPlayable"
+ "loadValuesAsynchronouslyForKeys:completionHandler:"
+ "makeSampleCursorWithPresentationTimeStamp:"
+ "mdta/com.apple.quicktime.cinematic-audio"
+ "numberWithBool:"
+ "numberWithDouble:"
+ "numberWithInteger:"
+ "numberWithUnsignedInt:"
+ "objectAtIndex:"
+ "objectAtIndexedSubscript:"
+ "playable"
+ "setDialogMixBias:atTime:"
+ "setDirection:"
+ "setInputParameters:"
+ "setMaxSampleCount:"
+ "setPreferredMinSampleCount:"
+ "setRenderingStyle:atTime:"
+ "setTrackID:"
+ "setValue:forKey:"
+ "spatialAudioMixMetadata"
+ "statusOfValueForKey:error:"
+ "v16@?0@\"NSData\"8"
+ "v24@?0@\"CNAssetSpatialAudioInfo\"8@\"NSError\"16"

```
