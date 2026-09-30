## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-830.2.0.0.0
-  __TEXT.__text: 0x1c6ac0
-  __TEXT.__auth_stubs: 0x5010
+830.4.1.0.0
+  __TEXT.__text: 0x1c71e0
+  __TEXT.__auth_stubs: 0x5020
   __TEXT.__objc_methlist: 0x340
-  __TEXT.__cstring: 0x71c6d
+  __TEXT.__cstring: 0x71f43
   __TEXT.__const: 0xfd30
   __TEXT.__gcc_except_tab: 0x3d8
   __TEXT.__oslogstring: 0x69f
-  __TEXT.__unwind_info: 0x2a78
+  __TEXT.__unwind_info: 0x2a88
   __TEXT.__eh_frame: 0xaa8
   __TEXT.__objc_classname: 0x174
   __TEXT.__objc_methname: 0x19a5

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x680
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x2818
+  __AUTH_CONST.__auth_got: 0x2820
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x79c0
   __AUTH_CONST.__cfstring: 0x10bc0

   __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x608
   __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0x18320
-  __DATA.__bss: 0x9a8
+  __DATA.__data: 0x18390
+  __DATA.__bss: 0x9b0
   __DATA.__common: 0xa04
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0xd30
-  __DATA_DIRTY.__bss: 0x2d8
+  __DATA_DIRTY.__data: 0xcc0
+  __DATA_DIRTY.__bss: 0x2d0
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3327
-  Symbols:   6257
-  CStrings:  9700
+  Functions: 3331
+  Symbols:   6262
+  CStrings:  9730
 
Symbols:
+ _fig_log_get_emitter
+ _APEndpointRemoteControlSessionCreate
+ _FigSignalErrorAt3
- _FigSignalErrorAt
- _APEndpointRemoteControlSessionAirPlayCreate
CStrings:
+ "APEndpointRemoteControlSessionCreate"
+ "APVirtualDisplayTestSink.c"
+ "Object invalidated"
+ "kCMBaseObjectError_Invalidated"
+ "messageID is missing in response event"
+ "APEndpoint.c"
+ "No data in response"
+ "No incoming message"
+ "Item is NULL"
+ "Cannot register path"
+ "APEndpointPlaybackSessionRemoteControl.m"
+ "APEndpointRemoteControlSession.%!{(MISSING)ptr}.notification"
+ "kFigBaseObjectError_ValueNotAvailable"
+ "Allocation error"
+ "kFigEndpointPlaybackSessionError_AllocationFailed"
+ "alloc failed"
+ "kFigEndpointError_AllocationFailed"
+ "Action not supported"
+ "kCMBaseObjectError_ParamErr"
+ "APEndpointRemoteControlSession"
+ "No matched request found"
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "Failed to serialize"
+ "Failed to de-serialize"
+ "[%!{(MISSING)ptr}] Disable remote audio render.\n"
+ "APEndpointRemoteControlSession.%!{(MISSING)ptr}.teardownQueue"
+ "APEndpointRemoteControlSession.%!{(MISSING)ptr}.network"
+ "kFigEndpointPlaybackSessionError_InvalidParameter"
+ "830.4.1"
+ "(Fig)"
+ "Failed to create deep copy"
+ "err"
+ "<APEndpointRemoteControlSession '%!@(MISSING)'>"
+ "kFigBaseObjectError_AllocationFailed"
+ "APEndpointStreamAggregateAudio.c"
+ "OSStatus APEndpointRemoteControlSessionCreate(CFAllocatorRef, APSenderSessionRef, CFStringRef, CFDictionaryRef, FigEndpointCommChannelCreationOptionControlType, FigEndpointRemoteControlSessionRef *)"
+ "endpointLocal_copyFromEndpointDescription"
+ "can't find valid video track"
+ "type is missing in response event"
- "OSStatus APEndpointRemoteControlSessionAirPlayCreate(CFAllocatorRef, APSenderSessionRef, CFStringRef, CFDictionaryRef, FigEndpointCommChannelCreationOptionControlType, FigEndpointRemoteControlSessionRef *)"
- "APEndpointRemoteControlSessionAirPlay.%!{(MISSING)ptr}.notification"
- "830.2"
- "<APEndpointRemoteControlSessionAirPlay '%!@(MISSING)'>"
- "APEndpointRemoteControlSessionAirPlay"
- "[%!{(MISSING)ptr}] Disable remote audio render. Supporting all AudioFormatsForBufferedSender.\n"
- "APEndpointRemoteControlSessionAirPlayCreate"
- "APEndpointRemoteControlSessionAirPlay.%!{(MISSING)ptr}.network"
- "APEndpointRemoteControlSessionAirPlay.%!{(MISSING)ptr}.teardownQueue"

```
