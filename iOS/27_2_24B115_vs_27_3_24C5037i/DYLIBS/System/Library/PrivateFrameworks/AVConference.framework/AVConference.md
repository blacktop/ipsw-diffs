## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2260.15.1.0.0
-  __TEXT.__text: 0x7db580
-  __TEXT.__objc_methlist: 0x3ad90
+2265.2.1.0.0
+  __TEXT.__text: 0x7db7bc
+  __TEXT.__objc_methlist: 0x3ada0
   __TEXT.__const: 0xc690
-  __TEXT.__cstring: 0x9fe77
-  __TEXT.__oslogstring: 0x144e55
+  __TEXT.__cstring: 0x9fe76
+  __TEXT.__oslogstring: 0x144ecb
   __TEXT.__gcc_except_tab: 0x2ddc
   __TEXT.__ustring: 0x2d4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1b7c0
+  __TEXT.__unwind_info: 0x1b7c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x77f8
+  __DATA_CONST.__const: 0x7800
   __DATA_CONST.__objc_classlist: 0x14b0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x508
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18ed0
+  __DATA_CONST.__objc_selrefs: 0x18ed8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x1260
   __DATA_CONST.__objc_arraydata: 0x27d8

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 35559
-  Symbols:   42090
-  CStrings:  34195
+  Functions: 35560
+  Symbols:   42092
+  CStrings:  34196
 
Symbols:
+ -[VCVideoStream shouldSkipVideoJitterBuffer:]
+ _kVCRateControlMachineLearningInferenceQueueSpecificKey
Functions:
~ __VCVideoPacketBuffer_AssembleFrame : 14648 -> 14812
~ _VideoDecoder_VTDecompressionCallback : 3712 -> 3928
~ -[VCSwitchManager initializeLocalSwitches] : 668 -> 704
~ _VCVideoCaptureServer_OnCaptureVideoFrame : 2716 -> 2712
~ -[VCRateControlMachineLearningInference initWithModelPath:] : 328 -> 348
~ -[VCRateControlMachineLearningInference dealloc] : 196 -> 232
+ -[VCVideoStream shouldSkipVideoJitterBuffer:]
~ -[VCVideoStream videoReceiverConfigWithVideoStreamConfig:] : 4544 -> 4568
~ _VCVideoCaptureServer_OnCaptureVideoFrame.cold.2 : 128 -> 124
CStrings:
+ " [%s] %s:%d SwitchManager: A/B testing turned off - using master local switch: %08X"
+ " [%s] %s:%d videoDecoder=%p decoded frame CGColorSpace attachment restored for streamID=%d width=%d height=%d"
+ "2265.2.1"
- " [%s] %s:%d SwitchManager: Non-seed build - using master local switch: %08X"
- "2260.15.1"
```
