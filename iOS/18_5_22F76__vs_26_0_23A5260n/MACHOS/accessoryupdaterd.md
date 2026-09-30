## accessoryupdaterd

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd`

```diff

-1207.120.19.0.0
-  __TEXT.__text: 0x53168
-  __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_stubs: 0x7640
-  __TEXT.__objc_methlist: 0x3b4c
+1338.0.21.0.2
+  __TEXT.__text: 0x51bb4
+  __TEXT.__auth_stubs: 0x10e0
+  __TEXT.__objc_stubs: 0x73c0
+  __TEXT.__objc_methlist: 0x3bfc
   __TEXT.__const: 0x400
-  __TEXT.__objc_methname: 0x901d
-  __TEXT.__cstring: 0x7ca4
+  __TEXT.__objc_methname: 0x9259
+  __TEXT.__cstring: 0x8474
   __TEXT.__objc_classname: 0x69e
   __TEXT.__objc_methtype: 0x1b3a
-  __TEXT.__oslogstring: 0x68e1
-  __TEXT.__gcc_except_tab: 0x548
+  __TEXT.__oslogstring: 0x66d8
+  __TEXT.__gcc_except_tab: 0x57c
   __TEXT.__dlopen_cstrs: 0xa4
-  __TEXT.__unwind_info: 0x1318
-  __DATA_CONST.__auth_got: 0x868
-  __DATA_CONST.__got: 0x3b8
+  __TEXT.__unwind_info: 0x12b0
+  __DATA_CONST.__auth_got: 0x880
+  __DATA_CONST.__got: 0x3c8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x15d8
-  __DATA_CONST.__cfstring: 0x57c0
+  __DATA_CONST.__const: 0x17a0
+  __DATA_CONST.__cfstring: 0x5820
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x178
-  __DATA_CONST.__objc_intobj: 0xf0
+  __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x92d8
-  __DATA.__objc_selrefs: 0x2340
-  __DATA.__objc_ivar: 0x538
+  __DATA.__objc_const: 0x9428
+  __DATA.__objc_selrefs: 0x2380
+  __DATA.__objc_ivar: 0x554
   __DATA.__objc_data: 0xf00
-  __DATA.__data: 0xb85
-  __DATA.__bss: 0x1290
+  __DATA.__data: 0xb45
+  __DATA.__bss: 0x1230
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 97A35D8D-8998-3E5E-B784-4C58282319F7
-  Functions: 2157
-  Symbols:   398
-  CStrings:  4272
+  UUID: F0E7A847-01AE-3DE3-BBB4-CC76AD11896E
+  Functions: 2112
+  Symbols:   403
+  CStrings:  4341
 
