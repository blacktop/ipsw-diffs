## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon`

```diff

-725.0.13.0.0
-  __TEXT.__text: 0xe4544
-  __TEXT.__auth_stubs: 0x2090
-  __TEXT.__objc_methlist: 0xa3ac
-  __TEXT.__const: 0xc00
-  __TEXT.__cstring: 0x9270
-  __TEXT.__swift5_typeref: 0x330
-  __TEXT.__oslogstring: 0xe3be
-  __TEXT.__constg_swiftt: 0x2ec
-  __TEXT.__swift5_reflstr: 0x113
-  __TEXT.__swift5_fieldmd: 0x18c
+725.40.5.0.0
+  __TEXT.__text: 0xe7574
+  __TEXT.__auth_stubs: 0x2180
+  __TEXT.__objc_methlist: 0xa46c
+  __TEXT.__const: 0xcc0
+  __TEXT.__cstring: 0x9558
+  __TEXT.__swift5_typeref: 0x390
+  __TEXT.__oslogstring: 0xe5a4
+  __TEXT.__constg_swiftt: 0x310
+  __TEXT.__swift5_reflstr: 0x254
+  __TEXT.__swift5_fieldmd: 0x220
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_assocty: 0x138
-  __TEXT.__swift5_proto: 0x70
-  __TEXT.__swift5_types: 0x58
+  __TEXT.__swift5_proto: 0x78
+  __TEXT.__swift5_types: 0x60
+  __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_protos: 0x4
   __TEXT.__gcc_except_tab: 0x2b14
   __TEXT.__ustring: 0x16c
-  __TEXT.__unwind_info: 0x2100
+  __TEXT.__unwind_info: 0x2158
   __TEXT.__eh_frame: 0x160
-  __TEXT.__objc_classname: 0x1dd2
-  __TEXT.__objc_methname: 0x135b0
-  __TEXT.__objc_methtype: 0x40f9
-  __TEXT.__objc_stubs: 0xb9e0
-  __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x1a58
+  __TEXT.__objc_classname: 0x1dec
+  __TEXT.__objc_methname: 0x13806
+  __TEXT.__objc_methtype: 0x41ae
+  __TEXT.__objc_stubs: 0xbae0
+  __DATA_CONST.__got: 0x378
+  __DATA_CONST.__const: 0x1a38
   __DATA_CONST.__objc_classlist: 0x5c0
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x4a0
+  __DATA_CONST.__objc_protolist: 0x4a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34f0
+  __DATA_CONST.__objc_selrefs: 0x3548
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x4e8
-  __DATA_CONST.__objc_arraydata: 0x2a8
-  __AUTH_CONST.__auth_got: 0x1058
-  __AUTH_CONST.__const: 0xb80
-  __AUTH_CONST.__cfstring: 0x45c0
-  __AUTH_CONST.__objc_const: 0x16198
+  __DATA_CONST.__objc_arraydata: 0x2d0
+  __AUTH_CONST.__auth_got: 0x10d0
+  __AUTH_CONST.__const: 0xcd0
+  __AUTH_CONST.__cfstring: 0x46a0
+  __AUTH_CONST.__objc_const: 0x16298
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH_CONST.__objc_intobj: 0x1470
-  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__objc_intobj: 0x14e8
+  __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH.__objc_data: 0xa40
   __AUTH.__data: 0x80
-  __DATA.__objc_ivar: 0xbcc
-  __DATA.__data: 0x37f8
+  __DATA.__objc_ivar: 0xbdc
+  __DATA.__data: 0x3898
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xc38
+  __DATA.__bss: 0xd48
+  __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x3110
   __DATA_DIRTY.__data: 0x140
   __DATA_DIRTY.__bss: 0x4f0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B1EA18A7-097D-39EB-8433-5C3FBE4BB7AD
-  Functions: 3307
-  Symbols:   11501
-  CStrings:  6107
+  UUID: 8E758027-60FD-3479-A958-BEE96E9A4272
+  Functions: 3353
+  Symbols:   11569
+  CStrings:  6168
 
Symbols:
+ +[MCMContainerClassPath _inLibraryRepairBlock_createURLIfNecessary:mode:owner:dataProtectionClass:quarantine:exists:error:]
+ -[MCMContainerClassPath _createURLIfNecessary:mode:owner:dataProtectionClass:quarantine:error:]
+ -[MCMContainerPath _createURLIfNecessary:mode:owner:dataProtectionClass:quarantine:exists:error:]
+ -[MCMContainerPath createIfNecessaryWithDataProtectionClass:quarantine:error:]
+ -[MCMContainerSchema _actionsFromVersion:toTargetVersion:context:error:]
+ -[MCMContainerSchema _interpolationReplacementsWithError:]
+ -[MCMContainerSchemaActionBase fmDir]
+ -[MCMContainerSchemaActionBase fmQuarantine]
+ -[MCMContainerSchemaActionBase setFmDir:]
+ -[MCMContainerSchemaActionBase setFmQuarantine:]
+ -[MCMFileManager fsMinimallySanitizedStringFromString:]
+ -[MCMFileManager quarantineNeededForDirectoryURL:]
+ -[MCMFileManager quarantineURL:identifier:error:]
+ -[MCMGlobalConfiguration csIdentifier]
+ -[MCMUserIdentity kernelPersonaType]
+ GCC_except_table1043
+ GCC_except_table1052
+ GCC_except_table1056
+ GCC_except_table1094
+ GCC_except_table1095
+ GCC_except_table1107
+ GCC_except_table1109
+ GCC_except_table1113
+ GCC_except_table1118
+ GCC_except_table1121
+ GCC_except_table1123
+ GCC_except_table1129
+ GCC_except_table1135
+ GCC_except_table1138
+ GCC_except_table1144
+ GCC_except_table1147
+ GCC_except_table1149
+ GCC_except_table1155
+ GCC_except_table1158
+ GCC_except_table1160
+ GCC_except_table1168
+ GCC_except_table1184
+ GCC_except_table1194
+ GCC_except_table1199
+ GCC_except_table1203
+ GCC_except_table1205
+ GCC_except_table1257
+ GCC_except_table1267
+ GCC_except_table1298
+ GCC_except_table1348
+ GCC_except_table1352
+ GCC_except_table1353
+ GCC_except_table1572
+ GCC_except_table1621
+ GCC_except_table1710
+ GCC_except_table1855
+ GCC_except_table1893
+ GCC_except_table1897
+ GCC_except_table1900
+ GCC_except_table1903
+ GCC_except_table1918
+ GCC_except_table1922
+ GCC_except_table1957
+ GCC_except_table1963
+ GCC_except_table2035
+ GCC_except_table2038
+ GCC_except_table2149
+ GCC_except_table2286
+ GCC_except_table2303
+ GCC_except_table2304
+ GCC_except_table2380
+ GCC_except_table2437
+ GCC_except_table2452
+ GCC_except_table2512
+ GCC_except_table2524
+ GCC_except_table2584
+ GCC_except_table2594
+ GCC_except_table2619
+ GCC_except_table2648
+ GCC_except_table2670
+ GCC_except_table2674
+ GCC_except_table2677
+ GCC_except_table2681
+ GCC_except_table2737
+ GCC_except_table2826
+ GCC_except_table2874
+ GCC_except_table2877
+ GCC_except_table2948
+ GCC_except_table402
+ GCC_except_table495
+ GCC_except_table685
+ GCC_except_table686
+ GCC_except_table762
+ GCC_except_table773
+ GCC_except_table835
+ GCC_except_table911
+ GCC_except_table956
+ GCC_except_table987
+ GCC_except_table989
+ _AnalyticsSendEventLazy
+ _OBJC_IVAR_$_MCMContainerSchemaActionBase._fmDir
+ _OBJC_IVAR_$_MCMContainerSchemaActionBase._fmQuarantine
+ _OBJC_IVAR_$_MCMGlobalConfiguration._csIdentifier
+ _OBJC_IVAR_$_MCMUserIdentity._kernelPersonaType
+ __Block_copy
+ __Block_release
+ __OBJC_$_PROP_LIST_MCMContainerPath.190
+ __OBJC_$_PROP_LIST_MCMGlobalConfiguration.204
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MCMFileManagerQuarantines
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MCMFileManagerQuarantines
+ __OBJC_LABEL_PROTOCOL_$_MCMFileManagerQuarantines
+ __OBJC_PROTOCOL_$_MCMFileManagerQuarantines
+ __PROTOCOLS_MCMAnalytics.4
+ ___49-[MCMFileManager quarantineURL:identifier:error:]_block_invoke
+ ___49-[MCMFileManager quarantineURL:identifier:error:]_block_invoke.589
+ ___49-[MCMFileManager quarantineURL:identifier:error:]_block_invoke.595
+ ___49-[MCMFileManager quarantineURL:identifier:error:]_block_invoke.601
+ ___52-[MCMContainerSchemaActionBase backupFileURL:error:]_block_invoke.142
+ ___52-[MCMContainerSchemaActionBase backupFileURL:error:]_block_invoke.148
+ ___52-[MCMContainerSchemaActionBase backupFileURL:error:]_block_invoke.154
+ ___52-[MCMContainerSchemaActionBase backupFileURL:error:]_block_invoke.160
+ ___55-[MCMFileManager _fixPOSIXPermsOnFD:FTSENT:stat:error:]_block_invoke.665
+ ___71+[MCMContainerSchemaActionBase actionWithName:arguments:context:error:]_block_invoke.122
+ ___71+[MCMContainerSchemaActionBase actionWithName:arguments:context:error:]_block_invoke.128
+ ___73-[MCMContainerSchemaActionBase makedirAtURL:followTerminalSymlink:error:]_block_invoke.174
+ ___73-[MCMContainerSchemaActionBase makedirAtURL:followTerminalSymlink:error:]_block_invoke.182
+ ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.630
+ ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.636
+ ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.642
+ ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.648
+ ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.654
+ ___95-[MCMContainerClassPath _createURLIfNecessary:mode:owner:dataProtectionClass:quarantine:error:]_block_invoke
+ ___97-[MCMContainerPath _createURLIfNecessary:mode:owner:dataProtectionClass:quarantine:exists:error:]_block_invoke
+ ___Block_byref_object_copy_.10022
+ ___Block_byref_object_copy_.1135
+ ___Block_byref_object_copy_.11817
+ ___Block_byref_object_copy_.12513
+ ___Block_byref_object_copy_.12858
+ ___Block_byref_object_copy_.13420
+ ___Block_byref_object_copy_.14277
+ ___Block_byref_object_copy_.14633
+ ___Block_byref_object_copy_.14894
+ ___Block_byref_object_copy_.2533
+ ___Block_byref_object_copy_.3286
+ ___Block_byref_object_copy_.3960
+ ___Block_byref_object_copy_.4355
+ ___Block_byref_object_copy_.5092
+ ___Block_byref_object_copy_.5362
+ ___Block_byref_object_copy_.7313
+ ___Block_byref_object_copy_.7845
+ ___Block_byref_object_copy_.8999
+ ___Block_byref_object_copy_.9191
+ ___Block_byref_object_copy_.9325
+ ___Block_byref_object_copy_.9793
+ ___Block_byref_object_dispose_.10023
+ ___Block_byref_object_dispose_.1136
+ ___Block_byref_object_dispose_.11818
+ ___Block_byref_object_dispose_.12514
+ ___Block_byref_object_dispose_.12859
+ ___Block_byref_object_dispose_.13421
+ ___Block_byref_object_dispose_.14278
+ ___Block_byref_object_dispose_.14634
+ ___Block_byref_object_dispose_.14895
+ ___Block_byref_object_dispose_.2534
+ ___Block_byref_object_dispose_.3287
+ ___Block_byref_object_dispose_.3961
+ ___Block_byref_object_dispose_.4356
+ ___Block_byref_object_dispose_.5093
+ ___Block_byref_object_dispose_.5363
+ ___Block_byref_object_dispose_.7314
+ ___Block_byref_object_dispose_.7846
+ ___Block_byref_object_dispose_.9000
+ ___Block_byref_object_dispose_.9192
+ ___Block_byref_object_dispose_.9326
+ ___Block_byref_object_dispose_.9794
+ ___block_descriptor_55_e8_32s40s_e19_B24?0"NSURL"8^16ls32l8s40l8
+ ___block_descriptor_63_e8_32s40s48r_e19_B24?0"NSURL"8^16ls32l8s40l8r48l8
+ ___block_literal_global.10919
+ ___block_literal_global.11859
+ ___block_literal_global.12.11857
+ ___block_literal_global.12064
+ ___block_literal_global.1209
+ ___block_literal_global.1271
+ ___block_literal_global.12867
+ ___block_literal_global.13219
+ ___block_literal_global.13402
+ ___block_literal_global.13682
+ ___block_literal_global.13885
+ ___block_literal_global.1397
+ ___block_literal_global.14625
+ ___block_literal_global.14714
+ ___block_literal_global.14734
+ ___block_literal_global.1779
+ ___block_literal_global.2648
+ ___block_literal_global.5069
+ ___block_literal_global.5408
+ ___block_literal_global.6580
+ ___block_literal_global.7205
+ ___block_literal_global.7749
+ ___block_literal_global.8358
+ ___block_literal_global.8629
+ ___block_literal_global.9450
+ ___block_literal_global.9547
+ ___swift_memcpy96_8
+ _block_copy_helper
+ _block_copy_helper.8
+ _block_descriptor
+ _block_descriptor.10
+ _block_destroy_helper
+ _block_destroy_helper.9
+ _container_audit_token_copy_executable_name_with_pid
+ _container_codesign_get_current_identifier
+ _container_qtn_error
+ _defaultManager.onceToken.9439
+ _gCMQuarantineSeam
+ _objc_msgSend$_actionsFromVersion:toTargetVersion:context:error:
+ _objc_msgSend$_createURLIfNecessary:mode:owner:dataProtectionClass:quarantine:error:
+ _objc_msgSend$_createURLIfNecessary:mode:owner:dataProtectionClass:quarantine:exists:error:
+ _objc_msgSend$_inLibraryRepairBlock_createURLIfNecessary:mode:owner:dataProtectionClass:quarantine:exists:error:
+ _objc_msgSend$_interpolationReplacementsWithError:
+ _objc_msgSend$createIfNecessaryWithDataProtectionClass:quarantine:error:
+ _objc_msgSend$csIdentifier
+ _objc_msgSend$fmQuarantine
+ _objc_msgSend$fsMinimallySanitizedStringFromString:
+ _objc_msgSend$kernelPersonaType
+ _objc_msgSend$pathExtension
+ _objc_msgSend$quarantineNeededForDirectoryURL:
+ _objc_msgSend$quarantineURL:identifier:error:
+ _objc_msgSend$recordAmbiguousPersonaRequestWithIdentifier:proxiedIdentifier:proximateIdentifier:explicitPersonaType:legacyPersonaPolicy:propagationFailed:containerClass:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objectdestroyTm
+ _sharedInstance.instance.12377
+ _sharedInstance.onceToken.10325
+ _sharedInstance.onceToken.12376
+ _swift_deallocObject
+ _swift_initStackObject
+ _swift_setDeallocating
+ _symbolic SS
+ _symbolic SSSg
+ _symbolic SS_So8NSObjectCt
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic _____ So12MCMAnalyticsC22ContainerManagerCommonE21AmbiguousPersonaEvent33_99B0A2C63C90E9410251F74CFD176766LLV
+ _symbolic _____ s5Int32V
+ _symbolic _____ySSSo8NSObjectCG s18_DictionaryStorageC
+ _symbolic _____ySS_So8NSObjectCtG s23_ContiguousArrayStorageC
+ _time
+ _type_layout_string So12MCMAnalyticsC22ContainerManagerCommonE21AmbiguousPersonaEvent33_99B0A2C63C90E9410251F74CFD176766LLV
- +[MCMContainerClassPath _inLibraryRepairBlock_createURLIfNecessary:mode:owner:dataProtectionClass:exists:error:]
- -[MCMContainerClassPath _createURLIfNecessary:mode:owner:dataProtectionClass:error:]
- -[MCMContainerPath _createURLIfNecessary:mode:owner:dataProtectionClass:exists:error:]
- -[MCMContainerPath createIfNecessaryWithDataProtectionClass:error:]
- -[MCMContainerSchema _actionsFromVersion:toTargetVersion:context:]
- -[MCMContainerSchema _interpolationReplacements]
- GCC_except_table1036
- GCC_except_table1045
- GCC_except_table1049
- GCC_except_table1087
- GCC_except_table1088
- GCC_except_table1100
- GCC_except_table1102
- GCC_except_table1106
- GCC_except_table1111
- GCC_except_table1114
- GCC_except_table1116
- GCC_except_table1122
- GCC_except_table1124
- GCC_except_table1126
- GCC_except_table1128
- GCC_except_table1137
- GCC_except_table1142
- GCC_except_table1148
- GCC_except_table1151
- GCC_except_table1153
- GCC_except_table1161
- GCC_except_table1177
- GCC_except_table1187
- GCC_except_table1192
- GCC_except_table1196
- GCC_except_table1198
- GCC_except_table1250
- GCC_except_table1260
- GCC_except_table1291
- GCC_except_table1339
- GCC_except_table1341
- GCC_except_table1345
- GCC_except_table1559
- GCC_except_table1608
- GCC_except_table1697
- GCC_except_table1842
- GCC_except_table1880
- GCC_except_table1884
- GCC_except_table1887
- GCC_except_table1890
- GCC_except_table1905
- GCC_except_table1909
- GCC_except_table1944
- GCC_except_table1950
- GCC_except_table2022
- GCC_except_table2025
- GCC_except_table2136
- GCC_except_table2273
- GCC_except_table2290
- GCC_except_table2291
- GCC_except_table2367
- GCC_except_table2424
- GCC_except_table2439
- GCC_except_table2499
- GCC_except_table2511
- GCC_except_table2571
- GCC_except_table2581
- GCC_except_table2606
- GCC_except_table2635
- GCC_except_table2657
- GCC_except_table2661
- GCC_except_table2664
- GCC_except_table2668
- GCC_except_table2724
- GCC_except_table2813
- GCC_except_table2861
- GCC_except_table2864
- GCC_except_table2935
- GCC_except_table396
- GCC_except_table488
- GCC_except_table678
- GCC_except_table679
- GCC_except_table755
- GCC_except_table766
- GCC_except_table828
- GCC_except_table904
- GCC_except_table949
- GCC_except_table980
- GCC_except_table982
- __OBJC_$_PROP_LIST_MCMContainerPath.189
- __OBJC_$_PROP_LIST_MCMGlobalConfiguration.196
- __PROTOCOLS_MCMAnalytics.3
- ___30-[MCMCommandCrashTest execute]_block_invoke
- ___52-[MCMContainerSchemaActionBase backupFileURL:error:]_block_invoke.141
- ___52-[MCMContainerSchemaActionBase backupFileURL:error:]_block_invoke.147
- ___52-[MCMContainerSchemaActionBase backupFileURL:error:]_block_invoke.153
- ___52-[MCMContainerSchemaActionBase backupFileURL:error:]_block_invoke.159
- ___55-[MCMFileManager _fixPOSIXPermsOnFD:FTSENT:stat:error:]_block_invoke.627
- ___71+[MCMContainerSchemaActionBase actionWithName:arguments:context:error:]_block_invoke.121
- ___71+[MCMContainerSchemaActionBase actionWithName:arguments:context:error:]_block_invoke.127
- ___73-[MCMContainerSchemaActionBase makedirAtURL:followTerminalSymlink:error:]_block_invoke.176
- ___84-[MCMContainerClassPath _createURLIfNecessary:mode:owner:dataProtectionClass:error:]_block_invoke
- ___86-[MCMContainerPath _createURLIfNecessary:mode:owner:dataProtectionClass:exists:error:]_block_invoke
- ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.592
- ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.598
- ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.604
- ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.610
- ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.616
- ___Block_byref_object_copy_.1132
- ___Block_byref_object_copy_.11784
- ___Block_byref_object_copy_.12479
- ___Block_byref_object_copy_.12824
- ___Block_byref_object_copy_.13382
- ___Block_byref_object_copy_.14238
- ___Block_byref_object_copy_.14594
- ___Block_byref_object_copy_.14852
- ___Block_byref_object_copy_.2504
- ___Block_byref_object_copy_.3276
- ___Block_byref_object_copy_.3942
- ___Block_byref_object_copy_.4340
- ___Block_byref_object_copy_.5077
- ___Block_byref_object_copy_.5349
- ___Block_byref_object_copy_.7283
- ___Block_byref_object_copy_.7816
- ___Block_byref_object_copy_.8969
- ___Block_byref_object_copy_.9161
- ___Block_byref_object_copy_.9295
- ___Block_byref_object_copy_.9763
- ___Block_byref_object_copy_.9992
- ___Block_byref_object_dispose_.1133
- ___Block_byref_object_dispose_.11785
- ___Block_byref_object_dispose_.12480
- ___Block_byref_object_dispose_.12825
- ___Block_byref_object_dispose_.13383
- ___Block_byref_object_dispose_.14239
- ___Block_byref_object_dispose_.14595
- ___Block_byref_object_dispose_.14853
- ___Block_byref_object_dispose_.2505
- ___Block_byref_object_dispose_.3277
- ___Block_byref_object_dispose_.3943
- ___Block_byref_object_dispose_.4341
- ___Block_byref_object_dispose_.5078
- ___Block_byref_object_dispose_.5350
- ___Block_byref_object_dispose_.7284
- ___Block_byref_object_dispose_.7817
- ___Block_byref_object_dispose_.8970
- ___Block_byref_object_dispose_.9162
- ___Block_byref_object_dispose_.9296
- ___Block_byref_object_dispose_.9764
- ___Block_byref_object_dispose_.9993
- ___block_descriptor_32_e12_v24?0^v8Q16l
- ___block_descriptor_54_e8_32s40s_e19_B24?0"NSURL"8^16ls32l8s40l8
- ___block_descriptor_62_e8_32s40s48r_e19_B24?0"NSURL"8^16ls32l8s40l8r48l8
- ___block_literal_global.10887
- ___block_literal_global.11826
- ___block_literal_global.12.11824
- ___block_literal_global.12031
- ___block_literal_global.1207
- ___block_literal_global.1269
- ___block_literal_global.12833
- ___block_literal_global.1292
- ___block_literal_global.13181
- ___block_literal_global.13364
- ___block_literal_global.13644
- ___block_literal_global.13846
- ___block_literal_global.1395
- ___block_literal_global.14586
- ___block_literal_global.14675
- ___block_literal_global.14695
- ___block_literal_global.1755
- ___block_literal_global.2626
- ___block_literal_global.5054
- ___block_literal_global.5395
- ___block_literal_global.6551
- ___block_literal_global.7175
- ___block_literal_global.7719
- ___block_literal_global.8329
- ___block_literal_global.8600
- ___block_literal_global.9420
- ___block_literal_global.9517
- _chown
- _container_codesign_copy_current_identifier
- _defaultManager.onceToken.9409
- _dirfd
- _getegid
- _mkdir
- _mkpath_np
- _objc_msgSend$_actionsFromVersion:toTargetVersion:context:
- _objc_msgSend$_createURLIfNecessary:mode:owner:dataProtectionClass:error:
- _objc_msgSend$_createURLIfNecessary:mode:owner:dataProtectionClass:exists:error:
- _objc_msgSend$_inLibraryRepairBlock_createURLIfNecessary:mode:owner:dataProtectionClass:exists:error:
- _objc_msgSend$_interpolationReplacements
- _objc_msgSend$createIfNecessaryWithDataProtectionClass:error:
- _objc_msgSend$initWithBytesNoCopy:length:encoding:deallocator:
- _sharedInstance.instance.12343
- _sharedInstance.onceToken.10294
- _sharedInstance.onceToken.12342
CStrings:
+ "-[MCMFileManager quarantineURL:identifier:error:]_block_invoke"
+ "20:33:49"
+ "@\"<MCMFileManagerCreatesDirectories>\""
+ "@\"<MCMFileManagerQuarantines>\""
+ "@\"NSDictionary\"8@?0"
+ "B32@0:8i16B20^@24"
+ "B52@0:8@16S24@28i36B40^@44"
+ "B60@0:8@16S24@28i36B40^B44^@52"
+ "Codesign identifier [%@] has invalid characters"
+ "Could not apply quarantine to path [%s]; error = %s"
+ "Could not init quarantine structure from path [%s]; error = %s"
+ "Could not set quarantine flags for path [%s]; error = %s"
+ "Could not set quarantine identifier for path [%s]; error = %s"
+ "Failed to quarantine dir at [%@]: %@"
+ "Failed to quarantine sub-dir at %@"
+ "MCMFileManagerQuarantines"
+ "MobileContainerManager-725.40.5~288"
+ "Quarantined [%s]"
+ "Responding CA event %s"
+ "Sep 16 2025"
+ "Submitting CA event %s"
+ "T@\"<MCMFileManagerCreatesDirectories>\",&,N,V_fmDir"
+ "T@\"<MCMFileManagerQuarantines>\",&,N,V_fmQuarantine"
+ "T@\"NSString\",R,N,V_csIdentifier"
+ "Unable to fetch current persona info"
+ "Unable to fetch current persona originator"
+ "Unable to fetch current persona originator info; personaid = %u"
+ "Unable to fetch current persona proximate"
+ "Unable to fetch current persona proximate info; personaid = %u"
+ "Unable to fetch originator procpath, pid = %d"
+ "_actionsFromVersion:toTargetVersion:context:error:"
+ "_createURLIfNecessary:mode:owner:dataProtectionClass:quarantine:error:"
+ "_createURLIfNecessary:mode:owner:dataProtectionClass:quarantine:exists:error:"
+ "_csIdentifier"
+ "_fmDir"
+ "_fmQuarantine"
+ "_inLibraryRepairBlock_createURLIfNecessary:mode:owner:dataProtectionClass:quarantine:exists:error:"
+ "_interpolationReplacementsWithError:"
+ "_kernelPersonaType"
+ "appex"
+ "bundle"
+ "com.apple.containermanager.ambiguous-persona"
+ "createIfNecessaryWithDataProtectionClass:quarantine:error:"
+ "csIdentifier"
+ "explicitPersonaType"
+ "fmDir"
+ "fmQuarantine"
+ "fsMinimallySanitizedStringFromString:"
+ "kernelPersonaType"
+ "originatorLaunchPersonaType"
+ "originatorProcess"
+ "pathExtension"
+ "propagatedPersonaType"
+ "propagationFailed"
+ "proxiedIdentifier"
+ "proximateIdentifier"
+ "proximateLaunchPersonaType"
+ "quarantineNeededForDirectoryURL:"
+ "quarantineURL:identifier:error:"
+ "recordAmbiguousPersonaRequestWithIdentifier:proxiedIdentifier:proximateIdentifier:explicitPersonaType:legacyPersonaPolicy:propagationFailed:containerClass:"
+ "setFmDir:"
+ "setFmQuarantine:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "v60@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32i40B44B48Q52"
+ "v60@0:8@16@24@32i40B44B48Q52"
- "20:28:29"
- "Aug 26 2025"
- "B48@0:8@16S24@28i36^@40"
- "B56@0:8@16S24@28i36^B40^@48"
- "MobileContainerManager-725.0.13~2098"
- "_actionsFromVersion:toTargetVersion:context:"
- "_createURLIfNecessary:mode:owner:dataProtectionClass:error:"
- "_createURLIfNecessary:mode:owner:dataProtectionClass:exists:error:"
- "_inLibraryRepairBlock_createURLIfNecessary:mode:owner:dataProtectionClass:exists:error:"
- "_interpolationReplacements"
- "createIfNecessaryWithDataProtectionClass:error:"
- "initWithBytesNoCopy:length:encoding:deallocator:"
- "v24@?0^v8Q16"

```
