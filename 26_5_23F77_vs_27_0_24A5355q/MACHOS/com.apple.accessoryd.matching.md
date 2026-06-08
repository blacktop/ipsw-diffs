## com.apple.accessoryd.matching

> `/System/Library/UserEventPlugins/com.apple.accessoryd.matching.plugin/com.apple.accessoryd.matching`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0x3bd58
-  __TEXT.__auth_stubs: 0xfc0
+1176.0.26.502.1
+  __TEXT.__text: 0x37dac
+  __TEXT.__auth_stubs: 0x1000
   __TEXT.__objc_stubs: 0x5080
   __TEXT.__objc_methlist: 0x23ac
-  __TEXT.__cstring: 0x4ef4
-  __TEXT.__objc_methname: 0x6eb0
-  __TEXT.__objc_classname: 0x2b5
-  __TEXT.__objc_methtype: 0xada
+  __TEXT.__cstring: 0x4fa9
+  __TEXT.__objc_methname: 0x6ebf
+  __TEXT.__objc_classname: 0x27f
+  __TEXT.__objc_methtype: 0xaeb
   __TEXT.__const: 0x228
-  __TEXT.__oslogstring: 0x3f3e
-  __TEXT.__gcc_except_tab: 0x524
+  __TEXT.__oslogstring: 0x3f4f
+  __TEXT.__gcc_except_tab: 0x404
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0xbb0
-  __DATA.__auth_got: 0x7f0
-  __DATA.__got: 0x358
-  __DATA.__auth_ptr: 0x18
-  __DATA.__const: 0x1070
+  __TEXT.__unwind_info: 0xa50
+  __DATA.__const: 0x10b0
   __DATA.__cfstring: 0x3940
   __DATA.__objc_classlist: 0xb0
   __DATA.__objc_catlist: 0x10

   __DATA.__objc_intobj: 0x60
   __DATA.__data: 0x39e
   __DATA.__objc_dictobj: 0x28
-  __DATA.__bss: 0x1d8
+  __DATA.__auth_got: 0x810
+  __DATA.__got: 0x358
+  __DATA.__auth_ptr: 0x18
+  __DATA.__bss: 0x1e8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 7A4ABD4A-FF4C-3A23-8E65-2D95B6AF58F1
-  Functions: 1502
-  Symbols:   8381
-  CStrings:  2976
+  UUID: 2C6A5A79-4E4B-3F07-B2D6-08FBFDF9132B
+  Functions: 1499
+  Symbols:   8400
+  CStrings:  2980
 
