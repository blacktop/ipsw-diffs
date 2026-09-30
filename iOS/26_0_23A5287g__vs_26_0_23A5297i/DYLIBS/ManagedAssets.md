## ManagedAssets

> `/System/Library/PrivateFrameworks/ManagedAssets.framework/ManagedAssets`

```diff

-269.0.19.0.0
-  __TEXT.__text: 0x28908
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x122c
+269.0.21.0.0
+  __TEXT.__text: 0x28a54
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__objc_methlist: 0x1234
   __TEXT.__const: 0xd0
   __TEXT.__gcc_except_tab: 0xf08
-  __TEXT.__cstring: 0x34b3
-  __TEXT.__oslogstring: 0x297c
-  __TEXT.__unwind_info: 0x9a8
+  __TEXT.__cstring: 0x34e0
+  __TEXT.__oslogstring: 0x29ba
+  __TEXT.__unwind_info: 0x9b0
   __TEXT.__objc_classname: 0x20e
-  __TEXT.__objc_methname: 0x36da
+  __TEXT.__objc_methname: 0x36f4
   __TEXT.__objc_methtype: 0x1369
-  __TEXT.__objc_stubs: 0x2160
+  __TEXT.__objc_stubs: 0x2180
   __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x1340
+  __DATA_CONST.__const: 0x1348
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd20
+  __DATA_CONST.__objc_selrefs: 0xd28
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x1f0
-  __AUTH_CONST.__auth_got: 0x338
+  __AUTH_CONST.__auth_got: 0x340
   __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x2580
+  __AUTH_CONST.__cfstring: 0x25e0
   __AUTH_CONST.__objc_const: 0x1898
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x11c
-  __DATA.__data: 0x710
+  __DATA.__data: 0x718
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1AD5DDF0-6751-3EC6-BB24-F81EB812D848
-  Functions: 748
-  Symbols:   2752
-  CStrings:  1674
+  UUID: E4E11922-33D1-3B02-8197-26388599A4F8
+  Functions: 749
+  Symbols:   2758
+  CStrings:  1682
 
Symbols:
+ -[ManagedAssetsClient removeObserverFromFilter:]
+ GCC_except_table104
+ GCC_except_table107
+ GCC_except_table119
+ GCC_except_table127
+ GCC_except_table146
+ GCC_except_table149
+ GCC_except_table154
+ GCC_except_table159
+ GCC_except_table169
+ GCC_except_table182
+ GCC_except_table191
+ GCC_except_table199
+ GCC_except_table56
+ GCC_except_table67
+ GCC_except_table75
+ GCC_except_table83
+ GCC_except_table96
+ ___145-[ManagedAssetsClient fetchCoreRxLensData:recordUUID:accPayload:rxIdL:rxIdR:axisL:axisR:calRequiredL:calRequiredR:version:attributes:completion:]_block_invoke.286
+ ___168-[ManagedAssetsClient fetchCoreRxLensData:recordUUID:accPayload:rxIdL:rxIdR:axisL:axisR:calRequiredL:calRequiredR:version:attributes:attributesOut:recordUUIDOut:error:]_block_invoke.288
+ ___168-[ManagedAssetsClient fetchCoreRxLensData:recordUUID:accPayload:rxIdL:rxIdR:axisL:axisR:calRequiredL:calRequiredR:version:attributes:attributesOut:recordUUIDOut:error:]_block_invoke.288.cold.1
+ ___27-[ManagedAssetsClient init]_block_invoke.204
+ ___27-[ManagedAssetsClient init]_block_invoke.207
+ ___27-[ManagedAssetsClient init]_block_invoke.210
+ ___42-[ManagedAssetsClient recoverRemoteAsset:]_block_invoke.278
+ ___42-[ManagedAssetsClient recoverRemoteAsset:]_block_invoke.278.cold.1
+ ___48-[ManagedAssetsClient testDaemon:results:error:]_block_invoke.289
+ ___48-[ManagedAssetsClient testDaemon:results:error:]_block_invoke.289.cold.1
+ ___52-[ManagedAssetsClient saveAVPSetupUserOption:error:]_block_invoke.307
+ ___52-[ManagedAssetsClient saveAVPSetupUserOption:error:]_block_invoke.307.cold.1
+ ___53-[ManagedAssetsClient recreateRemoteObserverXPCWith:]_block_invoke.299
+ ___60-[ManagedAssetsClient createAssetWithDescriptor:UUID:error:]_block_invoke.262
+ ___60-[ManagedAssetsClient createAssetWithDescriptor:UUID:error:]_block_invoke.262.cold.1
+ ___60-[ManagedAssetsClient createAssetWithDescriptor:UUID:error:]_block_invoke.262.cold.2
+ ___60-[ManagedAssetsClient createAssetWithDescriptor:UUID:error:]_block_invoke.263
+ ___62-[ManagedAssetsClient didReceiveAssetChangeWith:assethandles:]_block_invoke.283
+ ___62-[ManagedAssetsClient getAssetDataWithHandle:UUID:completion:]_block_invoke.279
+ ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.256
+ ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.256.cold.1
+ ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.256.cold.2
+ ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.259
+ ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.260
+ ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke_2.257
+ ___66-[ManagedAssetsClient recreateFileOrKVStoreObserverXPCWith:error:]_block_invoke.290
+ ___69-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:error:]_block_invoke.273
+ ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke.268
+ ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke.268.cold.1
+ ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke.270
+ ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke_2.269
+ ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke_2.271
+ ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke_3.272
+ ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke_3.272.cold.1
+ ___81-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:error:]_block_invoke.267
+ ___86-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:]_block_invoke.264
+ ___86-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:]_block_invoke.264.cold.1
+ ___86-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:]_block_invoke.266
+ ___86-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:]_block_invoke_2.265
+ ___block_literal_global.203
+ ___block_literal_global.206
+ ___block_literal_global.209
+ ___block_literal_global.212
+ ___block_literal_global.277
+ _dispatch_queue_get_label
+ _kManagedAssetsSerializedFeatureKey
+ _notifyQueueLabel
+ _objc_msgSend$removeObserverFromFilter:
- GCC_except_table103
- GCC_except_table106
- GCC_except_table118
- GCC_except_table126
- GCC_except_table145
- GCC_except_table148
- GCC_except_table153
- GCC_except_table158
- GCC_except_table168
- GCC_except_table181
- GCC_except_table190
- GCC_except_table198
- GCC_except_table26
- GCC_except_table40
- GCC_except_table55
- GCC_except_table66
- GCC_except_table74
- GCC_except_table82
- GCC_except_table95
- ___145-[ManagedAssetsClient fetchCoreRxLensData:recordUUID:accPayload:rxIdL:rxIdR:axisL:axisR:calRequiredL:calRequiredR:version:attributes:completion:]_block_invoke.281
- ___168-[ManagedAssetsClient fetchCoreRxLensData:recordUUID:accPayload:rxIdL:rxIdR:axisL:axisR:calRequiredL:calRequiredR:version:attributes:attributesOut:recordUUIDOut:error:]_block_invoke.283
- ___168-[ManagedAssetsClient fetchCoreRxLensData:recordUUID:accPayload:rxIdL:rxIdR:axisL:axisR:calRequiredL:calRequiredR:version:attributes:attributesOut:recordUUIDOut:error:]_block_invoke.283.cold.1
- ___27-[ManagedAssetsClient init]_block_invoke.202
- ___27-[ManagedAssetsClient init]_block_invoke.205
- ___27-[ManagedAssetsClient init]_block_invoke.208
- ___42-[ManagedAssetsClient recoverRemoteAsset:]_block_invoke.273
- ___42-[ManagedAssetsClient recoverRemoteAsset:]_block_invoke.273.cold.1
- ___48-[ManagedAssetsClient testDaemon:results:error:]_block_invoke.284
- ___48-[ManagedAssetsClient testDaemon:results:error:]_block_invoke.284.cold.1
- ___52-[ManagedAssetsClient saveAVPSetupUserOption:error:]_block_invoke.302
- ___52-[ManagedAssetsClient saveAVPSetupUserOption:error:]_block_invoke.302.cold.1
- ___53-[ManagedAssetsClient recreateRemoteObserverXPCWith:]_block_invoke.294
- ___60-[ManagedAssetsClient createAssetWithDescriptor:UUID:error:]_block_invoke.257
- ___60-[ManagedAssetsClient createAssetWithDescriptor:UUID:error:]_block_invoke.257.cold.1
- ___60-[ManagedAssetsClient createAssetWithDescriptor:UUID:error:]_block_invoke.257.cold.2
- ___60-[ManagedAssetsClient createAssetWithDescriptor:UUID:error:]_block_invoke.258
- ___62-[ManagedAssetsClient didReceiveAssetChangeWith:assethandles:]_block_invoke.278
- ___62-[ManagedAssetsClient getAssetDataWithHandle:UUID:completion:]_block_invoke.274
- ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.251
- ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.251.cold.1
- ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.251.cold.2
- ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.254
- ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke.255
- ___65-[ManagedAssetsClient createAssetWithDescriptor:UUID:completion:]_block_invoke_2.252
- ___66-[ManagedAssetsClient recreateFileOrKVStoreObserverXPCWith:error:]_block_invoke.285
- ___69-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:error:]_block_invoke.268
- ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke.263
- ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke.263.cold.1
- ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke.265
- ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke_2.264
- ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke_2.266
- ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke_3.267
- ___74-[ManagedAssetsClient updateAssetHandle:withOptions:assetData:completion:]_block_invoke_3.267.cold.1
- ___81-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:error:]_block_invoke.262
- ___86-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:]_block_invoke.259
- ___86-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:]_block_invoke.259.cold.1
- ___86-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:]_block_invoke.261
- ___86-[ManagedAssetsClient updateAssetWithHandle:UUID:assetData:assetAlgorithm:completion:]_block_invoke_2.260
- ___block_literal_global.201
- ___block_literal_global.204
- ___block_literal_global.207
- ___block_literal_global.210
- ___block_literal_global.272
CStrings:
+ "%s"
+ "com.apple.managedassets.serializedFeature"
+ "exportAssets completed"
+ "importAssets completed"
+ "removeNotificationObserver:%@ using queue: %@"
+ "removeObserverFromFilter:"
- "removeNotificationObserver:%@"

```
