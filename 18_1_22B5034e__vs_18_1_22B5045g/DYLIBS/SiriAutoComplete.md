## SiriAutoComplete

> `/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete`

```diff

-3401.14.1.0.0
-  __TEXT.__text: 0x3470c
-  __TEXT.__auth_stubs: 0x1270
-  __TEXT.__const: 0x1530
-  __TEXT.__cstring: 0xf47
-  __TEXT.__constg_swiftt: 0xb94
-  __TEXT.__swift5_typeref: 0x7f9
-  __TEXT.__swift5_reflstr: 0x478
-  __TEXT.__swift5_fieldmd: 0x6f4
-  __TEXT.__oslogstring: 0x22dc
-  __TEXT.__swift5_proto: 0x128
-  __TEXT.__swift5_types: 0x9c
-  __TEXT.__swift5_protos: 0x28
+3401.20.1.0.0
+  __TEXT.__text: 0x3bcb8
+  __TEXT.__auth_stubs: 0x1350
+  __TEXT.__const: 0x15d0
+  __TEXT.__cstring: 0x10f7
+  __TEXT.__constg_swiftt: 0xc28
+  __TEXT.__swift5_typeref: 0x8bd
+  __TEXT.__swift5_reflstr: 0x4d8
+  __TEXT.__swift5_fieldmd: 0x72c
+  __TEXT.__swift5_capture: 0xf4
+  __TEXT.__oslogstring: 0x25ac
+  __TEXT.__swift5_proto: 0x12c
+  __TEXT.__swift5_types: 0xa0
+  __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0xd08
-  __TEXT.__eh_frame: 0x1920
-  __TEXT.__objc_methname: 0x5ff
-  __DATA_CONST.__got: 0x2c0
+  __TEXT.__unwind_info: 0xef8
+  __TEXT.__eh_frame: 0x2168
+  __TEXT.__objc_methname: 0x654
+  __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__const: 0x150
-  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a0
-  __AUTH_CONST.__auth_got: 0x938
-  __AUTH_CONST.__auth_ptr: 0x318
-  __AUTH_CONST.__const: 0xda8
-  __AUTH_CONST.__objc_const: 0xe10
+  __DATA_CONST.__objc_selrefs: 0x2c0
+  __AUTH_CONST.__auth_got: 0x9a8
+  __AUTH_CONST.__auth_ptr: 0x358
+  __AUTH_CONST.__const: 0xe70
+  __AUTH_CONST.__objc_const: 0xee0
   __AUTH.__objc_data: 0x230
-  __AUTH.__data: 0xb88
-  __DATA.__data: 0x610
-  __DATA.__common: 0x88
+  __AUTH.__data: 0xc40
+  __DATA.__data: 0x718
+  __DATA.__common: 0x90
   __DATA.__bss: 0x1c00
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x580
+  __DATA_DIRTY.__data: 0x5a8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals
   - /System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions
   - /System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit
+  - /System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities
   - /System/Library/PrivateFrameworks/ToolKit.framework/ToolKit
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1190
-  Symbols:   525
-  CStrings:  297
+  Functions: 1307
+  Symbols:   598
+  CStrings:  317
 
Symbols:
+ _swift_dynamicCast
+ _swift_getDynamicType
CStrings:
+ "domain"
+ "fetchTitleforGenericIntent(for:intentEvent:bundleId:criteria:)"
+ "compatibilityVersion"
+ "sourcePhraseGenerationTimeoutSeconds"
+ "$__lazy_storage_$_eligibilityCriteria"
+ "isGenericIntent"
+ "sinkWithCompletion:shouldContinue:"
+ "SiriKitIntentSource: Constructed invocation phrase of \"%!s(MISSING)\" for intent %!s(MISSING)"
+ "isIntentEligibleForAutoComplete(bundleId:intentEvent:validParametersSet:nonNilIntentParameters:criteria:)"
+ "%!s(MISSING): %!l(MISSING)d app detected for %!s(MISSING), not adding app mention suffix"
+ "Adding phrase with identifier: %!s(MISSING), phrase: %!s(MISSING)"
+ "_TtC16SiriAutoComplete30MapsGenericIntentTitleProvider"
+ "Timeout error fetching phrases for %!s(MISSING)"
+ "%!s(MISSING): Fetching phrases"
+ "%!s(MISSING) already built index on a start up event like GM Available or Suggestions startup recently. Not building again"
+ "%!s(MISSING): index build is not enabled. Not running updateIndexForAppInstall"
+ "parameterIdentifier"
+ "titlesForValidParameterCombinations(bundleId:intentEvent:intent:criteria:)"
+ "Function: %!s(MISSING) > parametersByName was unexpectedly empty for generic intent from bundleId: %!s(MISSING)"
+ "Function: %!s(MISSING) > parametersByName does not contain the 'element' attribute; no phrase generated for generic intent from: %!s(MISSING)"
+ "fetchPhrasesTimeoutSeconds"
+ "Function: %!s(MISSING) > _validParameterCombinations not present or empty for non-generic intent from %!s(MISSING)"
+ "Function: %!s(MISSING) > parametersByName does not contain 'title' attribute; no phrase generated for generic intent from: %!s(MISSING)"
+ "%!s(MISSING) updateIndexForAppInstall with %!s(MISSING)"
+ "parametersByName"
+ "Function: %!s(MISSING) > parametersByName does not contain the 'compatibilityVersion' attribute; no phrase generated for generic intent from: %!s(MISSING)"
+ "extractTitle(bundleId:parametersByName:intent:)"
+ "%!f(MISSING) seconds have passed since requesting SiriKitIntentTranscript events, which is passed our threshold. Not continuing to process more events"
+ "%!s(MISSING): automatic index building is disabled"
+ "%!s(MISSING): appIntentSources feature flag is not enabled. Not indexing phrases from the App Intent sources"
+ "privatePlayMediaIntentData"
- "SiriAutoCompleteIndexBuilder updateIndexForAppInstall with %!s(MISSING)"
- "SiriAutoCompleteIndexBuilder: index build upon first installation is currently disabled"
- "SiriAutoCompleteIndexBuilder: index build is not enabled. Not running updateIndexForAppInstall"
- "_hasTitle"
- "SiriKitIntentSource: %!l(MISSING)d app detected for %!s(MISSING), not adding app mention suffix"
- "Skipping INIntent with missing title from bundleId: %!s(MISSING))"
- "isIntentEligibleForAutoComplete(bundleId:intentEvent:validParametersSet:criteria:)"
- "SiriAutoCompleteIndexBuilder: automatic index building is disabled"
- "eligibilityCriteria"
- "SiriKitIntentSource: More than one apps detected for %!s(MISSING), constructed invocation phrase of \"%!s(MISSING)\""
- "SiriAutoCompleteIndexBuilder: appIntentSources feature flag is not enabled. Not indexing phrases from the App Intent sources"

```
