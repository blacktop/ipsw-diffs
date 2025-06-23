## uarpd

> `/usr/libexec/uarpd`

```diff

-1338.0.21.0.2
-  __TEXT.__text: 0x74658
+1338.0.37.0.0
+  __TEXT.__text: 0x7a814
   __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__objc_stubs: 0x6e80
-  __TEXT.__objc_methlist: 0x5de0
-  __TEXT.__objc_methname: 0xa145
-  __TEXT.__objc_classname: 0x1458
-  __TEXT.__objc_methtype: 0x21ec
-  __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x6f25
-  __TEXT.__oslogstring: 0x4a71
-  __TEXT.__gcc_except_tab: 0xfc
-  __TEXT.__unwind_info: 0x1800
+  __TEXT.__objc_stubs: 0x7320
+  __TEXT.__objc_methlist: 0x61e0
+  __TEXT.__objc_methname: 0xa837
+  __TEXT.__objc_classname: 0x14c9
+  __TEXT.__objc_methtype: 0x2373
+  __TEXT.__const: 0x128
+  __TEXT.__cstring: 0x772c
+  __TEXT.__oslogstring: 0x51f9
+  __TEXT.__gcc_except_tab: 0x144
+  __TEXT.__unwind_info: 0x1918
   __DATA_CONST.__auth_got: 0x488
-  __DATA_CONST.__got: 0x438
-  __DATA_CONST.__const: 0xda0
-  __DATA_CONST.__cfstring: 0x3240
-  __DATA_CONST.__objc_classlist: 0x448
+  __DATA_CONST.__got: 0x450
+  __DATA_CONST.__const: 0xd98
+  __DATA_CONST.__cfstring: 0x33a0
+  __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x430
+  __DATA_CONST.__objc_superrefs: 0x448
   __DATA_CONST.__objc_intobj: 0x3c0
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0xc168
-  __DATA.__objc_selrefs: 0x2178
-  __DATA.__objc_ivar: 0x824
-  __DATA.__objc_data: 0x2ad0
+  __DATA.__objc_const: 0xc500
+  __DATA.__objc_selrefs: 0x22f8
+  __DATA.__objc_ivar: 0x848
+  __DATA.__objc_data: 0x2bc0
   __DATA.__data: 0x4f0
   __DATA.__bss: 0x11c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: B4C594F1-B1B4-301A-B18E-BFD0CDFBD242
-  Functions: 2806
+  UUID: 868DD569-C117-3412-B0EA-AA8C3FE2FECE
+  Functions: 2908
   Symbols:   199
-  CStrings:  3652
+  CStrings:  3825
 
CStrings:
+ "%@.uarp"
+ "%s: Add Personalizing Asset %@ for %@"
+ "%s: Add Staging Asset %@ for %@"
+ "%s: Added Dynamic Asset - %@"
+ "%s: Added Personalized Asset - %@"
+ "%s: Added Personalizing Asset - %@"
+ "%s: Assets for Endpoint %@"
+ "%s: Caching Asset - %@"
+ "%s: Caching Controller Asset <%@>"
+ "%s: Caching Controller Asset <%@>, appending %lu bytes of data"
+ "%s: Check Asset Manager for %@"
+ "%s: Could not find Personalizing Asset %@ for %@"
+ "%s: Create not encode UUID Database; %@"
+ "%s: Dynamic Asset - %@"
+ "%s: File for UARP Endpoint Database could not be created %@"
+ "%s: Finish Caching Controller Asset <%@>"
+ "%s: Firmware Asset %@ for %@"
+ "%s: Firmware Personalization already in progress for endpoint %@ skipping"
+ "%s: Firmware Staging already in progress for endpoint %@ skipping"
+ "%s: Moving Personalizing Asset to Personalized %@ for %@"
+ "%s: Pause Asset Manager for %@"
+ "%s: Personalized Asset %@ for %@"
+ "%s: Personalizing Asset %@ for %@"
+ "%s: Remove Staging Asset %@ for %@"
+ "%s: Removed Personalizing Asset - %@"
+ "%s: Resume Asset Manager for %@"
+ "%s: Updated via available asset notification"
+ "%s: asset length is zero for %@"
+ "%s: assetUUID not found %@"
+ "%s: attributes is nil for %@"
+ "%s: could not append to caching asset %@"
+ "%s: could not finalize caching asset %@"
+ "%s: could not get url for caching asset %@"
+ "%s: could not prepare caching asset %@"
+ "%s: deviceUUID is %@, release transport immediately"
+ "%s: deviceUUID is %@, transfers still in progress"
+ "%s: hash does not match for %@"
+ "%s: readDataUpToLength:error: failed with %@"
+ "-[UARPEndpointControllerInternal endpointControllerCacheAsset:assetUUID:appendData:reply:]"
+ "-[UARPEndpointControllerInternal endpointControllerCacheAssetFinish:assetUUID:hashData:reply:]"
+ "-[UARPEndpointControllerInternal endpointControllerCacheAssetStart:assetUUID:reply:]"
+ "-[UARPEndpointControllerInternal endpointControllerPullDynamicAsset:assetUUID:range:reply:]"
+ "-[UARPEndpointControllerInternal endpointControllerPullDynamicAssetFinish:assetUUID:hashData:reply:]"
+ "-[UARPEndpointControllerInternal endpointControllerPullDynamicAssetStart:assetUUID:reply:]"
+ "-[UARPEndpointControllerInternal endpointControllerQueryEncodedMappingDatabase:]"
+ "-[UARPEndpointLayer3 personalizeFirmwareAssetComplete:tssResponse:]_block_invoke"
+ "-[UARPEndpointLayer3 personalizeFirmwareSuperBinaryInternal:tssServerURL:]"
+ "-[UARPHostEndpoint personalizationComplete:]"
+ "-[UARPHostEndpoint personalizeFirmware:tssServerURL:]"
+ "-[UARPHostEndpoint showAllAssets]"
+ "-[UARPHostEndpoint stageFirmware:tssServerURL:]"
+ "-[UARPHostEndpoint stageFirmwareComplete:]"
+ "-[UARPHostManager appendDataToCachingAsset:data:]"
+ "-[UARPHostManager checkAssetManager:]"
+ "-[UARPHostManager checkAssetManager:]_block_invoke"
+ "-[UARPHostManager clearDatabase]"
+ "-[UARPHostManager createTempFolderAnalyticsAssets:error:]"
+ "-[UARPHostManager createTempFolderAssets:error:]"
+ "-[UARPHostManager createTempFolderCachedAssets:error:]"
+ "-[UARPHostManager createTempFolderCrashAssets:error:]"
+ "-[UARPHostManager createTempFolderHeySiriAssets:error:]"
+ "-[UARPHostManager createTempFolderLogsAssets:error:]"
+ "-[UARPHostManager createTempFolderMappedAnalyticsAssets:error:]"
+ "-[UARPHostManager createTempFolderPacketCaptures:error:]"
+ "-[UARPHostManager createTempFolderVoiceAssistAssets:error:]"
+ "-[UARPHostManager dataRangeFromDynamicAsset:range:]"
+ "-[UARPHostManager ensureDatabaseExists]"
+ "-[UARPHostManager pauseAssetManager:]"
+ "-[UARPHostManager pauseAssetManager:]_block_invoke"
+ "-[UARPHostManager resumeAssetManager:]"
+ "-[UARPHostManager resumeAssetManager:]_block_invoke"
+ "-[UARPHostManager showAllAssets]"
+ "@40@0:8@16{_NSRange=QQ}24"
+ "Active Firmware Version: %@ -> %@"
+ "Apple Model Number : %@ -> %@"
+ "Asset %@ for %@ to endpoint %@\n"
+ "Available Firmware Version: %@ -> %@"
+ "Caching Controller Asset <%@> to %@"
+ "Could not create superbinary for %@ to endpoint %@\n"
+ "Could not verify hash for asset <%@> to %@"
+ "Could not verify hash for controller cached asset <%@> to %@"
+ "Crash Analytics Apple Model Number"
+ "Crash Analytics Core Name"
+ "Crash Analytics Test Mode"
+ "Create not create superbinary <%@> for cached asset"
+ "Create not find caching asset <%@>"
+ "Create not find dynamic asset <%@>"
+ "Create not open file <%@> for cached asset; %@"
+ "Create not open file <%@> for dynamic asset; %@"
+ "File for cached asset <%@> could not be created %@"
+ "HSML"
+ "Hardware Fusing: %@ -> %@"
+ "Ignore Asset Manager Notification, Paused"
+ "Need to Personalize Asset %@ for endpoint %@\n"
+ "Process Asset Manager Notification"
+ "Serial Number : %@ -> %@"
+ "Stage and Apply Asset %@ to endpoint %@\n"
+ "T@\"NSData\",C,V_ecidData"
+ "T@\"NSString\",R,V_coreName"
+ "TC,R,V_testMode"
+ "TICS"
+ "TVAS"
+ "UARPMetaDataCrashAnalyticsAppleModelNumber"
+ "UARPMetaDataCrashAnalyticsCoreName"
+ "UARPMetaDataCrashAnalyticsTestMode"
+ "UUID : %@ -> %@"
+ "Verified hash for asset <%@> to %@"
+ "Verified hash for controller cached asset <%@> to %@"
+ "_cachedAssetsFolder"
+ "_cachingAssets"
+ "_coreName"
+ "_ecidData"
+ "_heySiriAssetsFolder"
+ "_mappedAnalyticsAssetsFolder"
+ "_pauseAssetManagerNotifications"
+ "_testMode"
+ "_voiceAssistAssetsFolder"
+ "appendDataToCachingAsset:data:"
+ "cachedassets"
+ "checkAssetManager:"
+ "clearAssetFolders"
+ "clearPacketCaptures"
+ "coreName"
+ "createTempFolderAnalyticsAssets:error:"
+ "createTempFolderAssets:error:"
+ "createTempFolderCachedAssets:error:"
+ "createTempFolderCrashAssets:error:"
+ "createTempFolderHeySiriAssets:error:"
+ "createTempFolderLogsAssets:error:"
+ "createTempFolderMappedAnalyticsAssets:error:"
+ "createTempFolderPacketCaptures:error:"
+ "createTempFolderVoiceAssistAssets:error:"
+ "dataRangeFromDynamicAsset:range:"
+ "device/assets/heysiri"
+ "device/assets/mappedanalytics"
+ "device/assets/voiceassist"
+ "ecidData"
+ "endpointControllerCacheAsset:assetUUID:appendData:reply:"
+ "endpointControllerCacheAssetFinish:assetUUID:hashData:reply:"
+ "endpointControllerCacheAssetStart:assetUUID:reply:"
+ "endpointControllerCheckAssetManager:"
+ "endpointControllerClearAssets"
+ "endpointControllerClearDatabase"
+ "endpointControllerClearPacketCaptures"
+ "endpointControllerPauseAssetManagerNotifications:reply:"
+ "endpointControllerPullDynamicAsset:assetUUID:range:reply:"
+ "endpointControllerPullDynamicAssetFinish:assetUUID:hashData:reply:"
+ "endpointControllerPullDynamicAssetStart:assetUUID:reply:"
+ "endpointControllerQueryEncodedMappingDatabase:"
+ "endpointControllerResumeAssetManagerNotifications:reply:"
+ "finalizeTransferCachingAsset:hashData:error:"
+ "finalizeTransferDynamicAsset:hashData:error:"
+ "findCachingAssetByUUID:"
+ "monitorForDevices:"
+ "pauseAssetManager:"
+ "personalizationComplete:"
+ "personalizationInProgress"
+ "personalizeFirmware:tssServerURL:"
+ "prepareCachingAsset:"
+ "resumeAssetManager:"
+ "setEcidData:"
+ "showAllAssets"
+ "stageFirmware:tssServerURL:"
+ "stageFirmwareComplete:"
+ "stagingInProgress"
+ "testMode"
+ "transfersInProgress"
+ "urlForCachingAsset:"
+ "urlForDynamicAsset:"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"NSData\">16"
+ "v32@0:8@\"NSUUID\"16@?<v@?B>24"
+ "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@?<v@?B>32"
+ "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@?<v@?BQ>32"
+ "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSData\"32@?<v@?B>40"
+ "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSData\"32@?<v@?B@\"NSURL\">40"
+ "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSURL\"32@?<v@?@\"NSNumber\">40"
+ "v56@0:8@\"NSUUID\"16@\"NSUUID\"24{_NSRange=QQ}32@?<v@?B@\"NSData\">48"
+ "v56@0:8@16@24{_NSRange=QQ}32@?48"
+ "verifyHash:url:error:"
- "%s: After updating with available asset notification"
- "%s: Before updating with available asset notification"
- "%s: endpointUUID is %@, assetUUID is %@, dynamicAssetURL is %@"
- "-[UARPEndpointControllerInternal endpointControllerExportDynamicAsset:endpointUUID:dynamicAssetURL:reply:]"
- "-[UARPHostManager createTempFolders:]"
- "Active Firmware Version: %@"
- "Apple Model Number : %@"
- "Available Firmware Version: %@"
- "File for UARP Endpoint Database could not be created %@"
- "Hardware Fusing: %@"
- "Need to Personalize Asset %s for endpoint %s\n"
- "Serial Number : %@"
- "Stage and Apply Asset %s to endpoint %s\n"
- "T@\"NSData\",C,V_ECIDData"
- "UUID : %@"
- "_ECIDData"
- "setECIDData:"
- "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSURL\"32@?<v@?B>40"

```
