## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/Versions/A/PeopleSuggester`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1933.12.0.0.0
-  __TEXT.__text: 0x109b8c
+1933.13.0.0.0
+  __TEXT.__text: 0x109c64
   __TEXT.__auth_stubs: 0xd50
   __TEXT.__objc_methlist: 0xa01c
   __TEXT.__const: 0x8c0

   __TEXT.__unwind_info: 0x3000
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x1262
-  __TEXT.__objc_methname: 0x222f0
+  __TEXT.__objc_methname: 0x2233a
   __TEXT.__objc_methtype: 0x27b6
   __TEXT.__objc_stubs: 0x12b00
   __DATA_CONST.__got: 0x8b8
Symbols:
+ +[_PSAppUsageUtilities boostAppsForSourceBundleId:attachments:mapping:traceId:parentSpanId:]
+ +[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:]
+ __196+[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:]_block_invoke
+ ___196+[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:]_block_invoke
+ _objc_msgSend$boostAppsForSourceBundleId:attachments:mapping:traceId:parentSpanId:
+ _objc_msgSend$mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:
- +[_PSAppUsageUtilities boostAppsForSourceBundleId:]
- +[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:]
- __163+[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:]_block_invoke
- ___163+[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:]_block_invoke
- _objc_msgSend$boostAppsForSourceBundleId:
- _objc_msgSend$mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:
Functions:
~ -[_PSEnsembleModel appExtensionSuggestionsFromContext:] : 792 -> 904
~ +[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:] -> +[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:] : 1076 -> 1180
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UnFMav/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/AppExtensionPredictions/_PSAppUsageUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UnFMav/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/CloudFamily/_PSFamilyRecommender.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UnFMav/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/_PSSuggestion.m"
+ "boostAppsForSourceBundleId:attachments:mapping:traceId:parentSpanId:"
+ "mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Cbhu59/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/AppExtensionPredictions/_PSAppUsageUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Cbhu59/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/CloudFamily/_PSFamilyRecommender.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Cbhu59/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/_PSSuggestion.m"
- "boostAppsForSourceBundleId:"
- "mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:"
```
