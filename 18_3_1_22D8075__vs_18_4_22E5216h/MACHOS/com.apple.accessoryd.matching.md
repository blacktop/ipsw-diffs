## com.apple.accessoryd.matching

> `/System/Library/UserEventPlugins/com.apple.accessoryd.matching.plugin/com.apple.accessoryd.matching`

```diff

-1025.82.1.0.0
-  __TEXT.__text: 0x35404
-  __TEXT.__auth_stubs: 0xef0
-  __TEXT.__objc_stubs: 0x4540
-  __TEXT.__objc_methlist: 0x1b88
-  __TEXT.__cstring: 0x41c3
-  __TEXT.__objc_methname: 0x5efb
+1043.100.29.0.0
+  __TEXT.__text: 0x36830
+  __TEXT.__auth_stubs: 0xf10
+  __TEXT.__objc_stubs: 0x47c0
+  __TEXT.__objc_methlist: 0x1e84
+  __TEXT.__cstring: 0x4411
+  __TEXT.__objc_methname: 0x61df
   __TEXT.__objc_classname: 0x26c
   __TEXT.__objc_methtype: 0xaaa
   __TEXT.__const: 0x120
-  __TEXT.__oslogstring: 0x3aa1
-  __TEXT.__gcc_except_tab: 0x2d4
-  __TEXT.__unwind_info: 0x878
-  __DATA.__auth_got: 0x788
-  __DATA.__got: 0x2c8
+  __TEXT.__oslogstring: 0x3b60
+  __TEXT.__gcc_except_tab: 0x334
+  __TEXT.__ustring: 0x18
+  __TEXT.__unwind_info: 0x8e8
+  __DATA.__auth_got: 0x798
+  __DATA.__got: 0x2e8
   __DATA.__auth_ptr: 0x10
-  __DATA.__const: 0xed0
-  __DATA.__cfstring: 0x3240
+  __DATA.__const: 0xe70
+  __DATA.__cfstring: 0x3560
   __DATA.__objc_classlist: 0x98
   __DATA.__objc_catlist: 0x10
   __DATA.__objc_protolist: 0x48
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x36a0
-  __DATA.__objc_selrefs: 0x1608
+  __DATA.__objc_const: 0x33c8
+  __DATA.__objc_selrefs: 0x1748
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_superrefs: 0x90
-  __DATA.__objc_ivar: 0x2e4
+  __DATA.__objc_ivar: 0x2fc
   __DATA.__objc_data: 0x5f0
-  __DATA.__data: 0x39e
-  __DATA.__objc_arraydata: 0xe8
+  __DATA.__objc_arraydata: 0x118
   __DATA.__objc_arrayobj: 0x90
-  __DATA.__objc_intobj: 0x48
-  __DATA.__objc_dictobj: 0x28
-  __DATA.__bss: 0x1a5
+  __DATA.__objc_intobj: 0x60
+  __DATA.__data: 0x39e
+  __DATA.__objc_dictobj: 0x50
+  __DATA.__bss: 0x1b0
   __DATA.__common: 0x20
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager
+  - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1096
-  Symbols:   6833
-  CStrings:  2224
+  Functions: 1244
+  Symbols:   7209
+  CStrings:  2286
 
Symbols:
+ +[ACCAnalyticsLogger addBuiltInFieldsToEvent:].cold.1
+ +[ACCAnalyticsLoggerSQLiteStore storeWithPath:schema:].cold.1
+ +[ACCObjCType typeForEncoding:].cold.1
+ +[ACCUserDefaults sharedDefaultsIapd].cold.1
+ +[ACCUserDefaults sharedDefaultsLogging].cold.1
+ +[ACCUserDefaults sharedDefaults].cold.1
+ +[IOUIAngelService interface].cold.1
+ -[ACCAnalyticsLogger logEventNamed:withAttributes:].cold.1
+ -[ACCUserNotification allowLockScreenDismissal]
+ -[ACCUserNotification iconConfiguration]
+ -[ACCUserNotification lockScreenMessage]
+ -[ACCUserNotification lockScreenTitle]
+ -[ACCUserNotification setAllowLockScreenDismissal:]
+ -[ACCUserNotification setIconConfiguration:]
+ -[ACCUserNotification setLockScreenMessage:]
+ -[ACCUserNotification setLockScreenTitle:]
+ -[ACCUserNotification updateBackingUserNotification]
+ -[ACCUserNotificationManager dismissAllNotifications]
+ -[ACCUserNotificationManager updateNotification:]
+ -[TRMPort _startInterestNotifications].cold.1
+ -[TRMPort deviceDescription]
+ -[TRMPort setDeviceDescription:]
+ -[TRMPortManager _startMatchingNotifications].cold.1
+ -[accessorydMatchingPlugin addUserNotificationForPort:]
+ -[accessorydMatchingPlugin addUserNotificationForPort:].cold.1
+ -[accessorydMatchingPlugin isLightning]
+ -[accessorydMatchingPlugin removeUserNotificationForPort:]
+ -[accessorydMatchingPlugin setIsLightning:]
+ -[accessorydMatchingPlugin startListeningForLDCMMitigationStatusChange].cold.5
+ ACMContextGetExternalForm.cold.1
+ GCC_except_table257
+ GCC_except_table67
+ GCC_except_table80
+ OBJC_IVAR_$_ACCUserNotification._allowLockScreenDismissal
+ OBJC_IVAR_$_ACCUserNotification._iconConfiguration
+ OBJC_IVAR_$_ACCUserNotification._lockScreenMessage
+ OBJC_IVAR_$_ACCUserNotification._lockScreenTitle
+ OBJC_IVAR_$_TRMPort._deviceDescription
+ OBJC_IVAR_$_accessorydMatchingPlugin._isLightning
+ _CFUserNotificationUpdate
+ _IORegistryEntryGetChildIterator
+ _OBJC_CLASS_$_NSSet
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _SBUserNotificationAllowLockscreenDismissalKey
+ _SBUserNotificationLockScreenAlertHeaderKey
+ _SBUserNotificationLockScreenAlertMessageKey
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.308
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.309
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.309.cold.1
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.312
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.312.cold.1
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.312.cold.2
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.312.cold.3
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.317
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.320
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.320.cold.1
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.320.cold.2
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.320.cold.3
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.320.cold.4
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.cold.1
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_2.314
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_2.314.cold.1
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_2.314.cold.2
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_2.318
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_2.318.cold.1
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_3.cold.1
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_3.cold.2
+ __58-[accessorydMatchingPlugin removeUserNotificationForPort:]_block_invoke.cold.1
+ __58-[accessorydMatchingPlugin removeUserNotificationForPort:]_block_invoke.cold.2
+ __IOAccessoryManagerEventCallback_block_invoke.886
+ __IOAccessoryManagerEventCallback_block_invoke.886.cold.1
+ __IOAccessoryManagerEventCallback_block_invoke.887
+ __IOAccessoryManagerEventCallback_block_invoke.887.cold.1
+ __IOAccessoryManagerEventCallback_block_invoke.888
+ __IOAccessoryManagerEventCallback_block_invoke.889
+ __IOAccessoryManagerEventCallback_block_invoke.891
+ __MergedGlobals
+ ___55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke
+ ___55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_2
+ ___55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_3
+ ___58-[accessorydMatchingPlugin removeUserNotificationForPort:]_block_invoke
+ ____acc_userNotifications_TRMUserNotification_block_invoke
+ ____isTRMDialogTimerRunning_block_invoke
+ ____shouldPresentTRMDialog_block_invoke
+ ____trmDialogTimer_block_invoke
+ ___block_descriptor_40_e8_32s_e8_v12?0i8ls32l8
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8lw32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_52_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___shouldPresentTRMDialog_block_invoke.cold.1
+ __block_literal_global.241
+ __block_literal_global.316
+ __block_literal_global.898
+ __block_literal_global.923
+ __block_literal_global.928
+ __block_literal_global.931
+ __block_literal_global.943
+ __block_literal_global.945
+ __gTRMNotificationTimer
+ __gTRMNotificationTimerRunning
+ __mainTransportTypeForPort
+ __messageWithMainTransportTypeAndDeviceDescription
+ __serviceLDCMMitigationStatusChanged_block_invoke.924
+ __serviceLDCMMitigationStatusChanged_block_invoke.924.cold.1
+ __serviceLDCMMitigationStatusChanged_block_invoke.924.cold.2
+ __serviceLDCMMitigationStatusChanged_block_invoke.924.cold.3
+ __serviceLDCMMitigationStatusChanged_block_invoke.924.cold.4
+ __shouldPresentTRMDialog
+ __trmDialogTimer
+ __userNotificationsTRM
+ _acc_userNotifications_TRMUserNotification.onceToken
+ _acc_userNotifications_TRMUserNotification.userNotification
+ _hook_usbConnectTypeChanged.cold.5
+ _kTRMDialogExternalPowerDebounceMS
+ _objc_msgSend$addUserNotificationForPort:
+ _objc_msgSend$allowLockScreenDismissal
+ _objc_msgSend$deviceDescription
+ _objc_msgSend$iconConfiguration
+ _objc_msgSend$lockScreenMessage
+ _objc_msgSend$lockScreenTitle
+ _objc_msgSend$minusSet:
+ _objc_msgSend$removeUserNotificationForPort:
+ _objc_msgSend$setAllowLockScreenDismissal:
+ _objc_msgSend$setDeviceDescription:
+ _objc_msgSend$setIconConfiguration:
+ _objc_msgSend$setLockScreenMessage:
+ _objc_msgSend$setLockScreenTitle:
+ _objc_msgSend$setUserAuthorizationStatus:completionHandler:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$string
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$updateBackingUserNotification
+ _objc_msgSend$updateNotification:
+ _objc_msgSend$userAuthorizationStatus
+ _shouldPresentTRMDialog.cold.1
+ _shouldPresentTRMDialog.cold.2
+ _shouldPresentTRMDialog.cold.3
+ _trmDialogTimer.cold.1
+ _trmDialogTimer.onceToken
+ _uiQueue.cold.1
+ addUserNotificationForPort:.onceToken
+ systemInfo_copyRegionCode.cold.1
+ systemInfo_isDeveloperBuild.cold.1
+ systemInfo_isInternalBuild.cold.1
+ systemInfo_systemSupportsPearl.cold.1
+ systemInfo_systemSupportsWAPI.cold.1
+ updateLogLevelFromKext.cold.1
- -[ACCUserNotificationManager dismisssAllNotifications]
- -[accessorydMatchingPlugin addDigitalIDClient:].cold.1
- -[accessorydMatchingPlugin initWithModule:].cold.1
- -[accessorydMatchingPlugin initWithModule:].cold.10
- -[accessorydMatchingPlugin initWithModule:].cold.11
- -[accessorydMatchingPlugin initWithModule:].cold.12
- -[accessorydMatchingPlugin initWithModule:].cold.13
- -[accessorydMatchingPlugin initWithModule:].cold.2
- -[accessorydMatchingPlugin initWithModule:].cold.3
- -[accessorydMatchingPlugin initWithModule:].cold.4
- -[accessorydMatchingPlugin initWithModule:].cold.5
- -[accessorydMatchingPlugin initWithModule:].cold.6
- -[accessorydMatchingPlugin initWithModule:].cold.7
- -[accessorydMatchingPlugin initWithModule:].cold.8
- -[accessorydMatchingPlugin initWithModule:].cold.9
- -[accessorydMatchingPlugin removeDigitalIDClient:].cold.1
- GCC_except_table237
- __43-[accessorydMatchingPlugin initWithModule:]_block_invoke.cold.2
- __IOAccessoryManagerEventCallback_block_invoke.862
- __IOAccessoryManagerEventCallback_block_invoke.862.cold.1
- __IOAccessoryManagerEventCallback_block_invoke.863
- __IOAccessoryManagerEventCallback_block_invoke.863.cold.1
- __IOAccessoryManagerEventCallback_block_invoke.864
- __IOAccessoryManagerEventCallback_block_invoke.865
- __IOAccessoryManagerEventCallback_block_invoke.867
- ____acc_userNotifications_restrictedModeUnlock_block_invoke
- ____isUnlockDialogTimerRunning_block_invoke
- ____presentUnlockDialog_block_invoke
- ____presentUnlockDialog_block_invoke_2
- ____presentUnlockDialog_block_invoke_3
- ____shouldPresentUnlockDialog_block_invoke
- ____unlockDialogTimer_block_invoke
- ___presentUnlockDialog_block_invoke.927
- ___presentUnlockDialog_block_invoke.927.cold.1
- ___presentUnlockDialog_block_invoke.930
- ___presentUnlockDialog_block_invoke.930.cold.1
- ___presentUnlockDialog_block_invoke.930.cold.2
- ___presentUnlockDialog_block_invoke.934
- ___presentUnlockDialog_block_invoke.934.cold.1
- ___presentUnlockDialog_block_invoke.934.cold.2
- ___presentUnlockDialog_block_invoke.937
- ___presentUnlockDialog_block_invoke.937.cold.1
- ___presentUnlockDialog_block_invoke.937.cold.2
- ___presentUnlockDialog_block_invoke.937.cold.3
- ___presentUnlockDialog_block_invoke.937.cold.4
- ___presentUnlockDialog_block_invoke_3.cold.1
- ___presentUnlockDialog_block_invoke_3.cold.2
- ___shouldPresentUnlockDialog_block_invoke.cold.1
- __block_literal_global.238
- __block_literal_global.874
- __block_literal_global.876
- __block_literal_global.885
- __block_literal_global.902
- __block_literal_global.905
- __block_literal_global.922
- __block_literal_global.924
- __block_literal_global.929
- __block_literal_global.932
- __block_literal_global.936
- __block_literal_global.939
- __block_literal_global.941
- __block_literal_global.963
- __connect
- __gUnlockNotificationTimer
- __gUnlockNotificationTimerRunning
- __initialized
- __isNullOrEqualMem2
- __serviceLDCMMitigationStatusChanged_block_invoke.903
- __serviceLDCMMitigationStatusChanged_block_invoke.903.cold.1
- __serviceLDCMMitigationStatusChanged_block_invoke.903.cold.2
- __serviceLDCMMitigationStatusChanged_block_invoke.903.cold.3
- __serviceLDCMMitigationStatusChanged_block_invoke.903.cold.4
- __shouldPresentUnlockDialog
- __unlockDialogTimer
- _acc_userNotifications_restrictedModeUnlock.onceToken
- _acc_userNotifications_restrictedModeUnlock.userNotification
- _kUnlockDialogExternalPowerDebounceMS
- _presentUnlockDialog.onceToken
- _shouldPresentUnlockDialog.cold.1
- _shouldPresentUnlockDialog.cold.2
- _shouldPresentUnlockDialog.cold.3
- _unlockDialogTimer.onceToken
- _updatePropertiesFromService.onceToken
- _updatePropertiesFromService.propertyFilter
CStrings:
+ "%s: (_gTRMNotificationTimerRunning: %s, userNotification: %s)"
+ "*\x13"
+ "-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke"
+ "Active"
+ "Adding user notification... (port: %@)"
+ "Allow"
+ "Allow accessory to connect?"
+ "Apple Inc. "
+ "Apple, Inc. "
+ "CIO"
+ "Could not find user notification! (portRegistryID: %@)"
+ "Device Model Name"
+ "Device Vendor Name"
+ "Device description changed!"
+ "DeviceSupports9Pin"
+ "Do you want to connect %@ to this Device?"
+ "Do you want to connect the Thunderbolt accessory to this Device?"
+ "Do you want to connect the USB accessory to this Device?"
+ "Do you want to connect the accessory to this Device?"
+ "Error setting user authorization status for port %@! (error: %@)"
+ "ISIconDecorationPosition"
+ "ISIconDecorationType"
+ "ISIconType"
+ "IconConfiguration"
+ "Manufacturer"
+ "Presenting TRM notification..."
+ "Product"
+ "Resetting TRM dialog timer to %ums..."
+ "Setting user authorization status... (userAuthorizationStatus: %d, self: %@)"
+ "Starting TRM dialog timer for %dms..."
+ "T@\"NSDictionary\",C,N,V_iconConfiguration"
+ "T@\"NSString\",&,N,V_deviceDescription"
+ "T@\"NSString\",C,N,V_lockScreenMessage"
+ "T@\"NSString\",C,N,V_lockScreenTitle"
+ "TB,N,V_allowLockScreenDismissal"
+ "TB,N,V_isLightning"
+ "TRM dialog should no longer be presented, not presenting dialog!"
+ "TRM dialog timer already running or dialog already up - not starting timer again."
+ "TRM dialog timer fired!"
+ "TransportType"
+ "USB2"
+ "USB3"
+ "User notification already exists for port! (port: %@, userNotification: %@)"
+ "_allowLockScreenDismissal"
+ "_deviceDescription"
+ "_gTRMNotificationTimerRunning: %s, userNotification: %s"
+ "_iconConfiguration"
+ "_isLightning"
+ "_lockScreenMessage"
+ "_lockScreenTitle"
+ "addUserNotificationForPort:"
+ "allowLockScreenDismissal"
+ "com.apple.graphic-icon.privacy"
+ "com.apple.graphic-icon.usb"
+ "deviceDescription"
+ "dismissAllNotifications"
+ "g\x11"
+ "iconConfiguration"
+ "isLightning"
+ "lockScreenMessage"
+ "lockScreenTitle"
+ "minusSet:"
+ "removeUserNotificationForPort:"
+ "setAllowLockScreenDismissal:"
+ "setDeviceDescription:"
+ "setIconConfiguration:"
+ "setIsLightning:"
+ "setLockScreenMessage:"
+ "setLockScreenTitle:"
+ "setWithArray:"
+ "shouldPresentTRMDialog: %s"
+ "string"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "updateBackingUserNotification"
+ "updateNotification:"
- "\x17\x13"
- "Presenting unlock notification..."
- "Resetting unlock dialog timer to %ums..."
- "Starting unlock dialog timer for %dms..."
- "Unlock dialog should no longer be presented, not presenting unlock dialog!"
- "Unlock dialog timer already running or dialog already up - not starting timer again."
- "Unlock dialog timer fired!"
- "Unlock notification presented when SpringBoard unlocked, dismissing user notification..."
- "_gUnlockNotificationTimerRunning: %s, _gUnlockNotification: %s"
- "_presentUnlockDialog: (_gUnlockNotificationTimerRunning: %s, _gUnlockNotification: %s)"
- "dismisssAllNotifications"
- "f\x11"
- "shouldPresentUnlockDialog: %s"

```
