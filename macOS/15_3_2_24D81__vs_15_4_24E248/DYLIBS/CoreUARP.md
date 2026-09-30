## CoreUARP

> `/System/Library/PrivateFrameworks/CoreUARP.framework/Versions/A/CoreUARP`

```diff

-1170.80.6.0.1
-  __TEXT.__text: 0x8a81c
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x8178
-  __TEXT.__const: 0x220
-  __TEXT.__cstring: 0x6d8a
-  __TEXT.__oslogstring: 0x5bca
-  __TEXT.__gcc_except_tab: 0x840
+1207.100.66.0.0
+  __TEXT.__text: 0x8e7c8
+  __TEXT.__auth_stubs: 0x7e0
+  __TEXT.__objc_methlist: 0x8914
+  __TEXT.__const: 0x230
+  __TEXT.__cstring: 0x71db
+  __TEXT.__oslogstring: 0x61f5
+  __TEXT.__gcc_except_tab: 0x834
   __TEXT.__dlopen_cstrs: 0x10e
-  __TEXT.__unwind_info: 0x24a0
-  __TEXT.__objc_classname: 0x17fe
-  __TEXT.__objc_methname: 0xd757
-  __TEXT.__objc_methtype: 0x39b7
-  __TEXT.__objc_stubs: 0x9420
-  __DATA_CONST.__got: 0x718
-  __DATA_CONST.__const: 0x16d0
-  __DATA_CONST.__objc_classlist: 0x648
+  __TEXT.__unwind_info: 0x2560
+  __TEXT.__objc_classname: 0x18c4
+  __TEXT.__objc_methname: 0xdaf0
+  __TEXT.__objc_methtype: 0x3a45
+  __TEXT.__objc_stubs: 0x95a0
+  __DATA_CONST.__got: 0x740
+  __DATA_CONST.__const: 0x1730
+  __DATA_CONST.__objc_classlist: 0x688
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2eb0
+  __DATA_CONST.__objc_selrefs: 0x3010
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x638
-  __AUTH_CONST.__auth_got: 0x3a0
+  __DATA_CONST.__objc_superrefs: 0x678
+  __AUTH_CONST.__auth_got: 0x400
   __AUTH_CONST.__const: 0x9c0
-  __AUTH_CONST.__cfstring: 0x6d20
-  __AUTH_CONST.__objc_const: 0x11a30
-  __AUTH_CONST.__objc_intobj: 0xc60
-  __AUTH.__objc_data: 0x3ed0
-  __DATA.__objc_ivar: 0xb64
+  __AUTH_CONST.__cfstring: 0x6ee0
+  __AUTH_CONST.__objc_const: 0x11888
+  __AUTH_CONST.__objc_intobj: 0xc90
+  __AUTH.__objc_data: 0x4150
+  __DATA.__objc_ivar: 0xb94
   __DATA.__data: 0x40d
   __DATA.__bss: 0x1b2b
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: F0EDC73A-19FC-380E-A6CF-AEE142CB25BC
-  Functions: 3737
-  Symbols:   8166
-  CStrings:  5516
+  UUID: 6F3C5047-7053-31A7-9E41-64F3EBD29746
+  Functions: 3838
+  Symbols:   8380
+  CStrings:  5649
 
Symbols:
+ +[NSFileHandle(Availability) uarpCreateFileHandleForWritingToURL:error:]
+ +[UARPAccessory logger].cold.1
+ +[UARPMetaDataTLV metaDataTable].cold.1
+ +[UARPSandboxExtension readTokenStringWithURL:]
+ +[UARPSandboxExtension readTokenStringWithURL:].cold.1
+ +[UARPSupportedAccessory findByMobileAssetAppleModelNumber:]
+ +[UARPSupportedAccessoryA3299 appleModelNumber]
+ +[UARPSupportedAccessoryA3299 productID]
+ +[UARPSupportedAccessoryAirTag appleModelNumber]
+ +[UARPSupportedAccessoryAirTag productID]
+ +[UARPSupportedAccessoryAirTag vendorID]
+ +[UARPSupportedAccessoryIP appleModelNumber]
+ -[UARPAccessoryHardwareIPv4 description]
+ -[UARPAccessoryHardwareIPv4 init]
+ -[UARPAccessoryHardwareIPv4 isEqual:]
+ -[UARPAccessoryHardwareIPv6 description]
+ -[UARPAccessoryHardwareIPv6 init]
+ -[UARPAccessoryHardwareIPv6 isEqual:]
+ -[UARPAccessoryHardwareSerial description]
+ -[UARPAccessoryHardwareSerial init]
+ -[UARPAssetVersion compare:]
+ -[UARPController pendingTatsuRequests].cold.1
+ -[UARPController pendingTatsuRequests].cold.2
+ -[UARPController personalizationHelperQueryPendingTssRequests:].cold.1
+ -[UARPController personalizationHelperTssResponse:updaterName:].cold.1
+ -[UARPDeploymentRule addDeploymentLimit:withGoLiveDate:error:]
+ -[UARPDeploymentRule countryList]
+ -[UARPDeploymentRule currentISOCountryCode]
+ -[UARPDeploymentRule deploymentLimit]
+ -[UARPDeploymentRule deploymentLimits]
+ -[UARPDeploymentRule goLiveDate]
+ -[UARPDeploymentRule hash]
+ -[UARPDeploymentRule initWithConfig:].cold.1
+ -[UARPDeploymentRule isDeploymentAllowed:].cold.1
+ -[UARPDeploymentRule isEqual:]
+ -[UARPDeploymentRule isFullyDeployedDeploymentLimits]
+ -[UARPDeploymentRule rampPeriod]
+ -[UARPDeploymentRule setCountryList:]
+ -[UARPDeploymentRule setCurrentISOCountryCode:]
+ -[UARPDeploymentRule setDeploymentLimit:]
+ -[UARPDeploymentRule setDeploymentLimits:]
+ -[UARPDeploymentRule setGoLiveDate:]
+ -[UARPDeploymentRule setIsFullyDeployedDeploymentLimits:]
+ -[UARPDeploymentRule setRampPeriod:]
+ -[UARPDeploymentRule validateDeploymentLimits:]
+ -[UARPDynamicAssetPersonalization processDynamicAsset:].cold.2
+ -[UARPDynamicAssetPersonalization processDynamicAsset:].cold.3
+ -[UARPIPDevice .cxx_destruct]
+ -[UARPIPDevice connect]
+ -[UARPIPDevice connect].cold.1
+ -[UARPIPDevice dealloc]
+ -[UARPIPDevice initRecvSource]
+ -[UARPIPDevice initRecvSource].cold.1
+ -[UARPIPDevice initRecvSource].cold.2
+ -[UARPIPDevice initRecvSource].cold.3
+ -[UARPIPDevice initSocketWithIPv4Address:port:]
+ -[UARPIPDevice initSocketWithIPv6Address:port:]
+ -[UARPIPDevice initWithIPAddress:port:delegate:]
+ -[UARPIPDevice initWithIPAddress:port:delegate:].cold.1
+ -[UARPIPDevice initWithIPAddress:port:delegate:].cold.2
+ -[UARPIPDevice initWithIPAddress:port:delegate:].cold.3
+ -[UARPIPDevice initWithIPAddress:port:family:delegate:]
+ -[UARPIPDevice recvUARPMsg]
+ -[UARPIPDevice recvUARPMsg].cold.1
+ -[UARPIPDevice recvUARPMsg].cold.2
+ -[UARPIPDevice recvUARPMsg].cold.3
+ -[UARPIPDevice sendData:]
+ -[UARPPersonalizationManager getOutstandingPersonalizationRequests:reply:].cold.1
+ -[UARPPersonalizationManager getOutstandingPersonalizationRequests:reply:].cold.2
+ -[UARPPersonalizationManager personalizationResponse:updaterName:].cold.1
+ -[UARPPersonalizationManager personalizationResponse:updaterName:].cold.2
+ -[UARPPersonalizationManager personalizationResponse:updaterName:].cold.3
+ -[UARPSuperBinaryAsset decomposeToURL:error:].cold.4
+ -[UARPSuperBinaryAsset decomposeToURL:error:].cold.5
+ -[UARPSuperBinaryPlist .cxx_destruct]
+ -[UARPSuperBinaryPlist initWithPlist:]
+ -[UARPSuperBinaryPlist mergePlist:]
+ -[UARPSuperBinaryPlist writeToURL:]
+ -[UARPSupportedAccessory initWithIPv4Dictionary:]
+ -[UARPSupportedAccessory initWithIPv6Dictionary:]
+ -[UARPSupportedAccessory initWithSerialDictionary:]
+ -[UARPSupportedAccessoryA3299 .cxx_destruct]
+ -[UARPSupportedAccessoryA3299 init]
+ -[UARPSupportedAccessoryAirTag init]
+ -[UARPSupportedAccessoryIP init]
+ -[UARPUploaderEndpoint handlePersonalizationResponse:].cold.2
+ -[UARPUploaderEndpoint handlePersonalizationResponse:].cold.3
+ -[UARPUploaderEndpoint handlePersonalizationResponse:].cold.4
+ -[UARPUploaderEndpoint handlePersonalizationResponse:].cold.5
+ -[UARPUploaderEndpoint handlePersonalizationResponse:].cold.6
+ -[UARPUploaderEndpoint im4mAssetReceived:].cold.2
+ -[UARPUploaderEndpoint im4mAssetReceived:].cold.3
+ -[UARPUploaderEndpoint im4mAssetReceived:].cold.4
+ -[UARPUploaderEndpoint pendingTssRequests]
+ -[UARPUploaderEndpoint pendingTssRequests].cold.1
+ -[UARPUploaderUARP pendingTssRequests].cold.1
+ -[UARPUploaderUARP tssResponseForEndpoint:tssResponse:].cold.1
+ -[UARPUploaderUARP tssResponseForEndpoint:tssResponse:].cold.2
+ -[UARPUploaderUARP tssResponseForEndpoint:tssResponse:].cold.3
+ InternalStorageDirectoryPath.cold.1
+ OBJC_IVAR_$_UARPDeploymentRule._deploymentLimits
+ OBJC_IVAR_$_UARPDeploymentRule._isFullyDeployedDeploymentLimits
+ OBJC_IVAR_$_UARPIPDevice._delegate
+ OBJC_IVAR_$_UARPIPDevice._log
+ OBJC_IVAR_$_UARPIPDevice._queue
+ OBJC_IVAR_$_UARPIPDevice._recvSource
+ OBJC_IVAR_$_UARPIPDevice._socketAddress
+ OBJC_IVAR_$_UARPIPDevice._socketAddressFamily
+ OBJC_IVAR_$_UARPIPDevice._socketAddressLength
+ OBJC_IVAR_$_UARPIPDevice._socketFileDescriptor
+ OBJC_IVAR_$_UARPSuperBinaryPlist._sbDict
+ OBJC_IVAR_$_UARPSupportedAccessoryA3299.hwID
+ TSSRequestLogToken.cold.1
+ UARPAssetSolicitionComplete.cold.5
+ UARPAssetSolicitionComplete.cold.6
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
+ _OBJC_CLASS_$_UARPAccessoryHardwareIPv4
+ _OBJC_CLASS_$_UARPAccessoryHardwareIPv6
+ _OBJC_CLASS_$_UARPAccessoryHardwareSerial
+ _OBJC_CLASS_$_UARPIPDevice
+ _OBJC_CLASS_$_UARPSuperBinaryPlist
+ _OBJC_CLASS_$_UARPSupportedAccessoryA3299
+ _OBJC_CLASS_$_UARPSupportedAccessoryAirTag
+ _OBJC_CLASS_$_UARPSupportedAccessoryIP
+ _OBJC_METACLASS_$_UARPAccessoryHardwareIPv4
+ _OBJC_METACLASS_$_UARPAccessoryHardwareIPv6
+ _OBJC_METACLASS_$_UARPAccessoryHardwareSerial
+ _OBJC_METACLASS_$_UARPIPDevice
+ _OBJC_METACLASS_$_UARPSuperBinaryPlist
+ _OBJC_METACLASS_$_UARPSupportedAccessoryA3299
+ _OBJC_METACLASS_$_UARPSupportedAccessoryAirTag
+ _OBJC_METACLASS_$_UARPSupportedAccessoryIP
+ __25-[UARPIPDevice sendData:]_block_invoke.cold.1
+ __30-[UARPIPDevice initRecvSource]_block_invoke.4
+ __30-[UARPIPDevice initRecvSource]_block_invoke.cold.1
+ __32-[UARPUploaderUARP tssResponse:]_block_invoke.cold.1
+ __32-[UARPUploaderUARP tssResponse:]_block_invoke.cold.2
+ __38-[UARPController pendingTatsuRequests]_block_invoke.cold.1
+ __38-[UARPUploaderUARP pendingTssRequests]_block_invoke.cold.1
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSFileHandle_$_Availability
+ __OBJC_$_CLASS_METHODS_UARPSupportedAccessoryA3299
+ __OBJC_$_CLASS_METHODS_UARPSupportedAccessoryAirTag
+ __OBJC_$_CLASS_METHODS_UARPSupportedAccessoryIP
+ __OBJC_$_INSTANCE_METHODS_UARPAccessoryHardwareIPv4
+ __OBJC_$_INSTANCE_METHODS_UARPAccessoryHardwareIPv6
+ __OBJC_$_INSTANCE_METHODS_UARPAccessoryHardwareSerial
+ __OBJC_$_INSTANCE_METHODS_UARPIPDevice
+ __OBJC_$_INSTANCE_METHODS_UARPSuperBinaryPlist
+ __OBJC_$_INSTANCE_METHODS_UARPSupportedAccessoryA3299
+ __OBJC_$_INSTANCE_METHODS_UARPSupportedAccessoryAirTag
+ __OBJC_$_INSTANCE_METHODS_UARPSupportedAccessoryIP
+ __OBJC_$_INSTANCE_VARIABLES_UARPIPDevice
+ __OBJC_$_INSTANCE_VARIABLES_UARPSuperBinaryPlist
+ __OBJC_$_INSTANCE_VARIABLES_UARPSupportedAccessoryA3299
+ __OBJC_$_PROP_LIST_UARPDeploymentRule
+ __OBJC_CLASS_RO_$_UARPAccessoryHardwareIPv4
+ __OBJC_CLASS_RO_$_UARPAccessoryHardwareIPv6
+ __OBJC_CLASS_RO_$_UARPAccessoryHardwareSerial
+ __OBJC_CLASS_RO_$_UARPIPDevice
+ __OBJC_CLASS_RO_$_UARPSuperBinaryPlist
+ __OBJC_CLASS_RO_$_UARPSupportedAccessoryA3299
+ __OBJC_CLASS_RO_$_UARPSupportedAccessoryAirTag
+ __OBJC_CLASS_RO_$_UARPSupportedAccessoryIP
+ __OBJC_METACLASS_RO_$_UARPAccessoryHardwareIPv4
+ __OBJC_METACLASS_RO_$_UARPAccessoryHardwareIPv6
+ __OBJC_METACLASS_RO_$_UARPAccessoryHardwareSerial
+ __OBJC_METACLASS_RO_$_UARPIPDevice
+ __OBJC_METACLASS_RO_$_UARPSuperBinaryPlist
+ __OBJC_METACLASS_RO_$_UARPSupportedAccessoryA3299
+ __OBJC_METACLASS_RO_$_UARPSupportedAccessoryAirTag
+ __OBJC_METACLASS_RO_$_UARPSupportedAccessoryIP
+ ___25-[UARPIPDevice sendData:]_block_invoke
+ ___30-[UARPIPDevice initRecvSource]_block_invoke
+ ___error
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
+ __dispatch_source_type_read
+ _close
+ _connect
+ _dispatch_source_get_data
+ _dispatch_source_set_cancel_handler
+ _inet_pton
+ _kAUAssetLocationTypeMobileAssetServerBasejumperBaseStr
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
+ _malloc_type_malloc
+ _objc_msgSend$addDeploymentLimit:withGoLiveDate:error:
+ _objc_msgSend$connect
+ _objc_msgSend$currentISOCountryCode
+ _objc_msgSend$initRecvSource
+ _objc_msgSend$initSocketWithIPv4Address:port:
+ _objc_msgSend$initSocketWithIPv6Address:port:
+ _objc_msgSend$initWithIPAddress:port:delegate:
+ _objc_msgSend$lastObject
+ _objc_msgSend$receivedData:device:
+ _objc_msgSend$recvUARPMsg
+ _objc_msgSend$replaceBytesInRange:withBytes:
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$validateDeploymentLimits:
+ _recv
+ _send
+ _setsockopt
+ _socket
+ _strerror
+ currentTrainName.cold.1
- -[UARPSuperBinaryAsset parseFromPlistSuperBinaryPayloads:payloadsURL:error:].cold.2
- -[UARPSuperBinaryAsset writeToURL:payloadStartOffset:error:].cold.12
- -[UARPUploaderUARP pendingTssRequestForEndpoint:]
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
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
- _objc_msgSend$pendingTssRequestForEndpoint:
CStrings:
+ "%s: "
+ "%s: Checking downstream endpoint (%u) for TSS requests for %@"
+ "%s: Checking endpoint %@ for TSS requests for response %@"
+ "%s: Checking for pending TSS requests on %@"
+ "%s: Checking pending TSS requests for (ds id is %u) %@"
+ "%s: Failed receive UARP message, closing socket"
+ "%s: Failed to connect"
+ "%s: Failed to connect on socket: %s"
+ "%s: Failed to create dispatch_source_t"
+ "%s: Failed to initialize deployment limits with error %@"
+ "%s: Failed to initialize recvSource"
+ "%s: Failed to initialize socket"
+ "%s: Failed to process IM4M; error %@"
+ "%s: Failed to receive UARP Message Header on connected socket: %s"
+ "%s: Failed to receive UARP Message Payload on connected socket: %s"
+ "%s: Failed to send UARP Message on connected socket"
+ "%s: Failed to set socket option SO_NOSIGPIPE for socket: %s"
+ "%s: Failed to set socket option SO_RCVTIMEO for socket: %s"
+ "%s: Found %lu for pending TSS requests on %@"
+ "%s: Generating Read Sandbox Extension Token for %@ "
+ "%s: No pending TSS request on %@"
+ "%s: No pending TSS request on downstream endpoint %@"
+ "%s: No pending/matching TSS requests on direct endpoint for %@"
+ "%s: Num of pending tatsu requests %lu"
+ "%s: Pending TSS requests, there is %lu rx dynamic assets"
+ "%s: RX IM4M Dynamic Asset"
+ "%s: RX IM4M Dynamic Asset failed to be processed"
+ "%s: Tag does not equal IM4M; %@"
+ "%s: UARP Message Payload length exceeds maximum (%u bytes)"
+ "%s: delegate is %@"
+ "%s: enter"
+ "%s: failed to consume sandbox token"
+ "%s; RX IM4M dynamic asset; %@"
+ "%s; failed to process dynamic asset"
+ "+[UARPSandboxExtension readTokenStringWithURL:]"
+ "-[UARPController personalizationHelperQueryPendingTssRequests:]"
+ "-[UARPController personalizationHelperTssResponse:updaterName:]"
+ "-[UARPDeploymentRule initWithConfig:]"
+ "-[UARPDynamicAssetPersonalization processDynamicAsset:]"
+ "-[UARPIPDevice connect]"
+ "-[UARPIPDevice initRecvSource]"
+ "-[UARPIPDevice initRecvSource]_block_invoke"
+ "-[UARPIPDevice initWithIPAddress:port:delegate:]"
+ "-[UARPIPDevice recvUARPMsg]"
+ "-[UARPIPDevice sendData:]_block_invoke"
+ "-[UARPUploaderEndpoint im4mAssetReceived:]"
+ "-[UARPUploaderEndpoint pendingTssRequests]"
+ "-[UARPUploaderUARP pendingTssRequests]"
+ "-[UARPUploaderUARP pendingTssRequests]_block_invoke"
+ "@\"<UARPIPDeviceDelegate>\""
+ "@32@0:8@16o^@24"
+ "@36@0:8@16S24@28"
+ "@40@0:8@16S24C28@32"
+ "A3299"
+ "Assets"
+ "B28@0:8@16S24"
+ "Error closing URL %@ to decompose superbinary; error is %@"
+ "Error expanding payload to URL; error is %@"
+ "Error seeking to offset for payload header; error is %@"
+ "Error seeking to offset for superbinary header; error is %@"
+ "Flash Section Length"
+ "GlowE"
+ "IPv4"
+ "IPv6"
+ "Invalid Deployment Rule: Deployment Limit %lu for %@ with Go Live Date %@ is invalid, must be strictly increasing"
+ "Invalid Deployment Rule: Deployment Limit already set on Go Live Date %@ for %@"
+ "Invalid Deployment Rule: Deployment already scheduled for full deployment for %@"
+ "Payload Ordered Index"
+ "Serial"
+ "T@\"NSMutableDictionary\",C,V_deploymentLimits"
+ "T@\"NSString\",C,V_currentISOCountryCode"
+ "TB,V_isFullyDeployedDeploymentLimits"
+ "UARPAccessoryHardwareIPv4"
+ "UARPAccessoryHardwareIPv6"
+ "UARPAccessoryHardwareSerial"
+ "UARPAssetSolicitionComplete"
+ "UARPIPDevice"
+ "UARPSuperBinaryPlist"
+ "UARPSupportedAccessoryA3299"
+ "UARPSupportedAccessoryAirTag"
+ "UARPSupportedAccessoryIP"
+ "UID_MODE"
+ "USB-C Dongle"
+ "^{sockaddr=CC[14c]}"
+ "_deploymentLimits"
+ "_isFullyDeployedDeploymentLimits"
+ "_recvSource"
+ "_sbDict"
+ "_socketAddress"
+ "_socketAddressFamily"
+ "_socketAddressLength"
+ "_socketFileDescriptor"
+ "addDeploymentLimit:withGoLiveDate:error:"
+ "com.apple.app-sandbox.read"
+ "connect"
+ "currentISOCountryCode"
+ "deploymentLimits"
+ "findByMobileAssetAppleModelNumber:"
+ "https://basejumper.apple.com"
+ "initRecvSource"
+ "initSocketWithIPv4Address:port:"
+ "initSocketWithIPv6Address:port:"
+ "initWithIPAddress:port:delegate:"
+ "initWithIPAddress:port:family:delegate:"
+ "initWithIPv4Dictionary:"
+ "initWithIPv6Dictionary:"
+ "initWithSerialDictionary:"
+ "isFullyDeployedDeploymentLimits"
+ "lastObject"
+ "mergePlist:"
+ "ota disabled"
+ "posting bsd notification to personalization helper; %s for %@"
+ "q24@0:8@16"
+ "readTokenStringWithURL:"
+ "receivedData:device:"
+ "recvUARPMsg"
+ "replaceBytesInRange:withBytes:"
+ "sendData:"
+ "setCurrentISOCountryCode:"
+ "setDeploymentLimits:"
+ "setIsFullyDeployedDeploymentLimits:"
+ "sortedArrayUsingSelector:"
+ "uarpCreateFileHandleForWritingToURL:error:"
+ "uarpIPDevice"
+ "v40@0:8@16@24^@32"
+ "validateDeploymentLimits:"
- "%s: Checking pending TSS requests for %@"
- "%s: No pending/matching TSS requests for %@"
- "%s: failed to cosume sandbox token"
- "-[UARPUploaderUARP pendingTssRequestForEndpoint:]"
- "GlowD"
- "pendingTssRequestForEndpoint:"
- "posting bsd notification to personalization helper; %s"

```
