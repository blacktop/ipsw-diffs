## SoftwareUpdateServicesUI

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI`

```diff

-231.100.2.0.0
-  __TEXT.__text: 0x995c
+244.0.0.502.1
+  __TEXT.__text: 0x986c
   __TEXT.__auth_stubs: 0x2d0
   __TEXT.__objc_methlist: 0xb00
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0xf63
+  __TEXT.__cstring: 0xf7b
   __TEXT.__oslogstring: 0x39c
   __TEXT.__gcc_except_tab: 0xd8
   __TEXT.__unwind_info: 0x140
   __TEXT.__objc_classname: 0x2a9
-  __TEXT.__objc_methname: 0x1a81
+  __TEXT.__objc_methname: 0x1d4c
   __TEXT.__objc_methtype: 0x4b8
-  __TEXT.__objc_stubs: 0x11a0
-  __DATA_CONST.__got: 0x258
-  __DATA_CONST.__const: 0x1e08
+  __TEXT.__objc_stubs: 0x15a0
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__const: 0x1e50
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x778
+  __DATA_CONST.__objc_selrefs: 0x878
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x50
   __AUTH_CONST.__auth_got: 0x178
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x1360
+  __AUTH_CONST.__cfstring: 0x1380
   __AUTH_CONST.__objc_const: 0x1a70
   __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0x98

   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E8B4ACA-1394-3CEA-AD83-B54B880FC473
+  UUID: 11BB4BE9-F28F-3677-940B-7B47AEEE820A
   Functions: 220
-  Symbols:   1852
-  CStrings:  745
+  Symbols:   1860
+  CStrings:  779
 
