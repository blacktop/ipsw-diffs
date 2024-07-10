## CoreUARP

> `/System/Library/PrivateFrameworks/CoreUARP.framework/Versions/A/CoreUARP`

```diff

-1163.0.0.0.0
-  __TEXT.__text: 0x875f8
+1155.0.0.0.0
+  __TEXT.__text: 0x84b10
   __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_methlist: 0x7dfc
+  __TEXT.__objc_methlist: 0x7c64
   __TEXT.__const: 0x210
-  __TEXT.__cstring: 0x6761
-  __TEXT.__oslogstring: 0x596b
-  __TEXT.__gcc_except_tab: 0x840
+  __TEXT.__cstring: 0x6600
+  __TEXT.__gcc_except_tab: 0x744
+  __TEXT.__oslogstring: 0x55ba
   __TEXT.__dlopen_cstrs: 0x10e
-  __TEXT.__unwind_info: 0x23e8
-  __TEXT.__objc_classname: 0x16a8
-  __TEXT.__objc_methname: 0xd70f
-  __TEXT.__objc_methtype: 0x39b4
-  __TEXT.__objc_stubs: 0x93c0
-  __DATA_CONST.__got: 0x6b0
-  __DATA_CONST.__const: 0x16b8
-  __DATA_CONST.__objc_classlist: 0x5e8
+  __TEXT.__unwind_info: 0x2300
+  __TEXT.__objc_classname: 0x161b
+  __TEXT.__objc_methname: 0xd328
+  __TEXT.__objc_methtype: 0x38d2
+  __TEXT.__objc_stubs: 0x90c0
+  __DATA_CONST.__got: 0x688
+  __DATA_CONST.__const: 0x1698
+  __DATA_CONST.__objc_classlist: 0x5d8
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e98
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x5d8
+  __DATA_CONST.__objc_selrefs: 0x2db0
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x5c8
   __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x980
-  __AUTH_CONST.__cfstring: 0x6860
-  __AUTH_CONST.__objc_const: 0x11160
+  __AUTH_CONST.__const: 0x8e0
+  __AUTH_CONST.__cfstring: 0x6760
+  __AUTH_CONST.__objc_const: 0x106a8
   __AUTH_CONST.__objc_intobj: 0xc60
-  __AUTH.__objc_data: 0x3b10
-  __DATA.__objc_ivar: 0xb30
-  __DATA.__data: 0x40d
-  __DATA.__bss: 0x1b0b
+  __AUTH.__objc_data: 0x3a70
+  __DATA.__objc_ivar: 0xaf4
+  __DATA.__data: 0x2ed
+  __DATA.__bss: 0x1aeb
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/GeoServices.framework/Versions/A/GeoServices
-  - /System/Library/PrivateFrameworks/OSAnalytics.framework/Versions/A/OSAnalytics
   - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 3657
-  Symbols:   7956
-  CStrings:  1234
+  Functions: 3603
+  Symbols:   7798
+  CStrings:  1223
 
Symbols:
+ -[UARPDynamicAssetCrashLogEvent getSuperBinaryMetaData]
+ -[UARPDynamicAssetCrashLogEvent getSuperBinaryMetaData].cold.1
+ -[UARPDynamicAssetCrashLogEvent getSuperBinaryMetaData].cold.2
+ -[UARPDynamicAssetCrashLogEvent getSuperBinaryMetaData].cold.3
+ -[UARPDynamicAssetCrashLogEvent getSuperBinaryMetaData].cold.4
+ -[UARPDynamicAssetCrashLogEvent getSuperBinaryMetaData].cold.5
+ -[UARPDynamicAssetMappedAnalyticsEvent expandMTICPayloads].cold.2
+ -[UARPUploaderEndpoint cleanupAgedPacketCaptures:]
+ -[UARPUploaderEndpoint uniquePacketCaptureFilename]
+ -[UARPUploaderUARP addTmapDatabaseFromAsset:]
+ -[UARPUploaderUARP copyLogsToTtr:]
+ -[UARPUploaderUARP copyLogsToTtr:].cold.1
+ -[UARPUploaderUARP copyLogsToTtr:].cold.2
+ -[UARPUploaderUARP createLogsFilename:forPayload:]
+ -[UARPUploaderUARP expandLogsToDirectory:forEndpoint:]
+ -[UARPUploaderUARP expandLogsToDirectory:forEndpoint:].cold.1
+ -[UARPUploaderUARP expandLogsToDirectory:forEndpoint:].cold.2
+ -[UARPUploaderUARP genericNotification:notificationName:error:].cold.2
+ -[UARPUploaderUARP solicitLogsFromEndpoint:]
+ -[UARPUploaderUARP solicitLogsFromEndpoint:].cold.1
+ -[UARPUploaderUARP uarpWriteData:toURL:]
+ -[UARPUploaderUARP uarpWriteData:toURL:].cold.1
+ -[UARPUploaderUARP uarpWriteData:toURL:].cold.2
+ -[UARPUploaderUARP uarpWriteData:toURL:].cold.3
+ -[UARPUploaderUARP uarpWriteData:toURL:].cold.4
+ GCC_except_table10
+ GCC_except_table221
+ GCC_except_table39
+ GCC_except_table40
+ OBJC_IVAR_$_UARPDynamicAssetCrashLogDecoder._uuid
+ __block_literal_global.738
+ __block_literal_global.740
+ __block_literal_global.742
+ __block_literal_global.875
+ __block_literal_global.877
+ __block_literal_global.882
+ __block_literal_global.950
+ __block_literal_global.952
+ _objc_msgSend$addTmapDatabaseFromAsset:
+ _objc_msgSend$archivedDataWithRootObject:
+ _objc_msgSend$cleanupAgedPacketCaptures:
+ _objc_msgSend$copyLogsToTtr:
+ _objc_msgSend$createLogsFilename:forPayload:
+ _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
+ _objc_msgSend$expandLogsToDirectory:forEndpoint:
+ _objc_msgSend$getSuperBinaryMetaData
+ _objc_msgSend$initWithSectionName:uuid:inputDictionary:
+ _objc_msgSend$initWithUuid:sectionName:inputDictionary:
+ _objc_msgSend$prepareAndSend
+ _objc_msgSend$replaceItemAtURL:withItemAtURL:backupItemName:options:resultingItemURL:error:
+ _objc_msgSend$solicitLogsFromEndpoint:
+ _objc_msgSend$uarpWriteData:toURL:
+ _objc_msgSend$unarchiveObjectWithData:
+ _objc_msgSend$uniquePacketCaptureFilename
- +[UARPDynamicAssetLogsEvent tag]
- -[UARPController personalizationHelperQueryPendingTssRequests:]
- -[UARPController personalizationHelperTssResponse:updaterName:]
- -[UARPController startPersonalizationHelperService:entitlement:]
- -[UARPDynamicAssetCmapDatabase addCmapMapping:].cold.2
- -[UARPDynamicAssetCmapEvent decoderId]
- -[UARPDynamicAssetCmapEvent initWithSectionName:decoderId:inputDictionary:]
- -[UARPDynamicAssetCmapMapping appendCmapEvents:]
- -[UARPDynamicAssetCmapMapping appendCmapEvents:].cold.1
- -[UARPDynamicAssetCmapMapping appendCmapEvents:].cold.2
- -[UARPDynamicAssetCmapMapping appendCmapEvents:].cold.3
- -[UARPDynamicAssetCrashLogDecoder initWithDecoderId:sectionName:inputDictionary:]
- -[UARPDynamicAssetCrashLogEvent expandToDirectory:forRemoteEndpoint:]
- -[UARPDynamicAssetCrashLogEvent processCrashAdditionalInfo]
- -[UARPDynamicAssetCrashLogEvent processCrashAdditionalInfo].cold.1
- -[UARPDynamicAssetCrashLogEvent processCrashAdditionalInfo].cold.2
- -[UARPDynamicAssetCrashLogEvent processCrashAdditionalInfo].cold.3
- -[UARPDynamicAssetCrashLogEvent processCrashAdditionalInfo].cold.4
- -[UARPDynamicAssetCrashLogEvent processCrashAdditionalInfo].cold.5
- -[UARPDynamicAssetCrashLogEvent sendSpeedTracer]
- -[UARPDynamicAssetCrashLogEvent sendSpeedTracer].cold.1
- -[UARPDynamicAssetLogsEvent .cxx_destruct]
- -[UARPDynamicAssetLogsEvent createLogsFilepath:forRemoteEndpoint:]
- -[UARPDynamicAssetLogsEvent decomposeUARP]
- -[UARPDynamicAssetLogsEvent decomposeUARP].cold.1
- -[UARPDynamicAssetLogsEvent expandToDirectory:forRemoteEndpoint:]
- -[UARPDynamicAssetLogsEvent expandToDirectory:forRemoteEndpoint:].cold.1
- -[UARPDynamicAssetLogsEvent initWithURL:]
- -[UARPDynamicAssetLogsEvent init]
- -[UARPDynamicAssetMappedAnalyticsEvent findMatchingTMAP]
- -[UARPDynamicAssetMappedAnalyticsEvent findMatchingTMAP].cold.1
- -[UARPDynamicAssetMappedAnalyticsEvent findMatchingTMAP].cold.2
- -[UARPDynamicAssetTmapDatabase addTmapMapping:].cold.2
- -[UARPDynamicAssetTmapMapping appendTmapEvents:endian:]
- -[UARPDynamicAssetTmapMapping appendTmapEvents:endian:].cold.1
- -[UARPPersonalizationManager .cxx_destruct]
- -[UARPPersonalizationManager dealloc]
- -[UARPPersonalizationManager getOutstandingPersonalizationRequests:reply:]
- -[UARPPersonalizationManager initWithMachServiceName:entitlement:delegate:queue:]
- -[UARPPersonalizationManager listener:shouldAcceptNewConnection:]
- -[UARPPersonalizationManager personalizationResponse:updaterName:]
- -[UARPPersonalizationManager xpcConnectionHasEntitlement:]
- -[UARPPersonalizationManager xpcConnectionHasEntitlement:].cold.1
- -[UARPPersonalizationManager xpcConnectionHasEntitlement:].cold.2
- -[UARPSuperBinaryAsset assetTag]
- -[UARPSuperBinaryAsset decomposeToURL:error:].cold.3
- -[UARPSuperBinaryAsset initWithURL:assetTag:]
- -[UARPSuperBinaryAsset timeCreated]
- -[UARPSuperBinaryAsset url]
- -[UARPUploaderEndpoint createUniqueEndpointFilename:withAssetTag:withSuffix:]
- -[UARPUploaderEndpoint im4mAssetReceived:].cold.1
- -[UARPUploaderUARP addMappingDatabaseFromAsset:]
- -[UARPUploaderUARP addUnprocessedDynamicAsset:withAssetTag:]
- -[UARPUploaderUARP ageOutUnprocessedDynamicAssets]
- -[UARPUploaderUARP copyDynamicAssetsForTapToRadar]
- -[UARPUploaderUARP processDynamicAssets]
- -[UARPUploaderUARP processMticDynamicAsset:]
- -[UARPUploaderUARP solicitDynamicAssetsForTapToRadar:]
- -[UARPUploaderUARP ttrDirectory]
- GCC_except_table224
- GCC_except_table31
- GCC_except_table7
- OBJC_IVAR_$_UARPController._personalizationManager
- OBJC_IVAR_$_UARPController._personalizationQueue
- OBJC_IVAR_$_UARPDynamicAssetCmapEvent._decoderId
- OBJC_IVAR_$_UARPDynamicAssetCrashLogDecoder._decoderId
- OBJC_IVAR_$_UARPDynamicAssetLogsEvent._asset
- OBJC_IVAR_$_UARPDynamicAssetLogsEvent._log
- OBJC_IVAR_$_UARPDynamicAssetLogsEvent._url
- OBJC_IVAR_$_UARPPersonalizationManager._delegate
- OBJC_IVAR_$_UARPPersonalizationManager._entitlement
- OBJC_IVAR_$_UARPPersonalizationManager._listener
- OBJC_IVAR_$_UARPPersonalizationManager._log
- OBJC_IVAR_$_UARPPersonalizationManager._queue
- OBJC_IVAR_$_UARPPersonalizationManager._serviceName
- OBJC_IVAR_$_UARPSuperBinaryAsset._assetTag
- OBJC_IVAR_$_UARPSuperBinaryAsset._timeCreated
- OBJC_IVAR_$_UARPUploaderUARP._unprocessedDynamicAssets
- UARPCleanupAgedFiles.cold.1
- UARPCopyFile.cold.1
- UARPStringCrashAnalyticsDirectoryFilePath.onceToken
- UARPStringCrashAnalyticsDirectoryFilePath.path
- UARPStringTapToRadarFilePath.onceToken
- UARPStringTapToRadarFilePath.path
- UARPWriteFile.cold.1
- UARPWriteFile.cold.2
- UARPWriteFile.cold.3
- UARPWriteFile.cold.4
- UARPlatformEndpointHandleMappedAnalytics.cold.2
- _OBJC_CLASS_$_NSXPCListener
- _OBJC_CLASS_$_OSALog
- _OBJC_CLASS_$_UARPDynamicAssetLogsEvent
- _OBJC_CLASS_$_UARPPersonalizationManager
- _OBJC_METACLASS_$_UARPDynamicAssetLogsEvent
- _OBJC_METACLASS_$_UARPPersonalizationManager
- _UARPCleanupAgedFiles
- _UARPCopyFile
- _UARPStringCrashAnalyticsDirectoryFilePath
- _UARPStringTapToRadarFilePath
- _UARPWriteFile
- _UARPlatformEndpointHandleCrashAnalytics
- _UARPlatformEndpointHandleLogs
- __65-[UARPPersonalizationManager listener:shouldAcceptNewConnection:]_block_invoke.11
- __65-[UARPPersonalizationManager listener:shouldAcceptNewConnection:]_block_invoke_2.cold.1
- __OBJC_$_CLASS_METHODS_UARPDynamicAssetLogsEvent
- __OBJC_$_INSTANCE_METHODS_UARPDynamicAssetLogsEvent
- __OBJC_$_INSTANCE_METHODS_UARPPersonalizationManager
- __OBJC_$_INSTANCE_VARIABLES_UARPDynamicAssetLogsEvent
- __OBJC_$_INSTANCE_VARIABLES_UARPPersonalizationManager
- __OBJC_$_PROP_LIST_UARPPersonalizationManager
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_UARPPersonalizationHelperProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_UARPPersonalizationProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_UARPPersonalizationHelperProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_UARPPersonalizationProtocol
- __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
- __OBJC_$_PROTOCOL_REFS_UARPPersonalizationHelperProtocol
- __OBJC_CLASS_PROTOCOLS_$_UARPController
- __OBJC_CLASS_PROTOCOLS_$_UARPPersonalizationManager
- __OBJC_CLASS_RO_$_UARPDynamicAssetLogsEvent
- __OBJC_CLASS_RO_$_UARPPersonalizationManager
- __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
- __OBJC_LABEL_PROTOCOL_$_UARPPersonalizationHelperProtocol
- __OBJC_LABEL_PROTOCOL_$_UARPPersonalizationProtocol
- __OBJC_METACLASS_RO_$_UARPDynamicAssetLogsEvent
- __OBJC_METACLASS_RO_$_UARPPersonalizationManager
- __OBJC_PROTOCOL_$_NSXPCListenerDelegate
- __OBJC_PROTOCOL_$_UARPPersonalizationHelperProtocol
- __OBJC_PROTOCOL_$_UARPPersonalizationProtocol
- __OBJC_PROTOCOL_REFERENCE_$_UARPPersonalizationProtocol
- ___48-[UARPDynamicAssetCrashLogEvent sendSpeedTracer]_block_invoke
- ___65-[UARPPersonalizationManager listener:shouldAcceptNewConnection:]_block_invoke
- ___65-[UARPPersonalizationManager listener:shouldAcceptNewConnection:]_block_invoke_2
- ___UARPStringCrashAnalyticsDirectoryFilePath_block_invoke
- ___UARPStringTapToRadarFilePath_block_invoke
- ___block_descriptor_40_e8_32s_e22_v16?0"NSFileHandle"8l
- ___block_descriptor_44_e8_32s_e5_v8?0l
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
- _kOSALogOptionOverrideFilePrefix
- _kUARPStringBsdNotificationPersonalizationNeededBTLEServer
- _kUARPStringCMAPDecoderId
- _kUARPStringCrashAnalyticsDirectory
- _kUARPStringTapToRadar
- _objc_msgSend$_setQueue:
- _objc_msgSend$activate
- _objc_msgSend$addMappingDatabaseFromAsset:
- _objc_msgSend$addUnprocessedDynamicAsset:withAssetTag:
- _objc_msgSend$ageOutUnprocessedDynamicAssets
- _objc_msgSend$appendCmapEvents:
- _objc_msgSend$appendTmapEvents:endian:
- _objc_msgSend$assetTag
- _objc_msgSend$copyDynamicAssetsForTapToRadar
- _objc_msgSend$createForSubmission:metadata:options:error:writing:
- _objc_msgSend$createLogsFilepath:forRemoteEndpoint:
- _objc_msgSend$createUniqueEndpointFilename:withAssetTag:withSuffix:
- _objc_msgSend$expandToDirectory:forRemoteEndpoint:
- _objc_msgSend$filepath
- _objc_msgSend$findMatchingTMAP
- _objc_msgSend$initWithDecoderId:sectionName:inputDictionary:
- _objc_msgSend$initWithMachServiceName:
- _objc_msgSend$initWithMachServiceName:entitlement:delegate:queue:
- _objc_msgSend$initWithSectionName:decoderId:inputDictionary:
- _objc_msgSend$initWithURL:assetTag:
- _objc_msgSend$pendingTatsuRequests
- _objc_msgSend$personalizationHelperQueryPendingTssRequests:
- _objc_msgSend$personalizationHelperTssResponse:updaterName:
- _objc_msgSend$processCrashAdditionalInfo
- _objc_msgSend$processCrashInstance
- _objc_msgSend$processDynamicAssets
- _objc_msgSend$processIdentifier
- _objc_msgSend$processMticDynamicAsset:
- _objc_msgSend$relativeString
- _objc_msgSend$sendSpeedTracer
- _objc_msgSend$setDelegate:
- _objc_msgSend$setExportedInterface:
- _objc_msgSend$setExportedObject:
- _objc_msgSend$solicitDynamicAssetsForTapToRadar:
- _objc_msgSend$timeCreated
- _objc_msgSend$timeIntervalSinceNow
- _objc_msgSend$ttrDirectory
- _objc_msgSend$valueForEntitlement:
- _objc_msgSend$writeData:
- _objc_msgSend$xpcConnectionHasEntitlement:
- _uarpPlatformGetMaxRxPayloadLength
- _uarpPlatformGetMaxTxPayloadLength
- _uarpPlatformSetMaxRxPayloadLength
- _uarpPlatformSetMaxTxPayloadLength
CStrings:
+ "%!@(MISSING)-%!@(MISSING)-%!@(MISSING)-%!@(MISSING)"
+ "%!@(MISSING)-%!@(MISSING).pcap"
+ "-[UARPUploaderUARP copyLogsToTtr:]"
+ "-[UARPUploaderUARP expandLogsToDirectory:forEndpoint:]"
+ "crshAnalytics"
+ "dd-MM-yyyy-hh-mm-ss"
- "%!@(MISSING)-"
- ", BSD Notifications = %!@(MISSING)"
- ", Service BSD Notifications = %!@(MISSING)"
- "-[UARPDynamicAssetCrashLogEvent expandToDirectory:forRemoteEndpoint:]"
- "-[UARPDynamicAssetLogsEvent expandToDirectory:forRemoteEndpoint:]"
- "-[UARPPersonalizationManager getOutstandingPersonalizationRequests:reply:]"
- "-[UARPPersonalizationManager personalizationResponse:updaterName:]"
- ".json"
- ".pcap"
- "AccessoryCrash"
- "CRSH"
- "UARPController personalization"
- "com.apple.uarp.BTLEServer.personalizationNeeded"
- "crsh"
- "decoderId"
- "taptoradar"
- "v16@?0@\"NSFileHandle\"8"

```
