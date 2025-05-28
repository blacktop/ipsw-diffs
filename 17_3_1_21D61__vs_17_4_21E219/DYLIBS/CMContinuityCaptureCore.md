## CMContinuityCaptureCore

> `/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore`

```diff

-472.1.2.0.0
-  __TEXT.__text: 0x5c0fc
+475.31.1.0.0
+  __TEXT.__text: 0x5c20c
   __TEXT.__auth_stubs: 0xb40
   __TEXT.__objc_methlist: 0x3140
   __TEXT.__const: 0x1b0
   __TEXT.__gcc_except_tab: 0x20b0
   __TEXT.__cstring: 0x593e
-  __TEXT.__oslogstring: 0x6e2a
+  __TEXT.__oslogstring: 0x6e56
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__unwind_info: 0x1460
   __TEXT.__objc_classname: 0xa62
-  __TEXT.__objc_methname: 0x8e86
+  __TEXT.__objc_methname: 0x8e9a
   __TEXT.__objc_methtype: 0x205f
   __TEXT.__objc_stubs: 0x6da0
   __DATA_CONST.__got: 0x278

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x7610
   __DATA_CONST.__objc_selrefs: 0x1fa0
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x310
+  __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x80
   __AUTH_CONST.__cfstring: 0x3400
   __AUTH_CONST.__objc_const: 0x1320

   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x5b0
   __AUTH.__objc_data: 0xe10
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x310
-  __DATA.__objc_superrefs: 0x160
   __DATA.__objc_ivar: 0x5bc
   __DATA.__data: 0xae0
   __DATA.__bss: 0x158

   - /usr/lib/libobjc.A.dylib
   Functions: 1607
   Symbols:   5813
-  CStrings:  3073
+  CStrings:  3075
 
Symbols:
+ ___62-[CMContinuityCaptureSidecarTransportBase setupSidecarStreams]_block_invoke.329
+ ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke.76
+ ___71-[CMContinuityCaptureRapportTransportBase _enqueueResponse:identifier:]_block_invoke.390
+ ___71-[CMContinuityCaptureRapportTransportBase _enqueueResponse:identifier:]_block_invoke.392
+ ___71-[CMContinuityCaptureSidecarTransportBase _enqueueResponse:identifier:]_block_invoke.313
+ ___71-[CMContinuityCaptureSidecarTransportBase _enqueueResponse:identifier:]_block_invoke.315
+ ___74-[CMContinuityCaptureTransportRapportDevice enqueueReactionEffect:entity:]_block_invoke.190
+ ___74-[CMContinuityCaptureTransportSidecarDevice enqueueReactionEffect:entity:]_block_invoke.120
+ ___81-[CMContinuityCaptureTransportRapportDevice captureStillImage:entity:completion:]_block_invoke.187
+ ___81-[CMContinuityCaptureTransportSidecarDevice captureStillImage:entity:completion:]_block_invoke.117
+ ___82-[CMContinuityCaptureTransportSidecarDevice handleSynchronizeAudioClockCompletion]_block_invoke.114
+ ___84-[CMContinuityCaptureSidecarTransportBase createTimeSyncClockForSession:completion:]_block_invoke.330
+ ___85-[CMContinuityCaptureTransportRapportDevice _relaySidebandMessageType:overTransport:]_block_invoke.175
+ ___85-[CMContinuityCaptureTransportRapportDevice _relaySidebandMessageType:overTransport:]_block_invoke.180
+ ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke.402
+ ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke.409
+ ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke_2.410
+ ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke_2.410.cold.1
+ ___95+[CMContinuityCaptureTransportRapportDevice queryCameraCapabilitiesFromRemoteDevice:transport:]_block_invoke.171
+ ___block_literal_global.122
+ ___block_literal_global.131
+ ___block_literal_global.192
+ ___block_literal_global.199
+ ___block_literal_global.317
+ ___block_literal_global.394
+ ___block_literal_global.67
- ___62-[CMContinuityCaptureSidecarTransportBase setupSidecarStreams]_block_invoke.328
- ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke.75
- ___71-[CMContinuityCaptureRapportTransportBase _enqueueResponse:identifier:]_block_invoke.388
- ___71-[CMContinuityCaptureRapportTransportBase _enqueueResponse:identifier:]_block_invoke.391
- ___71-[CMContinuityCaptureSidecarTransportBase _enqueueResponse:identifier:]_block_invoke.311
- ___71-[CMContinuityCaptureSidecarTransportBase _enqueueResponse:identifier:]_block_invoke.314
- ___74-[CMContinuityCaptureTransportRapportDevice enqueueReactionEffect:entity:]_block_invoke.189
- ___74-[CMContinuityCaptureTransportSidecarDevice enqueueReactionEffect:entity:]_block_invoke.119
- ___81-[CMContinuityCaptureTransportRapportDevice captureStillImage:entity:completion:]_block_invoke.186
- ___81-[CMContinuityCaptureTransportSidecarDevice captureStillImage:entity:completion:]_block_invoke.116
- ___82-[CMContinuityCaptureTransportSidecarDevice handleSynchronizeAudioClockCompletion]_block_invoke.113
- ___84-[CMContinuityCaptureSidecarTransportBase createTimeSyncClockForSession:completion:]_block_invoke.329
- ___85-[CMContinuityCaptureTransportRapportDevice _relaySidebandMessageType:overTransport:]_block_invoke.173
- ___85-[CMContinuityCaptureTransportRapportDevice _relaySidebandMessageType:overTransport:]_block_invoke.178
- ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke.401
- ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke.407
- ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke_2.409
- ___89-[CMContinuityCaptureRapportTransportBase createTimeSyncClockWithPeerAddress:completion:]_block_invoke_2.409.cold.1
- ___95+[CMContinuityCaptureTransportRapportDevice queryCameraCapabilitiesFromRemoteDevice:transport:]_block_invoke.170
- ___block_literal_global.130
- ___block_literal_global.191
- ___block_literal_global.198
- ___block_literal_global.316
- ___block_literal_global.393
- ___block_literal_global.66
CStrings:
+ "%@ Stream Stop failed with error %{public}@"
+ "T@\"NSString\",?,R,C"

```
