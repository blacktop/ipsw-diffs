## IntelligenceFlowContextRuntime

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime`

```diff

-3605.22.501.11.0
-  __TEXT.__text: 0x10ace4
+3610.18.2.501.3
+  __TEXT.__text: 0x115614
   __TEXT.__objc_methlist: 0x6d4
-  __TEXT.__const: 0x4b80
-  __TEXT.__swift5_typeref: 0x2bde
-  __TEXT.__swift5_fieldmd: 0x12b4
-  __TEXT.__constg_swiftt: 0x1b4c
+  __TEXT.__const: 0x4d80
+  __TEXT.__swift5_typeref: 0x2cbe
+  __TEXT.__swift5_fieldmd: 0x1348
+  __TEXT.__constg_swiftt: 0x1c10
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0xd4a
+  __TEXT.__swift5_reflstr: 0xdca
   __TEXT.__swift5_assocty: 0x220
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__swift5_proto: 0x1fc
-  __TEXT.__swift5_types: 0x1f4
-  __TEXT.__cstring: 0x1f8c
-  __TEXT.__oslogstring: 0x44a1
-  __TEXT.__swift_as_entry: 0x3a4
-  __TEXT.__swift_as_ret: 0x3f4
-  __TEXT.__swift_as_cont: 0x694
-  __TEXT.__swift5_capture: 0x183c
+  __TEXT.__swift5_proto: 0x204
+  __TEXT.__swift5_types: 0x204
+  __TEXT.__cstring: 0x20ac
+  __TEXT.__oslogstring: 0x46a2
+  __TEXT.__swift_as_entry: 0x3ac
+  __TEXT.__swift_as_ret: 0x40c
+  __TEXT.__swift_as_cont: 0x6c4
+  __TEXT.__swift5_capture: 0x18c4
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x3a80
-  __TEXT.__eh_frame: 0x8ccc
+  __TEXT.__unwind_info: 0x3c40
+  __TEXT.__eh_frame: 0x8edc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x148
-  __DATA_CONST.__objc_classlist: 0x108
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad0
+  __DATA_CONST.__objc_selrefs: 0xb20
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__got: 0x10c0
-  __AUTH_CONST.__const: 0x5880
+  __DATA_CONST.__got: 0x1190
+  __AUTH_CONST.__const: 0x5b10
   __AUTH_CONST.__cfstring: 0xc0
-  __AUTH_CONST.__objc_const: 0x1ef8
-  __AUTH_CONST.__auth_got: 0x2788
+  __AUTH_CONST.__objc_const: 0x1ff8
+  __AUTH_CONST.__auth_got: 0x28f0
   __AUTH.__objc_data: 0x288
-  __AUTH.__data: 0x4a8
-  __DATA.__data: 0xb68
+  __AUTH.__data: 0x550
+  __DATA.__data: 0xcd8
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x5b0
-  __DATA_DIRTY.__data: 0x3588
+  __DATA_DIRTY.__data: 0x3548
   __DATA_DIRTY.__bss: 0xe80
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppIntentsLiveEntitySupport.framework/AppIntentsLiveEntitySupport
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5113
-  Symbols:   330
-  CStrings:  427
+  Functions: 5348
+  Symbols:   338
+  CStrings:  441
 
