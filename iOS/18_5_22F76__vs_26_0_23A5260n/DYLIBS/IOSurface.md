## IOSurface

> `/System/Library/Frameworks/IOSurface.framework/IOSurface`

```diff

-372.5.2.0.0
-  __TEXT.__text: 0x11be0
-  __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_methlist: 0x7c8
-  __TEXT.__cstring: 0x2860
-  __TEXT.__const: 0x93
-  __TEXT.__oslogstring: 0x415
-  __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__unwind_info: 0x4a0
-  __TEXT.__objc_classname: 0x13e
-  __TEXT.__objc_methname: 0x1067
-  __TEXT.__objc_methtype: 0x54d
-  __TEXT.__objc_stubs: 0xb60
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0xa00
-  __DATA_CONST.__objc_classlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x10
+392.0.0.0.0
+  __TEXT.__text: 0x1397c
+  __TEXT.__auth_stubs: 0xe20
+  __TEXT.__objc_methlist: 0x9e4
+  __TEXT.__gcc_except_tab: 0x144
+  __TEXT.__const: 0x153
+  __TEXT.__oslogstring: 0x6ae
+  __TEXT.__cstring: 0x2906
+  __TEXT.__unwind_info: 0x530
+  __TEXT.__objc_classname: 0x192
+  __TEXT.__objc_methname: 0x135e
+  __TEXT.__objc_methtype: 0xc76
+  __TEXT.__objc_stubs: 0xc40
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__const: 0xa38
+  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x530
-  __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x688
-  __AUTH_CONST.__const: 0x198
-  __AUTH_CONST.__cfstring: 0x1f00
-  __AUTH_CONST.__objc_const: 0xe58
+  __DATA_CONST.__objc_selrefs: 0x618
+  __DATA_CONST.__objc_superrefs: 0x60
+  __AUTH_CONST.__auth_got: 0x728
+  __AUTH_CONST.__const: 0x1f8
+  __AUTH_CONST.__cfstring: 0x1fe0
+  __AUTH_CONST.__objc_const: 0x12e0
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x74
-  __DATA.__data: 0x208
-  __DATA.__crash_info: 0x40
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x98
+  __DATA.__data: 0x2c8
+  __DATA.__crash_info: 0x148
   __DATA.__bss: 0x138
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__data: 0x1b0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BC2EE6B1-9881-3F7B-9D7B-18A147BC8126
-  Functions: 592
-  Symbols:   1712
-  CStrings:  948
+  UUID: 70A35CB2-F544-36CD-94FA-33B36FAB3182
+  Functions: 648
+  Symbols:   1906
+  CStrings:  1048
 
Symbols:
+ -[IOSurfaceTransaction dealloc]
+ -[IOSurfaceTransaction event]
+ -[IOSurfaceTransaction fromSerialized:]
+ -[IOSurfaceTransaction fromSerialized:].cold.1
+ -[IOSurfaceTransaction initWithSharedEvent:waitValue:isWrite:]
+ -[IOSurfaceTransaction isWrite]
+ -[IOSurfaceTransaction waitValue]
+ -[IOSurfaceTransactionListImpl .cxx_construct]
+ -[IOSurfaceTransactionListImpl .cxx_destruct]
+ -[IOSurfaceTransactionListImpl dealloc]
+ -[IOSurfaceTransactionListImpl eventPortAtIndex:]
+ -[IOSurfaceTransactionListImpl eventPortAtIndex:].cold.1
+ -[IOSurfaceTransactionListImpl initWithSerializedData:numWritten:actualLength:selectedLength:]
+ -[IOSurfaceTransactionListImpl kernelFullListLength]
+ -[IOSurfaceTransactionListImpl length]
+ -[IOSurfaceTransactionListImpl selectedLength]
+ -[IOSurfaceTransactionListImpl transactionAtIndex:]
+ -[IOSurfaceTransactionListImpl transactionAtIndex:].cold.1
+ -[IOSurfaceTransactionListImpl transactionAtIndex:].cold.2
+ -[_IOSurfaceDebugDescription isWired]
+ GCC_except_table16
+ GCC_except_table19
+ GCC_except_table26
+ GCC_except_table7
+ _IOConnectTrap4
+ _IOSurfaceAppendTransaction
+ _IOSurfaceAppendTransaction.cold.1
+ _IOSurfaceAppendTransaction.cold.2
+ _IOSurfaceAppendTransaction.cold.3
+ _IOSurfaceClientAppendTransaction
+ _IOSurfaceClientPruneTransactionList
+ _IOSurfaceClientQueryTransactionList
+ _IOSurfacePruneTransactionList
+ _IOSurfacePruneTransactionList.cold.1
+ _IOSurfaceQueryTransactionList
+ _IOSurfaceQueryTransactionList.cold.1
+ _IOSurfaceQueryTransactionList.cold.2
+ _IOSurfaceQueryTransactionList.cold.3
+ _OBJC_CLASS_$_IOSurfaceTransaction
+ _OBJC_CLASS_$_IOSurfaceTransactionListImpl
+ _OBJC_IVAR_$_IOSurfaceTransaction._event
+ _OBJC_IVAR_$_IOSurfaceTransaction._isWrite
+ _OBJC_IVAR_$_IOSurfaceTransaction._waitValue
+ _OBJC_IVAR_$_IOSurfaceTransactionListImpl._kernelFullListLength
+ _OBJC_IVAR_$_IOSurfaceTransactionListImpl._length
+ _OBJC_IVAR_$_IOSurfaceTransactionListImpl._mtx
+ _OBJC_IVAR_$_IOSurfaceTransactionListImpl._selectedLength
+ _OBJC_IVAR_$_IOSurfaceTransactionListImpl._serializedData
+ _OBJC_IVAR_$_IOSurfaceTransactionListImpl._txnCache
+ _OBJC_METACLASS_$_IOSurfaceTransaction
+ _OBJC_METACLASS_$_IOSurfaceTransactionListImpl
+ __OBJC_$_INSTANCE_METHODS_IOSurfaceTransaction
+ __OBJC_$_INSTANCE_METHODS_IOSurfaceTransactionListImpl
+ __OBJC_$_INSTANCE_VARIABLES_IOSurfaceTransaction
+ __OBJC_$_INSTANCE_VARIABLES_IOSurfaceTransactionListImpl
+ __OBJC_$_PROP_LIST_IOSurfaceTransaction
+ __OBJC_$_PROP_LIST_IOSurfaceTransactionList
+ __OBJC_$_PROP_LIST_IOSurfaceTransactionListImpl
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_IOSurfaceTransactionList
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_IOSurfaceTransactionList
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_IOSurfaceTransactionList
+ __OBJC_CLASS_PROTOCOLS_$_IOSurfaceTransactionListImpl
+ __OBJC_CLASS_RO_$_IOSurfaceTransaction
+ __OBJC_CLASS_RO_$_IOSurfaceTransactionListImpl
+ __OBJC_LABEL_PROTOCOL_$_IOSurfaceTransactionList
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_IOSurfaceTransaction
+ __OBJC_METACLASS_RO_$_IOSurfaceTransactionListImpl
+ __OBJC_PROTOCOL_$_IOSurfaceTransactionList
+ __OBJC_PROTOCOL_$_NSObject
+ __ZNKSt3__120__shared_ptr_pointerIP30IOSurfaceTransactionSerializedNS_14default_deleteIA_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info
+ __ZNKSt9type_infoeqB8ne200100ERKS_
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZNSt3__110shared_ptrIA_30IOSurfaceTransactionSerializedEC2B8ne200100IS1_NS_14default_deleteIS2_EELi0EEEPT_T0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP20IOSurfaceTransactionEENS_22__unordered_map_hasherImS4_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP20IOSurfaceTransactionEENS_22__unordered_map_hasherImS4_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE25__emplace_unique_key_argsImJRKNS_21piecewise_construct_tENS_5tupleIJRKmEEENSK_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP20IOSurfaceTransactionEENS_22__unordered_map_hasherImS4_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE4findImEENS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP20IOSurfaceTransactionEENS_22__unordered_map_hasherImS4_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP20IOSurfaceTransactionEENS_22__unordered_map_hasherImS4_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS4_S9_S7_Lb1EEENS_9allocatorIS4_EEED2Ev
+ __ZNSt3__112__next_primeEm
+ __ZNSt3__119__shared_weak_count14__release_weakEv
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev
+ __ZNSt3__119__shared_weak_countD2Ev
+ __ZNSt3__119piecewise_constructE
+ __ZNSt3__120__shared_ptr_pointerIP30IOSurfaceTransactionSerializedNS_14default_deleteIA_S1_EENS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_pointerIP30IOSurfaceTransactionSerializedNS_14default_deleteIA_S1_EENS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_pointerIP30IOSurfaceTransactionSerializedNS_14default_deleteIA_S1_EENS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_pointerIP30IOSurfaceTransactionSerializedNS_14default_deleteIA_S1_EENS_9allocatorIS1_EEED1Ev
+ __ZNSt3__15mutex4lockEv
+ __ZNSt3__15mutex6unlockEv
+ __ZNSt3__15mutexD1Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZSt7nothrow
+ __ZSt9terminatev
+ __ZTINSt3__114default_deleteIA_30IOSurfaceTransactionSerializedEE
+ __ZTINSt3__119__shared_weak_countE
+ __ZTINSt3__120__shared_ptr_pointerIP30IOSurfaceTransactionSerializedNS_14default_deleteIA_S1_EENS_9allocatorIS1_EEEE
+ __ZTISt20bad_array_new_length
+ __ZTSNSt3__114default_deleteIA_30IOSurfaceTransactionSerializedEE
+ __ZTSNSt3__120__shared_ptr_pointerIP30IOSurfaceTransactionSerializedNS_14default_deleteIA_S1_EENS_9allocatorIS1_EEEE
+ __ZTVN10__cxxabiv117__class_type_infoE
+ __ZTVN10__cxxabiv120__si_class_type_infoE
+ __ZTVNSt3__120__shared_ptr_pointerIP30IOSurfaceTransactionSerializedNS_14default_deleteIA_S1_EENS_9allocatorIS1_EEEE
+ __ZdaPvSt19__type_descriptor_t
+ __ZdlPv
+ __ZdlPvSt19__type_descriptor_t
+ __ZnamRKSt9nothrow_t
+ __ZnwmSt19__type_descriptor_t
+ ___clang_call_terminate
+ ___cxa_allocate_exception
+ ___cxa_begin_catch
+ ___cxa_end_catch
+ ___cxa_rethrow
+ ___cxa_throw
+ ___gxx_personality_v0
+ __ioSurfaceAddClientRef.cold.1
+ _createDisplayMaskRectangleFromStruct
+ _createVersatileSenselArrayPatternFromStruct
+ _getUInt16FromDict
+ _iosCacheGet
+ _kIOSurfaceDisplayMaskRectangle
+ _kIOSurfaceDisplayMaskRectangle_RectangleHeight
+ _kIOSurfaceDisplayMaskRectangle_RectangleLeft
+ _kIOSurfaceDisplayMaskRectangle_RectangleTop
+ _kIOSurfaceDisplayMaskRectangle_RectangleWidth
+ _kIOSurfaceDisplayMaskRectangle_ReferenceRasterHeight
+ _kIOSurfaceDisplayMaskRectangle_ReferenceRasterWidth
+ _objc_msgSend$event
+ _objc_msgSend$fromSerialized:
+ _objc_msgSend$initWithSerializedData:numWritten:actualLength:selectedLength:
+ _objc_msgSend$initWithSharedEvent:waitValue:isWrite:
+ _objc_msgSend$isWrite
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$waitValue
+ _sniffDisplayMaskRectangleKeyToStruct
+ _sniffVersatileSenselArrayPatternKeyToStruct
+ _strcmp
- -[IOSurfaceSharedEvent supportsLowLatencySignalAndWait]
- _CFDictionaryAddValue
CStrings:
+ "#16@0:8"
+ ".cxx_construct"
+ "@\"IOSurfaceSharedEvent\""
+ "@\"IOSurfaceTransaction\"24@0:8Q16"
+ "@\"NSString\"16@0:8"
+ "@24@0:8:16"
+ "@24@0:8r^v16"
+ "@32@0:8:16@24"
+ "@36@0:8@16Q24B32"
+ "@40@0:8:16@24@32"
+ "@56@0:8{shared_ptr<IOSurfaceTransactionSerialized[]>=^{?}^{__shared_weak_count}}16Q32Q40Q48"
+ "B"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "DisplayMaskRectangle"
+ "I24@0:8Q16"
+ "IOSurfaceAppendTransaction got non-success return from kernel"
+ "IOSurfaceAppendTransaction got null buffer"
+ "IOSurfaceAppendTransaction got null transaction"
+ "IOSurfaceClient.m"
+ "IOSurfacePruneTransactionList got null buffer"
+ "IOSurfaceQueryTransactionList failed to allocate memory"
+ "IOSurfaceQueryTransactionList got non-success return from kernel"
+ "IOSurfaceQueryTransactionList got null buffer"
+ "IOSurfaceTransaction"
+ "IOSurfaceTransactionList"
+ "IOSurfaceTransactionListImpl"
+ "NSObject"
+ "RectangleHeight"
+ "RectangleLeft"
+ "RectangleTop"
+ "RectangleWidth"
+ "ReferenceRasterHeight"
+ "ReferenceRasterWidth"
+ "T#,R"
+ "T@\"IOSurfaceSharedEvent\",R,V_event"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TB,R,D"
+ "TB,R,V_isWrite"
+ "TQ,R,V_kernelFullListLength"
+ "TQ,R,V_length"
+ "TQ,R,V_selectedLength"
+ "TQ,R,V_waitValue"
+ "Vv16@0:8"
+ "[IOSurfaceTransaction fromSerialized] got nil event from serialized data"
+ "[IOSurfaceTransactionListImpl eventPortAtIndex] invalid index %zu"
+ "[IOSurfaceTransactionListImpl transactionAtIndex] failed to create transaction at index %zu"
+ "[IOSurfaceTransactionListImpl transactionAtIndex] invalid index %zu"
+ "^{_NSZone=}16@0:8"
+ "_event"
+ "_iosCacheDict"
+ "_isWrite"
+ "_kernelFullListLength"
+ "_length"
+ "_mtx"
+ "_selectedLength"
+ "_serializedData"
+ "_txnCache"
+ "_waitValue"
+ "autorelease"
+ "class"
+ "conformsToProtocol:"
+ "debugDescription"
+ "event"
+ "eventPortAtIndex:"
+ "fromSerialized:"
+ "initWithSerializedData:numWritten:actualLength:selectedLength:"
+ "initWithSharedEvent:waitValue:isWrite:"
+ "iosCacheSet"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "isWired"
+ "isWrite"
+ "kernelFullListLength"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "selectedLength"
+ "self"
+ "superclass"
+ "transactionAtIndex:"
+ "unsignedLongLongValue"
+ "waitValue"
+ "zone"
+ "{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}"
+ "{shared_ptr<IOSurfaceTransactionSerialized[]>=\"__ptr_\"^{?}\"__cntrl_\"^{__shared_weak_count}}"
+ "{unordered_map<unsigned long, IOSurfaceTransaction *, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, IOSurfaceTransaction *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, IOSurfaceTransaction *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "supportsLowLatencySignalAndWait"

```
