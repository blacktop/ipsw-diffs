## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-908.0.0.0.0
-  __TEXT.__text: 0x1536c8
+959.1.0.0.0
+  __TEXT.__text: 0x162f04
   __TEXT.__auth_stubs: 0xe80
-  __TEXT.__const: 0xc153
-  __TEXT.__gcc_except_tab: 0x8bc
-  __TEXT.__oslogstring: 0x10386
-  __TEXT.__cstring: 0x5bcb
-  __TEXT.__unwind_info: 0x1980
-  __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x18
+  __TEXT.__const: 0xc193
+  __TEXT.__gcc_except_tab: 0x940
+  __TEXT.__oslogstring: 0x140ce
+  __TEXT.__cstring: 0x522d
+  __TEXT.__unwind_info: 0x1b08
+  __DATA_CONST.__got: 0x340
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x748
-  __AUTH_CONST.__const: 0x4800
-  __AUTH_CONST.__cfstring: 0x720
+  __AUTH_CONST.__const: 0x4d60
+  __AUTH_CONST.__cfstring: 0x660
   __DATA.__common: 0x30
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: E76A047A-8826-3ED1-8340-611AA546DCE0
-  Functions: 2246
-  Symbols:   5508
-  CStrings:  1988
+  UUID: 5C057A16-6778-34B4-9D56-AABFF61938FD
+  Functions: 3913
+  Symbols:   10481
+  CStrings:  1977
 
Symbols:
+ _AVDRegister.cold.1
+ _AVDRegister.cold.2
+ _AVDRegister.cold.3
+ _AVDRegister.cold.4
+ _AVDRegister.cold.5
+ _AVDRegister.cold.6
+ _AppleAVDAllocateCVPixelBuffer.cold.1
+ _AppleAVDAllocateCVPixelBuffer.cold.2
+ _AppleAVDAllocateCVPixelBuffer.cold.3
+ _AppleAVDAllocateCVPixelBuffer.cold.4
+ _AppleAVDCheckPlatform.cold.1
+ _AppleAVDCreateDecodeDeviceInternal.cold.1
+ _AppleAVDCreateDecodeDeviceInternal.cold.2
+ _AppleAVDCreateDecodeDeviceInternal.cold.3
+ _AppleAVDDecodeFrame.cold.1
+ _AppleAVDDecodeFrame.cold.10
+ _AppleAVDDecodeFrame.cold.2
+ _AppleAVDDecodeFrame.cold.3
+ _AppleAVDDecodeFrame.cold.4
+ _AppleAVDDecodeFrame.cold.5
+ _AppleAVDDecodeFrame.cold.6
+ _AppleAVDDecodeFrame.cold.7
+ _AppleAVDDecodeFrame.cold.8
+ _AppleAVDDecodeFrame.cold.9
+ _AppleAVDDecodeFrameInternal.cold.1
+ _AppleAVDDecodeFrameInternal.cold.2
+ _AppleAVDDecodeFrameInternal.cold.3
+ _AppleAVDDecodeFrameInternal.cold.4
+ _AppleAVDDestroyDecodeDeviceInternal.cold.1
+ _AppleAVDGetParameter.cold.1
+ _AppleAVDGetPixelBufferFromBufferPool.cold.1
+ _AppleAVDGetPixelBufferFromBufferPool.cold.2
+ _AppleAVDGetPixelBufferFromBufferPool.cold.3
+ _AppleAVDGetSecondPixelBufferFromBufferPoolAndLink.cold.1
+ _AppleAVDInitializeDecoder.cold.1
+ _AppleAVDInitializeDecoder.cold.2
+ _AppleAVDInitializeDecoder.cold.3
+ _AppleAVDInitializeDecoder.cold.4
+ _AppleAVDInitializeDecoder.cold.5
+ _AppleAVDMapPixelBuffer.cold.1
+ _AppleAVDOpenConnection.cold.3
+ _AppleAVDOpenConnection.cold.4
+ _AppleAVDPutTiledPixelBufferIntoBufferPool.cold.1
+ _AppleAVDPutTiledPixelBufferIntoBufferPool.cold.2
+ _AppleAVDTerminateDecoder.cold.1
+ _AppleAVDTerminateDecoder.cold.2
+ _AppleAVDUnmapPixelBuffer.cold.1
+ _AppleAVDWrapperFghrnDecoderCleanUp.cold.1
+ _AppleAVDWrapperFghrnDecoderCleanUp.cold.2
+ _AppleAVDWrapperFghrnDecoderCopyProperty.cold.1
+ _AppleAVDWrapperFghrnDecoderCreateInstance.cold.1
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.1
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.10
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.11
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.12
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.13
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.14
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.15
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.16
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.17
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.2
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.3
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.4
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.5
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.6
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.7
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.8
+ _AppleAVDWrapperFghrnDecoderDecodeFrame.cold.9
+ _AppleAVDWrapperFghrnDecoderDecodeTile.cold.1
+ _AppleAVDWrapperFghrnDecoderDecodeTile.cold.10
+ _AppleAVDWrapperFghrnDecoderDecodeTile.cold.2
+ _AppleAVDWrapperFghrnDecoderDecodeTile.cold.3
+ _AppleAVDWrapperFghrnDecoderDecodeTile.cold.4
+ _AppleAVDWrapperFghrnDecoderDecodeTile.cold.5
+ _AppleAVDWrapperFghrnDecoderDecodeTile.cold.6
+ _AppleAVDWrapperFghrnDecoderDecodeTile.cold.7
+ _AppleAVDWrapperFghrnDecoderDecodeTile.cold.8
+ _AppleAVDWrapperFghrnDecoderDecodeTile.cold.9
+ _AppleAVDWrapperFghrnDecoderSetProperty.cold.1
+ _AppleAVDWrapperFghrnDecoderSetProperty.cold.2
+ _AppleAVDWrapperFghrnDecoderSetProperty.cold.3
+ _AppleAVDWrapperFghrnDecoderStartSession.cold.1
+ _AppleAVDWrapperFghrnDecoderStartSession.cold.2
+ _AppleAVDWrapperFghrnDecoderStartSession.cold.3
+ _AppleAVDWrapperFghrnDecoderStartSession.cold.4
+ _AppleAVDWrapperFghrnDecoderStartSession.cold.5
+ _AppleAVDWrapperFghrnDecoderStartSession.cold.6
+ _AppleAVDWrapperFghrnDecoderStartTileSession.cold.1
+ _AppleAVDWrapperFghrnDecoderStartTileSession.cold.10
+ _AppleAVDWrapperFghrnDecoderStartTileSession.cold.2
+ _AppleAVDWrapperFghrnDecoderStartTileSession.cold.3
+ _AppleAVDWrapperFghrnDecoderStartTileSession.cold.4
+ _AppleAVDWrapperFghrnDecoderStartTileSession.cold.5
+ _AppleAVDWrapperFghrnDecoderStartTileSession.cold.6
+ _AppleAVDWrapperFghrnDecoderStartTileSession.cold.7
+ _AppleAVDWrapperFghrnDecoderStartTileSession.cold.8
+ _AppleAVDWrapperFghrnDecoderStartTileSession.cold.9
+ _AppleAVDWrapperH264DecoderCleanUp.cold.1
+ _AppleAVDWrapperH264DecoderCleanUp.cold.2
+ _AppleAVDWrapperH264DecoderCopyProperty.cold.1
+ _AppleAVDWrapperH264DecoderCreateInstance.cold.1
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.1
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.10
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.11
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.12
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.13
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.14
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.15
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.16
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.17
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.18
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.19
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.2
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.20
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.21
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.22
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.23
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.24
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.3
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.4
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.5
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.6
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.7
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.8
+ _AppleAVDWrapperH264DecoderDecodeFrame.cold.9
+ _AppleAVDWrapperH264DecoderDecodeFrameWithOptions.cold.1
+ _AppleAVDWrapperH264DecoderDecodeFrameWithOptions.cold.2
+ _AppleAVDWrapperH264DecoderDecodeFrameWithOptions.cold.3
+ _AppleAVDWrapperH264DecoderDecodeFrameWithOptions.cold.4
+ _AppleAVDWrapperH264DecoderDecodeFrameWithOptions.cold.5
+ _AppleAVDWrapperH264DecoderDecodeFrameWithOptions.cold.6
+ _AppleAVDWrapperH264DecoderDecodeTile.cold.1
+ _AppleAVDWrapperH264DecoderDecodeTile.cold.2
+ _AppleAVDWrapperH264DecoderDecodeTile.cold.3
+ _AppleAVDWrapperH264DecoderDecodeTile.cold.4
+ _AppleAVDWrapperH264DecoderDecodeTile.cold.5
+ _AppleAVDWrapperH264DecoderDecodeTile.cold.6
+ _AppleAVDWrapperH264DecoderDecodeTile.cold.7
+ _AppleAVDWrapperH264DecoderSetProperty.cold.1
+ _AppleAVDWrapperH264DecoderSetProperty.cold.2
+ _AppleAVDWrapperH264DecoderSetProperty.cold.3
+ _AppleAVDWrapperH264DecoderSetProperty.cold.4
+ _AppleAVDWrapperH264DecoderSetProperty.cold.5
+ _AppleAVDWrapperH264DecoderSetProperty.cold.6
+ _AppleAVDWrapperH264DecoderSetProperty.cold.7
+ _AppleAVDWrapperH264DecoderSetProperty.cold.8
+ _AppleAVDWrapperH264DecoderSetProperty.cold.9
+ _AppleAVDWrapperH264DecoderStartSession.cold.1
+ _AppleAVDWrapperH264DecoderStartSession.cold.2
+ _AppleAVDWrapperH264DecoderStartSession.cold.3
+ _AppleAVDWrapperH264DecoderStartSession.cold.4
+ _AppleAVDWrapperH264DecoderStartSession.cold.5
+ _AppleAVDWrapperH264DecoderStartSession.cold.6
+ _AppleAVDWrapperH264DecoderStartSession.cold.7
+ _AppleAVDWrapperH264DecoderStartTileSession.cold.1
+ _AppleAVDWrapperH264DecoderStartTileSession.cold.2
+ _AppleAVDWrapperH264DecoderStartTileSession.cold.3
+ _AppleAVDWrapperH264DecoderStartTileSession.cold.4
+ _AppleAVDWrapperH264DecoderStartTileSession.cold.5
+ _AppleAVDWrapperH264DecoderStartTileSession.cold.6
+ _AppleAVDWrapperH264DecoderStartTileSession.cold.7
+ _AppleAVDWrapperH264DecoderStartTileSession.cold.8
+ _AppleAVDWrapperH264DecoderStartTileSession.cold.9
+ _AppleAVDWrapperHEVCDecoderCanAcceptFormatDescription.cold.1
+ _AppleAVDWrapperHEVCDecoderCleanUp.cold.1
+ _AppleAVDWrapperHEVCDecoderCleanUp.cold.2
+ _AppleAVDWrapperHEVCDecoderCleanUp.cold.3
+ _AppleAVDWrapperHEVCDecoderCopyProperty.cold.1
+ _AppleAVDWrapperHEVCDecoderCopyProperty.cold.2
+ _AppleAVDWrapperHEVCDecoderCopySupportedPropertyDictionary.cold.1
+ _AppleAVDWrapperHEVCDecoderCreateInstance.cold.1
+ _AppleAVDWrapperHEVCDecoderCreateInstance.cold.2
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.1
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.10
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.11
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.12
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.13
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.14
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.15
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.16
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.17
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.18
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.19
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.2
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.20
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.21
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.22
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.23
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.24
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.3
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.4
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.5
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.6
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.7
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.8
+ _AppleAVDWrapperHEVCDecoderDecodeFrame.cold.9
+ _AppleAVDWrapperHEVCDecoderDecodeFrameWithOptions.cold.1
+ _AppleAVDWrapperHEVCDecoderDecodeFrameWithOptions.cold.2
+ _AppleAVDWrapperHEVCDecoderDecodeFrameWithOptions.cold.3
+ _AppleAVDWrapperHEVCDecoderDecodeFrameWithOptions.cold.4
+ _AppleAVDWrapperHEVCDecoderDecodeFrameWithOptions.cold.5
+ _AppleAVDWrapperHEVCDecoderDecodeFrameWithOptions.cold.6
+ _AppleAVDWrapperHEVCDecoderDecodeFrameWithOptions.cold.7
+ _AppleAVDWrapperHEVCDecoderDecodeFrameWithOptions.cold.8
+ _AppleAVDWrapperHEVCDecoderDecodeTile.cold.1
+ _AppleAVDWrapperHEVCDecoderDecodeTile.cold.2
+ _AppleAVDWrapperHEVCDecoderDecodeTile.cold.3
+ _AppleAVDWrapperHEVCDecoderDecodeTile.cold.4
+ _AppleAVDWrapperHEVCDecoderDecodeTile.cold.5
+ _AppleAVDWrapperHEVCDecoderDecodeTile.cold.6
+ _AppleAVDWrapperHEVCDecoderDecodeTile.cold.7
+ _AppleAVDWrapperHEVCDecoderSetProperty.cold.1
+ _AppleAVDWrapperHEVCDecoderSetProperty.cold.10
+ _AppleAVDWrapperHEVCDecoderSetProperty.cold.11
+ _AppleAVDWrapperHEVCDecoderSetProperty.cold.2
+ _AppleAVDWrapperHEVCDecoderSetProperty.cold.3
+ _AppleAVDWrapperHEVCDecoderSetProperty.cold.4
+ _AppleAVDWrapperHEVCDecoderSetProperty.cold.5
+ _AppleAVDWrapperHEVCDecoderSetProperty.cold.6
+ _AppleAVDWrapperHEVCDecoderSetProperty.cold.7
+ _AppleAVDWrapperHEVCDecoderSetProperty.cold.8
+ _AppleAVDWrapperHEVCDecoderSetProperty.cold.9
+ _AppleAVDWrapperHEVCDecoderStartSession.cold.1
+ _AppleAVDWrapperHEVCDecoderStartSession.cold.2
+ _AppleAVDWrapperHEVCDecoderStartSession.cold.3
+ _AppleAVDWrapperHEVCDecoderStartSession.cold.4
+ _AppleAVDWrapperHEVCDecoderStartSession.cold.5
+ _AppleAVDWrapperHEVCDecoderStartSession.cold.6
+ _AppleAVDWrapperHEVCDecoderStartSession.cold.7
+ _AppleAVDWrapperHEVCDecoderStartSession.cold.8
+ _AppleAVDWrapperHEVCDecoderStartSession.cold.9
+ _AppleAVDWrapperHEVCDecoderStartTileSession.cold.1
+ _AppleAVDWrapperHEVCDecoderStartTileSession.cold.2
+ _AppleAVDWrapperHEVCDecoderStartTileSession.cold.3
+ _AppleAVDWrapperHEVCDecoderStartTileSession.cold.4
+ _AppleAVDWrapperHEVCDecoderStartTileSession.cold.5
+ _AppleAVDWrapperHEVCDecoderStartTileSession.cold.6
+ _AppleAVDWrapperHEVCDecoderStartTileSession.cold.7
+ _AppleAVDWrapperHEVCDecoderStartTileSession.cold.8
+ _AppleAVDWrapperHEVCDecoderStartTileSession.cold.9
+ _AppleAVDWrapperLghrnDecoderCleanUp.cold.1
+ _AppleAVDWrapperLghrnDecoderCleanUp.cold.2
+ _AppleAVDWrapperLghrnDecoderCopyProperty.cold.1
+ _AppleAVDWrapperLghrnDecoderCreateInstance.cold.1
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.1
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.10
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.11
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.12
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.13
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.14
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.15
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.16
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.17
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.18
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.19
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.2
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.20
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.21
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.22
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.23
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.24
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.25
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.26
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.3
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.4
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.5
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.6
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.7
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.8
+ _AppleAVDWrapperLghrnDecoderDecodeFrame.cold.9
+ _AppleAVDWrapperLghrnDecoderSetProperty.cold.1
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.1
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.10
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.11
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.12
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.13
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.14
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.15
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.16
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.17
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.18
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.2
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.3
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.4
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.5
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.6
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.7
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.8
+ _AppleAVDWrapperLghrnDecoderStartSession.cold.9
+ _CompareVpsParamsInFormatDescriptors
+ _CreateAVDFghrnInstance.cold.1
+ _CreateAVDFghrnInstance.cold.10
+ _CreateAVDFghrnInstance.cold.11
+ _CreateAVDFghrnInstance.cold.12
+ _CreateAVDFghrnInstance.cold.13
+ _CreateAVDFghrnInstance.cold.14
+ _CreateAVDFghrnInstance.cold.15
+ _CreateAVDFghrnInstance.cold.16
+ _CreateAVDFghrnInstance.cold.17
+ _CreateAVDFghrnInstance.cold.18
+ _CreateAVDFghrnInstance.cold.2
+ _CreateAVDFghrnInstance.cold.3
+ _CreateAVDFghrnInstance.cold.4
+ _CreateAVDFghrnInstance.cold.5
+ _CreateAVDFghrnInstance.cold.6
+ _CreateAVDFghrnInstance.cold.7
+ _CreateAVDFghrnInstance.cold.8
+ _CreateAVDFghrnInstance.cold.9
+ _CreateAVDFrameReceiver.cold.1
+ _CreateAVDFrameReceiver.cold.2
+ _CreateAVDFrameReceiver.cold.3
+ _CreateAVDH264Instance.cold.1
+ _CreateAVDH264Instance.cold.10
+ _CreateAVDH264Instance.cold.11
+ _CreateAVDH264Instance.cold.12
+ _CreateAVDH264Instance.cold.13
+ _CreateAVDH264Instance.cold.2
+ _CreateAVDH264Instance.cold.3
+ _CreateAVDH264Instance.cold.4
+ _CreateAVDH264Instance.cold.5
+ _CreateAVDH264Instance.cold.6
+ _CreateAVDH264Instance.cold.7
+ _CreateAVDH264Instance.cold.8
+ _CreateAVDH264Instance.cold.9
+ _CreateAVDHEVCInstance.cold.1
+ _CreateAVDHEVCInstance.cold.10
+ _CreateAVDHEVCInstance.cold.11
+ _CreateAVDHEVCInstance.cold.12
+ _CreateAVDHEVCInstance.cold.13
+ _CreateAVDHEVCInstance.cold.14
+ _CreateAVDHEVCInstance.cold.15
+ _CreateAVDHEVCInstance.cold.16
+ _CreateAVDHEVCInstance.cold.17
+ _CreateAVDHEVCInstance.cold.18
+ _CreateAVDHEVCInstance.cold.19
+ _CreateAVDHEVCInstance.cold.2
+ _CreateAVDHEVCInstance.cold.20
+ _CreateAVDHEVCInstance.cold.21
+ _CreateAVDHEVCInstance.cold.22
+ _CreateAVDHEVCInstance.cold.23
+ _CreateAVDHEVCInstance.cold.24
+ _CreateAVDHEVCInstance.cold.25
+ _CreateAVDHEVCInstance.cold.26
+ _CreateAVDHEVCInstance.cold.27
+ _CreateAVDHEVCInstance.cold.28
+ _CreateAVDHEVCInstance.cold.3
+ _CreateAVDHEVCInstance.cold.4
+ _CreateAVDHEVCInstance.cold.5
+ _CreateAVDHEVCInstance.cold.6
+ _CreateAVDHEVCInstance.cold.7
+ _CreateAVDHEVCInstance.cold.8
+ _CreateAVDHEVCInstance.cold.9
+ _CreateCompressedPixelBufferAttributesDictionary.cold.1
+ _CreateDispPixelBufferAttributesDictionary.cold.1
+ _CreateHeaderBuffer.cold.1
+ _CreateHeaderBuffer.cold.2
+ _CreateHeaderBuffer.cold.3
+ _CreateHeaderBuffer.cold.4
+ _CreateHeaderBuffer.cold.5
+ _CreateHeaderBuffer.cold.6
+ _CreateHeaderBuffer.cold.7
+ _CreatePixelBufferAttributesDictionary.cold.1
+ _CreateUncompressedPixelBufferAttributesDictionary.cold.1
+ _Fghrn_createFrameTypesArrayElement.cold.1
+ _Fghrn_createSupportedPropertyDictionary.cold.1
+ _Fghrn_createSupportedPropertyDictionary.cold.2
+ _Fghrn_createSupportedPropertyDictionary.cold.3
+ _GetIOSurfaceTypeFromSessionPixelBufferAttributes.cold.1
+ _GetIOSurfaceTypeFromSessionPixelBufferAttributes.cold.2
+ _GetIOSurfaceTypeFromSessionPixelBufferAttributes.cold.3
+ _GetIOSurfaceTypeFromSessionPixelBufferAttributes.cold.4
+ _InitDisplayPixelBufferCompressionNotSupported.cold.1
+ _InitDisplayPixelBufferCompressionNotSupported.cold.2
+ _InitDisplayPixelBufferCompressionNotSupported.cold.3
+ _InitPixelBufferCompressionSupported.cold.1
+ _InitPixelBufferCompressionSupported.cold.2
+ _InitPixelBufferCompressionSupported.cold.3
+ _InitPixelBufferCompressionSupported.cold.4
+ _InitReferencePixelBufferCompressionNotSupported.cold.1
+ _InitReferencePixelBufferCompressionNotSupported.cold.2
+ _InitReferencePixelBufferCompressionNotSupported.cold.3
+ _InitReferencePixelBufferCompressionNotSupported.cold.4
+ _Lghrn_createFrameTypesArrayElement.cold.1
+ _Lghrn_createSupportedPropertyDictionary.cold.1
+ _Lghrn_createSupportedPropertyDictionary.cold.2
+ _Lghrn_createSupportedPropertyDictionary.cold.3
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _StopAVDFrameReceiver.cold.1
+ _VideoDecoder_getCFPreferenceNumber.cold.1
+ _VideoDecoder_getCFPreferenceNumber.cold.2
+ _WriteNAL.cold.1
+ _WriteNAL.cold.2
+ __Z23AppleAVDDisplayCallbackP22_sAppleAVDVideoContextjjj10RvraParams16DecProfileParamsjijjj.cold.1
+ __Z23AppleAVDDisplayCallbackP22_sAppleAVDVideoContextjjj10RvraParams16DecProfileParamsjijjj.cold.10
+ __Z23AppleAVDDisplayCallbackP22_sAppleAVDVideoContextjjj10RvraParams16DecProfileParamsjijjj.cold.11
+ __Z23AppleAVDDisplayCallbackP22_sAppleAVDVideoContextjjj10RvraParams16DecProfileParamsjijjj.cold.12
+ __Z23AppleAVDDisplayCallbackP22_sAppleAVDVideoContextjjj10RvraParams16DecProfileParamsjijjj.cold.13
+ __Z23AppleAVDDisplayCallbackP22_sAppleAVDVideoContextjjj10RvraParams16DecProfileParamsjijjj.cold.2
+ __Z23AppleAVDDisplayCallbackP22_sAppleAVDVideoContextjjj10RvraParams16DecProfileParamsjijjj.cold.3
+ __Z23AppleAVDDisplayCallbackP22_sAppleAVDVideoContextjjj10RvraParams16DecProfileParamsjijjj.cold.4
+ __Z23AppleAVDDisplayCallbackP22_sAppleAVDVideoContextjjj10RvraParams16DecProfileParamsjijjj.cold.5
+ __Z23AppleAVDDisplayCallbackP22_sAppleAVDVideoContextjjj10RvraParams16DecProfileParamsjijjj.cold.6
+ __Z23AppleAVDDisplayCallbackP22_sAppleAVDVideoContextjjj10RvraParams16DecProfileParamsjijjj.cold.7
+ __Z23AppleAVDDisplayCallbackP22_sAppleAVDVideoContextjjj10RvraParams16DecProfileParamsjijjj.cold.8
+ __Z23AppleAVDDisplayCallbackP22_sAppleAVDVideoContextjjj10RvraParams16DecProfileParamsjijjj.cold.9
+ __Z25createDandelionAvcDecoderPv
+ __Z25createDandelionAvxDecoderPv
+ __Z25createDandelionLghDecoderPv
+ __Z26createDandelionHevcDecoderPv
+ __Z27AppleAVDDecodeFrameResponsePvijiii.cold.1
+ __Z27AppleAVDDecodeFrameResponsePvijiii.cold.2
+ __Z27AppleAVDDecodeFrameResponsePvijiii.cold.3
+ __Z28GetSupportBitsFromIORegistryv.cold.1
+ __Z28GetSupportBitsFromIORegistryv.cold.2
+ __Z28GetSupportBitsFromIORegistryv.cold.3
+ __Z28GetSupportBitsFromIORegistryv.cold.4
+ __Z28GetSupportBitsFromIORegistryv.cold.5
+ __Z28GetSupportBitsFromIORegistryv.cold.6
+ __Z30BilinearScaleInterchangeBufferP11__IOSurfaceS0_iiiiiij25scaler_bilinear_buffers_tS0_S0_.cold.1
+ __Z30BilinearScaleInterchangeBufferP11__IOSurfaceS0_iiiiiij25scaler_bilinear_buffers_tS0_S0_.cold.2
+ __ZN10AV1_Syntax12Parse_HeaderEPKhmP10av1_headerb.cold.1
+ __ZN10AV1_Syntax12Parse_HeaderEPKhmP10av1_headerb.cold.10
+ __ZN10AV1_Syntax12Parse_HeaderEPKhmP10av1_headerb.cold.11
+ __ZN10AV1_Syntax12Parse_HeaderEPKhmP10av1_headerb.cold.12
+ __ZN10AV1_Syntax12Parse_HeaderEPKhmP10av1_headerb.cold.2
+ __ZN10AV1_Syntax12Parse_HeaderEPKhmP10av1_headerb.cold.3
+ __ZN10AV1_Syntax12Parse_HeaderEPKhmP10av1_headerb.cold.4
+ __ZN10AV1_Syntax12Parse_HeaderEPKhmP10av1_headerb.cold.5
+ __ZN10AV1_Syntax12Parse_HeaderEPKhmP10av1_headerb.cold.6
+ __ZN10AV1_Syntax12Parse_HeaderEPKhmP10av1_headerb.cold.7
+ __ZN10AV1_Syntax12Parse_HeaderEPKhmP10av1_headerb.cold.8
+ __ZN10AV1_Syntax12Parse_HeaderEPKhmP10av1_headerb.cold.9
+ __ZN10AV1_Syntax16frame_header_obuEv.cold.1
+ __ZN10AV1_Syntax28Get_Frame_Size_Override_FlagEv.cold.1
+ __ZN10BufferPool11unmapBufferEjjb.cold.1
+ __ZN10BufferPool13getBufferInfoEjPP8Buf_Info.cold.1
+ __ZN10BufferPool13getBufferInfoEjPP8Buf_Info.cold.2
+ __ZN10BufferPool13releaseBufferEjjb.cold.1
+ __ZN10BufferPool14initBufferPoolEPvP19__CVPixelBufferPooliii
+ __ZN10BufferPool14initBufferPoolEPvP19__CVPixelBufferPooliii.cold.1
+ __ZN10BufferPool14initBufferPoolEPvP19__CVPixelBufferPooliii.cold.2
+ __ZN10BufferPool14initBufferPoolEPvP19__CVPixelBufferPooliii.cold.3
+ __ZN10BufferPool14initBufferPoolEPvP19__CVPixelBufferPooliii.cold.4
+ __ZN10BufferPool18shallowCloneBufferEjPj.cold.1
+ __ZN10BufferPool9getBufferEPjjP10__CVBufferP27OpaqueVTVideoDecoderSessionP25OpaqueVTVideoDecoderFrame.cold.1
+ __ZN10BufferPool9getBufferEPjjP10__CVBufferP27OpaqueVTVideoDecoderSessionP25OpaqueVTVideoDecoderFrame.cold.2
+ __ZN10BufferPool9getBufferEPjjP10__CVBufferP27OpaqueVTVideoDecoderSessionP25OpaqueVTVideoDecoderFrame.cold.3
+ __ZN10BufferPool9getBufferEPjjP10__CVBufferP27OpaqueVTVideoDecoderSessionP25OpaqueVTVideoDecoderFrame.cold.4
+ __ZN10BufferPool9getBufferEPjjP10__CVBufferP27OpaqueVTVideoDecoderSessionP25OpaqueVTVideoDecoderFrame.cold.5
+ __ZN10BufferPool9getBufferEPjjP10__CVBufferP27OpaqueVTVideoDecoderSessionP25OpaqueVTVideoDecoderFrame.cold.6
+ __ZN10BufferPool9getBufferEPjjP10__CVBufferP27OpaqueVTVideoDecoderSessionP25OpaqueVTVideoDecoderFrame.cold.7
+ __ZN10CPBManager11allocOneCPBEjmRjPhPbPS1_.cold.1
+ __ZN10CPBManager11allocOneCPBEjmRjPhPbPS1_.cold.2
+ __ZN10CPBManager11allocOneCPBEjmRjPhPbPS1_.cold.3
+ __ZN10CPBManager13releaseOneCPBEjb.cold.1
+ __ZN10CPBManager22waitForCPBsOutstandingEj.cold.1
+ __ZN10CPBManager22waitForCPBsOutstandingEj.cold.2
+ __ZN10CPBManager9initCacheEv.cold.1
+ __ZN10CPBManager9initCacheEv.cold.2
+ __ZN10CPBManager9initCacheEv.cold.3
+ __ZN10CPBManager9initCacheEv.cold.4
+ __ZN11CAVDDecoder11allocAVDMemEP20_avd_client_mem_infom11eAvdMapType11eAvdMemTypeh.cold.1
+ __ZN11CAVDDecoder12mapAVDMemoryEPvjm11eAvdMemType11eAvdMapTypeP20_avd_client_mem_infobbbyybh.cold.1
+ __ZN11CAVDDecoder13deallocAVDMemEP20_avd_client_mem_info.cold.1
+ __ZN11CAVDDecoder16VAMapPixelBufferEijjbyyb.cold.1
+ __ZN11CAVDDecoder17getSurfaceMemInfoEj.cold.1
+ __ZN11CAVDDecoder18VAUnmapPixelBufferEij.cold.1
+ __ZN11CAVDDecoder19calculateClearBytesEjjjjPjS0_.cold.1
+ __ZN11CAVDDecoder19calculateClearBytesEjjjjPjS0_.cold.2
+ __ZN11CAVDDecoder22iterateSurfaceRefCountEj.cold.1
+ __ZN11CAVDDecoder24calcLumaChromaTileOffsetEjjjjjPjS0_.cold.1
+ __ZN11CAVDDecoder24decrementSurfaceRefCountEj.cold.1
+ __ZN11CAVDDecoder24decrementSurfaceRefCountEj.cold.2
+ __ZN11CAVDDecoder24getDisplaySurfaceMemInfoEj.cold.1
+ __ZN13pthread_utils30pthreadCondTimedWaitRelativeNPEP22_opaque_pthread_cond_tP23_opaque_pthread_mutex_ty
+ __ZN14CAHDecClaryAvc11initPictureEjjb.cold.1
+ __ZN14CAHDecClaryAvc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecClaryAvc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecClaryAvc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecClaryAvc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecClaryAvc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecClaryAvc16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecClaryAvc16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecClaryAvc16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecClaryAvc24populatePictureRegistersEv.cold.1
+ __ZN14CAHDecClaryAvc24populatePictureRegistersEv.cold.2
+ __ZN14CAHDecClaryAvc24populatePictureRegistersEv.cold.3
+ __ZN14CAHDecClaryAvc24populatePictureRegistersEv.cold.4
+ __ZN14CAHDecClaryAvc24populatePictureRegistersEv.cold.5
+ __ZN14CAHDecClaryAvc24populatePictureRegistersEv.cold.6
+ __ZN14CAHDecClaryAvc4initEv.cold.1
+ __ZN14CAHDecClaryLgh12startPictureEj.cold.1
+ __ZN14CAHDecClaryLgh16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecClaryLgh16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecClaryLgh16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecClaryLgh16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecClaryLgh16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecClaryLgh16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN14CAHDecClaryLgh16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN14CAHDecClaryLgh16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecClaryLgh16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecClaryLgh16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecClaryLgh16allocWorkBuf_SPSEPv.cold.4
+ __ZN14CAHDecClaryLgh4initEv.cold.1
+ __ZN14CAHDecClaryLgh4initEv.cold.2
+ __ZN14CAHDecClaryLgh4initEv.cold.3
+ __ZN14CAHDecDaisyAvc11initPictureEjjb.cold.1
+ __ZN14CAHDecDaisyAvc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecDaisyAvc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecDaisyAvc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecDaisyAvc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecDaisyAvc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecDaisyAvc16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecDaisyAvc16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecDaisyAvc16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecDaisyAvc24populatePictureRegistersEv.cold.1
+ __ZN14CAHDecDaisyAvc24populatePictureRegistersEv.cold.2
+ __ZN14CAHDecDaisyAvc24populatePictureRegistersEv.cold.3
+ __ZN14CAHDecDaisyAvc24populatePictureRegistersEv.cold.4
+ __ZN14CAHDecDaisyAvc24populatePictureRegistersEv.cold.5
+ __ZN14CAHDecDaisyAvc24populatePictureRegistersEv.cold.6
+ __ZN14CAHDecDaisyAvc4initEv.cold.1
+ __ZN14CAHDecDaisyAvx12startPictureEj.cold.1
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.10
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.11
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.12
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.13
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_SPSEPv.cold.4
+ __ZN14CAHDecDaisyAvx24populateAddressRegistersEv.cold.1
+ __ZN14CAHDecDaisyAvx4initEv.cold.1
+ __ZN14CAHDecDaisyAvx4initEv.cold.2
+ __ZN14CAHDecDaisyAvx4initEv.cold.3
+ __ZN14CAHDecDaisyLgh12startPictureEj.cold.1
+ __ZN14CAHDecDaisyLgh16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecDaisyLgh16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecDaisyLgh16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecDaisyLgh16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecDaisyLgh16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecDaisyLgh16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN14CAHDecDaisyLgh16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN14CAHDecDaisyLgh16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecDaisyLgh16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecDaisyLgh16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecDaisyLgh16allocWorkBuf_SPSEPv.cold.4
+ __ZN14CAHDecDaisyLgh4initEv.cold.1
+ __ZN14CAHDecDaisyLgh4initEv.cold.2
+ __ZN14CAHDecDaisyLgh4initEv.cold.3
+ __ZN14CAHDecIxoraAvc11initPictureEjjb.cold.1
+ __ZN14CAHDecIxoraAvc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecIxoraAvc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecIxoraAvc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecIxoraAvc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecIxoraAvc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecIxoraAvc16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecIxoraAvc16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecIxoraAvc16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecIxoraAvc24populatePictureRegistersEv.cold.1
+ __ZN14CAHDecIxoraAvc24populatePictureRegistersEv.cold.2
+ __ZN14CAHDecIxoraAvc24populatePictureRegistersEv.cold.3
+ __ZN14CAHDecIxoraAvc24populatePictureRegistersEv.cold.4
+ __ZN14CAHDecIxoraAvc24populatePictureRegistersEv.cold.5
+ __ZN14CAHDecIxoraAvc24populatePictureRegistersEv.cold.6
+ __ZN14CAHDecIxoraAvc4initEv.cold.1
+ __ZN14CAHDecIxoraAvx12startPictureEj.cold.1
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_PPSEPvS0_S0_.cold.10
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_PPSEPvS0_S0_.cold.11
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_PPSEPvS0_S0_.cold.12
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_PPSEPvS0_S0_.cold.13
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecIxoraAvx16allocWorkBuf_SPSEPv.cold.4
+ __ZN14CAHDecIxoraAvx24populateAddressRegistersEv.cold.1
+ __ZN14CAHDecIxoraAvx4initEv.cold.1
+ __ZN14CAHDecIxoraAvx4initEv.cold.2
+ __ZN14CAHDecIxoraAvx4initEv.cold.3
+ __ZN14CAHDecIxoraLgh12startPictureEj.cold.1
+ __ZN14CAHDecIxoraLgh16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecIxoraLgh16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecIxoraLgh16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecIxoraLgh16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecIxoraLgh16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecIxoraLgh16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN14CAHDecIxoraLgh16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN14CAHDecIxoraLgh16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecIxoraLgh16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecIxoraLgh16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecIxoraLgh16allocWorkBuf_SPSEPv.cold.4
+ __ZN14CAHDecIxoraLgh4initEv.cold.1
+ __ZN14CAHDecIxoraLgh4initEv.cold.2
+ __ZN14CAHDecIxoraLgh4initEv.cold.3
+ __ZN14CAHDecLotusAvc11initPictureEjjb.cold.1
+ __ZN14CAHDecLotusAvc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecLotusAvc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecLotusAvc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecLotusAvc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecLotusAvc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecLotusAvc16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecLotusAvc16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecLotusAvc16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecLotusAvc24populatePictureRegistersEv.cold.1
+ __ZN14CAHDecLotusAvc24populatePictureRegistersEv.cold.2
+ __ZN14CAHDecLotusAvc24populatePictureRegistersEv.cold.3
+ __ZN14CAHDecLotusAvc24populatePictureRegistersEv.cold.4
+ __ZN14CAHDecLotusAvc24populatePictureRegistersEv.cold.5
+ __ZN14CAHDecLotusAvc24populatePictureRegistersEv.cold.6
+ __ZN14CAHDecLotusAvc4initEv.cold.1
+ __ZN14CAHDecLotusLgh12startPictureEj.cold.1
+ __ZN14CAHDecLotusLgh16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecLotusLgh16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecLotusLgh16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecLotusLgh16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecLotusLgh16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecLotusLgh16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN14CAHDecLotusLgh16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN14CAHDecLotusLgh16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecLotusLgh16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecLotusLgh16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecLotusLgh16allocWorkBuf_SPSEPv.cold.4
+ __ZN14CAHDecLotusLgh4initEv.cold.1
+ __ZN14CAHDecLotusLgh4initEv.cold.2
+ __ZN14CAHDecLotusLgh4initEv.cold.3
+ __ZN14CAHDecRoseHevc11initPictureEjjb.cold.1
+ __ZN14CAHDecRoseHevc15populateAvdWorkEj.cold.1
+ __ZN14CAHDecRoseHevc15populateAvdWorkEj.cold.2
+ __ZN14CAHDecRoseHevc15populateAvdWorkEj.cold.3
+ __ZN14CAHDecRoseHevc15populateAvdWorkEj.cold.4
+ __ZN14CAHDecRoseHevc15populateAvdWorkEj.cold.5
+ __ZN14CAHDecRoseHevc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecRoseHevc16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecRoseHevc16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecRoseHevc16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecRoseHevc16allocWorkBuf_SPSEPv.cold.4
+ __ZN14CAHDecRoseHevc16allocWorkBuf_SPSEPv.cold.5
+ __ZN14CAHDecRoseHevc16allocWorkBuf_SPSEPv.cold.6
+ __ZN14CAHDecRoseHevc16allocWorkBuf_SPSEPv.cold.7
+ __ZN14CAHDecRoseHevc16allocWorkBuf_SPSEPv.cold.8
+ __ZN14CAHDecRoseHevc16allocWorkBuf_SPSEPv.cold.9
+ __ZN14CAHDecRoseHevc22populateSliceRegistersEP14SliceRegistersi.cold.1
+ __ZN14CAHDecRoseHevc22populateSliceRegistersEP14SliceRegistersi.cold.2
+ __ZN14CAHDecRoseHevc22populateSliceRegistersEP14SliceRegistersi.cold.3
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.1
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.10
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.11
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.12
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.13
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.14
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.15
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.16
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.17
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.18
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.19
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.2
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.20
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.21
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.22
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.23
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.24
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.25
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.26
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.27
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.28
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.29
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.3
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.30
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.31
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.32
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.33
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.34
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.35
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.36
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.37
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.38
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.4
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.5
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.6
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.7
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.8
+ __ZN14CAHDecRoseHevc24populatePictureRegistersEv.cold.9
+ __ZN14CAHDecRoseHevc4initEv.cold.1
+ __ZN14CAHDecTansyAvc11initPictureEjjb.cold.1
+ __ZN14CAHDecTansyAvc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecTansyAvc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecTansyAvc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecTansyAvc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecTansyAvc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecTansyAvc16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecTansyAvc16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecTansyAvc16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecTansyAvc24populatePictureRegistersEv.cold.1
+ __ZN14CAHDecTansyAvc24populatePictureRegistersEv.cold.2
+ __ZN14CAHDecTansyAvc24populatePictureRegistersEv.cold.3
+ __ZN14CAHDecTansyAvc24populatePictureRegistersEv.cold.4
+ __ZN14CAHDecTansyAvc24populatePictureRegistersEv.cold.5
+ __ZN14CAHDecTansyAvc24populatePictureRegistersEv.cold.6
+ __ZN14CAHDecTansyAvc4initEv.cold.1
+ __ZN14CAHDecTansyAvx12startPictureEj.cold.1
+ __ZN14CAHDecTansyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecTansyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.10
+ __ZN14CAHDecTansyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.11
+ __ZN14CAHDecTansyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.12
+ __ZN14CAHDecTansyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.13
+ __ZN14CAHDecTansyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecTansyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecTansyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecTansyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecTansyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN14CAHDecTansyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN14CAHDecTansyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN14CAHDecTansyAvx16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN14CAHDecTansyAvx16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecTansyAvx16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecTansyAvx16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecTansyAvx16allocWorkBuf_SPSEPv.cold.4
+ __ZN14CAHDecTansyAvx24populateAddressRegistersEv.cold.1
+ __ZN14CAHDecTansyAvx4initEv.cold.1
+ __ZN14CAHDecTansyAvx4initEv.cold.2
+ __ZN14CAHDecTansyAvx4initEv.cold.3
+ __ZN14CAHDecTansyLgh12startPictureEj.cold.1
+ __ZN14CAHDecTansyLgh16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecTansyLgh16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecTansyLgh16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecTansyLgh16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecTansyLgh16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecTansyLgh16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN14CAHDecTansyLgh16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN14CAHDecTansyLgh16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecTansyLgh16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecTansyLgh16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecTansyLgh16allocWorkBuf_SPSEPv.cold.4
+ __ZN14CAHDecTansyLgh4initEv.cold.1
+ __ZN14CAHDecTansyLgh4initEv.cold.2
+ __ZN14CAHDecTansyLgh4initEv.cold.3
+ __ZN14CAHDecThymeAvc11initPictureEjjb.cold.1
+ __ZN14CAHDecThymeAvc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecThymeAvc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecThymeAvc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecThymeAvc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecThymeAvc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecThymeAvc16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecThymeAvc16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecThymeAvc16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecThymeAvc24populatePictureRegistersEv.cold.1
+ __ZN14CAHDecThymeAvc24populatePictureRegistersEv.cold.2
+ __ZN14CAHDecThymeAvc24populatePictureRegistersEv.cold.3
+ __ZN14CAHDecThymeAvc24populatePictureRegistersEv.cold.4
+ __ZN14CAHDecThymeAvc24populatePictureRegistersEv.cold.5
+ __ZN14CAHDecThymeAvc24populatePictureRegistersEv.cold.6
+ __ZN14CAHDecThymeAvc4initEv.cold.1
+ __ZN14CAHDecThymeAvx12startPictureEj.cold.1
+ __ZN14CAHDecThymeAvx16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecThymeAvx16allocWorkBuf_PPSEPvS0_S0_.cold.10
+ __ZN14CAHDecThymeAvx16allocWorkBuf_PPSEPvS0_S0_.cold.11
+ __ZN14CAHDecThymeAvx16allocWorkBuf_PPSEPvS0_S0_.cold.12
+ __ZN14CAHDecThymeAvx16allocWorkBuf_PPSEPvS0_S0_.cold.13
+ __ZN14CAHDecThymeAvx16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecThymeAvx16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecThymeAvx16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecThymeAvx16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecThymeAvx16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN14CAHDecThymeAvx16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN14CAHDecThymeAvx16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN14CAHDecThymeAvx16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN14CAHDecThymeAvx16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecThymeAvx16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecThymeAvx16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecThymeAvx16allocWorkBuf_SPSEPv.cold.4
+ __ZN14CAHDecThymeAvx24populateAddressRegistersEv.cold.1
+ __ZN14CAHDecThymeAvx4initEv.cold.1
+ __ZN14CAHDecThymeAvx4initEv.cold.2
+ __ZN14CAHDecThymeAvx4initEv.cold.3
+ __ZN14CAHDecThymeLgh12startPictureEj.cold.1
+ __ZN14CAHDecThymeLgh16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecThymeLgh16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecThymeLgh16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecThymeLgh16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecThymeLgh16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecThymeLgh16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN14CAHDecThymeLgh16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN14CAHDecThymeLgh16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecThymeLgh16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecThymeLgh16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecThymeLgh16allocWorkBuf_SPSEPv.cold.4
+ __ZN14CAHDecThymeLgh4initEv.cold.1
+ __ZN14CAHDecThymeLgh4initEv.cold.2
+ __ZN14CAHDecThymeLgh4initEv.cold.3
+ __ZN14CAHDecViolaAvc11initPictureEjjb.cold.1
+ __ZN14CAHDecViolaAvc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecViolaAvc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecViolaAvc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecViolaAvc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecViolaAvc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecViolaAvc16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecViolaAvc16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecViolaAvc16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecViolaAvc24populatePictureRegistersEv.cold.1
+ __ZN14CAHDecViolaAvc24populatePictureRegistersEv.cold.2
+ __ZN14CAHDecViolaAvc24populatePictureRegistersEv.cold.3
+ __ZN14CAHDecViolaAvc24populatePictureRegistersEv.cold.4
+ __ZN14CAHDecViolaAvc4initEv.cold.1
+ __ZN14CAHDecViolaLgh12startPictureEj.cold.1
+ __ZN14CAHDecViolaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN14CAHDecViolaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN14CAHDecViolaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN14CAHDecViolaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN14CAHDecViolaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN14CAHDecViolaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN14CAHDecViolaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN14CAHDecViolaLgh16allocWorkBuf_SPSEPv.cold.1
+ __ZN14CAHDecViolaLgh16allocWorkBuf_SPSEPv.cold.2
+ __ZN14CAHDecViolaLgh16allocWorkBuf_SPSEPv.cold.3
+ __ZN14CAHDecViolaLgh16allocWorkBuf_SPSEPv.cold.4
+ __ZN14CAHDecViolaLgh4initEv.cold.1
+ __ZN14CAHDecViolaLgh4initEv.cold.2
+ __ZN14CAHDecViolaLgh4initEv.cold.3
+ __ZN14CAVDAvcDecoder10activatePSEP15sAvcSliceHeader.cold.1
+ __ZN14CAVDAvcDecoder10activatePSEP15sAvcSliceHeader.cold.2
+ __ZN14CAVDAvcDecoder10activatePSEP15sAvcSliceHeader.cold.3
+ __ZN14CAVDAvcDecoder11VAGetParamsEjPj.cold.1
+ __ZN14CAVDAvcDecoder11VAGetParamsEjPj.cold.2
+ __ZN14CAVDAvcDecoder11VAGetParamsEjPj.cold.3
+ __ZN14CAVDAvcDecoder11VASetParamsEjPj.cold.1
+ __ZN14CAVDAvcDecoder11initPictureEP14sAvcNaluHeaderP7sAvcSPSP15sAvcSliceHeaderP15sAvcPictureInfob.cold.1
+ __ZN14CAVDAvcDecoder12VAStopDecodeEv.cold.1
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.1
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.10
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.11
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.12
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.13
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.14
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.15
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.16
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.17
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.18
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.19
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.2
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.20
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.21
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.22
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.23
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.24
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.25
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.26
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.27
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.28
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.29
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.3
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.30
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.31
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.4
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.5
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.6
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.7
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.8
+ __ZN14CAVDAvcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.9
+ __ZN14CAVDAvcDecoder13VAStartDecodeEPhi.cold.1
+ __ZN14CAVDAvcDecoder13VAStartDecodeEPhi.cold.10
+ __ZN14CAVDAvcDecoder13VAStartDecodeEPhi.cold.2
+ __ZN14CAVDAvcDecoder13VAStartDecodeEPhi.cold.3
+ __ZN14CAVDAvcDecoder13VAStartDecodeEPhi.cold.4
+ __ZN14CAVDAvcDecoder13VAStartDecodeEPhi.cold.5
+ __ZN14CAVDAvcDecoder13VAStartDecodeEPhi.cold.6
+ __ZN14CAVDAvcDecoder13VAStartDecodeEPhi.cold.7
+ __ZN14CAVDAvcDecoder13VAStartDecodeEPhi.cold.8
+ __ZN14CAVDAvcDecoder13VAStartDecodeEPhi.cold.9
+ __ZN14CAVDAvcDecoder14getRefBufIndexEjj.cold.1
+ __ZN14CAVDAvcDecoder17allocateHwDecoderEv.cold.1
+ __ZN14CAVDAvcDecoder24decodeGetRenderTargetRefEjjjPP9_vsurface.cold.1
+ __ZN14CAVDAvcDecoder24decodeGetRenderTargetRefEjjjPP9_vsurface.cold.2
+ __ZN14CAVDAvcDecoder6VAInitEv.cold.1
+ __ZN14CAVDAvcDecoder6VAInitEv.cold.2
+ __ZN14CAVDAvcDecoder6VAInitEv.cold.3
+ __ZN14CAVDAvcDecoder6VAInitEv.cold.4
+ __ZN14CAVDAvcDecoder6VAInitEv.cold.5
+ __ZN14CAVDAvcDecoder6VAInitEv.cold.6
+ __ZN14CAVDAvcDecoder6VAInitEv.cold.7
+ __ZN14CAVDAvcDecoder6VAInitEv.cold.8
+ __ZN14CAVDAvcDecoder6VAInitEv.cold.9
+ __ZN14CAVDAvxDecoder11initPictureEj.cold.1
+ __ZN14CAVDAvxDecoder11initPictureEj.cold.2
+ __ZN14CAVDAvxDecoder11initPictureEj.cold.3
+ __ZN14CAVDAvxDecoder11initPictureEj.cold.4
+ __ZN14CAVDAvxDecoder11initPictureEj.cold.5
+ __ZN14CAVDAvxDecoder11initPictureEj.cold.6
+ __ZN14CAVDAvxDecoder11initPictureEj.cold.7
+ __ZN14CAVDAvxDecoder11initPictureEj.cold.8
+ __ZN14CAVDAvxDecoder12VAStopDecodeEv.cold.1
+ __ZN14CAVDAvxDecoder12getSWRStrideEjjjj.cold.1
+ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.1
+ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.10
+ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.11
+ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.12
+ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.13
+ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.14
+ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.2
+ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.3
+ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.4
+ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.5
+ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.6
+ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.7
+ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.8
+ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.9
+ __ZN14CAVDAvxDecoder13VAStartDecodeEPhi.cold.1
+ __ZN14CAVDAvxDecoder13VAStartDecodeEPhi.cold.2
+ __ZN14CAVDAvxDecoder13VAStartDecodeEPhi.cold.3
+ __ZN14CAVDAvxDecoder13getDeltaLfResEv.cold.1
+ __ZN14CAVDAvxDecoder17allocateHwDecoderEv.cold.1
+ __ZN14CAVDAvxDecoder17sendDisplayBufferEj.cold.1
+ __ZN14CAVDAvxDecoder19VADecodeFrameHeaderEPhij.cold.1
+ __ZN14CAVDAvxDecoder19VADecodeFrameHeaderEPhij.cold.2
+ __ZN14CAVDAvxDecoder20checkVideoResolutionEjji.cold.1
+ __ZN14CAVDAvxDecoder20checkVideoResolutionEjji.cold.2
+ __ZN14CAVDAvxDecoder22getRestorationUnitSizeEi.cold.1
+ __ZN14CAVDAvxDecoder6VAInitEv.cold.1
+ __ZN14CAVDAvxDecoder6VAInitEv.cold.10
+ __ZN14CAVDAvxDecoder6VAInitEv.cold.2
+ __ZN14CAVDAvxDecoder6VAInitEv.cold.3
+ __ZN14CAVDAvxDecoder6VAInitEv.cold.4
+ __ZN14CAVDAvxDecoder6VAInitEv.cold.5
+ __ZN14CAVDAvxDecoder6VAInitEv.cold.6
+ __ZN14CAVDAvxDecoder6VAInitEv.cold.7
+ __ZN14CAVDAvxDecoder6VAInitEv.cold.8
+ __ZN14CAVDAvxDecoder6VAInitEv.cold.9
+ __ZN14CAVDLghDecoder12VAStopDecodeEv.cold.1
+ __ZN14CAVDLghDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.1
+ __ZN14CAVDLghDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.10
+ __ZN14CAVDLghDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.11
+ __ZN14CAVDLghDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.2
+ __ZN14CAVDLghDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.3
+ __ZN14CAVDLghDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.4
+ __ZN14CAVDLghDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.5
+ __ZN14CAVDLghDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.6
+ __ZN14CAVDLghDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.7
+ __ZN14CAVDLghDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.8
+ __ZN14CAVDLghDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.9
+ __ZN14CAVDLghDecoder13VAStartDecodeEPhi.cold.1
+ __ZN14CAVDLghDecoder17allocateHwDecoderEv.cold.1
+ __ZN14CAVDLghDecoder6VAInitEv.cold.1
+ __ZN14CAVDLghDecoder6VAInitEv.cold.2
+ __ZN14CAVDLghDecoder6VAInitEv.cold.3
+ __ZN14CAVDLghDecoder6VAInitEv.cold.4
+ __ZN14CAVDLghDecoder6VAInitEv.cold.5
+ __ZN14CAVDLghDecoder6VAInitEv.cold.6
+ __ZN14CAVDLghDecoder6VAInitEv.cold.7
+ __ZN15CAHDecCatnipAvc11initPictureEjjb.cold.1
+ __ZN15CAHDecCatnipAvc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN15CAHDecCatnipAvc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN15CAHDecCatnipAvc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN15CAHDecCatnipAvc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN15CAHDecCatnipAvc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN15CAHDecCatnipAvc16allocWorkBuf_SPSEPv.cold.1
+ __ZN15CAHDecCatnipAvc16allocWorkBuf_SPSEPv.cold.2
+ __ZN15CAHDecCatnipAvc16allocWorkBuf_SPSEPv.cold.3
+ __ZN15CAHDecCatnipAvc24populatePictureRegistersEv.cold.1
+ __ZN15CAHDecCatnipAvc24populatePictureRegistersEv.cold.2
+ __ZN15CAHDecCatnipAvc24populatePictureRegistersEv.cold.3
+ __ZN15CAHDecCatnipAvc24populatePictureRegistersEv.cold.4
+ __ZN15CAHDecCatnipAvc24populatePictureRegistersEv.cold.5
+ __ZN15CAHDecCatnipAvc24populatePictureRegistersEv.cold.6
+ __ZN15CAHDecCatnipAvc4initEv.cold.1
+ __ZN15CAHDecCatnipAvx12startPictureEj.cold.1
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_PPSEPvS0_S0_.cold.10
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_PPSEPvS0_S0_.cold.11
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_PPSEPvS0_S0_.cold.12
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_PPSEPvS0_S0_.cold.13
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_SPSEPv.cold.1
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_SPSEPv.cold.2
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_SPSEPv.cold.3
+ __ZN15CAHDecCatnipAvx16allocWorkBuf_SPSEPv.cold.4
+ __ZN15CAHDecCatnipAvx24populateAddressRegistersEv.cold.1
+ __ZN15CAHDecCatnipAvx4initEv.cold.1
+ __ZN15CAHDecCatnipAvx4initEv.cold.2
+ __ZN15CAHDecCatnipAvx4initEv.cold.3
+ __ZN15CAHDecCatnipLgh12startPictureEj.cold.1
+ __ZN15CAHDecCatnipLgh16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN15CAHDecCatnipLgh16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN15CAHDecCatnipLgh16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN15CAHDecCatnipLgh16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN15CAHDecCatnipLgh16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN15CAHDecCatnipLgh16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN15CAHDecCatnipLgh16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN15CAHDecCatnipLgh16allocWorkBuf_SPSEPv.cold.1
+ __ZN15CAHDecCatnipLgh16allocWorkBuf_SPSEPv.cold.2
+ __ZN15CAHDecCatnipLgh16allocWorkBuf_SPSEPv.cold.3
+ __ZN15CAHDecCatnipLgh16allocWorkBuf_SPSEPv.cold.4
+ __ZN15CAHDecCatnipLgh4initEv.cold.1
+ __ZN15CAHDecCatnipLgh4initEv.cold.2
+ __ZN15CAHDecCatnipLgh4initEv.cold.3
+ __ZN15CAHDecClaryHevc11initPictureEjjb.cold.1
+ __ZN15CAHDecClaryHevc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN15CAHDecClaryHevc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN15CAHDecClaryHevc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN15CAHDecClaryHevc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN15CAHDecClaryHevc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN15CAHDecClaryHevc16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN15CAHDecClaryHevc16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN15CAHDecClaryHevc16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN15CAHDecClaryHevc16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN15CAHDecClaryHevc16allocWorkBuf_SPSEPv.cold.1
+ __ZN15CAHDecClaryHevc16allocWorkBuf_SPSEPv.cold.2
+ __ZN15CAHDecClaryHevc16allocWorkBuf_SPSEPv.cold.3
+ __ZN15CAHDecClaryHevc24populatePictureRegistersEv.cold.1
+ __ZN15CAHDecClaryHevc24populatePictureRegistersEv.cold.2
+ __ZN15CAHDecClaryHevc24populatePictureRegistersEv.cold.3
+ __ZN15CAHDecClaryHevc24populatePictureRegistersEv.cold.4
+ __ZN15CAHDecClaryHevc4initEv.cold.1
+ __ZN15CAHDecCloverAvc11initPictureEjjb.cold.1
+ __ZN15CAHDecCloverAvc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN15CAHDecCloverAvc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN15CAHDecCloverAvc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN15CAHDecCloverAvc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN15CAHDecCloverAvc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN15CAHDecCloverAvc16allocWorkBuf_SPSEPv.cold.1
+ __ZN15CAHDecCloverAvc16allocWorkBuf_SPSEPv.cold.2
+ __ZN15CAHDecCloverAvc16allocWorkBuf_SPSEPv.cold.3
+ __ZN15CAHDecCloverAvc24populatePictureRegistersEv.cold.1
+ __ZN15CAHDecCloverAvc24populatePictureRegistersEv.cold.2
+ __ZN15CAHDecCloverAvc24populatePictureRegistersEv.cold.3
+ __ZN15CAHDecCloverAvc24populatePictureRegistersEv.cold.4
+ __ZN15CAHDecCloverAvc4initEv.cold.1
+ __ZN15CAHDecCloverLgh12startPictureEj.cold.1
+ __ZN15CAHDecCloverLgh16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN15CAHDecCloverLgh16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN15CAHDecCloverLgh16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN15CAHDecCloverLgh16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN15CAHDecCloverLgh16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN15CAHDecCloverLgh16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN15CAHDecCloverLgh16allocWorkBuf_SPSEPv.cold.1
+ __ZN15CAHDecCloverLgh16allocWorkBuf_SPSEPv.cold.2
+ __ZN15CAHDecCloverLgh16allocWorkBuf_SPSEPv.cold.3
+ __ZN15CAHDecCloverLgh16allocWorkBuf_SPSEPv.cold.4
+ __ZN15CAHDecCloverLgh4initEv.cold.1
+ __ZN15CAHDecCloverLgh4initEv.cold.2
+ __ZN15CAHDecCloverLgh4initEv.cold.3
+ __ZN15CAHDecDahliaAvc11initPictureEjjb.cold.1
+ __ZN15CAHDecDahliaAvc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN15CAHDecDahliaAvc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN15CAHDecDahliaAvc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN15CAHDecDahliaAvc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN15CAHDecDahliaAvc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN15CAHDecDahliaAvc16allocWorkBuf_SPSEPv.cold.1
+ __ZN15CAHDecDahliaAvc16allocWorkBuf_SPSEPv.cold.2
+ __ZN15CAHDecDahliaAvc16allocWorkBuf_SPSEPv.cold.3
+ __ZN15CAHDecDahliaAvc24populatePictureRegistersEv.cold.1
+ __ZN15CAHDecDahliaAvc24populatePictureRegistersEv.cold.2
+ __ZN15CAHDecDahliaAvc24populatePictureRegistersEv.cold.3
+ __ZN15CAHDecDahliaAvc24populatePictureRegistersEv.cold.4
+ __ZN15CAHDecDahliaAvc24populatePictureRegistersEv.cold.5
+ __ZN15CAHDecDahliaAvc24populatePictureRegistersEv.cold.6
+ __ZN15CAHDecDahliaAvc4initEv.cold.1
+ __ZN15CAHDecDahliaLgh12startPictureEj.cold.1
+ __ZN15CAHDecDahliaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN15CAHDecDahliaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN15CAHDecDahliaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN15CAHDecDahliaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN15CAHDecDahliaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN15CAHDecDahliaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN15CAHDecDahliaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN15CAHDecDahliaLgh16allocWorkBuf_SPSEPv.cold.1
+ __ZN15CAHDecDahliaLgh16allocWorkBuf_SPSEPv.cold.2
+ __ZN15CAHDecDahliaLgh16allocWorkBuf_SPSEPv.cold.3
+ __ZN15CAHDecDahliaLgh16allocWorkBuf_SPSEPv.cold.4
+ __ZN15CAHDecDahliaLgh4initEv.cold.1
+ __ZN15CAHDecDahliaLgh4initEv.cold.2
+ __ZN15CAHDecDahliaLgh4initEv.cold.3
+ __ZN15CAHDecDaisyHevc11initPictureEjjb.cold.1
+ __ZN15CAHDecDaisyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN15CAHDecDaisyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.10
+ __ZN15CAHDecDaisyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN15CAHDecDaisyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN15CAHDecDaisyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN15CAHDecDaisyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN15CAHDecDaisyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN15CAHDecDaisyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN15CAHDecDaisyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN15CAHDecDaisyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN15CAHDecDaisyHevc16allocWorkBuf_SPSEPv.cold.1
+ __ZN15CAHDecDaisyHevc16allocWorkBuf_SPSEPv.cold.2
+ __ZN15CAHDecDaisyHevc16allocWorkBuf_SPSEPv.cold.3
+ __ZN15CAHDecDaisyHevc24populatePictureRegistersEv.cold.1
+ __ZN15CAHDecDaisyHevc24populatePictureRegistersEv.cold.2
+ __ZN15CAHDecDaisyHevc24populatePictureRegistersEv.cold.3
+ __ZN15CAHDecDaisyHevc24populatePictureRegistersEv.cold.4
+ __ZN15CAHDecDaisyHevc4initEv.cold.1
+ __ZN15CAHDecIxoraHevc11initPictureEjjb.cold.1
+ __ZN15CAHDecIxoraHevc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN15CAHDecIxoraHevc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN15CAHDecIxoraHevc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN15CAHDecIxoraHevc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN15CAHDecIxoraHevc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN15CAHDecIxoraHevc16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN15CAHDecIxoraHevc16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN15CAHDecIxoraHevc16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN15CAHDecIxoraHevc16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN15CAHDecIxoraHevc16allocWorkBuf_SPSEPv.cold.1
+ __ZN15CAHDecIxoraHevc16allocWorkBuf_SPSEPv.cold.2
+ __ZN15CAHDecIxoraHevc16allocWorkBuf_SPSEPv.cold.3
+ __ZN15CAHDecIxoraHevc24populatePictureRegistersEv.cold.1
+ __ZN15CAHDecIxoraHevc24populatePictureRegistersEv.cold.2
+ __ZN15CAHDecIxoraHevc24populatePictureRegistersEv.cold.3
+ __ZN15CAHDecIxoraHevc24populatePictureRegistersEv.cold.4
+ __ZN15CAHDecIxoraHevc4initEv.cold.1
+ __ZN15CAHDecLotusHevc11initPictureEjjb.cold.1
+ __ZN15CAHDecLotusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN15CAHDecLotusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN15CAHDecLotusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN15CAHDecLotusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN15CAHDecLotusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN15CAHDecLotusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN15CAHDecLotusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN15CAHDecLotusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN15CAHDecLotusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN15CAHDecLotusHevc16allocWorkBuf_SPSEPv.cold.1
+ __ZN15CAHDecLotusHevc16allocWorkBuf_SPSEPv.cold.2
+ __ZN15CAHDecLotusHevc16allocWorkBuf_SPSEPv.cold.3
+ __ZN15CAHDecLotusHevc24populatePictureRegistersEv.cold.1
+ __ZN15CAHDecLotusHevc24populatePictureRegistersEv.cold.2
+ __ZN15CAHDecLotusHevc24populatePictureRegistersEv.cold.3
+ __ZN15CAHDecLotusHevc24populatePictureRegistersEv.cold.4
+ __ZN15CAHDecLotusHevc4initEv.cold.1
+ __ZN15CAHDecSalviaAvc11initPictureEjjb.cold.1
+ __ZN15CAHDecSalviaAvc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN15CAHDecSalviaAvc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN15CAHDecSalviaAvc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN15CAHDecSalviaAvc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN15CAHDecSalviaAvc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN15CAHDecSalviaAvc16allocWorkBuf_SPSEPv.cold.1
+ __ZN15CAHDecSalviaAvc16allocWorkBuf_SPSEPv.cold.2
+ __ZN15CAHDecSalviaAvc16allocWorkBuf_SPSEPv.cold.3
+ __ZN15CAHDecSalviaAvc24populatePictureRegistersEv.cold.1
+ __ZN15CAHDecSalviaAvc24populatePictureRegistersEv.cold.2
+ __ZN15CAHDecSalviaAvc24populatePictureRegistersEv.cold.3
+ __ZN15CAHDecSalviaAvc24populatePictureRegistersEv.cold.4
+ __ZN15CAHDecSalviaAvc4initEv.cold.1
+ __ZN15CAHDecSalviaLgh12startPictureEj.cold.1
+ __ZN15CAHDecSalviaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN15CAHDecSalviaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN15CAHDecSalviaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN15CAHDecSalviaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN15CAHDecSalviaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN15CAHDecSalviaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN15CAHDecSalviaLgh16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN15CAHDecSalviaLgh16allocWorkBuf_SPSEPv.cold.1
+ __ZN15CAHDecSalviaLgh16allocWorkBuf_SPSEPv.cold.2
+ __ZN15CAHDecSalviaLgh16allocWorkBuf_SPSEPv.cold.3
+ __ZN15CAHDecSalviaLgh16allocWorkBuf_SPSEPv.cold.4
+ __ZN15CAHDecSalviaLgh4initEv.cold.1
+ __ZN15CAHDecSalviaLgh4initEv.cold.2
+ __ZN15CAHDecSalviaLgh4initEv.cold.3
+ __ZN15CAHDecTansyHevc11initPictureEjjb.cold.1
+ __ZN15CAHDecTansyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN15CAHDecTansyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.10
+ __ZN15CAHDecTansyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN15CAHDecTansyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN15CAHDecTansyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN15CAHDecTansyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN15CAHDecTansyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN15CAHDecTansyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN15CAHDecTansyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN15CAHDecTansyHevc16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN15CAHDecTansyHevc16allocWorkBuf_SPSEPv.cold.1
+ __ZN15CAHDecTansyHevc16allocWorkBuf_SPSEPv.cold.2
+ __ZN15CAHDecTansyHevc16allocWorkBuf_SPSEPv.cold.3
+ __ZN15CAHDecTansyHevc24populatePictureRegistersEv.cold.1
+ __ZN15CAHDecTansyHevc24populatePictureRegistersEv.cold.2
+ __ZN15CAHDecTansyHevc24populatePictureRegistersEv.cold.3
+ __ZN15CAHDecTansyHevc24populatePictureRegistersEv.cold.4
+ __ZN15CAHDecTansyHevc4initEv.cold.1
+ __ZN15CAHDecThymeHevc11initPictureEjjb.cold.1
+ __ZN15CAHDecThymeHevc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN15CAHDecThymeHevc16allocWorkBuf_PPSEPvS0_S0_.cold.10
+ __ZN15CAHDecThymeHevc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN15CAHDecThymeHevc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN15CAHDecThymeHevc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN15CAHDecThymeHevc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN15CAHDecThymeHevc16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN15CAHDecThymeHevc16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN15CAHDecThymeHevc16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN15CAHDecThymeHevc16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN15CAHDecThymeHevc16allocWorkBuf_SPSEPv.cold.1
+ __ZN15CAHDecThymeHevc16allocWorkBuf_SPSEPv.cold.2
+ __ZN15CAHDecThymeHevc16allocWorkBuf_SPSEPv.cold.3
+ __ZN15CAHDecThymeHevc24populatePictureRegistersEv.cold.1
+ __ZN15CAHDecThymeHevc24populatePictureRegistersEv.cold.2
+ __ZN15CAHDecThymeHevc24populatePictureRegistersEv.cold.3
+ __ZN15CAHDecThymeHevc24populatePictureRegistersEv.cold.4
+ __ZN15CAHDecThymeHevc4initEv.cold.1
+ __ZN15CAHDecViolaHevc11initPictureEjjb.cold.1
+ __ZN15CAHDecViolaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN15CAHDecViolaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN15CAHDecViolaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN15CAHDecViolaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN15CAHDecViolaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN15CAHDecViolaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN15CAHDecViolaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN15CAHDecViolaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN15CAHDecViolaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN15CAHDecViolaHevc16allocWorkBuf_SPSEPv.cold.1
+ __ZN15CAHDecViolaHevc16allocWorkBuf_SPSEPv.cold.2
+ __ZN15CAHDecViolaHevc16allocWorkBuf_SPSEPv.cold.3
+ __ZN15CAHDecViolaHevc24populatePictureRegistersEv.cold.1
+ __ZN15CAHDecViolaHevc24populatePictureRegistersEv.cold.2
+ __ZN15CAHDecViolaHevc4initEv.cold.1
+ __ZN15CAVDHevcDecoder10activatePSEP27hevc_slice_segment_header_t.cold.1
+ __ZN15CAVDHevcDecoder11VAGetParamsEjPj.cold.1
+ __ZN15CAVDHevcDecoder11VAGetParamsEjPj.cold.2
+ __ZN15CAVDHevcDecoder11VASetParamsEjPj.cold.1
+ __ZN15CAVDHevcDecoder12VAStopDecodeEv.cold.1
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.1
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.10
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.11
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.12
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.13
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.14
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.15
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.16
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.17
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.18
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.19
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.2
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.20
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.21
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.22
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.23
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.24
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.25
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.26
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.27
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.28
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.29
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.3
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.4
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.5
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.6
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.7
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.8
+ __ZN15CAVDHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.9
+ __ZN15CAVDHevcDecoder13VAStartDecodeEPhi.cold.1
+ __ZN15CAVDHevcDecoder13VAStartDecodeEPhi.cold.2
+ __ZN15CAVDHevcDecoder13VAStartDecodeEPhi.cold.3
+ __ZN15CAVDHevcDecoder13VAStartDecodeEPhi.cold.4
+ __ZN15CAVDHevcDecoder13VAStartDecodeEPhi.cold.5
+ __ZN15CAVDHevcDecoder13VAStartDecodeEPhi.cold.6
+ __ZN15CAVDHevcDecoder13VAStartDecodeEPhi.cold.7
+ __ZN15CAVDHevcDecoder13VAStartDecodeEPhi.cold.8
+ __ZN15CAVDHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP15hevc_slice_infoP15HevcPictureInfo.cold.1
+ __ZN15CAVDHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP15hevc_slice_infoP15HevcPictureInfo.cold.2
+ __ZN15CAVDHevcDecoder17allocateHwDecoderEv.cold.1
+ __ZN15CAVDHevcDecoder23allocateMembersPerLayerEi.cold.1
+ __ZN15CAVDHevcDecoder23allocateMembersPerLayerEi.cold.10
+ __ZN15CAVDHevcDecoder23allocateMembersPerLayerEi.cold.11
+ __ZN15CAVDHevcDecoder23allocateMembersPerLayerEi.cold.12
+ __ZN15CAVDHevcDecoder23allocateMembersPerLayerEi.cold.13
+ __ZN15CAVDHevcDecoder23allocateMembersPerLayerEi.cold.14
+ __ZN15CAVDHevcDecoder23allocateMembersPerLayerEi.cold.2
+ __ZN15CAVDHevcDecoder23allocateMembersPerLayerEi.cold.3
+ __ZN15CAVDHevcDecoder23allocateMembersPerLayerEi.cold.4
+ __ZN15CAVDHevcDecoder23allocateMembersPerLayerEi.cold.5
+ __ZN15CAVDHevcDecoder23allocateMembersPerLayerEi.cold.6
+ __ZN15CAVDHevcDecoder23allocateMembersPerLayerEi.cold.7
+ __ZN15CAVDHevcDecoder23allocateMembersPerLayerEi.cold.8
+ __ZN15CAVDHevcDecoder23allocateMembersPerLayerEi.cold.9
+ __ZN15CAVDHevcDecoder24decodeGetRenderTargetRefEjPP9_vsurface.cold.1
+ __ZN15CAVDHevcDecoder24decodeGetRenderTargetRefEjPP9_vsurface.cold.2
+ __ZN15CAVDHevcDecoder24decodeGetRenderTargetRefEjPP9_vsurface.cold.3
+ __ZN15CAVDHevcDecoder24decodeGetRenderTargetRefEjPP9_vsurface.cold.4
+ __ZN15CAVDHevcDecoder28deriveHevcOutputControlFlagsEP22hevc_nal_unit_header_tP27hevc_slice_segment_header_tP15HevcPictureInfob.cold.1
+ __ZN15CAVDHevcDecoder6VAInitEv.cold.1
+ __ZN15CAVDHevcDecoder6VAInitEv.cold.2
+ __ZN15CAVDHevcDecoder6VAInitEv.cold.3
+ __ZN16AVDFrameReceiver10FrameEventEPviPyi
+ __ZN16AVDFrameReceiver10FrameEventEPviPyi.cold.1
+ __ZN16CAHDecCatnipHevc11initPictureEjjb.cold.1
+ __ZN16CAHDecCatnipHevc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN16CAHDecCatnipHevc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN16CAHDecCatnipHevc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN16CAHDecCatnipHevc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN16CAHDecCatnipHevc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN16CAHDecCatnipHevc16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN16CAHDecCatnipHevc16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN16CAHDecCatnipHevc16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN16CAHDecCatnipHevc16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN16CAHDecCatnipHevc16allocWorkBuf_SPSEPv.cold.1
+ __ZN16CAHDecCatnipHevc16allocWorkBuf_SPSEPv.cold.2
+ __ZN16CAHDecCatnipHevc16allocWorkBuf_SPSEPv.cold.3
+ __ZN16CAHDecCatnipHevc24populatePictureRegistersEv.cold.1
+ __ZN16CAHDecCatnipHevc24populatePictureRegistersEv.cold.2
+ __ZN16CAHDecCatnipHevc24populatePictureRegistersEv.cold.3
+ __ZN16CAHDecCatnipHevc24populatePictureRegistersEv.cold.4
+ __ZN16CAHDecCatnipHevc4initEv.cold.1
+ __ZN16CAHDecCloverHevc11initPictureEjjb.cold.1
+ __ZN16CAHDecCloverHevc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN16CAHDecCloverHevc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN16CAHDecCloverHevc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN16CAHDecCloverHevc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN16CAHDecCloverHevc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN16CAHDecCloverHevc16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN16CAHDecCloverHevc16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN16CAHDecCloverHevc16allocWorkBuf_SPSEPv.cold.1
+ __ZN16CAHDecCloverHevc16allocWorkBuf_SPSEPv.cold.2
+ __ZN16CAHDecCloverHevc16allocWorkBuf_SPSEPv.cold.3
+ __ZN16CAHDecCloverHevc24populatePictureRegistersEv.cold.1
+ __ZN16CAHDecCloverHevc24populatePictureRegistersEv.cold.2
+ __ZN16CAHDecCloverHevc4initEv.cold.1
+ __ZN16CAHDecDahliaHevc11initPictureEjjb.cold.1
+ __ZN16CAHDecDahliaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN16CAHDecDahliaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN16CAHDecDahliaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN16CAHDecDahliaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN16CAHDecDahliaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN16CAHDecDahliaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN16CAHDecDahliaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN16CAHDecDahliaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN16CAHDecDahliaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN16CAHDecDahliaHevc16allocWorkBuf_SPSEPv.cold.1
+ __ZN16CAHDecDahliaHevc16allocWorkBuf_SPSEPv.cold.2
+ __ZN16CAHDecDahliaHevc16allocWorkBuf_SPSEPv.cold.3
+ __ZN16CAHDecDahliaHevc24populatePictureRegistersEv.cold.1
+ __ZN16CAHDecDahliaHevc24populatePictureRegistersEv.cold.2
+ __ZN16CAHDecDahliaHevc24populatePictureRegistersEv.cold.3
+ __ZN16CAHDecDahliaHevc24populatePictureRegistersEv.cold.4
+ __ZN16CAHDecDahliaHevc4initEv.cold.1
+ __ZN16CAHDecSalviaHevc11initPictureEjjb.cold.1
+ __ZN16CAHDecSalviaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN16CAHDecSalviaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN16CAHDecSalviaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN16CAHDecSalviaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN16CAHDecSalviaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN16CAHDecSalviaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN16CAHDecSalviaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN16CAHDecSalviaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN16CAHDecSalviaHevc16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN16CAHDecSalviaHevc16allocWorkBuf_SPSEPv.cold.1
+ __ZN16CAHDecSalviaHevc16allocWorkBuf_SPSEPv.cold.2
+ __ZN16CAHDecSalviaHevc16allocWorkBuf_SPSEPv.cold.3
+ __ZN16CAHDecSalviaHevc24populatePictureRegistersEv.cold.1
+ __ZN16CAHDecSalviaHevc24populatePictureRegistersEv.cold.2
+ __ZN16CAHDecSalviaHevc4initEv.cold.1
+ __ZN17CAHDecHibiscusAvc11initPictureEjjb.cold.1
+ __ZN17CAHDecHibiscusAvc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN17CAHDecHibiscusAvc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN17CAHDecHibiscusAvc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN17CAHDecHibiscusAvc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN17CAHDecHibiscusAvc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN17CAHDecHibiscusAvc16allocWorkBuf_SPSEPv.cold.1
+ __ZN17CAHDecHibiscusAvc16allocWorkBuf_SPSEPv.cold.2
+ __ZN17CAHDecHibiscusAvc16allocWorkBuf_SPSEPv.cold.3
+ __ZN17CAHDecHibiscusAvc24populatePictureRegistersEv.cold.1
+ __ZN17CAHDecHibiscusAvc24populatePictureRegistersEv.cold.2
+ __ZN17CAHDecHibiscusAvc24populatePictureRegistersEv.cold.3
+ __ZN17CAHDecHibiscusAvc24populatePictureRegistersEv.cold.4
+ __ZN17CAHDecHibiscusAvc24populatePictureRegistersEv.cold.5
+ __ZN17CAHDecHibiscusAvc24populatePictureRegistersEv.cold.6
+ __ZN17CAHDecHibiscusAvc4initEv.cold.1
+ __ZN17CAHDecHibiscusAvx12startPictureEj.cold.1
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_PPSEPvS0_S0_.cold.10
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_PPSEPvS0_S0_.cold.11
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_PPSEPvS0_S0_.cold.12
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_PPSEPvS0_S0_.cold.13
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_SPSEPv.cold.1
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_SPSEPv.cold.2
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_SPSEPv.cold.3
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_SPSEPv.cold.4
+ __ZN17CAHDecHibiscusAvx24populateAddressRegistersEv.cold.1
+ __ZN17CAHDecHibiscusAvx4initEv.cold.1
+ __ZN17CAHDecHibiscusAvx4initEv.cold.2
+ __ZN17CAHDecHibiscusAvx4initEv.cold.3
+ __ZN17CAHDecHibiscusLgh12startPictureEj.cold.1
+ __ZN17CAHDecHibiscusLgh16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN17CAHDecHibiscusLgh16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN17CAHDecHibiscusLgh16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN17CAHDecHibiscusLgh16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN17CAHDecHibiscusLgh16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN17CAHDecHibiscusLgh16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN17CAHDecHibiscusLgh16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN17CAHDecHibiscusLgh16allocWorkBuf_SPSEPv.cold.1
+ __ZN17CAHDecHibiscusLgh16allocWorkBuf_SPSEPv.cold.2
+ __ZN17CAHDecHibiscusLgh16allocWorkBuf_SPSEPv.cold.3
+ __ZN17CAHDecHibiscusLgh16allocWorkBuf_SPSEPv.cold.4
+ __ZN17CAHDecHibiscusLgh4initEv.cold.1
+ __ZN17CAHDecHibiscusLgh4initEv.cold.2
+ __ZN17CAHDecHibiscusLgh4initEv.cold.3
+ __ZN17CAVDMvHevcDecoder12VAStopDecodeEv.cold.1
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.1
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.10
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.11
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.12
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.13
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.14
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.15
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.16
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.17
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.18
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.19
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.2
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.20
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.21
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.22
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.23
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.24
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.25
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.26
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.27
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.28
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.29
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.3
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.30
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.31
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.32
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.33
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.34
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.35
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.4
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.5
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.6
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.7
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.8
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhijiiiP14avd_seq_params.cold.9
+ __ZN17CAVDMvHevcDecoder13VAStartDecodeEPhi.cold.1
+ __ZN17CAVDMvHevcDecoder13VAStartDecodeEPhi.cold.10
+ __ZN17CAVDMvHevcDecoder13VAStartDecodeEPhi.cold.11
+ __ZN17CAVDMvHevcDecoder13VAStartDecodeEPhi.cold.12
+ __ZN17CAVDMvHevcDecoder13VAStartDecodeEPhi.cold.13
+ __ZN17CAVDMvHevcDecoder13VAStartDecodeEPhi.cold.2
+ __ZN17CAVDMvHevcDecoder13VAStartDecodeEPhi.cold.3
+ __ZN17CAVDMvHevcDecoder13VAStartDecodeEPhi.cold.4
+ __ZN17CAVDMvHevcDecoder13VAStartDecodeEPhi.cold.5
+ __ZN17CAVDMvHevcDecoder13VAStartDecodeEPhi.cold.6
+ __ZN17CAVDMvHevcDecoder13VAStartDecodeEPhi.cold.7
+ __ZN17CAVDMvHevcDecoder13VAStartDecodeEPhi.cold.8
+ __ZN17CAVDMvHevcDecoder13VAStartDecodeEPhi.cold.9
+ __ZN17CAVDMvHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP15hevc_slice_infoP15HevcPictureInfo.cold.1
+ __ZN17CAVDMvHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP15hevc_slice_infoP15HevcPictureInfo.cold.2
+ __ZN17CAVDMvHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP15hevc_slice_infoP15HevcPictureInfo.cold.3
+ __ZN17CAVDMvHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP15hevc_slice_infoP15HevcPictureInfo.cold.4
+ __ZN17CAVDMvHevcDecoder19mvhevcOutputBumpingEP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP27hevc_slice_segment_header_tP15HevcPictureInfo.cold.1
+ __ZN17CAVDMvHevcDecoder19mvhevcOutputBumpingEP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP27hevc_slice_segment_header_tP15HevcPictureInfo.cold.2
+ __ZN17CAVDMvHevcDecoder19mvhevcOutputBumpingEP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP27hevc_slice_segment_header_tP15HevcPictureInfo.cold.3
+ __ZN17CAVDMvHevcDecoder20InitMultiViewDpbInfoEv.cold.1
+ __ZN17CAVDMvHevcDecoder22insertCurPicIntoAuListEP15HevcPictureInfo.cold.1
+ __ZN17CAVDMvHevcDecoder22insertCurPicIntoAuListEP15HevcPictureInfo.cold.2
+ __ZN17CAVDMvHevcDecoder22insertCurPicIntoAuListEP15HevcPictureInfo.cold.3
+ __ZN17CAVDMvHevcDecoder27allocateMultiViewHwDecodersEi.cold.1
+ __ZN17CAVDMvHevcDecoder27allocateMultiViewHwDecodersEi.cold.2
+ __ZN17CAVDMvHevcDecoder27allocateMultiViewHwDecodersEi.cold.3
+ __ZN17CAVDMvHevcDecoder28deriveSpsParamsFromActiveVpsEP29hevc_sequence_parameter_set_ti.cold.1
+ __ZN17CAVDMvHevcDecoder9createDPBEP29hevc_sequence_parameter_set_tP15HevcPictureInfoi.cold.1
+ __ZN18CAHDecDandelionAvc11decHdrCSizeEj
+ __ZN18CAHDecDandelionAvc11decHdrYSizeEj
+ __ZN18CAHDecDandelionAvc11initPictureEjjb
+ __ZN18CAHDecDandelionAvc11initPictureEjjb.cold.1
+ __ZN18CAHDecDandelionAvc12decodeBufferEv
+ __ZN18CAHDecDandelionAvc12getSWRStrideEjjjj
+ __ZN18CAHDecDandelionAvc13decHdrCStrideEv
+ __ZN18CAHDecDandelionAvc13decHdrYStrideEv
+ __ZN18CAHDecDandelionAvc13getTileEndCTUEjj
+ __ZN18CAHDecDandelionAvc14decHdrCLinAddrEj
+ __ZN18CAHDecDandelionAvc14decHdrYLinAddrEj
+ __ZN18CAHDecDandelionAvc14populateSlicesEj
+ __ZN18CAHDecDandelionAvc14setVPInstrFifoEj
+ __ZN18CAHDecDandelionAvc15copyScalingListER15AvcScalingListsR13AvcQtMatCoeffPhS4_S4_i
+ __ZN18CAHDecDandelionAvc15freeWorkBuf_PPSEPv
+ __ZN18CAHDecDandelionAvc15freeWorkBuf_SPSEv
+ __ZN18CAHDecDandelionAvc15getTileIdxAboveEj
+ __ZN18CAHDecDandelionAvc15getTileStartCTUEjj
+ __ZN18CAHDecDandelionAvc15populateAvdWorkEj
+ __ZN18CAHDecDandelionAvc16allocWorkBuf_PPSEPvS0_S0_
+ __ZN18CAHDecDandelionAvc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN18CAHDecDandelionAvc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN18CAHDecDandelionAvc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN18CAHDecDandelionAvc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN18CAHDecDandelionAvc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN18CAHDecDandelionAvc16allocWorkBuf_SPSEPv
+ __ZN18CAHDecDandelionAvc16allocWorkBuf_SPSEPv.cold.1
+ __ZN18CAHDecDandelionAvc16allocWorkBuf_SPSEPv.cold.2
+ __ZN18CAHDecDandelionAvc16allocWorkBuf_SPSEPv.cold.3
+ __ZN18CAHDecDandelionAvc16decodeBufferSizeEv
+ __ZN18CAHDecDandelionAvc21updateCommonRegistersEj
+ __ZN18CAHDecDandelionAvc22populateSliceRegistersEP17AvcSliceRegistersi
+ __ZN18CAHDecDandelionAvc23populateCommonRegistersEv
+ __ZN18CAHDecDandelionAvc24populatePictureRegistersEv
+ __ZN18CAHDecDandelionAvc24populatePictureRegistersEv.cold.1
+ __ZN18CAHDecDandelionAvc24populatePictureRegistersEv.cold.2
+ __ZN18CAHDecDandelionAvc24populatePictureRegistersEv.cold.3
+ __ZN18CAHDecDandelionAvc24populatePictureRegistersEv.cold.4
+ __ZN18CAHDecDandelionAvc24populatePictureRegistersEv.cold.5
+ __ZN18CAHDecDandelionAvc24populatePictureRegistersEv.cold.6
+ __ZN18CAHDecDandelionAvc25AvcPicScalingListFallBackEP7sAvcSPSP7sAvcPPS
+ __ZN18CAHDecDandelionAvc25AvcSeqScalingListFallBackEP7sAvcSPS
+ __ZN18CAHDecDandelionAvc25populateSequenceRegistersEv
+ __ZN18CAHDecDandelionAvc4initEv
+ __ZN18CAHDecDandelionAvc4initEv.cold.1
+ __ZN18CAHDecDandelionAvcC2EP14CAVDAvcDecoder
+ __ZN18CAHDecDandelionAvcD0Ev
+ __ZN18CAHDecDandelionAvcD1Ev
+ __ZN18CAHDecDandelionAvcD2Ev
+ __ZN18CAHDecDandelionAvx10isLfPadDisEv
+ __ZN18CAHDecDandelionAvx11decHdrCSizeEj
+ __ZN18CAHDecDandelionAvx11decHdrYSizeEj
+ __ZN18CAHDecDandelionAvx11initPictureEjjb
+ __ZN18CAHDecDandelionAvx12decodeBufferEv
+ __ZN18CAHDecDandelionAvx12startPictureEj
+ __ZN18CAHDecDandelionAvx12startPictureEj.cold.1
+ __ZN18CAHDecDandelionAvx13DecodePictureEjj
+ __ZN18CAHDecDandelionAvx13decHdrCStrideEv
+ __ZN18CAHDecDandelionAvx13decHdrYStrideEv
+ __ZN18CAHDecDandelionAvx13getTileEndCTUEjj
+ __ZN18CAHDecDandelionAvx13populateTilesEv
+ __ZN18CAHDecDandelionAvx14decHdrCLinAddrEj
+ __ZN18CAHDecDandelionAvx14decHdrYLinAddrEj
+ __ZN18CAHDecDandelionAvx14populateSlicesEj
+ __ZN18CAHDecDandelionAvx14setVPInstrFifoEj
+ __ZN18CAHDecDandelionAvx15freeWorkBuf_PPSEPv
+ __ZN18CAHDecDandelionAvx15freeWorkBuf_SPSEv
+ __ZN18CAHDecDandelionAvx15getTileIdxAboveEj
+ __ZN18CAHDecDandelionAvx15getTileStartCTUEjj
+ __ZN18CAHDecDandelionAvx15populateAvdWorkEj
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.10
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.11
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.12
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.13
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_SPSEPv
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_SPSEPv.cold.1
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_SPSEPv.cold.2
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_SPSEPv.cold.3
+ __ZN18CAHDecDandelionAvx16allocWorkBuf_SPSEPv.cold.4
+ __ZN18CAHDecDandelionAvx16decodeBufferSizeEv
+ __ZN18CAHDecDandelionAvx17getPPSWorkBufSizeEPvS0_
+ __ZN18CAHDecDandelionAvx18populateClearTilesEv
+ __ZN18CAHDecDandelionAvx20getUpscaleConvolveX0Eiii
+ __ZN18CAHDecDandelionAvx21populateTileRegistersEP16AvxTileRegistersj
+ __ZN18CAHDecDandelionAvx21updateCommonRegistersEj
+ __ZN18CAHDecDandelionAvx22calc_az_left_tile_sizeEiiiiiiii
+ __ZN18CAHDecDandelionAvx22calc_lf_left_tile_sizeEiiiiiiiii
+ __ZN18CAHDecDandelionAvx22calc_lr_left_tile_sizeEiiiiiiiii
+ __ZN18CAHDecDandelionAvx22getUpscaleConvolveStepEii
+ __ZN18CAHDecDandelionAvx22ppsWorkBufSizeIncreaseEPvS0_
+ __ZN18CAHDecDandelionAvx23populateAvxVPDependencyEv
+ __ZN18CAHDecDandelionAvx23populateCommonRegistersEv
+ __ZN18CAHDecDandelionAvx24populateAddressRegistersEv
+ __ZN18CAHDecDandelionAvx24populateAddressRegistersEv.cold.1
+ __ZN18CAHDecDandelionAvx24populatePictureRegistersEv
+ __ZN18CAHDecDandelionAvx25populateSequenceRegistersEv
+ __ZN18CAHDecDandelionAvx27calc_lf_above_pix_tile_sizeEiiiiiiii
+ __ZN18CAHDecDandelionAvx27populateDecryptionRegistersEv
+ __ZN18CAHDecDandelionAvx4initEv
+ __ZN18CAHDecDandelionAvx4initEv.cold.1
+ __ZN18CAHDecDandelionAvx4initEv.cold.2
+ __ZN18CAHDecDandelionAvx4initEv.cold.3
+ __ZN18CAHDecDandelionAvxC2EP14CAVDAvxDecoder
+ __ZN18CAHDecDandelionAvxD0Ev
+ __ZN18CAHDecDandelionAvxD1Ev
+ __ZN18CAHDecDandelionAvxD2Ev
+ __ZN18CAHDecDandelionLgh11decHdrCSizeEj
+ __ZN18CAHDecDandelionLgh11decHdrYSizeEj
+ __ZN18CAHDecDandelionLgh11initPictureEjjb
+ __ZN18CAHDecDandelionLgh12decodeBufferEv
+ __ZN18CAHDecDandelionLgh12getSWRStrideEjjjj
+ __ZN18CAHDecDandelionLgh12startPictureEj
+ __ZN18CAHDecDandelionLgh12startPictureEj.cold.1
+ __ZN18CAHDecDandelionLgh13DecodePictureEj
+ __ZN18CAHDecDandelionLgh13decHdrCStrideEv
+ __ZN18CAHDecDandelionLgh13decHdrYStrideEv
+ __ZN18CAHDecDandelionLgh13getTileEndCTUEjj
+ __ZN18CAHDecDandelionLgh13populateTilesEv
+ __ZN18CAHDecDandelionLgh14clearSegBufferEv
+ __ZN18CAHDecDandelionLgh14decHdrCLinAddrEj
+ __ZN18CAHDecDandelionLgh14decHdrYLinAddrEj
+ __ZN18CAHDecDandelionLgh14populateSlicesEj
+ __ZN18CAHDecDandelionLgh14setVPInstrFifoEj
+ __ZN18CAHDecDandelionLgh15freeWorkBuf_PPSEPv
+ __ZN18CAHDecDandelionLgh15freeWorkBuf_SPSEv
+ __ZN18CAHDecDandelionLgh15getTileIdxAboveEj
+ __ZN18CAHDecDandelionLgh15getTileStartCTUEjj
+ __ZN18CAHDecDandelionLgh15populateAvdWorkEj
+ __ZN18CAHDecDandelionLgh16allocWorkBuf_PPSEPvS0_S0_
+ __ZN18CAHDecDandelionLgh16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN18CAHDecDandelionLgh16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN18CAHDecDandelionLgh16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN18CAHDecDandelionLgh16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN18CAHDecDandelionLgh16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN18CAHDecDandelionLgh16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN18CAHDecDandelionLgh16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN18CAHDecDandelionLgh16allocWorkBuf_SPSEPv
+ __ZN18CAHDecDandelionLgh16allocWorkBuf_SPSEPv.cold.1
+ __ZN18CAHDecDandelionLgh16allocWorkBuf_SPSEPv.cold.2
+ __ZN18CAHDecDandelionLgh16allocWorkBuf_SPSEPv.cold.3
+ __ZN18CAHDecDandelionLgh16allocWorkBuf_SPSEPv.cold.4
+ __ZN18CAHDecDandelionLgh16decodeBufferSizeEv
+ __ZN18CAHDecDandelionLgh21populateTileRegistersEP16LghTileRegisters
+ __ZN18CAHDecDandelionLgh21updateCommonRegistersEj
+ __ZN18CAHDecDandelionLgh23populateCommonRegistersEv
+ __ZN18CAHDecDandelionLgh24populatePictureRegistersEv
+ __ZN18CAHDecDandelionLgh25populateSequenceRegistersEv
+ __ZN18CAHDecDandelionLgh4initEv
+ __ZN18CAHDecDandelionLgh4initEv.cold.1
+ __ZN18CAHDecDandelionLgh4initEv.cold.2
+ __ZN18CAHDecDandelionLgh4initEv.cold.3
+ __ZN18CAHDecDandelionLghC2EP14CAVDLghDecoder
+ __ZN18CAHDecDandelionLghD0Ev
+ __ZN18CAHDecDandelionLghD1Ev
+ __ZN18CAHDecDandelionLghD2Ev
+ __ZN18CAHDecHibiscusHevc11initPictureEjjb.cold.1
+ __ZN18CAHDecHibiscusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN18CAHDecHibiscusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.10
+ __ZN18CAHDecHibiscusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN18CAHDecHibiscusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN18CAHDecHibiscusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN18CAHDecHibiscusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN18CAHDecHibiscusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN18CAHDecHibiscusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN18CAHDecHibiscusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN18CAHDecHibiscusHevc16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN18CAHDecHibiscusHevc16allocWorkBuf_SPSEPv.cold.1
+ __ZN18CAHDecHibiscusHevc16allocWorkBuf_SPSEPv.cold.2
+ __ZN18CAHDecHibiscusHevc16allocWorkBuf_SPSEPv.cold.3
+ __ZN18CAHDecHibiscusHevc24populatePictureRegistersEv.cold.1
+ __ZN18CAHDecHibiscusHevc24populatePictureRegistersEv.cold.2
+ __ZN18CAHDecHibiscusHevc24populatePictureRegistersEv.cold.3
+ __ZN18CAHDecHibiscusHevc24populatePictureRegistersEv.cold.4
+ __ZN18CAHDecHibiscusHevc4initEv.cold.1
+ __ZN19CAHDecDandelionHevc11decHdrCSizeEj
+ __ZN19CAHDecDandelionHevc11decHdrYSizeEj
+ __ZN19CAHDecDandelionHevc11initPictureEjjb
+ __ZN19CAHDecDandelionHevc11initPictureEjjb.cold.1
+ __ZN19CAHDecDandelionHevc12decodeBufferEv
+ __ZN19CAHDecDandelionHevc12getMVmemInfoEiP20_avd_client_mem_infoPj
+ __ZN19CAHDecDandelionHevc12getSWRStrideEjjjj
+ __ZN19CAHDecDandelionHevc13decHdrCStrideEv
+ __ZN19CAHDecDandelionHevc13decHdrYStrideEv
+ __ZN19CAHDecDandelionHevc13getTileEndCTUEjj
+ __ZN19CAHDecDandelionHevc14decHdrCLinAddrEj
+ __ZN19CAHDecDandelionHevc14decHdrYLinAddrEj
+ __ZN19CAHDecDandelionHevc14populateSlicesEj
+ __ZN19CAHDecDandelionHevc14setVPInstrFifoEj
+ __ZN19CAHDecDandelionHevc15copyScalingListER16HevcScalingListsR14HevcQtMatCoeffjR24hevc_scaling_list_data_t
+ __ZN19CAHDecDandelionHevc15freeWorkBuf_PPSEPv
+ __ZN19CAHDecDandelionHevc15freeWorkBuf_SPSEv
+ __ZN19CAHDecDandelionHevc15getTileIdxAboveEj
+ __ZN19CAHDecDandelionHevc15getTileStartCTUEjj
+ __ZN19CAHDecDandelionHevc15populateAvdWorkEj
+ __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_
+ __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.1
+ __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.10
+ __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.2
+ __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.3
+ __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.4
+ __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.5
+ __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.6
+ __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.7
+ __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.8
+ __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.9
+ __ZN19CAHDecDandelionHevc16allocWorkBuf_SPSEPv
+ __ZN19CAHDecDandelionHevc16allocWorkBuf_SPSEPv.cold.1
+ __ZN19CAHDecDandelionHevc16allocWorkBuf_SPSEPv.cold.2
+ __ZN19CAHDecDandelionHevc16allocWorkBuf_SPSEPv.cold.3
+ __ZN19CAHDecDandelionHevc16decodeBufferSizeEv
+ __ZN19CAHDecDandelionHevc17getTileHdrMemInfoEiP17_Tile_hdr_buffs_t
+ __ZN19CAHDecDandelionHevc21updateCommonRegistersEj
+ __ZN19CAHDecDandelionHevc22populateSliceRegistersEP18HevcSliceRegistersi
+ __ZN19CAHDecDandelionHevc23populateCommonRegistersEv
+ __ZN19CAHDecDandelionHevc24populatePictureRegistersEv
+ __ZN19CAHDecDandelionHevc24populatePictureRegistersEv.cold.1
+ __ZN19CAHDecDandelionHevc24populatePictureRegistersEv.cold.2
+ __ZN19CAHDecDandelionHevc24populatePictureRegistersEv.cold.3
+ __ZN19CAHDecDandelionHevc24populatePictureRegistersEv.cold.4
+ __ZN19CAHDecDandelionHevc25populateSequenceRegistersEv
+ __ZN19CAHDecDandelionHevc4initEv
+ __ZN19CAHDecDandelionHevc4initEv.cold.1
+ __ZN19CAHDecDandelionHevcD0Ev
+ __ZN19CAHDecDandelionHevcD1Ev
+ __ZN19CAHDecDandelionHevcD2Ev
+ __ZN22AppleAVDCommandBuilder13createDecoderEP25_sAppleAVDCreateDecoderInP26_sAppleAVDCreateDecoderOutP22_sAppleAVDVideoContext.cold.1
+ __ZN22AppleAVDCommandBuilder13createDecoderEP25_sAppleAVDCreateDecoderInP26_sAppleAVDCreateDecoderOutP22_sAppleAVDVideoContext.cold.10
+ __ZN22AppleAVDCommandBuilder13createDecoderEP25_sAppleAVDCreateDecoderInP26_sAppleAVDCreateDecoderOutP22_sAppleAVDVideoContext.cold.11
+ __ZN22AppleAVDCommandBuilder13createDecoderEP25_sAppleAVDCreateDecoderInP26_sAppleAVDCreateDecoderOutP22_sAppleAVDVideoContext.cold.12
+ __ZN22AppleAVDCommandBuilder13createDecoderEP25_sAppleAVDCreateDecoderInP26_sAppleAVDCreateDecoderOutP22_sAppleAVDVideoContext.cold.13
+ __ZN22AppleAVDCommandBuilder13createDecoderEP25_sAppleAVDCreateDecoderInP26_sAppleAVDCreateDecoderOutP22_sAppleAVDVideoContext.cold.14
+ __ZN22AppleAVDCommandBuilder13createDecoderEP25_sAppleAVDCreateDecoderInP26_sAppleAVDCreateDecoderOutP22_sAppleAVDVideoContext.cold.15
+ __ZN22AppleAVDCommandBuilder13createDecoderEP25_sAppleAVDCreateDecoderInP26_sAppleAVDCreateDecoderOutP22_sAppleAVDVideoContext.cold.2
+ __ZN22AppleAVDCommandBuilder13createDecoderEP25_sAppleAVDCreateDecoderInP26_sAppleAVDCreateDecoderOutP22_sAppleAVDVideoContext.cold.3
+ __ZN22AppleAVDCommandBuilder13createDecoderEP25_sAppleAVDCreateDecoderInP26_sAppleAVDCreateDecoderOutP22_sAppleAVDVideoContext.cold.4
+ __ZN22AppleAVDCommandBuilder13createDecoderEP25_sAppleAVDCreateDecoderInP26_sAppleAVDCreateDecoderOutP22_sAppleAVDVideoContext.cold.5
+ __ZN22AppleAVDCommandBuilder13createDecoderEP25_sAppleAVDCreateDecoderInP26_sAppleAVDCreateDecoderOutP22_sAppleAVDVideoContext.cold.6
+ __ZN22AppleAVDCommandBuilder13createDecoderEP25_sAppleAVDCreateDecoderInP26_sAppleAVDCreateDecoderOutP22_sAppleAVDVideoContext.cold.7
+ __ZN22AppleAVDCommandBuilder13createDecoderEP25_sAppleAVDCreateDecoderInP26_sAppleAVDCreateDecoderOutP22_sAppleAVDVideoContext.cold.8
+ __ZN22AppleAVDCommandBuilder13createDecoderEP25_sAppleAVDCreateDecoderInP26_sAppleAVDCreateDecoderOutP22_sAppleAVDVideoContext.cold.9
+ __ZN22AppleAVDCommandBuilder14decodeFrameFigEP26_sAppleAVDDecodeFrameFigInP27_sAppleAVDDecodeFrameFigOut.cold.1
+ __ZN22AppleAVDCommandBuilder14decodeFrameFigEP26_sAppleAVDDecodeFrameFigInP27_sAppleAVDDecodeFrameFigOut.cold.2
+ __ZN22AppleAVDCommandBuilder14decodeFrameFigEP26_sAppleAVDDecodeFrameFigInP27_sAppleAVDDecodeFrameFigOut.cold.3
+ __ZN22AppleAVDCommandBuilder14decodeFrameFigEP26_sAppleAVDDecodeFrameFigInP27_sAppleAVDDecodeFrameFigOut.cold.4
+ __ZN22AppleAVDCommandBuilder14decodeFrameFigEP26_sAppleAVDDecodeFrameFigInP27_sAppleAVDDecodeFrameFigOut.cold.5
+ __ZN22AppleAVDCommandBuilder14decodeFrameFigEP26_sAppleAVDDecodeFrameFigInP27_sAppleAVDDecodeFrameFigOut.cold.6
+ __ZN22AppleAVDCommandBuilder14decodeFrameFigEP26_sAppleAVDDecodeFrameFigInP27_sAppleAVDDecodeFrameFigOut.cold.7
+ __ZN22AppleAVDCommandBuilder14decodeFrameFigEP26_sAppleAVDDecodeFrameFigInP27_sAppleAVDDecodeFrameFigOut.cold.8
+ __ZN22AppleAVDCommandBuilder14destroyDecoderEP26_sAppleAVDDestroyDecoderInP27_sAppleAVDDestroyDecoderOut.cold.1
+ __ZN22AppleAVDCommandBuilder14destroyDecoderEP26_sAppleAVDDestroyDecoderInP27_sAppleAVDDestroyDecoderOut.cold.2
+ __ZN22AppleAVDCommandBuilder15allocRVRAMemoryEjj.cold.1
+ __ZN22AppleAVDCommandBuilder16scaleOutputFrameEPvS0_jjjjiPhjjj16scaler_context_t25scaler_bilinear_buffers_tS0_S0_.cold.1
+ __ZN22AppleAVDCommandBuilder16scaleOutputFrameEPvS0_jjjjiPhjjj16scaler_context_t25scaler_bilinear_buffers_tS0_S0_.cold.2
+ __ZN22AppleAVDCommandBuilder16scaleOutputFrameEPvS0_jjjjiPhjjj16scaler_context_t25scaler_bilinear_buffers_tS0_S0_.cold.3
+ __ZN22AppleAVDCommandBuilder16scaleOutputFrameEPvS0_jjjjiPhjjj16scaler_context_t25scaler_bilinear_buffers_tS0_S0_.cold.4
+ __ZN22AppleAVDCommandBuilder16scaleOutputFrameEPvS0_jjjjiPhjjj16scaler_context_t25scaler_bilinear_buffers_tS0_S0_.cold.5
+ __ZN22AppleAVDCommandBuilder23populateOnDemandDVAInfoEP18on_demand_dva_infoj.cold.1
+ __ZN22AppleAVDCommandBuilder23populateOnDemandDVAInfoEP18on_demand_dva_infoj.cold.2
+ __ZN22AppleAVDCommandBuilder28setReleaseCVPixelBufferIndexEij.cold.1
+ __ZN22AppleAVDCommandBuilder33retrieveSampleBufferForSIODecryptEv.cold.1
+ __ZN22AppleAVDCommandBuilder33retrieveSampleBufferForSIODecryptEv.cold.2
+ __ZN22AppleAVDCommandBuilder33retrieveSampleBufferForSIODecryptEv.cold.3
+ __ZN22AppleAVDCommandBuilder36decodeFrameFigHelper_CheckParametersEP26_sAppleAVDDecodeFrameFigInP27_sAppleAVDDecodeFrameFigOut.cold.1
+ __ZN22AppleAVDCommandBuilder36decodeFrameFigHelper_CheckParametersEP26_sAppleAVDDecodeFrameFigInP27_sAppleAVDDecodeFrameFigOut.cold.2
+ __ZN22AppleAVDCommandBuilder36decodeFrameFigHelper_CheckParametersEP26_sAppleAVDDecodeFrameFigInP27_sAppleAVDDecodeFrameFigOut.cold.3
+ __ZN22AppleAVDCommandBuilder36decodeFrameFigHelper_CheckParametersEP26_sAppleAVDDecodeFrameFigInP27_sAppleAVDDecodeFrameFigOut.cold.4
+ __ZN22AppleAVDCommandBuilder36decodeFrameFigHelper_VASetParametersEP26_sAppleAVDDecodeFrameFigIn.cold.1
+ __ZN22AppleAVDCommandBuilder36decodeFrameFigHelper_VASetParametersEP26_sAppleAVDDecodeFrameFigIn.cold.2
+ __ZN22AppleAVDCommandBuilder36decodeFrameFigHelper_VASetParametersEP26_sAppleAVDDecodeFrameFigIn.cold.3
+ __ZN22AppleAVDCommandBuilder36decodeFrameFigHelper_VASetParametersEP26_sAppleAVDDecodeFrameFigIn.cold.4
+ __ZN22AppleAVDCommandBuilder36decodeFrameFigHelper_VASetParametersEP26_sAppleAVDDecodeFrameFigIn.cold.5
+ __ZN22AppleAVDCommandBuilder36decodeFrameFigHelper_VASetParametersEP26_sAppleAVDDecodeFrameFigIn.cold.6
+ __ZN22AppleAVDCommandBuilder36decodeFrameFigHelper_VASetParametersEP26_sAppleAVDDecodeFrameFigIn.cold.7
+ __ZN22AppleAVDCommandBuilder36decodeFrameFigHelper_VASetParametersEP26_sAppleAVDDecodeFrameFigIn.cold.8
+ __ZN22AppleAVDCommandBuilder36decodeFrameFigHelper_VASetParametersEP26_sAppleAVDDecodeFrameFigIn.cold.9
+ __ZN22AppleAVDCommandBuilder37setReleaseBufferIndexToResponseBufferEP20_frameResponseBufferij.cold.1
+ __ZN22AppleAVDCommandBuilder45decodeFrameFigHelper_CreateAndSubmitDecodeCMDEP26_sAppleAVDDecodeFrameFigInii.cold.1
+ __ZN6CAHDec16addToPatcherListEP20_avd_client_mem_infojjyjjh.cold.1
+ __ZN6CAHDec16addToPatcherListEP20_avd_client_mem_infojjyjjh.cold.2
+ __ZN6CAHDec16addToPatcherListEP20_avd_client_mem_infojjyjjh.cold.3
+ __ZN6CAHDec16addToPatcherListEP20_avd_client_mem_infojjyjjh.cold.4
+ __ZN6CAHDec16addToPatcherListEP20_avd_client_mem_infojjyjjh.cold.5
+ __ZN6CAHDecD2Ev.cold.1
+ __ZN7AVC_RLM11initPictureER14sAvcNaluHeaderR7sAvcSPSR15sAvcSliceHeaderR15sAvcPictureInfo.cold.1
+ __ZN7AVC_RLM14initRefPicListER15sAvcSliceHeaderR13sAvcSliceInfoRK15sAvcPictureInfo.cold.1
+ __ZN7AVC_RLM14initRefPicListER15sAvcSliceHeaderR13sAvcSliceInfoRK15sAvcPictureInfo.cold.2
+ __ZN7AVC_RLM14initRefPicListER15sAvcSliceHeaderR13sAvcSliceInfoRK15sAvcPictureInfo.cold.3
+ __ZN7AVC_RLM14initRefPicListER15sAvcSliceHeaderR13sAvcSliceInfoRK15sAvcPictureInfo.cold.4
+ __ZN7AVC_RLM14initRefPicListER15sAvcSliceHeaderR13sAvcSliceInfoRK15sAvcPictureInfo.cold.5
+ __ZN7AVC_RLM15fillFrameNumGapER15sAvcSliceHeader.cold.1
+ __ZN7AVC_RLM19dec_ref_pic_markingER15sAvcSliceHeaderR15sAvcPictureInfo.cold.1
+ __ZN7AVC_RLM19dec_ref_pic_markingER15sAvcSliceHeaderR15sAvcPictureInfo.cold.2
+ __ZN7AVC_RLM19dec_ref_pic_markingER15sAvcSliceHeaderR15sAvcPictureInfo.cold.3
+ __ZN7AVC_RLM20slidingWindowProcessEb.cold.1
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.1
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.10
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.11
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.12
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.13
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.14
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.15
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.16
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.17
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.18
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.19
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.2
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.20
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.21
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.22
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.3
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.4
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.5
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.6
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.7
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.8
+ __ZN8AVC_RBSP16parseSliceHeaderEP15sAvcSliceHeaderP14sAvcNaluHeaderP7sAvcPPSP7sAvcSPS.cold.9
+ __ZN8AVC_RBSP38performRangeChecksAndComputeParametersEP7sAvcSPSP7sAvcPPS
+ __ZN8AVC_RBSP38performRangeChecksAndComputeParametersEP7sAvcSPSP7sAvcPPS.cold.1
+ __ZN8AVC_RBSP8parseHRDER7sAvcHRD.cold.1
+ __ZN8AVC_RBSP8parsePPSEP7sAvcPPSP7sAvcSPS.cold.1
+ __ZN8AVC_RBSP8parsePPSEP7sAvcPPSP7sAvcSPS.cold.2
+ __ZN8AVC_RBSP8parsePPSEP7sAvcPPSP7sAvcSPS.cold.3
+ __ZN8AVC_RBSP8parsePPSEP7sAvcPPSP7sAvcSPS.cold.4
+ __ZN8AVC_RBSP8parsePPSEP7sAvcPPSP7sAvcSPS.cold.5
+ __ZN8AVC_RBSP8parsePPSEP7sAvcPPSP7sAvcSPS.cold.6
+ __ZN8AVC_RBSP8parseSPSEP7sAvcSPS.cold.1
+ __ZN8AVC_RBSP8parseSPSEP7sAvcSPS.cold.2
+ __ZN8AVC_RBSP8parseSPSEP7sAvcSPS.cold.3
+ __ZN8AVC_RBSP8parseSPSEP7sAvcSPS.cold.4
+ __ZN8AVC_RBSP8parseSPSEP7sAvcSPS.cold.5
+ __ZN8AVC_RBSP8parseSPSEP7sAvcSPS.cold.6
+ __ZN9HEVC_RBSP15calcVPSNumViewsEP26hevc_video_parameter_set_t.cold.1
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.1
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.10
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.11
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.12
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.13
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.14
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.15
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.16
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.17
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.18
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.19
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.2
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.20
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.21
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.22
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.23
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.24
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.25
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.26
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.27
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.28
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.29
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.3
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.30
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.31
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.32
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.33
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.34
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.35
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.36
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.37
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.4
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.5
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.6
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.7
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.8
+ __ZN9HEVC_RBSP16parseSliceHeaderEP27hevc_slice_segment_header_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_tP26hevc_video_parameter_set_tbS1_.cold.9
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.1
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.10
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.11
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.12
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.13
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.14
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.15
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.16
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.17
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.18
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.19
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.2
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.20
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.21
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.22
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.3
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.4
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.5
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.6
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.7
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.8
+ __ZN9HEVC_RBSP17parseVPSextensionEP26hevc_video_parameter_set_t.cold.9
+ __ZN9HEVC_RBSP23calcLayerSetLayerIdListEP26hevc_video_parameter_set_t.cold.1
+ __ZN9HEVC_RBSP23calcLayerSetLayerIdListEP26hevc_video_parameter_set_t.cold.2
+ __ZN9HEVC_RBSP23calcLayerSetLayerIdListEP26hevc_video_parameter_set_t.cold.3
+ __ZN9HEVC_RBSP23calcLayerSetLayerIdListEP26hevc_video_parameter_set_t.cold.4
+ __ZN9HEVC_RBSP23parseShortTermRefPicSetEP29hevc_short_term_ref_pic_set_tjj.cold.1
+ __ZN9HEVC_RBSP26calcAddLayerSetLayerIdListEP26hevc_video_parameter_set_tt.cold.1
+ __ZN9HEVC_RBSP28parseRefPicListsModificationEP27hevc_slice_segment_header_t.cold.1
+ __ZN9HEVC_RBSP28parseRefPicListsModificationEP27hevc_slice_segment_header_t.cold.2
+ __ZN9HEVC_RBSP38performRangeChecksAndComputeParametersEP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_t
+ __ZN9HEVC_RBSP38performRangeChecksAndComputeParametersEP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_t.cold.1
+ __ZN9HEVC_RBSP38performRangeChecksAndComputeParametersEP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_t.cold.2
+ __ZN9HEVC_RBSP38performRangeChecksAndComputeParametersEP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_t.cold.3
+ __ZN9HEVC_RBSP38performRangeChecksAndComputeParametersEP29hevc_sequence_parameter_set_tP28hevc_picture_parameter_set_t.cold.4
+ __ZN9HEVC_RBSP8parsePPSEP28hevc_picture_parameter_set_tP29hevc_sequence_parameter_set_t.cold.1
+ __ZN9HEVC_RBSP8parsePPSEP28hevc_picture_parameter_set_tP29hevc_sequence_parameter_set_t.cold.10
+ __ZN9HEVC_RBSP8parsePPSEP28hevc_picture_parameter_set_tP29hevc_sequence_parameter_set_t.cold.11
+ __ZN9HEVC_RBSP8parsePPSEP28hevc_picture_parameter_set_tP29hevc_sequence_parameter_set_t.cold.12
+ __ZN9HEVC_RBSP8parsePPSEP28hevc_picture_parameter_set_tP29hevc_sequence_parameter_set_t.cold.2
+ __ZN9HEVC_RBSP8parsePPSEP28hevc_picture_parameter_set_tP29hevc_sequence_parameter_set_t.cold.3
+ __ZN9HEVC_RBSP8parsePPSEP28hevc_picture_parameter_set_tP29hevc_sequence_parameter_set_t.cold.4
+ __ZN9HEVC_RBSP8parsePPSEP28hevc_picture_parameter_set_tP29hevc_sequence_parameter_set_t.cold.5
+ __ZN9HEVC_RBSP8parsePPSEP28hevc_picture_parameter_set_tP29hevc_sequence_parameter_set_t.cold.6
+ __ZN9HEVC_RBSP8parsePPSEP28hevc_picture_parameter_set_tP29hevc_sequence_parameter_set_t.cold.7
+ __ZN9HEVC_RBSP8parsePPSEP28hevc_picture_parameter_set_tP29hevc_sequence_parameter_set_t.cold.8
+ __ZN9HEVC_RBSP8parsePPSEP28hevc_picture_parameter_set_tP29hevc_sequence_parameter_set_t.cold.9
+ __ZN9HEVC_RBSP8parseSPSEP26hevc_video_parameter_set_tP29hevc_sequence_parameter_set_tii.cold.1
+ __ZN9HEVC_RBSP8parseSPSEP26hevc_video_parameter_set_tP29hevc_sequence_parameter_set_tii.cold.2
+ __ZN9HEVC_RBSP8parseSPSEP26hevc_video_parameter_set_tP29hevc_sequence_parameter_set_tii.cold.3
+ __ZN9HEVC_RBSP8parseSPSEP26hevc_video_parameter_set_tP29hevc_sequence_parameter_set_tii.cold.4
+ __ZN9HEVC_RBSP8parseSPSEP26hevc_video_parameter_set_tP29hevc_sequence_parameter_set_tii.cold.5
+ __ZN9HEVC_RBSP8parseSPSEP26hevc_video_parameter_set_tP29hevc_sequence_parameter_set_tii.cold.6
+ __ZN9HEVC_RBSP8parseSPSEP26hevc_video_parameter_set_tP29hevc_sequence_parameter_set_tii.cold.7
+ __ZN9HEVC_RBSP8parseVPSEP26hevc_video_parameter_set_tib.cold.1
+ __ZTI18CAHDecDandelionAvc
+ __ZTI18CAHDecDandelionAvx
+ __ZTI18CAHDecDandelionLgh
+ __ZTI19CAHDecDandelionHevc
+ __ZTS18CAHDecDandelionAvc
+ __ZTS18CAHDecDandelionAvx
+ __ZTS18CAHDecDandelionLgh
+ __ZTS19CAHDecDandelionHevc
+ __ZTV18CAHDecDandelionAvc
+ __ZTV18CAHDecDandelionAvx
+ __ZTV18CAHDecDandelionLgh
+ __ZTV19CAHDecDandelionHevc
+ __os_log_error_impl
+ _createQualityOfServiceTier.cold.1
+ _getBitDepthsAndChromaFormatFromFormatDesc.cold.1
+ _getDecoderSuperFrameOffsetInfo.cold.1
+ _getDecoderSuperFrameOffsetInfo.cold.2
+ _getIOSurfaceCompressionType.cold.1
+ _getMultiViewLayerOffsetInfo.cold.1
+ _getMultiViewLayerOffsetInfo.cold.2
+ _h264_createFrameTypesArrayElement.cold.1
+ _h264_createSupportedPropertyDictionary.cold.1
+ _h264_createSupportedPropertyDictionary.cold.2
+ _h264_createSupportedPropertyDictionary.cold.3
+ _h264_createSupportedPropertyDictionary.cold.4
+ _hevc_createSupportedPropertyDictionary.cold.1
+ _hevc_createSupportedPropertyDictionary.cold.2
+ _kVTDecompressionPropertyKey_ClientPID
+ _myCreateSuggestedQualityOfServiceTiers.cold.1
+ _parseAvcSps.cold.1
+ _parseAvcSps.cold.2
+ _parseAvcSps.cold.3
+ _parseAvcSps.cold.4
+ _parseAvcSps.cold.5
+ _parseAvcSps.cold.6
+ _parseHevcSps.cold.1
+ _parseHevcSps.cold.10
+ _parseHevcSps.cold.2
+ _parseHevcSps.cold.3
+ _parseHevcSps.cold.4
+ _parseHevcSps.cold.5
+ _parseHevcSps.cold.6
+ _parseHevcSps.cold.7
+ _parseHevcSps.cold.8
+ _parseHevcSps.cold.9
+ _pthread_threadid_np
+ _registerDecoder.cold.1
- _AppleAVDWrapperFghrnDecoderCleanUpMVAV1Resources
- _CFDataCreate
- _FigHEVCBridge_HLSfMP4ParsingInfoDestroy
- __ZL16Default_Skip_Cdf
- __ZL18Default_Tx_8x8_Cdf
- __ZL20Default_Drl_Mode_Cdf
- __ZL20Default_Tx_16x16_Cdf
- __ZL20Default_Tx_32x32_Cdf
- __ZL20Default_Tx_64x64_Cdf
- __ZL21Default_Skip_Mode_Cdf
- __ZL23Default_Inter_Intra_Cdf
- __ZL32Default_Segment_Id_Predicted_Cdf
- __ZN10BufferPool14initBufferPoolEPvP19__CVPixelBufferPooliiii
- __ZN16AVDFrameReceiver9FrameDoneEPviPyi
- __ZN6CAHDec14getDecBufIndexEv
CStrings:
+ "%Y-%m-%d %H:%M:%S"
+ "/Library/Caches/com.apple.xbs/A30A585E-04BF-43D1-A564-8C4BEA216D97/TemporaryDirectory.4xfxLW/Sources/AppleAVD/framework/AppleAVDFrameReceiver.cpp"
+ "00:16:35"
+ "00:16:36"
+ "AVDFrameReceiver ERROR: numArgs invalid.\n"
+ "AVDFrameReceiverEntry"
+ "AppleAVD: ERROR: %{public}s():  Display index out of range (%d)\n"
+ "AppleAVD: ERROR: %{public}s(): %d %d %d %d - errorStatus %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): **mismatch** lh %d ml %d mls %d ex %d *new* lh %d ml %d mls %d ex %d\n"
+ "AppleAVD: ERROR: %{public}s(): **mismatch** lid %d vpslid %d lid %d vpslid %d\n"
+ "AppleAVD: ERROR: %{public}s(): **mismatch** vpser %d w %d h %d ctb %d cf %d ybd %d cbd %d nSz %d DpbSz %d vRange %u **new** w %d h %d ctb %d cf %d ybd %d cbd %d nSz %d DpbSz %d vRange %u\n"
+ "AppleAVD: ERROR: %{public}s(): -- DPB is full auIndex %d\n"
+ "AppleAVD: ERROR: %{public}s(): -- DPB is full numAus %d auIndex %d\n"
+ "AppleAVD: ERROR: %{public}s(): -- emptyLayer out of range\n"
+ "AppleAVD: ERROR: %{public}s(): -- m_numActiveAccessUnits out of range %d\n"
+ "AppleAVD: ERROR: %{public}s(): -- recover from error in KeyFrame -- slice[%4d].naluTupe = %d\n"
+ "AppleAVD: ERROR: %{public}s(): AVC decoder kVAGetVRAHDRBuff tag unsupported!\n"
+ "AppleAVD: ERROR: %{public}s(): AVC decoder kVASetVRAHDRBuff tag unsupported!\n"
+ "AppleAVD: ERROR: %{public}s(): AVC pps.num_slice_groups_minus1 = %d (shall be 0)\n"
+ "AppleAVD: ERROR: %{public}s(): AVC sps.frame_mbs_only_flag = %d (shall be 1)\n"
+ "AppleAVD: ERROR: %{public}s(): AVC sps.level_idc = %d (max is %d)\n\n"
+ "AppleAVD: ERROR: %{public}s(): AVC sps[%d] width %d height %d over size\n"
+ "AppleAVD: ERROR: %{public}s(): AVCSupported is not CFNumberType!\n\n"
+ "AppleAVD: ERROR: %{public}s(): AVC_Decoder::ParseHeader unsupported naluLengthSize \n"
+ "AppleAVD: ERROR: %{public}s(): AVD decoder null\n\n"
+ "AppleAVD: ERROR: %{public}s(): AVDFrameReceiver ERROR: receiver->Setup failed.\n"
+ "AppleAVD: ERROR: %{public}s(): AVDFrameReceiver ERROR: runLoopRef NULL\n\n"
+ "AppleAVD: ERROR: %{public}s(): Allocating new AppleAVDCommandBuilder failed\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD Foghorn codec registration FAILED\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD H264 codec registration FAILED\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD HEVC codec registration FAILED. CheckPlatform 0x%llx\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD Leghorn codec registration FAILED\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD::RVRAScaler returned error:%d \n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD::scaleOutputFrame unlockSurface Dest returned error %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD::scaleOutputFrame unlockSurface Src returned error %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD::scaleOutputFrame unlockSurface returned error %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDCheckPlatform() returned error %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDCreateDecodeDeviceInternal failed: %d\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDDecodeFrameInternal failed\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDDecodeFrameResponse kVASetSkipToNextIDR error: %d\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDDecodeFrameResponse() failed - decryptError: %d \n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDGetParameter [kAppleAVDGetCompressedPictureBuffer] failed with %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDGetParameter call for kAppleAVDGetFrameReceiverThreadPriority returned ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDOpenConnection - CreateAVDFrameReceiver failed %x\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter [kAppleAVDSetTileCVPixelBufRefDecode] failed with %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter call for kAppleAVDEnableIOFence returned ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter call for kAppleAVDEnableRVRA returned ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter call for kAppleAVDExtraInloopFilter returned ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter call for kAppleAVDSetAttachQPs returned ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter call for kAppleAVDSetAv1FilmGrainMode returned ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter call for kAppleAVDSetMVHEVCDisplayLayerIDs returned ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter call for kAppleAVDSetUsageMode returned ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter call for kAppleAVDSetVRADimensions returned ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter call for kAppleAVDSetVRAType returned ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter kAppleAVDSetEnableMuxedAlpha returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter:kAppleAVDSetTileCVPixelBufPostProcess failed\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter:kAppleAVDSetTileCVPixelBufRefDecode failed\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSubmitDecodeCMD failed: %d \n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDUserClient::createDecoder kVASetUsageMode error: %d \n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDWrapperFghrnDecoderDecodeFrame - ERROR! storage is NULL\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDWrapperH264DecoderDecodeFrame - AppleAVDSetParameter kAppleAVDEnableIOFence returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDWrapperH264DecoderDecodeFrame - AppleAVDSetParameter kAppleAVDSetUsageMode or kAppleAVDEnableRVRA returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDWrapperH264DecoderDecodeFrame - ERROR! storage is NULL\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDWrapperH264DecoderDecodeFrameWithOptions - ERROR! storage is NULL\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDWrapperH264DecoderDecodeTile - ERROR! storage is NULL\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDWrapperHEVCDecoderDecodeFrame - ERROR! storage is NULL\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDWrapperHEVCDecoderDecodeFrameWithOptions - ERROR! storage is NULL\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDWrapperHEVCDecoderDecodeTile - ERROR! storage is NULL\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDWrapperLghrnDecoderDecodeFrame - ERROR! storage is NULL\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghVideoDecoder ERROR: kAppleAVDMemCacheMode set failed\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghVideoDecoder_DecodeFrame ERROR: framenum %d decryptError %x\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghVideoDecoder_DecodeFrame ERROR: framenum %d kVTVideoDecoderMalfunctionErr\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghVideoDecoder_DecodeTile ERROR: framenum %d kVTVideoDecoderMalfunctionErr\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghrnDecoder - AppleAVDDeviceType returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghrnDecoder - ERROR closing connection\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghrnDecoder - ERROR setting parameter kAppleAVDPostEmitCleanUpCallBack\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghrnDecoder - ERROR setting parameter kAppleAVDSetParavirtualizedSession\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghrnDecoder - ERROR terminate decoder\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghrnDecoder ERROR: kAppleAVDGetSequenceParams : Could not get Params\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghrnVideoDecoder ERROR, there's no frame to decode\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghrnVideoDecoder ERROR: AppleAVDInitializeDecoder : init decoder device\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghrnVideoDecoder ERROR: Slice Offset = %d < %d is invalid\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghrnVideoDecoder ERROR: Unsupported picture size!\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghrnVideoDecoder ERROR: createAppleAVDHW_FghrnDecoderInstance returned error\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_H264Decoder - AppleAVDSetParameter kAppleAVDEnableRVRA returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_H264Decoder - ERROR closing connection\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_H264Decoder - ERROR setting parameter kAppleAVDPostEmitCleanUpCallBack\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_H264Decoder - ERROR setting parameter kAppleAVDSetParavirtualizedSession\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_H264Decoder - ERROR terminate decoder\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_H264VideoDecoder - AppleAVDSetParameter kAppleAVDHandleCRAFrameAsBLA returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_H264VideoDecoder - AppleAVDSetParameter kAppleAVDSetVRAType: Unsupported VRA Type 2\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_H264VideoDecoder ERROR: AppleAVDSetSPSWidthHeight : Could not set SetSPSWidthHeight\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_H264VideoDecoder ERROR: BAD encryptedSliceCount %d MAX_SLICES %d\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_H264VideoDecoder ERROR: SeqAndPicParamSetFromImageDescExt returned error\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_H264VideoDecoder ERROR: Unsupported picture size!\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_H264VideoDecoder ERROR: createAppleAVDHW_H264DecoderInstance returned error\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_H264VideoDecoder ERROR: kAppleAVDMemCacheMode set failed\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_H264VideoDecoder ERROR: kAppleAVDSetTryEveryFrame set failed\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_H264VideoDecoder_DecodeFrame ERROR: framenum %d decryptError %x\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_H264VideoDecoder_DecodeFrame ERROR: framenum %d kVTVideoDecoderMalfunctionErr\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - AppleAVDDeviceType returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDEnableRVRA returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDExtraInloopFilter returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDHandleCRAFrameAsBLA returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDMultiViewDecodeClient returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDSetEnableMuxedAlpha returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDSetMuxedAlphaStartingPlaneOffset returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDSetTaggedBufGroupArray returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDSetUsageMode or kAppleAVDEnableRVRA returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDSetVRAType: Unsupported VRA Type:%d\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - ERROR closing connection\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - ERROR opening kernel connection\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - ERROR setting parameter kAppleAVDDisplayCallBack\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - ERROR setting parameter kAppleAVDFIGUserRefCon\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - ERROR setting parameter kAppleAVDPostEmitCleanUpCallBack\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - ERROR setting parameter kAppleAVDSetOutputFileName\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - ERROR setting parameter kAppleAVDSetParavirtualizedSession\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - ERROR setting parameter kAppleAVDSetUsageMode\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder - ERROR terminate decoder\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder ERROR: AppleAVDInitializeDecoder : init decoder device\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder ERROR: Unsupported picture size!\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder ERROR: kAppleAVDGetNumLayersMultiViewClient : Could not get Params\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder ERROR: kAppleAVDGetSequenceParams : Could not get Params\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder: Cannot use type of %p %p\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCDecoder: cannot convert number %p %p\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCTileDecoder_DecodeFrame ERROR: framenum %d kVTVideoDecoderMalfunctionErr\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder ERROR: AppleAVDSetParameter:kAppleAVDSetTileCVPixelBufRefDecode failed\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder ERROR: AppleAVDSetSPSWidthHeight : Could not set SetSPSWidthHeight\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder ERROR: BAD encryptedSliceCount %zd MAX_SLICES %d\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder ERROR: CVPixelBufferCreate failed\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder ERROR: Could not get bitstream buffer\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder ERROR: Could not get getMultiViewLayerOffsetInfo\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder ERROR: CreateAVDHEVCInstance returned error\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder ERROR: CreateDispPixelBufferAttributesDictionary failed\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder ERROR: CreatePixelBufferAttributesDictionary failed\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder ERROR: kAppleAVDMemCacheMode set failed\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder ERROR: kAppleAVDSetNoSecondWrite: Could not set NoSecondWrite Flag!\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder ERROR: kAppleAVDSetTryEveryFrame set failed\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder Error:: CFDictionaryCreate (sHEVCVideoDecoderSupportedPropertyDictionary) failed\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder Error:: CFDictionaryCreate - HEVCVideoDecoder_CopySupportedPropertyDictionary- failed.\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder_DecodeFrame ERROR: framenum %d decryptError %x\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_HEVCVideoDecoder_DecodeFrame ERROR: framenum %d kVTVideoDecoderMalfunctionErr\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_LghVideoDecoder ERROR: BAD encryptedSliceCount %ld MAX_SLICES %d\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_LghVideoDecoder ERROR: kAppleAVDMemCacheMode set failed\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_LghVideoDecoder_DecodeFrame ERROR: framenum %d decryptError %x\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_LghVideoDecoder_DecodeFrame ERROR: framenum %d kVTVideoDecoderMalfunctionErr\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_LghrnDecoder - ERROR closing connection\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_LghrnDecoder - ERROR setting parameter kAppleAVDPostEmitCleanUpCallBack\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_LghrnDecoder - ERROR setting parameter kAppleAVDSetParavirtualizedSession\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_LghrnDecoder - ERROR terminate decoder\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_LghrnVideoDecoder ERROR: Unsupported picture size!\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_LghrnVideoDecoder ERROR: createAppleAVDHW_LghrnDecoderInstance returned error\n"
+ "AppleAVD: ERROR: %{public}s(): Asking fig to drop frame # %d with err %d - internalStatus: %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): B slice - reflist 0 has ref pics with non-unique POC\n\n"
+ "AppleAVD: ERROR: %{public}s(): B slice - reflist 1 has ref pics with non-unique POC\n\n"
+ "AppleAVD: ERROR: %{public}s(): Bad Bitstream! first_slice_segment_in_pic_flag NOT set on slice_count: %d\n"
+ "AppleAVD: ERROR: %{public}s(): Bad Bitstream! first_slice_segment_in_pic_flag set on slice_count: %d\n"
+ "AppleAVD: ERROR: %{public}s(): Bad Bitstream, failed with %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): Bad Bitstream, is_sf_frame = %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): Bad input size %d > allocated size (%d)\n"
+ "AppleAVD: ERROR: %{public}s(): BufferPool::shallowCloneBuffer:(%p) index = %u is invalid!\n"
+ "AppleAVD: ERROR: %{public}s(): CAVDAvcDecoder::DecodeGetRenderTargetRef rvra scaler backup buffers are not allocated!\n"
+ "AppleAVD: ERROR: %{public}s(): CAVDAvcDecoder::DecodeGetRenderTargetRef rvra scaler buffers are not allocated!\n"
+ "AppleAVD: ERROR: %{public}s(): CAVDHevcDecoder::DecodeGetRenderTargetRef rvra scaler backup buffers are not allocated!\n"
+ "AppleAVD: ERROR: %{public}s(): CAVDHevcDecoder::DecodeGetRenderTargetRef rvra scaler buffers are not allocated!\n"
+ "AppleAVD: ERROR: %{public}s(): CAVDMvHevcDecoder: Not supported!\n"
+ "AppleAVD: ERROR: %{public}s(): CVPixelBufferCreate failed\n"
+ "AppleAVD: ERROR: %{public}s(): CVPixelBufferCreate failed refSurfaceListIndx:%d\n"
+ "AppleAVD: ERROR: %{public}s(): CVPixelBufferCreate failed with %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): Calling processFrameDone()!\n"
+ "AppleAVD: ERROR: %{public}s(): Cannot find LongTermPicNumLX %d in refList[%d][%d] and beyond\n"
+ "AppleAVD: ERROR: %{public}s(): Cannot find picNumLX %d for refList[%d][%d]\n"
+ "AppleAVD: ERROR: %{public}s(): Cannot initialize condition variable, Error = %d\n"
+ "AppleAVD: ERROR: %{public}s(): Cannot initialize mutex, Error = %d\n"
+ "AppleAVD: ERROR: %{public}s(): Could not retrieve support bits from CFNumberRef!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Couldn't get AVCSupported property from IORegistry!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Couldn't get memInfo (NULL)! currBufIndex: %d\n"
+ "AppleAVD: ERROR: %{public}s(): Couldn't get memInfo (NULL)! refBufIndex: %d - i: %d\n"
+ "AppleAVD: ERROR: %{public}s(): Create CPBManager Failed\n"
+ "AppleAVD: ERROR: %{public}s(): Create layersErrorStatus Failed\n"
+ "AppleAVD: ERROR: %{public}s(): CreateAVDFghrnInstance ERROR: kAppleAVDSetTryEveryFrame set failed\n"
+ "AppleAVD: ERROR: %{public}s(): CreateAVDFghrnInstance returned error\n"
+ "AppleAVD: ERROR: %{public}s(): CreateAVDLghrnInstance ERROR: kAppleAVDSetTryEveryFrame set failed\n"
+ "AppleAVD: ERROR: %{public}s(): CreateDispPixelBufferAttributesDictionary failed\n"
+ "AppleAVD: ERROR: %{public}s(): CreatePixelBufferAttributesDictionary failed\n"
+ "AppleAVD: ERROR: %{public}s(): CreateUncompressedPixelBufferAttributesDictionaryRVRA() failed!\n"
+ "AppleAVD: ERROR: %{public}s(): CryptorSubsampleAuxiliaryData is NULL\n"
+ "AppleAVD: ERROR: %{public}s(): Decode buffer is NULL!\n"
+ "AppleAVD: ERROR: %{public}s(): DecodePicture fail\n"
+ "AppleAVD: ERROR: %{public}s(): ERROR failed to set kAppleAVDSetSliceHeaderThreshold to %d\n"
+ "AppleAVD: ERROR: %{public}s(): ERROR refCount is already 0!!\n"
+ "AppleAVD: ERROR: %{public}s(): ERROR setting kAppleAVDSetAVDCoreControlPerfWeight failed\n"
+ "AppleAVD: ERROR: %{public}s(): ERROR setting kAppleAVDSetAVDCoreSelect failed\n"
+ "AppleAVD: ERROR: %{public}s(): ERROR setting kAppleAVDSetAllowBitstreamToChangeFrameDimensions failed\n"
+ "AppleAVD: ERROR: %{public}s(): ERROR setting kAppleAVDSetAv1FilmGrainMode failed\n"
+ "AppleAVD: ERROR: %{public}s(): ERROR setting kAppleAVDSetCPBCacheBufferSizeFactor failed\n"
+ "AppleAVD: ERROR: %{public}s(): ERROR setting kAppleAVDSetCPBCacheNumBuffers failed\n"
+ "AppleAVD: ERROR: %{public}s(): ERROR setting kAppleAVDSetMiscPreferences failed\n"
+ "AppleAVD: ERROR: %{public}s(): ERROR setting kAppleAVDSetMsrRef failed\n"
+ "AppleAVD: ERROR: %{public}s(): ERROR setting kAppleAVDSetMultiVPParsing failed\n"
+ "AppleAVD: ERROR: %{public}s(): ERROR setting kAppleAVDSetOnDemandDVAMap failed\n"
+ "AppleAVD: ERROR: %{public}s(): ERROR setting kAppleAVDSetSkipVPSExtParsing failed\n"
+ "AppleAVD: ERROR: %{public}s(): ERROR!!!\n"
+ "AppleAVD: ERROR: %{public}s(): Error (0x%x) creating IOSurfaceAccelerator client.\n"
+ "AppleAVD: ERROR: %{public}s(): Error allocating CPBManager cache\n"
+ "AppleAVD: ERROR: %{public}s(): Error allocating patch requests list, m_fwPatchRequests=%p, m_fwPatchRequestWriteIndex=%u, m_maxFwPatchRequests=%u\n"
+ "AppleAVD: ERROR: %{public}s(): Error allocating temp buffer for RVRAInLoopChromaFilter() \n\n"
+ "AppleAVD: ERROR: %{public}s(): Error creating LGH parser!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Error deallocating patch requests list\n"
+ "AppleAVD: ERROR: %{public}s(): Error deallocating patch requests list, m_fwPatchRequests=%p, m_fwPatchRequestWriteIndex=%u, m_maxFwPatchRequests=%u\n"
+ "AppleAVD: ERROR: %{public}s(): Error getting chroma scratch buffer!\n"
+ "AppleAVD: ERROR: %{public}s(): Error getting decoder buffer!\n"
+ "AppleAVD: ERROR: %{public}s(): Error getting display buffer!\n"
+ "AppleAVD: ERROR: %{public}s(): Error getting second decoder buffer for scaling! (frameNum :%d)\n"
+ "AppleAVD: ERROR: %{public}s(): Error initializing m_bf_cond condition variable\n"
+ "AppleAVD: ERROR: %{public}s(): Error initializing mutex\n"
+ "AppleAVD: ERROR: %{public}s(): Error: list-0 slice(%2d) RefIdx[%2d] not found in %d ref_pics!!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Error: list-1 slice(%2d) RefIdx[%2d] not found in %d ref_pics!!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Exceeded buffers to release (%d)\n"
+ "AppleAVD: ERROR: %{public}s(): FGHDecoder ERROR: ConfigRecordData error - Cannot find config record\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to Create Pixel Buffer Pool! ERROR! CVReturnStatus: 0x%x\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to add %s %s buffer to patch list\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to allocate buffers!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to allocate m_decodeBufferMemInfo! Got %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to allocate members (error = %u)!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to copy data bytes (err = %d), nothing to decode\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to create HW Decoder object!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to create RLM\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to create compressed pixel buffer attributes dictionary! ERROR! Status: 0x%x\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to create display pixel buffer attributes dictionary! ERROR! Status: 0x%x\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to create histogram stat buffer! status: 0x%x\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to create pixel buffer! error: 0x%x\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to create reference pixel buffer attributes dictionary! ERROR! Status: 0x%x\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to create rlm!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to decode frame - status (%d)\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to destroy histogram stat buffer! status: 0x%x\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to get IOSurfaceRef!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to get slice data memInfo struct (slice %d)\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to initialize HW Decoder object!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to map pixel buffer! - error: 0x%x\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to properly convert Pixel Buffer Format CFNumber to an integer!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to retrieve data buffer from sampleBuffer\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to retrieve kVTDecompressionResolutionKey_Height from dictionary\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to retrieve kVTDecompressionResolutionKey_Width from dictionary\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to set HandleCRAFrameAsBLA parameter - status %d handleCRAFrameAsBLA %d\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to set parameter kVASetDisableSkipToIDR - status %d\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to set parameter kVASetEnableRVRA - status %d\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to set parameter kVASetMuxedAlphaParams - status %d\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to set parameter kVASetTileDecodeParams - status %d\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to set parameter kVASetVRATypeAndDimensions - status %d\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to set parameter kVASetYUVMD5Hash - status %d\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to set parameter! ERROR! Status: 0x%x\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to set usage mode parameter - status %d usageMode %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed to successfully retrieve support bits! (error = %d)\n\n"
+ "AppleAVD: ERROR: %{public}s(): Failed with error = %d\n"
+ "AppleAVD: ERROR: %{public}s(): FigBlockBufferCopyDataBytes failed with %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): FigCPECryptorCreateProcessedBlockBufferAndSubsampleAuxiliaryDataWithOptions returned error %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): FigDerivedObjectCreate failed\n"
+ "AppleAVD: ERROR: %{public}s(): Forcing panic due to SW timeout.\n\n"
+ "AppleAVD: ERROR: %{public}s(): Frame resolution below minimum supported %ux%u\n\n"
+ "AppleAVD: ERROR: %{public}s(): Frame# %d DecodeFrame failed with error 0x%08x\n\n"
+ "AppleAVD: ERROR: %{public}s(): Frame# %d, DecodeFrame failed with decryptError: %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): H3H264VideoDecoder FIG: Cannot use type of %p %p\n"
+ "AppleAVD: ERROR: %{public}s(): H3H264VideoDecoder FIG: cannot convert number %p %p\n"
+ "AppleAVD: ERROR: %{public}s(): HEVC decoder kVASetVRAHDRBuff tag unsupported for USP!\n"
+ "AppleAVD: ERROR: %{public}s(): HEVC pOrigRef is NULL!\n"
+ "AppleAVD: ERROR: %{public}s(): HEVC pScaledRef is NULL!\n"
+ "AppleAVD: ERROR: %{public}s(): HEVCDecoder ERROR: ConfigRecordData error - Cannot find config record\n"
+ "AppleAVD: ERROR: %{public}s(): HW Decoder failed to allocate decodeBuffer!\n\n"
+ "AppleAVD: ERROR: %{public}s(): IOIteratorNext failed!\n\n"
+ "AppleAVD: ERROR: %{public}s(): IOMainPort failed! (error = %d)\n\n"
+ "AppleAVD: ERROR: %{public}s(): IOServiceGetMatchingServices failed! (error = %d)\n\n"
+ "AppleAVD: ERROR: %{public}s(): IOServiceOpen failed %x\n"
+ "AppleAVD: ERROR: %{public}s(): IOSurface is too small for detiling (plane %d) - detiled dimensions: [%d x %d], IOSurface: [%zu x %zu]\n\n"
+ "AppleAVD: ERROR: %{public}s(): IOSurface is too small for tiling (plane %d): detiled dimensions - [%d x %d], IOSurface: [%zu x %zu]\n\n"
+ "AppleAVD: ERROR: %{public}s(): IOSurfaceGetDataProperty returned error (0x%x). Line = %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): IOSurfaceSetBulkAttachments2 returned error (0x%x)\n\n"
+ "AppleAVD: ERROR: %{public}s(): IOSurfaceSetDataProperty returned error (0x%x). Line = %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): Initialization of decoder object failed with %u\n\n"
+ "AppleAVD: ERROR: %{public}s(): Invalid AVD device type %d!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Invalid VRA Dimensions - w:%d h:%d\n"
+ "AppleAVD: ERROR: %{public}s(): Invalid dispbufIndex=%u or ctx->pBufferPool[poolIndex=%u] is NULL!, ctx->noSecondWrite %d\n"
+ "AppleAVD: ERROR: %{public}s(): Invalid parameter(s) m_p_cv_pool: %p - vtSession: %p - vtFrame: %p\n"
+ "AppleAVD: ERROR: %{public}s(): Invalid reference index (%d)\n"
+ "AppleAVD: ERROR: %{public}s(): LGH frame header parsing error !\n"
+ "AppleAVD: ERROR: %{public}s(): LGHDecoder ERROR: ConfigRecordData error - Cannot find config record\n"
+ "AppleAVD: ERROR: %{public}s(): Large Scale Tile decoding is not supported!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Line %d: %s mismatch b/w %s %d and %s %d\n"
+ "AppleAVD: ERROR: %{public}s(): Line %d: Error allocating %s\n"
+ "AppleAVD: ERROR: %{public}s(): Line %d: RNG_CHECK failed for %s x %d low %d up %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): MMC 1: Cannot find picNumX %d CurrPicNum %d difference_of_pic_nums_minus1 %d\n"
+ "AppleAVD: ERROR: %{public}s(): MMC 2: Cannot find LongTermPicNum %d\n"
+ "AppleAVD: ERROR: %{public}s(): MMC 3: Cannot find picNumX %d CurrPicNum %d difference_of_pic_nums_minus1 %d\n"
+ "AppleAVD: ERROR: %{public}s(): MUXED_ALPHA_CHROMA_SCRATCH_BUFF_INDEX map failed error: %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): NALU bad size! %d\n"
+ "AppleAVD: ERROR: %{public}s(): NALU too big! %d nal_ptr:%p, buf_end:%p\n"
+ "AppleAVD: ERROR: %{public}s(): NALU too big! %d nal_ptr:%p, buf_end:%p; dataLength: %8d\n"
+ "AppleAVD: ERROR: %{public}s(): NULL arguments - in (%p) out (%p)\n"
+ "AppleAVD: ERROR: %{public}s(): NULL context!\n\n"
+ "AppleAVD: ERROR: %{public}s(): NULL decoder\n"
+ "AppleAVD: ERROR: %{public}s(): NULL decoder! (%p)\n"
+ "AppleAVD: ERROR: %{public}s(): NULL sampleBuffer from the context!\n\n"
+ "AppleAVD: ERROR: %{public}s(): NULL uncompressed header!\n\n"
+ "AppleAVD: ERROR: %{public}s(): No non-existing ref frames found!\n\n"
+ "AppleAVD: ERROR: %{public}s(): No ref pics found!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Non-mod16 VRA dimensions with width %d, height %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): PS range check failed!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Parameter Set missing %d\n"
+ "AppleAVD: ERROR: %{public}s(): Parameter Set missing %d %d\n"
+ "AppleAVD: ERROR: %{public}s(): Parameter Set missing %d %d %d\n"
+ "AppleAVD: ERROR: %{public}s(): Parser av1_get_next_frame() function return fail!\n\n"
+ "AppleAVD: ERROR: %{public}s(): RASL picture %d with no associated IRAP picture\n"
+ "AppleAVD: ERROR: %{public}s(): RVRAInLoopChromaFilter() failed! \n\n"
+ "AppleAVD: ERROR: %{public}s(): RVRA_FIRST_BACKUP_BUFF_INDEX map failed: %d \n\n"
+ "AppleAVD: ERROR: %{public}s(): RVRA_SECOND_BACKUP_BUFF_INDEX map failed: %d \n\n"
+ "AppleAVD: ERROR: %{public}s(): RefIndex %d > ref_pics %d\n"
+ "AppleAVD: ERROR: %{public}s(): Registration for %c%c%c%c failed with status %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): Rejecting non-IDR frame in tiled decode %d\n"
+ "AppleAVD: ERROR: %{public}s(): Rejecting non-IRAP frame in tiled decode %d\n"
+ "AppleAVD: ERROR: %{public}s(): RenderSurfaceRefList NULL!! dispBufIndex: %d\n"
+ "AppleAVD: ERROR: %{public}s(): RequestedMVHEVCVideoLayerIDs not set ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): Retrieved kCVPixelBufferPixelFormatTypeKey entry was not a CFNumber or CFArray!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Scaler returned error (0x%x) for the transform.\n\n"
+ "AppleAVD: ERROR: %{public}s(): SurfaceRefList NULL!! refBufIndex: %d\n"
+ "AppleAVD: ERROR: %{public}s(): Sync Decode not enabled for FT chroma deblocking filter\n\n"
+ "AppleAVD: ERROR: %{public}s(): Timed out, waited at least %llums for frameNum %d! m_num_CPBs_on_the_fly=%u timeoutMS=%llu\n"
+ "AppleAVD: ERROR: %{public}s(): Trying to allocate a second buffer without the pool being initialized! Error!\n\n"
+ "AppleAVD: ERROR: %{public}s(): Trying to map to an index that already has a mapping\n"
+ "AppleAVD: ERROR: %{public}s(): Unexpected FG attachment size = %zu. Ignoring it.\n\n"
+ "AppleAVD: ERROR: %{public}s(): Unknown eventType %u.\n\n"
+ "AppleAVD: ERROR: %{public}s(): Unrecognized pixel buffer format: %c%c%c%c - defaulting to kIOSurfaceCompressionTypeNone\n\n"
+ "AppleAVD: ERROR: %{public}s(): VAMapPixelBuffer returned fail\n"
+ "AppleAVD: ERROR: %{public}s(): VAStartDecode failed error: %d \n"
+ "AppleAVD: ERROR: %{public}s(): VPS extension missing!\n\n"
+ "AppleAVD: ERROR: %{public}s(): VPS parsing error\n"
+ "AppleAVD: ERROR: %{public}s(): VRA illegal size %u %u %u %u\n"
+ "AppleAVD: ERROR: %{public}s(): VT Failed to get Pixel Buffer Pool! ERROR!\n"
+ "AppleAVD: ERROR: %{public}s(): VTDecoderSessionCopyResolvedPixelBufferAttributes failed with %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): WARNING! vm_deallocate failed! status: 0x%x Check for leaks! addr = 0x%llx - roundedUpSize: 0x%x\n"
+ "AppleAVD: ERROR: %{public}s(): WARNING! vm_deallocate failed! status: 0x%x Check for leaks! frameNumber: %d - addr = 0x%llx - roundedUpSize: 0x%x\n"
+ "AppleAVD: ERROR: %{public}s(): WARNING, fail to copy data bytes, nothing to decode\n"
+ "AppleAVD: ERROR: %{public}s(): WriteNAL AVD_HEVC_ERROR_BAD_NAL_LENGTH \n"
+ "AppleAVD: ERROR: %{public}s(): WriteNAL kAVD_DECODER_ERROR_BAD_NAL_LENGTH \n"
+ "AppleAVD: ERROR: %{public}s(): [CAVDAvcDecErr] %s\n"
+ "AppleAVD: ERROR: %{public}s(): [CAVDAvcDecErr] %s %d\n"
+ "AppleAVD: ERROR: %{public}s(): [CAVDAvxDecErr] %s\n"
+ "AppleAVD: ERROR: %{public}s(): [CAVDHevcDecErr] %s\n"
+ "AppleAVD: ERROR: %{public}s(): [CAVDHevcDecoder] m_pps_list mem alloc failed\n"
+ "AppleAVD: ERROR: %{public}s(): [CAVDHevcDecoder] m_slices mem alloc failed\n"
+ "AppleAVD: ERROR: %{public}s(): [CAVDHevcDecoder] m_sps_list mem alloc failed\n"
+ "AppleAVD: ERROR: %{public}s(): [CAVDMvHevcDecErr] %s\n"
+ "AppleAVD: ERROR: %{public}s(): [ERROR] fno: %8d Assign_Cur_Frame_New_FB return NULL\n"
+ "AppleAVD: ERROR: %{public}s(): [layer %d] Failed to allocate m_dec_pb_idx!\n\n"
+ "AppleAVD: ERROR: %{public}s(): [layer %d] Failed to allocate m_disp_pb_idx!\n\n"
+ "AppleAVD: ERROR: %{public}s(): [layer %d] Failed to allocate m_second_dec_pb_idx!\n\n"
+ "AppleAVD: ERROR: %{public}s(): [layer %d] Failed to create HW Decoder object!\n\n"
+ "AppleAVD: ERROR: %{public}s(): [layer %d] Failed to initialize HW Decoder object!\n\n"
+ "AppleAVD: ERROR: %{public}s(): [layer %d] HW Decoder failed to allocate decodeBuffer!\n\n"
+ "AppleAVD: ERROR: %{public}s(): [layer %d] error creating rlm!\n\n"
+ "AppleAVD: ERROR: %{public}s(): [line %u]: Failed to get slice data memInfo struct (slice %d)\n\n"
+ "AppleAVD: ERROR: %{public}s(): allLayersDecodeErr = %d, finalTagBufErr = %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): allocOneCPB error (%d)!\n\n"
+ "AppleAVD: ERROR: %{public}s(): allocateMultiViewHwDecoders failed with %u\n\n"
+ "AppleAVD: ERROR: %{public}s(): avdDec - Frame# %6d, DecodeFrame failed with error: 0x%x \n\n"
+ "AppleAVD: ERROR: %{public}s(): bad IOSurface* in tile offset check\n"
+ "AppleAVD: ERROR: %{public}s(): bad PPS index %d\n"
+ "AppleAVD: ERROR: %{public}s(): bad PPS index %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): bad SPS index %d\n"
+ "AppleAVD: ERROR: %{public}s(): bad SPS index %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): bad header, got error %d parsing header\n\n"
+ "AppleAVD: ERROR: %{public}s(): bad ref list0[%d]\n"
+ "AppleAVD: ERROR: %{public}s(): bad ref list1[%d]\n"
+ "AppleAVD: ERROR: %{public}s(): bad swr bit depth %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): bailing out because start didn't complete\n"
+ "AppleAVD: ERROR: %{public}s(): bit depth %d exceeds allocated depth 0\n\n"
+ "AppleAVD: ERROR: %{public}s(): buff NOT in use! error index %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): buffer map failed error: %d refSurfaceListIndx:%d\n\n"
+ "AppleAVD: ERROR: %{public}s(): calcLayerSetLayerIdList \n"
+ "AppleAVD: ERROR: %{public}s(): calcLumaChromaTileOffset returns fail\n"
+ "AppleAVD: ERROR: %{public}s(): called on plugin in state %d\n"
+ "AppleAVD: ERROR: %{public}s(): cannot find PPS\n"
+ "AppleAVD: ERROR: %{public}s(): cannot find SPS\n"
+ "AppleAVD: ERROR: %{public}s(): cannot initialize cond variable, return error %d [ %s ]\n"
+ "AppleAVD: ERROR: %{public}s(): cannot initialize mutex, return error %d [ %s ]\n"
+ "AppleAVD: ERROR: %{public}s(): caught initPicture error\n"
+ "AppleAVD: ERROR: %{public}s(): chroma compression format %d lossy level %d not supported\n\n"
+ "AppleAVD: ERROR: %{public}s(): clientID : %2d fail to alloc work buffer for pps frame_type %d, frameNum:%d \n\n"
+ "AppleAVD: ERROR: %{public}s(): clientID : %2d fail to alloc work buffer for sps frameNum:%d \n\n"
+ "AppleAVD: ERROR: %{public}s(): clientID : %2d, #### <WARNING> Failed resolution check for frame %u.\n\n"
+ "AppleAVD: ERROR: %{public}s(): clientID: %2d Error getting decoder buffer!, frameNum : %d\n"
+ "AppleAVD: ERROR: %{public}s(): clientID: %2d Error getting display buffer!, frameNum : %d\n"
+ "AppleAVD: ERROR: %{public}s(): clientID: %2d,DecodeError: %d,skipToIDR:%d,frameNum :%d\n"
+ "AppleAVD: ERROR: %{public}s(): clientID: %2d,DecodeError: %d,skipToIDR:%d,frameType: %d,frameNum :%d\n"
+ "AppleAVD: ERROR: %{public}s(): clientID: %2d. For AVIFs, only intra-frames are supported, frameNum : %d\n"
+ "AppleAVD: ERROR: %{public}s(): clientID:%2d LGH, reference list creation - invalid reference frames, frameType :%d, frameNum :%d !\n"
+ "AppleAVD: ERROR: %{public}s(): clientID:%2d, LGH Decoder frameWidth : %d, frameHeight : %d is out of range, frameNum :%d\n"
+ "AppleAVD: ERROR: %{public}s(): clientID:%2d, LGH, unsupported profile : %d !, frameType :%d, frameNum :%d\n"
+ "AppleAVD: ERROR: %{public}s(): closeAppleAVDHW_HEVCDecoderInstance returned error %d\n"
+ "AppleAVD: ERROR: %{public}s(): cmdBuilder->decodeFrameFig returned error: %d \n\n"
+ "AppleAVD: ERROR: %{public}s(): config record is too short\n\n"
+ "AppleAVD: ERROR: %{public}s(): crauxNumEntries %ld out of range\n"
+ "AppleAVD: ERROR: %{public}s(): createDPB fail\n"
+ "AppleAVD: ERROR: %{public}s(): createDecoder() error creating rvra buffers!\n"
+ "AppleAVD: ERROR: %{public}s(): createPixelBufferAttributesDictionary failed with %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): cryptor has NULL createProcessedBlockBufferAndSubsampleAuxiliaryDataWithOptions entry in vTable!\n\n"
+ "AppleAVD: ERROR: %{public}s(): decodeGetRenderTarget returned fail\n"
+ "AppleAVD: ERROR: %{public}s(): decodeGetRenderTargetRef RETURNED ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): decoder buffer is NULL, no frame will be sent to display\n"
+ "AppleAVD: ERROR: %{public}s(): either dataBuffer=%p is invalid or dataLength=%zu is invalid!\n"
+ "AppleAVD: ERROR: %{public}s(): either tile dataBuffer=%p is invalid or dataLength=%u is invalid!\n"
+ "AppleAVD: ERROR: %{public}s(): either tile dataBuffer=%p is invalid or dataLength=%zu is invalid!\n"
+ "AppleAVD: ERROR: %{public}s(): encrypted slices size > MAX_SLICES:%d\n"
+ "AppleAVD: ERROR: %{public}s(): encryptedSliceCount (%d) exceeds MAX_SLICES (%d)\n\n"
+ "AppleAVD: ERROR: %{public}s(): encryptedSliceCount (%ld) exceeds MAX_SLICES (%d)\n\n"
+ "AppleAVD: ERROR: %{public}s(): encryption mode 'eavc' is no longer supported\n\n"
+ "AppleAVD: ERROR: %{public}s(): error %d and decoder is %p\n"
+ "AppleAVD: ERROR: %{public}s(): error allocating surface\n\n"
+ "AppleAVD: ERROR: %{public}s(): error creating parser!\n\n"
+ "AppleAVD: ERROR: %{public}s(): error creating pps list!\n\n"
+ "AppleAVD: ERROR: %{public}s(): error creating rbsp!\n\n"
+ "AppleAVD: ERROR: %{public}s(): error creating rlm!\n\n"
+ "AppleAVD: ERROR: %{public}s(): error creating sps list!\n\n"
+ "AppleAVD: ERROR: %{public}s(): error deallocating AVD surface index %d from pool %u\n\n"
+ "AppleAVD: ERROR: %{public}s(): error index %d \n\n"
+ "AppleAVD: ERROR: %{public}s(): error index %d m_max_cache_size:%d \n\n"
+ "AppleAVD: ERROR: %{public}s(): error null input buffer\n"
+ "AppleAVD: ERROR: %{public}s(): error. Line: %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): fail to activate parameter set for slice\n"
+ "AppleAVD: ERROR: %{public}s(): fail to activate parameter set for slice\n\n"
+ "AppleAVD: ERROR: %{public}s(): fail to alloc work buffer for pps\n\n"
+ "AppleAVD: ERROR: %{public}s(): fail to allocate work buffer for pps\n"
+ "AppleAVD: ERROR: %{public}s(): fail to allocate work buffer for pps\n\n"
+ "AppleAVD: ERROR: %{public}s(): fail to allocate work buffer for sps\n"
+ "AppleAVD: ERROR: %{public}s(): fail to allocate work buffer for sps\n\n"
+ "AppleAVD: ERROR: %{public}s(): fail to copy data bytes\n"
+ "AppleAVD: ERROR: %{public}s(): fail to create reference picture list - result: %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): fail to get SWR stride for the picture\n\n"
+ "AppleAVD: ERROR: %{public}s(): fail to get bitdepth from parsed header\n\n"
+ "AppleAVD: ERROR: %{public}s(): fail to get chroma format idc from parsed header\n\n"
+ "AppleAVD: ERROR: %{public}s(): fail to get delta lf res\n\n"
+ "AppleAVD: ERROR: %{public}s(): fail to get probs info for current frame\n\n"
+ "AppleAVD: ERROR: %{public}s(): fail to get restoration unit size\n\n"
+ "AppleAVD: ERROR: %{public}s(): fail to init picture\n\n"
+ "AppleAVD: ERROR: %{public}s(): fail to parse av1 header\n\n"
+ "AppleAVD: ERROR: %{public}s(): failKind = %d\n"
+ "AppleAVD: ERROR: %{public}s(): failed \n"
+ "AppleAVD: ERROR: %{public}s(): failed \n\n"
+ "AppleAVD: ERROR: %{public}s(): failed - error: %d \n\n"
+ "AppleAVD: ERROR: %{public}s(): failed cmdBuilder->createDecoder!\n\n"
+ "AppleAVD: ERROR: %{public}s(): failed error: %d \n\n"
+ "AppleAVD: ERROR: %{public}s(): failed to allocate %d x4 bytes mem for slice->entry_point_offset_minus1\n"
+ "AppleAVD: ERROR: %{public}s(): failed to change video resolution to %ux%u\n\n"
+ "AppleAVD: ERROR: %{public}s(): failed to get bitdepth from parsed header\n\n"
+ "AppleAVD: ERROR: %{public}s(): failed to get chroma format idc from parsed header\n\n"
+ "AppleAVD: ERROR: %{public}s(): failed with error %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): failed with error %s\n\n"
+ "AppleAVD: ERROR: %{public}s(): fill frame num gap failed!\n\n"
+ "AppleAVD: ERROR: %{public}s(): foreError detected!! frameNumber: %d\n"
+ "AppleAVD: ERROR: %{public}s(): frame size %llu is probably bogus, pBuff=%p pBuffBegin=%p frameStart=%p\n\n"
+ "AppleAVD: ERROR: %{public}s(): frame# %d, AppleAVDSetParameter [kAppleAVDSetCryptRef] failed with %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): frame# %d, AppleAVDSetParameter [kAppleAVDSetCryptScheme] failed with %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): frame# %d, Could not get slice data for decryptor, err %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): frame# %d, Could not set kAppleAVDSetCryptScheme, err %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): frame# %d, FigCPECryptorGetExternalProtectionMethods, err %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): frame# %d, FigCPECryptorGetNativeSession returned err %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): frame# %d, cryptorIV is NULL, err %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): frame# %d, new CVPixelBufferPool created protectionOptions %llu %llu - ioSurfaceType: %d, err: %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): frame# %d, session: %p, decryptor attachment is NULL\n\n"
+ "AppleAVD: ERROR: %{public}s(): frameNum %d dispIndx %d errorStatus %d allLayersDecodeErr %d multiImageDecodeErr %d - multi-image emit displayCallBack callback\n\n"
+ "AppleAVD: ERROR: %{public}s(): frameNum %d failed to get an available buffer after %llums\n\n"
+ "AppleAVD: ERROR: %{public}s(): frame_header_obu: ERROR, cur_frame isn't valid\n\n"
+ "AppleAVD: ERROR: %{public}s(): framenum %d decryptError %x\n\n"
+ "AppleAVD: ERROR: %{public}s(): framenum %d kVTVideoDecoderMalfunctionErr\n\n"
+ "AppleAVD: ERROR: %{public}s(): getHwDecoder error\n"
+ "AppleAVD: ERROR: %{public}s(): got NULL vTable from cryptor object!\n\n"
+ "AppleAVD: ERROR: %{public}s(): hevc - unpermitted non-VCL NAL following last VCL NAL\n\n"
+ "AppleAVD: ERROR: %{public}s(): hwD->DecodePicture return %d\n"
+ "AppleAVD: ERROR: %{public}s(): index %d \n\n"
+ "AppleAVD: ERROR: %{public}s(): infoDict creation failed!\n\n"
+ "AppleAVD: ERROR: %{public}s(): initPicture failed\n\n"
+ "AppleAVD: ERROR: %{public}s(): initializing pixel buffer failed with %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): insertCurPicIntoAuList fail\n"
+ "AppleAVD: ERROR: %{public}s(): invalid VPS id!\n"
+ "AppleAVD: ERROR: %{public}s(): invalid bit depth [luma depth minus 8 = %d, chroma depth minus 8 = %d]\n\n"
+ "AppleAVD: ERROR: %{public}s(): invalid delta lf res %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): invalid dimensions (coded width %d, height %d)\n\n"
+ "AppleAVD: ERROR: %{public}s(): invalid marker bit and/or version number\n\n"
+ "AppleAVD: ERROR: %{public}s(): invalid profile\n\n"
+ "AppleAVD: ERROR: %{public}s(): invalid restoration unit size for Y plane %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): kCVPixelBufferPixelFormatTypeKey was not present in retrieved dictionary\n\n"
+ "AppleAVD: ERROR: %{public}s(): kJVTLibCompressedDataFormat_WrappedNALU_* :: NOT SUPPORTED, storage->naluLengthSize %d\n"
+ "AppleAVD: ERROR: %{public}s(): kVASetMultiVPParsing error: %d \n\n"
+ "AppleAVD: ERROR: %{public}s(): kVASetSliceHeaderThreshold error: %d \n\n"
+ "AppleAVD: ERROR: %{public}s(): kVASetUnlimitedResolution error: %d \n\n"
+ "AppleAVD: ERROR: %{public}s(): kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs error\n"
+ "AppleAVD: ERROR: %{public}s(): layer id not found in vps_layer_id_in_nuh\n"
+ "AppleAVD: ERROR: %{public}s(): layerActive mem alloc failed\n"
+ "AppleAVD: ERROR: %{public}s(): layerID %d > vps_max_layer_id %d!\n\n"
+ "AppleAVD: ERROR: %{public}s(): layers do not match! %d, %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): linear_orig subsampling format is not 4:2:0 (saw %d)\n\n"
+ "AppleAVD: ERROR: %{public}s(): linear_scaled subsampling format is not 4:2:0 (saw %d)\n\n"
+ "AppleAVD: ERROR: %{public}s(): luma compression format %d lossy level %d not supported\n\n"
+ "AppleAVD: ERROR: %{public}s(): m_auList mem alloc failed \n"
+ "AppleAVD: ERROR: %{public}s(): m_av1_header allocation failed\n\n"
+ "AppleAVD: ERROR: %{public}s(): m_curAu layerActive alloc failed\n"
+ "AppleAVD: ERROR: %{public}s(): m_curAu mem alloc failed \n"
+ "AppleAVD: ERROR: %{public}s(): m_cur_pic_info allocation failed\n\n"
+ "AppleAVD: ERROR: %{public}s(): m_dec_bufs allocation failed\n\n"
+ "AppleAVD: ERROR: %{public}s(): m_dec_pb_idx mem alloc failed \n"
+ "AppleAVD: ERROR: %{public}s(): m_dec_q allocation failed\n\n"
+ "AppleAVD: ERROR: %{public}s(): m_disp_pb_idx mem alloc failed \n"
+ "AppleAVD: ERROR: %{public}s(): m_disp_q allocation failed\n\n"
+ "AppleAVD: ERROR: %{public}s(): m_highestTid > vps_max_sub_layers_minus1\n\n"
+ "AppleAVD: ERROR: %{public}s(): m_num_CPBs_on_the_fly:%d == 0. Cannot release further.\n"
+ "AppleAVD: ERROR: %{public}s(): m_out_q allocation failed\n\n"
+ "AppleAVD: ERROR: %{public}s(): m_pps_list mem alloc failed\n\n"
+ "AppleAVD: ERROR: %{public}s(): m_second_dec_pb_idx mem alloc failed \n"
+ "AppleAVD: ERROR: %{public}s(): m_sliceInfo mem alloc failed\n\n"
+ "AppleAVD: ERROR: %{public}s(): m_slices mem alloc failed\n\n"
+ "AppleAVD: ERROR: %{public}s(): m_spsInfo mem alloc failed \n"
+ "AppleAVD: ERROR: %{public}s(): m_sps_list mem alloc failed\n\n"
+ "AppleAVD: ERROR: %{public}s(): max_num_ref_frames %d > dpbSize %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): max_num_ref_frames %d > nMaxDpbSize %d!\n\n"
+ "AppleAVD: ERROR: %{public}s(): mismatch - m_numLayers %d, numLayers %d\n"
+ "AppleAVD: ERROR: %{public}s(): mvhevc - unpermitted non-VCL NAL following last VCL NAL\n\n"
+ "AppleAVD: ERROR: %{public}s(): no instance storage!\n"
+ "AppleAVD: ERROR: %{public}s(): nuh_layer_id > max layer ! %d %d\n"
+ "AppleAVD: ERROR: %{public}s(): numLayersInIdList=%d, vps_ols_2d[%d][%d].vps_output_layer_flag == 0\n\n"
+ "AppleAVD: ERROR: %{public}s(): oversized iv %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): pBufferPool[%d] allocation failed!\n"
+ "AppleAVD: ERROR: %{public}s(): pBufferPool[%d] initBufferPool allocation failed!\n"
+ "AppleAVD: ERROR: %{public}s(): parse NAL error ! %d\n"
+ "AppleAVD: ERROR: %{public}s(): parse PPS error ! %d\n"
+ "AppleAVD: ERROR: %{public}s(): parse SPS error ! %d\n"
+ "AppleAVD: ERROR: %{public}s(): parse VPS error ! %d\n"
+ "AppleAVD: ERROR: %{public}s(): parse av1 header error\n\n"
+ "AppleAVD: ERROR: %{public}s(): parsePpsMultiLayerExtension error\n"
+ "AppleAVD: ERROR: %{public}s(): parsePpsRangeExtension error\n"
+ "AppleAVD: ERROR: %{public}s(): parseShortTermRefPicSet parsing failure\n"
+ "AppleAVD: ERROR: %{public}s(): pic size too large - either width (%d, %d) or height (%d, %d) > max dim. %d and it's 4:2:0, 8 bit, so software decoder can handle it.\n"
+ "AppleAVD: ERROR: %{public}s(): pluginState (%d) was already started! current: %d - requested: %d\n"
+ "AppleAVD: ERROR: %{public}s(): pluginState isn't kPluginCreated, is %d\n"
+ "AppleAVD: ERROR: %{public}s(): pps allocation error\n"
+ "AppleAVD: ERROR: %{public}s(): pps->num_ref_idx_l0_default_active_minus1 > HEVC_MAX_REF_INDEX_FOR_RPL, is %d\n"
+ "AppleAVD: ERROR: %{public}s(): pps->num_ref_idx_l1_default_active_minus1 > HEVC_MAX_REF_INDEX_FOR_RPL, is %d\n"
+ "AppleAVD: ERROR: %{public}s(): processed buffer length (%zu bytes) != sample buffer length (%zu bytes)\n\n"
+ "AppleAVD: ERROR: %{public}s(): protectedRegionOffsets is NULL\n\n"
+ "AppleAVD: ERROR: %{public}s(): protectedRegionSizes is NULL\n\n"
+ "AppleAVD: ERROR: %{public}s(): pthread_cond_timedwait exited with error: %d\n"
+ "AppleAVD: ERROR: %{public}s(): rbsp allocation error\n"
+ "AppleAVD: ERROR: %{public}s(): rbsp parseNAL return error\n"
+ "AppleAVD: ERROR: %{public}s(): rbsp return invalid bitUsed %d nalL_inBits = %d\n"
+ "AppleAVD: ERROR: %{public}s(): ref pic list0[%d] has dimension mismatch\n\n"
+ "AppleAVD: ERROR: %{public}s(): ref pic list1[%d] has dimension mismatch\n\n"
+ "AppleAVD: ERROR: %{public}s(): refList0 size <= num_ref_idx_l0_active_minus1!\n\n"
+ "AppleAVD: ERROR: %{public}s(): refList1 size <= num_ref_idx_l1_active_minus1!\n\n"
+ "AppleAVD: ERROR: %{public}s(): reference marking failed\n\n"
+ "AppleAVD: ERROR: %{public}s(): return with error %d\n"
+ "AppleAVD: ERROR: %{public}s(): saw %d operations without a terminating 0. memory_management_control_operation[%d] = %d\n"
+ "AppleAVD: ERROR: %{public}s(): sending error %d to test app main\n\n"
+ "AppleAVD: ERROR: %{public}s(): setDataProperty failed, error=%d\n\n"
+ "AppleAVD: ERROR: %{public}s(): setDataProperty(AV1FilmGrain) failed, IOSurface look up for ioSurfID 0x%x failed\n\n"
+ "AppleAVD: ERROR: %{public}s(): slice count 0\n"
+ "AppleAVD: ERROR: %{public}s(): slice count for frame is 0\n"
+ "AppleAVD: ERROR: %{public}s(): slice header parsing error - slice_count: %d - nal_unit_type: %d\n"
+ "AppleAVD: ERROR: %{public}s(): sliding window process failed!\n\n"
+ "AppleAVD: ERROR: %{public}s(): sps allocation error\n"
+ "AppleAVD: ERROR: %{public}s(): storage is NULL\n\n"
+ "AppleAVD: ERROR: %{public}s(): threadReady state false. Exiting due to timeout (waitCount=%u of %d sec) or error (=%d)\n"
+ "AppleAVD: ERROR: %{public}s(): tile offset out of bounds! [%d %d] + [%d %d], %d, %u >= %u ?, %u; %u %u %u\n"
+ "AppleAVD: ERROR: %{public}s(): tile offset out of bounds! [%u %u] + [%u %u], %u, %zu >= %zu ?, %u; %u %u %u\n"
+ "AppleAVD: ERROR: %{public}s(): tileX offset not a multiple of 64! tileOffsetX:%d\n"
+ "AppleAVD: ERROR: %{public}s(): tile[%d] width %d, need at least two CTU wide\n"
+ "AppleAVD: ERROR: %{public}s(): tile[%d] width %d, need at least two CTU wide\n\n"
+ "AppleAVD: ERROR: %{public}s(): tile_group_obu returned error.\n\n"
+ "AppleAVD: ERROR: %{public}s(): trying to set kAppleAVDExtraInloopFilter before videoContext was created!\n\n"
+ "AppleAVD: ERROR: %{public}s(): trying to set kAppleAVDSetVRADimensions before videoContext was created!\n\n"
+ "AppleAVD: ERROR: %{public}s(): unsupported chroma format %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): unsupported codec type %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): unsupported profile %d\n\n"
+ "AppleAVD: ERROR: %{public}s(): unsupported resolution, Lgh Codec, width : %d, height : %d \n\n"
+ "AppleAVD: ERROR: %{public}s(): vSurfInfoScalerRef was not set! (frameNum :%d)\n"
+ "AppleAVD: ERROR: %{public}s(): video resolution %ux%u exceeds allocated size %ux%u\n\n"
+ "AppleAVD: ERROR: %{public}s(): vm_allocate failed! allocStatus: %d - addr: 0x%llx\n\n"
+ "AppleAVD: ERROR: %{public}s(): vm_allocate failed! allocStatus: %d - addr: 0x%lx\n\n"
+ "AppleAVD: ERROR: %{public}s(): vps allocation error\n"
+ "AppleAVD: ERROR: %{public}s(): vps base layer %d, available %d\n"
+ "AppleAVD: ERROR: %{public}s(): vps error %d.\n"
+ "AppleAVD: ERROR: %{public}s(): vps->vps_layer_id_in_nuh[i] %d, vps->vps_layer_id_in_nuh[i-1] %d\n"
+ "AppleAVD: ERROR: %{public}s(): vps_view_order_idx >= vps_num_views\n\n"
+ "AppleAVD: ERROR: %{public}s(): vpsext->vps_layer_set_layer_id_list bad alloc \n"
+ "AppleAVD: ERROR: %{public}s(): vpsext->vps_layer_set_layer_id_list[m] bad alloc \n"
+ "AppleAVD: ERROR: %{public}s(): vpsext->vps_layers bad alloc \n"
+ "AppleAVD: ERROR: %{public}s(): vpsext->vps_layers_2d bad alloc \n"
+ "AppleAVD: ERROR: %{public}s(): vpsext->vps_layers_2d[i] bad alloc \n"
+ "AppleAVD: ERROR: %{public}s(): vpsext->vps_num_layers_in_id_list bad alloc \n"
+ "AppleAVD: ERROR: %{public}s(): vpsext->vps_splitting_flag && vpsext->vps_num_scalability_types == 0 \n"
+ "AppleAVD: ERROR: %{public}s(): width (%d) * height (%d) exceeds limit (%llu).\n\n"
+ "AppleAVD: INFO: %{public}s(): \n\n"
+ "AppleAVD: INFO: %{public}s():  %2d\n"
+ "AppleAVD: INFO: %{public}s():  %d %d %d %d %d %d %d %d %d\n\n"
+ "AppleAVD: INFO: %{public}s():  %s - CPBManager created! cacheSize: %d - timeLimit: %llums\n\n"
+ "AppleAVD: INFO: %{public}s():  Compressed buffers disabled! luma depth %d chroma format %d\n"
+ "AppleAVD: INFO: %{public}s():  Compressed buffers enabled! CompressionType:%d. luma depth %d chroma format %d\n"
+ "AppleAVD: INFO: %{public}s(): !frame_refs_short_signaling, ref_frame_idx[%d] = %d\n\n"
+ "AppleAVD: INFO: %{public}s(): #HEVC# storage->memCacheMode = %d\n"
+ "AppleAVD: INFO: %{public}s(): %d: get_bits(%d): %s = %d, m_bits_left %d from buffer: %p\n\n"
+ "AppleAVD: INFO: %{public}s(): 0 byte header size\n\n"
+ "AppleAVD: INFO: %{public}s(): ASSERT @ %s() :: Line %d Assert Broken \n\n"
+ "AppleAVD: INFO: %{public}s(): AV1 Internal bufferpool is full, invalid index %d\n\n"
+ "AppleAVD: INFO: %{public}s(): AVC pOrigRef is NULL!\n"
+ "AppleAVD: INFO: %{public}s(): AVC pScaledRef is NULL!\n"
+ "AppleAVD: INFO: %{public}s(): AVD Fghrn dump: could not open file %s\n\n"
+ "AppleAVD: INFO: %{public}s(): AVD Fghrn dump: could not open property log file %s\n\n"
+ "AppleAVD: INFO: %{public}s(): AVD Lghrn dump: could not open file %s\n\n"
+ "AppleAVD: INFO: %{public}s(): AVD Lghrn dump: could not open property log file %s\n\n"
+ "AppleAVD: INFO: %{public}s(): AVD h264 dump: could not open file %s\n\n"
+ "AppleAVD: INFO: %{public}s(): AVD h264 dump: could not open post DRM file %s\n\n"
+ "AppleAVD: INFO: %{public}s(): AVD h264 dump: could not open pre DRM file %s\n\n"
+ "AppleAVD: INFO: %{public}s(): AVD h264 dump: could not open property log file %s\n\n"
+ "AppleAVD: INFO: %{public}s(): AVD hevc dump: could not open file %s\n\n"
+ "AppleAVD: INFO: %{public}s(): AVD hevc dump: could not open post DRM file %s\n\n"
+ "AppleAVD: INFO: %{public}s(): AVD hevc dump: could not open pre DRM file %s\n\n"
+ "AppleAVD: INFO: %{public}s(): AVD hevc dump: could not open property log file %s\n\n"
+ "AppleAVD: INFO: %{public}s(): AVD hevc histogram dump: could not open file %s\n\n"
+ "AppleAVD: INFO: %{public}s(): After considering defaults write, setting filmGrainMode to: %d\n\n"
+ "AppleAVD: INFO: %{public}s(): Allocating new AppleAVDCommandBuilder\n\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVD Foghorn codec registered\n\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVD H264 codec registered\n\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVD HEVC codec registered. CheckPlatform 0x%llx\n\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVD Leghorn codec registered\n\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVD::scaleOutputFrame unsupported vra type\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVDDecodeFrame - frame # %d metadataDict attached\n\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVDDecodeFrame could not get display buffer from buffer pool\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVDDecodeFrame could not get reference buffer from buffer pool\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVDDecodeFrame could not get scaler buffer from buffer pool\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVDDecodeFrame could not put decode/reference buffer into the buffer pool\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVDDecodeFrame could not put display buffer into the buffer pool\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVDWrapperFghrnDecoderStartSession: storage->miscPreferences %d \n"
+ "AppleAVD: INFO: %{public}s(): AppleAVDWrapperHEVCDecoderCreateInstance - encryptionScheme %d\n\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVDWrapperLghrnDecoderStartSession: storage->miscPreferences %d \n"
+ "AppleAVD: INFO: %{public}s(): AppleAVD_FghrnVideoDecoder  %d %d %d %d %d %d %d %d %d %d %d\n\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVD_H264VideoDecoder: AppleAVDCheckPlatform() returns false. Unusual, but we can proceed assuming AVC L6 is not supported.\n\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVD_H264VideoDecoder: frame# %d, Could not set kAppleAVDSetCryptScheme, err %d\n\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVD_H264VideoDecoder: frame# %d, new CVPixelBufferPool created protectionOptions %llu %llu \n\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVD_HEVCDecoder - setting parameter kAppleAVDMultiViewDecodeClient %d \n"
+ "AppleAVD: INFO: %{public}s(): AppleAVD_HEVCVideoDecoder enableFileDump %d\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVD_HEVCVideoDecoder: frame# %d, Could not set kAppleAVDSetCryptScheme, err %d\n\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVD_HEVCVideoDecoder: frame# %d, new CVPixelBufferPool created protectionOptions %llu %llu \n\n"
+ "AppleAVD: INFO: %{public}s(): AppleAVD_LgrnVideoDecoder: frame# %d, Could not set kAppleAVDSetCryptScheme, err %d\n\n"
+ "AppleAVD: INFO: %{public}s(): Bad NAL type %d\n\n"
+ "AppleAVD: INFO: %{public}s(): Bad NAL type %d. Skipping.\n\n"
+ "AppleAVD: INFO: %{public}s(): Borage AVD is not supported in this AppleAVD driver!!!\n"
+ "AppleAVD: INFO: %{public}s(): BufferPoolId[%d]: Index %d is not in use! in_use: %d\n\n"
+ "AppleAVD: INFO: %{public}s(): CAVDHevcDecoder::VAGetIOSurfaceIDForBufferIndex couldn't resolve index\n\n"
+ "AppleAVD: INFO: %{public}s(): Cactus AVD is not supported in this AppleAVD driver!!!\n"
+ "AppleAVD: INFO: %{public}s(): ChrFmt changed: %d vs %d\n"
+ "AppleAVD: INFO: %{public}s(): ClientPID is zero\n"
+ "AppleAVD: INFO: %{public}s(): Compressed buffers disabled! luma depth %d chroma format %d\n"
+ "AppleAVD: INFO: %{public}s(): Compressed buffers enabled! CompressionType:%d. luma depth %d chroma format %d\n"
+ "AppleAVD: INFO: %{public}s(): Corrupted frame. Inter frame requests nonexistent reference.\n\n"
+ "AppleAVD: INFO: %{public}s(): Corrupted frame. Invalid context_update_tile_id %d \n\n"
+ "AppleAVD: INFO: %{public}s(): Data ended before all tiles were read.\n\n"
+ "AppleAVD: INFO: %{public}s(): Did not find free slot to evict from cache\n"
+ "AppleAVD: INFO: %{public}s(): Disabling decodeToBufferWithAlpha!\n"
+ "AppleAVD: INFO: %{public}s(): ERROR, obu size can't be larger than size of buffer\n\n"
+ "AppleAVD: INFO: %{public}s(): ERROR: layer sets do not match! %d, %d\n\n"
+ "AppleAVD: INFO: %{public}s(): Error: list-0 slice(%2d) RefIdx[%2d] not found in %d ref_pics!!\n\n"
+ "AppleAVD: INFO: %{public}s(): Error: list-1 slice(%2d) RefIdx[%2d] not found in %d ref_pics!!\n\n"
+ "AppleAVD: INFO: %{public}s(): Error: not able to get ivf frame\n\n"
+ "AppleAVD: INFO: %{public}s(): Error: not able to get next obu\n\n"
+ "AppleAVD: INFO: %{public}s(): FOUND IRAP-- SETTING m_skipToIdr FALSE! %d\n"
+ "AppleAVD: INFO: %{public}s(): FeatureFlagIsPWDEnabled: %s FeatureFlagIsHEVCWithAlphaCompressedIOSurfaces: %s MVHEVCAlpha: %s FeatureFlagIsFaceTimeCompressedIOSurfacesEnabled: %s\n"
+ "AppleAVD: INFO: %{public}s(): For OBU_FRAME type obu tile_start_and_end_present_flag must be 0. \n\n"
+ "AppleAVD: INFO: %{public}s(): Forcing panic due to SW timeout.\n\n"
+ "AppleAVD: INFO: %{public}s(): Frame dimensions are larger than the maximum values: width %d height %d\n\n"
+ "AppleAVD: INFO: %{public}s(): FrameReceiver->Emit thread called Invalidate|Finalize!\n"
+ "AppleAVD: INFO: %{public}s(): H13A descrambler is not supported\n\n"
+ "AppleAVD: INFO: %{public}s(): HEVC_Decoder::ParseHeader unsupported naluLengthSize %d\n"
+ "AppleAVD: INFO: %{public}s(): Invalid currBufIndex!\n"
+ "AppleAVD: INFO: %{public}s(): Invalid refBufIndex! index: %d\n"
+ "AppleAVD: INFO: %{public}s(): Invalid resolution\n"
+ "AppleAVD: INFO: %{public}s(): JumboSliceHeader at fnum %d bit_offset %d byte offset %d\n\n"
+ "AppleAVD: INFO: %{public}s(): Kopsia AVD is not supported in this AppleAVD driver!!!\n"
+ "AppleAVD: INFO: %{public}s(): LGH Internal bufferpool is full, invalid index %d\n\n"
+ "AppleAVD: INFO: %{public}s(): Level %d is not defined\n"
+ "AppleAVD: INFO: %{public}s(): LilyD AVD is not supported in this AppleAVD driver!!!\n"
+ "AppleAVD: INFO: %{public}s(): MultiView client %d\n"
+ "AppleAVD: INFO: %{public}s(): NALU bad size! %d\n"
+ "AppleAVD: INFO: %{public}s(): NALU too big! %d nal_ptr:%p, buf_end:%p\n"
+ "AppleAVD: INFO: %{public}s(): NULL DECODER type\n"
+ "AppleAVD: INFO: %{public}s(): NULL ppsList %p or spsList %p\n"
+ "AppleAVD: INFO: %{public}s(): NULL sliceHeader %p or nal_header %p or ppsList %p or spsList %p\n"
+ "AppleAVD: INFO: %{public}s(): NULL spsList\n"
+ "AppleAVD: INFO: %{public}s(): Narcissus AVD is not supported in this AppleAVD driver!!!\n"
+ "AppleAVD: INFO: %{public}s(): Only 4:4:4, 4:2:2 and 4:2:0 are currently supported, %d %d subsampling is not supported.\n\n"
+ "AppleAVD: INFO: %{public}s(): Outside of current operating range\n\n"
+ "AppleAVD: INFO: %{public}s(): PPS doesn't exist for slice header parsing\n"
+ "AppleAVD: INFO: %{public}s(): PPS size <= 0\n"
+ "AppleAVD: INFO: %{public}s(): Paravirtualized sessions - ineligible for compressed output!\n"
+ "AppleAVD: INFO: %{public}s(): ParseHeader unsupported naluLengthSize \n"
+ "AppleAVD: INFO: %{public}s(): Radish AVD is not supported in this AppleAVD driver!!!\n"
+ "AppleAVD: INFO: %{public}s(): RandomAccessSkipPic nal %d poc %d rapoc %d crasbla %d recov %d slice %d frame %d\n"
+ "AppleAVD: INFO: %{public}s(): RefPicList0 Missing Reference detected !\n"
+ "AppleAVD: INFO: %{public}s(): RefPicList1 Missing Reference detected !\n"
+ "AppleAVD: INFO: %{public}s(): RefPicture pool full, found duplicate ref picture slot, mark duplicate ref as unused \n\n"
+ "AppleAVD: INFO: %{public}s(): RefPicture pool full, mark oldest ref picture as unused \n\n"
+ "AppleAVD: INFO: %{public}s(): Rejecting RVRA scaling ratios beyond 16x! inWidth:%d inHeight:%d outWidth:%d outHeight:%d\n"
+ "AppleAVD: INFO: %{public}s(): Releasing CVPixelBufferRef!\n\n"
+ "AppleAVD: INFO: %{public}s(): Requested alloc size is = %zu too big\n\n"
+ "AppleAVD: INFO: %{public}s(): Requesting setting filmGrainMode to: %d\n\n"
+ "AppleAVD: INFO: %{public}s(): SETTING m_skipToIdr TRUE! fno=%d, err=%d\n"
+ "AppleAVD: INFO: %{public}s(): SPS doesn't exist for slice header parsing\n"
+ "AppleAVD: INFO: %{public}s(): SPS size <= 0\n"
+ "AppleAVD: INFO: %{public}s(): Successfully retrieved support bits! 0x%llx\n\n"
+ "AppleAVD: INFO: %{public}s(): Truncated packet or corrupt tile size.\n\n"
+ "AppleAVD: INFO: %{public}s(): Unexpected. av1_fb->buffer is 0x0!\n"
+ "AppleAVD: INFO: %{public}s(): Unmapping and deallocating CPB cache slot that is still in use!\n"
+ "AppleAVD: INFO: %{public}s(): Unsupported bitstream, sRGB colorspace not compatible with specified profile\n\n"
+ "AppleAVD: INFO: %{public}s(): Unsupported bitstream. Buffer does not contain a decoded frame.\n\n"
+ "AppleAVD: INFO: %{public}s(): Unsupported bitstream. Identity CICP Matrix incompatible with non 4:4:4 color sampling\n\n"
+ "AppleAVD: INFO: %{public}s(): Unsupported bitstream. header_size or obu_byte_alignment = -1 or sz < header_size\n\n"
+ "AppleAVD: INFO: %{public}s(): Unsupported bitstream. seq_header->reduced_still_picture_hdr = %d seq_header->still_picture= %d\n\n"
+ "AppleAVD: INFO: %{public}s(): Unsupported bitstream. seq_header->seq_level_idx[%d] = %d\n\n"
+ "AppleAVD: INFO: %{public}s(): Unsupported bitstream. seq_header->seq_level_idx[0] %d\n\n"
+ "AppleAVD: INFO: %{public}s(): Unsupported bitstream. tile_info not correct\n\n"
+ "AppleAVD: INFO: %{public}s(): Unsupported profile/bit-depth combination. seq_params->profile %d\n\n"
+ "AppleAVD: INFO: %{public}s(): Unsupported scaling dimensions! inWidth:%d inHeight:%d outWidth:%d outHeight:%d IOSurfaceGetWidthInCompressedTilesOfPlane:%zu IOSurfaceGetCompressedTileWidthOfPlane:%zu IOSurfaceGetHeightInCompressedTilesOfPlane:%zu IOSurfaceGetCompressedTileHeightOfPlane:%zu\n\n"
+ "AppleAVD: INFO: %{public}s(): Unsupported scaling dimensions! inWidth:%d inHeight:%d outWidth:%d outHeight:%d IOSurfaceGetWidthOfPlane:%zu extendedRight:%zu IOSurfaceGetHeightOfPlane:%zu extendedBottom:%zu\n\n"
+ "AppleAVD: INFO: %{public}s(): Unsupported sps->pic_width_in_luma_samples:%d or sps->pic_height_in_luma_samples:%d\n"
+ "AppleAVD: INFO: %{public}s(): VPS doesn't exist for slice header parsing\n"
+ "AppleAVD: INFO: %{public}s(): VPS doesn't exist to calc rep format!\n\n"
+ "AppleAVD: INFO: %{public}s(): VPS layers %d not supported\n"
+ "AppleAVD: INFO: %{public}s(): VPS size <= 0\n"
+ "AppleAVD: INFO: %{public}s(): Wrong sizeOfScalingList (%d). Should be either 16 or 64\n"
+ "AppleAVD: INFO: %{public}s(): [%4d, %4d] w->dataAddrHi = %08x, from %llx\n"
+ "AppleAVD: INFO: %{public}s(): about to kAppleAVDSetMiscPreferences, storage->miscPreferences is 0x%x\n\n"
+ "AppleAVD: INFO: %{public}s(): all intra frame found, reset m_skipToIdr to false; frm# %d\n"
+ "AppleAVD: INFO: %{public}s(): av1_populate_film_grain_params returned false\n"
+ "AppleAVD: INFO: %{public}s(): avdDec - Setting CFDebugMetaDataSEI to %d\n\n"
+ "AppleAVD: INFO: %{public}s(): backward refresh 0 fci_ref fc %p\n\n"
+ "AppleAVD: INFO: %{public}s(): backward refresh 1 fci_ref fc %p\n\n"
+ "AppleAVD: INFO: %{public}s(): bad PPS index %d\n\n"
+ "AppleAVD: INFO: %{public}s(): bad SPS index %d\n\n"
+ "AppleAVD: INFO: %{public}s(): bad buffer index %d\n\n"
+ "AppleAVD: INFO: %{public}s(): bad index %u\n"
+ "AppleAVD: INFO: %{public}s(): bad repFormatIdx \n"
+ "AppleAVD: INFO: %{public}s(): bad swr bit depth %d\n\n"
+ "AppleAVD: INFO: %{public}s(): bd changed: %d vs %d\n"
+ "AppleAVD: INFO: %{public}s(): begin ref_frame_idx[%d] = %d\n\n"
+ "AppleAVD: INFO: %{public}s(): bit depth %d not recognized\n\n"
+ "AppleAVD: INFO: %{public}s(): bit stream buffer too small for annexb obu\n\n"
+ "AppleAVD: INFO: %{public}s(): bit stream buffer too small for obu\n\n"
+ "AppleAVD: INFO: %{public}s(): bit_depth_chroma_minus8 inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d\n"
+ "AppleAVD: INFO: %{public}s(): bit_depth_luma_minus8 inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d\n"
+ "AppleAVD: INFO: %{public}s(): buf %p frame %p size %zu expect at least %d\n\n"
+ "AppleAVD: INFO: %{public}s(): buf[%2d]=%p ref_count = %2d order_hint=%d\n\n"
+ "AppleAVD: INFO: %{public}s(): buffer length == 0.  Copying dimensions from FigVideoDimensions %d %d\n"
+ "AppleAVD: INFO: %{public}s(): buffer ref_count is already zero\n\n"
+ "AppleAVD: INFO: %{public}s(): buffer size %zu expect bigger than %d (two super frame header bytes plus total frame size bytes)\n\n"
+ "AppleAVD: INFO: %{public}s(): called but plugin state is %d\n"
+ "AppleAVD: INFO: %{public}s(): called with NULL prefs ptr\n"
+ "AppleAVD: INFO: %{public}s(): called with invalid storage\n"
+ "AppleAVD: INFO: %{public}s(): cfg1: %d %d %d %d %d %d %d %d\n"
+ "AppleAVD: INFO: %{public}s(): cfg2: %d %d %d %d %d %d %d\n"
+ "AppleAVD: INFO: %{public}s(): cfg3: %d %d %d %d %d %d %d %d %d %d\n"
+ "AppleAVD: INFO: %{public}s(): checkRVRAScalingRatio returned error:%d\n\n"
+ "AppleAVD: INFO: %{public}s(): chip id is not used while ecid and/or board id is used\n\n"
+ "AppleAVD: INFO: %{public}s(): chroma_and_bit_depth_vps_present_flags is 0 for first rep format\n"
+ "AppleAVD: INFO: %{public}s(): chroma_format_idc inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d\n"
+ "AppleAVD: INFO: %{public}s(): clientID : %2d, frameInfoOut is NULL!!!, frameNum:%d\n"
+ "AppleAVD: INFO: %{public}s(): clientID : %2d, frameInfoOut is NULL!!!, frameType :%d, frameNum:%d\n"
+ "AppleAVD: INFO: %{public}s(): codecIntializationDataSize not zero %x %x, but ignored\n"
+ "AppleAVD: INFO: %{public}s(): codecType: AV1, %d x %d, session: %p, built %s %s\n"
+ "AppleAVD: INFO: %{public}s(): codecType: AVC, %d x %d,  session: %p built %s %s\n"
+ "AppleAVD: INFO: %{public}s(): codecType: AVC, encryptionScheme %d, %d x %d, session: %p\n"
+ "AppleAVD: INFO: %{public}s(): codecType: AVC, encryptionScheme %d, %d x %d, tryAllFrames = %d, usageMode: %d, session: %p built %s %s\n"
+ "AppleAVD: INFO: %{public}s(): codecType: Fghrn, encryptionScheme %d, %d x %d, built %s %s\n"
+ "AppleAVD: INFO: %{public}s(): codecType: Fghrn, encryptionScheme %d, %d x %d, session : %p\n"
+ "AppleAVD: INFO: %{public}s(): codecType: Fghrn, encryptionScheme %d, %d x %d, tryAllFrames = %d, session : %p, built %s %s\n"
+ "AppleAVD: INFO: %{public}s(): codecType: HEVC, %d x %d, session: %p, built %s %s\n"
+ "AppleAVD: INFO: %{public}s(): codecType: HEVC, encryptionScheme %d, %d x %d, session: %p\n"
+ "AppleAVD: INFO: %{public}s(): codecType: HEVC, encryptionScheme %d, %d x %d, tryAllFrames = %d, usageMode: %d, session: %p, built %s %s\n"
+ "AppleAVD: INFO: %{public}s(): codecType: Lghrn, encryptionScheme %d, %d x %d, built %s %s\n"
+ "AppleAVD: INFO: %{public}s(): codecType: Lghrn, encryptionScheme %d, %d x %d, session : %p\n"
+ "AppleAVD: INFO: %{public}s(): codecType: Lghrn, encryptionScheme %d, %d x %d, tryAllFrames = %d, session : %p, built %s %s\n"
+ "AppleAVD: INFO: %{public}s(): ctbYSize inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d\n"
+ "AppleAVD: INFO: %{public}s(): cur and ref frame format mismatch bd %d-%d ssx %d-%d ssy %d-%d\n\n"
+ "AppleAVD: INFO: %{public}s(): cur_frame pool[%d] = %p/%p\n\n"
+ "AppleAVD: INFO: %{public}s(): end ref_frame_idx[%d] = %d\n\n"
+ "AppleAVD: INFO: %{public}s(): enter\n"
+ "AppleAVD: INFO: %{public}s(): expect %02x-%02x-%02x got %02x-%02x-%02x\n\n"
+ "AppleAVD: INFO: %{public}s(): expect off_to_prot_data to be set when slice header is not byte aligned\n\n"
+ "AppleAVD: INFO: %{public}s(): extension_header_reserved_3bits must be set to 0. extension_header_reserved_3bits %d\n\n"
+ "AppleAVD: INFO: %{public}s(): fail to read annexb obu header and payload length\n\n"
+ "AppleAVD: INFO: %{public}s(): fail to read obu size\n\n"
+ "AppleAVD: INFO: %{public}s(): failed due to p_ctx=%p, p_cv_pool=%p, max_cache_size=%d, m_is_initialized=%d\n"
+ "AppleAVD: INFO: %{public}s(): fb refcnt\n\n"
+ "AppleAVD: INFO: %{public}s(): fb->buffer is NULL!!\n"
+ "AppleAVD: INFO: %{public}s(): found incomplete progressive sample! Quitting.\n"
+ "AppleAVD: INFO: %{public}s(): frame %d layerpresent %d layerID %d numLayers %d \n\n"
+ "AppleAVD: INFO: %{public}s(): frame marker expect 2 got %x\n\n"
+ "AppleAVD: INFO: %{public}s(): frameNum %d pthread_cond_timedwait (%d msec)! timedWaitMS: %llu\n"
+ "AppleAVD: INFO: %{public}s(): frameNum %d was not found in flight! Something is wrong\n"
+ "AppleAVD: INFO: %{public}s(): frameNumber = %d - No free slot found to assign bitstreamIndex.\n"
+ "AppleAVD: INFO: %{public}s(): frameType :%d \n"
+ "AppleAVD: INFO: %{public}s(): frame_header_obu returned -1\n\n"
+ "AppleAVD: INFO: %{public}s(): frame_mbs_only_flag inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d\n"
+ "AppleAVD: INFO: %{public}s(): frame_to_show pool[%d] = %p/%p\n\n"
+ "AppleAVD: INFO: %{public}s(): frm %8d decoded - frame_to_show w/ nil buffer for buf_idx=%4d\n"
+ "AppleAVD: INFO: %{public}s(): get_bits(%d): %s = %x, m_bits_left %d\n\n"
+ "AppleAVD: INFO: %{public}s(): height inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d\n"
+ "AppleAVD: INFO: %{public}s(): illegal num_entry_point_offsets %d\n"
+ "AppleAVD: INFO: %{public}s(): incompatible codec %d and decrypt method %d\n"
+ "AppleAVD: INFO: %{public}s(): inconsistent super frame header %x %x\n\n"
+ "AppleAVD: INFO: %{public}s(): internal build, useCompression %d\n"
+ "AppleAVD: INFO: %{public}s(): invalid dispbufIndex, refBufIndex = %d ctx->noSecondWrite %d or ctx->pBufferPool[AVD_PIXBUF_DEC] is NULL! \n\n"
+ "AppleAVD: INFO: %{public}s(): invalid frame to show map idx %d\n\n"
+ "AppleAVD: INFO: %{public}s(): invalid hdr %p buffer pointer %p pool %p\n\n"
+ "AppleAVD: INFO: %{public}s(): invalid input parameter\n\n"
+ "AppleAVD: INFO: %{public}s(): invalid out_length %d\n\n"
+ "AppleAVD: INFO: %{public}s(): invalid ref_frame_idx[%d] %d\n\n"
+ "AppleAVD: INFO: %{public}s(): invalid reference buffer %d\n\n"
+ "AppleAVD: INFO: %{public}s(): invalid stat crop width/height %d/%d\n"
+ "AppleAVD: INFO: %{public}s(): invalid weight table\n"
+ "AppleAVD: INFO: %{public}s(): ioSurfaceRef for refSurfaceListIndx:%d is NULL!\n"
+ "AppleAVD: INFO: %{public}s(): kVTDecompressionPropertyKey_Paravirtualized - paravirtualizedSession: %d\n"
+ "AppleAVD: INFO: %{public}s(): kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs not supported for hevc stream\n"
+ "AppleAVD: INFO: %{public}s(): kVTDecompressionPropertyKey_SelectPixelFormatWithAlpha storage->decodeToBufferWithAlpha:%d\n"
+ "AppleAVD: INFO: %{public}s(): kVTDecompressionPropertyKey_WriteDirectlyToPlanesOfTargetCVPixelBuffer storage->startingPlaneOffset:%d\n"
+ "AppleAVD: INFO: %{public}s(): key_func=9, set LK/KEYB\n\n"
+ "AppleAVD: INFO: %{public}s(): l0_count + l1_count ==0 !\n"
+ "AppleAVD: INFO: %{public}s(): lhvc is not received %d for mvhevc stream\n"
+ "AppleAVD: INFO: %{public}s(): linear_orig or linear_scaled is NULL\n\n"
+ "AppleAVD: INFO: %{public}s(): longest wait: ~%llums\n\n"
+ "AppleAVD: INFO: %{public}s(): m_buf_len should > 1 byte because there is extension header. m_buf_len = %lu\n\n"
+ "AppleAVD: INFO: %{public}s(): m_frame_refs[%d] pool[%d] = %p/%p\n\n"
+ "AppleAVD: INFO: %{public}s(): m_p_buf_pool is NULL \n\n"
+ "AppleAVD: INFO: %{public}s(): matrixId %d < scaling_list_pred_matrix_id_delta %d\n"
+ "AppleAVD: INFO: %{public}s(): max allow tiles %d got %d, tile rows : %d, tile cols : %d\n\n"
+ "AppleAVD: INFO: %{public}s(): maxCacheSize (%d) Exceeded 20!\n\n"
+ "AppleAVD: INFO: %{public}s(): maxDpbSize inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d\n"
+ "AppleAVD: INFO: %{public}s(): missing lt reference LtFoll %d stIdx %d\n"
+ "AppleAVD: INFO: %{public}s(): missing ref - skip RASL picture: %d crasbla %d \n\n"
+ "AppleAVD: INFO: %{public}s(): missing st reference StFoll %d stIdx %d\n"
+ "AppleAVD: INFO: %{public}s(): need frame context %p and header %p\n\n"
+ "AppleAVD: INFO: %{public}s(): need one extra byte for obu header\n\n"
+ "AppleAVD: INFO: %{public}s(): need one extra byts for obu header extension\n\n"
+ "AppleAVD: INFO: %{public}s(): next_32bits: %x m_bits_left %d\n\n"
+ "AppleAVD: INFO: %{public}s(): no frame buffer available\n\n"
+ "AppleAVD: INFO: %{public}s(): no reference frame has valid dimensions\n\n"
+ "AppleAVD: INFO: %{public}s(): none zero marker bit\n\n"
+ "AppleAVD: INFO: %{public}s(): none zero reserved bit\n\n"
+ "AppleAVD: INFO: %{public}s(): num_units_in_display_tick and time_scale must be greater than 0. num_units_in_display_tick %d time_scale %d\n\n"
+ "AppleAVD: INFO: %{public}s(): obu forbidden bit shuld not be set\n\n"
+ "AppleAVD: INFO: %{public}s(): obu_reserved_1bit must be set to 0. obu_reserved_1bit %d\n\n"
+ "AppleAVD: INFO: %{public}s(): out of range PPS id %d\n"
+ "AppleAVD: INFO: %{public}s(): out of range SPS id %d\n"
+ "AppleAVD: INFO: %{public}s(): out of range SPS id %u\n"
+ "AppleAVD: INFO: %{public}s(): oversized iv %d\n"
+ "AppleAVD: INFO: %{public}s(): pBufferPool[%d] is NULL cvPixBufIndex:%d!\n"
+ "AppleAVD: INFO: %{public}s(): pBufferPool[AVD_PIXBUF_DEC] && pBufferPool[AVD_PIXBUF_DISP] are NULL!\n"
+ "AppleAVD: INFO: %{public}s(): pIOSurfaceDst lockSurface failed with error:%d\n\n"
+ "AppleAVD: INFO: %{public}s(): pIOSurfaceDst lookup failed!\n\n"
+ "AppleAVD: INFO: %{public}s(): pIOSurfaceSrc lockSurface failed with error:%d\n\n"
+ "AppleAVD: INFO: %{public}s(): pIOSurfaceSrc lookup failed!\n\n"
+ "AppleAVD: INFO: %{public}s(): padding ineligible for compression w x h = %d %d, cw x cw = %d %d\n"
+ "AppleAVD: INFO: %{public}s(): parsing error, wrong tile start\n"
+ "AppleAVD: INFO: %{public}s(): pic_parameter_set_id(%d) out of range [0..%d]\n"
+ "AppleAVD: INFO: %{public}s(): pixel buffer format: %c%c%c%c - kIOSurfaceCompressionTypeAGX\n\n"
+ "AppleAVD: INFO: %{public}s(): pixel buffer format: %c%c%c%c - kIOSurfaceCompressionTypeHTPC\n\n"
+ "AppleAVD: INFO: %{public}s(): pixel buffer format: %c%c%c%c - kIOSurfaceCompressionTypeNone\n\n"
+ "AppleAVD: INFO: %{public}s(): pool[%d] = %p\n\n"
+ "AppleAVD: INFO: %{public}s(): ppRenderSurfaceList[%d] == NULL\n"
+ "AppleAVD: INFO: %{public}s(): ppsNALUAndRBSPSize %d size1 %d configRecordSize %zu i %d\n\n"
+ "AppleAVD: INFO: %{public}s(): preconfiguredPixBufAttrs is NULL!\n"
+ "AppleAVD: INFO: %{public}s(): primary ref fc %p\n\n"
+ "AppleAVD: INFO: %{public}s(): primary ref no fb, default %d fc %p\n\n"
+ "AppleAVD: INFO: %{public}s(): profile_idc(%d) is not valid\n"
+ "AppleAVD: INFO: %{public}s(): propertyValue (%p) is invalid!\n"
+ "AppleAVD: INFO: %{public}s(): raw obu must have size field\n\n"
+ "AppleAVD: INFO: %{public}s(): received reset Before Decoding - Flush DPB, framenumber %d\n"
+ "AppleAVD: INFO: %{public}s(): ref frame map\n\n"
+ "AppleAVD: INFO: %{public}s(): ref none, default %d fc %p\n\n"
+ "AppleAVD: INFO: %{public}s(): ref_frame_idx[%d] = %d, pool[%d] = %p/%p\n\n"
+ "AppleAVD: INFO: %{public}s(): ref_frame_map[%d] %p ref_count %d\n\n"
+ "AppleAVD: INFO: %{public}s(): ref_frame_map[%d] pool[%d] = %p/%p\n\n"
+ "AppleAVD: INFO: %{public}s(): release fb %d fci_wr fc %p, copy to pool[%d] fci_wr fc %p\n\n"
+ "AppleAVD: INFO: %{public}s(): releaseOneCPB returned %d\n\n"
+ "AppleAVD: INFO: %{public}s(): reset all ref_frame_idx to AV1_INVALID_IDX for key frame\n\n"
+ "AppleAVD: INFO: %{public}s(): resolution_change=1, segEn=%d, mi curr %4d x %4d, prev %4d x %4d\n"
+ "AppleAVD: INFO: %{public}s(): retain count is %ld\n"
+ "AppleAVD: INFO: %{public}s(): returning %d (0: reject; 1: accept)\n"
+ "AppleAVD: INFO: %{public}s(): rvra temp buff size isn't big enough! yuvsize:%u rvraTempBuffSize:%u\n\n"
+ "AppleAVD: INFO: %{public}s(): rvrascalerbuffsize alloc overflow %d\n"
+ "AppleAVD: INFO: %{public}s(): separate_colour_plane_flag inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d\n"
+ "AppleAVD: INFO: %{public}s(): seq_parameter_set_id(%d) out of range [0..%d]\n"
+ "AppleAVD: INFO: %{public}s(): set KEY(H13)\n\n"
+ "AppleAVD: INFO: %{public}s(): set LK/KEYB\n\n"
+ "AppleAVD: INFO: %{public}s(): set av1 dual vp mode as %d\n"
+ "AppleAVD: INFO: %{public}s(): setting storage->usageMode to %d\n\n"
+ "AppleAVD: INFO: %{public}s(): show %d, showable %d, filmGrainMode = %d, params_present %d, apply_grain %d, frame %d\n"
+ "AppleAVD: INFO: %{public}s(): show_existing - frame_to_show w/ nil buffer for buf_idx=%4d\n"
+ "AppleAVD: INFO: %{public}s(): skip m_bool_max_bits %d - m_bits_left %d\n\n"
+ "AppleAVD: INFO: %{public}s(): slice->slice_pic_parameter_set_id > HEVC_MAX_PPS_SET, is %d\n"
+ "AppleAVD: INFO: %{public}s(): spsChanged - bdC-8 : %d vs %d\n"
+ "AppleAVD: INFO: %{public}s(): spsChanged - bdY-8 : %d vs %d\n"
+ "AppleAVD: INFO: %{public}s(): spsChanged - ch_idc: %d vs %d\n"
+ "AppleAVD: INFO: %{public}s(): spsChanged - height: %d vs %d\n"
+ "AppleAVD: INFO: %{public}s(): spsChanged - maxBlk: %d vs %d\n"
+ "AppleAVD: INFO: %{public}s(): spsChanged - width : %d vs %d\n"
+ "AppleAVD: INFO: %{public}s(): storage->usageMode:%d storage->enableRVRA:%d storage->enableChromaFilter:%d\n"
+ "AppleAVD: INFO: %{public}s(): subsampling x/y %d/%d, unsupported chroma format idc\n\n"
+ "AppleAVD: INFO: %{public}s(): tg_end (%d) must be greater than or equal to tg_start (%d) \n\n"
+ "AppleAVD: INFO: %{public}s(): tg_end (%d) must be less than NumTiles (%d) \n\n"
+ "AppleAVD: INFO: %{public}s(): tg_start (%d) must be equal to %d \n\n"
+ "AppleAVD: INFO: %{public}s(): tile %d offset %lu size %lu corrupted\n\n"
+ "AppleAVD: INFO: %{public}s(): too many PPS %d\n"
+ "AppleAVD: INFO: %{public}s(): too many SPS %d\n"
+ "AppleAVD: INFO: %{public}s(): too many VPS %d\n"
+ "AppleAVD: INFO: %{public}s(): total frame size plus super frame index size %d not equal to buffer size %zu\n\n"
+ "AppleAVD: INFO: %{public}s(): transcryption attempted with incompatible scheme %d\n"
+ "AppleAVD: INFO: %{public}s(): um_ticks_per_picture_minus_1 cannot be (1 << 32) − 1. num_ticks_per_picture_minus_1 %d\n\n"
+ "AppleAVD: INFO: %{public}s(): uncomp_hdr->ref_frame_map[%d] = %p\n\n"
+ "AppleAVD: INFO: %{public}s(): undersized config record\n"
+ "AppleAVD: INFO: %{public}s(): unsupported bit stream w %d h %d bd %d %d CtbSizeY %d\n\n"
+ "AppleAVD: INFO: %{public}s(): unsupported profile %d\n"
+ "AppleAVD: INFO: %{public}s(): unsupported profile %d\n\n"
+ "AppleAVD: INFO: %{public}s(): value %d out of range!\n\n"
+ "AppleAVD: INFO: %{public}s(): value out of range: num_tile_columns_minus1 %d num_tile_rows_minus1 %d\n"
+ "AppleAVD: INFO: %{public}s(): videoLayerID %d index %d\n"
+ "AppleAVD: INFO: %{public}s(): vpsext->vps_num_target_opt_layer_id_lists[%d] == 0\n\n"
+ "AppleAVD: INFO: %{public}s(): vpsext->vps_num_target_opt_layer_id_lists[0] == 0\n\n"
+ "AppleAVD: INFO: %{public}s(): waited at least %llums for frameNum %d! m_num_CPBs_on_the_fly=%u timeoutMS=%llu\n"
+ "AppleAVD: INFO: %{public}s(): waited at least %llums! m_num_CPBs_on_the_fly(%u) > numToWaitFor(%d) timeoutMS=%llu\n"
+ "AppleAVD: INFO: %{public}s(): width inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d\n"
+ "AppleAVD: WARNING: %{public}s():  tile skip calculation has failed\n\n"
+ "AppleAVD: WARNING: %{public}s(): #### <WARNING> Bit depth changed: new_bit_depth_luma_minus8:%d m_orig_bit_depth_luma_minus8:%d new_bit_depth_chroma_minus8:%d m_orig_bit_depth_chroma_minus8:%d\n"
+ "AppleAVD: WARNING: %{public}s(): #### <WARNING> CTB size changed new_CtbSizeY:%d m_orig_CtbSizeY:%d\n"
+ "AppleAVD: WARNING: %{public}s(): #### <WARNING> Chroma format Changed: %d -> %d\n"
+ "AppleAVD: WARNING: %{public}s(): #### <WARNING> DPB Size Requirement Changed: origDpbSize: %d -> curDpbSize: %d, prevDpbSize: %d\n"
+ "AppleAVD: WARNING: %{public}s(): #### <WARNING> Frame resolution change not supported Frame %d old %d %d new %d %d\n"
+ "AppleAVD: WARNING: %{public}s(): #### <WARNING> new_bit_depth_luma_minus8:%d m_orig_bit_depth_luma_minus8:%d new_bit_depth_chroma_minus8:%d m_orig_bit_depth_chroma_minus8:%d\n"
+ "AppleAVD: WARNING: %{public}s(): #### <WARNING> new_chroma_format_idc:%d m_orig_chroma_format_idc:%d\n"
+ "AppleAVD: WARNING: %{public}s(): #### <WARNING> new_separate_colour_plane_flag:%d m_orig_separate_colour_plane_flag:%d\n"
+ "AppleAVD: WARNING: %{public}s(): %s %d 64->32 conversion problem!\n"
+ "AppleAVD: WARNING: %{public}s(): %u: WARNING! resizing CVPixelBufferPool is not supported\n"
+ "AppleAVD: WARNING: %{public}s(): AVC chroma plane with odd number of IMBs is unspported on Salvia A0\n"
+ "AppleAVD: WARNING: %{public}s(): AVD SWR stride (%d, %d) != IOSurface stride (%d, %d). If IOSurface is displayed, output will be corrupted. If YUV is written to file system, no corruption.\n"
+ "AppleAVD: WARNING: %{public}s(): Corrupted metadata OBU\n\n"
+ "AppleAVD: WARNING: %{public}s(): FGH chroma plane with odd number of IMBs is unspported on Salvia A0\n"
+ "AppleAVD: WARNING: %{public}s(): Got NULL infoFlagsOut!\n\n"
+ "AppleAVD: WARNING: %{public}s(): HEVC chroma plane with odd number of IMBs is unspported on Salvia A0\n"
+ "AppleAVD: WARNING: %{public}s(): LGH chroma plane with odd number of IMBs is unspported on Salvia A0\n"
+ "AppleAVD: WARNING: %{public}s(): Non-mod16 VRA dimensions with width %d, height %d\n\n"
+ "AppleAVD: WARNING: %{public}s(): Pixel Buffer Format array has %ld entries!\n\n"
+ "AppleAVD: WARNING: %{public}s(): Timed out, waited at least %llums! m_num_CPBs_on_the_fly=%u timeoutMS=%llu\n"
+ "AppleAVD: WARNING: %{public}s(): Unrecognized OBU type %d will be dropped\n\n"
+ "AppleAVD: WARNING: %{public}s(): _numActivePictures=%d is not valid, now clamped to 0\n\n"
+ "AppleAVD: WARNING: %{public}s(): bad PPS index %d\n"
+ "AppleAVD: WARNING: %{public}s(): bad SPS index %d\n"
+ "AppleAVD: WARNING: %{public}s(): clientID : %2d, #### <WARNING> Frame resolution change not supported frameNum:%d old (%dx%d) new (%dx%d)\n"
+ "AppleAVD: WARNING: %{public}s(): clientID : %2d, #### <WARNING> frameNum:%d m_cur_pic_info->chroma_format:%d m_orig_chroma_format_idc:%d\n"
+ "AppleAVD: WARNING: %{public}s(): clientID : %2d, #### <WARNING> frameNum:%d pHeader->BitDepth:%d m_orig_bit_depth_luma_minus8+8:%d\n"
+ "AppleAVD: WARNING: %{public}s(): coded size has changed!\n"
+ "AppleAVD: WARNING: %{public}s(): frame insertion is aborted because pic=NULL\n\n"
+ "AppleAVD: WARNING: %{public}s(): frameNum %d - BufferPoolId[%d]: Index %d is not in use! in_use: %d\n\n"
+ "AppleAVD: WARNING: %{public}s(): h->req.a.da.DecAddrYSize.val = %d\n"
+ "AppleAVD: WARNING: %{public}s(): h->req.a.da.RefAddrYSize.val = %d\n"
+ "AppleAVD: WARNING: %{public}s(): h->req.a.da.RefAddrYSize.val = %d\n\n"
+ "AppleAVD: WARNING: %{public}s(): index: %d - trying to release! frameNum (%d) < get frameNum (%d), returning early!\n"
+ "AppleAVD: WARNING: %{public}s(): index=%d is invalid, maximum allowable is %d\n\n"
+ "AppleAVD: WARNING: %{public}s(): initial_obu_buffer isn't empty like it should\n\n"
+ "AppleAVD: WARNING: %{public}s(): kVAGetApplyFoxtrot with m_active_sps %d m_active_pps %d\n"
+ "AppleAVD: WARNING: %{public}s(): no configOBUs[]\n\n"
+ "AppleAVD: WARNING: %{public}s(): out of memory on line %d\n\n"
+ "AppleAVD: WARNING: %{public}s(): pic size too wide %d %d or tall %d %d vs. %d but depth %d chroma fmt %d, so we'll attempt it anyway\n"
+ "AppleAVD: WARNING: %{public}s(): pluginState (%d) was already started! Trying to change kVTDecompressionPropertyKey_SelectPixelFormatWithAlpha\n"
+ "AppleAVD: WARNING: %{public}s(): pluginState (%d) was already started! Trying to change kVTDecompressionPropertyKey_WriteDirectlyToPlanesOfTargetCVPixelBuffer\n"
+ "AppleAVD: WARNING: %{public}s(): should not decode frame %d!\n\n"
+ "AppleAVD: WARNING: %{public}s(): timeout status: %d\n"
+ "AppleAVD: WARNING: %{public}s(): timeout timeoutStatus: %d\n"
+ "AppleAVD: WARNING: %{public}s(): trying to get FrameReceiverThreadPriority before videoContext was created!\n\n"
+ "AppleAVD: WARNING: %{public}s(): trying to set kAppleAVDEnableIOFence before videoContext was created!\n\n"
+ "AppleAVD: WARNING: %{public}s(): trying to set kAppleAVDEnableRVRA before videoContext was created!\n\n"
+ "AppleAVD: WARNING: %{public}s(): trying to set kAppleAVDExtraInloopFilter before videoContext was created!\n\n"
+ "AppleAVD: WARNING: %{public}s(): trying to set kAppleAVDSetAttachQPs before videoContext was created!\n\n"
+ "AppleAVD: WARNING: %{public}s(): trying to set kAppleAVDSetAv1FilmGrainMode before videoContext was created!\n\n"
+ "AppleAVD: WARNING: %{public}s(): trying to set kAppleAVDSetMVHEVCDisplayLayerIDs before videoContext was created!\n\n"
+ "AppleAVD: WARNING: %{public}s(): trying to set kAppleAVDSetUsageMode before videoContext was created!\n\n"
+ "AppleAVD: WARNING: %{public}s(): trying to set kAppleAVDSetVRADimensions before videoContext was created!\n\n"
+ "AppleAVD: WARNING: %{public}s(): trying to set kAppleAVDSetVRAType before videoContext was created!\n\n"
+ "AppleAVDDoResolutionChange"
+ "AppleAVDPutTiledPixelBufferIntoBufferPool"
+ "AppleAVDReleaseCVPixelBuffer"
+ "AppleAVDSetParameter"
+ "AppleAVDUnmapCVPixelBuffer"
+ "AppleAVDWrapperHEVCDecoderCopySupportedPropertyDictionary"
+ "CloseAVDFghrnInstance"
+ "CloseAVDH264Instance"
+ "CloseAVDHEVCInstance"
+ "CloseAVDLghrnInstance"
+ "CompareVpsParamsInFormatDescriptors"
+ "Decoder_getCFPreferenceNumber"
+ "DumpHevcStream"
+ "Feb  5 2026"
+ "FrameEvent"
+ "PrepareHistogramDump"
+ "VAGetIOSurfaceIDForBufferIndex"
+ "VAGetParams"
+ "VASetParams"
+ "VideoDecoder_getCFPreferenceNumber"
+ "WriteNAL"
+ "checkRVRAScalingRatio"
+ "frame_header_obu"
+ "getBitDepth"
+ "getChromaFormat"
+ "getDeltaLfRes"
+ "getRestorationUnitSize"
+ "getUpscaleConvolveStep"
+ "getUpscaleConvolveX0"
+ "get_bits"
+ "metadata_obu"
+ "next_32bits"
+ "numArgs == kAVD_USERCLIENT_RESPONSE_ARG_COUNT"
+ "parseRepformat"
+ "parseScalingListData"
+ "performRangeChecksAndComputeParameters"
+ "scalingList"
+ "shallowCloneBuffer"
+ "sps->CtbLog2SizeY"
- "/Library/Caches/com.apple.xbs/Sources/AppleAVD/framework/AppleAVDFrameReceiver.cpp"
- "20:56:07"
- "20:56:08"
- "AVD_CheckWireLimit"
- "AppleAVD: \n"
- "AppleAVD:  %2d"
- "AppleAVD:  Compressed buffers disabled! luma depth %d chroma format %d"
- "AppleAVD:  Compressed buffers enabled! CompressionType:%d. luma depth %d chroma format %d"
- "AppleAVD:  ERROR:  kJVTLibCompressedDataFormat_WrappedNALU_* :: NOT SUPPORTED, storage->naluLengthSize %d"
- "AppleAVD:  cannot initialize cond variable, return error %d [ %s ]"
- "AppleAVD:  cannot initialize mutex, return error %d [ %s ]"
- "AppleAVD: #### <WARNING> Bit depth changed: new_bit_depth_luma_minus8:%d m_orig_bit_depth_luma_minus8:%d new_bit_depth_chroma_minus8:%d m_orig_bit_depth_chroma_minus8:%d"
- "AppleAVD: #### <WARNING> CTB size changed new_CtbSizeY:%d m_orig_CtbSizeY:%d"
- "AppleAVD: #### <WARNING> Chroma format Changed: %d -> %d"
- "AppleAVD: #### <WARNING> DPB Size Requirement Changed: origDpbSize: %d -> curDpbSize: %d, prevDpbSize: %d"
- "AppleAVD: #### <WARNING> Frame resolution change not supported Frame %d old %d %d new %d %d"
- "AppleAVD: #### <WARNING> new_bit_depth_luma_minus8:%d m_orig_bit_depth_luma_minus8:%d new_bit_depth_chroma_minus8:%d m_orig_bit_depth_chroma_minus8:%d"
- "AppleAVD: #### <WARNING> new_chroma_format_idc:%d m_orig_chroma_format_idc:%d"
- "AppleAVD: #### <WARNING> new_separate_colour_plane_flag:%d m_orig_separate_colour_plane_flag:%d"
- "AppleAVD: #HEVC# storage->memCacheMode = %d"
- "AppleAVD: %d: get_bits(%d): %s = %d, m_bits_left %d from buffer: %p\n"
- "AppleAVD: %s - bad repFormatIdx "
- "AppleAVD: %s - kVTDecompressionPropertyKey_RequestedMVAV1SpatialVideoLayerIDs error"
- "AppleAVD: %s - kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs error"
- "AppleAVD: %s - kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs not supported for hevc stream"
- "AppleAVD: %s - lhvc is not received %d for mvhevc stream"
- "AppleAVD: %s - missing lt reference LtFoll %d stIdx %d"
- "AppleAVD: %s - missing st reference StFoll %d stIdx %d"
- "AppleAVD: %s -- DPB is full auIndex %d"
- "AppleAVD: %s -- DPB is full numAus %d auIndex %d"
- "AppleAVD: %s -- emptyLayer out of range"
- "AppleAVD: %s -- m_numActiveAccessUnits out of range %d"
- "AppleAVD: %s : clientID : %2d fail to alloc work buffer for sps frameNum:%d \n"
- "AppleAVD: %s : clientID:%2d, LGH Decoder frameWidth : %d, frameHeight : %d is out of range, frameNum :%d"
- "AppleAVD: %s ERROR: pluginState isn't kPluginCreated, is %d"
- "AppleAVD: %s Error: 0 is not the last operation. memory_management_control_operation[%d] = %d"
- "AppleAVD: %s MMC 1: Cannot find picNumX %d CurrPicNum %d difference_of_pic_nums_minus1 %d"
- "AppleAVD: %s MMC 2: Cannot find LongTermPicNum %d"
- "AppleAVD: %s MMC 3: Cannot find picNumX %d CurrPicNum %d difference_of_pic_nums_minus1 %d"
- "AppleAVD: %s MultiView client %d"
- "AppleAVD: %s NALU bad size! %d"
- "AppleAVD: %s NALU too big! %d nal_ptr:%p, buf_end:%p"
- "AppleAVD: %s NALU too big! %d nal_ptr:%p, buf_end:%p; dataLength: %8d"
- "AppleAVD: %s PPS size <= 0"
- "AppleAVD: %s Parameter Set missing %d"
- "AppleAVD: %s Parameter Set missing %d %d"
- "AppleAVD: %s Parameter Set missing %d %d %d"
- "AppleAVD: %s RASL picture %d with no associated IRAP picture"
- "AppleAVD: %s SPS size <= 0"
- "AppleAVD: %s VPS size <= 0"
- "AppleAVD: %s bad PPS index %d"
- "AppleAVD: %s bad SPS index %d"
- "AppleAVD: %s bad index %u"
- "AppleAVD: %s buffer length == 0.  Copying dimensions from FigVideoDimensions %d %d"
- "AppleAVD: %s called but plugin state is %d"
- "AppleAVD: %s called with NULL prefs ptr"
- "AppleAVD: %s called with invalid storage"
- "AppleAVD: %s clientID : %2d fail to alloc work buffer for pps frame_type %d, frameNum:%d \n"
- "AppleAVD: %s fail to alloc work buffer for pps\n"
- "AppleAVD: %s fail to allocate work buffer for pps"
- "AppleAVD: %s fail to allocate work buffer for pps\n"
- "AppleAVD: %s fail to allocate work buffer for sps"
- "AppleAVD: %s fail to allocate work buffer for sps\n"
- "AppleAVD: %s fail to get SWR stride for the picture\n"
- "AppleAVD: %s fail to get delta lf res\n"
- "AppleAVD: %s fail to get restoration unit size\n"
- "AppleAVD: %s incompatible codec %d and decrypt method %d"
- "AppleAVD: %s invalid VPS id!"
- "AppleAVD: %s invalid dispbufIndex, refBufIndex = %d ctx->noSecondWrite %d or ctx->pBufferPool[AVD_PIXBUF_DEC] is NULL! \n"
- "AppleAVD: %s layer id not found in vps_layer_id_in_nuh"
- "AppleAVD: %s layerActive mem alloc failed"
- "AppleAVD: %s m_auList mem alloc failed "
- "AppleAVD: %s m_curAu layerActive alloc failed"
- "AppleAVD: %s m_curAu mem alloc failed "
- "AppleAVD: %s m_dec_pb_idx mem alloc failed "
- "AppleAVD: %s m_disp_pb_idx mem alloc failed "
- "AppleAVD: %s m_second_dec_pb_idx mem alloc failed "
- "AppleAVD: %s m_spsInfo mem alloc failed "
- "AppleAVD: %s nuh_layer_id > max layer ! %d %d"
- "AppleAVD: %s out of range PPS id %d"
- "AppleAVD: %s out of range SPS id %d"
- "AppleAVD: %s out of range SPS id %u"
- "AppleAVD: %s oversized iv %d"
- "AppleAVD: %s parse NAL error ! %d"
- "AppleAVD: %s parse PPS error ! %d"
- "AppleAVD: %s parse SPS error ! %d"
- "AppleAVD: %s parse VPS error ! %d"
- "AppleAVD: %s retain count is %ld"
- "AppleAVD: %s return with error %d"
- "AppleAVD: %s sending error %d to test app main\n"
- "AppleAVD: %s too many PPS %d"
- "AppleAVD: %s too many SPS %d"
- "AppleAVD: %s too many VPS %d"
- "AppleAVD: %s videoLayerID %d index %d"
- "AppleAVD: %s() - AppleAVDSetParameter kAppleAVDSetEnableMuxedAlpha returned ERROR"
- "AppleAVD: %s() - Disabling decodeToBufferWithAlpha!"
- "AppleAVD: %s() - ERROR! storage is NULL\n"
- "AppleAVD: %s() - setting storage->usageMode to %d\n"
- "AppleAVD: %s() :  ERROR: CVPixelBufferCreate failed refSurfaceListIndx:%d"
- "AppleAVD: %s() :  ERROR: CreateUncompressedPixelBufferAttributesDictionaryRVRA() failed!"
- "AppleAVD: %s() :  ioSurfaceRef for refSurfaceListIndx:%d is NULL!"
- "AppleAVD: %s() : clientID: %2d Error getting decoder buffer!, frameNum : %d"
- "AppleAVD: %s() : clientID: %2d Error getting display buffer!, frameNum : %d"
- "AppleAVD: %s() : clientID: %2d. For AVIFs, only intra-frames are supported, frameNum : %d"
- "AppleAVD: %s() : received reset Before Decoding - Flush DPB, framenumber %d"
- "AppleAVD: %s() Cannot find LongTermPicNumLX %d in refList[%d][%d] and beyond"
- "AppleAVD: %s() Cannot find picNumLX %d for refList[%d][%d]"
- "AppleAVD: %s() ERROR: CryptorSubsampleAuxiliaryData is NULL"
- "AppleAVD: %s() ERROR: crauxNumEntries %ld out of range"
- "AppleAVD: %s() codecType: AV1, %d x %d, session: %p, built %s %s"
- "AppleAVD: %s() codecType: AVC, %d x %d,  session: %p built %s %s"
- "AppleAVD: %s() codecType: AVC, encryptionScheme %d, %d x %d, session: %p"
- "AppleAVD: %s() codecType: AVC, encryptionScheme %d, %d x %d, tryAllFrames = %d, usageMode: %d, session: %p built %s %s"
- "AppleAVD: %s() codecType: Fghrn, encryptionScheme %d, %d x %d, built %s %s"
- "AppleAVD: %s() codecType: Fghrn, encryptionScheme %d, %d x %d, session : %p"
- "AppleAVD: %s() codecType: Fghrn, encryptionScheme %d, %d x %d, tryAllFrames = %d, session : %p, built %s %s"
- "AppleAVD: %s() codecType: HEVC, %d x %d, session: %p, built %s %s"
- "AppleAVD: %s() codecType: HEVC, encryptionScheme %d, %d x %d, session: %p"
- "AppleAVD: %s() codecType: HEVC, encryptionScheme %d, %d x %d, tryAllFrames = %d, usageMode: %d, session: %p, built %s %s"
- "AppleAVD: %s() codecType: Lghrn, encryptionScheme %d, %d x %d, built %s %s"
- "AppleAVD: %s() codecType: Lghrn, encryptionScheme %d, %d x %d, session : %p"
- "AppleAVD: %s() codecType: Lghrn, encryptionScheme %d, %d x %d, tryAllFrames = %d, session : %p, built %s %s"
- "AppleAVD: %s() frameNum %d was not found in flight! Something is wrong"
- "AppleAVD: %s() releaseOneCPB returned %d\n"
- "AppleAVD: %s() slice header parsing error - slice_count: %d - nal_unit_type: %d"
- "AppleAVD: %s() tile[%d] width %d, need at least two CTU wide"
- "AppleAVD: %s() tile[%d] width %d, need at least two CTU wide\n"
- "AppleAVD: %s(), found incomplete progressive sample! Quitting."
- "AppleAVD: %s():  %d %d %d %d %d %d %d %d %d\n"
- "AppleAVD: %s():  fail to create reference picture list - result: %d\n"
- "AppleAVD: %s(): %d %d %d %d - errorStatus %d\n"
- "AppleAVD: %s(): **mismatch** w %d h %d cf %d ybd %d cbd %d nSz %d DpbSz %d vRange %u **new** w %d h %d cf %d ybd %d cbd %d nSz %d DpbSz %d vRange %u"
- "AppleAVD: %s(): AVC pOrigRef is NULL!"
- "AppleAVD: %s(): AVC pScaledRef is NULL!"
- "AppleAVD: %s(): After considering defaults write, setting filmGrainMode to: %d\n"
- "AppleAVD: %s(): AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDSetUsageMode or kAppleAVDEnableRVRA returned ERROR"
- "AppleAVD: %s(): AppleAVD_HEVCDecoder - ERROR setting parameter kAppleAVDSetUsageMode"
- "AppleAVD: %s(): Borage AVD is not supported in this AppleAVD driver!!!"
- "AppleAVD: %s(): BufferPoolId[%d]: Index %d is not in use! in_use: %d\n"
- "AppleAVD: %s(): Cactus AVD is not supported in this AppleAVD driver!!!"
- "AppleAVD: %s(): ChrFmt changed: %d vs %d"
- "AppleAVD: %s(): DecodePicture fail"
- "AppleAVD: %s(): Did not find free slot to evict from cache"
- "AppleAVD: %s(): ERROR :: closeAppleAVDHW_HEVCDecoderInstance returned error %d"
- "AppleAVD: %s(): ERROR failed to set kAppleAVDSetSliceHeaderThreshold to %d"
- "AppleAVD: %s(): ERROR refCount is already 0!!"
- "AppleAVD: %s(): ERROR setting kAppleAVDSetAVDCoreControlPerfWeight failed"
- "AppleAVD: %s(): ERROR setting kAppleAVDSetAllowBitstreamToChangeFrameDimensions failed"
- "AppleAVD: %s(): ERROR setting kAppleAVDSetAv1FilmGrainMode failed"
- "AppleAVD: %s(): ERROR setting kAppleAVDSetCPBCacheBufferSizeFactor failed"
- "AppleAVD: %s(): ERROR setting kAppleAVDSetCPBCacheNumBuffers failed"
- "AppleAVD: %s(): ERROR setting kAppleAVDSetMiscPreferences failed"
- "AppleAVD: %s(): ERROR setting kAppleAVDSetMsrRef failed"
- "AppleAVD: %s(): ERROR setting kAppleAVDSetMultiVPParsing failed"
- "AppleAVD: %s(): ERROR setting kAppleAVDSetOnDemandDVAMap failed"
- "AppleAVD: %s(): ERROR setting kAppleAVDSetSkipVPSExtParsing failed"
- "AppleAVD: %s(): ERROR!  Display index out of range (%d)"
- "AppleAVD: %s(): ERROR! Bad Bitstream! first_slice_segment_in_pic_flag NOT set on slice_count: %d"
- "AppleAVD: %s(): ERROR! Bad Bitstream! first_slice_segment_in_pic_flag set on slice_count: %d"
- "AppleAVD: %s(): ERROR! Couldn't get memInfo (NULL)! currBufIndex: %d"
- "AppleAVD: %s(): ERROR! Couldn't get memInfo (NULL)! refBufIndex: %d - i: %d"
- "AppleAVD: %s(): ERROR! Exceeded buffers to release (%d)"
- "AppleAVD: %s(): ERROR! Failed to decode frame - status (%d)"
- "AppleAVD: %s(): ERROR! Failed to set HandleCRAFrameAsBLA parameter - status %d handleCRAFrameAsBLA %d"
- "AppleAVD: %s(): ERROR! Failed to set parameter kVASetDisableSkipToIDR - status %d"
- "AppleAVD: %s(): ERROR! Failed to set parameter kVASetMuxedAlphaParams - status %d"
- "AppleAVD: %s(): ERROR! Failed to set parameter kVASetTileDecodeParams - status %d"
- "AppleAVD: %s(): ERROR! Failed to set parameter kVASetYUVMD5Hash - status %d"
- "AppleAVD: %s(): ERROR! Invalid parameter(s) m_p_cv_pool: %p - vtSession: %p - vtFrame: %p"
- "AppleAVD: %s(): ERROR! Invalid reference index (%d)"
- "AppleAVD: %s(): ERROR! NULL arguments - in (%p) out (%p)"
- "AppleAVD: %s(): ERROR! NULL decoder! (%p)"
- "AppleAVD: %s(): ERROR! RefIndex %d > ref_pics %d"
- "AppleAVD: %s(): ERROR! RenderSurfaceRefList NULL!! dispBufIndex: %d"
- "AppleAVD: %s(): ERROR! SurfaceRefList NULL!! refBufIndex: %d"
- "AppleAVD: %s(): ERROR! vm_allocate failed! allocStatus: %d - addr: 0x%llx\n"
- "AppleAVD: %s(): ERROR! vm_allocate failed! allocStatus: %d - addr: 0x%lx\n"
- "AppleAVD: %s(): ERROR!!!"
- "AppleAVD: %s(): ERROR: AppleAVDSetParameter:kAppleAVDSetTileCVPixelBufPostProcess failed"
- "AppleAVD: %s(): ERROR: AppleAVDSetParameter:kAppleAVDSetTileCVPixelBufRefDecode failed"
- "AppleAVD: %s(): ERROR: CVPixelBufferCreate failed"
- "AppleAVD: %s(): ERROR: Create layersErrorStatus Failed"
- "AppleAVD: %s(): ERROR: CreateAVDFghrnInstance returned error"
- "AppleAVD: %s(): ERROR: CreateDispPixelBufferAttributesDictionary failed"
- "AppleAVD: %s(): ERROR: CreatePixelBufferAttributesDictionary failed"
- "AppleAVD: %s(): Error (0x%x) creating IOSurfaceAccelerator client."
- "AppleAVD: %s(): Error allocating CPBManager cache"
- "AppleAVD: %s(): Error allocating patch requests list, m_fwPatchRequests=%p, m_fwPatchRequestWriteIndex=%u, m_maxFwPatchRequests=%u"
- "AppleAVD: %s(): Error allocating temp buffer for RVRAInLoopChromaFilter() \n"
- "AppleAVD: %s(): Error deallocating patch requests list"
- "AppleAVD: %s(): Error deallocating patch requests list, m_fwPatchRequests=%p, m_fwPatchRequestWriteIndex=%u, m_maxFwPatchRequests=%u"
- "AppleAVD: %s(): Error initializing m_bf_cond condition variable"
- "AppleAVD: %s(): Error initializing mutex"
- "AppleAVD: %s(): Error! Calling processHWResponse()!"
- "AppleAVD: %s(): Error: NULL decoder"
- "AppleAVD: %s(): Error: Unexpected FG attachment size = %zu. Ignoring it.\n"
- "AppleAVD: %s(): Failed to Create Pixel Buffer Pool! ERROR! CVReturnStatus: 0x%x"
- "AppleAVD: %s(): Failed to allocate buffers!\n"
- "AppleAVD: %s(): Failed to create compressed pixel buffer attributes dictionary! ERROR! Status: 0x%x"
- "AppleAVD: %s(): Failed to create display pixel buffer attributes dictionary! ERROR! Status: 0x%x"
- "AppleAVD: %s(): Failed to create histogram stat buffer! status: 0x%x"
- "AppleAVD: %s(): Failed to create pixel buffer! error: 0x%x\n"
- "AppleAVD: %s(): Failed to create reference pixel buffer attributes dictionary! ERROR! Status: 0x%x"
- "AppleAVD: %s(): Failed to destroy histogram stat buffer! status: 0x%x"
- "AppleAVD: %s(): Failed to get IOSurfaceRef!\n"
- "AppleAVD: %s(): Failed to map pixel buffer! - error: 0x%x\n"
- "AppleAVD: %s(): Failed to set parameter! ERROR! Status: 0x%x"
- "AppleAVD: %s(): FigDerivedObjectCreate failed"
- "AppleAVD: %s(): Forcing panic due to SW timeout.\n"
- "AppleAVD: %s(): Frame# %d DecodeFrame failed with error 0x%08x\n"
- "AppleAVD: %s(): Frame# %d, DecodeFrame failed with decryptError: %d\n"
- "AppleAVD: %s(): FrameReceiver->Emit thread called Invalidate|Finalize!"
- "AppleAVD: %s(): H13A descrambler is not supported\n"
- "AppleAVD: %s(): HEVC pOrigRef is NULL!"
- "AppleAVD: %s(): HEVC pScaledRef is NULL!"
- "AppleAVD: %s(): IOServiceOpen failed %x"
- "AppleAVD: %s(): IOSurfaceGetDataProperty returned error (0x%x). Line = %d\n"
- "AppleAVD: %s(): IOSurfaceSetBulkAttachments2 returned error (0x%x)\n"
- "AppleAVD: %s(): IOSurfaceSetDataProperty returned error (0x%x). Line = %d\n"
- "AppleAVD: %s(): Invalid currBufIndex!"
- "AppleAVD: %s(): Invalid refBufIndex! index: %d"
- "AppleAVD: %s(): Kopsia AVD is not supported in this AppleAVD driver!!!"
- "AppleAVD: %s(): LGH frame header parsing error !"
- "AppleAVD: %s(): Large Scale Tile decoding is not supported!\n"
- "AppleAVD: %s(): Level %d is not defined"
- "AppleAVD: %s(): LilyD AVD is not supported in this AppleAVD driver!!!"
- "AppleAVD: %s(): NULL DECODER type"
- "AppleAVD: %s(): Narcissus AVD is not supported in this AppleAVD driver!!!"
- "AppleAVD: %s(): Outside of current operating range\n"
- "AppleAVD: %s(): ParseHeader unsupported naluLengthSize "
- "AppleAVD: %s(): RVRAInLoopChromaFilter() failed! \n"
- "AppleAVD: %s(): Radish AVD is not supported in this AppleAVD driver!!!"
- "AppleAVD: %s(): RandomAccessSkipPic nal %d poc %d rapoc %d crasbla %d recov %d slice %d frame %d"
- "AppleAVD: %s(): RefPicList0 Missing Reference detected !"
- "AppleAVD: %s(): RefPicList1 Missing Reference detected !"
- "AppleAVD: %s(): Releasing CVPixelBufferRef!\n"
- "AppleAVD: %s(): Requested alloc size is = %zu too big\n"
- "AppleAVD: %s(): Requesting setting filmGrainMode to: %d\n"
- "AppleAVD: %s(): Scaler returned error (0x%x) for the transform.\n"
- "AppleAVD: %s(): Trying to allocate a second buffer without the pool being initialized! Error!\n"
- "AppleAVD: %s(): Unexpected. av1_fb->buffer is 0x0!"
- "AppleAVD: %s(): Unmapping and deallocating CPB cache slot that is still in use!"
- "AppleAVD: %s(): VAStartDecode failed error: %d "
- "AppleAVD: %s(): VPS layers %d not supported"
- "AppleAVD: %s(): VPS parsing error"
- "AppleAVD: %s(): VT Failed to get Pixel Buffer Pool! ERROR!"
- "AppleAVD: %s(): WARNING! Failed to create CFDictionary!"
- "AppleAVD: %s(): WARNING! Failed to create CFType! sessionIdentifier: %p - hist: %p - sessionFrameNumberRef: %p"
- "AppleAVD: %s(): WARNING! index: %d - trying to release! frameNum (%d) < get frameNum (%d), returning early!"
- "AppleAVD: %s(): WARNING! pluginState (%d) was already started! Trying to change kVTDecompressionPropertyKey_SelectPixelFormatWithAlpha"
- "AppleAVD: %s(): WARNING! pluginState (%d) was already started! Trying to change kVTDecompressionPropertyKey_WriteDirectlyToPlanesOfTargetCVPixelBuffer"
- "AppleAVD: %s(): WARNING! vm_deallocate failed! status: 0x%x Check for leaks! addr = 0x%llx - roundedUpSize: 0x%x"
- "AppleAVD: %s(): WARNING! vm_deallocate failed! status: 0x%x Check for leaks! frameNumber: %d - addr = 0x%llx - roundedUpSize: 0x%x"
- "AppleAVD: %s(): WARNING, coded size has changed!"
- "AppleAVD: %s(): WARNING, frame insertion is aborted because pic=NULL\n"
- "AppleAVD: %s(): WARNING, index=%d is invalid, maximum allowable is %d\n"
- "AppleAVD: %s(): Warning! AVD SWR stride (%d, %d) != IOSurface stride (%d, %d). If IOSurface is displayed, output will be corrupted. If YUV is written to file system, no corruption."
- "AppleAVD: %s(): [%4d, %4d] w->dataAddrHi = %08x, from %llx"
- "AppleAVD: %s(): [ERROR] fno: %8d Assign_Cur_Frame_New_FB return NULL"
- "AppleAVD: %s(): about to kAppleAVDSetMiscPreferences, storage->miscPreferences is 0x%x\n"
- "AppleAVD: %s(): all intra frame found, reset m_skipToIdr to false; frm# %d"
- "AppleAVD: %s(): allocOneCPB error (%d)!\n"
- "AppleAVD: %s(): av1_populate_film_grain_params returned false"
- "AppleAVD: %s(): avdDec - Frame# %6d, DecodeFrame failed with error: 0x%x \n"
- "AppleAVD: %s(): bad buffer index %d\n"
- "AppleAVD: %s(): bad ref list0[%d]"
- "AppleAVD: %s(): bad ref list1[%d]"
- "AppleAVD: %s(): bad swr bit depth %d\n"
- "AppleAVD: %s(): bd changed: %d vs %d"
- "AppleAVD: %s(): bit_depth_chroma_minus8 inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d"
- "AppleAVD: %s(): bit_depth_luma_minus8 inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d"
- "AppleAVD: %s(): buff NOT in use! error index %d\n"
- "AppleAVD: %s(): buffer map failed error: %d refSurfaceListIndx:%d\n"
- "AppleAVD: %s(): buffer ref_count is already zero\n"
- "AppleAVD: %s(): calcLumaChromaTileOffset returns fail"
- "AppleAVD: %s(): cannot find PPS"
- "AppleAVD: %s(): cannot find SPS"
- "AppleAVD: %s(): chip id is not used while ecid and/or board id is used\n"
- "AppleAVD: %s(): chroma_format_idc inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d"
- "AppleAVD: %s(): clientID : %2d, #### <WARNING> Frame resolution change not supported frameNum:%d old (%dx%d) new (%dx%d)"
- "AppleAVD: %s(): clientID : %2d, #### <WARNING> Frame resolutions exceed allocated storage frameNum:%d old (%dx%d) new (%dx%d)"
- "AppleAVD: %s(): clientID : %2d, #### <WARNING> frameNum:%d m_cur_pic_info->chroma_format:%d m_orig_chroma_format_idc:%d"
- "AppleAVD: %s(): clientID : %2d, #### <WARNING> frameNum:%d pHeader->BitDepth:%d m_orig_bit_depth_luma_minus8+8:%d"
- "AppleAVD: %s(): clientID : %2d, frameInfoOut is NULL!!!, frameNum:%d"
- "AppleAVD: %s(): clientID : %2d, frameInfoOut is NULL!!!, frameType :%d, frameNum:%d"
- "AppleAVD: %s(): clientID:%2d LGH, reference list creation - invalid reference frames, frameType :%d, frameNum :%d !"
- "AppleAVD: %s(): cmdBuilder->decodeFrameFig returned error: %d \n"
- "AppleAVD: %s(): createDPB fail"
- "AppleAVD: %s(): ctbYSize inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d"
- "AppleAVD: %s(): enter"
- "AppleAVD: %s(): error %d and decoder is %p"
- "AppleAVD: %s(): error allocating surface\n"
- "AppleAVD: %s(): error index %d \n"
- "AppleAVD: %s(): error index %d m_max_cache_size:%d \n"
- "AppleAVD: %s(): error null input buffer"
- "AppleAVD: %s(): error. Line: %d\n"
- "AppleAVD: %s(): error: width (%d) * height (%d) exceeds limit (%llu).\n"
- "AppleAVD: %s(): fail to activate parameter set for slice"
- "AppleAVD: %s(): fail to activate parameter set for slice\n"
- "AppleAVD: %s(): fail to create reference picture list - result: %d\n"
- "AppleAVD: %s(): fail to get probs info for current frame\n"
- "AppleAVD: %s(): failKind = %d"
- "AppleAVD: %s(): failed "
- "AppleAVD: %s(): failed \n"
- "AppleAVD: %s(): failed - error: %d \n"
- "AppleAVD: %s(): failed error: %d \n"
- "AppleAVD: %s(): failed to allocate %d x4 bytes mem for slice->entry_point_offset_minus1"
- "AppleAVD: %s(): failed with error %d\n"
- "AppleAVD: %s(): failed with error %s\n"
- "AppleAVD: %s(): fb->buffer is NULL!!"
- "AppleAVD: %s(): foreError detected!! frameNumber: %d"
- "AppleAVD: %s(): frame %d layerpresent %d layerID %d numLayers %d \n"
- "AppleAVD: %s(): frameNum %d dispIndx %d errorStatus %d allLayersDecodeErr %d multiImageDecodeErr %d - multi-image emit displayCallBack callback\n"
- "AppleAVD: %s(): frameNumber = %d - No free slot found to assign bitstreamIndex."
- "AppleAVD: %s(): frameType :%d "
- "AppleAVD: %s(): frame_header_obu returned -1\n"
- "AppleAVD: %s(): frame_mbs_only_flag inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d"
- "AppleAVD: %s(): frm %8d decoded - frame_to_show w/ nil buffer for buf_idx=%4d"
- "AppleAVD: %s(): height inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d"
- "AppleAVD: %s(): hwD->DecodePicture return %d"
- "AppleAVD: %s(): illegal num_entry_point_offsets %d"
- "AppleAVD: %s(): insertCurPicIntoAuList fail"
- "AppleAVD: %s(): invalid stat crop width/height %d/%d"
- "AppleAVD: %s(): kVTDecompressionPropertyKey_Paravirtualized - paravirtualizedSession: %d"
- "AppleAVD: %s(): kVTDecompressionPropertyKey_SelectPixelFormatWithAlpha storage->decodeToBufferWithAlpha:%d"
- "AppleAVD: %s(): kVTDecompressionPropertyKey_WriteDirectlyToPlanesOfTargetCVPixelBuffer storage->startingPlaneOffset:%d"
- "AppleAVD: %s(): key_func=9, set LK/KEYB\n"
- "AppleAVD: %s(): l0_count + l1_count ==0 !"
- "AppleAVD: %s(): m_num_CPBs_on_the_fly:%d == 0. Cannot release further."
- "AppleAVD: %s(): m_p_buf_pool is NULL \n"
- "AppleAVD: %s(): maxCacheSize (%d) Exceeded 20!\n"
- "AppleAVD: %s(): maxDpbSize inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d"
- "AppleAVD: %s(): mismatch - m_numLayers %d, numLayers %d"
- "AppleAVD: %s(): missing ref - skip RASL picture: %d crasbla %d \n"
- "AppleAVD: %s(): ppRenderSurfaceList[%d] == NULL"
- "AppleAVD: %s(): pps allocation error"
- "AppleAVD: %s(): preconfiguredPixBufAttrs is NULL!"
- "AppleAVD: %s(): propertyValue (%p) is invalid!"
- "AppleAVD: %s(): pthread_cond_timedwait (%d msec)! tryCount: %d"
- "AppleAVD: %s(): rbsp allocation error"
- "AppleAVD: %s(): rbsp parseNAL return error"
- "AppleAVD: %s(): rbsp return invalid bitUsed %d nalL_inBits = %d"
- "AppleAVD: %s(): resolution_change=1, segEn=%d, mi curr %4d x %4d, prev %4d x %4d"
- "AppleAVD: %s(): returning %d (0: reject; 1: accept)"
- "AppleAVD: %s(): separate_colour_plane_flag inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d"
- "AppleAVD: %s(): set KEY(H13)\n"
- "AppleAVD: %s(): set LK/KEYB\n"
- "AppleAVD: %s(): set av1 dual vp mode as %d"
- "AppleAVD: %s(): setDataProperty failed, error=%d\n"
- "AppleAVD: %s(): setDataProperty(AV1FilmGrain) failed, IOSurface look up for ioSurfID 0x%x failed\n"
- "AppleAVD: %s(): show %d, showable %d, filmGrainMode = %d, params_present %d, apply_grain %d, frame %d"
- "AppleAVD: %s(): show_existing - frame_to_show w/ nil buffer for buf_idx=%4d"
- "AppleAVD: %s(): slice count 0"
- "AppleAVD: %s(): sps allocation error"
- "AppleAVD: %s(): spsChanged - bdC-8 : %d vs %d"
- "AppleAVD: %s(): spsChanged - bdY-8 : %d vs %d"
- "AppleAVD: %s(): spsChanged - ch_idc: %d vs %d"
- "AppleAVD: %s(): spsChanged - height: %d vs %d"
- "AppleAVD: %s(): spsChanged - maxBlk: %d vs %d"
- "AppleAVD: %s(): spsChanged - width : %d vs %d"
- "AppleAVD: %s(): tile_group_obu returned error.\n"
- "AppleAVD: %s(): transcryption attempted with incompatible scheme %d"
- "AppleAVD: %s(): unsupported bit stream w %d h %d bd %d %d CtbSizeY %d\n"
- "AppleAVD: %s(): unsupported resolution, Lgh Codec, width : %d, height : %d \n"
- "AppleAVD: %s(): vps allocation error"
- "AppleAVD: %s(): width inconsistent. First SPS = %d. Subsequent SPS with sps_id %d = %d"
- "AppleAVD: %s():clientID: %2d,DecodeError: %d,skipToIDR:%d,frameNum :%d"
- "AppleAVD: %s():clientID: %2d,DecodeError: %d,skipToIDR:%d,frameType: %d,frameNum :%d"
- "AppleAVD: %s, VAMapPixelBuffer returned fail"
- "AppleAVD: %s, error: Trying to map to an index that already has a mapping"
- "AppleAVD: %s: !frame_refs_short_signaling, ref_frame_idx[%d] = %d\n"
- "AppleAVD: %s: 0 byte header size\n"
- "AppleAVD: %s: AV1 Internal bufferpool is full, invalid index %d\n"
- "AppleAVD: %s: Compressed buffers disabled! luma depth %d chroma format %d"
- "AppleAVD: %s: Compressed buffers enabled! CompressionType:%d. luma depth %d chroma format %d"
- "AppleAVD: %s: Corrupted frame. Inter frame requests nonexistent reference.\n"
- "AppleAVD: %s: Corrupted frame. Invalid context_update_tile_id %d \n"
- "AppleAVD: %s: Data ended before all tiles were read.\n"
- "AppleAVD: %s: ERROR, decoder buffer is NULL, no frame will be sent to display"
- "AppleAVD: %s: ERROR, fail to copy data bytes"
- "AppleAVD: %s: ERROR, frame size %llu is probably bogus, pBuff=%p pBuffBegin=%p frameStart=%p\n"
- "AppleAVD: %s: ERROR, obu size can't be larger than size of buffer\n"
- "AppleAVD: %s: ERROR: layer sets do not match! %d, %d\n"
- "AppleAVD: %s: ERROR: layers do not match! %d, %d\n"
- "AppleAVD: %s: For OBU_FRAME type obu tile_start_and_end_present_flag must be 0. \n"
- "AppleAVD: %s: Frame dimensions are larger than the maximum values: width %d height %d\n"
- "AppleAVD: %s: LGH Internal bufferpool is full, invalid index %d\n"
- "AppleAVD: %s: Only 4:4:4, 4:2:2 and 4:2:0 are currently supported, %d %d subsampling is not supported.\n"
- "AppleAVD: %s: Truncated packet or corrupt tile size.\n"
- "AppleAVD: %s: Unsupported bitstream, sRGB colorspace not compatible with specified profile\n"
- "AppleAVD: %s: Unsupported bitstream. Buffer does not contain a decoded frame.\n"
- "AppleAVD: %s: Unsupported bitstream. Identity CICP Matrix incompatible with non 4:4:4 color sampling\n"
- "AppleAVD: %s: Unsupported bitstream. header_size or obu_byte_alignment = -1 or sz < header_size\n"
- "AppleAVD: %s: Unsupported bitstream. seq_header->reduced_still_picture_hdr = %d seq_header->still_picture= %d\n"
- "AppleAVD: %s: Unsupported bitstream. seq_header->seq_level_idx[%d] = %d\n"
- "AppleAVD: %s: Unsupported bitstream. seq_header->seq_level_idx[0] %d\n"
- "AppleAVD: %s: Unsupported bitstream. tile_info not correct\n"
- "AppleAVD: %s: Unsupported profile/bit-depth combination. seq_params->profile %d\n"
- "AppleAVD: %s: VPS doesn't exist to calc rep format!\n"
- "AppleAVD: %s: WARNING _numActivePictures=%d is not valid, now clamped to 0\n"
- "AppleAVD: %s: WARNING, initial_obu_buffer isn't empty like it should\n"
- "AppleAVD: %s: WARNING, no configOBUs[]\n"
- "AppleAVD: %s: Warning, out of memory on line %d\n"
- "AppleAVD: %s: bad swr bit depth %d\n"
- "AppleAVD: %s: begin ref_frame_idx[%d] = %d\n"
- "AppleAVD: %s: bit depth %d not recognized\n"
- "AppleAVD: %s: bit stream buffer too small for annexb obu\n"
- "AppleAVD: %s: bit stream buffer too small for obu\n"
- "AppleAVD: %s: buf %p frame %p size %zu expect at least %d\n"
- "AppleAVD: %s: buffer size %zu expect bigger than %d (two super frame header bytes plus total frame size bytes)\n"
- "AppleAVD: %s: clientID:%2d, LGH, unsupported profile : %d !, frameType :%d, frameNum :%d"
- "AppleAVD: %s: cur and ref frame format mismatch bd %d-%d ssx %d-%d ssy %d-%d\n"
- "AppleAVD: %s: cur_frame pool[%d] = %p/%p\n"
- "AppleAVD: %s: end ref_frame_idx[%d] = %d\n"
- "AppleAVD: %s: error creating rbsp!\n"
- "AppleAVD: %s: expect %02x-%02x-%02x got %02x-%02x-%02x\n"
- "AppleAVD: %s: expect off_to_prot_data to be set when slice header is not byte aligned\n"
- "AppleAVD: %s: extension_header_reserved_3bits must be set to 0. extension_header_reserved_3bits %d\n"
- "AppleAVD: %s: fail to get bitdepth from parsed header\n"
- "AppleAVD: %s: fail to get chroma format idc from parsed header\n"
- "AppleAVD: %s: fail to init picture\n"
- "AppleAVD: %s: fail to read annexb obu header and payload length\n"
- "AppleAVD: %s: fail to read obu size\n"
- "AppleAVD: %s: failed to get bitdepth from parsed header\n"
- "AppleAVD: %s: failed to get chroma format idc from parsed header\n"
- "AppleAVD: %s: fb refcnt\n"
- "AppleAVD: %s: frame marker expect 2 got %x\n"
- "AppleAVD: %s: frame_to_show pool[%d] = %p/%p\n"
- "AppleAVD: %s: inconsistent super frame header %x %x\n"
- "AppleAVD: %s: invalid delta lf res %d\n"
- "AppleAVD: %s: invalid frame to show map idx %d\n"
- "AppleAVD: %s: invalid hdr %p buffer pointer %p pool %p\n"
- "AppleAVD: %s: invalid input parameter\n"
- "AppleAVD: %s: invalid out_length %d\n"
- "AppleAVD: %s: invalid ref_frame_idx[%d] %d\n"
- "AppleAVD: %s: invalid reference buffer %d\n"
- "AppleAVD: %s: invalid restoration unit size for Y plane %d\n"
- "AppleAVD: %s: m_buf_len should > 1 byte because there is extension header. m_buf_len = %lu\n"
- "AppleAVD: %s: m_frame_refs[%d] pool[%d] = %p/%p\n"
- "AppleAVD: %s: max allow tiles %d got %d, tile rows : %d, tile cols : %d\n"
- "AppleAVD: %s: need frame context %p and header %p\n"
- "AppleAVD: %s: need one extra byte for obu header\n"
- "AppleAVD: %s: need one extra byts for obu header extension\n"
- "AppleAVD: %s: no frame buffer available\n"
- "AppleAVD: %s: no reference frame has valid dimensions\n"
- "AppleAVD: %s: none zero marker bit\n"
- "AppleAVD: %s: none zero reserved bit\n"
- "AppleAVD: %s: num_units_in_display_tick and time_scale must be greater than 0. num_units_in_display_tick %d time_scale %d\n"
- "AppleAVD: %s: obu forbidden bit shuld not be set\n"
- "AppleAVD: %s: obu_reserved_1bit must be set to 0. obu_reserved_1bit %d\n"
- "AppleAVD: %s: parse av1 header error\n"
- "AppleAVD: %s: parsing error, wrong tile start"
- "AppleAVD: %s: pool[%d] = %p\n"
- "AppleAVD: %s: raw obu must have size field\n"
- "AppleAVD: %s: ref frame map\n"
- "AppleAVD: %s: ref_frame_idx[%d] = %d, pool[%d] = %p/%p\n"
- "AppleAVD: %s: ref_frame_map[%d] %p ref_count %d\n"
- "AppleAVD: %s: ref_frame_map[%d] pool[%d] = %p/%p\n"
- "AppleAVD: %s: reset all ref_frame_idx to AV1_INVALID_IDX for key frame\n"
- "AppleAVD: %s: skip m_bool_max_bits %d - m_bits_left %d\n"
- "AppleAVD: %s: subsampling x/y %d/%d, unsupported chroma format idc\n"
- "AppleAVD: %s: tg_end (%d) must be greater than or equal to tg_start (%d) \n"
- "AppleAVD: %s: tg_end (%d) must be less than NumTiles (%d) \n"
- "AppleAVD: %s: tg_start (%d) must be equal to %d \n"
- "AppleAVD: %s: tile %d offset %lu size %lu corrupted\n"
- "AppleAVD: %s: total frame size plus super frame index size %d not equal to buffer size %zu\n"
- "AppleAVD: %s: um_ticks_per_picture_minus_1 cannot be (1 << 32) − 1. num_ticks_per_picture_minus_1 %d\n"
- "AppleAVD: %s: unsupported profile %d\n"
- "AppleAVD: %s: value %d out of range!\n"
- "AppleAVD: %s: vpsext->vps_num_target_opt_layer_id_lists[%d] == 0\n"
- "AppleAVD: %s: vpsext->vps_num_target_opt_layer_id_lists[0] == 0\n"
- "AppleAVD: -- recover from error in KeyFrame -- slice[%4d].naluTupe = %d"
- "AppleAVD: <WARNING> %s(): h->req.a.da.DecAddrYSize.val = %d"
- "AppleAVD: <WARNING> %s(): h->req.a.da.RefAddrYSize.val = %d"
- "AppleAVD: ASSERT @ %s() :: Line %d Assert Broken \n"
- "AppleAVD: AVC pps.num_slice_groups_minus1 = %d (shall be 0) %s\n"
- "AppleAVD: AVC sps.frame_mbs_only_flag = %d (shall be 1) %s\n"
- "AppleAVD: AVC sps.level_idc = %d (max is %d) %s\n"
- "AppleAVD: AVC sps[%d] width %d height %d over size in %s\n"
- "AppleAVD: AVC_Decoder::ParseHeader unsupported naluLengthSize "
- "AppleAVD: AVD Fghrn dump: could not open file %s\n"
- "AppleAVD: AVD Fghrn dump: could not open property log file %s\n"
- "AppleAVD: AVD Lghrn dump: could not open file %s\n"
- "AppleAVD: AVD Lghrn dump: could not open property log file %s\n"
- "AppleAVD: AVD h264 dump: could not open file %s\n"
- "AppleAVD: AVD h264 dump: could not open post DRM file %s\n"
- "AppleAVD: AVD h264 dump: could not open pre DRM file %s\n"
- "AppleAVD: AVD h264 dump: could not open property log file %s\n"
- "AppleAVD: AVD hevc dump: could not open file %s\n"
- "AppleAVD: AVD hevc dump: could not open post DRM file %s\n"
- "AppleAVD: AVD hevc dump: could not open pre DRM file %s\n"
- "AppleAVD: AVD hevc dump: could not open property log file %s\n"
- "AppleAVD: AVD hevc histogram dump: could not open file %s\n"
- "AppleAVD: AVDFrameReceiver ERROR: receiver->Setup failed."
- "AppleAVD: AVDFrameReceiver ERROR: runLoopRef NULL\n"
- "AppleAVD: AppleAVD::RVRAScaler returned error:%d \n"
- "AppleAVD: AppleAVD::scaleOutputFrame unlockSurface Dest returned error %d\n"
- "AppleAVD: AppleAVD::scaleOutputFrame unlockSurface Src returned error %d\n"
- "AppleAVD: AppleAVD::scaleOutputFrame unlockSurface returned error %d\n"
- "AppleAVD: AppleAVD::scaleOutputFrame unsupported vra type"
- "AppleAVD: AppleAVDDecodeFrame - frame # %d metadataDict attached\n"
- "AppleAVD: AppleAVDDecodeFrame could not get display buffer from buffer pool"
- "AppleAVD: AppleAVDDecodeFrame could not get reference buffer from buffer pool"
- "AppleAVD: AppleAVDDecodeFrame could not get scaler buffer from buffer pool"
- "AppleAVD: AppleAVDDecodeFrame could not put decode/reference buffer into the buffer pool"
- "AppleAVD: AppleAVDDecodeFrame could not put display buffer into the buffer pool"
- "AppleAVD: AppleAVDDecodeFrameInternal failed\n"
- "AppleAVD: AppleAVDDecodeFrameResponse kVASetSkipToNextIDR error: %d"
- "AppleAVD: AppleAVDDecodeFrameResponse() failed - decryptError: %d \n"
- "AppleAVD: AppleAVDOpenConnection - CreateAVDFrameReceiver failed %x"
- "AppleAVD: AppleAVDUserClient::createDecoder kVASetUsageMode error: %d \n"
- "AppleAVD: AppleAVDWrapperFghrnDecoderDecodeFrame - ERROR! storage is NULL\n"
- "AppleAVD: AppleAVDWrapperFghrnDecoderStartSession: storage->miscPreferences %d "
- "AppleAVD: AppleAVDWrapperH264DecoderDecodeFrame - AppleAVDSetParameter kAppleAVDEnableIOFence returned ERROR"
- "AppleAVD: AppleAVDWrapperH264DecoderDecodeFrame - AppleAVDSetParameter kAppleAVDSetUsageMode or kAppleAVDEnableRVRA returned ERROR"
- "AppleAVD: AppleAVDWrapperH264DecoderDecodeFrame - ERROR! storage is NULL\n"
- "AppleAVD: AppleAVDWrapperH264DecoderDecodeFrameWithOptions - ERROR! storage is NULL\n"
- "AppleAVD: AppleAVDWrapperH264DecoderDecodeTile - ERROR! storage is NULL\n"
- "AppleAVD: AppleAVDWrapperHEVCDecoderCreateInstance - encryptionScheme %d\n"
- "AppleAVD: AppleAVDWrapperHEVCDecoderDecodeFrame - ERROR! storage is NULL\n"
- "AppleAVD: AppleAVDWrapperHEVCDecoderDecodeFrameWithOptions - ERROR! storage is NULL\n"
- "AppleAVD: AppleAVDWrapperHEVCDecoderDecodeTile - ERROR! storage is NULL\n"
- "AppleAVD: AppleAVDWrapperLghrnDecoderDecodeFrame - ERROR! storage is NULL\n"
- "AppleAVD: AppleAVDWrapperLghrnDecoderStartSession: storage->miscPreferences %d "
- "AppleAVD: AppleAVD_FghVideoDecoder ERROR: kAppleAVDMemCacheMode set failed"
- "AppleAVD: AppleAVD_FghVideoDecoder_DecodeFrame ERROR: framenum %d decryptError %x"
- "AppleAVD: AppleAVD_FghVideoDecoder_DecodeFrame ERROR: framenum %d kVTVideoDecoderMalfunctionErr"
- "AppleAVD: AppleAVD_FghVideoDecoder_DecodeTile ERROR: framenum %d kVTVideoDecoderMalfunctionErr"
- "AppleAVD: AppleAVD_FghrnDecoder - AppleAVDDeviceType returned ERROR"
- "AppleAVD: AppleAVD_FghrnDecoder - AppleAVDSetParameter kAppleAVDSetTaggedBufGroupArray returned ERROR"
- "AppleAVD: AppleAVD_FghrnDecoder - ERROR closing connection"
- "AppleAVD: AppleAVD_FghrnDecoder - ERROR setting parameter kAppleAVDPostEmitCleanUpCallBack"
- "AppleAVD: AppleAVD_FghrnDecoder - ERROR setting parameter kAppleAVDSetParavirtualizedSession"
- "AppleAVD: AppleAVD_FghrnDecoder - ERROR terminate decoder"
- "AppleAVD: AppleAVD_FghrnDecoder ERROR: kAppleAVDGetSequenceParams : Could not get Params"
- "AppleAVD: AppleAVD_FghrnVideoDecoder  %d %d %d %d %d %d %d %d %d %d %d\n"
- "AppleAVD: AppleAVD_FghrnVideoDecoder ERROR, there's no frame to decode\n"
- "AppleAVD: AppleAVD_FghrnVideoDecoder ERROR: AppleAVDInitializeDecoder : init decoder device"
- "AppleAVD: AppleAVD_FghrnVideoDecoder ERROR: Slice Offset = %d < %d is invalid\n"
- "AppleAVD: AppleAVD_FghrnVideoDecoder ERROR: Unsupported picture size!"
- "AppleAVD: AppleAVD_FghrnVideoDecoder ERROR: createAppleAVDHW_FghrnDecoderInstance returned error"
- "AppleAVD: AppleAVD_H264Decoder - AppleAVDSetParameter kAppleAVDEnableRVRA returned ERROR"
- "AppleAVD: AppleAVD_H264Decoder - ERROR closing connection"
- "AppleAVD: AppleAVD_H264Decoder - ERROR setting parameter kAppleAVDPostEmitCleanUpCallBack"
- "AppleAVD: AppleAVD_H264Decoder - ERROR setting parameter kAppleAVDSetParavirtualizedSession"
- "AppleAVD: AppleAVD_H264Decoder - ERROR terminate decoder"
- "AppleAVD: AppleAVD_H264VideoDecoder - AppleAVDSetParameter kAppleAVDHandleCRAFrameAsBLA returned ERROR"
- "AppleAVD: AppleAVD_H264VideoDecoder ERROR: AppleAVDSetSPSWidthHeight : Could not set SetSPSWidthHeight"
- "AppleAVD: AppleAVD_H264VideoDecoder ERROR: BAD encryptedSliceCount %d MAX_SLICES %d"
- "AppleAVD: AppleAVD_H264VideoDecoder ERROR: SeqAndPicParamSetFromImageDescExt returned error"
- "AppleAVD: AppleAVD_H264VideoDecoder ERROR: Unsupported picture size!"
- "AppleAVD: AppleAVD_H264VideoDecoder ERROR: createAppleAVDHW_H264DecoderInstance returned error"
- "AppleAVD: AppleAVD_H264VideoDecoder ERROR: kAppleAVDMemCacheMode set failed"
- "AppleAVD: AppleAVD_H264VideoDecoder ERROR: kAppleAVDSetTryEveryFrame set failed"
- "AppleAVD: AppleAVD_H264VideoDecoder: AppleAVDCheckPlatform() returns false. Unusual, but we can proceed assuming AVC L6 is not supported.\n"
- "AppleAVD: AppleAVD_H264VideoDecoder: frame# %d, Could not set kAppleAVDSetCryptScheme, err %d\n"
- "AppleAVD: AppleAVD_H264VideoDecoder: frame# %d, new CVPixelBufferPool created protectionOptions %llu %llu \n"
- "AppleAVD: AppleAVD_H264VideoDecoder_DecodeFrame ERROR: framenum %d decryptError %x"
- "AppleAVD: AppleAVD_H264VideoDecoder_DecodeFrame ERROR: framenum %d kVTVideoDecoderMalfunctionErr"
- "AppleAVD: AppleAVD_HEVCDecoder - AppleAVDDeviceType returned ERROR"
- "AppleAVD: AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDEnableRVRA returned ERROR"
- "AppleAVD: AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDExtraInloopFilter returned ERROR"
- "AppleAVD: AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDHandleCRAFrameAsBLA returned ERROR"
- "AppleAVD: AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDMultiViewDecodeClient returned ERROR"
- "AppleAVD: AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDSetEnableMuxedAlpha returned ERROR"
- "AppleAVD: AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDSetMuxedAlphaStartingPlaneOffset returned ERROR"
- "AppleAVD: AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDSetTaggedBufGroupArray returned ERROR"
- "AppleAVD: AppleAVD_HEVCDecoder - ERROR closing connection"
- "AppleAVD: AppleAVD_HEVCDecoder - ERROR opening kernel connection"
- "AppleAVD: AppleAVD_HEVCDecoder - ERROR setting parameter kAppleAVDDisplayCallBack"
- "AppleAVD: AppleAVD_HEVCDecoder - ERROR setting parameter kAppleAVDFIGUserRefCon"
- "AppleAVD: AppleAVD_HEVCDecoder - ERROR setting parameter kAppleAVDPostEmitCleanUpCallBack"
- "AppleAVD: AppleAVD_HEVCDecoder - ERROR setting parameter kAppleAVDSetOutputFileName"
- "AppleAVD: AppleAVD_HEVCDecoder - ERROR setting parameter kAppleAVDSetParavirtualizedSession"
- "AppleAVD: AppleAVD_HEVCDecoder - ERROR terminate decoder"
- "AppleAVD: AppleAVD_HEVCDecoder - setting parameter kAppleAVDMultiViewDecodeClient %d "
- "AppleAVD: AppleAVD_HEVCDecoder ERROR: AppleAVDInitializeDecoder : init decoder device"
- "AppleAVD: AppleAVD_HEVCDecoder ERROR: Unsupported picture size!"
- "AppleAVD: AppleAVD_HEVCDecoder ERROR: kAppleAVDGetNumLayersMultiViewClient : Could not get Params"
- "AppleAVD: AppleAVD_HEVCDecoder ERROR: kAppleAVDGetSequenceParams : Could not get Params"
- "AppleAVD: AppleAVD_HEVCDecoder: Cannot use type of %p %p"
- "AppleAVD: AppleAVD_HEVCDecoder: cannot convert number %p %p"
- "AppleAVD: AppleAVD_HEVCTileDecoder_DecodeFrame ERROR: framenum %d kVTVideoDecoderMalfunctionErr"
- "AppleAVD: AppleAVD_HEVCVideoDecoder ERROR: AppleAVDSetParameter:kAppleAVDSetTileCVPixelBufRefDecode failed"
- "AppleAVD: AppleAVD_HEVCVideoDecoder ERROR: AppleAVDSetSPSWidthHeight : Could not set SetSPSWidthHeight"
- "AppleAVD: AppleAVD_HEVCVideoDecoder ERROR: BAD encryptedSliceCount %zd MAX_SLICES %d"
- "AppleAVD: AppleAVD_HEVCVideoDecoder ERROR: CVPixelBufferCreate failed"
- "AppleAVD: AppleAVD_HEVCVideoDecoder ERROR: Could not get bitstream buffer"
- "AppleAVD: AppleAVD_HEVCVideoDecoder ERROR: Could not get getMultiViewLayerOffsetInfo"
- "AppleAVD: AppleAVD_HEVCVideoDecoder ERROR: CreateAVDHEVCInstance returned error"
- "AppleAVD: AppleAVD_HEVCVideoDecoder ERROR: CreateDispPixelBufferAttributesDictionary failed"
- "AppleAVD: AppleAVD_HEVCVideoDecoder ERROR: CreatePixelBufferAttributesDictionary failed"
- "AppleAVD: AppleAVD_HEVCVideoDecoder ERROR: kAppleAVDMemCacheMode set failed"
- "AppleAVD: AppleAVD_HEVCVideoDecoder ERROR: kAppleAVDSetNoSecondWrite: Could not set NoSecondWrite Flag!"
- "AppleAVD: AppleAVD_HEVCVideoDecoder ERROR: kAppleAVDSetTryEveryFrame set failed"
- "AppleAVD: AppleAVD_HEVCVideoDecoder Error:: CFDictionaryCreate (sHEVCVideoDecoderSupportedPropertyDictionary) failed"
- "AppleAVD: AppleAVD_HEVCVideoDecoder Error:: CFDictionaryCreate - HEVCVideoDecoder_CopySupportedPropertyDictionary- failed.\n"
- "AppleAVD: AppleAVD_HEVCVideoDecoder enableFileDump %d"
- "AppleAVD: AppleAVD_HEVCVideoDecoder: frame# %d, Could not set kAppleAVDSetCryptScheme, err %d\n"
- "AppleAVD: AppleAVD_HEVCVideoDecoder: frame# %d, new CVPixelBufferPool created protectionOptions %llu %llu \n"
- "AppleAVD: AppleAVD_HEVCVideoDecoder_DecodeFrame ERROR: framenum %d decryptError %x"
- "AppleAVD: AppleAVD_HEVCVideoDecoder_DecodeFrame ERROR: framenum %d kVTVideoDecoderMalfunctionErr"
- "AppleAVD: AppleAVD_LghVideoDecoder ERROR: BAD encryptedSliceCount %ld MAX_SLICES %d"
- "AppleAVD: AppleAVD_LghVideoDecoder ERROR: kAppleAVDMemCacheMode set failed"
- "AppleAVD: AppleAVD_LghVideoDecoder_DecodeFrame ERROR: framenum %d decryptError %x"
- "AppleAVD: AppleAVD_LghVideoDecoder_DecodeFrame ERROR: framenum %d kVTVideoDecoderMalfunctionErr"
- "AppleAVD: AppleAVD_LghrnDecoder - ERROR closing connection"
- "AppleAVD: AppleAVD_LghrnDecoder - ERROR setting parameter kAppleAVDPostEmitCleanUpCallBack"
- "AppleAVD: AppleAVD_LghrnDecoder - ERROR setting parameter kAppleAVDSetParavirtualizedSession"
- "AppleAVD: AppleAVD_LghrnDecoder - ERROR terminate decoder"
- "AppleAVD: AppleAVD_LghrnVideoDecoder ERROR: Unsupported picture size!"
- "AppleAVD: AppleAVD_LghrnVideoDecoder ERROR: createAppleAVDHW_LghrnDecoderInstance returned error"
- "AppleAVD: AppleAVD_LgrnVideoDecoder: frame# %d, Could not set kAppleAVDSetCryptScheme, err %d\n"
- "AppleAVD: Bad NAL type %d\n"
- "AppleAVD: Bad NAL type %d. Skipping.\n"
- "AppleAVD: CAVDAvcDecoder::DecodeGetRenderTargetRef rvra scaler backup buffers are not allocated!"
- "AppleAVD: CAVDAvcDecoder::DecodeGetRenderTargetRef rvra scaler buffers are not allocated!"
- "AppleAVD: CAVDHevcDecoder::DecodeGetRenderTargetRef rvra scaler backup buffers are not allocated!"
- "AppleAVD: CAVDHevcDecoder::DecodeGetRenderTargetRef rvra scaler buffers are not allocated!"
- "AppleAVD: CAVDHevcDecoder::VAGetIOSurfaceIDForBufferIndex couldn't resolve index\n"
- "AppleAVD: CAVDMvHevcDecoder: Not supported!"
- "AppleAVD: CreateAVDFghrnInstance ERROR: kAppleAVDSetTryEveryFrame set failed"
- "AppleAVD: CreateAVDLghrnInstance ERROR: kAppleAVDSetTryEveryFrame set failed"
- "AppleAVD: ERROR : vps base layer %d, available %d"
- "AppleAVD: ERROR : vps->vps_layer_id_in_nuh[i] %d, vps->vps_layer_id_in_nuh[i-1] %d"
- "AppleAVD: ERROR, config record is too short\n"
- "AppleAVD: ERROR, invalid marker bit and/or version number\n"
- "AppleAVD: ERROR, invalid profile\n"
- "AppleAVD: ERROR, unsupported chroma format %d\n"
- "AppleAVD: ERROR, unsupported profile %d\n"
- "AppleAVD: ERROR:  either dataBuffer=%p is invalid or dataLength=%zu is invalid!"
- "AppleAVD: ERROR:  either tile dataBuffer=%p is invalid or dataLength=%u is invalid!"
- "AppleAVD: ERROR:  either tile dataBuffer=%p is invalid or dataLength=%zu is invalid!"
- "AppleAVD: ERROR: %s called on plugin in state %d"
- "AppleAVD: ERROR: %s no instance storage!"
- "AppleAVD: ERROR: %s() - AppleAVD Foghorn codec registration FAILED\n"
- "AppleAVD: ERROR: %s() - AppleAVD H264 codec registration FAILED\n"
- "AppleAVD: ERROR: %s() - AppleAVD HEVC codec registration FAILED. CheckPlatform 0x%llx\n"
- "AppleAVD: ERROR: %s() - AppleAVD Leghorn codec registration FAILED\n"
- "AppleAVD: ERROR: %s() - AppleAVDCheckPlatform() returned error %d\n"
- "AppleAVD: ERROR: %s() - AppleAVDGetParameter call for kAppleAVDGetFrameReceiverThreadPriority returned ERROR\n"
- "AppleAVD: ERROR: %s() - AppleAVDSetParameter call for kAppleAVDEnableIOFence returned ERROR\n"
- "AppleAVD: ERROR: %s() - AppleAVDSetParameter call for kAppleAVDEnableRVRA returned ERROR\n"
- "AppleAVD: ERROR: %s() - AppleAVDSetParameter call for kAppleAVDExtraInloopFilter returned ERROR\n"
- "AppleAVD: ERROR: %s() - AppleAVDSetParameter call for kAppleAVDSetAttachQPs returned ERROR\n"
- "AppleAVD: ERROR: %s() - AppleAVDSetParameter call for kAppleAVDSetAv1FilmGrainMode returned ERROR\n"
- "AppleAVD: ERROR: %s() - AppleAVDSetParameter call for kAppleAVDSetMVAV1DisplayLayerIDs returned ERROR\n"
- "AppleAVD: ERROR: %s() - AppleAVDSetParameter call for kAppleAVDSetMVHEVCDisplayLayerIDs returned ERROR\n"
- "AppleAVD: ERROR: %s() - AppleAVDSetParameter call for kAppleAVDSetUsageMode returned ERROR\n"
- "AppleAVD: ERROR: %s() - AppleAVDSetParameter call for kAppleAVDSetVRADimensions returned ERROR\n"
- "AppleAVD: ERROR: %s() - AppleAVDSetParameter call for kAppleAVDSetVRAType returned ERROR\n"
- "AppleAVD: ERROR: %s() - Non-mod16 VRA dimensions with width %d, height %d\n"
- "AppleAVD: ERROR: %s() - RequestedMVHEVCVideoLayerIDs not set ERROR\n"
- "AppleAVD: ERROR: %s() - Sync Decode not enabled for FT chroma deblocking filter\n"
- "AppleAVD: ERROR: %s() - infoDict creation failed!\n"
- "AppleAVD: ERROR: %s() - trying to set kAppleAVDExtraInloopFilter before videoContext was created!\n"
- "AppleAVD: ERROR: %s() - trying to set kAppleAVDSetVRADimensions before videoContext was created!\n"
- "AppleAVD: ERROR: %s() Line %d: %s mismatch b/w %s %d and %s %d"
- "AppleAVD: ERROR: %s() Line %d: Error allocating %s"
- "AppleAVD: ERROR: %s() Line %d: RNG_CHECK failed for %s x %d low %d up %d\n"
- "AppleAVD: ERROR: %s() [line %u]: Failed to get slice data memInfo struct (slice %d)\n"
- "AppleAVD: ERROR: %s(): AVCSupported is not CFNumberType!\n"
- "AppleAVD: ERROR: %s(): AVD decoder null\n"
- "AppleAVD: ERROR: %s(): Allocating new AppleAVDCommandBuilder failed\n"
- "AppleAVD: ERROR: %s(): AppleAVDCreateDecodeDeviceInternal failed: %d"
- "AppleAVD: ERROR: %s(): AppleAVDGetParameter [kAppleAVDGetCompressedPictureBuffer] failed with %d\n"
- "AppleAVD: ERROR: %s(): AppleAVDSetParameter [kAppleAVDSetTileCVPixelBufRefDecode] failed with %d\n"
- "AppleAVD: ERROR: %s(): AppleAVDSubmitDecodeCMD failed: %d \n"
- "AppleAVD: ERROR: %s(): Asking fig to drop frame # %d with err %d - internalStatus: %d\n"
- "AppleAVD: ERROR: %s(): Bad Bitstream, failed with %d\n"
- "AppleAVD: ERROR: %s(): Bad Bitstream, is_sf_frame = %d\n"
- "AppleAVD: ERROR: %s(): Bad input size %d > allocated size (%d)"
- "AppleAVD: ERROR: %s(): CVPixelBufferCreate failed with %d\n"
- "AppleAVD: ERROR: %s(): Cannot initialize condition variable, Error = %d"
- "AppleAVD: ERROR: %s(): Cannot initialize mutex, Error = %d"
- "AppleAVD: ERROR: %s(): Could not retrieve support bits from CFNumberRef!\n"
- "AppleAVD: ERROR: %s(): Couldn't get AVCSupported property from IORegistry!\n"
- "AppleAVD: ERROR: %s(): Create CPBManager Failed"
- "AppleAVD: ERROR: %s(): ERROR, bit depth %d exceeds allocated depth 0\n"
- "AppleAVD: ERROR: %s(): ERROR, video resolution %ux%u exceeds allocated size %ux%u\n"
- "AppleAVD: ERROR: %s(): Error creating LGH parser!\n"
- "AppleAVD: ERROR: %s(): Error getting second decoder buffer for scaling! (frameNum :%d)"
- "AppleAVD: ERROR: %s(): Failed to add %s %s buffer to patch list\n"
- "AppleAVD: ERROR: %s(): Failed to allocate m_decodeBufferMemInfo[%d]! Got %d\n"
- "AppleAVD: ERROR: %s(): Failed to allocate members (error = %u)!\n"
- "AppleAVD: ERROR: %s(): Failed to copy data bytes (err = %d), nothing to decode\n"
- "AppleAVD: ERROR: %s(): Failed to create HW Decoder object!\n"
- "AppleAVD: ERROR: %s(): Failed to create RLM\n"
- "AppleAVD: ERROR: %s(): Failed to create rlm!\n"
- "AppleAVD: ERROR: %s(): Failed to get an available buffer after %d attempts!\n"
- "AppleAVD: ERROR: %s(): Failed to get slice data memInfo struct (slice %d)\n"
- "AppleAVD: ERROR: %s(): Failed to initialize HW Decoder object!\n"
- "AppleAVD: ERROR: %s(): Failed to properly convert Pixel Buffer Format CFNumber to an integer!\n"
- "AppleAVD: ERROR: %s(): Failed to retrieve data buffer from sampleBuffer\n"
- "AppleAVD: ERROR: %s(): Failed to retrieve kVTDecompressionResolutionKey_Height from dictionary\n"
- "AppleAVD: ERROR: %s(): Failed to retrieve kVTDecompressionResolutionKey_Width from dictionary\n"
- "AppleAVD: ERROR: %s(): Failed to set usage mode parameter - status %d usageMode %d\n"
- "AppleAVD: ERROR: %s(): Failed to successfully retrieve support bits! (error = %d)\n"
- "AppleAVD: ERROR: %s(): Failed with error = %d"
- "AppleAVD: ERROR: %s(): FigBlockBufferCopyDataBytes failed with %d\n"
- "AppleAVD: ERROR: %s(): FigCPECryptorCreateProcessedBlockBufferAndSubsampleAuxiliaryDataWithOptions returned error %d\n"
- "AppleAVD: ERROR: %s(): HW Decoder failed to allocate decodeBuffer!\n"
- "AppleAVD: ERROR: %s(): IOIteratorNext failed!\n"
- "AppleAVD: ERROR: %s(): IOMainPort failed! (error = %d)\n"
- "AppleAVD: ERROR: %s(): IOServiceGetMatchingServices failed! (error = %d)\n"
- "AppleAVD: ERROR: %s(): IOSurface is too small for detiling (plane %d) - detiled dimensions: [%d x %d], IOSurface: [%zu x %zu]\n"
- "AppleAVD: ERROR: %s(): IOSurface is too small for tiling (plane %d): detiled dimensions - [%d x %d], IOSurface: [%zu x %zu]\n"
- "AppleAVD: ERROR: %s(): Initialization of decoder object failed with %u\n"
- "AppleAVD: ERROR: %s(): Invalid AVD device type %d!\n"
- "AppleAVD: ERROR: %s(): Invalid dispbufIndex=%u or ctx->pBufferPool[poolIndex=%u] is NULL!, ctx->noSecondWrite %d"
- "AppleAVD: ERROR: %s(): MUXED_ALPHA_CHROMA_SCRATCH_BUFF_INDEX map failed error: %d\n"
- "AppleAVD: ERROR: %s(): NULL context!\n"
- "AppleAVD: ERROR: %s(): NULL sampleBuffer from the context!\n"
- "AppleAVD: ERROR: %s(): NULL uncompressed header!\n"
- "AppleAVD: ERROR: %s(): RVRA_FIRST_BACKUP_BUFF_INDEX map failed: %d \n"
- "AppleAVD: ERROR: %s(): RVRA_SECOND_BACKUP_BUFF_INDEX map failed: %d \n"
- "AppleAVD: ERROR: %s(): Registration for %c%c%c%c failed with status %d\n"
- "AppleAVD: ERROR: %s(): Retrieved kCVPixelBufferPixelFormatTypeKey entry was not a CFNumber or CFArray!\n"
- "AppleAVD: ERROR: %s(): Timed out, waited at least %llums! m_num_CPBs_on_the_fly=%u timeoutMS=%llu"
- "AppleAVD: ERROR: %s(): Unrecognized pixel buffer format: %c%c%c%c - defaulting to kIOSurfaceCompressionTypeNone\n"
- "AppleAVD: ERROR: %s(): VTDecoderSessionCopyResolvedPixelBufferAttributes failed with %d\n"
- "AppleAVD: ERROR: %s(): [layer %d] Failed to allocate m_dec_pb_idx!\n"
- "AppleAVD: ERROR: %s(): [layer %d] Failed to allocate m_disp_pb_idx!\n"
- "AppleAVD: ERROR: %s(): [layer %d] Failed to allocate m_second_dec_pb_idx!\n"
- "AppleAVD: ERROR: %s(): [layer %d] Failed to create HW Decoder object!\n"
- "AppleAVD: ERROR: %s(): [layer %d] Failed to initialize HW Decoder object!\n"
- "AppleAVD: ERROR: %s(): [layer %d] HW Decoder failed to allocate decodeBuffer!\n"
- "AppleAVD: ERROR: %s(): [layer %d] error creating rlm!\n"
- "AppleAVD: ERROR: %s(): allLayersDecodeErr = %d, finalTagBufErr = %d\n"
- "AppleAVD: ERROR: %s(): allocateMultiViewHwDecoders failed with %u\n"
- "AppleAVD: ERROR: %s(): createPixelBufferAttributesDictionary failed with %d\n"
- "AppleAVD: ERROR: %s(): cryptor has NULL createProcessedBlockBufferAndSubsampleAuxiliaryDataWithOptions entry in vTable!\n"
- "AppleAVD: ERROR: %s(): decode buffer at index %d is NULL!\n"
- "AppleAVD: ERROR: %s(): decodeGetRenderTarget returned fail"
- "AppleAVD: ERROR: %s(): encryptedSliceCount (%d) exceeds MAX_SLICES (%d)\n"
- "AppleAVD: ERROR: %s(): encryptedSliceCount (%ld) exceeds MAX_SLICES (%d)\n"
- "AppleAVD: ERROR: %s(): encryption mode 'eavc' is no longer supported\n"
- "AppleAVD: ERROR: %s(): error creating parser!\n"
- "AppleAVD: ERROR: %s(): error creating rlm!\n"
- "AppleAVD: ERROR: %s(): error deallocating AVD surface index %d from pool %u\n"
- "AppleAVD: ERROR: %s(): failed cmdBuilder->createDecoder!\n"
- "AppleAVD: ERROR: %s(): failed error: %d \n"
- "AppleAVD: ERROR: %s(): frame# %d, AppleAVDSetParameter [kAppleAVDSetCryptRef] failed with %d\n"
- "AppleAVD: ERROR: %s(): frame# %d, AppleAVDSetParameter [kAppleAVDSetCryptScheme] failed with %d\n"
- "AppleAVD: ERROR: %s(): frame# %d, Could not get slice data for decryptor, err %d\n"
- "AppleAVD: ERROR: %s(): frame# %d, Could not set kAppleAVDSetCryptScheme, err %d\n"
- "AppleAVD: ERROR: %s(): frame# %d, FigCPECryptorGetExternalProtectionMethods, err %d\n"
- "AppleAVD: ERROR: %s(): frame# %d, FigCPECryptorGetNativeSession returned err %d\n"
- "AppleAVD: ERROR: %s(): frame# %d, cryptorIV is NULL, err %d\n"
- "AppleAVD: ERROR: %s(): frame# %d, new CVPixelBufferPool created protectionOptions %llu %llu - ioSurfaceType: %d, err: %d\n"
- "AppleAVD: ERROR: %s(): frame# %d, session: %p, decryptor attachment is NULL\n"
- "AppleAVD: ERROR: %s(): framenum %d decryptError %x\n"
- "AppleAVD: ERROR: %s(): framenum %d kVTVideoDecoderMalfunctionErr\n"
- "AppleAVD: ERROR: %s(): got NULL vTable from cryptor object!\n"
- "AppleAVD: ERROR: %s(): hevc - unpermitted non-VCL NAL following last VCL NAL\n"
- "AppleAVD: ERROR: %s(): index %d \n"
- "AppleAVD: ERROR: %s(): initializing pixel buffer failed with %d\n"
- "AppleAVD: ERROR: %s(): invalid bit depth [luma depth minus 8 = %d, chroma depth minus 8 = %d]\n"
- "AppleAVD: ERROR: %s(): invalid dimensions (coded width %d, height %d)\n"
- "AppleAVD: ERROR: %s(): kCVPixelBufferPixelFormatTypeKey was not present in retrieved dictionary\n"
- "AppleAVD: ERROR: %s(): linear_orig subsampling format is not 4:2:0 (saw %d)\n"
- "AppleAVD: ERROR: %s(): linear_scaled subsampling format is not 4:2:0 (saw %d)\n"
- "AppleAVD: ERROR: %s(): m_av1_header allocation failed\n"
- "AppleAVD: ERROR: %s(): m_cur_pic_info allocation failed\n"
- "AppleAVD: ERROR: %s(): m_dec_bufs allocation failed\n"
- "AppleAVD: ERROR: %s(): m_dec_q allocation failed\n"
- "AppleAVD: ERROR: %s(): m_disp_q allocation failed\n"
- "AppleAVD: ERROR: %s(): m_highestTid > vps_max_sub_layers_minus1\n"
- "AppleAVD: ERROR: %s(): m_out_q allocation failed\n"
- "AppleAVD: ERROR: %s(): m_pps_list mem alloc failed\n"
- "AppleAVD: ERROR: %s(): m_sliceInfo mem alloc failed\n"
- "AppleAVD: ERROR: %s(): m_slices mem alloc failed\n"
- "AppleAVD: ERROR: %s(): m_sps_list mem alloc failed\n"
- "AppleAVD: ERROR: %s(): mvhevc - unpermitted non-VCL NAL following last VCL NAL\n"
- "AppleAVD: ERROR: %s(): oversized iv %d\n"
- "AppleAVD: ERROR: %s(): pic size too large - either width (%d, %d) or height (%d, %d) > max dim. %d and it's 4:2:0, 8 bit, so software decoder can handle it."
- "AppleAVD: ERROR: %s(): pluginState (%d) was already started! current: %d - requested: %d"
- "AppleAVD: ERROR: %s(): processed buffer length (%zu bytes) != sample buffer length (%zu bytes)\n"
- "AppleAVD: ERROR: %s(): protectedRegionOffsets is NULL\n"
- "AppleAVD: ERROR: %s(): protectedRegionSizes is NULL\n"
- "AppleAVD: ERROR: %s(): pthread_cond_timedwait exited with error: %d"
- "AppleAVD: ERROR: %s(): ref pic list0[%d] has dimension mismatch\n"
- "AppleAVD: ERROR: %s(): ref pic list1[%d] has dimension mismatch\n"
- "AppleAVD: ERROR: %s(): reference marking failed\n"
- "AppleAVD: ERROR: %s(): slice count for frame is 0"
- "AppleAVD: ERROR: %s(): threadReady state false. Exiting due to timeout (waitCount=%u of %d sec) or error (=%d)"
- "AppleAVD: ERROR: %s(): unsupported codec type %d\n"
- "AppleAVD: ERROR: %s(): vSurfInfoScalerRef was not set! (frameNum :%d)"
- "AppleAVD: ERROR: %s: B slice - reflist 0 has ref pics with non-unique POC\n"
- "AppleAVD: ERROR: %s: B slice - reflist 1 has ref pics with non-unique POC\n"
- "AppleAVD: ERROR: %s: No non-existing ref frames found!\n"
- "AppleAVD: ERROR: %s: No ref pics found!\n"
- "AppleAVD: ERROR: %s: VPS extension missing!\n"
- "AppleAVD: ERROR: %s: error creating pps list!\n"
- "AppleAVD: ERROR: %s: error creating rbsp!\n"
- "AppleAVD: ERROR: %s: error creating sps list!\n"
- "AppleAVD: ERROR: %s: fill frame num gap failed!\n"
- "AppleAVD: ERROR: %s: initPicture failed\n"
- "AppleAVD: ERROR: %s: layerID %d > vps_max_layer_id %d!\n"
- "AppleAVD: ERROR: %s: max_num_ref_frames %d > dpbSize %d\n"
- "AppleAVD: ERROR: %s: max_num_ref_frames %d > nMaxDpbSize %d!\n"
- "AppleAVD: ERROR: %s: numLayersInIdList=%d, vps_ols_2d[%d][%d].vps_output_layer_flag == 0\n"
- "AppleAVD: ERROR: %s: refList0 size <= num_ref_idx_l0_active_minus1!\n"
- "AppleAVD: ERROR: %s: refList1 size <= num_ref_idx_l1_active_minus1!\n"
- "AppleAVD: ERROR: %s: sliding window process failed!\n"
- "AppleAVD: ERROR: %s: vps_view_order_idx >= vps_num_views\n"
- "AppleAVD: ERROR: AVC decoder kVAGetVRAHDRBuff tag unsupported!"
- "AppleAVD: ERROR: AVC decoder kVASetVRAHDRBuff tag unsupported!"
- "AppleAVD: ERROR: AppleAVD_H264VideoDecoder - AppleAVDSetParameter kAppleAVDSetVRAType: Unsupported VRA Type 2\n"
- "AppleAVD: ERROR: AppleAVD_HEVCDecoder - AppleAVDSetParameter kAppleAVDSetVRAType: Unsupported VRA Type:%d\n"
- "AppleAVD: ERROR: BufferPool::shallowCloneBuffer:(%p) index = %u is invalid!"
- "AppleAVD: ERROR: CAVDHevcDecoder::%s() m_pps_list mem alloc failed"
- "AppleAVD: ERROR: CAVDHevcDecoder::%s() m_slices mem alloc failed"
- "AppleAVD: ERROR: CAVDHevcDecoder::%s() m_sps_list mem alloc failed"
- "AppleAVD: ERROR: ERROR: tileX offset not a multiple of 64! tileOffsetX:%d"
- "AppleAVD: ERROR: Failed to set parameter kVASetVRATypeAndDimensions - status %d"
- "AppleAVD: ERROR: H3H264VideoDecoder FIG: Cannot use type of %p %p"
- "AppleAVD: ERROR: H3H264VideoDecoder FIG: cannot convert number %p %p"
- "AppleAVD: ERROR: HEVC decoder kVASetVRAHDRBuff tag unsupported for USP!"
- "AppleAVD: ERROR: Invalid VRA Dimensions - w:%d h:%d"
- "AppleAVD: ERROR: Parser av1_get_next_frame() function return fail!\n"
- "AppleAVD: ERROR: VRA illegal size %u %u %u %u"
- "AppleAVD: ERROR: [CAVDAvcDecErr] %s"
- "AppleAVD: ERROR: [CAVDAvxDecErr] %s"
- "AppleAVD: ERROR: [CAVDHevcDecErr] %s"
- "AppleAVD: ERROR: [CAVDMvHevcDecErr] %s"
- "AppleAVD: ERROR: bad header, got error %d parsing header\n"
- "AppleAVD: ERROR: calcLayerSetLayerIdList "
- "AppleAVD: ERROR: createDecoder() error creating rvra buffers!"
- "AppleAVD: ERROR: fail to parse av1 header\n"
- "AppleAVD: ERROR: failed to change video resolution to %ux%u\n"
- "AppleAVD: ERROR: kVASetMultiVPParsing error: %d \n"
- "AppleAVD: ERROR: kVASetSliceHeaderThreshold error: %d \n"
- "AppleAVD: ERROR: kVASetUnlimitedResolution error: %d \n"
- "AppleAVD: ERROR: vpsext->vps_layer_set_layer_id_list bad alloc "
- "AppleAVD: ERROR: vpsext->vps_layer_set_layer_id_list[m] bad alloc "
- "AppleAVD: ERROR: vpsext->vps_layers bad alloc "
- "AppleAVD: ERROR: vpsext->vps_layers_2d bad alloc "
- "AppleAVD: ERROR: vpsext->vps_layers_2d[i] bad alloc "
- "AppleAVD: ERROR: vpsext->vps_num_layers_in_id_list bad alloc "
- "AppleAVD: ERROR: vpsext->vps_splitting_flag && vpsext->vps_num_scalability_types == 0 "
- "AppleAVD: Error getting chroma scratch buffer!"
- "AppleAVD: Error getting decoder buffer!"
- "AppleAVD: Error getting display buffer!"
- "AppleAVD: Error: list-0 slice(%2d) RefIdx[%2d] not found in %d ref_pics!!\n"
- "AppleAVD: Error: list-1 slice(%2d) RefIdx[%2d] not found in %d ref_pics!!\n"
- "AppleAVD: Error: not able to get ivf frame\n"
- "AppleAVD: Error: not able to get next obu\n"
- "AppleAVD: FGHDecoder ERROR: ConfigRecordData error - Cannot find config record"
- "AppleAVD: FOUND IRAP-- SETTING m_skipToIdr FALSE! %d"
- "AppleAVD: FeatureFlagIsPWDEnabled: %s FeatureFlagIsHEVCWithAlphaCompressedIOSurfaces: %s MVHEVCAlpha: %s FeatureFlagIsFaceTimeCompressedIOSurfacesEnabled: %s"
- "AppleAVD: HEVCDecoder ERROR: ConfigRecordData error - Cannot find config record"
- "AppleAVD: HEVC_Decoder::ParseHeader unsupported naluLengthSize %d"
- "AppleAVD: INFO: %s internal build, useCompression %d"
- "AppleAVD: INFO: %s() - AppleAVD Foghorn codec registered\n"
- "AppleAVD: INFO: %s() - AppleAVD H264 codec registered\n"
- "AppleAVD: INFO: %s() - AppleAVD HEVC codec registered. CheckPlatform 0x%llx\n"
- "AppleAVD: INFO: %s() - AppleAVD Leghorn codec registered\n"
- "AppleAVD: INFO: %s(): %s - CPBManager created! cacheSize: %d - timeLimit: %llums\n"
- "AppleAVD: INFO: %s(): Allocating new AppleAVDCommandBuilder\n"
- "AppleAVD: INFO: %s(): Successfully retrieved support bits! 0x%llx\n"
- "AppleAVD: INFO: %s(): longest wait: %llums (100ms intervals)\n"
- "AppleAVD: INFO: %s(): pixel buffer format: %c%c%c%c - kIOSurfaceCompressionTypeAGX\n"
- "AppleAVD: INFO: %s(): pixel buffer format: %c%c%c%c - kIOSurfaceCompressionTypeHTPC\n"
- "AppleAVD: INFO: %s(): pixel buffer format: %c%c%c%c - kIOSurfaceCompressionTypeNone\n"
- "AppleAVD: INFO: JumboSliceHeader at fnum %d bit_offset %d byte offset %d\n"
- "AppleAVD: INFO: Paravirtualized sessions - ineligible for compressed output!"
- "AppleAVD: INFO: padding ineligible for compression w x h = %d %d, cw x cw = %d %d"
- "AppleAVD: Invalid resolution in %s"
- "AppleAVD: LGHDecoder ERROR: ConfigRecordData error - Cannot find config record"
- "AppleAVD: NULL ppsList %p or spsList %p"
- "AppleAVD: NULL sliceHeader %p or nal_header %p or ppsList %p or spsList %p"
- "AppleAVD: NULL spsList"
- "AppleAVD: PPS doesn't exist for slice header parsing"
- "AppleAVD: RefPicture pool full, found duplicate ref picture slot, mark duplicate ref as unused \n"
- "AppleAVD: RefPicture pool full, mark oldest ref picture as unused \n"
- "AppleAVD: Rejecting RVRA scaling ratios beyond 16x! inWidth:%d inHeight:%d outWidth:%d outHeight:%d"
- "AppleAVD: Rejecting non-IDR frame in tiled decode %d"
- "AppleAVD: Rejecting non-IRAP frame in tiled decode %d"
- "AppleAVD: SETTING m_skipToIdr TRUE! fno=%d, err=%d"
- "AppleAVD: SPS doesn't exist for slice header parsing"
- "AppleAVD: Unsupported scaling dimensions! inWidth:%d inHeight:%d outWidth:%d outHeight:%d IOSurfaceGetWidthInCompressedTilesOfPlane:%zu IOSurfaceGetCompressedTileWidthOfPlane:%zu IOSurfaceGetHeightInCompressedTilesOfPlane:%zu IOSurfaceGetCompressedTileHeightOfPlane:%zu\n"
- "AppleAVD: Unsupported scaling dimensions! inWidth:%d inHeight:%d outWidth:%d outHeight:%d IOSurfaceGetWidthOfPlane:%zu extendedRight:%zu IOSurfaceGetHeightOfPlane:%zu extendedBottom:%zu\n"
- "AppleAVD: Unsupported sps->pic_width_in_luma_samples:%d or sps->pic_height_in_luma_samples:%d"
- "AppleAVD: VPS doesn't exist for slice header parsing"
- "AppleAVD: WARNING, fail to copy data bytes, nothing to decode"
- "AppleAVD: WARNING:  tile skip calculation has failed\n"
- "AppleAVD: WARNING: %s %d 64->32 conversion problem!"
- "AppleAVD: WARNING: %s() - trying to get FrameReceiverThreadPriority before videoContext was created!\n"
- "AppleAVD: WARNING: %s() - trying to set kAppleAVDEnableIOFence before videoContext was created!\n"
- "AppleAVD: WARNING: %s() - trying to set kAppleAVDEnableRVRA before videoContext was created!\n"
- "AppleAVD: WARNING: %s() - trying to set kAppleAVDExtraInloopFilter before videoContext was created!\n"
- "AppleAVD: WARNING: %s() - trying to set kAppleAVDSetAttachQPs before videoContext was created!\n"
- "AppleAVD: WARNING: %s() - trying to set kAppleAVDSetAv1FilmGrainMode before videoContext was created!\n"
- "AppleAVD: WARNING: %s() - trying to set kAppleAVDSetMVAV1DisplayLayerIDs before videoContext was created!\n"
- "AppleAVD: WARNING: %s() - trying to set kAppleAVDSetMVHEVCDisplayLayerIDs before videoContext was created!\n"
- "AppleAVD: WARNING: %s() - trying to set kAppleAVDSetUsageMode before videoContext was created!\n"
- "AppleAVD: WARNING: %s() - trying to set kAppleAVDSetVRADimensions before videoContext was created!\n"
- "AppleAVD: WARNING: %s() - trying to set kAppleAVDSetVRAType before videoContext was created!\n"
- "AppleAVD: WARNING: %s(): Got NULL infoFlagsOut!\n"
- "AppleAVD: WARNING: %s(): Non-mod16 VRA dimensions with width %d, height %d\n"
- "AppleAVD: WARNING: %s(): Pixel Buffer Format array has %ld entries!\n"
- "AppleAVD: WARNING: %s(): Timed out, waited at least %llums! m_num_CPBs_on_the_fly=%u timeoutMS=%llu"
- "AppleAVD: WARNING: %s(): bad PPS index %d"
- "AppleAVD: WARNING: %s(): bad SPS index %d"
- "AppleAVD: WARNING: %s(): frameNum %d - BufferPoolId[%d]: Index %d is not in use! in_use: %d\n"
- "AppleAVD: WARNING: %s(): h->req.a.da.RefAddrYSize.val = %d\n"
- "AppleAVD: WARNING: %s(): index: %d - trying to release! frameNum (%d) < get frameNum (%d), returning early!"
- "AppleAVD: WARNING: %s(): kVAGetApplyFoxtrot with m_active_sps %d m_active_pps %d"
- "AppleAVD: WARNING: %s(): pic size too wide %d %d or tall %d %d vs. %d but depth %d chroma fmt %d, so we'll attempt it anyway"
- "AppleAVD: WARNING: %s(): should not decode frame %d!\n"
- "AppleAVD: WARNING: %s(): timeout status: %d"
- "AppleAVD: WARNING: %s(): timeout timeoutStatus: %d"
- "AppleAVD: WARNING: %u: WARNING! resizing CVPixelBufferPool is not supported"
- "AppleAVD: WARNING: AVC chroma plane with odd number of IMBs is unspported on Salvia A0"
- "AppleAVD: WARNING: Corrupted metadata OBU\n"
- "AppleAVD: WARNING: FGH chroma plane with odd number of IMBs is unspported on Salvia A0"
- "AppleAVD: WARNING: HEVC chroma plane with odd number of IMBs is unspported on Salvia A0"
- "AppleAVD: WARNING: LGH chroma plane with odd number of IMBs is unspported on Salvia A0"
- "AppleAVD: WARNING: Unrecognized OBU type %d will be dropped\n"
- "AppleAVD: WriteNAL AVD_HEVC_ERROR_BAD_NAL_LENGTH "
- "AppleAVD: WriteNAL kAVD_DECODER_ERROR_BAD_NAL_LENGTH "
- "AppleAVD: Wrong sizeOfScalingList (%d). Should be either 16 or 64"
- "AppleAVD: [CAVDAvcDecErr] %s %d"
- "AppleAVD: [ERROR] %s(): chroma compression format %d lossy level %d not supported\n"
- "AppleAVD: [ERROR] %s(): luma compression format %d lossy level %d not supported\n"
- "AppleAVD: avdDec - Setting CFDebugMetaDataSEI to %d\n"
- "AppleAVD: backward refresh 0 fci_ref fc %p\n"
- "AppleAVD: backward refresh 1 fci_ref fc %p\n"
- "AppleAVD: bad IOSurface* in tile offset check"
- "AppleAVD: bad PPS index %d %s\n"
- "AppleAVD: bad SPS index %d %s\n"
- "AppleAVD: bailing out of %s because start didn't complete"
- "AppleAVD: buf[%2d]=%p ref_count = %2d order_hint=%d\n"
- "AppleAVD: caught initPicture error in %s"
- "AppleAVD: cfg1: %d %d %d %d %d %d %d %d"
- "AppleAVD: cfg2: %d %d %d %d %d %d %d %d"
- "AppleAVD: cfg3: %d %d %d %d %d %d %d %d %d %d"
- "AppleAVD: checkRVRAScalingRatio returned error:%d\n"
- "AppleAVD: chroma_and_bit_depth_vps_present_flags is 0 for first rep format"
- "AppleAVD: codecIntializationDataSize not zero %x %x, but ignored"
- "AppleAVD: decodeGetRenderTargetRef RETURNED ERROR\n"
- "AppleAVD: encrypted slices size > MAX_SLICES:%d"
- "AppleAVD: failed due to p_ctx=%p, p_cv_pool=%p, max_cache_size=%d, m_is_initialized=%d"
- "AppleAVD: frame_header_obu: ERROR, cur_frame isn't valid\n"
- "AppleAVD: getHwDecoder error in %s"
- "AppleAVD: get_bits(%d): %s = %x, m_bits_left %d\n"
- "AppleAVD: invalid weight table"
- "AppleAVD: linear_orig or linear_scaled is NULL\n"
- "AppleAVD: matrixId %d < scaling_list_pred_matrix_id_delta %d"
- "AppleAVD: next_32bits: %x m_bits_left %d\n"
- "AppleAVD: pBufferPool[%d] allocation failed!"
- "AppleAVD: pBufferPool[%d] initBufferPool allocation failed!"
- "AppleAVD: pBufferPool[%d] is NULL cvPixBufIndex:%d!"
- "AppleAVD: pBufferPool[AVD_PIXBUF_DEC] && pBufferPool[AVD_PIXBUF_DISP] are NULL!"
- "AppleAVD: pIOSurfaceDst lockSurface failed with error:%d\n"
- "AppleAVD: pIOSurfaceDst lookup failed!\n"
- "AppleAVD: pIOSurfaceSrc lockSurface failed with error:%d\n"
- "AppleAVD: pIOSurfaceSrc lookup failed!\n"
- "AppleAVD: parsePpsMultiLayerExtension error"
- "AppleAVD: parsePpsRangeExtension error"
- "AppleAVD: parseShortTermRefPicSet parsing failure"
- "AppleAVD: pic_parameter_set_id(%d) out of range [0..%d]"
- "AppleAVD: pps->num_ref_idx_l0_default_active_minus1 > HEVC_MAX_REF_INDEX_FOR_RPL, is %d"
- "AppleAVD: pps->num_ref_idx_l1_default_active_minus1 > HEVC_MAX_REF_INDEX_FOR_RPL, is %d"
- "AppleAVD: ppsNALUAndRBSPSize %d size1 %d configRecordSize %zu i %d\n"
- "AppleAVD: primary ref fc %p\n"
- "AppleAVD: primary ref no fb, default %d fc %p\n"
- "AppleAVD: profile_idc(%d) is not valid"
- "AppleAVD: ref none, default %d fc %p\n"
- "AppleAVD: release fb %d fci_wr fc %p, copy to pool[%d] fci_wr fc %p\n"
- "AppleAVD: rvra temp buff size isn't big enough! yuvsize:%u rvraTempBuffSize:%u\n"
- "AppleAVD: rvrascalerbuffsize alloc overflow in %s %d"
- "AppleAVD: seq_parameter_set_id(%d) out of range [0..%d]"
- "AppleAVD: slice->slice_pic_parameter_set_id > HEVC_MAX_PPS_SET, is %d"
- "AppleAVD: storage->usageMode:%d storage->enableRVRA:%d storage->enableChromaFilter:%d"
- "AppleAVD: tile offset out of bounds! [%d %d] + [%d %d], %d, %u >= %u ?, %u; %u %u %u"
- "AppleAVD: tile offset out of bounds! [%u %u] + [%u %u], %u, %zu >= %zu ?, %u; %u %u %u"
- "AppleAVD: uncomp_hdr->ref_frame_map[%d] = %p\n"
- "AppleAVD: undersized config record"
- "AppleAVD: unsupported profile %d"
- "AppleAVD: value out of range: num_tile_columns_minus1 %d num_tile_rows_minus1 %d"
- "FrameDone"
- "Jan 26 2026"
- "OSStatus parseAvcSps(unsigned char *, int, uint32_t *, uint32_t *, uint32_t *, uint32_t *, uint32_t *, uint32_t *)"
- "OSStatus parseHevcSps(unsigned char *, int, avd_seq_params *, int, sHevcVpsLayerDependency *, int)"
- "RequestedMVAV1SpatialIDs"
- "attachHistogramToIOSurface"
- "int CAHDecCatnipAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
- "int CAHDecClaryAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
- "int CAHDecDahliaAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
- "int CAHDecDaisyAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
- "int CAHDecHibiscusAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
- "int CAHDecIxoraAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
- "int CAHDecLotusAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
- "int CAHDecTansyAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
- "int CAHDecThymeAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
- "int CAHDecViolaAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
- "int CAVDAvcDecoder::activatePS(sAvcSliceHeader *)"
- "int CAVDAvxDecoder::getBitDepth(av1_sequence_header *, int *)"
- "int CAVDAvxDecoder::getChromaFormat(av1_sequence_header *, int *)"
- "int CAVDAvxDecoder::getDeltaLfRes()"
- "int CAVDAvxDecoder::getRestorationUnitSize(int)"
- "int CAVDAvxDecoder::getSWRStride(uint32_t, uint32_t, uint32_t, uint32_t)"
- "int CAVDAvxDecoder::initPicture(uint32_t)"
- "int32_t CAHDecCatnipAvx::getUpscaleConvolveStep(int, int)"
- "int32_t CAHDecCatnipAvx::getUpscaleConvolveX0(int, int, int32_t)"
- "int32_t CAHDecDaisyAvx::getUpscaleConvolveStep(int, int)"
- "int32_t CAHDecDaisyAvx::getUpscaleConvolveX0(int, int, int32_t)"
- "int32_t CAHDecHibiscusAvx::getUpscaleConvolveStep(int, int)"
- "int32_t CAHDecHibiscusAvx::getUpscaleConvolveX0(int, int, int32_t)"
- "int32_t CAHDecIxoraAvx::getUpscaleConvolveStep(int, int)"
- "int32_t CAHDecIxoraAvx::getUpscaleConvolveX0(int, int, int32_t)"
- "int32_t CAHDecTansyAvx::getUpscaleConvolveStep(int, int)"
- "int32_t CAHDecTansyAvx::getUpscaleConvolveX0(int, int, int32_t)"
- "int32_t CAHDecThymeAvx::getUpscaleConvolveStep(int, int)"
- "int32_t CAHDecThymeAvx::getUpscaleConvolveX0(int, int, int32_t)"
- "int32_t HEVC_RBSP::parsePPS(hevc_picture_parameter_set_t *, hevc_sequence_parameter_set_t *)"
- "int32_t HEVC_RBSP::parseSPS(hevc_video_parameter_set_t *, hevc_sequence_parameter_set_t *, int, int)"
- "kIOSurfaceLumaHistogramV1"
- "kIOSurfacePixelMetadata"
- "kIOSurfaceSessionCookie"
- "kIOSurfaceSessionFrameNumber"
- "virtual int CAHDecCatnipAvx::populatePictureRegisters()"
- "virtual int CAHDecDaisyAvx::populatePictureRegisters()"
- "virtual int CAHDecHibiscusAvx::populatePictureRegisters()"
- "virtual int CAHDecIxoraAvx::populatePictureRegisters()"
- "virtual int CAHDecTansyAvx::populatePictureRegisters()"
- "virtual int CAHDecThymeAvx::populatePictureRegisters()"
- "virtual int CAVDAvcDecoder::VADecodeFrame(unsigned char *, int, uint32_t, int, int, int, avd_seq_params *)"
- "virtual int CAVDAvcDecoder::VAGetParams(uint32_t, uint32_t *)"
- "virtual int CAVDAvcDecoder::VAStartDecode(unsigned char *, int)"
- "virtual int CAVDAvxDecoder::VADecodeFrame(unsigned char *, int, uint32_t, int, int, int, avd_seq_params *)"
- "virtual int CAVDAvxDecoder::VAStartDecode(unsigned char *, int)"
- "virtual int CAVDHevcDecoder::VADecodeFrame(unsigned char *, int, uint32_t, int, int, int, avd_seq_params *)"
- "virtual int CAVDLghDecoder::VADecodeFrame(unsigned char *, int, uint32_t, int, int, int, avd_seq_params *)"
- "virtual int CAVDMvHevcDecoder::VADecodeFrame(unsigned char *, int, uint32_t, int, int, int, avd_seq_params *)"

```
