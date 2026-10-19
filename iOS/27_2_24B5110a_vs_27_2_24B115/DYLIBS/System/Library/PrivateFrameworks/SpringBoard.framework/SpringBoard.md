## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

 4637.1.14.103.0
-  __TEXT.__text: 0xad435c
+  __TEXT.__text: 0xad6cd8
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xbe4f0
-  __TEXT.__const: 0x11370
-  __TEXT.__oslogstring: 0x65afe
-  __TEXT.__cstring: 0x85af0
+  __TEXT.__objc_methlist: 0xbe6c0
+  __TEXT.__const: 0x11380
+  __TEXT.__oslogstring: 0x660a4
+  __TEXT.__cstring: 0x85b58
   __TEXT.__gcc_except_tab: 0x18890
   __TEXT.__ustring: 0xd04
   __TEXT.__dlopen_cstrs: 0x373
-  __TEXT.__unwind_info: 0x3a080
+  __TEXT.__unwind_info: 0x3a108
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1dae0
-  __DATA_CONST.__objc_classlist: 0x5520
-  __DATA_CONST.__objc_catlist: 0x338
+  __DATA_CONST.__const: 0x1dac0
+  __DATA_CONST.__objc_classlist: 0x5540
+  __DATA_CONST.__objc_catlist: 0x350
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x2af8
+  __DATA_CONST.__objc_protolist: 0x2b08
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ed30
+  __DATA_CONST.__objc_selrefs: 0x4ee30
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x40c0
+  __DATA_CONST.__objc_superrefs: 0x40c8
   __DATA_CONST.__objc_arraydata: 0x18b8
-  __DATA_CONST.__got: 0xa9c0
+  __DATA_CONST.__got: 0xaa00
   __AUTH_CONST.__const: 0x10c68
-  __AUTH_CONST.__cfstring: 0x74f80
-  __AUTH_CONST.__objc_const: 0x28a9f0
+  __AUTH_CONST.__cfstring: 0x75020
+  __AUTH_CONST.__objc_const: 0x28b228
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x1740
   __AUTH_CONST.__objc_doubleobj: 0x850
   __AUTH_CONST.__objc_intobj: 0x2cb8
   __AUTH_CONST.__objc_dictobj: 0x2f8
-  __AUTH_CONST.__auth_got: 0x2c00
-  __AUTH.__objc_data: 0xd9d0
-  __DATA.__objc_ivar: 0xfd40
-  __DATA.__data: 0x210a0
+  __AUTH_CONST.__auth_got: 0x2c10
+  __AUTH.__objc_data: 0xda70
+  __DATA.__objc_ivar: 0xfd5c
+  __DATA.__data: 0x21160
   __DATA.__common: 0xa40
-  __DATA_DIRTY.__objc_data: 0x27970
+  __DATA_DIRTY.__objc_data: 0x27a10
   __DATA_DIRTY.__data: 0x140
   __DATA_DIRTY.__bss: 0x19e8
   __DATA_DIRTY.__common: 0x40

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  Functions: 73747
-  Symbols:   119682
-  CStrings:  23612
+  Functions: 73776
+  Symbols:   119766
+  CStrings:  23633
 
