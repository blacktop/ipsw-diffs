## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/Versions/A/PeopleSuggester`

```diff

-1971.0.0.0.0
-  __TEXT.__text: 0x12847c
-  __TEXT.__objc_methlist: 0xac94
+1977.0.0.0.0
+  __TEXT.__text: 0x128578
+  __TEXT.__objc_methlist: 0xaca4
   __TEXT.__const: 0x978
   __TEXT.__gcc_except_tab: 0x42b4
-  __TEXT.__cstring: 0x31426
-  __TEXT.__oslogstring: 0xfcd3
+  __TEXT.__cstring: 0x31454
+  __TEXT.__oslogstring: 0xfcb3
   __TEXT.__dlopen_cstrs: 0x160f
   __TEXT.__ustring: 0x7e4
   __TEXT.__unwind_info: 0x3360

   __DATA_CONST.__objc_selrefs: 0x6d58
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x39d78
-  __DATA_CONST.__got: 0x930
+  __DATA_CONST.__got: 0x928
   __AUTH_CONST.__const: 0x4310
-  __AUTH_CONST.__cfstring: 0x7f000
+  __AUTH_CONST.__cfstring: 0x7f020
   __AUTH_CONST.__objc_const: 0x155e8
   __AUTH_CONST.__objc_intobj: 0x1170
   __AUTH_CONST.__objc_arrayobj: 0x11d18
   __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH_CONST.__objc_dictobj: 0x226c8
-  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH_CONST.__auth_got: 0x6d8
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x1bd0
   __DATA.__objc_ivar: 0xf0c
-  __DATA.__data: 0x428
   __DATA.__bss: 0x778
-  __DATA_DIRTY.__objc_data: 0x1a40
+  __DATA_DIRTY.__objc_data: 0x3610
+  __DATA_DIRTY.__data: 0x428
   __DATA_DIRTY.__bss: 0x780
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/Versions/A/CoreDuetContext
   - /System/Library/PrivateFrameworks/CoreEmoji.framework/Versions/A/CoreEmoji
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/Versions/A/IntelligencePlatformLibrary
-  - /System/Library/PrivateFrameworks/ProactiveEventTracker.framework/Versions/A/ProactiveEventTracker
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/Versions/A/ProactiveSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /System/Library/PrivateFrameworks/Rapport.framework/Versions/A/Rapport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5236
-  Symbols:   10537
-  CStrings:  17731
+  Functions: 5237
+  Symbols:   10538
+  CStrings:  17732
 
Symbols:
+ +[_PSConstants facetimeSupportServiceBundleId]
+ __CDStringByConvertingPhoneNumberStringToASCII
+ _objc_msgSend$facetimeSupportServiceBundleId
- _OBJC_CLASS_$_PETEventTracker2
- _objc_msgSend$logMessage:
Functions:
~ -[_PSInteractionsStatistics(StaticFeatures) computeTimeSinceLastPhoneCallWithConversationId:interactionRecord:] : 392 -> 412
~ -[_PSInteractionsStatistics(StaticFeatures) computeTimeSinceLastIncomingInteractionForConversationId:interactionRecord:] : 260 -> 280
~ -[_PSInteractionsStatistics loadFeaturesAndPropertiesFromContactCatalog] : 4428 -> 4420
~ -[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:predictionContext:] : 16748 -> 16780
~ ___61-[_PSEnsembleModel sendDataToPETAsync:withConfig:andContext:]_block_invoke : 192 -> 140
~ -[_PSEnsembleModel psr_suggestionsFromSuggestionProxies:interactionsStatistics:maxSuggestions:predictionContext:] : 2128 -> 2160
+ +[_PSConstants facetimeSupportServiceBundleId]
~ ___37-[_PSFamilyRecommender currentFamily]_block_invoke : 1528 -> 1552
~ -[_PSContactResolver resolveContactIdentifier:] : 824 -> 844
~ -[_PSContactResolver resolveContactIfPossibleFromContactIdentifierString:pickFirstOfMultiple:] : 304 -> 336
~ +[_PSContactResolver normalizedHandlesDictionaryFromHandles:] : 440 -> 476
~ -[_PSContactCache getContactForHandle:handleType:] : 1200 -> 1224
~ ___46-[_PSPredictionContext supportsZKWSuggestions]_block_invoke : 720 -> 756
~ -[_PSContactCatalog resolveVisualIdentifiersForHandles:catalogContactData:keepGoing:] : 9352 -> 9376
CStrings:
+ "Loaded contact catalog: %lu conversations, %lu features, %lu properties, %lu personId sets, %lu bundleId counts, %lu visual identifiers, latencyMs=%.2f"
+ "_PSEnsemble: sent data to Biome"
+ "com.apple.CopresenceUI.FaceTimeSupportService"
- "Loaded contact catalog: %lu conversations, %lu features, %lu properties, %lu personId sets, %lu bundleId counts, %lu visual identifiers (skipped %lu timeSince* features), latencyMs=%.2f"
- "_PSEnsemble: sent data to PET"
```
