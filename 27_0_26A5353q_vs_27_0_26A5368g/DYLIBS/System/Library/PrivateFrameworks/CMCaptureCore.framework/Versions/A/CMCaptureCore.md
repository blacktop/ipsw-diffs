## CMCaptureCore

> `/System/Library/PrivateFrameworks/CMCaptureCore.framework/Versions/A/CMCaptureCore`

```diff

-748.0.0.0.2
-  __TEXT.__text: 0x1f6c sha256:81caab8b49ea0de261ba4f419ab24f4767da1d2df97549b1fb1e29d3a3b552ed
-  __TEXT.__cstring: 0xdd04 sha256:cd4aac082c40cfd5de0d6cb03b82c22983fe98ea12719cb9e529601c41a14462
+753.0.0.121.4
+  __TEXT.__text: 0x2084 sha256:35935cb8eb59c8060b447f39b7900b24f37a87131351839339212e2108643ba5
+  __TEXT.__cstring: 0xdde7 sha256:cf4d379f76cf60bfc63e8aef23916878830e8076c1e5ddddb79c2159cae99fa1
   __TEXT.__const: 0x25 sha256:031c6496f027acd96c8ae234a6335e00e03ad249171300455073cb94f16d142d
   __TEXT.__oslogstring: 0xa6 sha256:64932acfd64976011bab253fa8409f2ec826a007f0de65a3c56a005112dce31f
-  __TEXT.__unwind_info: 0x88 sha256:21b99b8af7b8cc1b741e663e3fb4e5b8b5d1a49a2d074f25cd1564420d4a585a
+  __TEXT.__unwind_info: 0x90 sha256:f414837e138e4f80b9f32867a155842c43de039a818fe695b3ffadec829ca3e7
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x5790 sha256:b85399f148a35a13edc25689ad690979a1f1514f5e3d0283d4340fad66249500
+  __DATA_CONST.__const: 0x57f8 sha256:8839fc1662b33555d42fca219402480ab8d058055c2a6e6b8f6c0627121bc8ff
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x10 sha256:7dac1e2bc89c640662876afa3406e3384146d4394f7216f31fabc64a2e4cc06d
+  __DATA_CONST.__objc_selrefs: 0x10 sha256:f489b4e60c81c186a5c685c171c682bc996d2db4ec02ac24754017c582289907
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__cfstring: 0x14300 sha256:681c1c6c99c20a43a21d894d3bb61514fa88af66622131ec7cbc8f15e3d03531
+  __AUTH_CONST.__cfstring: 0x14500 sha256:fb0f83ec4219868a1a3b9814753f93b9d5add5994a90a714ff78105e44a3ec8f
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__data: 0x8 sha256:c00275b56a4459b6d37f4b8f4b18d8090edcdf3733f669c76e23500b8d688827
+  __DATA.__data: 0x8 sha256:c838526523273209a49cfffdbb90873ac7274cdff8b386a4a2633a75545a2d44
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 60F08B36-6A44-3500-AA53-EB9E1F800EA4
-  Functions: 13
-  Symbols:   2926
-  CStrings:  5174
+  UUID: 51ED5468-400D-3FB0-8F56-2563335C4973
+  Functions: 14
+  Symbols:   2943
+  CStrings:  5206
 
Symbols:
+ _CFAutorelease
+ _CFStringAppend
+ _CFStringCreateMutable
+ _FigCaptureStillImageNRFProcessingFlagsToShortString
+ _kFigCaptureSampleBufferMetadata_SmartStyleEditInfos
+ _kFigCaptureSampleBufferMetadata_StructuredLightAutoFocusEnabled
+ _kFigCaptureSampleBufferMetadata_TimeOfFlightAutoFocusEnabled
+ _kFigCaptureStillImageProcessingMetadataKey_StillImageNRFProcessingFlags
+ _kFigCaptureStreamAHKey_MTE
+ _kFigCaptureStreamAHKey_TE
+ _kFigCaptureStreamMetadata_AH
+ _kFigCaptureStreamMetadata_InputSignals
+ _kFigCaptureStreamMetadata_Signals
+ _kFigCaptureStreamProperty_AHE
+ _kFigCaptureStreamProperty_LCTE
+ _kFigCaptureStreamProperty_MSS
+ _kFigQuicktimeMetadataKey_SmartStyleEditInfos
Functions:
~ _FigStartCaptureServers : 448 -> 444
~ _OUTLINED_FUNCTION_0 : sha256 a30ddda55a069cf5e2d3b31ff9a6ce04992156e172dfee360bc3bdf927ab3c76 -> ca197973c5785643d98867179af5f200de224cf5640f72a795bb660fbbdd0984
+ _FigCaptureStillImageNRFProcessingFlagsToShortString
~ _FigCaptureCopySerializableKeys : sha256 91c99e14b82b2f81db0242934a5ecfee9dd98057b681fbf86eb9de8df1fc4e01 -> eabdc8efe31e55416f403c81858c30a2908bf496b021884e84e64b4efa2b6a27
~ _FigCaptureStreamFocusingMethodIsContrastBased : sha256 60fb3937feb1cb49bacb38c05758388fd9a7ec2624eea84f6625dba576a77e33 -> dd6498c5b6cb8b4f58c76de418533bb41db4d98ac81b1ac82b895b4fca93a4e3
~ _FigCaptureStreamFocusingMethodIsPhaseDetectionBased : sha256 b1ff11f0a0178f05dcbde337b372203c62f203d2ce9428a16ec81a5d12dadb05 -> 500e8b4c0d5899f4b098301147ca490acec4f874468aa0886ac3728cf54e97bf
~ _FigCapturePortTypeIsFrontColorCamera : sha256 d8a05e38e3d9bb4e6a588c55ed567350a653338274bb37b818f784305b963a12 -> 7aa8606e3ec393173b42bd7b6482f8d6c17f0a64c70c463399b9aeb050edf4e7
~ _FigCapturePortTypeIsFrontSuperWideColorCamera : sha256 03711315789fd1480490f5b1417681618f162050a4e655c5f042305436c3f477 -> 97704c77b73a993e8e70506a8a8f09a992342cbb97952f38666bde83bdc761b1
~ _FigCapturePortTypeIsBackColorCamera : sha256 22bae83dc0ee7ebc260b6a5826f7744908701ae597def3bc9d88589c646481b0 -> 17121895ad6668ef4bf8dffe59e3433991002189cf208500e800c69021e9e3df
~ _FigCapturePortTypeIsExternalCamera : sha256 0007130741532a6a4297a847372f3d093239b1ab0b5464bd582c348a66223b6f -> ecbb65286f614463b0dda4744932e5f005859010106e32ea071687d4267f0942
~ FigStartCaptureServers.cold.1 : sha256 a0b59f5fe0c0dfa4cd357832f0529470dea9920e637e135ca18e4e1deb1dc856 -> a306f9af58d8ca002b716212235b5b0bfcecaaca3e1120f9b241df5db96f6eae
~ FigStartCaptureServers.cold.2 : sha256 13de5bee003914b4f4f6cd2da43414e0cd8c4930323538f26885f3c2ec0b9660 -> b59b04d5ca9ed4af521029b9ebbe7f48b57272fb9e0079c3033d9dc034ddc2b3
~ FigStartCaptureServers.cold.3 : sha256 48b21f72ccac708647b32a5379ec5e97060a57430a83d08a0418b9df5f3e7726 -> 6dd6c3163645359e321ea732ed89b05e010ef2141567250e3e108b5b28ef3c6a
~ _FigCaptureComputeImageGainFromMetadata : sha256 e2782256377b76b3aec36fa94f874a4788116de9a7fb9c839f88483721019328 -> 1a84d793a0325c3551c0cc2f4b8ed5b311d39832a99bd61df909ca05d2fd0a93
CStrings:
+ ", "
+ "AH"
+ "AHE"
+ "DisableDNR"
+ "InputSignals"
+ "LCTE"
+ "MSS"
+ "MTE"
+ "NonPhotoFormat"
+ "Signals"
+ "SmartStyleEditInfos"
+ "StillImageNRFProcessingFlags"
+ "StructuredLightAutoFocusEnabled"
+ "TE"
+ "TimeOfFlightAutoFocusEnabled"
+ "com.apple.quicktime.smartstyle.edit.infos"
+ "description=CameraCapture_CMCore-753.0.0.121.4"
- "description=CameraCapture_CMCore-748.0.0.0.2"

```
