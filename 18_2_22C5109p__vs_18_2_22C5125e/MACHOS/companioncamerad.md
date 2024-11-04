## companioncamerad

> `/System/Library/PrivateFrameworks/CompanionCamera.framework/Support/companioncamerad`

```diff

-2022.300.1.1.0
-  __TEXT.__text: 0x1e000
-  __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_stubs: 0x1d60
-  __TEXT.__objc_methlist: 0x27fc
-  __TEXT.__cstring: 0x10a8
-  __TEXT.__objc_methname: 0x3351
-  __TEXT.__objc_classname: 0x45f
-  __TEXT.__objc_methtype: 0x1152
+2022.300.4.0.0
+  __TEXT.__text: 0x1fcf4
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_stubs: 0x1de0
+  __TEXT.__objc_methlist: 0x2acc
+  __TEXT.__cstring: 0x118f
+  __TEXT.__objc_methname: 0x34dc
+  __TEXT.__objc_classname: 0x4bb
+  __TEXT.__objc_methtype: 0x1183
   __TEXT.__const: 0xf0
   __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__oslogstring: 0x5e4
+  __TEXT.__oslogstring: 0x60b
   __TEXT.__dlopen_cstrs: 0x4f
-  __TEXT.__unwind_info: 0x848
-  __DATA_CONST.__auth_got: 0x398
+  __TEXT.__unwind_info: 0x8b8
+  __DATA_CONST.__auth_got: 0x390
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__const: 0xa60
-  __DATA_CONST.__cfstring: 0xc60
-  __DATA_CONST.__objc_classlist: 0x148
+  __DATA_CONST.__cfstring: 0xca0
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x130
+  __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x5110
-  __DATA.__objc_selrefs: 0xd40
-  __DATA.__objc_ivar: 0x27c
-  __DATA.__objc_data: 0xcd0
+  __DATA.__objc_const: 0x5630
+  __DATA.__objc_selrefs: 0xdb0
+  __DATA.__objc_ivar: 0x294
+  __DATA.__objc_data: 0xe10
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 940
-  Symbols:   163
-  CStrings:  1029
+  Functions: 1004
+  Symbols:   162
+  CStrings:  1057
 
Symbols:
- _objc_retain_x26
CStrings:
+ "-[NCCompanionCamera pauseCapture:]"
+ "-[NCCompanionCamera resumeCapture:]"
+ "-[NCCompanionCamera xpc_didPauseCaptureTimerWithDate:]"
+ "-[NCCompanionCamera xpc_didResumeCaptureTimerWithDate:]"
+ "NCPauseCaptureRequest"
+ "NCPauseCaptureResponse"
+ "NCResumeCaptureRequest"
+ "NCResumeCaptureResponse"
+ "TB,N,V_capturingPaused"
+ "Td,N,V_capturePauseDate"
+ "Vv28@0:8B16@?<v@?@\"NSOrderedSet\"q@\"NSOrderedSet\"qB@\"NSDate\"B@\"NSDate\"qBBfBff@\"NSArray\"fqqqqqqqqBBBqB>20"
+ "_capturePauseDate"
+ "_capturingPaused"
+ "capturePauseDate"
+ "capturingPaused"
+ "hasCapturePauseDate"
+ "hasCapturingPaused"
+ "pauseCapture:"
+ "resumeCapture:"
+ "setCapturePauseDate:"
+ "setCapturingPaused:"
+ "setHasCapturePauseDate:"
+ "setHasCapturingPaused:"
+ "supportedCaptureDevice:%!@(MISSING) captureDevice:%!@(MISSING) supportedCaptureModes:%!@(MISSING) captureMode:%!@(MISSING) capturing:%!d(MISSING) captureStartDate:%!@(MISSING) capturingPaused:%!d(MISSING) capturePauseDate:%!@(MISSING) orientation:%!@(MISSING) toggleCameraDeviceSupport:%!d(MISSING) zoomSupport:%!d(MISSING) zoomAmount:%!f(MISSING) flashSupport:%!@(MISSING) flashMode:%!@(MISSING) hdrSupport:%!@(MISSING) hdrMode:%!@(MISSING) irisSupport:%!@(MISSING) irisMode:%!@(MISSING) sharedLibrarySupport:%!@(MISSING) sharedLibraryMode:%!@(MISSING) supportsMomentCapture:%!d(MISSING) burstSupport:%!d(MISSING) showingLivePreview:%!d(MISSING) shallowDepthOfFieldStatus:%!@(MISSING), spatial:%!d(MISSING)"
+ "v196@?0@\"NSOrderedSet\"8q16@\"NSOrderedSet\"24q32B40@\"NSDate\"44B52@\"NSDate\"56q64B72B76f80B84f88f92@\"NSArray\"96f104q108q116q124q132q140q148q156q164B172B176B180q184B192"
+ "xpc_didPauseCaptureTimerWithDate:"
+ "xpc_didResumeCaptureTimerWithDate:"
+ "xpc_pauseCaptureWithReply:"
+ "xpc_resumeCaptureWithReply:"
+ "{?=\"capturePauseDate\"b1\"captureStartDate\"b1\"captureDevice\"b1\"captureMode\"b1\"currentZoomMagnification\"b1\"flashMode\"b1\"flashSupport\"b1\"hdrMode\"b1\"hdrSupport\"b1\"irisMode\"b1\"irisSupport\"b1\"maximumZoomMagnification\"b1\"minimumZoomMagnification\"b1\"orientation\"b1\"shallowDepthOfFieldStatus\"b1\"sharedLibraryMode\"b1\"sharedLibrarySupport\"b1\"zoomAmount\"b1\"burstSupport\"b1\"capturing\"b1\"capturingPaused\"b1\"isSpatialCapture\"b1\"showingLivePreview\"b1\"supportsMomentCapture\"b1\"toggleCameraDeviceSupport\"b1\"zoomMagnificationSupport\"b1\"zoomSupport\"b1}"
- "Vv28@0:8B16@?<v@?@\"NSOrderedSet\"q@\"NSOrderedSet\"qB@\"NSDate\"qBBfBff@\"NSArray\"fqqqqqqqqBBBqB>20"
- "supportedCaptureDevice:%!@(MISSING) captureDevice:%!@(MISSING) supportedCaptureModes:%!@(MISSING) captureMode:%!@(MISSING) capturing:%!d(MISSING) captureStartDate:%!@(MISSING) orientation:%!@(MISSING) toggleCameraDeviceSupport:%!d(MISSING) zoomSupport:%!d(MISSING) zoomAmount:%!f(MISSING) flashSupport:%!@(MISSING) flashMode:%!@(MISSING) hdrSupport:%!@(MISSING) hdrMode:%!@(MISSING) irisSupport:%!@(MISSING) irisMode:%!@(MISSING) sharedLibrarySupport:%!@(MISSING) sharedLibraryMode:%!@(MISSING) supportsMomentCapture:%!d(MISSING) burstSupport:%!d(MISSING) showingLivePreview:%!d(MISSING) shallowDepthOfFieldStatus:%!@(MISSING), spatial:%!d(MISSING)"
- "v184@?0@\"NSOrderedSet\"8q16@\"NSOrderedSet\"24q32B40@\"NSDate\"44q52B60B64f68B72f76f80@\"NSArray\"84f92q96q104q112q120q128q136q144q152B160B164B168q172B180"
- "{?=\"captureStartDate\"b1\"captureDevice\"b1\"captureMode\"b1\"currentZoomMagnification\"b1\"flashMode\"b1\"flashSupport\"b1\"hdrMode\"b1\"hdrSupport\"b1\"irisMode\"b1\"irisSupport\"b1\"maximumZoomMagnification\"b1\"minimumZoomMagnification\"b1\"orientation\"b1\"shallowDepthOfFieldStatus\"b1\"sharedLibraryMode\"b1\"sharedLibrarySupport\"b1\"zoomAmount\"b1\"burstSupport\"b1\"capturing\"b1\"isSpatialCapture\"b1\"showingLivePreview\"b1\"supportsMomentCapture\"b1\"toggleCameraDeviceSupport\"b1\"zoomMagnificationSupport\"b1\"zoomSupport\"b1}"

```