Symbols:
+ _OBJC_CLASS_$_LNImage
+ _SecTaskCreateWithAuditToken
+ _SecTaskGetCodeSignStatus
+ _kMRMediaRemoteMediaTypeAudioBook
+ _kMRMediaRemoteMediaTypeMusic
+ _kMRMediaRemoteMediaTypePodcast
+ _kMRMediaRemoteNowPlayingInfoTypeAudio
+ _kMRMediaRemoteNowPlayingInfoTypeVideo
CStrings:
+ "AudiobookAppEntity"
+ "Processing HAL playbackStateSnapshot: %@"
+ "SiriKitArtistEntity"
+ "SiriKitPodcastShowEntity"
+ "SiriKitSongEntity"
+ "SiriVideoMovieEntity"
+ "Unknown HAL media type: %s"
+ "[AppCompatibility] Editing context fetched for %{private}s but no matching window found to inject synthetic entity"
+ "[AppCompatibility] Synthesized OnScreenText for %{private}s, removedTraversalEntities=%{public}ld"
+ "[AppNameResolver] Unable to resolve app name for %{private}s: %{public}s"
+ "[ContextMenuEntityExtractor] Pattern 3 exported nothing — keeping %ld excluded entities on the source"
+ "[DisplayRepresentation] artwork retrieval failed: %{public}s"
+ "[DisplayRepresentation] artwork retrieval returned no bytes"
+ "[DisplayRepresentation] no archived LNImage behind an AppIntents image; entity artwork will be absent"
+ "[EditingContextFetcher] fetch failed for %{private}s: %{public}s"
+ "[EditingContextFetcher] fetch for %{private}s returned no value"
+ "[EditingContextFetcher] probe reported no editable field for %{private}s; skipping fetch"
+ "[ElementEntityExtractor] Filtered non-schematized 3P transient entity: %s from %s"
+ "[EntityPolicy] ToolDatabase unavailable — skipping schema check for %{private}s from %{private}s"
+ "[UserContextFetcher] Direct fetch %s for targetWindow=%{public}s, bundle=%{private}s"
+ "[UserContextFetcher] Editing context fetched for %{private}s but no matching focused OnScreenText entity found to stitch into — editing context discarded"
+ "[UserContextFetcher] Layout scan incomplete — timed out waiting on %{private}s; foreground selection may be wrong"
+ "[UserContextFetcher] No usable target window after retries for bundle=%{private}s; marking layout-scan target foreground"
+ "[UserContextFetcher] Stitched editing context (cursor=%{public}ld, preservedCount=%{public}ld, hasMarkdown=%{bool,public}d) into focused entity in %{private}s"
+ "[UserContextFetcher] Window %{public}s (bundle=%{private}s) carries content from %{public}ld Siri-excluded region(s) belonging to [%{private}s]; redacted screenshot and dropped snapshot image data"
+ "[UserContextFetcher] Window %{public}s (bundle=%{private}s) found in layout scan but returned no content in detailed fetch."
+ "[UserContextFetcher] Window %{public}s (bundle=%{private}s) is access-excluded; returning content-free skeleton without scraping"
+ "[UserContextFetcher] fetchWindow(%{public}s) — UIIS returned empty hierarchy (no roots). processInfo=%{private}s"
+ "com.apple.iBooks"
+ "com.apple.siri.AudioAppIntentsExtension"
+ "com.apple.siri.SiriVideoAppIntents"
- "[AppCompatibility] Editing context fetched for %{public}s but no matching window found to inject synthetic entity"
- "[AppCompatibility] Synthesized OnScreenText for %{public}s, removedTraversalEntities=%{public}ld"
- "[AppNameResolver] Unable to resolve app name for %{public}s: %@"
- "[EditingContextFetcher] fetch failed for %{public}s: %{public}s"
- "[EditingContextFetcher] fetch for %{public}s returned no value"
- "[EditingContextFetcher] probe reported no editable field for %{public}s; skipping fetch"
- "[ElementEntityExtractor] Filtered 3P transient entity from %s"
- "[ElementEntityExtractor] ToolDatabase unavailable — blocking 3P entity %s from %s"
- "[UserContextFetcher] Direct fetch %s for targetWindow=%{public}s, bundle=%{public}s"
- "[UserContextFetcher] Editing context fetched for %{sensitive}s but no matching focused OnScreenText entity found to stitch into — editing context discarded"
- "[UserContextFetcher] Layout scan incomplete — timed out waiting on %{public}s; foreground selection may be wrong"
- "[UserContextFetcher] No usable target window after retries for bundle=%{public}s; marking layout-scan target foreground"
- "[UserContextFetcher] Stitched editing context (cursor=%{public}ld, preservedCount=%{public}ld, hasMarkdown=%{bool,public}d) into focused entity in %{sensitive}s"
- "[UserContextFetcher] Window %{public}s (bundle=%{public}s) carries content from %{public}ld Siri-excluded region(s) belonging to [%{sensitive}s]; redacted screenshot and dropped snapshot image data"
- "[UserContextFetcher] Window %{public}s (bundle=%{public}s) found in layout scan but returned no content in detailed fetch."
- "[UserContextFetcher] Window %{public}s (bundle=%{public}s) is access-excluded; returning content-free skeleton without scraping"
- "[UserContextFetcher] fetchWindow(%{public}s) — UIIS returned empty hierarchy (no roots). processInfo=%{public}s"
```
