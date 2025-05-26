## AccessibilityUtilities

> `/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities`

```diff

-3089.1.0.0.0
-  __TEXT.__text: 0xdd030
+3093.2.4.0.2
+  __TEXT.__text: 0xde5ac
   __TEXT.__auth_stubs: 0x3500
-  __TEXT.__objc_methlist: 0xd164
-  __TEXT.__cstring: 0x145d1
-  __TEXT.__const: 0xe0e
-  __TEXT.__gcc_except_tab: 0x1450
+  __TEXT.__objc_methlist: 0xd27c
+  __TEXT.__cstring: 0x14691
+  __TEXT.__const: 0xe5e
+  __TEXT.__gcc_except_tab: 0x145c
   __TEXT.__oslogstring: 0x4493
   __TEXT.__dlopen_cstrs: 0x9ae
   __TEXT.__ustring: 0x68
-  __TEXT.__swift5_typeref: 0x5da
-  __TEXT.__swift5_capture: 0x7ec
-  __TEXT.__swift5_fieldmd: 0x168
-  __TEXT.__constg_swiftt: 0x250
-  __TEXT.__swift5_reflstr: 0x8b
+  __TEXT.__swift5_typeref: 0x604
+  __TEXT.__swift5_capture: 0x804
+  __TEXT.__swift5_fieldmd: 0x1a0
+  __TEXT.__constg_swiftt: 0x288
+  __TEXT.__swift5_reflstr: 0x9b
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_proto: 0x14
-  __TEXT.__swift5_types: 0x28
-  __TEXT.__unwind_info: 0x3dbc
-  __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x11aa
-  __TEXT.__objc_methname: 0x25b6b
-  __TEXT.__objc_methtype: 0x2e3a
-  __TEXT.__objc_stubs: 0x13fe0
-  __DATA_CONST.__got: 0x8c8
-  __DATA_CONST.__const: 0x35e8
-  __DATA_CONST.__objc_classlist: 0x4f0
+  __TEXT.__swift5_types: 0x30
+  __TEXT.__unwind_info: 0x3e50
+  __TEXT.__eh_frame: 0x78
+  __TEXT.__objc_classname: 0x11ca
+  __TEXT.__objc_methname: 0x25b95
+  __TEXT.__objc_methtype: 0x2d85
+  __TEXT.__objc_stubs: 0x14280
+  __DATA_CONST.__got: 0x8c0
+  __DATA_CONST.__const: 0x35e0
+  __DATA_CONST.__objc_classlist: 0x4f8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xdfa0
-  __DATA_CONST.__objc_selrefs: 0x8948
-  __DATA_CONST.__objc_arraydata: 0x698
-  __AUTH_CONST.__const: 0x2ad0
-  __AUTH_CONST.__cfstring: 0x13fe0
-  __AUTH_CONST.__objc_const: 0x4208
+  __DATA_CONST.__objc_const: 0xe1c8
+  __DATA_CONST.__objc_selrefs: 0x89f0
+  __DATA_CONST.__objc_arraydata: 0x6a0
+  __AUTH_CONST.__const: 0x2c58
+  __AUTH_CONST.__cfstring: 0x14100
+  __AUTH_CONST.__objc_const: 0x4250
   __AUTH_CONST.__auth_ptr: 0x50
   __AUTH_CONST.__objc_intobj: 0x1080
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__auth_got: 0x1a90
-  __AUTH.__objc_data: 0x27b0
+  __AUTH.__objc_data: 0x2800
   __AUTH.__data: 0x18
   __DATA.__objc_protorefs: 0x38
-  __DATA.__objc_classrefs: 0x640
+  __DATA.__objc_classrefs: 0x648
   __DATA.__objc_superrefs: 0x2e8
-  __DATA.__objc_ivar: 0xa70
-  __DATA.__data: 0x10a8
-  __DATA.__bss: 0x860
+  __DATA.__objc_ivar: 0xa98
+  __DATA.__data: 0x10b8
+  __DATA.__bss: 0x880
   __DATA.__common: 0x12
   __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__data: 0x1e0
-  __DATA_DIRTY.__bss: 0x500
+  __DATA_DIRTY.__bss: 0x4e8
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6442
-  Symbols:   18793
-  CStrings:  9711
+  Functions: 6504
+  Symbols:   18904
+  CStrings:  9761
 
Symbols:
+ +[AXTripleClickHelpers isReduceWhitePointEnabled]
+ +[AXTripleClickHelpers stateForTripleClickOption:]
+ +[AXTripleClickHelpers toggleHearingControlCenter]
+ -[AXAssistiveTouchServer currentBubbleElement]
+ -[AXEventTapManager _hidFilterListForPair:filterEvents:]
+ -[AXEventTapManager _installEventTap:skipDeviceMatching:filterEvents:]
+ -[AXEventTapManager _installHIDFilter:skipDeviceMatching:filterEvents:]
+ -[AXEventTapManager installEventTap:identifier:type:skipDeviceMatching:filterEvents:matchingServiceHandler:]
+ -[AXEventTapManagerFilterEvents setWantsATVRemoteEvents:]
+ -[AXEventTapManagerFilterEvents setWantsAccessibilityEvents:]
+ -[AXEventTapManagerFilterEvents setWantsDigitizerEvents:]
+ -[AXEventTapManagerFilterEvents setWantsKeyboardEvents:]
+ -[AXEventTapManagerFilterEvents setWantsLisaEvents:]
+ -[AXEventTapManagerFilterEvents setWantsMouseEvents:]
+ -[AXEventTapManagerFilterEvents setWantsStylusEvents:]
+ -[AXEventTapManagerFilterEvents setWantsVolumeButtonEvents:]
+ -[AXEventTapManagerFilterEvents wantsATVRemoteEvents]
+ -[AXEventTapManagerFilterEvents wantsAccessibilityEvents]
+ -[AXEventTapManagerFilterEvents wantsDigitizerEvents]
+ -[AXEventTapManagerFilterEvents wantsKeyboardEvents]
+ -[AXEventTapManagerFilterEvents wantsLisaEvents]
+ -[AXEventTapManagerFilterEvents wantsMouseEvents]
+ -[AXEventTapManagerFilterEvents wantsStylusEvents]
+ -[AXEventTapManagerFilterEvents wantsVolumeButtonEvents]
+ -[AXSwitchControlServer lastSpokenPhrases]
+ -[FKAAvailableCommands _updateCachedSiriShortcutsCommands]
+ -[FKAAvailableCommands cachedSiriShortcutsCommands]
+ -[FKAAvailableCommands setCachedSiriShortcutsCommands:]
+ -[FKAAvailableCommands setSiriShortcutsQueue:]
+ -[FKAAvailableCommands siriShortcutsQueue]
+ -[_NSObject_SwiftObject_SafeSwiftValuesSupport safeSwiftCallAsFunction:]
+ GCC_except_table1006
+ GCC_except_table1007
+ GCC_except_table119
+ GCC_except_table13
+ GCC_except_table39
+ GCC_except_table40
+ GCC_except_table464
+ GCC_except_table467
+ GCC_except_table468
+ GCC_except_table632
+ GCC_except_table690
+ GCC_except_table73
+ GCC_except_table928
+ GCC_except_table932
+ _AXAccessibilityIntentConfiguredActionTemplateParameterKey
+ _AXAssistiveTouchIconTypeActionButton
+ _AXDeviceHasReduceTransparency
+ _AXDeviceHasStaccato
+ _AXDeviceSupportsHaptics
+ _AXDeviceSupportsLiveSpeech
+ _AXDeviceSupportsSonification
+ _AXProcessIsSurfBoard
+ _AXProcessIsSurfBoard._AXProcessIsPineBoardOnceToken
+ _AXProcessIsSurfBoard._AXProcessIsSurfBoard
+ _AXWatchControlEltonLocalizedStringForKey
+ _AX_MuseBuddyBundleName
+ _AX_SurfBoardBundleName
+ _OBJC_CLASS_$_AXEventTapManagerFilterEvents
+ _OBJC_IVAR_$_AXEventTapManagerFilterEvents._wantsATVRemoteEvents
+ _OBJC_IVAR_$_AXEventTapManagerFilterEvents._wantsAccessibilityEvents
+ _OBJC_IVAR_$_AXEventTapManagerFilterEvents._wantsDigitizerEvents
+ _OBJC_IVAR_$_AXEventTapManagerFilterEvents._wantsKeyboardEvents
+ _OBJC_IVAR_$_AXEventTapManagerFilterEvents._wantsLisaEvents
+ _OBJC_IVAR_$_AXEventTapManagerFilterEvents._wantsMouseEvents
+ _OBJC_IVAR_$_AXEventTapManagerFilterEvents._wantsStylusEvents
+ _OBJC_IVAR_$_AXEventTapManagerFilterEvents._wantsVolumeButtonEvents
+ _OBJC_IVAR_$_FKAAvailableCommands._cachedSiriShortcutsCommands
+ _OBJC_IVAR_$_FKAAvailableCommands._siriShortcutsQueue
+ _OBJC_METACLASS_$_AXEventTapManagerFilterEvents
+ __AXSafeSwiftCallAsFunctionForKey
+ __OBJC_$_INSTANCE_METHODS_AXEventTapManagerFilterEvents
+ __OBJC_$_INSTANCE_VARIABLES_AXEventTapManagerFilterEvents
+ __OBJC_$_PROP_LIST_AXEventTapManagerFilterEvents
+ __OBJC_CLASS_RO_$_AXEventTapManagerFilterEvents
+ __OBJC_METACLASS_RO_$_AXEventTapManagerFilterEvents
+ ___29+[AXSpringBoardServer server]_block_invoke.382
+ ___35-[AXCapabilityManager capabilities]_block_invoke_23
+ ___35-[AXCapabilityManager capabilities]_block_invoke_24
+ ___35-[AXCapabilityManager capabilities]_block_invoke_25
+ ___58-[FKAAvailableCommands _updateCachedSiriShortcutsCommands]_block_invoke
+ ___58-[FKAAvailableCommands _updateCachedSiriShortcutsCommands]_block_invoke_2
+ ___71-[AXEventTapManager _installHIDFilter:skipDeviceMatching:filterEvents:]_block_invoke
+ ___AXFallbackDeviceSizeMM_block_invoke.108
+ ___AXFallbackDeviceSizeMM_block_invoke.108.cold.1
+ ___AXLoadPunctuationTable_block_invoke.281
+ ___AXProcessIsSurfBoard_block_invoke
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8lw32l8
+ ___block_literal_global.102
+ ___block_literal_global.110
+ ___block_literal_global.124
+ ___block_literal_global.136
+ ___block_literal_global.139
+ ___block_literal_global.199
+ ___block_literal_global.207
+ ___block_literal_global.209
+ ___block_literal_global.230
+ ___block_literal_global.235
+ ___block_literal_global.237
+ ___block_literal_global.239
+ ___block_literal_global.256
+ ___block_literal_global.258
+ ___block_literal_global.260
+ ___block_literal_global.2665
+ ___block_literal_global.2736
+ ___block_literal_global.2744
+ ___block_literal_global.275
+ ___block_literal_global.276
+ ___block_literal_global.2762
+ ___block_literal_global.2780
+ ___block_literal_global.279
+ ___block_literal_global.280
+ ___block_literal_global.281
+ ___block_literal_global.293
+ ___block_literal_global.296
+ ___block_literal_global.298
+ ___block_literal_global.303
+ ___block_literal_global.305
+ ___block_literal_global.307
+ ___block_literal_global.313
+ ___block_literal_global.316
+ ___block_literal_global.318
+ ___block_literal_global.323
+ ___block_literal_global.327
+ ___block_literal_global.331
+ ___block_literal_global.336
+ ___block_literal_global.349
+ ___block_literal_global.354
+ ___block_literal_global.365
+ ___block_literal_global.366
+ ___block_literal_global.403
+ ___block_literal_global.410
+ ___block_literal_global.4176
+ ___block_literal_global.429
+ ___block_literal_global.436
+ ___block_literal_global.438
+ ___block_literal_global.441
+ ___block_literal_global.50
+ ___block_literal_global.538
+ ___block_literal_global.798
+ ___block_literal_global.858
+ ___block_literal_global.87
+ ___block_literal_global.98
+ __unnamed_array_storage.220
+ __unnamed_array_storage.222
+ __unnamed_array_storage.223
+ __unnamed_array_storage.225
+ __unnamed_array_storage.245
+ __unnamed_array_storage.2766
+ __unnamed_array_storage.279
+ __unnamed_array_storage.457
+ __unnamed_array_storage.464
+ __unnamed_array_storage.478
+ __unnamed_array_storage.479
+ _objc_msgSend$_hidFilterListForPair:filterEvents:
+ _objc_msgSend$_installEventTap:skipDeviceMatching:filterEvents:
+ _objc_msgSend$_installHIDFilter:skipDeviceMatching:filterEvents:
+ _objc_msgSend$_updateCachedSiriShortcutsCommands
+ _objc_msgSend$cachedSiriShortcutsCommands
+ _objc_msgSend$installEventTap:identifier:type:skipDeviceMatching:filterEvents:matchingServiceHandler:
+ _objc_msgSend$setCachedSiriShortcutsCommands:
+ _objc_msgSend$setWantsATVRemoteEvents:
+ _objc_msgSend$setWantsAccessibilityEvents:
+ _objc_msgSend$setWantsDigitizerEvents:
+ _objc_msgSend$setWantsKeyboardEvents:
+ _objc_msgSend$setWantsLisaEvents:
+ _objc_msgSend$setWantsMouseEvents:
+ _objc_msgSend$setWantsStylusEvents:
+ _objc_msgSend$setWantsVolumeButtonEvents:
+ _objc_msgSend$siriShortcutsQueue
+ _objc_msgSend$toggleHearingControlCenter
+ _objc_msgSend$valueForTripleClickOption:
+ _objc_msgSend$wantsATVRemoteEvents
+ _objc_msgSend$wantsAccessibilityEvents
+ _objc_msgSend$wantsDigitizerEvents
+ _objc_msgSend$wantsKeyboardEvents
+ _objc_msgSend$wantsLisaEvents
+ _objc_msgSend$wantsMouseEvents
+ _objc_msgSend$wantsStylusEvents
+ _objc_msgSend$wantsVolumeButtonEvents
+ _objectdestroy.144Tm
+ _server.onceToken.381
+ _symbolic Sb_SbypXpSgt
+ _symbolic SpyxG
+ _symbolic _____ 22AccessibilityUtilities01_A15CallbackHandlerV
+ _symbolic _____ 22AccessibilityUtilities01_A23OptionalCallbackHandlerV
+ _symbolic yyc
+ _symbolic yycSg
- -[AXEventTapManager _hidFilterListForPair:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:wantsStylusEvents:]
- -[AXEventTapManager _installEventTap:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:wantsStylusEvents:]
- -[AXEventTapManager _installHIDFilter:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:wantsStylusEvents:]
- -[AXEventTapManager installEventTap:identifier:type:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:]
- -[AXEventTapManager installEventTap:identifier:type:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:matchingServiceHandler:]
- -[AXEventTapManager installEventTap:identifier:type:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:wantsStylusEvents:]
- -[AXEventTapManager installEventTap:identifier:type:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:wantsStylusEvents:matchingServiceHandler:]
- -[AXSettings setVoiceOverUseActiveSiriVoice:]
- -[AXSettings voiceOverUseActiveSiriVoice]
- GCC_except_table1008
- GCC_except_table1009
- GCC_except_table117
- GCC_except_table12
- GCC_except_table32
- GCC_except_table37
- GCC_except_table466
- GCC_except_table469
- GCC_except_table470
- GCC_except_table634
- GCC_except_table69
- GCC_except_table692
- GCC_except_table93
- GCC_except_table930
- GCC_except_table934
- _AXShouldCrashOnValidationErrors._Value
- _AXShouldCrashOnValidationErrors.onceToken
- _AXUIAccessibilitySpeechAttributePoorMansPronunciationHelp
- __AXSCrashOnValidationErrors
- ___196-[AXEventTapManager _installHIDFilter:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:wantsStylusEvents:]_block_invoke
- ___29+[AXSpringBoardServer server]_block_invoke.388
- ___AXFallbackDeviceSizeMM_block_invoke.105
- ___AXFallbackDeviceSizeMM_block_invoke.105.cold.1
- ___AXLoadPunctuationTable_block_invoke.287
- ___AXShouldCrashOnValidationErrors_block_invoke
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8ls32l8
- ___block_literal_global.104
- ___block_literal_global.121
- ___block_literal_global.129
- ___block_literal_global.16
- ___block_literal_global.196
- ___block_literal_global.204
- ___block_literal_global.206
- ___block_literal_global.211
- ___block_literal_global.212
- ___block_literal_global.245
- ___block_literal_global.262
- ___block_literal_global.264
- ___block_literal_global.2676
- ___block_literal_global.272
- ___block_literal_global.2740
- ___block_literal_global.2748
- ___block_literal_global.2766
- ___block_literal_global.277
- ___block_literal_global.2784
- ___block_literal_global.282
- ___block_literal_global.285
- ___block_literal_global.286
- ___block_literal_global.289
- ___block_literal_global.291
- ___block_literal_global.299
- ___block_literal_global.300
- ___block_literal_global.304
- ___block_literal_global.309
- ___block_literal_global.314
- ___block_literal_global.324
- ___block_literal_global.332
- ___block_literal_global.337
- ___block_literal_global.35
- ___block_literal_global.356
- ___block_literal_global.358
- ___block_literal_global.395
- ___block_literal_global.402
- ___block_literal_global.4182
- ___block_literal_global.421
- ___block_literal_global.428
- ___block_literal_global.433
- ___block_literal_global.544
- ___block_literal_global.804
- ___block_literal_global.84
- ___block_literal_global.864
- ___block_literal_global.89
- ___block_literal_global.99
- __unnamed_array_storage.226
- __unnamed_array_storage.228
- __unnamed_array_storage.229
- __unnamed_array_storage.231
- __unnamed_array_storage.251
- __unnamed_array_storage.2770
- __unnamed_array_storage.285
- __unnamed_array_storage.469
- __unnamed_array_storage.470
- __unnamed_array_storage.484
- __unnamed_array_storage.485
- _kAXSVoiceOverUseActiveSiriVoice
- _objc_msgSend$_hidFilterListForPair:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:wantsStylusEvents:
- _objc_msgSend$_installEventTap:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:wantsStylusEvents:
- _objc_msgSend$_installHIDFilter:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:wantsStylusEvents:
- _objc_msgSend$installEventTap:identifier:type:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:wantsStylusEvents:
- _objc_msgSend$installEventTap:identifier:type:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:wantsStylusEvents:matchingServiceHandler:
- _objectdestroy.135Tm
- _server.onceToken.387
CStrings:
+ "\x05"
+ "@56@0:8@?16@24i32B36@40@?48"
+ "AXAssistiveTouchIconTypeActionButton"
+ "AXEventTapManagerFilterEvents"
+ "AXHaptics"
+ "AXLiveSpeech"
+ "AXReduceTransparency"
+ "AX_Not_OSXR_Capability"
+ "AX_OSXR_Capability"
+ "ColorFiltersEnabled"
+ "HAND_GESTURE_DOUBLE_TAP"
+ "HAND_GESTURE_TAP"
+ "T@\"NSArray\",&,N,V_cachedSiriShortcutsCommands"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_siriShortcutsQueue"
+ "TB,N,V_wantsATVRemoteEvents"
+ "TB,N,V_wantsAccessibilityEvents"
+ "TB,N,V_wantsDigitizerEvents"
+ "TB,N,V_wantsKeyboardEvents"
+ "TB,N,V_wantsLisaEvents"
+ "TB,N,V_wantsMouseEvents"
+ "TB,N,V_wantsStylusEvents"
+ "TB,N,V_wantsVolumeButtonEvents"
+ "WatchControl-elton"
+ "_cachedSiriShortcutsCommands"
+ "_hidFilterListForPair:filterEvents:"
+ "_installEventTap:skipDeviceMatching:filterEvents:"
+ "_installHIDFilter:skipDeviceMatching:filterEvents:"
+ "_siriShortcutsQueue"
+ "_updateCachedSiriShortcutsCommands"
+ "_wantsATVRemoteEvents"
+ "_wantsAccessibilityEvents"
+ "_wantsDigitizerEvents"
+ "_wantsKeyboardEvents"
+ "_wantsLisaEvents"
+ "_wantsMouseEvents"
+ "_wantsStylusEvents"
+ "_wantsVolumeButtonEvents"
+ "cachedSiriShortcutsCommands"
+ "cn"
+ "com.apple.Accessibility.FKAAvailableCommands.SiriShortcuts"
+ "com.apple.SurfBoard"
+ "com.apple.musebuddy"
+ "currentBubbleElement"
+ "feature"
+ "installEventTap:identifier:type:skipDeviceMatching:filterEvents:matchingServiceHandler:"
+ "isReduceWhitePointEnabled"
+ "q20@0:8i16"
+ "safeSwiftCallAsFunction:"
+ "setCachedSiriShortcutsCommands:"
+ "setSiriShortcutsQueue:"
+ "setWantsATVRemoteEvents:"
+ "setWantsAccessibilityEvents:"
+ "setWantsDigitizerEvents:"
+ "setWantsKeyboardEvents:"
+ "setWantsLisaEvents:"
+ "setWantsMouseEvents:"
+ "setWantsStylusEvents:"
+ "setWantsVolumeButtonEvents:"
+ "siriShortcutsQueue"
+ "stateForTripleClickOption:"
+ "toggleHearingControlCenter"
+ "touch-id"
+ "v36@0:8@16B24@28"
+ "wantsATVRemoteEvents"
+ "wantsAccessibilityEvents"
+ "wantsDigitizerEvents"
+ "wantsKeyboardEvents"
+ "wantsLisaEvents"
+ "wantsMouseEvents"
+ "wantsStylusEvents"
+ "wantsVolumeButtonEvents"
+ "yue"
- "@52@0:8@16B24B28B32B36B40B44B48"
- "@64@0:8@?16@24i32B36B40B44B48B52B56B60"
- "@68@0:8@?16@24i32B36B40B44B48B52B56B60B64"
- "@72@0:8@?16@24i32B36B40B44B48B52B56B60@?64"
- "@76@0:8@?16@24i32B36B40B44B48B52B56B60B64@?68"
- "AXValidation Error"
- "AX_HW_TTY_Capability"
- "AX_SW_TTY_Capability"
- "HAND_GESTURE_DOUBLE_PINCH"
- "HAND_GESTURE_PINCH"
- "See syslog"
- "VoiceOverUseActiveSiriVoice"
- "_hidFilterListForPair:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:wantsStylusEvents:"
- "_installEventTap:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:wantsStylusEvents:"
- "_installHIDFilter:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:wantsStylusEvents:"
- "installEventTap:identifier:type:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:"
- "installEventTap:identifier:type:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:matchingServiceHandler:"
- "installEventTap:identifier:type:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:wantsStylusEvents:"
- "installEventTap:identifier:type:skipDeviceMatching:wantsDigitizerEvents:wantsKeyboardEvents:wantsATVRemoteEvents:wantsLisaEvents:wantsMouseEvents:wantsAccessibilityEvents:wantsStylusEvents:matchingServiceHandler:"
- "setVoiceOverUseActiveSiriVoice:"
- "v56@0:8@16B24B28B32B36B40B44B48B52"
- "voiceOverUseActiveSiriVoice"

```
