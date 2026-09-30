## SiriOntology

> `/System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology`

```diff

 3500.45.1.0.0
-  __TEXT.__text: 0x44ca98
+  __TEXT.__text: 0x44caac
   __TEXT.__auth_stubs: 0x1af0
   __TEXT.__objc_methlist: 0x26e8
   __TEXT.__const: 0x4e498

   __TEXT.__unwind_info: 0x15708
   __TEXT.__eh_frame: 0x61b8
   __TEXT.__objc_classname: 0x4e8
-  __TEXT.__objc_methname: 0x458c
-  __TEXT.__objc_methtype: 0x16bd
+  __TEXT.__objc_methname: 0x4590
+  __TEXT.__objc_methtype: 0x170f
   __TEXT.__objc_stubs: 0x1d80
   __DATA_CONST.__got: 0x570
   __DATA_CONST.__const: 0x1f60

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 5B178148-1562-3F57-B5E7-39E41F80D301
+  UUID: B698EF78-0B0B-3135-B184-0BD021FE9E9D
   Functions: 40132
   Symbols:   24144
   CStrings:  10460
Functions:
~ -[USOEntityNode addEntitySpan:] : 6124 -> 6136
~ __ZNSt3__16vectorIN5boost6detail12adj_list_genINS1_14adjacency_listINS1_4vecSES5_NS1_14bidirectionalSEPN4siri8ontology12UsoGraphNodeENS8_12UsoGraphEdgeENS1_11no_propertyENS1_5listSEEES5_S5_S6_SA_SB_SC_SD_E6config13stored_vertexENS_9allocatorISH_EEE24__emplace_back_slow_pathIJSH_EEEPSH_DpOT_ : 352 -> 356
~ __ZNSt3__16vectorIN5boost6detail12adj_list_genINS1_14adjacency_listINS1_4vecSES5_NS1_14bidirectionalSEPN4siri8ontology12UsoGraphNodeENS8_12UsoGraphEdgeENS1_11no_propertyENS1_5listSEEES5_S5_S6_SA_SB_SC_SD_E6config13stored_vertexENS_9allocatorISH_EEE6resizeEm : 420 -> 424
~ __ZN4siri8ontology13UsoEntityNode21addUtteranceAlignmentERNS0_21UsoUtteranceAlignmentE : 468 -> 472
~ __ZNSt3__16vectorINS_10unique_ptrIN4siri8ontology14AsrAlternativeENS_14default_deleteIS4_EEEENS_9allocatorIS7_EEE9push_backB8ne200100EOS7_ : 248 -> 256
~ __ZNSt3__16vectorINS_10unique_ptrIN4siri8ontology12SpanPropertyENS_14default_deleteIS4_EEEENS_9allocatorIS7_EEE9push_backB8ne200100EOS7_ : 248 -> 256
~ __ZNSt3__16vectorINS_10unique_ptrIN4siri8ontology13UsoIdentifierENS_14default_deleteIS4_EEEENS_9allocatorIS7_EEE9push_backB8ne200100EOS7_ : 248 -> 256
~ __ZN4siri8ontology17PrintGraphVisitor9tree_edgeEN5boost6detail14edge_desc_implINS2_17bidirectional_tagEmEERKNS2_14adjacency_listINS2_4vecSES8_NS2_14bidirectionalSEPNS0_12UsoGraphNodeENS0_12UsoGraphEdgeENS2_11no_propertyENS2_5listSEEE : 4120 -> 4108
~ __ZNK4siri8ontology8UsoGraph35prettyPrintSortedUsoGraphAlignmentsEv : 3232 -> 3240
~ __ZN4siri8ontology13UsoEntityNode21addUtteranceAlignmentEjjjjjNSt3__18optionalIiEES4_ : 528 -> 532
~ __ZN4siri8ontology13UsoEntityNode21addUtteranceAlignmentEjjj : 508 -> 512
~ __ZN4siri8ontology13UsoEntityNode21addUtteranceAlignmentENSt3__110unique_ptrINS0_21UsoUtteranceAlignmentENS2_14default_deleteIS4_EEEE : 288 -> 292
~ __ZN4siri8ontology15UsoVocabManagerC2ERKNSt3__16vectorIPKNS0_16OntologyUnitNameENS2_9allocatorIS6_EEEERKNS0_15OntologyVersionE : 2372 -> 2364
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN4siri8ontology16OntologyUnitNameENS_14default_deleteISB_EEEEEENS_22__unordered_map_hasherIS7_SF_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SF_SK_SI_Lb1EEENS5_ISF_EEE25__emplace_unique_key_argsIS7_JS7_NS8_INSA_16OntologyNodeNameENSC_ISR_EEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeISF_PvEEEEbEERKT_DpOT0_ : 640 -> 636
~ __ZN4siri8ontology15UsoVocabManager20createCustomVerbNameENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE : 1724 -> 1704
~ __ZN4siri8ontology15UsoVocabManager20createCustomEdgeNameENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE : 1192 -> 1172
~ __ZNSt3__112__hash_tableINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS6_EENS_8equal_toIS6_EENS4_IS6_EEE25__emplace_unique_key_argsIS6_JRKS6_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_ : 1104 -> 1100
~ +[USOObjCGraphRedactionUtils getRedactedEntitySpan:isContactRelatedEntityNode:] : 3332 -> 3344
~ -[USOSerializedGraph toCppUsoGraph:withError:] : 7676 -> 7684
CStrings:
+ "@24@0:8{unique_ptr<siri::ontology::UsoGraph, std::default_delete<siri::ontology::UsoGraph>>={?=^{UsoGraph}}}16"
+ "@40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16"
+ "T{unique_ptr<siri::ontology::UsoGraph, std::default_delete<siri::ontology::UsoGraph>>={?=^{UsoGraph}}},N"
+ "v24@0:8{unique_ptr<siri::ontology::UsoGraph, std::default_delete<siri::ontology::UsoGraph>>={?=^{UsoGraph}}}16"
+ "v88@0:8^v16@24@32^{UsoGraphNode=^^?^{UsoGraph}Q}40{vector<std::pair<std::reference_wrapper<siri::ontology::UsoGraphNode>, std::reference_wrapper<const siri::ontology::UsoGraphEdge>>, std::allocator<std::pair<std::reference_wrapper<siri::ontology::UsoGraphNode>, std::reference_wrapper<const siri::ontology::UsoGraphEdge>>>>=^v^v{?=^v}}48{shared_ptr<siri::ontology::UsoVocabManager>=^{UsoVocabManager}^{__shared_weak_count}}72"
+ "{unique_ptr<siri::ontology::UsoEntitySpan, std::default_delete<siri::ontology::UsoEntitySpan>>={?=^{UsoEntitySpan}}}16@0:8"
+ "{unique_ptr<siri::ontology::UsoEntitySpan, std::default_delete<siri::ontology::UsoEntitySpan>>={?=^{UsoEntitySpan}}}204@0:8{UsoEntitySpan={optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}})B}{optional<siri::ontology::UsoEntitySpan::SpanSource>=(?=ci)B}{optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}})B}{optional<std::unique_ptr<siri::ontology::MatchInfo>>=(?=c{unique_ptr<siri::ontology::MatchInfo, std::default_delete<siri::ontology::MatchInfo>>={?=^{MatchInfo}}})B}{vector<std::unique_ptr<siri::ontology::SpanProperty>, std::allocator<std::unique_ptr<siri::ontology::SpanProperty>>>=^v^v{?=^v}}{optional<unsigned int>=(?=cI)B}{optional<unsigned int>=(?=cI)B}{vector<std::unique_ptr<siri::ontology::AsrAlternative>, std::allocator<std::unique_ptr<siri::ontology::AsrAlternative>>>=^v^v{?=^v}}{optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}})B}}16B200"
+ "{unique_ptr<siri::ontology::UsoGraph, std::default_delete<siri::ontology::UsoGraph>>=\"\"{?=\"__ptr_\"^{UsoGraph}}}"
+ "{unique_ptr<siri::ontology::UsoGraph, std::default_delete<siri::ontology::UsoGraph>>={?=^{UsoGraph}}}16@0:8"
+ "{unique_ptr<siri::ontology::UsoGraph, std::default_delete<siri::ontology::UsoGraph>>={?=^{UsoGraph}}}40@0:8{shared_ptr<siri::ontology::UsoVocabManager>=^{UsoVocabManager}^{__shared_weak_count}}16^@32"
+ "{unique_ptr<siri::ontology::UsoIdentifier, std::default_delete<siri::ontology::UsoIdentifier>>={?=^{UsoIdentifier}}}140@0:8{UsoIdentifier={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}})B}{optional<double>=(?=cd)B}{optional<siri::ontology::UsoIdentifier::NluComponent>=(?=ci)B}{optional<unsigned int>=(?=cI)B}{optional<unsigned int>=(?=cI)B}}16B136"
+ "{unique_ptr<siri::ontology::UsoIdentifier, std::default_delete<siri::ontology::UsoIdentifier>>={?=^{UsoIdentifier}}}16@0:8"
- "@24@0:8{unique_ptr<siri::ontology::UsoGraph, std::default_delete<siri::ontology::UsoGraph>>=^{UsoGraph}}16"
- "@40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16"
- "T{unique_ptr<siri::ontology::UsoGraph, std::default_delete<siri::ontology::UsoGraph>>=^{UsoGraph}},N"
- "v24@0:8{unique_ptr<siri::ontology::UsoGraph, std::default_delete<siri::ontology::UsoGraph>>=^{UsoGraph}}16"
- "v88@0:8^v16@24@32^{UsoGraphNode=^^?^{UsoGraph}Q}40{vector<std::pair<std::reference_wrapper<siri::ontology::UsoGraphNode>, std::reference_wrapper<const siri::ontology::UsoGraphEdge>>, std::allocator<std::pair<std::reference_wrapper<siri::ontology::UsoGraphNode>, std::reference_wrapper<const siri::ontology::UsoGraphEdge>>>>=^v^v^v}48{shared_ptr<siri::ontology::UsoVocabManager>=^{UsoVocabManager}^{__shared_weak_count}}72"
- "{unique_ptr<siri::ontology::UsoEntitySpan, std::default_delete<siri::ontology::UsoEntitySpan>>=^{UsoEntitySpan}}16@0:8"
- "{unique_ptr<siri::ontology::UsoEntitySpan, std::default_delete<siri::ontology::UsoEntitySpan>>=^{UsoEntitySpan}}204@0:8{UsoEntitySpan={optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})})B}{optional<siri::ontology::UsoEntitySpan::SpanSource>=(?=ci)B}{optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})})B}{optional<std::unique_ptr<siri::ontology::MatchInfo>>=(?=c{unique_ptr<siri::ontology::MatchInfo, std::default_delete<siri::ontology::MatchInfo>>=^{MatchInfo}})B}{vector<std::unique_ptr<siri::ontology::SpanProperty>, std::allocator<std::unique_ptr<siri::ontology::SpanProperty>>>=^v^v^v}{optional<unsigned int>=(?=cI)B}{optional<unsigned int>=(?=cI)B}{vector<std::unique_ptr<siri::ontology::AsrAlternative>, std::allocator<std::unique_ptr<siri::ontology::AsrAlternative>>>=^v^v^v}{optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})})B}}16B200"
- "{unique_ptr<siri::ontology::UsoGraph, std::default_delete<siri::ontology::UsoGraph>>=\"__ptr_\"^{UsoGraph}}"
- "{unique_ptr<siri::ontology::UsoGraph, std::default_delete<siri::ontology::UsoGraph>>=^{UsoGraph}}16@0:8"
- "{unique_ptr<siri::ontology::UsoGraph, std::default_delete<siri::ontology::UsoGraph>>=^{UsoGraph}}40@0:8{shared_ptr<siri::ontology::UsoVocabManager>=^{UsoVocabManager}^{__shared_weak_count}}16^@32"
- "{unique_ptr<siri::ontology::UsoIdentifier, std::default_delete<siri::ontology::UsoIdentifier>>=^{UsoIdentifier}}140@0:8{UsoIdentifier={basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}{optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})})B}{optional<double>=(?=cd)B}{optional<siri::ontology::UsoIdentifier::NluComponent>=(?=ci)B}{optional<unsigned int>=(?=cI)B}{optional<unsigned int>=(?=cI)B}}16B136"
- "{unique_ptr<siri::ontology::UsoIdentifier, std::default_delete<siri::ontology::UsoIdentifier>>=^{UsoIdentifier}}16@0:8"

```
