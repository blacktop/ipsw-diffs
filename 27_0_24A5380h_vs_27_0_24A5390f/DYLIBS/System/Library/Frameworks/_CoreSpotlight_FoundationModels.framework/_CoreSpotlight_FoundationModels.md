## _CoreSpotlight_FoundationModels

> `/System/Library/Frameworks/_CoreSpotlight_FoundationModels.framework/_CoreSpotlight_FoundationModels`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-2451.1.101.0.0
-  __TEXT.__text: 0x424204
+2454.100.0.0.0
+  __TEXT.__text: 0x4253cc
   __TEXT.__objc_methlist: 0x23c
-  __TEXT.__const: 0xac3f2
-  __TEXT.__constg_swiftt: 0xdf60
-  __TEXT.__swift5_typeref: 0x117fa
+  __TEXT.__const: 0xac512
+  __TEXT.__constg_swiftt: 0xdf6c
+  __TEXT.__swift5_typeref: 0x117f2
   __TEXT.__swift5_builtin: 0x7e4
-  __TEXT.__swift5_reflstr: 0x53d7
-  __TEXT.__swift5_fieldmd: 0x13820
+  __TEXT.__swift5_reflstr: 0x53e7
+  __TEXT.__swift5_fieldmd: 0x13844
   __TEXT.__swift5_assocty: 0x4930
   __TEXT.__swift5_proto: 0x685c
   __TEXT.__swift5_types: 0x1830
-  __TEXT.__cstring: 0x2a6d3
+  __TEXT.__cstring: 0x2a9a3
   __TEXT.__swift5_capture: 0x2124
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift_as_entry: 0x508
   __TEXT.__swift_as_ret: 0x610
   __TEXT.__swift_as_cont: 0x4d4
-  __TEXT.__swift5_mpenum: 0xbe8
+  __TEXT.__swift5_mpenum: 0xbb8
   __TEXT.__oslogstring: 0x175
-  __TEXT.__unwind_info: 0x13790
-  __TEXT.__eh_frame: 0x1a164
+  __TEXT.__unwind_info: 0x137c0
+  __TEXT.__eh_frame: 0x1a16c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x868
+  __DATA_CONST.__objc_selrefs: 0x870
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x36d58
+  __AUTH_CONST.__const: 0x36ce0
   __AUTH_CONST.__objc_const: 0x1e80
-  __AUTH_CONST.__auth_got: 0x1240
+  __AUTH_CONST.__auth_got: 0x1250
   __AUTH.__objc_data: 0x280
-  __AUTH.__data: 0x9c80
+  __AUTH.__data: 0x9d00
   __DATA.__data: 0x11348
   __DATA.__bss: 0xcf960
   __DATA.__common: 0x40

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 27996
-  Symbols:   9381
-  CStrings:  2101
+  Functions: 28007
+  Symbols:   9383
+  CStrings:  2106
 
Symbols:
+ _objc_msgSend$prepare
+ _symbolic SDy_____Say_____GG 13CoreSpotlight23SearchableItemAttributeV AA0cD0V
+ _symbolic Say_____G 13CoreSpotlight14SearchableItemV
+ _symbolic _____ 13CoreSpotlight14SearchableItemV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 13CoreSpotlight14SearchableItemV
- _symbolic SDy_____SaySo16CSSearchableItemCGG 13CoreSpotlight23SearchableItemAttributeV
- _symbolic So16CSSearchableItemC
- _type_layout_string 31_CoreSpotlight_FoundationModels20ScoredSearchableItemV
CStrings:
+ "  Combine via operation when both apply (e.g. paraphrase intent narrowed by a literal name): semanticSimilar AND allText."
+ "  allText — full-text search across default-indexed fields. Use when a specific word, name, or phrase MUST appear literally. To match kMDItemKeywords specifically, use a predicate node with attribute:\"kMDItemKeywords\"."
+ "  semanticSimilar — embedding similarity to a query phrase. Default for topic / paraphrase / \"about X\" / \"similar to\" intent, where the user's words may not appear verbatim in the result. Pass the user's prompt as the query string."
+ "**Free-form text:** Two nodes serve different intents — pick by what the user actually asked for."
+ "- Literal word that must appear → allText node"
+ "- Topic / paraphrase / \"about X\" / \"similar to\" → semanticSimilar node (default for free-form intent)"
+ "Content words for keyword fallback — items without embeddings match via these terms. Extract content-bearing words from the phrase, dropping particles and prepositions."
+ "User's full natural language phrase for embedding-similarity search."
- "**Full-text search:** Use allText node for free-form full-text search across all default-indexed fields (subject, body, displayName, etc. — NOT field-specific). To match kMDItemKeywords specifically, use a predicate node with attribute:\"kMDItemKeywords\"."
- "- Search terms → allText node"
- "Query text for semantic similarity (e.g., 'machine learning research', 'vacation photos', 'budget planning')."
```
