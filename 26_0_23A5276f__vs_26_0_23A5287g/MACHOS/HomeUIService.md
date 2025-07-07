## HomeUIService

> `/Applications/HomeUIService.app/HomeUIService`

```diff

-1082.1.0.0.0
-  __TEXT.__text: 0x803d4
-  __TEXT.__auth_stubs: 0x13e0
-  __TEXT.__objc_stubs: 0xe4a0
-  __TEXT.__objc_methlist: 0x76d4
-  __TEXT.__objc_methname: 0x14f0c
-  __TEXT.__cstring: 0x903d
-  __TEXT.__objc_classname: 0x1482
+1088.0.0.0.0
+  __TEXT.__text: 0x813e0
+  __TEXT.__auth_stubs: 0x13f0
+  __TEXT.__objc_stubs: 0xe5c0
+  __TEXT.__objc_methlist: 0x7754
+  __TEXT.__const: 0x7b4
+  __TEXT.__objc_methname: 0x14fa7
+  __TEXT.__cstring: 0x907d
+  __TEXT.__objc_classname: 0x14a6
   __TEXT.__objc_methtype: 0x3ce5
-  __TEXT.__const: 0x7a4
-  __TEXT.__oslogstring: 0x7a0a
-  __TEXT.__gcc_except_tab: 0x1250
+  __TEXT.__oslogstring: 0x7bca
+  __TEXT.__gcc_except_tab: 0x1224
   __TEXT.__dlopen_cstrs: 0x52
   __TEXT.__constg_swiftt: 0x360
-  __TEXT.__swift5_typeref: 0x1236
+  __TEXT.__swift5_typeref: 0x1232
   __TEXT.__swift5_fieldmd: 0x178
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_reflstr: 0x181
   __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_capture: 0x180
+  __TEXT.__swift5_capture: 0x1a0
   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x30
-  __TEXT.__unwind_info: 0x1e60
-  __TEXT.__eh_frame: 0x920
-  __DATA_CONST.__auth_got: 0xa00
-  __DATA_CONST.__got: 0xbe8
+  __TEXT.__unwind_info: 0x1e80
+  __TEXT.__eh_frame: 0x970
+  __DATA_CONST.__auth_got: 0xa08
+  __DATA_CONST.__got: 0xbf0
   __DATA_CONST.__auth_ptr: 0x250
-  __DATA_CONST.__const: 0x3218
-  __DATA_CONST.__cfstring: 0x4200
-  __DATA_CONST.__objc_classlist: 0x3e8
+  __DATA_CONST.__const: 0x3268
+  __DATA_CONST.__cfstring: 0x42e0
+  __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x370
-  __DATA_CONST.__objc_intobj: 0xe28
+  __DATA_CONST.__objc_superrefs: 0x378
+  __DATA_CONST.__objc_intobj: 0xe58
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_arraydata: 0xb8
   __DATA_CONST.__objc_arrayobj: 0x78
-  __DATA.__objc_const: 0xd2e8
-  __DATA.__objc_selrefs: 0x4d30
-  __DATA.__objc_ivar: 0x670
-  __DATA.__objc_data: 0x2670
+  __DATA.__objc_const: 0xd450
+  __DATA.__objc_selrefs: 0x4d78
+  __DATA.__objc_ivar: 0x678
+  __DATA.__objc_data: 0x26c0
   __DATA.__data: 0x1b20
   __DATA.__bss: 0x500
   __DATA.__common: 0x20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: ABA89DA5-2B34-3B9A-A6AF-B2159A322242
-  Functions: 2834
-  Symbols:   825
-  CStrings:  5546
+  UUID: 1FB4A63F-7765-33B6-80E9-A6521AAC82C2
+  Functions: 2846
+  Symbols:   827
+  CStrings:  5573
 
Symbols:
+ _$s13HomeDataModel16ThermostatPresetV05shortE5LabelSSvg
+ _$sSS11utf8CStrings15ContiguousArrayVys4Int8VGvg
+ _OBJC_CLASS_$_UIStackView
- _$s13HomeDataModel16ThermostatPresetV11presetLabelSSvg
CStrings:
+ "(%s) Skipping %@ because accessory %@ does not have presets, hf_shouldShowPresetConfiguration = %d"
+ "(%s) Skipping %@ because accessory %@ does not support `Adaptive Temperature`, supportsAdaptiveTemperatureAutomations = %d"
+ "(%s) Skipping %@ because accessory %@ does not support `Cleaner Energy`, supportsCleanEnergyAutomation = %d."
+ "(%s) Skipping %@ because accessory %@ has already onboarded for or may have previously dismissed `Cleaner Energy`."
+ "(%s) Skipping %@ because accessory %@ has already onboarded for or may have previously dismissed for `Adaptive Temperature`."
+ "(%s) Skipping %@ because feature flag `HOME_ENABLE_ACTIVITY_STATE` is not enabled."
+ "(%s) Skipping %@ because home %@ does not have any residents capable of supporting home activity state."
+ "(%s) Skipping %@ because isAllowedToEnableAdaptiveTemperatureAutomations = %d, HM_FEATURE_ICICLE_DRIP_ENABLED = %d"
+ "(%s) Skipping %@ because the home is not allowed to enable Adaptive Temperature, isAllowedToEnableAdaptiveTemperatureAutomations = %d"
+ "(%s) Skipping %@ for accessory %@ because grid forecast is not supported in home region."
+ "(%s): Home has utility subscription: %{BOOL}d"
+ "-[HSPCAdaptiveTemperatureViewController _enableAdaptiveTemperature]"
+ "-[HSPCAdaptiveTemperatureViewController _enableAdaptiveTemperature]_block_invoke_3"
+ "-[HSPCAdaptiveTemperatureViewController _hasOnboardedForAdaptiveTemperatureWithCompletion:]_block_invoke"
+ "-[HSPCAdaptiveTemperatureViewController _notNowTapped]"
+ "-[HSPCAdaptiveTemperatureViewController _notNowTapped]_block_invoke_2"
+ "-[HSPCCleanEnergyAutomationViewController _enableCleanEnergyAutomation]"
+ "-[HSPCCleanEnergyAutomationViewController _hasOnboardedForCleanEnergyAutomationWithCompletion:]_block_invoke"
+ "-[HSPCCleanEnergyAutomationViewController _notNowTapped]"
+ "-[HSPCCleanEnergyAutomationViewController initWithCoordinator:config:]"
+ "-[HSPCSetTemperaturesViewController _hasOnboardedForAdaptiveTemperature]_block_invoke"
+ "-[HSPCSetTemperaturesViewController _hasOnboardedForAdaptiveTemperature]_block_invoke_2"
+ "-[HSSetupStateMachine _shouldSkipAdaptiveTempStep:forConfig:]"
+ "-[HSSetupStateMachine _shouldSkipCleanEnergyStep:forConfig:]"
+ "AdaptiveTemperature"
+ "CleanEnergy"
+ "HSPCAdaptiveTemperatureViewController"
+ "HSPCCleanEnergyAutomationViewController"
+ "HSPCUpdateToOptimizeEnergySavingsViewController"
+ "HSThermostatAdaptiveTemperature_AtHome"
+ "HSThermostatAdaptiveTemperature_AtHomeDescription"
+ "HSThermostatAdaptiveTemperature_AwayExtendedAway"
+ "HSThermostatAdaptiveTemperature_AwayExtendedAwayDescription"
+ "HSThermostatAdaptiveTemperature_Description"
+ "HSThermostatAdaptiveTemperature_Title"
+ "HSThermostatCleanEnergy_Description"
+ "HSThermostatCleanEnergy_TOUDescription"
+ "HSThermostatCleanEnergy_Title"
+ "HSThermostatContinue"
+ "HSThermostatUnqualifiedHome_BottomDescription"
+ "HSThermostatUnqualifiedHome_Continue"
+ "HSThermostatUnqualifiedHome_Title"
+ "HSThermostatUnqualifiedHome_TopDescription"
+ "UpdateToOptimizeEnergySavings"
+ "_createCenterContentView"
+ "_enableAdaptiveTemperature"
+ "_enableCleanEnergyAutomation"
+ "_hasOnboardedForAdaptiveTemperature"
+ "_hasOnboardedForAdaptiveTemperatureWithCompletion:"
+ "_hasOnboardedForCleanEnergyAutomationWithCompletion:"
+ "_shouldSkipAdaptiveTempStep:forConfig:"
+ "_shouldSkipCleanEnergyStep:forConfig:"
+ "clock.fill"
+ "hf_isGridForecastSupported"
+ "house.fill"
+ "initWithArrangedSubviews:"
+ "moon.stars.fill"
+ "orangeColor"
+ "setAlignment:"
+ "setAxis:"
+ "setDistribution:"
+ "setSpacing:"
- "(%s) Skipping %@ because accessory %@ does not support `Adaptive Temperature`."
- "(%s) Skipping %@ because accessory %@ does not support `Clean Energy Automation`"
- "(%s) Skipping %@ because accessory %@ does not support `Clean Energy Automation` and/or does not contain any presets"
- "(%s) Skipping %@ because accessory %@ has already onboared or may have previously dismissed for `Optimize For Cleaner Energy`."
- "(%s) Skipping %@ because accessory %@ has already onboared or may have previously dismissed for `Optimize for Energy Savings`."
- "(%s) Skipping %@ because feature flag is not enabled."
- "(%s) Skipping %@ because home %@ does not have resident capable of supporting home activity state."
- "-[HSPCOptimizeCleanerEnergyAutomationViewController _enableOptimizeCleanerEnergyAutomation]"
- "-[HSPCOptimizeCleanerEnergyAutomationViewController _hasOnboardedForOptimizeCleanerEnergyAutomationWithCompletion:]_block_invoke"
- "-[HSPCOptimizeCleanerEnergyAutomationViewController _notNowTapped]"
- "-[HSPCOptimizeEnergySavingsViewController _enableOptimizeEnergySavings]"
- "-[HSPCOptimizeEnergySavingsViewController _enableOptimizeEnergySavings]_block_invoke_3"
- "-[HSPCOptimizeEnergySavingsViewController _hasOnboardedForOptimizeEnergySavingsWithCompletion:]_block_invoke"
- "-[HSPCOptimizeEnergySavingsViewController _notNowTapped]"
- "-[HSPCOptimizeEnergySavingsViewController _notNowTapped]_block_invoke_2"
- "-[HSPCSetTemperaturesViewController _hasOnboardedForOptimizeEnergySavings]_block_invoke"
- "-[HSPCSetTemperaturesViewController _hasOnboardedForOptimizeEnergySavings]_block_invoke_2"
- "-[HSSetupStateMachine _shouldSkipAutoClimateStep:forConfig:]"
- "HSPCOptimizeCleanerEnergyAutomationViewController"
- "HSPCOptimizeEnergySavingsViewController"
- "HSThermostatDone"
- "HSThermostatOptimizeCleanerEnergyButton"
- "HSThermostatOptimizeCleanerEnergy_Description"
- "HSThermostatOptimizeCleanerEnergy_TOUDescription"
- "HSThermostatOptimizeCleanerEnergy_Title"
- "HSThermostatOptimizeEnergySavingsButton"
- "HSThermostatOptimizeEnergySavings_AtHome"
- "HSThermostatOptimizeEnergySavings_AtHomeDescription"
- "HSThermostatOptimizeEnergySavings_AwayExtendedAway"
- "HSThermostatOptimizeEnergySavings_AwayExtendedAwayDescription"
- "HSThermostatOptimizeEnergySavings_Description"
- "HSThermostatOptimizeEnergySavings_Sleeping"
- "HSThermostatOptimizeEnergySavings_SleepingDescription"
- "HSThermostatOptimizeEnergySavings_Title"
- "OptimizeCleanerEnergy"
- "OptimizeEnergySavings"
- "_enableOptimizeCleanerEnergyAutomation"
- "_enableOptimizeEnergySavings"
- "_hasOnboardedForOptimizeCleanerEnergyAutomationWithCompletion:"
- "_hasOnboardedForOptimizeEnergySavings"
- "_hasOnboardedForOptimizeEnergySavingsWithCompletion:"
- "_shouldSkipAutoClimateStep:forConfig:"

```
