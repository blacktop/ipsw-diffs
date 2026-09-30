## MusicScriptUpdateService

> `/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService`

```diff

-4025.200.11.0.0
-  __TEXT.__text: 0x496c0c
-  __TEXT.__auth_stubs: 0x8f30
+4025.210.21.1.0
+  __TEXT.__text: 0x498c28
+  __TEXT.__auth_stubs: 0x8f90
   __TEXT.__objc_stubs: 0xe00
-  __TEXT.__objc_methlist: 0x4934
-  __TEXT.__const: 0x24220
-  __TEXT.__objc_methname: 0xdf05
-  __TEXT.__cstring: 0x146a4
-  __TEXT.__swift5_typeref: 0x19d12
+  __TEXT.__objc_methlist: 0x4984
+  __TEXT.__const: 0x24070
+  __TEXT.__objc_methname: 0xdfc4
+  __TEXT.__cstring: 0x14774
+  __TEXT.__swift5_typeref: 0x19cc8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1133c
-  __TEXT.__swift5_reflstr: 0xc301
-  __TEXT.__swift5_fieldmd: 0xddc4
-  __TEXT.__oslogstring: 0x9727
-  __TEXT.__swift5_proto: 0x172c
-  __TEXT.__swift5_types: 0xf90
+  __TEXT.__constg_swiftt: 0x11378
+  __TEXT.__swift5_reflstr: 0xc321
+  __TEXT.__swift5_fieldmd: 0xddb4
+  __TEXT.__oslogstring: 0x9607
+  __TEXT.__swift5_proto: 0x1714
+  __TEXT.__swift5_types: 0xf8c
   __TEXT.__objc_classname: 0x59e
   __TEXT.__objc_methtype: 0x3afd
-  __TEXT.__swift5_capture: 0x79dc
-  __TEXT.__swift5_builtin: 0xbb8
-  __TEXT.__swift5_assocty: 0x2528
+  __TEXT.__swift5_capture: 0x79fc
+  __TEXT.__swift5_builtin: 0xba4
+  __TEXT.__swift5_assocty: 0x24f8
   __TEXT.__swift5_protos: 0x12c
   __TEXT.__swift_as_entry: 0x918
   __TEXT.__swift_as_ret: 0x808
   __TEXT.__swift5_mpenum: 0x19c
-  __TEXT.__unwind_info: 0xfa88
-  __TEXT.__eh_frame: 0x16564
-  __DATA_CONST.__auth_got: 0x47a0
-  __DATA_CONST.__got: 0x32c0
-  __DATA_CONST.__auth_ptr: 0x2f48
-  __DATA_CONST.__const: 0x335d8
+  __TEXT.__unwind_info: 0xfaf8
+  __TEXT.__eh_frame: 0x165a4
+  __DATA_CONST.__auth_got: 0x47d0
+  __DATA_CONST.__got: 0x32c8
+  __DATA_CONST.__auth_ptr: 0x2f38
+  __DATA_CONST.__const: 0x33618
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x558
   __DATA_CONST.__objc_catlist: 0xd0

   __DATA_CONST.__objc_protorefs: 0x220
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x1a5b0
-  __DATA.__objc_selrefs: 0x4818
+  __DATA.__objc_const: 0x1a678
+  __DATA.__objc_selrefs: 0x4850
   __DATA.__objc_ivar: 0x5c
-  __DATA.__objc_data: 0x8348
+  __DATA.__objc_data: 0x83c0
   __DATA.__data: 0x17b98
   __DATA.__objc_stublist: 0x18
   __DATA.__common: 0x3b18
-  __DATA.__bss: 0x25f10
+  __DATA.__bss: 0x25c00
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C0DE59E9-5E57-3DB7-85F1-A7B413DC1904
-  Functions: 22317
-  Symbols:   1117
-  CStrings:  5985
+  UUID: CB904858-CF4E-3EE8-9351-FD8A1F7E4092
+  Functions: 22339
+  Symbols:   1115
+  CStrings:  5994
 
Symbols:
+ _MPModelPropertyAlbumTrackCount
+ _MPModelRelationshipAlbumRepresentativeSong
+ _UIAccessibilityButtonShapesEnabled
- _NLLanguageJapanese
- _NLLanguageSimplifiedChinese
- _NLLanguageTraditionalChinese
- _UIApplicationDidEnterBackgroundNotification
- _UIApplicationWillEnterForegroundNotification
CStrings:
+ "Failed to fetch music video from Media API with catalogID=%{public}s: %@"
+ "Failed to fetch song from Media API with catalogID=%{public}s: %@"
+ "No window scene associated! This could lead to a major power regression when the app is backgrounded!"
+ "Performing Media API request for %s with catalogID=%{public}s"
+ "T@\"MPModelSong\",N,R"
+ "T@\"MPPropertySet\",N,R"
+ "_setNonLargeBackground:"
+ "accessibilitySubtitleLabelText"
+ "accessibilityTitleLabelText"
+ "jafar"
+ "orphanMusicVideo"
+ "orphanMusicVideoPropertySet"
+ "representativeTitle"
+ "representativeTitlePropertySet"
+ "setAllowedScrollTypesMask:"
+ "timeMark"
+ "timeMarkOffsetConstraint"
+ "transitionStartValue"
- "ArtworkColors(background: "
- "Failed to fetch colors for music video from Media API with catalogID=%{public}s: %@"
- "Failed to fetch colors for song from Media API with catalogID=%{public}s: %@"
- "Failed to fetch music video from Media API with catalogID=%{public}s"
- "Failed to fetch song from Media API with catalogID=%{public}s"
- "FavoriteHighContrastDark"
- "FavoriteHighContrastLight"
- "No catalogID for Entry=%{public}s"
- "No catalogID for MPModelSong=%{public}@"
- "No catalogID for Track=%{public}s"
- "Performing Media API request for song with catalogID=%{public}s"
- "Retrieved artwork colors=%{public}s from Media API for song with identifiers=%{public}s"
- "carmageddon"
- "lumajustments"
- "totalItemCount"

```
