## SpringBoardServices

> `/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA_DIRTY.__objc_data`

```diff

-4630.1.102.0.0
-  __TEXT.__text: 0x7b5fc
-  __TEXT.__objc_methlist: 0x8b58
-  __TEXT.__cstring: 0xde60
+4636.102.1.0.0
+  __TEXT.__text: 0x7caec
+  __TEXT.__objc_methlist: 0x8e58
+  __TEXT.__cstring: 0xdf69
   __TEXT.__const: 0x768
-  __TEXT.__oslogstring: 0x490e
-  __TEXT.__gcc_except_tab: 0xcbc
+  __TEXT.__oslogstring: 0x4b4a
+  __TEXT.__gcc_except_tab: 0xcf8
   __TEXT.__dlopen_cstrs: 0x170
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x29f8
+  __TEXT.__unwind_info: 0x2a60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3908
-  __DATA_CONST.__objc_classlist: 0x6d0
-  __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x2c0
+  __DATA_CONST.__const: 0x3978
+  __DATA_CONST.__objc_classlist: 0x700
+  __DATA_CONST.__objc_catlist: 0x28
+  __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3490
-  __DATA_CONST.__objc_protorefs: 0x1b8
-  __DATA_CONST.__objc_superrefs: 0x488
+  __DATA_CONST.__objc_selrefs: 0x35a8
+  __DATA_CONST.__objc_protorefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0x498
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x8c0
-  __AUTH_CONST.__const: 0x2908
-  __AUTH_CONST.__cfstring: 0xaea0
-  __AUTH_CONST.__objc_const: 0x260a8
+  __DATA_CONST.__got: 0x8e8
+  __AUTH_CONST.__const: 0x2928
+  __AUTH_CONST.__cfstring: 0xaee0
+  __AUTH_CONST.__objc_const: 0x279a8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x830
-  __AUTH.__objc_data: 0x3ac0
-  __DATA.__objc_ivar: 0x874
-  __DATA.__data: 0x2210
-  __DATA.__bss: 0x900
+  __AUTH.__objc_data: 0x3ca0
+  __DATA.__objc_ivar: 0x894
+  __DATA.__data: 0x2390
+  __DATA.__bss: 0x910
   __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0x268
+  __DATA_DIRTY.__bss: 0x278
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4302
-  Symbols:   9101
-  CStrings:  2126
+  Functions: 4359
+  Symbols:   9256
+  CStrings:  2137
 
Symbols:
+ +[SBSFDIDeviceControlClientSettingsExtension protocol]
+ +[SBSFDIDeviceControlSceneExtension clientComponents]
+ +[SBSFDIDeviceControlSceneExtension clientSettingsExtensions]
+ +[SBSFDIDeviceControlSceneExtension hostComponents]
+ +[SBSSecureIndicatorElevationAssertionServiceSpecification identifier]
+ +[SBSSecureIndicatorElevationAssertionServiceSpecification interface]
+ +[SBSSecureIndicatorElevationAssertionServiceSpecification serviceQuality]
+ -[FBSScene(SBSFDIDeviceControl) sbs_fdiDeviceControlComponent]
+ -[SBSFDIDeviceControlClientComponent disablesLiftToWake]
+ -[SBSFDIDeviceControlClientComponent disablesTapToWake]
+ -[SBSFDIDeviceControlClientComponent restrictsToConfigurationA]
+ -[SBSFDIDeviceControlClientComponent setDisablesLiftToWake:]
+ -[SBSFDIDeviceControlClientComponent setDisablesTapToWake:]
+ -[SBSFDIDeviceControlClientComponent setRestrictsToConfigurationA:]
+ -[SBSFDIDeviceControlHostComponent .cxx_destruct]
+ -[SBSFDIDeviceControlHostComponent _clientSettings]
+ -[SBSFDIDeviceControlHostComponent coordinator]
+ -[SBSFDIDeviceControlHostComponent disablesLiftToWake]
+ -[SBSFDIDeviceControlHostComponent disablesTapToWake]
+ -[SBSFDIDeviceControlHostComponent invalidate]
+ -[SBSFDIDeviceControlHostComponent restrictsToConfigurationA]
+ -[SBSFDIDeviceControlHostComponent scene:didUpdateClientSettings:]
+ -[SBSFDIDeviceControlHostComponent setCoordinator:]
+ -[SBSHomeScreenService canSwapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:]
+ -[SBSHomeScreenService replaceApplicationIconsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:]
+ -[SBSHomeScreenService swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:]
+ -[SBSHomeScreenService tearDownAndResetRootIconLists]
+ -[SBSLockScreenContentAction abortForUsageViolation:]
+ -[SBSRelaunchAction abortForUsageViolation:]
+ -[SBSRemoteAlertActivationContext deviceCanBeTreatedAsEffectivelyLocked]
+ -[SBSRemoteAlertActivationContext setDeviceCanBeTreatedAsEffectivelyLocked:]
+ -[SBSSecureIndicatorElevationAssertion .cxx_destruct]
+ -[SBSSecureIndicatorElevationAssertion _sendCurrentStyle]
+ -[SBSSecureIndicatorElevationAssertion dealloc]
+ -[SBSSecureIndicatorElevationAssertion initWithStyle:reason:]
+ -[SBSSecureIndicatorElevationAssertion invalidate]
+ -[SBSSecureIndicatorElevationAssertion setStyle:]
+ -[SBSSecureIndicatorElevationAssertion style]
+ -[SBSSystemNotesConnectAction abortForUsageViolation:]
+ -[SBSSystemNotesCreateAction abortForUsageViolation:]
+ -[SBSSystemNotesTakeScreenshotAction abortForUsageViolation:]
+ _OBJC_CLASS_$_FBSScene
+ _OBJC_CLASS_$_FBSSceneComponent
+ _OBJC_CLASS_$_FBSSceneExtension
+ _OBJC_CLASS_$_FBSSettingsExtension
+ _OBJC_CLASS_$_SBSFDIDeviceControlClientComponent
+ _OBJC_CLASS_$_SBSFDIDeviceControlClientSettingsExtension
+ _OBJC_CLASS_$_SBSFDIDeviceControlHostComponent
+ _OBJC_CLASS_$_SBSFDIDeviceControlSceneExtension
+ _OBJC_CLASS_$_SBSSecureIndicatorElevationAssertion
+ _OBJC_CLASS_$_SBSSecureIndicatorElevationAssertionServiceSpecification
+ _OBJC_IVAR_$_SBSFDIDeviceControlHostComponent._coordinator
+ _OBJC_IVAR_$_SBSRemoteAlertActivationContext._deviceCanBeTreatedAsEffectivelyLocked
+ _OBJC_IVAR_$_SBSSecureIndicatorElevationAssertion._connection
+ _OBJC_IVAR_$_SBSSecureIndicatorElevationAssertion._connectionQueue
+ _OBJC_IVAR_$_SBSSecureIndicatorElevationAssertion._isValid
+ _OBJC_IVAR_$_SBSSecureIndicatorElevationAssertion._reason
+ _OBJC_IVAR_$_SBSSecureIndicatorElevationAssertion._style
+ _OBJC_IVAR_$_SBSSecureIndicatorElevationAssertion._styleLock
+ _OBJC_METACLASS_$_FBSSceneComponent
+ _OBJC_METACLASS_$_FBSSceneExtension
+ _OBJC_METACLASS_$_FBSSettingsExtension
+ _OBJC_METACLASS_$_SBSFDIDeviceControlClientComponent
+ _OBJC_METACLASS_$_SBSFDIDeviceControlClientSettingsExtension
+ _OBJC_METACLASS_$_SBSFDIDeviceControlHostComponent
+ _OBJC_METACLASS_$_SBSFDIDeviceControlSceneExtension
+ _OBJC_METACLASS_$_SBSSecureIndicatorElevationAssertion
+ _OBJC_METACLASS_$_SBSSecureIndicatorElevationAssertionServiceSpecification
+ _SBLogFDIDeviceControl
+ _SBLogFDIDeviceControl.__logObj
+ _SBLogFDIDeviceControl.onceToken
+ __OBJC_$_CATEGORY_FBSScene_$_SBSFDIDeviceControl
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_FBSScene_$_SBSFDIDeviceControl
+ __OBJC_$_CLASS_METHODS_SBSFDIDeviceControlClientSettingsExtension
+ __OBJC_$_CLASS_METHODS_SBSFDIDeviceControlSceneExtension
+ __OBJC_$_CLASS_METHODS_SBSSecureIndicatorElevationAssertionServiceSpecification
+ __OBJC_$_CLASS_PROP_LIST_SBSSecureIndicatorElevationAssertionServiceSpecification
+ __OBJC_$_INSTANCE_METHODS_SBSFDIDeviceControlClientComponent
+ __OBJC_$_INSTANCE_METHODS_SBSFDIDeviceControlHostComponent
+ __OBJC_$_INSTANCE_METHODS_SBSSecureIndicatorElevationAssertion
+ __OBJC_$_INSTANCE_VARIABLES_SBSFDIDeviceControlHostComponent
+ __OBJC_$_INSTANCE_VARIABLES_SBSSecureIndicatorElevationAssertion
+ __OBJC_$_PROP_LIST_FBSScene_$_SBSFDIDeviceControl
+ __OBJC_$_PROP_LIST_SBSFDIDeviceControlClientComponent
+ __OBJC_$_PROP_LIST_SBSFDIDeviceControlClientSettings
+ __OBJC_$_PROP_LIST_SBSFDIDeviceControlHostComponent
+ __OBJC_$_PROP_LIST_SBSFDIDeviceControlMutableClientSettings
+ __OBJC_$_PROP_LIST_SBSSecureIndicatorElevationAssertion
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSFDIDeviceControlClientSettings
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSFDIDeviceControlMutableClientSettings
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSSecureIndicatorElevationAssertionServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSFDIDeviceControlClientSettings
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSFDIDeviceControlMutableClientSettings
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSSecureIndicatorElevationAssertionServerInterface
+ __OBJC_$_PROTOCOL_REFS_SBSFDIDeviceControlClientSettings
+ __OBJC_$_PROTOCOL_REFS_SBSFDIDeviceControlMutableClientSettings
+ __OBJC_$_PROTOCOL_REFS_SBSSecureIndicatorElevationAssertionClientInterface
+ __OBJC_$_PROTOCOL_REFS_SBSSecureIndicatorElevationAssertionServerInterface
+ __OBJC_CLASS_PROTOCOLS_$_SBSFDIDeviceControlClientComponent
+ __OBJC_CLASS_PROTOCOLS_$_SBSFDIDeviceControlHostComponent
+ __OBJC_CLASS_PROTOCOLS_$_SBSSecureIndicatorElevationAssertion
+ __OBJC_CLASS_RO_$_SBSFDIDeviceControlClientComponent
+ __OBJC_CLASS_RO_$_SBSFDIDeviceControlClientSettingsExtension
+ __OBJC_CLASS_RO_$_SBSFDIDeviceControlHostComponent
+ __OBJC_CLASS_RO_$_SBSFDIDeviceControlSceneExtension
+ __OBJC_CLASS_RO_$_SBSSecureIndicatorElevationAssertion
+ __OBJC_CLASS_RO_$_SBSSecureIndicatorElevationAssertionServiceSpecification
+ __OBJC_LABEL_PROTOCOL_$_SBSFDIDeviceControlClientSettings
+ __OBJC_LABEL_PROTOCOL_$_SBSFDIDeviceControlMutableClientSettings
+ __OBJC_LABEL_PROTOCOL_$_SBSSecureIndicatorElevationAssertionClientInterface
+ __OBJC_LABEL_PROTOCOL_$_SBSSecureIndicatorElevationAssertionServerInterface
+ __OBJC_METACLASS_RO_$_SBSFDIDeviceControlClientComponent
+ __OBJC_METACLASS_RO_$_SBSFDIDeviceControlClientSettingsExtension
+ __OBJC_METACLASS_RO_$_SBSFDIDeviceControlHostComponent
+ __OBJC_METACLASS_RO_$_SBSFDIDeviceControlSceneExtension
+ __OBJC_METACLASS_RO_$_SBSSecureIndicatorElevationAssertion
+ __OBJC_METACLASS_RO_$_SBSSecureIndicatorElevationAssertionServiceSpecification
+ __OBJC_PROTOCOL_$_SBSFDIDeviceControlClientSettings
+ __OBJC_PROTOCOL_$_SBSFDIDeviceControlMutableClientSettings
+ __OBJC_PROTOCOL_$_SBSSecureIndicatorElevationAssertionClientInterface
+ __OBJC_PROTOCOL_$_SBSSecureIndicatorElevationAssertionServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_SBSFDIDeviceControlMutableClientSettings
+ __OBJC_PROTOCOL_REFERENCE_$_SBSSecureIndicatorElevationAssertionClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_SBSSecureIndicatorElevationAssertionServerInterface
+ ___59-[SBSFDIDeviceControlClientComponent setDisablesTapToWake:]_block_invoke
+ ___60-[SBSFDIDeviceControlClientComponent setDisablesLiftToWake:]_block_invoke
+ ___61-[SBSSecureIndicatorElevationAssertion initWithStyle:reason:]_block_invoke
+ ___61-[SBSSecureIndicatorElevationAssertion initWithStyle:reason:]_block_invoke_2
+ ___67-[SBSFDIDeviceControlClientComponent setRestrictsToConfigurationA:]_block_invoke
+ ___69+[SBSSecureIndicatorElevationAssertionServiceSpecification interface]_block_invoke
+ ___SBLogFDIDeviceControl_block_invoke
+ ___block_descriptor_33_e69_v24?0"FBSMutableSceneClientSettings"8"FBSSceneTransitionContext"16l
+ ___block_descriptor_40_e8_32s_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8ls32l8
+ ___block_descriptor_56_e8_32s40s48w_e42_v16?0"<BSServiceConnectionConfiguring>"8ls32l8s40l8w48l8
+ _objc_msgSend$_clientSettings
+ _objc_msgSend$_sendCurrentStyle
+ _objc_msgSend$abort
+ _objc_msgSend$applyFDIDeviceControlClientSettings:
+ _objc_msgSend$canSwapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:
+ _objc_msgSend$clientScene
+ _objc_msgSend$clientSettings
+ _objc_msgSend$componentForExtension:ofClass:
+ _objc_msgSend$containsProperty:
+ _objc_msgSend$disablesLiftToWake
+ _objc_msgSend$disablesTapToWake
+ _objc_msgSend$hostScene
+ _objc_msgSend$replaceApplicationIconsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:
+ _objc_msgSend$restrictsToConfigurationA
+ _objc_msgSend$setDeviceCanBeTreatedAsEffectivelyLocked:
+ _objc_msgSend$setDisablesLiftToWake:
+ _objc_msgSend$setDisablesTapToWake:
+ _objc_msgSend$setElevationStyleNum:
+ _objc_msgSend$setRestrictsToConfigurationA:
+ _objc_msgSend$settingsDiff
+ _objc_msgSend$swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:
+ _objc_msgSend$tearDownAndResetRootIconLists
+ _objc_msgSend$updateClientSettings:
- _objc_msgSend$canSwapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:
- _objc_msgSend$swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:
CStrings:
+ "FDIDeviceControl"
+ "SBSFDIDeviceControlHostComponent: client settings changed (liftToWake=%{BOOL}u tapToWake=%{BOOL}u configurationA=%{BOOL}u); updating"
+ "SBSFDIDeviceControlHostComponent: invalidating FDIDeviceControl"
+ "SBSHomeScreenService: failed replaceApplicationIconsWithBundleIdentifier request (no target)."
+ "SBSHomeScreenService: failed tearDownAndResetRootIconLists (no target)."
+ "SBSSecureIndicatorElevationAssertion(%{public}@) connection interrupted. Reactivating."
+ "SBSSecureIndicatorElevationAssertion(%{public}@) connection invalidated remotely. (Do you have the required entitlement?)"
+ "com.apple.SpringBoardServices.SBSSecureIndicatorElevationAssertion.connectionQueue"
+ "com.apple.springboard.secure-indicator-elevation-service"
+ "deviceCanBeTreatedAsEffectivelyLocked"
+ "v24@?0@\"FBSMutableSceneClientSettings\"8@\"FBSSceneTransitionContext\"16"
```
