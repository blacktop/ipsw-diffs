## CMContinuityCaptureCore

> `/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0x8fd4c
-  __TEXT.__auth_stubs: 0x1010
+587.140.7.122.2
+  __TEXT.__text: 0x91770
+  __TEXT.__auth_stubs: 0x1050
   __TEXT.__objc_methlist: 0x5624
   __TEXT.__const: 0x2a8
-  __TEXT.__gcc_except_tab: 0x4320
-  __TEXT.__cstring: 0x763c
-  __TEXT.__oslogstring: 0xa0a4
+  __TEXT.__gcc_except_tab: 0x435c
+  __TEXT.__cstring: 0x7833
+  __TEXT.__oslogstring: 0xa6f4
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x2090
+  __TEXT.__unwind_info: 0x20a8
   __TEXT.__objc_classname: 0xd65
-  __TEXT.__objc_methname: 0xbd3e
+  __TEXT.__objc_methname: 0xbd58
   __TEXT.__objc_methtype: 0x280e
-  __TEXT.__objc_stubs: 0x90a0
-  __DATA_CONST.__got: 0x750
+  __TEXT.__objc_stubs: 0x90c0
+  __DATA_CONST.__got: 0x758
   __DATA_CONST.__const: 0x1b28
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a48
+  __DATA_CONST.__objc_selrefs: 0x2a50
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x818
-  __AUTH_CONST.__const: 0xa00
-  __AUTH_CONST.__cfstring: 0x4000
+  __AUTH_CONST.__auth_got: 0x838
+  __AUTH_CONST.__const: 0x9e0
+  __AUTH_CONST.__cfstring: 0x4040
   __AUTH_CONST.__objc_const: 0x9d00
   __AUTH_CONST.__objc_intobj: 0x510
   __AUTH_CONST.__objc_doubleobj: 0x80

   __DATA.__objc_ivar: 0x854
   __DATA.__data: 0xcd0
   __DATA.__bss: 0x158
-  __DATA.__common: 0x80
+  __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23FFF334-36BE-3D86-B054-BF4DF305D340
-  Functions: 2327
-  Symbols:   8299
-  CStrings:  4521
+  UUID: B553F428-6E3A-3041-91DA-4BC5CC3BD6DA
+  Functions: 2336
+  Symbols:   8324
+  CStrings:  4552
 
Symbols:
+ -[CVPixelBufferCoder initWithCoder:].cold.2
+ -[CVPixelBufferCoder initWithCoder:].cold.3
+ _CFPreferencesGetAppIntegerValue
+ _CVPixelBufferGetIOSurface
+ _IOSurfaceGetID
+ ___67-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]_block_invoke
+ ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke.77
+ ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke.78
+ ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke.82
+ ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke.71
+ ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke.72
+ ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_2.73
+ _gCMContinuityCaptureTimeSyncClockTrace
+ _gGMFigKTraceEnabled
+ _kdebug_trace
+ _objc_msgSend$availableClockIdentifiers
- ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke.81
- ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke_3
- ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke_4
- ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_3
- ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_4
- ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_5
- ___block_literal_global.72
CStrings:
+ "-[CMContinuityCaptureTimeSyncClock initWithClock:]"
+ "-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]"
+ "-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]_block_invoke"
+ "-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_2"
+ "-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke_2"
+ "-[CVPixelBufferCoder _createPixelBufferForImage:fillWidth:fillHeight:]"
+ "-[CVPixelBufferCoder encodeWithCoder:]"
+ "-[CVPixelBufferCoder initWithCoder:]"
+ "-[NSCoder(CVPixelBuffer) decodeCVPixelBufferForKey:expectSourceMedia:]"
+ "<<<< CMContinuityCaptureTimeSyncClock >>>> %s: %@ %lld: (%lld) %lld -> %lld"
+ "<<<< CMContinuityCaptureTimeSyncClock >>>> %s: %@ starting heart beat signposts with interval %lu seconds"
+ "<<<< CMContinuityCaptureTimeSyncClock >>>> %s: Failed to create PTP clock with identifier %llu, available identifiers %@"
+ "<<<< CMContinuityCaptureXPCClientCCD >>>> %s: connection interrupted %@. Scheduling reconnect in 3 seconds."
+ "<<<< CMContinuityCaptureXPCClientCCD >>>> %s: connection invalidated %@"
+ "<<<< CMContinuityCaptureXPCServer >>>> %s: connection interrupted %@"
+ "<<<< CMContinuityCaptureXPCServer >>>> %s: connection invalidated %@"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Could not create pixel buffer: %d"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Could not read source media %@, falling back to pixel buffer copy"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Could not serialize pixel buffer, error %d"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Error creating pixel buffer %zu x %zu: %d"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Expected source media but pixel buffer data was found instead (not fatal)"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Failed to create pixel buffer %zu x %zu"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Fallback not using atom data, outdated peer connection for pixel buffer"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: No pixel data"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: bad source image offset"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: image planes don't match, encoded %d allocated %d"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: source image offset overrun"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: source image stride overrun"
+ "availableClockIdentifiers"
+ "cmcontinuitycapturetimesyncclock_trace"
+ "continuitycapture_timesync_heartbeat_interval"
- "-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_5"
- "-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke_4"

```
