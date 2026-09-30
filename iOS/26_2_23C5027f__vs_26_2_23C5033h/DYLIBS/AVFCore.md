## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

```diff

-2395.3.2.0.0
-  __TEXT.__text: 0x1b20cc
-  __TEXT.__auth_stubs: 0x3c70
+2395.4.1.0.0
+  __TEXT.__text: 0x1b20c4
+  __TEXT.__auth_stubs: 0x3c80
   __TEXT.__objc_methlist: 0x1b044
-  __TEXT.__cstring: 0x242c6
+  __TEXT.__cstring: 0x242e6
   __TEXT.__const: 0x1e48
   __TEXT.__gcc_except_tab: 0x6998
   __TEXT.__oslogstring: 0x3fad

   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0xce8
   __DATA_CONST.__objc_arraydata: 0x308
-  __AUTH_CONST.__auth_got: 0x1e48
+  __AUTH_CONST.__auth_got: 0x1e50
   __AUTH_CONST.__const: 0x1118
   __AUTH_CONST.__cfstring: 0x19140
   __AUTH_CONST.__objc_const: 0x30830

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3E81AA9A-EA87-31CB-A8B3-04CF6D0526CB
+  UUID: 89153475-149C-3DB4-8745-C05FAC010388
   Functions: 11387
-  Symbols:   38949
+  Symbols:   38950
   CStrings:  16810
 
Symbols:
+ _CMAudioFormatDescriptionGetRichestDecodableFormatAndChannelLayout
Functions:
~ -[AVAssetReaderTrackOutput description] : 112 -> 136
~ _AVCopyBestAudioChannelLayoutFromFormatDescription : 212 -> 240
~ +[AVMetadataItem identifierForKey:keySpace:] : 100 -> 96
~ +[AVMetadataItem keyForIdentifier:] : 92 -> 80
~ +[AVMetadataItem keySpaceForIdentifier:] : 92 -> 80
~ -[AVPlayer _addVideoLayer:] : 176 -> 164
~ -[AVPlayer _removeVideoLayer:] : 184 -> 172
~ _AVExportSettingsAverageBitRateForSourceAndExportPresetWithEncoderSpecification : 176 -> 172
~ -[AVSampleBufferAudioRenderer _uninstallNotificationHandlers] : 232 -> 244
~ -[AVSampleBufferAudioRenderer copyFigSampleBufferAudioRenderer:] : 60 -> 56
~ -[AVPlayerPlaybackCoordinator _connectToCoordinationMedium:] : 172 -> 168
~ -[AVPlayerItemIntegratedTimeline(AVPlayerItemIntegratedTimelineObserver) _ensureObserversAreScheduledForItem:] : 124 -> 120
~ +[AVContentKeyRequest _prepareCryptor:forRenewal:andReturnKeyRequestID:isInchargeOfKeyRequest:error:] : 256 -> 252
CStrings:
+ "<%@: %p, track = %@, formatDescriptions = %@, outputSettings = %@>"
- "<%@: %p, track = %@, outputSettings = %@>"

```
