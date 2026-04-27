## CoreRecognition

> `/System/Library/PrivateFrameworks/CoreRecognition.framework/CoreRecognition`

```diff

-430.2.2.0.0
-  __TEXT.__text: 0x55184
-  __TEXT.__auth_stubs: 0x1370
-  __TEXT.__objc_methlist: 0x2204
-  __TEXT.__const: 0x79c
-  __TEXT.__gcc_except_tab: 0x80f4
-  __TEXT.__cstring: 0x3843
-  __TEXT.__oslogstring: 0x52
+430.2.3.0.0
+  __TEXT.__text: 0x5777c
+  __TEXT.__auth_stubs: 0x1390
+  __TEXT.__objc_methlist: 0x238c
+  __TEXT.__const: 0x7bc
+  __TEXT.__gcc_except_tab: 0x8660
+  __TEXT.__cstring: 0x38fa
+  __TEXT.__oslogstring: 0x3d6
   __TEXT.__ustring: 0x1282
-  __TEXT.__unwind_info: 0x13b0
+  __TEXT.__unwind_info: 0x14a0
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x2f1
-  __TEXT.__objc_methname: 0x78f3
-  __TEXT.__objc_methtype: 0x1759
-  __TEXT.__objc_stubs: 0x73e0
-  __DATA_CONST.__got: 0x5c0
-  __DATA_CONST.__const: 0xa18
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__objc_classname: 0x316
+  __TEXT.__objc_methname: 0x7da8
+  __TEXT.__objc_methtype: 0x1785
+  __TEXT.__objc_stubs: 0x7680
+  __DATA_CONST.__got: 0x5d0
+  __DATA_CONST.__const: 0xaa8
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f88
+  __DATA_CONST.__objc_selrefs: 0x2048
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x3dc0
-  __AUTH_CONST.__auth_got: 0x9d0
+  __AUTH_CONST.__auth_got: 0x9e0
   __AUTH_CONST.__const: 0x990
-  __AUTH_CONST.__cfstring: 0xfb40
-  __AUTH_CONST.__objc_const: 0x35a8
+  __AUTH_CONST.__cfstring: 0xfbe0
+  __AUTH_CONST.__objc_const: 0x38c0
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x29c
+  __AUTH.__objc_data: 0x7d0
+  __DATA.__objc_ivar: 0x2c8
   __DATA.__data: 0x240
   __DATA.__bss: 0x98
   __DATA.__common: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2EACFD91-B721-3978-AD66-789848D6E21D
-  Functions: 1067
-  Symbols:   4369
-  CStrings:  4780
+  UUID: 5E77AC30-2B5F-3D55-8247-2B7769FBAD4B
+  Functions: 1115
+  Symbols:   4523
+  CStrings:  4847
 
Symbols:
+ -[CRAlignmentLayer hideCardAlignmentRect]
+ -[CRAlignmentLayer hideCardInfoOverlay]
+ -[CRAlignmentLayer setHideCardAlignmentRect:]
+ -[CRAlignmentLayer setHideCardInfoOverlay:]
+ -[CRCameraReader ccProcessingImage]
+ -[CRCameraReader ccProcessingQueue]
+ -[CRCameraReader continuousMode]
+ -[CRCameraReader dispatchSampleBuffer:onQueue:semaphore:work:]
+ -[CRCameraReader documentCaptureMaxDimension]
+ -[CRCameraReader enableManualDocumentCapture]
+ -[CRCameraReader findDocumentObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]
+ -[CRCameraReader hideCardAlignmentRect]
+ -[CRCameraReader hideCardInfoOverlay]
+ -[CRCameraReader idCorrectedCardBuffer]
+ -[CRCameraReader idProcessingImage]
+ -[CRCameraReader idProcessingQueue]
+ -[CRCameraReader reallocateCorrectedCardBuffers]
+ -[CRCameraReader sendDidRecognizeObjects:]
+ -[CRCameraReader setCcProcessingImage:]
+ -[CRCameraReader setCcProcessingQueue:]
+ -[CRCameraReader setContinuousMode:]
+ -[CRCameraReader setDocumentCaptureMaxDimension:]
+ -[CRCameraReader setEnableManualDocumentCapture:]
+ -[CRCameraReader setHideCardAlignmentRect:]
+ -[CRCameraReader setHideCardInfoOverlay:]
+ -[CRCameraReader setIdCorrectedCardBuffer:]
+ -[CRCameraReader setIdProcessingImage:]
+ -[CRCameraReader setIdProcessingQueue:]
+ -[CRCameraReaderOutputDocumentCapture capturePath]
+ -[CRCameraReaderOutputDocumentCapture imageValue]
+ -[CRCameraReaderOutputDocumentCapture targetVertices]
+ -[CRCameraReaderOutputDocumentCapture vertices]
+ GCC_except_table110
+ GCC_except_table111
+ GCC_except_table115
+ GCC_except_table119
+ GCC_except_table122
+ GCC_except_table123
+ GCC_except_table124
+ GCC_except_table155
+ GCC_except_table162
+ GCC_except_table164
+ GCC_except_table165
+ GCC_except_table166
+ GCC_except_table169
+ GCC_except_table175
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table18
+ GCC_except_table181
+ GCC_except_table182
+ GCC_except_table183
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table191
+ GCC_except_table192
+ GCC_except_table194
+ GCC_except_table196
+ GCC_except_table198
+ GCC_except_table199
+ GCC_except_table200
+ GCC_except_table201
+ GCC_except_table202
+ GCC_except_table206
+ GCC_except_table207
+ GCC_except_table208
+ GCC_except_table31
+ GCC_except_table36
+ GCC_except_table362
+ GCC_except_table365
+ GCC_except_table368
+ GCC_except_table42
+ GCC_except_table54
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table67
+ GCC_except_table71
+ GCC_except_table82
+ GCC_except_table84
+ GCC_except_table92
+ GCC_except_table96
+ _CRCameraReaderDocumentCapturePathAutomatic
+ _CRCameraReaderDocumentCapturePathManual
+ _CROutputTypeDocumentCapture
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_CRCameraReaderOutputDocumentCapture
+ _OBJC_IVAR_$_CRAlignmentLayer._hideCardAlignmentRect
+ _OBJC_IVAR_$_CRAlignmentLayer._hideCardInfoOverlay
+ _OBJC_IVAR_$_CRCameraReader._continuousMode
+ _OBJC_IVAR_$_CRCameraReader._enableManualDocumentCapture
+ _OBJC_IVAR_$_CRCameraReader._hideCardAlignmentRect
+ _OBJC_IVAR_$_CRCameraReader._hideCardInfoOverlay
+ _OBJC_METACLASS_$_CRCameraReaderOutputDocumentCapture
+ __OBJC_$_INSTANCE_METHODS_CRCameraReaderOutputDocumentCapture
+ __OBJC_$_PROP_LIST_CRCameraReaderOutputDocumentCapture
+ __OBJC_CLASS_RO_$_CRCameraReaderOutputDocumentCapture
+ __OBJC_METACLASS_RO_$_CRCameraReaderOutputDocumentCapture
+ ___29-[CRCameraReader stopSession]_block_invoke_3
+ ___29-[CRCameraReader stopSession]_block_invoke_4
+ ___39-[CRCameraReader setOutputObjectTypes:]_block_invoke
+ ___41-[CRCameraReader didReceiveMemoryWarning]_block_invoke_2
+ ___41-[CRCameraReader didReceiveMemoryWarning]_block_invoke_3
+ ___41-[CRCameraReader didReceiveMemoryWarning]_block_invoke_4
+ ___42-[CRCameraReader sendDidRecognizeObjects:]_block_invoke
+ ___46-[CRCameraReader setOutputCapturedImageWidth:]_block_invoke
+ ___48-[CRCameraReader reallocateCorrectedCardBuffers]_block_invoke
+ ___48-[CRCameraReader reallocateCorrectedCardBuffers]_block_invoke_2
+ ___49-[CRCameraReader setDocumentCaptureMaxDimension:]_block_invoke
+ ___62-[CRCameraReader dispatchSampleBuffer:onQueue:semaphore:work:]_block_invoke
+ ___69-[CRCameraReader captureOutput:didOutputSampleBuffer:fromConnection:]_block_invoke_4
+ ___69-[CRCameraReader captureOutput:didOutputSampleBuffer:fromConnection:]_block_invoke_5
+ ___69-[CRCameraReader captureOutput:didOutputSampleBuffer:fromConnection:]_block_invoke_6
+ ___69-[CRCameraReader captureOutput:didOutputSampleBuffer:fromConnection:]_block_invoke_7
+ ___block_descriptor_107_ea8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_48_ea8_32s40s_e42_v48?0^{__CVBuffer=}8"NSData"16{?=qiIq}24ls32l8s40l8
+ ___block_descriptor_58_ea8_32s40s_e42_v48?0^{__CVBuffer=}8"NSData"16{?=qiIq}24ls32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_81_ea8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.202
+ ___block_literal_global.323
+ ___block_literal_global.325
+ ___block_literal_global.328
+ ___block_literal_global.415
+ ___block_literal_global.417
+ ___block_literal_global.454
+ ___block_literal_global.456
+ ___block_literal_global.476
+ ___block_literal_global.481
+ ___block_literal_global.486
+ ___block_literal_global.505
+ ___block_literal_global.518
+ ___block_literal_global.526
+ ___block_literal_global.528
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_msgSend$ccProcessingImage
+ _objc_msgSend$ccProcessingQueue
+ _objc_msgSend$continuousMode
+ _objc_msgSend$dispatchSampleBuffer:onQueue:semaphore:work:
+ _objc_msgSend$documentCaptureMaxDimension
+ _objc_msgSend$enableManualDocumentCapture
+ _objc_msgSend$findDocumentObjects:inPixelBuffer:cameraIntrinsicData:frameTime:
+ _objc_msgSend$hideCardAlignmentRect
+ _objc_msgSend$hideCardInfoOverlay
+ _objc_msgSend$idCorrectedCardBuffer
+ _objc_msgSend$idProcessingImage
+ _objc_msgSend$idProcessingQueue
+ _objc_msgSend$reallocateCorrectedCardBuffers
+ _objc_msgSend$sendDidRecognizeObjects:
+ _objc_msgSend$setCcProcessingImage:
+ _objc_msgSend$setCcProcessingQueue:
+ _objc_msgSend$setContinuousMode:
+ _objc_msgSend$setHideCardAlignmentRect:
+ _objc_msgSend$setHideCardInfoOverlay:
+ _objc_msgSend$setIdProcessingImage:
+ _objc_msgSend$setIdProcessingQueue:
- GCC_except_table100
- GCC_except_table101
- GCC_except_table102
- GCC_except_table109
- GCC_except_table127
- GCC_except_table128
- GCC_except_table133
- GCC_except_table136
- GCC_except_table139
- GCC_except_table140
- GCC_except_table141
- GCC_except_table168
- GCC_except_table174
- GCC_except_table30
- GCC_except_table322
- GCC_except_table325
- GCC_except_table328
- GCC_except_table37
- GCC_except_table38
- GCC_except_table39
- GCC_except_table47
- GCC_except_table62
- GCC_except_table63
- GCC_except_table64
- GCC_except_table68
- GCC_except_table87
- _OBJC_IVAR_$_CRCameraReader._continousMode
- _OBJC_IVAR_$_CRCameraReader._correctedCardBuffer
- ___block_descriptor_73_ea8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_99_ea8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.200
- ___block_literal_global.310
- ___block_literal_global.312
- ___block_literal_global.315
- ___block_literal_global.399
- ___block_literal_global.401
- ___block_literal_global.438
- ___block_literal_global.440
- ___block_literal_global.460
- ___block_literal_global.465
- ___block_literal_global.470
- ___block_literal_global.489
- ___block_literal_global.502
- ___block_literal_global.512
- _objc_release_x2
CStrings:
+ ", "
+ "CRCameraReader document detection is only enabled in manual mode"
+ "CRCameraReaderDocumentCapturePathAutomatic"
+ "CRCameraReaderDocumentCapturePathManual"
+ "CRCameraReaderOutputDocumentCapture"
+ "CROutputTypeDocumentCapture"
+ "CROutputTypeDocumentCapture only supports manual capture via enableManualDocumentCapture"
+ "Capture exceeded session timeout."
+ "Disabling continuousMode, it is not supported for outputType(s) %@"
+ "Ignoring attempt to set CameraReader document output image width to %ld, below minimum width of %d."
+ "Skipping Credit Card recognition, multiple concurrent pipelines are only supported in continuousMode"
+ "Skipping ID scanning, multiple concurrent pipelines are only supported in continuousMode"
+ "Skipping document scanning, multiple concurrent pipelines are only supported in continuousMode"
+ "Skipping text camera, multiple concurrent pipelines are only supported in continuousMode"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_ccProcessingQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_idProcessingQueue"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,V_ccProcessingImage"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,V_idProcessingImage"
+ "TB,V_continuousMode"
+ "TB,V_enableManualDocumentCapture"
+ "TB,V_hideCardAlignmentRect"
+ "TB,V_hideCardInfoOverlay"
+ "TQ,V_documentCaptureMaxDimension"
+ "T^{__CVBuffer=},V_idCorrectedCardBuffer"
+ "_ccProcessingImage"
+ "_ccProcessingQueue"
+ "_continuousMode"
+ "_documentCaptureMaxDimension"
+ "_enableManualDocumentCapture"
+ "_hideCardAlignmentRect"
+ "_hideCardInfoOverlay"
+ "_idCorrectedCardBuffer"
+ "_idProcessingImage"
+ "_idProcessingQueue"
+ "ccProcessingImage"
+ "ccProcessingQueue"
+ "com.apple.CoreRecognition.ccProcessingQueue"
+ "com.apple.CoreRecognition.idProcessingQueue"
+ "continuousMode"
+ "dispatchSampleBuffer:onQueue:semaphore:work:"
+ "documentCaptureMaxDimension"
+ "enableManualDocumentCapture"
+ "findCodeInSampleBuffer: Box to found code timeout exceeded."
+ "findDocumentObjects:inPixelBuffer:cameraIntrinsicData:frameTime:"
+ "findObjects: Box to found code timeout exceeded."
+ "hideCardAlignmentRect"
+ "hideCardInfoOverlay"
+ "idCorrectedCardBuffer"
+ "idProcessingImage"
+ "idProcessingQueue"
+ "reallocateCorrectedCardBuffers"
+ "sendDidRecognizeObjects:"
+ "setCcProcessingImage:"
+ "setCcProcessingQueue:"
+ "setContinuousMode:"
+ "setDocumentCaptureMaxDimension:"
+ "setEnableManualDocumentCapture:"
+ "setHideCardAlignmentRect:"
+ "setHideCardInfoOverlay:"
+ "setIdCorrectedCardBuffer:"
+ "setIdProcessingImage:"
+ "setIdProcessingQueue:"
+ "v48@0:8^{opaqueCMSampleBuffer=}16@24@32@?40"
+ "v48@?0^{__CVBuffer=}8@\"NSData\"16{?=qiIq}24"
+ "\x81"
- "TB,V_continousMode"
- "_continousMode"

```
