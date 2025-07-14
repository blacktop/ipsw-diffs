## Metal

> `/System/Library/Frameworks/Metal.framework/Metal`

```diff

-341.29.1.0.0
-  __TEXT.__text: 0x15add8
+341.35.0.0.0
+  __TEXT.__text: 0x15cf7c
   __TEXT.__auth_stubs: 0x18f0
-  __TEXT.__objc_methlist: 0x12928
-  __TEXT.__gcc_except_tab: 0x544c
+  __TEXT.__objc_methlist: 0x12958
+  __TEXT.__gcc_except_tab: 0x55f8
   __TEXT.__const: 0x1beb0
-  __TEXT.__cstring: 0x1c421
+  __TEXT.__cstring: 0x1c450
   __TEXT.__oslogstring: 0x133c
   __TEXT.__ustring: 0x1be
   __TEXT.text_env: 0x25b0
-  __TEXT.__unwind_info: 0x5f48
-  __TEXT.__eh_frame: 0x1b4
+  __TEXT.__unwind_info: 0x600c
+  __TEXT.__eh_frame: 0x1c8
   __TEXT.__objc_classname: 0x2fbb
-  __TEXT.__objc_methname: 0x2aaaa
+  __TEXT.__objc_methname: 0x2ac0e
   __TEXT.__objc_methtype: 0x166fb
-  __TEXT.__objc_stubs: 0x11fc0
+  __TEXT.__objc_stubs: 0x12000
   __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__const: 0x2bf8
   __DATA_CONST.__objc_classlist: 0xa20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x32860
-  __DATA_CONST.__objc_selrefs: 0x6d78
+  __DATA_CONST.__objc_const: 0x32920
+  __DATA_CONST.__objc_selrefs: 0x6d98
   __AUTH_CONST.__objc_const: 0x74f8
-  __AUTH_CONST.__cfstring: 0x10340
+  __AUTH_CONST.__cfstring: 0x10360
   __AUTH_CONST.__const: 0x2ee8
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH.__objc_data: 0x2b70
   __DATA.__got_weak: 0x8
   __DATA.__objc_protorefs: 0x50
-  __DATA.__objc_classrefs: 0x8c0
+  __DATA.__objc_classrefs: 0x8c8
   __DATA.__objc_superrefs: 0x928
-  __DATA.__objc_ivar: 0x18cc
+  __DATA.__objc_ivar: 0x18d8
   __DATA.__data: 0x2f08
   __DATA.__bss: 0x188
   __DATA.__common: 0x28

   __DATA_DIRTY.__bss: 0x170
   __DATA_DIRTY.__common: 0x19
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface

   - /usr/lib/libcompression.dylib
   - /usr/lib/libllvm-flatbuffers.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BC8595C0-3E62-39C5-B4B5-3ADE76F5AF41
-  Functions: 9810
-  Symbols:   28125
-  CStrings:  12844
+  UUID: 8092CD07-6A8D-3415-A8F7-C840E44805B8
+  Functions: 9837
+  Symbols:   28195
+  CStrings:  12857
 
Symbols:
+ -[MTLArrayTypeInternal formattedDescription:withPrintedTypes:]
+ -[MTLBindingInternal formattedDescription:withPrintedTypes:]
+ -[MTLIndirectConstantArgument formattedDescription:withPrintedTypes:]
+ -[MTLInferredInput formattedDescription:withPrintedTypes:]
+ -[MTLPointerTypeInternal formattedDescription:withPrintedTypes:]
+ -[MTLPostVertexDumpOutput formattedDescription:withPrintedTypes:]
+ -[MTLStructMemberInternal formattedDescription:withPrintedTypes:]
+ -[MTLStructTypeInternal formattedDescription:withPrintedTypes:]
+ -[MTLTextureReferenceTypeInternal formattedDescription:withPrintedTypes:]
+ -[MTLTypeInternal formattedDescription:withPrintedTypes:]
+ -[_MTLDevice areWritableHeapsEnabled]
+ -[_MTLDevice setWritableHeapsEnabled:]
+ GCC_except_table127
+ GCC_except_table159
+ GCC_except_table160
+ GCC_except_table697
+ GCC_except_table700
+ GCC_except_table705
+ GCC_except_table79
+ _OBJC_CLASS_$_LSExtensionPointRecord
+ _OBJC_IVAR_$_MTLGPUBVHBuilder.KERNEL_INDEX_INITIALIZE_DEBUG_FRAGMENT_INDICES
+ _OBJC_IVAR_$__MTLDevice._isPlugin
+ _OBJC_IVAR_$__MTLDevice._writableHeapsEnabled
+ __ZL19deserializeArgumentPU23objcproto12MTLDeviceSPI11objc_objectPKN13AirReflection6NodeIdEPKN11flatbuffers6VectorINS5_6OffsetINS1_4NodeEEEEER28ReflectionDeserializeContextPP18MTLBindingInternal
+ __ZL20deserializeArgumentsPU23objcproto12MTLDeviceSPI11objc_objectPKN11flatbuffers6VectorIPKN13AirReflection6NodeIdEEEPKNS2_INS1_6OffsetINS3_4NodeEEEEER28ReflectionDeserializeContextRPP18MTLBindingInternalbPj
+ __ZL25deserializeGlobalBindingsPU23objcproto12MTLDeviceSPI11objc_objectPKN11flatbuffers6VectorIPKN13AirReflection6NodeIdEEER28ReflectionDeserializeContextPKNS2_INS1_6OffsetINS3_4NodeEEEEERPP18MTLBindingInternal
+ __ZL25deserializeStructArgumentPU23objcproto12MTLDeviceSPI11objc_objectPKN13AirReflection6NodeIdEPKN11flatbuffers6VectorINS5_6OffsetINS1_4NodeEEEEER28ReflectionDeserializeContextPb
+ __ZN12ContextStackC1E15MTLFunctionTypeb
+ __ZN12ContextStackD2Ev
+ __ZN28ReflectionDeserializeContext14getStructForIdEm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP21MTLStructTypeInternalEENS_22__unordered_map_hasherImS4_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP21MTLStructTypeInternalEENS_22__unordered_map_hasherImS4_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE13__move_assignERSF_NS_17integral_constantIbLb1EEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP21MTLStructTypeInternalEENS_22__unordered_map_hasherImS4_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE25__emplace_unique_key_argsImJNS_4pairIKmS3_EEEEENSH_INS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP21MTLStructTypeInternalEENS_22__unordered_map_hasherImS4_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE25__emplace_unique_key_argsImJRKNS_4pairIKmS3_EEEEENSH_INS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP21MTLStructTypeInternalEENS_22__unordered_map_hasherImS4_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE4findImEENS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP21MTLStructTypeInternalEENS_22__unordered_map_hasherImS4_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP21MTLStructTypeInternalEENS_22__unordered_map_hasherImS4_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP21MTLStructTypeInternalEENS_22__unordered_map_hasherImS4_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS4_S9_S7_Lb1EEENS_9allocatorIS4_EEED2Ev
+ __ZNSt3__113unordered_mapImP21MTLStructTypeInternalNS_4hashImEENS_8equal_toImEENS_9allocatorINS_4pairIKmS2_EEEEEC2ERKSC_
+ __ZNSt3__114__split_bufferIP12ContextStackNS_9allocatorIS2_EEE10push_frontEOS2_
+ __ZNSt3__114__split_bufferIP12ContextStackNS_9allocatorIS2_EEE9push_backEOS2_
+ __ZNSt3__114__split_bufferIP12ContextStackNS_9allocatorIS2_EEED2Ev
+ __ZNSt3__114__split_bufferIP12ContextStackRNS_9allocatorIS2_EEE10push_frontERKS2_
+ __ZNSt3__114__split_bufferIP12ContextStackRNS_9allocatorIS2_EEE9push_backEOS2_
+ __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIP12ContextStackEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__15dequeI12ContextStackNS_9allocatorIS1_EEE19__add_back_capacityEv
+ __ZNSt3__15dequeI12ContextStackNS_9allocatorIS1_EEE25__maybe_remove_back_spareB7v160006Eb
+ __ZNSt3__15dequeI12ContextStackNS_9allocatorIS1_EEE8pop_backEv
+ __ZNSt3__15dequeI12ContextStackNS_9allocatorIS1_EEE9push_backEOS1_
+ __ZNSt3__15dequeI12ContextStackNS_9allocatorIS1_EEED2B7v160006Ev
+ ___block_literal_global.1148
+ ___block_literal_global.1232
+ ___block_literal_global.1448
+ ___block_literal_global.1562
+ ___block_literal_global.1566
+ ___block_literal_global.1716
+ ___block_literal_global.2014
+ ___block_literal_global.2017
+ ___block_literal_global.2019
+ ___block_literal_global.224
+ _objc_msgSend$formattedDescription:withPrintedTypes:
+ _objc_msgSend$isCurrentProcessAnApplicationExtension
- -[MTLArrayTypeInternal formattedDescription:]
- -[MTLIndirectConstantArgument formattedDescription:]
- -[MTLInferredInput formattedDescription:]
- -[MTLPointerTypeInternal formattedDescription:]
- -[MTLPostVertexDumpOutput formattedDescription:]
- -[MTLStructMemberInternal formattedDescription:]
- -[MTLStructTypeInternal formattedDescription:]
- -[MTLTextureReferenceTypeInternal formattedDescription:]
- GCC_except_table695
- GCC_except_table698
- GCC_except_table703
- __ZL19deserializeArgumentPU23objcproto12MTLDeviceSPI11objc_objectPKN13AirReflection6NodeIdEPKN11flatbuffers6VectorINS5_6OffsetINS1_4NodeEEEEERK18DeserializeContextPP18MTLBindingInternal
- __ZL20deserializeArgumentsPU23objcproto12MTLDeviceSPI11objc_objectPKN11flatbuffers6VectorIPKN13AirReflection6NodeIdEEEPKNS2_INS1_6OffsetINS3_4NodeEEEEERK18DeserializeContextRPP18MTLBindingInternalbPj
- __ZL25deserializeGlobalBindingsPU23objcproto12MTLDeviceSPI11objc_objectPKN11flatbuffers6VectorIPKN13AirReflection6NodeIdEEERK18DeserializeContextPKNS2_INS1_6OffsetINS3_4NodeEEEEERPP18MTLBindingInternal
- __ZL25deserializeStructArgumentPU23objcproto12MTLDeviceSPI11objc_objectPKN13AirReflection6NodeIdEPKN11flatbuffers6VectorINS5_6OffsetINS1_4NodeEEEEERK18DeserializeContext
- ___block_literal_global.1144
- ___block_literal_global.1228
- ___block_literal_global.1441
- ___block_literal_global.1555
- ___block_literal_global.1559
- ___block_literal_global.1705
- ___block_literal_global.2003
- ___block_literal_global.2006
- ___block_literal_global.2008
- ___block_literal_global.223
CStrings:
+ "08:52:07"
+ "<Recursive>"
+ "KERNEL_INDEX_INITIALIZE_DEBUG_FRAGMENT_INDICES"
+ "Nov 12 2023"
+ "Nov 12 2023 08:52:07"
+ "TB,GareWritableHeapsEnabled,SsetWritableHeapsEnabled:"
+ "TB,GareWritableHeapsEnabled,SsetWritableHeapsEnabled:,V_writableHeapsEnabled"
+ "_isPlugin"
+ "_writableHeapsEnabled"
+ "applegpu_g15g"
+ "applegpu_g15s"
+ "areWritableHeapsEnabled"
+ "formattedDescription:withPrintedTypes:"
+ "initializeDebugFragmentIndicesKernel"
+ "isCurrentProcessAnApplicationExtension"
+ "setWritableHeapsEnabled:"
+ "writableHeapsEnabled"
- "14:40:16"
- "Oct 17 2023"
- "Oct 17 2023 14:40:16"
- "applegpu__g275"
- "applegpu__g419"

```
