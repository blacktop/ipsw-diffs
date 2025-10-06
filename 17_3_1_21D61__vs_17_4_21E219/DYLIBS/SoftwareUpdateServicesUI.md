## SoftwareUpdateServicesUI

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI`

```diff

-192.80.1.0.0
-  __TEXT.__text: 0x8820
+200.100.3.0.1
+  __TEXT.__text: 0x94c8
   __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__objc_methlist: 0x864
+  __TEXT.__objc_methlist: 0x84c
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0xcbd
+  __TEXT.__cstring: 0xdb2
   __TEXT.__oslogstring: 0x39c
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__unwind_info: 0x13c
-  __TEXT.__objc_classname: 0x291
-  __TEXT.__objc_methname: 0x17e0
-  __TEXT.__objc_methtype: 0x387
-  __TEXT.__objc_stubs: 0x1080
-  __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x1080
-  __DATA_CONST.__objc_classlist: 0x88
+  __TEXT.__objc_classname: 0x2a8
+  __TEXT.__objc_methname: 0x190a
+  __TEXT.__objc_methtype: 0x469
+  __TEXT.__objc_stubs: 0x1120
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__const: 0x19b8
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1680
-  __DATA_CONST.__objc_selrefs: 0x6a0
-  __AUTH_CONST.__objc_const: 0x620
-  __AUTH_CONST.__cfstring: 0xfc0
+  __DATA_CONST.__objc_const: 0x1788
+  __DATA_CONST.__objc_selrefs: 0x690
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x100
+  __DATA_CONST.__objc_superrefs: 0x50
+  __AUTH_CONST.__objc_const: 0x668
+  __AUTH_CONST.__cfstring: 0x1120
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__auth_got: 0x188
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x100
-  __DATA.__objc_superrefs: 0x40
-  __DATA.__objc_ivar: 0x88
-  __DATA.__data: 0x280
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_ivar: 0x90
+  __DATA.__data: 0x2b0
   __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x50

   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8DF3BDC5-D404-3B9D-8BE6-5BF44078B606
-  Functions: 211
-  Symbols:   1343
-  CStrings:  669
+  UUID: 91A00BEC-3BB4-3929-86C4-DA05FC78D75B
+  Functions: 213
+  Symbols:   1691
+  CStrings:  700
 
