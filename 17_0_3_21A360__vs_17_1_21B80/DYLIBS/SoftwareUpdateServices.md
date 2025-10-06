## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-732.0.3.0.0
-  __TEXT.__text: 0x3ee74
-  __TEXT.__auth_stubs: 0xb90
-  __TEXT.__objc_methlist: 0x4c84
-  __TEXT.__cstring: 0xe836
+746.40.12.0.0
+  __TEXT.__text: 0x405b8
+  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__objc_methlist: 0x4d2c
+  __TEXT.__cstring: 0xec97
   __TEXT.__const: 0x190
-  __TEXT.__gcc_except_tab: 0x598
-  __TEXT.__oslogstring: 0x4b9
-  __TEXT.__unwind_info: 0x1528
-  __TEXT.__objc_classname: 0x9dc
-  __TEXT.__objc_methname: 0xd955
-  __TEXT.__objc_methtype: 0x2165
-  __TEXT.__objc_stubs: 0x9d60
-  __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0x1468
-  __DATA_CONST.__objc_classlist: 0x270
+  __TEXT.__gcc_except_tab: 0x740
+  __TEXT.__oslogstring: 0x52f
+  __TEXT.__unwind_info: 0x1640
+  __TEXT.__objc_classname: 0xa02
+  __TEXT.__objc_methname: 0xdae5
+  __TEXT.__objc_methtype: 0x21df
+  __TEXT.__objc_stubs: 0x9ea0
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__const: 0x14b8
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xbef0
-  __DATA_CONST.__objc_selrefs: 0x30a0
+  __DATA_CONST.__objc_const: 0xc020
+  __DATA_CONST.__objc_selrefs: 0x3108
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__cfstring: 0x9900
+  __AUTH_CONST.__cfstring: 0x9aa0
   __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__objc_const: 0x21a0
+  __AUTH_CONST.__objc_const: 0x21e8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x5d8
-  __AUTH.__objc_data: 0xcf8
+  __AUTH_CONST.__auth_got: 0x5e8
+  __AUTH.__objc_data: 0xd48
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x430
-  __DATA.__objc_superrefs: 0x1f8
-  __DATA.__objc_ivar: 0x544
+  __DATA.__objc_classrefs: 0x450
+  __DATA.__objc_superrefs: 0x200
+  __DATA.__objc_ivar: 0x554
   __DATA.__data: 0xb30
   __DATA.__bss: 0xb0
   __DATA_DIRTY.__objc_data: 0xb68

   - /System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C774927A-85B9-3DFB-9577-9460E2A0CEB7
-  Functions: 2042
-  Symbols:   7369
-  CStrings:  5364
+  UUID: 64FA9AEC-5402-3B5B-92F3-BBD6D535121E
+  Functions: 2064
+  Symbols:   7467
+  CStrings:  5425
 
