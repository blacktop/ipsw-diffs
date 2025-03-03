## MediaPlayer

> `/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer`

```diff

-4024.500.24.0.0
-  __TEXT.__text: 0x339a60
-  __TEXT.__auth_stubs: 0x5040
-  __TEXT.__objc_methlist: 0x26f28
+4024.500.33.0.0
+  __TEXT.__text: 0x33c9a8
+  __TEXT.__auth_stubs: 0x5050
+  __TEXT.__objc_methlist: 0x26fe8
   __TEXT.__dlopen_cstrs: 0x4bd
   __TEXT.__const: 0x16c08
-  __TEXT.__cstring: 0x2d4cb
+  __TEXT.__cstring: 0x2d6d1
   __TEXT.__constg_swiftt: 0x80
   __TEXT.__swift5_typeref: 0x42
   __TEXT.__swift5_reflstr: 0xc
   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x8
-  __TEXT.__gcc_except_tab: 0x18df4
-  __TEXT.__oslogstring: 0x141cb
+  __TEXT.__gcc_except_tab: 0x18f48
+  __TEXT.__oslogstring: 0x1446d
   __TEXT.__ustring: 0x1ca
-  __TEXT.__unwind_info: 0xbf20
+  __TEXT.__unwind_info: 0xbfa0
   __TEXT.__eh_frame: 0x1538
   __TEXT.__objc_classname: 0x6061
-  __TEXT.__objc_methname: 0x5f84a
+  __TEXT.__objc_methname: 0x5f994
   __TEXT.__objc_methtype: 0xdabd
-  __TEXT.__objc_stubs: 0x314e0
-  __DATA_CONST.__got: 0x2e60
-  __DATA_CONST.__const: 0xd028
+  __TEXT.__objc_stubs: 0x31580
+  __DATA_CONST.__got: 0x2e70
+  __DATA_CONST.__const: 0xd058
   __DATA_CONST.__objc_classlist: 0x1478
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x3f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12a90
+  __DATA_CONST.__objc_selrefs: 0x12ae8
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0xd68
+  __DATA_CONST.__objc_superrefs: 0xd70
   __DATA_CONST.__objc_arraydata: 0x7e8
-  __AUTH_CONST.__auth_got: 0x2838
+  __AUTH_CONST.__auth_got: 0x2840
   __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__const: 0xe7e0
-  __AUTH_CONST.__cfstring: 0x24ce0
-  __AUTH_CONST.__objc_const: 0x433c8
+  __AUTH_CONST.__const: 0xe820
+  __AUTH_CONST.__cfstring: 0x24f60
+  __AUTH_CONST.__objc_const: 0x43438
   __AUTH_CONST.__objc_intobj: 0x858
   __AUTH_CONST.__objc_arrayobj: 0xe70
-  __AUTH_CONST.__objc_doubleobj: 0x70
+  __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xa2d0
   __AUTH.__data: 0xd8
-  __DATA.__objc_ivar: 0x2b74
+  __DATA.__objc_ivar: 0x2b78
   __DATA.__data: 0x33f0
   __DATA.__bss: 0xd00
   __DATA.__common: 0xa29

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 16151
-  Symbols:   20895
-  CStrings:  22873
+  Functions: 16205
+  Symbols:   20954
+  CStrings:  22915
 
Symbols:
+ _AVAudioSessionMediaServicesWereLostNotification
+ _AVAudioSessionMediaServicesWereResetNotification
+ _MPModelPropertyPodcastEpisodeSubtitle
+ _MPModelPropertyPodcastEpisodeSubtitleShort
+ _dispatch_suspend
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _MPChangeDetailOperationMaximumElementCount
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initializeBufferWithCopyOfBuffer
CStrings:
+ "\x0f\x02)"
+ "%{public}@ Executing legacy request query %{public}@"
+ "%{public}@ Executing request %{public}@ against library %{public}@"
+ "%{public}@ Executing request using view %{public}@"
+ "%{public}@ Failed to create or find media playlist"
+ "%{public}@ Finished"
+ "%{public}@ Finished error=%{public}@"
+ "%{public}@ Updating existing playlist with persistent ID=%lld, %lu tracks and properties: '%{public}@"
+ "<%@ %p: [filter: %@]>"
+ "<none>"
+ "MPModelPropertyPodcastEpisodeSubtitle"
+ "MPModelPropertyPodcastEpisodeSubtitleShort"
+ "Skipping sorting by allowed item identifiers because allowedItemIdentifiers for _entityTranslationContext does not contain either a persistentID or a possiblePersistentID."
+ "Skipping sorting by allowed item identifiers because allowedItemIdentifiers for _sectionTranslationContext does not contain either a persistentID or a possiblePersistentID."
+ "Translator was missing mapping for MPModelPropertyPodcastEpisodeSubtitle"
+ "Translator was missing mapping for MPModelPropertyPodcastEpisodeSubtitleShort"
+ "Wake server reason:%{public}@"
+ "__MPModelPropertyPodcastEpisodeSubtitleShort__MAPPING_MISSING__"
+ "__MPModelPropertyPodcastEpisodeSubtitle__MAPPING_MISSING__"
+ "__subtitleShort_KEY"
+ "__subtitle_KEY"
+ "_currentTrackList"
+ "_handleMediaServicesLost:"
+ "_handleMediaServicesReset:"
+ "_mediaServiceLost"
+ "_setPlaylistName:"
+ "_wakeServerIfConnectedForReason:"
+ "art[url]"
+ "clean-lyrics"
+ "com.apple.MediaPlayer.MPModelLibraryPlaylistEditController.accessQueue"
+ "favorited"
+ "favorited-collection"
+ "favorited-entity"
+ "ignore-restrictions"
+ "in-library"
+ "include-empty"
+ "local"
+ "loved"
+ "pinned-collections"
+ "pinned-containers"
+ "purchased"
+ "setSubtitleShort:"
+ "subtitleShort"
+ "unprotected"
- "\x01\x1f)"
- "%{public}@ Updating existing playlist with %lu tracks and properties: '%{public}@"

```
