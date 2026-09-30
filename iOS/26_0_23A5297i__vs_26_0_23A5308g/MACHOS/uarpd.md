## uarpd

> `/usr/libexec/uarpd`

```diff

-1338.0.62.0.1
-  __TEXT.__text: 0x81a50
-  __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_stubs: 0x7800
-  __TEXT.__objc_methlist: 0x6728
-  __TEXT.__objc_methname: 0xb030
-  __TEXT.__objc_classname: 0x158e
-  __TEXT.__objc_methtype: 0x2599
+1338.0.72.0.0
+  __TEXT.__text: 0x83d10
+  __TEXT.__auth_stubs: 0x970
+  __TEXT.__objc_stubs: 0x78e0
+  __TEXT.__objc_methlist: 0x6988
+  __TEXT.__objc_methname: 0xb40a
+  __TEXT.__objc_classname: 0x162e
+  __TEXT.__objc_methtype: 0x2564
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x817b
-  __TEXT.__oslogstring: 0x5b19
+  __TEXT.__cstring: 0x8581
+  __TEXT.__oslogstring: 0x5c88
   __TEXT.__gcc_except_tab: 0x158
-  __TEXT.__unwind_info: 0x1a28
-  __DATA_CONST.__auth_got: 0x4a0
-  __DATA_CONST.__got: 0x470
-  __DATA_CONST.__const: 0xf40
-  __DATA_CONST.__cfstring: 0x41e0
-  __DATA_CONST.__objc_classlist: 0x490
+  __TEXT.__unwind_info: 0x1a50
+  __DATA_CONST.__auth_got: 0x4c8
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__const: 0xee0
+  __DATA_CONST.__cfstring: 0x4320
+  __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x478
-  __DATA_CONST.__objc_intobj: 0x3f0
+  __DATA_CONST.__objc_superrefs: 0x498
+  __DATA_CONST.__objc_intobj: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0xd018
-  __DATA.__objc_selrefs: 0x24b8
-  __DATA.__objc_ivar: 0x8e4
-  __DATA.__objc_data: 0x2da0
-  __DATA.__data: 0x4f0
-  __DATA.__bss: 0x11c0
+  __DATA.__objc_const: 0xd380
+  __DATA.__objc_selrefs: 0x2530
+  __DATA.__objc_ivar: 0x904
+  __DATA.__objc_data: 0x2ee0
+  __DATA.__data: 0x4e8
+  __DATA.__bss: 0x1178
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 0B1B624F-CBCC-3018-9E75-D01570B61070
-  Functions: 3036
-  Symbols:   203
-  CStrings:  4211
+  UUID: 794E0065-1C40-34C1-99B9-3A7302361AE7
+  Functions: 3066
+  Symbols:   207
+  CStrings:  4295
 
Symbols:
+ _MGCopyAnswer
+ _notify_cancel
+ _notify_post
+ _notify_register_check
+ _notify_set_state
- _NSFilePosixPermissions
CStrings:
+ "%s: Asset DENIED due to OS Version %@"
+ "%s: Asset is %sOK offer via OTA"
+ "%s: Check Asset offer rules %@"
+ "%s: Device Class cannot be queried"
+ "%s: Device Class is %@"
+ "%s: Event Folder Name for %@ is %@"
+ "%s: Failed to register for %s (%u)"
+ "%s: File for TMAP Database could not be created %@"
+ "%s: Minimum build is %@, asset qualifies for OS Build of %@"
+ "%s: Minimum build is %@, which is greater than or equal to OS Build of %@"
+ "%s: No minimum build for OS Build of %@"
+ "%s: OS Build Version cannot be queried"
+ "%s: OS Build Version is %@"
+ "%s: Unable to expand MTIC asset for processing"
+ "%s: Unable to init MTIC asset for processing"
+ "%s: Unable to init mtic"
+ "%s: failed to create directory %@ for event %@; %@"
+ "%s: reporting from database %@"
+ "%s: reporting from endpoint %@"
+ "%s: unknown staged firmware version"
+ "-[UARPAssetMTIC setupEventFolder:sysdiagnoseFolder:]"
+ "-[UARPHostEndpoint hostEndpointSupportsChargingChimeDebounce:]"
+ "-[UARPHostEndpoint hostEndpointSupportsHeySiri:]"
+ "-[UARPHostEndpoint hostEndpointSupportsJustSiri:]"
+ "-[UARPHostEndpoint hostEndpointSupportsVoiceAssist:]"
+ "-[UARPHostManager commonProcessMTIC:tmapSnapshot:]"
+ "-[UARPHostManager createTempFolderSysdiagnose:error:]"
+ "-[UARPHostManager createTempFolderSysdiagnoseApproved:error:]"
+ "-[UARPHostManager createTempFolderTMAPDatabase:error:]"
+ "-[UARPHostManager ensureTMAPDatabaseExists]"
+ "-[UARPHostManager iOSPreflightOfferRestriction:osBuildVersion:]"
+ "-[UARPHostManager macOSPreflightOfferRestriction:osBuildVersion:]"
+ "-[UARPHostManager preflightOfferRestrictionByOS:]"
+ "-[UARPHostManager preflightOfferRestrictions:]"
+ "-[UARPHostManager registerForNotifications]"
+ "-[UARPHostManager tvOSPreflightOfferRestriction:osBuildVersion:]"
+ "-[UARPHostManager visionOSPreflightOfferRestriction:osBuildVersion:]"
+ "-[UARPHostManager watchOSPreflightOfferRestriction:osBuildVersion:]"
+ "AllAMN.tmap"
+ "AppleTV"
+ "Assume no entries in TMAP Database at %@"
+ "B40@0:8@16@24^@32"
+ "BuildVersion"
+ "Coul not create TMAP mapping for Apple Model Numbers %@"
+ "Could not decode TMAP Database at %@"
+ "Could not initialize TMAP database"
+ "Could not initialize UUID database"
+ "Could not open TMAP Database at %@"
+ "Create not close TMAP Database; %@"
+ "Create not encode new entry for TMAP Database; %@"
+ "Create not open file for TMAP Database; %@"
+ "Create not truncate TMAP Database; %@"
+ "Create not write encoded data to TMAP Database; %@"
+ "DeviceClass"
+ "Failed to close File Handle at %@; error is %@"
+ "Failed to create File Handle at: %@; error is %@"
+ "Failed to write File Handle at %@; error is %@"
+ "Folder for TMAP Database could not be created %@"
+ "MTIC Payload has no event id TLV"
+ "MTIC Payload has no matching database entry"
+ "MTIC has no Payload Data"
+ "Mac"
+ "Minimum iOS Version"
+ "Minimum macOS Version"
+ "Minimum tvOS Version"
+ "Minimum visionOS Version"
+ "Minimum watchOS Version"
+ "NOT "
+ "Posting MTIC events to Core Analytics: %@"
+ "RealityDevice"
+ "T@\"NSString\",R,V_osVersion"
+ "TB,R,V_supportsChargingChimeDebounce"
+ "TB,R,V_supportsHeySiri"
+ "TB,R,V_supportsJustSiri"
+ "TB,R,V_supportsVoiceAssist"
+ "TMAP Data could not be serialized; error: %@"
+ "TMAP Data could not be unarchived; error: %@"
+ "TMAP Data not a dictionary"
+ "TMAP Endian must be String"
+ "UARPMetaDataHostMinimumVersion_iOS"
+ "UARPMetaDataHostMinimumVersion_macOS"
+ "UARPMetaDataHostMinimumVersion_tvOS"
+ "UARPMetaDataHostMinimumVersion_visionOS"
+ "UARPMetaDataHostMinimumVersion_watchOS"
+ "Unable to write JSON: %@"
+ "Watch"
+ "_mticQueue"
+ "_notifyTokenFirmwareUpdate"
+ "_notifyTokenUrgentFirmwareUpdate"
+ "_osVersion"
+ "_supportsChargingChimeDebounce"
+ "_supportsHeySiri"
+ "_supportsJustSiri"
+ "_supportsVoiceAssist"
+ "_sysdiagnoseApprovedFolder"
+ "_sysdiagnoseFolder"
+ "_tmapDatabaseFolder"
+ "_tmapDatabaseURL"
+ "asyncProcessMTIC:"
+ "com.apple.accessoryUpdater.uarp.firmareUpdateApplied"
+ "com.apple.accessoryUpdater.uarp.urgentFirmwareUpdateApplied"
+ "com.apple.uarp.uarpd.manager.mtic"
+ "commonProcessMTIC:tmapSnapshot:"
+ "contributeSysdiagnoseMetrics:eventFileURL:"
+ "createTempFolderSysdiagnose:error:"
+ "createTempFolderSysdiagnoseApproved:error:"
+ "createTempFolderTMAPDatabase:error:"
+ "ensureTMAPDatabaseExists"
+ "flushTMAPDatabase"
+ "hostEndpointSupportsChargingChimeDebounce:"
+ "hostEndpointSupportsHeySiri:"
+ "hostEndpointSupportsJustSiri:"
+ "hostEndpointSupportsVoiceAssist:"
+ "iOSPreflightOfferRestriction:osBuildVersion:"
+ "iPad"
+ "iPhone"
+ "ingestTMAPPayloads:"
+ "loadTMAPDatabase"
+ "macOSPreflightOfferRestriction:osBuildVersion:"
+ "osVersion"
+ "postNotificationFirmwareUpdate"
+ "postNotificationUrgentFirmwareUpdate"
+ "postToCoreAnalytics"
+ "preflightOfferRestrictionByOS:"
+ "preflightOfferRestrictions:"
+ "prepareEventForSysdiagnose:sysdiagnoseFolder:"
+ "prepareForSysdiagnose:"
+ "processAsset:tmapSnapshot:"
+ "processMTIC:"
+ "registerForNotifications"
+ "removeObjectForKey:"
+ "setupEventFolder:sysdiagnoseFolder:"
+ "supportsChargingChimeDebounce"
+ "supportsHeySiri"
+ "supportsJustSiri"
+ "supportsVoiceAssist"
+ "tmapDatabase.plist"
+ "tvOSPreflightOfferRestriction:osBuildVersion:"
+ "visionOSPreflightOfferRestriction:osBuildVersion:"
+ "watchOSPreflightOfferRestriction:osBuildVersion:"
+ "writeSysdiagnoseMetrics:fileHandle:error:"
- "%@/%@"
- "%s: Decomposing UARP asset containing TMAP payload %@"
- "%s: Failed to expand MTIC"
- "%s: Finding and adding TMAP database entries if exists in asset %@"
- "%s: Missing matching TMAP, saving for later"
- "%s: Unable to create file at %@"
- "%s: Unable to remove files at %@ (%@)"
- "+[UARPAssetMTIC processAssetURL:tempFolderPath:]"
- "+[UARPAssetMTIC processAssetURL:tempFolderPath:]_block_invoke"
- "+[UARPMappedAnalyticsDatabase addEntries:tempFolderPath:]"
- "-[UARPMappedAnalyticsDatabase cleanUpTmapDatabaseFiles]"
- "-[UARPMappedAnalyticsDatabase createTmapDatabaseFile]"
- "@\"UARPMappedAnalyticsDatabase\""
- "@\"UARPSuperBinaryLayer3\""
- "All MTIC data for this asset: %@"
- "B32@0:8^I16@24"
- "Cannot expand SuperBinary"
- "Could not add TMAP mapping"
- "Decomposing TMAP from asset located at %@"
- "Failed to close File Handle at %@ - %@"
- "Failed to create File Handle at: %@ - %@"
- "Failed to decompose MTIC"
- "Failed to expand MTIC payloads"
- "Failed to find End of File to File Handle at %@ - %@"
- "Failed to set permission for location %@: %@"
- "Failed to write to File Handle at %@ - %@"
- "MTIC has no Payload Data: %@"
- "Mapped Analytics Event %@\n"
- "Mapped Analytics Payload %@\n"
- "No TMAP Mapping to match Apple Model Number."
- "Process MTIC Apple Model Number tlv is not of type UARPMetaDataMappedAnalyticsAppleModelNumber"
- "Process MTIC Apple Model Number tlv is not on payload"
- "Process MTIC Event ID tlv is not of type UARPMetaDataMappedAnalyticsEventID"
- "Process MTIC Event ID tlv is not on payload"
- "TMAP Data is nil or not a dictionary: TMAP Value: %@, Error: %@"
- "TMAP Endian must be String."
- "Tmap Database File exists on disk, but unable to find Tmap Database URL"
- "UARPMappedAnalyticsDatabase"
- "Unable to create File at: %@"
- "Unable to create directory at %@ with %@"
- "Unable to expand Data"
- "Unable to find Matching TMAP for Apple Model Number: %@"
- "Unable to find TMAP Database - cannot expand MTIC Payloads"
- "_asset"
- "_plistURL"
- "addEntries:tempFolderPath:"
- "addSysdiagnoseMetrics:coreAnalyticsEvent:"
- "cleanUpTmapDatabaseFiles"
- "componentsJoinedByString:"
- "createTmapDatabaseFile"
- "decomposeUARP:"
- "dictionaryWithContentsOfFile:"
- "expandMTICPayloads"
- "expandMticData:withEventID:appleModelNumber:"
- "findMatchingTMAP"
- "findTmapDatabaseFileUrl"
- "flushToDisk"
- "getAppleModelNumber:inPayload:"
- "getEventID:inPayload:"
- "initTmapDatabase:"
- "initTmapDatabaseWithPlist:"
- "loadPlist"
- "prepareAndSend:"
- "processAssetURL:tempFolderPath:"
- "setString:"
- "tmapDatabaseFileExists"
- "writeToURL:atomically:"

```
