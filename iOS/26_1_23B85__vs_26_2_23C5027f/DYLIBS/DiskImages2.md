## DiskImages2

> `/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2`

```diff

 514.40.7.0.0
-  __TEXT.__text: 0x1b5390
+  __TEXT.__text: 0x1b54c4
   __TEXT.__auth_stubs: 0x2220
   __TEXT.__objc_methlist: 0x388c
   __TEXT.__const: 0x1176a
-  __TEXT.__gcc_except_tab: 0x181e0
+  __TEXT.__gcc_except_tab: 0x181e4
   __TEXT.__cstring: 0x11668
   __TEXT.__oslogstring: 0x1891
   __TEXT.__ustring: 0x13c

   __TEXT.__unwind_info: 0xc6f0
   __TEXT.__eh_frame: 0x150
   __TEXT.__objc_classname: 0x6a2
-  __TEXT.__objc_methname: 0x7060
-  __TEXT.__objc_methtype: 0x239a
+  __TEXT.__objc_methname: 0x7064
+  __TEXT.__objc_methtype: 0x23ea
   __TEXT.__objc_stubs: 0x6180
   __DATA_CONST.__got: 0x5b0
-  __DATA_CONST.__const: 0xe20
+  __DATA_CONST.__const: 0xe18
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38

   - /usr/lib/libz.1.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/local/lib/libcurl.4.dylib
-  UUID: 876CC1E8-18D2-37FE-9670-6E86C889266B
+  UUID: C82E7510-9215-33FA-86BF-F67B9F02AA6A
   Functions: 10329
-  Symbols:   29662
+  Symbols:   29660
   CStrings:  4228
 
Symbols:
+ __ZN3$_68__invokeIP19io_rings_consumer_tEEDaT_
+ __ZN3$_78__invokeIP19io_rings_consumer_tbEEDaT_T0_
+ __ZN4$_108__invokeIP19io_rings_consumer_tEEDaT_
- __ZN3$_58__invokeIP19io_rings_consumer_tEEDaT_
- __ZN3$_68__invokeIP19io_rings_consumer_tbEEDaT_T0_
- __ZN3$_78__invokeIP19io_rings_consumer_tEEDaT_
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit_$_FetchRestoreKeys
Functions:
~ __ZN15DiskImagePlugin4readERN9DiskImage7ContextERKN9sg_vec_ns7details15sg_vec_iteratorES7_ : 1324 -> 1336
~ __ZN15DiskImagePlugin5writeERN9DiskImage7ContextERKN9sg_vec_ns7details15sg_vec_iteratorES7_ : 2152 -> 2164
~ __ZN15DiskImagePlugin10read_asyncERNS_18ContextPluginAsyncERKN9sg_vec_ns7details15sg_vec_iteratorES6_ : 2096 -> 2116
~ __ZNSt3__16vectorI26di_async_sub_transaction_tNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_ : 332 -> 336
~ __ZL27create_stack_vec_from_graphP14DiskImageGraphb : 1516 -> 1520
~ __ZNKSt3__120__shared_ptr_pointerIPN6crypto17passphrase_headerENS_14default_deleteIS2_EENS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNKSt3__120__shared_ptr_pointerIPcNS_14default_deleteIA_cEENS_9allocatorIcEEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNKSt3__120__shared_ptr_pointerIPhNS_14default_deleteIA_hEENS_9allocatorIhEEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNKSt3__120__shared_ptr_pointerIP9DiskImageNS_14default_deleteIS1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNKSt3__120__shared_ptr_pointerIPN6crypto6headerENS_14default_deleteIS2_EENS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZN22di_hybrid_subscriber_t15handle_read_sqeEPK14io_rings_sqe_tRN7pool_ns6pool_tIN9DiskImage7ContextENSt3__114default_deleteEE16pooled_element_tEi : 1920 -> 1896
~ __ZN26di_async_sub_transaction_t19append_empty_bufferEjj : 256 -> 260
~ __ZN26di_async_sub_transaction_t18enqueue_new_bufferEm : 340 -> 344
~ __ZNKSt3__120__shared_ptr_pointerIPcZN26di_async_sub_transaction_t15allocate_bufferEmEUlPT_E_NS_9allocatorIcEEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__16vectorINS_10shared_ptrIcEENS_9allocatorIS2_EEE18__insert_with_sizeB8ne200100INS_13move_iteratorINS_11__wrap_iterIPS2_EEEESB_EESA_NS8_IPKS2_EET_T0_l : 460 -> 456
~ __ZNSt3__16vectorINS_10shared_ptrIN9DiskImage7ContextEEENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJNS_10unique_ptrIN15DiskImagePlugin18ContextPluginAsyncENS_14default_deleteISB_EEEEEEEPS4_DpOT_ : 256 -> 252
~ __ZNKSt3__120__shared_ptr_pointerIPN15DiskImagePlugin18ContextPluginAsyncENS_14default_deleteIS2_EENS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__16vectorINS_10shared_ptrIN9DiskImage7ContextEEENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJNS_10unique_ptrIS3_NS_14default_deleteIS3_EEEEEEEPS4_DpOT_ : 256 -> 252
~ __ZNKSt3__120__shared_ptr_pointerIPN9DiskImage7ContextENS_14default_deleteIS2_EENS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__15dequeINS_6atomicIPN9DiskImage7ContextEEENS_9allocatorIS5_EEE19__add_back_capacityEv : 468 -> 472
~ __ZNSt3__114__split_bufferIPNS_6atomicIPN9DiskImage7ContextEEENS_9allocatorIS6_EEE13emplace_frontIJS6_EEEvDpOT_ : 268 -> 272
~ __ZNKSt3__120__shared_ptr_pointerIP19di_hybrid_context_tZN22di_hybrid_subscriber_t15handle_read_sqeEPK14io_rings_sqe_tRN7pool_ns6pool_tIN9DiskImage7ContextENS_14default_deleteEE16pooled_element_tEiE3$_0NS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__15dequeIP26di_async_sub_transaction_tNS_9allocatorIS2_EEE19__add_back_capacityEv : 468 -> 472
~ __ZNSt3__114__split_bufferIPPN3ref7details21tagged_allocated_typeIN7di_asif7details5tableEyEENS_9allocatorIS9_EEE13emplace_frontIJS9_EEEvDpOT_ : 268 -> 272
~ __ZNKSt3__120__shared_ptr_pointerIPcZL15make_shared_bufmEUlS1_E_NS_9allocatorIcEEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__15dequeIN6crypto12promise_sg_tENS_9allocatorIS2_EEE19__add_back_capacityEv : 468 -> 472
~ __ZN13pstack_headerC2ERKNSt3__110shared_ptrI7BackendEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb : 1440 -> 1444
~ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne200100IONS1_9__variant15__value_visitorIZN13diskimage_uio7details26diskimage_open_params_impl25create_diskimage_from_hdrEvE3$_0EEJRNS0_6__baseILNS0_6_TraitE1EJNS_9monostateEN4udif6headerEN7di_asif6headerE10raw_header13pstack_header13plugin_headerEEEEEEDcT_DpT0_ : 1196 -> 1200
~ __ZNSt3__16vectorINS_5tupleIJNS_10shared_ptrI9DiskImageEEN18DiskImageStackable4roleEEEENS_9allocatorIS7_EEE24__emplace_back_slow_pathIJNS1_IJNS_10unique_ptrIS3_NS_14default_deleteIS3_EEEES6_EEEEEEPS7_DpOT_ : 296 -> 292
~ __ZNSt3__16vectorIN6crypto4keys8key_pairENS_9allocatorIS3_EEE18__assign_with_sizeB8ne200100IPS3_S8_EEvT_T0_l : 368 -> 372
~ __ZNSt3__16vectorIN6crypto4keys8key_pairENS_9allocatorIS3_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZN15rawTestPlugin_t12subscriber_t7_addSQEEPK14io_rings_sqe_t : 248 -> 252
~ __ZNSt3__16vectorIPK14io_rings_sqe_tNS_9allocatorIS3_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNKSt3__120__shared_ptr_pointerIP21io_rings_subscriber_tZN20object_subscribers_tILm16EE9subscribeERS1_EUlS2_E_NS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__16vectorINS_10shared_ptrI16LockableResourceEENS_9allocatorIS3_EEE18__assign_with_sizeB8ne200100IPS3_S8_EEvT_T0_l : 316 -> 328
~ __ZNSt3__16vectorINS_10shared_ptrIN14sparse_bundles4Band11ContextBandEEENS_9allocatorIS5_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN6crypto4keys8key_pairENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_ : 352 -> 356
~ __ZNSt3__16vectorIN14sparse_bundles8band_ptrENS_9allocatorIS2_EEE7reserveEm : 220 -> 236
~ __ZNSt3__16vectorIN14sparse_bundles8band_ptrENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_ : 304 -> 308
~ __ZN16ContextAllocatorIN5locks3StdEJNSt3__110unique_ptrIN17DiskImageUDIFReadI10UDIFReaderINS0_4NoneEE13DiskImageUDIFE11ContextUDIFENS2_14default_deleteISA_EEEENS2_10shared_ptrI9BackendSGEEEE12emplace_backEOSD_OSG_ : 276 -> 280
~ __ZNSt3__16vectorI17ChecksumSchedulerIN8checksum3AnyIN5locks4NoneEJNS2_4NoneENS2_5CRC32EEE10bind_algosEN7details11udif_verify14scheduler_typeENS4_3StdEENS_9allocatorISE_EEE24__emplace_back_slow_pathIJSE_EEEPSE_DpOT_ : 332 -> 336
~ __ZNSt3__16vectorIN3ref15tagged_weak_ptrIN7di_asif7details5tableEyEENS_9allocatorIS6_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN3ref7details18ref_cnt_set_handleENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_ : 308 -> 312
~ __ZNSt3__16vectorIyNS_9allocatorIyEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNKSt3__120__shared_ptr_pointerIPcZL15make_shared_bufmEUlS1_E_NS_9allocatorIcEEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__16vectorI8sg_entryNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJKNS_10shared_ptrIcEERK7WrapperIyNS_17integral_constantIbLb1EEEJ7be_typeEERySF_EEEPS1_DpOT_ : 388 -> 400
~ __ZNSt3__16vectorIN7di_asif11meta_headerENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRNS1_7details11ContextASIFERNS7_3dirEyEEEPS2_DpOT_ : 452 -> 448
~ __ZNSt3__16vectorIN7di_asif11meta_headerENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRNS1_7details11ContextASIFERNS7_3dirERKyEEEPS2_DpOT_ : 452 -> 448
~ __ZNSt3__15dequeIPN3ref7details21tagged_allocated_typeIN7di_asif7details11map_elementEyEENS_9allocatorIS8_EEE19__add_back_capacityEv : 468 -> 472
~ __ZNSt3__15dequeIyNS_9allocatorIyEEE19__add_back_capacityEv : 468 -> 472
~ __ZNSt3__114__split_bufferIPyNS_9allocatorIS1_EEE13emplace_frontIJS1_EEEvDpOT_ : 268 -> 272
~ __ZNSt3__15dequeIPN3ref7details21tagged_allocated_typeIN7di_asif7details5tableEyEENS_9allocatorIS8_EEE19__add_back_capacityEv : 468 -> 472
~ __ZN18DiskImageIOBreaker16ContextIOBreakerC2ERS_ONSt3__110unique_ptrIN9DiskImage7ContextENS2_14default_deleteIS5_EEEE : 524 -> 528
~ __ZNSt3__16vectorIN18DiskImageStackable15stackable_layerENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRS2_EEEPS2_DpOT_ : 300 -> 304
~ __ZNSt3__16vectorIN9DiskImage18diskimage_extent_tENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNKSt3__120__shared_ptr_pointerIDnN18DiskImageIOBreaker10shared_refMUlT_E_ENS_9allocatorIcEEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__16vectorI10fileItem_tNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_ : 328 -> 332
~ __ZN15BufferAllocator10add_bufferEv : 240 -> 244
~ __ZNKSt3__120__shared_ptr_pointerIPN5boost10error_infoINS1_9algorithm9bad_char_EcEENS_10shared_ptrIS5_E27__shared_ptr_default_deleteIS5_S5_EENS_9allocatorIS5_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNKSt3__120__shared_ptr_pointerIPN5boost16exception_detail15error_info_baseENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNKSt3__120__shared_ptr_pointerIPcNS_10shared_ptrIcE27__shared_ptr_default_deleteIccEENS_9allocatorIcEEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZN13diskimage_uio6crypto7details24supported_cryptos_impl_tC2Ev : 956 -> 964
~ __ZNSt3__15dequeIN13diskimage_uio6crypto16encryption_propsENS_9allocatorIS3_EEE19__add_back_capacityEv : 468 -> 472
~ __ZNSt3__15dequeIN21crypto_format_backend12promise_io_tENS_9allocatorIS2_EEE19__add_back_capacityEv : 468 -> 472
~ __ZN6crypto31crypto_format_auth_table_reader21read_auth_descriptorsEv : 1112 -> 1116
~ __ZNSt3__16vectorIN6crypto21auth_entry_descriptorENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 72 -> 76
~ __ZNKSt3__120__shared_ptr_pointerIPPK10__CFStringNS_14default_deleteIA_S3_EENS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZN14sparse_bundles4Band12ContextsList3addERKNSt3__110shared_ptrINS0_11ContextBandEEE : 316 -> 320
~ __ZNKSt3__120__shared_ptr_pointerIPN14sparse_bundles4Band11ContextBandENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNKSt3__120__shared_ptr_pointerIPN11AEA_backend14shared_state_tENS_10shared_ptrIS2_E27__shared_ptr_default_deleteIS2_S2_EENS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZN9FileLocal11write_zerosEymmPc : 408 -> 412
~ __ZNSt3__15dequeIN9FileLocal12promise_io_tENS_9allocatorIS2_EEE19__add_back_capacityEv : 468 -> 472
~ __ZNSt3__16vectorINS_4__fs10filesystem4pathENS_9allocatorIS3_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__15dequeIPN3ref7details21tagged_allocated_typeI13CurrentReaderyEENS_9allocatorIS6_EEE19__add_back_capacityEv : 468 -> 472
~ __ZNKSt3__120__shared_ptr_pointerIPNS_6vectorIN3ref15tagged_weak_ptrI13CurrentReaderyEENS_9allocatorIS5_EEEENS_10shared_ptrIS8_E27__shared_ptr_default_deleteIS8_S8_EENS6_IS8_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__16vectorIN3gcd9gcd_queueENS_9allocatorIS2_EEE7reserveEm : 188 -> 204
~ __ZNSt3__16vectorIN3gcd9gcd_queueENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_ : 268 -> 272
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CBNZugBrszNgo7Gv-l-Vh5G_Q7Gmaq8Jz2OnSOU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CBNZugBrszNgo7Gv-l-Vh5G_Q7Gmaq8Jz2OnSOU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CBNZugBrszNgo7Gv-l-Vh5G_Q7Gmaq8Jz2OnSOU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "@32@0:8@16{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>={?=^{header}}}24"
+ "@32@0:8@16{unique_ptr<udif::header, std::default_delete<udif::header>>={?=^{header}}}24"
+ "T{vector<std::shared_ptr<LockableResource>, std::allocator<std::shared_ptr<LockableResource>>>=^v^v{?=^v}},R,N"
+ "v24@0:8{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>={?=^{header}}}16"
+ "{expected<crypto::crypto_serializer_t, std::error_code>={__conditional_no_unique_address<true, std::__expected_base<crypto::crypto_serializer_t, std::error_code>::__repr>={__repr={__conditional_no_unique_address<false, std::__expected_base<crypto::crypto_serializer_t, std::error_code>::__union_t>=(__union_t={crypto_serializer_t=^^?{interval_set<unsigned long long, std::less, boost::icl::discrete_interval<unsigned long long>, std::allocator>={set<boost::icl::discrete_interval<unsigned long long>, boost::icl::exclusive_less_than<boost::icl::discrete_interval<unsigned long long>>, std::allocator<boost::icl::discrete_interval<unsigned long long>>>={__tree<boost::icl::discrete_interval<unsigned long long>, boost::icl::exclusive_less_than<boost::icl::discrete_interval<unsigned long long>>, std::allocator<boost::icl::discrete_interval<unsigned long long>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}}^{format}{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}}{error_code=i^{error_category}})}B}}}24@0:8^v16"
+ "{expected<std::unique_ptr<diskimage_uio::diskimage>, std::error_code>=(storage<std::unique_ptr<diskimage_uio::diskimage>, std::error_code>=c{unique_ptr<diskimage_uio::diskimage, std::default_delete<diskimage_uio::diskimage>>={?=^{diskimage}}}{error_code=i^{error_category}})B}16@0:8"
+ "{optional<crypto::auth_table>=\"\"(?=\"__null_state_\"c\"__val_\"{auth_table=\"descriptors\"{vector<crypto::auth_entry_descriptor, std::allocator<crypto::auth_entry_descriptor>>=\"__begin_\"^{auth_entry_descriptor}\"__end_\"^{auth_entry_descriptor}\"\"{?=\"__cap_\"^{auth_entry_descriptor}}}\"reader\"{shared_ptr<crypto::auth_table_reader_t>=\"__ptr_\"^{auth_table_reader_t}\"__cntrl_\"^{__shared_weak_count}}})\"__engaged_\"B}"
+ "{unique_ptr<DiskImage, std::default_delete<DiskImage>>={?=^{DiskImage}}}16@0:8"
+ "{unique_ptr<DiskImage, std::default_delete<DiskImage>>={?=^{DiskImage}}}24@0:8B16B20"
+ "{unique_ptr<DiskImage, std::default_delete<DiskImage>>={?=^{DiskImage}}}24@0:8^@16"
+ "{unique_ptr<const info::DiskImageInfo, std::default_delete<const info::DiskImageInfo>>={?=^{DiskImageInfo}}}28@0:8B16^@20"
+ "{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>=\"\"{?=\"__ptr_\"^{header}}}"
+ "{unique_ptr<diskimage_uio::diskimage, std::default_delete<diskimage_uio::diskimage>>=\"\"{?=\"__ptr_\"^{diskimage}}}"
+ "{unique_ptr<diskimage_uio::diskimage_open_params, std::default_delete<diskimage_uio::diskimage_open_params>>=\"\"{?=\"__ptr_\"^{diskimage_open_params}}}"
+ "{unique_ptr<udif::header, std::default_delete<udif::header>>=\"\"{?=\"__ptr_\"^{header}}}"
+ "{vector<std::shared_ptr<LockableResource>, std::allocator<std::shared_ptr<LockableResource>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
+ "{vector<std::shared_ptr<LockableResource>, std::allocator<std::shared_ptr<LockableResource>>>=^v^v{?=^v}}16@0:8"
- "/AppleInternal/Library/BuildRoots/4~CAp5ugBuFOZj3SFZock7LEV6hNKxt-dWHHHKubM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
- "/AppleInternal/Library/BuildRoots/4~CAp5ugBuFOZj3SFZock7LEV6hNKxt-dWHHHKubM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
- "/AppleInternal/Library/BuildRoots/4~CAp5ugBuFOZj3SFZock7LEV6hNKxt-dWHHHKubM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "@32@0:8@16{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>=^{header}}24"
- "@32@0:8@16{unique_ptr<udif::header, std::default_delete<udif::header>>=^{header}}24"
- "T{vector<std::shared_ptr<LockableResource>, std::allocator<std::shared_ptr<LockableResource>>>=^v^v^v},R,N"
- "v24@0:8{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>=^{header}}16"
- "{expected<crypto::crypto_serializer_t, std::error_code>={__conditional_no_unique_address<true, std::__expected_base<crypto::crypto_serializer_t, std::error_code>::__repr>={__repr={__conditional_no_unique_address<false, std::__expected_base<crypto::crypto_serializer_t, std::error_code>::__union_t>=(__union_t={crypto_serializer_t=^^?{interval_set<unsigned long long, std::less, boost::icl::discrete_interval<unsigned long long>, std::allocator>={set<boost::icl::discrete_interval<unsigned long long>, boost::icl::exclusive_less_than<boost::icl::discrete_interval<unsigned long long>>, std::allocator<boost::icl::discrete_interval<unsigned long long>>>={__tree<boost::icl::discrete_interval<unsigned long long>, boost::icl::exclusive_less_than<boost::icl::discrete_interval<unsigned long long>>, std::allocator<boost::icl::discrete_interval<unsigned long long>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}}^{format}{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}}{error_code=i^{error_category}})}B}}}24@0:8^v16"
- "{expected<std::unique_ptr<diskimage_uio::diskimage>, std::error_code>=(storage<std::unique_ptr<diskimage_uio::diskimage>, std::error_code>=c{unique_ptr<diskimage_uio::diskimage, std::default_delete<diskimage_uio::diskimage>>=^{diskimage}}{error_code=i^{error_category}})B}16@0:8"
- "{optional<crypto::auth_table>=\"\"(?=\"__null_state_\"c\"__val_\"{auth_table=\"descriptors\"{vector<crypto::auth_entry_descriptor, std::allocator<crypto::auth_entry_descriptor>>=\"__begin_\"^{auth_entry_descriptor}\"__end_\"^{auth_entry_descriptor}\"__cap_\"^{auth_entry_descriptor}}\"reader\"{shared_ptr<crypto::auth_table_reader_t>=\"__ptr_\"^{auth_table_reader_t}\"__cntrl_\"^{__shared_weak_count}}})\"__engaged_\"B}"
- "{unique_ptr<DiskImage, std::default_delete<DiskImage>>=^{DiskImage}}16@0:8"
- "{unique_ptr<DiskImage, std::default_delete<DiskImage>>=^{DiskImage}}24@0:8B16B20"
- "{unique_ptr<DiskImage, std::default_delete<DiskImage>>=^{DiskImage}}24@0:8^@16"
- "{unique_ptr<const info::DiskImageInfo, std::default_delete<const info::DiskImageInfo>>=^{DiskImageInfo}}28@0:8B16^@20"
- "{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>=\"__ptr_\"^{header}}"
- "{unique_ptr<diskimage_uio::diskimage, std::default_delete<diskimage_uio::diskimage>>=\"__ptr_\"^{diskimage}}"
- "{unique_ptr<diskimage_uio::diskimage_open_params, std::default_delete<diskimage_uio::diskimage_open_params>>=\"__ptr_\"^{diskimage_open_params}}"
- "{unique_ptr<udif::header, std::default_delete<udif::header>>=\"__ptr_\"^{header}}"
- "{vector<std::shared_ptr<LockableResource>, std::allocator<std::shared_ptr<LockableResource>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
- "{vector<std::shared_ptr<LockableResource>, std::allocator<std::shared_ptr<LockableResource>>>=^v^v^v}16@0:8"

```
