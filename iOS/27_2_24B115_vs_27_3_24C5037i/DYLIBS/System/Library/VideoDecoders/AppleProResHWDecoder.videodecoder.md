## AppleProResHWDecoder.videodecoder

> `/System/Library/VideoDecoders/AppleProResHWDecoder.videodecoder`

```diff

-600.53.0.0.0
-  __TEXT.__text: 0x2192c
+602.0.0.0.0
+  __TEXT.__text: 0x21928
   __TEXT.__gcc_except_tab: 0x494
   __TEXT.__const: 0x743e0
   __TEXT.__cstring: 0x131f
-  __TEXT.__oslogstring: 0x487d
+  __TEXT.__oslogstring: 0x4888
   __TEXT.__unwind_info: 0x8b0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__weak_got: 0x8
Functions:
~ __ZL29ProResDecoder_GetSubFrameInfoP17ProResFrameHeaderP19ProResPictureHeaderPhjP25ProResDecoderSubFrameInfojb : 632 -> 612
~ __ZL31ProResDecoder_prepareInputFrameP27ProResDecoderPrivateStorageP25ProResDecoderSubFrameInfoP37ProRes_DecodeFrame_UserKernel_In_InfoPP10__CVBufferPhj : 1144 -> 1160
CStrings:
+ "ERROR AppleProResHW (0x%x): %d: %s(): Inconsistent subrame slices pSubFrameInfo->fr[%d].subFrameSize=%d subFrOffs=%d\n\n"
- "AppleProResHW (0x%x): %s(): Inconsistent subrame slices pSubFrameInfo->fr[%d].subFrameSize=%d subFrOffs=%d\n"
```
