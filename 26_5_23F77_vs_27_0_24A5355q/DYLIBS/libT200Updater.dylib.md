## libT200Updater.dylib

> `/usr/lib/updaters/libT200Updater.dylib`

```diff

-1.0.0.7.66
-  __TEXT.__text: 0x109a4
-  __TEXT.__auth_stubs: 0x710
-  __TEXT.__cstring: 0x490c
-  __TEXT.__const: 0x1087
-  __TEXT.__oslogstring: 0x1b9
-  __TEXT.__unwind_info: 0x258
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0xe90
-  __AUTH_CONST.__auth_got: 0x388
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0xc60
-  __DATA.__data: 0x10
+1.0.0.8.94
+  __TEXT.__text: 0x12708
+  __TEXT.__cstring: 0x54f5
+  __TEXT.__const: 0x1498
+  __TEXT.__oslogstring: 0x1bd
+  __TEXT.__unwind_info: 0x2a0
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0xee8
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x90
+  __AUTH_CONST.__cfstring: 0xe80
+  __AUTH_CONST.__auth_got: 0x3d8
+  __DATA.__data: 0x150
   __DATA.__common: 0xd0
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
-  UUID: 5499F7B5-625F-343C-879B-6EF33F29F686
-  Functions: 415
-  Symbols:   1463
-  CStrings:  764
+  UUID: C3375CA0-FFAA-339C-8C10-5A2BACACD920
+  Functions: 410
+  Symbols:   1481
+  CStrings:  845
 
Symbols:
+ _BC__getNumOfGasGaugeSupported
+ _BC__selectGG
+ _CFErrorCopyUserInfo
+ _IOIteratorNext
+ _IOServiceGetMatchingServices
+ _T200GetBatteryModelIDs
+ _T200GetBatteryModelIDs.cold.1
+ _T200GetBatteryModelIDs.cold.2
+ _T200GetBatteryModelIDs.cold.3
+ _T200GetBatteryModelIDs.cold.4
+ _T200UpdaterExecCommand.cold.1
+ _T200UpdaterExecCommand.cold.2
+ _T200UpdaterExecCommand.cold.3
+ _T200UpdaterExecCommand.cold.4
+ _T200UpdaterGetTagsWithLogging.cold.10
+ _T200UpdaterGetTagsWithLogging.cold.8
+ _T200UpdaterGetTagsWithLogging.cold.9
+ __Block_object_assign
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __T200GetChipIdFromDT
+ __T200GetChipIdFromDT.cold.1
+ __T200GetChipIdFromDT.cold.2
+ __T200GetChipIdFromDT.cold.3
+ __T200GetChipIdFromDT.cold.4
+ __T200GetChipIdFromDT.cold.5
+ __T200GetChipIdFromDT.cold.6
+ __T200GetChipIdFromDT.cold.7
+ __T200GetNumActiveBattery
+ __T200GetNumEnabledBMUFromDT
+ __T200GetNumEnabledBMUFromDT.cold.1
+ __T200GetNumEnabledBMUFromDT.cold.2
+ __T200GetNumEnabledBMUFromDT.cold.3
+ __T200GetNumEnabledBMUFromDT.cold.4
+ __T200UpdaterExecCommand.parallel_mutex
+ ____T200UpdaterExecCommand_block_invoke
+ ___block_descriptor_tmp
+ ___copy_helper_block_8_32r
+ ___destroy_helper_block_8_32r
+ __isBatteryDevFused
+ __isBatteryDevFused.cold.1
+ __oidSha3_384
+ __performBatteryUpdateThread
+ __performBatteryUpdateThread.cold.1
+ __performBatteryUpdateThread.cold.10
+ __performBatteryUpdateThread.cold.100
+ __performBatteryUpdateThread.cold.101
+ __performBatteryUpdateThread.cold.11
+ __performBatteryUpdateThread.cold.12
+ __performBatteryUpdateThread.cold.13
+ __performBatteryUpdateThread.cold.14
+ __performBatteryUpdateThread.cold.15
+ __performBatteryUpdateThread.cold.16
+ __performBatteryUpdateThread.cold.17
+ __performBatteryUpdateThread.cold.18
+ __performBatteryUpdateThread.cold.19
+ __performBatteryUpdateThread.cold.2
+ __performBatteryUpdateThread.cold.20
+ __performBatteryUpdateThread.cold.21
+ __performBatteryUpdateThread.cold.22
+ __performBatteryUpdateThread.cold.23
+ __performBatteryUpdateThread.cold.24
+ __performBatteryUpdateThread.cold.25
+ __performBatteryUpdateThread.cold.26
+ __performBatteryUpdateThread.cold.27
+ __performBatteryUpdateThread.cold.28
+ __performBatteryUpdateThread.cold.29
+ __performBatteryUpdateThread.cold.3
+ __performBatteryUpdateThread.cold.30
+ __performBatteryUpdateThread.cold.31
+ __performBatteryUpdateThread.cold.32
+ __performBatteryUpdateThread.cold.33
+ __performBatteryUpdateThread.cold.34
+ __performBatteryUpdateThread.cold.35
+ __performBatteryUpdateThread.cold.36
+ __performBatteryUpdateThread.cold.37
+ __performBatteryUpdateThread.cold.38
+ __performBatteryUpdateThread.cold.39
+ __performBatteryUpdateThread.cold.4
+ __performBatteryUpdateThread.cold.40
+ __performBatteryUpdateThread.cold.41
+ __performBatteryUpdateThread.cold.42
+ __performBatteryUpdateThread.cold.43
+ __performBatteryUpdateThread.cold.44
+ __performBatteryUpdateThread.cold.45
+ __performBatteryUpdateThread.cold.46
+ __performBatteryUpdateThread.cold.47
+ __performBatteryUpdateThread.cold.48
+ __performBatteryUpdateThread.cold.49
+ __performBatteryUpdateThread.cold.5
+ __performBatteryUpdateThread.cold.50
+ __performBatteryUpdateThread.cold.51
+ __performBatteryUpdateThread.cold.52
+ __performBatteryUpdateThread.cold.53
+ __performBatteryUpdateThread.cold.54
+ __performBatteryUpdateThread.cold.55
+ __performBatteryUpdateThread.cold.56
+ __performBatteryUpdateThread.cold.57
+ __performBatteryUpdateThread.cold.58
+ __performBatteryUpdateThread.cold.59
+ __performBatteryUpdateThread.cold.6
+ __performBatteryUpdateThread.cold.60
+ __performBatteryUpdateThread.cold.61
+ __performBatteryUpdateThread.cold.62
+ __performBatteryUpdateThread.cold.63
+ __performBatteryUpdateThread.cold.64
+ __performBatteryUpdateThread.cold.65
+ __performBatteryUpdateThread.cold.66
+ __performBatteryUpdateThread.cold.67
+ __performBatteryUpdateThread.cold.68
+ __performBatteryUpdateThread.cold.69
+ __performBatteryUpdateThread.cold.7
+ __performBatteryUpdateThread.cold.70
+ __performBatteryUpdateThread.cold.71
+ __performBatteryUpdateThread.cold.72
+ __performBatteryUpdateThread.cold.73
+ __performBatteryUpdateThread.cold.74
+ __performBatteryUpdateThread.cold.75
+ __performBatteryUpdateThread.cold.76
+ __performBatteryUpdateThread.cold.77
+ __performBatteryUpdateThread.cold.78
+ __performBatteryUpdateThread.cold.79
+ __performBatteryUpdateThread.cold.8
+ __performBatteryUpdateThread.cold.80
+ __performBatteryUpdateThread.cold.81
+ __performBatteryUpdateThread.cold.82
+ __performBatteryUpdateThread.cold.83
+ __performBatteryUpdateThread.cold.84
+ __performBatteryUpdateThread.cold.85
+ __performBatteryUpdateThread.cold.86
+ __performBatteryUpdateThread.cold.87
+ __performBatteryUpdateThread.cold.88
+ __performBatteryUpdateThread.cold.89
+ __performBatteryUpdateThread.cold.9
+ __performBatteryUpdateThread.cold.90
+ __performBatteryUpdateThread.cold.91
+ __performBatteryUpdateThread.cold.92
+ __performBatteryUpdateThread.cold.93
+ __performBatteryUpdateThread.cold.94
+ __performBatteryUpdateThread.cold.95
+ __performBatteryUpdateThread.cold.96
+ __performBatteryUpdateThread.cold.97
+ __performBatteryUpdateThread.cold.98
+ __performBatteryUpdateThread.cold.99
+ _computeCRC32.crc_table
+ _createCFErrorWithBatteryIndex
+ _createCFErrorWithBatteryIndex.cold.1
+ _createCFErrorWithBatteryIndex.cold.2
+ _createCFErrorWithBatteryIndex.cold.3
+ _createCFErrorWithBatteryIndex.cold.4
+ _createCFErrorWithUnderlyingError
+ _createCFErrorWithUnderlyingError.cold.1
+ _dispatch_apply
+ _dispatch_get_global_queue
+ _display_info_mutex
+ _foutput_mutex
+ _gas_gauge_selection_mutex
+ _kCFErrorUnderlyingErrorKey
+ _kT200ErrorBatteryIndexKey
+ _kT200ErrorBatteryModelIDKey
+ _kT200OptionBundleDataDict
+ _kT200OptionRestoreOptions
+ _kT200OptionT200Firmware
+ _kT200TagDisableParallelUpdate
+ _kT200TagSingleBatteryRestore
+ _kT200UpdaterBatteryIndex
+ _kT200UpdaterNumOfActiveBMUs
+ _log_mutex
+ _oidSha3_384
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
+ _puts
- _CopyHWVersion
- _CopyHWVersion.cold.1
- _OUTLINED_FUNCTION_25
- _OUTLINED_FUNCTION_26
- _OUTLINED_FUNCTION_27
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_29
- _READ_DATA__getVIQTReadings
- _T200UpdaterCopyFirmwareWithLogging.cold.15
- _T200UpdaterCopyFirmwareWithLogging.cold.16
- _T200UpdaterIsDone.cold.2
- __T200GetBMUID.cold.7
- __T200GetBMUID.cold.8
- __T200GetBMUID.cold.9
- __T200UpdaterExecCommand
- __T200UpdaterExecCommand.cold.1
- __T200UpdaterExecCommand.cold.10
- __T200UpdaterExecCommand.cold.100
- __T200UpdaterExecCommand.cold.101
- __T200UpdaterExecCommand.cold.102
- __T200UpdaterExecCommand.cold.103
- __T200UpdaterExecCommand.cold.104
- __T200UpdaterExecCommand.cold.105
- __T200UpdaterExecCommand.cold.106
- __T200UpdaterExecCommand.cold.107
- __T200UpdaterExecCommand.cold.108
- __T200UpdaterExecCommand.cold.109
- __T200UpdaterExecCommand.cold.11
- __T200UpdaterExecCommand.cold.110
- __T200UpdaterExecCommand.cold.111
- __T200UpdaterExecCommand.cold.112
- __T200UpdaterExecCommand.cold.113
- __T200UpdaterExecCommand.cold.114
- __T200UpdaterExecCommand.cold.115
- __T200UpdaterExecCommand.cold.12
- __T200UpdaterExecCommand.cold.13
- __T200UpdaterExecCommand.cold.14
- __T200UpdaterExecCommand.cold.15
- __T200UpdaterExecCommand.cold.16
- __T200UpdaterExecCommand.cold.17
- __T200UpdaterExecCommand.cold.18
- __T200UpdaterExecCommand.cold.19
- __T200UpdaterExecCommand.cold.2
- __T200UpdaterExecCommand.cold.20
- __T200UpdaterExecCommand.cold.21
- __T200UpdaterExecCommand.cold.22
- __T200UpdaterExecCommand.cold.23
- __T200UpdaterExecCommand.cold.24
- __T200UpdaterExecCommand.cold.25
- __T200UpdaterExecCommand.cold.26
- __T200UpdaterExecCommand.cold.27
- __T200UpdaterExecCommand.cold.28
- __T200UpdaterExecCommand.cold.29
- __T200UpdaterExecCommand.cold.3
- __T200UpdaterExecCommand.cold.30
- __T200UpdaterExecCommand.cold.31
- __T200UpdaterExecCommand.cold.32
- __T200UpdaterExecCommand.cold.33
- __T200UpdaterExecCommand.cold.34
- __T200UpdaterExecCommand.cold.35
- __T200UpdaterExecCommand.cold.36
- __T200UpdaterExecCommand.cold.37
- __T200UpdaterExecCommand.cold.38
- __T200UpdaterExecCommand.cold.39
- __T200UpdaterExecCommand.cold.4
- __T200UpdaterExecCommand.cold.40
- __T200UpdaterExecCommand.cold.41
- __T200UpdaterExecCommand.cold.42
- __T200UpdaterExecCommand.cold.43
- __T200UpdaterExecCommand.cold.44
- __T200UpdaterExecCommand.cold.45
- __T200UpdaterExecCommand.cold.46
- __T200UpdaterExecCommand.cold.47
- __T200UpdaterExecCommand.cold.48
- __T200UpdaterExecCommand.cold.49
- __T200UpdaterExecCommand.cold.5
- __T200UpdaterExecCommand.cold.50
- __T200UpdaterExecCommand.cold.51
- __T200UpdaterExecCommand.cold.52
- __T200UpdaterExecCommand.cold.53
- __T200UpdaterExecCommand.cold.54
- __T200UpdaterExecCommand.cold.55
- __T200UpdaterExecCommand.cold.56
- __T200UpdaterExecCommand.cold.57
- __T200UpdaterExecCommand.cold.58
- __T200UpdaterExecCommand.cold.59
- __T200UpdaterExecCommand.cold.6
- __T200UpdaterExecCommand.cold.60
- __T200UpdaterExecCommand.cold.61
- __T200UpdaterExecCommand.cold.62
- __T200UpdaterExecCommand.cold.63
- __T200UpdaterExecCommand.cold.64
- __T200UpdaterExecCommand.cold.65
- __T200UpdaterExecCommand.cold.66
- __T200UpdaterExecCommand.cold.67
- __T200UpdaterExecCommand.cold.68
- __T200UpdaterExecCommand.cold.69
- __T200UpdaterExecCommand.cold.7
- __T200UpdaterExecCommand.cold.70
- __T200UpdaterExecCommand.cold.71
- __T200UpdaterExecCommand.cold.72
- __T200UpdaterExecCommand.cold.73
- __T200UpdaterExecCommand.cold.74
- __T200UpdaterExecCommand.cold.75
- __T200UpdaterExecCommand.cold.76
- __T200UpdaterExecCommand.cold.77
- __T200UpdaterExecCommand.cold.78
- __T200UpdaterExecCommand.cold.79
- __T200UpdaterExecCommand.cold.8
- __T200UpdaterExecCommand.cold.80
- __T200UpdaterExecCommand.cold.81
- __T200UpdaterExecCommand.cold.82
- __T200UpdaterExecCommand.cold.83
- __T200UpdaterExecCommand.cold.84
- __T200UpdaterExecCommand.cold.85
- __T200UpdaterExecCommand.cold.86
- __T200UpdaterExecCommand.cold.87
- __T200UpdaterExecCommand.cold.88
- __T200UpdaterExecCommand.cold.89
- __T200UpdaterExecCommand.cold.9
- __T200UpdaterExecCommand.cold.90
- __T200UpdaterExecCommand.cold.91
- __T200UpdaterExecCommand.cold.92
- __T200UpdaterExecCommand.cold.93
- __T200UpdaterExecCommand.cold.94
- __T200UpdaterExecCommand.cold.95
- __T200UpdaterExecCommand.cold.96
- __T200UpdaterExecCommand.cold.97
- __T200UpdaterExecCommand.cold.98
- __T200UpdaterExecCommand.cold.99
- __check_update_needed.cold.10
- __check_update_needed.cold.11
- __check_update_needed.cold.9
- __commitImageSMCIF.cold.3
- __commitImageSMCIF.cold.4
- __getInfoSMCIF.cold.11
- __getInfoSMCIF.cold.12
- __getInfoSMCIF.cold.13
- __getInfoSMCIF.cold.14
- __getInfoSMCIF.cold.15
- __updateBMUTags.cold.21
- __updateBMUTags.cold.22
- __updateBMUTags.cold.23
- _getChemistryId
- _getChemistryId.cold.1
- _getChemistryId.cold.2
CStrings:
+ "\t\t<BoardID>0x%X</BoardID> \n"
+ "\t\t<ModelID>0x%X</ModelID> \n"
+ "\t<BatteryIndex>%d</BatteryIndex> \n"
+ " [Battery %d]"
+ "%@%@"
+ "%@%@; %@: %u"
+ "%@%@; %u"
+ "%@%d"
+ "%@%d%@"
+ "%s:%d BMUID 0x%X \n"
+ "%s:%d Battery BoardID: 0x%X. \n"
+ "%s:%d Battery update failed for Battery Index: %d with error: %d\n"
+ "%s:%d Battery[%d] ModelID: 0x%X \n"
+ "%s:%d BoardId from IODT 0x%X \n"
+ "%s:%d ChipId from IODT 0x%X \n"
+ "%s:%d DeviceInfo Dict\n"
+ "%s:%d Disable Parallel Update: %d \n"
+ "%s:%d End queryInfo for Battery Index: %d \n"
+ "%s:%d End. Return: %d \n"
+ "%s:%d Error: Failed to performVersionCheck for Config for Battery Idx: %d. \n"
+ "%s:%d Error: Failed to performVersionCheck for DNVD for Battery Idx: %d. \n"
+ "%s:%d Error: Failed to performVersionCheck for FW for Battery Idx: %d. \n"
+ "%s:%d FW Override: %d \n"
+ "%s:%d Is Battery DevFused? %d \n"
+ "%s:%d Looking for FirmwareData in BundleDataDict\n"
+ "%s:%d NumEnabledBMU from IODT 0x%X \n"
+ "%s:%d NumSupportedBMU from IODT 0x%X \n"
+ "%s:%d Number of Active Battery (%d) exceeds Max Number of Supported Battery (%d). \n"
+ "%s:%d Number of Active Battery for FW Updater: %d \n"
+ "%s:%d Number of Active Battery: %d \n"
+ "%s:%d Number of AppleGasGaugeUpdate supported: %d \n"
+ "%s:%d Options Dict\n"
+ "%s:%d PSimPresent from IODT 0x%X \n"
+ "%s:%d Parallel battery update failed\n"
+ "%s:%d Performing Parallel battery updates for %d batteries\n"
+ "%s:%d Performing Sequential battery updates for %d batteries\n"
+ "%s:%d Performing single battery restore for Battery Index: %d\n"
+ "%s:%d Sequential battery update failed\n"
+ "%s:%d Single Battery Restore: %d (Target Battery Index: %d) \n"
+ "%s:%d Single battery restore failed\n"
+ "%s:%d Single battery restore failed for Battery Index: %d with error: %d\n"
+ "%s:%d Skipping update - BoardID mismatch: DT=0x%X, Battery=0x%X, battery is dev fused and internal restore \n"
+ "%s:%d Skipping update - BoardID or ChipID parameter not present in EDM, battery is dev fused and internal restore \n"
+ "%s:%d Skipping update - Internal device with battery-state=-1.\n"
+ "%s:%d Start queryInfo for Battery Index: %d \n"
+ "%s:%d Update is required for Battery Idx %d. \n"
+ "%s:%d update required for Battery Idx %d? DNVD: %d, Config: %d, Firmware: %d. \n"
+ "*batModelIDs"
+ ","
+ "ActiveBMUs"
+ "BMU"
+ "BatFWRestore: %s"
+ "BatFWUpdater: %s"
+ "BatFWUpdater: Error - cannot open AppleSMC"
+ "BatFWUpdater: Failed to BC__connect"
+ "BatFWUpdater: GasGauge Registry Value %d \n"
+ "BatFWUpdater: Select GG %d for side channel communication\n"
+ "BatFWUpdater: [%d] BC__commitImage \n"
+ "BatFWUpdater: [%d] BC__getInfo \n"
+ "BatFWUpdater: [%d] BC__sendImage \n"
+ "BatFWUpdater: [%d] BC__sendImage CRC32: 0x%08X (data_length: %llu bytes)\n"
+ "BatFWUpdater: [%d] BC__startUpdate \n"
+ "BatFWUpdater: [%d] Connect to AppleGasGaugeUpdate PackIndex:%d \n"
+ "BatFWUpdater: [%d] Error committing image. 0x%X \n"
+ "BatFWUpdater: [%d] Error getting info: 0x%X \n"
+ "BatFWUpdater: [%d] Error getting info: 0x%X. Retrying... \n"
+ "BatFWUpdater: [%d] Error starting update: 0x%X \n"
+ "BatFWUpdater: [%d] Error starting update: 0x%X. Retrying... \n"
+ "BatFWUpdater: [%d] Error writing image. 0x%X \n"
+ "BatFWUpdater: [%d] FW:%u CFG:%u DNVD1:%u DNVD2:%u BL:%u UniqueId:%u Chemistry:%u hwId:0x%08X isTwoStageSupported:%u \n"
+ "BatFWUpdater: [%d] Failed to BC__GasGauge_connect \n"
+ "BatFWUpdater: cannot open gas gauge device "
+ "BatteryIndex"
+ "BatteryIndexInfo is NULL"
+ "BatteryModelID"
+ "BundleDataDict"
+ "DisableParallelUpdate"
+ "Missing kT200OptionFirmwareData and kT200OptionBundleDataDict"
+ "Options is NULL"
+ "PackIndex"
+ "RestoreOptions"
+ "SingleBatteryRestore"
+ "T200: Failed to allocate parallel error tracking"
+ "T200: Get Firmware Image(s) Failed [ChemID: %u]"
+ "T200Firmware"
+ "T200GetBatteryModelIDs"
+ "T200GetBoardIdFromDT"
+ "Unable to get BMUID"
+ "Unable to get kT200TagMeasurementFirmwarePlist"
+ "Unable to get kT200TagResponseFirmwareTicket"
+ "[%d] %s:%d  show fOptions \n"
+ "[%d] %s:%d BC__commitImage failed commStatus=0x%X"
+ "[%d] %s:%d BC__sendImage failed commStatus=0x%X \n"
+ "[%d] %s:%d Battery UniqueID is Zero. Use Battery Unique ID from getInfo.\n"
+ "[%d] %s:%d Battery UniqueID: %u \n"
+ "[%d] %s:%d Certificate BC__sendImage failed commStatus=0x%X \n"
+ "[%d] %s:%d DigestMap BC__sendImage failed commStatus=0x%X \n"
+ "[%d] %s:%d Do we need to update(0-No 1-Yes)= %d, current veridian fw: %d set-id:%d    new_firmware:%d new_set-id:%d \n"
+ "[%d] %s:%d Does Image updated (0-No 1-Yes)= %d, Veridian Image Loaded: %d set-id:%d    Veridian Image Requested:%d new_set-id:%d \n"
+ "[%d] %s:%d ERROR:Failed Updating the Configuration "
+ "[%d] %s:%d ERROR:Failed Updating the Configuration \n"
+ "[%d] %s:%d ERROR:Failed Updating the DNVD "
+ "[%d] %s:%d ERROR:Failed Updating the DNVD \n"
+ "[%d] %s:%d ERROR:Failed Updating the Firmware "
+ "[%d] %s:%d ERROR:Failed Updating the Firmware \n"
+ "[%d] %s:%d End"
+ "[%d] %s:%d End \n"
+ "[%d] %s:%d End  Failed  Error:%d "
+ "[%d] %s:%d End  Failed  Error:%d  \n"
+ "[%d] %s:%d End Crypto \n"
+ "[%d] %s:%d End Failed with %d  \n"
+ "[%d] %s:%d End Send Binary Image %d  \n"
+ "[%d] %s:%d End Send Binary Image %d  Faild targetUpdaterError=%d \n"
+ "[%d] %s:%d End Send Certificate smc API \n"
+ "[%d] %s:%d End Send DigestMap+Crypto smc API \n"
+ "[%d] %s:%d End Send Manifest smc API \n"
+ "[%d] %s:%d End performNextStage for Battery Index: %d \n"
+ "[%d] %s:%d End with error %d \n"
+ "[%d] %s:%d Entitlment update successful  \n"
+ "[%d] %s:%d Failed to commitImage with status %d \n"
+ "[%d] %s:%d Failed to send bin with status %d \n"
+ "[%d] %s:%d Failed with Error:%d  \n"
+ "[%d] %s:%d In BootedOS, performNextStage is Skipped if isTwoStageSupported is False \n"
+ "[%d] %s:%d Manifest BC__sendImage failed commStatus=0x%X \n"
+ "[%d] %s:%d Send dummy Digest Dictionary for Access Mode Enable \n"
+ "[%d] %s:%d Signal Start Update \n"
+ "[%d] %s:%d Skip Start Update command \n"
+ "[%d] %s:%d Skip updating as this is not supported cell-id \n"
+ "[%d] %s:%d Skipping Second stage in update \n"
+ "[%d] %s:%d Skipping update \n"
+ "[%d] %s:%d Start"
+ "[%d] %s:%d Start \n"
+ "[%d] %s:%d Start  \n"
+ "[%d] %s:%d Start Send DigestMap+Crypto smc API \n"
+ "[%d] %s:%d Start Send Manifest smc API \n"
+ "[%d] %s:%d Start performNextStage for Battery Index: %d \n"
+ "[%d] %s:%d Success. Valid Configuration Version (%u) found on HW. Skip Retry. \n"
+ "[%d] %s:%d Success. Valid DNVD2 Version (%u) found on HW. Skip Retry. \n"
+ "[%d] %s:%d Success. Valid Firmware Version (%u) found on HW. Skip Retry. \n"
+ "[%d] %s:%d Update status:dnvd:%d conf:%d firmware:%d \n"
+ "[%d] %s:%d Updater Status (%d) before retry. \n"
+ "[%d] %s:%d Veridian Fw  detected maj=%d med=%d min=%d rev=%d \n"
+ "[%d] %s:%d _send_bin failed, commStatus=0x%X, Retry...%d \n"
+ "[%d] %s:%d cell_ID %d not supported. Error: %d \n"
+ "[%d] %s:%d cert len:%u \n"
+ "[%d] %s:%d commitImage status  %d \n"
+ "[%d] %s:%d digestmap len:%u \n"
+ "[%d] %s:%d end \n"
+ "[%d] %s:%d failed with result =%d \n"
+ "[%d] %s:%d hwVersionstr = %s  \n"
+ "[%d] %s:%d image len:%u \n"
+ "[%d] %s:%d manifest len:%u \n"
+ "[%d] %s:%d sendbin status  %d \n"
+ "[%d] %s:%d set_id_0=%d set_id_1=%d set_id_2=%d \n"
+ "[%d] %s:%d start \n"
+ "[%d] %s:%d start Send Binary Image to Update Configuration SMC API, update %d \n"
+ "[%d] %s:%d start Send Binary Image to Update DNVD SMC API, update %d \n"
+ "[%d] %s:%d start Send Binary Image to Update Firmware SMC API, update %d \n"
+ "[%d] %s:%d start Send Certificate smc API  \n"
+ "_T200GetNumActiveBattery"
+ "_T200UpdaterExecCommand_block_invoke"
+ "_getBatteryBoardID"
+ "_isBatteryDevFused"
+ "_performBatteryUpdateThread"
+ "batModelIDs"
+ "batteryErrors && batteryResults"
+ "batteryIndexMsg"
+ "batteryInfo"
+ "bundleDataDict"
+ "chip_id"
+ "deviceInfo"
+ "numBatteryCount"
+ "numOfActiveBatteryRef != NULL"
+ "result == kT200Success || t200UpdaterData->batteryRestoreOptions.internalRestore == FALSE"
+ "subDeviceInfo && (CFGetTypeID(subDeviceInfo)==CFDictionaryGetTypeID())"
+ "t200UpdaterData->batteryInfo[batIdx].batteryUniqueID == uint32Val"
+ "t200UpdaterData->batteryInfo[batIdx].chipID == uint32Val"
+ "t200UpdaterData->batteryInfo[batIdx].productionMode == boolVal"
+ "t200UpdaterData->batteryInfo[batIdx].targetUpdaterError = %d"
+ "t200UpdaterData->batteryInfo[batIdx].targetUpdaterError == kT200Success"
+ "userInfo"
+ "v16@?0Q8"
- "%s:%d  show fOptions \n"
- "%s:%d BC__commitImage failed commStatus=0x%X"
- "%s:%d BC__sendImage failed commStatus=0x%X \n"
- "%s:%d BMUID %08x \n"
- "%s:%d Certificate BC__sendImage failed commStatus=0x%X \n"
- "%s:%d ChipId from IODT %08x \n"
- "%s:%d DigestMap BC__sendImage failed commStatus=0x%X \n"
- "%s:%d Do we need to update(0-No 1-Yes)= %d, current veridian fw: %d set-id:%d    new_firmware:%d new_set-id:%d \n"
- "%s:%d Does Image updated (0-No 1-Yes)= %d, Veridian Image Loaded: %d set-id:%d    Veridian Image Requested:%d new_set-id:%d \n"
- "%s:%d ERROR:Failed Updating the Configuration "
- "%s:%d ERROR:Failed Updating the Configuration \n"
- "%s:%d ERROR:Failed Updating the DNVD "
- "%s:%d ERROR:Failed Updating the DNVD \n"
- "%s:%d ERROR:Failed Updating the Firmware "
- "%s:%d ERROR:Failed Updating the Firmware \n"
- "%s:%d End"
- "%s:%d End  Failed  Error:%d "
- "%s:%d End  Failed  Error:%d  \n"
- "%s:%d End Crypto \n"
- "%s:%d End Failed with %d  \n"
- "%s:%d End Send Binary Image %d  \n"
- "%s:%d End Send Binary Image %d  Faild targetUpdaterError=%d \n"
- "%s:%d End Send Certificate smc API \n"
- "%s:%d End Send DigestMap+Crypto smc API \n"
- "%s:%d End Send Manifest smc API \n"
- "%s:%d End with error %d \n"
- "%s:%d Entitlment update successful  \n"
- "%s:%d Error: Failed to performVersionCheck for Config. \n"
- "%s:%d Error: Failed to performVersionCheck for DNVD. \n"
- "%s:%d Error: Failed to performVersionCheck for FW. \n"
- "%s:%d Failed getting hw_version\n"
- "%s:%d Failed to send bin with status %d \n"
- "%s:%d Failed to wait return status = %d \n"
- "%s:%d Failed with Error:%d  \n"
- "%s:%d In BootedOS, performNextStage is Skipped if isTwoStageSupported is False \n"
- "%s:%d Manifest BC__sendImage failed commStatus=0x%X \n"
- "%s:%d NumEnabled from IODT %08x \n"
- "%s:%d NumEnabledBMU %08x \n"
- "%s:%d NumSupported from IODT %08x \n"
- "%s:%d NumSupportedBMU %08x \n"
- "%s:%d PSimPresent from IODT %08x \n"
- "%s:%d Send dummy Digest Dictionary for Access Mode Enable \n"
- "%s:%d Signal Start Update \n"
- "%s:%d Skip Start Update command \n"
- "%s:%d Skip updating as this is not supported cell-id \n"
- "%s:%d Skipping Second stage in update \n"
- "%s:%d Skipping update \n"
- "%s:%d Start"
- "%s:%d Start Send DigestMap+Crypto smc API \n"
- "%s:%d Start Send Manifest smc API \n"
- "%s:%d Success. Valid Configuration Version (%u) found on HW. Skip Retry. \n"
- "%s:%d Success. Valid DNVD2 Version (%u) found on HW. Skip Retry. \n"
- "%s:%d Success. Valid Firmware Version (%u) found on HW. Skip Retry. \n"
- "%s:%d Update NOT required. \n"
- "%s:%d Update status:dnvd:%d conf:%d firmware:%d \n"
- "%s:%d Updater Status (%d) before retry. \n"
- "%s:%d Veridian Fw  detected maj=%d med=%d min=%d rev=%d \n"
- "%s:%d _send_bin failed, commStatus=0x%X, Retry...%d \n"
- "%s:%d cell_ID %d not supported. Error: %d \n"
- "%s:%d cert len:%u \n"
- "%s:%d chemistry=%u silicon_ver=%s\n"
- "%s:%d digestmap len:%u \n"
- "%s:%d fOptions getting the kT200OptionOptions \n"
- "%s:%d failed with result =%d \n"
- "%s:%d hwVersionstr = %s  \n"
- "%s:%d image len:%u \n"
- "%s:%d manifest len:%u \n"
- "%s:%d sendbin status  %d \n"
- "%s:%d set_id_0=%d set_id_1=%d set_id_2=%d \n"
- "%s:%d show deviceInfoRef \n"
- "%s:%d start Send Binary Image to Update Configuration SMC API, update %d \n"
- "%s:%d start Send Binary Image to Update DNVD SMC API, update %d \n"
- "%s:%d start Send Binary Image to Update Firmware SMC API, update %d \n"
- "%s:%d start Send Certificate smc API  \n"
- "%s:%d update required? DNVD: %d, Config: %d, Firmware: %d. \n"
- "</VIQTReadings> \n"
- "<VIQTReadings> \n"
- "BC__commitImage"
- "BC__sendImage"
- "BC__startUpdate"
- "CFDictionaryGetValue"
- "CFNumberGetValue((CFNumberRef)tmp, kCFNumberSInt64Type, &chemistryID_sint64)"
- "CommStatus = %d"
- "CopyHWVersion"
- "Error committing image. 0x%X \n"
- "Error getting info: 0x%X \n"
- "Error getting info: 0x%X. Retrying... \n"
- "Error starting update: 0x%X \n"
- "Error starting update: 0x%X. Retrying... \n"
- "Error writing image. 0x%X \n"
- "Error: fOutput is NULL."
- "Failed to BC__GasGauge_connect"
- "GasGauge Registry Value %d\n"
- "Missing ChemistryID"
- "Missing HWVersion"
- "Missing device info"
- "Skipping update on internal device with battery-state=-1.\n"
- "T200: Get Firmware Image(s) Failed"
- "T200Options"
- "T200Parameters"
- "TATSU request dict is NULL"
- "_waitTillTargetUpdaterReady"
- "cannot open gas gauge device"
- "chemistryID!=0"
- "deviceInfoRef"
- "fw:%u cfg:%u dnvd1:%u dnvd2:%u crypto:%u chipId:%u chemistry:%u hwId:%u isTwoStageSupported:%u \n"
- "getChemistryId"
- "hw_version!=NULL"
- "result == kT200Success || t200UpdaterData->internalRestore == FALSE"
- "t200UpdaterData->battarey_id == uint32Val"
- "t200UpdaterData->chipID == uint32Val"
- "t200UpdaterData->fOutput"
- "t200UpdaterData->productionMode == boolVal"
- "t200UpdaterData->targetUpdaterError = %d"
- "t200UpdaterData->targetUpdaterError == kT200Success"
- "tmp && (CFGetTypeID(tmp)==CFDictionaryGetTypeID())"
- "tmp && (CFGetTypeID(tmp)==CFNumberGetTypeID())"
- "tmp && (CFGetTypeID(tmp)==CFStringGetTypeID())"

```
