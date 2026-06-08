## ManagedAssets

> `/System/Library/PrivateFrameworks/ManagedAssets.framework/ManagedAssets`

```diff

-269.100.5.0.0
-  __TEXT.__text: 0x28b74
-  __TEXT.__auth_stubs: 0x610
+279.0.0.0.0
+  __TEXT.__text: 0x267b0
   __TEXT.__objc_methlist: 0x1234
-  __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0xf10
-  __TEXT.__cstring: 0x34cd
-  __TEXT.__oslogstring: 0x29ba
-  __TEXT.__unwind_info: 0xa20
-  __TEXT.__objc_classname: 0x20e
-  __TEXT.__objc_methname: 0x36f4
-  __TEXT.__objc_methtype: 0x1369
-  __TEXT.__objc_stubs: 0x2180
-  __DATA_CONST.__got: 0x148
+  __TEXT.__const: 0xc8
+  __TEXT.__gcc_except_tab: 0xb5c
+  __TEXT.__cstring: 0x34e3
+  __TEXT.__oslogstring: 0x2a04
+  __TEXT.__unwind_info: 0x9a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1348
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x80

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x1f0
-  __AUTH_CONST.__auth_got: 0x318
+  __DATA_CONST.__got: 0x148
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0x25e0
   __AUTH_CONST.__objc_const: 0x1898
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x11c
   __DATA.__data: 0x718

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3AE7D085-3248-3AFE-A9D1-7D26157214C8
-  Functions: 756
-  Symbols:   2773
-  CStrings:  1680
+  UUID: DF4CF667-F688-3C53-9B81-4AB0B2445AD9
+  Functions: 749
+  Symbols:   2746
+  CStrings:  969
 
Symbols:
+ GCC_except_table23
+ ___61-[ManagedAssetsClient(FileAsset) queryFile:attributes:error:]_block_invoke.59
+ ___61-[ManagedAssetsClient(FileAsset) queryFile:attributes:error:]_block_invoke.59.cold.1
+ ___61-[ManagedAssetsClient(FileAsset) queryFile:attributes:error:]_block_invoke.59.cold.2
+ ___62-[ManagedAssetsClient(FileAsset) commitFile:attributes:error:]_block_invoke.51
+ ___62-[ManagedAssetsClient(FileAsset) commitFile:attributes:error:]_block_invoke.51.cold.1
+ ___62-[ManagedAssetsClient(FileAsset) deleteFile:attributes:error:]_block_invoke.56
+ ___62-[ManagedAssetsClient(FileAsset) deleteFile:attributes:error:]_block_invoke.56.cold.1
+ ___63-[ManagedAssetsClient(KVStore) deleteKVStore:attributes:error:]_block_invoke.50
+ ___63-[ManagedAssetsClient(KVStore) deleteKVStore:attributes:error:]_block_invoke.50.cold.1
+ ___65-[ManagedAssetsClient(AnchorPersist) getDataForAllAnchors:error:]_block_invoke.45.cold.1
+ ___66-[ManagedAssetsClient(FileAsset) queryFile:attributes:completion:]_block_invoke.57
+ ___67-[ManagedAssetsClient(FileAsset) commitFile:attributes:completion:]_block_invoke.50
+ ___67-[ManagedAssetsClient(FileAsset) deleteFile:attributes:completion:]_block_invoke.55
+ ___67-[ManagedAssetsClient(FileAsset) diskUsage:attributes:usage:error:]_block_invoke.60
+ ___67-[ManagedAssetsClient(FileAsset) diskUsage:attributes:usage:error:]_block_invoke.60.cold.1
+ ___68-[ManagedAssetsClient(KVStore) deleteKVStore:attributes:completion:]_block_invoke.48
+ ___68-[ManagedAssetsClient(KVStore) deleteKVStore:attributes:completion:]_block_invoke.49.cold.1
+ ___70-[ManagedAssetsClient(AnchorPersist) getDataForAllAnchors:completion:]_block_invoke.38.cold.1
+ ___70-[ManagedAssetsClient(FileAsset) openFile:mode:attributes:completion:]_block_invoke.34
+ ___71-[ManagedAssetsClient(KVStore) queryDataInStore:keys:attributes:error:]_block_invoke.44
+ ___71-[ManagedAssetsClient(KVStore) queryDataInStore:keys:attributes:error:]_block_invoke.44.cold.1
+ ___72-[ManagedAssetsClient(KVStore) deleteDataInStore:keys:attributes:error:]_block_invoke.47
+ ___72-[ManagedAssetsClient(KVStore) deleteDataInStore:keys:attributes:error:]_block_invoke.47.cold.1
+ ___72-[ManagedAssetsClient(KVStore) putDataInStore:records:attributes:error:]_block_invoke.37
+ ___72-[ManagedAssetsClient(KVStore) putDataInStore:records:attributes:error:]_block_invoke.37.cold.1
+ ___74-[ManagedAssetsClient(KVStore) checkIfKVStoreGroupExistUsing:exist:error:]_block_invoke.51
+ ___74-[ManagedAssetsClient(KVStore) checkIfKVStoreGroupExistUsing:exist:error:]_block_invoke.51.cold.1
+ ___74-[ManagedAssetsClient(KVStore) checkIfKVStoreGroupExistUsing:exist:error:]_block_invoke.51.cold.2
+ ___76-[ManagedAssetsClient(KVStore) createKVStore:recordFields:attributes:error:]_block_invoke.34
+ ___76-[ManagedAssetsClient(KVStore) createKVStore:recordFields:attributes:error:]_block_invoke.34.cold.1
+ ___76-[ManagedAssetsClient(KVStore) queryDataInStore:keys:attributes:completion:]_block_invoke.41
+ ___76-[ManagedAssetsClient(KVStore) queryDataInStore:keys:attributes:completion:]_block_invoke.42.cold.1
+ ___77-[ManagedAssetsClient(KVStore) deleteDataInStore:keys:attributes:completion:]_block_invoke.45
+ ___77-[ManagedAssetsClient(KVStore) deleteDataInStore:keys:attributes:completion:]_block_invoke.46.cold.1
+ ___77-[ManagedAssetsClient(KVStore) putDataInStore:records:attributes:completion:]_block_invoke.35
+ ___77-[ManagedAssetsClient(KVStore) putDataInStore:records:attributes:completion:]_block_invoke.36.cold.1
+ ___79-[ManagedAssetsClient(FileAsset) openFile:mode:attributes:attributesOut:error:]_block_invoke.38
+ ___79-[ManagedAssetsClient(KVStore) updateDataInStore:keys:values:attributes:error:]_block_invoke.40
+ ___79-[ManagedAssetsClient(KVStore) updateDataInStore:keys:values:attributes:error:]_block_invoke.40.cold.1
+ ___80-[ManagedAssetsClient(FileAsset) requestFile:isDirectory:mode:attributes:error:]_block_invoke.49
+ ___80-[ManagedAssetsClient(FileAsset) requestFile:isDirectory:mode:attributes:error:]_block_invoke.49.cold.1
+ ___80-[ManagedAssetsClient(FileAsset) requestFile:isDirectory:mode:attributes:error:]_block_invoke.49.cold.2
+ ___80-[ManagedAssetsClient(FileAsset) requestFile:isDirectory:mode:attributes:error:]_block_invoke.49.cold.3
+ ___80-[ManagedAssetsClient(FileAsset) requestFile:isDirectory:mode:attributes:error:]_block_invoke.49.cold.4
+ ___81-[ManagedAssetsClient(KVStore) createKVStore:recordFields:attributes:completion:]_block_invoke.30
+ ___81-[ManagedAssetsClient(KVStore) createKVStore:recordFields:attributes:completion:]_block_invoke.33
+ ___81-[ManagedAssetsClient(KVStore) createKVStore:recordFields:attributes:completion:]_block_invoke.33.cold.1
+ ___84-[ManagedAssetsClient(KVStore) updateDataInStore:keys:values:attributes:completion:]_block_invoke.38
+ ___84-[ManagedAssetsClient(KVStore) updateDataInStore:keys:values:attributes:completion:]_block_invoke.39.cold.1
+ ___85-[ManagedAssetsClient(FileAsset) requestFile:isDirectory:mode:attributes:completion:]_block_invoke.39
+ ___block_descriptor_56_e8_32r40r48r_e29_v32?0"NSFileHandle"8Q16^B24lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e29_v32?0"NSFileHandle"8Q16^B24ls32l8s40l8r48l8
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x5
- GCC_except_table182
- GCC_except_table191
- GCC_except_table199
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_21
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_23
- ___61-[ManagedAssetsClient(FileAsset) queryFile:attributes:error:]_block_invoke.60
- ___61-[ManagedAssetsClient(FileAsset) queryFile:attributes:error:]_block_invoke.60.cold.1
- ___61-[ManagedAssetsClient(FileAsset) queryFile:attributes:error:]_block_invoke.60.cold.2
- ___62-[ManagedAssetsClient(FileAsset) commitFile:attributes:error:]_block_invoke.52
- ___62-[ManagedAssetsClient(FileAsset) commitFile:attributes:error:]_block_invoke.52.cold.1
- ___62-[ManagedAssetsClient(FileAsset) deleteFile:attributes:error:]_block_invoke.57
- ___62-[ManagedAssetsClient(FileAsset) deleteFile:attributes:error:]_block_invoke.57.cold.1
- ___63-[ManagedAssetsClient(KVStore) deleteKVStore:attributes:error:]_block_invoke.51
- ___63-[ManagedAssetsClient(KVStore) deleteKVStore:attributes:error:]_block_invoke.51.cold.1
- ___66-[ManagedAssetsClient(FileAsset) queryFile:attributes:completion:]_block_invoke.58
- ___67-[ManagedAssetsClient(FileAsset) commitFile:attributes:completion:]_block_invoke.51
- ___67-[ManagedAssetsClient(FileAsset) deleteFile:attributes:completion:]_block_invoke.56
- ___67-[ManagedAssetsClient(FileAsset) diskUsage:attributes:usage:error:]_block_invoke.61
- ___67-[ManagedAssetsClient(FileAsset) diskUsage:attributes:usage:error:]_block_invoke.61.cold.1
- ___68-[ManagedAssetsClient(KVStore) deleteKVStore:attributes:completion:]_block_invoke.50
- ___68-[ManagedAssetsClient(KVStore) deleteKVStore:attributes:completion:]_block_invoke.50.cold.1
- ___70-[ManagedAssetsClient(FileAsset) openFile:mode:attributes:completion:]_block_invoke.35
- ___71-[ManagedAssetsClient(KVStore) queryDataInStore:keys:attributes:error:]_block_invoke.45
- ___71-[ManagedAssetsClient(KVStore) queryDataInStore:keys:attributes:error:]_block_invoke.45.cold.1
- ___72-[ManagedAssetsClient(KVStore) deleteDataInStore:keys:attributes:error:]_block_invoke.48
- ___72-[ManagedAssetsClient(KVStore) deleteDataInStore:keys:attributes:error:]_block_invoke.48.cold.1
- ___72-[ManagedAssetsClient(KVStore) putDataInStore:records:attributes:error:]_block_invoke.38
- ___72-[ManagedAssetsClient(KVStore) putDataInStore:records:attributes:error:]_block_invoke.38.cold.1
- ___74-[ManagedAssetsClient(KVStore) checkIfKVStoreGroupExistUsing:exist:error:]_block_invoke.52
- ___74-[ManagedAssetsClient(KVStore) checkIfKVStoreGroupExistUsing:exist:error:]_block_invoke.52.cold.1
- ___74-[ManagedAssetsClient(KVStore) checkIfKVStoreGroupExistUsing:exist:error:]_block_invoke.52.cold.2
- ___76-[ManagedAssetsClient(KVStore) createKVStore:recordFields:attributes:error:]_block_invoke.35
- ___76-[ManagedAssetsClient(KVStore) createKVStore:recordFields:attributes:error:]_block_invoke.35.cold.1
- ___76-[ManagedAssetsClient(KVStore) queryDataInStore:keys:attributes:completion:]_block_invoke.43
- ___76-[ManagedAssetsClient(KVStore) queryDataInStore:keys:attributes:completion:]_block_invoke.43.cold.1
- ___77-[ManagedAssetsClient(KVStore) deleteDataInStore:keys:attributes:completion:]_block_invoke.47
- ___77-[ManagedAssetsClient(KVStore) deleteDataInStore:keys:attributes:completion:]_block_invoke.47.cold.1
- ___77-[ManagedAssetsClient(KVStore) putDataInStore:records:attributes:completion:]_block_invoke.37
- ___77-[ManagedAssetsClient(KVStore) putDataInStore:records:attributes:completion:]_block_invoke.37.cold.1
- ___79-[ManagedAssetsClient(FileAsset) openFile:mode:attributes:attributesOut:error:]_block_invoke.39
- ___79-[ManagedAssetsClient(KVStore) updateDataInStore:keys:values:attributes:error:]_block_invoke.41
- ___79-[ManagedAssetsClient(KVStore) updateDataInStore:keys:values:attributes:error:]_block_invoke.41.cold.1
- ___80-[ManagedAssetsClient(FileAsset) requestFile:isDirectory:mode:attributes:error:]_block_invoke.50
- ___80-[ManagedAssetsClient(FileAsset) requestFile:isDirectory:mode:attributes:error:]_block_invoke.50.cold.1
- ___80-[ManagedAssetsClient(FileAsset) requestFile:isDirectory:mode:attributes:error:]_block_invoke.50.cold.2
- ___80-[ManagedAssetsClient(FileAsset) requestFile:isDirectory:mode:attributes:error:]_block_invoke.50.cold.3
- ___80-[ManagedAssetsClient(FileAsset) requestFile:isDirectory:mode:attributes:error:]_block_invoke.50.cold.4
- ___81-[ManagedAssetsClient(KVStore) createKVStore:recordFields:attributes:completion:]_block_invoke.31
- ___81-[ManagedAssetsClient(KVStore) createKVStore:recordFields:attributes:completion:]_block_invoke.34
- ___81-[ManagedAssetsClient(KVStore) createKVStore:recordFields:attributes:completion:]_block_invoke.34.cold.1
- ___84-[ManagedAssetsClient(KVStore) updateDataInStore:keys:values:attributes:completion:]_block_invoke.40
- ___84-[ManagedAssetsClient(KVStore) updateDataInStore:keys:values:attributes:completion:]_block_invoke.40.cold.1
- ___85-[ManagedAssetsClient(FileAsset) requestFile:isDirectory:mode:attributes:completion:]_block_invoke.40
- ___block_descriptor_48_e8_32r40r_e29_v32?0"NSFileHandle"8Q16^B24lr32l8r40l8
- ___block_descriptor_48_e8_32s40s_e29_v32?0"NSFileHandle"8Q16^B24ls32l8s40l8
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "failed to read anchor %@: %@"
+ "skipping anchor with invalid UUID string: %@"
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSFileHandle\""
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSPointerArray\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@32@0:8^@16^@24"
- "@36@0:8@16B24^@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24^@32"
- "@40@0:8@16@24q32"
- "@40@0:8@16Q24Q32"
- "@48@0:8@16@24@32^@40"
- "@48@0:8Q16@24@32@40"
- "@52@0:8@16B24Q28@36o^@44"
- "@56@0:8@16Q24@32o^@40o^@48"
- "@56@0:8@16Q24Q32Q40^@48"
- "@56@0:8@16q24@32^Q40^@48"
- "@56@0:8Q16@24@32@40Q48"
- "@64@0:8@16@24^Q32Q40Q48^@56"
- "AddAnchorGroup:clientIdentifier:completion:"
- "AnchorPersist"
- "B"
- "B120@0:8@16@24@32q40q48q56q64B72B76Q80@88^@96^@104^@112"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8@16^@24"
- "B32@0:8^Q16^@24"
- "B32@0:8q16^@24"
- "B40@0:8@16@24^@32"
- "B40@0:8@16@24o^@32"
- "B40@0:8@16Q24^@32"
- "B40@0:8@16^@24^@32"
- "B40@0:8@16^B24^@32"
- "B48@0:8@16@24@32^@40"
- "B48@0:8@16@24^Q32^@40"
- "B48@0:8@16Q24Q32^@40"
- "B56@0:8@16@24@32@40^@48"
- "B64@0:8@16@24@32@40Q48^@56"
- "CheckIfCloudAssetZonesWithCompletion:"
- "CreateAsset:uuid:sessionToken:completion:"
- "CreateProfile:guest:completion:"
- "Debugging"
- "DeleteAllAssetsExcept:withOptions:completion:"
- "DeleteAllNonDefaultProfilesWithCompletion:"
- "DeleteAsset:uuid:completion:"
- "DeleteAsset:withOptions:completion:"
- "DeleteAssetsWithOptions:completion:"
- "DeleteProfile:completion:"
- "DeleteTempAsset:tokens:"
- "FileAsset"
- "GetAllAnchorGroups:completion:"
- "GetAllProfilesWithCompletion:"
- "GetAssetData:uuid:completion:"
- "GetAssetMeteData:uuid:completion:"
- "GetCurrentProfileType:"
- "GetLastSwitchTimeForPersistedGuestWithCompletion:"
- "GetTempAssetFileHandle:assetType:assetHandle:completion:"
- "GetTempAssetFilePathWithAssetType:completion:"
- "ImportSerializedV2Assets:option:profileType:axData:completion:"
- "JSONObjectWithData:options:error:"
- "KVStore"
- "MAAnchorPersistServices"
- "MACoreRxServices"
- "MADebuggingServices"
- "MAFile"
- "MAFileServices"
- "MAInUseArbiterServices"
- "MAKVStoreDataField"
- "MAKVStoreServices"
- "MANotificationServices"
- "MAProfileServices"
- "MASDAssetDescriptor"
- "MASDAssetMetadata"
- "MASDNotificationObserver"
- "MASDPlainAsset"
- "MASDRemoteSharingObserver"
- "MASDSerializedAssetFileInfo"
- "MASDSerializedAssets"
- "ManagedAssetsClient"
- "ManagedAssetsDataServices"
- "ManagedAssetsServerProtocol"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "PersistGuestProfileWithCompletion:"
- "Profile"
- "Q16@0:8"
- "QueryAssetMetaData:completion:"
- "QueryAssets:completion:"
- "RegisterOberverWithGroup:observerType:resourceNames:profile:events:completion:"
- "RegisterRemoteSharingOberverWithCompletion:"
- "RemoveAllAnchorGroups:completion:"
- "RemoveAnchorGroup:clientIdentifier:completion:"
- "SerializeAllAssets:option:completion:"
- "ShareAssetsWithGroup:sessionUUID:capability:completion:"
- "SwitchProfile:completion:"
- "T#,R"
- "T@\"NSData\",&,N,V_assetData"
- "T@\"NSData\",&,N,V_assetMetaData"
- "T@\"NSData\",&,N,V_creatorAttest"
- "T@\"NSData\",&,N,V_serverAttest"
- "T@\"NSData\",R,C,N,V_creatorAttest"
- "T@\"NSData\",R,C,N,V_data"
- "T@\"NSData\",R,C,N,V_serverAttest"
- "T@\"NSDate\",R,C,N,V_creationTime"
- "T@\"NSDate\",R,C,N,V_lastUpdatedTime"
- "T@\"NSDictionary\",R,N,V_attributes"
- "T@\"NSFileHandle\",&,N,V_assetFileHandle"
- "T@\"NSMutableArray\",&,N,V_assets"
- "T@\"NSString\",&,N,V_assetDataPath"
- "T@\"NSString\",&,N,V_assetHandle"
- "T@\"NSString\",&,N,V_deviceIdentifier"
- "T@\"NSString\",&,N,V_deviceName"
- "T@\"NSString\",&,N,V_enrollmentIdentifier"
- "T@\"NSString\",&,N,V_label"
- "T@\"NSString\",&,N,V_lastUpdateAlgorithmVersion"
- "T@\"NSString\",&,N,V_lastUpdateOSVersion"
- "T@\"NSString\",&,N,V_sandboxToken"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_algorithmVersion"
- "T@\"NSString\",R,C,N,V_ckrecordIdentifier"
- "T@\"NSString\",R,C,N,V_deviceIdentifier"
- "T@\"NSString\",R,C,N,V_deviceName"
- "T@\"NSString\",R,C,N,V_enrollmentIdentifier"
- "T@\"NSString\",R,C,N,V_label"
- "T@\"NSString\",R,C,N,V_lastUpdatedAlgorithmVersion"
- "T@\"NSString\",R,C,N,V_lastUpdatedOSVersion"
- "T@\"NSString\",R,C,N,V_participantIdentifier"
- "T@\"NSString\",R,C,N,V_sessionIdentifier"
- "T@\"NSString\",R,N,V_pathname"
- "TB,N"
- "TB,N,V_automicallyReleaseExtension"
- "TB,R"
- "TB,R,N"
- "TQ,N,V_assetDataLen"
- "TQ,N,V_options"
- "TQ,N,V_type"
- "TQ,R"
- "TQ,R,N,V_assetState"
- "TQ,R,N,V_syncOption"
- "TQ,R,N,V_type"
- "Td,N,V_creationTime"
- "Td,N,V_lastUpdatedTime"
- "Tq,N,V_assetState"
- "Tq,N,V_profileType"
- "Tq,N,V_type"
- "UTF8String"
- "UUID"
- "UUIDString"
- "UnpersistGuestProfileWithCompletion:"
- "UpdateAsset:uuid:sessionToken:algorithmVersion:completion:"
- "UpdateAssetV2:sessionToken:options:completion:"
- "Vv104@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32q40q48q56q64B72B76Q80@\"NSDictionary\"88@?<v@?@\"NSString\"@\"NSDictionary\"@\"NSError\">96"
- "Vv104@0:8@16@24@32q40q48q56q64B72B76Q80@88@?96"
- "Vv16@0:8"
- "Vv24@0:8@?16"
- "Vv24@0:8@?<v@?@\"NSDate\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSDictionary\"@\"NSString\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
- "Vv24@0:8@?<v@?B@\"NSError\">16"
- "Vv24@0:8@?<v@?Q@\"NSError\">16"
- "Vv28@0:8B16@\"NSArray\"20"
- "Vv28@0:8B16@20"
- "Vv32@0:8@\"NSDictionary\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "Vv32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "Vv32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"NSDictionary\"16@?<v@?B@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\"@\"NSString\"@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@16@?24"
- "Vv32@0:8Q16@?24"
- "Vv32@0:8Q16@?<v@?@\"NSString\"@\"NSString\"@\"NSString\"@\"NSError\">24"
- "Vv32@0:8q16@?24"
- "Vv32@0:8q16@?<v@?@\"NSError\">24"
- "Vv36@0:8@\"NSUUID\"16B24@?<v@?@\"NSUUID\"@\"NSError\">28"
- "Vv36@0:8@16B24@?28"
- "Vv40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSArray\"QQ@\"NSData\"@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?Q@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"MASDAssetMetadata\"@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSFileHandle\"@\"NSData\"@\"NSData\"@\"NSError\">32"
- "Vv40@0:8@\"NSUUID\"16Q24@?<v@?@\"NSDate\"@\"NSError\">32"
- "Vv40@0:8@16@24@?32"
- "Vv40@0:8@16Q24@?32"
- "Vv48@0:8@\"MASDAssetDescriptor\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSString\"@\"NSError\">40"
- "Vv48@0:8@\"NSArray\"16@\"NSUUID\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "Vv48@0:8@\"NSArray\"16Q24@\"NSDictionary\"32@?<v@?@\"NSArray\"@\"NSDictionary\"@\"NSError\">40"
- "Vv48@0:8@\"NSString\"16@\"NSArray\"24@\"NSDictionary\"32@?<v@?@\"NSError\">40"
- "Vv48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?@\"NSArray\"@\"NSError\">40"
- "Vv48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?@\"NSError\">40"
- "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?@\"NSError\">40"
- "Vv48@0:8@\"NSString\"16Q24@\"NSDictionary\"32@?<v@?@\"NSFileHandle\"@\"NSDictionary\"@\"NSError\">40"
- "Vv48@0:8@16@24@32@?40"
- "Vv48@0:8@16Q24@32@?40"
- "Vv48@0:8q16Q24@\"NSString\"32@?<v@?@\"NSFileHandle\"@\"NSString\"@\"NSData\"@\"NSError\">40"
- "Vv48@0:8q16Q24@32@?40"
- "Vv52@0:8@\"NSString\"16Q24@\"NSDictionary\"32B40@?<v@?@\"NSString\"@\"NSDictionary\"@\"NSString\"@\"NSError\">44"
- "Vv52@0:8@16Q24@32B40@?44"
- "Vv56@0:8@\"NSDictionary\"16@\"NSDictionary\"24Q32@\"NSData\"40@?<v@?@\"NSString\"Q@\"NSError\">48"
- "Vv56@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32@\"NSDictionary\"40@?<v@?@\"NSError\">48"
- "Vv56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSError\">48"
- "Vv56@0:8@16@24@32@40@?48"
- "Vv56@0:8@16@24Q32@40@?48"
- "Vv56@0:8{?=[8I]}16@?48"
- "Vv56@0:8{?=[8I]}16@?<v@?@\"NSError\">48"
- "Vv56@0:8{?=[8I]}16@?<v@?Q@\"NSError\">48"
- "Vv56@0:8{?=[8I]}16@?<v@?Q@\"NSString\"@\"NSError\">48"
- "WakeUp"
- "^{_NSZone=}16@0:8"
- "^{__CFNotificationCenter=}"
- "_assetEventFilters"
- "_assetEventObservers"
- "_assets"
- "_attributes"
- "_automicallyReleaseExtension"
- "_backgroundQueue"
- "_bidirectionalXPCObservers"
- "_bidirectionalXPCObserversMetaData"
- "_bidirectional_xpcObserver_lock"
- "_conn"
- "_darwinCenter"
- "_extHandle"
- "_fasConn"
- "_has"
- "_lastUpdateAlgorithmVersion"
- "_lastUpdateOSVersion"
- "_name"
- "_notifyQueue"
- "_options"
- "_pathname"
- "_profileEventFilters"
- "_profileEventObservers"
- "_profileType"
- "_released"
- "_remoteNotifyQueue"
- "_remoteObserverConn"
- "_remotesharingObservers"
- "_serviceName"
- "_setError"
- "addAnchorGroup:clientIdentifier:error:"
- "addAssetChangeEventObserver:type:events:error:"
- "addAssets:"
- "addEntriesFromDictionary:"
- "addFileEventObserver:fileNames:sharingGroup:profile:events:error:"
- "addKVStoreEventObserver:storeNames:sharingGroup:profile:events:error:"
- "addObject:"
- "addObjectsFromArray:"
- "addOrUpdateDataForAnchorIdentifier:clientIdentifier:data:completion:"
- "addOrUpdateDataForAnchorIdentifier:clientIdentifier:data:error:"
- "addPointer:"
- "addProfileChangeEventObserver:events:error:"
- "algorithmVersion"
- "allKeys"
- "allObjects"
- "allocWithZone:"
- "appendFormat:"
- "array"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "assetDataLen"
- "assetDataPath"
- "assetFileHandle"
- "assetMetaData"
- "assetsAtIndex:"
- "assetsCount"
- "assetsType"
- "attributes"
- "attributesOfFileSystemForPath:error:"
- "automicallyReleaseExtension"
- "autorelease"
- "availableData"
- "availableSpace:error:"
- "boolValue"
- "bytes"
- "cStringUsingEncoding:"
- "checkIfCloudZonesWithCompletionHandler:"
- "checkIfKVStoreGroupExistUsing:exist:error:"
- "checkIfKVStoreGroupExistUsing:reply:"
- "ckrecordIdentifier"
- "class"
- "clearAssets"
- "closeAndReturnError:"
- "closeFile"
- "commitFile:attributes:completion:"
- "commitFile:attributes:error:"
- "commitFile:attributes:reply:"
- "compact"
- "conformsToProtocol:"
- "constructV2Blob:expectedSize:sizeLimit:profileType:error:"
- "containsObject:"
- "contentsOfDirectoryAtPath:error:"
- "copy"
- "copyTo:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAssetWithDescriptor:UUID:completion:"
- "createAssetWithDescriptor:UUID:error:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createKVStore:fields:attributes:reply:"
- "createKVStore:recordFields:attributes:completion:"
- "createKVStore:recordFields:attributes:error:"
- "createProfileWith:guest:error:"
- "d"
- "d16@0:8"
- "daemonTest:completion:"
- "data"
- "dataWithBytes:length:"
- "dataWithContentsOfFile:"
- "dataWithJSONObject:options:error:"
- "dataWithLength:"
- "dataWithPropertyList:format:options:error:"
- "dealloc"
- "debugDescription"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "defaultManager"
- "deleteAllAssetsExcept:error:"
- "deleteAllAssetsWithCompletion:"
- "deleteAllAssetsWithOptions:completion:"
- "deleteAllAssetsWithOptions:error:"
- "deleteAllAssetsWithUUID:completion:"
- "deleteAllAssetsWithUUID:error:"
- "deleteAllNonDefaultProfilesWithError:"
- "deleteAssetWithHandle:UUID:completion:"
- "deleteAssetWithHandle:UUID:error:"
- "deleteAssetWithHandle:withOptions:completion:"
- "deleteAssetWithHandle:withOptions:error:"
- "deleteAssetsWithOptions:completion:"
- "deleteDataInStore:keys:attributes:completion:"
- "deleteDataInStore:keys:attributes:error:"
- "deleteDataInStore:keys:attributes:reply:"
- "deleteFile:attributes:completion:"
- "deleteFile:attributes:error:"
- "deleteFile:attributes:reply:"
- "deleteKVStore:attributes:completion:"
- "deleteKVStore:attributes:error:"
- "deleteKVStore:attributes:reply:"
- "deleteProfileWith:error:"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "didReceiveAssetChangeWith:assethandles:"
- "didReceiveError:"
- "didReceiveFileEventWith:filenames:profile:group:"
- "didReceiveKVStoreEventWith:KVStores:profile:group:"
- "didReceiveProfileChangeWith:profile:type:"
- "didReceiveShareAssets:participant:error:"
- "diskUsage:attributes:usage:error:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "exportAllAssets:error:"
- "exportAssets:option:error:"
- "exportAssetsToPath:option:profile:error:"
- "exportCorePrescription:profile:payloadSize:sizeLimit:profileType:error:"
- "exportedInterface"
- "fetchCoreRxLensData:recordUUID:accPayload:rxIdL:rxIdR:axisL:axisR:calRequiredL:calRequiredR:version:attributes:attributesOut:recordUUIDOut:error:"
- "fetchCoreRxLensData:recordUUID:accPayload:rxIdL:rxIdR:axisL:axisR:calRequiredL:calRequiredR:version:attributes:completion:"
- "fetchCoreRxLensData:recordUUID:accPayload:rxIdL:rxIdR:axisL:axisR:calRequiredL:calRequiredR:version:attributes:reply:"
- "fileDescriptor"
- "fileExistsAtPath:isDirectory:"
- "fileHandleForReadingAtPath:"
- "fileOrKVStoreObserverXPCExitHandler:"
- "fileSystemRepresentation"
- "getAllAnchorGroupsForClient:error:"
- "getAllProfilesWith:error:"
- "getAssetDataWithHandle:UUID:completion:"
- "getAssetDataWithHandle:UUID:error:"
- "getAssetMetaDataWithHandle:UUID:completion:"
- "getAssetMetaDataWithHandle:UUID:error:"
- "getBytes:range:"
- "getConnectedClientsWithCompletion:"
- "getDaemonProcessInfo:"
- "getDataForAllAnchors:completion:"
- "getDataForAllAnchors:error:"
- "getDataForAnchorIdentifier:clientIdentifier:completion:"
- "getDataForAnchorIdentifier:clientIdentifier:error:"
- "getDiskUsage:attributes:reply:"
- "getInUseStatusReport:"
- "getLastSwitchTimeForPersistedGuestWithError:"
- "getProfileLastSwitchInTS:error:"
- "getProfileLastSwitchOutTS:error:"
- "getProfileSwitchTime:mode:completion:"
- "hasAssetData"
- "hasAssetState"
- "hasCreatorAttest"
- "hasDeviceIdentifier"
- "hasDeviceName"
- "hasEnrollmentIdentifier"
- "hasError"
- "hasLabel"
- "hasLastUpdateAlgorithmVersion"
- "hasServerAttest"
- "hasSuffix:"
- "hash"
- "importAllAssets:completion:"
- "importAssets:option:completion:"
- "importAssetsFromPath:option:completion:"
- "importCorePrescription:profile:error:"
- "init"
- "initAssetMetadataWithInfoDictionary:"
- "initDescriptorWithOptions:withData:error:"
- "initDescriptorWithType:withLabel:withData:withVersion:"
- "initDescriptorWithType:withLabel:withData:withVersion:withSyncOption:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithData:"
- "initWithFormat:arguments:"
- "initWithLength:"
- "initWithMachServiceName:options:"
- "initWithName:type:options:"
- "initWithPath:attributes:extensionHandle:"
- "initWithUUIDString:"
- "integerValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualForAllFields:"
- "isEqualToData:"
- "isEqualToDate:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isReadableFileAtPath:"
- "isSameObserver:error:"
- "isWritableFileAtPath:"
- "keyEnumerator"
- "lastUpdatedAlgorithmVersion"
- "lastUpdatedOSVersion"
- "length"
- "mergeFrom:"
- "mutableBytes"
- "now"
- "null"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithLongLong:"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "openFile:mode:attributes:attributesOut:error:"
- "openFile:mode:attributes:completion:"
- "openFile:mode:attributes:reply:"
- "openFiles:mode:attributes:reply:"
- "options"
- "parseAssetBlob:error:"
- "parseExportOption:error:"
- "parseV2BlobPayload:error:"
- "participantIdentifier"
- "pathWithComponents:"
- "pathname"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistGuestProfileWithError:"
- "pointerAtIndex:"
- "position"
- "prefetchFile:attributes:completion:"
- "propertyListWithData:options:format:error:"
- "putDataInStore:records:attributes:completion:"
- "putDataInStore:records:attributes:error:"
- "putDataInStore:records:attributes:reply:"
- "q"
- "q16@0:8"
- "queryAssetMetaDataWithOptions:error:"
- "queryAssetsWithOptions:completion:"
- "queryAssetsWithOptions:error:"
- "queryDataInStore:keys:attributes:completion:"
- "queryDataInStore:keys:attributes:error:"
- "queryDataInStore:keys:attributes:reply:"
- "queryFile:attributes:completion:"
- "queryFile:attributes:error:"
- "queryFile:attributes:reply:"
- "queryInUseStatusWithAppBundle:completion:"
- "queryInUseStatusWithAuditToken:completion:"
- "readDataToEndOfFileAndReturnError:"
- "readFrom:"
- "recoverRemoteAsset:"
- "recoverRemoteAsset:completion:"
- "recoveryTaskWhenDaemonIsReady"
- "recreateFileOrKVStoreObserverXPCWith:error:"
- "recreateRemoteObserverXPCWith:"
- "registerDarwinNotification:"
- "registerOberverWithAppBundle:completion:"
- "registerOberverWithAuditToken:completion:"
- "release"
- "releaseSandboxExtension"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "remoteObserverXPCExitHandler"
- "removeAllAnchorGroupsForClient:error:"
- "removeAllObjects"
- "removeAnchorGroup:clientIdentifier:error:"
- "removeDataForAllAnchors:error:"
- "removeDataForAnchorIdentifiers:clientIdentifier:error:"
- "removeItemAtPath:error:"
- "removeNotificationObserver:"
- "removeNotificationObserverPointer:observerType:"
- "removeObjectForKey:"
- "removeObserverFromFilter:"
- "removePointerAtIndex:"
- "requestFile:isDirectory:mode:attributes:completion:"
- "requestFile:isDirectory:mode:attributes:error:"
- "requestFileWithSandboxExtension:mode:attributes:isDirectory:reply:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "sandboxToken"
- "saveAVPSetupUserOption:completion:"
- "saveAVPSetupUserOption:error:"
- "saveObserverMetaData:fileNames:sharingGroup:profile:events:type:"
- "seekToFileOffset:"
- "self"
- "sessionIdentifier"
- "set"
- "setAssetData:"
- "setAssetDataLen:"
- "setAssetDataPath:"
- "setAssetFileHandle:"
- "setAssetHandle:"
- "setAssetMetaData:"
- "setAssetState:"
- "setAssets:"
- "setAttributes:ofItemAtPath:error:"
- "setAutomicallyReleaseExtension:"
- "setCkrecordIdentifier:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCreationTime:"
- "setCreatorAttest:"
- "setDeviceIdentifier:"
- "setDeviceName:"
- "setEnrollmentIdentifier:"
- "setExportedInterface:"
- "setExportedObject:"
- "setHasAssetState:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLabel:"
- "setLastUpdateAlgorithmVersion:"
- "setLastUpdateOSVersion:"
- "setLastUpdatedAlgorithmVersion:"
- "setLastUpdatedOSVersion:"
- "setLastUpdatedTime:"
- "setName:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOptions:"
- "setPosition:"
- "setProfileType:"
- "setRemoteObjectInterface:"
- "setSandboxToken:"
- "setServerAttest:"
- "setType:"
- "setWithObjects:"
- "sharedInstance"
- "stringWithCapacity:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "strongToStrongObjectsMapTable"
- "subdataWithRange:"
- "subscribeDarwinNotification:"
- "superclass"
- "supportsSecureCoding"
- "switchProfileWith:error:"
- "syncOption"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "testDaemon:results:error:"
- "timeIntervalSince1970"
- "unarchivedObjectOfClasses:fromData:error:"
- "unpersistGuestProfileWithError:"
- "unregisterDarwinNotificationIfNeed:"
- "unregisterOberverWithAppBundle:completion:"
- "unregisterOberverWithAuditToken:completion:"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "unsubscribeDarwinNotification:"
- "updateAssetHandle:withOptions:assetData:completion:"
- "updateAssetHandle:withOptions:assetData:error:"
- "updateAssetHandleWithOptions:options:assetData:completion:"
- "updateAssetHandleWithOptions:options:assetData:error:"
- "updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:"
- "updateAssetWithHandle:UUID:assetData:assetAlgorithm:error:"
- "updateDataInStore:keys:values:attributes:completion:"
- "updateDataInStore:keys:values:attributes:error:"
- "updateDataInStore:keys:values:attributes:reply:"
- "v104@0:8@16@24@32q40q48q56q64B72B76Q80@88@?96"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8Q16@\"NSDictionary\"24"
- "v32@0:8Q16@24"
- "v40@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSError\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8Q16@\"NSString\"24Q32"
- "v40@0:8Q16@24Q32"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16Q24@32@?40"
- "v48@0:8Q16@\"NSArray\"24@\"NSString\"32@\"NSString\"40"
- "v48@0:8Q16@24@32@40"
- "v52@0:8@16B24Q28@36@?44"
- "v56@0:8@16@24@32@40@?48"
- "v64@0:8@\"NSString\"16Q24@\"NSArray\"32@\"NSString\"40Q48@?<v@?@\"NSError\">56"
- "v64@0:8@16@24@32@40Q48Q56"
- "v64@0:8@16Q24@32@40Q48@?56"
- "weakObjectsPointerArray"
- "weakToStrongObjectsMapTable"
- "weakToWeakObjectsMapTable"
- "writeData:error:"
- "writeTo:"
- "writeToFile:options:error:"
- "writeV2BlobWith:optype:payload:profileType:error:"
- "zone"
- "{?=\"assetState\"b1}"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
