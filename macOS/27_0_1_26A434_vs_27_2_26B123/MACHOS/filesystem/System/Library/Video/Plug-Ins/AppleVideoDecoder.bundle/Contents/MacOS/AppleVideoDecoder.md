## AppleVideoDecoder

> `/System/Library/Video/Plug-Ins/AppleVideoDecoder.bundle/Contents/MacOS/AppleVideoDecoder`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-993.1.0.0.0
-  __TEXT.__text: 0x14cf20
-  __TEXT.__auth_stubs: 0xf70
+995.0.0.0.0
+  __TEXT.__text: 0x14d380
+  __TEXT.__auth_stubs: 0xf80
   __TEXT.__const: 0xbf90
-  __TEXT.__oslogstring: 0x157cf
-  __TEXT.__cstring: 0x5301
+  __TEXT.__oslogstring: 0x15adc
+  __TEXT.__cstring: 0x533c
   __TEXT.__gcc_except_tab: 0x968
-  __TEXT.__unwind_info: 0x3310
+  __TEXT.__unwind_info: 0x3330
   __DATA_CONST.__const: 0x4670
   __DATA_CONST.__cfstring: 0x6e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x7c0
+  __DATA_CONST.__auth_got: 0x7c8
   __DATA_CONST.__got: 0x328
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__data: 0x88

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3682
-  Symbols:   361
-  CStrings:  2001
+  Functions: 3692
+  Symbols:   362
+  CStrings:  2009
 
Symbols:
+ _arc4random_buf
CStrings:
+ "23:18:23"
+ "23:18:24"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder ERROR: Could not enable multiview decoding\n"
+ "AppleAVD: ERROR: %{public}s(): calcLayersToDecodeFromDisplayLayersList ERROR: numLayersToDecode %d exceeds supported 2\n"
+ "AppleAVD: ERROR: %{public}s(): kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs cannot be changed after decoding has started (frame# %d)\n"
+ "AppleAVD: ERROR: %{public}s(): kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs error: invalid layer id at index %d\n"
+ "AppleAVD: ERROR: %{public}s(): kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs error: videoLayerID %d not declared in VPS at index %d\n"
+ "AppleAVD: ERROR: %{public}s(): kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs error: videoLayerID %d out of range [0, %d) at index %d\n"
+ "Oct 14 2026"
+ "calcLayersToDecodeFromDisplayLayersList"
+ "m_avc_max_slices"
+ "too many slices!"
- "20:48:33"
- "20:48:34"
- "AVC_MAX_SLICES"
- "Aug 11 2026"
```
