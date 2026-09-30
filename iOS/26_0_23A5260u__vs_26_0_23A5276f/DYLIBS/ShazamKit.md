## ShazamKit

> `/System/Library/Frameworks/ShazamKit.framework/ShazamKit`

```diff

-423.0.29.0.0
-  __TEXT.__text: 0x80120
-  __TEXT.__auth_stubs: 0x19b0
-  __TEXT.__objc_methlist: 0x4758
-  __TEXT.__const: 0x2118a
-  __TEXT.__gcc_except_tab: 0x3898
-  __TEXT.__cstring: 0x38f2
-  __TEXT.__oslogstring: 0xff6
-  __TEXT.__constg_swiftt: 0x4c0
-  __TEXT.__swift5_typeref: 0xa0e
-  __TEXT.__swift5_reflstr: 0x34c
-  __TEXT.__swift5_fieldmd: 0x408
+423.0.33.0.0
+  __TEXT.__text: 0x82c60
+  __TEXT.__auth_stubs: 0x1b80
+  __TEXT.__objc_methlist: 0x4848
+  __TEXT.__const: 0x213fa
+  __TEXT.__gcc_except_tab: 0x38ac
+  __TEXT.__cstring: 0x3b62
+  __TEXT.__oslogstring: 0x1016
+  __TEXT.__constg_swiftt: 0x51c
+  __TEXT.__swift5_typeref: 0xa8e
+  __TEXT.__swift5_reflstr: 0x39c
+  __TEXT.__swift5_fieldmd: 0x504
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_assocty: 0x230
   __TEXT.__swift5_capture: 0x214
-  __TEXT.__swift5_proto: 0xb8
-  __TEXT.__swift5_types: 0x68
+  __TEXT.__swift5_proto: 0xdc
+  __TEXT.__swift5_types: 0x74
   __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2ce8
-  __TEXT.__eh_frame: 0x1068
-  __TEXT.__objc_classname: 0xab8
-  __TEXT.__objc_methname: 0x976a
-  __TEXT.__objc_methtype: 0x1cf5
-  __TEXT.__objc_stubs: 0x71a0
-  __DATA_CONST.__got: 0x660
-  __DATA_CONST.__const: 0x8e0
-  __DATA_CONST.__objc_classlist: 0x318
+  __TEXT.__unwind_info: 0x2de0
+  __TEXT.__eh_frame: 0x1228
+  __TEXT.__objc_classname: 0xad8
+  __TEXT.__objc_methname: 0x99e0
+  __TEXT.__objc_methtype: 0x1d2b
+  __TEXT.__objc_stubs: 0x72a0
+  __DATA_CONST.__got: 0x698
+  __DATA_CONST.__const: 0x8f0
+  __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21e8
+  __DATA_CONST.__objc_selrefs: 0x2240
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x208
-  __AUTH_CONST.__auth_got: 0xcf0
-  __AUTH_CONST.__const: 0x17e8
-  __AUTH_CONST.__cfstring: 0x2400
-  __AUTH_CONST.__objc_const: 0x8c70
+  __DATA_CONST.__objc_superrefs: 0x210
+  __AUTH_CONST.__auth_got: 0xdd8
+  __AUTH_CONST.__const: 0x1938
+  __AUTH_CONST.__cfstring: 0x2520
+  __AUTH_CONST.__objc_const: 0x8e20
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x938
+  __AUTH.__objc_data: 0x988
   __AUTH.__data: 0x6f8
-  __DATA.__objc_ivar: 0x43c
-  __DATA.__data: 0x1b20e0
+  __DATA.__objc_ivar: 0x448
+  __DATA.__data: 0x1b2140
   __DATA.__common: 0x1c8
-  __DATA.__bss: 0x18f0
+  __DATA.__bss: 0x1d70
   __DATA_DIRTY.__objc_data: 0x1680
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x70

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
+  - /System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal
   - /System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 41C8FF97-299D-3244-8AE4-841A458A9504
-  Functions: 3020
-  Symbols:   8317
-  CStrings:  2837
+  UUID: EC2D21FA-17C7-39C7-9E00-3C46068F22DB
+  Functions: 3092
+  Symbols:   8408
+  CStrings:  2877
 
Symbols:
+ +[SHArtwork supportsSecureCoding]
+ +[SHArtwork urlWithURLTemplate:width:height:]
+ +[SHArtwork validateDictionary:error:]
+ +[SHAttribution findContainingAppBundleIdentifierForIdentifier:]
+ +[SHHapticSpatialTrackInformation supportsSecureCoding]
+ +[SHMediaItemDaemonConnection fetchRawSongResponseDataUsingMediaItemIdentifier:]
+ -[SHArtwork URLWithWidth:height:]
+ -[SHArtwork copyWithZone:]
+ -[SHArtwork encodeWithCoder:]
+ -[SHArtwork initWithCoder:]
+ -[SHArtwork initWithDictionary:error:]
+ -[SHArtwork maximumHeight]
+ -[SHArtwork maximumWidth]
+ -[SHArtwork newPrimaryTextColor]
+ -[SHArtwork newQuarternaryTextColor]
+ -[SHArtwork newSecondaryTextColor]
+ -[SHArtwork newTertiaryTextColor]
+ -[SHHaptic associatedSpatialTrackInformation]
+ -[SHHaptic initWithHapticTracks:representingMediaItem:spatialTrackInformation:error:]
+ -[SHHapticSpatialTrackInformation .cxx_destruct]
+ -[SHHapticSpatialTrackInformation description]
+ -[SHHapticSpatialTrackInformation encodeWithCoder:]
+ -[SHHapticSpatialTrackInformation initWithCoder:]
+ -[SHHapticSpatialTrackInformation initWithSpatialStartOffset:offsets:timeDrift:matchesStereo:]
+ -[SHHapticSpatialTrackInformation matchesStereo]
+ -[SHHapticSpatialTrackInformation offsets]
+ -[SHHapticSpatialTrackInformation startOffset]
+ -[SHHapticSpatialTrackInformation timeDrift]
+ -[SHMediaItem fetchRawSongResponseData]
+ -[SHShazamKitServiceConnection synchronouslyFetchRawSongResponseDataForMediaItemIdentifier:completionHandler:]
+ _NSURLErrorDomain
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_SHHapticSpatialTrackInformation
+ _OBJC_IVAR_$_SHHaptic._associatedSpatialTrackInformation
+ _OBJC_IVAR_$_SHHapticSpatialTrackInformation._matchesStereo
+ _OBJC_IVAR_$_SHHapticSpatialTrackInformation._offsets
+ _OBJC_IVAR_$_SHHapticSpatialTrackInformation._startOffset
+ _OBJC_IVAR_$_SHHapticSpatialTrackInformation._timeDrift
+ _OBJC_METACLASS_$_SHHapticSpatialTrackInformation
+ __OBJC_$_CLASS_METHODS_SHHapticSpatialTrackInformation
+ __OBJC_$_CLASS_PROP_LIST_SHArtwork
+ __OBJC_$_CLASS_PROP_LIST_SHHapticSpatialTrackInformation
+ __OBJC_$_INSTANCE_METHODS_SHHapticSpatialTrackInformation
+ __OBJC_$_INSTANCE_VARIABLES_SHHapticSpatialTrackInformation
+ __OBJC_$_PROP_LIST_SHHapticSpatialTrackInformation
+ __OBJC_CLASS_PROTOCOLS_$_SHArtwork
+ __OBJC_CLASS_PROTOCOLS_$_SHHapticSpatialTrackInformation
+ __OBJC_CLASS_RO_$_SHHapticSpatialTrackInformation
+ __OBJC_METACLASS_RO_$_SHHapticSpatialTrackInformation
+ ___110-[SHShazamKitServiceConnection synchronouslyFetchRawSongResponseDataForMediaItemIdentifier:completionHandler:]_block_invoke
+ ___80+[SHMediaItemDaemonConnection fetchRawSongResponseDataUsingMediaItemIdentifier:]_block_invoke
+ ___block_descriptor_40_e8_32r_e16_v16?0"NSData"8lr32l8
+ ___block_literal_global.110
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_memcpy128_8
+ ___swift_mutable_project_boxed_opaque_existential_1
+ ___swift_project_boxed_opaque_existential_1
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_ShazamKit
+ _associated conformance 9ShazamKit29MediaAPIArtworkRepresentation33_E02952E2DBCAE1324FA494CAA294A306LLV10CodingKeysOSHAASQ
+ _associated conformance 9ShazamKit29MediaAPIArtworkRepresentation33_E02952E2DBCAE1324FA494CAA294A306LLV10CodingKeysOs0L3KeyAAs23CustomStringConvertible
+ _associated conformance 9ShazamKit29MediaAPIArtworkRepresentation33_E02952E2DBCAE1324FA494CAA294A306LLV10CodingKeysOs0L3KeyAAs28CustomDebugStringConvertible
+ _objc_msgSend$URLWithWidth:height:
+ _objc_msgSend$associatedSpatialTrackInformation
+ _objc_msgSend$fetchRawSongResponseDataUsingMediaItemIdentifier:
+ _objc_msgSend$findContainingAppBundleIdentifierForIdentifier:
+ _objc_msgSend$initWithHapticTracks:representingMediaItem:spatialTrackInformation:error:
+ _objc_msgSend$initWithSpatialStartOffset:offsets:timeDrift:matchesStereo:
+ _objc_msgSend$matchesStereo
+ _objc_msgSend$maximumHeight
+ _objc_msgSend$maximumWidth
+ _objc_msgSend$offsets
+ _objc_msgSend$startOffset
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$synchronouslyFetchRawSongResponseDataForMediaItemIdentifier:completionHandler:
+ _objc_msgSend$timeDrift
+ _objc_msgSend$urlWithURLTemplate:width:height:
+ _objc_msgSend$validateDictionary:error:
+ _swift_allocError
+ _swift_makeBoxUnique
+ _symbolic SDySSypG
+ _symbolic SSSg
+ _symbolic SiSg
+ _symbolic So9SHArtworkC
+ _symbolic _____ 9ShazamKit29MediaAPIArtworkRepresentation33_E02952E2DBCAE1324FA494CAA294A306LLV
+ _symbolic _____ 9ShazamKit29MediaAPIArtworkRepresentation33_E02952E2DBCAE1324FA494CAA294A306LLV10CodingKeysO
+ _symbolic _____ 9ShazamKit9SHArtworkV
+ _symbolic _____Sg 8MusicKit7ArtworkV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9ShazamKit29MediaAPIArtworkRepresentation33_E02952E2DBCAE1324FA494CAA294A306LLV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9ShazamKit29MediaAPIArtworkRepresentation33_E02952E2DBCAE1324FA494CAA294A306LLV10CodingKeysO
+ _symbolic ypXmT______t s13DecodingErrorO7ContextV
+ _type_layout_string 9ShazamKit29MediaAPIArtworkRepresentation33_E02952E2DBCAE1324FA494CAA294A306LLV
+ _type_layout_string 9ShazamKit9SHArtworkV
- +[SHArtwork urlWithURLTemplate:size:]
- -[SHArtwork URLWithSize:]
- -[SHArtwork artworkSize]
- -[SHArtwork height]
- -[SHArtwork initWithDictionary:]
- -[SHArtwork newTextColor1]
- -[SHArtwork newTextColor2]
- -[SHArtwork newTextColor3]
- -[SHArtwork newTextColor4]
- -[SHArtwork width]
- -[SHAttribution findContainingAppBundleIdentifier]
- -[SHHaptic initWithHapticTracks:representingMediaItem:spatialOffsets:error:]
- _OBJC_IVAR_$_SHHaptic._spatialOffsets
- _OBJC_IVAR_$_SHMediaItem._artwork
- ___block_literal_global.108
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_ShazamKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_ShazamKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_ShazamKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_ShazamKit
- _objc_msgSend$URLWithSize:
- _objc_msgSend$findContainingAppBundleIdentifier
- _objc_msgSend$height
- _objc_msgSend$initWithDictionary:
- _objc_msgSend$initWithHapticTracks:representingMediaItem:spatialOffsets:error:
- _objc_msgSend$spatialOffsets
- _objc_msgSend$urlWithURLTemplate:size:
- _objc_msgSend$width
CStrings:
+ "%ld"
+ "@\"SHHapticSpatialTrackInformation\""
+ "@40@0:8@16q24q32"
+ "@44@0:8d16@24d32B40"
+ "Artwork cannot be constructed without a URL"
+ "Error fetching raw response data: %@"
+ "Failed to decode MusicKit.Artwork from SHArtwork"
+ "Failed to serialize (MediaAPIArtworkRepresentation in _E02952E2DBCAE1324FA494CAA294A306)"
+ "JSONObjectWithData:options:error:"
+ "Passing <= 0 maximum size is unsupported, instead do not pass maximum value"
+ "SHHapticSpatialTrackInformation"
+ "SHHapticSpatialTrackInformationCodingKey"
+ "SHHapticSpatialTrackInformationMatchesStereoCodingKey"
+ "SHHapticSpatialTrackInformationOffsetsCodingKey"
+ "SHHapticSpatialTrackInformationSpatialStartOffsetCodingKey"
+ "SHHapticSpatialTrackInformationTimeDriftCodingKey"
+ "StartOffset: %f, TimeDrift: %f, Matches Stereo: %d"
+ "T@\"NSArray\",R,N,V_offsets"
+ "T@\"SHArtwork\",R,N"
+ "T@\"SHHapticSpatialTrackInformation\",R,N,V_associatedSpatialTrackInformation"
+ "TB,R,N,V_matchesStereo"
+ "Td,R,N,V_startOffset"
+ "Td,R,N,V_timeDrift"
+ "URLWithWidth:height:"
+ "_associatedSpatialTrackInformation"
+ "_matchesStereo"
+ "_offsets"
+ "_startOffset"
+ "_timeDrift"
+ "associatedSpatialTrackInformation"
+ "dataWithJSONObject:options:error:"
+ "fetchRawSongResponseData"
+ "fetchRawSongResponseDataUsingMediaItemIdentifier:"
+ "findContainingAppBundleIdentifierForIdentifier:"
+ "initWithHapticTracks:representingMediaItem:spatialTrackInformation:error:"
+ "initWithSpatialStartOffset:offsets:timeDrift:matchesStereo:"
+ "matchesStereo"
+ "maximumHeight"
+ "maximumWidth"
+ "newPrimaryTextColor"
+ "newQuarternaryTextColor"
+ "newSecondaryTextColor"
+ "newTertiaryTextColor"
+ "offsets"
+ "startOffset"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "synchronouslyFetchRawSongResponseDataForMediaItemIdentifier:completionHandler:"
+ "timeDrift"
+ "urlWithURLTemplate:width:height:"
+ "v16@?0@\"NSData\"8"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSData\">24"
+ "validateDictionary:error:"
- "%.f"
- "@\"SHArtwork\""
- "@40@0:8@16{CGSize=dd}24"
- "T@\"NSArray\",R,N,V_spatialOffsets"
- "T@\"NSString\",R,N"
- "T@\"SHArtwork\",R,N,V_artwork"
- "T{CGSize=dd},R,N"
- "URLWithSize:"
- "_artwork"
- "_spatialOffsets"
- "artworkSize"
- "findContainingAppBundleIdentifier"
- "initWithDictionary:"
- "initWithHapticTracks:representingMediaItem:spatialOffsets:error:"
- "newTextColor1"
- "newTextColor2"
- "newTextColor3"
- "newTextColor4"
- "urlWithURLTemplate:size:"
- "{CGSize=dd}16@0:8"

```
