## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1267.406.30.2.0
-  __TEXT.__text: 0x48dde8
-  __TEXT.__auth_stubs: 0x2530
+1267.529.0.0.0
+  __TEXT.__text: 0x4913f8
+  __TEXT.__auth_stubs: 0x2550
   __TEXT.__objc_stubs: 0x740
   __TEXT.__init_offsets: 0x4c4
   __TEXT.__objc_methlist: 0x134
-  __TEXT.__gcc_except_tab: 0x5445c
-  __TEXT.__const: 0xb07de
-  __TEXT.__cstring: 0x27764
+  __TEXT.__const: 0xb0776
+  __TEXT.__gcc_except_tab: 0x5577c
+  __TEXT.__cstring: 0x276fc
   __TEXT.__objc_classname: 0x34
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_capture: 0x158
-  __TEXT.__oslogstring: 0x4cf10
+  __TEXT.__oslogstring: 0x4c923
   __TEXT.__objc_methname: 0x5b9
   __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_reflstr: 0x4c
   __TEXT.__swift5_fieldmd: 0x68
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
+  __TEXT.__swift_as_entry: 0x34
+  __TEXT.__swift_as_ret: 0x28
   __TEXT.__objc_methtype: 0x22f
   __TEXT.__dof_VirtualAu: 0x303
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0xf3c8
-  __TEXT.__eh_frame: 0x7a8
-  __DATA_CONST.__auth_got: 0x12b0
-  __DATA_CONST.__got: 0x450
+  __TEXT.__unwind_info: 0xf568
+  __TEXT.__eh_frame: 0x780
+  __DATA_CONST.__auth_got: 0x12c0
+  __DATA_CONST.__got: 0x460
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x23ef8
+  __DATA_CONST.__const: 0x242d0
   __DATA_CONST.__cfstring: 0x39c0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_selrefs: 0x208
   __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0x268
-  __DATA.__data: 0x3b8
-  __DATA.__bss: 0x21198
+  __DATA.__data: 0x3c0
+  __DATA.__bss: 0x212d8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9865
-  Symbols:   731
-  CStrings:  10509
+  Functions: 9898
+  Symbols:   735
+  CStrings:  10495
 
