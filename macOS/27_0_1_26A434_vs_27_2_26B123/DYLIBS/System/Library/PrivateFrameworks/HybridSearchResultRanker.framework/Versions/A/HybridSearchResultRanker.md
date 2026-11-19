## HybridSearchResultRanker

> `/System/Library/PrivateFrameworks/HybridSearchResultRanker.framework/Versions/A/HybridSearchResultRanker`

```diff

-67.0.0.0.0
-  __TEXT.__text: 0xbc4bc
-  __TEXT.__const: 0x43c8
-  __TEXT.__oslogstring: 0x3bc6
+73.3.4.0.0
+  __TEXT.__text: 0xbd94c
+  __TEXT.__const: 0x43f8
+  __TEXT.__oslogstring: 0x3d06
   __TEXT.__swift5_typeref: 0x21ae
-  __TEXT.__swift5_reflstr: 0x1e66
+  __TEXT.__swift5_reflstr: 0x1f06
   __TEXT.__swift5_assocty: 0x140
   __TEXT.__constg_swiftt: 0xec8
-  __TEXT.__swift5_fieldmd: 0x22a4
+  __TEXT.__swift5_fieldmd: 0x22e0
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_proto: 0x210
   __TEXT.__swift5_types: 0x1a4
   __TEXT.__swift_as_entry: 0xf4
   __TEXT.__swift_as_ret: 0x10c
   __TEXT.__swift_as_cont: 0x1cc
-  __TEXT.__cstring: 0x1db4
-  __TEXT.__swift5_capture: 0x1490
+  __TEXT.__cstring: 0x1ed4
+  __TEXT.__swift5_capture: 0x14c0
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1e28
-  __TEXT.__eh_frame: 0x3e48
+  __TEXT.__unwind_info: 0x1e78
+  __TEXT.__eh_frame: 0x3ef0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x170
+  __DATA_CONST.__objc_selrefs: 0x178
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x6888
+  __AUTH_CONST.__const: 0x6948
   __AUTH_CONST.__objc_const: 0x1b0
-  __AUTH_CONST.__auth_got: 0x11b8
-  __AUTH_CONST.__auth_ptr: 0x5a8
-  __AUTH.__data: 0xde8
-  __DATA.__data: 0x1378
-  __DATA.__bss: 0x41d0
-  __DATA.__common: 0x38
+  __AUTH_CONST.__auth_got: 0x11c0
+  __AUTH_CONST.__auth_ptr: 0x5b0
+  __AUTH.__data: 0x730
+  __DATA.__data: 0x9a0
+  __DATA.__bss: 0x3ed0
+  __DATA_DIRTY.__data: 0x1090
+  __DATA_DIRTY.__bss: 0x300
+  __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4140
+  Functions: 4166
   Symbols:   151
-  CStrings:  277
+  CStrings:  286
 
CStrings:
+ "Biome RankerEvent donation attempted: items=%{public}ld section=%{public}ld rankingMs=%{public}lld"
+ "CLIFF DETECTION SKIPPED: contact-resolution boost active — all %ld candidates are tophits"
+ "MailL2RankingBiomeRankerEventDonationEnabled"
+ "MailL2RankingContactResolutionBoostEnabled"
+ "MailL2RankingMaxBiomeRankedItemsToEmit"
+ "MailL2RankingTophitCandidatePoolMultiplier"
+ "contact-resolution boost"
+ "contact_resolution_boost"
+ "unwanted_category"
+ "╟───────────────────────────────────────────────────────────────\n║ Total L1 Results (all scopes): %ld\n╠═══════════════════════════════════════════════════════════════\n║ Ranking Configuration:\n║   L2 Ranking: %s\n║   Temporal: %s\n║   Query Match: %s\n║   Engagement: %s\n║   Structural: %s\n║   Quality: %s\n║   Body Matching: %s\n║   Person Query Ranking: %s\n║   Contact Resolution Boost: %s\n║   Time-Sensitive Query Boost: %s\n╚═══════════════════════════════════════════════════════════════"
+ "╟───────────────────────────────────────────────────────────────\n║ Total L1 Results: %ld\n║ Query Limit: %ld\n║ Query Tophit Limit: %ld\n╠═══════════════════════════════════════════════════════════════\n║ Ranking Configuration:\n║   L2 Ranking: %s\n║   Temporal: %s\n║   Query Match: %s\n║   Engagement: %s\n║   Structural: %s\n║   Quality: %s\n║   Body Matching: %s\n║   Person Query Ranking: %s\n║   Contact Resolution Boost: %s\n║   Time-Sensitive Query Boost: %s\n╚═══════════════════════════════════════════════════════════════"
+ "╠═══════════════════════════════════════════════════════════════\n║ Ranking Configuration:\n║   L2 Ranking: %s\n║   Temporal: %s\n║   Query Match: %s\n║   Engagement: %s\n║   Structural: %s\n║   Quality: %s\n║   Body Matching: %s\n║   Person Query Ranking: %s\n║   Contact Resolution Boost: %s\n║   Time-Sensitive Query Boost: %s\n╚═══════════════════════════════════════════════════════════════"
- "╟───────────────────────────────────────────────────────────────\n║ Total L1 Results (all scopes): %ld\n╠═══════════════════════════════════════════════════════════════\n║ Ranking Configuration:\n║   L2 Ranking: %s\n║   Temporal: %s\n║   Query Match: %s\n║   Engagement: %s\n║   Structural: %s\n║   Quality: %s\n║   Body Matching: %s\n║   Person Query Ranking: %s\n║   Time-Sensitive Query Boost: %s\n╚═══════════════════════════════════════════════════════════════"
- "╟───────────────────────────────────────────────────────────────\n║ Total L1 Results: %ld\n║ Query Limit: %ld\n║ Query Tophit Limit: %ld\n╠═══════════════════════════════════════════════════════════════\n║ Ranking Configuration:\n║   L2 Ranking: %s\n║   Temporal: %s\n║   Query Match: %s\n║   Engagement: %s\n║   Structural: %s\n║   Quality: %s\n║   Body Matching: %s\n║   Person Query Ranking: %s\n║   Time-Sensitive Query Boost: %s\n╚═══════════════════════════════════════════════════════════════"
- "╠═══════════════════════════════════════════════════════════════\n║ Ranking Configuration:\n║   L2 Ranking: %s\n║   Temporal: %s\n║   Query Match: %s\n║   Engagement: %s\n║   Structural: %s\n║   Quality: %s\n║   Body Matching: %s\n║   Person Query Ranking: %s\n║   Time-Sensitive Query Boost: %s\n╚═══════════════════════════════════════════════════════════════"
```
