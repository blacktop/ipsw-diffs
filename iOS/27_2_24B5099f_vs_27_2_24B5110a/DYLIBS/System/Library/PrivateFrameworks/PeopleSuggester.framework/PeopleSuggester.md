## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1976.0.0.0.0
-  __TEXT.__text: 0x125300
+1977.0.0.0.0
+  __TEXT.__text: 0x1252f4
   __TEXT.__objc_methlist: 0xaedc
   __TEXT.__const: 0x988
   __TEXT.__gcc_except_tab: 0x4a90
   __TEXT.__cstring: 0x31662
-  __TEXT.__oslogstring: 0x1124c
+  __TEXT.__oslogstring: 0x1122c
   __TEXT.__dlopen_cstrs: 0x19c8
   __TEXT.__ustring: 0xb22
   __TEXT.__unwind_info: 0x4550

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7150
+  __DATA_CONST.__objc_selrefs: 0x7148
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x39e80
-  __DATA_CONST.__got: 0xa50
+  __DATA_CONST.__got: 0xa48
   __AUTH_CONST.__const: 0x1cc0
   __AUTH_CONST.__cfstring: 0x7fc40
   __AUTH_CONST.__objc_const: 0x15978

   - /System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji
   - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
-  - /System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 5368
-  Symbols:   7994
+  Symbols:   7993
   CStrings:  17939
 
Symbols:
- _OBJC_CLASS_$_PETEventTracker2
Functions:
~ -[_PSInteractionsStatistics(StaticFeatures) computeTimeSinceLastPhoneCallWithConversationId:interactionRecord:] : 352 -> 368
~ -[_PSInteractionsStatistics(StaticFeatures) computeTimeSinceLastIncomingInteractionForConversationId:interactionRecord:] : 228 -> 252
~ -[_PSInteractionsStatistics loadFeaturesAndPropertiesFromContactCatalog] : 4144 -> 4136
~ ___61-[_PSEnsembleModel sendDataToPETAsync:withConfig:andContext:]_block_invoke : 180 -> 136
CStrings:
+ "Loaded contact catalog: %lu conversations, %lu features, %lu properties, %lu personId sets, %lu bundleId counts, %lu visual identifiers, latencyMs=%.2f"
+ "_PSEnsemble: sent data to Biome"
- "Loaded contact catalog: %lu conversations, %lu features, %lu properties, %lu personId sets, %lu bundleId counts, %lu visual identifiers (skipped %lu timeSince* features), latencyMs=%.2f"
- "_PSEnsemble: sent data to PET"
```
