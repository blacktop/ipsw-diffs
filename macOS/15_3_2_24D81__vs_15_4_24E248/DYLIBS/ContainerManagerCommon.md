## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/Versions/A/ContainerManagerCommon`

```diff

-689.0.0.0.0
-  __TEXT.__text: 0xd8a78
-  __TEXT.__auth_stubs: 0x1780
-  __TEXT.__objc_methlist: 0x7284
-  __TEXT.__const: 0x320
-  __TEXT.__gcc_except_tab: 0x2744
-  __TEXT.__cstring: 0x869d
-  __TEXT.__oslogstring: 0xbcc3
-  __TEXT.__ustring: 0x16c
+689.100.6.0.0
+  __TEXT.__text: 0xda848
+  __TEXT.__auth_stubs: 0x17c0
+  __TEXT.__objc_methlist: 0x9334
+  __TEXT.__const: 0x330
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x1b80
-  __TEXT.__objc_classname: 0x1ae6
-  __TEXT.__objc_methname: 0x119f3
-  __TEXT.__objc_methtype: 0x3b7c
-  __TEXT.__objc_stubs: 0xa9a0
-  __DATA_CONST.__got: 0x258
+  __TEXT.__gcc_except_tab: 0x2788
+  __TEXT.__cstring: 0x86e0
+  __TEXT.__oslogstring: 0xbced
+  __TEXT.__ustring: 0x16c
+  __TEXT.__unwind_info: 0x1bb0
+  __TEXT.__objc_classname: 0x1b2b
+  __TEXT.__objc_methname: 0x11c06
+  __TEXT.__objc_methtype: 0x3bac
+  __TEXT.__objc_stubs: 0xaae0
+  __DATA_CONST.__got: 0x260
   __DATA_CONST.__const: 0x3d8
-  __DATA_CONST.__objc_classlist: 0x540
+  __DATA_CONST.__objc_classlist: 0x550
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x370
+  __DATA_CONST.__objc_protolist: 0x378
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3008
+  __DATA_CONST.__objc_selrefs: 0x30c8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x4b0
+  __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x360
-  __AUTH_CONST.__auth_got: 0xbd0
+  __AUTH_CONST.__auth_got: 0xbf0
   __AUTH_CONST.__const: 0x1cb0
   __AUTH_CONST.__cfstring: 0x4960
-  __AUTH_CONST.__objc_const: 0x16480
+  __AUTH_CONST.__objc_const: 0x13a10
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x1410
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH.__objc_data: 0x3480
-  __DATA.__objc_ivar: 0xa88
-  __DATA.__data: 0x2a70
+  __AUTH.__objc_data: 0x3520
+  __DATA.__objc_ivar: 0xb34
+  __DATA.__data: 0x2ad0
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x420
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: D1A12C39-FD55-3B55-9587-49BC806D4F7C
-  Functions: 2794
-  Symbols:   7550
-  CStrings:  5584
+  UUID: E83C8EC8-910D-3DB4-82C0-76A4AD23F5B2
+  Functions: 2851
+  Symbols:   7689
+  CStrings:  5615
 
Symbols:
+ +[MCMCommandUpdateInfo command]
+ +[MCMCommandUpdateInfo incomingMessageClass]
+ +[MCMPOSIXUser _posixUserWithPWD:]
+ -[MCMCommandAcquireSandboxExtensionWithUUID includedCreator]
+ -[MCMCommandAcquireSandboxExtensionWithUUID includedInfo]
+ -[MCMCommandAcquireSandboxExtensionWithUUID includedPath]
+ -[MCMCommandAcquireSandboxExtensionWithUUID includedUserManagedAssetsPath]
+ -[MCMCommandDiskUsageForContainer includedCreator]
+ -[MCMCommandDiskUsageForContainer includedInfo]
+ -[MCMCommandDiskUsageForContainer includedPath]
+ -[MCMCommandDiskUsageForContainer includedUserManagedAssetsPath]
+ -[MCMCommandInfoValueForKey includedCreator]
+ -[MCMCommandInfoValueForKey includedInfo]
+ -[MCMCommandInfoValueForKey includedPath]
+ -[MCMCommandInfoValueForKey includedUserManagedAssetsPath]
+ -[MCMCommandProcessRestoredContainer includedCreator]
+ -[MCMCommandProcessRestoredContainer includedInfo]
+ -[MCMCommandProcessRestoredContainer includedPath]
+ -[MCMCommandProcessRestoredContainer includedUserManagedAssetsPath]
+ -[MCMCommandRecreateContainerStructure includedCreator]
+ -[MCMCommandRecreateContainerStructure includedInfo]
+ -[MCMCommandRecreateContainerStructure includedPath]
+ -[MCMCommandRecreateContainerStructure includedUserManagedAssetsPath]
+ -[MCMCommandRegenerateDirectoryUUID includedCreator]
+ -[MCMCommandRegenerateDirectoryUUID includedInfo]
+ -[MCMCommandRegenerateDirectoryUUID includedPath]
+ -[MCMCommandRegenerateDirectoryUUID includedUserManagedAssetsPath]
+ -[MCMCommandSetInfoValue includedCreator]
+ -[MCMCommandSetInfoValue includedInfo]
+ -[MCMCommandSetInfoValue includedPath]
+ -[MCMCommandSetInfoValue includedUserManagedAssetsPath]
+ -[MCMCommandUpdateInfo .cxx_destruct]
+ -[MCMCommandUpdateInfo concreteContainerIdentity]
+ -[MCMCommandUpdateInfo deleteKeys]
+ -[MCMCommandUpdateInfo execute]
+ -[MCMCommandUpdateInfo fullReplace]
+ -[MCMCommandUpdateInfo includedCreator]
+ -[MCMCommandUpdateInfo includedInfo]
+ -[MCMCommandUpdateInfo includedPath]
+ -[MCMCommandUpdateInfo includedUserManagedAssetsPath]
+ -[MCMCommandUpdateInfo infoDict]
+ -[MCMCommandUpdateInfo initWithMessage:context:reply:]
+ -[MCMCommandUpdateInfo preflightClientAllowed]
+ -[MCMMetadata _modifiedDictBySetttingValue:forKey:onInfo:]
+ -[MCMMetadata metadataByDeletingInfoDictKeys:]
+ -[MCMMetadata metadataBySettingValuesWithInfoDict:fullReplace:]
+ -[MCMXPCMessageUpdateInfo .cxx_destruct]
+ -[MCMXPCMessageUpdateInfo deleteKeys]
+ -[MCMXPCMessageUpdateInfo fullReplace]
+ -[MCMXPCMessageUpdateInfo infoDict]
+ -[MCMXPCMessageUpdateInfo initWithXPCObject:context:error:]
+ -[MCMXPCMessageWithConcreteContainerBase includedCreator]
+ -[MCMXPCMessageWithConcreteContainerBase includedInfo]
+ -[MCMXPCMessageWithConcreteContainerBase includedPath]
+ -[MCMXPCMessageWithConcreteContainerBase includedUserManagedAssetsPath]
+ GCC_except_table1036
+ GCC_except_table1037
+ GCC_except_table1049
+ GCC_except_table1062
+ GCC_except_table1065
+ GCC_except_table1069
+ GCC_except_table1071
+ GCC_except_table1073
+ GCC_except_table1075
+ GCC_except_table1078
+ GCC_except_table1083
+ GCC_except_table1085
+ GCC_except_table1093
+ GCC_except_table1096
+ GCC_except_table1098
+ GCC_except_table1108
+ GCC_except_table1124
+ GCC_except_table1134
+ GCC_except_table1139
+ GCC_except_table1145
+ GCC_except_table1147
+ GCC_except_table1199
+ GCC_except_table1209
+ GCC_except_table1240
+ GCC_except_table1288
+ GCC_except_table1290
+ GCC_except_table1294
+ GCC_except_table1295
+ GCC_except_table1490
+ GCC_except_table1537
+ GCC_except_table1623
+ GCC_except_table1760
+ GCC_except_table1798
+ GCC_except_table1810
+ GCC_except_table1851
+ GCC_except_table1857
+ GCC_except_table1914
+ GCC_except_table1917
+ GCC_except_table2011
+ GCC_except_table2026
+ GCC_except_table2164
+ GCC_except_table2181
+ GCC_except_table2182
+ GCC_except_table2258
+ GCC_except_table2303
+ GCC_except_table2318
+ GCC_except_table2335
+ GCC_except_table2384
+ GCC_except_table2396
+ GCC_except_table2456
+ GCC_except_table2468
+ GCC_except_table2535
+ GCC_except_table2539
+ GCC_except_table2541
+ GCC_except_table2545
+ GCC_except_table2603
+ GCC_except_table2696
+ GCC_except_table2746
+ GCC_except_table2749
+ GCC_except_table2820
+ GCC_except_table752
+ GCC_except_table753
+ GCC_except_table859
+ GCC_except_table903
+ GCC_except_table932
+ GCC_except_table936
+ GCC_except_table947
+ GCC_except_table984
+ GCC_except_table992
+ GCC_except_table998
+ OBJC_IVAR_$_MCMCommandAcquireSandboxExtensionWithUUID._includedCreator
+ OBJC_IVAR_$_MCMCommandAcquireSandboxExtensionWithUUID._includedInfo
+ OBJC_IVAR_$_MCMCommandAcquireSandboxExtensionWithUUID._includedPath
+ OBJC_IVAR_$_MCMCommandAcquireSandboxExtensionWithUUID._includedUserManagedAssetsPath
+ OBJC_IVAR_$_MCMCommandDiskUsageForContainer._includedCreator
+ OBJC_IVAR_$_MCMCommandDiskUsageForContainer._includedInfo
+ OBJC_IVAR_$_MCMCommandDiskUsageForContainer._includedPath
+ OBJC_IVAR_$_MCMCommandDiskUsageForContainer._includedUserManagedAssetsPath
+ OBJC_IVAR_$_MCMCommandInfoValueForKey._includedCreator
+ OBJC_IVAR_$_MCMCommandInfoValueForKey._includedInfo
+ OBJC_IVAR_$_MCMCommandInfoValueForKey._includedPath
+ OBJC_IVAR_$_MCMCommandInfoValueForKey._includedUserManagedAssetsPath
+ OBJC_IVAR_$_MCMCommandProcessRestoredContainer._includedCreator
+ OBJC_IVAR_$_MCMCommandProcessRestoredContainer._includedInfo
+ OBJC_IVAR_$_MCMCommandProcessRestoredContainer._includedPath
+ OBJC_IVAR_$_MCMCommandProcessRestoredContainer._includedUserManagedAssetsPath
+ OBJC_IVAR_$_MCMCommandRecreateContainerStructure._includedCreator
+ OBJC_IVAR_$_MCMCommandRecreateContainerStructure._includedInfo
+ OBJC_IVAR_$_MCMCommandRecreateContainerStructure._includedPath
+ OBJC_IVAR_$_MCMCommandRecreateContainerStructure._includedUserManagedAssetsPath
+ OBJC_IVAR_$_MCMCommandRegenerateDirectoryUUID._includedCreator
+ OBJC_IVAR_$_MCMCommandRegenerateDirectoryUUID._includedInfo
+ OBJC_IVAR_$_MCMCommandRegenerateDirectoryUUID._includedPath
+ OBJC_IVAR_$_MCMCommandRegenerateDirectoryUUID._includedUserManagedAssetsPath
+ OBJC_IVAR_$_MCMCommandSetInfoValue._includedCreator
+ OBJC_IVAR_$_MCMCommandSetInfoValue._includedInfo
+ OBJC_IVAR_$_MCMCommandSetInfoValue._includedPath
+ OBJC_IVAR_$_MCMCommandSetInfoValue._includedUserManagedAssetsPath
+ OBJC_IVAR_$_MCMCommandUpdateInfo._concreteContainerIdentity
+ OBJC_IVAR_$_MCMCommandUpdateInfo._deleteKeys
+ OBJC_IVAR_$_MCMCommandUpdateInfo._fullReplace
+ OBJC_IVAR_$_MCMCommandUpdateInfo._includedCreator
+ OBJC_IVAR_$_MCMCommandUpdateInfo._includedInfo
+ OBJC_IVAR_$_MCMCommandUpdateInfo._includedPath
+ OBJC_IVAR_$_MCMCommandUpdateInfo._includedUserManagedAssetsPath
+ OBJC_IVAR_$_MCMCommandUpdateInfo._infoDict
+ OBJC_IVAR_$_MCMXPCMessageUpdateInfo._deleteKeys
+ OBJC_IVAR_$_MCMXPCMessageUpdateInfo._fullReplace
+ OBJC_IVAR_$_MCMXPCMessageUpdateInfo._infoDict
+ OBJC_IVAR_$_MCMXPCMessageWithConcreteContainerBase._includedCreator
+ OBJC_IVAR_$_MCMXPCMessageWithConcreteContainerBase._includedInfo
+ OBJC_IVAR_$_MCMXPCMessageWithConcreteContainerBase._includedPath
+ OBJC_IVAR_$_MCMXPCMessageWithConcreteContainerBase._includedUserManagedAssetsPath
+ _OBJC_$_PROP_LIST_MCMMetadata.261
+ _OBJC_$_PROP_LIST_MCMMetadataMinimal.216
+ _OBJC_CLASS_$_MCMCommandUpdateInfo
+ _OBJC_CLASS_$_MCMXPCMessageUpdateInfo
+ _OBJC_METACLASS_$_MCMCommandUpdateInfo
+ _OBJC_METACLASS_$_MCMXPCMessageUpdateInfo
+ __Block_byref_object_copy_.10847
+ __Block_byref_object_copy_.11431
+ __Block_byref_object_copy_.11816
+ __Block_byref_object_copy_.12174
+ __Block_byref_object_copy_.12342
+ __Block_byref_object_copy_.13218
+ __Block_byref_object_copy_.13521
+ __Block_byref_object_copy_.13777
+ __Block_byref_object_copy_.3055
+ __Block_byref_object_copy_.3699
+ __Block_byref_object_copy_.4066
+ __Block_byref_object_copy_.4756
+ __Block_byref_object_copy_.5034
+ __Block_byref_object_copy_.6745
+ __Block_byref_object_copy_.7220
+ __Block_byref_object_copy_.8270
+ __Block_byref_object_copy_.8407
+ __Block_byref_object_copy_.8457
+ __Block_byref_object_copy_.8906
+ __Block_byref_object_copy_.9106
+ __Block_byref_object_dispose_.10848
+ __Block_byref_object_dispose_.11432
+ __Block_byref_object_dispose_.11817
+ __Block_byref_object_dispose_.12175
+ __Block_byref_object_dispose_.12343
+ __Block_byref_object_dispose_.13219
+ __Block_byref_object_dispose_.13522
+ __Block_byref_object_dispose_.13778
+ __Block_byref_object_dispose_.3056
+ __Block_byref_object_dispose_.3700
+ __Block_byref_object_dispose_.4067
+ __Block_byref_object_dispose_.4757
+ __Block_byref_object_dispose_.5035
+ __Block_byref_object_dispose_.6746
+ __Block_byref_object_dispose_.7221
+ __Block_byref_object_dispose_.8271
+ __Block_byref_object_dispose_.8408
+ __Block_byref_object_dispose_.8458
+ __Block_byref_object_dispose_.8907
+ __Block_byref_object_dispose_.9107
+ __OBJC_$_CLASS_METHODS_MCMCommandUpdateInfo
+ __OBJC_$_INSTANCE_METHODS_MCMCommandUpdateInfo
+ __OBJC_$_INSTANCE_METHODS_MCMXPCMessageUpdateInfo
+ __OBJC_$_INSTANCE_VARIABLES_MCMCommandUpdateInfo
+ __OBJC_$_INSTANCE_VARIABLES_MCMXPCMessageUpdateInfo
+ __OBJC_$_PROP_LIST_MCMCommandUpdateInfo
+ __OBJC_$_PROP_LIST_MCMParametersUpdateInfo
+ __OBJC_$_PROP_LIST_MCMXPCMessageUpdateInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MCMParametersUpdateInfo
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MCMParametersUpdateInfo
+ __OBJC_$_PROTOCOL_REFS_MCMParametersUpdateInfo
+ __OBJC_CLASS_PROTOCOLS_$_MCMCommandUpdateInfo
+ __OBJC_CLASS_PROTOCOLS_$_MCMXPCMessageUpdateInfo
+ __OBJC_CLASS_RO_$_MCMCommandUpdateInfo
+ __OBJC_CLASS_RO_$_MCMXPCMessageUpdateInfo
+ __OBJC_LABEL_PROTOCOL_$_MCMParametersUpdateInfo
+ __OBJC_METACLASS_RO_$_MCMCommandUpdateInfo
+ __OBJC_METACLASS_RO_$_MCMXPCMessageUpdateInfo
+ __OBJC_PROTOCOL_$_MCMParametersUpdateInfo
+ ___46+[MCMPOSIXUser _posixUserWithUID:name:useUID:]_block_invoke
+ ___block_descriptor_48_e8_32r_e61_B40?0{container_pwd_s=II**}8^^{container_error_extended_s}32l
+ __block_literal_global.10886
+ __block_literal_global.11084
+ __block_literal_global.11825
+ __block_literal_global.12168
+ __block_literal_global.12613
+ __block_literal_global.12841
+ __block_literal_global.13513
+ __block_literal_global.13604
+ __block_literal_global.13624
+ __block_literal_global.20
+ __block_literal_global.2458
+ __block_literal_global.4731
+ __block_literal_global.5072
+ __block_literal_global.6166
+ __block_literal_global.6650
+ __block_literal_global.7125
+ __block_literal_global.7943
+ __block_literal_global.8586
+ __block_literal_global.8689
+ __block_literal_global.9874
+ _container_get_creator_codesign_identifier
+ _container_get_info
+ _container_get_path
+ _container_get_user_managed_assets_relative_path
+ _container_pwd_for_name
+ _container_pwd_for_uid
+ _gCMPWDSeam
+ _objc_msgSend$_modifiedDictBySetttingValue:forKey:onInfo:
+ _objc_msgSend$_posixUserWithPWD:
+ _objc_msgSend$deleteKeys
+ _objc_msgSend$fullReplace
+ _objc_msgSend$includedCreator
+ _objc_msgSend$includedInfo
+ _objc_msgSend$includedPath
+ _objc_msgSend$includedUserManagedAssetsPath
+ _objc_msgSend$infoDict
+ _objc_msgSend$metadataByDeletingInfoDictKeys:
+ _objc_msgSend$metadataBySettingValuesWithInfoDict:fullReplace:
+ defaultManager.onceToken.8574
+ sharedInstance.onceToken.9388
- +[MCMPOSIXUser _posixUserWithPasswdPtr:]
- GCC_except_table1019
- GCC_except_table1020
- GCC_except_table1032
- GCC_except_table1035
- GCC_except_table1039
- GCC_except_table1045
- GCC_except_table1048
- GCC_except_table1054
- GCC_except_table1058
- GCC_except_table1061
- GCC_except_table1064
- GCC_except_table1066
- GCC_except_table1068
- GCC_except_table1076
- GCC_except_table1079
- GCC_except_table1091
- GCC_except_table1107
- GCC_except_table1117
- GCC_except_table1122
- GCC_except_table1128
- GCC_except_table1130
- GCC_except_table1182
- GCC_except_table1192
- GCC_except_table1215
- GCC_except_table1263
- GCC_except_table1265
- GCC_except_table1269
- GCC_except_table1270
- GCC_except_table1461
- GCC_except_table1508
- GCC_except_table1590
- GCC_except_table1723
- GCC_except_table1761
- GCC_except_table1773
- GCC_except_table1814
- GCC_except_table1820
- GCC_except_table1877
- GCC_except_table1880
- GCC_except_table1969
- GCC_except_table1984
- GCC_except_table2122
- GCC_except_table2139
- GCC_except_table2140
- GCC_except_table2216
- GCC_except_table2257
- GCC_except_table2272
- GCC_except_table2289
- GCC_except_table2338
- GCC_except_table2350
- GCC_except_table2410
- GCC_except_table2422
- GCC_except_table2447
- GCC_except_table2489
- GCC_except_table2495
- GCC_except_table2499
- GCC_except_table2557
- GCC_except_table2642
- GCC_except_table2692
- GCC_except_table2763
- GCC_except_table738
- GCC_except_table739
- GCC_except_table845
- GCC_except_table889
- GCC_except_table915
- GCC_except_table919
- GCC_except_table930
- GCC_except_table967
- GCC_except_table975
- GCC_except_table981
- _OBJC_$_PROP_LIST_MCMMetadata.254
- _OBJC_$_PROP_LIST_MCMMetadataMinimal.211
- __Block_byref_object_copy_.10576
- __Block_byref_object_copy_.11143
- __Block_byref_object_copy_.11522
- __Block_byref_object_copy_.11889
- __Block_byref_object_copy_.12057
- __Block_byref_object_copy_.12900
- __Block_byref_object_copy_.13445
- __Block_byref_object_copy_.2977
- __Block_byref_object_copy_.3601
- __Block_byref_object_copy_.3977
- __Block_byref_object_copy_.4660
- __Block_byref_object_copy_.4903
- __Block_byref_object_copy_.6592
- __Block_byref_object_copy_.7049
- __Block_byref_object_copy_.8081
- __Block_byref_object_copy_.8218
- __Block_byref_object_copy_.8268
- __Block_byref_object_copy_.8717
- __Block_byref_object_copy_.8917
- __Block_byref_object_dispose_.10577
- __Block_byref_object_dispose_.11144
- __Block_byref_object_dispose_.11523
- __Block_byref_object_dispose_.11890
- __Block_byref_object_dispose_.12058
- __Block_byref_object_dispose_.12901
- __Block_byref_object_dispose_.13446
- __Block_byref_object_dispose_.2978
- __Block_byref_object_dispose_.3602
- __Block_byref_object_dispose_.3978
- __Block_byref_object_dispose_.4661
- __Block_byref_object_dispose_.4904
- __Block_byref_object_dispose_.6593
- __Block_byref_object_dispose_.7050
- __Block_byref_object_dispose_.8082
- __Block_byref_object_dispose_.8219
- __Block_byref_object_dispose_.8269
- __Block_byref_object_dispose_.8718
- __Block_byref_object_dispose_.8918
- ___block_descriptor_42_e8_32s_e14_"NSError"8?0l
- __block_literal_global.10615
- __block_literal_global.10813
- __block_literal_global.11531
- __block_literal_global.11883
- __block_literal_global.12328
- __block_literal_global.12555
- __block_literal_global.13194
- __block_literal_global.13282
- __block_literal_global.13302
- __block_literal_global.19
- __block_literal_global.2386
- __block_literal_global.4635
- __block_literal_global.4940
- __block_literal_global.6015
- __block_literal_global.6497
- __block_literal_global.6954
- __block_literal_global.7755
- __block_literal_global.8397
- __block_literal_global.8500
- __block_literal_global.9615
- _getpwnam_r
- _getpwuid_r
- _objc_msgSend$_posixUserWithPasswdPtr:
- defaultManager.onceToken.8385
- sharedInstance.onceToken.9199
CStrings:
+ "21:03:29"
+ "@24@0:8@\"NSSet\"16"
+ "@28@0:8@\"NSDictionary\"16B24"
+ "@40@0:8{container_pwd_s=II**}16"
+ "B40@?0{container_pwd_s=II**}8^^{container_error_extended_s}32"
+ "MCMCommandUpdateInfo"
+ "MCMParametersUpdateInfo"
+ "MCMXPCMessageUpdateInfo"
+ "Mar  7 2025"
+ "MobileContainerManager-689.100.6~278"
+ "No container with identity: %@"
+ "T@\"NSDictionary\",R,N,V_infoDict"
+ "T@\"NSSet\",R,N,V_deleteKeys"
+ "TB,R,D,N"
+ "TB,R,N,V_fullReplace"
+ "TB,R,N,V_includedCreator"
+ "TB,R,N,V_includedInfo"
+ "TB,R,N,V_includedPath"
+ "TB,R,N,V_includedUserManagedAssetsPath"
+ "Unable to get user (%{public}d/[%@]/%{public}d); error = %{public}s"
+ "_deleteKeys"
+ "_fullReplace"
+ "_includedCreator"
+ "_includedInfo"
+ "_includedPath"
+ "_includedUserManagedAssetsPath"
+ "_infoDict"
+ "_modifiedDictBySetttingValue:forKey:onInfo:"
+ "_posixUserWithPWD:"
+ "assertion failure: \"notificationPort != ((void*)0)\" -> %llu"
+ "deleteKeys"
+ "fullReplace"
+ "includedCreator"
+ "includedInfo"
+ "includedPath"
+ "includedUserManagedAssetsPath"
+ "infoDict"
+ "metadataByDeletingInfoDictKeys:"
+ "metadataBySettingValuesWithInfoDict:fullReplace:"
- "23:10:47"
- "@24@0:8^{passwd=**IIq****q}16"
- "Could not get _SC_GETPW_R_SIZE_MAX sysconf."
- "Dec 13 2024"
- "MobileContainerManager-689~7130"
- "NULL passwd"
- "_posixUserWithPasswdPtr:"
- "assertion failure: \"notificationPort != ((void *)0)\" -> %lld"

```
