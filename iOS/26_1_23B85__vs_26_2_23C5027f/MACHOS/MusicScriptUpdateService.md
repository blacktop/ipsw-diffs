## MusicScriptUpdateService

> `/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService`

```diff

-4025.210.3.0.0
-  __TEXT.__text: 0x4b31bc
-  __TEXT.__auth_stubs: 0x8f60
-  __TEXT.__objc_stubs: 0xe00
+4025.310.10.2.0
+  __TEXT.__text: 0x4adb64
+  __TEXT.__auth_stubs: 0x8fa0
+  __TEXT.__objc_stubs: 0xe40
   __TEXT.__objc_methlist: 0x498c
-  __TEXT.__const: 0x28028
-  __TEXT.__objc_methname: 0xe004
-  __TEXT.__cstring: 0x147f4
-  __TEXT.__swift5_typeref: 0x19d10
+  __TEXT.__const: 0x27ea8
+  __TEXT.__objc_methname: 0xe029
+  __TEXT.__cstring: 0x14934
+  __TEXT.__swift5_typeref: 0x19c8e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x11404
-  __TEXT.__swift5_reflstr: 0xc3d1
-  __TEXT.__swift5_fieldmd: 0xde3c
-  __TEXT.__oslogstring: 0x9607
-  __TEXT.__swift5_proto: 0x1718
+  __TEXT.__constg_swiftt: 0x1139c
+  __TEXT.__swift5_reflstr: 0xc524
+  __TEXT.__swift5_fieldmd: 0xde38
+  __TEXT.__oslogstring: 0x8b4a
+  __TEXT.__swift5_proto: 0x1724
   __TEXT.__swift5_types: 0xf90
-  __TEXT.__objc_classname: 0x59e
+  __TEXT.__objc_classname: 0x5b6
   __TEXT.__objc_methtype: 0x3afd
-  __TEXT.__swift5_capture: 0x7c0c
-  __TEXT.__swift5_builtin: 0xb90
-  __TEXT.__swift5_assocty: 0x24f8
+  __TEXT.__swift5_capture: 0x8018
+  __TEXT.__swift5_builtin: 0xb7c
+  __TEXT.__swift5_assocty: 0x2510
   __TEXT.__swift5_protos: 0x12c
-  __TEXT.__swift_as_entry: 0x918
-  __TEXT.__swift_as_ret: 0x808
-  __TEXT.__swift5_mpenum: 0x194
-  __TEXT.__unwind_info: 0xfbb8
-  __TEXT.__eh_frame: 0x165ac
-  __DATA_CONST.__auth_got: 0x47b8
-  __DATA_CONST.__got: 0x32b8
-  __DATA_CONST.__auth_ptr: 0x2f50
-  __DATA_CONST.__const: 0x33b50
-  __DATA_CONST.__cfstring: 0xe0
-  __DATA_CONST.__objc_classlist: 0x558
-  __DATA_CONST.__objc_catlist: 0xd0
+  __TEXT.__swift_as_entry: 0x8b4
+  __TEXT.__swift_as_ret: 0x794
+  __TEXT.__swift5_mpenum: 0x184
+  __TEXT.__ustring: 0xec
+  __TEXT.__unwind_info: 0xf978
+  __TEXT.__eh_frame: 0x154e4
+  __DATA_CONST.__auth_got: 0x47d8
+  __DATA_CONST.__got: 0x3290
+  __DATA_CONST.__auth_ptr: 0x2f78
+  __DATA_CONST.__const: 0x342b8
+  __DATA_CONST.__cfstring: 0x120
+  __DATA_CONST.__objc_classlist: 0x550
+  __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x460
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x220
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x1a720
-  __DATA.__objc_selrefs: 0x4860
+  __DATA.__objc_const: 0x1a710
+  __DATA.__objc_selrefs: 0x4868
   __DATA.__objc_ivar: 0x5c
-  __DATA.__objc_data: 0x8408
-  __DATA.__data: 0x17ce8
+  __DATA.__objc_data: 0x8320
+  __DATA.__data: 0x17d10
   __DATA.__objc_stublist: 0x18
-  __DATA.__common: 0x3b28
-  __DATA.__bss: 0x25c80
+  __DATA.__common: 0x3ca8
+  __DATA.__bss: 0x25e00
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 20CFC6AD-92C7-32E6-A56B-069DF4AA4768
-  Functions: 22466
-  Symbols:   1115
-  CStrings:  6001
+  UUID: 338001D5-9B79-38AC-A51A-A0C43A018974
+  Functions: 22482
+  Symbols:   1107
+  CStrings:  5988
 
Symbols:
+ _NSLog
+ _uset_containsAllCodePoints
+ _uset_openPattern
+ _uset_span
- _ICURLBagKeyAMPMusicAPIDomains
- _ICURLBagKeyCountryCode
- _MPModelPropertyLyricsHasLibraryLyrics
- _MPModelPropertyLyricsHasStoreLyrics
- _MPModelPropertyLyricsHasTimeSyncedLyrics
- _MPModelPropertyLyricsText
- _MPModelPropertySongArtistUploadedContent
- _MPModelRelationshipSongLyrics
- _OBJC_CLASS_$_MPStoreLyricsRequest
- _OBJC_CLASS_$_MusicLyricsLoader
- _OBJC_CLASS_$_NSJSONSerialization
- _OBJC_METACLASS_$_MusicLyricsLoader
CStrings:
+ "Initialized lyrics with catalog lyrics %{public}s, preferredTranslation: %{public}s, preferredTransliteration: %{public}s, currentTransliteration: %{public}s, currentTranslation: %{public}s preferredLanguageCodes: %{public}s, preferredScriptCodes: %{public}s"
+ "MiniPlayerArtworkVisible"
+ "MusicUtilitiesAdditions"
+ "["
+ "[State] Successfully loaded lyrics for song %{public}s."
+ "_fastCharacterContents"
+ "catalogLyrics"
+ "chineseJapaneseCharactersAnalysis"
+ "constrainToSafeAreaOf:"
+ "constrainToSafeAreaOf:padding:"
+ "getCharacters:range:"
+ "jaxson"
+ "jonah"
+ "libraryImportEnabled"
+ "nowPlaying.AutoMixButton"
+ "nowPlaying.CrossFadeButton"
+ "nowPlaying.SongTransitionsBadge.blending"
+ "nowPlaying.SongTransitionsBadge.crossfading"
+ "nowPlaying.SongTransitionsBadge.mixing"
+ "nowPlaying.SongTransitionsBadge.trimming"
+ "nowPlaying.TranslationButton"
+ "nowPlaying.hidePronunciation"
+ "nowPlaying.hideTranslation"
+ "nowPlaying.showPronunciation"
+ "nowPlaying.showTranslation"
+ "v32@0:8@16d24"
- " song.catalogID="
- "%{public}s loadLyrics(for:completion:) completed for %{public}s"
- "/syllable-lyrics"
- "Data request error: %{public}@"
- "Initialized lyrics with identifier %{public}s, preferredTranslation: %{public}s, preferredTransliteration: %{public}s, currentTransliteration: %{public}s, currentTranslation: %{public}s preferredLanguageCodes: %{public}s, preferredScriptCodes: %{public}s"
- "Invalid response: %{public}s"
- "JSONObjectWithData:options:error:"
- "Loader supportsLyrics=%{bool,public}d [bag is nil] song.title=%{public}s song.identifiers=%{public}s"
- "Loader supportsLyrics=%{bool,public}d [can't support store lyrics] lyrics.hasStoreLyrics=%{bool,public}d allowsSubscriptionContent=%{bool,public}d song.title=%{public}s song.identifiers=%{public}s"
- "Loader supportsLyrics=%{bool,public}d [can't support store lyrics] song.hasLyrics=%{bool,public}d allowsSubscriptionContent=%{bool,public}d %{public}s"
- "Loader supportsLyrics=%{bool,public}d [no lyrics keys in bag] song.title=%{public}s song.identifiers=%{public}s"
- "Loader supportsLyrics=%{bool,public}d [no musicSubscription key in bag] song.title=%{public}s song.identifiers=%{public}s"
- "Loader supportsLyrics=%{bool,public}d [not supported by subscription] subscriptionCapabilities.contains(.catalogLyricsViewing)=false %{public}s"
- "Loader supportsLyrics=%{bool,public}d [not supported by subscription] subscriptionCapabilities.contains(.catalogLyricsViewing)=false song.title=%{public}s song.identifiers=%{public}s"
- "Loader supportsLyrics=%{public}s [bag is nil] %{public}s"
- "Loader supportsLyrics=%{public}s [no lyrics keys in bag] %{public}s"
- "Loader supportsLyrics=%{public}s [no musicSubscription key in bag] %{public}s"
- "Loader supportsLyrics=false [MPModelLyrics was nil] song.title=%{public}s song.identifiers=%{public}s"
- "Loader supportsLyrics=false [hasLyrics and hasCustomLyrics were false] %{public}s"
- "Loader supportsLyrics=false [no lyrics found] lyrics.hasLibraryLyrics=%{bool,public}d lyrics.hasStoreLyrics=%{bool,public}d song.title=%{public}s song.identifiers=%{public}s"
- "Loader<%{public}s> loadLyrics(for:completion:) didn't load lyrics [no lyrics found] song.hasLyrics=false song.hasCustomLyrics=%{public}s song.customLyrics=%{public}s %{public}s"
- "Loader<%{public}s> loadLyrics(for:completion:) didn't load store lyrics [not supported by subscription] subscriptionStatus=%{public}s subscriptionStatus.capabilities.contains(.catalogLyricsViewing)=%{bool,public}d %{public}s"
- "Loader<%{public}s> loadLyrics(for:completion:) didn't parse TTML custom lyrics with error=%{public}s song.hasCustomLyrics=%{public}s song.customLyrics=%{public}s %{public}s"
- "Loader<%{public}s> loadLyrics(for:completion:) returned without loading lyrics [hasLyrics and hasCustomLyrics were false] %{public}s"
- "MusicLyricsLoader"
- "[State] Successfully loaded lyrics for song %{public}s with result %{public}s"
- "_loader"
- "fetchStoreLyrics: Bag is nil"
- "fetchStoreLyrics: Couldn't build URL: %{public}s"
- "fetchStoreLyrics: Unable to get the domain from the bag"
- "fetchStoreLyrics: song has no storeID"
- "hasLibraryLyrics"
- "loadLyrics(for:)"
- "mliEnabled"
- "mliEntryPointText"
- "operationQueue"
- "pins_widget"
- "supportsLyricsFor:"
- "supportsLyricsForURLBag:"
- "ttmlLocalizations"

```
