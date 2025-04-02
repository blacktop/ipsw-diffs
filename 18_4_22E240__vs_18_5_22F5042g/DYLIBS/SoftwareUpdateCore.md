## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2171.100.143.0.0
-  __TEXT.__text: 0x9e7a0
+2171.120.23.0.2
+  __TEXT.__text: 0x9ece0
   __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x7654
+  __TEXT.__objc_methlist: 0x766c
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x1477d
-  __TEXT.__oslogstring: 0xb67c
+  __TEXT.__cstring: 0x1479b
+  __TEXT.__oslogstring: 0xb727
   __TEXT.__gcc_except_tab: 0x6e0
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__unwind_info: 0x16b0
   __TEXT.__objc_classname: 0x700
-  __TEXT.__objc_methname: 0x149f5
+  __TEXT.__objc_methname: 0x14a79
   __TEXT.__objc_methtype: 0xf19
-  __TEXT.__objc_stubs: 0xe2a0
+  __TEXT.__objc_stubs: 0xe2e0
   __DATA_CONST.__got: 0x870
   __DATA_CONST.__const: 0x2200
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x41b8
+  __DATA_CONST.__objc_selrefs: 0x41c8
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x460
   __AUTH_CONST.__const: 0x460
   __AUTH_CONST.__cfstring: 0x12260
-  __AUTH_CONST.__objc_const: 0xa130
+  __AUTH_CONST.__objc_const: 0xa160
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x93c
+  __DATA.__objc_ivar: 0x940
   __DATA.__data: 0x360
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0xc80

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2919
-  Symbols:   3893
-  CStrings:  6352
+  Functions: 2921
+  Symbols:   3895
+  CStrings:  6358
 
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
