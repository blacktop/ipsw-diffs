## CMContinuityCaptureCore

> `/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore`

```diff

-566.2.0.0.0
-  __TEXT.__text: 0x91ac8
-  __TEXT.__auth_stubs: 0x1030
-  __TEXT.__objc_methlist: 0x46e0
-  __TEXT.__const: 0x348
-  __TEXT.__gcc_except_tab: 0x42dc
-  __TEXT.__cstring: 0x7787
-  __TEXT.__oslogstring: 0xa616
+575.5.1.0.0
+  __TEXT.__text: 0x8fa84
+  __TEXT.__auth_stubs: 0xff0
+  __TEXT.__objc_methlist: 0x46c0
+  __TEXT.__const: 0x330
+  __TEXT.__gcc_except_tab: 0x4220
+  __TEXT.__cstring: 0x7583
+  __TEXT.__oslogstring: 0x9f9b
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x1f78
-  __TEXT.__objc_classname: 0xd65
-  __TEXT.__objc_methname: 0xbcb2
-  __TEXT.__objc_methtype: 0x27ef
-  __TEXT.__objc_stubs: 0x9080
-  __DATA_CONST.__got: 0x750
-  __DATA_CONST.__const: 0x1ae8
+  __TEXT.__unwind_info: 0x1f40
+  __TEXT.__objc_classname: 0xd62
+  __TEXT.__objc_methname: 0xbc5c
+  __TEXT.__objc_methtype: 0x280e
+  __TEXT.__objc_stubs: 0x9000
+  __DATA_CONST.__got: 0x748
+  __DATA_CONST.__const: 0x1b30
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2838
+  __DATA_CONST.__objc_selrefs: 0x2818
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x828
+  __AUTH_CONST.__auth_got: 0x808
   __AUTH_CONST.__const: 0xa00
-  __AUTH_CONST.__cfstring: 0x3f20
-  __AUTH_CONST.__objc_const: 0xb7c8
+  __AUTH_CONST.__cfstring: 0x3f80
+  __AUTH_CONST.__objc_const: 0xb808
   __AUTH_CONST.__objc_intobj: 0x510
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1360
-  __DATA.__objc_ivar: 0x838
+  __AUTH.__objc_data: 0x1220
+  __DATA.__objc_ivar: 0x840
   __DATA.__data: 0xcd0
-  __DATA.__bss: 0x190
-  __DATA.__common: 0x90
+  __DATA.__bss: 0x158
+  __DATA.__common: 0x80
+  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2243
-  Symbols:   3138
-  CStrings:  4061
+  Functions: 2234
+  Symbols:   3123
+  CStrings:  4030
 
Symbols:
+ _CMContinuityCaptureDeviceActiveConfigurationKVOKey
+ _fig_note_initialize_category_with_default_work_cf
+ _os_transaction_create
- _CFPreferencesGetAppIntegerValue
- _CVPixelBufferGetIOSurface
- _IOSurfaceGetID
- _dispatch_activate
- _fig_note_initialize_category_with_default_work
- _gGMFigKTraceEnabled
- _kCMContinuityCaptureEventAWDLDegradedEntry
- _kCMContinuityCaptureEventAWDLDegradedExit
- _kdebug_trace
CStrings:
+ "\x04\x11##"
+ "%!{(MISSING)public}@ postEvent : %!{(MISSING)public}@ entity : %!d(MISSING)"
+ "-[CMContinuityCaptureProvider registerStreamIntentForDevice:forTransportType:completion:]"
+ "-[CMContinuityCaptureVideoDevice stateMachineStartSendingBlurredFrames]"
+ "-[CMContinuityCaptureVideoDevice stateMachineStopSendingBlurredFrames]"
+ "-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_5"
+ "-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke_4"
+ "@\"NSObject<OS_os_transaction>\""
+ "_blurredFrameDispatchTimer"
+ "_blurredFrameTimerActive"
+ "_dockKitNotificationAgentIsTracking"
+ "_transaction"
+ "com.apple.continuitycamera"
+ "stateMachineStartSendingBlurredFrames"
+ "stateMachineStopSendingBlurredFrames"
+ "v24@?0@\"CMContinuityCaptureState\"8@\"CMContinuityCaptureStateMachineEvent\"16"
- "\x04\x11#\""
- "%!{(MISSING)public}@ %!{(MISSING)public}s device:%!{(MISSING)public}@"
- "%!{(MISSING)public}@ Connection Interrupted, AWDL Degraded"
- "-[CMContinuityCaptureCompositeDevice _disableStreamSessionForDevice:]"
- "-[CMContinuityCaptureProvider _registerStreamIntentForDevice:forTransportType:completion:]"
- "-[CMContinuityCaptureTimeSyncClock initWithClock:]"
- "-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]"
- "-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]_block_invoke"
- "-[CMContinuityCaptureVideoDevice stateMachineStartPauseTimer]"
- "-[CMContinuityCaptureVideoDevice stateMachineStopPauseTimer]"
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
- "_disableStreamSessionForDevice:"
- "_fakeFrameDispatchTimer"
- "_registerStreamIntentForDevice:forTransportType:completion:"
- "_unregisterStreamIntentForDevice:"
- "availableClockIdentifiers"
- "cmcontinuitycapturetimesyncclock_trace"
- "continuitycapture_timesync_heartbeat_interval"
- "disableStreamSessionForDevice:"
- "kCMContinuityCaptureEventAWDLDegradedEntry"
- "kCMContinuityCaptureEventAWDLDegradedExit"
- "stateMachineStartPauseTimer"
- "stateMachineStopPauseTimer"
- "\xf0Q"

```
