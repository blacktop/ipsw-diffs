## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/Versions/A/PeopleSuggester`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1962.0.1.0.0
-  __TEXT.__text: 0x127c04
-  __TEXT.__objc_methlist: 0xac94
+1967.0.0.0.0
+  __TEXT.__text: 0x128164
+  __TEXT.__objc_methlist: 0xac9c
   __TEXT.__const: 0x978
   __TEXT.__gcc_except_tab: 0x41fc
-  __TEXT.__cstring: 0x31337
-  __TEXT.__oslogstring: 0xfd50
+  __TEXT.__cstring: 0x313ac
+  __TEXT.__oslogstring: 0xfd9f
   __TEXT.__dlopen_cstrs: 0x160f
   __TEXT.__ustring: 0x7e4
-  __TEXT.__unwind_info: 0x3348
+  __TEXT.__unwind_info: 0x3358
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d38
+  __DATA_CONST.__objc_selrefs: 0x6d58
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x39d78
-  __DATA_CONST.__got: 0x928
+  __DATA_CONST.__got: 0x930
   __AUTH_CONST.__const: 0x4340
-  __AUTH_CONST.__cfstring: 0x7eee0
+  __AUTH_CONST.__cfstring: 0x7f000
   __AUTH_CONST.__objc_const: 0x155e8
   __AUTH_CONST.__objc_intobj: 0x1170
   __AUTH_CONST.__objc_arrayobj: 0x11d18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5229
-  Symbols:   10528
-  CStrings:  17723
+  Functions: 5232
+  Symbols:   10534
+  CStrings:  17733
 
Symbols:
+ +[_PSAppUsageUtilities boostAppsForSourceBundleId:attachments:mapping:traceId:parentSpanId:]
+ +[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:]
+ -[_PSContactCatalog _attemptLoadContactCatalogCapturingAttributes:]
+ _NSFileSize
+ __196+[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:]_block_invoke
+ ___196+[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:]_block_invoke
+ _objc_msgSend$_attemptLoadContactCatalogCapturingAttributes:
+ _objc_msgSend$attributesOfItemAtPath:error:
+ _objc_msgSend$boostAppsForSourceBundleId:attachments:mapping:traceId:parentSpanId:
+ _objc_msgSend$mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$unsignedLongLongValue
- +[_PSAppUsageUtilities boostAppsForSourceBundleId:]
- +[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:]
- __163+[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:]_block_invoke
- ___163+[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:]_block_invoke
- _objc_msgSend$boostAppsForSourceBundleId:
- _objc_msgSend$mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAGntE/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/AppExtensionPredictions/_PSAppUsageUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAGntE/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/CloudFamily/_PSFamilyRecommender.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAGntE/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/_PSSuggestion.m"
+ "Contact catalog root is not a dictionary; got %{public}@ (fileSize=%llu bytes)"
+ "fileNotFound"
+ "fileSizeBytes"
+ "loadContactCatalog"
+ "nonDictionary"
+ "outcome"
+ "parseFailed"
+ "readFailed"
+ "rootClass"
+ "versionMismatch"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ttHUjs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/AppExtensionPredictions/_PSAppUsageUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ttHUjs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/CloudFamily/_PSFamilyRecommender.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ttHUjs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/_PSSuggestion.m"
```
