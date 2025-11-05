## libAce3Updater.dylib

> `/usr/lib/updaters/libAce3Updater.dylib`

```diff

-1170.80.6.0.1
-  __TEXT.__text: 0x1ce2c
-  __TEXT.__auth_stubs: 0x760
+1207.100.66.0.0
+  __TEXT.__text: 0x1dd60
+  __TEXT.__auth_stubs: 0x780
   __TEXT.__objc_methlist: 0x384
-  __TEXT.__cstring: 0x4ad0
-  __TEXT.__const: 0x158
+  __TEXT.__cstring: 0x54c2
+  __TEXT.__const: 0x240
   __TEXT.__oslogstring: 0x7
-  __TEXT.__unwind_info: 0x708
+  __TEXT.__unwind_info: 0x758
   __TEXT.__objc_classname: 0x84
   __TEXT.__objc_methname: 0x9f0
-  __TEXT.__objc_methtype: 0x7a0
+  __TEXT.__objc_methtype: 0x7d4
   __TEXT.__objc_stubs: 0x960
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x460

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x298
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH_CONST.__auth_got: 0x3c8
   __AUTH_CONST.__const: 0x30
   __AUTH_CONST.__cfstring: 0xe60
   __AUTH_CONST.__objc_const: 0x918

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FB4E311B-7C91-3BF4-925A-9A7D8443F53A
-  Functions: 866
-  Symbols:   1201
-  CStrings:  864
+  UUID: 77CFE4DF-523E-3B79-889C-9C19628C4B26
+  Functions: 903
+  Symbols:   1251
+  CStrings:  913
 
Symbols:
+ USBCUpdateQueryLogicalUnitNumber.cold.1
+ USBCUpdateQueryLogicalUnitNumber.cold.2
+ USBCUpdateQueryLogicalUnitNumber.cold.3
+ USBCUpdateQueryLogicalUnitNumber.cold.4
+ USBCUpdateQueryLogicalUnitNumber.cold.5
+ _CoreUARPRestoreEndpointRemoteEndpointAssetSolicitation
+ _CoreUARPRestoreSetAssetSolicitationCallbacks
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _UarpRestoreAssetSolicitation
+ _UarpRestoreAssetSolicitationHandler
+ _UarpRestoreLayer3AssetSolicitationProgress
+ _UarpRestoreLayer3AssetSolicitationStatus
+ _UarpRestoreLayer3AssetSolicitationStatusQueueHandler
+ _UarpRestoreLayer3LogTokenForCategory
+ __MergedGlobals
+ _fAssetStore
+ _remove
+ _sprintf
+ fAssetAllHeadersAndMetaDataComplete.cold.1
+ flash.cold.1
- _lun_to_rid_lookup
- _num_updatable_aces
CStrings:
+ "%s.%u.payload"
+ "%s: NULL fSolicitProgress"
+ "CoreUARPRestoreEndpointRemoteEndpointAssetSolicitation"
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
+ "UarpRestoreAssetSolicitation"
+ "UarpRestoreAssetSolicitationHandler"
+ "UarpRestoreLayer3AssetSolicitationProgress"
+ "UarpRestoreLayer3AssetSolicitationStatusQueueHandler"
+ "^{_uarpRestoreEndpoint={uarpRestoreLayer3Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}{uarpPlatformOptionsObj=IIISCSSSiSSC}{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S}{uarpPlatformEndpointApple=CCCC{uarpPlatformEndpointAppleCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}}{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^vSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}S^^{uarpPlatformTransmitBufferEntry}S^^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}}^{_uarpRestoreAsset}^{_uarpRestoreAsset}^vCS****{UARPVersion=IIII}{UARPVersion=IIII}@@****(?=IQ)IIQ*IIIIICCCCI*CIIII^vI*ICCC*I}"
+ "^{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}16@0:8"
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
+ "v28@0:8I16^{_UARPSiliconContext=@^v^v{uarpRestoreCallbacks=^?^?}^{_uarpRestoreEndpoint}^v^v{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}I****{UARP4ccTag=CCCC}**Q^v}20"
+ "v48@0:8@16@24^v32^{_UARPSiliconContext=@^v^v{uarpRestoreCallbacks=^?^?}^{_uarpRestoreEndpoint}^v^v{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}I****{UARP4ccTag=CCCC}**Q^v}40"
- "UARP Restore: %s: pEndpoint is NULL"
- "UARP Restore: Failed to deny unknown dynamic asset; 0x%08x"
- "^{_uarpRestoreEndpoint={uarpRestoreLayer3Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?}{uarpPlatformOptionsObj=IIISCSSSiSSC}{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S}{uarpPlatformEndpointApple=CCCC{uarpPlatformEndpointAppleCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}}{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^vSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}S^^{uarpPlatformTransmitBufferEntry}S^^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}}^{_uarpRestoreAsset}^{_uarpRestoreAsset}^vCS****{UARPVersion=IIII}{UARPVersion=IIII}@@****(?=IQ)IIQ*IIIIICCCCI*CIIII^vI*ICCC*I}"
- "^{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}16@0:8"
- "v28@0:8I16^{_UARPSiliconContext=@^v^v{uarpRestoreCallbacks=^?^?}^{_uarpRestoreEndpoint}^v^v{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}I*****Q^v}20"
- "v48@0:8@16@24^v32^{_UARPSiliconContext=@^v^v{uarpRestoreCallbacks=^?^?}^{_uarpRestoreEndpoint}^v^v{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}I*****Q^v}40"

```
