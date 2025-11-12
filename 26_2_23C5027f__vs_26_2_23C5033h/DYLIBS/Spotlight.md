## Spotlight

> `/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight`

```diff

-2400.16.0.0.0
+2400.17.1.0.0
   __TEXT.__text: 0x539c4
   __TEXT.__auth_stubs: 0x1040
   __TEXT.__objc_methlist: 0x207c

   __TEXT.__eh_frame: 0x60
   __TEXT.__objc_classname: 0x235
   __TEXT.__objc_methname: 0x93c1
-  __TEXT.__objc_methtype: 0x170b
+  __TEXT.__objc_methtype: 0x170e
   __TEXT.__objc_stubs: 0x8ae0
   __DATA_CONST.__got: 0x1318
   __DATA_CONST.__const: 0xb98

   - /System/Library/PrivateFrameworks/SpotlightRecommendation.framework/SpotlightRecommendation
   - /System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources
   - /System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices
+  - /System/Library/PrivateFrameworks/SpotlightUIServices.framework/SpotlightUIServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EB83D147-D2E8-3F58-A865-1E6E886E7711
+  UUID: 28CC83C7-BD48-369C-B858-ABE26AACF3CB
   Functions: 964
   Symbols:   4721
   CStrings:  2829
Symbols:
+ _OBJC_CLASS_$_SPUISDataDetectorResultGenerator
+ _OBJC_CLASS_$_SPUISDateFormatManager
+ _OBJC_CLASS_$_SPUISRecentResultsManager
+ _OBJC_CLASS_$_SPUISSectionBuilderHandler
+ _OBJC_CLASS_$_SPUISSuggestionResultBuilder
+ ___107-[SPFederatedQueryTask sendResults:reset:partiallyComplete:update:complete:unchanged:delayedTopHit:reason:]_block_invoke.661
+ ___121-[SPParsecQuery query:didFinishWithResults:withSuggestions:withCorrections:withAlternativeResults:suggestionsAreBlended:]_block_invoke.609
+ ___121-[SPParsecQuery query:didFinishWithResults:withSuggestions:withCorrections:withAlternativeResults:suggestionsAreBlended:]_block_invoke.609.cold.1
+ ___23-[SPZKWQueryTask start]_block_invoke.531
+ ___23-[SPZKWQueryTask start]_block_invoke.531.cold.1
+ ___23-[SPZKWQueryTask start]_block_invoke.539
+ ___23-[SPZKWQueryTask start]_block_invoke.540
+ ___23-[SPZKWQueryTask start]_block_invoke.544
+ ___23-[SPZKWQueryTask start]_block_invoke.544.cold.1
+ ___23-[SPZKWQueryTask start]_block_invoke.544.cold.2
+ ___23-[SPZKWQueryTask start]_block_invoke.554
+ ___27+[SPCSSearchQuery activate]_block_invoke.594
+ ___29+[SPCSSearchQuery initialize]_block_invoke.582
+ ___34+[SPFederatedQueryTask initialize]_block_invoke.599
+ ___39-[SPParsecQuery queryDidFinishLoading:]_block_invoke.524
+ ___40-[SPFederatedQueryTask addAndStartQuery]_block_invoke.802
+ ___40-[SPFederatedQueryTask addAndStartQuery]_block_invoke_2.807
+ ___47-[SPCSSearchQuery updateMailAttachmentResults:]_block_invoke.637
+ ___51-[SPFederatedQueryTask sendFinishedDomains:reason:]_block_invoke.690
+ ___51-[SPFederatedQueryTask sendFinishedDomains:reason:]_block_invoke.694
+ ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.756
+ ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.761
+ ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.775
+ ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke.581
+ ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_2.584
+ ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_3.585
+ ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_4.586
+ ____ZN12_GLOBAL__N_117updateMailVIPListEv_block_invoke.1058
+ ____ZN12_GLOBAL__N_117updateMailVIPListEv_block_invoke.1058.cold.1
+ ___block_literal_global.1056
+ ___block_literal_global.529
+ ___block_literal_global.552
+ ___block_literal_global.584
+ ___block_literal_global.588
+ ___block_literal_global.596
+ ___block_literal_global.604
+ ___block_literal_global.632
+ ___block_literal_global.638
+ ___block_literal_global.656
+ ___block_literal_global.663
+ ___block_literal_global.667
+ ___block_literal_global.668
+ ___block_literal_global.681
+ ___block_literal_global.684
+ ___block_literal_global.686
+ ___block_literal_global.709
+ ___block_literal_global.743
+ ___block_literal_global.751
+ ___block_literal_global.764
+ ___block_literal_global.777
+ ___block_literal_global.829
+ ___block_literal_global.853
+ ___block_literal_global.856
+ ___block_literal_global.868
- _OBJC_CLASS_$_SSDataDetectorResultGenerator
- _OBJC_CLASS_$_SSDateFormatManager
- _OBJC_CLASS_$_SSRecentResultsManager
- _OBJC_CLASS_$_SSSectionBuilderHandler
- _OBJC_CLASS_$_SSSuggestionResultBuilder
- ___107-[SPFederatedQueryTask sendResults:reset:partiallyComplete:update:complete:unchanged:delayedTopHit:reason:]_block_invoke.313
- ___121-[SPParsecQuery query:didFinishWithResults:withSuggestions:withCorrections:withAlternativeResults:suggestionsAreBlended:]_block_invoke.189
- ___121-[SPParsecQuery query:didFinishWithResults:withSuggestions:withCorrections:withAlternativeResults:suggestionsAreBlended:]_block_invoke.189.cold.1
- ___23-[SPZKWQueryTask start]_block_invoke.105
- ___23-[SPZKWQueryTask start]_block_invoke.105.cold.1
- ___23-[SPZKWQueryTask start]_block_invoke.113
- ___23-[SPZKWQueryTask start]_block_invoke.114
- ___23-[SPZKWQueryTask start]_block_invoke.118
- ___23-[SPZKWQueryTask start]_block_invoke.118.cold.1
- ___23-[SPZKWQueryTask start]_block_invoke.118.cold.2
- ___23-[SPZKWQueryTask start]_block_invoke.128
- ___27+[SPCSSearchQuery activate]_block_invoke.183
- ___29+[SPCSSearchQuery initialize]_block_invoke.171
- ___34+[SPFederatedQueryTask initialize]_block_invoke.245
- ___39-[SPParsecQuery queryDidFinishLoading:]_block_invoke.101
- ___40-[SPFederatedQueryTask addAndStartQuery]_block_invoke.454
- ___40-[SPFederatedQueryTask addAndStartQuery]_block_invoke_2.459
- ___47-[SPCSSearchQuery updateMailAttachmentResults:]_block_invoke.226
- ___51-[SPFederatedQueryTask sendFinishedDomains:reason:]_block_invoke.342
- ___51-[SPFederatedQueryTask sendFinishedDomains:reason:]_block_invoke.346
- ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.408
- ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.413
- ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.427
- ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke.161
- ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_2.164
- ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_3.165
- ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_4.166
- ____ZN12_GLOBAL__N_117updateMailVIPListEv_block_invoke.650
- ____ZN12_GLOBAL__N_117updateMailVIPListEv_block_invoke.650.cold.1
- ___block_literal_global.115
- ___block_literal_global.141
- ___block_literal_global.173
- ___block_literal_global.177
- ___block_literal_global.185
- ___block_literal_global.250
- ___block_literal_global.257
- ___block_literal_global.273
- ___block_literal_global.275
- ___block_literal_global.281
- ___block_literal_global.287
- ___block_literal_global.301
- ___block_literal_global.308
- ___block_literal_global.315
- ___block_literal_global.319
- ___block_literal_global.333
- ___block_literal_global.395
- ___block_literal_global.403
- ___block_literal_global.416
- ___block_literal_global.429
- ___block_literal_global.481
- ___block_literal_global.505
- ___block_literal_global.508
- ___block_literal_global.523
- ___block_literal_global.648
CStrings:
+ "@\"SPUISDataDetectorResultGenerator\""
- "@\"SSDataDetectorResultGenerator\""

```
