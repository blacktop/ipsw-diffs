## Spotlight

> `/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight`

```diff

-2385.1.0.1.0
-  __TEXT.__text: 0x539e8
+2387.1.0.0.0
+  __TEXT.__text: 0x539d8
   __TEXT.__auth_stubs: 0x1040
   __TEXT.__objc_methlist: 0x2064
   __TEXT.__const: 0x190

   __TEXT.__objc_methname: 0x93a9
   __TEXT.__objc_methtype: 0x16c2
   __TEXT.__objc_stubs: 0x8ae0
-  __DATA_CONST.__got: 0x1318
+  __DATA_CONST.__got: 0x1310
   __DATA_CONST.__const: 0xb98
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6FC2CB2F-F4A7-3DE7-BBDB-ACC67EF21673
+  UUID: DFDE22BE-F07E-3CFC-8612-C8E49DC286A8
   Functions: 965
-  Symbols:   4718
+  Symbols:   4717
   CStrings:  2827
 
Symbols:
+ ___107-[SPFederatedQueryTask sendResults:reset:partiallyComplete:update:complete:unchanged:delayedTopHit:reason:]_block_invoke.313
+ ___121-[SPParsecQuery query:didFinishWithResults:withSuggestions:withCorrections:withAlternativeResults:suggestionsAreBlended:]_block_invoke.189
+ ___121-[SPParsecQuery query:didFinishWithResults:withSuggestions:withCorrections:withAlternativeResults:suggestionsAreBlended:]_block_invoke.189.cold.1
+ ___23-[SPZKWQueryTask start]_block_invoke.105
+ ___23-[SPZKWQueryTask start]_block_invoke.105.cold.1
+ ___23-[SPZKWQueryTask start]_block_invoke.113
+ ___23-[SPZKWQueryTask start]_block_invoke.114
+ ___23-[SPZKWQueryTask start]_block_invoke.118
+ ___23-[SPZKWQueryTask start]_block_invoke.118.cold.1
+ ___23-[SPZKWQueryTask start]_block_invoke.118.cold.2
+ ___23-[SPZKWQueryTask start]_block_invoke.128
+ ___30-[SPRecommendationQuery start]_block_invoke.154
+ ___31-[SPRecommendationQuery begin:]_block_invoke.86
+ ___31-[SPRecommendationQuery begin:]_block_invoke.86.cold.1
+ ___31-[SPRecommendationQuery begin:]_block_invoke.89
+ ___31-[SPRecommendationQuery begin:]_block_invoke.97
+ ___31-[SPRecommendationQuery begin:]_block_invoke.98
+ ___34+[SPFederatedQueryTask initialize]_block_invoke.245
+ ___39-[SPParsecQuery queryDidFinishLoading:]_block_invoke.101
+ ___40-[SPFederatedQueryTask addAndStartQuery]_block_invoke.454
+ ___40-[SPFederatedQueryTask addAndStartQuery]_block_invoke_2.459
+ ___51-[SPFederatedQueryTask sendFinishedDomains:reason:]_block_invoke.342
+ ___51-[SPFederatedQueryTask sendFinishedDomains:reason:]_block_invoke.346
+ ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.408
+ ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.413
+ ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.427
+ ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke.161
+ ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_2.164
+ ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_3.165
+ ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_4.166
+ ___block_literal_global.103
+ ___block_literal_global.115
+ ___block_literal_global.141
+ ___block_literal_global.198
+ ___block_literal_global.250
+ ___block_literal_global.281
+ ___block_literal_global.308
+ ___block_literal_global.315
+ ___block_literal_global.319
+ ___block_literal_global.333
+ ___block_literal_global.395
+ ___block_literal_global.403
+ ___block_literal_global.416
+ ___block_literal_global.429
+ ___block_literal_global.481
+ ___block_literal_global.505
+ ___block_literal_global.508
+ ___block_literal_global.523
+ ___block_literal_global.84
+ ___block_literal_global.85
- _NSFileProtectionNone
- ___107-[SPFederatedQueryTask sendResults:reset:partiallyComplete:update:complete:unchanged:delayedTopHit:reason:]_block_invoke.319
- ___121-[SPParsecQuery query:didFinishWithResults:withSuggestions:withCorrections:withAlternativeResults:suggestionsAreBlended:]_block_invoke.195
- ___121-[SPParsecQuery query:didFinishWithResults:withSuggestions:withCorrections:withAlternativeResults:suggestionsAreBlended:]_block_invoke.195.cold.1
- ___23-[SPZKWQueryTask start]_block_invoke.111
- ___23-[SPZKWQueryTask start]_block_invoke.111.cold.1
- ___23-[SPZKWQueryTask start]_block_invoke.119
- ___23-[SPZKWQueryTask start]_block_invoke.120
- ___23-[SPZKWQueryTask start]_block_invoke.124
- ___23-[SPZKWQueryTask start]_block_invoke.124.cold.1
- ___23-[SPZKWQueryTask start]_block_invoke.124.cold.2
- ___23-[SPZKWQueryTask start]_block_invoke.134
- ___30-[SPRecommendationQuery start]_block_invoke.160
- ___31-[SPRecommendationQuery begin:]_block_invoke.103
- ___31-[SPRecommendationQuery begin:]_block_invoke.104
- ___31-[SPRecommendationQuery begin:]_block_invoke.92
- ___31-[SPRecommendationQuery begin:]_block_invoke.92.cold.1
- ___31-[SPRecommendationQuery begin:]_block_invoke.95
- ___34+[SPFederatedQueryTask initialize]_block_invoke.251
- ___39-[SPParsecQuery queryDidFinishLoading:]_block_invoke.107
- ___40-[SPFederatedQueryTask addAndStartQuery]_block_invoke.460
- ___40-[SPFederatedQueryTask addAndStartQuery]_block_invoke_2.465
- ___51-[SPFederatedQueryTask sendFinishedDomains:reason:]_block_invoke.348
- ___51-[SPFederatedQueryTask sendFinishedDomains:reason:]_block_invoke.352
- ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.414
- ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.419
- ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.433
- ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke.167
- ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_2.170
- ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_3.171
- ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_4.172
- ___block_literal_global.109
- ___block_literal_global.121
- ___block_literal_global.147
- ___block_literal_global.204
- ___block_literal_global.256
- ___block_literal_global.293
- ___block_literal_global.314
- ___block_literal_global.321
- ___block_literal_global.325
- ___block_literal_global.339
- ___block_literal_global.401
- ___block_literal_global.409
- ___block_literal_global.422
- ___block_literal_global.435
- ___block_literal_global.487
- ___block_literal_global.511
- ___block_literal_global.514
- ___block_literal_global.529
- ___block_literal_global.86
- ___block_literal_global.90
- ___block_literal_global.91

```
