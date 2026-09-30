## Accessory Updater Service

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/Accessory Updater Service.xpc/Accessory Updater Service`

```diff

-3148.80.1.0.2
-  __TEXT.__text: 0x70660
-  __TEXT.__auth_stubs: 0x1760
-  __TEXT.__objc_stubs: 0x2c60
-  __TEXT.__objc_methlist: 0x2ae8
-  __TEXT.__const: 0x57e0
+3196.100.158.0.1
+  __TEXT.__text: 0x746c8
+  __TEXT.__auth_stubs: 0x1870
+  __TEXT.__objc_stubs: 0x2ce0
+  __TEXT.__objc_methlist: 0x2e64
+  __TEXT.__const: 0x5c80
   __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__cstring: 0x166af
-  __TEXT.__objc_methname: 0x35f8
-  __TEXT.__objc_classname: 0xb08
-  __TEXT.__objc_methtype: 0xcf2
-  __TEXT.__oslogstring: 0x794
-  __TEXT.__unwind_info: 0x1600
-  __DATA_CONST.__auth_got: 0xbc0
-  __DATA_CONST.__got: 0x358
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x2038
-  __DATA_CONST.__cfstring: 0xf420
+  __TEXT.__cstring: 0x163c5
+  __TEXT.__objc_methname: 0x364e
+  __TEXT.__objc_classname: 0xb12
+  __TEXT.__objc_methtype: 0xd02
+  __TEXT.__oslogstring: 0x150c
+  __TEXT.__unwind_info: 0x1808
+  __DATA_CONST.__auth_got: 0xc48
+  __DATA_CONST.__got: 0x3c0
+  __DATA_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__const: 0x2338
+  __DATA_CONST.__cfstring: 0xf500
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0x5ab8
-  __DATA.__objc_selrefs: 0xe98
+  __DATA.__objc_const: 0x54a0
+  __DATA.__objc_selrefs: 0xf58
   __DATA.__objc_ivar: 0x37c
   __DATA.__objc_data: 0x14f0
-  __DATA.__data: 0xab0
-  __DATA.__bss: 0xaf0
+  __DATA.__data: 0xaf0
+  __DATA.__bss: 0x9f0
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
+  - /System/Library/PrivateFrameworks/DeviceInterface.framework/DeviceInterface
   - /System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2003
-  Symbols:   1734
-  CStrings:  4448
+  Functions: 2443
+  Symbols:   1800
+  CStrings:  4519
 
