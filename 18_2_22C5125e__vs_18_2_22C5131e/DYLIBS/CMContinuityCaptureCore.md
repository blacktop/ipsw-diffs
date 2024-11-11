## CMContinuityCaptureCore

> `/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore`

```diff

-587.60.10.122.3
-  __TEXT.__text: 0x91888
-  __TEXT.__auth_stubs: 0x1040
+587.60.14.122.2
+  __TEXT.__text: 0x8fe94
+  __TEXT.__auth_stubs: 0x1000
   __TEXT.__objc_methlist: 0x46d0
-  __TEXT.__const: 0x348
-  __TEXT.__gcc_except_tab: 0x425c
-  __TEXT.__cstring: 0x77bf
-  __TEXT.__oslogstring: 0xa651
+  __TEXT.__const: 0x330
+  __TEXT.__gcc_except_tab: 0x4220
+  __TEXT.__cstring: 0x75c8
+  __TEXT.__oslogstring: 0xa001
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x1f50
+  __TEXT.__unwind_info: 0x1f40
   __TEXT.__objc_classname: 0xd64
-  __TEXT.__objc_methname: 0xbc99
+  __TEXT.__objc_methname: 0xbc7f
   __TEXT.__objc_methtype: 0x280e
-  __TEXT.__objc_stubs: 0x9040
-  __DATA_CONST.__got: 0x750
+  __TEXT.__objc_stubs: 0x9020
+  __DATA_CONST.__got: 0x748
   __DATA_CONST.__const: 0x1b30
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2828
+  __DATA_CONST.__objc_selrefs: 0x2820
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x830
-  __AUTH_CONST.__const: 0x9e0
-  __AUTH_CONST.__cfstring: 0x3fc0
+  __AUTH_CONST.__auth_got: 0x810
+  __AUTH_CONST.__const: 0xa00
+  __AUTH_CONST.__cfstring: 0x3f80
   __AUTH_CONST.__objc_const: 0xb828
   __AUTH_CONST.__objc_intobj: 0x510
   __AUTH_CONST.__objc_doubleobj: 0x80

   __DATA.__objc_ivar: 0x844
   __DATA.__data: 0xcd0
   __DATA.__bss: 0x158
-  __DATA.__common: 0x90
+  __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2238
-  Symbols:   3134
-  CStrings:  4065
+  Functions: 2237
+  Symbols:   3128
+  CStrings:  4036
 
Symbols:
- _CFPreferencesGetAppIntegerValue
- _CVPixelBufferGetIOSurface
- _IOSurfaceGetID
- _gGMFigKTraceEnabled
- _kdebug_trace
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
- "<<<< CMContinuityCaptureTimeSyncClock >>>> %!s(MISSING): %!@(MISSING) %!l(MISSING)ld: (%!l(MISSING)ld) %!l(MISSING)ld -> %!l(MISSING)ld"
- "<<<< CMContinuityCaptureTimeSyncClock >>>> %!s(MISSING): %!@(MISSING) starting heart beat signposts with interval %!l(MISSING)u seconds"
- "<<<< CMContinuityCaptureTimeSyncClock >>>> %!s(MISSING): Failed to create PTP clock with identifier %!l(MISSING)lu, available identifiers %!@(MISSING)"
- "<<<< CMContinuityCaptureXPCClientCCD >>>> %!s(MISSING): connection interrupted %!@(MISSING). Scheduling reconnect in 3 seconds."
- "<<<< CMContinuityCaptureXPCClientCCD >>>> %!s(MISSING): connection invalidated %!@(MISSING)"
- "<<<< CMContinuityCaptureXPCServer >>>> %!s(MISSING): connection interrupted %!@(MISSING)"
- "<<<< CMContinuityCaptureXPCServer >>>> %!s(MISSING): connection invalidated %!@(MISSING)"
- "<<<< NSCoding+CVPixelBufferRef >>>> %!s(MISSING): Could not create pixel buffer: %!d(MISSING)"
- "<<<< NSCoding+CVPixelBufferRef >>>> %!s(MISSING): Could not read source media %!@(MISSING), falling back to pixel buffer copy"
- "<<<< NSCoding+CVPixelBufferRef >>>> %!s(MISSING): Could not serialize pixel buffer, error %!d(MISSING)"
- "<<<< NSCoding+CVPixelBufferRef >>>> %!s(MISSING): Error creating pixel buffer %!z(MISSING)u x %!z(MISSING)u: %!d(MISSING)"
- "<<<< NSCoding+CVPixelBufferRef >>>> %!s(MISSING): Expected source media but pixel buffer data was found instead (not fatal)"
- "<<<< NSCoding+CVPixelBufferRef >>>> %!s(MISSING): Failed to create pixel buffer %!z(MISSING)u x %!z(MISSING)u"
- "<<<< NSCoding+CVPixelBufferRef >>>> %!s(MISSING): Fallback not using atom data, outdated peer connection for pixel buffer"
- "<<<< NSCoding+CVPixelBufferRef >>>> %!s(MISSING): No pixel data"
- "<<<< NSCoding+CVPixelBufferRef >>>> %!s(MISSING): bad source image offset"
- "<<<< NSCoding+CVPixelBufferRef >>>> %!s(MISSING): image planes don't match, encoded %!d(MISSING) allocated %!d(MISSING)"
- "<<<< NSCoding+CVPixelBufferRef >>>> %!s(MISSING): source image offset overrun"
- "<<<< NSCoding+CVPixelBufferRef >>>> %!s(MISSING): source image stride overrun"
- "availableClockIdentifiers"
- "cmcontinuitycapturetimesyncclock_trace"
- "continuitycapture_timesync_heartbeat_interval"

```
