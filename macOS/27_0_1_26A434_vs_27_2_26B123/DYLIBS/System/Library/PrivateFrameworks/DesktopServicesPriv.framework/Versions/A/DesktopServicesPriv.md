## DesktopServicesPriv

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/DesktopServicesPriv`

```diff

-1857.0.0.0.0
-  __TEXT.__text: 0x22dc34
-  __TEXT.__objc_methlist: 0x3d74
-  __TEXT.__gcc_except_tab: 0x34ca4
-  __TEXT.__const: 0x83a0
-  __TEXT.__cstring: 0x9f4e
-  __TEXT.__oslogstring: 0x86d1
+1857.1.9.100.0
+  __TEXT.__text: 0x232e5c
+  __TEXT.__objc_methlist: 0x3eac
+  __TEXT.__gcc_except_tab: 0x35554
+  __TEXT.__cstring: 0x9fa5
+  __TEXT.__const: 0x83e8
+  __TEXT.__oslogstring: 0x8a12
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x10638
+  __TEXT.__unwind_info: 0x10778
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd70
-  __DATA_CONST.__objc_classlist: 0x2d0
+  __DATA_CONST.__const: 0xd88
+  __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x88
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x2680
+  __DATA_CONST.__objc_selrefs: 0x26b0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x160
+  __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0xcc8
-  __AUTH_CONST.__const: 0xb608
-  __AUTH_CONST.__cfstring: 0x4a60
-  __AUTH_CONST.__objc_const: 0x6408
+  __DATA_CONST.__got: 0xcd8
+  __AUTH_CONST.__const: 0xb5b0
+  __AUTH_CONST.__cfstring: 0x4ae0
+  __AUTH_CONST.__objc_const: 0x64c0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1900
+  __AUTH_CONST.__auth_got: 0x1918
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x11d0
+  __AUTH.__objc_data: 0x1220
   __AUTH.__data: 0x20
   __DATA.__objc_ivar: 0x314
-  __DATA.__data: 0x898
-  __DATA.__bss: 0x1148
+  __DATA.__data: 0x938
+  __DATA.__bss: 0x1158
   __DATA.__common: 0xe1
   __DATA_DIRTY.__objc_data: 0xa50
-  __DATA_DIRTY.__data: 0x4d8
-  __DATA_DIRTY.__bss: 0x1028
+  __DATA_DIRTY.__data: 0x498
+  __DATA_DIRTY.__bss: 0x1018
   __DATA_DIRTY.__common: 0x158
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
   - /System/Library/PrivateFrameworks/NetAuth.framework/Versions/A/NetAuth
   - /System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing
+  - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libfakelink.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9824
-  Symbols:   16772
-  CStrings:  2365
+  Functions: 9876
+  Symbols:   16852
+  CStrings:  2383
 
