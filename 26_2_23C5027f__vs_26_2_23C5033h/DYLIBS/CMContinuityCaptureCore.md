## CMContinuityCaptureCore

> `/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore`

```diff

-664.60.5.0.1
-  __TEXT.__text: 0x8c010
-  __TEXT.__auth_stubs: 0x1060
+664.60.7.0.0
+  __TEXT.__text: 0x8a790
+  __TEXT.__auth_stubs: 0x1020
   __TEXT.__objc_methlist: 0x5d88
-  __TEXT.__const: 0x310
-  __TEXT.__gcc_except_tab: 0x3190
-  __TEXT.__cstring: 0x7b83
-  __TEXT.__oslogstring: 0xa9a1
+  __TEXT.__const: 0x300
+  __TEXT.__gcc_except_tab: 0x3170
+  __TEXT.__cstring: 0x798c
+  __TEXT.__oslogstring: 0xa351
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x20e8
+  __TEXT.__unwind_info: 0x20d0
   __TEXT.__objc_classname: 0xdf6
-  __TEXT.__objc_methname: 0xd8d1
+  __TEXT.__objc_methname: 0xd8b7
   __TEXT.__objc_methtype: 0x2f1b
-  __TEXT.__objc_stubs: 0x9640
-  __DATA_CONST.__got: 0x7b0
+  __TEXT.__objc_stubs: 0x9620
+  __DATA_CONST.__got: 0x7a8
   __DATA_CONST.__const: 0x1bd0
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e90
+  __DATA_CONST.__objc_selrefs: 0x2e88
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x840
-  __AUTH_CONST.__const: 0xa20
-  __AUTH_CONST.__cfstring: 0x4280
+  __AUTH_CONST.__auth_got: 0x820
+  __AUTH_CONST.__const: 0xa40
+  __AUTH_CONST.__cfstring: 0x4240
   __AUTH_CONST.__objc_const: 0xa478
   __AUTH_CONST.__objc_intobj: 0x510
   __AUTH_CONST.__objc_doubleobj: 0x80

   __DATA.__objc_ivar: 0x88c
   __DATA.__data: 0xd98
   __DATA.__bss: 0x168
-  __DATA.__common: 0x90
+  __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F0413878-CA86-339D-8ECC-0A29D571E61B
-  Functions: 2405
-  Symbols:   8568
-  CStrings:  4803
+  UUID: CCE35D25-85CF-321F-B4DE-25D3FEE93EFB
+  Functions: 2396
+  Symbols:   8543
+  CStrings:  4772
 
Symbols:
+ ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke.91
+ ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke_3
+ ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke_4
+ ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_3
+ ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_4
+ ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_5
+ ___block_literal_global.81
- -[CVPixelBufferCoder initWithCoder:].cold.2
- -[CVPixelBufferCoder initWithCoder:].cold.3
- _CFPreferencesGetAppIntegerValue
- _CVPixelBufferGetIOSurface
- _IOSurfaceGetID
- ___67-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]_block_invoke
- ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke.87
- ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke.88
- ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke.92
- ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke.80
- ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke.81
- ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_2.82
- _gCMContinuityCaptureTimeSyncClockTrace
- _gGMFigKTraceEnabled
- _kdebug_trace
- _objc_msgSend$availableClockIdentifiers
CStrings:
+ "-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_5"
+ "-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke_4"
- "-[CMContinuityCaptureTimeSyncClock initWithClock:]"
- "-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]"
- "-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]_block_invoke"
- "-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_2"
- "-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke_2"
- "-[CVPixelBufferCoder _createPixelBufferForImage:fillWidth:fillHeight:]"
- "-[CVPixelBufferCoder encodeWithCoder:]"
- "-[CVPixelBufferCoder initWithCoder:]"
- "-[NSCoder(CVPixelBuffer) decodeCVPixelBufferForKey:expectSourceMedia:]"
- "<<<< CMContinuityCaptureTimeSyncClock >>>> %s: %@ %lld: (%lld) %lld -> %lld"
- "<<<< CMContinuityCaptureTimeSyncClock >>>> %s: %@ starting heart beat signposts with interval %lu seconds"
- "<<<< CMContinuityCaptureTimeSyncClock >>>> %s: Failed to create PTP clock with identifier %llu, available identifiers %@"
- "<<<< CMContinuityCaptureXPCClientCCD >>>> %s: connection interrupted %@. Scheduling reconnect in 3 seconds."
- "<<<< CMContinuityCaptureXPCClientCCD >>>> %s: connection invalidated %@"
- "<<<< CMContinuityCaptureXPCServer >>>> %s: connection interrupted %@"
- "<<<< CMContinuityCaptureXPCServer >>>> %s: connection invalidated %@"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: Could not create pixel buffer: %d"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: Could not read source media %@, falling back to pixel buffer copy"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: Could not serialize pixel buffer, error %d"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: Error creating pixel buffer %zu x %zu: %d"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: Expected source media but pixel buffer data was found instead (not fatal)"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: Failed to create pixel buffer %zu x %zu"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: Fallback not using atom data, outdated peer connection for pixel buffer"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: No pixel data"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: bad source image offset"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: image planes don't match, encoded %d allocated %d"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: source image offset overrun"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: source image stride overrun"
- "availableClockIdentifiers"
- "cmcontinuitycapturetimesyncclock_trace"
- "continuitycapture_timesync_heartbeat_interval"

```
