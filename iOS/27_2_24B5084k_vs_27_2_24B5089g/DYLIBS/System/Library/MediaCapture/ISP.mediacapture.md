## ISP.mediacapture

> `/System/Library/MediaCapture/ISP.mediacapture`

```diff

-20.104.4.0.0
-  __TEXT.__text: 0x1edd00
+20.105.6.0.0
+  __TEXT.__text: 0x1eddb4
   __TEXT.__init_offsets: 0xc
   __TEXT.__objc_methlist: 0x270
   __TEXT.__gcc_except_tab: 0x5dcc
-  __TEXT.__const: 0x28d4d
+  __TEXT.__const: 0x28dcd
   __TEXT.__oslogstring: 0x238c7
-  __TEXT.__cstring: 0x1ac4d
+  __TEXT.__cstring: 0x1abf7
   __TEXT.__unwind_info: 0x6840
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x8e0
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x3ba8
+  __DATA_CONST.__got: 0x3bd8
   __AUTH_CONST.__const: 0x2580
-  __AUTH_CONST.__cfstring: 0xad40
+  __AUTH_CONST.__cfstring: 0xac80
   __AUTH_CONST.__objc_const: 0x8a0
   __AUTH_CONST.__weak_auth_got: 0xb0
   __AUTH_CONST.__objc_intobj: 0xd8

   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
   Functions: 6134
-  Symbols:   8096
-  CStrings:  7117
+  Symbols:   8102
+  CStrings:  7111
 
Symbols:
+ _kFigCaptureStreamMetadata_SmartTapAlgorithmMetadata
+ _kFigCaptureStreamSegmentFocusTrackingDataKey_FocusBias
+ _kFigCaptureStreamSegmentFocusTrackingDataKey_MaskConfidence
+ _kFigCaptureStreamSegmentFocusTrackingDataKey_ObjectID
+ _kFigCaptureStreamSegmentFocusTrackingDataKey_TotalPoints
+ _kFigCaptureStreamSegmentFocusTrackingDataKey_ValidCoverage
Functions:
~ __ZN3ISP23PCEFrontEtrogPresetListC2Ev : 180 -> 228
~ __ZL20StillImageCaptureNowPKvP16ISPCaptureStreamP15ISPCaptureGroupP16ISPCaptureDevice : 22816 -> 22836
~ __ZL22SetVideoOutputsEnabledPKvP16ISPCaptureStreamP15ISPCaptureGroupP16ISPCaptureDevice : 5120 -> 5316
~ __ZL33CopySupportedOutputConfigurationsPK13__CFAllocatorPvP16ISPCaptureStreamP15ISPCaptureGroupP16ISPCaptureDevice : 1024 -> 1052
~ __Z22MyISPFrameReceivedProcPvyjjPN3ISP33ISPFrameReceiverImageBufferStructE : 28096 -> 28100
~ __ZN3ISP35InitSupportedMetadataPropertiesDictERP14__CFDictionary : 52776 -> 52780
~ __ZN3ISP44GenerateAndAttachCoreMediaMetaDataDictionaryEP14__CFDictionaryP10__CVBufferPNSt3__15dequeIS3_NS4_9allocatorIS3_EEEEPNS_24ISPMetaDataOptionsStructEPNS_9ISPDeviceEdP19ISPCameraTimeStructPNS_26ISPOscarTimeSyncInfoStructE : 167968 -> 167848
CStrings:
- "FocusBias"
- "MaskConfidence"
- "ObjectID"
- "SmartTapAlgorithmMetadata"
- "TotalPoints"
- "ValidCoverage"
```
