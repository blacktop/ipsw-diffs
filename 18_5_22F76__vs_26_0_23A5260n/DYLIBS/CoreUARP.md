## CoreUARP

> `/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP`

```diff

-1207.120.19.0.0
-  __TEXT.__text: 0x868f0
-  __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x899c
-  __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x719d
-  __TEXT.__oslogstring: 0x6267
-  __TEXT.__gcc_except_tab: 0x804
+1338.0.21.0.2
+  __TEXT.__text: 0x8b154
+  __TEXT.__auth_stubs: 0xa20
+  __TEXT.__objc_methlist: 0x8b34
+  __TEXT.__const: 0x220
+  __TEXT.__cstring: 0x7c29
+  __TEXT.__oslogstring: 0x656f
+  __TEXT.__gcc_except_tab: 0x8b4
   __TEXT.__dlopen_cstrs: 0x10e
-  __TEXT.__unwind_info: 0x24d0
-  __TEXT.__objc_classname: 0x18c4
-  __TEXT.__objc_methname: 0xdc9d
-  __TEXT.__objc_methtype: 0x3a57
-  __TEXT.__objc_stubs: 0x9660
-  __DATA_CONST.__got: 0x748
-  __DATA_CONST.__const: 0x1e68
+  __TEXT.__unwind_info: 0x2588
+  __TEXT.__objc_classname: 0x18d0
+  __TEXT.__objc_methname: 0xe0af
+  __TEXT.__objc_methtype: 0x3f03
+  __TEXT.__objc_stubs: 0x9800
+  __DATA_CONST.__got: 0x758
+  __DATA_CONST.__const: 0x2098
   __DATA_CONST.__objc_classlist: 0x688
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3060
+  __DATA_CONST.__objc_selrefs: 0x3148
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x678
-  __AUTH_CONST.__auth_got: 0x500
+  __AUTH_CONST.__auth_got: 0x520
   __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x6f00
-  __AUTH_CONST.__objc_const: 0x11958
+  __AUTH_CONST.__cfstring: 0x7360
+  __AUTH_CONST.__objc_const: 0x11a88
   __AUTH_CONST.__objc_intobj: 0xca8
-  __AUTH.__objc_data: 0x2120
-  __DATA.__objc_ivar: 0xba4
+  __AUTH.__objc_data: 0x2080
+  __DATA.__objc_ivar: 0xbc4
   __DATA.__data: 0x40d
   __DATA.__bss: 0x1a5b
-  __DATA_DIRTY.__objc_data: 0x2030
+  __DATA_DIRTY.__objc_data: 0x20d0
   __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: E455D0A1-B3AD-310E-810C-BC0C92BE24EF
-  Functions: 3827
-  Symbols:   12266
-  CStrings:  5667
+  UUID: 792D0C57-DD30-3A6B-B26A-21DA10BB425D
+  Functions: 3906
+  Symbols:   12415
+  CStrings:  5849
 
Symbols:
+ +[UARPSupportedAccessoryA3421 appleModelNumber]
+ -[NSFileHandle(FTABWrite) ftabWriteData:error:]
+ -[TmapFieldTLV description]
+ -[TmapFieldTLV endianToString]
+ -[TmapFieldTLV expandString:inCoreAnalytics:].cold.2
+ -[TmapFieldTLV fieldTypeToString]
+ -[TmapFieldTLV fieldTypeToString].cold.1
+ -[TmapFieldTLV initWithDictionary:endian:].cold.6
+ -[TmapFieldTLV isFieldPrivacyRestricted]
+ -[UARPAccessoryHardwareHID doesMatchVendorID:productID:]
+ -[UARPAssetVersion isEqual:]
+ -[UARPAssetVersion isGreaterThan:]
+ -[UARPController queryCompleteForAccessory:nonceHash:error:]
+ -[UARPController queryCompleteForAccessory:nonceSeed:error:]
+ -[UARPController sendMessageToAccessory:uarpMsg:].cold.1
+ -[UARPDeploymentRule compareOSVersion:withVersion:]
+ -[UARPDeploymentRule initWithMinOSVersion:maxOSVersion:]
+ -[UARPDynamicAssetMappedAnalyticsEvent decomposeUARP].cold.1
+ -[UARPDynamicAssetMappedAnalyticsEvent initWithURL:serialNumber:]
+ -[UARPDynamicAssetTmapDatabase description]
+ -[UARPDynamicAssetTmapDatabase expandMticData:withEventID:appleModelNumber:serialNumber:]
+ -[UARPDynamicAssetTmapDatabase expandMticData:withEventID:appleModelNumber:serialNumber:].cold.1
+ -[UARPDynamicAssetTmapDatabase initTmapDatabaseWithPlist:]
+ -[UARPDynamicAssetTmapDatabase initTmapDatabaseWithPlist:].cold.1
+ -[UARPDynamicAssetTmapDatabase initWithUrl:]
+ -[UARPDynamicAssetTmapDatabase initWithUrl:].cold.1
+ -[UARPDynamicAssetTmapDatabase loadPlist]
+ -[UARPDynamicAssetTmapEvent description]
+ -[UARPDynamicAssetTmapMapping addSysdiagnoseMetrics:coreAnalyticsEvent:serialNumber:]
+ -[UARPDynamicAssetTmapMapping addSysdiagnoseMetrics:coreAnalyticsEvent:serialNumber:].cold.1
+ -[UARPDynamicAssetTmapMapping description]
+ -[UARPDynamicAssetTmapMapping expandMticData:withEventID:serialNumber:]
+ -[UARPDynamicAssetTmapMapping expandMticData:withEventID:serialNumber:].cold.1
+ -[UARPDynamicAssetTmapMapping expandMticData:withEventID:serialNumber:].cold.2
+ -[UARPSuperBinaryAsset copyWithZone:]
+ -[UARPSuperBinaryAsset initWithURL:assetTag:serialNumber:]
+ -[UARPSuperBinaryAsset serialNumber]
+ -[UARPSupportedAccessory assetTypeOverride]
+ -[UARPSupportedAccessory compare:]
+ -[UARPSupportedAccessory setAssetTypeOverride:]
+ -[UARPSupportedAccessory setSupportsPallas:]
+ -[UARPSupportedAccessory setSupportsSoftwareUpdateAssets:]
+ -[UARPSupportedAccessory supportsPallas]
+ -[UARPSupportedAccessory supportsSoftwareUpdateAssets]
+ -[UARPSupportedAccessoryA3421 .cxx_destruct]
+ -[UARPSupportedAccessoryA3421 init]
+ -[UARPSupportedAccessoryManager findByHardwareID:]
+ -[UARPSupportedAccessoryManager findByIdentifier:]
+ -[UARPUploaderEndpoint addTxFirmwareAsset:].cold.1
+ -[UARPUploaderEndpoint addTxFirmwareAsset:].cold.2
+ -[UARPUploaderEndpoint initDownstreamWithDirectEndpoint:endpointID:uploader:]
+ -[UARPUploaderEndpoint initWithUARPAccessory:endpointID:uploader:]
+ -[UARPUploaderEndpoint initWithUARPAccessory:endpointID:uploader:].cold.1
+ -[UARPUploaderUARP addUnprocessedDynamicAsset:withAssetTag:serialNumber:]
+ -[UARPUploaderUARP addUnprocessedDynamicAsset:withAssetTag:serialNumber:].cold.1
+ -[UARPUploaderUARP updateNonceHash:remoteEndpoint:]
+ -[UARPUploaderUARP updateNonceSeed:remoteEndpoint:]
+ GCC_except_table189
+ GCC_except_table192
+ GCC_except_table205
+ GCC_except_table209
+ GCC_except_table214
+ GCC_except_table221
+ GCC_except_table5
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_UARPSupportedAccessoryA3421
+ _OBJC_IVAR_$_TmapFieldTLV._fieldPrivacyRestricted
+ _OBJC_IVAR_$_UARPDeploymentRule._maxOSVersion
+ _OBJC_IVAR_$_UARPDeploymentRule._minOSVersion
+ _OBJC_IVAR_$_UARPDynamicAssetMappedAnalyticsEvent._serialNumber
+ _OBJC_IVAR_$_UARPDynamicAssetTmapDatabase._plistURL
+ _OBJC_IVAR_$_UARPSuperBinaryAsset._serialNumber
+ _OBJC_IVAR_$_UARPSupportedAccessory._assetTypeOverride
+ _OBJC_IVAR_$_UARPSupportedAccessory._supportsPallas
+ _OBJC_IVAR_$_UARPSupportedAccessory._supportsSoftwareUpdateAssets
+ _OBJC_IVAR_$_UARPSupportedAccessoryA3421.hwID
+ _OBJC_METACLASS_$_UARPSupportedAccessoryA3421
+ _OUTLINED_FUNCTION_11
+ _UARPLayer2EndpointBulkInformationQuery
+ _UARPLayer2EndpointBulkInformationResponse
+ _UARPLayer2EndpointIDComponents
+ _UARPLayer2EndpointIDs
+ _UARPLayer2MonotonicClockTime
+ _UARPPersonalizationTSSResponseLazyManifest
+ _UARPProtocolVersionRequiresDownstreamMessageACK
+ _UARPProtocolVersionResponseAdjustByProtocolVersion
+ __OBJC_$_CLASS_METHODS_UARPSupportedAccessoryA3421
+ __OBJC_$_INSTANCE_METHODS_UARPSupportedAccessoryA3421
+ __OBJC_$_INSTANCE_VARIABLES_UARPSupportedAccessoryA3421
+ __OBJC_CLASS_RO_$_UARPSupportedAccessoryA3421
+ __OBJC_METACLASS_RO_$_UARPSupportedAccessoryA3421
+ ___53-[UARPUploaderUARP recvDataFromAccessory:data:error:]_block_invoke.cold.2
+ ___54-[UARPUploaderUARP assetStagingComplete:asset:status:]_block_invoke
+ ___55-[UARPController queryCompleteForAccessory:ecid:error:]_block_invoke_2
+ ___56-[UARPController queryCompleteForAccessory:epoch:error:]_block_invoke_2
+ ___57-[UARPController queryCompleteForAccessory:chipID:error:]_block_invoke_2
+ ___58-[UARPController queryCompleteForAccessory:boardID:error:]_block_invoke_2
+ ___60-[UARPController queryCompleteForAccessory:liveNonce:error:]_block_invoke_2
+ ___60-[UARPController queryCompleteForAccessory:nonceHash:error:]_block_invoke
+ ___60-[UARPController queryCompleteForAccessory:nonceSeed:error:]_block_invoke
+ ___63-[UARPController queryCompleteForAccessory:chipRevision:error:]_block_invoke_2
+ ___63-[UARPController queryCompleteForAccessory:securityMode:error:]_block_invoke_2
+ ___65-[UARPController queryCompleteForAccessory:enableMixMatch:error:]_block_invoke_2
+ ___65-[UARPController queryCompleteForAccessory:manifestPrefix:error:]_block_invoke_2
+ ___65-[UARPController queryCompleteForAccessory:productionMode:error:]_block_invoke_2
+ ___65-[UARPController queryCompleteForAccessory:securityDomain:error:]_block_invoke_2
+ ___73-[UARPUploaderUARP addUnprocessedDynamicAsset:withAssetTag:serialNumber:]_block_invoke
+ ___UARPPersonalizationTSSResponseLazyManifest_block_invoke
+ ___block_descriptor_40_e8_32r_e25_v32?0"NSString"816^B24lr32l8
+ ___block_descriptor_58_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_66_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
+ ___block_literal_global.1008
+ ___block_literal_global.1010
+ ___block_literal_global.1018
+ ___block_literal_global.1023
+ ___block_literal_global.762
+ ___block_literal_global.764
+ ___block_literal_global.766
+ ___block_literal_global.920
+ ___block_literal_global.922
+ ___block_literal_global.927
+ ___block_literal_global.932
+ ___block_literal_global.937
+ _calloc
+ _clock_gettime
+ _fCoreUARPLayer3MonotonicClockTime
+ _fCoreUARPLayer3NonceHashResponse
+ _fCoreUARPLayer3NonceSeedResponse
+ _fUarpLayer3DownstreamReachable2
+ _fUarpLayer3DownstreamUnreachable2
+ _getpid
+ _getuid
+ _isRunningAsAccessoryUpdaterDaemonRoleAccount
+ _kUARPAssetLocationTypeMobileAssetServerAirPodsDeveloperSeed
+ _kUARPAssetLocationTypeMobileAssetServerAirPodsPublicSeed
+ _kUARPDaemonHID
+ _kUARPDaemonNotificationMatching
+ _kUARPDaemonPersonalization
+ _kUARPNotificationPersonalizationNeededBTLEServer
+ _kUARPNotificationPersonalizationNeededHID
+ _kUARPNotificationPersonalizationNeededInternal
+ _kUARPServiceBTLEPersonalizationNeededEventName
+ _kUARPServiceHIDPersonalizationNeededEventName
+ _kUARPServicePersonalization
+ _kUARPServicePersonalizationBTLEServer
+ _kUARPServicePersonalizationNeededQueue
+ _kUARPStringTMAPFieldPrivacyRestricted
+ _kUarpDaemonLoggingSubsystem
+ _objc_msgSend$addSysdiagnoseMetrics:coreAnalyticsEvent:serialNumber:
+ _objc_msgSend$addUnprocessedDynamicAsset:withAssetTag:serialNumber:
+ _objc_msgSend$compareOSVersion:withVersion:
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$directEndpoint
+ _objc_msgSend$endianToString
+ _objc_msgSend$expandMticData:withEventID:appleModelNumber:serialNumber:
+ _objc_msgSend$expandMticData:withEventID:serialNumber:
+ _objc_msgSend$fieldTypeToString
+ _objc_msgSend$ftabWriteData:error:
+ _objc_msgSend$initDownstreamWithDirectEndpoint:endpointID:uploader:
+ _objc_msgSend$initWithUARPAccessory:endpointID:uploader:
+ _objc_msgSend$initWithURL:assetTag:serialNumber:
+ _objc_msgSend$initWithURL:serialNumber:
+ _objc_msgSend$isFieldPrivacyRestricted
+ _objc_msgSend$isGreaterThan:
+ _objc_msgSend$operatingSystemVersion
+ _objc_msgSend$processInfo
+ _objc_msgSend$queryCompleteForAccessory:nonceHash:error:
+ _objc_msgSend$queryCompleteForAccessory:nonceSeed:error:
+ _objc_msgSend$updateNonceHash:remoteEndpoint:
+ _objc_msgSend$updateNonceSeed:remoteEndpoint:
+ _uarpAllocateTransmitBuffers
+ _uarpMessageAdjustedForEndpointID
+ _uarpMessagePrintToBuffer
+ _uarpMessageTypeToString
+ _uarpMsgRecvDownstreamEndpointMessageSendAck
+ _uarpPlatformAssetFindFirmware
+ _uarpPlatformCleanupAssets
+ _uarpPlatformConfigureEndpointIDs
+ _uarpPlatformConfigureEndpointTags
+ _uarpPlatformDelegateForDownstreamID
+ _uarpPlatformDownstreamEndpointAddToList
+ _uarpPlatformDownstreamEndpointDelegateFindOnListByID
+ _uarpPlatformDownstreamEndpointFindOnList
+ _uarpPlatformDownstreamEndpointFindOnListByDelegate
+ _uarpPlatformDownstreamEndpointIDFindOnListByDelegate
+ _uarpPlatformDownstreamEndpointReachable
+ _uarpPlatformDownstreamEndpointRemoveFromList
+ _uarpPlatformDownstreamEndpointUnreachable
+ _uarpPlatformEndpointBulkInfoQuery
+ _uarpPlatformEndpointBulkInfoResponse
+ _uarpPlatformEndpointBulkInfoResponseAddTLV
+ _uarpPlatformEndpointDeinit
+ _uarpPlatformEndpointDiscoverEndpointIDs
+ _uarpPlatformGetSupportsBulkInfoQueries
+ _uarpPlatformGetUseHostPushModel
+ _uarpPlatformQueryEndpointComponentDiscovery
+ _uarpPlatformReleaseEndpointIDs
+ _uarpPlatformReleaseEndpointTags
+ _uarpPlatformSendDownstreamMessageWithDownstreamID
+ _uarpPlatformSendMessageFromDownstreamEndpointID
+ _uarpPlatformSendMessageToDownstreamEndpointID
+ _uarpRemoteEndpointForAsset
+ _uarpTransmitMessageToDownstreamEndpointID
+ _uarpTransmitQueuePurge
+ _uarpTransmitQueueReclaimEntries
- -[UARPController pendingTatsuRequests].cold.2
- -[UARPDynamicAssetCrashLogEvent setAppleModelNumber:]
- -[UARPDynamicAssetPersonalization processDynamicAsset:].cold.2
- -[UARPDynamicAssetPersonalization processDynamicAsset:].cold.3
- -[UARPDynamicAssetTmapDatabase expandMticData:withEventID:appleModelNumber:].cold.1
- -[UARPDynamicAssetTmapMapping addSysdiagnoseMetrics:coreAnalyticsEvent:]
- -[UARPDynamicAssetTmapMapping addSysdiagnoseMetrics:coreAnalyticsEvent:].cold.1
- -[UARPDynamicAssetTmapMapping expandMticData:withEventID:].cold.1
- -[UARPDynamicAssetTmapMapping expandMticData:withEventID:].cold.2
- -[UARPPersonalizationManager getOutstandingPersonalizationRequests:reply:].cold.2
- -[UARPSuperBinaryPlist .cxx_destruct]
- -[UARPSuperBinaryPlist initWithPlist:]
- -[UARPSuperBinaryPlist mergePlist:]
- -[UARPSuperBinaryPlist writeToURL:]
- -[UARPUploaderEndpoint handlePersonalizationResponse:].cold.3
- -[UARPUploaderEndpoint handlePersonalizationResponse:].cold.4
- -[UARPUploaderEndpoint handlePersonalizationResponse:].cold.5
- -[UARPUploaderEndpoint handlePersonalizationResponse:].cold.6
- -[UARPUploaderEndpoint im4mAssetReceived:].cold.4
- -[UARPUploaderEndpoint initDownstreamWithDirectEndpoint:layer2Context:uploader:]
- -[UARPUploaderEndpoint initWithUARPAccessory:layer2Context:uploader:]
- -[UARPUploaderEndpoint initWithUARPAccessory:uploader:].cold.1
- -[UARPUploaderEndpoint pendingTssRequests].cold.1
- -[UARPUploaderUARP tssResponseForEndpoint:tssResponse:].cold.1
- -[UARPUploaderUARP tssResponseForEndpoint:tssResponse:].cold.2
- -[UARPUploaderUARP tssResponseForEndpoint:tssResponse:].cold.3
- GCC_except_table174
- GCC_except_table177
- GCC_except_table184
- GCC_except_table190
- GCC_except_table194
- GCC_except_table206
- _OBJC_CLASS_$_UARPSuperBinaryPlist
- _OBJC_IVAR_$_TmapFieldTLV._expansionFunction
- _OBJC_IVAR_$_UARPSuperBinaryPlist._sbDict
- _OBJC_METACLASS_$_UARPSuperBinaryPlist
- _UARPAssetSolicitionComplete.cold.6
- _UARPPersonalizationTSSRequestWithSigningServer.cold.3
- _UARPPersonalizationTSSRequestWithSigningServerSSO.cold.2
- _UARPPlatformControllerAssetSetupCallbacksInbound
- __OBJC_$_INSTANCE_METHODS_UARPSuperBinaryPlist
- __OBJC_$_INSTANCE_VARIABLES_UARPSuperBinaryPlist
- __OBJC_CLASS_RO_$_UARPSuperBinaryPlist
- __OBJC_METACLASS_RO_$_UARPSuperBinaryPlist
- ___32-[UARPUploaderUARP tssResponse:]_block_invoke.cold.1
- ___32-[UARPUploaderUARP tssResponse:]_block_invoke.cold.2
- ___60-[UARPUploaderUARP addUnprocessedDynamicAsset:withAssetTag:]_block_invoke
- ___73-[UARPUploaderUARP offerDynamicAssetToAccessory:asset:internalOffer:tag:]_block_invoke.cold.1
- ___block_descriptor_72_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_literal_global.1001
- ___block_literal_global.1009
- ___block_literal_global.1014
- ___block_literal_global.756
- ___block_literal_global.758
- ___block_literal_global.760
- ___block_literal_global.911
- ___block_literal_global.913
- ___block_literal_global.918
- ___block_literal_global.923
- ___block_literal_global.928
- ___block_literal_global.999
- _fUarpLayer3DownstreamReachable
- _fUarpLayer3DownstreamRecvMessage
- _fUarpLayer3DownstreamUnreachable
- _objc_msgSend$addSysdiagnoseMetrics:coreAnalyticsEvent:
- _objc_msgSend$addUnprocessedDynamicAsset:withAssetTag:
- _objc_msgSend$byteString
- _objc_msgSend$expandMticData:withEventID:
- _objc_msgSend$expandMticData:withEventID:appleModelNumber:
- _objc_msgSend$initDownstreamWithDirectEndpoint:layer2Context:uploader:
- _objc_msgSend$initWithUARPAccessory:layer2Context:uploader:
- _objc_msgSend$initWithURL:assetTag:
- _objc_msgSend$values
- _uarpAssetQueueSolicitation
- _uarpAvailableTransmitBuffer
- _uarpPlatformAssetApproveOfferVersion
- _uarpPlatformEndpointIsMessageTypePending
- _uarpPlatformTransmitQueueLogEntry
- _uarpTransmitQueuePendingEntryComplete
- _uarpTransmitQueueProcessRecv
CStrings:
+ "\tBoot Nonce: "
+ "    Compression Header: "
+ " Algorithm <%u>, Actual Offset <%u>, Compressed Length <%u>, Uncompressed Length <%u> "
+ "%ld.%ld.%ld"
+ "%s: <ROLE=%s> : Add Downstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>"
+ "%s: <ROLE=%s> : RemoveDownstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>"
+ "%s: Do NOT offer NIL firmware to %@"
+ "%s: Do not offer firmware (active == asset) %@ to %@"
+ "%s: Do not offer firmware (active > asset) %@ to %@"
+ "%s: Do not offer firmware (staged == asset) %@ to %@"
+ "%s: Do not offer firmware (staged > asset) %@ to %@"
+ "%s: ESPRESSO Corrupt Entry ? pBuffer = %p, pMsg = %p"
+ "%s: ESPRESSO: Being asked to send ZERO length buffer to accessory"
+ "%s: ESPRESSO: ZERO Length Message from Transport"
+ "%s: ESPRESSO:Bonus Message <type=0x%04x, length=x0x%04x, id=0x%04x>"
+ "%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>"
+ "%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too small ! expected <%u>, got <%u>"
+ "%s: Wait until Protocol Version to [Re-]Offer firmware to %@"
+ "%s: [Re-]Offer firmware %@ to %@ (staged %@)"
+ "-[UARPController sendMessageToAccessory:uarpMsg:]"
+ "<ROLE=%s> ESPRESSO: UARP.LAYER2.RECV.MSG: Length too small <%u>"
+ "<ROLE=%s> UARP.LAYER2.DATA.RESP offset=0x%08x, requestedlength=%u"
+ "@44@0:8@16I24@28@36"
+ "A3421"
+ "A3502"
+ "A3503"
+ "Add Tx Firmware Asset %@"
+ "Agnes PRQ1"
+ "AirPodsDeveloperSeed"
+ "AirPodsPublicSeed"
+ "Apple Model Number %@\n"
+ "Apply Staged Assets Request"
+ "Apply Staged Assets Response"
+ "Asset Available Notification"
+ "Asset Available Notification Ack"
+ "Asset Data Transfer Notification"
+ "Asset Data Transfer Notification Ack"
+ "Asset Processing Notification"
+ "Asset Processing Notification Ack"
+ "Asset Rescinded Notification"
+ "Asset Rescinded Notification Ack"
+ "B24@0:8S16S20"
+ "B44@0:8@16@24S32^@36"
+ "Buffer Overflow"
+ "Buffer Would Overflow"
+ "Data Request"
+ "Data Response"
+ "Downstream Endpoint Discovery"
+ "Downstream Endpoint Discovery Ack"
+ "Downstream Endpoint Message"
+ "Downstream Endpoint Message Ack"
+ "Downstream Endpoint Reachable"
+ "Downstream Endpoint Reachable Ack"
+ "Downstream Endpoint Unreachable"
+ "Downstream Endpoint Unreachable Ack"
+ "Dynamic Asset PreProcessing Notification"
+ "Dynamic Asset PreProcessing Notification Ack"
+ "Dynamic Asset Solicitation"
+ "Dynamic Asset Solicitation Ack"
+ "ERROR: <<< MULTIPLE FW ASSETS >>>"
+ "ERROR: >>> MULTIPLE FW ASSETS <<<"
+ "Endpoint Bulk Information Request"
+ "Endpoint Bulk Information Request Ack"
+ "Endpoint Bulk Information Response"
+ "Endpoint Bulk Information Response Ack"
+ "Endpoint Component Discovery Request"
+ "Endpoint Component Discovery Response"
+ "Endpoint Discovery Request"
+ "Endpoint Discovery Response"
+ "Event Field Endian %@ \n"
+ "Event Field Length %lu\n"
+ "Event Field Name %@\n"
+ "Event Field Type %@ \n"
+ "Event ID %u\n"
+ "Event Name %@\n"
+ "Failed to offering dynamic asset; accessory is %@ asset is %@. Status is %s"
+ "FieldPrivacyRestricted"
+ "Information Request"
+ "Information Response"
+ "Invalid EndpointID"
+ "LuckSeed"
+ "MTIC Event String is unable to be decoded."
+ "No Apple Model Number for TMAP Mapping"
+ "No Event Field Name"
+ "No Event Name"
+ "No Field Type"
+ "No Firmware Update Available"
+ "No Firmware Update Available Ack"
+ "No TMAP Database"
+ "No TMAP Database - cannot init"
+ "No TMAP Event TLVs"
+ "No TMAP Events"
+ "No serial number provided for dynamic asset: %@"
+ "Pending Tx Firmware Asset %@"
+ "Sync"
+ "T@\"NSData\",C,V_ecidData"
+ "T@\"NSData\",C,V_manifest"
+ "T@\"NSData\",C,V_payloadDigest"
+ "T@\"NSError\",C,V_installerProgressError"
+ "T@\"NSNumber\",C,V_demote"
+ "T@\"NSNumber\",C,V_digestListSize"
+ "T@\"NSNumber\",C,V_effectiveProductionMode"
+ "T@\"NSNumber\",C,V_effectiveSecurityMode"
+ "T@\"NSNumber\",C,V_installerOverallProgress"
+ "T@\"NSNumber\",C,V_isTrusted"
+ "T@\"NSNumber\",C,V_trustedOverride"
+ "T@\"NSString\",C,V_assetTypeOverride"
+ "T@\"NSString\",C,V_friendlyName"
+ "T@\"NSString\",C,V_hardwareVersion"
+ "T@\"NSString\",C,V_hwFusingType"
+ "T@\"NSString\",C,V_modelName"
+ "T@\"NSString\",C,V_serialNumber"
+ "T@\"UARPAssetVersion\",C,V_firmwareVersion"
+ "T@\"UARPAssetVersion\",C,V_stagedFirmwareVersion"
+ "TB,V_supportsPallas"
+ "TB,V_supportsSoftwareUpdateAssets"
+ "TMAP Event %@\n"
+ "TMAP Event TLV %@\n"
+ "TMAP Field Privacy Restricted must be Number (Boolean)."
+ "TMAP Mapping %@\n"
+ "T^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?IIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}},R,V_uarpAsset"
+ "T^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S^{uarpLayer2EndpointIDInfo}S^{uarpDownstreamEndpointObj}I^{uarpMemoryTracker}},R"
+ "T^{uarpPlatformEndpointApple=CCCC{uarpPlatformEndpointAppleCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}},R"
+ "T^{uarpPlatformOptionsObj=IIISCSSSiSSCSCC},R"
+ "T^{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^vSSSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}},R"
+ "UARP: TSS Request to default server"
+ "UARPSupportedAccessoryA3421"
+ "Vendor Specific"
+ "Version Discovery Request"
+ "Version Discovery Response"
+ "[pid=%d] %s"
+ "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?IIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}"
+ "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?IIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}16@0:8"
+ "^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S^{uarpLayer2EndpointIDInfo}S^{uarpDownstreamEndpointObj}I^{uarpMemoryTracker}}16@0:8"
+ "^{uarpPlatformEndpointApple=CCCC{uarpPlatformEndpointAppleCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}}16@0:8"
+ "^{uarpPlatformOptionsObj=IIISCSSSiSSCSCC}16@0:8"
+ "^{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^vSSSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}}16@0:8"
+ "_assetTypeOverride"
+ "_fieldPrivacyRestricted"
+ "_maxOSVersion"
+ "_minOSVersion"
+ "_plistURL"
+ "_supportsPallas"
+ "_supportsSoftwareUpdateAssets"
+ "addSysdiagnoseMetrics:coreAnalyticsEvent:serialNumber:"
+ "addUnprocessedDynamicAsset:withAssetTag:serialNumber:"
+ "assetTypeOverride"
+ "btlePersonalizationNeeded"
+ "com.apple.notifyd.matching"
+ "com.apple.uarp.daemon"
+ "com.apple.uarp.personalization-needed.dispatchqueue"
+ "com.apple.uarphidd"
+ "com.apple.uarppersonalization"
+ "com.apple.uarppersonalization.btleserver"
+ "com.apple.uarppersonalizationd"
+ "compareOSVersion:withVersion:"
+ "dictionaryWithContentsOfFile:"
+ "doesMatchVendorID:productID:"
+ "endianToString"
+ "expandMticData:withEventID:appleModelNumber:serialNumber:"
+ "expandMticData:withEventID:serialNumber:"
+ "fieldTypeToString"
+ "findByIdentifier:"
+ "ftabWriteData:error:"
+ "hidPersonalizationNeeded"
+ "initDownstreamWithDirectEndpoint:endpointID:uploader:"
+ "initTmapDatabaseWithPlist:"
+ "initWithMinOSVersion:maxOSVersion:"
+ "initWithUARPAccessory:endpointID:uploader:"
+ "initWithURL:assetTag:serialNumber:"
+ "initWithURL:serialNumber:"
+ "initWithUrl:"
+ "isFieldPrivacyRestricted"
+ "isGreaterThan:"
+ "loadPlist"
+ "maxOSVersion"
+ "minOSVersion"
+ "nonce hash"
+ "nonce seed"
+ "operatingSystemVersion"
+ "processInfo"
+ "q32@0:8@16@24"
+ "q36@0:8Q16@24S32"
+ "queryCompleteForAccessory:nonceHash:error:"
+ "queryCompleteForAccessory:nonceSeed:error:"
+ "setAssetTypeOverride:"
+ "setSupportsPallas:"
+ "setSupportsSoftwareUpdateAssets:"
+ "supportsPallas"
+ "supportsSoftwareUpdateAssets"
+ "uarpMessageAdjustedForEndpointID() failed; <%u> %s"
+ "uarpMsgRecvDownstreamEndpointReachable"
+ "uarpMsgRecvDownstreamEndpointUnreachable"
+ "uarpMsgRecvDownstreamEndpointUnreachableAck"
+ "uarpPlatformEndpointRecvMessage"
+ "uarpTransmitEntryIsValidToSend"
+ "updateNonceHash:remoteEndpoint:"
+ "updateNonceSeed:remoteEndpoint:"
+ "v24@0:8^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?IIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}16"
+ "yyyy-MM-dd-HH-mm-ss"
+ "{uarpPlatformEndpoint=\"_options\"{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C\"numPreallocatedBuffers\"S\"supportsBulkInfoQueries\"C\"useHostPushModel\"C}\"pVendorExtension\"^v\"protectedCallbacks\"{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fMonotonicClockTime\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDiscoveredEndpointID\"^?\"fDiscoveredComponent\"^?\"fBulkInfoQuery\"^?\"fBulkInfoResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable2\"^?\"fDownstreamUnreachable2\"^?\"fDownstreamReleased2\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?\"fDownstreamReachable\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?}\"pDelegate\"^v\"role\"i\"numRemoteEndpointSlots\"I\"pRemoteEPs\"^^{uarpPlatformRemoteEndpoint}\"pAssetList\"^{uarpPlatformAsset}\"nextTxAssetID\"i\"rxLock\"C\"nextRemoteEndpointID\"i\"fVendorSpecific\"^?\"numEndpointIDs\"S\"pEndpointIDInfo\"^{uarpLayer2EndpointIDInfo}\"nextDownstreamID\"S\"pDownstreamEndpoints\"^{uarpDownstreamEndpointObj}\"numMemoryTrackers\"I\"pMemoryTracker\"^{uarpMemoryTracker}}"
+ "{uarpPlatformEndpointApple=\"supportsPersonalization\"C\"supportsHeySiri\"C\"supportsJustSiri\"C\"supportsVoiceAssist\"C\"callbacks\"{uarpPlatformEndpointAppleCallbacks=\"fAppleModelNumber\"^?\"fAppleModelNumberResponse\"^?\"fHwFusingType\"^?\"fHwFusingTypeResponse\"^?\"fManifestPrefix\"^?\"fManifestPrefixResponse\"^?\"fBoardID\"^?\"fBoardIDResponse\"^?\"fChipID\"^?\"fChipIDResponse\"^?\"fChipRevision\"^?\"fChipRevisionResponse\"^?\"fECID\"^?\"fECIDResponse\"^?\"fECIDData\"^?\"fECIDDataResponse\"^?\"fSecurityDomain\"^?\"fSecurityDomainResponse\"^?\"fSecurityMode\"^?\"fSecurityModeResponse\"^?\"fProductionMode\"^?\"fProductionModeResponse\"^?\"fChipEpoch\"^?\"fChipEpochResponse\"^?\"fEnableMixMatch\"^?\"fEnableMixMatchResponse\"^?\"fSoCLiveNonce\"^?\"fSoCLiveNonceResponse\"^?\"fPrefixNeedsLogicalUnitNumber\"^?\"fPrefixNeedsLogicalUnitNumberResponse\"^?\"fSuffixNeedsLogicalUnitNumber\"^?\"fSuffixNeedsLogicalUnitNumberResponse\"^?\"fLogicalUnitNumber\"^?\"fLogicalUnitNumberResponse\"^?\"fTicketLongName\"^?\"fTicketLongNameResponse\"^?\"fRequiresPersonalization\"^?\"fRequiresPersonalizationResponse\"^?\"fApBoardID\"^?\"fApBoardIDResponse\"^?\"fApChipID\"^?\"fApChipIDResponse\"^?\"fApProductionMode\"^?\"fApProductionModeResponse\"^?\"fApSecurityMode\"^?\"fApSecurityModeResponse\"^?\"fHardwareSpecific\"^?\"fHardwareSpecificResponse\"^?\"fNonce\"^?\"fNonceResponse\"^?\"fLife\"^?\"fLifeResponse\"^?\"fProvisioning\"^?\"fProvisioningResponse\"^?\"fManifestEpoch\"^?\"fManifestEpochResponse\"^?\"fManifestSuffix\"^?\"fManifestSuffixResponse\"^?\"fNonceSeed\"^?\"fNonceSeedResponse\"^?\"fNonceHash\"^?\"fNonceHashResponse\"^?\"fRealHdcpKeyPresent\"^?\"fRealHdcpKeyPresentResponse\"^?\"fFTABGeneration\"^?\"fFTABGenerationResponse\"^?}}"
+ "{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C\"numPreallocatedBuffers\"S\"supportsBulkInfoQueries\"C\"useHostPushModel\"C}"
+ "{uarpPlatformRemoteEndpoint=\"_options\"{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C\"numPreallocatedBuffers\"S\"supportsBulkInfoQueries\"C\"useHostPushModel\"C}\"pDelegate\"^v\"selectedProtocolVersion\"S\"supportsBulkInfoQueries\"S\"useHostPushModel\"S\"isWatchdogSet\"C\"_remoteEndpointID\"i\"dataTransferAllowed\"C\"dataTransferAllowedLocal\"C\"txMsgID\"S\"lastRxMsgID\"S\"uarpStats\"{UARPStatistics=\"packetsNoVersionAgreement\"I\"packetsMissed\"I\"packetsDuplicate\"I\"packetsOutOfOrder\"I}\"_solicitationQueue\"^{UARP4ccTag}\"pStreamingCtx\"^{uarpPlatformStreamingBuffer}\"pTxQueueAvailable\"^{uarpPlatformTransmitBufferEntry}\"pTxQueuePendingResponses\"^{uarpPlatformTransmitBufferEntry}\"downstreamID\"S\"activeFirmwareVersion\"{UARPVersion=\"major\"I\"minor\"I\"release\"I\"build\"I}\"stagedFirmwareVersion\"{UARPVersion=\"major\"I\"minor\"I\"release\"I\"build\"I}\"pUpstreamEP\"^{uarpPlatformRemoteEndpoint}}"
+ "\xf0\xf0\xc1"
- "\tBoot Nonce: %@\n"
- "    Algorithm <%u>, Actual Offset <%u>, Compressed Length <%u>, Uncompressed Length <%u>\n"
- "%s: Do not Offer firmware to %@"
- "%s: Zero Length Message from Transport"
- "%s: [Re-]Offer firmware %@ to %@"
- "</Compression Header>\n"
- "<Compression Header>\n"
- "<ROLE=%s> UARP.LAYER2.DATA.RESP Outstanding Data Request <%s>, offset=0x%08x, requestedlength=%u"
- "@40@0:8@16^v24@32"
- "@40@0:8@16^{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^vSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}S^^{uarpPlatformTransmitBufferEntry}S^^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}}24@32"
- "B48@0:8@16@24Q32^@40"
- "CrystalF"
- "Failed to offering dynamic asset; accessory is %@ asset is %@"
- "T@\"NSData\",&,V_ecidData"
- "T@\"NSData\",&,V_payloadDigest"
- "T@\"NSError\",&,V_installerProgressError"
- "T@\"NSNumber\",&,V_demote"
- "T@\"NSNumber\",&,V_digestListSize"
- "T@\"NSNumber\",&,V_effectiveProductionMode"
- "T@\"NSNumber\",&,V_effectiveSecurityMode"
- "T@\"NSNumber\",&,V_installerOverallProgress"
- "T@\"NSNumber\",&,V_isTrusted"
- "T@\"NSNumber\",&,V_trustedOverride"
- "T@\"NSString\",&,V_appleModelNumber"
- "T@\"NSString\",&,V_friendlyName"
- "T@\"NSString\",&,V_hardwareVersion"
- "T@\"NSString\",&,V_hwFusingType"
- "T@\"NSString\",&,V_manufacturerName"
- "T@\"NSString\",&,V_modelName"
- "T@\"NSString\",&,V_serialNumber"
- "T@\"UARPAssetVersion\",&,V_firmwareVersion"
- "T@\"UARPAssetVersion\",&,V_stagedFirmwareVersion"
- "T^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}},R,V_uarpAsset"
- "T^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S},R"
- "T^{uarpPlatformEndpointApple=CCCC{uarpPlatformEndpointAppleCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}},R"
- "T^{uarpPlatformOptionsObj=IIISCSSSiSSC},R"
- "T^{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^vSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}S^^{uarpPlatformTransmitBufferEntry}S^^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}},R"
- "UARPSuperBinaryPlist"
- "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}"
- "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}16@0:8"
- "^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S}16@0:8"
- "^{uarpPlatformEndpointApple=CCCC{uarpPlatformEndpointAppleCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}}16@0:8"
- "^{uarpPlatformOptionsObj=IIISCSSSiSSC}16@0:8"
- "^{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^vSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}S^^{uarpPlatformTransmitBufferEntry}S^^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}}"
- "^{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^vSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}S^^{uarpPlatformTransmitBufferEntry}S^^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}}16@0:8"
- "_expansionFunction"
- "_sbDict"
- "addSysdiagnoseMetrics:coreAnalyticsEvent:"
- "initDownstreamWithDirectEndpoint:layer2Context:uploader:"
- "initWithUARPAccessory:layer2Context:uploader:"
- "mergePlist:"
- "q40@0:8Q16@24Q32"
- "v24@0:8^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}16"
- "yyyy-MM-dd-hh-mm-ss"
- "{uarpPlatformEndpoint=\"_options\"{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C}\"pVendorExtension\"^v\"protectedCallbacks\"{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?}\"pDelegate\"^v\"role\"i\"numRemoteEndpointSlots\"I\"pRemoteEPs\"^^{uarpPlatformRemoteEndpoint}\"pAssetList\"^{uarpPlatformAsset}\"nextTxAssetID\"i\"rxLock\"C\"nextRemoteEndpointID\"i\"fVendorSpecific\"^?\"nextDownstreamID\"S}"
- "{uarpPlatformEndpointApple=\"supportsPersonalization\"C\"supportsHeySiri\"C\"supportsJustSiri\"C\"supportsVoiceAssist\"C\"callbacks\"{uarpPlatformEndpointAppleCallbacks=\"fAppleModelNumber\"^?\"fAppleModelNumberResponse\"^?\"fHwFusingType\"^?\"fHwFusingTypeResponse\"^?\"fManifestPrefix\"^?\"fManifestPrefixResponse\"^?\"fBoardID\"^?\"fBoardIDResponse\"^?\"fChipID\"^?\"fChipIDResponse\"^?\"fChipRevision\"^?\"fChipRevisionResponse\"^?\"fECID\"^?\"fECIDResponse\"^?\"fECIDData\"^?\"fECIDDataResponse\"^?\"fSecurityDomain\"^?\"fSecurityDomainResponse\"^?\"fSecurityMode\"^?\"fSecurityModeResponse\"^?\"fProductionMode\"^?\"fProductionModeResponse\"^?\"fChipEpoch\"^?\"fChipEpochResponse\"^?\"fEnableMixMatch\"^?\"fEnableMixMatchResponse\"^?\"fSoCLiveNonce\"^?\"fSoCLiveNonceResponse\"^?\"fPrefixNeedsLogicalUnitNumber\"^?\"fPrefixNeedsLogicalUnitNumberResponse\"^?\"fSuffixNeedsLogicalUnitNumber\"^?\"fSuffixNeedsLogicalUnitNumberResponse\"^?\"fLogicalUnitNumber\"^?\"fLogicalUnitNumberResponse\"^?\"fTicketLongName\"^?\"fTicketLongNameResponse\"^?\"fRequiresPersonalization\"^?\"fRequiresPersonalizationResponse\"^?\"fApBoardID\"^?\"fApBoardIDResponse\"^?\"fApChipID\"^?\"fApChipIDResponse\"^?\"fApProductionMode\"^?\"fApProductionModeResponse\"^?\"fApSecurityMode\"^?\"fApSecurityModeResponse\"^?\"fHardwareSpecific\"^?\"fHardwareSpecificResponse\"^?\"fNonce\"^?\"fNonceResponse\"^?\"fLife\"^?\"fLifeResponse\"^?\"fProvisioning\"^?\"fProvisioningResponse\"^?\"fManifestEpoch\"^?\"fManifestEpochResponse\"^?\"fManifestSuffix\"^?\"fManifestSuffixResponse\"^?}}"
- "{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C}"
- "\xf0q"

```
