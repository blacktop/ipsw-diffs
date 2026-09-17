## uarpd

> `/usr/libexec/uarpd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1587.1.3.0.0
-  __TEXT.__text: 0xaaed0
+1587.40.26.0.0
+  __TEXT.__text: 0xacbe4
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_stubs: 0xa7e0
-  __TEXT.__objc_methlist: 0x8820
-  __TEXT.__objc_methname: 0xf586
-  __TEXT.__objc_classname: 0x1d20
-  __TEXT.__cstring: 0xb215
-  __TEXT.__objc_methtype: 0x2ad1
+  __TEXT.__objc_stubs: 0xabc0
+  __TEXT.__objc_methlist: 0x8980
+  __TEXT.__objc_methname: 0xf964
+  __TEXT.__objc_classname: 0x1d25
+  __TEXT.__cstring: 0xb5df
+  __TEXT.__objc_methtype: 0x2b2b
   __TEXT.__const: 0x148
   __TEXT.__gcc_except_tab: 0x1ec
-  __TEXT.__oslogstring: 0x96a9
-  __TEXT.__unwind_info: 0x3280
-  __DATA_CONST.__const: 0x1180
-  __DATA_CONST.__cfstring: 0x5700
+  __TEXT.__oslogstring: 0x9936
+  __TEXT.__unwind_info: 0x3318
+  __DATA_CONST.__const: 0x11b0
+  __DATA_CONST.__cfstring: 0x5720
   __DATA_CONST.__objc_classlist: 0x610
-  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x4b0
-  __DATA_CONST.__got: 0x660
-  __DATA.__objc_const: 0x10910
-  __DATA.__objc_selrefs: 0x3228
-  __DATA.__objc_ivar: 0xb74
+  __DATA_CONST.__got: 0x668
+  __DATA.__objc_const: 0x109b8
+  __DATA.__objc_selrefs: 0x3320
+  __DATA.__objc_ivar: 0xb78
   __DATA.__objc_data: 0x3ca0
   __DATA.__data: 0x548
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 4009
-  Symbols:   219
-  CStrings:  5031
+  Functions: 4048
+  Symbols:   220
+  CStrings:  5099
 
Symbols:
+ _OBJC_CLASS_$_UARPHostEndpointProperties
CStrings:
+ "%s: Cancelling inactivity timer for %@"
+ "%s: Created power assertion for %@"
+ "%s: Do not offer asset %@ to %@; reported no firmware available"
+ "%s: EndpointUUID %@; available firmware %@ is greater than active firmware %@"
+ "%s: EndpointUUID %@; available firmware %@, not greater than active firmware %@"
+ "%s: Failed to create power assertion for %@; error %d"
+ "%s: Failed to release power assertion for %@; error %d"
+ "%s: No Firmware Asset for endpoint %@"
+ "%s: No available firmware for endpointUUID is %@"
+ "%s: No power assertion to release for %@"
+ "%s: Power assertion disabled for %@"
+ "%s: Previous power assertion created for %@"
+ "%s: Released power assertion for %@"
+ "%s: Releasing power assertion for %@"
+ "%s: Request to plumb transport for %@"
+ "%s: Taking power assertion for %@"
+ "%s: Transport set to staging only for %@; checking version before requesting to plumb transport"
+ "%s: endpointUUID is %@, transportForStagingOnly is not set"
+ "%s: inactivity timer expired for %@"
+ "%s: no firmware available"
+ "-[UARPEndpointLayer3 noFirmwareAvailable]_block_invoke"
+ "-[UARPEndpointLayer3 notifyEndpointRemoteNotResponding]"
+ "-[UARPHostEndpoint activityTimerExpireForSource:]"
+ "-[UARPHostEndpoint hostEndpointAvailable:endpointProperties:]"
+ "-[UARPHostEndpoint hostEndpointNoFirmwareUpdateAvailable]"
+ "-[UARPHostEndpoint hostEndpointTransportAvailable:]"
+ "-[UARPHostEndpoint hostEntryDeviceCheckAvailableFirmware]"
+ "-[UARPHostEndpoint hostEntryDeviceInactivityTimeout]_block_invoke"
+ "-[UARPHostEndpoint hostEntryDeviceNoFirmwareUpdateAvailable]_block_invoke"
+ "-[UARPHostEndpoint layer3EndpointPersonalizationNeeded:asset:]_block_invoke"
+ "-[UARPHostEndpoint layer3EndpointRemoteNotResponding:]"
+ "-[UARPHostEndpoint powerAssertionCreate]"
+ "-[UARPHostEndpoint powerAssertionRelease]"
+ "-[UARPHostManager(HostEndpointNotifications) hostEndpointInactive:]"
+ "-[UARPHostManager(HostEndpointNotifications) hostEndpointUnresponsive:]"
+ "-[UARPHostManagerService(UARPEndpointControllerDelegate) uarpHostManagerServiceEndpointInactive:]"
+ "-[UARPHostManagerService(UARPEndpointControllerDelegate) uarpHostManagerServiceEndpointUnresponsive:]"
+ "Endpoint %@: Remote Not Responding"
+ "PreventUserIdleSystemSleep"
+ "TB,R,V_blockFirmwareUpdate"
+ "UARP"
+ "^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}C^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S^{uarpLayer2EndpointIDInfo}S^{uarpDownstreamEndpointObj}I^{uarpMemoryTracker}}"
+ "_activityTimer"
+ "_blockFirmwareUpdate"
+ "activeFirmwareVersionInternal"
+ "activityTimerCancel"
+ "activityTimerCancelOnQueue"
+ "activityTimerExpireForSource:"
+ "activityTimerReset"
+ "blockFirmwareUpdate"
+ "endpointControllerDelegateEndpointInactive:"
+ "endpointControllerDelegateEndpointUnresponsive:"
+ "hostEndpointAvailable:endpointProperties:"
+ "hostEndpointDelegateInactivityTimeout:"
+ "hostEndpointDelegateNoFirmwareUpdateAvailable:"
+ "hostEndpointInactive:"
+ "hostEndpointNoFirmwareUpdateAvailable"
+ "hostEndpointTransportAvailable:"
+ "hostEndpointUnresponsive:"
+ "hostEntryDeviceCheckAvailableFirmware"
+ "hostEntryDeviceInactivityTimeout"
+ "hostEntryDeviceNoFirmwareUpdateAvailable"
+ "isMatchingUUID:"
+ "layer2CallbackRemoteNotResponding:length:"
+ "layer3EndpointRemoteNotResponding:"
+ "noFirmwareAvailable"
+ "noSleepWhileStaging"
+ "notifyEndpointRemoteNotResponding"
+ "numPacketRetries"
+ "setTransportForStagingOnly:"
+ "timeoutActivity"
+ "timeoutPacketRetry"
+ "transportForStagingOnly"
+ "uarpHostManagerServiceEndpointInactive:"
+ "uarpHostManagerServiceEndpointUnresponsive:"
+ "v28@0:8*16I24"
+ "v32@0:8@\"NSUUID\"16@\"UARPHostEndpointProperties\"24"
+ "{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestAssetBuffer\"^?\"fReturnAssetBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fRemoteNotResponding\"^?\"fMonotonicClockTime\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDiscoveredEndpointID\"^?\"fDiscoveredComponent\"^?\"fBulkInfoQuery\"^?\"fBulkInfoResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable3\"^?\"fDownstreamUnreachable2\"^?\"fDownstreamReleased2\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?\"fDownstreamReachable\"^?\"fDownstreamReachable2\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?}"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xc31"
- "%s: Request to plumb transport for %@, based on transport policy of %ld"
- "%s: Starting TapToRadar flow if upstream endpoint is in process for %@"
- "%s: Transport Release Policy is Immediate for %@; checking version before requesting to plumb transport"
- "%s: endpointUUID is %@, release transport immediately"
- "%s: endpointUUID is %@, transport release policy is %ld"
- "-[UARPHostEndpoint hostEndpointAvailable:releasePolicy:endpointProperties:]"
- "-[UARPHostEndpoint hostEndpointTransportAvailable:releasePolicy:]"
- "^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}C^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S^{uarpLayer2EndpointIDInfo}S^{uarpDownstreamEndpointObj}I^{uarpMemoryTracker}}"
- "_transportReleasePolicy"
- "{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestAssetBuffer\"^?\"fReturnAssetBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fMonotonicClockTime\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDiscoveredEndpointID\"^?\"fDiscoveredComponent\"^?\"fBulkInfoQuery\"^?\"fBulkInfoResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable3\"^?\"fDownstreamUnreachable2\"^?\"fDownstreamReleased2\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?\"fDownstreamReachable\"^?\"fDownstreamReachable2\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?}"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xb31"
```
