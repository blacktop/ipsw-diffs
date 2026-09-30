## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-830.10.1.1.0
-  __TEXT.__text: 0x1c8c54
-  __TEXT.__auth_stubs: 0x5060
+835.13.1.11.1
+  __TEXT.__text: 0x1c91cc
+  __TEXT.__auth_stubs: 0x5070
   __TEXT.__objc_methlist: 0x340
-  __TEXT.__cstring: 0x722d1
-  __TEXT.__const: 0xfd80
+  __TEXT.__cstring: 0x72681
+  __TEXT.__const: 0xfd70
   __TEXT.__gcc_except_tab: 0x3fc
   __TEXT.__oslogstring: 0x69f
-  __TEXT.__unwind_info: 0x2ac0
+  __TEXT.__unwind_info: 0x2ad0
   __TEXT.__eh_frame: 0xaa8
   __TEXT.__objc_classname: 0x174
   __TEXT.__objc_methname: 0x19a5
   __TEXT.__objc_methtype: 0xa56
   __TEXT.__objc_stubs: 0x1760
-  __DATA_CONST.__got: 0x1d30
-  __DATA_CONST.__const: 0x5f38
+  __DATA_CONST.__got: 0x1d28
+  __DATA_CONST.__const: 0x5f98
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x680
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x2840
+  __AUTH_CONST.__auth_got: 0x2848
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x79e0
+  __AUTH_CONST.__const: 0x7a20
   __AUTH_CONST.__cfstring: 0x10c60
   __AUTH_CONST.__objc_const: 0x1178
   __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x738
   __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0x18440
+  __DATA.__data: 0x18448
   __DATA.__bss: 0x9b0
-  __DATA.__common: 0xa04
+  __DATA.__common: 0xa08
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0xcc0
   __DATA_DIRTY.__bss: 0x2d0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3348
+  Functions: 3349
   Symbols:   6287
-  CStrings:  9738
+  CStrings:  9768
 
Symbols:
+ _FigSignalErrorAt3
+ _fig_log_get_emitter
- _FigSignalErrorAt
- _kAPSNetworkClockNotification_GrandmasterChanged
CStrings:
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "(Fig)"
+ "835.13.1.11.1"
+ "APEndpoint.c"
+ "APEndpointPlaybackSessionRemoteControl.m"
+ "APEndpointStreamAggregateAudio.c"
+ "APVirtualDisplayTestSink.c"
+ "Action not supported"
+ "Allocation error"
+ "Boolean apsession_isPeerKnown(APSenderSessionRef)"
+ "Cannot register path"
+ "Failed to create deep copy"
+ "Failed to de-serialize"
+ "Failed to serialize"
+ "Item is NULL"
+ "No data in response"
+ "No incoming message"
+ "No matched request found"
+ "Object invalidated"
+ "[%!{(MISSING)ptr}] Now Playing Info Updated: F=%!s(MISSING), Ar=%!@(MISSING), Al=%!@(MISSING), Ti=%!@(MISSING), T#=%!@(MISSING) of TT=%!@(MISSING), ET=%!@(MISSING) of Du=%!@(MISSING), Art=%!@(MISSING) (%!d(MISSING) bytes)\n"
+ "[%!{(MISSING)ptr}] Peer known with client [%!{(MISSING)ptr}] %!s(MISSING) (isPeerKnown: %!s(MISSING))%!?(MISSING){end}, error: %!m(MISSING)\n"
+ "[%!{(MISSING)ptr}] Updating stream resumed time for %!@(MISSING) (added: %!d(MISSING), total: %!d(MISSING), resumeEndEvent: 0x%!x(MISSING))"
+ "alloc failed"
+ "can't find valid video track"
+ "err"
+ "kCMBaseObjectError_Invalidated"
+ "kCMBaseObjectError_ParamErr"
+ "kFigBaseObjectError_AllocationFailed"
+ "kFigBaseObjectError_ValueNotAvailable"
+ "kFigEndpointError_AllocationFailed"
+ "kFigEndpointPlaybackSessionError_AllocationFailed"
+ "kFigEndpointPlaybackSessionError_InvalidParameter"
+ "messageID is missing in response event"
+ "type is missing in response event"
+ "void apPlayback_handleMetadataEvent(APMetadataSourceRef, CFTypeRef, APMetadataSourceEventType, CFTypeRef, CFStringRef, Boolean)"
+ "void carEndpoint_updateStreamResumedTimeIfNeeded(FigEndpointRef, APEndpointCarPlayStreamInfoRef, APSEventRecorderEvent)"
+ "void metadataSender_handleMRNowPlayingInfoChanged(APMetadataSenderRef, CFDictionaryRef, CFStringRef, Boolean)"
+ "void metadataSender_sendMRNowPlayingInfo(APMetadataSenderRef, CFDictionaryRef, CFStringRef, Boolean)"
+ "void metadataSource_handleNowPlayingInfoChangedInternal(APMetadataSourceRef, CFDictionaryRef, CFStringRef, Boolean)"
- "830.10.1.1"
- "BAE [%!{(MISSING)ptr}] %!s(MISSING)[0x%!X(MISSING)] Grandmaster changed\n"
- "[%!{(MISSING)ptr}] Now Playing Info Updated: Ar=%!@(MISSING), Al=%!@(MISSING), Ti=%!@(MISSING), T#=%!@(MISSING) of TT=%!@(MISSING), ET=%!@(MISSING) of Du=%!@(MISSING), Art=%!@(MISSING) (%!d(MISSING) bytes)\n"
- "metadataSource_notifyMetadataChangeApplier"
- "void apPlayback_handleMetadataEvent(APMetadataSourceRef, CFTypeRef, APMetadataSourceEventType, CFTypeRef, CFStringRef)"
- "void bufferedAudioEngine_handleClockGrandmasterChanged(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
- "void metadataSender_handleMRNowPlayingInfoChanged(APMetadataSenderRef, CFDictionaryRef, CFStringRef)"
- "void metadataSender_sendMRNowPlayingInfo(APMetadataSenderRef, CFDictionaryRef, CFStringRef)"
- "void metadataSource_handleNowPlayingInfoChangedInternal(APMetadataSourceRef, CFDictionaryRef, CFStringRef)"

```
