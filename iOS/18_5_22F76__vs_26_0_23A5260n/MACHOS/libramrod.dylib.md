## libramrod.dylib

> `/usr/lib/libramrod.dylib`

```diff

-3196.122.1.0.0
-  __TEXT.__text: 0xe2620
-  __TEXT.__auth_stubs: 0x2880
-  __TEXT.__objc_methlist: 0x109c
-  __TEXT.__cstring: 0x28a1a
-  __TEXT.__const: 0x94938
-  __TEXT.__gcc_except_tab: 0xb20
-  __TEXT.__oslogstring: 0x1ad2
-  __TEXT.__unwind_info: 0x1d80
-  __TEXT.__eh_frame: 0x410
-  __TEXT.__objc_classname: 0x18c
-  __TEXT.__objc_methname: 0x2751
-  __TEXT.__objc_methtype: 0xb58
-  __TEXT.__objc_stubs: 0x2740
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x1f10
-  __DATA_CONST.__objc_classlist: 0x90
+3476.0.6.0.1
+  __TEXT.__text: 0xd7b64
+  __TEXT.__auth_stubs: 0x2800
+  __TEXT.__objc_methlist: 0x106c
+  __TEXT.__cstring: 0x28348
+  __TEXT.__const: 0x94860
+  __TEXT.__gcc_except_tab: 0xb60
+  __TEXT.__oslogstring: 0x9e5
+  __TEXT.__unwind_info: 0x1c10
+  __TEXT.__eh_frame: 0x3c0
+  __TEXT.__objc_classname: 0x17d
+  __TEXT.__objc_methname: 0x272d
+  __TEXT.__objc_methtype: 0xb47
+  __TEXT.__objc_stubs: 0x2720
+  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__const: 0x1f78
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc08
-  __AUTH_CONST.__auth_got: 0x1458
-  __AUTH_CONST.__const: 0x1f50
-  __AUTH_CONST.__cfstring: 0xbfc0
-  __AUTH_CONST.__objc_const: 0x1990
+  __DATA_CONST.__objc_selrefs: 0xc10
+  __AUTH_CONST.__auth_got: 0x1418
+  __AUTH_CONST.__const: 0x1fd0
+  __AUTH_CONST.__cfstring: 0xb420
+  __AUTH_CONST.__objc_const: 0x18f0
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x5a0
-  __AUTH.__data: 0x858
-  __DATA.__objc_classrefs: 0x120
-  __DATA.__objc_superrefs: 0x80
+  __AUTH.__objc_data: 0x550
+  __AUTH.__data: 0x2b8
+  __DATA.__objc_classrefs: 0x118
+  __DATA.__objc_superrefs: 0x78
   __DATA.__objc_ivar: 0x11c
-  __DATA.__data: 0x2388
-  __DATA.__bss: 0xb00
+  __DATA.__data: 0x2198
+  __DATA.__bss: 0x828
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libimg4.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libpartition2_dynamic.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 148E1288-79FC-314D-A124-41228E54816B
-  Functions: 2718
-  Symbols:   1885
-  CStrings:  7607
+  UUID: 9D3E096C-839F-303B-B6AF-779B951AE1EF
+  Functions: 2549
+  Symbols:   1776
+  CStrings:  7274
 
Symbols:
+ _AMAuthInstallApFtabIsValid
+ _IOUSBDeviceControllerGetService
+ _IOUSBDeviceDescriptionGetProductID
+ _IOUSBDeviceDescriptionSetProductID
+ _checkpoint_closure_context_set_end_time
+ _checkpoint_closure_context_set_start_time
+ _checkpoint_engine_get_statistics
+ _copy_main_usb_controller
+ _dispatch_retain
+ _dispatch_source_get_handle
+ _dlclose
+ _get_main_usb_connection_speed_in_mbps
+ _getsockopt
+ _has_main_connection
+ _is_main_connection
+ _kAMAuthInstallApParameterCertificateEpoch
+ _kCheckpointEngineStatsCheckpointEndTime
+ _kCheckpointEngineStatsCheckpointIsAsyncAwait
+ _kCheckpointEngineStatsCheckpointIsForcedSyncCheckpoint
+ _kCheckpointEngineStatsCheckpointIsRetry
+ _kCheckpointEngineStatsCheckpointPreciseTime
+ _kCheckpointEngineStatsCheckpointStartTime
+ _kCheckpointEngineStatsCheckpointSubenginesKey
+ _kCheckpointEngineStatsCheckpointsKey
+ _kCheckpointEngineStatsEngineIDKey
+ _kImg4TagStr_bapp
+ _kImg4TagStr_bcfg
+ _kImg4TagStr_bnvd
+ _kImg4TagStr_chrm
+ _kImg4TagStr_cmtp
+ _kImg4TagStr_dspf
+ _kImg4TagStr_exrm
+ _kImg4TagStr_ipwr
+ _kImg4TagStr_lhrx
+ _kImg4TagStr_lhtx
+ _kImg4TagStr_odfw
+ _kImg4TagStr_pcfw
+ _kImg4TagStr_pdfw
+ _kImg4TagStr_pgfw
+ _log_ramdisk_network_stats
+ _pthread_sigmask
+ _ramrod_execute_config_set_process_launched_block
+ _ramrod_socket_log_statistics
+ _ramrod_sync_apfs_metrics_nvram
+ _ramrod_sync_apfs_metrics_nvram_checkpoint
+ _ramrod_update_twostage_enabled
+ _ramrod_write_os_info_for_nerd
+ _register_main_connection
- _CFAbsoluteTimeGetCurrent
- _CFArrayCreate
- _CFDataSetLength
- _CFMakeCollectable
- _CFPreferencesCopyValue
- _CFStringCreateWithBytesNoCopy
- _DERApTicketItemSpecs
- _DERDecodeItem
- _DERDecodeItemPartialBuffer
- _DERDecodeItemPartialBufferGetLength
- _DERDecodeSeqContentInit
- _DERDecodeSeqInit
- _DERDecodeSeqNext
- _DERDecodeSequenceContentWithBlock
- _DERDecodeSequenceWithBlock
- _DERNumApTicketItemSpecs
- _DERParseBitString
- _DERParseBoolean
- _DERParseBooleanWithDefault
- _DERParseInteger
- _DERParseInteger64
- _DERParseSequence
- _DERParseSequenceContent
- _DERParseSequenceContentToObject
- _DERParseSequenceToObject
- _IOAllowPowerChange
- _IOConnectMapMemory
- _IOConnectUnmapMemory
- _IORegisterForSystemPower
- _OBJC_CLASS_$_IMG3NorUpdater
- _OBJC_METACLASS_$_IMG3NorUpdater
- _OSThermalNotificationCurrentLevel
- _RAMROD_UPDATE_OPT_UPDATE_GAS_GAUGE
- _batteryThread
- _battery_health_metric_config
- _bq_sealed
- _bq_sleep_mode
- _bq_vlow_enable
- _bq_write_dfchecksum
- _calculateChemicalWeightedRa
- _calculateWra
- _controlOp16
- _controlRead16
- _controlReadS16
- _controlReadU16
- _controlWrite16
- _copyfile_skip_existing_callback
- _drainDataLog
- _dumpBuffer
- _findRaWeightMulitplier
- _gasgauge_close
- _gasgauge_currentlog_entries
- _gasgauge_currentlog_get_entries
- _gasgauge_currentlog_interval
- _gasgauge_currentlog_sleepinterval
- _gasgauge_currentlog_start
- _gasgauge_currentlog_start__
- _gasgauge_currentlog_start_collection
- _gasgauge_currentlog_stop
- _gasgauge_disconnect
- _gasgauge_info
- _gasgauge_open
- _gasgauge_sn
- _gasgauge_start_update_thread
- _gasgauge_swupdate
- _gasgauge_swupdate_log
- _gasgauge_watch
- _gaugeDisableInterrupts
- _gaugeDisconnect
- _gaugeEnableInterrupts
- _getFWVersion
- _ggctl_close_device
- _ggctl_connect
- _ggctl_controlRead16
- _ggctl_controlWrite16
- _ggctl_disconnect
- _ggctl_drainDataLog
- _ggctl_enable_currentlog
- _ggctl_gaugeInterrupts
- _ggctl_get_device_configuration
- _ggctl_get_hdq_state
- _ggctl_hdqBreak
- _ggctl_hdqRead16
- _ggctl_hdqRead8
- _ggctl_hdqWrite8
- _ggctl_map_currentlog
- _ggctl_open_device
- _ggctl_readBlock
- _ggctl_reset
- _ggctl_writeBlock
- _hdqBreak
- _hdqRead16
- _hdqRead8
- _hdqReadS16
- _hdqReadS8
- _hdqReadU16
- _hdqReadU8
- _hdqWrite8
- _image3AESDecryptUsingLocalKey
- _image3AdvanceCursorWithZeroPad
- _image3Discard
- _image3Finalize
- _image3Free
- _image3GetNestedImage
- _image3GetTagSignedNumber
- _image3GetTagString
- _image3GetTagStruct
- _image3GetTagUnsignedNumber
- _image3InstantiateFromBuffer
- _image3InstantiateNew
- _image3Malloc
- _image3PKISignHash
- _image3PKIVerifyHash
- _image3SHA1Generate
- _image3SHA1Partial
- _image3SetTagSignedNumber
- _image3SetTagString
- _image3SetTagStructure
- _image3SetTagUnsignedNumber
- _image3TagIsPresent
- _image3UnFinalize
- _image3ValidateSignature
- _kCFPreferencesCurrentHost
- _kCFPreferencesCurrentUser
- _mount
- _okToLoad
- _os_release
- _pmps_service
- _pthread_attr_setdetachstate
- _pthread_setname_np
- _putchar
- _ramrod_convert_hfs_to_apfs
- _ramrod_copyfile_callback
- _ramrod_device_is_formatted_for_LwVM
- _ramrod_device_is_formatted_for_apfs
- _ramrod_disconnect_battery
- _ramrod_populate_preboot_volume_for_nerd
- _ramrod_sync_conversion_metrics_nvram
- _ramrod_sync_conversion_metrics_nvram_checkpoint
- _ramrod_ticket_create_img3
- _ramrod_ticket_img3_copy_data
- _ramrod_ticket_is_img3
- _readBlock
- _readIMAXAndSOCSmoothData
- _readLifetimeData
- _readRaTableData
- _readRegister
- _readShutdownReasonData
- _realloc
- _registerName
- _service
- _startUpdateThread
- _swupdate_checkpoint
- _uart_close_device
- _uart_open_device
- _writeBatteryDiagnosticData
- _writeBlock
CStrings:
+ "%@ property is not a CFData\n"
+ "%@/%s"
+ "%s/%s.%s"
+ "%s: %@ was not found in the list of available FUD images"
+ "%s: %s (%d)"
+ "%s: %s: copy_available_fud_image_names returned NULL"
+ "%s: %s: failed to convert image name to C string"
+ "%s: Creating directory(%@) to save current OS state"
+ "%s: Dictionary is %@\n"
+ "%s: Failed to allocate path string to save Booted OS state\n"
+ "%s: Failed to allocate string to save the path for the state file\n"
+ "%s: Failed to chmod bootedOsStateFile at %@ errno=%d: (%s)..Deleting the file"
+ "%s: Failed to chown bootedOSStateFile at %@ errno=%d: (%s)..Deleting the file"
+ "%s: Failed to create directory : %@"
+ "%s: Failed to delete BootedOsState file at %@. Error: %@"
+ "%s: Failed to fetch data for %s FUD image."
+ "%s: Failed to get c string representation of the bootedOSStateFile path to fixup permissions..Deleting the file"
+ "%s: Failed to get uid/gid for mobile user to chown the bootedOSState file..Deleting the file at %@"
+ "%s: Failed to set permissions on BootedOSState file..Deleting it"
+ "%s: Failed to write env data to file\n"
+ "%s: Is a NOP please remove this call.\n"
+ "%s: No exiting file\n"
+ "%s: Read the current file so we can modify it\n"
+ "%s: Saving env data to %@"
+ "%s: Successfully fixed up permissions for %@"
+ "%s: Updating file permissions\n"
+ "%s: missing parameters\n"
+ "%{public}s"
+ "B32@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24"
+ "B40@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24^@32"
+ "BootedOSState.plist"
+ "CHECKPOINT_INTERNAL_ERROR(%s): You may not start a checkpoint engine from inside a async checkpoint.\n"
+ "CHECKPOINT_INTERNAL_ERROR(%s): checkpoint engine deallocated out of sequence\n"
+ "CHECKPOINT_INTERNAL_ERROR(%s): checkpoints_dictionary alloc failed\n"
+ "CHECKPOINT_INTERNAL_ERROR(%s): engine id alloc failed\n"
+ "CHECKPOINT_INTERNAL_ERROR(%s): failed to init statistics dictionary\n"
+ "CHECKPOINT_INTERNAL_ERROR(%s): parent is set but we're not in a checkpoint step.\n"
+ "CHECKPOINT_INTERNAL_ERROR(%s): parent stat update alloc failed\n"
+ "CHECKPOINT_INTERNAL_ERROR(%s): subengines alloc failed.\n"
+ "CLOSED"
+ "CLOSE_WAIT"
+ "CLOSING"
+ "Checkpoints"
+ "ConnectionSpeed"
+ "Controller/NeRD"
+ "Cryptexes/Supplemental"
+ "CurrentState"
+ "Disable"
+ "ESTABLISHED"
+ "Enable"
+ "EndTime"
+ "Engine ID"
+ "FIN_WAIT_1"
+ "FIN_WAIT_2"
+ "FUD Firmware %s is FTAB.\n"
+ "ForcedSync"
+ "IsAsyncAwait"
+ "IsRetry"
+ "IsTwoStageSupported"
+ "LAST_ACK"
+ "LISTEN"
+ "Rose finished.\n"
+ "Runtime check for two-stage support: %s"
+ "SYN_RCVD"
+ "SYN_SENT"
+ "StartTime"
+ "Subengines"
+ "TCP connection statistics:\n    connected: %u\n    accepted: %u\n    dropped: %u\n    rxmit timeouts: %u\n    keepalive timeouts: %u\n\n"
+ "TCP packet statistics:\n    total pkts in/out: %u/%u\n    seq pkts in/out: %u/%u\n    ack pkts in/out: %u/%u\n    ooo pkts in: %u (%u bytes)\n    rxmit pkts out: %u (%u bytes)\n    rcvbadsum: %u\n    rcvbadoff: %u\n    rcvmemdrop: %u\n    rcvshort: %u\n    rcvduppack: %u\n    rcvpartduppack: %u\n    fcholdpacket: %u\n    reordered_pkts: %u\n    recovered_pkts: %u\n\n"
+ "TIME_WAIT"
+ "TQ,V_layout"
+ "TimeInNS"
+ "Updater %@ should be skipped for %s.."
+ "UpdaterSupported"
+ "Vinyl updaterSupported missing or returned not supported\n"
+ "ZBM"
+ "[0x%08x] %{public}s"
+ "[0x%08x](warning) %{public}s"
+ "_get_supplemental_preboot_paths"
+ "_layout"
+ "appendImages:"
+ "await_update_appletcon"
+ "checkpoint_engine_pop"
+ "com.apple.restored.roseupdater"
+ "could not create CFNumber for %@\n"
+ "firmware_update_se: Waiting for Rose To Finish\n"
+ "fixup_permissions_for_bootedos_state_file"
+ "ftab"
+ "img4"
+ "layout"
+ "net.inet.tcp.disable_access_to_stats"
+ "net.inet.tcp.stats"
+ "ramrod_splat_commit_proposed_internal"
+ "ramrod_sync_apfs_metrics_nvram"
+ "ramrod_update_twostage_enabled"
+ "ramrod_write_os_info_for_nerd"
+ "setLayout:"
+ "snap-has-combined-images"
+ "snapHasCombinedImages"
+ "sock %3d: already main connection\n"
+ "sock %3d: became main connection\n"
+ "sock %3d: connection summary\n    state: %s (%hhu) options: %#x flags: %#x\n    bytes in/out: %llu/%llu\n    pkts in/out: %llu/%llu\n    bytes ooo in: %llu\n    bytes rxmit out: %llu\n    buffer sizes in/out: %d/%d\n    pending bytes in/out: %d/%d\n    window in/out: %u/%u\n    mss: %u\n    rtt: %u ms\n    rttvar: %u ms"
+ "sock %3d: could not query TCP_CONNECTION_INFO: %s"
+ "sock %3d: rejected duplicate main connection\n"
+ "supplemental"
+ "unable to lookup %@ property\n"
+ "v12@?0i8"
+ "v24@0:8Q16"
+ "waitUntilTime:"
- " %02x"
- "%d: retry OpenProtector (%d)"
- "%s : failed to sync conversion metrics\n"
- "%s has been successfully converted to APFS\n"
- "%s returned an error when writing img3 object"
- "%s/%s.img4"
- "%s/NeRD/%s"
- "%s: \"ExternalConnected\" property not boolean\n"
- "%s: %s: copy_fud_data returned NULL"
- "%s: %s: failed to convert dictionary key to C string"
- "%s: Can't find AppleARMPMUCharger to check external power status\n"
- "%s: Couldn't create matching dict to find AppleARMPMUCharger service\n"
- "%s: Failed to disconnect battery: %d\n"
- "%s: Failed to open AppleEpochManager connection.\n"
- "%s: Failed to set recovery EPOCH. Error: %d\n"
- "%s: No \"ExternalConnected\" property on ApplePMUCharger\n"
- "%s: No external power\n"
- "%s: external power not connected - disconnecting battery to reset HW\n"
- "%s: failed to open gasgauge - can't disconnect battery\n"
- "%s: flashing %c%c%c%c data (length = 0x%lx)\n"
- "%s: gasgauge_swupdate returned %d"
- "%s: nil epoch passed, will not set."
- "%s: unable to create CFData for img3 ticket"
- "%s: unable to create img3 ticket"
- "%s: waiting for %d seconds before checking for external power\n"
- "%s: waiting for power button\n"
- "%s:%d  Error Reading Shutdown reason"
- "%s:%d  updatesDone=%d POLLING THE BATTERY"
- "%s:%d  updatesDone=%d PUBLISHING BATTERY data"
- "%s:%d  updatesDone=%d READING FLAGS"
- "%s:%d  updatesDone=%d criticalValue=%d external_connected=%d UpSeconds=%llu batteryInfo.voltage=%d"
- "%s:%d  updatesDone=%d criticalValue=%d external_connected=%d UpSeconds=%llu cfd=%d cfd-voltage=%d batteryInfo.voltage=%d"
- "%s:%d  updatesDone=%d dictionary failed"
- "%s:%d  updatesDone=%d, fullUpdate=%d, bootFullUpdate=%d, forceFullUpdate=%d] "
- "%s:%d UpSeconds=%llu (cfd = %u) forcing critical to 0"
- "%s:%d break failed (%d)"
- "%s:%d break failed break_failures=%d (%d)"
- "%s:%d cannot create dictionary"
- "%s:%d cannot disable gauge interrupts (%d)"
- "%s:%d cannot dump stats and logs (%x)"
- "%s:%d cannot read data"
- "%s:%d cannot read upo data"
- "%s:%d cannot update thermal state"
- "%s:%d deadline expired at UpSeconds=%llu (cfd = %u)"
- "%s:%d invalid timestamp"
- "%s:%d updatesDone=%d UpSeconds=%llu voltage=%d (low)"
- "*** %s:%d updatesDone=%d last_update_ignored=%d now=%f deadline=%f *** "
- "*** %s:%d updatesDone=%d last_update_ignored=%d now=%f deadline=%f update_interval=%f *** "
- "*** %s:%d updatesDone=%d message.messageType=%#x  (ign) *** "
- "*** %s:%d updatesDone=%d message.messageType=%#x system_sleep=%d *** "
- "*** %s:%d updatesDone=%d same_adaptor=%d adaptor_type=%d external_connected=%d *** "
- "-F"
- "-S"
- "-[IMG3NorUpdater _encodeAndWriteIMG3Data:isLLB:isTicket:withError:]"
- "-[IMG3NorUpdater updateBootFirmwareWithCallback:context:error:]"
- "-fdy"
- "/Library/Caches/com.apple.xbs/Sources/AppleHDQGasGauge/AppleHDQGasGauge.c"
- "/System/Library/Filesystems/apfs.fs/hfs_convert"
- "/dev/cu.gas-gauge"
- "/mnt5/conversion_logs"
- "/sbin/fsck_hfs"
- "/sbin/mount_hfs"
- "/usr/share/progressui/disconnect-prompt.tga"
- "/usr/share/progressui/power-button-prompt.tga"
- "/usr/standalone/firmware/Bora/"
- "000000"
- "AbsoluteCapacity"
- "AdapterInfo"
- "Added atvAbsMaxVoltageMV=%u to battery dict"
- "Amperage"
- "AppleARMPMUCharger"
- "AppleDynamicATV"
- "AppleEpochManager"
- "AppleHDQGasGauge.c"
- "AppleHDQGasGaugeControl"
- "AppleImage3NORAccess"
- "AppleRawBatteryFlags"
- "AppleRawExternalConnected"
- "AtCriticalLevel"
- "AverageCurrent"
- "AverageTemperature"
- "B32@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24"
- "B40@0:8^{__CFData=}16B24B28^@32"
- "B40@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24^@32"
- "BatteryData"
- "BatteryHealthMetric"
- "BatteryShutdownReason"
- "CCA: GasGauge still calibrating now=%lu"
- "CCA: cannot disable DLOG (%#x)"
- "CCA: cannot read DLOG status (%#x)"
- "CCA: disabled DLOG updatesDone=%d ccaDeadline=%lu"
- "CCA: re-enable DLOG updatesDone=%d, now=%lu"
- "CCA: re-enable DLOG updatesDone=%u, now=%lu"
- "CCA: usermode cannot disable DLOG (%#x)"
- "CCA: wait for deadline now=%lu"
- "Cannot create the lifetime dictionary"
- "ChargeTable"
- "ChargerAlert"
- "ChargerData"
- "ChargerStatus"
- "ChargerTimeout"
- "ChargerWatchdogTimeout"
- "ChargingCurrent"
- "ChargingVoltage"
- "ChemID"
- "ChemicalWeightedRa"
- "Conversion failed for %s\n"
- "Copying from path: %s\n"
- "Critical battery shutdown disabled"
- "CriticalBattery"
- "CriticalFlagDelay"
- "CurrentCapacity"
- "CycleCount"
- "CycleCountLastQmax"
- "DOD0"
- "DebugPolling"
- "DesignCapacity"
- "ExternalConnected"
- "FCFlag"
- "Failed to instantiate img3 image"
- "Failed to read img3 type"
- "Failed to write Img3 Firmware data"
- "Failed to write Img3 Ticket data"
- "Failed to write Img3 boot data"
- "Flags"
- "FlashWriteCount"
- "ForceFullGGUpdateOnBoot"
- "FullAvailableCapacity"
- "FullChargeCapacity"
- "Gas Gauge"
- "GasGauge-updateThread"
- "GasGaugeFirmwareVersion"
- "GaugeFlagRaw"
- "GaugeResetCounter"
- "HighAvgCurrentLastRun"
- "IMG3NorUpdater"
- "IMaxAndSocSmoothTable"
- "IOPMUBootBatteryHealthMetric"
- "IOPMUBootErrorClear"
- "IOPMUBootUPOState"
- "IORegistryEntrySetCFProperties(0x%x)"
- "ITMiscStatus"
- "ITSimulationCounter"
- "Img3 Ticket Data updated"
- "Img3 encoding failed"
- "LifetimeData"
- "LightweightVolumeManager_Media"
- "LowAvgCurrentLastRun"
- "ManufactureDate"
- "MaxCapacity"
- "MaximumChargeCurrent"
- "MaximumDeltaVoltage"
- "MaximumDischargeCurrent"
- "MaximumFCC"
- "MaximumOverChargedCapacity"
- "MaximumOverDischargedCapacity"
- "MaximumPackVoltage"
- "MaximumQmax"
- "MaximumRa0-8"
- "MaximumTemperature"
- "MfgData"
- "MinimumDeltaVoltage"
- "MinimumFCC"
- "MinimumPackVoltage"
- "MinimumQmax"
- "MinimumRa0-8"
- "MinimumTemperature"
- "No gas gauge update for this platform."
- "NominalChargeCapacity"
- "NotChargingReason"
- "OCVTakenFlag"
- "PassedCharge"
- "PoSMEnabled"
- "PoSMLowerThreshold"
- "PoSMUpperThreshold"
- "PresentDOD"
- "Qmax"
- "Qstart"
- "RDISCnt"
- "RSS"
- "RaTable"
- "RaTableRaw"
- "RaUpdateCounter"
- "Raw"
- "RemainingCapacity"
- "ResScale"
- "ResetEnabled"
- "RestricLogCounter"
- "SOCBasedShutdown"
- "SPI writer was unavailable at write-time."
- "ShutDownAverageCurrent"
- "ShutDownCycleCount"
- "ShutDownCycleCountLastQmax"
- "ShutDownDLog"
- "ShutDownDOD0"
- "ShutDownFullChargeCapacity"
- "ShutDownMaxDischargeCurrent"
- "ShutDownMaxRa08"
- "ShutDownNominalChargeCapacity"
- "ShutDownPassedCharge"
- "ShutDownPresentDOD"
- "ShutDownPrevAverageCurrent"
- "ShutDownPrevFullChargeCapacity"
- "ShutDownPrevNominalChargeCapacity"
- "ShutDownPrevRemainingCapacity"
- "ShutDownPrevVoltage"
- "ShutDownQstart"
- "ShutDownRSS"
- "ShutDownRaTableRaw"
- "ShutDownRemainingCapacity"
- "ShutDownResScale"
- "ShutDownTemperature"
- "ShutDownTimeAbove95"
- "ShutDownTimestamp"
- "ShutDownUISoc"
- "ShutDownVoltage"
- "StateOfCharge"
- "Temperature"
- "TemperatureSamples"
- "ThermalCoolDown"
- "TimeAbove95Perc"
- "TimeRemaining"
- "TotalOperatingTime"
- "Unexpected imageType in firmware"
- "UpdateSampleConfig"
- "UpdateTime"
- "UserMode"
- "Voltage"
- "WeightedRa"
- "[%s]: Failed to unmount APFS converted mount point: %d: %s\n"
- "[0x%08x] %s"
- "[0x%08x](warning) %s"
- "_ApTicketCopyTagData failed %d\n"
- "_encodeAndWriteIMG3Data:isLLB:isTicket:withError:"
- "atvAbsMaxVoltageMV"
- "atvBatteryCapacityMA"
- "battery"
- "batteryDataCount<=kNumBatteryDataUpdateKeys"
- "can't parse top-level container\n"
- "cannot disable DLOG (%#x)"
- "cannot disable currentlog %#x"
- "cannot drain data log (%d)"
- "cannot drain the data log (%d)"
- "cannot enable current log (%d)"
- "cannot enable gauge interrupts (%d)"
- "cannot read average current (%d)"
- "cannot read battery data count=%d (err=%d)"
- "changed updateSampleConfig=%#x"
- "checkreset"
- "com.apple.AppleHDQGasGauge"
- "com.apple.gasgauge"
- "could not create CFNumber for esdm-fuses\n"
- "could not finalize ticket img3"
- "could not find %s service"
- "could not find hw.model: %s"
- "could not open service: %#x"
- "could not read gas gauge control status"
- "data log clients: %d"
- "data log entries: %u"
- "data log supported: %d"
- "debug"
- "debugLog"
- "determinePoSMThreshold, changed:%d %d %d %d "
- "determinePoSMThreshold, cmp:%d>%u %d>%u %d>%u %d>%u"
- "determinePoSMThreshold, enabled:%d %d %d %d "
- "determinePoSMThreshold,minThreshold=%u threshold:%u %u %u %u"
- "determineVACVoltage, vacLevelCount=%d, vac95LevelCount=%d"
- "determineVACVoltage:: vac95BasedVoltageMV=%d absMaxVoltageMV=%d"
- "determineVACVoltage:: vacBasedVoltageMV=%d"
- "determineVACVoltage:: waiting for vbat(%d) < vac(%d)"
- "disabled passedCharge PCFF=%d err=%d"
- "disabling DLOG (num_clients=%i)"
- "distantFuture"
- "dynATV: cannot write to charger startus (%d)"
- "esdm-fuses property is not a CFData\n"
- "failed to allocate propertyData\n"
- "failed to create data tag for ticket"
- "failed to create img3\n"
- "failure last_update_failed_counter=%d last_success at %g, supressing %d subsequent errors"
- "flags update only"
- "fsck failed on BaseBand Data (%s)\n"
- "fsck failed on Data (%s)\n"
- "fsck failed on System (%s)\n"
- "fsck succeeded on BaseBand Data (%s)\n"
- "fsck succeeded on Data (%s)\n"
- "fsck succeeded on System (%s)\n"
- "gas gauge charge table bad checksum: checksum %#x checksum byte %#x expecting %#x"
- "gas gauge charge table inconsistent: %d data entries, %d bytes"
- "gas gauge charge table invalid type: %#x"
- "gas gauge firmware 1.09: disabling critical battery shutdown"
- "gas gauge reset detected (flags %#x capacity %d/%dmAh voltage %dmV current %dmA)"
- "gas gauge: SWI line low, issuing reset"
- "gas gauge: cannot determine the state of SWI line"
- "gas gauge: cannot issue a reset"
- "gas gauge: critical flag delay %d"
- "gas gauge: debug_polling=%d"
- "gas gauge: log counter %d"
- "gas gauge: reset"
- "gas gauge: userModeEnabled=%d"
- "gasgauge success after previous %gs failure"
- "gasgauge success after previous failure"
- "gasgauge: %llu updateThread critical(%d, 0x%x), uscfg=0x%x, dyn=%d cfd=%d cfd-voltage=%d, upos=%x"
- "gasgauge: SWI line low issuing reset"
- "gasgauge: SWI line low reset disabled, ignoring"
- "gasgauge: SWI line, cannot determine the state of line"
- "gasgauge: could not map data log: %s"
- "gasgauge: could not register for battery events err=%x"
- "gasgauge: could not register for power source events"
- "gasgauge: could not register for system power notifications"
- "gasgauge: listening for battery interrupts"
- "gasgauge: updateThread start"
- "gasgauge: updateThread terminated"
- "gathering data log updatesDone=%d num_clients=%d"
- "ggctl_open_device"
- "hw.model"
- "iMaxAndSocSmoothTable"
- "image4-supported"
- "initWithTimeIntervalSinceNow:"
- "item data length (%zu) is larger than provided buffer length (%zu)\n"
- "kern.boottime"
- "log"
- "looking up root ticket hash\n"
- "malformed ticket\n"
- "mask real UPOState=%x FCC=%d RemCap=%d new FCC=%d new RemCap=%d"
- "mount update failed for root filesystem (%s): %s\n"
- "num_client<0, client error?"
- "parseBatteryData"
- "ramrod_convert_hfs_to_apfs"
- "ramrod_disconnect_battery"
- "ramrod_splat_commit_proposed"
- "ramrod_sync_conversion_metrics_nvram"
- "ramrod_ticket_create_img3"
- "readShutdownReasonData"
- "root-ticket-hash"
- "sock %3d: set SO_NOSIGPIPE=%d"
- "stats"
- "statsAndLogs"
- "timeIntervalSinceNow"
- "timeSinceAwake"
- "unable to lookup esdm-fuses property\n"
- "unable to mmap %zu bytes for image3 data"
- "updateThermalCoolDownState"
- "updateThread"
- "update_gas_gauge"
- "waitUntilDate:"
- "warning: specified fixed sized volume slice was too large\n"

```
