## DeepVideoProcessingCore

> `/System/Library/PrivateFrameworks/DeepVideoProcessingCore.framework/DeepVideoProcessingCore`

```diff

-2.9.0.0.0
-  __TEXT.__text: 0x711dc
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0x5094
-  __TEXT.__const: 0x6b0
-  __TEXT.__cstring: 0x6051
-  __TEXT.__oslogstring: 0x3340
-  __TEXT.__gcc_except_tab: 0x2dc
-  __TEXT.__unwind_info: 0x1288
+2.10.0.0.0
+  __TEXT.__text: 0x6d674
+  __TEXT.__auth_stubs: 0xec0
+  __TEXT.__objc_methlist: 0x50b4
+  __TEXT.__const: 0x688
+  __TEXT.__cstring: 0x658b
+  __TEXT.__oslogstring: 0x33ab
+  __TEXT.__gcc_except_tab: 0x2e0
+  __TEXT.__unwind_info: 0x12f0
   __TEXT.__objc_classname: 0x6cb
-  __TEXT.__objc_methname: 0x13c2b
-  __TEXT.__objc_methtype: 0x77a0
-  __TEXT.__objc_stubs: 0x7760
+  __TEXT.__objc_methname: 0x13c81
+  __TEXT.__objc_methtype: 0x77ae
+  __TEXT.__objc_stubs: 0x77e0
   __DATA_CONST.__got: 0x388
   __DATA_CONST.__const: 0x310
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29c8
+  __DATA_CONST.__objc_selrefs: 0x29d8
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x7a8
+  __AUTH_CONST.__auth_got: 0x778
   __AUTH_CONST.__const: 0xf0
-  __AUTH_CONST.__cfstring: 0x3120
-  __AUTH_CONST.__objc_const: 0x111a8
+  __AUTH_CONST.__cfstring: 0x3260
+  __AUTH_CONST.__objc_const: 0x11208
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1900
-  __DATA.__objc_ivar: 0x1500
+  __DATA.__objc_ivar: 0x150c
   __DATA.__data: 0x260
   __DATA.__bss: 0x8
   __DATA.__common: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 79B6A6A5-CAFC-3610-803A-C8756866AFF5
-  Functions: 2473
-  Symbols:   8421
-  CStrings:  4657
+  UUID: 53A7E964-A3D3-37B8-B9DF-29BD7E4056A3
+  Functions: 2540
+  Symbols:   8602
+  CStrings:  4682
 
Symbols:
+ -[FRCProcessor processWithFrameRateParams:error:].cold.2
+ -[ImageProcessor preserveCMAttachmentFirstFrame:secondFrame:]
+ -[ImageProcessor restoreCMAttachmentToFirstFrame:secondFrame:]
+ -[VSRProcessor matchScaledBufferResolution:scaleFactor:]
+ _OBJC_IVAR_$_ImageProcessor._anchorFrameCMAttachment
+ _OBJC_IVAR_$_ImageProcessor._isFullRange
+ _OBJC_IVAR_$_VSRProcessor._scaleFactor
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _objc_msgSend$bufferHeight
+ _objc_msgSend$bufferWidth
+ _objc_msgSend$matchScaledBufferResolution:scaleFactor:
+ _objc_msgSend$restoreCMAttachmentToFirstFrame:secondFrame:
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ "B32@0:8@16q24"
+ "Skipping resolution check for scaled frames because base resolution is not set. Call matchBufferResolution first."
+ "Warning while calling preserveCMAttachmentFirstFrame"
+ "Warning while calling restoreCMAttachmentToFirstFrame"
+ "frameRateParams destination frame buffer resolution mismatch with FRCProcessor's buffer resolution for the DVPFrameProcessor session"
+ "frameRateParams reference frame buffer resolution mismatch with FRCProcessor's buffer resolution for the DVPFrameProcessor session"
+ "matchScaledBufferResolution:scaleFactor:"
+ "motionBlurParams destination frame buffer resolution mismatch with VSAProcessor's buffer resolution for the DVPFrameProcessor session"
+ "motionBlurParams next frame buffer resolution mismatch with VSAProcessor's buffer resolution for the DVPFrameProcessor session"
+ "motionBlurParams previous frame buffer resolution mismatch with VSAProcessor's buffer resolution for the DVPFrameProcessor session"
+ "opticalFlowParams next frame buffer resolution mismatch with OpticalFlowProcessor's buffer resolution for the DVPFrameProcessor session"
+ "restoreCMAttachmentToFirstFrame:secondFrame:"
+ "superResolutionParams destination frame buffer resolution mismatch with VSRProcessor's scaled output resolution for the DVPFrameProcessor session"
+ "superResolutionParams previous frame buffer resolution mismatch with VSRProcessor's buffer resolution for the DVPFrameProcessor session"
+ "superResolutionParams previous output frame buffer resolution mismatch with VSRProcessor's scaled output resolution for the DVPFrameProcessor session"

```
