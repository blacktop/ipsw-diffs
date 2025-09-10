## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-746.80.1.0.0
-  __TEXT.__text: 0x40640
-  __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_methlist: 0x4d44
-  __TEXT.__cstring: 0xed32
-  __TEXT.__const: 0x190
-  __TEXT.__gcc_except_tab: 0x740
+781.100.15.0.0
+  __TEXT.__text: 0x4b428
+  __TEXT.__auth_stubs: 0xc20
+  __TEXT.__objc_methlist: 0x52b4
+  __TEXT.__cstring: 0xf980
+  __TEXT.__const: 0x188
+  __TEXT.__gcc_except_tab: 0x86c
   __TEXT.__oslogstring: 0x52f
-  __TEXT.__unwind_info: 0x1640
-  __TEXT.__objc_classname: 0xa02
-  __TEXT.__objc_methname: 0xdb13
-  __TEXT.__objc_methtype: 0x21df
-  __TEXT.__objc_stubs: 0x9ea0
-  __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0x14b8
-  __DATA_CONST.__objc_classlist: 0x278
+  __TEXT.__unwind_info: 0x170c
+  __TEXT.__objc_classname: 0xa7c
+  __TEXT.__objc_methname: 0xe46d
+  __TEXT.__objc_methtype: 0x221b
+  __TEXT.__objc_stubs: 0xa880
+  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__const: 0x14f0
+  __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xd8
+  __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc040
-  __DATA_CONST.__objc_selrefs: 0x3118
+  __DATA_CONST.__objc_const: 0xbdc8
+  __DATA_CONST.__objc_selrefs: 0x33f8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x478
+  __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__cfstring: 0x9b20
-  __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__objc_const: 0x21e8
+  __AUTH_CONST.__cfstring: 0xa2a0
+  __AUTH_CONST.__const: 0x4c0
+  __AUTH_CONST.__objc_const: 0x2350
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x5e8
-  __AUTH.__objc_data: 0xd48
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x450
-  __DATA.__objc_superrefs: 0x200
-  __DATA.__objc_ivar: 0x554
-  __DATA.__data: 0xb30
-  __DATA.__bss: 0xb0
+  __AUTH_CONST.__auth_got: 0x620
+  __AUTH.__objc_data: 0xe88
+  __DATA.__objc_ivar: 0x5a0
+  __DATA.__data: 0x9b8
+  __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0xb68
-  __DATA_DIRTY.__bss: 0x130
+  __DATA_DIRTY.__bss: 0x140
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
+  - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F42BF39E-EBB2-333B-A652-4941332EF67B
-  Functions: 2066
-  Symbols:   7471
-  CStrings:  5435
+  UUID: 8684138D-A720-33C7-9E0A-5FDBB61FA3EF
+  Functions: 2188
+  Symbols:   7846
+  CStrings:  5702
 
