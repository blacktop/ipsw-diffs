## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__oslogstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2718.0.5.0.0
-  __TEXT.__text: 0xaed2c
-  __TEXT.__objc_methlist: 0x83e4
+2718.0.12.0.0
+  __TEXT.__text: 0xaf128
+  __TEXT.__objc_methlist: 0x842c
+  __TEXT.__cstring: 0x1620d
   __TEXT.__const: 0x1e2
-  __TEXT.__cstring: 0x1618d
-  __TEXT.__oslogstring: 0xcef3
   __TEXT.__gcc_except_tab: 0x764
+  __TEXT.__oslogstring: 0xcef3
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x43
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1910
+  __TEXT.__unwind_info: 0x1918
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a30
+  __DATA_CONST.__objc_selrefs: 0x4a58
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x200
+  __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_arraydata: 0xe8
-  __DATA_CONST.__got: 0xb00
+  __DATA_CONST.__got: 0xb30
   __AUTH_CONST.__const: 0x508
-  __AUTH_CONST.__cfstring: 0x13760
-  __AUTH_CONST.__objc_const: 0xbb28
+  __AUTH_CONST.__cfstring: 0x137a0
+  __AUTH_CONST.__objc_const: 0xbb88
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__auth_got: 0x6f0
   __AUTH.__objc_data: 0x7c8
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0xab0
+  __DATA.__objc_ivar: 0xab8
   __DATA.__data: 0x3d8
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0xed8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3285
-  Symbols:   7783
-  CStrings:  3298
+  Functions: 3291
+  Symbols:   7803
+  CStrings:  3300
 
Symbols:
+ -[SUCoreDescriptor preSUStagingOptionalCount]
+ -[SUCoreDescriptor preSUStagingRequiredCount]
+ -[SUCoreDescriptor setPreSUStagingOptionalCount:]
+ -[SUCoreDescriptor setPreSUStagingRequiredCount:]
+ -[SUCoreScanPSUSDetermineResult assignToUpdate:]
+ -[SUCoreScanPSUSDetermineResult init]
+ GCC_except_table51
+ GCC_except_table58
+ GCC_except_table66
+ _OBJC_IVAR_$_SUCoreDescriptor._preSUStagingOptionalCount
+ _OBJC_IVAR_$_SUCoreDescriptor._preSUStagingRequiredCount
+ _kSUCoreControllerPreSUStagingOptionalCountKey
+ _kSUCoreControllerPreSUStagingOptionalStagedCountKey
+ _kSUCoreControllerPreSUStagingOptionalStagedSizeKey
+ _kSUCoreControllerPreSUStagingRequiredCountKey
+ _kSUCoreControllerPreSUStagingRequiredStagedCountKey
+ _kSUCoreControllerPreSUStagingRequiredStagedSizeKey
+ _objc_msgSend$assignToUpdate:
+ _objc_msgSend$preSUStagingOptionalCount
+ _objc_msgSend$preSUStagingRequiredCount
+ _objc_msgSend$setPreSUStagingOptionalCount:
+ _objc_msgSend$setPreSUStagingRequiredCount:
- GCC_except_table49
- GCC_except_table64
CStrings:
+ "                             enablePSUS: %@\n            enablePSUSForOptionalAssets: %@\n    minFreeSpacePostStageOptionalAssets: %llu\n           preSUStagingCacheDeleteLevel: %d\n              preSUStagingRequiredCount: %lu\n              preSUStagingOptionalCount: %lu\n      autoDownloadAllowableOverCellular: %@\n          downloadAllowableOverCellular: %@\n                           downloadable: %@\n               disableSiriVoiceDeletion: %@\n                        disableCDLevel4: %@\n                  disableCDCriticalMode: %@\n                     disableAppDemotion: %@\n                    disableMASuspension: %@\n                  disableInstallTonight: %@\n                  forcePasscodeRequired: %@\n                            rampEnabled: %@\n                         badgingEnabled: %@\n                       granularlyRamped: %@\n                       mdmDelayInterval: %llu\n                      autoUpdateEnabled: %@\n                       hideInstallAlert: %@\n                     containsSFRContent: %@\n                   installAlertInterval: %llu\n             allowAutoDownloadOnBattery: %@\n             autoDownloadOnBatteryDelay: %llu\n        autoDownloadOnBatteryMinBattery: %llu\n                         disableSplombo: %@\n                          setupCritical: %@\n               criticalCellularOverride: %@\n                   criticalOutOfBoxOnly: %@\n                     lastEmergencyBuild: %@\n                 lastEmergencyOSVersion: %@\n                mandatoryUpdateEligible: %@\n              mandatoryUpdateVersionMin: %@\n              mandatoryUpdateVersionMax: %@\n                mandatoryUpdateOptional: %@\n mandatoryUpdateRestrictedToOutOfTheBox: %@\n                   oneShotBuddyDisabled: %@\n             oneShotBuddyDisabledBuilds: %@\n"
+ "PSUSOptionalCount"
+ "PSUSRequiredCount"
- "                             enablePSUS: %@\n            enablePSUSForOptionalAssets: %@\n    minFreeSpacePostStageOptionalAssets: %llu\n           preSUStagingCacheDeleteLevel: %d\n      autoDownloadAllowableOverCellular: %@\n          downloadAllowableOverCellular: %@\n                           downloadable: %@\n               disableSiriVoiceDeletion: %@\n                        disableCDLevel4: %@\n                  disableCDCriticalMode: %@\n                     disableAppDemotion: %@\n                    disableMASuspension: %@\n                  disableInstallTonight: %@\n                  forcePasscodeRequired: %@\n                            rampEnabled: %@\n                         badgingEnabled: %@\n                       granularlyRamped: %@\n                       mdmDelayInterval: %llu\n                      autoUpdateEnabled: %@\n                       hideInstallAlert: %@\n                     containsSFRContent: %@\n                   installAlertInterval: %llu\n             allowAutoDownloadOnBattery: %@\n             autoDownloadOnBatteryDelay: %llu\n        autoDownloadOnBatteryMinBattery: %llu\n                         disableSplombo: %@\n                          setupCritical: %@\n               criticalCellularOverride: %@\n                   criticalOutOfBoxOnly: %@\n                     lastEmergencyBuild: %@\n                 lastEmergencyOSVersion: %@\n                mandatoryUpdateEligible: %@\n              mandatoryUpdateVersionMin: %@\n              mandatoryUpdateVersionMax: %@\n                mandatoryUpdateOptional: %@\n mandatoryUpdateRestrictedToOutOfTheBox: %@\n                   oneShotBuddyDisabled: %@\n             oneShotBuddyDisabledBuilds: %@\n"
```
