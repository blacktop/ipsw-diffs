## MLAssetIO

> `/System/Library/PrivateFrameworks/MLAssetIO.framework/MLAssetIO`

```diff

-3505.3.1.0.0
-  __TEXT.__text: 0x5cb24
+3505.4.1.0.0
+  __TEXT.__text: 0x5c8a0
   __TEXT.__auth_stubs: 0xe30
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1184
   __TEXT.__const: 0x74b8
-  __TEXT.__gcc_except_tab: 0x6064
-  __TEXT.__cstring: 0x6ad5
+  __TEXT.__gcc_except_tab: 0x5fd8
+  __TEXT.__cstring: 0x69a9
   __TEXT.__oslogstring: 0x602
-  __TEXT.__unwind_info: 0x2570
+  __TEXT.__unwind_info: 0x2548
   __TEXT.__objc_classname: 0x2c5
   __TEXT.__objc_methname: 0x1f74
-  __TEXT.__objc_methtype: 0x19d9
+  __TEXT.__objc_methtype: 0x19e5
   __TEXT.__objc_stubs: 0x1840
   __DATA_CONST.__got: 0x278
   __DATA_CONST.__const: 0x928

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F02FD4E9-3D6F-3D25-8B2F-9001673DD59C
-  Functions: 2097
-  Symbols:   6346
-  CStrings:  1853
+  UUID: CF174607-7D5C-3A2D-B1A9-B566B6334A57
+  Functions: 2093
+  Symbols:   6333
+  CStrings:  1847
 
Symbols:
+ GCC_except_table426
+ GCC_except_table430
+ GCC_except_table537
- GCC_except_table309
- GCC_except_table41
- GCC_except_table53
- GCC_except_table536
- GCC_except_table79
- __ZN6google8protobuf3MapINSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEES8_E8InnerMap13iterator_baseINS0_7MapPairIS8_S8_EEEC2ENS2_14__map_iteratorINS2_15__tree_iteratorINS2_12__value_typeINS2_17reference_wrapperIKS8_EEPvEEPNS2_11__tree_nodeISM_SL_EElEEEEPKSA_m
- __ZN6google8protobuf3MapINSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEES8_E8InnerMap16CreateEmptyTableEm
- __ZN6google8protobuf3MapINSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEES8_E8InnerMap18InsertUniqueInTreeEmPNSA_4NodeE
- __ZN6google8protobuf3MapINSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEES8_E8InnerMap19TableEntryIsTooLongEm
- __ZN6google8protobuf5Arena6CreateINSt3__13mapINS3_17reference_wrapperIKNS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEPvNS0_8internal18TransparentSupportISB_E4lessENSF_12MapAllocatorINS3_4pairIKSD_SE_EEEEEEJSI_SN_EEEPT_PS1_DpOT0_
CStrings:
+ "CHECK failed: !tree->empty(): "
+ "CHECK failed: (bucket_index_ & 1) == (0u): "
+ "CHECK failed: m_->index_of_first_non_null_ == m_->num_buckets_ || m_->table_[m_->index_of_first_non_null_] != nullptr: "
+ "CHECK failed: node_ != nullptr && m_ != nullptr: "
+ "{unique_ptr<MIL::IRProgram, std::default_delete<MIL::IRProgram>>=\"\"{?=\"__ptr_\"^{IRProgram}}}"
+ "{vector<MIOFunctionInfo, std::allocator<MIOFunctionInfo>>=\"__begin_\"^{MIOFunctionInfo}\"__end_\"^{MIOFunctionInfo}\"\"{?=\"__cap_\"^{MIOFunctionInfo}}}"
- "CHECK failed: !TableEntryIsTree(b) && !TableEntryIsTree(b ^ 1): "
- "CHECK failed: (count) <= (kMaxLength): "
- "CHECK failed: (count) == (tree->size()): "
- "CHECK failed: (n & (n - 1)) == (0u): "
- "CHECK failed: (new_num_buckets) >= (kMinTableSize): "
- "CHECK failed: (result.bucket_index_) == (b & ~static_cast<size_type>(1)): "
- "CHECK failed: (table_[b]) == (table_[b ^ 1]): "
- "CHECK failed: find(node->kv.first) == end(): "
- "CHECK failed: index_of_first_non_null_ == num_buckets_ || table_[index_of_first_non_null_] != nullptr: "
- "CHECK failed: n >= kMinTableSize: "
- "{unique_ptr<MIL::IRProgram, std::default_delete<MIL::IRProgram>>=\"__ptr_\"^{IRProgram}}"
- "{vector<MIOFunctionInfo, std::allocator<MIOFunctionInfo>>=\"__begin_\"^{MIOFunctionInfo}\"__end_\"^{MIOFunctionInfo}\"__cap_\"^{MIOFunctionInfo}}"

```
