## LoginUIKit

> `/System/Library/PrivateFrameworks/LoginUIKit.framework/Versions/A/LoginUIKit`

```diff

-413.0.0.0.0
-  __TEXT.__text: 0xac058
-  __TEXT.__objc_methlist: 0xac50
-  __TEXT.__const: 0x134e
-  __TEXT.__cstring: 0xa1dd
-  __TEXT.__gcc_except_tab: 0x10ec
+415.0.0.0.0
+  __TEXT.__text: 0xad5c0
+  __TEXT.__objc_methlist: 0xacec
+  __TEXT.__const: 0x1350
+  __TEXT.__cstring: 0xa2a5
+  __TEXT.__gcc_except_tab: 0x112c
   __TEXT.__dlopen_cstrs: 0x404
   __TEXT.__ustring: 0x3a
-  __TEXT.__oslogstring: 0x721
+  __TEXT.__oslogstring: 0x72c
   __TEXT.__swift5_typeref: 0x524
   __TEXT.__constg_swiftt: 0x480
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift_as_ret: 0x5c
   __TEXT.__swift_as_cont: 0x8c
   __TEXT.__swift5_fieldmd: 0x16c
-  __TEXT.__swift5_reflstr: 0x103
+  __TEXT.__swift5_reflstr: 0xfe
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0x3c
-  __TEXT.__unwind_info: 0x2d10
+  __TEXT.__unwind_info: 0x2da0
   __TEXT.__eh_frame: 0xf08
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x940
+  __DATA_CONST.__const: 0x980
   __DATA_CONST.__objc_classlist: 0x5b8
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x100
+  __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5ff0
+  __DATA_CONST.__objc_selrefs: 0x6060
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x4e8
   __DATA_CONST.__objc_arraydata: 0x1a8
-  __DATA_CONST.__got: 0x11a0
-  __AUTH_CONST.__const: 0x3381
-  __AUTH_CONST.__cfstring: 0x8d20
+  __DATA_CONST.__got: 0x11b0
+  __AUTH_CONST.__const: 0x3518
+  __AUTH_CONST.__cfstring: 0x8e80
   __AUTH_CONST.__objc_const: 0x10ee8
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x1e0

   __AUTH_CONST.__auth_got: 0x1190
   __AUTH.__objc_data: 0x35c0
   __AUTH.__data: 0x340
-  __DATA.__objc_ivar: 0xb38
-  __DATA.__data: 0xff0
-  __DATA.__bss: 0xe20
+  __DATA.__objc_ivar: 0xb40
+  __DATA.__data: 0xf30
+  __DATA.__bss: 0xe40
   __DATA.__common: 0xd8
   __DATA_DIRTY.__objc_data: 0x4a8
   __DATA_DIRTY.__data: 0x58

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4694
-  Symbols:   9565
-  CStrings:  1405
+  Functions: 4732
+  Symbols:   9630
+  CStrings:  1418
 
Symbols:
+ +[LUIPrefs _invalidateManagedPreferences]
+ +[LUIPrefs _managedPreferencesFromDisk]
+ +[LUIPrefs _managedPreferences]
+ +[LUIUserController fvUnlockPlatformSSOEnabled]
+ +[LUIUserController prefetchFVUnlockPlatformSSOEnabled]
+ -[LUI2BatteryViewController _imageForBattery:showPercentage:]
+ -[LUI2BatteryViewController _powerStateDidChange:]
+ -[LUI2BatteryViewController paused]
+ -[LUI2BatteryViewController setPaused:]
+ -[LUI2ProgressBarWindowController showWindow:]
+ -[LUI2RecoveryKeyFormatter _recoveryKeyByRemappingCharacters:]
+ -[LUI2UserCollectionViewController _dispatchAvatarTransition:]
+ -[LUI2UserCollectionViewController _dispatchAvatarTransitionWithFilter:transition:]
+ -[LUI2UserCollectionViewController _transitionToSelected]
+ -[LUI2UserCollectionViewController enumerateAllCollectionViewItemsAndPerformBlock:]
+ -[LUI2UserView finishAddingUserAvatar]
+ -[LUI2UserView prepareToAddUserAvatar]
+ -[LUI2UserView revealUserAvatar]
+ -[LUIBattery isLowPowerModeEnabled]
+ -[LUIBatteryStatusController _powerStateDidChange:]
+ -[LUIBatteryStatusController paused]
+ -[LUIBatteryStatusController setPaused:]
+ -[LUIFVUnlockUser isPSSOUser]
+ -[LUIUserController _userListHasAuthenticatedPSSOTemporaryUser:]
+ -[TRMPortManager _performOnQueueSync:]
+ -[TRMPortManager _stopAllPorts]
+ GCC_except_table108
+ GCC_except_table110
+ GCC_except_table113
+ GCC_except_table117
+ GCC_except_table125
+ GCC_except_table130
+ GCC_except_table135
+ GCC_except_table138
+ GCC_except_table140
+ GCC_except_table142
+ GCC_except_table34
+ GCC_except_table37
+ GCC_except_table61
+ GCC_except_table65
+ GCC_except_table69
+ GCC_except_table70
+ GCC_except_table83
+ GCC_except_table85
+ GCC_except_table92
+ OBJC_IVAR_$_LUI2BatteryViewController._paused
+ OBJC_IVAR_$_LUIBatteryStatusController._paused
+ _NSProcessInfoPowerStateDidChangeNotification
+ _OBJC_CLASS_$_NSProcessInfo
+ __32-[LUI2UserViewController resume]_block_invoke_2
+ __57-[LUI2UserCollectionViewController _transitionToSelected]_block_invoke
+ __57-[LUI2UserCollectionViewController _transitionToSelected]_block_invoke_2
+ __60-[LUI2UserCollectionViewController _resumeAvatarInUserView:]_block_invoke_2
+ ___23-[TRMPortManager ports]_block_invoke
+ ___31-[TRMPortManager _stopAllPorts]_block_invoke
+ ___32-[LUI2UserViewController resume]_block_invoke_4
+ ___36-[TRMPortManager hasRestrictedPorts]_block_invoke_2
+ ___37-[TRMPort _stopInterestNotifications]_block_invoke
+ ___47+[LUIUserController fvUnlockPlatformSSOEnabled]_block_invoke
+ ___55+[LUIUserController prefetchFVUnlockPlatformSSOEnabled]_block_invoke
+ ___57-[LUI2UserCollectionViewController _transitionToSelected]_block_invoke
+ ___57-[LUI2UserCollectionViewController _transitionToSelected]_block_invoke_2
+ ___60-[LUI2UserCollectionViewController _resumeAvatarInUserView:]_block_invoke_3
+ ___60-[LUI2UserCollectionViewController _resumeAvatarInUserView:]_block_invoke_4
+ ___62-[LUI2UserCollectionViewController _dispatchAvatarTransition:]_block_invoke
+ ___64-[LUIUserController _userListHasAuthenticatedPSSOTemporaryUser:]_block_invoke
+ ___83-[LUI2UserCollectionViewController _dispatchAvatarTransitionWithFilter:transition:]_block_invoke
+ ___block_descriptor_136_e8_32s40s48s56s64s72s80bs_e5_v8?0l
+ ___block_descriptor_32_e34_v16?0"AVTLockscreenCoordinator"8l
+ ___block_descriptor_32_e37_v24?0"AVTLockscreenCoordinator"816l
+ ___block_descriptor_40_e8_32bs_e37_v24?0"AVTLockscreenCoordinator"816l
+ ___block_descriptor_40_e8_32s_e29_v32?0"LUI2UserView"8Q16^B24l
+ ___block_descriptor_40_e8_32s_e34_16?0"AVTLockscreenCoordinator"8l
+ ___block_descriptor_40_e8_32w_e34_v16?0"AVTLockscreenCoordinator"8l
+ ___block_descriptor_48_e8_32s40r_e5_v8?0l
+ ___block_descriptor_48_e8_32s_e5_v8?0l
+ ___block_descriptor_56_e8_32bs40bs48w_e5_v8?0l
+ ___block_descriptor_72_e8_32s40w48w56w64w_e5_v8?0l
+ ___copy_helper_block_e8_32b40b48w
+ ___copy_helper_block_e8_32s40s48s56s64s72s80b
+ ___copy_helper_block_e8_32s40w48w56w64w
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s
+ ___destroy_helper_block_e8_32s40w48w56w64w
+ _objc_msgSend$_dispatchAvatarTransition:
+ _objc_msgSend$_dispatchAvatarTransitionWithFilter:transition:
+ _objc_msgSend$_imageForBattery:showPercentage:
+ _objc_msgSend$_invalidateManagedPreferences
+ _objc_msgSend$_managedPreferences
+ _objc_msgSend$_managedPreferencesFromDisk
+ _objc_msgSend$_performOnQueueSync:
+ _objc_msgSend$_recoveryKeyByRemappingCharacters:
+ _objc_msgSend$_stopAllPorts
+ _objc_msgSend$_transitionToSelected
+ _objc_msgSend$_userListHasAuthenticatedPSSOTemporaryUser:
+ _objc_msgSend$enumerateAllCollectionViewItemsAndPerformBlock:
+ _objc_msgSend$finishAddingUserAvatar
+ _objc_msgSend$fvUnlockPlatformSSOEnabled
+ _objc_msgSend$isLowPowerModeEnabled
+ _objc_msgSend$prefetchFVUnlockPlatformSSOEnabled
+ _objc_msgSend$prepareToAddUserAvatar
+ _objc_msgSend$processInfo
+ _objc_msgSend$progressBar
+ _objc_msgSend$removeAllAnimations
+ _objc_msgSend$revealUserAvatar
+ _objc_msgSend$setPaused:
+ _objc_msgSend$setRendersContinuously:
+ _sManagedPreferences
+ _sManagedPreferencesLoaded
+ fvUnlockPlatformSSOEnabled.enabled
+ fvUnlockPlatformSSOEnabled.onceToken
- -[LUI2BatteryViewController _imageForBattery:]
- -[LUI2UserCollectionViewController _transitionToSelected:]
- -[LUI2UserCollectionViewController enumerateCollectionViewItemsAndPerformBlock:]
- -[LUI2UserView avatarView:didRenderAvatar:]
- GCC_except_table100
- GCC_except_table101
- GCC_except_table104
- GCC_except_table119
- GCC_except_table124
- GCC_except_table132
- GCC_except_table134
- GCC_except_table136
- GCC_except_table36
- GCC_except_table42
- GCC_except_table53
- GCC_except_table58
- GCC_except_table59
- GCC_except_table63
- GCC_except_table74
- GCC_except_table82
- GCC_except_table84
- GCC_except_table88
- GCC_except_table96
- __32-[LUI2UserViewController resume]_block_invoke
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AVTViewDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_VFXWorldRendererDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_AVTViewDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_VFXWorldRendererDelegate
- __OBJC_$_PROTOCOL_REFS_AVTViewDelegate
- __OBJC_$_PROTOCOL_REFS_VFXWorldRendererDelegate
- __OBJC_LABEL_PROTOCOL_$_AVTViewDelegate
- __OBJC_LABEL_PROTOCOL_$_VFXWorldRendererDelegate
- __OBJC_PROTOCOL_$_AVTViewDelegate
- __OBJC_PROTOCOL_$_VFXWorldRendererDelegate
- ___22-[TRMPortManager stop]_block_invoke
- ___43-[LUI2UserView avatarView:didRenderAvatar:]_block_invoke
- ___58-[LUI2UserCollectionViewController _transitionToSelected:]_block_invoke
- ___58-[LUI2UserCollectionViewController _transitionToSelected:]_block_invoke_2
- ___58-[LUI2UserCollectionViewController _transitionToSelected:]_block_invoke_3
- ___63-[LUI2UserCollectionViewController showAvatarPickerAfterDelay:]_block_invoke_2
- ___block_descriptor_128_e8_32s40s48s56s64s72bs_e5_v8?0l
- ___block_descriptor_40_e8_32w_e29_v32?0"LUI2UserView"8Q16^B24l
- ___copy_helper_block_e8_32s40s48s56s64s72b
- ___destroy_helper_block_e8_32s40s48s56s64s72s
- _objc_msgSend$_transitionToSelected:
CStrings:
+ "\""
+ "0"
+ "23456789ABCDEFGHJKLMNOPQRTUVWXYZ"
+ "5"
+ "@16@?0@\"AVTLockscreenCoordinator\"8"
+ "L"
+ "Low Power Mode"
+ "Modern Style"
+ "O"
+ "Other user can be shown because PSSO temporary accounts are enabled"
+ "S"
+ "Show Percentage"
+ "v16@?0@\"AVTLockscreenCoordinator\"8"
+ "v24@?0@\"AVTLockscreenCoordinator\"8@16"
- "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
```
