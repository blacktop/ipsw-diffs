## inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

-63.100.22.0.0
-  __TEXT.__text: 0x53080
-  __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_stubs: 0x5620
-  __TEXT.__objc_methlist: 0x2bf4
-  __TEXT.__cstring: 0x20e6
-  __TEXT.__objc_methname: 0x5922
-  __TEXT.__objc_classname: 0x49e
-  __TEXT.__objc_methtype: 0x10f0
-  __TEXT.__const: 0x1631
-  __TEXT.__oslogstring: 0x57af
-  __TEXT.__gcc_except_tab: 0x11d0
+63.120.18.0.0
+  __TEXT.__text: 0x63a5c
+  __TEXT.__auth_stubs: 0x1150
+  __TEXT.__objc_stubs: 0x60e0
+  __TEXT.__objc_methlist: 0x2ee4
+  __TEXT.__cstring: 0x3399
+  __TEXT.__objc_methname: 0x62e8
+  __TEXT.__objc_classname: 0x4c4
+  __TEXT.__objc_methtype: 0x119c
+  __TEXT.__const: 0x24f1
+  __TEXT.__oslogstring: 0x5de9
+  __TEXT.__gcc_except_tab: 0x13e0
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1218
-  __DATA_CONST.__auth_got: 0x6c8
-  __DATA_CONST.__got: 0x2d8
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x6fe8
-  __DATA_CONST.__cfstring: 0x23e0
-  __DATA_CONST.__objc_classlist: 0x118
+  __TEXT.__unwind_info: 0x15c8
+  __DATA_CONST.__auth_got: 0x8b8
+  __DATA_CONST.__got: 0x328
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x8a98
+  __DATA_CONST.__cfstring: 0x2b20
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xd0
-  __DATA_CONST.__objc_intobj: 0x1578
+  __DATA_CONST.__objc_superrefs: 0xd8
+  __DATA_CONST.__objc_intobj: 0x16b0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__objc_arraydata: 0x408
-  __DATA_CONST.__objc_arrayobj: 0x468
-  __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x7010
-  __DATA.__objc_selrefs: 0x1958
-  __DATA.__objc_ivar: 0x2c4
-  __DATA.__objc_data: 0xaf0
-  __DATA.__data: 0x6c8
-  __DATA.__bss: 0xe0
-  __DATA.__common: 0x10
+  __DATA_CONST.__objc_arraydata: 0x4b8
+  __DATA_CONST.__objc_arrayobj: 0x4f8
+  __DATA_CONST.__objc_dictobj: 0x78
+  __DATA.__objc_const: 0x73d0
+  __DATA.__objc_selrefs: 0x1c40
+  __DATA.__objc_ivar: 0x300
+  __DATA.__objc_data: 0xb90
+  __DATA.__data: 0x1aa0
+  __DATA.__bss: 0x110
+  __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2367
-  Symbols:   317
-  CStrings:  2223
+  Functions: 2818
+  Symbols:   388
+  CStrings:  2617
 
