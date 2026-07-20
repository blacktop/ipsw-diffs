## AppleProResHWEncoder.videoencoder

> `/System/Library/VideoEncoders/AppleProResHWEncoder.videoencoder`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`

```diff

-600.38.0.0.0
-  __TEXT.__text: 0x20820
+600.45.0.0.0
+  __TEXT.__text: 0x209c8
   __TEXT.__const: 0x746f0
   __TEXT.__gcc_except_tab: 0x310
-  __TEXT.__cstring: 0x1403
-  __TEXT.__oslogstring: 0x40f4
-  __TEXT.__unwind_info: 0x448
+  __TEXT.__cstring: 0x1491
+  __TEXT.__oslogstring: 0x4151
+  __TEXT.__unwind_info: 0x440
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x188
-  __AUTH_CONST.__cfstring: 0x360
+  __AUTH_CONST.__cfstring: 0x4a0
   __AUTH_CONST.__weak_auth_got: 0x40
   __AUTH_CONST.__auth_got: 0x598
   __DATA.__data: 0xb

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
-  - /System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   Functions: 494
-  Symbols:   603
-  CStrings:  403
+  Symbols:   593
+  CStrings:  414
 
Symbols:
- _kFigCaptureStreamMetadata_AGC
- _kFigCaptureStreamMetadata_AWBComboBGain
- _kFigCaptureStreamMetadata_AWBComboRGain
- _kFigCaptureStreamMetadata_ConversionGain
- _kFigCaptureStreamMetadata_DistortionOpticalCenterV2
- _kFigCaptureStreamMetadata_LensShadingModulationWeight
- _kFigCaptureStreamMetadata_PostDemosaicGain
- _kFigCaptureStreamMetadata_ReadNoise_1x
- _kFigCaptureStreamMetadata_ReadNoise_8x
- _kFigCaptureStreamMetadata_SensorCropRect
Functions:
~ __Z18findMetadataSetTagPhjRKjS1_ : 340 -> 364
~ __Z23addVDDMetadataToMetaExtPK14__CFDictionaryPNSt3__16vectorIhNS2_9allocatorIhEEEERhj : 976 -> 1272
~ __Z23addLSCMetadataToMetaExtPK14__CFDictionaryPNSt3__16vectorIhNS2_9allocatorIhEEEERhj : 560 -> 668
~ __Z22getLog2DownscaleFactorjjPj : 64 -> 60
CStrings:
+ "AD"
+ "AGC"
+ "AWBComboBGain"
+ "AWBComboRGain"
+ "ConversionGain"
+ "DistortionOpticalCenterV2"
+ "LensShadingModulationWeight"
+ "PostDemosaicGain"
+ "ReadNoise_1x"
+ "ReadNoise_8x"
+ "SensorCropRect"
+ "WARNING AppleProResHW (0x%x): %d: %s(): VDD metadata keys not present in metadataDictionary\n"
- "ProResRawNRMetadata"
```