Symbols:
+ _AMAuthInstallBundleSetEntryEnabled
+ _AMAuthInstallPlatformCreateDataFromMappedFileURL
+ _AMAuthInstallSupportCreateDataFromMappedFileURL
+ _AMRRestoreInitializeTADNotificationsExternal
+ _AMSupportCreateDictionaryFromFileURL
+ _AMSupportPlatformCreateDataFromFileURL
+ _AMSupportPlatformCreateDataFromMappedFileURL
+ _AMSupportPlatformOpenFileStreamWithURL
+ _AMSupportPlatformWriteDataToFileURL
+ _CFStringCreateWithCharacters
+ _IOConnectCallMethod
+ _IOObjectConformsTo
+ _IOObjectCopyBundleIdentifierForClass
+ _IORegistryEntryCreateCFProperties
+ _IOServiceClose
+ _IOServiceOpen
+ _OBJC_CLASS_$_MantaFTABFile
+ _OBJC_CLASS_$_MantaFTABSubfile
+ _OBJC_METACLASS_$_MantaFTABFile
+ _OBJC_METACLASS_$_MantaFTABSubfile
+ _TADFU_Device_Epoch_String
+ _TADFU_Device_InterfaceID
+ _TADFU_Device_LocationID
+ _TADFU_Device_Manufacturer_String
+ _TADFU_Device_Nonce_String
+ _TADFU_Device_Payload_Base_Address
+ _TADFU_Device_Payload_Capacity
+ _TADFU_Device_ProductID
+ _TADFU_Device_Product_String
+ _TADFU_Device_Serial_Number_String
+ _TADFU_Device_VendorID
+ __AMRTADModeDeviceCreate
+ __AMRTADModeDeviceDisconnected
+ __AMRestoreErrorForAMSupportError
+ __AMRestoreGetDeviceIDToMatchAPOnly
+ ___stderrp
+ __registryIDToDevice
+ _cfstring_to_c_string
+ _clock_gettime
+ _debug_usb_free
+ _debug_usb_get_location
+ _debug_usb_init_for_service
+ _debug_usb_read
+ _debug_usb_set_endpoint_for_portal
+ _debug_usb_write
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_get_label
+ _dispatch_retain
+ _fileno
+ _fprintf
+ _iokitUtils_popDeviceForService
+ _iokitUtils_setDeviceForService
+ _iokitUtils_startDiscovery
+ _kCFAllocatorSystemDefault
+ _libDFU_deviceTransport
+ _libDFU_release
+ _libDFU_setDispatchQueueForDiscovery
+ _libDFU_startDeviceDiscoveryForVIDPID
+ _lseek
+ _mach_task_self_
+ _memcmp
+ _nanosleep
+ _objc_retain_x24
+ _os_parse_boot_arg_int
+ _pthread_threadid_np
+ _releaseMemoryRegions
+ _serialize_paw
+ _serialize_pcr
+ _serialize_pcw
+ _stmDFU_parseConfiguration
+ _taDFU_AppleKIS_startDeviceDiscoveryForVIDPID
+ _taDFU_Library_startDeviceDiscoveryForVIDPID
+ _taDFU_deviceinterfaced_startDeviceDiscoveryForVIDPID
+ _taDFU_deviceinterfaced_startDeviceDiscoveryGeneric
+ _taDFU_startDeviceDiscoveryForVIDPID
+ _taDFU_useKISKext
+ _tadfu_disconnected_callback
+ _tadfu_discovery_callback
+ _tadfu_transport_client_complete_dfu
+ _tadfu_transport_client_create_with_device_discovery_callbacks
+ _tadfu_transport_client_download_data
+ _usbDFU_appendSuffix
+ _usbDFU_clearStatus
+ _usbDFU_copyStringDescriptor
+ _usbDFU_downloadBlock
+ _usbDFU_getStatus
+ _usbDFU_release
+ _usbDFU_startDeviceDiscoveryForVIDPID
- _AMAuthInstallApImg4Stitch
- _AMAuthInstallPlatformCreateBufferFromNativeFilePath
- _AMAuthInstallPlatformWriteBufferToNativeFilePath
- _AMAuthInstallPlatformWriteDataToFileURL
- _AMFDRLogSetHandler
- _AMRestoreCaptureSubsystemLogs
- _AMSupportCreateDataFromFileURL
- _DERImg4DecodeFindInSequence
- _OBJC_CLASS_$_FTABFile
- _OBJC_CLASS_$_FTABSubfile
- _OBJC_METACLASS_$_FTABFile
- _OBJC_METACLASS_$_FTABSubfile
- __locationIDToDevice
- _dlerror
- _feof
- _mmap
- _munmap
- _objc_retain_x25
- _pthread_mach_thread_np
- _pthread_self
- _readlink
- _rewind
CStrings:
+ "%04d-%02d-%02d %02d:%02d:%02d.%03d %s[%d:%llx]: "
+ "%c%u*%u%c%c%n"
+ "%s %@ device->_productString %s"
+ "%s %@ device->_serialNumberString %s"
+ "%s %@ device->_vendorString %s"
+ "%s %@ deviceData->epochString %s"
+ "%s %@ deviceData->nonceString %s"
+ "%s %@ interfaceID %llu"
+ "%s %@ locationID %u"
+ "%s %@ payloadBaseAddress %llu"
+ "%s %@ payloadCapacity %u"
+ "%s %@ productID %u"
+ "%s %@ vendorID %u"
+ "%s *epoch %s"
+ "%s *nonce %s"
+ "%s Overriding behavior with boot-arg, using kext: %d"
+ "%s adding unclaimed device to array %s"
+ "%s allocated device %s deviceData %s"
+ "%s callbacks->discoveryCallback and callbacks->terminationCallback provided"
+ "%s callbacksMap %s unclaimedDevicesMap %s deviceKey %lu callbacks %s queue %s"
+ "%s calling callback->discoveryCallback for device %s"
+ "%s calling callback->terminationCallback for device %s"
+ "%s calling callbacks->discoveryCallback on device %s"
+ "%s completeDFUResult %d"
+ "%s convertedString %s"
+ "%s convertedString: %s"
+ "%s created array %s"
+ "%s created tadfu transport client with tadfu_transport_client_create_with_device_discovery_callbacks. globalDeviceDiscoveryClient %s"
+ "%s device %s"
+ "%s device %s callbacksMap %s unclaimedDevicesMap %s deviceKey %lu"
+ "%s device %s epoch %s"
+ "%s device %s file %s address %lu."
+ "%s device %s nonce %s"
+ "%s device->_deviceData %s"
+ "%s device->_productString %@ %s"
+ "%s device->_serialNumberString %@ %s"
+ "%s device->_vendorString %@ %s"
+ "%s deviceAdded %s context %s"
+ "%s deviceData->epochString %@ %s"
+ "%s deviceData->epochString %s"
+ "%s deviceData->nonceString %@ %s"
+ "%s deviceData->nonceString %s"
+ "%s deviceForLocationID %s deviceForVidPid %s"
+ "%s deviceList %s"
+ "%s deviceRemoved %s context %s"
+ "%s deviceinterfaced enabled: %d"
+ "%s devices %s"
+ "%s dfuDevice %s with interfaceID %llu."
+ "%s dictionary %s"
+ "%s dictionaryValue %@ %s"
+ "%s did not succeed. Releasing device %s"
+ "%s downloadBlockResult %d"
+ "%s failed to convert file path to CFURL"
+ "%s failed to load %@: %d"
+ "%s file %s validated with transferSize %llu, deviceData->payloadCapacity %u"
+ "%s finished creating device %s"
+ "%s first %s second %s"
+ "%s found count %ld devices"
+ "%s freeing tmpBuffer %s"
+ "%s globalDeviceDiscoveryClient %s"
+ "%s go through the unclaimed devices. array %s"
+ "%s got device %s from array"
+ "%s index to remove %ld"
+ "%s initialized discovery globals vidPidCallbacksMap %s locationIDCallbacksMap %s unclaimedDevicesMatchingVidPidMap %s unclaimedDevicesMatchingLocationIDMap %s globalDeviceDiscoveryClient %s"
+ "%s interfaceID %llu device %s context %s."
+ "%s interfaceIDMatches %d"
+ "%s key %s value %s context %s."
+ "%s preferences override: %d"
+ "%s removing key %lu from map"
+ "%s stringToConvert %s"
+ "%s tmpBuffer %s"
+ "%s tmpBufferSize %ld"
+ "%s unclaimed devices array %s"
+ "%s vid %u pid %u callbacks %s queue %s"
+ "%s vid %u pid %u keyForVidPid %u"
+ "(External) Unable to set up TAD device connected notification: 0x%x"
+ "-[MantaFTABFile addSubfileWithTagName:contentsOfURL:]"
+ "-[MantaFTABFile initWithContentsOfURL:]"
+ "-[MantaFTABFile parseFileData]"
+ "/0x%lx%n"
+ "<AMTADModeDevice %p>"
+ "<TAD Device %p>"
+ "@\"MantaFTABSubfile\""
+ "@%[^/]%n"
+ "AMAuthInstallPlatformCreateDataFromMappedFileURL returned %d"
+ "AMTADModeDevice"
+ "Adding OptionalFirmware: %@"
+ "Ap,SecurePageTableMonitor"
+ "Ap,TrustedExecutionMonitor"
+ "Ap,cL4"
+ "Apple Mobile Device (DFU Mode)"
+ "AppleKIS"
+ "Can't load plist since file path is NULL"
+ "Device discovery queue: %s"
+ "Device in use by another client. %d retries used."
+ "EnableDeviceInterfaceDaemon"
+ "Epoch"
+ "IOPropertyMatch"
+ "Interface in use by another client. %d retries used."
+ "MantaFTABFile"
+ "MantaFTABSubfile"
+ "OptionalFirmware"
+ "Read config 0x%x 0x%x 0x%x ... 0x%x 0x%x"
+ "Read config end portal: %d seq: 0x%x index: 0x%x words: %d"
+ "Read config error portal: %d seq: 0x%x index: 0x%x words: %d"
+ "Read config start portal: %d seq: 0x%x index: 0x%x words: %d"
+ "RecoveryOSAp,GFX1Firmware"
+ "Starting Device Discovery for DFU devices with VID 0x%x PID 0x%x"
+ "T@\"MantaFTABSubfile\",R,V_manifest"
+ "TADFUDevice"
+ "Unable to start discovery of Debug USB devices!"
+ "Write config end portal: %d seq: 0x%x index: 0x%x words: %d"
+ "Write config error portal: %d seq: 0x%x index: 0x%x words: %d"
+ "Write config response 0x%x 0x%x 0x%x 0x%x 0x%x"
+ "Write config start portal: %d seq: 0x%x index: 0x%x words: %d"
+ "Write data end portal: %d seq: 0x%x addr: 0x%llx bytes: %d"
+ "Write data error portal: %d seq: 0x%x addr: 0x%llx bytes: %d"
+ "Write data response 0x%x 0x%x 0x%x 0x%x 0x%x"
+ "Write data start portal: %d seq: 0x%x addr: 0x%llx bytes: %d"
+ "_AMAuthInstallApImg4StitchToURL"
+ "_AMAuthInstallSupportCreateDataFromCopiedOrMappedFileURL"
+ "_AMRTADModeDeviceFinalize"
+ "_AMRestoreCreateCFPropertyListWithContentsOfFile"
+ "_WriteStreamIntoFile"
+ "a device with a duplicate registry id was connected!"
+ "addDeviceToList"
+ "cfstring_to_c_string"
+ "com.apple.libDFU"
+ "com.apple.libDFU.deviceDiscoveryQueue"
+ "com.apple.libDFU.libraryOperationQueue"
+ "com.apple.purplerestore.device_notification"
+ "dfuDevicesAreEqual"
+ "excl"
+ "failed to restore device %s@%x with error %d\n"
+ "handleDevices"
+ "initServiceDiscoveryGlobals"
+ "initServiceDiscoveryGlobals_block_invoke"
+ "initWithBytesNoCopy:length:freeWhenDone:"
+ "initWithLength:"
+ "kUSBVendorString"
+ "keyForVIDPID"
+ "kis-kext"
+ "libauthinstall_device-1049.100.22"
+ "mutableBytes"
+ "q24@0:8@16"
+ "setLength:"
+ "sptm"
+ "taDFU_Daemon_deviceAddedCallback"
+ "taDFU_Daemon_deviceAddedGeneric"
+ "taDFU_Daemon_deviceAddedLocationIDHandler"
+ "taDFU_Daemon_deviceAddedVidPidHandler"
+ "taDFU_Daemon_deviceRemovedCallback"
+ "taDFU_Daemon_deviceRemovedGeneric"
+ "taDFU_Daemon_deviceRemovedLocationIDHandler"
+ "taDFU_Daemon_deviceRemovedVidPidHandler"
+ "taDFU_KISDaemon_download"
+ "taDFU_KISDaemon_epoch"
+ "taDFU_KISDaemon_nonce"
+ "taDFU_KISDaemon_release"
+ "taDFU_deviceinterfaced_createDFUDevice"
+ "taDFU_deviceinterfaced_startDeviceDiscoveryForVIDPID"
+ "taDFU_deviceinterfaced_startDeviceDiscoveryGeneric"
+ "taDFU_deviceinterfaced_startDeviceDiscoveryGeneric_block_invoke"
+ "taDFU_useKISKext"
+ "taDFU_use_deviceinterfaced"
+ "trxm"
+ "untranslated AMSupportError=%d"
- "%04d-%02d-%02d %02d:%02d:%02d.%03d %s[%d:%x]: "
- "%s failed to load %s: %d"
- "-[FTABFile addSubfileWithTagName:contentsOfURL:]"
- "-[FTABFile initWithContentsOfURL:]"
- "-[FTABFile parseFileData]"
- ".."
- "@\"FTABSubfile\""
- "AMAuthInstallApImg4Stitch"
- "AMAuthInstallPlatformCreateBufferFromNativeFilePath"
- "AMAuthInstallPlatformOpenFileStreamWithURL"
- "AMAuthInstallPlatformWriteBufferToNativeFilePath"
- "AMAuthInstallSupportCreateDataFromFileURL"
- "AMAuthInstallSupportCreateDictionaryFromFileURL"
- "AMFDRAppendPermissionsString"
- "AMFDRCopyClientId"
- "AMFDRCopyDeviceKeys"
- "AMFDRCopyDisposableKeys"
- "AMFDRCopyUnderlyingDictionary"
- "AMFDRCreateInstanceString"
- "AMFDRCreateLocalPending"
- "AMFDRCreatePermissionsString"
- "AMFDRCreateWithOptions"
- "AMFDRDataCopy"
- "AMFDRDataCopyDigest"
- "AMFDRDataCopySslRoots"
- "AMFDRDataCopyTrustObject"
- "AMFDRDataDelete"
- "AMFDRDataExport"
- "AMFDRDataIterate"
- "AMFDRDataLocalCreateFullKey"
- "AMFDRDataMultiCopy"
- "AMFDRDataMultiDelete"
- "AMFDRDataMultiExport"
- "AMFDRDataMultiPut"
- "AMFDRDataPrefetch"
- "AMFDRDataPresent"
- "AMFDRDataPut"
- "AMFDRDataPutForSysCfgKey"
- "AMFDRDataRecover"
- "AMFDRGetCert"
- "AMFDRGetInfo"
- "AMFDRGetOptions"
- "AMFDRGetSealingMap"
- "AMFDRGetTrustError"
- "AMFDRLogSetHandler"
- "AMFDRPerformManifestCheck"
- "AMFDRSealedDataCreate"
- "AMFDRSealedDataCreateSealingRequest"
- "AMFDRSealedDataPopulate"
- "AMFDRSealingMapCopyInstanceWithIdentifiers"
- "AMFDRSealingMapCopyLocalData"
- "AMFDRSealingMapCopyLocalDataForClass"
- "AMFDRSealingMapCopyLocalMinimalManifestForInstance"
- "AMFDRSealingMapCopyRequiredIdentifiers"
- "AMFDRSealingMapCreateAndPopulateSealedData"
- "AMFDRSealingMapCreateRecoveryPermissions"
- "AMFDRSealingMapGetEntriesForDevice"
- "AMFDRSealingMapGetEntry"
- "AMFDRSealingMapRecoverCurrentDevice"
- "AMFDRSealingMapSetMGCopyAnswer"
- "AMFDRSealingMapVerifyAndCommitSealedData"
- "AMFDRSealingMapVerifySealing"
- "AMFDRSetOption"
- "AMFDRSetRecoveryVerifier"
- "AMFDRSetSealingMap"
- "AMSupportCreateDataFromFileURL returned %d"
- "Can't load dictionary since file path is NULL"
- "FTABFile"
- "FTABSubfile"
- "Looks like the file we were expecting was deleted out from under us."
- "T@\"FTABSubfile\",R,V_manifest"
- "The file actually exists but is a symlink to %s, which is not there."
- "The file is actually a symlink but appears to be corrupted. readlink(2) returned %zd."
- "Tried to create a location ID for a disconnecting device but failed."
- "_AMRestoreCreateCFDictionaryWithContentsOfFile"
- "a device with a duplicate location id was connected!"
- "a device with no location id was connected!"
- "com.apple.purplerestore.device_notificaion"
- "failed to convert url to file system representation"
- "failed to create property list: %@"
- "failed to load %s: %s\n"
- "failed to load '%s' from '%s'\n"
- "failed to open file for writing: %s"
- "failed to stitch img4 file"
- "fstat failed: %s"
- "libauthinstall_device-1033.80.3"
- "lstat(2) says the file exists, even though open(2) failed to find it. Mabye a race condition?"
- "malloc(%d) failed: %s"
- "malloc(%zu) failed: %s"
- "open failed: %s"
- "path: %s"
- "read failed: %s"
- "srcFileURL is NULL"
- "tid:%x"
- "unable to create CFData"
- "unable to fstat DFU file: %s"
- "unable to mmap DFU file: %s"

```