Symbols:
+ __ZNKSt3__14__fs10filesystem18directory_iterator13__dereferenceEv
+ __ZNKSt3__14__fs10filesystem4path13__parent_pathEv
+ __ZNSt3__117bad_function_callD1Ev
+ __ZNSt3__14__fs10filesystem18directory_iterator11__incrementEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem18directory_iteratorC1ERKNS1_4pathEPNS_10error_codeENS1_17directory_optionsE
+ __ZTVNSt3__117bad_function_callE
- __ZNKSt9exception4whatEv
- _swift_arrayDestroy
CStrings:
+ "%25s:%-5d %lu: %s."
+ "%25s:%-5d ASSERTION FAILURE: \"IOProc client data (actual = %p, expected = %p) corruption\""
+ "%25s:%-5d ASSERTION FAILURE: \"IOProc proc pointer (actual = %p, expected = %p) corruption\""
+ "%25s:%-5d AudioObjectGetPropertyData(kAudioDevicePropertyDataSources) returned error %s for device %lu."
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationActiveDataSourcesKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationOverriddenPortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationPreferredSubPortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationRoutablePortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationSubPortPreferencesKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationUnroutablePortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationVPBlockConfigurationKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationActiveDataSourcesKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationOverriddenPortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationPreferredSubPortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationRoutablePortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationSubPortPreferencesKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationUnroutablePortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationVPBlockConfigurationKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActivePortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationActiveDataSourcesKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActivePortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationPreferredSubPortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActivePortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationSubPortPreferencesKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActivePortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationUnroutablePortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActivePortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationVPBlockConfigurationKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveSubPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationActiveDataSourcesKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveSubPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationInitiationContextKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveSubPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationOverriddenPortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveSubPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationPreferredSubPortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveSubPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationRoutablePortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveSubPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationSubPortPreferencesKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveSubPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationUnroutablePortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveSubPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationVPBlockConfigurationKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyBuiltInPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationActiveDataSourcesKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyBuiltInPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationOverriddenPortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyBuiltInPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationPreferredSubPortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyBuiltInPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationRoutablePortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyBuiltInPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationSubPortPreferencesKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyBuiltInPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationUnroutablePortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyBuiltInPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationVPBlockConfigurationKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyConnectedPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationActiveDataSourcesKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyConnectedPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationOverriddenPortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyConnectedPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationPreferredSubPortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyConnectedPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationRoutablePortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyConnectedPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationSubPortPreferencesKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyConnectedPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationUnroutablePortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyConnectedPortsForRouteConfiguration doesn't support kVirtualAudioPlugInRouteConfigurationVPBlockConfigurationKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyCreateVAD - either kVirtualAudioPlugInMirrorVADKey or kVirtualAudioPlugInPortIDsKey is required. has mirror vad key: %d has portIDs key: %d\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationIsDisruptive doesn't support kVirtualAudioPlugInRouteConfigurationActiveDataSourcesKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationIsDisruptive doesn't support kVirtualAudioPlugInRouteConfigurationPreferredSubPortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationIsDisruptive doesn't support kVirtualAudioPlugInRouteConfigurationScreenDarkPolicyEnabledKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationIsDisruptive doesn't support kVirtualAudioPlugInRouteConfigurationSubPortPreferencesKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationIsDisruptive doesn't support kVirtualAudioPlugInRouteConfigurationVPBlockConfigurationKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support kVirtualAudioPlugInRouteConfigurationActiveDataSourcesKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support kVirtualAudioPlugInRouteConfigurationCreateSpeakerAlertVADKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support kVirtualAudioPlugInRouteConfigurationDefaultToSpeakerKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support kVirtualAudioPlugInRouteConfigurationDeviceHintsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support kVirtualAudioPlugInRouteConfigurationDisableSpeakerAlertVADKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support kVirtualAudioPlugInRouteConfigurationDisallowHFPKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support kVirtualAudioPlugInRouteConfigurationDisallowedPortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support kVirtualAudioPlugInRouteConfigurationInitiationContextKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support kVirtualAudioPlugInRouteConfigurationOverriddenPortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support kVirtualAudioPlugInRouteConfigurationPreferredSubPortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support kVirtualAudioPlugInRouteConfigurationRoutablePortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support kVirtualAudioPlugInRouteConfigurationScreenDarkPolicyEnabledKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support kVirtualAudioPlugInRouteConfigurationSubPortPreferencesKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support kVirtualAudioPlugInRouteConfigurationUnroutablePortsKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support kVirtualAudioPlugInRouteConfigurationVPBlockConfigurationKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType requires that RouteConfiguration dictionary has kVirtualAudioPlugInRouteConfigurationCategoryKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType requires that RouteConfiguration dictionary has kVirtualAudioPlugInRouteConfigurationModeKey.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInRouteConfigurationDecoupledInputOutputKey can only be true when category is kVirtualAudioPlugInRoutingCategoryPlayAndRecord \" \"or kVirtualAudioPlugInRoutingCategoryEARCLoopback; currently requested category is %s.\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"mDeviceIOProcParams.has_value() == true. An IOProc ID has already been created for the given IOProc\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Could not load LSM Parameters from file, assuming this device has none.\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Error loading parameter [%s] from lsm_parameters.plist.\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"The HAL returned kAudioObjectUnknown for %s index %lu.\""
+ "%25s:%-5d IsAudioLoopbackDevice() - modelUID is %s. Loopback found: %s"
+ "%25s:%-5d Loading LSM Parameters: %s"
+ "%25s:%-5d Re-apply CPMS Power Gain Limit dB: Setting GraaphParameter %s for AU %s. Power Limit = %fdB"
+ "%25s:%-5d Re-apply CPMS Scalar: Setting GraphParameter %s for AU %s Budget Value = %f"
+ "%25s:%-5d Re-apply CPMS X-Lim: Setting GraphParameter %s for AU %s Scale Distance = %f"
+ "%25s:%-5d Setting ProductID to unknown because graph configurations do not exist."
+ "%25s:%-5d Stream Format %lu: %s."
+ "%25s:%-5d VolumeCommand: Getting parameter '%s' to %f on processor type '%s' index %u"
+ "%25s:%-5d getting %s formats for output stream ID %u on device ID %lu (uid: \"%@\")."
+ "@@ Strips Feb 21 2025 18:00:00"
+ "Could not load LSM Parameters from file, assuming this device has none."
+ "Error loading parameter [%s] from lsm_parameters.plist."
+ "PowerBudget_Alarm"
+ "PowerBudget_Default"
+ "PowerBudget_Telephony"
+ "PowerBudget_WaterEjection"
+ "PowerGainLimitDB_Alarm"
+ "PowerGainLimitDB_Default"
+ "The HAL returned kAudioObjectUnknown for %s index %lu."
+ "VA ModelManagerMonitor:: exception while executing Task...%@"
+ "XLim_Default"
+ "XLim_WaterEjection"
+ "chem_sense"
+ "lsm_parameters.plist"
- "%25s:%-5d  Unhandled case in switch"
- "%25s:%-5d %u: %s."
- "%25s:%-5d ASSERTION FAILURE: \"Unexpected policy mute action\""
- "%25s:%-5d AudioObjectGetPropertyData(kAudioDevicePropertyDataSources) return no input data sources for device %u."
- "%25s:%-5d AudioObjectGetPropertyData(kAudioDevicePropertyDataSources) returned error %s for device %u."
- "%25s:%-5d AudioObjectGetPropertyDataSize(kAudioDevicePropertyDataSources) returned error %s for device %u."
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationActiveDataSourcesKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationOverriddenPortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationPreferredSubPortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationRoutablePortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationSubPortPreferencesKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationUnroutablePortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationVPBlockConfigurationKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationActiveDataSourcesKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationOverriddenPortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationPreferredSubPortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationRoutablePortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationSubPortPreferencesKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationUnroutablePortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationVPBlockConfigurationKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActivePortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationActiveDataSourcesKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActivePortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationPreferredSubPortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActivePortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationSubPortPreferencesKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActivePortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationUnroutablePortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActivePortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationVPBlockConfigurationKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveSubPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationActiveDataSourcesKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveSubPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationInitiationContextKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveSubPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationOverriddenPortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveSubPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationPreferredSubPortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveSubPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationRoutablePortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveSubPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationSubPortPreferencesKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveSubPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationUnroutablePortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyActiveSubPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationVPBlockConfigurationKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyBuiltInPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationActiveDataSourcesKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyBuiltInPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationOverriddenPortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyBuiltInPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationPreferredSubPortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyBuiltInPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationRoutablePortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyBuiltInPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationSubPortPreferencesKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyBuiltInPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationUnroutablePortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyBuiltInPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationVPBlockConfigurationKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyConnectedPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationActiveDataSourcesKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyConnectedPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationOverriddenPortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyConnectedPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationPreferredSubPortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyConnectedPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationRoutablePortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyConnectedPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationSubPortPreferencesKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyConnectedPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationUnroutablePortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyConnectedPortsForRouteConfiguration doesn't support \" \"kVirtualAudioPlugInRouteConfigurationVPBlockConfigurationKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyCreateVAD - either kVirtualAudioPlugInMirrorVADKey or kVirtualAudioPlugInPortIDsKey is \" \"required. has mirror vad key: %d has portIDs key: %d\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationIsDisruptive doesn't support \" \"kVirtualAudioPlugInRouteConfigurationActiveDataSourcesKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationIsDisruptive doesn't support \" \"kVirtualAudioPlugInRouteConfigurationPreferredSubPortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationIsDisruptive doesn't support \" \"kVirtualAudioPlugInRouteConfigurationScreenDarkPolicyEnabledKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationIsDisruptive doesn't support \" \"kVirtualAudioPlugInRouteConfigurationSubPortPreferencesKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationIsDisruptive doesn't support \" \"kVirtualAudioPlugInRouteConfigurationVPBlockConfigurationKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support \" \"kVirtualAudioPlugInRouteConfigurationActiveDataSourcesKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support \" \"kVirtualAudioPlugInRouteConfigurationCreateSpeakerAlertVADKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support \" \"kVirtualAudioPlugInRouteConfigurationDefaultToSpeakerKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support \" \"kVirtualAudioPlugInRouteConfigurationDeviceHintsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support \" \"kVirtualAudioPlugInRouteConfigurationDisableSpeakerAlertVADKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support \" \"kVirtualAudioPlugInRouteConfigurationDisallowHFPKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support \" \"kVirtualAudioPlugInRouteConfigurationDisallowedPortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support \" \"kVirtualAudioPlugInRouteConfigurationInitiationContextKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support \" \"kVirtualAudioPlugInRouteConfigurationOverriddenPortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support \" \"kVirtualAudioPlugInRouteConfigurationPreferredSubPortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support \" \"kVirtualAudioPlugInRouteConfigurationRoutablePortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support \" \"kVirtualAudioPlugInRouteConfigurationScreenDarkPolicyEnabledKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support \" \"kVirtualAudioPlugInRouteConfigurationSubPortPreferencesKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support \" \"kVirtualAudioPlugInRouteConfigurationUnroutablePortsKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType doesn't support \" \"kVirtualAudioPlugInRouteConfigurationVPBlockConfigurationKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType requires that RouteConfiguration dictionary has \" \"kVirtualAudioPlugInRouteConfigurationCategoryKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType requires that RouteConfiguration dictionary has \" \"kVirtualAudioPlugInRouteConfigurationModeKey.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareIllegalOperationError): \"kVirtualAudioPlugInRouteConfigurationDecoupledInputOutputKey can only be true when category is \" \"kVirtualAudioPlugInRoutingCategoryPlayAndRecord \" \"or kVirtualAudioPlugInRoutingCategoryEARCLoopback; currently requested category is %s.\""
- "%25s:%-5d EXCEPTION (kAudioHardwareUnspecifiedError): (\"Error processing kVirtualAudioPlugInPropertyCategoryInfo.\")"
- "%25s:%-5d EXCEPTION (kAudioHardwareUnspecifiedError): (\"Routing category info lookup failed.\")"
- "%25s:%-5d EXCEPTION (status) [error status is an error]: \"AudioObjectGetPropertyDataSize(%s) returned error %s (%d).\""
- "%25s:%-5d EXCEPTION (std::logic_error): \"Bad ActivePortsFilter passed to function: %u.\""
- "%25s:%-5d EXCEPTION (std::logic_error): \"invalid volume strategy: %d\""
- "%25s:%-5d EXCEPTION (std::logic_error): \"lhs and rhs ranges do not intersect\""
- "%25s:%-5d EXCEPTION (std::runtime_error): \"AirPlay audio device returned control list size of 0\""
- "%25s:%-5d EXCEPTION (std::runtime_error): \"Expected %u bytes, got %u bytes instead\""
- "%25s:%-5d EXCEPTION (std::runtime_error): \"The HAL returned a size of %u while we expected %lu\""
- "%25s:%-5d EXCEPTION (std::runtime_error): \"The HAL returned a size of %u while we expected %u\""
- "%25s:%-5d EXCEPTION (std::runtime_error): \"The HAL returned input stream size of %u\""
- "%25s:%-5d EXCEPTION (std::runtime_error): \"The HAL returned kAudioObjectUnknown for %s index %u.\""
- "%25s:%-5d EXCEPTION (theResult) [error theResult is an error]: \"AudioObjectGetPropertyData(kAudioDevicePropertyStreams, '%s') failed.\""
- "%25s:%-5d EXCEPTION (theResult) [error theResult is an error]: \"Error %d ('%s') determining the number of stream formats for stream %d\""
- "%25s:%-5d EXCEPTION (theResult) [error theResult is an error]: \"Error %d ('%s') reading the stream formats for stream %d\""
- "%25s:%-5d EXCEPTION (theResult) [error theResult is an error]: \"Error getting property %s on device %u.\""
- "%25s:%-5d Error %d ('%s') determining the number of stream formats for stream %u"
- "%25s:%-5d GetExternalSpeakerDSPChain: Ignoring invalid SpeakerDSPChainType: %d"
- "%25s:%-5d GetHeadsetPlaybackDSPChain: Ignoring invalid HeadsetPlaybackDSPChainType: %d"
- "%25s:%-5d Ignoring invalid volume strategy: %d"
- "%25s:%-5d Stream Format %u: %s."
- "%25s:%-5d The HAL returned a size of %u while we expected %lu"
- "%25s:%-5d The HAL returned fewer stream formats (%u) than were expected (%u)"
- "%25s:%-5d The HAL returned more stream formats (%u) than were expected (%u)"
- "%25s:%-5d failed to read device UID for device %u (status = %d, propSize = %u, uid = %p)"
- "%25s:%-5d getting %s formats for output stream ID %u on device ID %u (uid: \"%@\")."
- "@@ Strips Dec 20 2024 18:13:46"
- "AirPlay audio device returned control list size of 0"
- "Bad ActivePortsFilter passed to function: %u."
- "DeviceSettings_D20Family.cpp"
- "DeviceSettings_D40Family.cpp"
- "Expected %u bytes, got %u bytes instead"
- "ModelManagerMonitor:: exception while executing Task...%@"
- "PlatformUtilities_iOS.cpp"
- "The HAL returned a size of %u while we expected %lu"
- "The HAL returned a size of %u while we expected %u"
- "The HAL returned input stream size of %u"
- "The HAL returned kAudioObjectUnknown for %s index %u."
- "invalid volume strategy: %d"
- "lhs and rhs ranges do not intersect"

```
