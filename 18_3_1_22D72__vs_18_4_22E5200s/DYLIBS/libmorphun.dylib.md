## libmorphun.dylib

> `/usr/lib/libmorphun.dylib`

```diff

-3402.12.1.0.0
-  __TEXT.__text: 0x120340
-  __TEXT.__auth_stubs: 0xf10
-  __TEXT.__gcc_except_tab: 0x1634c
-  __TEXT.__const: 0x15230c
-  __TEXT.__ustring: 0xfb1c
-  __TEXT.__cstring: 0x27a9
+3404.47.1.0.0
+  __TEXT.__text: 0x124ff4
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__const: 0x152470
+  __TEXT.__gcc_except_tab: 0x1686c
+  __TEXT.__ustring: 0xf66e
+  __TEXT.__cstring: 0x282b
   __TEXT.__oslogstring: 0x62
-  __TEXT.__unwind_info: 0x66c0
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__unwind_info: 0x6640
+  __DATA_CONST.__got: 0x120
   __DATA_CONST.__const: 0x12400
-  __AUTH_CONST.__auth_got: 0x790
+  __AUTH_CONST.__auth_got: 0x788
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x20440
+  __AUTH_CONST.__const: 0x20400
   __AUTH_CONST.__cfstring: 0x60
   __DATA.__data: 0x308
-  __DATA.__bss: 0x13c0
-  __DATA_DIRTY.__bss: 0x328
+  __DATA.__bss: 0x1180
+  __DATA_DIRTY.__bss: 0x548
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libgermantok.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libmecab.dylib
-  Functions: 3823
-  Symbols:   4716
-  CStrings:  250
+  Functions: 3829
+  Symbols:   4784
+  CStrings:  249
 
Symbols:
+ __ZN7morphun6dialog14PronounConcept13getMatchStateERKNSt3__13mapIPKNS0_15SemanticFeatureENS2_12basic_stringIDsNS2_11char_traitsIDsEENS2_9allocatorIDsEEEENS1_8ptr_lessIS4_EENSA_INS2_4pairIKS6_SC_EEEEEERS5_RKSC_
+ __ZN7morphun6dialog14PronounConcept14getPronounDataERKNS0_20SemanticFeatureModelE
+ __ZN7morphun6dialog14PronounConcept18PRONOUN_DATA_CACHEEv
+ __ZN7morphun6dialog14PronounConcept25createPronounDataForModelERKNS0_20SemanticFeatureModelEPKDs
+ __ZN7morphun6dialog14PronounConcept25getFeatureValueForPronounERKNSt3__13mapIPKNS0_15SemanticFeatureENS2_12basic_stringIDsNS2_11char_traitsIDsEENS2_9allocatorIDsEEEENS1_8ptr_lessIS4_EENSA_INS2_4pairIKS6_SC_EEEEEERS5_
+ __ZN7morphun8analysis20ConfigurableAnalyzer15splitDelimitersEiiRPNS_5TokenEPKS2_PKNS_5ChunkE
+ __ZNK7morphun10dictionary18DictionaryMetaData17getKnownWordsSizeEv
+ __ZNK7morphun10dictionary36DictionaryMetaData_MMappedDictionary15getAllWordsSizeEv
+ __ZNK7morphun6dialog14PronounConcept13isCustomMatchEv
+ __ZNK7morphun6dialog14PronounConcept15getCurrentValueEPKNS0_26SemanticFeatureConceptBaseEbb
+ __ZNK7morphun6dialog14PronounConcept21getFirstPossibleValueEPKNS0_26SemanticFeatureConceptBaseEbb
+ __ZNSt19bad_optional_accessD1Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTISt19bad_optional_access
+ __ZTVNSt3__117bad_function_callE
+ __ZTVSt19bad_optional_access
+ _mpron_isCustomMatch
+ _u_strFromUTF8WithSub
+ _ucnv_getType
+ _uregex_findNext
+ _uregex_start
- __ZN7morphun8analysis20ConfigurableAnalyzer15splitDelimitersEiiiRPNS_5TokenEPKS2_PKNS_5ChunkE
- __ZNK7morphun6dialog14PronounConcept15getCurrentValueEPKNS0_26SemanticFeatureConceptBaseEb
- __ZNK7morphun6dialog14PronounConcept21getFirstPossibleValueEPKNS0_26SemanticFeatureConceptBaseEb
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5rfindEcm
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- __ZNKSt9exception4whatEv
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKc
- __ZNSt3__19to_stringEi
- _u_strFromUTF8
- _uset_addAllCodePoints
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:149: MARISA_STATE_ERROR: trie_.get() == NULL"
+ "3404.47"
- "3402.12"
- "cmn"
- "iw"

```
