## SiriObservation

> `/System/Library/PrivateFrameworks/SiriObservation.framework/Versions/A/SiriObservation`

```diff

-3403.5.1.0.0
-  __TEXT.__text: 0x11ad4
+3404.80.4.0.0
+  __TEXT.__text: 0x11a68
   __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0xf54
+  __TEXT.__objc_methlist: 0x1310
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x188
   __TEXT.__oslogstring: 0x5d6

   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x800
+  __DATA_CONST.__objc_selrefs: 0x8e0
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0xc0
   __AUTH_CONST.__auth_got: 0x1e0
   __AUTH_CONST.__const: 0x7f0
   __AUTH_CONST.__cfstring: 0xa20
-  __AUTH_CONST.__objc_const: 0x26a8
+  __AUTH_CONST.__objc_const: 0x1fd0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0x500

   - /System/Library/PrivateFrameworks/MediaRemote.framework/Versions/A/MediaRemote
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2A4F0981-F781-3701-A97D-1B9EA7B8A151
+  UUID: 740FA1F3-E787-3461-85EF-068C64984D1D
   Functions: 475
   Symbols:   1146
   CStrings:  812
Functions:
~ -[SOClockAlarmObserver _setUp] : 1300 -> 1268
~ ___38-[SOClockAlarmObserver alarmsChanged:]_block_invoke : 452 -> 448
~ -[SOMediaNowPlayingObserver _fetchLastPlayingDateWithCompletion:] : 764 -> 760
~ ___65-[SOMediaNowPlayingObserver _fetchLastPlayingDateWithCompletion:]_block_invoke : 324 -> 320
~ ___65-[SOMediaNowPlayingObserver _fetchLastPlayingDateWithCompletion:]_block_invoke_2 : 152 -> 140
~ -[SOMediaNowPlayingObserver _fetchNowPlayingAppPlaybackStateForReason:completion:] : 504 -> 500
~ -[SOMediaNowPlayingObserver _updateProxyGroupPlayerState] : 324 -> 320
~ -[SOMediaNowPlayingObserver _stopObservingNowPlayingAppPlaybackState] : 404 -> 408
~ -[SOClockTimerObserver _setUp] : 1300 -> 1268
~ ___38-[SOClockTimerObserver timersChanged:]_block_invoke : 452 -> 448
~ -[SOAlarm hash] : 308 -> 304
~ -[SOAlarm _descriptionWithIndent:] : 304 -> 300
~ -[SOTimer hash] : 364 -> 360

```