Symbols:
+ _CFDictionaryGetTypeID
+ _CFDictionaryGetValue
+ _CFGetTypeID
+ _CFNumberGetValue
+ _CFStringCreateWithCString
+ _IOConnectCallMethod
+ _IORegistryEntrySearchCFProperty
+ _OBJC_CLASS_$_CWFChannel
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSURL
+ _SecCertificateCopyData
+ _SecCertificateCreateWithPEM
+ ___NSDictionary0__struct
+ ___error
+ ___stdoutp
+ __dispatch_source_type_timer
+ _calloc
+ _cc_clear
+ _cccbc_one_shot
+ _cccbc_update
+ _ccder_blob_decode_len
+ _ccder_blob_decode_range
+ _ccder_blob_decode_sequence_tl
+ _ccder_blob_encode_body
+ _ccder_blob_encode_body_tl
+ _ccder_sizeof
+ _ccec_compact_import_pub
+ _ccecb_one_shot
+ _cced25519_verify
+ _cchkdf
+ _ccn_read_uint
+ _ccn_write_uint_padded
+ _ccnistkdf_ctr_hmac
+ _ccpbkdf2_hmac
+ _class_getProperty
+ _close
+ _dispatch_assert_queue$V2
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _fcntl
+ _fprintf
+ _fts_close
+ _fts_open
+ _fts_read
+ _fts_set
+ _kIOMasterPortDefault
+ _malloc
+ _memcpy
+ _memset_s
+ _open
+ _open_dprotected_np
+ _printf
+ _putchar
+ _puts
+ _qsort
+ _read
+ _realpath$DARWIN_EXTSN
+ _snprintf
+ _stat
+ _statfs
+ _strlen
+ _strnstr
+ _sysctlbyname
+ _syslog
+ _write
CStrings:
+ "\x051"
+ "\x06"
+ "\tSize Distribution:"
+ "\n"
+ "\x0f\f"
+ " (skip)"
+ " dir: %s %i\n"
+ "%.2lf"
+ "%02lx"
+ "%@(%@)"
+ "%@: Received command %ld, got error when handling it: %@"
+ "%i"
+ "%i,%u,%u,%u,%lld,%lld,%lld,"
+ "%lld,%d\n"
+ "%s%s"
+ "%s%s\n"
+ "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
+ "%s%s:%s%s%s%s%u:%s%u:%s bad 1%s\n"
+ "%s%s:%s%s%s%s%u:%s%u:%s bad 2%s\n"
+ "%s%s:%s%s%s%s%u:%s%u:%s fail%s\n"
+ "%s%s:%s%s%s%s%u:%s%u:%s ioreg: %d, boot_arg: %d%s\n"
+ "%s/mobile"
+ "%s:\n\tNum files:\t%u,\n\tNum hardlinks:\t%u,\n\tNum compressed:\t%u,\n\tTotal Size:\t%lld,\n\tMin File Size:\t%lld,\n\tMax File Size:\t%lld,\n"
+ "%s: mode=%o, u/g=%i:%i class=%i%s\n"
+ "%{public}@ SMC Key is not supported: %{bool}d"
+ ","
+ "-apfs_shared_datavolume"
+ "/.fseventsd"
+ "/.overprovisioning_file"
+ "/.ssh"
+ "/Applications"
+ "/Containers"
+ "/Documents/Pearl"
+ "/Keychains"
+ "/Library"
+ "/Library/Accounts"
+ "/Library/AddressBook"
+ "/Library/AggregateDictionary"
+ "/Library/ApplePushService"
+ "/Library/Assistant"
+ "/Library/BackBoard"
+ "/Library/Backup"
+ "/Library/BulletinBoard"
+ "/Library/Caches"
+ "/Library/Calendar"
+ "/Library/CallHistoryDB"
+ "/Library/Carrier Bundles"
+ "/Library/ConfigurationProfiles"
+ "/Library/ControlCenter"
+ "/Library/Cookies"
+ "/Library/CoreBrightness"
+ "/Library/CoreDuet"
+ "/Library/CoreFollowUp"
+ "/Library/CountryBundles"
+ "/Library/CrashReporter"
+ "/Library/DataAccess"
+ "/Library/DeviceRegistry"
+ "/Library/DeviceRegistry.dontBackUp"
+ "/Library/DeviceRegistry.state"
+ "/Library/DoNotDisturb"
+ "/Library/Fonts"
+ "/Library/FrontBoard"
+ "/Library/ISP"
+ "/Library/IdentityServices"
+ "/Library/Keyboard"
+ "/Library/Logs"
+ "/Library/Logs/AppleSupport"
+ "/Library/Logs/CoreDuet"
+ "/Library/Logs/CrashReporter"
+ "/Library/Mail"
+ "/Library/ManagedAssets"
+ "/Library/MediaStream"
+ "/Library/MedicalID"
+ "/Library/MobileBluetooth"
+ "/Library/MobileContainerManager"
+ "/Library/MobileInstallation"
+ "/Library/NFStorage"
+ "/Library/NanoBackup"
+ "/Library/NanoPreferencesSync"
+ "/Library/NanoTimeKit"
+ "/Library/Passes"
+ "/Library/Preferences"
+ "/Library/SMS"
+ "/Library/SoftwareUpdate"
+ "/Library/SpringBoard"
+ "/Library/SyncedPreferences"
+ "/Library/TCC"
+ "/Library/Trial"
+ "/Library/UserConfigurationProfiles"
+ "/Library/UserNotifications"
+ "/Library/VoiceServices"
+ "/Library/Voicemail"
+ "/Library/WebClips"
+ "/Library/adi"
+ "/Library/mad"
+ "/Library/mad/activation_records"
+ "/Library/terminus"
+ "/Managed Preferences"
+ "/Managed Preferences/mobile"
+ "/Media"
+ "/Media/Downloads"
+ "/Media/iTunes_Control"
+ "/MobileAsset"
+ "/MobileDevice/ProvisioningProfiles"
+ "/MobileSoftwareUpdate"
+ "/backup"
+ "/containers"
+ "/db"
+ "/db/com.apple.xpc.launchd"
+ "/installd"
+ "/iomfb_bics_daemon"
+ "/keybags"
+ "/log"
+ "/log/com.apple.xpc.launchd"
+ "/logs"
+ "/logs/AppleSupport"
+ "/logs/BurnIn"
+ "/mobile"
+ "/networkd"
+ "/preferences"
+ "/protected/trustd"
+ "/root"
+ "/root/Library"
+ "/root/Library/Caches"
+ "/root/Library/Lockdown"
+ "/root/Library/Logs"
+ "/root/Library/MobileContainerManager"
+ "/root/Library/Preferences"
+ "/run"
+ "/tmp"
+ "/var/mobile/Library/Logs/com.apple.inboxupdaterd"
+ "/vm"
+ "/wireless"
+ "00000000000000000000"
+ "0102030405060708090A"
+ "0102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F20"
+ "416476"
+ "53656173686970"
+ ":"
+ "<Unknown Format>"
+ "<user>"
+ "<var>"
+ "@\"NSFileHandle\""
+ "@\"NSMutableDictionary\"24@0:8@\"NSDictionary\"16"
+ "@\"NSObject<OS_dispatch_source>\""
+ "@40@0:8@16@24^@32"
+ "@48@0:8@16@24Q32^@40"
+ "Adv"
+ "AppleKeyStore"
+ "AppleKeyStoreTest"
+ "B16@?0^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}8"
+ "B32@0:8@16q24"
+ "BackCase_Charge"
+ "BackCase_MLB"
+ "BackCase_RF"
+ "Band"
+ "Bandwidth"
+ "CLASS A"
+ "CLASS B"
+ "CLASS C"
+ "CLASS D"
+ "CLASS NONE"
+ "Cannot find IO registry entry for IOPMUPrimary"
+ "Cannot find IO registry entry property for IOPMUBootLPMCtrl"
+ "ChannelName"
+ "Checking if device has LPM mode set..."
+ "Command %@ is not allowed at state %ld, rejecting..."
+ "CountryCode"
+ "CoverGlass_Center"
+ "CoverGlass_LED"
+ "Data"
+ "DataCollector: container at %@ already exist but is not a directory."
+ "DataCollector: data of class %@ ignored because it is not serializable into json"
+ "DataCollector: failed to close thermal data file: %@"
+ "DataCollector: failed to create container at %@: %@"
+ "DataCollector: failed to remove container at %@."
+ "DataCollector: failed to save non-thermal data: %@"
+ "DataCollector: failed to serialize key events: %@"
+ "DataCollector: failed to write thermal data to file: %@"
+ "DataCollector: failed to write to thermal data file: %@"
+ "DataCollector: start to collect thermal data every %ld seconds"
+ "DataCollector: was not able to open %@ for writing"
+ "DataCollector: will clear data generated."
+ "DataCollector: will start."
+ "DataCollector: will stop."
+ "Deriving Device IDs for BT advertisement..."
+ "Deriving Device IDs for BT connection..."
+ "Deriving Device IDs for BT wake..."
+ "Deriving Device Key for Seaship..."
+ "Device ID derived: %{public}@ for timestamp: %u"
+ "Device is not ready for SS update in state %ld"
+ "Device key derived: %{public}@"
+ "EscrowPasscodePeriod"
+ "EscrowTokenPeriod"
+ "Failed to compute ECDH shared secret: %d"
+ "Failed to compute Seaship Device Key"
+ "Failed to compute Seaship Device Key: %{public}@"
+ "Failed to create certificate from PEM data"
+ "Failed to derive Device ID: %d"
+ "Failed to derive Seaship Device Key"
+ "Failed to derive Seaship Device Key: %d"
+ "Failed to load existing key events: %@"
+ "Failed to load existing key events: expecting array but %@ is found"
+ "Failed to read LPM parameters from template file: %{public}@"
+ "Failed to update PMU register"
+ "Free Blocks:%lld blocks of size:%d\n"
+ "Handling isLPMSetWithReply: xpc call"
+ "IODeviceTree:/filesystems"
+ "IOService"
+ "IOService:/IOResources/AppleKeyStore"
+ "IOService:/IOResources/AppleKeyStoreTest"
+ "JSONObjectWithData:options:error:"
+ "LPMTemplateFile"
+ "LTK"
+ "MIBUCryptoHelper"
+ "MIBUDataCollector"
+ "Non-Prod"
+ "Prod"
+ "Resp"
+ "Scanning for wifi with SSID: %{public}@ and channel: %{public}lu"
+ "Seaship"
+ "Setting LPM parameter key: %{public}@ with value: %{public}@"
+ "Setting device to LPM mode with options: %{public}@"
+ "Setting for wifi with SSID: %{public}@ and channel: %{public}lu"
+ "Shared secret computed: %{public}@"
+ "ShippingUpdateStart"
+ "SoCTempMaxAverage"
+ "T@\"NSNumber\",&,N,V_band"
+ "T@\"NSNumber\",&,N,V_bandwidth"
+ "T@\"NSNumber\",&,N,V_channelName"
+ "T@\"NSNumber\",&,N,V_wifiChannel"
+ "T@\"NSString\",&,N,V_countryCode"
+ "T@\"NSString\",&,N,V_wifiSSID"
+ "TCMb"
+ "TQ,N,V_wifiChannel"
+ "TVBM"
+ "TVFD"
+ "TVFL"
+ "Tag"
+ "Time"
+ "Time,%@\n"
+ "Unable to read template file"
+ "Unexpected data type found for IOPMUBootLPMCtrl"
+ "Unexpected data type found for lpm3 key"
+ "Unknown LPM parameter key: %@"
+ "Unknown LPM parameter key: %{public}@"
+ "Use Pandora Key Server certificates of grade: %{public}@"
+ "UsePandoraNonProdCerts"
+ "UsePlistForDeviceIKM"
+ "UseScriptForDeviceKey"
+ "VirtualBatteryTemp"
+ "WiFiChannel"
+ "_aks_operation"
+ "_band"
+ "_bandwidth"
+ "_channelName"
+ "_collectThermalData"
+ "_collectThermalDataWithKeys:interval:"
+ "_container"
+ "_countryCode"
+ "_deriveDeviceIDsForUseCase:outError:"
+ "_deriveDeviceKeyWithLabel:andContext:outError:"
+ "_doubleFromData:"
+ "_fileForStatsData"
+ "_fileForThermalData"
+ "_findServicePmuPrimary"
+ "_finishCollectingThermalData"
+ "_keyEvents"
+ "_keyEventsSaved"
+ "_loadKeyEvents"
+ "_merge_dict_cb"
+ "_networkd"
+ "_pandoraCertificates:"
+ "_prepare"
+ "_prepareThermalDataFile"
+ "_readLPMFlagFromIOPMUBootLPMCtrl:"
+ "_saveKeyEvents"
+ "_securityd"
+ "_stringForDate:"
+ "_stringForNumberinData:forKey:"
+ "_thermalCollectionQueue"
+ "_thermalCollectionTimer"
+ "_thermalColumnNames"
+ "_thermalDataFile"
+ "_thermalKeyMapping"
+ "_updateIOPMUBootLPMCtrl"
+ "_wifiChannel"
+ "_wifiSSID"
+ "_wireless"
+ "addKeyEvent:additionalData:"
+ "aks"
+ "aks-client-queue"
+ "aks_delete_xart_leak"
+ "aks_fs_supports_enhanced_apfs"
+ "aks_fv_new_kek"
+ "aks_fv_new_sibling_vek"
+ "aks_fv_new_vek"
+ "aks_fv_rewrap_kek"
+ "aks_fv_set_protection"
+ "aks_fv_unwrap_vek_with_acm"
+ "aks_get_internal_info_for_key"
+ "aks_internal_state"
+ "aks_kext_get_options"
+ "aks_kext_set_options"
+ "aks_run_internal_test"
+ "aks_stash_escrow"
+ "appendFormat:"
+ "arrayWithArray:"
+ "bandwidth"
+ "channelName"
+ "clear"
+ "closeAndReturnError:"
+ "com.apple.mobileinboxupdate.data_collection.thermal"
+ "componentsJoinedByString:"
+ "could not create file: %s (%s)\n"
+ "could not open file: %s (%s)\n"
+ "countryCode"
+ "createFileAtPath:contents:attributes:"
+ "currentLocale"
+ "d24@0:8@16"
+ "daemon"
+ "dataWithContentsOfFile:"
+ "dataWithJSONObject:options:error:"
+ "der_key_validate"
+ "deriveDeviceIDsForBTAdvertisement:"
+ "deriveDeviceIDsForBTConnection:"
+ "deriveDeviceIDsForBTWake:"
+ "deriveDeviceIDsFromDeviceKey:forUseCase:withTimestamp:outError:"
+ "deriveDeviceKeyForSeaship:"
+ "dictFromSMCKeyMapping:"
+ "dictionaryWithContentsOfURL:error:"
+ "e-apfs"
+ "failed to open connection to %s\n"
+ "failed to write restore bag to disk %s\n"
+ "file: %s %i\n"
+ "fileExistsAtPath:isDirectory:"
+ "fileHandleForWritingAtPath:"
+ "fileURLWithPath:"
+ "flags"
+ "hexStringRepresentation"
+ "initWithBytesNoCopy:length:freeWhenDone:"
+ "initWithPacketConsumer:hostPort:tcpAddress:tcpPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:controllerDelegate:"
+ "isLPMSet:"
+ "isLPMSetWithReply:"
+ "isValidJSONObject:"
+ "kern.bootargs"
+ "localizedDescription"
+ "mobile"
+ "now"
+ "objectAtIndexedSubscript:"
+ "objectForKeyedSubscript:"
+ "pandoraCertsData:"
+ "root"
+ "seaship"
+ "seekToEndOfFile"
+ "setBand:"
+ "setBandwidth:"
+ "setChannelName:"
+ "setChannels:"
+ "setCountryCode:"
+ "setDateFormat:"
+ "setDeviceIDAdvScanCount:"
+ "setDeviceIDDiagInfo:"
+ "setDeviceIDDiagLength:"
+ "setDeviceIDInfo:"
+ "setDeviceIDInputKeyMaterial:"
+ "setDeviceIDLength:"
+ "setDeviceIDSalt:"
+ "setDeviceIDTimestampEffectiveBits:"
+ "setDeviceIDTimestampFrequency:"
+ "setDeviceIDTimestampLsbsTruncated:"
+ "setDiagnosticTxAdvBackoff:"
+ "setDiagnosticTxAdvDuration:"
+ "setDiagnosticTxAdvInterval:"
+ "setFlags:"
+ "setLocale:"
+ "setMacKeyDiagInfo:"
+ "setMacKeyDiagLength:"
+ "setNumberOfDelayIterations:"
+ "setValue:forKey:"
+ "setWiFiSSID:andChannel:"
+ "setWifiChannel:"
+ "setWifiSSID:"
+ "shared allow list:"
+ "shipping_update_stats.json"
+ "shipping_update_thermal.csv"
+ "stat failed: %s\n"
+ "stringByAppendingPathComponent:"
+ "stringFromDate:"
+ "stringWithCapacity:"
+ "summaryReport"
+ "timeIntervalSinceReferenceDate"
+ "unsignedIntegerValue"
+ "usePandoraNonProdCerts"
+ "usePlistForDeviceIKM"
+ "useScriptForDeviceKey"
+ "user allow list:"
+ "v16@?0^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}8"
+ "v32@0:8@16Q24"
+ "wheel"
+ "wifiChannel"
+ "writeData:error:"
+ "writeToFile:options:error:"
+ "yyyy-MM-dd HH:mm:ss"
- "\x05"
- "\x0f\x06"
- "%{public}@ SMC Key is supported: %{bool}d"
- "Device already activated"
- "Failed to set device to LPM; empty scan payload"
- "Scanning for wifi with SSID: %{public}@"
- "Setting device to LPM mode with scan payload: %{public}@"
- "findServicePmuPrimary"
- "initWithPacketConsumer:hostPort:tcpAddress:tcpPort:groupAddress:groupPort:interfaceName:serviceName:controllerDelegate:"
- "updateIOPMUBootLPMCtrl"

```
