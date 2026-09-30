## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-3.512.0.0.0
-  __TEXT.__text: 0x1b26b0
+3.605.0.0.0
+  __TEXT.__text: 0x1b2580
   __TEXT.__auth_stubs: 0x3180
   __TEXT.__init_offsets: 0x18
   __TEXT.__objc_methlist: 0x268
   __TEXT.__const: 0x236af
-  __TEXT.__oslogstring: 0x1c4ce
-  __TEXT.__cstring: 0x185e5
+  __TEXT.__oslogstring: 0x1c407
+  __TEXT.__cstring: 0x1866f
   __TEXT.__gcc_except_tab: 0x6524
   __TEXT.__unwind_info: 0x3ca0
   __TEXT.__eh_frame: 0xa0

   __TEXT.__objc_methname: 0x1cbd
   __TEXT.__objc_methtype: 0x105f
   __TEXT.__objc_stubs: 0x1f80
-  __DATA_CONST.__got: 0x3238
+  __DATA_CONST.__got: 0x3240
   __DATA_CONST.__const: 0xa270
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x18d0
-  __AUTH_CONST.__auth_ptr: 0x98
+  __AUTH_CONST.__auth_ptr: 0x90
   __AUTH_CONST.__const: 0x2718
   __AUTH_CONST.__cfstring: 0x9c00
   __AUTH_CONST.__objc_const: 0x880

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5459
-  Symbols:   8905
-  CStrings:  6465
+  Functions: 5463
+  Symbols:   8911
+  CStrings:  6469
 
Symbols:
+ _CVAFaceTrackingLiteFilterCopyDecodedOutput
+ _kFigCaptureStreamSecureFaceTrackingConfigurationKey_TrackingFailureFieldOfViewModifier
- _CVAFaceTrackingLiteCopyDecodedOutput
- __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNode29AddSecureTrackedFacesMetadataEPNS_24H16ISPFilterGraphMessageERK37ISPExclaveCoreChRunKitFaceProcessRsltb
CStrings:
+ "%s - Cannot set face kit settings! ch=%u err=%u\n"
+ "%s - ch=%u enableaccessibility=%{bool}d enablespatialaudio=%{bool}d\n"
+ "%s - failed to copy decoded face tracking output cvaret=%d\n"
+ "%s - failed to create result dictionary for reqid=0x%08x\n"
+ "%s - failed to run face kit first pass err=%u reqid=0x%08x\n"
+ "%s - unrecognized activation expression=%u\n"
+ "%s - unrecognized confidence level=%u\n"
+ "%s - unrecognized failure type=%u\n"
+ "ConfigureFrameworkFaceKitSettings"
+ "FaceProcessResultCreateDictionaryRepresentation"
+ "convertExpressionActivation"
+ "convertTrackingConfidenceLevel"
+ "convertTrackingFailureType"
+ "face kit first pass channel=%u reqid=0x%08x\n"
- "%s - Cannot set face kit settings! result=%u\n"
- "%s - DetectedFaces=%u, TrackedFaces=%u\n"
- "%s - [Exclaves]: EK Face Kit Runkit failed, idl error=%d\n"
- "%s - [Exclaves]: H16ISPGraphExclaveFaceTrackingNode::%s index: %zu AngleInfoRoll: %f Rect[%f %f %f %f] Confidence %f \n"
- "%s - [Exclaves]: RGB Face Tracking: channel=%u\n"
- "AddSecureTrackedFacesMetadata"
- "Sent FaceKit config! channel=%u, numtrackedfaces=%u\n"
- "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::%s CVAFaceTrackingLiteCopyDecodedOutput failed, err=0x%08X \n"
- "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::%s RunKit FT reqID:0x%08x channel %d\n"
- "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::%s Skipped processing secure face tracking algorithm\n"

```
