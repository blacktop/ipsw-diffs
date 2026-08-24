## uarpd

> `/usr/libexec/uarpd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__data`

```diff

-1587.0.27.0.0
-  __TEXT.__text: 0xaa678
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_stubs: 0xa560
-  __TEXT.__objc_methlist: 0x86a8
-  __TEXT.__objc_methname: 0xf20e
-  __TEXT.__objc_classname: 0x1cf6
-  __TEXT.__cstring: 0xaefc
-  __TEXT.__objc_methtype: 0x2a72
+1587.1.3.0.0
+  __TEXT.__text: 0xad1d0
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__objc_stubs: 0xa7e0
+  __TEXT.__objc_methlist: 0x8820
+  __TEXT.__objc_methname: 0xf586
+  __TEXT.__objc_classname: 0x1d20
+  __TEXT.__cstring: 0xb1df
+  __TEXT.__objc_methtype: 0x2ad1
   __TEXT.__const: 0x148
-  __TEXT.__oslogstring: 0x9052
-  __TEXT.__gcc_except_tab: 0x19c
-  __TEXT.__unwind_info: 0x2398
-  __DATA_CONST.__const: 0x11b0
-  __DATA_CONST.__cfstring: 0x5460
-  __DATA_CONST.__objc_classlist: 0x608
+  __TEXT.__gcc_except_tab: 0x1ec
+  __TEXT.__oslogstring: 0x96a9
+  __TEXT.__unwind_info: 0x2438
+  __DATA_CONST.__const: 0x1180
+  __DATA_CONST.__cfstring: 0x55e0
+  __DATA_CONST.__objc_classlist: 0x610
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x5f0
-  __DATA_CONST.__objc_intobj: 0x3d8
+  __DATA_CONST.__objc_superrefs: 0x5f8
+  __DATA_CONST.__objc_intobj: 0x408
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x478
-  __DATA_CONST.__got: 0x648
-  __DATA.__objc_const: 0x105e8
-  __DATA.__objc_selrefs: 0x3170
-  __DATA.__objc_ivar: 0xb30
-  __DATA.__objc_data: 0x3c50
+  __DATA_CONST.__auth_got: 0x4b0
+  __DATA_CONST.__got: 0x660
+  __DATA.__objc_const: 0x10910
+  __DATA.__objc_selrefs: 0x3228
+  __DATA.__objc_ivar: 0xb74
+  __DATA.__objc_data: 0x3ca0
   __DATA.__data: 0x548
   __DATA.__bss: 0x1178
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDiagnostics.framework/Versions/A/CoreDiagnostics

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 3961
-  Symbols:   209
-  CStrings:  4939
+  Functions: 4009
+  Symbols:   219
+  CStrings:  5022
 
Symbols:
+ _IOPMAssertionCreateWithName
+ _IOPMAssertionRelease
+ _NSURLIsExcludedFromBackupKey
+ _OBJC_CLASS_$_UARPEndpointPersonalityiCloud
+ _OBJC_EHTYPE_$_NSException
+ _dispatch_assert_queue$V2
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
+ _objc_begin_catch
+ _objc_end_catch
CStrings:
+ "%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@"
+ "%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@"
+ "%s: %@ tool mode active, will pretend to publish"
+ "%s: Could create personality for database entry %@"
+ "%s: Created network assertion for %@"
+ "%s: Endpoint %@ Setting PG/PN to %@-%@"
+ "%s: Failed to create network assertion for %@; error %d"
+ "%s: Failed to exclude datavault directory from backup with error %@"
+ "%s: Failed to release network assertion for %@; error %d"
+ "%s: Failed to write serial number TLV to MTIC at %@ with error: %@"
+ "%s: Host Endpoint not present for UUID %@; posting xpc event"
+ "%s: No network assertion to release for %@"
+ "%s: Previous network assertion created for %@"
+ "%s: Released network assertion for %@"
+ "%s: Releasing network assertion for %@"
+ "%s: Skipping serial number TLV injection for MTIC at %@ (protocolVersion: %@, serialNumber: %@)"
+ "%s: Successfully wrote serial number TLV to MTIC at %@"
+ "%s: Taking network assertion for %@"
+ "%s: Unable to create serial number TLV for MTIC at %@, skipping injection"
+ "%s: Unable to expand MTIC asset at %@, skipping serial number TLV injection"
+ "%s: Unable to init MTIC asset at %@, skipping serial number TLV injection"
+ "%s: Unable to process MTIC payloads at %@"
+ "%s: endpoint transport domain is nil, don't send xpc event"
+ "%s: endpoint uuid cannot be nil"
+ "%s: need tool mode method to publish %@ for endpointUUID = %@, uarpTransportDomain = %@"
+ "%s: no publisher; cannot post %@ for endpointUUID = %@, uarpTransportDomain = %@"
+ "%s: publish %@ for endpointUUID = %@, uarpTransportDomain = %@"
+ "%s: scanned %lu entries at %@; this folder may be growing faster than it can be pruned"
+ "%s: uncompressedLength (%u) exceeds decompressionBuffer size (%lu)"
+ "%s: we accept asset manager notifications endpoint %@"
+ "-[UARPAnalyticsManager analyticsManagerProcessMTIC:mticTag:protocolVersion:endpointConfiguration:]"
+ "-[UARPAnalyticsManager injectSerialNumberTLV:mticURL:mticTag:]"
+ "-[UARPEndpointAssetAvailabilityEventManager activateDaemonMode]"
+ "-[UARPEndpointAssetAvailabilityEventManager activateToolMode]"
+ "-[UARPEndpointAssetAvailabilityEventManager endpointAssetAvailable:]"
+ "-[UARPEndpointDatabaseEntry endpointPersonality]"
+ "-[UARPEndpointDatabaseEntry mobileAssetPersonality]"
+ "-[UARPEndpointLayer3 configureEndpointLayer2Tags]"
+ "-[UARPEndpointLayer3 directConfiguration]_block_invoke"
+ "-[UARPHostEndpoint networkAssertionCreate]"
+ "-[UARPHostEndpoint networkAssertionRelease]"
+ "@\"UARPEndpointAssetAvailabilityEventManager\""
+ "NetworkClientActive"
+ "Product Group"
+ "Product Number"
+ "ProductGroup"
+ "ProductNumber"
+ "Pruned Expired File at %@"
+ "Q24@0:8@16"
+ "T@\"NSString\",&,V_productGroup"
+ "T@\"NSString\",&,V_productNumber"
+ "T@\"NSString\",&,V_transportDomain"
+ "T@\"NSString\",C,V_productGroup"
+ "T@\"NSString\",C,V_productNumber"
+ "TransportDomain"
+ "UARP Endpoint Asset Availability Event: Add Subscriber: token = %llu descriptor = %@"
+ "UARP Endpoint Asset Availability Event: Received initial barrier"
+ "UARP Endpoint Asset Availability Event: Remove Subscriber: token = %llu"
+ "UARP Endpoint Asset Availability Event: action = %u token = %llu descriptor = %@"
+ "UARPEndpointAssetAvailabilityEventManager"
+ "Unable to create JSON for event %@ (file %@): %@"
+ "^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}C^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S^{uarpLayer2EndpointIDInfo}S^{uarpDownstreamEndpointObj}I^{uarpMemoryTracker}}"
+ "_endpointAssetEventManager"
+ "_kInternalQueueKey"
+ "_networkAssertionID"
+ "_networkAssertionName"
+ "_productGroup"
+ "_productNumber"
+ "_toolMode"
+ "_transportDomain"
+ "analyticsManagerProcessMTIC:mticTag:protocolVersion:endpointConfiguration:"
+ "arrayWithCapacity:"
+ "asyncProcessMTIC:hostEndpoint:"
+ "clearMatchingLayer2Context:"
+ "com.apple.uarp.endpoint.assetavailable"
+ "com.apple.uarp.endpoint.assetavailable.subscriber"
+ "com.apple.uarp.uarpd.networkassertion"
+ "commonProcessMTIC:hostEndpoint:"
+ "configureEndpointLayer2Tags"
+ "deleteURL:"
+ "endpointAssetAvailable:"
+ "endpointPersonality"
+ "generateNetworkAssertionName"
+ "generatePowerAssertionName"
+ "initWithProductGroup:productNumber:domain:"
+ "injectSerialNumberTLV:mticURL:mticTag:"
+ "layer2CallbackRequestAssetBuffer:"
+ "layer2CallbackReturnAssetBuffer:"
+ "main"
+ "metrics"
+ "mobileAssetPersonality"
+ "networkAssertionCreate"
+ "networkAssertionRelease"
+ "pgpnPersonality"
+ "productGroup"
+ "productNumber"
+ "publishEndpointAssetAvailableEvent:"
+ "r^v"
+ "reason"
+ "setProductGroup:"
+ "setProductNumber:"
+ "setResourceValue:forKey:error:"
+ "setTransportDomain:"
+ "skipDescendants"
+ "transportDomain"
+ "uarpTransportDomain"
+ "{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestAssetBuffer\"^?\"fReturnAssetBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fMonotonicClockTime\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDiscoveredEndpointID\"^?\"fDiscoveredComponent\"^?\"fBulkInfoQuery\"^?\"fBulkInfoResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable3\"^?\"fDownstreamUnreachable2\"^?\"fDownstreamReleased2\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?\"fDownstreamReachable\"^?\"fDownstreamReachable2\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?}"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xb31"
- "\v"
- "%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@"
- "%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@-%@"
- "%s: All ripe files pruned at %@"
- "%s: Could create mobile asset personality for database entry %@"
- "%s: Hit max prunings at %@"
- "%s: Host Endpoint not present for UUID %@"
- "%s: Need to add support for non-Apple Model Number endpoints"
- "%s: we do accept asset manager notifications endpoint %@"
- "-[UARPAnalyticsManager analyticsManagerProcessMTIC:mticTag:]"
- "-[UARPEndpointLayer3 directConfiguration]"
- "-[UARPHostEndpoint personalityForDatabaseEntry:]"
- "File %@ is not old enough to prune; last modified date %@"
- "Pruned Expired File at %@; last modified date %@"
- "Q32@0:8@16@24"
- "^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}C^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S^{uarpLayer2EndpointIDInfo}S^{uarpDownstreamEndpointObj}I^{uarpMemoryTracker}}"
- "analyticsManagerProcessMTIC:mticTag:"
- "asyncProcessMTIC:"
- "personalityForDatabaseEntry:"
- "powerAssertionName:"
- "processURL:pruneBaseTime:"
- "q24@?0@\"NSURL\"8@\"NSURL\"16"
- "sortedArrayUsingComparator:"
- "{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fMonotonicClockTime\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDiscoveredEndpointID\"^?\"fDiscoveredComponent\"^?\"fBulkInfoQuery\"^?\"fBulkInfoResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable3\"^?\"fDownstreamUnreachable2\"^?\"fDownstreamReleased2\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?\"fDownstreamReachable\"^?\"fDownstreamReachable2\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?}"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x831"
```