Symbols:
+ -[SUSUICommandLineToolClient getAlertStatus:]
+ -[SUSUICommandLineToolClient showMiniAlertWithDescriptors:errorCode:downloadDescriptor:scanResultsDescriptor:autoInstallForecast:andRollbackDescriptor:result:]
+ -[SUSUICommandLineToolClient showMiniAlertWithScan:errorCode:result:]
+ -[SUSUIFakeSUDescriptor fakeDocumentation]
+ -[SUSUIFakeSUDescriptor init]
+ -[SUSUIFakeSUScanResults fakeAlternateDescriptor]
+ -[SUSUIFakeSUScanResults fakePreferredDescriptor]
+ -[SUSUIFakeSUScanResults init]
+ -[SUSUIPreferences preventPostUpdateAlert]
+ -[SUSUIPreferences preventRebootAlert]
+ GCC_except_table29
+ OBJC_IVAR_$_SUDescriptor._assetID
+ OBJC_IVAR_$_SUDescriptor._audienceType
+ OBJC_IVAR_$_SUDescriptor._autoDownloadAllowableForCellular
+ OBJC_IVAR_$_SUDescriptor._autoUpdateEnabled
+ OBJC_IVAR_$_SUDescriptor._criticalOutOfBoxOnly
+ OBJC_IVAR_$_SUDescriptor._disableIntallTonight
+ OBJC_IVAR_$_SUDescriptor._downloadAllowableForCellular
+ OBJC_IVAR_$_SUDescriptor._downloadSize
+ OBJC_IVAR_$_SUDescriptor._downloadable
+ OBJC_IVAR_$_SUDescriptor._forcePasscodeRequired
+ OBJC_IVAR_$_SUDescriptor._hideInstallAlert
+ OBJC_IVAR_$_SUDescriptor._humanReadableUpdateName
+ OBJC_IVAR_$_SUDescriptor._installationSize
+ OBJC_IVAR_$_SUDescriptor._isSplatOnly
+ OBJC_IVAR_$_SUDescriptor._mandatoryUpdateEligible
+ OBJC_IVAR_$_SUDescriptor._mandatoryUpdateOptional
+ OBJC_IVAR_$_SUDescriptor._mandatoryUpdateRestrictedToOutOfTheBox
+ OBJC_IVAR_$_SUDescriptor._mandatoryUpdateVersionMax
+ OBJC_IVAR_$_SUDescriptor._mandatoryUpdateVersionMin
+ OBJC_IVAR_$_SUDescriptor._msuPrepareSize
+ OBJC_IVAR_$_SUDescriptor._preferenceType
+ OBJC_IVAR_$_SUDescriptor._prerequisiteBuild
+ OBJC_IVAR_$_SUDescriptor._prerequisiteOS
+ OBJC_IVAR_$_SUDescriptor._productBuildVersion
+ OBJC_IVAR_$_SUDescriptor._productSystemName
+ OBJC_IVAR_$_SUDescriptor._productVersion
+ OBJC_IVAR_$_SUDescriptor._promoteAlternateUpdate
+ OBJC_IVAR_$_SUDescriptor._publisher
+ OBJC_IVAR_$_SUDescriptor._rampEnabled
+ OBJC_IVAR_$_SUDescriptor._setupCritical
+ OBJC_IVAR_$_SUDescriptor._unarchiveSize
+ OBJC_IVAR_$_SUDescriptor._updateType
+ OBJC_IVAR_$_SUDescriptor._upgradeType
+ _MA_AUTO_ASSET_SHORT_TERM_LOCK_FILESYSTEM_ATOMIC_INSTANCE
+ _MA_AUTO_ASSET_SHORT_TERM_LOCK_FILESYSTEM_BASE_LOCATION
+ _MA_AUTO_ASSET_SHORT_TERM_LOCK_FILESYSTEM_DIRECTORY
+ _MA_AUTO_ASSET_SHORT_TERM_LOCK_FILESYSTEM_EXTENSION
+ _MA_AUTO_ASSET_SHORT_TERM_LOCK_FILESYSTEM_LATEST
+ _MA_AUTO_ASSET_SHORT_TERM_LOCK_FILESYSTEM_SPECIFIC
+ _MA_PALLAS_AUDIENCE_EXTERNAL_PRE_RELEASE
+ _MA_SANDBOX_EXTENSION_PATH_KEY
+ _OBJC_CLASS_$_SUSUIFakeSUScanResults
+ _OBJC_CLASS_$_SUScanResults
+ _OBJC_IVAR_$_SUSUIPreferences._preventPostUpdateAlert
+ _OBJC_IVAR_$_SUSUIPreferences._preventRebootAlert
+ _OBJC_METACLASS_$_SUSUIFakeSUScanResults
+ _OBJC_METACLASS_$_SUScanResults
+ __OBJC_$_INSTANCE_METHODS_SUSUIFakeSUScanResults
+ __OBJC_CLASS_RO_$_SUSUIFakeSUScanResults
+ __OBJC_METACLASS_RO_$_SUSUIFakeSUScanResults
+ ___159-[SUSUICommandLineToolClient showMiniAlertWithDescriptors:errorCode:downloadDescriptor:scanResultsDescriptor:autoInstallForecast:andRollbackDescriptor:result:]_block_invoke
+ ___159-[SUSUICommandLineToolClient showMiniAlertWithDescriptors:errorCode:downloadDescriptor:scanResultsDescriptor:autoInstallForecast:andRollbackDescriptor:result:]_block_invoke_2
+ ___43-[SUSUIControllerClient getPasscodePolicy:]_block_invoke.238
+ ___45-[SUSUICommandLineToolClient getAlertStatus:]_block_invoke
+ ___69-[SUSUICommandLineToolClient showMiniAlertWithScan:errorCode:result:]_block_invoke
+ ___69-[SUSUICommandLineToolClient showMiniAlertWithScan:errorCode:result:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSString"8"NSError"16ls32l8
+ _kSUSUIPreferencePreventPostUpdateAlert
+ _kSUSUIPreferencePreventRebootAlert
+ _objc_msgSend$fakeAlternateDescriptor
+ _objc_msgSend$fakePreferredDescriptor
+ _objc_msgSend$getAlertStatus:
+ _objc_msgSend$preventPostUpdateAlert
+ _objc_msgSend$showMiniAlertWithDescriptors:errorCode:downloadDescriptor:scanResultsDescriptor:autoInstallForecast:andRollbackDescriptor:result:
+ _objc_msgSend$showMiniAlertWithScan:errorCode:result:
- -[SUSUICommandLineToolClient showMiniAlert:usingFakeData:errorCode:]
- -[SUSUIFakeSUDescriptor documentation]
- -[SUSUIFakeSUDescriptor downloadSize]
- -[SUSUIFakeSUDescriptor humanReadableUpdateName]
- -[SUSUIFakeSUDescriptor installationSize]
- -[SUSUIFakeSUDescriptor isDownloadableOverCellular]
- -[SUSUIFakeSUDescriptor isDownloadable]
- -[SUSUIFakeSUDescriptor preparationSize]
- -[SUSUIFakeSUDescriptor productBuildVersion]
- -[SUSUIFakeSUDescriptor productSystemName]
- -[SUSUIFakeSUDescriptor productVersion]
- -[SUSUIFakeSUDescriptor publisher]
- -[SUSUIFakeSUDescriptor updateType]
- GCC_except_table24
- ___43-[SUSUIControllerClient getPasscodePolicy:]_block_invoke.214
- _objc_msgSend$showMiniAlert:usingFakeData:errorCode:
CStrings:
+ "/private/var/MobileAsset/AssetsV2/locks"
+ "0206c249-b301-46e0-9d6a-23ce9c5d875d"
+ "FakeApple"
+ "FakeOS"
+ "FakeOS 17.0"
+ "SUSUIFakeSUScanResults"
+ "T@\"NSString\",?,R,C"
+ "TB,R,N,V_preventPostUpdateAlert"
+ "TB,R,N,V_preventRebootAlert"
+ "_preventPostUpdateAlert"
+ "_preventRebootAlert"
+ "atomic_instance"
+ "fakeAlternateDescriptor"
+ "fakeDocumentation"
+ "fakePreferredDescriptor"
+ "getAlertStatus:"
+ "initWithPreferredDescriptor:alternateDescriptor:"
+ "keybagInterfacePasscodeDidChange:"
+ "latest"
+ "locker"
+ "preventPostUpdateAlert"
+ "preventRebootAlert"
+ "sandboxExtensionPathKey"
+ "shared_locks"
+ "showMiniAlertWithDescriptors:errorCode:downloadDescriptor:scanResultsDescriptor:autoInstallForecast:andRollbackDescriptor:result:"
+ "showMiniAlertWithScan:errorCode:result:"
+ "specific"
+ "v24@0:8@\"SUKeybagInterface\"16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v40@0:8Q16@\"NSNumber\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8Q16@24@?32"
+ "v72@0:8Q16@\"NSNumber\"24@\"SUDownload\"32@\"SUScanResults\"40@\"SUAutoInstallForecast\"48@\"SURollbackDescriptor\"56@?<v@?@\"NSString\"@\"NSError\">64"
+ "v72@0:8Q16@24@32@40@48@56@?64"
- "Apple"
- "documentation"
- "downloadSize"
- "humanReadableUpdateName"
- "iOS"
- "installationSize"
- "isDownloadable"
- "isDownloadableOverCellular"
- "preparationSize"
- "productSystemName"
- "publisher"
- "showMiniAlert:usingFakeData:errorCode:"
- "updateType"
- "v36@0:8Q16B24@\"NSNumber\"28"
- "v36@0:8Q16B24@28"

```