Symbols:
+ +[SBDeviceEmulationController applicationInitializationContext]
+ +[SBDeviceEmulationController deviceContext]
+ +[SBDeviceEmulationController displayContext]
+ +[SBFDIDeviceControlCoordinator _scene:hasEntitlement:]
+ +[SBFDIDeviceControlCoordinator addSceneExtensionIfNeeded:]
+ +[SBScreenEdgeCompensationDisplayTransformer isScreenEdgeCompensationEnabled]
+ +[SBScreenEdgeCompensationDisplayTransformer sceneTransformForWindowScene:]
+ +[SBScreenEdgeCompensationDisplayTransformer transformedConfigurationForConfiguration:]
+ -[SBFDIDeviceControlBacklightInformer isRestricting]
+ -[SBFDIDeviceControlBacklightInformer setRestricting:]
+ -[SBFDIDeviceControlBacklightInformer shouldTurnOnScreenForBacklightSource:]
+ -[SBFDIDeviceControlCoordinator .cxx_destruct]
+ -[SBFDIDeviceControlCoordinator _updateBacklightRestrictionForWindowScene:wantsRestriction:]
+ -[SBFDIDeviceControlCoordinator _updateLiftToWakeForWindowScenes:wantsSuppression:]
+ -[SBFDIDeviceControlCoordinator _updateShieldButtonsRestrictionForWindowScenes:wantsRestriction:]
+ -[SBFDIDeviceControlCoordinator _updateTapToWakeForWindowScenes:wantsSuppression:]
+ -[SBFDIDeviceControlCoordinator applyFDIDeviceControlClientSettings:]
+ -[SBFDIDeviceControlCoordinator init]
+ -[SBFDIDeviceControlCoordinator invalidate]
+ -[SBSAPlatformMetricsContext _setSensorVariant:]
+ -[SBSAPlatformMetricsContext copyBySettingSensorVariant:]
+ -[SBSAPlatformMetricsContext sensorVariant]
+ -[SBSAPlatformMetricsContextMutator sensorVariant]
+ -[SBSAPlatformMetricsContextMutator setSensorVariant:]
+ -[UISMutableApplicationInitializationContext(DeviceEmulation) sb_configureForDeviceEmulation]
+ -[UISMutableDeviceContext(DeviceEmulation) sb_configureForDeviceEmulation]
+ -[UISMutableDisplayContext(DeviceEmulation) sb_configureForDeviceEmulation]
+ _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
+ _OBJC_CLASS_$_SBDeviceEmulationController
+ _OBJC_CLASS_$_SBFDIDeviceControlBacklightInformer
+ _OBJC_CLASS_$_SBFDIDeviceControlCoordinator
+ _OBJC_CLASS_$_SBSFDIDeviceControlHostComponent
+ _OBJC_CLASS_$_SBSFDIDeviceControlSceneExtension
+ _OBJC_CLASS_$_SBScreenEdgeCompensationDisplayTransformer
+ _OBJC_CLASS_$_SSKHostingConfiguration
+ _OBJC_CLASS_$_SSKLayerConfiguration
+ _OBJC_IVAR_$_SBApplicationInfo._disableD2026ClassicMode
+ _OBJC_IVAR_$_SBFDIDeviceControlBacklightInformer._restricting
+ _OBJC_IVAR_$_SBFDIDeviceControlCoordinator._backlightInformer
+ _OBJC_IVAR_$_SBFDIDeviceControlCoordinator._disableLiftToWakeAssertions
+ _OBJC_IVAR_$_SBFDIDeviceControlCoordinator._disableShieldButtonsAssertions
+ _OBJC_IVAR_$_SBFDIDeviceControlCoordinator._disableTapToWakeAssertions
+ _OBJC_IVAR_$_SBFDIDeviceControlCoordinator._restrictedBacklightControllers
+ _OBJC_METACLASS_$_SBDeviceEmulationController
+ _OBJC_METACLASS_$_SBFDIDeviceControlBacklightInformer
+ _OBJC_METACLASS_$_SBFDIDeviceControlCoordinator
+ _OBJC_METACLASS_$_SBScreenEdgeCompensationDisplayTransformer
+ _SBLogDisplayTransforming
+ _SBLogFDIDeviceControl
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableApplicationInitializationContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableDeviceContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableDisplayContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_UISMutableApplicationInitializationContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_UISMutableDeviceContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_UISMutableDisplayContext_$_DeviceEmulation
+ __OBJC_$_CLASS_METHODS_SBDeviceEmulationController
+ __OBJC_$_CLASS_METHODS_SBFDIDeviceControlCoordinator
+ __OBJC_$_CLASS_METHODS_SBScreenEdgeCompensationDisplayTransformer
+ __OBJC_$_CLASS_PROP_LIST_SBDeviceEmulationController
+ __OBJC_$_INSTANCE_METHODS_SBFDIDeviceControlBacklightInformer
+ __OBJC_$_INSTANCE_METHODS_SBFDIDeviceControlCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_SBFDIDeviceControlBacklightInformer
+ __OBJC_$_INSTANCE_VARIABLES_SBFDIDeviceControlCoordinator
+ __OBJC_$_PROP_LIST_SBFDIDeviceControlBacklightInformer
+ __OBJC_$_PROP_LIST_SBFDIDeviceControlCoordinator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBBacklightInforming
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSFDIDeviceControlCoordinating
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBBacklightInforming
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSFDIDeviceControlCoordinating
+ __OBJC_$_PROTOCOL_REFS_SBBacklightInforming
+ __OBJC_$_PROTOCOL_REFS_SBSFDIDeviceControlCoordinating
+ __OBJC_CLASS_PROTOCOLS_$_SBFDIDeviceControlBacklightInformer
+ __OBJC_CLASS_PROTOCOLS_$_SBFDIDeviceControlCoordinator
+ __OBJC_CLASS_RO_$_SBDeviceEmulationController
+ __OBJC_CLASS_RO_$_SBFDIDeviceControlBacklightInformer
+ __OBJC_CLASS_RO_$_SBFDIDeviceControlCoordinator
+ __OBJC_CLASS_RO_$_SBScreenEdgeCompensationDisplayTransformer
+ __OBJC_LABEL_PROTOCOL_$_SBBacklightInforming
+ __OBJC_LABEL_PROTOCOL_$_SBSFDIDeviceControlCoordinating
+ __OBJC_METACLASS_RO_$_SBDeviceEmulationController
+ __OBJC_METACLASS_RO_$_SBFDIDeviceControlBacklightInformer
+ __OBJC_METACLASS_RO_$_SBFDIDeviceControlCoordinator
+ __OBJC_METACLASS_RO_$_SBScreenEdgeCompensationDisplayTransformer
+ __OBJC_PROTOCOL_$_SBBacklightInforming
+ __OBJC_PROTOCOL_$_SBSFDIDeviceControlCoordinating
+ ___57-[SBSAPlatformMetricsContext copyBySettingSensorVariant:]_block_invoke
- -[SBLockScreenBiometricAuthenticationCoordinator _shouldShowAlertForSeed]
- ___block_descriptor_33_e31_v16?0"SSKDisplayPreferences"8l
CStrings:
+ "%{public}@: screen edge compensation transform built: %{BOOL}u"
+ "Applying screen edge compensation: D76 main display size matched; rewriting bounds from %{public}@ to %{public}@"
+ "EdgeSwipeBandExpansionEnabled"
+ "FDIDeviceControl"
+ "SBDisableD2026ClassicMode"
+ "SBFDIDeviceControlCoordinator: acquired lift-to-wake disable across %lu window scenes"
+ "SBFDIDeviceControlCoordinator: acquired shield-buttons disable across %lu non-main-root window scenes"
+ "SBFDIDeviceControlCoordinator: acquired tap-to-wake disable across %lu window scenes"
+ "SBFDIDeviceControlCoordinator: attached FDI device control extension to entitled scene %{public}@"
+ "SBFDIDeviceControlCoordinator: invalidate"
+ "SBFDIDeviceControlCoordinator: powered off + registered wake veto on non-main-root display for scene %{public}@"
+ "SBFDIDeviceControlCoordinator: released lift-to-wake disable across %lu window scenes"
+ "SBFDIDeviceControlCoordinator: released shield-buttons disable across %lu window scenes"
+ "SBFDIDeviceControlCoordinator: released tap-to-wake disable across %lu window scenes"
+ "SBFDIDeviceControlCoordinator: removed wake veto from non-main-root display for scene %{public}@"
+ "SBFDIDeviceControlCoordinator: updating FDI device control (liftToWake=%{BOOL}u tapToWake=%{BOOL}u configurationA=%{BOOL}u) across %lu window scenes"
+ "Skipping screen edge compensation: isMainD76Display=%{BOOL}u"
+ "Unable to build screen edge compensated display configuration: %{public}@ from configuration: %{public}@"
+ "Unable to create redacted display configuration: %@ from configuration:%@"
+ "com.apple.Energy"
+ "sensorVariant"
```
