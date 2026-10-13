## PhotoAnalysis

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis`

```diff

-916.51.202.0.0
-  __TEXT.__text: 0x269ee8
+916.57.151.0.0
+  __TEXT.__text: 0x26a0b8
   __TEXT.__objc_methlist: 0x615c
   __TEXT.__const: 0xdb40
   __TEXT.__constg_swiftt: 0x4634

   __TEXT.__swift5_fieldmd: 0x4580
   __TEXT.__swift5_builtin: 0x1f4
   __TEXT.__swift5_assocty: 0x750
-  __TEXT.__cstring: 0x105f3
+  __TEXT.__cstring: 0x10661
   __TEXT.__swift5_capture: 0x3500
   __TEXT.__oslogstring: 0x158ef
   __TEXT.__swift5_proto: 0x7d0

   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__got: 0x2200
   __AUTH_CONST.__const: 0xd728
-  __AUTH_CONST.__cfstring: 0x8360
+  __AUTH_CONST.__cfstring: 0x83e0
   __AUTH_CONST.__objc_const: 0x12a00
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x30

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 9733
   Symbols:   6396
-  CStrings:  3214
+  CStrings:  3218
 
Functions:
~ -[PHAWallpaperSuggestionAnalyticsSender wallpaperGenerationSummaryWithGeneratedSuggestionLocalIdentifiers:] : 864 -> 952
~ -[PHAWallpaperSuggestionAnalyticsSender existingWallpaperSuggestionSummary] : 1256 -> 1344
~ +[PHAWallpaperSuggestionAnalyticsSender wallpaperSuggestionStatisticsFromSuggestions:] : 556 -> 628
~ -[PHAWallpaperSuggestionAnalyticsSender ambientGenerationSummaryWithGeneratedSuggestionLocalIdentifiers:] : 672 -> 720
~ +[PHAWallpaperSuggestionAnalyticsSender ambientSuggestionStatisticsFromSuggestions:] : 408 -> 448
~ -[PHAWallpaperSuggestionAnalyticsSender existingAmbientSuggestionSummary] : 804 -> 852
~ +[PHAWallpaperSuggestionGenerationUtils isGraphDependentSubtype:] : 308 -> 336
~ -[PHAWallpaperSuggestionRefreshSession fetchSuggestionsForGalleryDonationWithSuggestionUUIDsToAvoid:] : 1256 -> 1308
CStrings:
+ "group_suggestion_count"
+ "group_suggestions_generated"
+ "top_group_suggestion_count"
+ "top_group_suggestions_generated"
```
