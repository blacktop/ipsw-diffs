## ManagedAssets

> `/System/Library/PrivateFrameworks/ManagedAssets.framework/ManagedAssets`

```diff

-269.0.14.0.0
-  __TEXT.__text: 0x2862c
+269.0.17.0.0
+  __TEXT.__text: 0x28a8c
   __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x120c
+  __TEXT.__objc_methlist: 0x122c
   __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0xf04
+  __TEXT.__gcc_except_tab: 0xf24
   __TEXT.__cstring: 0x34b3
-  __TEXT.__oslogstring: 0x292e
-  __TEXT.__unwind_info: 0x998
+  __TEXT.__oslogstring: 0x29af
+  __TEXT.__unwind_info: 0x9a8
   __TEXT.__objc_classname: 0x20e
-  __TEXT.__objc_methname: 0x3699
-  __TEXT.__objc_methtype: 0x132b
-  __TEXT.__objc_stubs: 0x2160
+  __TEXT.__objc_methname: 0x36da
+  __TEXT.__objc_methtype: 0x1369
+  __TEXT.__objc_stubs: 0x2180
   __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x1318
+  __DATA_CONST.__const: 0x1340
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd10
+  __DATA_CONST.__objc_selrefs: 0xd20
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x1f0
   __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0x2580
-  __AUTH_CONST.__objc_const: 0x1890
+  __AUTH_CONST.__objc_const: 0x1898
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 09BF197D-80A0-3AAD-832D-270A4A25BBF6
-  Functions: 744
-  Symbols:   2746
-  CStrings:  1667
+  UUID: 59CDE06B-79A3-337D-B937-2BFA050BB452
+  Functions: 749
+  Symbols:   2761
+  CStrings:  1675
 
Symbols:
+ -[ManagedAssetsClient saveAVPSetupUserOption:error:]
+ GCC_except_table168
+ GCC_except_table181
+ GCC_except_table190
+ GCC_except_table198
+ ___145-[ManagedAssetsClient fetchCoreRxLensData:recordUUID:accPayload:rxIdL:rxIdR:axisL:axisR:calRequiredL:calRequiredR:version:attributes:completion:]_block_invoke.281
+ ___168-[ManagedAssetsClient fetchCoreRxLensData:recordUUID:accPayload:rxIdL:rxIdR:axisL:axisR:calRequiredL:calRequiredR:version:attributes:attributesOut:recordUUIDOut:error:]_block_invoke.283
+ ___168-[ManagedAssetsClient fetchCoreRxLensData:recordUUID:accPayload:rxIdL:rxIdR:axisL:axisR:calRequiredL:calRequiredR:version:attributes:attributesOut:recordUUIDOut:error:]_block_invoke.283.cold.1
+ ___27-[ManagedAssetsClient init]_block_invoke.208
+ ___42-[ManagedAssetsClient recoverRemoteAsset:]_block_invoke.273
+ ___42-[ManagedAssetsClient recoverRemoteAsset:]_block_invoke.273.cold.1
+ ___48-[ManagedAssetsClient testDaemon:results:error:]_block_invoke.284
+ ___48-[ManagedAssetsClient testDaemon:results:error:]_block_invoke.284.cold.1
+ ___52-[ManagedAssetsClient saveAVPSetupUserOption:error:]_block_invoke
+ ___52-[ManagedAssetsClient saveAVPSetupUserOption:error:]_block_invoke.302
+ ___52-[ManagedAssetsClient saveAVPSetupUserOption:error:]_block_invoke.302.cold.1
+ ___52-[ManagedAssetsClient saveAVPSetupUserOption:error:]_block_invoke.cold.1
+ ___53-[ManagedAssetsClient recreateRemoteObserverXPCWith:]_block_invoke.294
+ ___60-[ManagedAssetsClient createAssetWithDescriptor:UUID:error:]_block_invoke.257
+ ___60-[ManagedAssetsClient createAssetWithDescriptor:UUID:error:]_block_invoke.257.cold.1
+ ___60-[ManagedAssetsClient createAssetWithDescriptor:UUID:error:]_block_invoke.257.cold.2
+ ___60-[ManagedAssetsClient createAssetWithDescriptor:UUID:error:]_block_invoke.258
+ ___62-[ManagedAssetsClient didReceiveAssetChangeWith:assethandles:]_block_invoke.278
+ ___62-[ManagedAssetsClient getAssetDataWithHandle:UUID:completion:]_block_invoke.274
+ ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.251.cold.1
+ ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.251.cold.2
+ ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.254
+ ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.255
+ ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke_2.252
+ ___65-[ManagedAssetsClient(AnchorPersist) getDataForAllAnchors:error:]_block_invoke.45
+ ___66-[ManagedAssetsClient recreateFileOrKVStoreObserverXPCWith:error:]_block_invoke.285
+ ___68-[ManagedAssetsClient(AnchorPersist) removeDataForAllAnchors:error:]_block_invoke.46
+ ___68-[ManagedAssetsClient(AnchorPersist) removeDataForAllAnchors:error:]_block_invoke.46.cold.1
+ ___69-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:error:]_block_invoke.268
+ ___70-[ManagedAssetsClient(AnchorPersist) getDataForAllAnchors:completion:]_block_invoke.27.cold.1
+ ___70-[ManagedAssetsClient(AnchorPersist) getDataForAllAnchors:completion:]_block_invoke.29
+ ___70-[ManagedAssetsClient(AnchorPersist) getDataForAllAnchors:completion:]_block_invoke.36
+ ___70-[ManagedAssetsClient(AnchorPersist) getDataForAllAnchors:completion:]_block_invoke.36.cold.1
+ ___70-[ManagedAssetsClient(AnchorPersist) getDataForAllAnchors:completion:]_block_invoke.38
+ ___72-[ManagedAssetsClient(AnchorPersist) getAllAnchorGroupsForClient:error:]_block_invoke.52
+ ___72-[ManagedAssetsClient(AnchorPersist) getAllAnchorGroupsForClient:error:]_block_invoke.52.cold.1
+ ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke.263
+ ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke.263.cold.1
+ ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke.265
+ ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke_2.264
+ ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke_2.266
+ ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke_3.267
+ ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke_3.267.cold.1
+ ___75-[ManagedAssetsClient(AnchorPersist) removeAllAnchorGroupsForClient:error:]_block_invoke.54
+ ___75-[ManagedAssetsClient(AnchorPersist) removeAllAnchorGroupsForClient:error:]_block_invoke.54.cold.1
+ ___76-[ManagedAssetsClient(AnchorPersist) addAnchorGroup:clientIdentifier:error:]_block_invoke.50
+ ___76-[ManagedAssetsClient(AnchorPersist) addAnchorGroup:clientIdentifier:error:]_block_invoke.50.cold.1
+ ___79-[ManagedAssetsClient(AnchorPersist) removeAnchorGroup:clientIdentifier:error:]_block_invoke.51
+ ___79-[ManagedAssetsClient(AnchorPersist) removeAnchorGroup:clientIdentifier:error:]_block_invoke.51.cold.1
+ ___81-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:error:]_block_invoke.262
+ ___86-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:]_block_invoke.259
+ ___86-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:]_block_invoke.259.cold.1
+ ___86-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:]_block_invoke.261
+ ___86-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:]_block_invoke_2.260
+ ___93-[ManagedAssetsClient(AnchorPersist) getDataForAnchorIdentifier:clientIdentifier:completion:]_block_invoke.43
+ ___93-[ManagedAssetsClient(AnchorPersist) getDataForAnchorIdentifier:clientIdentifier:completion:]_block_invoke.43.cold.1
+ ___93-[ManagedAssetsClient(AnchorPersist) getDataForAnchorIdentifier:clientIdentifier:completion:]_block_invoke.43.cold.2
+ ___block_descriptor_56_e8_32r40r_e17_v16?0"NSError"8lr32l8r40l8
+ ___block_literal_global.210
+ ___block_literal_global.272
+ _objc_msgSend$saveAVPSetupUserOption:completion:
- GCC_except_table178
- GCC_except_table187
- GCC_except_table195
- ___145-[ManagedAssetsClient fetchCoreRxLensData:recordUUID:accPayload:rxIdL:rxIdR:axisL:axisR:calRequiredL:calRequiredR:version:attributes:completion:]_block_invoke.278
- ___168-[ManagedAssetsClient fetchCoreRxLensData:recordUUID:accPayload:rxIdL:rxIdR:axisL:axisR:calRequiredL:calRequiredR:version:attributes:attributesOut:recordUUIDOut:error:]_block_invoke.280
- ___168-[ManagedAssetsClient fetchCoreRxLensData:recordUUID:accPayload:rxIdL:rxIdR:axisL:axisR:calRequiredL:calRequiredR:version:attributes:attributesOut:recordUUIDOut:error:]_block_invoke.280.cold.1
- ___27-[ManagedAssetsClient init]_block_invoke.199
- ___42-[ManagedAssetsClient recoverRemoteAsset:]_block_invoke.270
- ___42-[ManagedAssetsClient recoverRemoteAsset:]_block_invoke.270.cold.1
- ___48-[ManagedAssetsClient testDaemon:results:error:]_block_invoke.281
- ___48-[ManagedAssetsClient testDaemon:results:error:]_block_invoke.281.cold.1
- ___53-[ManagedAssetsClient recreateRemoteObserverXPCWith:]_block_invoke.291
- ___60-[ManagedAssetsClient createAssetWithDescriptor:UUID:error:]_block_invoke.254
- ___60-[ManagedAssetsClient createAssetWithDescriptor:UUID:error:]_block_invoke.254.cold.1
- ___60-[ManagedAssetsClient createAssetWithDescriptor:UUID:error:]_block_invoke.254.cold.2
- ___60-[ManagedAssetsClient createAssetWithDescriptor:UUID:error:]_block_invoke.255
- ___62-[ManagedAssetsClient didReceiveAssetChangeWith:assethandles:]_block_invoke.275
- ___62-[ManagedAssetsClient getAssetDataWithHandle:UUID:completion:]_block_invoke.271
- ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.248
- ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.248.cold.1
- ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.248.cold.2
- ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.252
- ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke_2.249
- ___65-[ManagedAssetsClient(AnchorPersist) getDataForAllAnchors:error:]_block_invoke.43
- ___66-[ManagedAssetsClient recreateFileOrKVStoreObserverXPCWith:error:]_block_invoke.282
- ___68-[ManagedAssetsClient(AnchorPersist) removeDataForAllAnchors:error:]_block_invoke.45
- ___68-[ManagedAssetsClient(AnchorPersist) removeDataForAllAnchors:error:]_block_invoke.45.cold.1
- ___69-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:error:]_block_invoke.265
- ___70-[ManagedAssetsClient(AnchorPersist) getDataForAllAnchors:completion:]_block_invoke.35
- ___70-[ManagedAssetsClient(AnchorPersist) getDataForAllAnchors:completion:]_block_invoke.35.cold.1
- ___70-[ManagedAssetsClient(AnchorPersist) getDataForAllAnchors:completion:]_block_invoke.37
- ___70-[ManagedAssetsClient(AnchorPersist) getDataForAllAnchors:completion:]_block_invoke_2
- ___72-[ManagedAssetsClient(AnchorPersist) getAllAnchorGroupsForClient:error:]_block_invoke.51
- ___72-[ManagedAssetsClient(AnchorPersist) getAllAnchorGroupsForClient:error:]_block_invoke.51.cold.1
- ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke.260
- ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke.260.cold.1
- ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke.262
- ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke_2.261
- ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke_2.263
- ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke_3.264
- ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke_3.264.cold.1
- ___75-[ManagedAssetsClient(AnchorPersist) removeAllAnchorGroupsForClient:error:]_block_invoke.53
- ___75-[ManagedAssetsClient(AnchorPersist) removeAllAnchorGroupsForClient:error:]_block_invoke.53.cold.1
- ___76-[ManagedAssetsClient(AnchorPersist) addAnchorGroup:clientIdentifier:error:]_block_invoke.49
- ___76-[ManagedAssetsClient(AnchorPersist) addAnchorGroup:clientIdentifier:error:]_block_invoke.49.cold.1
- ___79-[ManagedAssetsClient(AnchorPersist) removeAnchorGroup:clientIdentifier:error:]_block_invoke.50
- ___79-[ManagedAssetsClient(AnchorPersist) removeAnchorGroup:clientIdentifier:error:]_block_invoke.50.cold.1
- ___81-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:error:]_block_invoke.259
- ___86-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:]_block_invoke.256
- ___86-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:]_block_invoke.256.cold.1
- ___86-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:]_block_invoke.258
- ___86-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:]_block_invoke_2.257
- ___93-[ManagedAssetsClient(AnchorPersist) getDataForAnchorIdentifier:clientIdentifier:completion:]_block_invoke.42
- ___93-[ManagedAssetsClient(AnchorPersist) getDataForAnchorIdentifier:clientIdentifier:completion:]_block_invoke.42.cold.1
- ___93-[ManagedAssetsClient(AnchorPersist) getDataForAnchorIdentifier:clientIdentifier:completion:]_block_invoke.42.cold.2
- ___block_literal_global.198
- ___block_literal_global.269
CStrings:
+ "B32@0:8q16^@24"
+ "Vv32@0:8q16@?24"
+ "Vv32@0:8q16@?<v@?@\"NSError\">24"
+ "failed to get all anchors for client, error: %@"
+ "failed to perform saveAVPSetupUserOption, error: %@"
+ "notifyAVPSetupUserOption:%ld"
+ "saveAVPSetupUserOption:completion:"
+ "saveAVPSetupUserOption:error:"

```
