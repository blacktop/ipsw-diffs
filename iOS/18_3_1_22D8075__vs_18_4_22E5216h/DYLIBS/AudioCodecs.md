## AudioCodecs

> `/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs`

```diff

-746.4.3.0.0
-  __TEXT.__text: 0x596a34
-  __TEXT.__auth_stubs: 0x1600
-  __TEXT.__const: 0x302e80
-  __TEXT.__gcc_except_tab: 0xfeec
-  __TEXT.__oslogstring: 0x17cc1
-  __TEXT.__cstring: 0xa522
+746.5.9.0.0
+  __TEXT.__text: 0x597804
+  __TEXT.__auth_stubs: 0x1540
+  __TEXT.__const: 0x3028cc
+  __TEXT.__cstring: 0xa21c
+  __TEXT.__gcc_except_tab: 0x104d4
+  __TEXT.__oslogstring: 0x17ba0
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0x8c00
-  __TEXT.__eh_frame: 0x680
+  __TEXT.__unwind_info: 0x89d8
+  __TEXT.__eh_frame: 0x790
   __DATA_CONST.__got: 0x258
-  __DATA_CONST.__const: 0xd318
-  __AUTH_CONST.__auth_got: 0xb08
+  __DATA_CONST.__const: 0xd2b8
+  __AUTH_CONST.__auth_got: 0xaa8
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0xe878
-  __AUTH_CONST.__cfstring: 0x42e0
+  __AUTH_CONST.__const: 0xf2a8
+  __AUTH_CONST.__cfstring: 0x4320
   __DATA.__data: 0x2d4
-  __DATA.__bss: 0x598
-  __DATA_DIRTY.__bss: 0xc8
+  __DATA.__bss: 0x5f8
+  __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 9028
-  Symbols:   9724
-  CStrings:  3071
+  Functions: 8789
+  Symbols:   9868
+  CStrings:  3044
 
Symbols:
+ _CFPreferencesGetAppBooleanValue
+ _CMBaseObjectIsMemberOfClass
+ _CMBlockBufferCreateWithMemoryBlock
+ _FigCPECryptorGetTypeID
+ _FigCPEFairPlayCryptorGetClassID
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTVNSt3__117bad_function_callE
+ ___strlcpy_chk
+ _kCFAllocatorDefault
+ _kCFAllocatorNull
- _IOConnectCallScalarMethod
- _IOConnectCallStructMethod
- _IOConnectMapMemory
- _IOConnectUnmapMemory
- _IOIteratorNext
- _IOObjectRelease
- _IOServiceClose
- _IOServiceGetMatchingServices
- _IOServiceMatching
- _IOServiceOpen
- __ZNKSt9exception4whatEv
- __ZNSt3__113basic_filebufIcNS_11char_traitsIcEEE5closeEv
- __ZNSt3__113basic_filebufIcNS_11char_traitsIcEEEC1Ev
- __ZNSt3__113basic_filebufIcNS_11char_traitsIcEEED1Ev
- __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__18ios_base4initEPv
- __ZNSt3__18ios_base5clearEj
- __ZNSt3__19basic_iosIcNS_11char_traitsIcEEED2Ev
- __ZTTNSt3__114basic_ifstreamIcNS_11char_traitsIcEEEE
- __ZTVNSt3__114basic_ifstreamIcNS_11char_traitsIcEEEE
- _kIOMainPortDefault
- _mach_task_self_
- _strncpy
CStrings:
+ "%25s:%-5d  ERROR: Failed to initialize Metadata reader"
+ "%25s:%-5d  ERROR: Failed to initialize binary metadata container"
+ "%25s:%-5d  ERROR: Invalid binary metadata pointer"
+ "%25s:%-5d  Error deserializing spectral data"
+ "%25s:%-5d  Error: Incorrect table index selection in ArithmeticCodingProcessor::Decompress"
+ "%25s:%-5d  Failed to initialize Ancillary Config"
+ "%25s:%-5d  Failed to initialize Ancillary DRC Loudness encoder"
+ "%25s:%-5d  Failed to initialize Ancillary data encoder"
+ "%25s:%-5d  Insufficient number of bits to decode"
+ "%25s:%-5d  Invalid number of mChannelBedChannelCount in ChannelBedHeadphoneMetadata::Deserialize"
+ "%25s:%-5d  MP4ALSSpecificConfig::Deserialize: channel position out of range"
+ "%25s:%-5d (%p) Error decrypting buffer, mCPECryptor = %p, err = %d\n"
+ "%25s:%-5d (%p) Insufficient output buffer size, ioBufferList->mBuffers[%d].mDataByteSize = %d bytes, required buffer size = %d\n"
+ "%25s:%-5d (%p) No cryptor set\n"
+ "%25s:%-5d (%p) error decoding from wrapped codec's ProduceOutputBufferList\n"
+ "%25s:%-5d (%p) error decoding from wrapped codec's ProduceOutputPackets\n"
+ "%25s:%-5d ERROR: Selection Set Index out of range\n"
+ "%25s:%-5d ERROR: version mismatch in downmix coefficient coding\n"
+ "12:42:04"
+ "563550AD-2332-40E8-8F46-D9BB1837A496"
+ "ACAC3CPEDecoderWrapper"
+ "ACAC3CPEDecoderWrapperNew"
+ "ACAPACCPEDecoderWrapper"
+ "ACAppleLosslessCPEDecoderWrapper"
+ "ACAtmosCPEDecoderWrapper"
+ "ACCPEDecoderWrapper.cpp"
+ "ACEC3CPEDecoderWrapper"
+ "ACFLACCPEDecoderWrapper"
+ "ACMP4AACCPEDecoderWrapper"
+ "ACMP4AACHECPEDecorderWrapper"
+ "ACMP4AACHEV2CPEDecorderWrapper"
+ "ACUSACCPEDecoderWrapper"
+ "Apple LLVM 17.0.0 (clang-1700.0.13.2) [+internal-os]"
+ "Apple QAC3 Transcoder"
+ "Apple ZAC3 Transcoder"
+ "Feb 21 2025"
+ "FeedWrappedCodec"
+ "GCC, version "
+ "asso_bed"
+ "description.mStartOffset == 0"
+ "fed"
+ "main_bed"
- "%25s:%-5d  Consumed more data than available"
- "%25s:%-5d  Error getting dataa stream element"
- "%25s:%-5d  Error in processing metadata source"
- "%25s:%-5d  Error: using reserved codebook"
- "%25s:%-5d  Failed to allocate memory for transcode metadata"
- "%25s:%-5d  Failed to initialize Extension Config"
- "%25s:%-5d  Failed to initialize base decoder"
- "%25s:%-5d  Failed to initialize extension encoder"
- "%25s:%-5d  Failed to initialize the PCM metadata"
- "%25s:%-5d  Failed to initialize the PCM metadata reader"
- "%25s:%-5d  MP4AudioESDS::Deserialize: the requested byte offset is not supported"
- "%25s:%-5d  Metadata Source is not initialized"
- "%25s:%-5d  Metadata source is not in PCMMetadata"
- "%25s:%-5d (%p) Decrypted format: %s"
- "%25s:%-5d (%p) FigCPECryptorGetNativeSession returned %d\n"
- "%25s:%-5d (%p) Setting FigCPECryptorRef\n"
- "%25s:%-5d (%p) subtype not recognized"
- "%25s:%-5d ACProtectedAC3PassThroughDecoder::Initialize: subtype not recognized"
- "%25s:%-5d ERROR: layer not supported %d (GetLayerElevation)\n"
- "%25s:%-5d ERROR: layer not supported %d (GetPanningPair)\n"
- "%25s:%-5d ERROR: layer not supported %d (GetPanningPairSelect)\n"
- "%25s:%-5d ERROR: layer not supported %d (getCPCount)\n"
- "%25s:%-5d ERROR: unexpected value"
- "%25s:%-5d ERROR: unexpected value of generalDrcConfigProfile : %d\n"
- "%25s:%-5d insufficient client buffer size\n"
- "%25s:%-5d kIOAudioCodecUserClientInitialize returned %d\n\n"
- "%25s:%-5d kIOAudioCodecUserClientProcessFrame returned %d\n\n"
- "%25s:%-5d kIOAudioCodecUserClientUninitialize returned %d\n\n"
- "01:22:20"
- "ACProtectedAACDecoder"
- "ACProtectedAACDecoder.cpp"
- "ACProtectedAC3PassThroughDecoder"
- "ACProtectedAC3PassThroughDecoder.cpp"
- "ACProtectedAPACDecoder"
- "ACProtectedAPACDecoder.cpp"
- "ACProtectedAppleLosslessDecoder"
- "ACProtectedAppleLosslessDecoder.cpp"
- "ACProtectedDDPAtmosDecoder"
- "ACProtectedDDPAtmosDecoder.cpp"
- "ACProtectedFLACDecoder"
- "ACProtectedFLACDecoder.cpp"
- "ACProtectedUSACDecoder"
- "ACProtectedUSACDecoder.cpp"
- "APACMetadata.h"
- "Apple LLVM 16.0.0 (clang-1600.0.26.6) [+internal-os]"
- "Cannot allocate memory"
- "Could not find a valid connection: No IOService"
- "Dec 20 2024"
- "Deserialize"
- "ERROR_t huff_dec_1D(HANDLE_CDK_BITSTREAM, const DATA_TYPE, const INT, SCHAR *, const INT, const INT)"
- "ERROR_t huff_dec_2D(HANDLE_CDK_BITSTREAM, const DATA_TYPE, const INT, const INT, SCHAR (*)[2], const INT, const INT, SCHAR **)"
- "IOAudioCodecAACDecoderInterface.cpp"
- "IOAudioCodecPassThroughInterface.cpp"
- "IOAudioCodecs"
- "IOServiceGetMatchingServices error"
- "IOServiceGetMatchingServices returned %d\n\n"
- "IOServiceOpen failed"
- "IOServiceOpen returned %d\n"
- "Not supported"
- "PassThroughDecode"
- "Protected APAC Decoder"
- "Reset"
- "SetFormats"
- "invalid frameClass"
- "kIOAudioCodecUserClientOpen failed"
- "kIOAudioCodecUserClientOpen returned %d\n"
- "m_connection"
- "void avq_dec::re8_decode_base_index(const int32_t, const int32_t, int32_t *const)"
- "~IOAudioCodecPassThroughInterface"

```