Symbols:
+ +[SUAlertPresentationManager sharedInstance]
+ +[SUUtility deleteAUKeepAliveFile]
+ +[SUUtility deleteKeepAliveFilePath:]
+ +[SUUtility updateError:withAdditionalUserInfo:]
+ +[SUUtility writeAUKeepAliveFile]
+ +[SUUtility writeKeepAliveFilePath:]
+ -[CTDataDelegate .cxx_destruct]
+ -[SUAlertButtonDefinition .cxx_destruct]
+ -[SUAlertButtonDefinition handler]
+ -[SUAlertButtonDefinition initWithLabel:presentationStyle:isPreferredButton:handler:]
+ -[SUAlertButtonDefinition isPreferredButton]
+ -[SUAlertButtonDefinition label]
+ -[SUAlertButtonDefinition presentationStyle]
+ -[SUAlertItemDefinition .cxx_destruct]
+ -[SUAlertItemDefinition buttons]
+ -[SUAlertItemDefinition initWithTitle:message:buttons:]
+ -[SUAlertItemDefinition message]
+ -[SUAlertItemDefinition setButtons:]
+ -[SUAlertItemDefinition setMessage:]
+ -[SUAlertItemDefinition setTitle:]
+ -[SUAlertItemDefinition title]
+ -[SUAlertPresentationManager .cxx_destruct]
+ -[SUAlertPresentationManager _dismissAlert:animated:]
+ -[SUAlertPresentationManager _dismissAlertsOfClass:animated:]
+ -[SUAlertPresentationManager _dismissAllAlertsExcludingClasses:animated:]
+ -[SUAlertPresentationManager _noteAlertDeactivated:]
+ -[SUAlertPresentationManager _presentAlert:animated:]
+ -[SUAlertPresentationManager _presentedAlertsOfClass:]
+ -[SUAlertPresentationManager _presentedAlerts]
+ -[SUAlertPresentationManager _updateAlert:animated:]
+ -[SUAlertPresentationManager _updateAllAlertLockState:]
+ -[SUAlertPresentationManager dismissAlert:animated:]
+ -[SUAlertPresentationManager dismissAlertsOfClass:animated:]
+ -[SUAlertPresentationManager dismissAllAlertsAnimated:]
+ -[SUAlertPresentationManager dismissAllAlertsExcludingClasses:animated:]
+ -[SUAlertPresentationManager init]
+ -[SUAlertPresentationManager isPresentingAlertsOfClass:]
+ -[SUAlertPresentationManager presentAlert:animated:]
+ -[SUAlertPresentationManager presentedAlertsOfClass:]
+ -[SUAlertPresentationManager presentedAlerts]
+ -[SUAlertPresentationManager updateAlert:animated:]
+ -[SUAlertPresentationManager updateAllAlertLockState:]
+ -[SUAppPurgingAlertItem .cxx_destruct]
+ -[SUAppPurgingAlertItem _noButton]
+ -[SUAppPurgingAlertItem _yesButton]
+ -[SUAppPurgingAlertItem alertWasDismissed:]
+ -[SUAppPurgingAlertItem buttons]
+ -[SUAppPurgingAlertItem initWithHandler:]
+ -[SUAppPurgingAlertItem message]
+ -[SUAppPurgingAlertItem title]
+ -[SUAssetStateMatcher .cxx_destruct]
+ -[SUAutoInstallFailureAlertItem .cxx_destruct]
+ -[SUAutoInstallFailureAlertItem _okButton]
+ -[SUAutoInstallFailureAlertItem _radarButton]
+ -[SUAutoInstallFailureAlertItem buttons]
+ -[SUAutoInstallFailureAlertItem initWithError:buildNumber:]
+ -[SUAutoInstallFailureAlertItem message]
+ -[SUAutoInstallFailureAlertItem title]
+ -[SUAutoInstallForecast .cxx_destruct]
+ -[SUAutoInstallOperation .cxx_destruct]
+ -[SUAutoUpdatePasscodePolicy .cxx_destruct]
+ -[SUBaseAlertItem .cxx_destruct]
+ -[SUBaseAlertItem _SBPresentationStyleForSUSPresentationStyle:]
+ -[SUBaseAlertItem _cancelNotification]
+ -[SUBaseAlertItem _createNotification]
+ -[SUBaseAlertItem _notificationButtonActions]
+ -[SUBaseAlertItem _notificationButtons]
+ -[SUBaseAlertItem _notificationFlags]
+ -[SUBaseAlertItem _notificationOptions]
+ -[SUBaseAlertItem _notificationWasDismissed:]
+ -[SUBaseAlertItem _setPresentationManager:]
+ -[SUBaseAlertItem _updateNotification]
+ -[SUBaseAlertItem alertWasDismissed:]
+ -[SUBaseAlertItem allowInSetup]
+ -[SUBaseAlertItem allowLockScreenDismissal]
+ -[SUBaseAlertItem allowMenuButtonDismissal]
+ -[SUBaseAlertItem allowNoButton]
+ -[SUBaseAlertItem allowedApps]
+ -[SUBaseAlertItem buildAlertItemDefinition]
+ -[SUBaseAlertItem buttons]
+ -[SUBaseAlertItem contentExtensionID]
+ -[SUBaseAlertItem dealloc]
+ -[SUBaseAlertItem dismiss]
+ -[SUBaseAlertItem extensionDictionary]
+ -[SUBaseAlertItem forcesModalAlertAppearance]
+ -[SUBaseAlertItem init]
+ -[SUBaseAlertItem isUILocked]
+ -[SUBaseAlertItem message]
+ -[SUBaseAlertItem present]
+ -[SUBaseAlertItem reappearsAfterLock]
+ -[SUBaseAlertItem reappearsAfterUnlock]
+ -[SUBaseAlertItem setIsUILocked:]
+ -[SUBaseAlertItem shouldShowCountdown]
+ -[SUBaseAlertItem shouldShowInLockScreen]
+ -[SUBaseAlertItem showButtonsOnLockScreen]
+ -[SUBaseAlertItem title]
+ -[SUBaseAlertItem undimsScreen]
+ -[SUBaseAlertItem update]
+ -[SUBaseAlertItem willPresentAlert]
+ -[SUCSScheduler .cxx_destruct]
+ -[SUCarrierDownloadPolicyProperties .cxx_destruct]
+ -[SUDefaultDownloadPolicy .cxx_destruct]
+ -[SUDescriptor allowAutoDownloadOnBattery]
+ -[SUDescriptor autoDownloadOnBatteryDelay]
+ -[SUDescriptor autoDownloadOnBatteryMinBattery]
+ -[SUDescriptor granularlyRamped]
+ -[SUDescriptor setAllowAutoDownloadOnBattery:]
+ -[SUDescriptor setAutoDownloadOnBatteryDelay:]
+ -[SUDescriptor setAutoDownloadOnBatteryMinBattery:]
+ -[SUDescriptor setGranularlyRamped:]
+ -[SUDescriptor(SUBattery) releasedBefore:]
+ -[SUDocumentationData .cxx_destruct]
+ -[SUDownload .cxx_destruct]
+ -[SUInstallationConstraintMonitorCarplay .cxx_destruct]
+ -[SUInstallationConstraintMonitorForBatteryDiskAndKeybag .cxx_destruct]
+ -[SUInstallationConstraintMonitorForBatteryDiskAndKeybag keybagInterfacePasscodeDidChange:]
+ -[SUInstallationConstraintMonitorMediaPlaying .cxx_destruct]
+ -[SUInstallationConstraintMonitorNetwork .cxx_destruct]
+ -[SUInstallationConstraintMonitorPhoneCalls .cxx_destruct]
+ -[SUInstallationConstraintMonitorSync .cxx_destruct]
+ -[SUInstallationConstraintMonitorWombat .cxx_destruct]
+ -[SUKeybagInterface .cxx_destruct]
+ -[SUKeybagInterface _queue_passcodeChanged]
+ -[SUKeybagOptions .cxx_destruct]
+ -[SUManagedDeviceUpdateDelay .cxx_destruct]
+ -[SUManagerClient autoScanAndDownloadNow:IfAvailable:]
+ -[SUNetworkMonitor .cxx_destruct]
+ -[SUOperationProgress .cxx_destruct]
+ -[SUPreferenceEntry .cxx_destruct]
+ -[SUPreferences fakeAppOffload]
+ -[SUPreferences fakeInstallFailure]
+ -[SUPreferences overrideAllowAutoDownloadOnBattery]
+ -[SUPreferences overrideAutoDownloadOnBatteryDelay]
+ -[SUPreferences overrideGranularRamping]
+ -[SUPreferences overrideRamping]
+ -[SUPreferences overrideScanSessionIDRampingPortion]
+ -[SURollbackDescriptor .cxx_destruct]
+ -[SURollbackSuggestionInfo .cxx_destruct]
+ -[SURollbackSuggestionProcessInfo .cxx_destruct]
+ -[SUSFollowUpController .cxx_destruct]
+ -[SUScanResults .cxx_destruct]
+ -[SUState setUpdateFullyUnrampedDates:]
+ -[SUState updateFullyUnrampedDates]
+ -[SUUpdateDiscoveryDateManager .cxx_destruct]
+ -[SUUpdateDiscoveryDateManager removeDiscoveryDateForBuildVersion:]
+ -[_SUAutoInstallOperationModel .cxx_destruct]
+ GCC_except_table101
+ GCC_except_table110
+ GCC_except_table122
+ GCC_except_table140
+ GCC_except_table165
+ GCC_except_table192
+ GCC_except_table200
+ GCC_except_table222
+ GCC_except_table227
+ GCC_except_table235
+ GCC_except_table271
+ GCC_except_table52
+ GCC_except_table60
+ GCC_except_table83
+ GCC_except_table88
+ OBJC_IVAR_$_SUDescriptor._granularlyRamped
+ OBJC_IVAR_$_SUState._updateFullyUnrampedDates
+ _CFUserNotificationGetResponseDictionary
+ _CFUserNotificationUpdate
+ _MCPasscodeChangedNotification
+ _NSStringFromClass
+ _OBJC_CLASS_$_NSExtensionItem
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_SBSMutableUserNotificationButtonDefinition
+ _OBJC_CLASS_$_SUAlertButtonDefinition
+ _OBJC_CLASS_$_SUAlertItemDefinition
+ _OBJC_CLASS_$_SUAlertPresentationManager
+ _OBJC_CLASS_$_SUAppPurgingAlertItem
+ _OBJC_CLASS_$_SUAutoInstallFailureAlertItem
+ _OBJC_CLASS_$_SUBaseAlertItem
+ _OBJC_IVAR_$_SUAlertButtonDefinition._handler
+ _OBJC_IVAR_$_SUAlertButtonDefinition._isPreferredButton
+ _OBJC_IVAR_$_SUAlertButtonDefinition._label
+ _OBJC_IVAR_$_SUAlertButtonDefinition._presentationStyle
+ _OBJC_IVAR_$_SUAlertItemDefinition._buttons
+ _OBJC_IVAR_$_SUAlertItemDefinition._message
+ _OBJC_IVAR_$_SUAlertItemDefinition._title
+ _OBJC_IVAR_$_SUAlertPresentationManager._alerts
+ _OBJC_IVAR_$_SUAppPurgingAlertItem._handler
+ _OBJC_IVAR_$_SUAutoInstallFailureAlertItem._buildNumber
+ _OBJC_IVAR_$_SUAutoInstallFailureAlertItem._error
+ _OBJC_IVAR_$_SUAutoInstallFailureAlertItem._message
+ _OBJC_IVAR_$_SUAutoInstallFailureAlertItem._title
+ _OBJC_IVAR_$_SUBaseAlertItem._isUILocked
+ _OBJC_IVAR_$_SUBaseAlertItem._manager
+ _OBJC_IVAR_$_SUBaseAlertItem._notification
+ _OBJC_IVAR_$_SUBaseAlertItem._stateQ
+ _OBJC_IVAR_$_SUDescriptor._allowAutoDownloadOnBattery
+ _OBJC_IVAR_$_SUDescriptor._autoDownloadOnBatteryDelay
+ _OBJC_IVAR_$_SUDescriptor._autoDownloadOnBatteryMinBattery
+ _OBJC_IVAR_$_SUKeybagInterface._passcodeChangedNotifyToken
+ _OBJC_METACLASS_$_SUAlertButtonDefinition
+ _OBJC_METACLASS_$_SUAlertItemDefinition
+ _OBJC_METACLASS_$_SUAlertPresentationManager
+ _OBJC_METACLASS_$_SUAppPurgingAlertItem
+ _OBJC_METACLASS_$_SUAutoInstallFailureAlertItem
+ _OBJC_METACLASS_$_SUBaseAlertItem
+ _SBSUserNotificationButtonDefinitionResponseIndexKey
+ _SBSUserNotificationButtonDefinitionsKey
+ _SBUserNotificationAllowInSetupKey
+ _SBUserNotificationAllowLockscreenDismissalKey
+ _SBUserNotificationAllowMenuButtonDismissal
+ _SBUserNotificationAllowedApplicationsKey
+ _SBUserNotificationDismissOnLock
+ _SBUserNotificationDisplayActionButtonOnLockScreen
+ _SBUserNotificationDontDismissOnUnlock
+ _SBUserNotificationExtensionIdentifierKey
+ _SBUserNotificationExtensionItemsKey
+ _SBUserNotificationForcesModalAlertAppearance
+ _SBUserNotificationWakeDisplay
+ _SUHasEnoughBatteryForAutoDownloadForDescriptor
+ _SULogAlerts
+ _SULogAlerts.__instance
+ _SULogAlerts.__once
+ _SURequiredBatteryLevelForAutoDownloadForDescriptor
+ _SUSoftwareUpdateAssetKeyGranularlyRamped
+ __OBJC_$_CLASS_METHODS_SUAlertPresentationManager
+ __OBJC_$_CLASS_METHODS_SUDescriptor(SUBattery)
+ __OBJC_$_INSTANCE_METHODS_SUAlertButtonDefinition
+ __OBJC_$_INSTANCE_METHODS_SUAlertItemDefinition
+ __OBJC_$_INSTANCE_METHODS_SUAlertPresentationManager
+ __OBJC_$_INSTANCE_METHODS_SUAppPurgingAlertItem
+ __OBJC_$_INSTANCE_METHODS_SUAutoInstallFailureAlertItem
+ __OBJC_$_INSTANCE_METHODS_SUBaseAlertItem
+ __OBJC_$_INSTANCE_METHODS_SUDescriptor(SUBattery)
+ __OBJC_$_INSTANCE_VARIABLES_SUAlertButtonDefinition
+ __OBJC_$_INSTANCE_VARIABLES_SUAlertItemDefinition
+ __OBJC_$_INSTANCE_VARIABLES_SUAlertPresentationManager
+ __OBJC_$_INSTANCE_VARIABLES_SUAppPurgingAlertItem
+ __OBJC_$_INSTANCE_VARIABLES_SUAutoInstallFailureAlertItem
+ __OBJC_$_INSTANCE_VARIABLES_SUBaseAlertItem
+ __OBJC_$_PROP_LIST_SUAlertButtonDefinition
+ __OBJC_$_PROP_LIST_SUAlertItemDefinition
+ __OBJC_$_PROP_LIST_SUBaseAlertItem
+ __OBJC_CLASS_RO_$_SUAlertButtonDefinition
+ __OBJC_CLASS_RO_$_SUAlertItemDefinition
+ __OBJC_CLASS_RO_$_SUAlertPresentationManager
+ __OBJC_CLASS_RO_$_SUAppPurgingAlertItem
+ __OBJC_CLASS_RO_$_SUAutoInstallFailureAlertItem
+ __OBJC_CLASS_RO_$_SUBaseAlertItem
+ __OBJC_METACLASS_RO_$_SUAlertButtonDefinition
+ __OBJC_METACLASS_RO_$_SUAlertItemDefinition
+ __OBJC_METACLASS_RO_$_SUAlertPresentationManager
+ __OBJC_METACLASS_RO_$_SUAppPurgingAlertItem
+ __OBJC_METACLASS_RO_$_SUAutoInstallFailureAlertItem
+ __OBJC_METACLASS_RO_$_SUBaseAlertItem
+ ___25-[SUBaseAlertItem update]_block_invoke
+ ___26-[SUBaseAlertItem dismiss]_block_invoke
+ ___26-[SUBaseAlertItem present]_block_invoke
+ ___26-[SUKeybagInterface _init]_block_invoke_3
+ ___34-[SUAppPurgingAlertItem _noButton]_block_invoke
+ ___35-[SUAppPurgingAlertItem _yesButton]_block_invoke
+ ___35-[SUState updateFullyUnrampedDates]_block_invoke
+ ___38-[SUBaseAlertItem _createNotification]_block_invoke
+ ___38-[SUBaseAlertItem _createNotification]_block_invoke_2
+ ___38-[SUBaseAlertItem _createNotification]_block_invoke_3
+ ___38-[SUBaseAlertItem _createNotification]_block_invoke_4
+ ___38-[SUBaseAlertItem _createNotification]_block_invoke_5
+ ___38-[SUBaseAlertItem _createNotification]_block_invoke_6
+ ___38-[SUBaseAlertItem _createNotification]_block_invoke_7
+ ___39-[SUState setUpdateFullyUnrampedDates:]_block_invoke
+ ___42-[SUAutoInstallFailureAlertItem _okButton]_block_invoke
+ ___43-[SUKeybagInterface _queue_passcodeChanged]_block_invoke
+ ___44+[SUAlertPresentationManager sharedInstance]_block_invoke
+ ___45-[SUAutoInstallFailureAlertItem _radarButton]_block_invoke
+ ___54-[SUManagerClient autoScanAndDownloadNow:IfAvailable:]_block_invoke
+ ___54-[SUManagerClient autoScanAndDownloadNow:IfAvailable:]_block_invoke_2
+ ___67-[SUUpdateDiscoveryDateManager removeDiscoveryDateForBuildVersion:]_block_invoke
+ ___91-[SUInstallationConstraintMonitorForBatteryDiskAndKeybag keybagInterfacePasscodeDidChange:]_block_invoke
+ ___SULogAlerts_block_invoke
+ ___block_descriptor_40_e8_32bs_e15_v28?0Q8i16^B20ls32l8
+ ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e79_v40?0"SUDownload"8"SUInstallPolicy"16"SUAutoInstallOperation"24"NSError"32ls32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32r40r_e20_v20?0B8"NSError"12lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e20_v24?0Q8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e23_v32?0Q8Q16"NSError"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSDate"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSNumber"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"SUDescriptor"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e35_v24?0"SUScanResults"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e35_v32?0B8B12"NSError"16"NSError"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e42_v24?0"SUCoreDDMDeclaration"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e42_v24?0"SURollbackDescriptor"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e43_v24?0"SUAutoInstallForecast"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e45_v28?0B8"SURollbackDescriptor"12"NSError"20ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e50_v24?0"_SUAutoInstallOperationModel"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e85_v40?0"SUDownload"8"SUInstallPolicy"16"_SUAutoInstallOperationModel"24"NSError"32ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e34_v24?0"SUDescriptor"8"NSError"16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e48_v28?0B8"ASDPurgeableAppResponse"12"NSError"20lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e8_v12?0I8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e15_v32?08Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_51_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e20_v20?0B8"NSError"12ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8u48l8r40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_74_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48bs56bs64bs72bs80r_e8_v12?0i8ls32l8s48l8r80l8s40l8s56l8s64l8s72l8
+ ___block_literal_global.16
+ ___block_literal_global.239
+ ___block_literal_global.242
+ ___block_literal_global.245
+ ___block_literal_global.256
+ ___block_literal_global.261
+ ___block_literal_global.266
+ ___block_literal_global.271
+ ___block_literal_global.276
+ ___block_literal_global.281
+ ___block_literal_global.286
+ ___block_literal_global.291
+ ___block_literal_global.299
+ ___block_literal_global.304
+ ___block_literal_global.334
+ ___block_literal_global.394
+ ___block_literal_global.399
+ ___block_literal_global.592
+ ___block_literal_global.600
+ ___block_literal_global.720
+ __requiredBatteryLevelToAutoDownload
+ __unnamed_array_storage.631
+ __unnamed_array_storage.634
+ _getCurrentBatteryLevel
+ _kSUAutomaticInstallationKey
+ _objc_msgSend$_SBPresentationStyleForSUSPresentationStyle:
+ _objc_msgSend$_cancelNotification
+ _objc_msgSend$_createNotification
+ _objc_msgSend$_dismissAlert:animated:
+ _objc_msgSend$_dismissAlertsOfClass:animated:
+ _objc_msgSend$_dismissAllAlertsExcludingClasses:animated:
+ _objc_msgSend$_noButton
+ _objc_msgSend$_noteAlertDeactivated:
+ _objc_msgSend$_notificationButtonActions
+ _objc_msgSend$_notificationButtons
+ _objc_msgSend$_notificationFlags
+ _objc_msgSend$_notificationOptions
+ _objc_msgSend$_notificationWasDismissed:
+ _objc_msgSend$_okButton
+ _objc_msgSend$_presentAlert:animated:
+ _objc_msgSend$_presentedAlerts
+ _objc_msgSend$_presentedAlertsOfClass:
+ _objc_msgSend$_queue_passcodeChanged
+ _objc_msgSend$_updateAlert:animated:
+ _objc_msgSend$_updateAllAlertLockState:
+ _objc_msgSend$_updateNotification
+ _objc_msgSend$_yesButton
+ _objc_msgSend$alertWasDismissed:
+ _objc_msgSend$allowAutoDownloadOnBattery
+ _objc_msgSend$allowInSetup
+ _objc_msgSend$allowLockScreenDismissal
+ _objc_msgSend$allowMenuButtonDismissal
+ _objc_msgSend$allowNoButton
+ _objc_msgSend$allowedApps
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$autoDownloadOnBatteryDelay
+ _objc_msgSend$autoDownloadOnBatteryMinBattery
+ _objc_msgSend$autoScanAndDownloadNow:ifAvailable:
+ _objc_msgSend$build
+ _objc_msgSend$buildAlertItemDefinition
+ _objc_msgSend$buttons
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$contentExtensionID
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$deleteKeepAliveFilePath:
+ _objc_msgSend$dismiss
+ _objc_msgSend$dismissAlertsOfClass:animated:
+ _objc_msgSend$extensionDictionary
+ _objc_msgSend$fakeAppOffload
+ _objc_msgSend$forcesModalAlertAppearance
+ _objc_msgSend$granularlyRamped
+ _objc_msgSend$handler
+ _objc_msgSend$initWithHandler:
+ _objc_msgSend$initWithLabel:presentationStyle:isPreferredButton:handler:
+ _objc_msgSend$initWithTitle:
+ _objc_msgSend$isPreferredButton
+ _objc_msgSend$isVirtualDevice
+ _objc_msgSend$keybagInterfacePasscodeDidChange:
+ _objc_msgSend$label
+ _objc_msgSend$localTimeZone
+ _objc_msgSend$message
+ _objc_msgSend$now
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$overrideAllowAutoDownloadOnBattery
+ _objc_msgSend$overrideAutoDownloadOnBatteryDelay
+ _objc_msgSend$overrideGranularRamping
+ _objc_msgSend$overrideRamping
+ _objc_msgSend$present
+ _objc_msgSend$presentAlert:animated:
+ _objc_msgSend$presentationStyle
+ _objc_msgSend$presentedAlertsOfClass:
+ _objc_msgSend$reappearsAfterLock
+ _objc_msgSend$reappearsAfterUnlock
+ _objc_msgSend$releasedBefore:
+ _objc_msgSend$setAllowAutoDownloadOnBattery:
+ _objc_msgSend$setAutoDownloadOnBatteryDelay:
+ _objc_msgSend$setAutoDownloadOnBatteryMinBattery:
+ _objc_msgSend$setButtons:
+ _objc_msgSend$setDateStyle:
+ _objc_msgSend$setGranularlyRamped:
+ _objc_msgSend$setIsPreferredButton:
+ _objc_msgSend$setIsUILocked:
+ _objc_msgSend$setPresentationStyle:
+ _objc_msgSend$setUpdateFullyUnrampedDates:
+ _objc_msgSend$shouldShowInLockScreen
+ _objc_msgSend$showButtonsOnLockScreen
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$title
+ _objc_msgSend$undimsScreen
+ _objc_msgSend$unmetConstraints
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$update
+ _objc_msgSend$willPresentAlert
+ _objc_msgSend$writeKeepAliveFilePath:
+ _objc_release_x3
+ _objc_release_x4
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
+ _prettyPrintDate:.__dateFormatter
+ _specificTimeOnDate
- +[SUAppPurgingNotification postAppPurgingNotificationWithCompletion:]
- +[SUUtility postAutoUpdateInformationalNotification:body:buttonText:altButtonText:withCompletion:]
- +[SUUtility postFailureNotification:body:buttonText:altButtonText:]
- -[SUAutoDownloadPolicy minimumPowerRequirement]
- -[SUAutoInstallFailureNotification .cxx_destruct]
- -[SUAutoInstallFailureNotification dealloc]
- -[SUAutoInstallFailureNotification dismissNotification]
- -[SUAutoInstallFailureNotification init]
- -[SUAutoInstallFailureNotification postNotificationForError:]
- -[SUAutoInstallFailureNotification postNotificationForError:withUpdateBuildNumber:]
- -[SUAutoInstallForecast dealloc]
- -[SUAutoUpdatePasscodePolicy dealloc]
- -[SUCarrierDownloadPolicyProperties dealloc]
- -[SUDefaultDownloadPolicy dealloc]
- -[SUDefaultDownloadPolicy minimumPowerRequirement]
- -[SUDownload dealloc]
- -[SUDownloadMetadata dealloc]
- -[SUInstallationConstraintMonitorBase dealloc]
- -[SUInstallationConstraintMonitorCarplay dealloc]
- -[SUInstallationConstraintMonitorSync dealloc]
- -[SUKeybagInterface dealloc]
- -[SUManagedDeviceUpdateDelay dealloc]
- -[SUManagerClient scheduleDateActivity:]
- -[SUOperationProgress dealloc]
- -[SUSFollowUpController dealloc]
- -[SUScanResults dealloc]
- -[SUState alternateLastScannedDescriptor]
- -[SUState preferredLastScannedDescriptor]
- -[SUState setAlternateLastScannedDescriptor:]
- -[SUState setPreferredLastScannedDescriptor:]
- -[SUUpdateDiscoveryDateManager dealloc]
- -[_SUAutoInstallForecastDateCache dealloc]
- -[_SUAutoInstallOperationModel dealloc]
- GCC_except_table104
- GCC_except_table116
- GCC_except_table137
- GCC_except_table169
- GCC_except_table183
- GCC_except_table194
- GCC_except_table219
- GCC_except_table224
- GCC_except_table229
- GCC_except_table269
- GCC_except_table54
- GCC_except_table62
- GCC_except_table80
- GCC_except_table85
- GCC_except_table98
- OBJC_IVAR_$_SUState._alternateLastScannedDescriptor
- OBJC_IVAR_$_SUState._preferredLastScannedDescriptor
- _OBJC_CLASS_$_SUAppPurgingNotification
- _OBJC_CLASS_$_SUAutoInstallFailureNotification
- _OBJC_IVAR_$_SUAutoInstallFailureNotification._notification
- _OBJC_IVAR_$_SUAutoInstallFailureNotification._notificationLock
- _OBJC_METACLASS_$_SUAppPurgingNotification
- _OBJC_METACLASS_$_SUAutoInstallFailureNotification
- __OBJC_$_CLASS_METHODS_SUAppPurgingNotification
- __OBJC_$_CLASS_METHODS_SUDescriptor
- __OBJC_$_INSTANCE_METHODS_SUAutoInstallFailureNotification
- __OBJC_$_INSTANCE_METHODS_SUDescriptor
- __OBJC_$_INSTANCE_VARIABLES_SUAutoInstallFailureNotification
- __OBJC_$_PROP_LIST_SUAppPurgingNotification
- __OBJC_$_PROP_LIST_SUAutoInstallFailureNotification
- __OBJC_$_PROTOCOL_CLASS_METHODS_OPT_SUAppPurgingNotification
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SUAutoInstallFailureNotification
- __OBJC_$_PROTOCOL_METHOD_TYPES_SUAppPurgingNotification
- __OBJC_$_PROTOCOL_METHOD_TYPES_SUAutoInstallFailureNotification
- __OBJC_$_PROTOCOL_REFS_SUAppPurgingNotification
- __OBJC_$_PROTOCOL_REFS_SUAutoInstallFailureNotification
- __OBJC_CLASS_PROTOCOLS_$_SUAppPurgingNotification
- __OBJC_CLASS_PROTOCOLS_$_SUAutoInstallFailureNotification
- __OBJC_CLASS_RO_$_SUAppPurgingNotification
- __OBJC_CLASS_RO_$_SUAutoInstallFailureNotification
- __OBJC_LABEL_PROTOCOL_$_SUAppPurgingNotification
- __OBJC_LABEL_PROTOCOL_$_SUAutoInstallFailureNotification
- __OBJC_METACLASS_RO_$_SUAppPurgingNotification
- __OBJC_METACLASS_RO_$_SUAutoInstallFailureNotification
- __OBJC_PROTOCOL_$_SUAppPurgingNotification
- __OBJC_PROTOCOL_$_SUAutoInstallFailureNotification
- ___40-[SUManagerClient scheduleDateActivity:]_block_invoke
- ___41-[SUState alternateLastScannedDescriptor]_block_invoke
- ___41-[SUState preferredLastScannedDescriptor]_block_invoke
- ___45-[SUState setAlternateLastScannedDescriptor:]_block_invoke
- ___45-[SUState setPreferredLastScannedDescriptor:]_block_invoke
- ___46-[SUInstallationConstraintMonitorSync dealloc]_block_invoke
- ___49-[SUInstallationConstraintMonitorNetwork dealloc]_block_invoke
- ___55-[SUAutoInstallFailureNotification dismissNotification]_block_invoke
- ___69+[SUAppPurgingNotification postAppPurgingNotificationWithCompletion:]_block_invoke
- ___83-[SUAutoInstallFailureNotification postNotificationForError:withUpdateBuildNumber:]_block_invoke
- ___83-[SUAutoInstallFailureNotification postNotificationForError:withUpdateBuildNumber:]_block_invoke_2
- ___98+[SUUtility postAutoUpdateInformationalNotification:body:buttonText:altButtonText:withCompletion:]_block_invoke
- ___block_descriptor_40_e8_32b_e15_v28?0Q8i16^B20ls32l8
- ___block_descriptor_40_e8_32b_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_40_e8_32b_e34_v24?0"NSDictionary"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32b_e79_v40?0"SUDownload"8"SUInstallPolicy"16"SUAutoInstallOperation"24"NSError"32ls32l8
- ___block_descriptor_40_e8_32o_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_40_e8_32o_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_41_e8_32o_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32b_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32o40b_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_48_e8_32o40b_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_48_e8_32o40b_e20_v24?0Q8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32o40b_e23_v32?0Q8Q16"NSError"24ls32l8s40l8
- ___block_descriptor_48_e8_32o40b_e28_v24?0"NSDate"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32o40b_e30_v24?0"NSNumber"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32o40b_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32o40b_e34_v24?0"SUDescriptor"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32o40b_e35_v24?0"SUScanResults"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32o40b_e35_v32?0B8B12"NSError"16"NSError"24ls32l8s40l8
- ___block_descriptor_48_e8_32o40b_e42_v24?0"SUCoreDDMDeclaration"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32o40b_e42_v24?0"SURollbackDescriptor"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32o40b_e43_v24?0"SUAutoInstallForecast"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32o40b_e45_v28?0B8"SURollbackDescriptor"12"NSError"20ls32l8s40l8
- ___block_descriptor_48_e8_32o40b_e50_v24?0"_SUAutoInstallOperationModel"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32o40b_e5_v8?0ls32l8s40l8
- ___block_descriptor_48_e8_32o40b_e5_v8?0ls40l8s32l8
- ___block_descriptor_48_e8_32o40b_e85_v40?0"SUDownload"8"SUInstallPolicy"16"_SUAutoInstallOperationModel"24"NSError"32ls32l8s40l8
- ___block_descriptor_48_e8_32o40o_e15_v32?08Q16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32o40o_e5_v8?0ls32l8s40l8
- ___block_descriptor_48_e8_32o40r_e34_v24?0"SUDescriptor"8"NSError"16ls32l8r40l8
- ___block_descriptor_48_e8_32o40r_e48_v28?0B8"ASDPurgeableAppResponse"12"NSError"20lr40l8s32l8
- ___block_descriptor_48_e8_32o40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_48_e8_32o40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_48_e8_32o40r_e8_v12?0I8lr40l8s32l8
- ___block_descriptor_48_e8_32o_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32r_e20_v20?0B8"NSError"12lr32l8
- ___block_descriptor_48_e8_32r_e29_v24?0"NSArray"8"NSError"16lr32l8
- ___block_descriptor_51_e8_32b_e5_v8?0ls32l8
- ___block_descriptor_56_e8_32o40b48r_e5_v8?0ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32o40o48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32o40o48r_e5_v8?0ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32o40o_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_e8_32o40r48r_e20_v20?0B8"NSError"12ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32o40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_64_e8_32o40b_e5_v8?0ls40l8s32l8
- ___block_descriptor_74_e8_32o40o48o56o64o_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_88_e8_32s40s48bs56bs64bs72bs80r_e8_v12?0B8ls32l8s48l8r80l8s40l8s56l8s64l8s72l8
- ___block_literal_global.19
- ___block_literal_global.24
- ___block_literal_global.29
- ___block_literal_global.34
- ___block_literal_global.374
- ___block_literal_global.382
- ___block_literal_global.39
- ___block_literal_global.391
- ___block_literal_global.396
- ___block_literal_global.44
- ___block_literal_global.49
- ___block_literal_global.505
- ___block_literal_global.54
- ___block_literal_global.62
- ___block_literal_global.67
- ___block_literal_global.97
- __getUnmetConstraintBodyStrings
- __iOSAutoDownloadBatterySatisifed
- __splatAutoDownloadBatteryRequiement
- __splatAutoDownloadBatterySatisfied
- __splatAutoDownloadMinimumBatteryRequirement
- __stringsForError
- __unnamed_array_storage.413
- __unnamed_array_storage.416
- _kCFUserNotificationAlternateButtonTitleKey
- _kCFUserNotificationDefaultButtonTitleKey
- _nw_release
- _objc_loadWeak
- _objc_msgSend$alternateLastScannedDescriptor
- _objc_msgSend$dismissNotification
- _objc_msgSend$floatValue
- _objc_msgSend$isMainThread
- _objc_msgSend$postAppPurgingNotificationWithCompletion:
- _objc_msgSend$postNotificationForError:withUpdateBuildNumber:
- _objc_msgSend$preferredLastScannedDescriptor
- _objc_msgSend$scheduleDateActivity:
- _objc_msgSend$setAlternateLastScannedDescriptor:
- _objc_msgSend$setPreferredLastScannedDescriptor:
CStrings:
+ "\x01\x11"
+ "\x015"
+ "\x02\x11"
+ "\x03"
+ "\x03\x11"
+ "\x05"
+ "\x06"
+ "\b\x1f\x0e"
+ "\n            Publisher: %@\n            HumanReadableUpdateName: %@\n            ProductSystemName: %@\n            ProductVersion: %@\n            ProductVersionExtra: %@\n            ProductBuildVersion: %@\n            PrerequisiteBuild: %@\n            PrerequisiteOS: %@\n            ReleaseType: %@\n            DownloadSize: %@\n            UnarchiveSize: %@\n            MSUPrepareSize: %@\n            PreparationSize: %@\n            InstallationSize: %@\n            UpdateType: %@\n            Downloadable: %@\n            DownloadableOverCellular: %@\n            AutoDownloadableOverCellular: %@\n            AutoUpdateEnabled: %@\n            StreamingZipCapable: %d\n            TotalRequiredFreeSpace: %@\n            Documentation: %@\n            SiriVoiceDeletion: %d\n            CDLevel4Deletion: %d\n            appDemotionDisabled: %d\n            installTonightDisabled: %d\n            rampEnabled: %d\n            granularlyRamped: %d\n            setupCritical: %@\n            criticalOutOfBoxOnly: %d\n            criticalDownloadPolicy: %@\n            releaseDate: %@\n            mdmDelayInterval: %@\n            assetID: %@\n            hideInstallAlert %@\n            audienceType %@\n            preferenceType %@\n            upgradeType %@\n            promoteAlternateUpdate: %@\n            isSplatOnly: %@\n            mandatoryUpdateEligible: %@\n            mandatoryUpdateVersionMin: %@\n            mandatoryUpdateVersionMax: %@\n            mandatoryUpdateOptional: %@\n            mandatoryUpdateRestrictedToOutOfTheBox: %@\n            forcePasscodeRequired: %@\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %u\n            autoDownloadOnBatteryMinbattery: %u%%\n"
+ "\nw\x11R!"
+ "\x11#"
+ "\x13"
+ "#"
+ "%@ is being presented for %@. Dismiss it first"
+ "%s: %@ is OFF"
+ "%s: %@ is ON"
+ "%s: %@: require %u%% battery"
+ "%s: Non-auto-downloading doesn't have any power requirements"
+ "%s: currentBatteryLevel = %llu, requiredBatteryLevel = %llu"
+ "%s: failed to get battery level; returning 0"
+ "-[SUManagerClient autoScanAndDownloadNow:IfAvailable:]"
+ "-[SUManagerClient autoScanAndDownloadNow:IfAvailable:]_block_invoke"
+ "-[SUPreferences autoInstallSecurityResponseForceOff]"
+ "-[SUPreferences autoInstallSecurityResponseForceOn]"
+ "-[SUPreferences autoInstallSystemDataFilesForceOff]"
+ "-[SUPreferences autoInstallSystemDataFilesForceOn]"
+ "-[SUPreferences autoUpdateForceOff]"
+ "-[SUPreferences autoUpdateForceOn]"
+ "/var/mobile/Library/SoftwareUpdate/susdAUKeepAlive"
+ "0@`"
+ "@\"SUAlertPresentationManager\""
+ "@44@0:8@16Q24B32@?36"
+ "@?"
+ "@?16@0:8"
+ "Alerts"
+ "AllowAutoDownloadOnBattery"
+ "App offload accepted by user"
+ "AutoDownloadOnBatteryDelay"
+ "AutoDownloadOnBatteryMinBattery"
+ "B24@0:8d16"
+ "BOOL SUHasEnoughBatteryForAutoDownloadForDescriptor(SUDescriptor *__strong _Nonnull, NSDate *__strong _Nonnull)"
+ "BOOL SUHasEnoughBatteryForDownloadForDescriptor(SUDescriptor *__strong _Nonnull)"
+ "Default set to override granular ramping to YES"
+ "Default set to override ramping to YES"
+ "Delay before auto-downloading on battery after the update is fully-unramped"
+ "Failed to delete keep alive file:%@"
+ "Failed to update %@ for %@"
+ "Failed to write keep alive file:%@"
+ "Faking an app offload with %@"
+ "GranularlyRamped"
+ "I"
+ "I16@0:8"
+ "If set to true, allow auto-downloading on battery"
+ "If set to true, descriptors will be considered granularly ramped"
+ "If set to true, descriptors will be considered ramped"
+ "If set to true, fake an app offload when making room"
+ "If set to true, force an installation failure"
+ "Invalid passcode policy type: %lu. Leaving policy as %@"
+ "LastDownload: %@            \npreferredLastScannedCoreDescriptor: %@            \nalternateLastScannedCoreDescriptor: %@            \nFailedPatchDescriptors: %@            \nScheduledManualDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadPolicyChangeTime: %@            \nLastScanDate: %@            \nLastAutoDownloadDate: %@            \nNeedsOneTimeAutodownloadRetry: %@            \nStashbagIsPersisted: %@            \nLastProductVersion: %@            \nLastProductBuild: %@            \nLastProductType: %@            \nLastReleaseType: %@            \nLastSplatRestoreVersion: %@            \nLastAutoInstallOperationModel: %@            \nManagedDeviceDelay: %@            \nInstallPolicy: %@            \nMandatoryUpdateDict: %@            \nLastRollbackRecommendedBuildVersion: %@            \rolledBackBuildVersions: %@            \nsessionID: %@            \nlastDeletedAssetID: %@            \nlastAssetAudience: %@            \nappliedSate: %@            \nunderExclusiveControl: %@            \nLastRecommendedUpdateVersion: %@            \nLastRecommendedUpdateInterval: %@            \nLastRecommendedUpdateDiscoveryDate: %@            \nUpdateDiscoveryDates: %@"
+ "NSNumber * _Nonnull SURequiredBatteryLevelForDownloadForDescriptor(SUDescriptor *__strong _Nonnull)"
+ "NSNumber *getCurrentBatteryLevel(void)"
+ "No action registered for button %ld"
+ "No keep alive file found at:%@"
+ "No notification for %@"
+ "No passcode set, keybag is not required"
+ "OK_BUTTON"
+ "SUAlertButtonDefinition"
+ "SUAlertItemDefinition"
+ "SUAlertPresentationManager"
+ "SUAppPurgingAlertItem"
+ "SUAutoInstallFailureAlertItem"
+ "SUAutomaticInstallation"
+ "SUBaseAlertItem"
+ "SUBaseAlertItem Default Title"
+ "SUBattery"
+ "SUFakeAppOffload"
+ "SUFakeInstallFailure"
+ "SUFullyUnrampedDates"
+ "SUKeybagInterface got passcode changed event"
+ "SUOverrideAllowAutoDownloadOnBattery"
+ "SUOverrideAutoDownloadOnBatteryDelay"
+ "SUOverrideGranularRamping"
+ "SUOverrideRamping"
+ "SUOverrideScanSessionIDRampingPortion"
+ "Successfully deleted keep alive file:%@"
+ "Successfully wrote keep alive file:%@"
+ "T@\"<SUAutoInstallOperationDelegate>\",W,N,V_delegate"
+ "T@\"NSArray\",&,N,V_buttons"
+ "T@\"NSDictionary\",&,N,V_updateFullyUnrampedDates"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,&,N,V_label"
+ "T@?,R,&,N,V_handler"
+ "TB,N,GgranularlyRamped,V_granularlyRamped"
+ "TB,N,GrampEnabled,V_rampEnabled"
+ "TB,N,V_allowAutoDownloadOnBattery"
+ "TB,N,V_isUILocked"
+ "TB,R,N,V_isPreferredButton"
+ "TI,N,V_autoDownloadOnBatteryDelay"
+ "TI,N,V_autoDownloadOnBatteryMinBattery"
+ "TQ,R,N,V_presentationStyle"
+ "To override the ramping portion of a scan session id"
+ "User clicked button index %ld"
+ "WiFi background assertion count changed: %lu"
+ "[%@] User accepted to purge apps."
+ "[%@] User declined to purge apps."
+ "[%@] was dismissed for %ld"
+ "[%@] willPresentAlert"
+ "[Alerts] Dismissing alert: %@"
+ "[Alerts] Dismissing alerts of class: %@"
+ "[Alerts] Dismissing all alerts excluding classes: %@"
+ "[Alerts] Failed presenting alert: %@"
+ "[Alerts] Presenting alert: %@"
+ "[Alerts] Updating alert lock state to isUILocked: %@"
+ "[Alerts] Updating alert: %@"
+ "[Auto scan] Apple Internal: Downloading every 1 day"
+ "_SBPresentationStyleForSUSPresentationStyle:"
+ "_alerts"
+ "_allowAutoDownloadOnBattery"
+ "_autoDownloadOnBatteryDelay"
+ "_autoDownloadOnBatteryMinBattery"
+ "_buildNumber"
+ "_buttons"
+ "_cancelNotification"
+ "_createNotification"
+ "_dismissAlert:animated:"
+ "_dismissAlertsOfClass:animated:"
+ "_dismissAllAlertsExcludingClasses:animated:"
+ "_error"
+ "_granularlyRamped"
+ "_handler"
+ "_isPreferredButton"
+ "_isUILocked"
+ "_label"
+ "_manager"
+ "_noButton"
+ "_noteAlertDeactivated:"
+ "_notificationButtonActions"
+ "_notificationButtons"
+ "_notificationFlags"
+ "_notificationOptions"
+ "_notificationWasDismissed:"
+ "_okButton"
+ "_passcodeChangedNotifyToken"
+ "_presentAlert:animated:"
+ "_presentationStyle"
+ "_presentedAlerts"
+ "_presentedAlertsOfClass:"
+ "_queue_passcodeChanged"
+ "_radarButton"
+ "_setPresentationManager:"
+ "_stateQ"
+ "_updateAlert:animated:"
+ "_updateAllAlertLockState:"
+ "_updateFullyUnrampedDates"
+ "_updateNotification"
+ "_yesButton"
+ "alertWasDismissed:"
+ "allowAutoDownloadOnBattery"
+ "allowInSetup"
+ "allowLockScreenDismissal"
+ "allowMenuButtonDismissal"
+ "allowNoButton"
+ "allowedApps"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "autoDownloadOnBatteryDelay"
+ "autoDownloadOnBatteryDelay = %.0lf sec (~ %.2lf days)"
+ "autoDownloadOnBatteryDelay is set to %.0lf sec by default"
+ "autoDownloadOnBatteryMinBattery"
+ "autoScanAndDownloadNow:IfAvailable:"
+ "autoScanAndDownloadNow:ifAvailable:"
+ "build"
+ "buildAlertItemDefinition"
+ "buttons"
+ "cStringUsingEncoding:"
+ "com.apple.sus.alertItem.stateQ"
+ "connected to charger"
+ "contentExtensionID"
+ "created %@ for %@ with error %ld"
+ "currentCalendar"
+ "deleteAUKeepAliveFile"
+ "deleteKeepAliveFilePath:"
+ "dismiss"
+ "dismissAlert:animated:"
+ "dismissAlertsOfClass:animated:"
+ "dismissAllAlertsAnimated:"
+ "dismissAllAlertsExcludingClasses:animated:"
+ "emergency or critical update"
+ "extensionDictionary"
+ "failed to get button index from response dictionary"
+ "failed to get response dictionary from CFUserNotification: %ld"
+ "failed to query metadata: %ld"
+ "fakeAppOffload"
+ "fakeInstallFailure"
+ "forcesModalAlertAppearance"
+ "fullyUnrampedDate = %@ for %@; timeElapsed = %.0lf sec (~ %.2lf days)"
+ "granularlyRamped"
+ "handler"
+ "i24@0:8Q16"
+ "index does not match any button"
+ "initWithError:buildNumber:"
+ "initWithHandler:"
+ "initWithLabel:presentationStyle:isPreferredButton:handler:"
+ "initWithTitle:"
+ "initWithTitle:message:buttons:"
+ "isPreferredButton"
+ "isPresentingAlertsOfClass:"
+ "isUILocked"
+ "keybagInterfacePasscodeDidChange:"
+ "label"
+ "localTimeZone"
+ "neededSpace = %llu"
+ "notification was canceled (alert = %@)"
+ "notification was dismissed for %ld"
+ "notificationOptions %@"
+ "now"
+ "numberWithUnsignedInt:"
+ "off-charger, auto-download, SU, iOS, auto-download on battery allowed, delay not satisfied"
+ "off-charger, auto-download, SU, iOS, auto-download on battery allowed, delay satisfied"
+ "off-charger, auto-download, SU, iOS, auto-download on battery not allowed"
+ "off-charger, auto-download, splat, released 24 hours ago"
+ "off-charger, auto-download, splat, released within 24 hours"
+ "overrideAllowAutoDownloadOnBattery"
+ "overrideAutoDownloadOnBatteryDelay"
+ "overrideGranularRamping"
+ "overrideRamping"
+ "overrideScanSessionIDRampingPortion"
+ "present"
+ "presentAlert:animated:"
+ "presentationStyle"
+ "presentedAlerts"
+ "presentedAlertsOfClass:"
+ "reappearsAfterLock"
+ "reappearsAfterUnlock"
+ "releasedBefore:"
+ "removeDiscoveryDateForBuildVersion:"
+ "setAllowAutoDownloadOnBattery:"
+ "setAutoDownloadOnBatteryDelay:"
+ "setAutoDownloadOnBatteryMinBattery:"
+ "setButtons:"
+ "setDateStyle:"
+ "setGranularlyRamped:"
+ "setIsPreferredButton:"
+ "setIsUILocked:"
+ "setPresentationStyle:"
+ "setUpdateFullyUnrampedDates:"
+ "shouldShowCountdown"
+ "shouldShowInLockScreen"
+ "showButtonsOnLockScreen"
+ "timeIntervalSinceDate:"
+ "undimsScreen"
+ "unsatisfiedConstraints = %lu, ignorableConstraints = %lu, realUnsatisfiedConstraints = %lu"
+ "unsigned int _requiredBatteryLevelToAutoDownload(SUDescriptor *__strong _Nonnull, BOOL, BOOL)"
+ "unsignedIntValue"
+ "update"
+ "updateAlert:animated:"
+ "updateAllAlertLockState:"
+ "updateError:withAdditionalUserInfo:"
+ "updateFullyUnrampedDates"
+ "v24@0:8@\"SUKeybagInterface\"16"
+ "v28@0:8#16B24"
+ "v28@0:8B16@?<v@?@\"SUScanResults\"@\"NSError\">20"
+ "weakSelf is gone..."
+ "willPresentAlert"
+ "writeAUKeepAliveFile"
+ "writeKeepAliveFilePath:"
+ "yyyy-MM-dd'T'HH:mm:ss"
- "\n\x1f\r"
- "\n            Publisher: %@\n            HumanReadableUpdateName: %@\n            ProductSystemName: %@\n            ProductVersion: %@\n            ProductVersionExtra: %@\n            ProductBuildVersion: %@\n            PrerequisiteBuild: %@\n            PrerequisiteOS: %@\n            ReleaseType: %@\n            DownloadSize: %@\n            UnarchiveSize: %@\n            MSUPrepareSize: %@\n            PreparationSize: %@\n            InstallationSize: %@\n            UpdateType: %@\n            Downloadable: %@\n            DownloadableOverCellular: %@\n            AutoDownloadableOverCellular: %@\n            AutoUpdateEnabled: %@\n            StreamingZipCapable: %d\n            TotalRequiredFreeSpace: %@\n            Documentation: %@\n            SiriVoiceDeletion: %d\n            CDLevel4Deletion: %d\n            appDemotionDisabled: %d\n            installTonightDisabled: %d\n            rampEnabled: %d\n            setupCritical: %@\n            criticalOutOfBoxOnly: %d\n            criticalDownloadPolicy: %@\n            releaseDate: %@\n            mdmDelayInterval: %@\n            assetID: %@\n            hideInstallAlert %@\n            audienceType %@\n            preferenceType %@\n            upgradeType %@\n            promoteAlternateUpdate: %@\n            isSplatOnly: %@\n            mandatoryUpdateEligible: %@\n            mandatoryUpdateVersionMin: %@\n            mandatoryUpdateVersionMax: %@\n            mandatoryUpdateOptional: %@\n            mandatoryUpdateRestrictedToOutOfTheBox: %@\n            forcePasscodeRequired: %@\n"
- "\nw\x11R\x11"
- "%@ dismissed."
- "-[SUManagerClient scheduleDateActivity:]"
- "-[SUManagerClient scheduleDateActivity:]_block_invoke"
- "/private/var/"
- "@\"NSNumber\"16@0:8"
- "@\"NSObject\""
- "BOOL SUHasEnoughBatteryForInstallation(SUDescriptor *, SUInstallOptions *)"
- "BOOL _splatAutoDownloadBatterySatisfied(SUDescriptor *)"
- "Button %d is pressed"
- "Failed to delete keep alive file"
- "Failed to write keep alive file"
- "Ignoring unmet constraint: %@"
- "Invalid passcode policy type: %d. Leaving policy as %@"
- "LastDownload: %@            \npreferredLastScannedDescriptor: %@            \npreferredLastScannedCoreDescriptor: %@            \nalternateLastScannedDescriptor: %@            \nalternateLastScannedCoreDescriptor: %@            \nFailedPatchDescriptors: %@            \nScheduledManualDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadPolicyChangeTime: %@            \nLastScanDate: %@            \nLastAutoDownloadDate: %@            \nNeedsOneTimeAutodownloadRetry: %@            \nStashbagIsPersisted: %@            \nLastProductVersion: %@            \nLastProductBuild: %@            \nLastProductType: %@            \nLastReleaseType: %@            \nLastSplatRestoreVersion: %@            \nLastAutoInstallOperationModel: %@            \nManagedDeviceDelay: %@            \nInstallPolicy: %@            \nMandatoryUpdateDict: %@            \nLastRollbackRecommendedBuildVersion: %@            \rolledBackBuildVersions: %@            \nsessionID: %@            \nlastDeletedAssetID: %@            \nlastAssetAudience: %@            \nappliedSate: %@            \nunderExclusiveControl: %@            \nLastRecommendedUpdateVersion: %@            \nLastRecommendedUpdateInterval: %@            \nLastRecommendedUpdateDiscoveryDate: %@            \nUpdateDiscoveryDates: %@"
- "No keep alive file found"
- "Posting install tonight failure notification with error: %@"
- "SUAlternateLastScannedDescriptor"
- "SUAppPurgingNotification"
- "SUAutoInstallFailureNotification"
- "SUPreferredLastScannedDescriptor"
- "Successfully deleted keep alive file"
- "Successfully wrote keep alive file"
- "T@\"<SUAutoInstallOperationDelegate>\",N,V_delegate"
- "T@\"SUDescriptor\",C,N,V_alternateLastScannedDescriptor"
- "T@\"SUDescriptor\",C,N,V_preferredLastScannedDescriptor"
- "TB,N,V_rampEnabled"
- "Unexpected nil notification"
- "Unexpected response from CFUserNotification %d"
- "WiFi background assertion count changed: %d"
- "[Auto scan] Apple Internal: Downloading every 2 hours"
- "[Auto scan] Apple Internal: Scanning every 2 hours"
- "_alternateLastScannedDescriptor"
- "_notificationLock"
- "_preferredLastScannedDescriptor"
- "alternateLastScannedDescriptor"
- "dismissNotification"
- "failed to create alert message body"
- "failed to create alert message header"
- "failed to get response from CFUserNotification: %d"
- "failed to query metadata: %d"
- "floatValue"
- "isMainThread"
- "minimumPowerRequirement"
- "postAppPurgingNotificationWithCompletion:"
- "postAutoUpdateInformationalNotification:body:buttonText:altButtonText:withCompletion:"
- "postFailureNotification:body:buttonText:altButtonText:"
- "postNotificationForError:"
- "postNotificationForError:withUpdateBuildNumber:"
- "preferredLastScannedDescriptor"
- "scheduleDateActivity:"
- "setAlternateLastScannedDescriptor:"
- "setPreferredLastScannedDescriptor:"
- "v12@?0B8"
- "v24@0:8@?<v@?B>16"
- "v32@0:8@\"NSError\"16@\"NSString\"24"
- "v48@0:8@16@24@32@40"
- "v56@0:8@16@24@32@40@?48"

```
