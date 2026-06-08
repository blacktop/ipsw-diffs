## libAce3Updater.dylib

> `/usr/lib/updaters/libAce3Updater.dylib`

```diff

-1345.120.5.0.0
-  __TEXT.__text: 0x1f19c
-  __TEXT.__auth_stubs: 0x880
+1576.0.0.0.0
+  __TEXT.__text: 0x1ef4c
   __TEXT.__objc_methlist: 0x3b4
-  __TEXT.__cstring: 0x5ec6
+  __TEXT.__cstring: 0x5edb
   __TEXT.__const: 0x200
   __TEXT.__oslogstring: 0x7
-  __TEXT.__unwind_info: 0x7a8
-  __TEXT.__objc_classname: 0x84
-  __TEXT.__objc_methname: 0xa38
-  __TEXT.__objc_methtype: 0x852
-  __TEXT.__objc_stubs: 0x9c0
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__unwind_info: 0x798
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x5e0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c0
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x448
-  __AUTH_CONST.__cfstring: 0xfc0
+  __DATA_CONST.__got: 0xc0
+  __AUTH_CONST.__cfstring: 0xfe0
   __AUTH_CONST.__objc_const: 0x918
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x98
   __DATA.__data: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 39DC5EAE-95D3-3710-A61B-9AEB138B72F5
-  Functions: 955
-  Symbols:   1674
-  CStrings:  1002
+  UUID: 6F40934C-D415-39E8-BE5B-6E52FF145F17
+  Functions: 953
+  Symbols:   1672
+  CStrings:  825
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x4
+ _objc_retain_x8
+ _uarpPlatformEndpointAssetFullyStagedRequiresReboot
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "AppleHPM"
+ "IOParentMatch"
- ".cxx_destruct"
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSString\""
- "@\"SoCUpdaterHelper\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@36@0:8C16@20@28"
- "@36@0:8I16@20@28"
- "@40@0:8@16^?24^v32"
- "Ace3UpdateController"
- "Ace3UpdaterInstance"
- "AppleHPMARM"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "C"
- "C16@0:8"
- "I"
- "I16@0:8"
- "KeyPrefixSearch"
- "SoCUpdaterHelper"
- "T@\"NSDictionary\",R"
- "T@\"NSString\",R"
- "T@\"NSString\",R,V_restorePartition"
- "T@\"SoCUpdaterHelper\",&,V_log"
- "TB,R"
- "TB,R,V_isDone"
- "TB,R,V_skipSameVersion"
- "TC,V_routerID"
- "TI,V_applyFlags"
- "TI,V_logicUnitNumber"
- "TI,V_stagingStatus"
- "TI,V_stagingStatusReason"
- "Ti,V_updaterMode"
- "UARPSoCUpdaterController"
- "UARPSoCUpdaterInstance"
- "UTF8String"
- "^?"
- "^v"
- "^v16@0:8"
- "^{_uarpRestoreEndpoint={uarpRestoreLayer3Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}{uarpPlatformOptionsObj=IIISCSSSiSSCSCC}{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S^{uarpLayer2EndpointIDInfo}S^{uarpDownstreamEndpointObj}I^{uarpMemoryTracker}}{uarpPlatformEndpointApple=CCCC{uarpPlatformEndpointAppleCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}}{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^vSSSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}}^{_uarpRestoreAsset}^{_uarpRestoreAsset}^vCSi^ii^i****{UARPVersion=IIII}{UARPVersion=IIII}@@****(?=IQ)IIQ*IIIIICCCCI*CIIII^vI*ICCC*I}"
- "^{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}16@0:8"
- "_applyAssetUARPSemaphore"
- "_applyFlags"
- "_assetTransferUARPSemaphore"
- "_endpoint"
- "_forceLocalSigning"
- "_initUARPSemaphore"
- "_isDone"
- "_lastPercentComplete"
- "_log"
- "_logContext"
- "_logFunction"
- "_logicUnitNumber"
- "_logicUnitNumberFromDevice"
- "_manifestPrefixName"
- "_name"
- "_nextUpdateProgressReportPercentThreshold"
- "_pAssetContext"
- "_personalizationRequests"
- "_prefixNeedsLogicalUnitNumber"
- "_queue"
- "_requiresPersonalization"
- "_restorePartition"
- "_routerID"
- "_skipSameVersion"
- "_stagingResult"
- "_stagingStatus"
- "_stagingStatusReason"
- "_suffixNeedsLogicalUnitNumber"
- "_ticketLongName"
- "_tssRequest"
- "_tssRequestServerURL"
- "_uarpContext"
- "_updaterMode"
- "_updaters"
- "_verbose"
- "addEntriesFromDictionary:"
- "addObject:"
- "appendString:"
- "applyAssetComplete"
- "applyFlags"
- "applyStagedFirmware"
- "arrayWithArray:"
- "assetTransferUARPComplete"
- "boolValue"
- "bytes"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createUpdaterInstanceFor:helper:options:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "firmwareTagName"
- "firmwareTags"
- "hasPrefix:"
- "i"
- "i16@0:8"
- "init"
- "initUARP"
- "initUARPComplete"
- "initUARPRestoreQueryInfo"
- "initUARPWithFirmware:"
- "initWithFormat:arguments:"
- "initWithHelper:options:"
- "initWithLogicUnitNumber:helper:options:"
- "initWithOptions:logFunction:logContext:"
- "initWithRouterID:helper:options:"
- "initializeUpdatersWithOptions:"
- "isDone"
- "isEqual:"
- "isEqualToString:"
- "keyWithPrefix:"
- "length"
- "log"
- "log:"
- "logInternal:arguments:"
- "logicUnitNumber"
- "manifestPrefix"
- "name"
- "namePrefix"
- "numberOfAvailableUnits"
- "numberWithBool:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "offerFirmwareData:"
- "offerFirmwareDataWithDictionary:"
- "offerFirmwareForUpdater:inputDict:"
- "offerPersonalizationDataWithDictionary:"
- "offerPersonalizationResponse:"
- "personalizationRequestDict"
- "personalizationRequests"
- "printUpdaterMode"
- "r*16@0:8"
- "receievePersonalizationRequestByOfferFirmwareData:"
- "restorePartition"
- "routerID"
- "setApplyFlags:"
- "setLog:"
- "setLogicUnitNumber:"
- "setRouterID:"
- "setStagingStatus:"
- "setStagingStatusReason:"
- "setUpdaterMode:"
- "skipApplyStage"
- "skipSameVersion"
- "stagingCompleteWithStatus:reason:"
- "stagingStatus"
- "stagingStatusReason"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "ticketName"
- "ticketNameTags"
- "tssRequestWithOptions:serverURL:assetCtx:siliconCtx:"
- "uarpRestoreInitOptions"
- "uarpRestoreLayer4Callbacks"
- "uarpRestoreQueueName"
- "unsignedIntValue"
- "updateAppleProperty:siliconCtx:"
- "updateStagingProgressWithBytesSent:bytesTotal:"
- "updaterLog:"
- "updaterMode"
- "useLocalSigning"
- "v16@0:8"
- "v20@0:8C16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8I16I20"
- "v28@0:8I16^{_UARPSiliconContext=@^v^v{uarpRestoreCallbacks=^?^?}^{_uarpRestoreEndpoint}^v^v{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}I****{UARP4ccTag=CCCC}**Q^v}20"
- "v32@0:8@16*24"
- "v48@0:8@16@24^v32^{_UARPSiliconContext=@^v^v{uarpRestoreCallbacks=^?^?}^{_uarpRestoreEndpoint}^v^v{uarpRestoreLayer4Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}I****{UARP4ccTag=CCCC}**Q^v}40"
- "verboseLog:"

```
