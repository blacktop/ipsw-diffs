## icprefd-xpc

> `/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/icprefd-xpc.xpc/icprefd-xpc`

```diff

-2019.0.0.0.0
-  __TEXT.__text: 0x6ec4
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_stubs: 0xa00
-  __TEXT.__objc_methlist: 0x244
-  __TEXT.__cstring: 0x21dc
-  __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x410
-  __TEXT.__objc_methname: 0xaea
-  __TEXT.__oslogstring: 0x75
+2020.1.5.0.0
+  __TEXT.__text: 0x2a4c
+  __TEXT.__auth_stubs: 0x280
+  __TEXT.__objc_stubs: 0x740
+  __TEXT.__objc_methlist: 0x11c
+  __TEXT.__const: 0x18
+  __TEXT.__gcc_except_tab: 0x34
+  __TEXT.__cstring: 0x7ef
+  __TEXT.__oslogstring: 0x1a
+  __TEXT.__objc_methname: 0x78b
+  __TEXT.__objc_classname: 0x2a
+  __TEXT.__objc_methtype: 0x115
   __TEXT.__ustring: 0xe
-  __TEXT.__objc_classname: 0x43
-  __TEXT.__objc_methtype: 0x1d6
-  __TEXT.__unwind_info: 0x1e0
-  __DATA_CONST.__auth_got: 0x250
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x2b8
-  __DATA_CONST.__cfstring: 0x1fc0
-  __DATA_CONST.__objc_classlist: 0x10
+  __TEXT.__unwind_info: 0xb8
+  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__got: 0x108
+  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__cfstring: 0x740
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_intobj: 0x6c0
-  __DATA_CONST.__objc_arraydata: 0x2880
-  __DATA_CONST.__objc_dictobj: 0x21c0
-  __DATA.__objc_const: 0x278
-  __DATA.__objc_selrefs: 0x310
-  __DATA.__objc_ivar: 0x14
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x68
-  __DATA.__common: 0x8
-  __DATA.__bss: 0x38
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA.__objc_const: 0x148
+  __DATA.__objc_selrefs: 0x228
+  __DATA.__objc_ivar: 0xc
+  __DATA.__objc_data: 0x50
+  __DATA.__data: 0x60
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/ImageCaptureDevices.framework/ImageCaptureDevices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: B16D9E00-C235-3219-900A-21282646A262
-  Functions: 84
-  Symbols:   360
-  CStrings:  656
+  UUID: 3675E345-F48E-3996-9404-C54EC70AA859
+  Functions: 25
+  Symbols:   186
+  CStrings:  210
 
Symbols:
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ICAuthManagerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ICAuthManagerProtocol
+ __OBJC_LABEL_PROTOCOL_$_ICAuthManagerProtocol
+ __OBJC_PROTOCOL_$_ICAuthManagerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ICAuthManagerProtocol
+ _objc_msgSend$_xpcConnection
+ _objc_msgSend$captureReadUserIntentForBundleIdentifier:withNotification:
+ _objc_msgSend$captureUserIntentForConnection:accessType:
+ _objc_msgSend$captureUserIntentForControlWithBundleIdentifier:withNotification:
+ _objc_msgSend$getControlNotifiedStatusWithBundleIdentifier:
+ _objc_msgSend$setControlNotifiedStatus:withBundleIdentifier:
+ _objc_release_x22
- +[ICDeviceAccessManager sharedAccessManager]
- +[ICDeviceAccessManager sharedAccessManager].cold.1
- -[ICDeviceAccessManager addBundleIdentifier:]
- -[ICDeviceAccessManager addBundleIdentifier:].cold.1
- -[ICDeviceAccessManager allBundleIdentifiers]
- -[ICDeviceAccessManager bundleIdentifier:stateForAccessType:]
- -[ICDeviceAccessManager bundleIdentifiersAccessingExternalCamerasWithStatus]
- -[ICDeviceAccessManager bundleIdentifiersAccessingExternalCameras]
- -[ICDeviceAccessManager bundleIdentifiersWithAccessType:]
- -[ICDeviceAccessManager captureUserIntentForBundleIdentifier:withNotification:]
- -[ICDeviceAccessManager captureUserIntentForControlWithBundleIdentifier:withNotification:]
- -[ICDeviceAccessManager connection:stateForAccessType:]
- -[ICDeviceAccessManager dealloc]
- -[ICDeviceAccessManager dealloc].cold.1
- -[ICDeviceAccessManager deviceAccessQueue]
- -[ICDeviceAccessManager displayAlertForApplication:withNotification:completionBlock:]
- -[ICDeviceAccessManager displayAlertForControlWithNotification:completionBlock:]
- -[ICDeviceAccessManager externalMediaAccessDB]
- -[ICDeviceAccessManager init]
- -[ICDeviceAccessManager openDB:]
- -[ICDeviceAccessManager revokeBundleIdentifier:]
- -[ICDeviceAccessManager revokeBundleIdentifier:].cold.1
- -[ICDeviceAccessManager setDeviceAccessQueue:]
- -[ICDeviceAccessManager setExternalMediaAccessDB:]
- -[ICDeviceAccessManager updateApplicationWithBundleIdentifier:withStatus:]
- -[ICDeviceAccessManager updateBundleIdentifier:accessType:withState:]
- -[ICDeviceAccessManager validateBundleIdentifierInstalled:]
- GCC_except_table11
- GCC_except_table12
- GCC_except_table15
- GCC_except_table17
- GCC_except_table2
- GCC_except_table22
- GCC_except_table26
- GCC_except_table33
- GCC_except_table36
- GCC_except_table39
- GCC_except_table8
- ICLocalizedString.bundle
- ICLocalizedString.cold.1
- ICLocalizedString.once
- OBJC_IVAR_$_ICDeviceAccessManager._deviceAccessQueue
- OBJC_IVAR_$_ICDeviceAccessManager._externalMediaAccessDB
- _CFErrorCopyDescription
- _CFUserNotificationCreate
- _CFUserNotificationReceiveResponse
- _ICAcessQuery
- _ICAcessStatusQuery
- _ICLoggingDomain
- _OBJC_CLASS_$_NSBundle
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_NSFileManager
- _OBJC_CLASS_$_NSProcessInfo
- _OBJC_METACLASS_$_ICDeviceAccessManager
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- __29-[ICDeviceAccessManager init]_block_invoke.cold.1
- __29-[ICDeviceAccessManager init]_block_invoke.cold.2
- __45-[ICDeviceAccessManager allBundleIdentifiers]_block_invoke.cold.1
- __48-[ICDeviceAccessManager revokeBundleIdentifier:]_block_invoke.cold.1
- __57-[ICDeviceAccessManager bundleIdentifiersWithAccessType:]_block_invoke.cold.1
- __59-[ICDeviceAccessManager validateBundleIdentifierInstalled:]_block_invoke.cold.1
- __63-[ICRemotePrefManager checkFilesAndFoldersAccess:shouldPrompt:]_block_invoke.89
- __66-[ICDeviceAccessManager bundleIdentifiersAccessingExternalCameras]_block_invoke.cold.1
- __69-[ICDeviceAccessManager updateBundleIdentifier:accessType:withState:]_block_invoke.128
- __69-[ICDeviceAccessManager updateBundleIdentifier:accessType:withState:]_block_invoke.cold.1
- __69-[ICDeviceAccessManager updateBundleIdentifier:accessType:withState:]_block_invoke_2.cold.1
- __74-[ICDeviceAccessManager updateApplicationWithBundleIdentifier:withStatus:]_block_invoke.70
- __74-[ICDeviceAccessManager updateApplicationWithBundleIdentifier:withStatus:]_block_invoke.cold.1
- __76-[ICDeviceAccessManager bundleIdentifiersAccessingExternalCamerasWithStatus]_block_invoke.cold.1
- __ICOSLogCreate.cold.1
- __ICOSLogCreate.onceToken
- __OBJC_$_CLASS_METHODS_ICDeviceAccessManager
- __OBJC_$_INSTANCE_METHODS_ICDeviceAccessManager
- __OBJC_$_INSTANCE_VARIABLES_ICDeviceAccessManager
- __OBJC_$_PROP_LIST_ICDeviceAccessManager
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ICXPCAuthManagerProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_ICXPCAuthManagerProtocol
- __OBJC_CLASS_RO_$_ICDeviceAccessManager
- __OBJC_LABEL_PROTOCOL_$_ICXPCAuthManagerProtocol
- __OBJC_METACLASS_RO_$_ICDeviceAccessManager
- __OBJC_PROTOCOL_$_ICXPCAuthManagerProtocol
- __OBJC_PROTOCOL_REFERENCE_$_ICXPCAuthManagerProtocol
- ___29-[ICDeviceAccessManager init]_block_invoke
- ___44+[ICDeviceAccessManager sharedAccessManager]_block_invoke
- ___45-[ICDeviceAccessManager addBundleIdentifier:]_block_invoke
- ___45-[ICDeviceAccessManager allBundleIdentifiers]_block_invoke
- ___48-[ICDeviceAccessManager revokeBundleIdentifier:]_block_invoke
- ___57-[ICDeviceAccessManager bundleIdentifiersWithAccessType:]_block_invoke
- ___59-[ICDeviceAccessManager validateBundleIdentifierInstalled:]_block_invoke
- ___63-[ICRemotePrefManager checkFilesAndFoldersAccess:shouldPrompt:]_block_invoke
- ___66-[ICDeviceAccessManager bundleIdentifiersAccessingExternalCameras]_block_invoke
- ___69-[ICDeviceAccessManager updateBundleIdentifier:accessType:withState:]_block_invoke
- ___69-[ICDeviceAccessManager updateBundleIdentifier:accessType:withState:]_block_invoke_2
- ___74-[ICDeviceAccessManager updateApplicationWithBundleIdentifier:withStatus:]_block_invoke
- ___76-[ICDeviceAccessManager bundleIdentifiersAccessingExternalCamerasWithStatus]_block_invoke
- ___79-[ICDeviceAccessManager captureUserIntentForBundleIdentifier:withNotification:]_block_invoke
- ___90-[ICDeviceAccessManager captureUserIntentForControlWithBundleIdentifier:withNotification:]_block_invoke
- ___ICLocalizedString_block_invoke
- _____ICOSLogCreate_block_invoke
- ___block_descriptor_32_e20_v16?0^{__CFError=}8l
- ___block_descriptor_40_e8_32r_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16lr32l8
- ___block_descriptor_48_e8_32o40r_e11_v20?0B8Q12lr40l8s32l8
- ___block_descriptor_48_e8_32o40r_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16lr40l8s32l8
- ___block_descriptor_48_e8_32o40r_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16ls32l8r40l8
- ___block_descriptor_56_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32o40o48r_e5_v8?0ls32l8r48l8s40l8
- ___block_descriptor_64_e8_32o40o48o56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_descriptor_72_e8_32o40o48o56o_e5_v8?0ls32l8s40l8s48l8s56l8
- __block_literal_global.11
- __block_literal_global.130
- __block_literal_global.40
- __block_literal_global.73
- __os_log_default
- __os_log_error_impl
- _dispatch_async
- _dispatch_queue_create
- _dispatch_time
- _kCFAllocatorDefault
- _kTCCServiceExternalCameraMedia
- _objc_msgSend$addObjectsFromArray:
- _objc_msgSend$allBundleIdentifiers
- _objc_msgSend$array
- _objc_msgSend$bundleIdentifiersWithAccessType:
- _objc_msgSend$bundleWithPath:
- _objc_msgSend$captureUserIntentForBundleIdentifier:withNotification:
- _objc_msgSend$containsObject:
- _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
- _objc_msgSend$date
- _objc_msgSend$defaultManager
- _objc_msgSend$deviceAccessQueue
- _objc_msgSend$displayAlertForApplication:withNotification:completionBlock:
- _objc_msgSend$displayAlertForControlWithNotification:completionBlock:
- _objc_msgSend$externalMediaAccessDB
- _objc_msgSend$fileExistsAtPath:
- _objc_msgSend$intValue
- _objc_msgSend$integerValue
- _objc_msgSend$localizedStringForKey:value:table:
- _objc_msgSend$numberWithInteger:
- _objc_msgSend$objectForKeyedSubscript:
- _objc_msgSend$openDB:
- _objc_msgSend$processInfo
- _objc_msgSend$processName
- _objc_msgSend$revokeBundleIdentifier:
- _objc_msgSend$stringByAppendingPathComponent:
- _objc_msgSend$stringWithUTF8String:
- _objc_msgSend$timeIntervalSince1970
- _objc_msgSend$validateBundleIdentifierInstalled:
- _os_log_create
- _sqlite3_close
- _sqlite3_exec
- _sqlite3_open
- _tcc_attributed_entity_get_path
- _tcc_authorization_record_get_authorization_right
- _tcc_authorization_record_get_authorization_value
- _tcc_authorization_record_get_service
- _tcc_authorization_record_get_subject_attributed_entity
- _tcc_authorization_record_get_subject_identity
- _tcc_credential_create_for_process_with_audit_token
- _tcc_identity_create
- _tcc_identity_get_identifier
- _tcc_message_options_create
- _tcc_message_options_set_reply_handler_policy
- _tcc_message_options_set_request_usage_string_policy
- _tcc_server_create
- _tcc_server_message_get_authorization_records_by_identity
- _tcc_server_message_get_authorization_records_by_service
- _tcc_server_message_request_authorization
- _tcc_server_message_request_authorization_change
- _tcc_server_message_set_authorization_value
- _tcc_service_get_name
- _tcc_service_singleton_for_CF_name
- _tcc_service_singleton_for_name
- _xpc_bool_get_value
- _xpc_connection_copy_entitlement_value
- _xpc_connection_get_audit_token
- sharedAccessManager.mgr
- sharedAccessManager.onceToken
CStrings:
+ "(good news) ---> New kTCCServiceExternalCameraMedia Service"
+ "ICAuthManagerProtocol"
+ "_xpcConnection"
+ "captureReadUserIntentForBundleIdentifier:withNotification:"
+ "captureUserIntentForConnection:accessType:"
+ "getControlNotifiedStatusWithBundleIdentifier:"
+ "setControlNotifiedStatus:withBundleIdentifier:"
- "%@ (read) Access State %d, adding"
- "%@ (read) Access State Unknown, not adding"
- "%@ (read) Access State Unknown, not updating"
- "%@ (write) Access State %d, adding"
- "%@ (write) Access State Unknown, not adding"
- "%@ (write) Access State Unknown, not updating"
- "%@ Setting (read) Access State %d"
- "%@ Setting (write) Access State %d"
- "%@ is already in the database, will not be added again"
- "%s"
- "%{public}20s ! %{public}@"
- "(check) Authorization Right: %llu"
- "(check) Granted %@ access to *contents* on external device"
- "(check) User denied or disabled %@ access to *contents* on external device"
- "(prompt) ---> New kTCCServiceExternalCameraMedia Service"
- "(prompt) Granted %@ access to *contents* on external device"
- "(prompt) User denied or disabled %@ access to *contents* on external device"
- "/System/Library/Frameworks/ImageCaptureCore.framework"
- "/var/mobile/Library/com.apple.imagecapture"
- "???"
- "@\"NSObject<OS_dispatch_queue>\""
- "@24@0:8@16"
- "B24@0:8@16"
- "Bundle was not found to be installed on the device, revoking access defensively to require the user to re-authorize upon install."
- "Bundle:%s -- value: %llu"
- "CREATE TABLE IF NOT EXISTS external_device_access (ID INTEGER PRIMARY KEY AUTOINCREMENT, bundle_id TEXT, date_added INTEGER, read_access INTEGER, write_access INTEGER, control_informed INTEGER)"
- "DELETE FROM external_device_access WHERE bundle_id IS '%@';"
- "DEPRECATED"
- "EEXIST"
- "ENOSPC"
- "EPERM"
- "Failed to close database"
- "Failed to create table: external_device_access - %s"
- "Failed to open/create database"
- "ICDeviceAccessManager"
- "ICDeviceAccessManagerQueue"
- "ICLegacyReturnCodeCannotYieldDevice"
- "ICLegacyReturnCodeCommunicationErr"
- "ICLegacyReturnCodeDataTypeNotFoundErr"
- "ICLegacyReturnCodeDeviceAlreadyOpenErr"
- "ICLegacyReturnCodeDeviceIOServicePathNotFoundErr"
- "ICLegacyReturnCodeDeviceInternalErr"
- "ICLegacyReturnCodeDeviceInvalidParamErr"
- "ICLegacyReturnCodeDeviceLocationIDNotFoundErr"
- "ICLegacyReturnCodeDeviceMemoryAllocationErr"
- "ICLegacyReturnCodeDeviceNotFoundErr"
- "ICLegacyReturnCodeDeviceNotOpenErr"
- "ICLegacyReturnCodeDeviceUnsupportedErr"
- "ICLegacyReturnCodeExtensionInternalErr"
- "ICLegacyReturnCodeFileCorruptedErr"
- "ICLegacyReturnCodeFrameworkInternalErr"
- "ICLegacyReturnCodeIOPendingErr"
- "ICLegacyReturnCodeIndexOutOfRangeErr"
- "ICLegacyReturnCodeInvalidObjectErr"
- "ICLegacyReturnCodeInvalidPropertyErr"
- "ICLegacyReturnCodeInvalidSessionErr"
- "ICLegacyReturnCodePropertyTypeNotFoundErr"
- "ICReturnCommunicationTimedOut"
- "ICReturnConnectionFailedToOpen"
- "ICReturnDeleteFilesCanceled"
- "ICReturnDeleteFilesFailed"
- "ICReturnDeviceCommandGeneralFailure"
- "ICReturnDeviceCouldNotPair"
- "ICReturnDeviceFailedToCloseSession"
- "ICReturnDeviceFailedToCompleteTransfer"
- "ICReturnDeviceFailedToOpenSession"
- "ICReturnDeviceFailedToSendData"
- "ICReturnDeviceFailedToTakePicture"
- "ICReturnDeviceIsBusyEnumerating"
- "ICReturnDeviceIsPasscodeLocked"
- "ICReturnDeviceNeedsCredentials"
- "ICReturnDeviceSoftwareInstallationCanceled"
- "ICReturnDeviceSoftwareInstallationCompleted"
- "ICReturnDeviceSoftwareInstallationFailed"
- "ICReturnDeviceSoftwareIsBeingInstalled"
- "ICReturnDeviceSoftwareNotAvailable"
- "ICReturnDeviceSoftwareNotInstalled"
- "ICReturnDownloadCanceled"
- "ICReturnDownloadFailed"
- "ICReturnFailedToCompletePassThroughCommand"
- "ICReturnFailedToCompleteSendMessageRequest"
- "ICReturnFailedToDisabeTethering"
- "ICReturnFailedToDisableTethering"
- "ICReturnFailedToEnabeTethering"
- "ICReturnFailedToEnableTethering"
- "ICReturnInvalidParam"
- "ICReturnReceivedUnsolicitedScannerStatusInfo"
- "ICReturnScanOperationCanceled"
- "ICReturnScannerFailedToCompleteOverviewScan"
- "ICReturnScannerFailedToCompleteScan"
- "ICReturnScannerFailedToSelectFunctionalUnit"
- "ICReturnScannerInUseByLocalUser"
- "ICReturnScannerInUseByRemoteUser"
- "ICReturnSessionNotOpened"
- "ICReturnUploadFailed"
- "ICXPCAuthManagerProtocol"
- "INSERT INTO external_device_access(bundle_id,date_added,read_access,write_access,control_informed) VALUES ('%@',%lu,%lu,%lu,%lu);"
- "ImageCaptureCore"
- "KERN_NO_ACCESS"
- "No work performed in new TCC path"
- "PrivacySettings"
- "Q32@0:8@16@24"
- "Revoking Application BundleID %@"
- "SELECT bundle_id FROM external_device_access WHERE bundle_id IS '%@';"
- "SELECT bundle_id FROM external_device_access;"
- "SELECT bundle_id, %@ FROM external_device_access;"
- "T@\"NSArray\",R,C,N"
- "T@\"NSObject<OS_dispatch_queue>\",V_deviceAccessQueue"
- "T^{sqlite3=},N,V_externalMediaAccessDB"
- "UPDATE external_device_access SET %@ = %lu WHERE bundle_id = '%@';"
- "[IOReturn.h] _device iokit channel busy."
- "[IOReturn.h] _device iokit timeout."
- "[MacErrors.h] _device call unimplemented."
- "[MacErrors.h] _device parameter invalid."
- "[MacErrors.h] _file not found."
- "[MacErrors.h] _scanner has too many clients."
- "[MacErrors.h] _user operation canceled."
- "[errno.h] _device out of space."
- "[errno.h] _file already exists."
- "[errno.h] _file operation not permitted."
- "[kern_return.h] _kernel reurned no access."
- "^{sqlite3=}"
- "^{sqlite3=}16@0:8"
- "_appledevice is locked or unpaired."
- "_appledevice pairing failed."
- "_appledevice unpairing failed."
- "_camera delete files canceled."
- "_camera delete files failed."
- "_camera disable tethering failed."
- "_camera enable tethering failed."
- "_camera failed to take picture."
- "_camera is enumerating content."
- "_camera passthru command failed."
- "_camera received incorrect data size."
- "_camera send data failed."
- "_device IO Pending."
- "_device already open."
- "_device can't allocate memory."
- "_device close session failed."
- "_device command failed."
- "_device communication error."
- "_device download canceled."
- "_device download failed."
- "_device fw GUID invalid."
- "_device internal error."
- "_device ioservice path invalid."
- "_device module XPC communication failed."
- "_device not found."
- "_device not open."
- "_device open session failed."
- "_device parameter invalid."
- "_device send message failed."
- "_device session invalid."
- "_device session not open."
- "_device unsupported."
- "_device upload failed."
- "_device usb location ID invalid. "
- "_device won't yield."
- "_deviceAccessQueue"
- "_externalMediaAccessDB"
- "_file corrupted."
- "_framework internal error."
- "_module communication timed out."
- "_module parameter invalid"
- "_object data type not found."
- "_object index out of range."
- "_object invalid."
- "_object property invalid."
- "_object property type invalid."
- "_obsolete | _device software install canceled."
- "_obsolete | _device software install failed."
- "_obsolete | _device software installed."
- "_obsolete | _device software installing."
- "_obsolete | _device software not available."
- "_obsolete | _device software not installed."
- "_obsoleted"
- "_operation success."
- "_scaner action canceled."
- "_scanner functional unit selection failed."
- "_scanner in use locally."
- "_scanner in use remotely."
- "_scanner overview scan failed."
- "_scanner reported unsolicited error."
- "_scanner reported unsolicited status."
- "_scanner requested scan failed."
- "_uscandevice needs credentials."
- "addObjectsFromArray:"
- "adding"
- "allBundleIdentifiers"
- "array"
- "bundleIdentifiersAccessingExternalCameras"
- "bundleIdentifiersAccessingExternalCamerasWithStatus"
- "bundleIdentifiersAccessingExternalCamerasWithStatus: %@"
- "bundleIdentifiersWithAccessType:"
- "bundleWithPath:"
- "bundle_id"
- "captureUserIntentForBundleIdentifier:withNotification:"
- "com.apple.imagecapture"
- "connection:stateForAccessType:"
- "containsObject:"
- "control_informed"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "date"
- "defaultManager"
- "deviceAccessQueue"
- "displayAlertForApplication:withNotification:completionBlock:"
- "displayAlertForControlWithNotification:completionBlock:"
- "entity"
- "externalDeviceAccess.db"
- "externalMediaAccessDB"
- "fBsyErr"
- "fileExistsAtPath:"
- "fnfErr"
- "i"
- "i24@0:8@16"
- "icaccess"
- "intValue"
- "integerValue"
- "kICASandboxViolation"
- "kICASecureSessionRequired"
- "kIOReturnBusy"
- "kIOReturnTimeout"
- "legacy"
- "localizedStringForKey:value:table:"
- "modern"
- "numberWithInteger:"
- "objectForKeyedSubscript:"
- "openDB:"
- "paramErr"
- "processInfo"
- "processName"
- "read_access"
- "revokeBundleIdentifier:"
- "setDeviceAccessQueue:"
- "setExternalMediaAccessDB:"
- "stringByAppendingPathComponent:"
- "stringWithUTF8String:"
- "success"
- "tcc_server_message_get_authorization_records_by_service error %@"
- "text"
- "timeIntervalSince1970"
- "unimpErr"
- "updateApplicationWithBundleIdentifier:%@ withStatus:%d"
- "updateApplicationWithBundleIdentifier:withStatus:"
- "userCanceledErr"
- "v16@?0^{__CFError=}8"
- "v20@?0B8Q12"
- "v24@0:8^{sqlite3=}16"
- "v24@?0@\"NSObject<OS_tcc_authorization_record>\"8^{__CFError=}16"
- "v28@0:8@16B24"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24Q32"
- "validateBundleIdentifierInstalled:"
- "value"
- "whitelisted"
- "write_access"

```
