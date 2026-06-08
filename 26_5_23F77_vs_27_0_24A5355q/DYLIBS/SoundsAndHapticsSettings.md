## SoundsAndHapticsSettings

> `/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings`

```diff

-1114.4.1.0.0
-  __TEXT.__text: 0x1f8d4
-  __TEXT.__auth_stubs: 0x12a0
-  __TEXT.__objc_methlist: 0x16e4
+1127.0.0.0.0
+  __TEXT.__text: 0x22eb0
+  __TEXT.__objc_methlist: 0x1b04
   __TEXT.__const: 0xc84
-  __TEXT.__gcc_except_tab: 0x448
-  __TEXT.__cstring: 0x2543
-  __TEXT.__oslogstring: 0xa7c
-  __TEXT.__swift5_typeref: 0x106a
+  __TEXT.__gcc_except_tab: 0x9e8
+  __TEXT.__oslogstring: 0x1103
+  __TEXT.__cstring: 0x31d3
+  __TEXT.__swift5_typeref: 0x1070
   __TEXT.__swift5_reflstr: 0x163
   __TEXT.__swift5_assocty: 0xf8
   __TEXT.__constg_swiftt: 0x404

   __TEXT.__swift5_types: 0x38
   __TEXT.__swift5_capture: 0x84
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x880
+  __TEXT.__unwind_info: 0x920
   __TEXT.__eh_frame: 0x70
-  __TEXT.__objc_classname: 0x5d8
-  __TEXT.__objc_methname: 0x546d
-  __TEXT.__objc_methtype: 0xc01
-  __TEXT.__objc_stubs: 0x4660
-  __DATA_CONST.__got: 0x770
-  __DATA_CONST.__const: 0x2a8
-  __DATA_CONST.__objc_classlist: 0xe0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2a0
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1760
+  __DATA_CONST.__objc_selrefs: 0x1838
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x960
+  __DATA_CONST.__objc_superrefs: 0x90
+  __DATA_CONST.__got: 0x768
   __AUTH_CONST.__const: 0x4f0
-  __AUTH_CONST.__cfstring: 0x1900
-  __AUTH_CONST.__objc_const: 0x2330
+  __AUTH_CONST.__cfstring: 0x1b00
+  __AUTH_CONST.__objc_const: 0x2850
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__objc_doubleobj: 0x40
+  __AUTH_CONST.__objc_doubleobj: 0x50
+  __AUTH_CONST.__auth_got: 0xa08
   __AUTH.__objc_data: 0x630
   __AUTH.__data: 0x220
-  __DATA.__objc_ivar: 0x114
-  __DATA.__data: 0x730
+  __DATA.__objc_ivar: 0x160
+  __DATA.__data: 0x7f0
+  __DATA.__bss: 0x680
   __DATA.__common: 0x10
-  __DATA.__bss: 0x7f0
-  __DATA_DIRTY.__objc_data: 0x498
+  __DATA_DIRTY.__objc_data: 0x538
   __DATA_DIRTY.__data: 0x1e0
-  __DATA_DIRTY.__bss: 0x150
+  __DATA_DIRTY.__bss: 0x2c0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/AVRouting

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7A6B700A-F186-3ABB-B3FC-34B7469AF474
-  Functions: 695
-  Symbols:   2241
-  CStrings:  1598
+  UUID: 81C21FFE-ECB4-39EC-84DB-0B29A930DA68
+  Functions: 794
+  Symbols:   2554
+  CStrings:  663
 
Symbols:
+ -[SHSAlarmControl .cxx_destruct]
+ -[SHSAlarmControl _handleEffectiveVolumeDidChangeNotification:]
+ -[SHSAlarmControl _handleServerConnectionDiedNotification:]
+ -[SHSAlarmControl _logFaultCalledForBackground]
+ -[SHSAlarmControl _logFaultCalledForInactive]
+ -[SHSAlarmControl _setup]
+ -[SHSAlarmControl _systemController]
+ -[SHSAlarmControl _tearDown]
+ -[SHSAlarmControl _updateVolume:]
+ -[SHSAlarmControl _volumeChangeCoalescingCount]
+ -[SHSAlarmControl _volumeInitialized]
+ -[SHSAlarmControl alarmVolumeMatchesRingtone]
+ -[SHSAlarmControl appWantsVolumeChangeEvents]
+ -[SHSAlarmControl dealloc]
+ -[SHSAlarmControl delegate]
+ -[SHSAlarmControl flushPendingVolumeChanges]
+ -[SHSAlarmControl init]
+ -[SHSAlarmControl reload]
+ -[SHSAlarmControl setAlarmVolumeMatchesRingtone:]
+ -[SHSAlarmControl setAppWantsVolumeChangeEvents:]
+ -[SHSAlarmControl setDelegate:]
+ -[SHSAlarmControl setVolume:]
+ -[SHSAlarmControl set_logFaultCalledForBackground:]
+ -[SHSAlarmControl set_logFaultCalledForInactive:]
+ -[SHSAlarmControl set_systemController:]
+ -[SHSAlarmControl set_volumeChangeCoalescingCount:]
+ -[SHSAlarmControl set_volumeInitialized:]
+ -[SHSAlarmControl volume]
+ -[SHSAudioPlayback currentPreview]
+ -[SHSAudioPlayback isPlayingRingtoneOrAlarmPreview]
+ -[SHSAudioPlayback isPlayingSystemSoundsPreview]
+ -[SHSAudioPlayback playRingtoneWithIdentifier:loop:forAlertType:]
+ -[SHSAudioPlayback playRingtoneWithIdentifier:loop:forAlertType:].cold.1
+ -[SHSAudioPlayback playSystemSoundPreviewWithIdentifier:loop:volume:]
+ -[SHSAudioPlayback playSystemSoundPreviewWithIdentifier:loop:volume:].cold.1
+ -[SHSAudioPlayback setCurrentPreview:]
+ -[SHSAudioPlayback setSystemSoundsPreview:]
+ -[SHSAudioPlayback systemSoundsPreview]
+ -[SHSSoundsPrefController _alarmControl]
+ -[SHSSoundsPrefController _alarmVolumeSlider]
+ -[SHSSoundsPrefController _alertVolumeSlider]
+ -[SHSSoundsPrefController _attachAlarmSliderTouchHandlers:]
+ -[SHSSoundsPrefController _attachAlertSliderTouchHandlers:]
+ -[SHSSoundsPrefController _reattachTouchHandlersForVisibleVolumeSliders]
+ -[SHSSoundsPrefController _systemSoundsControl]
+ -[SHSSoundsPrefController alarmControl:volumeValueDidChange:]
+ -[SHSSoundsPrefController alarmControlDidObserveEffectiveSystemVolumeChange:]
+ -[SHSSoundsPrefController alarmSliderTouchBegan:]
+ -[SHSSoundsPrefController alarmSliderTouchEnded:]
+ -[SHSSoundsPrefController alarmVolume:]
+ -[SHSSoundsPrefController alertSliderTouchBegan:]
+ -[SHSSoundsPrefController alertSliderTouchEnded:]
+ -[SHSSoundsPrefController alertVolume:]
+ -[SHSSoundsPrefController matchAlarmRingtoneVolume:]
+ -[SHSSoundsPrefController matchRingtoneVolume:]
+ -[SHSSoundsPrefController ringtoneVolume:]
+ -[SHSSoundsPrefController setAlarmVolume:specifier:]
+ -[SHSSoundsPrefController setAlertVolume:specifier:]
+ -[SHSSoundsPrefController setMatchAlarmRingtoneVolume:specifier:]
+ -[SHSSoundsPrefController setMatchRingtoneVolume:specifier:]
+ -[SHSSoundsPrefController setRingtoneVolume:specifier:]
+ -[SHSSoundsPrefController set_alarmControl:]
+ -[SHSSoundsPrefController set_alarmVolumeSlider:]
+ -[SHSSoundsPrefController set_alertVolumeSlider:]
+ -[SHSSoundsPrefController set_systemSoundsControl:]
+ -[SHSSoundsPrefController startSystemSoundVolumePreview]
+ -[SHSSoundsPrefController startVolumePreviewForAlertType:]
+ -[SHSSoundsPrefController systemSoundsControl:volumeValueDidChange:]
+ -[SHSSoundsPrefController systemSoundsControlDidObserveEffectiveSystemVolumeChange:]
+ -[SHSSoundsPrefController viewWillAppear:].cold.1
+ -[SHSSoundsPrefController viewWillDisappear:].cold.1
+ -[SHSSystemSoundsControl .cxx_destruct]
+ -[SHSSystemSoundsControl _handleEffectiveVolumeDidChangeNotification:]
+ -[SHSSystemSoundsControl _handleServerConnectionDiedNotification:]
+ -[SHSSystemSoundsControl _logFaultCalledForBackground]
+ -[SHSSystemSoundsControl _logFaultCalledForInactive]
+ -[SHSSystemSoundsControl _setup]
+ -[SHSSystemSoundsControl _systemController]
+ -[SHSSystemSoundsControl _tearDown]
+ -[SHSSystemSoundsControl _updateVolume:]
+ -[SHSSystemSoundsControl _volumeChangeCoalescingCount]
+ -[SHSSystemSoundsControl _volumeInitialized]
+ -[SHSSystemSoundsControl appWantsVolumeChangeEvents]
+ -[SHSSystemSoundsControl dealloc]
+ -[SHSSystemSoundsControl delegate]
+ -[SHSSystemSoundsControl flushPendingVolumeChanges]
+ -[SHSSystemSoundsControl init]
+ -[SHSSystemSoundsControl reload]
+ -[SHSSystemSoundsControl setAppWantsVolumeChangeEvents:]
+ -[SHSSystemSoundsControl setDelegate:]
+ -[SHSSystemSoundsControl setSystemSoundsVolumeMatchesRingtone:]
+ -[SHSSystemSoundsControl setVolume:]
+ -[SHSSystemSoundsControl set_logFaultCalledForBackground:]
+ -[SHSSystemSoundsControl set_logFaultCalledForInactive:]
+ -[SHSSystemSoundsControl set_systemController:]
+ -[SHSSystemSoundsControl set_volumeChangeCoalescingCount:]
+ -[SHSSystemSoundsControl set_volumeInitialized:]
+ -[SHSSystemSoundsControl systemSoundsVolumeMatchesRingtone]
+ -[SHSSystemSoundsControl volume]
+ GCC_except_table10
+ GCC_except_table19
+ GCC_except_table21
+ GCC_except_table23
+ GCC_except_table8
+ _AVSystemController_EffectiveVolumeNotificationParameter_ActiveAudioCategory
+ _AVSystemController_EffectiveVolumeNotificationParameter_SilenceVolumeHUD
+ _OBJC_CLASS_$_SHSAlarmControl
+ _OBJC_CLASS_$_SHSSystemSoundsControl
+ _OBJC_CLASS_$_TLAlert
+ _OBJC_CLASS_$_TLAlertConfiguration
+ _OBJC_IVAR_$_SHSAlarmControl.__logFaultCalledForBackground
+ _OBJC_IVAR_$_SHSAlarmControl.__logFaultCalledForInactive
+ _OBJC_IVAR_$_SHSAlarmControl.__systemController
+ _OBJC_IVAR_$_SHSAlarmControl.__volumeChangeCoalescingCount
+ _OBJC_IVAR_$_SHSAlarmControl.__volumeInitialized
+ _OBJC_IVAR_$_SHSAlarmControl._appWantsVolumeChangeEvents
+ _OBJC_IVAR_$_SHSAlarmControl._delegate
+ _OBJC_IVAR_$_SHSAlarmControl._volume
+ _OBJC_IVAR_$_SHSAlarmControl._volumeFlushGeneration
+ _OBJC_IVAR_$_SHSAudioPlayback._currentPreview
+ _OBJC_IVAR_$_SHSAudioPlayback._systemSoundsPreview
+ _OBJC_IVAR_$_SHSSoundsPrefController.__alarmControl
+ _OBJC_IVAR_$_SHSSoundsPrefController.__alarmVolumeSlider
+ _OBJC_IVAR_$_SHSSoundsPrefController.__alertVolumeSlider
+ _OBJC_IVAR_$_SHSSoundsPrefController.__systemSoundsControl
+ _OBJC_IVAR_$_SHSSoundsPrefController._currentPreviewAlertType
+ _OBJC_IVAR_$_SHSSystemSoundsControl.__logFaultCalledForBackground
+ _OBJC_IVAR_$_SHSSystemSoundsControl.__logFaultCalledForInactive
+ _OBJC_IVAR_$_SHSSystemSoundsControl.__systemController
+ _OBJC_IVAR_$_SHSSystemSoundsControl.__volumeChangeCoalescingCount
+ _OBJC_IVAR_$_SHSSystemSoundsControl.__volumeInitialized
+ _OBJC_IVAR_$_SHSSystemSoundsControl._appWantsVolumeChangeEvents
+ _OBJC_IVAR_$_SHSSystemSoundsControl._delegate
+ _OBJC_IVAR_$_SHSSystemSoundsControl._volume
+ _OBJC_IVAR_$_SHSSystemSoundsControl._volumeFlushGeneration
+ _OBJC_METACLASS_$_SHSAlarmControl
+ _OBJC_METACLASS_$_SHSSystemSoundsControl
+ __OBJC_$_INSTANCE_METHODS_SHSAlarmControl
+ __OBJC_$_INSTANCE_METHODS_SHSSystemSoundsControl
+ __OBJC_$_INSTANCE_VARIABLES_SHSAlarmControl
+ __OBJC_$_INSTANCE_VARIABLES_SHSSystemSoundsControl
+ __OBJC_$_PROP_LIST_SHSAlarmControl
+ __OBJC_$_PROP_LIST_SHSSystemSoundsControl
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SHSAlarmControlDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SHSSystemSoundsControlDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SHSAlarmControlDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SHSSystemSoundsControlDelegate
+ __OBJC_$_PROTOCOL_REFS_SHSAlarmControlDelegate
+ __OBJC_$_PROTOCOL_REFS_SHSSystemSoundsControlDelegate
+ __OBJC_CLASS_RO_$_SHSAlarmControl
+ __OBJC_CLASS_RO_$_SHSSystemSoundsControl
+ __OBJC_LABEL_PROTOCOL_$_SHSAlarmControlDelegate
+ __OBJC_LABEL_PROTOCOL_$_SHSSystemSoundsControlDelegate
+ __OBJC_METACLASS_RO_$_SHSAlarmControl
+ __OBJC_METACLASS_RO_$_SHSSystemSoundsControl
+ __OBJC_PROTOCOL_$_SHSAlarmControlDelegate
+ __OBJC_PROTOCOL_$_SHSSystemSoundsControlDelegate
+ ___25-[SHSAlarmControl _setup]_block_invoke
+ ___25-[SHSAlarmControl reload]_block_invoke
+ ___26-[SHSAlarmControl dealloc]_block_invoke
+ ___28-[SHSAlarmControl _tearDown]_block_invoke
+ ___29-[SHSAlarmControl setVolume:]_block_invoke
+ ___29-[SHSAlarmControl setVolume:]_block_invoke.27
+ ___29-[SHSAlarmControl setVolume:]_block_invoke_2
+ ___32-[SHSSystemSoundsControl _setup]_block_invoke
+ ___32-[SHSSystemSoundsControl reload]_block_invoke
+ ___33-[SHSAlarmControl _updateVolume:]_block_invoke
+ ___33-[SHSSystemSoundsControl dealloc]_block_invoke
+ ___35-[SHSSystemSoundsControl _tearDown]_block_invoke
+ ___36-[SHSSystemSoundsControl setVolume:]_block_invoke
+ ___36-[SHSSystemSoundsControl setVolume:]_block_invoke.27
+ ___36-[SHSSystemSoundsControl setVolume:]_block_invoke_2
+ ___40-[SHSSystemSoundsControl _updateVolume:]_block_invoke
+ ___45-[SHSAlarmControl alarmVolumeMatchesRingtone]_block_invoke
+ ___49-[SHSAlarmControl setAlarmVolumeMatchesRingtone:]_block_invoke
+ ___59-[SHSAlarmControl _handleServerConnectionDiedNotification:]_block_invoke
+ ___59-[SHSSystemSoundsControl systemSoundsVolumeMatchesRingtone]_block_invoke
+ ___63-[SHSAlarmControl _handleEffectiveVolumeDidChangeNotification:]_block_invoke
+ ___63-[SHSSystemSoundsControl setSystemSoundsVolumeMatchesRingtone:]_block_invoke
+ ___66-[SHSSystemSoundsControl _handleServerConnectionDiedNotification:]_block_invoke
+ ___70-[SHSSystemSoundsControl _handleEffectiveVolumeDidChangeNotification:]_block_invoke
+ ___77-[SHSSoundsPrefController alarmControlDidObserveEffectiveSystemVolumeChange:]_block_invoke
+ ___84-[SHSSoundsPrefController systemSoundsControlDidObserveEffectiveSystemVolumeChange:]_block_invoke
+ ___block_descriptor_52_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.43
+ ___swift__destructor
+ ___swift__destructor.24
+ ___swift_closure_destructor
+ ___swift_closure_destructor.11
+ ___swift_closure_destructor.17
+ ___swift_closure_destructor.27
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA4ViewPAAE11buttonStyleyQrqd__AA015PrimitiveButtonG0Rd__lFQOyAA0I0VyACyAA5LabelVyAA6HStackVyAA05TupleD0VyAA4TextV_AA6SpacerVQPGGAA012_ConditionalD0VyACyAeAE10fontWeightyQrAA4FontV0Q0VSgFQOyACyAA5ImageVAA30_EnvironmentKeyWritingModifierVyAZSgGG_Qo_A5_yAA5ColorVSgGGA3_GGAA01_d5ShapeW0VyAA9RectangleVGGG_AA05PlainiG0VQo_AA023AccessibilityAttachmentW0VGAaDHPqd0__AaDHD3_A26_HO_A28_AA0eW0HPyHCHC.22
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA4ViewPAAE20accessibilityElement8childrenQrAA26AccessibilityChildBehaviorV_tFQOyACyAeAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyACyAA6ToggleVyAA5LabelVyAA4TextVACyAA5ImageVAA24_ForegroundStyleModifierVyAA5ColorVGGGGAA022_EnvironmentKeyWritingV0VyAA08AnyShapeU0VSgGG_SbQo_A2_yAA0D10TransitionVGG_Qo_AA0i10AttachmentV0VGAaDHPqd__AaDHD2_A13_HO_A15_AA0eV0HPyHCHC.30
+ _kCoreBrightnessDisplayInfoDisplayBuiltIn_block_invoke.na_once_object_7
+ _kCoreBrightnessDisplayInfoDisplayBuiltIn_block_invoke.na_once_token_7
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_alarmControl
+ _objc_msgSend$_alarmVolumeSlider
+ _objc_msgSend$_alertVolumeSlider
+ _objc_msgSend$_attachAlarmSliderTouchHandlers:
+ _objc_msgSend$_attachAlertSliderTouchHandlers:
+ _objc_msgSend$_reattachTouchHandlersForVisibleVolumeSliders
+ _objc_msgSend$_systemSoundsControl
+ _objc_msgSend$addTarget:action:forControlEvents:
+ _objc_msgSend$alarmControl:volumeValueDidChange:
+ _objc_msgSend$alarmControlDidObserveEffectiveSystemVolumeChange:
+ _objc_msgSend$alarmVolumeMatchesRingtone
+ _objc_msgSend$alertWithConfiguration:
+ _objc_msgSend$attributeForKey:
+ _objc_msgSend$currentPreview
+ _objc_msgSend$flushPendingVolumeChanges
+ _objc_msgSend$initWithType:
+ _objc_msgSend$isPlayingRingtoneOrAlarmPreview
+ _objc_msgSend$isPlayingSystemSoundsPreview
+ _objc_msgSend$playRingtoneWithIdentifier:loop:forAlertType:
+ _objc_msgSend$playSystemSoundPreviewWithIdentifier:loop:volume:
+ _objc_msgSend$removeTarget:action:forControlEvents:
+ _objc_msgSend$setAlarmVolumeMatchesRingtone:
+ _objc_msgSend$setAudioCategory:
+ _objc_msgSend$setCurrentPreview:
+ _objc_msgSend$setForPreview:
+ _objc_msgSend$setShouldRepeat:
+ _objc_msgSend$setSystemSoundsPreview:
+ _objc_msgSend$setSystemSoundsVolumeMatchesRingtone:
+ _objc_msgSend$setToneIdentifier:
+ _objc_msgSend$set_alarmVolumeSlider:
+ _objc_msgSend$set_alertVolumeSlider:
+ _objc_msgSend$startSystemSoundVolumePreview
+ _objc_msgSend$startVolumePreviewForAlertType:
+ _objc_msgSend$stop
+ _objc_msgSend$stopPlayback
+ _objc_msgSend$systemSoundsControl:volumeValueDidChange:
+ _objc_msgSend$systemSoundsControlDidObserveEffectiveSystemVolumeChange:
+ _objc_msgSend$systemSoundsPreview
+ _objc_msgSend$systemSoundsVolumeMatchesRingtone
+ _objc_msgSend$visibleCells
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x4
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x21
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x26
+ _swift_retain_x28
+ _swift_retain_x8
+ _symbolic _____y_____y___________QPGG 7SwiftUI6HStackV AA12TupleContentV AA4TextV AA6SpacerV
+ _symbolic _____y_____y_____yAAy_____y_____y_____y___________QPGG_____yAAy_____yAAy__________y_____SgGG_Qo_ALy_____SgGGAKGG_____y_____GGG______Qo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE11buttonStyleyQrqd__AA015PrimitiveButtonG0Rd__lFQO AA0I0V AA5LabelV AA6HStackV AA05TupleD0V AA4TextV AA6SpacerV AA012_ConditionalD0V AeAE10fontWeightyQrAA4FontV0Q0VSgFQO AA5ImageV AA30_EnvironmentKeyWritingModifierV AX AA5ColorV AA01_d5ShapeW0V AA9RectangleV AA05PlainiG0V AA023AccessibilityAttachmentW0V
+ _symbolic _____y_____y_____y___________QPGG_____y_____y_____yAIy__________y_____SgGG_Qo_AKy_____SgGGAJGG 7SwiftUI5LabelV AA6HStackV AA12TupleContentV AA4TextV AA6SpacerV AA012_ConditionalF0V AA08ModifiedF0V AA4ViewPAAE10fontWeightyQrAA4FontV0M0VSgFQO AA5ImageV AA30_EnvironmentKeyWritingModifierV AT AA5ColorV
+ _symbolic _____y_____y_____y_____y___________QPGG_____yAAy_____yAAy__________y_____SgGG_Qo_AKy_____SgGGAJGG_____y_____GG 7SwiftUI15ModifiedContentV AA5LabelV AA6HStackV AA05TupleD0V AA4TextV AA6SpacerV AA012_ConditionalD0V AA4ViewPAAE10fontWeightyQrAA4FontV0M0VSgFQO AA5ImageV AA30_EnvironmentKeyWritingModifierV AT AA5ColorV AA01_d5ShapeS0V AA9RectangleV
+ _symbolic _____y_____y_____y_____y_____y___________QPGG_____yABy_____yABy__________y_____SgGG_Qo_ALy_____SgGGAKGG_____y_____GGG 7SwiftUI6ButtonV AA15ModifiedContentV AA5LabelV AA6HStackV AA05TupleE0V AA4TextV AA6SpacerV AA012_ConditionalE0V AA4ViewPAAE10fontWeightyQrAA4FontV0N0VSgFQO AA5ImageV AA30_EnvironmentKeyWritingModifierV AV AA5ColorV AA01_e5ShapeT0V AA9RectangleV
+ _symbolic _____y_____y_____y_____y_____y_____y___________QPGG_____yABy_____yABy__________y_____SgGG_Qo_ALy_____SgGGAKGG_____y_____GGG______Qo_ 7SwiftUI4ViewPAAE11buttonStyleyQrqd__AA015PrimitiveButtonE0Rd__lFQO AA0G0V AA15ModifiedContentV AA5LabelV AA6HStackV AA05TupleI0V AA4TextV AA6SpacerV AA012_ConditionalI0V AcAE10fontWeightyQrAA4FontV0Q0VSgFQO AA5ImageV AA30_EnvironmentKeyWritingModifierV AX AA5ColorV AA01_i5ShapeW0V AA9RectangleV AA05PlaingE0V
- -[SHSAudioPlayback _audioSession]
- -[SHSAudioPlayback _currentItem]
- -[SHSAudioPlayback _playerLooper]
- -[SHSAudioPlayback _queuePlayer]
- -[SHSAudioPlayback _serverConnectionDiedToken]
- -[SHSAudioPlayback playRingtoneWithIdentifier:loop:].cold.1
- -[SHSAudioPlayback playRingtoneWithIdentifier:loop:].cold.2
- -[SHSAudioPlayback ringtoneIdentifier]
- -[SHSAudioPlayback setAudioSessionCategory]
- -[SHSAudioPlayback setAudioSessionCategory].cold.1
- -[SHSAudioPlayback setRingtoneIdentifier:]
- -[SHSAudioPlayback set_audioSession:]
- -[SHSAudioPlayback set_currentItem:]
- -[SHSAudioPlayback set_playerLooper:]
- -[SHSAudioPlayback set_queuePlayer:]
- -[SHSAudioPlayback set_serverConnectionDiedToken:]
- -[SHSSoundsPrefController startRingtonePreview]
- GCC_except_table0
- _AVSystemController_SystemVolumeDidChangeNotification
- _CMTimeMake
- _OBJC_CLASS_$_AVPlayerItem
- _OBJC_CLASS_$_AVPlayerLooper
- _OBJC_CLASS_$_AVQueuePlayer
- _OBJC_IVAR_$_SHSAudioPlayback.__audioSession
- _OBJC_IVAR_$_SHSAudioPlayback.__currentItem
- _OBJC_IVAR_$_SHSAudioPlayback.__playerLooper
- _OBJC_IVAR_$_SHSAudioPlayback.__queuePlayer
- _OBJC_IVAR_$_SHSAudioPlayback.__serverConnectionDiedToken
- _OBJC_IVAR_$_SHSAudioPlayback._ringtoneIdentifier
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- ___24-[SHSAudioPlayback init]_block_invoke
- ___44-[SHSAudioPlayback stopRingtoneWithFadeOut:]_block_invoke_2
- ___44-[SHSAudioPlayback stopRingtoneWithFadeOut:]_block_invoke_2.cold.1
- ___52-[SHSAudioPlayback playRingtoneWithIdentifier:loop:]_block_invoke
- ___52-[SHSAudioPlayback playRingtoneWithIdentifier:loop:]_block_invoke.cold.1
- ___block_descriptor_40_e8_32w_e24_v16?0"NSNotification"8lw32l8
- ___block_literal_global.3
- __block_invoke.na_once_object_787
- __block_invoke.na_once_token_787
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_SoundsAndHapticsSettings
- _get_witness_table 7SwiftUI15ModifiedContentVyAA4ViewPAAE11buttonStyleyQrqd__AA015PrimitiveButtonG0Rd__lFQOyAA0I0VyACyAA5LabelVyAA6HStackVyAA05TupleE0VyAA4TextV_AA6SpacerVtGGAA012_ConditionalD0VyACyAeAE10fontWeightyQrAA4FontV0Q0VSgFQOyACyAA5ImageVAA30_EnvironmentKeyWritingModifierVyAZSgGG_Qo_A5_yAA5ColorVSgGGA3_GGAA01_d5ShapeW0VyAA9RectangleVGGG_AA05PlainiG0VQo_AA023AccessibilityAttachmentW0VGAaDHPqd0__AaDHD3_A26_HO_A28_AA0eW0HPyHCHC.22
- _get_witness_table 7SwiftUI15ModifiedContentVyAA4ViewPAAE20accessibilityElement8childrenQrAA26AccessibilityChildBehaviorV_tFQOyACyAeAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyACyAA6ToggleVyAA5LabelVyAA4TextVACyAA5ImageVAA24_ForegroundStyleModifierVyAA5ColorVGGGGAA022_EnvironmentKeyWritingV0VyAA08AnyShapeU0VSgGG_SbQo_A2_yAA0D10TransitionVGG_Qo_AA0i10AttachmentV0VGAaDHPqd__AaDHD2_A13_HO_A15_AA0eV0HPyHCHC.31
- _objc_msgSend$_audioSession
- _objc_msgSend$_currentItem
- _objc_msgSend$_playerLooper
- _objc_msgSend$_queuePlayer
- _objc_msgSend$addObserverForName:object:queue:usingBlock:
- _objc_msgSend$canInsertItem:afterItem:
- _objc_msgSend$cancelPreviousPerformRequestsWithTarget:
- _objc_msgSend$disableLooping
- _objc_msgSend$filePathForToneIdentifier:
- _objc_msgSend$fileURLWithPath:
- _objc_msgSend$insertItem:afterItem:
- _objc_msgSend$isPlayingRingtone
- _objc_msgSend$pause
- _objc_msgSend$playerItemWithURL:
- _objc_msgSend$playerLooperWithPlayer:templateItem:
- _objc_msgSend$rate
- _objc_msgSend$removeAllItems
- _objc_msgSend$ringtoneIdentifier
- _objc_msgSend$setActive:error:
- _objc_msgSend$setAudioSessionCategory
- _objc_msgSend$setRate:withVolumeRampDuration:
- _objc_msgSend$setRingtoneIdentifier:
- _objc_msgSend$set_audioSession:
- _objc_msgSend$set_currentItem:
- _objc_msgSend$set_playerLooper:
- _objc_msgSend$set_queuePlayer:
- _objc_msgSend$startRingtonePreview
- _objc_retain_x23
- _symbolic _____y_____y___________tGG 7SwiftUI6HStackV AA9TupleViewV AA4TextV AA6SpacerV
- _symbolic _____y_____y_____yAAy_____y_____y_____y___________tGG_____yAAy_____yAAy__________y_____SgGG_Qo_ALy_____SgGGAKGG_____y_____GGG______Qo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE11buttonStyleyQrqd__AA015PrimitiveButtonG0Rd__lFQO AA0I0V AA5LabelV AA6HStackV AA05TupleE0V AA4TextV AA6SpacerV AA012_ConditionalD0V AeAE10fontWeightyQrAA4FontV0Q0VSgFQO AA5ImageV AA30_EnvironmentKeyWritingModifierV AX AA5ColorV AA01_d5ShapeW0V AA9RectangleV AA05PlainiG0V AA023AccessibilityAttachmentW0V
- _symbolic _____y_____y_____y___________tGG_____y_____y_____yAIy__________y_____SgGG_Qo_AKy_____SgGGAJGG 7SwiftUI5LabelV AA6HStackV AA9TupleViewV AA4TextV AA6SpacerV AA19_ConditionalContentV AA08ModifiedJ0V AA0F0PAAE10fontWeightyQrAA4FontV0M0VSgFQO AA5ImageV AA30_EnvironmentKeyWritingModifierV AT AA5ColorV
- _symbolic _____y_____y_____y_____y___________tGG_____yAAy_____yAAy__________y_____SgGG_Qo_AKy_____SgGGAJGG_____y_____GG 7SwiftUI15ModifiedContentV AA5LabelV AA6HStackV AA9TupleViewV AA4TextV AA6SpacerV AA012_ConditionalD0V AA0H0PAAE10fontWeightyQrAA4FontV0M0VSgFQO AA5ImageV AA30_EnvironmentKeyWritingModifierV AT AA5ColorV AA01_d5ShapeS0V AA9RectangleV
- _symbolic _____y_____y_____y_____y_____y___________tGG_____yABy_____yABy__________y_____SgGG_Qo_ALy_____SgGGAKGG_____y_____GGG 7SwiftUI6ButtonV AA15ModifiedContentV AA5LabelV AA6HStackV AA9TupleViewV AA4TextV AA6SpacerV AA012_ConditionalE0V AA0I0PAAE10fontWeightyQrAA4FontV0N0VSgFQO AA5ImageV AA30_EnvironmentKeyWritingModifierV AV AA5ColorV AA01_e5ShapeT0V AA9RectangleV
- _symbolic _____y_____y_____y_____y_____y_____y___________tGG_____yABy_____yABy__________y_____SgGG_Qo_ALy_____SgGGAKGG_____y_____GGG______Qo_ 7SwiftUI4ViewPAAE11buttonStyleyQrqd__AA015PrimitiveButtonE0Rd__lFQO AA0G0V AA15ModifiedContentV AA5LabelV AA6HStackV AA05TupleC0V AA4TextV AA6SpacerV AA012_ConditionalI0V AcAE10fontWeightyQrAA4FontV0Q0VSgFQO AA5ImageV AA30_EnvironmentKeyWritingModifierV AX AA5ColorV AA01_i5ShapeW0V AA9RectangleV AA05PlaingE0V
CStrings:
+ "%s: Alarm slider touch began at volume: %f"
+ "%s: Alarm slider touch ended at volume: %f"
+ "%s: Alarm volume is following ringtone, suppressing preview."
+ "%s: Alert slider touch began at volume: %f"
+ "%s: Alert slider touch ended at volume: %f"
+ "%s: Calling '%{public}@' delegate %{public}@ (ActiveCategory='%{public}@', Category='%{public}@')."
+ "%s: Could not deactivate audio session (may already be inactive): %{public}@"
+ "%s: Cross-category notification detected (ActiveCategory='%{public}@', Category='%{public}@'), suppressing delegate callback."
+ "%s: Failed to create TLAlert for alertType=%{public}@"
+ "%s: Failed to create TLAlert for system sounds preview with identifier '%{public}@'"
+ "%s: Failed to set audio session category to '%{public}@' with error '%{public}@'."
+ "%s: Flushing pending volume changes, current volume: %f"
+ "%s: Full notification userInfo: %@"
+ "%s: Is volume change '%{public}@', is alarm category '%{public}@', category '%{public}@'."
+ "%s: Is volume change '%{public}@', is system sounds category '%{public}@', category '%{public}@'."
+ "%s: Registered touch handlers for alarm volume slider"
+ "%s: Registered touch handlers for alert volume slider"
+ "%s: Removed touch handlers for alarm volume slider"
+ "%s: Removed touch handlers for alert volume slider"
+ "%s: Removed touch-end handlers for alert volume slider (matching enabled)"
+ "%s: Retrieved AVSystemController alarm volume: %f."
+ "%s: Retrieved AVSystemController system sounds volume: %f."
+ "%s: Retrieved matching state from AVSystemController: %{public}@."
+ "%s: Set audio session category to '%{public}@' (not yet active)."
+ "%s: Set matching state in AVSystemController to: %{public}@."
+ "%s: Setting AVSystemController alarm volume to: %f."
+ "%s: Setting AVSystemController system sounds volume to: %f."
+ "%s: SilenceVolumeHUD='%@', ActiveAudioCategory='%{public}@'"
+ "%s: Skipping final preview - initial preview still playing"
+ "%s: Start (setting to %{public}@)."
+ "%s: System sounds volume is following ringtone, suppressing preview."
+ "%s: alertType=%{public}@"
+ "%s: identifier: '%{public}@', loop '%{public}@', alertType '%{public}@'."
+ "%s: identifier: '%{public}@', loop '%{public}@', volume '%{public}f' (ignored - using system volume)."
+ "-[SHSAlarmControl _handleEffectiveVolumeDidChangeNotification:]"
+ "-[SHSAlarmControl _handleEffectiveVolumeDidChangeNotification:]_block_invoke"
+ "-[SHSAlarmControl _handleServerConnectionDiedNotification:]"
+ "-[SHSAlarmControl _handleServerConnectionDiedNotification:]_block_invoke"
+ "-[SHSAlarmControl _setup]"
+ "-[SHSAlarmControl _setup]_block_invoke"
+ "-[SHSAlarmControl _tearDown]"
+ "-[SHSAlarmControl _tearDown]_block_invoke"
+ "-[SHSAlarmControl _updateVolume:]"
+ "-[SHSAlarmControl _updateVolume:]_block_invoke"
+ "-[SHSAlarmControl alarmVolumeMatchesRingtone]"
+ "-[SHSAlarmControl alarmVolumeMatchesRingtone]_block_invoke"
+ "-[SHSAlarmControl dealloc]"
+ "-[SHSAlarmControl dealloc]_block_invoke"
+ "-[SHSAlarmControl flushPendingVolumeChanges]"
+ "-[SHSAlarmControl reload]"
+ "-[SHSAlarmControl reload]_block_invoke"
+ "-[SHSAlarmControl setAlarmVolumeMatchesRingtone:]"
+ "-[SHSAlarmControl setAlarmVolumeMatchesRingtone:]_block_invoke"
+ "-[SHSAlarmControl setVolume:]"
+ "-[SHSAlarmControl setVolume:]_block_invoke"
+ "-[SHSAlarmControl setVolume:]_block_invoke_2"
+ "-[SHSAudioPlayback playRingtoneWithIdentifier:loop:forAlertType:]"
+ "-[SHSAudioPlayback playSystemSoundPreviewWithIdentifier:loop:volume:]"
+ "-[SHSSoundsPrefController _attachAlarmSliderTouchHandlers:]"
+ "-[SHSSoundsPrefController _attachAlertSliderTouchHandlers:]"
+ "-[SHSSoundsPrefController alarmControlDidObserveEffectiveSystemVolumeChange:]"
+ "-[SHSSoundsPrefController alarmSliderTouchBegan:]"
+ "-[SHSSoundsPrefController alarmSliderTouchEnded:]"
+ "-[SHSSoundsPrefController alertSliderTouchBegan:]"
+ "-[SHSSoundsPrefController alertSliderTouchEnded:]"
+ "-[SHSSoundsPrefController setMatchRingtoneVolume:specifier:]"
+ "-[SHSSoundsPrefController startSystemSoundVolumePreview]"
+ "-[SHSSoundsPrefController startVolumePreviewForAlertType:]"
+ "-[SHSSoundsPrefController systemSoundsControlDidObserveEffectiveSystemVolumeChange:]"
+ "-[SHSSoundsPrefController tableView:didEndDisplayingCell:forRowAtIndexPath:]"
+ "-[SHSSoundsPrefController viewWillAppear:]"
+ "-[SHSSystemSoundsControl _handleEffectiveVolumeDidChangeNotification:]"
+ "-[SHSSystemSoundsControl _handleEffectiveVolumeDidChangeNotification:]_block_invoke"
+ "-[SHSSystemSoundsControl _handleServerConnectionDiedNotification:]"
+ "-[SHSSystemSoundsControl _handleServerConnectionDiedNotification:]_block_invoke"
+ "-[SHSSystemSoundsControl _setup]"
+ "-[SHSSystemSoundsControl _setup]_block_invoke"
+ "-[SHSSystemSoundsControl _tearDown]"
+ "-[SHSSystemSoundsControl _tearDown]_block_invoke"
+ "-[SHSSystemSoundsControl _updateVolume:]"
+ "-[SHSSystemSoundsControl _updateVolume:]_block_invoke"
+ "-[SHSSystemSoundsControl dealloc]"
+ "-[SHSSystemSoundsControl dealloc]_block_invoke"
+ "-[SHSSystemSoundsControl flushPendingVolumeChanges]"
+ "-[SHSSystemSoundsControl reload]"
+ "-[SHSSystemSoundsControl reload]_block_invoke"
+ "-[SHSSystemSoundsControl setSystemSoundsVolumeMatchesRingtone:]"
+ "-[SHSSystemSoundsControl setSystemSoundsVolumeMatchesRingtone:]_block_invoke"
+ "-[SHSSystemSoundsControl setVolume:]"
+ "-[SHSSystemSoundsControl setVolume:]_block_invoke"
+ "-[SHSSystemSoundsControl setVolume:]_block_invoke_2"
+ "-[SHSSystemSoundsControl systemSoundsVolumeMatchesRingtone]"
+ "-[SHSSystemSoundsControl systemSoundsVolumeMatchesRingtone]_block_invoke"
+ "1"
+ "ALARM_TIMER_GROUP"
+ "ALARM_TIMER_VOLUME"
+ "ALARM_TIMER_VOLUME_FOOTER"
+ "ALARM_VOLUME_SLIDER"
+ "ALERT_NOTIFICATION_GROUP"
+ "ALERT_NOTIFICATION_VOLUME"
+ "ALERT_NOTIFICATION_VOLUME_FOOTER"
+ "ALERT_VOLUME_SLIDER"
+ "Alarm"
+ "DeviceSupportsClosedLoopHaptics"
+ "IndependentVolumeControls"
+ "IsAlarmVolumeFollowingRingtoneVolumeAttribute"
+ "IsSystemSoundsAndHapticsVolumeFollowingRingtoneVolumeAttribute"
+ "RINGER_AND_ALERTS"
+ "RINGER_AND_ALERTS_GROUP"
+ "RINGTONE"
+ "RINGTONE_HAPTICS"
+ "RINGTONE_VOL_CANNOT_BE_ADJUSTED"
+ "SOUNDS_ALERT_GROUP"
+ "SystemSoundsAndHaptics"
+ "\xf2"
- "#16@0:8"
- "$__lazy_storage_$_hapticsOptionsViewModel"
- "%s: 'Change with Buttons' is not active, ignoring."
- "%s: Activating audio session prior to playback."
- "%s: Deactivating Audio Session."
- "%s: Failed to activate audio session with error '%{public}@'."
- "%s: Failed to set the audio session category to '%{public}@' with error '%{public}@'."
- "%s: Player could not insert item."
- "%s: Requesting playback of current ringtone for alert type '%{public}@'."
- "%s: Setting audio session category '%{public}@'."
- "%s: identifier: '%{public}@', loop '%{public}@'."
- "-[SHSAudioPlayback playRingtoneWithIdentifier:loop:]"
- "-[SHSAudioPlayback playRingtoneWithIdentifier:loop:]_block_invoke"
- "-[SHSAudioPlayback setAudioSessionCategory]"
- "-[SHSAudioPlayback stopRingtoneWithFadeOut:]_block_invoke"
- "-[SHSAudioPlayback stopRingtoneWithFadeOut:]_block_invoke_2"
- "-[SHSSoundsPrefController startRingtonePreview]"
- ".cxx_destruct"
- "@"
- "@\"<SHSRingerControlDelegate>\""
- "@\"ADASManager\""
- "@\"AVAudioSession\""
- "@\"AVPlayerItem\""
- "@\"AVPlayerLooper\""
- "@\"AVQueuePlayer\""
- "@\"AVSystemController\""
- "@\"CoreTelephonyClient\""
- "@\"HKHealthStore\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"40@0:8@\"UITextView\"16{_NSRange=QQ}24"
- "@\"NSNumber\""
- "@\"NSNumberFormatter\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"PSSpecifier\""
- "@\"SHSAudioPlayback\""
- "@\"SHSBadgeView\""
- "@\"SHSDualSIMToneTitleView\""
- "@\"SHSRingerControl\""
- "@\"TKTonePickerViewController\""
- "@\"TKVibrationPickerViewController\""
- "@\"UIAction\"40@0:8@\"UITextView\"16@\"UITextItem\"24@\"UIAction\"32"
- "@\"UILabel\""
- "@\"UIMenu\"40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSArray\"32"
- "@\"UIMenu\"48@0:8@\"UITextView\"16{_NSRange=QQ}24@\"NSArray\"40"
- "@\"UIScrollView\""
- "@\"UIStackView\""
- "@\"UITextItemMenuConfiguration\"40@0:8@\"UITextView\"16@\"UITextItem\"24@\"UIMenu\"32"
- "@\"UIView\""
- "@\"UIView\"24@0:8@\"UIScrollView\"16"
- "@\"UIView<PSHeaderFooterView>\"24@0:8@\"PSSpecifier\"16"
- "@\"UIViewController\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8q16@24"
- "@36@0:8@16@24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16{_NSRange=QQ}24"
- "@40@0:8q16@24@32"
- "@48@0:8@16{_NSRange=QQ}24@40"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIScrollView\"16"
- "B24@0:8@\"UITextView\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "B40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSString\"32"
- "B40@0:8@16@24@32"
- "B48@0:8@\"UITextView\"16@\"NSTextAttachment\"24{_NSRange=QQ}32"
- "B48@0:8@\"UITextView\"16@\"NSURL\"24{_NSRange=QQ}32"
- "B48@0:8@\"UITextView\"16{_NSRange=QQ}24@\"NSString\"40"
- "B48@0:8@16@24{_NSRange=QQ}32"
- "B48@0:8@16{_NSRange=QQ}24@40"
- "B56@0:8@\"UITextView\"16@\"NSTextAttachment\"24{_NSRange=QQ}32q48"
- "B56@0:8@\"UITextView\"16@\"NSURL\"24{_NSRange=QQ}32q48"
- "B56@0:8@16@24{_NSRange=QQ}32q48"
- "CoreTelephonyClientCarrierBundleDelegate"
- "DeviceInRetailKioskMode"
- "DeviceiPad"
- "DeviceiPod"
- "HAPTICS"
- "NSObject"
- "PSHeaderFooterView"
- "PSListControllerTestableSpecifiers"
- "Q16@0:8"
- "Q20@0:8B16"
- "RINGER_AND_ALERT_GROUP"
- "SHSAnalytics"
- "SHSAudioPlayback"
- "SHSBadgeView"
- "SHSCrownVolumeControlEnabledTelemetryEvent"
- "SHSDualSIMListCell"
- "SHSDualSIMListController"
- "SHSDualSIMToneController"
- "SHSDualSIMToneHelper"
- "SHSDualSIMToneTitleView"
- "SHSHeadphoneAudioAccessoriesController"
- "SHSHeadphoneHearingProtectionController"
- "SHSHeadphoneLevelLimitDescriptionCell"
- "SHSHeadphoneLevelLimitSliderCell"
- "SHSHeadphoneNotificationTableCell"
- "SHSHeadphoneNotificationsController"
- "SHSKeyboardClicksControllerViewController"
- "SHSNavigationComponents"
- "SHSRingSilentFooter"
- "SHSRingerControl"
- "SHSRingerControlDelegate"
- "SHSSoundsPrefController"
- "SHSToneController"
- "T#,R"
- "T@\"<SHSRingerControlDelegate>\",W,N,V_delegate"
- "T@\"ADASManager\",&,N,V_audioSettingsManager"
- "T@\"AVAudioSession\",&,N,V__audioSession"
- "T@\"AVPlayerItem\",&,N,V__currentItem"
- "T@\"AVPlayerLooper\",&,N,V__playerLooper"
- "T@\"AVQueuePlayer\",&,N,V__queuePlayer"
- "T@\"AVSystemController\",&,N,V__systemController"
- "T@\"CoreTelephonyClient\",&,N,V__client"
- "T@\"HKHealthStore\",&,N,V_healthStore"
- "T@\"NSArray\",&,N,V_weeklyNotificationData"
- "T@\"NSNumber\",&,N,V__cachedShouldHideValue"
- "T@\"NSNumber\",&,N,V_levelLimitThreshold"
- "T@\"NSNumberFormatter\",&,N,V_numberFormatter"
- "T@\"NSString\",&,N,V_ringtoneIdentifier"
- "T@\"NSString\",&,N,V_topic"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N"
- "T@\"NSString\",R"
- "T@\"NSString\",R,C"
- "T@\"PSSpecifier\",&,N,V__audioGroupSpecifier"
- "T@\"PSSpecifier\",&,N,V__headphoneLevelLimitingSpecifier"
- "T@\"PSSpecifier\",&,N,V__voiceMailSpecifier"
- "T@\"SHSAudioPlayback\",&,N,V__audioPlayback"
- "T@\"SHSBadgeView\",&,N,V_badgeView"
- "T@\"SHSBadgeView\",&,N,V_centeredBadgeView"
- "T@\"SHSDualSIMToneTitleView\",&,N,V_titleView"
- "T@\"SHSRingerControl\",&,N,V__ringerControl"
- "T@\"TKTonePickerViewController\",&,N,V_tonePickerViewController"
- "T@\"TKVibrationPickerViewController\",&,N,V_vibrationPickerViewController"
- "T@\"UILabel\",&,N,V_badgeLabel"
- "T@\"UILabel\",&,N,V_centeredNameLabel"
- "T@\"UILabel\",&,N,V_detailToneTextLabel"
- "T@\"UILabel\",&,N,V_nameLabel"
- "T@\"UILabel\",&,N,V_numberLabel"
- "T@\"UILabel\",&,N,V_titleLabel"
- "T@\"UIScrollView\",&,N,V_scrollView"
- "T@\"UIStackView\",&,N,V_stackView"
- "T@\"UIView\",&,N,V_descriptionLabel"
- "T@\"_NSLocalizedStringResource\",R,C,N"
- "T@\"_TtC24SoundsAndHapticsSettings31HeadphoneAudioNotificationModel\",N,R"
- "T@,&,N,V__serverConnectionDiedToken"
- "TB,N"
- "TB,N,G_isVolumeSliderVisible,V__volumeSliderVisible"
- "TB,N,GisDeviceInRetailKioskMode,V_DeviceInRetailKioskMode"
- "TB,N,GisDeviceiPad,V_DeviceiPad"
- "TB,N,GisDeviceiPod,V_DeviceiPod"
- "TB,N,V__logFaultCalledForBackground"
- "TB,N,V__logFaultCalledForInactive"
- "TB,N,V__volumeInitialized"
- "TB,N,V_appWantsVolumeChangeEvents"
- "TB,N,V_hasDifferentTones"
- "TB,N,V_isDefaultSIMLineController"
- "TB,R,N"
- "TB,R,N,V_shouldShowHeadphoneNotificationsSection"
- "TKTonePickerViewControllerDelegate"
- "TKVibrationPickerViewControllerDelegate"
- "TQ,R"
- "Td,N,V_baseline"
- "Td,N,V_cornerRadius"
- "Td,N,V_fontSize"
- "Td,N,V_minPadding"
- "Tf,N,V_volume"
- "Ti,N,V_weeklyNotificationCount"
- "Tq,N,V__voiceMailSpecifierIndex"
- "Tq,N,V__volumeChangeCoalescingCount"
- "Tq,N,V_alertType"
- "UIScrollViewDelegate"
- "UITextViewDelegate"
- "URLWithString:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_$observationRegistrar"
- "_DeviceInRetailKioskMode"
- "_DeviceiPad"
- "_DeviceiPod"
- "_TtC24SoundsAndHapticsSettings22SHSSilentModeTableCell"
- "_TtC24SoundsAndHapticsSettings24SHSViewControllerFactory"
- "_TtC24SoundsAndHapticsSettings26SHSHapticsOptionsViewModel"
- "_TtC24SoundsAndHapticsSettings31HeadphoneAudioNotificationModel"
- "_TtC24SoundsAndHapticsSettings31SHSHapticsOptionsViewController"
- "_TtC24SoundsAndHapticsSettings33HeadphoneNotificationChartFactory"
- "_TtC24SoundsAndHapticsSettingsP33_0556572A3F538935E22F6FDC453FEDF438SHSSilentModeTableCellContentViewModel"
- "_TtC24SoundsAndHapticsSettingsP33_BA36E6B266DEB43A86F52B82F3EDD6AF19ResourceBundleClass"
- "_TtP24SoundsAndHapticsSettings29SHSHapticsOptionsViewDelegate_"
- "__audioGroupSpecifier"
- "__audioPlayback"
- "__audioSession"
- "__cachedShouldHideValue"
- "__client"
- "__currentItem"
- "__headphoneLevelLimitingSpecifier"
- "__logFaultCalledForBackground"
- "__logFaultCalledForInactive"
- "__playerLooper"
- "__queuePlayer"
- "__ringerControl"
- "__serverConnectionDiedToken"
- "__systemController"
- "__voiceMailSpecifier"
- "__voiceMailSpecifierIndex"
- "__volumeChangeCoalescingCount"
- "__volumeInitialized"
- "__volumeSliderVisible"
- "_alertType"
- "_appWantsVolumeChangeEvents"
- "_audioGroupSpecifier"
- "_audioPlayback"
- "_audioSession"
- "_audioSettingsManager"
- "_badgeLabel"
- "_badgeView"
- "_baseline"
- "_cachedShouldHideValue"
- "_centeredBadgeView"
- "_centeredNameLabel"
- "_client"
- "_constraints"
- "_cornerRadius"
- "_countLabel"
- "_currentItem"
- "_data"
- "_defaultToneIdentifierForTonePickerWithAlertType:topic:"
- "_defaultVibrationIdentifierForVibrationPickerWithAlertType:topic:"
- "_delegate"
- "_descriptionLabel"
- "_detailToneTextLabel"
- "_deviceType"
- "_feedbackSupportLevel"
- "_fontSize"
- "_handleAlertOverridePolicyDidChangeNotification:"
- "_handleEffectiveVolumeDidChangeNotification:"
- "_handleServerConnectionDiedNotification:"
- "_hapticValue:"
- "_hasDifferentTones"
- "_hasTelephony"
- "_headphoneLevelLimitingSpecifier"
- "_healthStore"
- "_hostingController"
- "_initWithAlertType:tableViewStyle:"
- "_insertTonePickerView"
- "_isDefaultSIMLineController"
- "_isKeyHapticsSupported"
- "_isOn"
- "_isVolumeSliderVisible"
- "_keyboardClicksTitle:"
- "_keyboardFeedbackSpecifier"
- "_levelLimitThreshold"
- "_logFaultCalledForBackground"
- "_logFaultCalledForInactive"
- "_maxValueView"
- "_minPadding"
- "_minValueView"
- "_nameLabel"
- "_notificationChart"
- "_notificationData"
- "_numberFormatter"
- "_numberLabel"
- "_playerLooper"
- "_preferredFontForTextStyle:variant:"
- "_queuePlayer"
- "_reloadSectionHeaderFooters:withRowAnimation:"
- "_ringerControl"
- "_ringtoneIdentifier"
- "_scrollView"
- "_serverConnectionDiedToken"
- "_setBadge:andLabel:andPhoneNumber:"
- "_setCenteredBadge:andLabel:"
- "_setHapticValue:specifier:"
- "_setHidesShadow:"
- "_setHyphenationFactor:"
- "_setInteractiveTextSelectionDisabled:"
- "_setSectionContentInset:"
- "_setSoundValue:specifier:"
- "_setSystemVolumeHUDEnabled:"
- "_setSystemVolumeHUDEnabled:forAudioCategory:"
- "_setup"
- "_shouldHideChart"
- "_shouldShowHeadphoneNotificationsSection"
- "_specifier"
- "_stackView"
- "_systemController"
- "_tearDown"
- "_titleLabel"
- "_titleView"
- "_tonePickerViewController"
- "_topic"
- "_updateReloadSpecifierInParentController"
- "_updateVolume:"
- "_vibrationPickerViewController"
- "_voiceMailSpecifier"
- "_voiceMailSpecifierIndex"
- "_volume"
- "_volumeChangeCoalescingCount"
- "_volumeHUDsuppressed"
- "_volumeInitialized"
- "_volumeSliderCell"
- "_volumeSliderVisible"
- "_weeklyNotificationCount"
- "_weeklyNotificationData"
- "accessibilityConstraintsWithVariableBindings:metrics:hideChart:"
- "actionWithTitle:style:handler:"
- "activateConstraints:"
- "addAction:"
- "addArrangedSubview:"
- "addAttribute:value:range:"
- "addChildViewController:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "addObserverForName:object:queue:usingBlock:"
- "addSubview:"
- "ageOfToggleForSilentModeOn:"
- "alertControllerWithTitle:message:preferredStyle:"
- "alertTypeSupportsSIMBasedToneCustomization:"
- "altTextColor"
- "appWantsVolumeChangeEvents"
- "appearance"
- "appendAttributedString:"
- "applicationState"
- "areAnimationsEnabled"
- "array"
- "arrayByAddingObjectsFromArray:"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "audioSettingsManager"
- "autorelease"
- "auxiliarySession"
- "availableInputDevices"
- "badgeLabel"
- "badgeView"
- "baseline"
- "beginUpdates"
- "bluetoothSettingsLinkText"
- "boolValue"
- "booleanCapabilitiesToTest"
- "bottomAnchor"
- "bounds"
- "bundleForClass:"
- "bundleURL"
- "canBeChecked"
- "canChangeRingtoneWithButtons"
- "canChangeRingtoneWithButtons:"
- "canInsertItem:afterItem:"
- "canReload"
- "cancelPreviousPerformRequestsWithTarget:"
- "cancelPreviousPerformRequestsWithTarget:selector:object:"
- "capHeight"
- "carrierBundleChange:"
- "categoryTypeForIdentifier:"
- "cellForRowAtIndexPath:"
- "cellReuseIdentifier"
- "cellStyle"
- "cellType"
- "centerXAnchor"
- "centerYAnchor"
- "centeredBadgeView"
- "centeredNameLabel"
- "class"
- "clearColor"
- "combinedDescription"
- "components:fromDate:"
- "components:fromDate:toDate:options:"
- "configurationWithPointSize:"
- "configurationWithPointSize:weight:"
- "confirmForgetAudioAccessoriesAction"
- "conformsToProtocol:"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintEqualToAnchor:multiplier:"
- "constraintEqualToConstant:"
- "constraintEqualToSystemSpacingBelowAnchor:multiplier:"
- "constraintGreaterThanOrEqualToAnchor:"
- "constraintGreaterThanOrEqualToAnchor:constant:"
- "constraintGreaterThanOrEqualToAnchor:multiplier:"
- "constraintGreaterThanOrEqualToConstant:"
- "constraintGreaterThanOrEqualToSystemSpacingAfterAnchor:multiplier:"
- "constraintLessThanOrEqualToAnchor:"
- "constraintsWithVisualFormat:options:metrics:views:"
- "containsObject:"
- "containsSpecifier:"
- "contentSize"
- "contentView"
- "control"
- "copyCarrierBundleValueWithDefault:key:bundleType:error:"
- "cornerRadius"
- "countByEnumeratingWithState:objects:count:"
- "create"
- "createDescriptionLabel"
- "createHapticsOptionsViewController:delegate:"
- "createScrollView"
- "createTitleLabel"
- "currentCalendar"
- "currentDevice"
- "currentLocale"
- "currentToneIdentifierForAlertType:"
- "currentToneIdentifierForAlertType:topic:"
- "currentVibrationIdentifierForAlertType:"
- "currentVibrationIdentifierForAlertType:topic:"
- "d"
- "d16@0:8"
- "d24@0:8d16"
- "d32@0:8d16@\"UITableView\"24"
- "d32@0:8d16@24"
- "dateByAddingComponents:toDate:options:"
- "dateFromComponents:"
- "day"
- "deactivateConstraints:"
- "dealloc"
- "debugDescription"
- "defaultBundleChange"
- "defaultCenter"
- "defaultMetrics"
- "defaultToneIdentifierForAlertType:"
- "defaultToneIdentifierForAlertType:topic:"
- "defaultVibrationIdentifierForAlertType:"
- "defaultVibrationIdentifierForAlertType:topic:"
- "defaultWorkspace"
- "delegate"
- "deleteAllAudioAccessoryData"
- "description"
- "descriptionLabel"
- "descriptionText"
- "detailControllerClass"
- "detailTextForToneWithSpecifier:"
- "detailTextLabel"
- "detailToneTextLabel"
- "deviceID"
- "deviceName"
- "deviceTypeString"
- "dictionaryWithObjects:forKeys:count:"
- "didBackground"
- "didLock"
- "didMoveToParentViewController:"
- "disableLooping"
- "dismiss"
- "dismissViewControllerAnimated:completion:"
- "endDate"
- "endInterruption"
- "endUpdates"
- "executeQuery:"
- "f"
- "f16@0:8"
- "fallbackInputDevice"
- "fetchCTSubscriptionsInUse"
- "fetchLocalizedPhoneNumberForContext:"
- "fetchShortLabelForContext:"
- "filePathForToneIdentifier:"
- "fileURLWithPath:"
- "firstBaselineAnchor"
- "firstObject"
- "floatValue"
- "font"
- "fontDescriptor"
- "fontDescriptorWithSymbolicTraits:"
- "fontSize"
- "fontWithDescriptor:size:"
- "footerHyperlinkColor"
- "frame"
- "getConnectedToHeadphonesEnabled"
- "getFixedVolumeControlsFooterWithSwitch:"
- "getHeadphoneLevelLimitEnabled"
- "getHeadphoneLevelLimitSetting"
- "getHeadphoneNotificationsEnabled"
- "getMicrophoneLabel:"
- "getMobileSubscriberHomeCountryList:error:"
- "getPhoneNumber:error:"
- "getPreferenceFor:"
- "getSelectedHapticsOption"
- "getSelectedHapticsOptionTitleWithSpecifier:"
- "getShortLabel:error:"
- "getSilentMode"
- "getSilentModeFooterWithSwitch:"
- "getSubscriptionInfoWithError:"
- "getVolume:forCategory:"
- "gqDnklGQnpv5ilgh5uHckw"
- "groupSpecifierWithID:"
- "groupSpecifierWithID:name:"
- "handleInputNotification:"
- "handleSilentModeNotification:"
- "hapticsOptionsDidChange:"
- "hasDifferentTones"
- "hasMultipleCTSubscriptionsInUse"
- "hasSpecificDefaultToneIdentifierForAlertType:topic:"
- "hasSpecificDefaultVibrationIdentifierForAlertType:topic:"
- "hasValidGetter"
- "hash"
- "headphoneAudioDevicesSpecifier"
- "headphoneLevelLimitDescriptionSpecifier"
- "headphoneLevelLimitGroupSpecifier"
- "headphoneLevelLimitLockedByRestrictions"
- "headphoneLevelLimitSliderSpecifier"
- "headphoneLevelLimitSwitchSpecifier"
- "headphoneNotificationsGroupSpecifier"
- "headphoneNotificationsSwitchSpecifier"
- "headphoneWeeklyNotificationDescriptionSpecifier"
- "healthLinkText"
- "healthStore"
- "heightAnchor"
- "i16@0:8"
- "identifier"
- "imageWithTintColor:renderingMode:"
- "indexForIndexPath:"
- "indexOfObject:"
- "indexOfSpecifierWithID:"
- "indexPathForSpecifier:"
- "indexSetWithIndex:"
- "indexSetWithIndexesInRange:"
- "init"
- "initWithArrangedSubviews:"
- "initWithArray:"
- "initWithBarButtonSystemItem:target:action:"
- "initWithBundleType:"
- "initWithCalendarIdentifier:"
- "initWithCoder:"
- "initWithDeviceFeatures:"
- "initWithFrame:"
- "initWithKey:ascending:"
- "initWithKey:defaultValue:table:locale:bundleURL:"
- "initWithKey:table:locale:bundleURL:"
- "initWithNibName:bundle:"
- "initWithPath:"
- "initWithSampleType:predicate:limit:sortDescriptors:resultsHandler:"
- "initWithSpecifier:"
- "initWithString:"
- "initWithString:attributes:"
- "initWithStyle:reuseIdentifier:"
- "initWithStyle:reuseIdentifier:specifier:"
- "insertContiguousSpecifiers:afterSpecifierID:animated:"
- "insertItem:afterItem:"
- "insertObject:atIndex:"
- "insertObjects:atIndexes:"
- "insertSpecifier:afterSpecifierID:animated:"
- "insertSpecifier:atIndex:"
- "intValue"
- "integerValue"
- "intrinsicContentSize"
- "isDefaultSIMLineController"
- "isDeviceInRetailKioskMode"
- "isDeviceiPad"
- "isDeviceiPod"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMainThread"
- "isMemberOfClass:"
- "isOn"
- "isPlayingRingtone"
- "isProxy"
- "isSimDataOnly"
- "isSimHidden"
- "isSuspendedUnderLock"
- "isTracking"
- "isViewLoaded"
- "label"
- "labelColor"
- "labelID"
- "lastBaselineAnchor"
- "layer"
- "layoutMargins"
- "layoutMarginsGuide"
- "layoutSubviews"
- "leadingAnchor"
- "length"
- "levelLimitThreshold"
- "linkText:withLink:"
- "loadConstraintsForTitleView"
- "loadSpecifiersFromPlistName:target:"
- "loadView"
- "localizedStringForKey:value:table:"
- "localizedUppercaseString"
- "lowercaseString"
- "minPadding"
- "name"
- "nameForToneIdentifier:"
- "nameLabel"
- "navigationBar"
- "navigationController"
- "navigationItem"
- "newImageView"
- "newTextView"
- "number"
- "numberFormatter"
- "numberLabel"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "opaqueSessionID"
- "openSensitiveURL:withOptions:"
- "openURL:withCompletionHandler:"
- "operatorBundleChange:"
- "parentController"
- "parentViewController"
- "pause"
- "pe_emitNavigationEventForSystemSettingsWithGraphicIconIdentifier:title:localizedNavigationComponents:deepLink:"
- "performGetter"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:afterDelay:"
- "performSelector:withObject:withObject:"
- "performSetterWithValue:"
- "play"
- "playRingtoneWithIdentifier:loop:"
- "playerItemWithURL:"
- "playerLooperWithPlayer:templateItem:"
- "postNotificationName:object:"
- "predicateForSamplesWithStartDate:endDate:options:"
- "preferenceSpecifierNamed:target:set:get:detail:cell:edit:"
- "preferredContentSizeCategory"
- "preferredFontForTextStyle:"
- "preferredHeightForWidth:"
- "preferredHeightForWidth:inTableView:"
- "prepareForReuse"
- "presentHapticsController:"
- "presentViewController:animated:completion:"
- "profileManagementSpecifier"
- "propertyForKey:"
- "q"
- "q16@0:8"
- "queryNotificationCountsFromDate:toDate:"
- "rangeOfString:"
- "rate"
- "readPreferenceValue:"
- "refreshCellContentsWithSpecifier:"
- "refreshContentsWithSpecifier:"
- "refreshShouldHideAllVoicemailUI"
- "registerClass:forCellReuseIdentifier:"
- "regularConstraintsWithVariableBindings:metrics:hideChart:"
- "release"
- "reload"
- "reloadSpecifier:"
- "reloadSpecifierID:"
- "reloadSpecifierID:animated:"
- "reloadSpecifiers"
- "removeAllItems"
- "removeFromParentViewController"
- "removeFromSuperview"
- "removeObject:"
- "removeObserver:"
- "removeObserver:name:object:"
- "removeSpecifier:"
- "removeSpecifierID:"
- "removeSpecifierID:animated:"
- "replaceObjectAtIndex:withObject:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "ringerControl:volumeValueDidChange:"
- "ringerControlDidObserveEffectiveSystemVolumeChange:"
- "ringtoneIdentifier"
- "safeAreaLayoutGuide"
- "scaledFontForFont:"
- "scaledValueForValue:"
- "scheme"
- "scrollView"
- "scrollViewDidChangeAdjustedContentInset:"
- "scrollViewDidEndDecelerating:"
- "scrollViewDidEndDragging:willDecelerate:"
- "scrollViewDidEndScrollingAnimation:"
- "scrollViewDidEndZooming:withView:atScale:"
- "scrollViewDidScroll:"
- "scrollViewDidScrollToTop:"
- "scrollViewDidZoom:"
- "scrollViewShouldScrollToTop:"
- "scrollViewWillBeginDecelerating:"
- "scrollViewWillBeginDragging:"
- "scrollViewWillBeginZooming:withView:"
- "scrollViewWillEndDragging:withVelocity:targetContentOffset:"
- "secondaryLabelColor"
- "section"
- "selectedOption"
- "self"
- "separatorColor"
- "serverDiedNotificationHandler:"
- "setAccessibilityIdentifier:"
- "setAccessoryType:"
- "setActive:"
- "setActive:error:"
- "setActive:withOptions:error:"
- "setAdjustsFontForContentSizeCategory:"
- "setAlertType:"
- "setAlignment:"
- "setAllowsDeletingDefaultVibration:"
- "setAppWantsVolumeChangeEvents:"
- "setAttribute:forKey:error:"
- "setAttributedText:"
- "setAttributes:range:"
- "setAudioSessionCategory"
- "setAudioSessionID:"
- "setAudioSettingsManager:"
- "setAutoresizingMask:"
- "setAxis:"
- "setBackgroundColor:"
- "setBadgeLabel:"
- "setBadgeView:"
- "setBarTintColor:"
- "setBaseline:"
- "setButtonAction:"
- "setCalendar:"
- "setCanChangeRingtoneWithButtons:"
- "setCanChangeRingtoneWithButtons:specifier:"
- "setCategory:error:"
- "setCategory:mode:options:error:"
- "setCenteredBadgeView:"
- "setCenteredNameLabel:"
- "setConnectedToHeadphonesEnabled:forSpecifier:"
- "setContentCompressionResistancePriority:forAxis:"
- "setContentHuggingPriority:forAxis:"
- "setContentInset:"
- "setContentInsetAdjustmentBehavior:"
- "setContentMode:"
- "setContentSize:"
- "setCornerRadius:"
- "setCurrentToneIdentifier:forAlertType:topic:"
- "setCurrentVibrationIdentifier:forAlertType:topic:"
- "setCustomSpacing:afterView:"
- "setData:"
- "setDateFormat:"
- "setDay:"
- "setDefaultToneIdentifier:"
- "setDefaultVibrationIdentifier:"
- "setDelegate:"
- "setDescriptionLabel:"
- "setDetailControllerClass:"
- "setDetailToneTextLabel:"
- "setDeviceInRetailKioskMode:"
- "setDeviceiPad:"
- "setDeviceiPod:"
- "setDiscoveryMode:forClientIdentifiers:"
- "setDistribution:"
- "setEditable:"
- "setFixedVolumeControls:specifier:"
- "setFont:"
- "setFontSize:"
- "setFrame:"
- "setHasDifferentTones:"
- "setHeadphoneLevelLimitEnabled:forSpecifier:"
- "setHeadphoneLevelLimitValue:forSpecifier:"
- "setHeadphoneNotificationsEnabled:forSpecifier:"
- "setHealthStore:"
- "setHidden:"
- "setIdentifier:"
- "setImage:"
- "setIsDefaultSIMLineController:"
- "setItems:"
- "setLateNightMode:specifier:"
- "setLayoutMargins:"
- "setLayoutMarginsRelativeArrangement:"
- "setLevelLimitThreshold:"
- "setLineBreakMode:"
- "setLineFragmentPadding:"
- "setLocale:"
- "setLocalizedDateFormatFromTemplate:"
- "setMasksToBounds:"
- "setMaximumFractionDigits:"
- "setMinPadding:"
- "setMonth:"
- "setName:"
- "setNameLabel:"
- "setNeedsLayout"
- "setNeedsUpdateConstraints"
- "setNoneAtTop:"
- "setNotANumberSymbol:"
- "setNumberFormatter:"
- "setNumberLabel:"
- "setNumberOfLines:"
- "setNumberStyle:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPlayKeyboardSound:specifier:"
- "setPlayLockSound:specifier:"
- "setPreferenceFor:value:"
- "setPreferenceValue:specifier:"
- "setProperty:forKey:"
- "setRate:withVolumeRampDuration:"
- "setRightBarButtonItem:"
- "setRingtoneIdentifier:"
- "setScrollEnabled:"
- "setScrollView:"
- "setSelectable:"
- "setSelectedToneIdentifier:"
- "setSelectionStyle:"
- "setSeparatorStyle:"
- "setShowInStatusBarEnabled:specifier:"
- "setShowsDefault:"
- "setShowsEditButtonInNavigationBar:"
- "setShowsNone:"
- "setShowsUserGenerated:"
- "setShowsVerticalScrollIndicator:"
- "setShowsVibrations:"
- "setSilentMode:untilTime:reason:clientType:"
- "setSilentModeEnabled:specifier:"
- "setSilentModeOff:"
- "setSilentModeOn:"
- "setSoundEffects:specifier:"
- "setSpacing:"
- "setSpecifier:"
- "setStackView:"
- "setSystemHapticsEnabled:specifier:"
- "setTag:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTextContainerInset:"
- "setTintColor:"
- "setTitle:"
- "setTitleLabel:"
- "setTitleView:"
- "setTonePickerViewController:"
- "setTopic:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setTranslucent:"
- "setType:"
- "setUpSilentModeNotifications"
- "setUserInteractionEnabled:"
- "setValue:"
- "setVibrationPickerViewController:"
- "setVisceral:"
- "setVolume:"
- "setVolume:specifier:"
- "setVolumeHUDsuppression:"
- "setVolumeTo:forCategory:"
- "setWeeklyNotificationCount:"
- "setWeeklyNotificationData:"
- "set_audioGroupSpecifier:"
- "set_audioPlayback:"
- "set_audioSession:"
- "set_cachedShouldHideValue:"
- "set_client:"
- "set_currentItem:"
- "set_headphoneLevelLimitingSpecifier:"
- "set_logFaultCalledForBackground:"
- "set_logFaultCalledForInactive:"
- "set_playerLooper:"
- "set_queuePlayer:"
- "set_ringerControl:"
- "set_serverConnectionDiedToken:"
- "set_systemController:"
- "set_voiceMailSpecifier:"
- "set_voiceMailSpecifierIndex:"
- "set_volumeChangeCoalescingCount:"
- "set_volumeInitialized:"
- "set_volumeSliderVisible:"
- "sf_inRetailKioskMode"
- "sf_isiPad"
- "shared"
- "sharedAVSystemController"
- "sharedApplication"
- "sharedInstance"
- "sharedPreferencesController"
- "sharedSystemAudioInputContext"
- "sharedToneManager"
- "sharedVibrationManager"
- "shouldShowHeadphoneNotificationsSection"
- "shouldShowHealthFeatures"
- "shouldShowSIMBasedToneCustomizationForAlertType:"
- "showController:animate:"
- "showInStatusBarEnabled:"
- "shs_localizedPathComponentForTonePickerSpecifier:"
- "shs_rootPaneComponent"
- "silentModeEnabled:"
- "size"
- "sizeThatFits:"
- "soundEffects:"
- "specifier"
- "specifierAtIndex:"
- "specifierForID:"
- "specifiers"
- "stackView"
- "standardUserDefaults"
- "startDate"
- "startOfDayForDate:"
- "startRingtonePreview"
- "stopPlayback"
- "stopRingtoneWithFadeOut:"
- "string"
- "stringByAppendingString:"
- "stringFromDate:"
- "stringFromNumber:"
- "stringValue"
- "stringWithFormat:"
- "subscriptions"
- "subscriptionsInUse"
- "superclass"
- "superview"
- "systemBackgroundColor"
- "systemFontOfSize:"
- "systemGrayColor"
- "systemHapticsEnabled:"
- "systemImageNamed:"
- "systemImageNamed:withConfiguration:"
- "systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:"
- "table"
- "tableView"
- "tableView:cellForRowAtIndexPath:"
- "tableView:didEndDisplayingCell:forRowAtIndexPath:"
- "tertiaryLabelColor"
- "text"
- "textColor"
- "textContainer"
- "textLabel"
- "textSize"
- "textView:didBeginFormattingWithViewController:"
- "textView:didEndFormattingWithViewController:"
- "textView:editMenuForTextInRange:suggestedActions:"
- "textView:editMenuForTextInRanges:suggestedActions:"
- "textView:insertInputSuggestion:"
- "textView:menuConfigurationForTextItem:defaultMenu:"
- "textView:primaryActionForTextItem:defaultAction:"
- "textView:shouldChangeTextInRange:replacementText:"
- "textView:shouldChangeTextInRanges:replacementText:"
- "textView:shouldInteractWithTextAttachment:inRange:"
- "textView:shouldInteractWithTextAttachment:inRange:interaction:"
- "textView:shouldInteractWithURL:inRange:"
- "textView:shouldInteractWithURL:inRange:interaction:"
- "textView:textItemMenuWillDisplayForTextItem:animator:"
- "textView:textItemMenuWillEndForTextItem:animator:"
- "textView:willBeginFormattingWithViewController:"
- "textView:willDismissEditMenuWithAnimator:"
- "textView:willEndFormattingWithViewController:"
- "textView:willPresentEditMenuWithAnimator:"
- "textView:writingToolsIgnoredRangesInEnclosingRange:"
- "textViewDidBeginEditing:"
- "textViewDidChange:"
- "textViewDidChangeSelection:"
- "textViewDidEndEditing:"
- "textViewShouldBeginEditing:"
- "textViewShouldEndEditing:"
- "textViewWritingToolsDidEnd:"
- "textViewWritingToolsWillBegin:"
- "titleLabel"
- "titleText"
- "titleView"
- "toggleContentViewModel"
- "tonePickerViewController"
- "tonePickerViewController:didChangeIgnoreMute:"
- "tonePickerViewController:didDismissVibrationPickerViewController:"
- "tonePickerViewController:requestsPresentingToneClassicsViewController:animated:"
- "tonePickerViewController:requestsPresentingVibrationPickerViewController:animated:"
- "tonePickerViewController:selectedMediaItemWithIdentifier:"
- "tonePickerViewController:selectedToneWithIdentifier:"
- "tonePickerViewController:willPresentVibrationPickerViewController:"
- "topAnchor"
- "topic"
- "trackingDualSIMToneValueChanged:didSelectDifferentTones:"
- "trackingVibrateOnRingValueChanged:age:"
- "trackingVibrateOnSilentValueChanged:age:"
- "trailingAnchor"
- "traitCollection"
- "unregisterSilentModeNotifications"
- "updateConstraints"
- "updateContentsWithTitle:badgeText:"
- "updateDifferentTonesState"
- "updateHeadphoneLevelLimitDescriptionText"
- "updateHeadphoneLevelLimitText"
- "updateMonthlyNotificationCounts:withNames:forDates:"
- "updateSilentModeGroupFooterWithNewValue:"
- "updateVoiceMailVisibility"
- "updateVolume"
- "userDefaultVoice"
- "userInfo"
- "userPreferredInputDevice:"
- "v16@0:8"
- "v16@?0@\"NSNotification\"8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v20@0:8i16"
- "v24@0:8@\"CTXPCServiceSubscriptionContext\"16"
- "v24@0:8@\"PSSpecifier\"16"
- "v24@0:8@\"SHSRingerControl\"16"
- "v24@0:8@\"UIScrollView\"16"
- "v24@0:8@\"UITextView\"16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"SHSRingerControl\"16f24"
- "v28@0:8@\"TKTonePickerViewController\"16B24"
- "v28@0:8@\"UIScrollView\"16B24"
- "v28@0:8@16B24"
- "v28@0:8@16f24"
- "v28@0:8B16Q20"
- "v32@0:8@\"TKTonePickerViewController\"16@\"NSNumber\"24"
- "v32@0:8@\"TKTonePickerViewController\"16@\"NSString\"24"
- "v32@0:8@\"TKTonePickerViewController\"16@\"TKVibrationPickerViewController\"24"
- "v32@0:8@\"TKVibrationPickerViewController\"16@\"NSString\"24"
- "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
- "v32@0:8@\"UITextView\"16@\"<UIEditMenuInteractionAnimating>\"24"
- "v32@0:8@\"UITextView\"16@\"UIInputSuggestion\"24"
- "v32@0:8@\"UITextView\"16@\"UITextFormattingViewController\"24"
- "v32@0:8@16@24"
- "v36@0:8@\"TKTonePickerViewController\"16@\"TKVibrationPickerViewController\"24B32"
- "v36@0:8@\"TKTonePickerViewController\"16@\"UIViewController\"24B32"
- "v36@0:8@16@24B32"
- "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
- "v40@0:8@\"UITextView\"16@\"UITextItem\"24@\"<UIContextMenuInteractionAnimating>\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24d32"
- "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
- "valueForKeyPath:"
- "valueLabel"
- "valueWithNonretainedObject:"
- "vibrationPickerViewController"
- "vibrationPickerViewController:selectedVibrationWithIdentifier:"
- "view"
- "viewDidAppear:"
- "viewDidLoad"
- "viewForZoomingInScrollView:"
- "viewWillAppear:"
- "viewWillDisappear:"
- "visceral"
- "volume"
- "volume:"
- "weeklyNotificationCount"
- "weeklyNotificationCount:"
- "weeklyNotificationData"
- "whiteColor"
- "widthAnchor"
- "willBecomeActive"
- "willForeground"
- "willHideSlider"
- "willMoveToParentViewController:"
- "willResignActive"
- "willShowSlider"
- "window"
- "windowScene"
- "windows"
- "zone"
- "{CGSize=dd}16@0:8"

```
