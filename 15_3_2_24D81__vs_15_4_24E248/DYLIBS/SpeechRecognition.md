## SpeechRecognition

> `/System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/SpeechRecognition.framework/Versions/A/SpeechRecognition`

```diff

 6.0.4.0.0
-  __TEXT.__text: 0x5884
+  __TEXT.__text: 0x5870
   __TEXT.__auth_stubs: 0x640
   __TEXT.__gcc_except_tab: 0xfc
   __TEXT.__cstring: 0x18e

   - /System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/Versions/A/SpeechRecognitionCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 90EA193B-5126-3529-B39C-64B1B7A10488
+  UUID: DAA76C7F-FE64-34EC-A2C0-109947AC2603
   Functions: 150
   Symbols:   311
   CStrings:  29
Symbols:
+ __ZNKSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __ZNKSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__113__tree_removeB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
Functions:
~ __Z29StartFeedbackServerConnectionv : 256 -> 248
~ __ZN20OpaqueSRSpeechObject11FindWrapperEPKvP26SRRecognitionSystemWrapper : 288 -> 276
~ _SRGetProperty : 1436 -> 1440
~ ___SRGetProperty_block_invoke : 720 -> 704
~ ___SRNewRecognizer_block_invoke : 304 -> 296
~ _SRGetLanguageModel : 104 -> 108
~ _SRGetIndexedItem : 96 -> 100
~ _SRCountItems : 76 -> 80
~ __ZNSt3__16__treeINS_12__value_typeIPKvP20OpaqueSRSpeechObjectEENS_19__map_value_compareIS3_S6_NS_4lessIS3_EELb1EEENS_9allocatorIS6_EEE14__erase_uniqueIS3_EEmRKT_ : 124 -> 132
~ __ZNSt3__113__tree_removeB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_ -> __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_ : 900 -> 896
~ __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_ -> __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_ : 408 -> 412

```
