## libAce3Updater.dylib

> `/usr/lib/updaters/libAce3Updater.dylib`

```diff

-1170.80.6.0.1
-  __TEXT.__text: 0x1cad8
-  __TEXT.__auth_stubs: 0x880
+1207.100.54.502.1
+  __TEXT.__text: 0x1d920
+  __TEXT.__auth_stubs: 0x8a0
   __TEXT.__objc_methlist: 0x384
-  __TEXT.__cstring: 0x4af0
-  __TEXT.__const: 0x158
+  __TEXT.__cstring: 0x54e2
+  __TEXT.__const: 0x240
   __TEXT.__oslogstring: 0x7
-  __TEXT.__unwind_info: 0x710
+  __TEXT.__unwind_info: 0x760
   __TEXT.__objc_classname: 0x84
   __TEXT.__objc_methname: 0x9f0
-  __TEXT.__objc_methtype: 0x7a0
+  __TEXT.__objc_methtype: 0x7d4
   __TEXT.__objc_stubs: 0x960
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x488

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x298
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__auth_got: 0x458
   __AUTH_CONST.__cfstring: 0xe60
   __AUTH_CONST.__objc_const: 0x918
   __AUTH.__objc_data: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 864
-  Symbols:   1052
-  CStrings:  752
+  Functions: 901
+  Symbols:   1103
+  CStrings:  801
 
Symbols:
+ _CoreUARPRestoreEndpointRemoteEndpointAssetSolicitation
+ _CoreUARPRestoreSetAssetSolicitationCallbacks
+ _UarpRestoreAssetSolicitation
+ _remove
+ _sprintf
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
