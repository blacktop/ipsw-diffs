## GPUToolsiOS

> `/System/Library/PrivateFrameworks/GPUToolsiOS.framework/GPUToolsiOS`

```diff

-304.7.0.0.0
+310.8.0.0.0
   __TEXT.__text: 0x2950
   __TEXT.__auth_stubs: 0x2e0
   __TEXT.__objc_methlist: 0x334

   __TEXT.__unwind_info: 0x1b0
   __TEXT.__objc_classname: 0x49
   __TEXT.__objc_methname: 0x782
-  __TEXT.__objc_methtype: 0xd9d
+  __TEXT.__objc_methtype: 0x99c
   __TEXT.__objc_stubs: 0x5a0
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 81035733-252A-358E-9738-CF811EFE7A6E
+  UUID: FB055527-8879-3EC0-9677-70D6038F4E2C
   Functions: 51
   Symbols:   264
   CStrings:  156
Symbols:
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIU8__strongP7CALayerbEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIyU8__strongP7CALayerEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEED1B8ne200100Ev
+ __ZNSt3__113__tree_removeB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZnwmSt19__type_descriptor_t
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIU8__strongP7CALayerbEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIyU8__strongP7CALayerEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
- __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __Znwm
Functions:
~ __ZNSt3__16__treeINS_12__value_typeIyU8__strongP7CALayerEENS_19__map_value_compareIyS5_NS_4lessIyEELb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIyJRKNS_21piecewise_construct_tENS_5tupleIJRKyEEENSH_IJEEEEEENS_4pairINS_15__tree_iteratorIS5_PNS_11__tree_nodeIS5_PvEElEEbEERKT_DpOT0_ : 228 -> 236
~ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_ -> __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIyU8__strongP7CALayerEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEED1B8ne200100Ev : 412 -> 76
~ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIyU8__strongP7CALayerEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_ -> __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_ : 92 -> 412
~ __ZNSt3__16__treeINS_12__value_typeIU8__strongP7CALayerbEENS_19__map_value_compareIS4_S5_NS_4lessIS4_EELb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIS4_JRKNS_21piecewise_construct_tENS_5tupleIJRU8__strongKS3_EEENSH_IJEEEEEENS_4pairINS_15__tree_iteratorIS5_PNS_11__tree_nodeIS5_PvEElEEbEERKT_DpOT0_ : 236 -> 244
~ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIU8__strongP7CALayerbEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_ -> __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIU8__strongP7CALayerbEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEED1B8ne200100Ev : 92 -> 76
~ __ZNSt3__16__treeINS_12__value_typeIP7CALayerbEENS_19__map_value_compareIS4_S5_NS_4lessIS4_EELb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIS4_JRKNS_21piecewise_construct_tENS_5tupleIJRKS3_EEENSH_IJEEEEEENS_4pairINS_15__tree_iteratorIS5_PNS_11__tree_nodeIS5_PvEElEEbEERKT_DpOT0_ : 196 -> 212
CStrings:
+ "{map<CALayer *, bool, std::less<CALayer *>, std::allocator<std::pair<CALayer *const, bool>>>=\"__tree_\"{__tree<std::__value_type<CALayer *, bool>, std::__map_value_compare<CALayer *, std::__value_type<CALayer *, bool>, std::less<CALayer *>>, std::allocator<std::__value_type<CALayer *, bool>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{map<CALayer *__unsafe_unretained, bool, std::less<CALayer *__unsafe_unretained>, std::allocator<std::pair<CALayer *const __unsafe_unretained, bool>>>=\"__tree_\"{__tree<std::__value_type<CALayer *__unsafe_unretained, bool>, std::__map_value_compare<CALayer *__unsafe_unretained, std::__value_type<CALayer *__unsafe_unretained, bool>, std::less<CALayer *__unsafe_unretained>>, std::allocator<std::__value_type<CALayer *__unsafe_unretained, bool>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{map<unsigned long long, CALayer *, std::less<unsigned long long>, std::allocator<std::pair<const unsigned long long, CALayer *>>>=\"__tree_\"{__tree<std::__value_type<unsigned long long, CALayer *>, std::__map_value_compare<unsigned long long, std::__value_type<unsigned long long, CALayer *>, std::less<unsigned long long>>, std::allocator<std::__value_type<unsigned long long, CALayer *>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{map<CALayer *, bool, std::less<CALayer *>, std::allocator<std::pair<CALayer *const, bool>>>=\"__tree_\"{__tree<std::__value_type<CALayer *, bool>, std::__map_value_compare<CALayer *, std::__value_type<CALayer *, bool>, std::less<CALayer *>>, std::allocator<std::__value_type<CALayer *, bool>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<CALayer *, bool>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<CALayer *, std::__value_type<CALayer *, bool>, std::less<CALayer *>>>=\"__value_\"Q}}}"
- "{map<CALayer *__unsafe_unretained, bool, std::less<CALayer *__unsafe_unretained>, std::allocator<std::pair<CALayer *const __unsafe_unretained, bool>>>=\"__tree_\"{__tree<std::__value_type<CALayer *__unsafe_unretained, bool>, std::__map_value_compare<CALayer *__unsafe_unretained, std::__value_type<CALayer *__unsafe_unretained, bool>, std::less<CALayer *__unsafe_unretained>>, std::allocator<std::__value_type<CALayer *__unsafe_unretained, bool>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<CALayer *__unsafe_unretained, bool>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<CALayer *__unsafe_unretained, std::__value_type<CALayer *__unsafe_unretained, bool>, std::less<CALayer *__unsafe_unretained>>>=\"__value_\"Q}}}"
- "{map<unsigned long long, CALayer *, std::less<unsigned long long>, std::allocator<std::pair<const unsigned long long, CALayer *>>>=\"__tree_\"{__tree<std::__value_type<unsigned long long, CALayer *>, std::__map_value_compare<unsigned long long, std::__value_type<unsigned long long, CALayer *>, std::less<unsigned long long>>, std::allocator<std::__value_type<unsigned long long, CALayer *>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<unsigned long long, CALayer *>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<unsigned long long, std::__value_type<unsigned long long, CALayer *>, std::less<unsigned long long>>>=\"__value_\"Q}}}"

```
