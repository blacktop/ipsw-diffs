## shazamd

> `/System/Library/Frameworks/ShazamKit.framework/shazamd`

```diff

-423.0.29.0.0
-  __TEXT.__text: 0x4820c
+423.0.33.0.0
+  __TEXT.__text: 0x489d0
   __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_stubs: 0xbc40
-  __TEXT.__objc_methlist: 0x591c
-  __TEXT.__const: 0x1b0
+  __TEXT.__objc_stubs: 0xbde0
+  __TEXT.__objc_methlist: 0x595c
+  __TEXT.__const: 0x1b8
   __TEXT.__gcc_except_tab: 0xcf8
-  __TEXT.__objc_methname: 0xf3b6
-  __TEXT.__cstring: 0x276c
-  __TEXT.__oslogstring: 0x3c91
-  __TEXT.__objc_classname: 0x1319
-  __TEXT.__objc_methtype: 0x2cf8
+  __TEXT.__objc_methname: 0xf5ad
+  __TEXT.__cstring: 0x27c1
+  __TEXT.__oslogstring: 0x3e01
+  __TEXT.__objc_classname: 0x132f
+  __TEXT.__objc_methtype: 0x2d4d
   __TEXT.__swift5_typeref: 0x7c
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_reflstr: 0x10
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
   __TEXT.__ustring: 0x164
-  __TEXT.__unwind_info: 0x1330
+  __TEXT.__unwind_info: 0x1340
   __DATA_CONST.__auth_got: 0x4a0
-  __DATA_CONST.__got: 0x7f0
+  __DATA_CONST.__got: 0x7f8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1760
-  __DATA_CONST.__cfstring: 0x2280
-  __DATA_CONST.__objc_classlist: 0x488
+  __DATA_CONST.__const: 0x1748
+  __DATA_CONST.__cfstring: 0x2360
+  __DATA_CONST.__objc_classlist: 0x490
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA.__objc_const: 0xc250
-  __DATA.__objc_selrefs: 0x3560
+  __DATA.__objc_const: 0xc2e8
+  __DATA.__objc_selrefs: 0x35c8
   __DATA.__objc_ivar: 0x578
-  __DATA.__objc_data: 0x2dc0
+  __DATA.__objc_data: 0x2e10
   __DATA.__data: 0x1640
   __DATA.__bss: 0x100
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AEFD39CC-C69E-3C2D-A278-85BC9BAC247E
-  Functions: 1706
-  Symbols:   438
-  CStrings:  3851
+  UUID: 6EF75907-BB48-3BA8-8553-1E91834E87E0
+  Functions: 1711
+  Symbols:   435
+  CStrings:  3887
 
Symbols:
+ _OBJC_CLASS_$_SHHapticSpatialTrackInformation
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "@\"SHHapticSpatialTrackInformation\""
+ "Attempting to download archive for appleMusicID:%@ with filename %@. Has spatial track info: %@"
+ "Fetching raw song response from data store for mediaItem ID: %@"
+ "Haptic spatial track information isn't available."
+ "NO"
+ "No data store to retrieve raw song response."
+ "No spatial track information in server response."
+ "Parsing spatial track information"
+ "Returning haptic track's spatial information: %@"
+ "SHHapticSpatialTrackValidator"
+ "SHHapticsSpatialTrackParser"
+ "Spatial track info is valid? %@, Matches stereo: %d, time drift %f"
+ "T@\"SHHapticSpatialTrackInformation\",R,N,V_spatialTrackInformation"
+ "Validating spatial information of Adam ID %@, ISRC: %@"
+ "YES"
+ "[Remote] Media Library continued syncing for next batch. Sync ID: %@. "
+ "_spatialTrackInformation"
+ "allKeys"
+ "attributesByName"
+ "beginLibrarySyncWithStartCondition:"
+ "fetchObjectsForRequest:withPredicate:context:"
+ "fetchRawSongResponseDataForLibraryTrackIdentifier:"
+ "initWithHapticTracks:representingMediaItem:spatialTrackInformation:error:"
+ "initWithRequestMediaItem:spatialTrackInformation:networkDownloadResponse:"
+ "initWithSpatialStartOffset:offsets:timeDrift:matchesStereo:"
+ "isCloseMatch"
+ "isValidSpatialTrackInformation:"
+ "libraryWillBeginSync:withStartCondition:"
+ "matchesStereo"
+ "rawSongResponseDataForMediaItemIdentifier:"
+ "setFetchLimit:"
+ "setPropertiesToFetch:"
+ "setResultType:"
+ "spatialAttributes"
+ "spatialTrackInformation"
+ "spatialTrackInformationFromAttributes:"
+ "startOffsetInMilliseconds"
+ "syncID == %@"
+ "synchronouslyFetchRawSongResponseDataForMediaItemIdentifier:completionHandler:"
+ "timeDrift"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSData\">24"
+ "v32@0:8@\"SHLShazamLibrary\"16@\"NSString\"24"
- "Attempting to download archive with filename %@. Spatial offsets count %ld"
- "No offset in response, returning empty spatial offsets"
- "Parsing spatial offsets from response %@"
- "Returning spatial offsets with count %ld"
- "SHServerHapticsSpatialOffsetsParser"
- "T@\"NSArray\",R,N,V_spatialOffsets"
- "_spatialOffsets"
- "beginLibrarySync"
- "fetchManagedObjectForRequest:withPredicate:context:"
- "initWithHapticTracks:representingMediaItem:spatialOffsets:error:"
- "initWithRequestMediaItem:spatialOffsets:networkDownloadResponse:"
- "libraryWillBeginSync:"
- "offsetsFromResponse:"
- "v24@0:8@\"SHLShazamLibrary\"16"

```
