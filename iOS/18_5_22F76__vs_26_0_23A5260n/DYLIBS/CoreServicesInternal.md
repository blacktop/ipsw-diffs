## CoreServicesInternal

> `/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal`

```diff

-554.9.0.0.0
-  __TEXT.__text: 0x2d714
+573.0.0.0.0
+  __TEXT.__text: 0x2db48
   __TEXT.__auth_stubs: 0x1480
   __TEXT.__delay_stubs: 0x160
   __TEXT.__delay_helper: 0x3b0
-  __TEXT.__const: 0x630
-  __TEXT.__cstring: 0x1b86
-  __TEXT.__oslogstring: 0x1fca
+  __TEXT.__cstring: 0x1b91
+  __TEXT.__const: 0x5e0
+  __TEXT.__oslogstring: 0x2009
   __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__got: 0x708
+  __DATA_CONST.__got: 0x728
   __DATA_CONST.__const: 0x288
   __AUTH_CONST.__auth_got: 0xa80
   __AUTH_CONST.__const: 0x328
   __AUTH_CONST.__cfstring: 0x1020
   __DATA.__data: 0x94
-  __DATA.__bss: 0x1011
+  __DATA.__bss: 0x4a
   __DATA_DIRTY.__data: 0x250
-  __DATA_DIRTY.__bss: 0xe58
+  __DATA_DIRTY.__bss: 0x1e78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/FileProvider.framework/FileProvider

   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: D4E1B200-4644-3E6A-BCC5-C46120C5A985
-  Functions: 609
-  Symbols:   1851
-  CStrings:  595
+  UUID: 1AE6B156-5EB3-3AD0-8193-0F14029473C6
+  Functions: 612
+  Symbols:   1867
+  CStrings:  597
 
Symbols:
+ _CFAllocatorAllocateTyped
+ _CFStringHasPrefix
+ __MergedGlobals.62
+ __ZL33createFileResourceIdentifierValuePK7__CFURLPK15_FileAttributesPv.cold.1
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn200100ILi0EEEPKc
+ __ZNSt3__113__tree_removeB8nn200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8nn200100Ev
+ __ZNSt3__116__pad_and_outputB8nn200100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn200100Ev
+ __ZNSt3__124__put_character_sequenceB8nn200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__127__tree_balance_after_insertB8nn200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE9push_backB8nn200100EOS2_
+ __ZNSt3__1lsB8nn200100INS_11char_traitsIcEEEERNS_13basic_ostreamIcT_EES6_RKNS_8__iom_t4IcEE
+ __ZSt28__throw_bad_array_new_lengthB8nn200100v
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ _csi_FSObjTypeToFSNodeObjectType
+ _csi_FileIDTreeCreateMountPointArrayWithOptions
+ _csi_FileIDTreeGetEntryInfoFromFileID
+ _csi_FileIDTreeGetFileIDFromPath
+ _kCFURLUbiquitousItemIsExcludedFromSyncKey
+ _kCFURLUbiquitousItemIsSyncPausedKey
+ _kCFURLUbiquitousItemSupportedSyncControlsKey
- _CFAllocatorAllocate
- _CoreServicesInternalVersionNumber
- _CoreServicesInternalVersionString
- _DirEnumEntryAllocate
- __MergedGlobals.59
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn190102Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn190102ILi0EEEPKc
- __ZNSt3__113__tree_removeB8nn190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__116__pad_and_outputB8nn190102IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn190102Ev
- __ZNSt3__124__put_character_sequenceB8nn190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__127__tree_balance_after_insertB8nn190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__1lsB8nn190102INS_11char_traitsIcEEEERNS_13basic_ostreamIcT_EES6_RKNS_8__iom_t4IcEE
- __ZSt28__throw_bad_array_new_lengthB8nn190102v
- __Znwm
CStrings:
+ "%s: this would have gone down the fallback path if enabled: %@"
+ "createFileResourceIdentifierValue"
+ "file:///.file/id="
- "NSURLUbiquitousItemIsExcludedFromSyncKey"

```
