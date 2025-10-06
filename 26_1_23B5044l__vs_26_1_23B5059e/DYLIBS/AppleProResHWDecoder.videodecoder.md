## AppleProResHWDecoder.videodecoder

> `/System/Library/VideoDecoders/AppleProResHWDecoder.videodecoder`

```diff

-501.1.0.0.0
-  __TEXT.__text: 0x231b4
-  __TEXT.__auth_stubs: 0xa20
-  __TEXT.__const: 0x74120
-  __TEXT.__gcc_except_tab: 0x45c
-  __TEXT.__cstring: 0x111b
-  __TEXT.__oslogstring: 0x3dd3
-  __TEXT.__unwind_info: 0x3e8
-  __DATA_CONST.__got: 0x1f0
-  __AUTH_CONST.__auth_got: 0x518
+501.4.0.0.0
+  __TEXT.__text: 0x246b0
+  __TEXT.__auth_stubs: 0xaf0
+  __TEXT.__const: 0x741a0
+  __TEXT.__gcc_except_tab: 0x4c0
+  __TEXT.__cstring: 0x1245
+  __TEXT.__oslogstring: 0x3f85
+  __TEXT.__unwind_info: 0x440
+  __DATA_CONST.__got: 0x248
+  __AUTH_CONST.__auth_got: 0x580
   __AUTH_CONST.__const: 0x138
-  __AUTH_CONST.__cfstring: 0xc0
+  __AUTH_CONST.__cfstring: 0x160
   __DATA.__data: 0xb
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: B129D8EB-9578-3D05-87AB-5EC453C1DF22
-  Functions: 470
-  Symbols:   1320
-  CStrings:  375
+  UUID: 4B910D85-4E5A-3A41-B61E-201D742D7442
+  Functions: 485
+  Symbols:   1383
+  CStrings:  402
 
Symbols:
+ GCC_except_table10
+ GCC_except_table13
+ GCC_except_table16
+ GCC_except_table30
+ _CFDataCreateWithBytesNoCopy
+ _CFDataGetBytePtr
+ _CFDataGetBytes
+ _CFDataGetLength
+ _CFPropertyListCreateData
+ _CFPropertyListCreateWithData
+ _CGPointMakeWithDictionaryRepresentation
+ _CGRectMakeWithDictionaryRepresentation
+ __Z18findMetadataSetTagPhjRKjS1_
+ __Z18writeMExtHeaderTagPNSt3__16vectorIhNS_9allocatorIhEEEEjjj
+ __Z19addEOMDTagToMetaExtPNSt3__16vectorIhNS_9allocatorIhEEEE
+ __Z23addGDCMetadataToMetaExtPK14__CFDictionaryPNSt3__16vectorIhNS2_9allocatorIhEEEERhj
+ __Z23addLSCMetadataToMetaExtPK14__CFDictionaryPNSt3__16vectorIhNS2_9allocatorIhEEEERhj
+ __Z23addVDDMetadataToMetaExtPK14__CFDictionaryPNSt3__16vectorIhNS2_9allocatorIhEEEERhj
+ __Z23writeMExtPSIMIdentifierPNSt3__16vectorIhNS_9allocatorIhEEEEjjPKc
+ __Z28addISPDebugMetadataToMetaExtPK14__CFDictionaryPNSt3__16vectorIhNS2_9allocatorIhEEEERhjPcj
+ __Z28copyMetadataSetToMetadataExtPhPNSt3__16vectorIhNS0_9allocatorIhEEEEj
+ __Z29checkIfMetadataTagsArePresentPNSt3__16vectorIhNS_9allocatorIhEEEEP20MEXT_VALIDITY_STRUCT
+ __Z32checkGDCMetadataFromFrameMetaExtjjPhj
+ __Z32checkLSCMetadataFromFrameMetaExtjjPhj
+ __Z32checkPlatformForProResRAWSupportv
+ __Z32checkVDDMetadataFromFrameMetaExtjjPhj
+ __Z36ProResDecoder_ParseMetadataExtensionP17ProResFrameHeaderPNSt3__16vectorIhNS1_9allocatorIhEEEEPhjPcjj.cold.1
+ __Z36ProResDecoder_ParseMetadataExtensionP17ProResFrameHeaderPNSt3__16vectorIhNS1_9allocatorIhEEEEPhjPcjj.cold.2
+ __Z39extractISPDebugMetadataFromFrameMetaExtjjPhjPNSt3__16vectorIhNS0_9allocatorIhEEEEPPK14__CFDictionaryPcjj
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE8__appendEm
+ _fclose
+ _fopen
+ _fwrite
+ _kCFAllocatorNull
+ _kFigCaptureStreamMetadata_AGC
+ _kFigCaptureStreamMetadata_AWBComboBGain
+ _kFigCaptureStreamMetadata_AWBComboRGain
+ _kFigCaptureStreamMetadata_ConversionGain
+ _kFigCaptureStreamMetadata_DistortionOpticalCenterV2
+ _kFigCaptureStreamMetadata_LensShadingModulationWeight
+ _kFigCaptureStreamMetadata_PostDemosaicGain
+ _kFigCaptureStreamMetadata_ReadNoise_1x
+ _kFigCaptureStreamMetadata_ReadNoise_8x
+ _kFigCaptureStreamMetadata_SensorCropRect
+ _strncmp
+ _sysctlbyname
- GCC_except_table29
- __Z16checkFrameHeaderP17ProResFrameHeaderb21ProRes_UserClientTypej.cold.16
CStrings:
+ "%s/frame-%03d.plist"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Error in parsing MetadataExt for frame %d\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Only EOMD presenty in metaExt for Frame %d\n"
+ "PreDemosaicGain"
+ "ProResDecoder_ParseMetadataExtension"
+ "ProResRawGDCMetadata"
+ "ProResRawNRMetadata"
+ "TemporalHomographyMatrix"
+ "V53"
+ "V54"
+ "WARNING AppleProResHW (0x%x): %d: %s(): Invalid Homography Matrix size: %zu, expected: %zu\n"
+ "WARNING AppleProResHW (0x%x): %d: %s(): Invalid metadata present for frame %d in metadataExt\n"
+ "WARNING AppleProResHW (0x%x): %d: %s(): LSC metadata keys not present in metadataDictionary\n"
+ "WARNING AppleProResHW (0x%x): %d: %s(): No encoded alpha, assuming the frame is opaque\n"
+ "WarpRectilinear2"
+ "addLSCMetadataToMetaExt"
+ "addVDDMetadataToMetaExt"
+ "com.apple.gdc"
+ "com.apple.ispdebugmetadata"
+ "com.apple.lsc"
+ "com.apple.vdd"
+ "hw.targettype"
+ "wb"
- "ERROR AppleProResHW (0x%x): %d: %s(): No encoded alpha when frame is supposed to be non-opaque\n"

```
