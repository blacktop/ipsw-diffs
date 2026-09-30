## libSEUpdater.dylib

> `/usr/lib/updaters/libSEUpdater.dylib`

```diff

 57.2.1.0.0
-  __TEXT.__text: 0x65ef4
+  __TEXT.__text: 0x65f20
   __TEXT.__auth_stubs: 0x1210
   __TEXT.__init_offsets: 0x1c
   __TEXT.__objc_methlist: 0x654

   __TEXT.__unwind_info: 0x1a18
   __TEXT.__objc_classname: 0x9a
   __TEXT.__objc_methname: 0x1263
-  __TEXT.__objc_methtype: 0x707
+  __TEXT.__objc_methtype: 0x70f
   __TEXT.__objc_stubs: 0xfe0
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__const: 0x580

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnfrestore.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 86C04BBC-C330-396C-AC4A-8BA6483CE6C8
+  UUID: 9B5038DD-2D68-3AC2-999B-72E573B77B9B
   Functions: 1337
   Symbols:   4370
   CStrings:  1770
Functions:
~ __ZN4SLAM5ErrorC1EPKcz : 440 -> 444
~ __ZN4SLAM5Error3AddEPKcz : 412 -> 416
~ __ZN4SLAM12ScriptResult10addMessageERKNS_16ExecutionMessageE : 292 -> 296
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE18__assign_with_sizeB8ne200100IPS6_SA_EEvT_T0_l : 416 -> 420
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorIN4SLAM16ExecutionMessageENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS0_IhNS_9allocatorIhEEEENS1_IS3_EEE24__emplace_back_slow_pathIJRPhS7_EEEPS3_DpOT_ : 308 -> 304
~ __ZNKSt3__120__shared_ptr_pointerIPN13SEUpdaterUtil8SELogObjENS_10shared_ptrIS2_E27__shared_ptr_default_deleteIS2_S2_EENS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZN9SEUpdater14GetPackageInfoENSt3__110shared_ptrINS_19P73BaseSEControllerEEE : 2556 -> 2564
~ __ZN9SEUpdater15GetInstanceInfoENSt3__110shared_ptrINS_19P73BaseSEControllerEEE : 3740 -> 3748
~ __ZNKSt3__120__shared_ptr_pointerIPNS_6vectorIhNS_9allocatorIhEEEENS_10shared_ptrIS4_E27__shared_ptr_default_deleteIS4_S4_EENS2_IS4_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__16vectorINS0_IhNS_9allocatorIhEEEENS1_IS3_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNK13SERestoreInfo15P73BaseFirmware21updateMeasurementDictEP14__CFDictionaryNSt3__110shared_ptrIKNS_12SEDeviceInfoEEE : 2292 -> 2284
~ __ZNK13SERestoreInfo15P73BaseFirmware18makeDeliveryObjectERK7DERItem : 7544 -> 7448
~ __ZNSt3__16vectorINS0_ItNS_9allocatorItEEEENS1_IS3_EEE24__emplace_back_slow_pathIJRS3_EEEPS3_DpOT_ : 300 -> 304
~ __ZNSt3__16vectorIN13SERestoreInfo4BLOBENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS0_ItNS_9allocatorItEEEENS1_IS3_EEE16__init_with_sizeB8ne200100IPS3_S7_EEvT_T0_m : 276 -> 280
~ __ZN9SEUpdater23P73BaseUpdateController9doPerformEv : 50972 -> 50992
~ __ZN9SEUpdater23P73BaseUpdateController21PerformSLAMMigrationsEv : 8916 -> 8924
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_19__map_value_compareIS7_S8_NS_4lessIS7_EELb1EEENS5_IS8_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJOS7_EEENSJ_IJEEEEEENS_4pairINS_15__tree_iteratorIS8_PNS_11__tree_nodeIS8_PvEElEEbEERKT_DpOT0_ : 204 -> 208
~ __ZNKSt3__120__shared_ptr_pointerIPN13SEUpdaterUtil5ErrorEZN3ctu20SharedSynchronizableIS2_E15make_shared_ptrIS2_EENS_10shared_ptrIT_EEPS9_EUlS3_E_NS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZN13SERestoreInfo14SEFirmwareBaseC2EPK8__CFData : 1272 -> 1276
~ __ZNKSt3__120__shared_ptr_pointerIPcNS_10shared_ptrIcE27__shared_ptr_default_deleteIccEENS_9allocatorIcEEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorIhNS5_IhEEEEEENS_22__unordered_map_hasherIS7_SB_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SB_SG_SE_Lb1EEENS5_ISB_EEE25__emplace_unique_key_argsIS7_JRKNS_4pairIKS7_SA_EEEEENSN_INS_15__hash_iteratorIPNS_11__hash_nodeISB_PvEEEEbEERKT_DpOT0_ : 704 -> 700
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_13unordered_mapIhN13SERestoreInfo5CApduENS_4hashIhEENS_8equal_toIhEENS5_INS_4pairIKhSA_EEEEEEEENS_22__unordered_map_hasherIS7_SK_NSB_IS7_EENSD_IS7_EELb1EEENS_21__unordered_map_equalIS7_SK_SN_SM_Lb1EEENS5_ISK_EEE25__emplace_unique_key_argsIS7_JRKNSF_IKS7_SJ_EEEEENSF_INS_15__hash_iteratorIPNS_11__hash_nodeISK_PvEEEEbEERKT_DpOT0_ : 692 -> 688
~ __ZNSt3__16vectorIN13SEUpdaterUtil14JCOPConfigItemENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZN13SEUpdaterUtil9parseArgsERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERNS0_3mapIS6_S6_NS0_4lessIS6_EENS4_INS0_4pairIS7_S6_EEEEEE : 5736 -> 5772
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_19__map_value_compareIS7_S8_NS_4lessIS7_EELb1EEENS5_IS8_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRKS7_EEENSJ_IJEEEEEENS_4pairINS_15__tree_iteratorIS8_PNS_11__tree_nodeIS8_PvEElEEbEERKT_DpOT0_ : 236 -> 248
CStrings:
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16@0:8"
+ "{vector<unsigned char, std::allocator<unsigned char>>=**{?=*}}16@0:8"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16@0:8"
- "{vector<unsigned char, std::allocator<unsigned char>>=***}16@0:8"

```
