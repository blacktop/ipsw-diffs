## MOVStreamIO

> `/System/Library/PrivateFrameworks/MOVStreamIO.framework/MOVStreamIO`

```diff

-3.39.5.0.0
-  __TEXT.__text: 0x8bd2c
+3.40.1.0.0
+  __TEXT.__text: 0x95460
   __TEXT.__delay_stubs: 0x240
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x6c08
-  __TEXT.__const: 0x3c12
-  __TEXT.__cstring: 0x8d4d
-  __TEXT.__oslogstring: 0x3cc0
-  __TEXT.__gcc_except_tab: 0xe850
+  __TEXT.__objc_methlist: 0x6c88
+  __TEXT.__const: 0x4524
+  __TEXT.__cstring: 0x92a3
+  __TEXT.__oslogstring: 0x3cf6
+  __TEXT.__gcc_except_tab: 0xe890
   __TEXT.__ustring: 0x64a
-  __TEXT.__swift5_typeref: 0x127
-  __TEXT.__swift5_reflstr: 0x124
-  __TEXT.__swift5_assocty: 0x30
-  __TEXT.__constg_swiftt: 0xd0
-  __TEXT.__swift5_fieldmd: 0x1d8
-  __TEXT.__swift5_proto: 0x30
-  __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x36b0
-  __TEXT.__eh_frame: 0xb8
+  __TEXT.__swift5_typeref: 0x38e
+  __TEXT.__swift5_reflstr: 0x40c
+  __TEXT.__swift5_assocty: 0x78
+  __TEXT.__constg_swiftt: 0x3fc
+  __TEXT.__swift5_fieldmd: 0x464
+  __TEXT.__swift5_proto: 0x54
+  __TEXT.__swift5_types: 0x70
+  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_mpenum: 0x10
+  __TEXT.__swift5_capture: 0x18
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_cont: 0x18
+  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__unwind_info: 0x39a8
+  __TEXT.__eh_frame: 0x6f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xb90
-  __DATA_CONST.__objc_classlist: 0x3a8
+  __DATA_CONST.__const: 0xbb0
+  __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33d0
+  __DATA_CONST.__objc_selrefs: 0x3430
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x338
-  __DATA_CONST.__got: 0x8a8
-  __AUTH_CONST.__const: 0x1130
-  __AUTH_CONST.__cfstring: 0x6220
-  __AUTH_CONST.__objc_const: 0xf430
+  __DATA_CONST.__got: 0x9b0
+  __AUTH_CONST.__const: 0x1850
+  __AUTH_CONST.__cfstring: 0x6260
+  __AUTH_CONST.__objc_const: 0xf760
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0xbd8
-  __AUTH.__objc_data: 0x90
-  __DATA.__objc_ivar: 0x674
-  __DATA.__data: 0xb6c
-  __DATA.__common: 0x28
+  __AUTH_CONST.__auth_got: 0xf48
+  __AUTH.__objc_data: 0xe0
+  __AUTH.__data: 0x318
+  __DATA.__objc_ivar: 0x678
+  __DATA.__data: 0xc9c
+  __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x2440
   __DATA_DIRTY.__data: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2555
-  Symbols:   6018
-  CStrings:  1286
+  Functions: 2769
+  Symbols:   6172
+  CStrings:  1319
 
Symbols:
+ +[MOVStreamIOUtility isSlimTrack:withCompressionFormat:]
+ +[MOVStreamIOUtility isSlimYZipEncodedTrack:]
+ +[MOVStreamIOUtility slimYZipEncoderConfig]
+ +[MOVStreamOutputSettings slimCompressionFormatForConfiguration:]
+ -[MIOWriter finishWarning]
+ -[MIOWriter finishWithCompletionHandler:finishWarningHandler:]
+ -[MIOWriter finishWithTimeout:endTime:completionHandler:finishWarningHandler:]
+ -[MIOWriter setFinishWarning:]
+ -[MOVStreamReader grabNextMetadataForStream:timeRange:error:]
+ -[MOVStreamReader lastAVError]
+ _CMBlockBufferCopyDataBytes
+ _CMBlockBufferGetDataLength
+ _CMSampleBufferCreateReady
+ _CMSampleBufferGetSampleTimingInfo
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_MIOWriter._finishWarning
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _VTCompressionSessionEncodeFrameWithOutputHandler
+ _VTDecompressionSessionCreate
+ _VTDecompressionSessionDecodeFrameWithOutputHandler
+ _VTDecompressionSessionInvalidate
+ _VTDecompressionSessionWaitForAsynchronousFrames
+ _VTSessionSetProperties
+ __Block_copy
+ __Block_release
+ __DATA__TtC11MOVStreamIO18PixelBufferEncoder
+ __DATA__TtC11MOVStreamIO19SampleBufferDecoder
+ __DATA__TtC11MOVStreamIOP33_8135F46ADAFE8C6E6DC02D482E2F304215DecodeResultBox
+ __IVARS__TtC11MOVStreamIO18PixelBufferEncoder
+ __IVARS__TtC11MOVStreamIO19SampleBufferDecoder
+ __IVARS__TtC11MOVStreamIOP33_8135F46ADAFE8C6E6DC02D482E2F304215DecodeResultBox
+ __METACLASS_DATA__TtC11MOVStreamIO18PixelBufferEncoder
+ __METACLASS_DATA__TtC11MOVStreamIO19SampleBufferDecoder
+ __METACLASS_DATA__TtC11MOVStreamIOP33_8135F46ADAFE8C6E6DC02D482E2F304215DecodeResultBox
+ ___78-[MIOWriter finishWithTimeout:endTime:completionHandler:finishWarningHandler:]_block_invoke
+ ___block_descriptor_56_e8_32s40bs48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_88_e8_32bs40bs48w_e5_v8?0lw48l8s32l8s40l8
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_closure_destructor
+ ___swift_memcpy16_8
+ ___swift_memcpy24_4
+ ___swift_memcpy24_8
+ ___swift_memcpy25_8
+ ___swift_memcpy33_8
+ ___swift_memcpy4_4
+ ___swift_memcpy56_8
+ ___swift_memcpy8_8
+ __swift_dead_method_stub
+ __swift_implicitisolationactor_to_executor_cast
+ _associated conformance 11MOVStreamIO14VTSessionErrorO10Foundation09LocalizedD0AAs0D0
+ _associated conformance s6UInt32Vs26ExpressibleByStringLiteral11MOVStreamIO0dE4TypesACP_s01_bc7BuiltindE0
+ _associated conformance s6UInt32Vs26ExpressibleByStringLiteral11MOVStreamIOs0bc23ExtendedGraphemeClusterE0
+ _associated conformance s6UInt32Vs33ExpressibleByUnicodeScalarLiteral11MOVStreamIO0deF4TypesACP_s01_bc7BuiltindeF0
+ _associated conformance s6UInt32Vs43ExpressibleByExtendedGraphemeClusterLiteral11MOVStreamIO0defG4TypesACP_s01_bc7BuiltindefG0
+ _associated conformance s6UInt32Vs43ExpressibleByExtendedGraphemeClusterLiteral11MOVStreamIOs0bc13UnicodeScalarG0
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _get_enum_tag_for_layout_string 10Foundation4DataV15_RepresentationO
+ _get_enum_tag_for_layout_string 11MOVStreamIO14VTSessionErrorO
+ _get_enum_tag_for_layout_string 11MOVStreamIO30SampleBufferSerializationErrorO
+ _kMIOUseSlimYZipCompression
+ _kSlim_kVTCompressionPropertyKey_Format
+ _objc_msgSend$__swift_setObject:forKeyedSubscript:
+ _objc_msgSend$finishWithTimeout:endTime:completionHandler:finishWarningHandler:
+ _objc_msgSend$isSlimTrack:withCompressionFormat:
+ _objc_msgSend$setFinishWarning:
+ _objc_msgSend$slimCompressionFormatForConfiguration:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_allocError
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_initWithTake
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
+ _swift_deallocObject
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_deletedMethodError
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getErrorValue
+ _swift_getForeignTypeMetadata
+ _swift_getSingletonMetadata
+ _swift_lookUpClassMethod
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain
+ _swift_retain_x2
+ _swift_retain_x27
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_task_addCancellationHandler
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_removeCancellationHandler
+ _swift_task_switch
+ _swift_updateClassMetadata2
+ _swift_willThrow
+ _symbolic $ss26ExpressibleByStringLiteralP
+ _symbolic $ss33ExpressibleByUnicodeScalarLiteralP
+ _symbolic $ss43ExpressibleByExtendedGraphemeClusterLiteralP
+ _symbolic BD
+ _symbolic SDySSypG
+ _symbolic SS3key_yp5valuet
+ _symbolic SS_ypt
+ _symbolic Say_____G s5UInt8V
+ _symbolic ScCy___________pG 11MOVStreamIO19SampleBufferDecoderC12DecodedFrameV s5ErrorP
+ _symbolic ScCy___________pGSg 11MOVStreamIO19SampleBufferDecoderC12DecodedFrameV s5ErrorP
+ _symbolic Scsy___________pG So17CMSampleBufferRefa s5ErrorP
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ 11MOVStreamIO12BinaryReaderV
+ _symbolic _____ 11MOVStreamIO12BinaryWriterV
+ _symbolic _____ 11MOVStreamIO14VTSessionErrorO
+ _symbolic _____ 11MOVStreamIO15DecodeResultBox33_8135F46ADAFE8C6E6DC02D482E2F3042LLC
+ _symbolic _____ 11MOVStreamIO15DecodeResultBox33_8135F46ADAFE8C6E6DC02D482E2F3042LLC5StateO
+ _symbolic _____ 11MOVStreamIO18PixelBufferEncoderC
+ _symbolic _____ 11MOVStreamIO19SampleBufferDecoderC
+ _symbolic _____ 11MOVStreamIO19SampleBufferDecoderC12DecodedFrameV
+ _symbolic _____ 11MOVStreamIO19SampleBufferDecoderC12EncodedFrameV
+ _symbolic _____ 11MOVStreamIO30SampleBufferSerializationErrorO
+ _symbolic _____ So11CMTimeFlagsV
+ _symbolic _____ So11CVBufferRefa
+ _symbolic _____ So16os_unfair_lock_sV
+ _symbolic _____ So17CMSampleBufferRefa
+ _symbolic _____ So23VTCompressionSessionRefa
+ _symbolic _____ So25VTDecompressionSessionRefa
+ _symbolic _____ So6CMTimea
+ _symbolic _____ s5Int32V
+ _symbolic _____ s5Int64V
+ _symbolic _____Sg So6CMTimea
+ _symbolic _____XDXMT 11MOVStreamIO18PixelBufferEncoderC
+ _symbolic ______SS7contextt s5Int32V
+ _symbolic ______p s5ErrorP
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 11MOVStreamIO15DecodeResultBox33_8135F46ADAFE8C6E6DC02D482E2F3042LLC5StateO
+ _symbolic _____y_____SgG 2os21OSAllocatedUnfairLockV 11MOVStreamIO14VTSessionErrorO
+ _symbolic _____y_____Sg_____G s13ManagedBufferCsRi__rlE 11MOVStreamIO14VTSessionErrorO So16os_unfair_lock_sV
+ _symbolic _____y__________G s13ManagedBufferCsRi__rlE 11MOVStreamIO15DecodeResultBox33_8135F46ADAFE8C6E6DC02D482E2F3042LLC5StateO So16os_unfair_lock_sV
+ _symbolic _____y___________pG s6ResultOsRi_zRi0_zrlE 11MOVStreamIO19SampleBufferDecoderC12DecodedFrameV s5ErrorP
+ _symbolic _____y___________p_G Scs12ContinuationV So17CMSampleBufferRefa s5ErrorP
+ _symbolic _____y___________p__G Scs12ContinuationV11YieldResultO So17CMSampleBufferRefa s5ErrorP
+ _symbolic _____y___________p__G Scs12ContinuationV15BufferingPolicyO So17CMSampleBufferRefa s5ErrorP
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
+ _symbolic yp
+ _type_layout_string 11MOVStreamIO12BinaryReaderV
+ _type_layout_string 11MOVStreamIO12BinaryWriterV
+ _type_layout_string 11MOVStreamIO14VTSessionErrorO
+ _type_layout_string 11MOVStreamIO19SampleBufferDecoderC12DecodedFrameV
+ _type_layout_string 11MOVStreamIO19SampleBufferDecoderC12EncodedFrameV
+ _type_layout_string 11MOVStreamIO30SampleBufferSerializationErrorO
+ _type_layout_string So11CMTimeFlagsV
+ _type_layout_string So6CMTimea
- GCC_except_table85
- ___57-[MIOWriter finishWithTimeout:endTime:completionHandler:]_block_invoke
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- ___block_descriptor_88_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
- ___swift_memcpy32_8
- _kSlim_kVTCompressionPropertyKey_SlimXFormat
- _symbolic SaySJG
- _symbolic _____ySJG s23_ContiguousArrayStorageC
CStrings:
+ " failed with OSStatus "
+ " must be greater than the previous pts "
+ "3.40.1"
+ "CMBlockBufferCopyDataBytes"
+ "CMBlockBufferCreateWithMemoryBlock"
+ "CMBlockBufferReplaceDataBytes"
+ "CMSampleBufferCreateReady"
+ "CMSampleBufferGetSampleTimingInfo"
+ "CMVideoFormatDescriptionCreate"
+ "End of metadata stream."
+ "Plain 'slim' encoding is deprecated. Use slimX (kMIOUseSlimXCompression) or another encoder instead."
+ "UseSlimYZipCompression"
+ "VTCompressionSessionCompleteFrames"
+ "VTCompressionSessionCreate"
+ "VTCompressionSessionEncodeFrame"
+ "VTDecompressionSessionCreate"
+ "VTDecompressionSessionDecodeFrame"
+ "VTSessionError: "
+ "VTSessionError: frame was dropped"
+ "VTSessionError: invalid input - "
+ "VTSessionError: output callback fired with no buffer despite a successful status"
+ "VTSessionError: session has already been invalidated by finish()"
+ "VTSessionSetProperties"
+ "decode output callback"
+ "decoded plist was not a dictionary"
+ "encode output callback"
+ "expected exactly 1 sample, got "
+ "failed to decode plist dictionary: "
+ "failed to encode plist dictionary: "
+ "missing data buffer"
+ "missing video format description"
+ "payload too large to length-prefix: "
+ "sample data length overflows Int: "
+ "truncated record: expected "
+ "unsupported format version "
- "3.39.5"
- "Error on saving session start time: %{public}@"
```
