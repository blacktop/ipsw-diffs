## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`

```diff

-24200.24.35.401.0
-  __TEXT.__text: 0x30feb4
-  __TEXT.__auth_stubs: 0x4e30
-  __TEXT.__objc_methlist: 0x11e78
-  __TEXT.__cstring: 0x27cda
+24200.24.37.301.0
+  __TEXT.__text: 0x310ea4
+  __TEXT.__auth_stubs: 0x4e20
+  __TEXT.__objc_methlist: 0x11ea0
+  __TEXT.__cstring: 0x27d4c
   __TEXT.__const: 0x9e90
-  __TEXT.__constg_swiftt: 0x58d4
-  __TEXT.__swift5_typeref: 0x3dfd
+  __TEXT.__constg_swiftt: 0x58dc
+  __TEXT.__swift5_typeref: 0x3df5
   __TEXT.__swift5_reflstr: 0x3621
   __TEXT.__swift5_fieldmd: 0x36b8
   __TEXT.__swift5_builtin: 0x5f0

   __TEXT.__swift5_types: 0x3cc
   __TEXT.__swift5_mpenum: 0xc4
   __TEXT.__swift5_protos: 0xb8
-  __TEXT.__oslogstring: 0x2d874
-  __TEXT.__swift5_capture: 0x2bf4
-  __TEXT.__gcc_except_tab: 0x5d6c
+  __TEXT.__oslogstring: 0x2daf4
+  __TEXT.__swift5_capture: 0x2c10
+  __TEXT.__gcc_except_tab: 0x5d7c
   __TEXT.__ustring: 0x354
   __TEXT.__dlopen_cstrs: 0x114
-  __TEXT.__unwind_info: 0x9dc8
-  __TEXT.__eh_frame: 0x7008
+  __TEXT.__unwind_info: 0x9df0
+  __TEXT.__eh_frame: 0x701c
   __TEXT.__objc_classname: 0x39ea
-  __TEXT.__objc_methname: 0x35ee2
-  __TEXT.__objc_methtype: 0x8faa
-  __TEXT.__objc_stubs: 0x25000
-  __DATA_CONST.__got: 0x2c28
-  __DATA_CONST.__const: 0x8d38
+  __TEXT.__objc_methname: 0x35f64
+  __TEXT.__objc_methtype: 0x8fc5
+  __TEXT.__objc_stubs: 0x25060
+  __DATA_CONST.__got: 0x2c48
+  __DATA_CONST.__const: 0x8d40
   __DATA_CONST.__objc_classlist: 0xbe0
   __DATA_CONST.__objc_catlist: 0x268
   __DATA_CONST.__objc_protolist: 0x750
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb4c0
+  __DATA_CONST.__objc_selrefs: 0xb4d8
   __DATA_CONST.__objc_protorefs: 0x350
   __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x238
-  __AUTH_CONST.__auth_got: 0x2728
-  __AUTH_CONST.__auth_ptr: 0xa70
-  __AUTH_CONST.__const: 0xc4c8
-  __AUTH_CONST.__cfstring: 0x1ae40
-  __AUTH_CONST.__objc_const: 0x33a50
+  __AUTH_CONST.__auth_got: 0x2720
+  __AUTH_CONST.__auth_ptr: 0xaa8
+  __AUTH_CONST.__const: 0xc520
+  __AUTH_CONST.__cfstring: 0x1ae80
+  __AUTH_CONST.__objc_const: 0x33ae0
   __AUTH_CONST.__objc_intobj: 0x7f8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH.__objc_data: 0x4188
-  __AUTH.__data: 0x14c8
+  __AUTH.__objc_data: 0x40d8
+  __AUTH.__data: 0x13d0
   __DATA.__objc_ivar: 0x1898
-  __DATA.__data: 0x5be8
-  __DATA.__bss: 0xa798
+  __DATA.__data: 0x5b98
+  __DATA.__bss: 0xa498
   __DATA.__common: 0xa8
-  __DATA_DIRTY.__objc_data: 0x4c38
-  __DATA_DIRTY.__data: 0x4e98
-  __DATA_DIRTY.__bss: 0x2640
+  __DATA_DIRTY.__objc_data: 0x4ce8
+  __DATA_DIRTY.__data: 0x4fe8
+  __DATA_DIRTY.__bss: 0x2938
   __DATA_DIRTY.__common: 0xf0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 15718
-  Symbols:   11439
-  CStrings:  17023
+  Functions: 15739
+  Symbols:   11444
+  CStrings:  17040
 
Symbols:
+ _OBJC_CLASS_$_ICPrivacyInfo
+ _MPCPlaybackEngineEventItemMetadataKeyPodcastPageContext
CStrings:
+ "podcast-page-context"
+ "[MPRQ:MPC:%!p(MISSING)] __MPCPlaybackRequestEnvironmentFromProtoAccountInfo | using device active account [matching non-delegate account, non-sub, fallback allowed] account=%!{(MISSING)public}@"
+ "Podcasts: Unable to query `podcastPageContext`. No metadata found."
+ "Unable to load fallback intent. %!@(MISSING)"
+ "SPIR: %!p(MISSING): Declining to use StorePlatform due to required privacy acknowledgement."
+ "End of queue reached. Loaded %!l(MISSING)d new item(s) into the player."
+ "iosControlCenter"
+ "com.apple.springboard"
+ "No tracklist token set on MPC intent"
+ "T@\"MPCPlaybackIntent\",R,C,N"
+ "sharedPrivacyInfo"
+ "Error getting podcast intent from MPCPlaybackIntent"
+ "podcastPageContext"
+ "Unexpected autoPlayEndPosition.entryType: %!d(MISSING)"
+ "privacyAcknowledgementRequiredForMusic"
+ "_MPCOverrideAllowsInsertionPositionLast"
+ "Error getting intent from %!s(MISSING) - %!@(MISSING)"
+ "Cannot insert at Last [MediaPlayer/QueueFA is ON]"
+ "@\"MPCPlaybackIntent\"16@0:8"
+ "Podcasts: Not reporting `podcastPageContext`. No related `itemBegin` event found."
+ "T@\"MPCPlaybackIntent\",R,N"
- "Cannot insert at Last [MediaPlayer/QueueFA is ON"
- "Did reach end of queue: %!s(MISSING)"
- "Error getting intent"
- "MPCPublisherCreateStationCommand"
- "BehaviorPodcasts-didReachEndOfQueue-populateUpNext"

```