Symbols:
+ _MA_CONTENT_CACHE_SERVER_URL_OVERRIDE_DEFAULT_KEY
+ ___43-[SUSUIControllerClient getPasscodePolicy:]_block_invoke.286
+ _objc_msgSend$_setDisableInstallTonight:
+ _objc_msgSend$_setMsuPrepareSize:
+ _objc_msgSend$_setUnarchiveSize:
+ _objc_msgSend$setAssetID:
+ _objc_msgSend$setAudienceType:
+ _objc_msgSend$setAutoDownloadAllowableForCellular:
+ _objc_msgSend$setAutoUpdateEnabled:
+ _objc_msgSend$setCriticalOutOfBoxOnly:
+ _objc_msgSend$setDownloadSize:
+ _objc_msgSend$setDownloadable:
+ _objc_msgSend$setForcePasscodeRequired:
+ _objc_msgSend$setHideInstallAlert:
+ _objc_msgSend$setHumanReadableUpdateName:
+ _objc_msgSend$setInstallationSize:
+ _objc_msgSend$setIsSplatOnly:
+ _objc_msgSend$setMandatoryUpdateEligible:
+ _objc_msgSend$setMandatoryUpdateOptional:
+ _objc_msgSend$setMandatoryUpdateRestrictedToOutOfTheBox:
+ _objc_msgSend$setMandatoryUpdateVersionMax:
+ _objc_msgSend$setMandatoryUpdateVersionMin:
+ _objc_msgSend$setPreferenceType:
+ _objc_msgSend$setPrerequisiteBuild:
+ _objc_msgSend$setPrerequisiteOS:
+ _objc_msgSend$setProductBuildVersion:
+ _objc_msgSend$setProductSystemName:
+ _objc_msgSend$setProductVersion:
+ _objc_msgSend$setPromoteAlternateUpdate:
+ _objc_msgSend$setPublisher:
+ _objc_msgSend$setRampEnabled:
+ _objc_msgSend$setSetupCritical:
+ _objc_msgSend$setUpdateType:
+ _objc_msgSend$setUpgradeType:
- OBJC_IVAR_$_SUDescriptor._assetID
- OBJC_IVAR_$_SUDescriptor._audienceType
- OBJC_IVAR_$_SUDescriptor._autoDownloadAllowableForCellular
- OBJC_IVAR_$_SUDescriptor._autoUpdateEnabled
- OBJC_IVAR_$_SUDescriptor._criticalOutOfBoxOnly
- OBJC_IVAR_$_SUDescriptor._disableIntallTonight
- OBJC_IVAR_$_SUDescriptor._downloadAllowableForCellular
- OBJC_IVAR_$_SUDescriptor._downloadSize
- OBJC_IVAR_$_SUDescriptor._downloadable
- OBJC_IVAR_$_SUDescriptor._forcePasscodeRequired
- OBJC_IVAR_$_SUDescriptor._hideInstallAlert
- OBJC_IVAR_$_SUDescriptor._humanReadableUpdateName
- OBJC_IVAR_$_SUDescriptor._installationSize
- OBJC_IVAR_$_SUDescriptor._isSplatOnly
- OBJC_IVAR_$_SUDescriptor._mandatoryUpdateEligible
- OBJC_IVAR_$_SUDescriptor._mandatoryUpdateOptional
- OBJC_IVAR_$_SUDescriptor._mandatoryUpdateRestrictedToOutOfTheBox
- OBJC_IVAR_$_SUDescriptor._mandatoryUpdateVersionMax
- OBJC_IVAR_$_SUDescriptor._mandatoryUpdateVersionMin
- OBJC_IVAR_$_SUDescriptor._msuPrepareSize
- OBJC_IVAR_$_SUDescriptor._preferenceType
- OBJC_IVAR_$_SUDescriptor._prerequisiteBuild
- OBJC_IVAR_$_SUDescriptor._prerequisiteOS
- OBJC_IVAR_$_SUDescriptor._productBuildVersion
- OBJC_IVAR_$_SUDescriptor._productSystemName
- OBJC_IVAR_$_SUDescriptor._productVersion
- OBJC_IVAR_$_SUDescriptor._promoteAlternateUpdate
- OBJC_IVAR_$_SUDescriptor._publisher
- OBJC_IVAR_$_SUDescriptor._rampEnabled
- OBJC_IVAR_$_SUDescriptor._setupCritical
- OBJC_IVAR_$_SUDescriptor._unarchiveSize
- OBJC_IVAR_$_SUDescriptor._updateType
- OBJC_IVAR_$_SUDescriptor._upgradeType
- ___43-[SUSUIControllerClient getPasscodePolicy:]_block_invoke.283
Functions:
~ -[SUSUIFakeSUDescriptor init] : 1172 -> 932
CStrings:
+ "ContentCacheURLOverride"
+ "_setDisableInstallTonight:"
+ "_setMsuPrepareSize:"
+ "_setUnarchiveSize:"
+ "setAssetID:"
+ "setAudienceType:"
+ "setAutoDownloadAllowableForCellular:"
+ "setAutoUpdateEnabled:"
+ "setCriticalOutOfBoxOnly:"
+ "setDownloadSize:"
+ "setDownloadable:"
+ "setForcePasscodeRequired:"
+ "setHideInstallAlert:"
+ "setHumanReadableUpdateName:"
+ "setInstallationSize:"
+ "setIsSplatOnly:"
+ "setMandatoryUpdateEligible:"
+ "setMandatoryUpdateOptional:"
+ "setMandatoryUpdateRestrictedToOutOfTheBox:"
+ "setMandatoryUpdateVersionMax:"
+ "setMandatoryUpdateVersionMin:"
+ "setPreferenceType:"
+ "setPrerequisiteBuild:"
+ "setPrerequisiteOS:"
+ "setProductBuildVersion:"
+ "setProductSystemName:"
+ "setProductVersion:"
+ "setPromoteAlternateUpdate:"
+ "setPublisher:"
+ "setRampEnabled:"
+ "setSetupCritical:"
+ "setUpdateType:"
+ "setUpgradeType:"

```
