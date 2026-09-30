## SoftwareUpdateController

> `/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController`

```diff

-166.100.3.0.0
-  __TEXT.__text: 0xd268
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0x14dc
-  __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x3292
-  __TEXT.__oslogstring: 0x17
+166.120.3.0.0
+  __TEXT.__text: 0xf118
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_methlist: 0x155c
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x38bc
+  __TEXT.__oslogstring: 0xcb
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0x330
-  __TEXT.__objc_classname: 0x13a
-  __TEXT.__objc_methname: 0x3f55
-  __TEXT.__objc_methtype: 0xd4a
-  __TEXT.__objc_stubs: 0x2060
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x360
-  __DATA_CONST.__objc_classlist: 0x58
+  __TEXT.__unwind_info: 0x358
+  __TEXT.__objc_classname: 0x14d
+  __TEXT.__objc_methname: 0x44b2
+  __TEXT.__objc_methtype: 0xd58
+  __TEXT.__objc_stubs: 0x2b20
+  __DATA_CONST.__got: 0x228
+  __DATA_CONST.__const: 0x3b8
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd20
+  __DATA_CONST.__objc_selrefs: 0xf08
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x378
+  __DATA_CONST.__objc_arraydata: 0x8
+  __AUTH_CONST.__auth_got: 0x388
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x2360
-  __AUTH_CONST.__objc_const: 0x24a8
+  __AUTH_CONST.__cfstring: 0x2ac0
+  __AUTH_CONST.__objc_const: 0x2568
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x1c0
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH.__objc_data: 0x3c0
+  __DATA.__objc_ivar: 0x1c4
   __DATA.__data: 0x348
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
+  - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
+  - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
   - /System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 407
-  Symbols:   651
-  CStrings:  1158
+  Functions: 421
+  Symbols:   687
+  CStrings:  1288
 
Symbols:
+ _ASAttributeDownloadSize
+ _ASAttributeUnarchivedSize
+ _MAGetPallasAudience
+ _MAPurgeCatalogsWithPurpose
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_SUControllerSUCore
+ _OBJC_CLASS_$_SUCoreLog
+ _OBJC_CLASS_$_SUCorePolicy
+ _OBJC_CLASS_$_SUCoreScan
+ _OBJC_METACLASS_$_SUControllerSUCore
+ _kCFErrorDomainMobileSoftwareUpdate
+ _kCFErrorDomainPersonalization
+ _kSUAssetMandatoryUpdateEligibleKey
+ _kSUAssetMandatoryUpdateOptionalKey
+ _kSUAssetMandatoryUpdateRestrictedToOutOfTheBoxKey
+ _kSUAssetMandatoryUpdateVersionMaxKey
+ _kSUAssetMandatoryUpdateVersionMinKey
+ _kSUAssetRampKey
+ _kSUAssetTypeSoftwareUpdate
+ _kSUAssetTypeUpdateDocumentation
+ _kSUControllerLogMILESTONE
+ _kSUCoreErrorDomain
CStrings:
+ "-[SUControllerManager paramsForOTAScans:]"
+ "-[SUControllerManager scanForUpdatesFromNonTVOSDevice:completion:]_block_invoke_2"
+ "4"
+ "@\"SUCoreScan\""
+ "AllowSameVersion"
+ "AssetAudienceUUID"
+ "Build"
+ "Device is update to date.  No update found."
+ "DeviceClass"
+ "Failed to purged catalog for %@.  Error: %@"
+ "Failed to scan for update"
+ "HWModelStr"
+ "IsInternal"
+ "MA audience: %@"
+ "MSU operation failed"
+ "MobileAsset error"
+ "MobileSoftwareUpdate operation failed"
+ "MobileSoftwareUpdate personalization failed"
+ "OSVersion"
+ "PrerequisiteBuild"
+ "PrerequisiteBuildVersion"
+ "PrerequisiteOSVersion"
+ "PrerequisiteProductVersion"
+ "PrerequisiteRestoreVersion"
+ "ProductType"
+ "Provided scan parameter dictionary is missing required parameter for scanning: %@"
+ "ReleaseType"
+ "RestrictToFull"
+ "SUCCESS"
+ "SUControllerSUCore"
+ "SUCore error with no equivalent SUController error"
+ "SUCore underlying error indicating no error"
+ "SUProductSystemName"
+ "SUPublisher"
+ "Scan completed without errors, but primaryUpdateAsset is nil"
+ "Successfully purged catalog for %@"
+ "T@\"SUCoreScan\",&,N,V_scanner"
+ "UUID"
+ "UUIDString"
+ "[DESCRIPTOR_FROM_CORE] SUCore descriptor is missing documentation information"
+ "[DESCRIPTOR_FROM_CORE] SUCore descriptor is missing documentation information, allowed for %@ devices"
+ "[__MILESTONE__]"
+ "_scanner"
+ "allocation failed"
+ "already in progress"
+ "assetAudienceUUID"
+ "attributes"
+ "bad argument"
+ "buildVersion"
+ "cleanProductVersion:"
+ "com.apple.MobileAsset.SoftwareUpdate"
+ "connection error"
+ "created scan params: %@"
+ "delayPeriodDays"
+ "domain"
+ "domain=%@, code=%llu, description=%@"
+ "download failed"
+ "errorFromCoreError:"
+ "expected an SUCore underlying error"
+ "failed disk space check"
+ "getMADocumentationAsset"
+ "getMASoftwareUpdateAsset"
+ "hwModelStr"
+ "hwModelString"
+ "initWithSoftwareUpdateAssetType:documentationAssetType:usingPolicies:usingExtensions:"
+ "initWithUUID:"
+ "insufficient disk space"
+ "internal error"
+ "invalid state for operation"
+ "isBootedOSSecureInternal"
+ "isInternal"
+ "isRequestedPMVSupervisedPolicy"
+ "localizedDescription"
+ "locateAvailableUpdateWithPolicy:completion:"
+ "malformed message"
+ "missing required element"
+ "mobileAssetPurposeOverride"
+ "newDescriptorFromAsset:"
+ "newDescriptorFromCoreDescriptor:corePolicy:"
+ "newProgressFromCoreProgress:"
+ "newSafeErrorDescription:"
+ "newer update found"
+ "no documentation found"
+ "not supported"
+ "numToBool:"
+ "operation abandoned"
+ "operation canceled"
+ "oslog"
+ "paramsForOTAScans:"
+ "prerequisiteRestoreVersion"
+ "productType"
+ "purge failed"
+ "query failed"
+ "requestedProductMarketingVersion"
+ "restoreVersion"
+ "safeBooleanForKey:"
+ "safeObjectForKey:ofClass:"
+ "safeStringForKey:"
+ "safeULLForKey:"
+ "scan postponed"
+ "scanForUpdatesFromNonTVOSDevice:completion:"
+ "scanner"
+ "setAdditionalOptions:"
+ "setAdditionalServerParams:"
+ "setAllowSameVersion:"
+ "setAllowsCellular:"
+ "setAssetAudienceUUID:"
+ "setDeviceClass:"
+ "setDiscretionary:"
+ "setDownloadTimeoutSecs:"
+ "setEnablePreSUStaging:"
+ "setEnablePreSUStagingForOptionalAssets:"
+ "setHwModelStr:"
+ "setIsInternal:"
+ "setMobileAssetPurposeOverride:"
+ "setPrerequisiteRestoreVersion:"
+ "setProductType:"
+ "setRampingScanType:"
+ "setRequiresPowerPluggedIn:"
+ "setRestrictToFull:"
+ "setRestrictToIncremental:"
+ "setSafeObject:forKey:"
+ "setScanner:"
+ "setSessionId:"
+ "softwareUpdateScanPolicy"
+ "transport related error"
+ "tvOS-%@-%@"
+ "unsupported command"
+ "up to date"
+ "v16@?0@\"NSError\"8"
+ "v40@?0@\"SUCorePolicy\"8@\"MAAsset\"16@\"MAAsset\"24@\"NSError\"32"
- "3"

```
