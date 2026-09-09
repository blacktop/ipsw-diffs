## DiskImages2

> `/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2`

```diff

 598.0.1.0.0
-  __TEXT.__text: 0x1f25d4
+  __TEXT.__text: 0x1f2750
   __TEXT.__objc_methlist: 0x3d0c
   __TEXT.__const: 0x172fa
-  __TEXT.__gcc_except_tab: 0x1b4dc
+  __TEXT.__gcc_except_tab: 0x1b4d8
   __TEXT.__cstring: 0x17538
   __TEXT.__oslogstring: 0x1d7e
   __TEXT.__ustring: 0x13c

   __TEXT.__swift5_typeref: 0x58
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xe548
+  __TEXT.__unwind_info: 0xe540
   __TEXT.__eh_frame: 0xf0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
Functions:
~ __ZN6sg_vecC2ERK8sg_entry : 324 -> 320
~ __ZL27create_stack_vec_from_graphP14DiskImageGraphb : 1484 -> 1492
~ __ZN7details27for_each_sg_in_vec_internalINSt3__16__bindIM9DiskImageF11io_result_tRNS3_7ContextERK8sg_entryEJPS3_NS1_17reference_wrapperIS5_EERKNS1_12placeholders4__phILi1EEEEEEEES4_OT_N9sg_vec_ns7details15sg_vec_iteratorESP_mb : 932 -> 936
~ __ZN17DiskImageUDIFReadI10UDIFReaderIN5locks4NoneEE13DiskImageUDIFE4readERN9DiskImage7ContextERKN9sg_vec_ns7details15sg_vec_iteratorESD_ : 3852 -> 3844
~ __ZN17DiskImageUDIFReadI10UDIFReaderIN5locks4NoneEE13DiskImageUDIFE7trim_ioERK8sg_entryRKN4udif11run_io_infoERKN5boost9container12small_vectorISA_Lm16EvvEEm : 152 -> 148
~ __ZNSt3__15dequeIP26di_async_sub_transaction_tNS_9allocatorIS2_EEE12emplace_backIJS2_EEERS2_DpOT_ : 168 -> 172
~ __ZN22di_hybrid_subscriber_t6cancelEv : 772 -> 776
~ __ZN22di_hybrid_subscriber_t14handle_sub_cqeER26di_async_sub_transaction_ti : 1072 -> 1068
~ __ZN7pool_ns6pool_tIN9DiskImage7ContextENSt3__114default_deleteEED2Ev : 156 -> 160
~ __ZNSt3__16vectorI5iovecNS_9allocatorIS1_EEE18__insert_with_sizeB9foe210106INS_13move_iteratorINS_11__wrap_iterIPS1_EEEESA_EES9_NS7_IPKS1_EET_T0_l : 560 -> 576
~ __ZNSt3__15dequeINS_6atomicIPN9DiskImage7ContextEEENS_9allocatorIS5_EEE12emplace_backIJRS4_EEERS5_DpOT_ : 168 -> 172
~ __ZNSt3__114__split_bufferIPNS_6atomicIPN9DiskImage7ContextEEENS_9allocatorIS6_EEE12emplace_backIJS6_EEEvDpOT_ : 260 -> 264
~ __ZNSt3__114__split_bufferIPNS_6atomicIPN9DiskImage7ContextEEERNS_9allocatorIS6_EEE12emplace_backIJS6_EEEvDpOT_ : 260 -> 264
~ __ZNSt3__114__split_bufferIPPN3ref7details21tagged_allocated_typeIN7di_asif7details5tableEyEENS_9allocatorIS9_EEE12emplace_backIJS9_EEEvDpOT_ : 260 -> 264
~ __ZNSt3__114__split_bufferIPPN3ref7details21tagged_allocated_typeIN7di_asif7details5tableEyEERNS_9allocatorIS9_EEE12emplace_backIJS9_EEEvDpOT_ : 260 -> 264
~ __ZN17AIOInfrastructure16submit_aio_batchEN5boost9container12small_vectorINSt3__110unique_ptrI16aio_request_baseNS3_14default_deleteIS5_EEEELm16EvvEE : 1152 -> 1148
~ __ZNSt3__110__function6__funcIZN17AIOInfrastructureC1EvE3$_0FvP10kevent64_siEEclEOS5_Oi : 744 -> 740
~ __ZN6crypto8crypt_op31backend_futures_prepare_and_runERK19fixed_size_vector_tI8sg_entryER7BackendMS6_F9lw_futureIN12batch_ctx_ns14batched_resultIiEEERKS2_ERS1_ISC_E : 792 -> 796
~ __ZN6crypto8crypt_op24crypt_consecutive_vectorclEv : 736 -> 728
~ __ZNSt3__15dequeIN6crypto12promise_sg_tENS_9allocatorIS2_EEE12emplace_backIJS2_EEERS2_DpOT_ : 268 -> 276
~ __ZNSt3__15dequeIN6crypto12promise_sg_tENS_9allocatorIS2_EEED2B9foe210106Ev : 316 -> 320
~ __ZN11BackendZero11run_futuresEv.resume : 588 -> 604
~ __ZN13diskimage_uio29resolve_stack_nodes_from_pathERKNS_14resolve_paramsE : 628 -> 632
~ __ZN13diskimage_uio17diskimage_context4readERKNS_15small_vector_ns4llvm23SmallVectorTemplateBaseINS_9buffer_ns5boost4asio14mutable_bufferELb1EEEymONSt3__110unique_ptrINS_6crypto14per_io_cryptorENSB_14default_deleteISE_EEEE : 1120 -> 1124
~ __ZN13diskimage_uio17diskimage_context5writeERKNS_15small_vector_ns4llvm23SmallVectorTemplateBaseINS_9buffer_ns5boost4asio12const_bufferELb1EEEymONSt3__110unique_ptrINS_6crypto14per_io_cryptorENSB_14default_deleteISE_EEEE : 1120 -> 1124
~ __ZN13diskimage_uioL16io_vec_to_sg_vecINSt3__14spanIK5iovecLm18446744073709551615EEEEE6sg_vecRKT_ymNS_13option_set_ns10option_setIN8sg_entry7flags_tEEE : 636 -> 624
~ __ZN6sg_vecC2EO8sg_entry : 296 -> 292
~ __ZN15rawTestPlugin_t12subscriber_t7_addSQEEPK14io_rings_sqe_t : 248 -> 244
~ _io_rings_cancel : 304 -> 308
~ _io_rings_return_status_ex : 280 -> 284
~ __ZN16ContextAllocatorIN5locks3StdEJNSt3__110unique_ptrIN17DiskImageUDIFReadI10UDIFReaderINS0_4NoneEE13DiskImageUDIFE11ContextUDIFENS2_14default_deleteISA_EEEENS2_10shared_ptrI9BackendSGEEEE12emplace_backEOSD_OSG_ : 276 -> 272
~ __ZNSt3__15dequeIyNS_9allocatorIyEEE12emplace_backIJRyEEES5_DpOT_ : 168 -> 172
~ __ZN7di_asif7details5table5flushERNS0_11ContextASIFE : 2436 -> 2476
~ __ZZN7di_asif7details5table5writeERNS0_11ContextASIFERKN9sg_vec_ns7details15sg_vec_iteratorES8_ENK3$_1clEv : 584 -> 576
~ __ZN7finallyIZN7di_asif7details5table5writeERNS1_11ContextASIFERKN9sg_vec_ns7details15sg_vec_iteratorES9_E3$_0ED1Ev : 240 -> 236
~ __ZN7di_asif7details3dir9flush_dirERNS0_11ContextASIFEy : 2224 -> 2260
~ __ZN5boost9container35uninitialized_move_and_insert_allocINS0_22small_vector_allocatorIN3ref7details14ref_cnt_handleENS0_13new_allocatorIvEEvEEPS5_S9_NS0_3dtl20insert_emplace_proxyIS8_S9_JS5_EEEEEvRT_T0_SF_SF_T1_mT2_ : 344 -> 348
~ __ZNSt3__114__split_bufferIPyNS_9allocatorIS1_EEE12emplace_backIJS1_EEEvDpOT_ : 260 -> 264
~ __ZNSt3__114__split_bufferIPyRNS_9allocatorIS1_EEE12emplace_backIJS1_EEEvDpOT_ : 260 -> 264
~ __ZN3ref9AllocatorIN7di_asif7details5tableEyED2Ev : 560 -> 564
~ __ZN3ref9AllocatorIN7di_asif7details11map_elementEyED2Ev : 552 -> 560
~ __ZNSt3__15dequeIyNS_9allocatorIyEEE22__insert_bidirectionalB9foe210106INS_16__deque_iteratorIyPyRyPS6_lLl512EEEEES9_NS5_IyPKyRSA_PKSB_lLl512EEET_SG_m : 1400 -> 1460
~ __ZNSt3__15dequeIyNS_9allocatorIyEEE20__add_front_capacityEm : 804 -> 808
~ __ZNKSt3__116__deque_iteratorIyPyRyPS1_lLl512EEplB9foe210106El : 100 -> 96
~ __ZNSt3__15dequeIyNS_9allocatorIyEEE19__add_back_capacityEm : 788 -> 792
~ __ZNKSt3__116__deque_iteratorIyPyRyPS1_lLl512EEmiB9foe210106El : 104 -> 100
~ __ZNSt3__15dequeIPN3ref7details21tagged_allocated_typeIN7di_asif7details5tableEyEENS_9allocatorIS8_EEE12emplace_backIJS8_EEERS8_DpOT_ : 168 -> 172
~ __ZNSt3__15dequeIPN3ref7details21tagged_allocated_typeIN7di_asif7details11map_elementEyEENS_9allocatorIS8_EEE12emplace_backIJS8_EEERS8_DpOT_ : 168 -> 172
~ __ZN7di_asif7details5table17get_table_extentsINSt3__115insert_iteratorINS3_3setIyNS3_4lessIyEENS3_9allocatorIyEEEEEEEEvRNS0_11ContextASIFET_ : 476 -> 468
~ __ZN18DiskImageIOBreaker16ContextIOBreakerC2ERS_ONSt3__110unique_ptrIN9DiskImage7ContextENS2_14default_deleteIS5_EEEE : 500 -> 504
~ __ZN18DiskImageStackable21get_di_extents_for_ioERNS_16ContextStackableEmRKN5boost3icl17discrete_intervalIyNSt3__14lessEEE : 1140 -> 1144
~ __ZN6sg_vecC2EON5boost9container12small_vectorINSt3__14pairINS3_10shared_ptrIcEEmEELm5EvvEEymN13diskimage_uio13option_set_ns10option_setIN8sg_entry7flags_tEEE : 156 -> 152
~ __ZN15BufferAllocator10add_bufferEv : 240 -> 236
~ __ZN2cf27add_key_value_pairs_to_dictERK13CFAutoReleaseIP14__CFDictionaryERKSt16initializer_listINSt3__14pairIPK10__CFStringS0_IPKvEEEE : 80 -> 72
~ __ZN13diskimage_uio6crypto18registered_cryptos15register_cryptoERKNS0_16encryption_propsE : 328 -> 364
~ __ZNSt3__15dequeIN13diskimage_uio6crypto16encryption_propsENS_9allocatorIS3_EEE7emplaceIJS3_EEENS_16__deque_iteratorIS3_PS3_RS3_PS9_lLl256EEENS8_IS3_PKS3_RSD_PKSE_lLl256EEEDpOT_ : 892 -> 976
~ __ZNK13diskimage_uio6crypto18registered_cryptos4findERKNS0_16encryption_propsE : 276 -> 284
~ __ZNSt3__15dequeIN13diskimage_uio6crypto16encryption_propsENS_9allocatorIS3_EEE20__add_front_capacityEv : 572 -> 576
~ __ZNSt3__14prevB9foe210106INS_16__deque_iteratorIN13diskimage_uio6crypto16encryption_propsEPS4_RS4_PS5_lLl256EEELi0EEET_S9_ : 76 -> 80
~ __ZNKSt3__116__deque_iteratorIN13diskimage_uio6crypto16encryption_propsEPS3_RS3_PS4_lLl256EEplB9foe210106El : 92 -> 96
~ __ZN9lock_free8bitmap_t19update_pair_elementEyyyRKNSt3__14pairIbbEE : 212 -> 216
~ __ZNK9lock_free8bitmap_t7get_bitEy : 300 -> 304
~ __ZN9lock_free8bitmap_t7set_bitEyb : 320 -> 324
~ __ZN21crypto_format_backend11run_futuresEv.resume : 3956 -> 3968
~ __ZN18DITelemetryManager18register_telemetryER15DITelemetryBase : 296 -> 288
~ __ZN17CompressedBackend11future_readERK8sg_entry : 1092 -> 1096
~ __ZN14FileLocalAsync24submit_pending_aio_batchEv : 2048 -> 2056
~ __ZN9FileLocal11run_futuresEv.resume : 2860 -> 2864
~ __ZNSt3__15dequeIPN3ref7details21tagged_allocated_typeI13CurrentReaderyEENS_9allocatorIS6_EEE12emplace_backIJS6_EEERS6_DpOT_ : 168 -> 172
~ __ZN3ref9AllocatorI13CurrentReaderyED2Ev : 552 -> 560
```
