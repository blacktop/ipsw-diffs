## PerfPowerServicesSignpostReader

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerServicesSignpostReader.xpc/PerfPowerServicesSignpostReader`

```diff

-2964.42.2.0.0
-  __TEXT.__text: 0xaac8
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_stubs: 0x1b40
-  __TEXT.__objc_methlist: 0x5a0
-  __TEXT.__const: 0xe0
+2964.60.10.0.0
+  __TEXT.__text: 0xba64
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_stubs: 0x1c40
+  __TEXT.__objc_methlist: 0x600
+  __TEXT.__const: 0xf0
   __TEXT.__oslogstring: 0xa12
-  __TEXT.__cstring: 0xbf9
-  __TEXT.__objc_methname: 0x1bfc
-  __TEXT.__objc_classname: 0x85
-  __TEXT.__objc_methtype: 0x258
-  __TEXT.__gcc_except_tab: 0x31c
-  __TEXT.__unwind_info: 0x228
-  __DATA_CONST.__auth_got: 0x2a8
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x388
-  __DATA_CONST.__cfstring: 0x1260
-  __DATA_CONST.__objc_classlist: 0x20
+  __TEXT.__cstring: 0xc38
+  __TEXT.__objc_methname: 0x1c9a
+  __TEXT.__objc_classname: 0xa9
+  __TEXT.__objc_methtype: 0x7b1
+  __TEXT.__gcc_except_tab: 0x490
+  __TEXT.__unwind_info: 0x2e8
+  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__const: 0x3b0
+  __DATA_CONST.__cfstring: 0x1280
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x8e0
-  __DATA.__objc_selrefs: 0x888
-  __DATA.__objc_ivar: 0x7c
-  __DATA.__objc_data: 0x140
+  __DATA.__objc_const: 0x9b8
+  __DATA.__objc_selrefs: 0x8c8
+  __DATA.__objc_ivar: 0x84
+  __DATA.__objc_data: 0x190
   __DATA.__data: 0x120
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: BE492A47-806D-346F-81EA-C6F7F86A161F
-  Functions: 160
-  Symbols:   158
-  CStrings:  748
+  UUID: D3B57B24-8A90-3621-8DD6-89571DF6ADEC
+  Functions: 186
+  Symbols:   178
+  CStrings:  765
 
Symbols:
+ _OBJC_CLASS_$_XPCSignpostReaderGlitchAggregator
+ _OBJC_METACLASS_$_XPCSignpostReaderGlitchAggregator
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorD1Ev
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZNSt3__112__next_primeEm
+ __ZSt9terminatev
+ __ZTISt12length_error
+ __ZTISt20bad_array_new_length
+ __ZTVSt12length_error
+ __ZdlPv
+ __ZnwmSt19__type_descriptor_t
+ ___cxa_allocate_exception
+ ___cxa_begin_catch
+ ___cxa_free_exception
+ ___cxa_throw
+ ___gxx_personality_v0
+ _memcpy
+ _memmove
CStrings:
+ ".cxx_construct"
+ "@\"XPCSignpostReaderGlitchAggregator\""
+ "T@\"XPCSignpostReaderGlitchAggregator\",&,V_glitchAggregator"
+ "XPCSignpostReaderGlitchAggregator"
+ "_glitchAggregator"
+ "_pendingSignpostAnimations"
+ "_processedAnimationSummaries"
+ "_updateIntervalsForBundle:"
+ "_updateIntervalsIfNeededForBundle:"
+ "addAnimationInterval:forBundle:"
+ "copy"
+ "durationMs"
+ "firstObject"
+ "glitchAggregator"
+ "lastObject"
+ "normalizedGlitchScores"
+ "percentBadAnimations"
+ "setGlitchAggregator:"
+ "v32@?0@\"NSString\"8@\"NSArray\"16^B24"
+ "vector"
+ "{unordered_map<NSString *, std::vector<_Animation>, std::hash<NSString *>, std::equal_to<NSString *>, std::allocator<std::pair<NSString *const, std::vector<_Animation>>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSString *, std::vector<_Animation>>, std::__unordered_map_hasher<NSString *, std::__hash_value_type<NSString *, std::vector<_Animation>>, std::hash<NSString *>, std::equal_to<NSString *>>, std::__unordered_map_equal<NSString *, std::__hash_value_type<NSString *, std::vector<_Animation>>, std::equal_to<NSString *>, std::hash<NSString *>>, std::allocator<std::__hash_value_type<NSString *, std::vector<_Animation>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, std::vector<_Animation>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, std::vector<_Animation>>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, std::vector<_Animation>>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, std::vector<_Animation>>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "T@\"NSMutableDictionary\",&,V_uniqueAnimationIntervalsByProcess"
- "_uniqueAnimationIntervalsByProcess"
- "initWithArray:"
- "setUniqueAnimationIntervalsByProcess:"
- "uniqueAnimationIntervalsByProcess"

```
