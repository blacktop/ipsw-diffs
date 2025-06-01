## AnnounceDaemon

> `/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon`

```diff

-217.40.9.0.0
-  __TEXT.__text: 0x4f388
+217.50.3.0.0
+  __TEXT.__text: 0x4f74c
   __TEXT.__auth_stubs: 0x1010
-  __TEXT.__objc_methlist: 0x2e34
+  __TEXT.__objc_methlist: 0x2e9c
   __TEXT.__const: 0x26c
-  __TEXT.__cstring: 0x2aa8
-  __TEXT.__oslogstring: 0x5684
+  __TEXT.__cstring: 0x2bd8
+  __TEXT.__oslogstring: 0x573f
   __TEXT.__gcc_except_tab: 0xae4
   __TEXT.__swift5_typeref: 0x1eb
   __TEXT.__swift5_capture: 0x54

   __TEXT.__swift5_fieldmd: 0xe4
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0x127c
+  __TEXT.__unwind_info: 0x1288
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x9d2
-  __TEXT.__objc_methname: 0xb4f6
+  __TEXT.__objc_methname: 0xb6c0
   __TEXT.__objc_methtype: 0x2911
-  __TEXT.__objc_stubs: 0x89a0
+  __TEXT.__objc_stubs: 0x8a60
   __DATA_CONST.__got: 0x4c8
-  __DATA_CONST.__const: 0x1690
+  __DATA_CONST.__const: 0x16b8
   __DATA_CONST.__objc_classlist: 0x150
-  __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x178
+  __DATA_CONST.__objc_catlist: 0x88
+  __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6590
-  __DATA_CONST.__objc_selrefs: 0x25f0
-  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_const: 0x6648
+  __DATA_CONST.__objc_selrefs: 0x2630
+  __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_classrefs: 0x3c8
   __DATA_CONST.__objc_superrefs: 0x108
   __AUTH_CONST.__const: 0x900
-  __AUTH_CONST.__objc_const: 0x12e8
+  __AUTH_CONST.__objc_const: 0x1328
   __AUTH_CONST.__cfstring: 0x13a0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x818
   __AUTH.__objc_data: 0x598
   __AUTH.__data: 0x68
-  __DATA.__objc_ivar: 0x290
+  __DATA.__objc_ivar: 0x294
   __DATA.__objc_data: 0x68
-  __DATA.__data: 0x1260
+  __DATA.__data: 0x12c8
   __DATA.__bss: 0x280
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x948

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C358367F-63AE-3FA2-92DB-FDD8B72CA5DE
-  Functions: 1484
-  Symbols:   5399
-  CStrings:  3144
+  UUID: 5F87DD36-82D9-3760-B53F-5A1114FA3A3F
+  Functions: 1506
+  Symbols:   5405
+  CStrings:  3165
 
Symbols:
+ -[ANTrackPlayer setSomeOtherSidekickSessionAudioIsPlaying:]
+ -[ANTrackPlayer someOtherSidekickSessionAudioIsPlaying]
+ GCC_except_table70
+ _OBJC_IVAR_$_ANTrackPlayer._someOtherSidekickSessionAudioIsPlaying
+ __CATEGORY_NSXPCInterface_$_AnnounceDaemon
+ __OBJC_$_CLASS_METHODS_NSXPCInterface(AnnounceDaemon)
+ ___46-[ANTrackPlayer playerItemPlayedToEndHandler:]_block_invoke.71
+ ___64-[ANAnnounceServiceListener listener:shouldAcceptNewConnection:]_block_invoke.32
+ ___66-[ANTonePlayerServiceListener listener:shouldAcceptNewConnection:]_block_invoke.5
+ ___71-[ANPlaybackSessionServiceListener listener:shouldAcceptNewConnection:]_block_invoke.19
+ ___71-[ANPlaybackSessionServiceListener listener:shouldAcceptNewConnection:]_block_invoke.23
+ ___96-[ANPlaybackSessionServiceListener coordinator:didReceiveAnnouncement:forGroupID:forEndpointID:]_block_invoke.31
+ ___block_descriptor_56_e8_32s40w_e5_v8?0ls32l8w40l8
+ _objc_msgSend$an_announceServiceInterface
+ _objc_msgSend$an_localPlaybackSessionServiceDelegateInterface
+ _objc_msgSend$an_localPlaybackSessionServiceInterface
+ _objc_msgSend$an_remotePlaybackSessionServiceDelegateInterface
+ _objc_msgSend$an_remotePlaybackSessionServiceInterface
+ _objc_msgSend$an_tonePlayerServiceInterface
- GCC_except_table71
- __OBJC_PROTOCOL_REFERENCE_$_ANAnnounceServiceInterface
- __OBJC_PROTOCOL_REFERENCE_$_ANLocalPlaybackSessionServiceInterface
- __OBJC_PROTOCOL_REFERENCE_$_ANLocalPlaybackSessionServiceInterfaceDelegate
- __OBJC_PROTOCOL_REFERENCE_$_ANRemotePlaybackSessionServiceClientInterface
- __OBJC_PROTOCOL_REFERENCE_$_ANRemotePlaybackSessionServiceInterface
- __OBJC_PROTOCOL_REFERENCE_$_ANTonePlayerServiceInterface
- ___46-[ANTrackPlayer playerItemPlayedToEndHandler:]_block_invoke.72
- ___49-[ANTrackPlayer audioSessionInterruptionHandler:]_block_invoke.71
- ___64-[ANAnnounceServiceListener listener:shouldAcceptNewConnection:]_block_invoke.98
- ___66-[ANTonePlayerServiceListener listener:shouldAcceptNewConnection:]_block_invoke.49
- ___71-[ANPlaybackSessionServiceListener listener:shouldAcceptNewConnection:]_block_invoke.89
- ___71-[ANPlaybackSessionServiceListener listener:shouldAcceptNewConnection:]_block_invoke.92
- ___96-[ANPlaybackSessionServiceListener coordinator:didReceiveAnnouncement:forGroupID:forEndpointID:]_block_invoke.100
CStrings:
+ "-[ANTrackPlayer audioSessionInterruptionHandler:]"
+ "Playback state is not interrupted. Will not resume playback after delaying for %f seconds"
+ "Setting Playback State to %lu"
+ "Still interrupted. Resuming playback after delaying for %f seconds"
+ "T@\"NSXPCInterface\",N,R"
+ "TB,N,V_someOtherSidekickSessionAudioIsPlaying"
+ "_someOtherSidekickSessionAudioIsPlaying"
+ "accessoryDidUpdateSupportsCompanionInitiatedObliterate:"
+ "an_announceServiceInterface"
+ "an_localPlaybackSessionServiceDelegateInterface"
+ "an_localPlaybackSessionServiceInterface"
+ "an_remotePlaybackSessionServiceDelegateInterface"
+ "an_remotePlaybackSessionServiceInterface"
+ "an_tonePlayerServiceInterface"
+ "setSomeOtherSidekickSessionAudioIsPlaying:"
+ "someOtherSidekickSessionAudioIsPlaying"
- "-[ANTrackPlayer audioSessionInterruptionHandler:]_block_invoke"

```
