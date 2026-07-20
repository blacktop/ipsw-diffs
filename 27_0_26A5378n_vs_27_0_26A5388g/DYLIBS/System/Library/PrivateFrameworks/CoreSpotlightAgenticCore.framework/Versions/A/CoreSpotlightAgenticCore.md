## CoreSpotlightAgenticCore

> `/System/Library/PrivateFrameworks/CoreSpotlightAgenticCore.framework/Versions/A/CoreSpotlightAgenticCore`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
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
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-2451.1.401.0.0
-  __TEXT.__text: 0x40bd20
+2454.100.0.0.0
+  __TEXT.__text: 0x40c59c
   __TEXT.__objc_methlist: 0x1bc
-  __TEXT.__const: 0xaa848
+  __TEXT.__const: 0xaa988
   __TEXT.__constg_swiftt: 0xd920
   __TEXT.__swift5_typeref: 0x1124e
   __TEXT.__swift5_builtin: 0x780
-  __TEXT.__swift5_reflstr: 0x4e66
-  __TEXT.__swift5_fieldmd: 0x12e48
+  __TEXT.__swift5_reflstr: 0x4e76
+  __TEXT.__swift5_fieldmd: 0x12e6c
   __TEXT.__swift5_assocty: 0x48b0
   __TEXT.__swift5_proto: 0x67d0
   __TEXT.__swift5_types: 0x1784
-  __TEXT.__cstring: 0x2a5b9
+  __TEXT.__cstring: 0x2a819
   __TEXT.__swift5_capture: 0x2058
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift_as_entry: 0x49c
   __TEXT.__swift_as_ret: 0x58c
   __TEXT.__swift_as_cont: 0x4c8
-  __TEXT.__swift5_mpenum: 0xbac
+  __TEXT.__swift5_mpenum: 0xb7c
   __TEXT.__oslogstring: 0x175
-  __TEXT.__unwind_info: 0x131a0
-  __TEXT.__eh_frame: 0x193b4
+  __TEXT.__unwind_info: 0x131a8
+  __TEXT.__eh_frame: 0x193bc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x800
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x34e08
+  __AUTH_CONST.__const: 0x34e10
   __AUTH_CONST.__objc_const: 0x1e20
   __AUTH_CONST.__auth_got: 0x1058
   __AUTH.__objc_data: 0x280

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 27435
+  Functions: 27439
   Symbols:   9163
-  CStrings:  2086
+  CStrings:  2090
 
CStrings:
+ "  Combine semanticSimilar AND allText when paraphrase intent is narrowed by a required literal term."
+ "  Use allText alone only when a specific word or name MUST appear literally in the result. To match kMDItemKeywords specifically, use a predicate node with attribute:\"kMDItemKeywords\"."
+ "**Free-form text:** For topic/paraphrase/\"about X\"/\"similar to\" intent, use semanticSimilar — fill `query` with the full NL phrase and `keywords` with content-bearing words (drop particles and prepositions). The keyword fallback is compiled in automatically."
+ "- Literal word that must appear → allText node"
+ "- Semantic/topic intent (\"about X\", paraphrase, \"similar to\") → semanticSimilar(query: full phrase, keywords: key terms)"
+ "Content words for keyword fallback — items without embeddings match via these terms. Extract content-bearing words from the phrase, dropping particles and prepositions."
+ "User's full natural language phrase for embedding-similarity search."
- "**Full-text search:** Use allText node for free-form full-text search across all default-indexed fields (subject, body, displayName, etc. — NOT field-specific). To match kMDItemKeywords specifically, use a predicate node with attribute:\"kMDItemKeywords\"."
- "- Search terms → allText node"
- "Query text for semantic similarity (e.g., 'machine learning research', 'vacation photos', 'budget planning')."
```