Symbols:
+ -[SUAutoInstallFailureNotification .cxx_destruct]
+ -[SUAutoInstallForecast _isForecastExpired]
+ -[SUDownload isPromoted]
+ -[SUDownload setPromoted:]
+ -[SUInstallationConstraintMonitorWombat _queue_pollSatisfied]
+ -[SUInstallationConstraintMonitorWombat _set_queue_wombatEnabled:]
+ -[SUInstallationConstraintMonitorWombat _wombatEnabledDidChange:]
+ -[SUInstallationConstraintMonitorWombat _wombatEnabledDidChange:].cold.1
+ -[SUInstallationConstraintMonitorWombat _wombatEnabledDidChange:].cold.2
+ -[SUInstallationConstraintMonitorWombat initOnQueue:withDownload:]
+ -[SUInstallationConstraintMonitorWombat unsatisfiedConstraints]
+ -[SUManagerClient currentAutoInstallOperationForecast:]
+ -[SUManagerClient getMandatorySoftwareUpdateDictionaryWithError:]
+ -[SUManagerClient scheduleUpdate:withError:]
+ -[SUPreferences spacePurgeTime]
+ GCC_except_table104
+ GCC_except_table107
+ GCC_except_table116
+ GCC_except_table119
+ GCC_except_table12
+ GCC_except_table137
+ GCC_except_table15
+ GCC_except_table16
+ GCC_except_table17
+ GCC_except_table183
+ GCC_except_table186
+ GCC_except_table189
+ GCC_except_table19
+ GCC_except_table194
+ GCC_except_table197
+ GCC_except_table219
+ GCC_except_table224
+ GCC_except_table229
+ GCC_except_table232
+ GCC_except_table269
+ GCC_except_table270
+ GCC_except_table6
+ GCC_except_table8
+ GCC_except_table98
+ _AVSystemController_SubscribeToNotificationsAttribute
+ _AVSystemController_WombatEnabledAttribute
+ _AVSystemController_WombatEnabledDidChangeNotification
+ _AVSystemController_WombatEnabledDidChangeNotificationParameter
+ _OBJC_CLASS_$_AVSystemController
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_SUInstallationConstraintMonitorWombat
+ _OBJC_IVAR_$_SUAutoInstallFailureNotification._notificationLock
+ _OBJC_IVAR_$_SUDownload._promoted
+ _OBJC_IVAR_$_SUInstallationConstraintMonitorWombat._avController
+ _OBJC_IVAR_$_SUInstallationConstraintMonitorWombat._queue_wombatEnabled
+ _OBJC_METACLASS_$_SUInstallationConstraintMonitorWombat
+ __OBJC_$_INSTANCE_METHODS_SUInstallationConstraintMonitorWombat
+ __OBJC_$_INSTANCE_VARIABLES_SUInstallationConstraintMonitorWombat
+ __OBJC_CLASS_RO_$_SUInstallationConstraintMonitorWombat
+ __OBJC_METACLASS_RO_$_SUInstallationConstraintMonitorWombat
+ ___44-[SUManagerClient scheduleUpdate:withError:]_block_invoke
+ ___44-[SUManagerClient scheduleUpdate:withError:]_block_invoke_2
+ ___55-[SUManagerClient currentAutoInstallOperationForecast:]_block_invoke
+ ___55-[SUManagerClient currentAutoInstallOperationForecast:]_block_invoke_2
+ ___65-[SUInstallationConstraintMonitorWombat _wombatEnabledDidChange:]_block_invoke
+ ___65-[SUManagerClient getMandatorySoftwareUpdateDictionaryWithError:]_block_invoke
+ ___65-[SUManagerClient getMandatorySoftwareUpdateDictionaryWithError:]_block_invoke_2
+ ___block_descriptor_48_e8_32o40b_e43_v24?0"SUAutoInstallForecast"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32r40r_e34_v24?0"NSDictionary"8"NSError"16lr32l8r40l8
+ ___block_literal_global.99
+ _objc_msgSend$_set_queue_wombatEnabled:
+ _objc_msgSend$activate
+ _objc_msgSend$attributeForKey:
+ _objc_msgSend$currentAutoInstallOperationForecast:
+ _objc_msgSend$isMainThread
+ _objc_msgSend$isPromoted
+ _objc_msgSend$scheduleUpdate:withError:
+ _objc_msgSend$setAttribute:forKey:error:
+ _objc_msgSend$setPromoted:
+ _objc_msgSend$sleepForTimeInterval:
+ _objc_msgSend$spacePurgeTime
+ _objc_sync_enter
+ _objc_sync_exit
- GCC_except_table103
- GCC_except_table106
- GCC_except_table115
- GCC_except_table118
- GCC_except_table133
- GCC_except_table179
- GCC_except_table182
- GCC_except_table185
- GCC_except_table190
- GCC_except_table193
- GCC_except_table217
- GCC_except_table222
- GCC_except_table225
- GCC_except_table263
- GCC_except_table97
- ___34-[SUManagerClient scheduleUpdate:]_block_invoke
- ___34-[SUManagerClient scheduleUpdate:]_block_invoke_2
- ___block_literal_global.84
- _objc_msgSend$resume
CStrings:
+ "\n                \thasReadMeSummary: %@\n                \thasReadMe: %@\n                \thasLicenseAgreement: %@\n                \thasIconImageName: %@\n                \thasIconImage: %@\n                \thumanReadableUpdateName: %@\n                \tnotificationTitle:%@\n                \tnotificationBody:%@\n                \trecommendedUpdateTitle:%@\n                \trecommendedUpdateBody:%@\n                \tmandatoryUpdateBody:%@"
+ "\n            Descriptor: %@\n            DownloadOptions: %@\n            Progress: %@\n            isPromoted: %@"
+ "%@ - is wombat constraint changed (satisfied? %@)"
+ "%s: Current free space without purging: %llu"
+ "%s: Failed to get network path evaluator"
+ "%s: Failed to get status from %@"
+ "%s: Failed to get userinfo from %@"
+ "%s: Needed bytes: %llu"
+ "%s: Network path is expensive? %@"
+ "%s: Post CacheDelete neededBytes: %llu; amountPurgeable: %llu"
+ "%s: [DEFAULTS] space purge failed"
+ "%s: [DEFAULTS] space purge succeeded"
+ "%s: [DEFAULTS] spacePurgeTime set, sleeping %d secs"
+ "%s: haveEnoughSpace: %@"
+ "+[SUSpace makeRoomForUpdate:completion:]"
+ "-[SUInstallationConstraintMonitorWombat _wombatEnabledDidChange:]"
+ "-[SUManagerClient currentAutoInstallOperationForecast:]"
+ "-[SUManagerClient currentAutoInstallOperationForecast:]_block_invoke"
+ "-[SUManagerClient getMandatorySoftwareUpdateDictionaryWithError:]"
+ "-[SUManagerClient getMandatorySoftwareUpdateDictionaryWithError:]_block_invoke"
+ "-[SUManagerClient scheduleUpdate:withError:]"
+ "-[SUManagerClient scheduleUpdate:withError:]_block_invoke"
+ "-[SUNetworkMonitor isCurrentNetworkTypeExpensive]_block_invoke"
+ "@\"AVSystemController\""
+ "@\"NSObject\""
+ "B32@0:8@\"SUCoreDDMDeclaration\"16^@24"
+ "Loaded rolled back build versions: %@"
+ "Number of seconds for space purge (+[SUSpace makeRoomForUpdate:error:]) to finish. Even => success; odd => failure."
+ "SUInstallationConstraintMonitorWombat"
+ "SUSpacePurgeTime"
+ "Sytem partition growth for [%@] <%p> = %llu bytes"
+ "TB,N,GisPromoted,V_promoted"
+ "WombatEnabled"
+ "_avController"
+ "_isForecastExpired"
+ "_notificationLock"
+ "_promoted"
+ "_queue_wombatEnabled"
+ "_set_queue_wombatEnabled:"
+ "_wombatEnabledDidChange:"
+ "activate"
+ "attributeForKey:"
+ "com.apple.SoftwareUpdateServices.followup.InsufficientDiskSpace"
+ "currentAutoInstallOperationForecast:"
+ "getMandatorySoftwareUpdateDictionaryWithError:"
+ "isMainThread"
+ "isPromoted"
+ "promoted"
+ "scheduleUpdate:withError:"
+ "setAttribute:forKey:error:"
+ "setPromoted:"
+ "sleepForTimeInterval:"
+ "spacePurgeTime"
+ "v24@0:8@?<v@?@\"SUAutoInstallForecast\"@\"NSError\">16"
+ "v24@?0@\"SUAutoInstallForecast\"8@\"NSError\"16"
- "\n            \thasReadMeSummary: %@\n            \thasReadMe: %@\n            \thasLicenseAgreement: %@\n            \thasIconImageName: %@\n            \thasIconImage: %@\n            \thumanReadableUpdateName: %@\n            \tnotificationTitle:%@\n            \tnotificationBody:%@\n            \trecommendedUpdateTitle:%@\n            \trecommendedUpdateBody:%@\n            \tmandatoryUpdateBody:%@"
- "\n            Descriptor: %@\n            DownloadOptions: %@\n            Progress: %@"
- "-[SUManagerClient scheduleUpdate:]"
- "-[SUManagerClient scheduleUpdate:]_block_invoke"
- "Current free space without purging: %llu"
- "Failed to get network path evaluator"
- "Sytem partition growth = %llu bytes"
- "resume"

```
