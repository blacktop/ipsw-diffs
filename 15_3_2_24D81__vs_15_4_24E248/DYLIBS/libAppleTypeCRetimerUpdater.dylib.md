## libAppleTypeCRetimerUpdater.dylib

> `/usr/lib/updaters/libAppleTypeCRetimerUpdater.dylib`

```diff

-1170.80.6.0.1
-  __TEXT.__text: 0x42250
-  __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x4000
-  __TEXT.__cstring: 0x66e1
-  __TEXT.__const: 0x570
+1207.100.66.0.0
+  __TEXT.__text: 0x43358
+  __TEXT.__auth_stubs: 0x9b0
+  __TEXT.__objc_methlist: 0x4114
+  __TEXT.__cstring: 0x714a
+  __TEXT.__const: 0x5b0
   __TEXT.__gcc_except_tab: 0x138
   __TEXT.__oslogstring: 0x1492
-  __TEXT.__unwind_info: 0x14b8
+  __TEXT.__unwind_info: 0x1520
   __TEXT.__objc_classname: 0x1ab8
   __TEXT.__objc_methname: 0x4f48
-  __TEXT.__objc_methtype: 0x12c8
+  __TEXT.__objc_methtype: 0x12e9
   __TEXT.__objc_stubs: 0x4000
   __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0x1610
+  __DATA_CONST.__const: 0x1660
   __DATA_CONST.__objc_classlist: 0x3b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1448
   __DATA_CONST.__objc_superrefs: 0x370
-  __AUTH_CONST.__auth_got: 0x4d0
-  __AUTH_CONST.__const: 0x510
-  __AUTH_CONST.__cfstring: 0x5820
-  __AUTH_CONST.__objc_const: 0x8f78
+  __AUTH_CONST.__auth_got: 0x4e8
+  __AUTH_CONST.__const: 0x530
+  __AUTH_CONST.__cfstring: 0x5960
+  __AUTH_CONST.__objc_const: 0x8dd0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x2530
   __DATA.__objc_ivar: 0x624

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 556FD1F5-B6D0-3185-9C10-C1A77842FDD3
-  Functions: 2159
-  Symbols:   4681
-  CStrings:  3352
+  UUID: 8CEFA828-3203-36A3-AFC0-40B683F63D94
+  Functions: 2183
+  Symbols:   4725
+  CStrings:  3422
 
Symbols:
+ +[UARPMetaDataTLV metaDataTable].cold.1
+ -[UARPAssetVersion compare:]
+ InternalStorageDirectoryPath.cold.1
+ TSSRequestLogToken.cold.1
+ UARPStringCmapDatabaseFilePath.cold.1
+ UARPStringCmapDirectoryPath.cold.1
+ UARPStringCrashAnalyticsDirectoryFilePath.cold.1
+ UARPStringDynamicAssetsFilepath.cold.1
+ UARPStringLogsDirectoryFilePath.cold.1
+ UARPStringPcapFilesFilepath.cold.1
+ UARPStringPifMetricsFilePath.cold.1
+ UARPStringSupplementalAssetsFilepath.cold.1
+ UARPStringSysdiagnoseDirectoryFilePath.cold.1
+ UARPStringTapToRadarFilePath.cold.1
+ UARPStringTempFilesFilepath.cold.1
+ UARPStringTmapDatabaseFilePath.cold.1
+ UARPStringTmapDirectoryPath.cold.1
+ _CoreUARPRestoreEndpointRemoteEndpointAssetSolicitation
+ _CoreUARPRestoreSetAssetSolicitationCallbacks
+ _UarpRestoreAssetSolicitation
+ _UarpRestoreAssetSolicitationHandler
+ _UarpRestoreLayer3AssetSolicitationProgress
+ _UarpRestoreLayer3AssetSolicitationStatus
+ _UarpRestoreLayer3AssetSolicitationStatusQueueHandler
+ _UarpRestoreLayer3LogTokenForCategory
+ __block_literal_global.1006
+ __block_literal_global.1011
+ __block_literal_global.753
+ __block_literal_global.755
+ __block_literal_global.757
+ __block_literal_global.908
+ __block_literal_global.910
+ __block_literal_global.915
+ __block_literal_global.920
+ __block_literal_global.925
+ __block_literal_global.996
+ __block_literal_global.998
+ _fAssetStore
+ _kUARPStringMetadataDevicePayloadOrderedIndex
+ _kUARPStringMetadataDeviceTlvFlashSectionLength
+ _kUARPStringMobileAssetAssetsKey
+ _kUARPStringMobileAssetDeploymentCountryListKey
+ _kUARPStringMobileAssetDeploymentDeploymentLimitKey
+ _kUARPStringMobileAssetDeploymentGoLiveDateKey
+ _kUARPStringMobileAssetDeploymentRampPeriodKey
+ _kUARPStringPersonalizationOptionUIDMode
+ _kUARPSupportedAccessoryKeyTransportIP
+ _kUARPSupportedAccessoryKeyTransportSerial
+ _remove
+ _sprintf
+ _strlen
- _OUTLINED_FUNCTION_6
- __block_literal_global.741
- __block_literal_global.743
- __block_literal_global.745
- __block_literal_global.878
- __block_literal_global.880
- __block_literal_global.885
- __block_literal_global.890
- __block_literal_global.895
- __block_literal_global.966
- __block_literal_global.968
- __block_literal_global.976
- __block_literal_global.981
CStrings:
+ "%s.%u.payload"
+ "%s: NULL fSolicitProgress"
+ "Assets"
+ "CoreUARPRestoreEndpointRemoteEndpointAssetSolicitation"
+ "Flash Section Length"
+ "IP"
+ "Payload Ordered Index"
+ "Serial"
+ "UARP Restore (Asset Solicitation): %s: %u bytes written"
+ "UARP Restore (Asset Solicitation): %s: Asset fully staged"
+ "UARP Restore (Asset Solicitation): %s: Get %u Bytes from offset %u"
+ "UARP Restore (Asset Solicitation): %s: No Asset Metadata"
+ "UARP Restore (Asset Solicitation): %s: No Payload Metadata"
+ "UARP Restore (Asset Solicitation): %s: Set %u Bytes from offset %u"
+ "UARP Restore (Asset Solicitation): %s: fAssetMetaDataTLV not implemented"
+ "UARP Restore (Asset Solicitation): %s: fAssetProcessingNotification2 not implemented"
+ "UARP Restore (Asset Solicitation): %s: fPayloadMetaDataTLV not implemented"
+ "UARP Restore (Asset Solicitation): %s: fseek failed"
+ "UARP Restore (Asset Solicitation): %s: pAsset is NULL"
+ "UARP Restore (Asset Solicitation): %s: pAsset->_fp is NULL"
+ "UARP Restore (Asset Solicitation): %s: pEndpoint is NULL"
+ "UARP Restore (Asset Solicitation): %s: pPayload->_fp is NULL"
+ "UARP Restore (Asset Solicitation): %s: remove failed"
+ "UARP Restore (Asset Solicitation): %s: uarpAssetQueryPayloadInfo failed with status: %u"
+ "UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointAssetQueryNumberOfPayloads failed with status: %u"
+ "UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointAssetRequestMetaData failed with status: %u"
+ "UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointAssetSetPayloadIndex failed with status: %u"
+ "UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointPayloadRequestData failed with status: %u"
+ "UARP Restore (Asset Solicitation): %s: uarpPlatformEndpointPayloadRequestMetaData failed with status: %u"
+ "UARP Restore Layer 3: Solicit Status; status <0x%04x>, reason <0x%04x>"
+ "UARP Restore: %s: Accepted dynamic asset"
+ "UARP Restore: %s: Provided filepath is greater than max filepath length %i"
+ "UARP Restore: %s: Rx pRestoreAsset was NULL"
+ "UARP Restore: %s: UARPRestoreAsset->_fp is NULL"
+ "UARP Restore: %s: fLayer3AssetSolicitationProgress is NULL"
+ "UARP Restore: %s: fLayer3AssetSolicitationStatus is NULL"
+ "UARP Restore: %s: uarpPlatformEndpointPrepareSolicitedDynamicAsset() failed; 0x%08x"
+ "UARP Restore: %s: uarpPlatformEndpointSolicitDynamicAsset() failed; 0x%08x"
+ "UID_MODE"
+ "UarpRestoreAssetSolicitation"
+ "UarpRestoreAssetSolicitationHandler"
+ "UarpRestoreLayer3AssetSolicitationProgress"
+ "UarpRestoreLayer3AssetSolicitationStatusQueueHandler"
+ "^{_UARPSiliconContext=@^v^v{uarpRestoreCallbacks=^?^?}^{_uarpRestoreEndpoint}^v^v{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}I****{UARP4ccTag=CCCC}**Q^v}"
+ "countryList"
+ "deploymentLimit"
+ "fAssetGetBytesAtOffset2"
+ "fAssetMetaDataComplete"
+ "fAssetMetaDataTLV"
+ "fAssetProcessingNotification2"
+ "fAssetReady"
+ "fAssetSetBytesAtOffset2"
+ "fAssetStore"
+ "fPayloadData"
+ "fPayloadDataComplete"
+ "fPayloadMetaDataComplete"
+ "fPayloadMetaDataTLV"
+ "fPayloadReady"
+ "fPayloadWriteToAsset"
+ "fRestoreUARPDynamicAssetOffered"
+ "goLiveDate"
+ "q24@0:8@16"
+ "rampPeriod"
- "UARP Restore: %s: pEndpoint is NULL"
- "UARP Restore: Failed to deny unknown dynamic asset; 0x%08x"
- "^{_UARPSiliconContext=@^v^v{uarpRestoreCallbacks=^?^?}^{_uarpRestoreEndpoint}^v^v{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}I*****Q^v}"

```
