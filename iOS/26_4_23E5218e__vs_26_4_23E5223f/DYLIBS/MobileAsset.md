## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

```diff

-1837.100.250.0.0
-  __TEXT.__text: 0x8da24
+1837.100.266.0.0
+  __TEXT.__text: 0x8e6a4
   __TEXT.__auth_stubs: 0x9f0
-  __TEXT.__objc_methlist: 0x6aac
+  __TEXT.__objc_methlist: 0x6ae4
   __TEXT.__const: 0x2a8
-  __TEXT.__cstring: 0x128fb
-  __TEXT.__oslogstring: 0xaf04
-  __TEXT.__gcc_except_tab: 0x1350
-  __TEXT.__unwind_info: 0x1ef8
+  __TEXT.__cstring: 0x12a43
+  __TEXT.__oslogstring: 0xb0d8
+  __TEXT.__gcc_except_tab: 0x1398
+  __TEXT.__unwind_info: 0x1f28
   __TEXT.__objc_classname: 0x94b
-  __TEXT.__objc_methname: 0x17820
-  __TEXT.__objc_methtype: 0x1819
-  __TEXT.__objc_stubs: 0x8b00
+  __TEXT.__objc_methname: 0x178da
+  __TEXT.__objc_methtype: 0x182e
+  __TEXT.__objc_stubs: 0x8b80
   __DATA_CONST.__got: 0x448
-  __DATA_CONST.__const: 0x23f8
+  __DATA_CONST.__const: 0x2490
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3578
+  __DATA_CONST.__objc_selrefs: 0x35a0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x2f0
   __AUTH_CONST.__auth_got: 0x508
-  __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0xf340
+  __AUTH_CONST.__const: 0x7c0
+  __AUTH_CONST.__cfstring: 0xf440
   __AUTH_CONST.__objc_const: 0xa7a0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH.__objc_data: 0xaf0
   __DATA.__objc_ivar: 0x8f0
   __DATA.__data: 0x358
-  __DATA.__bss: 0x1a0
+  __DATA.__bss: 0x1c0
   __DATA_DIRTY.__objc_data: 0xdc0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x1f0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BE5449E1-5612-37AD-9DA8-822828ED54BB
-  Functions: 2967
-  Symbols:   9032
-  CStrings:  7615
+  UUID: C36704EA-6F3C-39E8-97D3-A02CBD03738C
+  Functions: 2982
+  Symbols:   9080
+  CStrings:  7644
 
Symbols:
+ +[MAAutoAsset waitForStartupActivated]
+ -[MAAutoAsset _waitForStartupActivatedFailure:withResponseError:description:completion:]
+ -[MAAutoAsset _waitForStartupActivatedSuccess:]
+ -[MAAutoAsset _waitForStartupActivatedThen:]
+ -[MAAutoAsset _waitForStartupActivated]
+ GCC_except_table164
+ GCC_except_table170
+ GCC_except_table177
+ GCC_except_table183
+ GCC_except_table202
+ GCC_except_table208
+ GCC_except_table213
+ GCC_except_table219
+ GCC_except_table224
+ GCC_except_table230
+ GCC_except_table235
+ GCC_except_table242
+ GCC_except_table247
+ GCC_except_table262
+ GCC_except_table269
+ GCC_except_table279
+ GCC_except_table284
+ GCC_except_table290
+ GCC_except_table295
+ GCC_except_table301
+ GCC_except_table306
+ GCC_except_table309
+ GCC_except_table311
+ _MAPreferencesShouldSecureNetworkMonitorInhibitConnected
+ _MAPreferencesShouldSecureNetworkMonitorInhibitConnected._secureNetworkMonitorInhibitConnected
+ _MAPreferencesShouldSecureNetworkMonitorInhibitConnected.cold.1
+ _MAPreferencesShouldSecureNetworkMonitorInhibitConnected.onceToken
+ ___101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke.997
+ ___39-[MAAutoAsset _waitForStartupActivated]_block_invoke
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1230
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1231
+ ___44-[MAAutoAsset _waitForStartupActivatedThen:]_block_invoke
+ ___44-[MAAutoAsset _waitForStartupActivatedThen:]_block_invoke_2
+ ___44-[MAAutoAsset _waitForStartupActivatedThen:]_block_invoke_3
+ ___50-[MAPushNotificationController _serviceConnection]_block_invoke.1218
+ ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1259
+ ___65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.974
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1224
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1225
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1229
+ ___Block_byref_object_copy_.1393
+ ___Block_byref_object_copy_.768
+ ___Block_byref_object_dispose_.1394
+ ___Block_byref_object_dispose_.769
+ ___MAPreferencesShouldSecureNetworkMonitorInhibitConnected_block_invoke
+ ___MAPreferencesShouldSecureNetworkMonitorInhibitConnected_block_invoke.cold.1
+ ____MAPreferencesCopyValue_block_invoke.1525
+ ____MAensureExtension_block_invoke.1400
+ ____MAsendDownloadAsset_block_invoke.1304
+ ____MAsendPMVCancelDownload_block_invoke.1322
+ ____MAsendPMVDownload_block_invoke.1310
+ ___assetTypeWithWildcardDisallowedCharacterSet_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e42_v24?0"SUCoreConnectMessage"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.1033
+ ___block_literal_global.1035
+ ___block_literal_global.1037
+ ___block_literal_global.1040
+ ___block_literal_global.1213
+ ___block_literal_global.1217
+ ___block_literal_global.1221
+ ___block_literal_global.1223
+ ___block_literal_global.1224
+ ___block_literal_global.1241
+ ___block_literal_global.1265
+ ___block_literal_global.1270
+ ___block_literal_global.1280
+ ___block_literal_global.1285
+ ___block_literal_global.1307
+ ___block_literal_global.1500
+ ___block_literal_global.1524
+ ___block_literal_global.1531
+ ___block_literal_global.1533
+ ___block_literal_global.1538
+ ___block_literal_global.1540
+ ___block_literal_global.1542
+ ___block_literal_global.1544
+ ___block_literal_global.1547
+ ___block_literal_global.2943
+ ___block_literal_global.2945
+ ___block_literal_global.2947
+ ___block_literal_global.2949
+ _assetTypeWithWildcardDisallowedCharacterSet
+ _assetTypeWithWildcardDisallowedCharacterSet.cold.1
+ _assetTypeWithWildcardDisallowedCharacterSet.disallowedSet
+ _assetTypeWithWildcardDisallowedCharacterSet.once
+ _kMobileAssetPreferencesDownloadManagerSyncDelaySecs
+ _kMobileAssetPreferencesSecureNetworkMonitorInhibitConnected
+ _objc_msgSend$_waitForStartupActivated
+ _objc_msgSend$_waitForStartupActivatedFailure:withResponseError:description:completion:
+ _objc_msgSend$_waitForStartupActivatedSuccess:
+ _objc_msgSend$_waitForStartupActivatedThen:
- GCC_except_table162
- GCC_except_table168
- GCC_except_table175
- GCC_except_table181
- GCC_except_table195
- GCC_except_table200
- GCC_except_table206
- GCC_except_table211
- GCC_except_table217
- GCC_except_table222
- GCC_except_table228
- GCC_except_table233
- GCC_except_table240
- GCC_except_table245
- GCC_except_table260
- GCC_except_table267
- GCC_except_table277
- GCC_except_table282
- GCC_except_table288
- GCC_except_table293
- GCC_except_table299
- GCC_except_table304
- ___101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke.988
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1221
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1222
- ___50-[MAPushNotificationController _serviceConnection]_block_invoke.1209
- ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1250
- ___65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.965
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1215
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1216
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1220
- ___Block_byref_object_copy_.1384
- ___Block_byref_object_copy_.765
- ___Block_byref_object_dispose_.1385
- ___Block_byref_object_dispose_.766
- ____MAPreferencesCopyValue_block_invoke.1510
- ____MAensureExtension_block_invoke.1391
- ____MAsendDownloadAsset_block_invoke.1295
- ____MAsendPMVCancelDownload_block_invoke.1313
- ____MAsendPMVDownload_block_invoke.1301
- ___block_literal_global.1024
- ___block_literal_global.1026
- ___block_literal_global.1028
- ___block_literal_global.1031
- ___block_literal_global.1204
- ___block_literal_global.1208
- ___block_literal_global.1212
- ___block_literal_global.1214
- ___block_literal_global.1215
- ___block_literal_global.1232
- ___block_literal_global.1253
- ___block_literal_global.1269
- ___block_literal_global.1274
- ___block_literal_global.1298
- ___block_literal_global.1491
- ___block_literal_global.1513
- ___block_literal_global.1516
- ___block_literal_global.1518
- ___block_literal_global.1523
- ___block_literal_global.1525
- ___block_literal_global.1527
- ___block_literal_global.1530
- ___block_literal_global.2929
- ___block_literal_global.2931
- ___block_literal_global.2933
- ___block_literal_global.2935
CStrings:
+ "0123456789.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-*"
+ "Download failed due to an error from the Streaming Extractor framework"
+ "DownloadManagerSyncDelaySecs"
+ "MA-AUTO-CONTROL:WAIT_FOR_STARTUP_ACTIVATED"
+ "MA-auto(client){_waitForStartupActivatedFailure} | %{public}@ | SUCCESS"
+ "MA-auto(client){_waitForStartupActivatedFailure} | %{public}@ | error:%{public}@"
+ "MA-auto{_waitForStartupActivatedFailure} | no client completion block | %{public}@"
+ "MA-auto{_waitForStartupActivatedSuccess} | SUCCESS"
+ "MA-auto{_waitForStartupActivatedSuccess} | no client completion block"
+ "MA-auto{waitForStartupActivated} | no client completion block | %{public}@"
+ "MAAuto:_waitForStartupActivatedThen"
+ "MADownloadSTExtractorError"
+ "SecureNetworkMonitorInhibitConnected"
+ "_waitForStartupActivated"
+ "_waitForStartupActivatedFailure:withResponseError:description:completion:"
+ "_waitForStartupActivatedSuccess:"
+ "_waitForStartupActivatedThen:"
+ "auto(waitForStartupActivated)"
+ "v48@0:8q16@24@32@?40"
+ "waitForStartupActivated"

```