Symbols:
+ _InternalStorageDirectoryPath
+ _currentTrainName
+ _kUARPAssetLocationTypeMobileAssetServerAirPodsDeveloperSeed
+ _kUARPAssetLocationTypeMobileAssetServerAirPodsPublicSeed
+ _kUARPServicePersonalization
+ _nullableObjectsEqual
+ _uarpVersionCompareStrings
- _CFMakeCollectable
- _OBJC_CLASS_$_NSUUID
CStrings:
+ "%s: <ROLE=%s> : Add Downstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>"
+ "%s: <ROLE=%s> : RemoveDownstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>"
+ "%s: ESPRESSO Corrupt Entry ? pBuffer = %p, pMsg = %p"
+ "%s: ESPRESSO:Bonus Message <type=0x%04x, length=x0x%04x, id=0x%04x>"
+ "%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>"
+ "%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too small ! expected <%u>, got <%u>"
+ "<ROLE=%s> ESPRESSO: UARP.LAYER2.RECV.MSG: Length too small <%u>"
+ "<ROLE=%s> UARP.LAYER2.DATA.RESP offset=0x%08x, requestedlength=%u"
+ "AUInternalSettingsPallasOptions"
+ "AUInternalSettingsPallasOptions.plist"
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
+ "Audience"
+ "Buffer Overflow"
+ "Buffer Would Overflow"
+ "CUSTOMER_AUDIENCE"
+ "CUSTOMER_SEED_AUDIENCE"
+ "CUSTOM_AUDIENCE"
+ "Clearing seed enablement for %{public}@"
+ "Comparing asset with version %@ / state %ld"
+ "Configure Pallas"
+ "Custom Audience"
+ "Custom Pallas Audience"
+ "Customer Audience"
+ "Customer Seed Audience"
+ "DEVELOPER_SEED"
+ "Data Request"
+ "Data Response"
+ "Developer Seed"
+ "Did not find an available asset for %{public}@. Falling back to Customer."
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
+ "Endpoint Bulk Information Request"
+ "Endpoint Bulk Information Request Ack"
+ "Endpoint Bulk Information Response"
+ "Endpoint Bulk Information Response Ack"
+ "Endpoint Component Discovery Request"
+ "Endpoint Component Discovery Response"
+ "Endpoint Discovery Request"
+ "Endpoint Discovery Response"
+ "INTERNAL_LIVEON_AUDIENCE"
+ "INTERNAL_STAGING"
+ "Information Request"
+ "Information Response"
+ "Internal Living On"
+ "Internal Staging"
+ "Internal Variant"
+ "Invalid EndpointID"
+ "MOBILE_ASSET_UNTESTED"
+ "Mobile Asset Untested"
+ "No Firmware Update Available"
+ "No Firmware Update Available Ack"
+ "Overriding fallback asset location for %{public}@ from %{public}@ to %{public}@"
+ "Pallas Enabled"
+ "Sync"
+ "T@\"NSObject<OS_dispatch_queue>\",N,V_queue"
+ "T@\"NSString\",R,V_mobileAssetModelNumber"
+ "T@\"NSString\",R,V_pallasAudienceOverride"
+ "TB,R,V_pallasInternalAssetVariant"
+ "TB,R,V_pallasSupportEnabled"
+ "TB,V_inTeardown"
+ "TQ,R,V_pallasAudience"
+ "Vendor Specific"
+ "Version Discovery Request"
+ "Version Discovery Response"
+ "_inTeardown"
+ "_mobileAssetModelNumber"
+ "_pallasAudience"
+ "_pallasAudienceOverride"
+ "_pallasInternalAssetVariant"
+ "_pallasSupportEnabled"
+ "absoluteString"
+ "com.apple.uarpassetmanager.settings"
+ "generateUARPCacheFilePath"
+ "inTeardown"
+ "isEqualToDictionary:"
+ "isFusingEqual:"
+ "mobileAssetCacheURLForRemoteURL"
+ "mobileAssetModelNumber"
+ "pallasAudience"
+ "pallasAudienceOverride"
+ "pallasInternalAsset"
+ "pallasInternalAssetVariant"
+ "pallasSupportEnabled"
+ "setInTeardown:"
+ "setMobileAssetModelNumber:"
+ "setPallasAudience:"
+ "setPallasAudienceOverride:"
+ "setPallasInternalAssetVariant:"
+ "setPallasSupportEnabled:"
+ "setQueue:"
+ "settingsFromSeedBuild"
+ "uarpMsgRecvDownstreamEndpointReachable"
+ "uarpMsgRecvDownstreamEndpointUnreachable"
+ "uarpMsgRecvDownstreamEndpointUnreachableAck"
+ "uarpPlatformEndpointRecvMessage"
+ "uarpTransmitEntryIsValidToSend"
- "$RC_RELEASE"
- "$SIDEBUILD_PARENT_TRAIN"
- "%@/%@-%c%c%c%c"
- "%@/%@/%@%@"
- "%@/AirPods2022Seed"
- "%s: Checking for firmware in directory %@"
- "%s: Failed to create power assertion %@ with error %d"
- "%s: Failed to release power assertion with error %d"
- "%s: Invalid powerAssertionID received from caller"
- ".uarp"
- "/var/db/accessoryupdater/uarp/"
- "<ROLE=%s> UARP.LAYER2.DATA.RESP Outstanding Data Request <%s>, offset=0x%08x, requestedlength=%u"
- "AirPods2022Seed"
- "AirPodsDeveloperSeed"
- "BOOL createPowerAssertion(NSString *__strong, IOPMAssertionID *)"
- "BOOL releasePowerAssertion(IOPMAssertionID)"
- "Cannot copy file, Source File does not exist: %@"
- "Comparing asset with version %@ / state %@"
- "CrystalF"
- "Directory for dynamic assets does not exist at %@"
- "Failed to close File Handle at %@ - %@"
- "Failed to copy File %@ to New Location: %@ - %@"
- "Failed to create File Handle at: %@ - %@"
- "Failed to create directory at %@"
- "Failed to create file at %@"
- "Failed to create file for dynamic asset %@ at %@"
- "Failed to find End of File to File Handle at %@ - %@"
- "Failed to write to File Handle at %@ - %@"
- "MADownloading"
- "MAInstalled"
- "MAInstalledNotInCatalog"
- "MAInstalledWithOs"
- "MAInvalid"
- "MANotPresent"
- "MARequiredByOs"
- "MAUnknown"
- "Removing Expired File at %@"
- "Successfully copied %@ to %@"
- "Unable to create File at: %@"
- "char1"
- "char2"
- "char3"
- "char4"
- "com.apple.uarp.stagingstatus."
- "com.apple.uarppersonalization"
- "componentsJoinedByString:"
- "contentsOfDirectoryAtPath:error:"
- "dataWithData:"
- "mobileAssetCacheFileURLForRemoteURL"
- "tag"
- "uarpFilepathForRemotePath"
- "uarpFirmwareForAccessory"
- "yyyy-MM-dd-hh-mm-ss"

```