Symbols:
+ +[DSQuarantine settleQuarantine:atURL:error:]
+ -[FIChildrenIterator countByEnumeratingWithState:objects:count:]
+ -[FICompoundNodeIterator countByEnumeratingWithState:objects:count:]
+ -[FICustomNode keyNodesForMappingToPresentationNode]
+ -[FICustomNode remapKeyNodesToPresentationNode]
+ -[FICustomNode setKeyNodesForMappingToPresentationNode:]
+ -[FINodeIterator countByEnumeratingWithState:objects:count:]
+ -[FINodeIteratorWithExtraChildren countByEnumeratingWithState:objects:count:]
+ -[FIPassthroughOperationURLNode fiDomain]
+ -[FIPassthroughOperationURLNode fileName]
+ -[FIPassthroughOperationURLNode fileOpNode]
+ -[FIPassthroughOperationURLNode fileParent]
+ -[FIPassthroughOperationURLNode fileURL]
+ -[FIPassthroughOperationURLNode fpDomain]
+ -[FIPassthroughOperationURLNode fpItem]
+ -[FIPassthroughOperationURLNode infoNode]
+ -[FIPassthroughOperationURLNode initWithURL:]
+ -[FIPassthroughOperationURLNode isValid]
+ -[FIPassthroughOperationURLNode iteratorWithOptions:]
+ -[FIPassthroughOperationURLNode nodeToMoveOrDelete]
+ -[FIPassthroughOperationURLNode parent]
+ -[FIPassthroughOperationURLNode shortDescription]
+ -[FIPassthroughOperationURLNode source]
+ GCC_except_table1001
+ GCC_except_table1002
+ GCC_except_table1003
+ GCC_except_table1004
+ GCC_except_table1006
+ GCC_except_table1007
+ GCC_except_table1009
+ GCC_except_table1013
+ GCC_except_table1018
+ GCC_except_table1019
+ GCC_except_table1023
+ GCC_except_table1030
+ GCC_except_table1041
+ GCC_except_table1046
+ GCC_except_table1048
+ GCC_except_table1051
+ GCC_except_table1052
+ GCC_except_table1058
+ GCC_except_table1059
+ GCC_except_table1060
+ GCC_except_table1066
+ GCC_except_table1072
+ GCC_except_table1082
+ GCC_except_table1083
+ GCC_except_table1084
+ GCC_except_table1086
+ GCC_except_table1094
+ GCC_except_table1098
+ GCC_except_table1099
+ GCC_except_table1109
+ GCC_except_table1111
+ GCC_except_table1112
+ GCC_except_table1113
+ GCC_except_table1115
+ GCC_except_table1118
+ GCC_except_table1127
+ GCC_except_table1128
+ GCC_except_table1134
+ GCC_except_table1136
+ GCC_except_table1137
+ GCC_except_table1138
+ GCC_except_table1140
+ GCC_except_table1146
+ GCC_except_table1154
+ GCC_except_table1156
+ GCC_except_table1163
+ GCC_except_table1165
+ GCC_except_table1166
+ GCC_except_table1174
+ GCC_except_table1208
+ GCC_except_table1213
+ GCC_except_table1221
+ GCC_except_table1222
+ GCC_except_table1223
+ GCC_except_table1224
+ GCC_except_table1233
+ GCC_except_table1241
+ GCC_except_table1248
+ GCC_except_table1253
+ GCC_except_table1258
+ GCC_except_table1264
+ GCC_except_table1265
+ GCC_except_table1274
+ GCC_except_table1278
+ GCC_except_table1279
+ GCC_except_table1280
+ GCC_except_table1284
+ GCC_except_table1302
+ GCC_except_table1303
+ GCC_except_table1304
+ GCC_except_table1305
+ GCC_except_table1307
+ GCC_except_table1308
+ GCC_except_table1310
+ GCC_except_table1327
+ GCC_except_table1328
+ GCC_except_table1330
+ GCC_except_table1331
+ GCC_except_table1337
+ GCC_except_table1343
+ GCC_except_table1345
+ GCC_except_table1346
+ GCC_except_table1347
+ GCC_except_table1352
+ GCC_except_table1353
+ GCC_except_table1372
+ GCC_except_table1375
+ GCC_except_table1376
+ GCC_except_table1377
+ GCC_except_table1378
+ GCC_except_table1379
+ GCC_except_table1380
+ GCC_except_table1381
+ GCC_except_table1384
+ GCC_except_table1385
+ GCC_except_table1393
+ GCC_except_table1398
+ GCC_except_table1400
+ GCC_except_table1401
+ GCC_except_table1415
+ GCC_except_table1416
+ GCC_except_table1417
+ GCC_except_table1418
+ GCC_except_table1419
+ GCC_except_table1420
+ GCC_except_table1421
+ GCC_except_table1422
+ GCC_except_table1423
+ GCC_except_table1435
+ GCC_except_table1442
+ GCC_except_table1444
+ GCC_except_table1448
+ GCC_except_table1454
+ GCC_except_table1458
+ GCC_except_table1466
+ GCC_except_table1470
+ GCC_except_table1474
+ GCC_except_table1476
+ GCC_except_table1478
+ GCC_except_table1482
+ GCC_except_table1486
+ GCC_except_table1497
+ GCC_except_table1505
+ GCC_except_table1508
+ GCC_except_table1509
+ GCC_except_table1510
+ GCC_except_table1512
+ GCC_except_table1513
+ GCC_except_table1514
+ GCC_except_table1515
+ GCC_except_table1522
+ GCC_except_table1533
+ GCC_except_table1540
+ GCC_except_table1541
+ GCC_except_table1542
+ GCC_except_table1543
+ GCC_except_table1544
+ GCC_except_table1549
+ GCC_except_table1550
+ GCC_except_table1551
+ GCC_except_table1552
+ GCC_except_table1563
+ GCC_except_table1568
+ GCC_except_table1575
+ GCC_except_table1579
+ GCC_except_table1580
+ GCC_except_table1581
+ GCC_except_table1582
+ GCC_except_table1584
+ GCC_except_table1611
+ GCC_except_table1624
+ GCC_except_table1625
+ GCC_except_table1627
+ GCC_except_table1628
+ GCC_except_table1629
+ GCC_except_table1630
+ GCC_except_table1631
+ GCC_except_table1632
+ GCC_except_table1633
+ GCC_except_table1634
+ GCC_except_table1635
+ GCC_except_table1636
+ GCC_except_table1637
+ GCC_except_table1638
+ GCC_except_table1641
+ GCC_except_table340
+ GCC_except_table404
+ GCC_except_table434
+ GCC_except_table470
+ GCC_except_table473
+ GCC_except_table485
+ GCC_except_table490
+ GCC_except_table497
+ GCC_except_table511
+ GCC_except_table530
+ GCC_except_table533
+ GCC_except_table539
+ GCC_except_table542
+ GCC_except_table560
+ GCC_except_table586
+ GCC_except_table589
+ GCC_except_table607
+ GCC_except_table609
+ GCC_except_table617
+ GCC_except_table625
+ GCC_except_table659
+ GCC_except_table671
+ GCC_except_table685
+ GCC_except_table698
+ GCC_except_table726
+ GCC_except_table735
+ GCC_except_table747
+ GCC_except_table750
+ GCC_except_table758
+ GCC_except_table767
+ GCC_except_table770
+ GCC_except_table773
+ GCC_except_table782
+ GCC_except_table784
+ GCC_except_table785
+ GCC_except_table788
+ GCC_except_table790
+ GCC_except_table793
+ GCC_except_table794
+ GCC_except_table796
+ GCC_except_table799
+ GCC_except_table807
+ GCC_except_table810
+ GCC_except_table811
+ GCC_except_table814
+ GCC_except_table819
+ GCC_except_table824
+ GCC_except_table826
+ GCC_except_table827
+ GCC_except_table829
+ GCC_except_table836
+ GCC_except_table841
+ GCC_except_table846
+ GCC_except_table847
+ GCC_except_table849
+ GCC_except_table852
+ GCC_except_table854
+ GCC_except_table865
+ GCC_except_table867
+ GCC_except_table871
+ GCC_except_table877
+ GCC_except_table881
+ GCC_except_table886
+ GCC_except_table891
+ GCC_except_table895
+ GCC_except_table896
+ GCC_except_table897
+ GCC_except_table902
+ GCC_except_table906
+ GCC_except_table912
+ GCC_except_table933
+ GCC_except_table934
+ GCC_except_table938
+ GCC_except_table943
+ GCC_except_table945
+ GCC_except_table971
+ GCC_except_table973
+ GCC_except_table976
+ GCC_except_table978
+ GCC_except_table980
+ GCC_except_table984
+ GCC_except_table990
+ _OBJC_CLASS_$_FIPassthroughOperationURLNode
+ _OBJC_METACLASS_$_FIPassthroughOperationURLNode
+ _SecTaskCreateWithAuditToken
+ _ZNSt3__116__if_likely_elseB9nqe220106IZNS_6vectorINS_4pairIU8__strongP16FPProviderDomainiEENS_9allocatorIS6_EEE12emplace_backIJS6_EEERS6_DpOT_EUlvE_ZNSA_IJS6_EEESB_SE_EUlvE0_EEvbT_T0_
+ __45+[DSQuarantine settleQuarantine:atURL:error:]_block_invoke
+ __OBJC_$_INSTANCE_METHODS_FIPassthroughOperationURLNode
+ __OBJC_$_PROP_LIST_FICustomNode
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSFastEnumeration
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSFastEnumeration
+ __OBJC_CLASS_RO_$_FIPassthroughOperationURLNode
+ __OBJC_LABEL_PROTOCOL_$_NSFastEnumeration
+ __OBJC_METACLASS_RO_$_FIPassthroughOperationURLNode
+ __OBJC_PROTOCOL_$_NSFastEnumeration
+ __Z16static_objc_castI5NSSetIP6FINodeEU8__strongPS3_EPT_T0_
+ __Z16static_objc_castI5NSSetU8__strongPS0_IP6FINodeEEPT_T0_
+ __Z16static_objc_castI8FIDSNodePKvEPT_T0_
+ __Z16static_objc_castI8FIDSNodeU8__strongP29FIPassthroughOperationURLNodeEPT_T0_
+ __Z19kTStringLiteralDataIJLc110ELc111ELc32ELc102ELc111ELc108ELc108ELc111ELc119ELc32ELc85ELc82ELc76EEE
+ __Z31HelperOptionsForScriptingSender16OperationOptionsP6NSData
+ __Z9objc_castI29FIPassthroughOperationURLNodeU8__strongP6FINodeEPT_T0_
+ __Z9objc_castI7NSArrayU8__strongP8NSObjectEPT_T0_
+ __ZGVZL22FINodeOffsetToNodeIvarvE10nodeOffset
+ __ZL23kKeyNodesAssociationKey
+ __ZN10TCFURLInfo10InitializeERK12cstring_view
+ __ZN10TCFURLInfo20POSIXErrorToOSStatusEi
+ __ZN10TCFURLInfo22RenameWithoutReplacingERK12cstring_viewS2_
+ __ZN11TFSIteratorC1EPK7__CFURLPK9__CFArray12LSPropertiesb17FSInfoVirtualType
+ __ZN11TFSIteratorC2EPK7__CFURLPK9__CFArray12LSPropertiesb17FSInfoVirtualType
+ __ZN12cstring_viewC1EP8NSString
+ __ZN12cstring_viewC1ERK7TString
+ __ZN13TNodeIterator27CountByEnumeratingWithStateER22NSFastEnumerationStateNSt3__14spanIP11objc_objectLm18446744073709551615EEE
+ __ZN16TDSHelperContextC1E16OperationOptionsPK10__CFStringP6NSData
+ __ZN16TDSHelperContextC2E16OperationOptionsPK10__CFStringP6NSData
+ __ZN18TDSHelperOperationC2ERK17OperationSelectorPK10__CFString16OperationOptionsP6NSData
+ __ZN18type_traits_extras12CopyAsHelperINSt3__16vectorINS1_4pairIU8__strongP16FPProviderDomainiEENS1_9allocatorIS7_EEEEE16MakeWithCapacityEm
+ __ZN26TDSHelperCopyMoveOperation19ResolvePathsForMoveERKNSt3__110shared_ptrIK18TDSOperationRecordEE
+ __ZN26TDSHelperCopyMoveOperation4MoveERK8TNodePtrS2_RK18TDSOperationRecordPK7TStringbbbRS6_Rb
+ __ZN4TRefIP9__SecTask20TRetainReleasePolicyIS1_EED2Ev
+ __ZN5TNode31SortedDomainsInBulkRequestOrderEP7NSArrayIP16FPProviderDomainE
+ __ZN7StDeferIZN26TDSHelperCopyMoveOperation4MoveERK8TNodePtrS3_RK18TDSOperationRecordPK7TStringbbbRS7_RbE3$_0ED1Ev
+ __ZN7TFSInfo10InitializeEPK7__CFURL12LSPropertiesbbb20ModifyURLCachePolicy
+ __ZN7TFSInfo23ExtendedDirectoryAccessEPK7__CFURL17ExtendedDirAccess
+ __ZN7TFSInfo25InitializeWithExternalURLEPK7__CFURL12LSPropertiesbbb
+ __ZN7TFSInfo26InitializeWithResolveFlagsEPK7__CFURL12LSPropertiesb
+ __ZNK10TCFURLInfo12ResolveFlagsEv
+ __ZNK26TDSHelperCopyMoveOperation19ResolvedPathForNodeERK8TNodePtr
+ __ZNK26TDSHelperCopyMoveOperation25ResolvedSourcePathForItemERK18TDSOperationRecordRK8TNodePtr
+ __ZNK7TFSInfo11DerivedInfoEPK7__CFURL12LSProperties
+ __ZNK7TFSInfo11DerivedInfoERK7TStringb
+ __ZNK7TFSInfo15MoveAndRenameToERKNSt3__110shared_ptrIS_EEPK7TStringRS5_RS6_S9_
+ __ZNK7TFSInfo22FetchExtendedDirAccessEv
+ __ZNK7TString9utf8_sizeEv
+ __ZNKSt3__112__hash_tableINS_17__hash_value_typeI8TNodePtr7TStringEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S3_EENS_4hashIS2_EENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_S8_SC_SA_EENS_9allocatorIS8_EEE4findIS2_EENS_21__hash_const_iteratorIPNS_11__hash_nodeIS4_PvEEEERKT_
+ __ZNKSt3__16ranges7__begin4__fnclB9nqe220106IRNS0_14transform_viewB10llvm18_nuaINS0_11filter_viewB10llvm18_nuaINS0_15take_while_viewB10llvm18_nuaINS0_8subrangeINS_11__wrap_iterIPP13TPropertyInfoEESC_LNS0_13subrange_kindE1EEEZN21THFSPlusPropertyStore21CopyPropertiesForNameERK7TStringbE3$_0EEZNSF_21CopyPropertiesForNameESI_bE3$_1EEZNSF_21CopyPropertiesForNameESI_bE3$_2EEEEDaOT_
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN5TNode31SortedDomainsInBulkRequestOrderEP7NSArrayIP16FPProviderDomainEE3$_3PNS_4pairIU8__strongS5_iEELb0EEEvT1_SE_T0_NS_15iterator_traitsISE_E15difference_typeEb
+ __ZNSt3__112__hash_tableI7TStringNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEE13__move_assignERS8_NS_17integral_constantIbLb1EEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI8TNodePtr7TStringEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S3_EENS_4hashIS2_EENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_S8_SC_SA_EENS_9allocatorIS8_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI8TNodePtr7TStringEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S3_EENS_4hashIS2_EENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_S8_SC_SA_EENS_9allocatorIS8_EEE21__construct_node_hashIJRS7_S3_EEENS_10unique_ptrINS_11__hash_nodeIS4_PvEENS_22__hash_node_destructorINSG_ISO_EEEEEEmDpOT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI8TNodePtr7TStringEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S3_EENS_4hashIS2_EENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_S8_SC_SA_EENS_9allocatorIS8_EEE4findIS2_EENS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI8TNodePtr7TStringEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S3_EENS_4hashIS2_EENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_S8_SC_SA_EENS_9allocatorIS8_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI8TNodePtr7TStringEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S3_EENS_4hashIS2_EENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_S8_SC_SA_EENS_9allocatorIS8_EEED2Ev
+ __ZNSt3__114__split_bufferINS_4pairIU8__strongP16FPProviderDomainiEERNS_9allocatorIS5_EEED2Ev
+ __ZNSt3__116__if_likely_elseB9nqe220106IZNS_6vectorINS_4pairIU8__strongP16FPProviderDomainiEENS_9allocatorIS6_EEE12emplace_backIJS6_EEERS6_DpOT_EUlvE_ZNSA_IJS6_EEESB_SE_EUlvE0_EEvbT_T0_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeI8TNodePtr7TStringEEPvEEEEEclB9nqe220106EPS8_
+ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERZN5TNode31SortedDomainsInBulkRequestOrderEP7NSArrayIP16FPProviderDomainEE3$_3PNS_4pairIU8__strongS5_iEEEEbT1_SE_T0_
+ __ZNSt3__14pairIK7TStringjEC1B9nqe220106IS1_4$_27Li0EEEOT_OT0_
+ __ZNSt3__14pairIKj7TStringEC1B9nqe220106I4$_28S2_Li0EEEOT_OT0_
+ __ZNSt3__16invokeB9nqe220106IRZNK21THFSPlusPropertyStore14UniqueNameListENS_8optionalI8PropertyEEE3$_0JRP13TPropertyInfoEEENS_20__invoke_result_implIvJT_DpT0_EE4typeEOSB_DpOSC_
+ __ZNSt3__16ranges14__find_if_implB9nqe220106INS_11__wrap_iterIPP13TPropertyInfoEENS0_15take_while_viewB10llvm18_nuaINS0_8subrangeIS6_S6_LNS0_13subrange_kindE1EEEZN21THFSPlusPropertyStore21CopyPropertiesForNameERK7TStringbE3$_0E10__sentinelILb1EEENS_17reference_wrapperIZNSB_21CopyPropertiesForNameESE_bE3$_1EENS_8identityEEET_SN_T0_RT1_RT2_
+ __ZNSt3__16vectorINS_4pairIU8__strongP16FPProviderDomainiEENS_9allocatorIS5_EEE16__destroy_vectorclB9nqe220106Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP16FPProviderDomainiEENS_9allocatorIS5_EEE20__throw_length_errorB9nqe220106Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP16FPProviderDomainiEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJS5_EEEPS5_DpOT_
+ __ZNSt3__16vectorINS_4pairIU8__strongP16FPProviderDomainiEENS_9allocatorIS5_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS5_RS7_EE
+ __ZNSt3__16vectorINS_4pairIU8__strongP16FPProviderDomainiEENS_9allocatorIS5_EEE7reserveEm
+ __ZNSt3__17__sort3B9nqe220106INS_17_ClassicAlgPolicyERZN5TNode31SortedDomainsInBulkRequestOrderEP7NSArrayIP16FPProviderDomainEE3$_3PNS_4pairIU8__strongS5_iEELi0EEEbT1_SE_SE_T0_
+ __ZNSt3__17__sort4B9nqe220106INS_17_ClassicAlgPolicyERZN5TNode31SortedDomainsInBulkRequestOrderEP7NSArrayIP16FPProviderDomainEE3$_3PNS_4pairIU8__strongS5_iEELi0EEEvT1_SE_SE_SE_T0_
+ __ZNSt3__17__sort5B9nqe220106INS_17_ClassicAlgPolicyERZN5TNode31SortedDomainsInBulkRequestOrderEP7NSArrayIP16FPProviderDomainEE3$_3PNS_4pairIU8__strongS5_iEELi0EEEvT1_SE_SE_SE_SE_T0_
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB9nqe220106IRPNS_4pairIU8__strongP16FPProviderDomainiEESA_EEvOT_OT0_
+ __ZNSt3__19allocatorINS_4pairIU8__strongP16FPProviderDomainiEEE17allocate_at_leastB9nqe220106Em
+ __ZZL22FINodeOffsetToNodeIvarvE10nodeOffset
+ __ZZL33CarbonCoreExtendedDirectoryAccessPK7__CFURL17ExtendedDirAccessE13kAccessRights
+ __ZZN10TCFURLInfo22RenameWithoutReplacingERK12cstring_viewS2_E11sLocalMutex
+ __ZZN26TDSHelperCopyMoveOperation19ResolvePathsForMoveERKNSt3__110shared_ptrIK18TDSOperationRecordEEENK3$_0clERK8TNodePtr
+ __ZZN26TDSHelperCopyMoveOperation4MoveERK8TNodePtrS2_RK18TDSOperationRecordPK7TStringbbbRS6_RbEN3$_1clEv
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeI8TNodePtr7TStringEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S3_EENS_4hashIS2_EENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_S8_SC_SA_EENS_9allocatorIS8_EEE16__emplace_uniqueB9nqe220106IJRS7_S3_EEENS6_INS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEEbEEDpOT_ENKUlSK_SK_OS3_E_clESK_SK_SV_
+ __ZZZN26TDSHelperCopyMoveOperation4MoveERK8TNodePtrS2_RK18TDSOperationRecordPK7TStringbbbRS6_RbENK3$_0clEvENKUlvE_clEv
+ ___45+[DSQuarantine settleQuarantine:atURL:error:]_block_invoke
+ ___block_descriptor_48_ea8_32c98_ZTSKZN23TFileCoordinationRecord28CopyURLForCoordinatedWritingEPK7__CFURLNS_14WritingOptionsEE3$_0_e24_v24?0"NSURL"8?<v?>16l
+ ___block_descriptor_56_ea8_32c106_ZTSKZN23TFileCoordinationRecord28CopyURLForCoordinatedReadingERKNSt3__110shared_ptrIK10TCFURLInfoEEbE3$_0_e24_v24?0"NSURL"8?<v?>16l
+ _kTCCServiceSystemPolicyAllFiles
+ _objc_getAssociatedObject
+ _objc_msgSend$_URLByInsertingResolveFlags:
+ _objc_msgSend$isOnMainVolume
+ _objc_msgSend$keyNodesForMappingToPresentationNode
+ _objc_msgSend$remapKeyNodesToPresentationNode
+ _objc_msgSend$settleQuarantine:atURL:error:
+ _objc_setAssociatedObject
- GCC_except_table1011
- GCC_except_table1012
- GCC_except_table1022
- GCC_except_table1024
- GCC_except_table1028
- GCC_except_table1042
- GCC_except_table1047
- GCC_except_table1050
- GCC_except_table1053
- GCC_except_table1061
- GCC_except_table1071
- GCC_except_table1073
- GCC_except_table1075
- GCC_except_table1076
- GCC_except_table1080
- GCC_except_table1092
- GCC_except_table1095
- GCC_except_table1100
- GCC_except_table1101
- GCC_except_table1102
- GCC_except_table1103
- GCC_except_table1104
- GCC_except_table1105
- GCC_except_table1117
- GCC_except_table1120
- GCC_except_table1123
- GCC_except_table1125
- GCC_except_table1129
- GCC_except_table1130
- GCC_except_table1133
- GCC_except_table1147
- GCC_except_table1148
- GCC_except_table1149
- GCC_except_table1152
- GCC_except_table1158
- GCC_except_table1159
- GCC_except_table1160
- GCC_except_table1192
- GCC_except_table1197
- GCC_except_table1199
- GCC_except_table1202
- GCC_except_table1204
- GCC_except_table1205
- GCC_except_table1216
- GCC_except_table1220
- GCC_except_table1226
- GCC_except_table1227
- GCC_except_table1229
- GCC_except_table1232
- GCC_except_table1236
- GCC_except_table1239
- GCC_except_table1242
- GCC_except_table1244
- GCC_except_table1246
- GCC_except_table1249
- GCC_except_table1251
- GCC_except_table1261
- GCC_except_table1266
- GCC_except_table1271
- GCC_except_table1276
- GCC_except_table1283
- GCC_except_table1285
- GCC_except_table1290
- GCC_except_table1291
- GCC_except_table1295
- GCC_except_table1296
- GCC_except_table1315
- GCC_except_table1319
- GCC_except_table1320
- GCC_except_table1321
- GCC_except_table1322
- GCC_except_table1323
- GCC_except_table1324
- GCC_except_table1325
- GCC_except_table1341
- GCC_except_table1342
- GCC_except_table1354
- GCC_except_table1359
- GCC_except_table1360
- GCC_except_table1361
- GCC_except_table1362
- GCC_except_table1363
- GCC_except_table1364
- GCC_except_table1367
- GCC_except_table1368
- GCC_except_table1369
- GCC_except_table1386
- GCC_except_table1387
- GCC_except_table1389
- GCC_except_table1390
- GCC_except_table1396
- GCC_except_table1402
- GCC_except_table1403
- GCC_except_table1404
- GCC_except_table1405
- GCC_except_table1406
- GCC_except_table1409
- GCC_except_table1410
- GCC_except_table1411
- GCC_except_table1412
- GCC_except_table1426
- GCC_except_table1431
- GCC_except_table1433
- GCC_except_table1443
- GCC_except_table1452
- GCC_except_table1453
- GCC_except_table1457
- GCC_except_table1461
- GCC_except_table1465
- GCC_except_table1467
- GCC_except_table1468
- GCC_except_table1469
- GCC_except_table1473
- GCC_except_table1487
- GCC_except_table1488
- GCC_except_table1498
- GCC_except_table1499
- GCC_except_table1500
- GCC_except_table1503
- GCC_except_table1519
- GCC_except_table1520
- GCC_except_table1525
- GCC_except_table1526
- GCC_except_table1527
- GCC_except_table1528
- GCC_except_table1529
- GCC_except_table1536
- GCC_except_table1537
- GCC_except_table1538
- GCC_except_table1548
- GCC_except_table1560
- GCC_except_table1564
- GCC_except_table1565
- GCC_except_table1566
- GCC_except_table1567
- GCC_except_table1569
- GCC_except_table1571
- GCC_except_table1574
- GCC_except_table1577
- GCC_except_table1578
- GCC_except_table1583
- GCC_except_table1585
- GCC_except_table1587
- GCC_except_table1588
- GCC_except_table1590
- GCC_except_table1591
- GCC_except_table1594
- GCC_except_table1596
- GCC_except_table1597
- GCC_except_table1599
- GCC_except_table1610
- GCC_except_table1626
- GCC_except_table213
- GCC_except_table322
- GCC_except_table367
- GCC_except_table395
- GCC_except_table420
- GCC_except_table424
- GCC_except_table436
- GCC_except_table445
- GCC_except_table466
- GCC_except_table467
- GCC_except_table471
- GCC_except_table474
- GCC_except_table475
- GCC_except_table491
- GCC_except_table503
- GCC_except_table504
- GCC_except_table540
- GCC_except_table548
- GCC_except_table567
- GCC_except_table568
- GCC_except_table571
- GCC_except_table585
- GCC_except_table587
- GCC_except_table590
- GCC_except_table600
- GCC_except_table603
- GCC_except_table619
- GCC_except_table627
- GCC_except_table628
- GCC_except_table632
- GCC_except_table636
- GCC_except_table644
- GCC_except_table649
- GCC_except_table657
- GCC_except_table667
- GCC_except_table670
- GCC_except_table672
- GCC_except_table707
- GCC_except_table708
- GCC_except_table749
- GCC_except_table753
- GCC_except_table765
- GCC_except_table774
- GCC_except_table777
- GCC_except_table786
- GCC_except_table789
- GCC_except_table798
- GCC_except_table800
- GCC_except_table802
- GCC_except_table804
- GCC_except_table805
- GCC_except_table806
- GCC_except_table815
- GCC_except_table817
- GCC_except_table821
- GCC_except_table825
- GCC_except_table831
- GCC_except_table834
- GCC_except_table845
- GCC_except_table848
- GCC_except_table850
- GCC_except_table853
- GCC_except_table863
- GCC_except_table866
- GCC_except_table870
- GCC_except_table876
- GCC_except_table880
- GCC_except_table883
- GCC_except_table885
- GCC_except_table889
- GCC_except_table890
- GCC_except_table893
- GCC_except_table894
- GCC_except_table899
- GCC_except_table903
- GCC_except_table905
- GCC_except_table911
- GCC_except_table915
- GCC_except_table921
- GCC_except_table923
- GCC_except_table926
- GCC_except_table942
- GCC_except_table948
- GCC_except_table950
- GCC_except_table968
- GCC_except_table970
- GCC_except_table972
- GCC_except_table982
- GCC_except_table983
- GCC_except_table987
- GCC_except_table992
- GCC_except_table993
- GCC_except_table995
- GCC_except_table996
- GCC_except_table997
- GCC_except_table998
- __44+[DSQuarantine applyQuarantine:toURL:error:]_block_invoke
- __Z16static_objc_castI8FIDSNodePvEPT_T0_
- __Z19kTStringLiteralDataIJLc99ELc111ELc109ELc46ELc97ELc112ELc112ELc108ELc101ELc46EEE
- __Z20IsDomainDisconnectedP16FPProviderDomain
- __ZGVZ17FIDSNodeFromTNodePK5TNodeE10nodeOffset
- __ZL15MakeNoFollowURLP5NSURL
- __ZL15TagsDictForNodeP6FINodeb
- __ZL20NormalizeNoFollowURLP5NSURLRb
- __ZN10TCFURLInfo10InitializeEPKc
- __ZN10TCFURLInfo22RenameWithoutReplacingEPKcS1_
- __ZN11TFSIteratorC1EPK7__CFURLPK9__CFArray12LSPropertiesb
- __ZN11TFSIteratorC2EPK7__CFURLPK9__CFArray12LSPropertiesb
- __ZN16TDSHelperContextC1E16OperationOptionsPK10__CFString
- __ZN16TDSHelperContextC2E16OperationOptionsPK10__CFString
- __ZN18TDSHelperOperationC2ERK17OperationSelectorPK10__CFString16OperationOptions
- __ZN18type_traits_extras12CopyAsHelperIU8__strongP14NSMutableArrayIP5FITagEE16MakeWithCapacityEm
- __ZN26IDContainerIteratorAdaptorI14NSMutableArrayIP16FPProviderDomainEE17NSForwardIteratorIS3_EC2EPS3_
- __ZN26IDContainerIteratorAdaptorI14NSMutableArrayIP16FPProviderDomainEEC2ElPS3_
- __ZN26TDSHelperCopyMoveOperation4MoveERK8TNodePtrS2_PK7TStringbbbRS3_Rb
- __ZN26TDSHelperCopyMoveOperationC2ERK17OperationSelectorPK10__CFString16OperationOptionsP6NSData
- __ZN29TDSHelperNewFSObjectOperationC2ERK17OperationSelectorPK10__CFString16OperationOptionsP6NSData
- __ZN4TRefIP9__SecTask21CFRetainReleasePolicyED2Ev
- __ZN7StDeferIZN26TDSHelperCopyMoveOperation4MoveERK8TNodePtrS3_PK7TStringbbbRS4_RbE3$_0ED1Ev
- __ZN7TFSInfo10initializeEPK7__CFURL12LSPropertiesbbb20ModifyURLCachePolicy
- __ZN7TFSInfo25initializeWithExternalURLEPK7__CFURL12LSPropertiesbbb
- __ZNK18TDSHelperOperation19ScriptingAuditTokenEv
- __ZNK26TDSHelperCopyMoveOperation19ScriptingAuditTokenEv
- __ZNK29TDSHelperNewFSObjectOperation19ScriptingAuditTokenEv
- __ZNK7TFSInfo15MoveAndRenameToERKNSt3__110shared_ptrIS_EEPK7TStringRS5_
- __ZNSt3__14pairIK7TStringjEC1B9nqe220106IS1_4$_26Li0EEEOT_OT0_
- __ZNSt3__14pairIKj7TStringEC1B9nqe220106I4$_26S2_Li0EEEOT_OT0_
- __ZNSt3__16vectorI13TPropertyInfoNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
- __ZZ17FIDSNodeFromTNodePK5TNodeE10nodeOffset
- __ZZN10TCFURLInfo22RenameWithoutReplacingEPKcS1_E11sLocalMutex
- __ZZN26TDSHelperCopyMoveOperation4MoveERK8TNodePtrS2_PK7TStringbbbRS3_RbEN3$_1clEv
- __ZZZN26TDSHelperCopyMoveOperation4MoveERK8TNodePtrS2_PK7TStringbbbRS3_RbENK3$_0clEvENKUlvE_clEv
- ___44+[DSQuarantine applyQuarantine:toURL:error:]_block_invoke
- ___block_descriptor_56_ea8_32c98_ZTSKZN23TFileCoordinationRecord28CopyURLForCoordinatedWritingEPK7__CFURLNS_14WritingOptionsEE3$_0_e24_v24?0"NSURL"8?<v?>16l
- ___block_descriptor_64_ea8_32c106_ZTSKZN23TFileCoordinationRecord28CopyURLForCoordinatedReadingERKNSt3__110shared_ptrIK10TCFURLInfoEEbE3$_0_e24_v24?0"NSURL"8?<v?>16l
CStrings:
+ "<%@ %p '%@'>"
+ "<none>"
+ "Could not resolve '%{public}@' for a move"
+ "Could not serialize the default quarantine record"
+ "Ignoring malformed scripting audit token (%lu bytes)"
+ "Lookup of '%{public}@' needed FP's cache, but nothing is monitoring the provider list"
+ "Mapping %lu key node(s) to presentation node %{public}@"
+ "No key nodes to map to presentation node %{public}@"
+ "Stored %lu key node(s) on %{public}@"
+ "Unwinding after error - %{public}@"
+ "_node ivar not at expected location, expected 8, got %td"
+ "com.apple.private.tcc.allow"
+ "iCloud Drive container is already mapped to a custom node %{public}@ iCloud navigation may be broken"
+ "initialization of passthrough info rejecting url %{public}@"
+ "kPassthroughOperationURL"
+ "no follow URL"
+ "rename refused a symlinked component on a resolved path\n\t old: `%{public}@`\n\t new: `%{public}@`"
+ "settleQuarantine:atURL:error: failed to get url wrapper: %@"
+ "settleQuarantine:atURL:error: quarantine did not reach all of %{public}@ (first failure at %{public}@): %@"
- "applyQuarantine:toURL:error: failed to get url wrapper: %@"
```