Symbols:
+ -[accessorydMatchingPlugin findKnownBTDevices].cold.6
+ -[accessorydMatchingPlugin findUniqueEventsOnPrimaryPort:scanReason:resultsArray:].cold.2
+ -[accessorydMatchingPlugin findUniqueEventsOnPrimaryPort:scanReason:resultsArray:].cold.3
+ -[accessorydMatchingPlugin findUniqueEventsOnPrimaryPort:scanReason:resultsArray:].cold.4
+ -[accessorydMatchingPlugin findUniqueEventsOnPrimaryPort:scanReason:resultsArray:].cold.5
+ -[accessorydMatchingPlugin launchDigitalIDClients].cold.1
+ -[accessorydMatchingPlugin printRMEventArray].cold.2
+ -[accessorydMatchingPlugin printRMEventArray].cold.3
+ -[accessorydMatchingPlugin printRMEventArray].cold.4
+ -[accessorydMatchingPlugin printRMEventArray].cold.5
+ -[accessorydMatchingPlugin removeStandardModeEvents].cold.2
+ -[accessorydMatchingPlugin removeStandardModeEvents].cold.3
+ -[ueaPluginSystemSettingsMonitor notifyDriverOfBluetoothSetting:andAirplaneMode:forPrimaryPort:]
+ -[ueaPluginSystemSettingsMonitor notifyDriverOfBluetoothSetting:andAirplaneMode:forPrimaryPort:].cold.1
+ -[ueaPluginSystemSettingsMonitor notifyDriverOfBluetoothSetting:andAirplaneMode:forPrimaryPort:].cold.2
+ -[ueaPluginSystemSettingsMonitor notifyDriverOfBluetoothSetting:andAirplaneMode:forPrimaryPort:].cold.3
+ -[ueaPluginSystemSettingsMonitor notifyDriverOfBluetoothSetting:andAirplaneMode:forPrimaryPort:].cold.4
+ -[ueaPluginSystemSettingsMonitor notifyDriverOfBluetoothSetting:andAirplaneMode:forPrimaryPort:].cold.5
+ -[ueaPluginSystemSettingsMonitor notifyDriverOfBluetoothSetting:andAirplaneMode:forPrimaryPort:].cold.6
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCAnalytics.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCAnalyticsLogger.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCObjCType.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCSQLite.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCSQLiteStatement.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCStrings.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCUserDefaults.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCUserNotification.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCUserNotificationManager.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCUserNotifications.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/IOUIAngelService.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/IOUserNotification.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/TRMPort.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/TRMPortManager.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/acc_analytics_utilities.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/acc_restricted_mode.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/acc_user_notification.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/accessorydMatchingPlugin.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/common_cf.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/logging_accessories_uea.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/logging_wrapper.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/system_info.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ueaPluginSystemSettings.o
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Sources/CoreAccessories/Apple/Accessory_Frameworks/CoreAccessories/
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Sources/CoreAccessories/Apple/accessorydMatchingPlugin/
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Sources/CoreAccessories/Common/Common_C/
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Sources/CoreAccessories/Common/Common_CF/
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Sources/CoreAccessories/Common/Common_ObjC/
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Sources/CoreAccessories/Common/SplunkAnalytics/
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Sources/CoreAccessories/Common/SplunkAnalytics/ACCAnalyticsLogger/
+ /Library/Caches/com.apple.xbs/6E609522-BCE4-4267-888D-F9E730CF32ED/TemporaryDirectory.bMirSv/Sources/CoreAccessories/Common/SplunkAnalytics/ACCAnalyticsLogger/SQLite/
+ EnableAccessoryPower.cold.4
+ EnableAccessoryPower.cold.5
+ EnableAccessoryPower.cold.6
+ IOAccessoryManagerAdded.cold.1
+ IOAccessoryManagerAdded.cold.2
+ IOAccessoryManagerAdded.cold.3
+ IOAccessoryManagerAdded.cold.4
+ IOAccessoryManagerAdded.cold.5
+ IOAccessoryManagerAdded.cold.6
+ IOAccessoryManagerAdded.cold.7
+ IOAccessoryManagerAdded.cold.8
+ IOAccessoryManagerAdded.cold.9
+ IOAccessoryManagerTerminated.cold.1
+ IOAccessoryPortTerminated.cold.1
+ _ACMGetEnvironmentVariableData
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_70
+ __IOAccessoryManagerEventCallback_block_invoke.962.cold.1
+ __IOAccessoryManagerEventCallback_block_invoke.964
+ __IOAccessoryManagerEventCallback_block_invoke.966
+ ___logObjectForModule_block_invoke
+ __block_literal_global.1002
+ __block_literal_global.1005
+ __block_literal_global.1007
+ __block_literal_global.1010
+ __block_literal_global.1022
+ __block_literal_global.1024
+ __block_literal_global.321
+ __block_literal_global.361
+ __block_literal_global.903
+ __block_literal_global.973
+ __block_literal_global.982
+ __logObjectForModule_block_invoke.cold.1
+ __serviceLDCMMitigationStatusChanged_block_invoke.1003
+ __serviceLDCMMitigationStatusChanged_block_invoke.1003.cold.1
+ __serviceLDCMMitigationStatusChanged_block_invoke.1003.cold.2
+ __serviceLDCMMitigationStatusChanged_block_invoke.1003.cold.3
+ __serviceLDCMMitigationStatusChanged_block_invoke.1003.cold.4
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$notifyDriverOfBluetoothSetting:andAirplaneMode:forPrimaryPort:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x5
+ _shouldPresentTRMDialog.cold.4
+ _shouldPresentTRMDialog.cold.5
+ logObjectForModule.onceToken
+ serviceAddedLDCM.cold.4
+ serviceAddedLDCM.cold.5
+ serviceAddedLDCM.cold.6
+ serviceAddedLDCM.cold.7
+ serviceAddedTRM.cold.4
+ serviceAddedTRM.cold.5
- -[ueaPluginSystemSettingsMonitor notifyDriverOfBluetoothSetting:andAirplaneMode:]
- -[ueaPluginSystemSettingsMonitor notifyDriverOfBluetoothSetting:andAirplaneMode:].cold.1
- -[ueaPluginSystemSettingsMonitor notifyDriverOfBluetoothSetting:andAirplaneMode:].cold.2
- -[ueaPluginSystemSettingsMonitor notifyDriverOfBluetoothSetting:andAirplaneMode:].cold.3
- -[ueaPluginSystemSettingsMonitor notifyDriverOfBluetoothSetting:andAirplaneMode:].cold.4
- -[ueaPluginSystemSettingsMonitor notifyDriverOfBluetoothSetting:andAirplaneMode:].cold.5
- -[ueaPluginSystemSettingsMonitor notifyDriverOfBluetoothSetting:andAirplaneMode:].cold.6
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCAnalytics.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCAnalyticsLogger.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCObjCType.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCSQLite.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCSQLiteStatement.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCStrings.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCUserDefaults.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCUserNotification.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCUserNotificationManager.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ACCUserNotifications.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/IOUIAngelService.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/IOUserNotification.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/TRMPort.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/TRMPortManager.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/acc_analytics_utilities.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/acc_restricted_mode.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/acc_user_notification.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/accessorydMatchingPlugin.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/common_cf.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/logging_accessories_uea.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/logging_wrapper.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/system_info.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/ueaPluginSystemSettings.o
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Sources/CoreAccessories/Apple/Accessory_Frameworks/CoreAccessories/
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Sources/CoreAccessories/Apple/accessorydMatchingPlugin/
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Sources/CoreAccessories/Common/Common_C/
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Sources/CoreAccessories/Common/Common_CF/
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Sources/CoreAccessories/Common/Common_ObjC/
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Sources/CoreAccessories/Common/SplunkAnalytics/
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Sources/CoreAccessories/Common/SplunkAnalytics/ACCAnalyticsLogger/
- /Library/Caches/com.apple.xbs/20E26F65-FE2D-4094-9D50-92EBD3914167/TemporaryDirectory.nqwfyF/Sources/CoreAccessories/Common/SplunkAnalytics/ACCAnalyticsLogger/SQLite/
- GCC_except_table261
- __IOAccessoryManagerEventCallback_block_invoke.960
- __IOAccessoryManagerEventCallback_block_invoke.960.cold.1
- __IOAccessoryManagerEventCallback_block_invoke.965
- __block_literal_global.1001
- __block_literal_global.1004
- __block_literal_global.1006
- __block_literal_global.1009
- __block_literal_global.1021
- __block_literal_global.1023
- __block_literal_global.322
- __block_literal_global.360
- __block_literal_global.972
- __block_literal_global.981
- __serviceLDCMMitigationStatusChanged_block_invoke.1002
- __serviceLDCMMitigationStatusChanged_block_invoke.1002.cold.1
- __serviceLDCMMitigationStatusChanged_block_invoke.1002.cold.2
- __serviceLDCMMitigationStatusChanged_block_invoke.1002.cold.3
- __serviceLDCMMitigationStatusChanged_block_invoke.1002.cold.4
- _objc_msgSend$notifyDriverOfBluetoothSetting:andAirplaneMode:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "ACMCredential - ACMCredentialDataPKITokenValidated"
+ "ACMCredential - ACMCredentialDataPKITokenValidated2"
+ "ACMGetEnvironmentVariableData"
+ "IOServiceOpen fail kernStatus:%02X, ioConnForService:%04X ioService:%d port:%d"
+ "PearlIDCapability"
+ "notifyDriverOfBluetoothSetting:andAirplaneMode: bt %d, apm %d, port %d"
+ "notifyDriverOfBluetoothSetting:andAirplaneMode:forPrimaryPort:"
+ "v28@0:8B16B20i24"
- "8olRm6C1xqr7AJGpLRnpSw"
- "IOServiceOpen fail kernStatus:%02X, ioConnForService:%04X ioService:%d"
- "notifyDriverOfBluetoothSetting:andAirplaneMode:"
- "notifyDriverOfBluetoothSetting:andAirplaneMode: bt %d, apm %d"

```
