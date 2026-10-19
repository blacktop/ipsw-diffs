## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

 995.0.0.0.0
-  __TEXT.__text: 0x18e200
+  __TEXT.__text: 0x18e60c
   __TEXT.__objc_methlist: 0x1fc
   __TEXT.__const: 0xc4cf
-  __TEXT.__oslogstring: 0x161a6
-  __TEXT.__cstring: 0x562e
+  __TEXT.__oslogstring: 0x164b3
+  __TEXT.__cstring: 0x5669
   __TEXT.__gcc_except_tab: 0xe74
-  __TEXT.__unwind_info: 0x3c40
+  __TEXT.__unwind_info: 0x3c58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4380
+  Functions: 4388
   Symbols:   3658
-  CStrings:  2064
+  CStrings:  2072
 
CStrings:
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder ERROR: Could not enable multiview decoding\n"
+ "AppleAVD: ERROR: %{public}s(): calcLayersToDecodeFromDisplayLayersList ERROR: numLayersToDecode %d exceeds supported 2\n"
+ "AppleAVD: ERROR: %{public}s(): kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs cannot be changed after decoding has started (frame# %d)\n"
+ "AppleAVD: ERROR: %{public}s(): kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs error: invalid layer id at index %d\n"
+ "AppleAVD: ERROR: %{public}s(): kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs error: videoLayerID %d not declared in VPS at index %d\n"
+ "AppleAVD: ERROR: %{public}s(): kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs error: videoLayerID %d out of range [0, %d) at index %d\n"
+ "calcLayersToDecodeFromDisplayLayersList"
+ "m_avc_max_slices"
+ "too many slices!"
- "AVC_MAX_SLICES"
```
