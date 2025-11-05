## OSInstaller

> `/System/Library/PrivateFrameworks/OSInstaller.framework/Versions/A/OSInstaller`

```diff

-1584.80.2.0.0
-  __TEXT.__text: 0x5775c
-  __TEXT.__auth_stubs: 0xc40
-  __TEXT.__objc_methlist: 0x3414
-  __TEXT.__cstring: 0xe219
-  __TEXT.__gcc_except_tab: 0x2344
+1591.101.1.0.0
+  __TEXT.__text: 0x5ff84
+  __TEXT.__auth_stubs: 0x10b0
+  __TEXT.__objc_methlist: 0x370c
+  __TEXT.__cstring: 0xff60
+  __TEXT.__gcc_except_tab: 0x23bc
   __TEXT.__ustring: 0x34
-  __TEXT.__const: 0xe0
-  __TEXT.__unwind_info: 0xc40
+  __TEXT.__const: 0x148
+  __TEXT.__oslogstring: 0xe11
+  __TEXT.__unwind_info: 0xce8
+  __TEXT.__eh_frame: 0xb4
   __TEXT.__objc_classname: 0x663
-  __TEXT.__objc_methname: 0xa6e7
-  __TEXT.__objc_methtype: 0x9be
-  __TEXT.__objc_stubs: 0x9880
-  __DATA_CONST.__got: 0x790
-  __DATA_CONST.__const: 0x238
+  __TEXT.__objc_methname: 0xa844
+  __TEXT.__objc_methtype: 0x9cf
+  __TEXT.__objc_stubs: 0x99c0
+  __DATA_CONST.__got: 0x7d0
+  __DATA_CONST.__const: 0x270
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2978
+  __DATA_CONST.__objc_selrefs: 0x2b00
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x170
-  __AUTH_CONST.__auth_got: 0x630
-  __AUTH_CONST.__const: 0xa60
-  __AUTH_CONST.__cfstring: 0x5f40
-  __AUTH_CONST.__objc_const: 0x5bf0
+  __AUTH_CONST.__auth_got: 0x868
+  __AUTH_CONST.__const: 0xa20
+  __AUTH_CONST.__cfstring: 0x64a0
+  __AUTH_CONST.__objc_const: 0x5720
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH.__objc_data: 0x1360
-  __DATA.__objc_ivar: 0x3f8
+  __DATA.__objc_ivar: 0x3fc
   __DATA.__data: 0x250
-  __DATA.__bss: 0xe0
+  __DATA.__bss: 0x100
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /System/Library/Frameworks/KernelManagement.framework/Versions/A/KernelManagement
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/Versions/A/AppleKeyStore
   - /System/Library/PrivateFrameworks/BridgeOSInstall.framework/Versions/A/BridgeOSInstall
   - /System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/DesktopServicesPriv
   - /System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/DiskImages

   - /System/Library/PrivateFrameworks/SystemMigration.framework/Versions/A/SystemMigration
   - /System/Library/PrivateFrameworks/SystemMigrationUtils.framework/Versions/A/SystemMigrationUtils
   - /System/Library/PrivateFrameworks/SystemPolicy.framework/Versions/A/SystemPolicy
+  - /System/Library/PrivateFrameworks/apfs_boot_mount.framework/Versions/A/apfs_boot_mount
   - /usr/lib/libIASAuthReboot.dylib
   - /usr/lib/libIASUnifiedProgress.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libamsupport.dylib
+  - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libc++.1.dylib
+  - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4F16FF64-B772-3E2D-A2F2-1A3DEAA35778
-  Functions: 1266
-  Symbols:   3742
-  CStrings:  4333
+  - /usr/lib/libpartition2_dynamic.dylib
+  UUID: 02489020-034D-3FFB-94A9-2C819251038B
+  Functions: 1423
+  Symbols:   3999
+  CStrings:  4735
 
Symbols:
+ +[OSIPrepareVolumeElement virtualMemoryFolderName].cold.1
+ +[OSISystemProfiler sharedProfiler].cold.1
+ +[OSIUtilities bless2Device:once:]
+ +[OSIUtilities blessDevice:once:]
+ +[OSIUtilities blessLegacyMode:path:once:]
+ +[OSIUtilities blessMountPoint:once:]
+ -[OSITemplateMigrationOptions migrateRequiringBuild]
+ -[OSITemplateMigrationOptions setMigrateRequiringBuild:]
+ -[OSSUUpdate initWithProductKey:withDistribution:withDistributionController:].cold.1
+ OBJC_IVAR_$_OSITemplateMigrationOptions._migrateRequiringBuild
+ _CFArrayGetTypeID
+ _CFBooleanGetValue
+ _CFDataCreateWithBytesNoCopy
+ _CFDictionaryGetTypeID
+ _CFEqual
+ _CFErrorGetCode
+ _CFNumberGetTypeID
+ _CFNumberGetValue
+ _CFPropertyListCreateWithData
+ _CFStringCompare
+ _CFStringCreateWithCString
+ _CFStringFindAndReplace
+ _CFStringGetCString
+ _CFStringGetFileSystemRepresentation
+ _CFStringGetMaximumSizeOfFileSystemRepresentation
+ _CGSInitialEnableOfDisplayUpdates
+ _IOBSDNameMatching
+ _IOConnectCallScalarMethod
+ _IOConnectCallStructMethod
+ _IOIteratorNext
+ _IOObjectConformsTo
+ _IOObjectGetClass
+ _IOObjectRetain
+ _IORegistryEntryCreateIterator
+ _IORegistryEntryGetChildIterator
+ _IORegistryEntryGetName
+ _IORegistryEntryGetParentEntry
+ _IOServiceGetMatchingServices
+ _Img4DecodeGetPayloadPropertiesInteger
+ _Img4DecodeGetPayloadType
+ _Img4DecodeGetPayloadVersion
+ _Img4DecodeInit
+ _Img4DecodeInitPayload
+ _MBSLog
+ _OBJC_CLASS_$_LPStaticAPFSVolume
+ _OBJC_CLASS_$_LPStaticMedia
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _UUID_NULL
+ __41+[OSIUtilities insistentUnmount:purpose:]_block_invoke.313
+ __48-[OSITemplateMigrationController startOperation]_block_invoke.147
+ __MergedGlobals
+ ___assert_rtn
+ ___isPlatformVersionAtLeast
+ ___memcpy_chk
+ ___strlcat_chk
+ __availability_version_check
+ __img4_chip_ap_reduced
+ __img4_chip_ap_sha2_384
+ __img4_chip_ap_vma2
+ __img4_runtime_default
+ __initializeAvailabilityCheck
+ __isPlatformVersionAtLeast.cold.1
+ __isPlatformVersionAtLeast.cold.2
+ __kCFSystemVersionBuildVersionKey
+ __os_log_default
+ __os_log_error_impl
+ __os_log_impl
+ _abm_get_isc_device_node
+ _abm_get_isc_device_path
+ _basename_r
+ _binary_to_hex_string
+ _bless2_boot_real
+ _bless2_boot_with_args
+ _bless2_isc_preboot
+ _bless2_os_preboot
+ _bless2_summarize
+ _bless2_summary_free
+ _bless2_verify_real
+ _bootobjects_path_internal
+ _bootpolicy_get_nsih
+ _bootpolicy_get_security_mode
+ _bootpolicy_volume_has_local_policy
+ _compatibilityInitializeAvailabilityCheck
+ _custom_i4rt_get_bool
+ _dispatch_once_f
+ _fcntl
+ _file_load
+ _file_unload
+ _fstat
+ _ftell
+ _fw_execute
+ _get_apfs_iokit
+ _get_apfs_role
+ _get_img4_tag
+ _get_iocv_property
+ _get_logger
+ _get_media_group_uuid
+ _get_nsih_path
+ _get_property_uuid
+ _getuid
+ _img4_chip_select_personalized_ap
+ _img4_firmware_destroy
+ _img4_firmware_execute
+ _img4_firmware_new
+ _img4_firmware_select_chip
+ _imgdec2errno
+ _initializeAvailabilityCheck
+ _isc_dev_for_role
+ _kCFAllocatorNull
+ _kCFBooleanTrue
+ _load_bootcaches
+ _log_context
+ _log_function
+ _malloc
+ _mmap
+ _munge_boot_volume
+ _munmap
+ _must_check_external
+ _objc_msgSend$bless2Device:once:
+ _objc_msgSend$compare:options:
+ _objc_msgSend$devNodePath
+ _objc_msgSend$initWithFormat:arguments:
+ _objc_msgSend$liveMediaForSnapshotAtPath:
+ _objc_msgSend$mediaForBSDNameOrDeviceNode:
+ _objc_msgSend$mediaForPath:isSnapshot:
+ _objc_msgSend$migrateRequiringBuild
+ _objc_msgSend$mountWithError:
+ _objc_msgSend$setMigrateRequiringBuild:
+ _open_dict_key
+ _os_log_type_enabled
+ _printf
+ _read
+ _rewind
+ _set_boot_volume_with_key
+ _set_smc_key
+ _smc_close
+ _smc_open
+ _smc_write_key
+ _snprintf
+ _sscanf
+ _string_for_bp_error
+ _strlcpy
+ _strlen
+ _strncmp
+ _strrchr
+ _strstr
+ _strtol
+ _uuid_copy
+ _uuid_is_null
+ _uuid_parse
+ _uuid_reswap
+ _uuid_unparse
+ _uuid_unparse_upper
+ _validate_device
+ _validate_object
+ _validate_uuid
+ _vol_role_disk
+ _volume_role_filter_
+ _volume_to_gpt
+ _walk_up_until
+ binary_to_hex_string.cold.1
+ bless2_boot_real.cold.1
+ bless2_boot_real.cold.2
+ bless2_boot_real.cold.3
+ bless2_boot_real.cold.4
+ bless2_boot_real.cold.5
+ bless2_boot_with_args.cold.1
+ bless2_boot_with_args.cold.10
+ bless2_boot_with_args.cold.11
+ bless2_boot_with_args.cold.12
+ bless2_boot_with_args.cold.13
+ bless2_boot_with_args.cold.14
+ bless2_boot_with_args.cold.15
+ bless2_boot_with_args.cold.16
+ bless2_boot_with_args.cold.2
+ bless2_boot_with_args.cold.3
+ bless2_boot_with_args.cold.4
+ bless2_boot_with_args.cold.5
+ bless2_boot_with_args.cold.6
+ bless2_boot_with_args.cold.7
+ bless2_boot_with_args.cold.8
+ bless2_boot_with_args.cold.9
+ bless2_summarize.cold.1
+ bless2_summarize.cold.10
+ bless2_summarize.cold.2
+ bless2_summarize.cold.3
+ bless2_summarize.cold.4
+ bless2_summarize.cold.5
+ bless2_summarize.cold.6
+ bless2_summarize.cold.7
+ bless2_summarize.cold.8
+ bless2_summarize.cold.9
+ bless2_verify_real.cold.1
+ bless2_verify_real.cold.2
+ bless2_verify_real.cold.3
+ bootobjects_path_internal.cold.1
+ bootobjects_path_internal.cold.2
+ bootobjects_path_internal.cold.3
+ bootobjects_path_internal.cold.4
+ file_load.cold.1
+ file_load.cold.2
+ file_load.cold.3
+ file_load.cold.4
+ file_load.cold.5
+ file_unload.cold.1
+ get_apfs_role.cold.1
+ get_apfs_role.cold.2
+ get_img4_tag.cold.1
+ get_img4_tag.cold.2
+ get_media_group_uuid.cold.1
+ get_nsih_path.cold.1
+ get_nsih_path.cold.2
+ get_nsih_path.cold.3
+ get_nsih_path.cold.4
+ get_nsih_path.cold.5
+ get_nsih_path.cold.6
+ get_property_uuid.cold.1
+ get_property_uuid.cold.2
+ get_property_uuid.cold.3
+ imgdec2errno.cold.1
+ isc_dev_for_role.cold.1
+ isc_dev_for_role.cold.2
+ load_bootcaches.cold.1
+ load_bootcaches.cold.2
+ load_bootcaches.cold.3
+ load_bootcaches.cold.4
+ load_bootcaches.cold.5
+ load_bootcaches.cold.6
+ load_bootcaches.cold.7
+ munge_boot_volume.cold.1
+ munge_boot_volume.cold.2
+ must_check_external.cold.1
+ must_check_external.cold.2
+ must_check_external.cold.3
+ must_check_external.cold.4
+ must_check_external.cold.5
+ open_dict_key.cold.1
+ set_boot_volume_with_key.cold.1
+ set_boot_volume_with_key.cold.2
+ set_boot_volume_with_key.cold.3
+ set_boot_volume_with_key.cold.4
+ smc_close.cold.1
+ smc_close.cold.2
+ smc_close.cold.3
+ smc_open.cold.1
+ smc_open.cold.2
+ smc_open.cold.3
+ smc_open.cold.4
+ smc_write_key.cold.1
+ smc_write_key.cold.2
+ smc_write_key.cold.3
+ uuid_reswap.cold.1
+ validate_device.cold.1
+ validate_device.cold.2
+ validate_device.cold.3
+ validate_device.cold.4
+ validate_device.cold.5
+ validate_object.cold.1
+ validate_object.cold.2
+ validate_object.cold.3
+ validate_object.cold.4
+ validate_object.cold.5
+ validate_object.cold.6
+ vol_role_disk.cold.1
+ vol_role_disk.cold.2
+ vol_role_disk.cold.3
+ vol_role_disk.cold.4
+ volume_to_gpt.cold.1
+ volume_to_gpt.cold.2
- _IOConnectCallMethod
- __48-[OSITemplateMigrationController startOperation]_block_invoke.135
- ___41+[OSIUtilities insistentUnmount:purpose:]_block_invoke_2
- ___chkstk_darwin
- ___get_aks_client_connection_block_invoke
- ___get_aks_client_dispatch_queue_block_invoke
- ___stdoutp
- __block_descriptor_tmp.141
- __block_descriptor_tmp.160
- __block_literal_global.162
- __copy_aks_client_connection
- _aks_fv_set_protection
- _ccder_blob_decode_range
- _ccder_blob_encode_body_tl
- _ccder_blob_encode_tl
- _der_utils_decode_fv_data
- _der_utils_decode_implicit_raw_octet_string_copy_len
- _der_utils_encode_fv_data
- _der_utils_encode_fv_params
- _fprintf
- _get_aks_client_connection
- _memset_s
- get_aks_client_connection.connection
- get_aks_client_dispatch_queue.connection_queue
- get_aks_client_dispatch_queue.onceToken
CStrings:
+ "!(out->data & FILE_MMAPPED_FLAG)"
+ "!error"
+ "%02hhX"
+ "%d.%d.%d"
+ "%s/%s"
+ "%s/%s/%s/%s"
+ "%s/boot/%s"
+ "%s: The provided devNode is nil."
+ "%s: could not get path for external preboot volume\n"
+ "%s: could not get path for policy volume\n"
+ "%s: could not get path for preboot volume\n"
+ "%s:%s:%s"
+ "+[OSIUtilities bless2Device:once:]"
+ "--bootefi"
+ "--nextonly"
+ "40A0DDD2-77F8-4392-B4A3-1E7304206516:alt-boot-volume"
+ "40A0DDD2-77F8-4392-B4A3-1E7304206516:boot-volume"
+ "52637672-7900-11AA-AA11-00306543ECAC"
+ "69646961-6700-11AA-AA11-00306543ECAC"
+ "7C3457EF-0000-11AA-AA11-00306543ECAC"
+ "ACM error in Boot Policy"
+ "AppleAPFSContainerScheme"
+ "AppleAPFSVolume"
+ "AppleSMC"
+ "B36@0:8@16@24B32"
+ "BOOT_KEY_BOOT_ONCE"
+ "BOOT_KEY_EXT_PREBOOT_FD"
+ "BOOT_KEY_EXT_PREBOOT_PATH"
+ "BOOT_KEY_NOVERIFY"
+ "BOOT_KEY_POLICY_FD"
+ "BOOT_KEY_POLICY_PATH"
+ "BOOT_KEY_PREBOOT_FD"
+ "BOOT_KEY_PREBOOT_PATH"
+ "BSD Name"
+ "Bless-once of %@ failed with status %d"
+ "Bless-once of %@ succeeded!"
+ "Bless-once output:\n%@"
+ "Boot Policy data size error"
+ "Boot Policy file I/O error"
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetFileSystemRepresentation(cfstr, path, max)"
+ "CFStringGetTypeID"
+ "Calling bless2_boot_with_args() for target %@ and args: %@"
+ "Cannot Bless-once: %@ doesn't exist."
+ "Cannot find device for path: %@"
+ "Content Hint"
+ "Could not create firmware object"
+ "Could not create firmware object\n"
+ "Current security mode is %s\n"
+ "Device Characteristics"
+ "EmbeddedDeviceTypeRoot"
+ "Error in SEP communication"
+ "Error in SEP storage"
+ "Failed to gather either LPAPFSMedia for Preboot(%s)[%@] or iSCPreboot(%s)[%@]."
+ "Failed to mount isc_preboot_media(%s) due to error. %@"
+ "Failed to mount preboot_media(%s) due to error. %@"
+ "Full"
+ "Generic BootPolicy error"
+ "IOBlockStorageDevice"
+ "IOGUIDPartitionScheme"
+ "IOMedia"
+ "IOService"
+ "Image4 error in Boot Policy"
+ "Incorrect type for argument: %s\n"
+ "Invalid Startup Disk"
+ "Invalid file descriptor value %d for argument %s\n"
+ "Invalid underlying gpt type '%s'\n"
+ "Key not written to the SMC; continuing..."
+ "Key not written to the SMC; continuing...\n"
+ "Key store error in Boot Policy"
+ "Missing argument: %s or %s required\n"
+ "NVRAM set %s = %s\n"
+ "No valid chip was available for this firmware"
+ "No valid chip was available for this firmware\n"
+ "Permissive"
+ "Physical Interconnect"
+ "Protocol Characteristics"
+ "Recovery"
+ "Reduced"
+ "Role"
+ "Security mode error in Boot Policy"
+ "SupportsExternalPrebootObjects"
+ "T@\"NSString\",&,V_migrateRequiringBuild"
+ "Template Migration: A required build of (%@) is set, but the SystemVerison.plist is empty."
+ "Template Migration: A required build of (%@) is set, however the target has (%@)."
+ "Template Migration: Existing Template is in-sync with System volume, and options are set not to template migrate in this state."
+ "Template Migration: Setting requiredTasks to OSITemplateMigrationTasksNothing"
+ "Template Migration: Unmount Errors (In-Order): %@"
+ "TemplateMigrationRequireBuildKey"
+ "Unknown BootPolicy error"
+ "Version"
+ "Virtual Interface"
+ "VolGroupUUID"
+ "[iocv="
+ "_migrateRequiringBuild"
+ "backing storage looks like a diskimage"
+ "backing storage looks like a diskimage\n"
+ "bad type for external preboot key in bootcaches"
+ "bad type for external preboot key in bootcaches\n"
+ "binary_to_hex_string"
+ "bless2"
+ "bless2 entry is not a dictionary"
+ "bless2 entry is not a dictionary\n"
+ "bless2.c"
+ "bless2Device:once:"
+ "bless2_boot_with_args"
+ "bless2_boot_with_args() failed: %d (%s)"
+ "bless2_isc_preboot failed for a bless2_summarize of the dev_node:%@"
+ "bless2_os_preboot failed for a bless2_summarize of the dev_node:%@"
+ "bless2_summarize failed for %@: %d (%s)"
+ "blessDevice:once:"
+ "blessLegacyMode:path:once:"
+ "blessMountPoint:once:"
+ "boot object %s failed to verify: %d\n"
+ "boot_once"
+ "cannot allocate volume properties"
+ "cannot allocate volume properties\n"
+ "cannot convert dev node to cstring"
+ "cannot convert dev node to cstring\n"
+ "cannot convert device path name to cstring"
+ "cannot convert device path name to cstring\n"
+ "cannot convert uuid to cstring"
+ "cannot convert uuid to cstring\n"
+ "cannot create cfdata"
+ "cannot create cfdata\n"
+ "cannot create key string"
+ "cannot create key string\n"
+ "cannot create property string"
+ "cannot create property string\n"
+ "cannot deserialize plist, cf error %zd\n"
+ "cannot determine container type %d\n"
+ "cannot find gpt"
+ "cannot find gpt\n"
+ "cannot find isc container"
+ "cannot find isc container\n"
+ "cannot find uuid for volume: %d\n"
+ "cannot form nsih string for path, %d\n"
+ "cannot get ISC preboot volume mount point, %d\n"
+ "cannot get boot triple %d\n"
+ "cannot get bsd dev node"
+ "cannot get bsd dev node\n"
+ "cannot get current active nsih value, %s\n"
+ "cannot get current security mode, %s\n"
+ "cannot get external preboot volume mount point, %d\n"
+ "cannot get gpt slice uuid %d\n"
+ "cannot get local policy status, %s\n"
+ "cannot get nvram entry"
+ "cannot get nvram entry\n"
+ "cannot get policy volume mount point, %d\n"
+ "cannot get preboot volume mount point, %d\n"
+ "cannot get protocol characteristics"
+ "cannot get protocol characteristics\n"
+ "cannot get service"
+ "cannot get service\n"
+ "cannot get tag for object payload, %d\n"
+ "cannot get uuid ???"
+ "cannot get uuid ???\n"
+ "cannot get volume uuid %d\n"
+ "cannot get volume's container"
+ "cannot get volume's container\n"
+ "cannot iterate children, mach err 0x%x\n"
+ "cannot load bootcaches.plist %d\n"
+ "cannot load bootcaches.plist file %d\n"
+ "cannot open bootcaches.plist file %d\n"
+ "cannot parse object payload as an im4p, %d\n"
+ "cannot set property mach err 0x%x\n"
+ "cannot set the container UUID %d\n"
+ "cf_is_dict(plist)"
+ "child %s, class %s\n"
+ "com.apple.bless"
+ "compare:options:"
+ "container type uuid '%s'\n"
+ "container uuid '%s'\n"
+ "could not allocate memory for version string: %d\n"
+ "could not extract last path component from %s: %d"
+ "could not find AppleSMC kext: %X\n"
+ "could not find iBoot img4 file: %s\n"
+ "could not get AppleSMC kext from iterator"
+ "could not get AppleSMC kext from iterator\n"
+ "could not get device path for iSC preboot, %d\n"
+ "could not get iterator for volume device: %X\n"
+ "could not get version string for iBoot img4"
+ "could not get version string for iBoot img4\n"
+ "could not initiate communication with AppleSMC service: %X\n"
+ "could not open AppleSMC service: %X\n"
+ "could not open boot object %s: %d\n"
+ "could not parse %s as an Image4 file: %d\n"
+ "could not read contents of boot object %s: %d\n"
+ "could not read contents of iBoot img4 file: %s\n"
+ "could not send close message to AppleSMC service: %X\n"
+ "could not write AppleSMC key: %X\n"
+ "devNodePath"
+ "disk is external?: %d\n"
+ "error closing AppleSMC service: %X\n"
+ "ext_preboot_path"
+ "ext_preboot_vol"
+ "file %llu too large %lld\n"
+ "file_load"
+ "file_load_len"
+ "get_apfs_role"
+ "get_media_group_uuid"
+ "group uuid '%s'\n"
+ "initWithFormat:arguments:"
+ "invalid I/O port for writing SMC key"
+ "invalid I/O port for writing SMC key\n"
+ "invalid type for device characteristics"
+ "invalid type for device characteristics\n"
+ "invalid type for invalid-startup-disk property"
+ "invalid type for invalid-startup-disk property\n"
+ "iokit returned non-uuid"
+ "iokit returned non-uuid\n"
+ "is_apfs_volume(vol)"
+ "kCFAllocatorNull"
+ "liveMediaForSnapshotAtPath:"
+ "mediaForBSDNameOrDeviceNode:"
+ "mediaForPath:isSnapshot:"
+ "migrateRequiringBuild"
+ "missing bless2 plist dictionary"
+ "missing bless2 plist dictionary\n"
+ "mountWithError:"
+ "munmap failed with %d\n"
+ "no 'iocv' payload property in iBoot, looking at version string"
+ "no 'iocv' payload property in iBoot, looking at version string\n"
+ "no 'iocv' property in version string"
+ "no 'iocv' property in version string\n"
+ "no device characteristics for volume"
+ "no device characteristics for volume\n"
+ "not backed by gpt"
+ "not backed by gpt\n"
+ "noverify"
+ "numChars >= 0"
+ "only read %zd of %zu bytes (%d)\n"
+ "open_dict_key"
+ "parent of container scheme is ???"
+ "parent of container scheme is ???\n"
+ "parent of container scheme is not gpt, it's '%s'(%zu)\n"
+ "plist_deserialize"
+ "policy_path"
+ "policy_vol"
+ "preboot_path"
+ "preboot_vol"
+ "r"
+ "restore"
+ "root privilege is required to set the boot volume"
+ "root privilege is required to set the boot volume\n"
+ "sEOC SMC key will not be written.  Continuing..."
+ "sEOC SMC key will not be written.  Continuing...\n"
+ "save && (save != EINVAL)"
+ "setMigrateRequiringBuild:"
+ "string too small for nsih path"
+ "string too small for nsih path\n"
+ "the volume does not have a group uuid"
+ "the volume does not have a group uuid\n"
+ "unmapped img4 error %d\n"
+ "usr/standalone/bootcaches.plist"
+ "usr/standalone/firmware/devicetree.img4"
+ "usr/standalone/firmware/iBoot.img4"
+ "uuid_reswap"
+ "value too large for SMC communication: %lu bytes\n"
+ "volume has no local policy"
+ "volume has no local policy\n"
+ "volume not on a valid boot device (per registry property)"
+ "volume not on a valid boot device (per registry property)\n"
+ "volume uuid '%s'\n"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "+[OSIUtilities insistentUnmount:purpose:]_block_invoke_2"
- "AppleKeyStore"
- "IOService:/IOResources/AppleKeyStore"
- "Template Migration: Existing Template is in-sync with System volume, and options are set not to template migrate in this state. Nothing to do."
- "Template Migration: Failed to unmount the %@ volume: %@"
- "aks"
- "aks-client-queue"
- "aks_fv_prot_cmd_stash_commit = %d"
- "aks_fv_prot_cmd_stash_destroy = %d"
- "aks_fv_set_protection"
- "failed to open connection to %s\n"

```
