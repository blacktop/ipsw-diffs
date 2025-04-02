## VisualPairing

> `/System/iOSSupport/System/Library/PrivateFrameworks/VisualPairing.framework/Versions/A/VisualPairing`

```diff

-200.3.0.0.0
-  __TEXT.__text: 0x1d3fc
+200.600.1.0.0
+  __TEXT.__text: 0x1d7c0
   __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0x624
+  __TEXT.__objc_methlist: 0x74c
   __TEXT.__const: 0x34c7e
-  __TEXT.__cstring: 0xa7d
-  __TEXT.__gcc_except_tab: 0x428
-  __TEXT.__unwind_info: 0x408
+  __TEXT.__cstring: 0xac2
+  __TEXT.__gcc_except_tab: 0x448
+  __TEXT.__unwind_info: 0x440
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0xb9
-  __TEXT.__objc_methname: 0x166b
-  __TEXT.__objc_methtype: 0x3fb
-  __TEXT.__objc_stubs: 0x11c0
+  __TEXT.__objc_classname: 0xcd
+  __TEXT.__objc_methname: 0x1874
+  __TEXT.__objc_methtype: 0x44c
+  __TEXT.__objc_stubs: 0x1260
   __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x18
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__const: 0x38
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c0
+  __DATA_CONST.__objc_selrefs: 0x740
   __AUTH_CONST.__auth_got: 0x238
-  __AUTH_CONST.__const: 0x4f0
+  __AUTH_CONST.__const: 0x510
   __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0xd50
+  __AUTH_CONST.__objc_const: 0xf30
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_classrefs: 0xf0
-  __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0xe8
-  __DATA.__data: 0x2f0
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_classrefs: 0xf8
+  __DATA.__objc_superrefs: 0x30
+  __DATA.__objc_ivar: 0x100
+  __DATA.__data: 0x360
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
-  - /System/iOSSupport/System/Library/Frameworks/AVKit.framework/Versions/A/AVKit
   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 313
-  Symbols:   761
-  CStrings:  468
+  Functions: 338
+  Symbols:   817
+  CStrings:  504
 
Symbols:
+ -[VPPresenterView _initCommon]
+ -[VPPresenterView initWithCoder:]
+ -[VPPresenterView init]
+ -[VPPresenterView setWatermarkOpacityMultiplier:]
+ -[VPPresenterView setWatermarkScaleFactor:]
+ -[VPPresenterView watermarkOpacityMultiplier]
+ -[VPPresenterView watermarkScaleFactor]
+ -[VPWatermarkReader .cxx_destruct]
+ -[VPWatermarkReader extractedCodeLength]
+ -[VPWatermarkReader firstCapturedFrameDate]
+ -[VPWatermarkReader firstScannedCodeDate]
+ -[VPWatermarkReader init]
+ -[VPWatermarkReader latestError]
+ -[VPWatermarkReader progressHandler]
+ -[VPWatermarkReader readWatermarkIn:]
+ -[VPWatermarkReader readWatermarkInPixelBuffer:error:]
+ -[VPWatermarkReader readerHeight]
+ -[VPWatermarkReader readerResetCount]
+ -[VPWatermarkReader readerRowBytes]
+ -[VPWatermarkReader readerWidth]
+ -[VPWatermarkReader reset]
+ -[VPWatermarkReader setExtractedCodeLength:]
+ -[VPWatermarkReader setFirstCapturedFrameDate:]
+ -[VPWatermarkReader setFirstScannedCodeDate:]
+ -[VPWatermarkReader setLatestError:]
+ -[VPWatermarkReader setProgressHandler:]
+ -[VPWatermarkReader setReaderHeight:]
+ -[VPWatermarkReader setReaderResetCount:]
+ -[VPWatermarkReader setReaderRowBytes:]
+ -[VPWatermarkReader setReaderWidth:]
+ -[VPWatermarkReader setStartDate:]
+ -[VPWatermarkReader startDate]
+ GCC_except_table13
+ GCC_except_table17
+ GCC_except_table7
+ OBJC_IVAR_$_VPWatermarkReader._extractedCodeLength
+ OBJC_IVAR_$_VPWatermarkReader._firstCapturedFrameDate
+ OBJC_IVAR_$_VPWatermarkReader._firstScannedCodeDate
+ OBJC_IVAR_$_VPWatermarkReader._latestError
+ OBJC_IVAR_$_VPWatermarkReader._progressHandler
+ OBJC_IVAR_$_VPWatermarkReader._reader
+ OBJC_IVAR_$_VPWatermarkReader._readerHeight
+ OBJC_IVAR_$_VPWatermarkReader._readerLastProgress
+ OBJC_IVAR_$_VPWatermarkReader._readerLastWatermarkTicks
+ OBJC_IVAR_$_VPWatermarkReader._readerResetCount
+ OBJC_IVAR_$_VPWatermarkReader._readerResetTicks
+ OBJC_IVAR_$_VPWatermarkReader._readerRowBytes
+ OBJC_IVAR_$_VPWatermarkReader._readerWidth
+ OBJC_IVAR_$_VPWatermarkReader._startDate
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_VPWatermarkReader
+ _OBJC_METACLASS_$_VPWatermarkReader
+ __NSConcreteGlobalBlock
+ __OBJC_$_INSTANCE_METHODS_VPWatermarkReader
+ __OBJC_$_INSTANCE_VARIABLES_VPWatermarkReader
+ __OBJC_$_PROP_LIST_VPWatermarkReader
+ __OBJC_CLASS_RO_$_VPWatermarkReader
+ __OBJC_METACLASS_RO_$_VPWatermarkReader
+ ___28-[VPScannerView _initCommon]_block_invoke
+ ___block_descriptor_32_e8_v12?0f8l
+ ___block_literal_global
+ _gLogCategory_SVW
+ _objc_msgSend$readWatermarkInPixelBuffer:error:
+ _objc_msgSend$readerHeight
+ _objc_msgSend$readerRowBytes
+ _objc_msgSend$readerWidth
+ _objc_msgSend$setProgressHandler:
- -[VPScannerView extractedCodeLength]
- -[VPScannerView firstCapturedFrameDate]
- -[VPScannerView firstScannedCodeDate]
- -[VPScannerView readerResetCount]
- -[VPScannerView setExtractedCodeLength:]
- -[VPScannerView setFirstCapturedFrameDate:]
- -[VPScannerView setFirstScannedCodeDate:]
- -[VPScannerView setReaderResetCount:]
- GCC_except_table14
- GCC_except_table8
- OBJC_IVAR_$_VPScannerView._extractedCodeLength
- OBJC_IVAR_$_VPScannerView._readerResetCount
CStrings:
+ "\x04\x133"
+ "-[VPScannerView _initCommon]_block_invoke"
+ "-[VPWatermarkReader readWatermarkInPixelBuffer:error:]"
+ "@\"VPWatermarkReader\""
+ "@24@0:8^{__CVBuffer=}16"
+ "@32@0:8^{__CVBuffer=}16^@24"
+ "Current Scan Progress %0.f\n"
+ "D!"
+ "SVW"
+ "T@?,C,N,V_progressHandler"
+ "TQ,N,V_watermarkScaleFactor"
+ "TQ,V_readerHeight"
+ "TQ,V_readerRowBytes"
+ "TQ,V_readerWidth"
+ "Tf,N,V_watermarkOpacityMultiplier"
+ "VPWatermarkReader"
+ "_progressHandler"
+ "_watermarkOpacityMultiplier"
+ "_watermarkReader"
+ "_watermarkScaleFactor"
+ "f16@0:8"
+ "init"
+ "progressHandler"
+ "readWatermarkIn:"
+ "readWatermarkInPixelBuffer:error:"
+ "reset"
+ "setProgressHandler:"
+ "setReaderHeight:"
+ "setReaderRowBytes:"
+ "setReaderWidth:"
+ "setWatermarkOpacityMultiplier:"
+ "setWatermarkScaleFactor:"
+ "v12@?0f8"
+ "watermarkOpacityMultiplier"
+ "watermarkScaleFactor"
- "\x04r4!"
- "-[VPScannerView captureOutput:didOutputSampleBuffer:fromConnection:]"

```
