## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/Versions/A/SoftwareUpdateCore`

```diff

-2171.101.1.0.0
-  __TEXT.__text: 0xaa8e8
+2171.120.23.501.1
+  __TEXT.__text: 0xaaf70
   __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_methlist: 0x7294
+  __TEXT.__objc_methlist: 0x72ac
   __TEXT.__const: 0x118
-  __TEXT.__cstring: 0x14222
-  __TEXT.__oslogstring: 0xac7f
+  __TEXT.__cstring: 0x14240
+  __TEXT.__oslogstring: 0xad2a
   __TEXT.__gcc_except_tab: 0x6d4
   __TEXT.__unwind_info: 0x15d0
   __TEXT.__objc_classname: 0x6d5
-  __TEXT.__objc_methname: 0x13fd7
+  __TEXT.__objc_methname: 0x1405b
   __TEXT.__objc_methtype: 0xec2
-  __TEXT.__objc_stubs: 0xd780
+  __TEXT.__objc_stubs: 0xd7c0
   __DATA_CONST.__got: 0x810
   __DATA_CONST.__const: 0x13b0
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f00
+  __DATA_CONST.__objc_selrefs: 0x3f10
   __DATA_CONST.__objc_superrefs: 0x1b0
   __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x350
   __AUTH_CONST.__const: 0x1220
   __AUTH_CONST.__cfstring: 0x11e80
-  __AUTH_CONST.__objc_const: 0x9cb0
+  __AUTH_CONST.__objc_const: 0x9ce0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH.__objc_data: 0x11d0
-  __DATA.__objc_ivar: 0x8f4
+  __DATA.__objc_ivar: 0x8f8
   __DATA.__data: 0x360
   __DATA.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2847
-  Symbols:   6701
-  CStrings:  6174
+  Functions: 2849
+  Symbols:   6706
+  CStrings:  6180
 
Symbols:
+ -[SUCorePolicy mobileAssetPurposeOverride]
+ -[SUCorePolicy setMobileAssetPurposeOverride:]
+ OBJC_IVAR_$_SUCorePolicy._mobileAssetPurposeOverride
+ __127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.636
+ __127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.637
+ __127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke_2.640
+ __79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.606
+ __79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.610
+ __79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke_2.613
+ __block_literal_global.612
+ __block_literal_global.635
+ __block_literal_global.639
+ _objc_msgSend$mobileAssetPurposeOverride
+ _objc_msgSend$setMobileAssetPurposeOverride:
- __127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.630
- __127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.634
- __127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke_2.637
- __79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.603
- __79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.604
- __79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke_2.610
- __block_literal_global.609
- __block_literal_global.632
- __block_literal_global.636
CStrings:
+ "\n[>>>\n    SubPolicies(specifiedUsedPolicies:0x%llX)\n%@    AssetTypes(softwareUpdateAssetType:%@|documentationAssetType:%@)\n    Versions(prerequisiteBuildVersion:%@|prerequisiteProductVersion:%@|prerequisiteRestoreVersion:%@|targetRestoreVersion:%@|installedSFRVersion:%@)\n    Device(deviceClass:%@|hwModelStr:%@|productType:%@|releaseType:%@|isInternal:%@)\n    Config(restrictToFull:%@|allowSameVersion:%@|background:%@|allowsCellular:%@|checkAvailableSpace:%@|cacheDeleteUrgency:%@|userAgentString:%@|userInitiated:%@|skipVolumeSealing:%@|qualityOfService:%@)\n    Target(targetVolumeUUID:%@|updateVolumePath:%@)\n    Preflight(performPreflightEncryptedCheck:%@|performPreflightSnapshotCheck:%@|updateBrainLocationOverride:%@)\n    Personalization(SSOToken:%@|personalizedManifestRootsPath:%@|personalizationServerURL:%@|proxyHostName:%@|proxyPortNumber:%@)\n    Authentication(localAuthenticationContext:%@|downloadAuthorizationHeader:%@|localAuthenticationUserID:%@|mdmBootstrapToken:%@)\n    BridgeOS(bridgeOSIgnoreMinimumVersionCheck:%@|bridgeOSDownloadDirectory:%@|enableEmbeddedOSInstall:%@|enableBridgeOSInstall:%@|enableOSPersonalization:%@)\n    Metrics(updateMetricEventFields:%@|updateMetricContext:%@\n    Defaults(defaultDescriptorValues:%@|assetAudienceUUID:%@|alternateAssetAudienceUUID:%@|disableAlternateUpdate:%@|disableSplombo:%@|mobileAssetPurposeOverride:%@)\n    PSUS(enable:%@|enableForOptionalAssets:%@)\n    Extensions(%@)\n<<<]"
+ "%{public}@ SU metadata query using mobileAssetPurposeOverride as purpose: %{public}@"
+ "%{public}@ doc metadata query using mobileAssetPurposeOverride as purpose: %{public}@"
+ "T@\"NSString\",&,N,V_mobileAssetPurposeOverride"
+ "_\x0f\x0f\x02"
+ "_mobileAssetPurposeOverride"
+ "mobileAssetPurposeOverride"
+ "setMobileAssetPurposeOverride:"
- "\n[>>>\n    SubPolicies(specifiedUsedPolicies:0x%llX)\n%@    AssetTypes(softwareUpdateAssetType:%@|documentationAssetType:%@)\n    Versions(prerequisiteBuildVersion:%@|prerequisiteProductVersion:%@|prerequisiteRestoreVersion:%@|targetRestoreVersion:%@|installedSFRVersion:%@)\n    Device(deviceClass:%@|hwModelStr:%@|productType:%@|releaseType:%@|isInternal:%@)\n    Config(restrictToFull:%@|allowSameVersion:%@|background:%@|allowsCellular:%@|checkAvailableSpace:%@|cacheDeleteUrgency:%@|userAgentString:%@|userInitiated:%@|skipVolumeSealing:%@|qualityOfService:%@)\n    Target(targetVolumeUUID:%@|updateVolumePath:%@)\n    Preflight(performPreflightEncryptedCheck:%@|performPreflightSnapshotCheck:%@|updateBrainLocationOverride:%@)\n    Personalization(SSOToken:%@|personalizedManifestRootsPath:%@|personalizationServerURL:%@|proxyHostName:%@|proxyPortNumber:%@)\n    Authentication(localAuthenticationContext:%@|downloadAuthorizationHeader:%@|localAuthenticationUserID:%@|mdmBootstrapToken:%@)\n    BridgeOS(bridgeOSIgnoreMinimumVersionCheck:%@|bridgeOSDownloadDirectory:%@|enableEmbeddedOSInstall:%@|enableBridgeOSInstall:%@|enableOSPersonalization:%@)\n    Metrics(updateMetricEventFields:%@|updateMetricContext:%@\n    Defaults(defaultDescriptorValues:%@|assetAudienceUUID:%@|alternateAssetAudienceUUID:%@|disableAlternateUpdate:%@|disableSplombo:%@)\n    PSUS(enable:%@|enableForOptionalAssets:%@)\n    Extensions(%@)\n<<<]"
- "_\x0f\x0f\x01"

```
