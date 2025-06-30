## AUDeveloperSettings

> `/System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings`

```diff

-916.0.46.0.0
-  __TEXT.__text: 0x849c
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0x560
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x1f7e
-  __TEXT.__gcc_except_tab: 0x26c
+916.40.22.0.2
+  __TEXT.__text: 0xbfa8
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_methlist: 0x7d8
+  __TEXT.__const: 0x74
+  __TEXT.__oslogstring: 0x257
+  __TEXT.__cstring: 0x2256
+  __TEXT.__gcc_except_tab: 0x2e0
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__oslogstring: 0x146
-  __TEXT.__unwind_info: 0x274
-  __TEXT.__objc_classname: 0x1c1
-  __TEXT.__objc_methname: 0x186e
-  __TEXT.__objc_methtype: 0x3a6
-  __TEXT.__objc_stubs: 0x15a0
-  __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0xc30
-  __DATA_CONST.__objc_classlist: 0x58
+  __TEXT.__unwind_info: 0x324
+  __TEXT.__objc_classname: 0x265
+  __TEXT.__objc_methname: 0x2012
+  __TEXT.__objc_methtype: 0x661
+  __TEXT.__objc_stubs: 0x1ee0
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__const: 0xdd0
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf88
-  __DATA_CONST.__objc_selrefs: 0x688
-  __AUTH_CONST.__cfstring: 0x28c0
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__objc_const: 0x430
-  __AUTH_CONST.__auth_got: 0x230
-  __AUTH.__objc_data: 0x320
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x150
-  __DATA.__objc_superrefs: 0x50
-  __DATA.__objc_ivar: 0x90
-  __DATA.__data: 0x120
+  __DATA_CONST.__objc_const: 0x1fc8
+  __DATA_CONST.__objc_selrefs: 0x8f0
+  __AUTH_CONST.__objc_const: 0x550
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__cfstring: 0x2c80
+  __AUTH_CONST.__auth_got: 0x270
+  __AUTH.__objc_data: 0x410
+  __DATA.__objc_protorefs: 0x18
+  __DATA.__objc_classrefs: 0x1a8
+  __DATA.__objc_superrefs: 0x60
+  __DATA.__objc_ivar: 0xe0
+  __DATA.__data: 0x2a0
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
+  - /System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F72ABB00-F346-38DE-9D32-3F113FCDDBB7
-  Functions: 152
-  Symbols:   1086
-  CStrings:  1036
+  UUID: F6A3A94F-728D-330F-BCD4-46D100FFFE92
+  Functions: 224
+  Symbols:   1437
+  CStrings:  1245
 
Symbols:
+ +[AUObserverXPC xpcConnectionToDaemon]
+ +[AUObserverXPC xpcConnectionToDaemon].cold.1
+ +[AUObserverXPC xpcConnectionToDaemon].cold.2
+ -[AUDeveloperSettingsAboutListController .cxx_destruct]
+ -[AUDeveloperSettingsAboutListController addAccessoryID:assetID:]
+ -[AUDeveloperSettingsAboutListController backgroundSetupUI]
+ -[AUDeveloperSettingsAboutListController backgroundUpdateProgress]
+ -[AUDeveloperSettingsAboutListController cleanupProgress]
+ -[AUDeveloperSettingsAboutListController currentSpecifierMatchesAccessoryID:]
+ -[AUDeveloperSettingsAboutListController firmwareUpdateProgressForAccessoryID:assetID:bytesSent:bytesTotal:]
+ -[AUDeveloperSettingsAboutListController firmwareUpdateProgressForAccessoryID:assetID:bytesSent:bytesTotal:].cold.1
+ -[AUDeveloperSettingsAboutListController getAssetLocationForSupplementalAsset:]
+ -[AUDeveloperSettingsAboutListController getFirmwareAssetLocation:]
+ -[AUDeveloperSettingsAboutListController getHWRevision:]
+ -[AUDeveloperSettingsAboutListController getSupplementalAssetLocation:]
+ -[AUDeveloperSettingsAboutListController removeAccessoryID:]
+ -[AUDeveloperSettingsAboutListController stagingCompleteForAccessoryID:assetID:status:]
+ -[AUDeveloperSettingsAboutListController viewWillAppear:]
+ -[AUDeveloperSettingsAboutListController viewWillDisappear:]
+ -[AUInternalSettingsController .cxx_destruct]
+ -[AUInternalSettingsController addAccessoryID:assetID:]
+ -[AUInternalSettingsController firmwareUpdateProgressForAccessoryID:assetID:bytesSent:bytesTotal:]
+ -[AUInternalSettingsController modifySpecifiersForAccessoryID:withStatus:]
+ -[AUInternalSettingsController removeAccessoryID:]
+ -[AUInternalSettingsController stagingCompleteForAccessoryID:assetID:status:]
+ -[AUInternalSettingsController viewDidDisappear:]
+ -[AUInternalSettingsController viewWillAppear:]
+ -[AUInternalSettingsInProgressTableCell refreshCellContentsWithSpecifier:]
+ -[AUObserverXPC .cxx_destruct]
+ -[AUObserverXPC addAccessoryID:assetID:]
+ -[AUObserverXPC dealloc]
+ -[AUObserverXPC firmwareUpdateProgressForAccessoryID:assetID:bytesSent:bytesTotal:]
+ -[AUObserverXPC init]
+ -[AUObserverXPC listener:shouldAcceptNewConnection:]
+ -[AUObserverXPC registerClient:]
+ -[AUObserverXPC remoteObject]
+ -[AUObserverXPC removeAccessoryID:]
+ -[AUObserverXPC removeObserver]
+ -[AUObserverXPC stagingCompleteForAccessoryID:assetID:status:]
+ -[AUObserverXPC stopMonitoring]
+ -[AUObserverXPC unregisterClient]
+ -[UIProgressFooterView .cxx_destruct]
+ -[UIProgressFooterView assetLabel]
+ -[UIProgressFooterView clearProgress]
+ -[UIProgressFooterView detailProgressLabel]
+ -[UIProgressFooterView initWithSpecifier:]
+ -[UIProgressFooterView progressIsComplete]
+ -[UIProgressFooterView progressView]
+ -[UIProgressFooterView refreshContentsWithSpecifier:]
+ -[UIProgressFooterView setAssetLabel:]
+ -[UIProgressFooterView setDetailProgressLabel:]
+ -[UIProgressFooterView setProgressView:]
+ -[UIProgressFooterView setupSubviewsAndConstraints]
+ GCC_except_table3
+ _CGAffineTransformScale
+ _CGRectZero
+ _OBJC_CLASS_$_AUInternalSettingsInProgressTableCell
+ _OBJC_CLASS_$_AUObserverXPC
+ _OBJC_CLASS_$_NSLayoutConstraint
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_NSXPCListener
+ _OBJC_CLASS_$_UARPSupportedAccessory
+ _OBJC_CLASS_$_UIColor
+ _OBJC_CLASS_$_UILabel
+ _OBJC_CLASS_$_UIProgressFooterView
+ _OBJC_CLASS_$_UIProgressView
+ _OBJC_CLASS_$_UITableViewHeaderFooterView
+ _OBJC_IVAR_$_AUDeveloperSettingsAboutListController._accessoryID
+ _OBJC_IVAR_$_AUDeveloperSettingsAboutListController._accessoryInfoGroupSpecifier
+ _OBJC_IVAR_$_AUDeveloperSettingsAboutListController._activePartnerSerialNumber
+ _OBJC_IVAR_$_AUDeveloperSettingsAboutListController._assetID
+ _OBJC_IVAR_$_AUDeveloperSettingsAboutListController._assetVersion
+ _OBJC_IVAR_$_AUDeveloperSettingsAboutListController._observer
+ _OBJC_IVAR_$_AUDeveloperSettingsAboutListController._progressView
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._assetLocationKey
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._basejumperBuildKey
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._basejumperTrainKey
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._serialNumber
+ _OBJC_IVAR_$_AUDeveloperSettingsTextEditingController._assetLocationKey
+ _OBJC_IVAR_$_AUDeveloperSettingsTextEditingController._basejumperBuildKey
+ _OBJC_IVAR_$_AUDeveloperSettingsTextEditingController._basejumperTrainKey
+ _OBJC_IVAR_$_AUInternalSettingsController._accessoryToStatus
+ _OBJC_IVAR_$_AUInternalSettingsController._observer
+ _OBJC_IVAR_$_AUObserverXPC._internalQueue
+ _OBJC_IVAR_$_AUObserverXPC._registeredClient
+ _OBJC_IVAR_$_AUObserverXPC._uuid
+ _OBJC_IVAR_$_AUObserverXPC._xpcConnection
+ _OBJC_IVAR_$_AUObserverXPC._xpcListener
+ _OBJC_IVAR_$_UIProgressFooterView._assetLabel
+ _OBJC_IVAR_$_UIProgressFooterView._detailProgressLabel
+ _OBJC_IVAR_$_UIProgressFooterView._progressView
+ _OBJC_METACLASS_$_AUInternalSettingsInProgressTableCell
+ _OBJC_METACLASS_$_AUObserverXPC
+ _OBJC_METACLASS_$_UIProgressFooterView
+ _OBJC_METACLASS_$_UITableViewHeaderFooterView
+ _PSFooterViewKey
+ _UARPFirmwareStagingCompletionStatusToString
+ __OBJC_$_CLASS_METHODS_AUObserverXPC
+ __OBJC_$_INSTANCE_METHODS_AUInternalSettingsInProgressTableCell
+ __OBJC_$_INSTANCE_METHODS_AUObserverXPC
+ __OBJC_$_INSTANCE_METHODS_UIProgressFooterView
+ __OBJC_$_INSTANCE_VARIABLES_AUDeveloperSettingsAboutListController
+ __OBJC_$_INSTANCE_VARIABLES_AUInternalSettingsController
+ __OBJC_$_INSTANCE_VARIABLES_AUObserverXPC
+ __OBJC_$_INSTANCE_VARIABLES_UIProgressFooterView
+ __OBJC_$_PROP_LIST_AUDeveloperSettingsAboutListController
+ __OBJC_$_PROP_LIST_AUInternalSettingsController
+ __OBJC_$_PROP_LIST_AUObserverXPC
+ __OBJC_$_PROP_LIST_UIProgressFooterView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AUObserverXPCClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AUObserverXPCProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PSHeaderFooterView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PSHeaderFooterView
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AUObserverXPCClient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AUObserverXPCProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PSHeaderFooterView
+ __OBJC_$_PROTOCOL_REFS_AUObserverXPCClient
+ __OBJC_$_PROTOCOL_REFS_AUObserverXPCProvider
+ __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_AUDeveloperSettingsAboutListController
+ __OBJC_CLASS_PROTOCOLS_$_AUInternalSettingsController
+ __OBJC_CLASS_PROTOCOLS_$_AUObserverXPC
+ __OBJC_CLASS_PROTOCOLS_$_UIProgressFooterView
+ __OBJC_CLASS_RO_$_AUInternalSettingsInProgressTableCell
+ __OBJC_CLASS_RO_$_AUObserverXPC
+ __OBJC_CLASS_RO_$_UIProgressFooterView
+ __OBJC_LABEL_PROTOCOL_$_AUObserverXPCClient
+ __OBJC_LABEL_PROTOCOL_$_AUObserverXPCProvider
+ __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_LABEL_PROTOCOL_$_PSHeaderFooterView
+ __OBJC_METACLASS_RO_$_AUInternalSettingsInProgressTableCell
+ __OBJC_METACLASS_RO_$_AUObserverXPC
+ __OBJC_METACLASS_RO_$_UIProgressFooterView
+ __OBJC_PROTOCOL_$_AUObserverXPCClient
+ __OBJC_PROTOCOL_$_AUObserverXPCProvider
+ __OBJC_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_PROTOCOL_$_PSHeaderFooterView
+ __OBJC_PROTOCOL_REFERENCE_$_AUObserverXPCClient
+ __OBJC_PROTOCOL_REFERENCE_$_AUObserverXPCProvider
+ ___29-[AUObserverXPC remoteObject]_block_invoke
+ ___29-[AUObserverXPC remoteObject]_block_invoke.cold.1
+ ___31-[AUObserverXPC stopMonitoring]_block_invoke
+ ___32-[AUObserverXPC registerClient:]_block_invoke
+ ___33-[AUObserverXPC unregisterClient]_block_invoke
+ ___35-[AUObserverXPC removeAccessoryID:]_block_invoke
+ ___40-[AUObserverXPC addAccessoryID:assetID:]_block_invoke
+ ___52-[AUObserverXPC listener:shouldAcceptNewConnection:]_block_invoke
+ ___52-[AUObserverXPC listener:shouldAcceptNewConnection:]_block_invoke.59
+ ___52-[AUObserverXPC listener:shouldAcceptNewConnection:]_block_invoke_2
+ ___52-[AUObserverXPC listener:shouldAcceptNewConnection:]_block_invoke_2.cold.1
+ ___53-[UIProgressFooterView refreshContentsWithSpecifier:]_block_invoke
+ ___57-[AUDeveloperSettingsAboutListController cleanupProgress]_block_invoke
+ ___59-[AUDeveloperSettingsAboutListController backgroundSetupUI]_block_invoke
+ ___60-[AUDeveloperSettingsAboutListController removeAccessoryID:]_block_invoke
+ ___62-[AUObserverXPC stagingCompleteForAccessoryID:assetID:status:]_block_invoke
+ ___66-[AUDeveloperSettingsAboutListController backgroundUpdateProgress]_block_invoke
+ ___74-[AUInternalSettingsController modifySpecifiersForAccessoryID:withStatus:]_block_invoke
+ ___83-[AUObserverXPC firmwareUpdateProgressForAccessoryID:assetID:bytesSent:bytesTotal:]_block_invoke
+ ___block_descriptor_36_e5_v8?0l
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.636
+ ___block_literal_global.638
+ _dispatch_after
+ _dispatch_queue_create
+ _dispatch_sync
+ _dispatch_time
+ _kAUObserverXpcServiceName
+ _kAUSettingsAccessoryHWRevision
+ _kAUSettingsAccessorySupplementalAssetLocation
+ _kAUSettingsAccessorySupplementalBuild
+ _kAUSettingsAccessorySupplementalTrain
+ _kAUSettingsProgressActiveSerialNumber
+ _kAUSettingsProgressActiveUpdate
+ _kAUSettingsProgressComplete
+ _kAUSettingsProgressKeyBuild
+ _kAUSettingsProgressKeyBytesSent
+ _kAUSettingsProgressKeyBytesTotal
+ _kHWRevisionKey
+ _kSupplementalAssetLocationKey
+ _kSupplementalBasejumperBuildKey
+ _kSupplementalBasejumperTrainKey
+ _kUARPSupportedAccessoryCaseModelNameIdentifier
+ _kUARPSupportedAccessoryKeyPersonalities
+ _kUARPSupportedAccessoryKeyUpdateRequiresPowerAssertion
+ _objc_msgSend$UUID
+ _objc_msgSend$_setQueue:
+ _objc_msgSend$activateConstraints:
+ _objc_msgSend$addAccessoryID:assetID:
+ _objc_msgSend$addObserver:withEndpoint:
+ _objc_msgSend$addSubview:
+ _objc_msgSend$allObjects
+ _objc_msgSend$anonymousListener
+ _objc_msgSend$array
+ _objc_msgSend$assetLabel
+ _objc_msgSend$assetVersion
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$cleanupProgress
+ _objc_msgSend$clearColor
+ _objc_msgSend$clearProgress
+ _objc_msgSend$compare:
+ _objc_msgSend$constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:
+ _objc_msgSend$containsString:
+ _objc_msgSend$contentView
+ _objc_msgSend$currentSpecifierMatchesAccessoryID:
+ _objc_msgSend$detailProgressLabel
+ _objc_msgSend$endpoint
+ _objc_msgSend$findByAppleModelNumber:
+ _objc_msgSend$firmwareUpdateProgressForAccessoryID:assetID:bytesSent:bytesTotal:
+ _objc_msgSend$font
+ _objc_msgSend$fontWithSize:
+ _objc_msgSend$getAssetLocationForSupplementalAsset:
+ _objc_msgSend$getHWRevision:
+ _objc_msgSend$getSerialNumber:
+ _objc_msgSend$getSupplementalAssetLocation:
+ _objc_msgSend$grayColor
+ _objc_msgSend$initWithFrame:
+ _objc_msgSend$initWithProgressViewStyle:
+ _objc_msgSend$initWithSpecifier:
+ _objc_msgSend$invalidate
+ _objc_msgSend$lastObject
+ _objc_msgSend$longValue
+ _objc_msgSend$mainBundle
+ _objc_msgSend$modifySpecifiersForAccessoryID:withStatus:
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$path
+ _objc_msgSend$performSelectorInBackground:withObject:
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$progress
+ _objc_msgSend$progressIsComplete
+ _objc_msgSend$progressView
+ _objc_msgSend$refreshContentsWithSpecifier:
+ _objc_msgSend$registerClient:
+ _objc_msgSend$remoteURL
+ _objc_msgSend$removeAccessoryID:
+ _objc_msgSend$removeObserver
+ _objc_msgSend$serialNumber
+ _objc_msgSend$setAssetLabel:
+ _objc_msgSend$setBackgroundColor:
+ _objc_msgSend$setDetailProgressLabel:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setFont:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setProgress:
+ _objc_msgSend$setProgress:animated:
+ _objc_msgSend$setProgressView:
+ _objc_msgSend$setTextColor:
+ _objc_msgSend$setTransform:
+ _objc_msgSend$setTranslatesAutoresizingMaskIntoConstraints:
+ _objc_msgSend$setupSubviewsAndConstraints
+ _objc_msgSend$stagingCompleteForAccessoryID:assetID:status:
+ _objc_msgSend$stopMonitoring
+ _objc_msgSend$supplementalAssets
+ _objc_msgSend$transform
+ _objc_msgSend$unregisterClient
+ _objc_msgSend$xpcConnectionToDaemon
+ _objc_release_x10
+ _objc_retain_x26
- -[AUDeveloperSettingsAboutListController getAssetLocation:]
- _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._basejumperSpecifier
- _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._internalSeedSpecifier
- _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._livabilitySpecifier
- _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._locationRadioGroup
- ___block_literal_global.627
- ___block_literal_global.629
CStrings:
+ "\x01\x13"
+ "\x02"
+ "\x03"
+ "\b\x11\x14"
+ "%@ %@ %@"
+ "%@ %s"
+ "%@: (%@ / %@ bytes)"
+ "%s: Got xpc connection"
+ "%s: remoteObject: %@"
+ "+[AUObserverXPC xpcConnectionToDaemon]"
+ "-"
+ "-[AUObserverXPC remoteObject]"
+ "-[AUObserverXPC remoteObject]_block_invoke"
+ "-[AUObserverXPC removeObserver]"
+ "..."
+ "@\"<AUObserverXPCClient>\""
+ "@\"AUObserverXPC\""
+ "@\"NSMutableDictionary\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSUUID\""
+ "@\"NSXPCListener\""
+ "@\"UARPAccessoryID\""
+ "@\"UARPAssetID\""
+ "@\"UILabel\""
+ "@\"UIProgressView\""
+ "@\"UIView<PSHeaderFooterView>\""
+ "@\"UIView<PSHeaderFooterView>\"24@0:8@\"PSSpecifier\"16"
+ "@20@0:8B16"
+ "AUInternalSettingsInProgressTableCell"
+ "AUObserverXPC"
+ "AUObserverXPCClient"
+ "AUObserverXPCProvider"
+ "AUSettingsProgressActiveUpdate"
+ "AUSettingsProgressComplete"
+ "AUSettingsProgressKeyBuild"
+ "AUSettingsProgressKeyBytesSent"
+ "AUSettingsProgressKeyBytesTotal"
+ "Accessory connected: %@ with asset: %@"
+ "Accessory disconnected: %@"
+ "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
+ "B32@0:8@16@24"
+ "Case"
+ "Completed"
+ "Connection from PID %d invalidated"
+ "Connection to PID %d interrupted"
+ "FW update progress: %@ bytes/total: %lu/%lu"
+ "Hardware Revision"
+ "LOCATION_NOT_ELIGIBLE"
+ "NO"
+ "NSXPCListenerDelegate"
+ "New connection from PID %d"
+ "PSHeaderFooterView"
+ "Personalities"
+ "Staging"
+ "Staging complete: %@"
+ "Supplemental Asset Location"
+ "Supplemental Build"
+ "Supplemental Train"
+ "T@\"UILabel\",&,N,V_assetLabel"
+ "T@\"UILabel\",&,N,V_detailProgressLabel"
+ "T@\"UIProgressView\",&,N,V_progressView"
+ "UIProgressFooterView"
+ "UpdateRequiresPowerAssertion"
+ "YES"
+ "_accessoryID"
+ "_accessoryInfoGroupSpecifier"
+ "_accessoryToStatus"
+ "_activePartnerSerialNumber"
+ "_assetID"
+ "_assetLabel"
+ "_assetLocationKey"
+ "_assetVersion"
+ "_basejumperBuildKey"
+ "_basejumperTrainKey"
+ "_detailProgressLabel"
+ "_internalQueue"
+ "_observer"
+ "_progressView"
+ "_registeredClient"
+ "_serialNumber"
+ "_setQueue:"
+ "_uuid"
+ "_xpcListener"
+ "activateConstraints:"
+ "addAccessoryID:assetID:"
+ "addObserver:withEndpoint:"
+ "addSubview:"
+ "allObjects"
+ "anonymousListener"
+ "array"
+ "arrow.clockwise.circle"
+ "assetLabel"
+ "assetVersion"
+ "backgroundSetupUI"
+ "backgroundUpdateProgress"
+ "bundleIdentifier"
+ "cleanupProgress"
+ "clearColor"
+ "clearProgress"
+ "com.apple.accessoryupdater.observer"
+ "compare:"
+ "constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:"
+ "containsString:"
+ "contentView"
+ "currentSpecifierMatchesAccessoryID:"
+ "d24@0:8d16"
+ "d32@0:8d16@\"UITableView\"24"
+ "d32@0:8d16@24"
+ "detailProgressLabel"
+ "endpoint"
+ "findByAppleModelNumber:"
+ "firmwareUpdateProgressForAccessoryID:assetID:bytesSent:bytesTotal:"
+ "font"
+ "fontWithSize:"
+ "getAssetLocationForSupplementalAsset:"
+ "getFirmwareAssetLocation:"
+ "getHWRevision:"
+ "getSupplementalAssetLocation:"
+ "grayColor"
+ "hwRevision"
+ "initWithFrame:"
+ "initWithProgressViewStyle:"
+ "initWithSpecifier:"
+ "invalidate"
+ "kAUSettingsProgressActiveSerialNumber"
+ "lastObject"
+ "listener:shouldAcceptNewConnection:"
+ "longValue"
+ "mainBundle"
+ "modifySpecifiersForAccessoryID:withStatus:"
+ "numberWithUnsignedLong:"
+ "objectAtIndex:"
+ "path"
+ "performSelectorInBackground:withObject:"
+ "preferredHeightForWidth:"
+ "preferredHeightForWidth:inTableView:"
+ "processIdentifier"
+ "progress"
+ "progressIsComplete"
+ "progressView"
+ "refreshContentsWithSpecifier:"
+ "registerClient:"
+ "remoteURL"
+ "removeAccessoryID:"
+ "removeObserver"
+ "setAssetLabel:"
+ "setBackgroundColor:"
+ "setDetailProgressLabel:"
+ "setExportedInterface:"
+ "setExportedObject:"
+ "setFont:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setProgress:"
+ "setProgress:animated:"
+ "setProgressView:"
+ "setTextColor:"
+ "setTransform:"
+ "setTranslatesAutoresizingMaskIntoConstraints:"
+ "setupSubviewsAndConstraints"
+ "stagingCompleteForAccessoryID:assetID:status:"
+ "stopMonitoring"
+ "stopped due to disconnect"
+ "supplementalAssetLocation"
+ "supplementalAssets"
+ "supplementalBasejumperBuild"
+ "supplementalBasejumperTrain"
+ "transform"
+ "unregisterClient"
+ "v24@0:8@\"NSUUID\"16"
+ "v24@0:8@\"PSSpecifier\"16"
+ "v24@0:8@\"UARPAccessoryID\"16"
+ "v28@0:8@16B24"
+ "v32@0:8@\"NSUUID\"16@\"NSXPCListenerEndpoint\"24"
+ "v32@0:8@\"UARPAccessoryID\"16@\"UARPAssetID\"24"
+ "v40@0:8@\"UARPAccessoryID\"16@\"UARPAssetID\"24Q32"
+ "v40@0:8@16@24Q32"
+ "v48@0:8@\"UARPAccessoryID\"16@\"UARPAssetID\"24Q32Q40"
+ "v48@0:8@16@24Q32Q40"
+ "viewDidDisappear:"
+ "xpcConnectionToDaemon"
- "\f\x11"
- "_basejumperSpecifier"
- "_internalSeedSpecifier"
- "_livabilitySpecifier"
- "getAssetLocation:"

```
