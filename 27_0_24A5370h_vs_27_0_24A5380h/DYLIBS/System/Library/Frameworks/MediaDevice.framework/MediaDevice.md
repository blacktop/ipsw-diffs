## MediaDevice

> `/System/Library/Frameworks/MediaDevice.framework/MediaDevice`

```diff

-  __TEXT.__text: 0x2e824
-  __TEXT.__objc_methlist: 0x42c
-  __TEXT.__const: 0xea8
-  __TEXT.__cstring: 0xcaf
-  __TEXT.__swift5_typeref: 0x686
-  __TEXT.__swift5_fieldmd: 0x34c
-  __TEXT.__constg_swiftt: 0x6e4
-  __TEXT.__swift5_reflstr: 0x379
+  __TEXT.__text: 0x314d4
+  __TEXT.__objc_methlist: 0x454
+  __TEXT.__const: 0x1098
+  __TEXT.__cstring: 0xd2f
+  __TEXT.__swift5_typeref: 0x6e2
+  __TEXT.__swift5_fieldmd: 0x368
+  __TEXT.__constg_swiftt: 0x734
+  __TEXT.__swift5_reflstr: 0x399
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift5_types: 0x30
-  __TEXT.__swift5_assocty: 0x90
-  __TEXT.__swift5_proto: 0x68
-  __TEXT.__oslogstring: 0xeeb
-  __TEXT.__swift5_capture: 0xadc
-  __TEXT.__swift_as_entry: 0x60
+  __TEXT.__swift5_proto: 0x80
+  __TEXT.__swift5_types: 0x34
+  __TEXT.__oslogstring: 0xf7b
+  __TEXT.__swift5_capture: 0xbbc
+  __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__swift_as_cont: 0x5c
-  __TEXT.__unwind_info: 0x7b0
-  __TEXT.__eh_frame: 0xe60
+  __TEXT.__swift_as_cont: 0x64
+  __TEXT.__unwind_info: 0x840
+  __TEXT.__eh_frame: 0xf80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x408
+  __DATA_CONST.__objc_selrefs: 0x460
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__got: 0x250
-  __AUTH_CONST.__const: 0x13a0
-  __AUTH_CONST.__cfstring: 0x3a0
+  __DATA_CONST.__got: 0x270
+  __AUTH_CONST.__const: 0x14b8
+  __AUTH_CONST.__cfstring: 0x480
   __AUTH_CONST.__objc_const: 0xa48
-  __AUTH_CONST.__auth_got: 0x850
+  __AUTH_CONST.__auth_got: 0x898
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x1e8
-  __DATA.__data: 0x538
-  __DATA.__bss: 0xc90
+  __DATA.__data: 0x578
+  __DATA.__bss: 0xf90
   - /System/Library/Frameworks/AVKit.framework/AVKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 763
-  Symbols:   734
-  CStrings:  200
+  Functions: 807
+  Symbols:   775
+  CStrings:  219
 
Sections:
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift_as_ret : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
Symbols:
+ -[MDESerializationHelper dictionaryFromMediaSelectionOptionSourceWithDisplayName:identifier:extendedLanguageTag:mediaCharacteristics:]
+ -[MDESerializationHelper dictionaryFromMetadataWithHasVideo:presentationSize:hasAudio:hasLegible:title:subtitle:artworks:]
+ -[MDESerializationHelper dictionaryFromPlaybackPositionWithPosition:hostTime:rate:]
+ -[MDESerializationHelper dictionaryFromSeekRequestWithPosition:tolerance:]
+ -[MDESerializationHelper dictionaryFromTimelineSegmentWithTimeRange:segmentType:marked:requiresLinearPlayback:identifier:]
+ -[MDESerializationHelper playbackPositionFromDictionary:]
+ _OBJC_CLASS_$_AVPlaybackUserInterfaceContentArtwork
+ _OBJC_CLASS_$_AVPlaybackUserInterfaceContentMetadata
+ _OBJC_CLASS_$_AVPlaybackUserInterfaceContentURLArtwork
+ _OBJC_CLASS_$_AVPlaybackUserInterfaceContentVideoProperties
+ _OBJC_CLASS_$_AVPlaybackUserInterfaceMediaSelectionOption
+ _OBJC_CLASS_$_AVPlaybackUserInterfacePlaybackPosition
+ _OBJC_CLASS_$_AVPlaybackUserInterfaceTimelineSegment
+ ___NSArray0__struct
+ _associated conformance So21AVMediaCharacteristicaSHSCSQ
+ _associated conformance So21AVMediaCharacteristicas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So21AVMediaCharacteristicas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _objc_msgSend$array
+ _objc_msgSend$artworkWithURL:contentType:size:
+ _objc_msgSend$dictionaryFromMediaSelectionOptionSourceWithDisplayName:identifier:extendedLanguageTag:mediaCharacteristics:
+ _objc_msgSend$dictionaryFromMetadataWithHasVideo:presentationSize:hasAudio:hasLegible:title:subtitle:artworks:
+ _objc_msgSend$dictionaryFromPlaybackPositionWithPosition:hostTime:rate:
+ _objc_msgSend$dictionaryFromTimelineSegmentWithTimeRange:segmentType:marked:requiresLinearPlayback:identifier:
+ _objc_msgSend$floatValue
+ _objc_msgSend$hostTime
+ _objc_msgSend$initWithDisplayName:identifier:extendedLanguageTag:mediaCharacteristics:
+ _objc_msgSend$initWithPosition:hostTime:rate:
+ _objc_msgSend$initWithPresentationSize:
+ _objc_msgSend$initWithTimeRange:segmentType:marked:requiresLinearPlayback:identifier:
+ _objc_msgSend$initWithVideoProperties:title:subtitle:artworkRepresentations:
+ _objc_msgSend$mediaCharacteristics
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$position
+ _objc_msgSend$rate
+ _objc_msgSend$segmentType
+ _objc_retain_x7
+ _swift_dynamicCastObjCClass
+ _swift_getForeignTypeMetadata
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic So8NSStringC
+ _symbolic _____ So21AVMediaCharacteristica
+ _symbolic _____Sg 5AVKit38AVPlaybackUserInterfaceContentMetadataV15VideoPropertiesV
+ _symbolic _____Sg_ABt 5AVKit38AVPlaybackUserInterfaceContentMetadataV15VideoPropertiesV
+ _symbolic ______XlSg 5AVKit35AVPlaybackUserInterfaceControllableP
+ _symbolic _____yxGSgXwz_x_qd_______Rz_____Rd__r__lXX 11MediaDevice32_SMCBridgeExtensionConfigurationC AA0abD0P 5AVKit35AVPlaybackUserInterfaceControllableP
+ _type_layout_string So21AVMediaCharacteristica
- -[MDESerializationHelper dictionaryFromMediaSelectionOptionSourceWithDisplayName:identifier:extendedLanguageTag:]
- -[MDESerializationHelper dictionaryFromMetadataWithAudioOnly:presentationSize:title:subtitle:albumArtworks:]
- -[MDESerializationHelper dictionaryFromTimelineSegmentWithTimeRange:auxiliaryContent:marked:requiresLinearPlayback:identifier:]
- _OBJC_CLASS_$_AVInterfaceAlbumArtwork
- _OBJC_CLASS_$_AVInterfaceMediaSelectionOptionSource
- _OBJC_CLASS_$_AVInterfaceMetadata
- _OBJC_CLASS_$_AVInterfaceTimelineSegment
- _objc_msgSend$arrayWithCapacity:
- _objc_msgSend$dictionaryFromMediaSelectionOptionSourceWithDisplayName:identifier:extendedLanguageTag:
- _objc_msgSend$dictionaryFromMetadataWithAudioOnly:presentationSize:title:subtitle:albumArtworks:
- _objc_msgSend$dictionaryFromTimelineSegmentWithTimeRange:auxiliaryContent:marked:requiresLinearPlayback:identifier:
- _objc_msgSend$initWithAudioOnly:presentationSize:title:subtitle:albumArtworkRepresentations:
- _objc_msgSend$initWithDisplayName:identifier:extendedLanguageTag:
- _objc_msgSend$initWithTimeRange:auxiliaryContent:marked:requiresLinearPlayback:identifier:
- _objc_msgSend$initWithURL:contentType:size:
- _objc_msgSend$isAuxiliaryContent
- _objc_retain_x25
- _objc_retain_x4
- _symbolic ______XlSg 5AVKit23AVInterfaceControllableP
- _symbolic _____yxGSgXwz_x_qd_______Rz_____Rd__r__lXX 11MediaDevice32_SMCBridgeExtensionConfigurationC AA0abD0P 5AVKit23AVInterfaceControllableP
CStrings:
+ "AVPlaybackUserInterfaceControllable state: %s"
+ "artworks"
+ "audioDescriptionOptions"
+ "audioDescriptionOptions changed, count: %ld"
+ "currentAudioDescriptionOption"
+ "currentAudioDescriptionOption changed to: %s"
+ "currentAudioDescriptionOption changed to: nil"
+ "error changed to: %s"
+ "hasAudio"
+ "hasLegible"
+ "hasVideo"
+ "hostTime"
+ "mediaCharacteristics"
+ "playbackPosition"
+ "playbackPosition did change to: %f @ rate %f"
+ "position"
+ "rate"
+ "segmentType"
+ "tolerance"
- "AVInterfaceControllable state: %s"
- "albumArtworks"
- "audioOnly"
- "auxiliaryContent"
- "currentPlaybackPosition"
- "currentPlaybackPosition did change to: %f"
- "playbackError changed to: %s"

```
