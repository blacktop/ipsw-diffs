## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1364.411.0.0.0
-  __TEXT.__text: 0x513888
-  __TEXT.__auth_stubs: 0x26f0
+1364.531.0.0.0
+  __TEXT.__text: 0x4fd8a8
+  __TEXT.__auth_stubs: 0x2720
   __TEXT.__objc_stubs: 0xb20
   __TEXT.__init_offsets: 0x4e8
   __TEXT.__objc_methlist: 0x124
-  __TEXT.__const: 0xb0c1a
-  __TEXT.__gcc_except_tab: 0x5f0ec
-  __TEXT.__cstring: 0x289ca
-  __TEXT.__objc_classname: 0x34
-  __TEXT.__swift5_typeref: 0x133
+  __TEXT.__const: 0xb0baa
+  __TEXT.__gcc_except_tab: 0x5f538
+  __TEXT.__cstring: 0x288c0
+  __TEXT.__swift5_typeref: 0x131
   __TEXT.__swift5_capture: 0x178
-  __TEXT.__oslogstring: 0x4ec3b
-  __TEXT.__objc_methname: 0x7d4
+  __TEXT.__oslogstring: 0x4eea5
+  __TEXT.__objc_methname: 0x858
+  __TEXT.__objc_classname: 0x6b
+  __TEXT.__objc_methtype: 0x2ba
   __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_reflstr: 0x4c
   __TEXT.__swift5_fieldmd: 0x68

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x28
-  __TEXT.__objc_methtype: 0x241
   __TEXT.__dof_VirtualAu: 0x340
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0x116c8
-  __TEXT.__eh_frame: 0x7a0
-  __DATA_CONST.__auth_got: 0x1390
+  __TEXT.__unwind_info: 0x11898
+  __TEXT.__eh_frame: 0x758
+  __DATA_CONST.__auth_got: 0x13a8
   __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x281c0
-  __DATA_CONST.__cfstring: 0x2e00
+  __DATA_CONST.__const: 0x28240
+  __DATA_CONST.__cfstring: 0x2dc0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10

   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x268
   __DATA.__data: 0x340
-  __DATA.__bss: 0x258f8
+  __DATA.__bss: 0x25a18
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6A128AA0-8EB3-3066-BE63-0281CE474F8D
-  Functions: 11681
-  Symbols:   773
-  CStrings:  11346
+  UUID: 44A7C3E3-2B4C-38F0-98F9-CAE1CF1C7283
+  Functions: 11704
+  Symbols:   776
+  CStrings:  11365
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm
+ _objc_retainAutoreleasedReturnValue
+ _strstr
+ _sysctlbyname
+ _wmemchr
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
CStrings:
+ "        "
+ "%25s:%-5d AudioDidStop: device does not have kAppleEmbeddedAudio_DevicePropertySidetonePlayThru"
+ "%25s:%-5d AudioDidStop: device has kAppleEmbeddedAudio_DevicePropertySidetonePlayThru"
+ "%25s:%-5d Creating sidetone device. isUSBSidetoneEnabled: %d isInputPortSidetoneEnabled: %d"
+ "%25s:%-5d Headset could not be identified based on override identifier: \"%s\". Using default settings."
+ "%25s:%-5d Input injection is enabled on this device"
+ "%25s:%-5d Port_DiscreteSpeaker_Aspen::SetPropertyData() - boot chime volume curve has been generated.The volume curve dB points are %s"
+ "%25s:%-5d Port_DiscreteSpeaker_Aspen::SetPropertyData() - boot chime volume has been written. Incoming ringer volume %.2f, converted decibel value %f, linear volume written to nvram %f"
+ "%25s:%-5d SetPortSubType(MicrophoneWired) to '%s'"
+ "%25s:%-5d Sidetone device has kAppleEmbeddedAudio_DevicePropertySidetonePlayThru"
+ "%25s:%-5d Sidetone device missing kAppleEmbeddedAudio_DevicePropertySidetonePlayThru"
+ "%25s:%-5d SidetoneManager::UpdateHardware"
+ "%25s:%-5d Stored default input volume, setting the input volume on the device"
+ "%25s:%-5d USB::DisableSidetone"
+ "%25s:%-5d Unknown value (%u) for Bluetooth property (%s)"
+ "%25s:%-5d UpdateSampleRate. sidetoneIsEnabled: %d"
+ "%25s:%-5d device has kAppleEmbeddedAudio_DevicePropertySidetonePlayThru"
+ "%25s:%-5d kVirtualAudioPortPropertyBootChimeVolumeCurve is not present on the current sw volume command. This is not an error."
+ "%25s:%-5d setting sidetone enable to %d"
+ "%25s:%-5d sidetone device does not support kAudioDevicePropertySidetoneEQData, could not update the sidetone EQ"
+ "%25s:%-5d trying to enable sidetone"
+ ": [ "
+ "@@ Strips Jan 29 2026 23:39:11"
+ "Audio Loopback"
+ "PAIR: {"
+ "ThirdPartyAudioSwitching"
+ "VAModelManagerAssertion"
+ "VAModelManagerMonitor"
+ "VirtualAudioDevice_"
+ "_off"
+ "_on"
+ "aop-audio-debug=0x40"
+ "inputPortModelUID"
+ "kern.bootargs"
+ "mled.austrip"
+ "outputPortModelUID"
+ "siri"
+ "speaker"
+ "volumelimit"
+ "{ConnectionPropertiesMap={map<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties, std::less<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination>, std::allocator<std::pair<const va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties>>>={__tree<std::__value_type<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties>, std::__map_value_compare<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, std::pair<const va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties>, std::less<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination>>, std::allocator<std::pair<const va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}{map<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties, std::less<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination>, std::allocator<std::pair<const va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties>>>={__tree<std::__value_type<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties>, std::__map_value_compare<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, std::pair<const va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties>, std::less<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination>>, std::allocator<std::pair<const va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}{map<unsigned int, va::ConnectionPropertiesMap::ConnectionProperties, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, va::ConnectionPropertiesMap::ConnectionProperties>>>={__tree<std::__value_type<unsigned int, va::ConnectionPropertiesMap::ConnectionProperties>, std::__map_value_compare<unsigned int, std::pair<const unsigned int, va::ConnectionPropertiesMap::ConnectionProperties>, std::less<unsigned int>>, std::allocator<std::pair<const unsigned int, va::ConnectionPropertiesMap::ConnectionProperties>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}}8@?0"
- "%25s:%-5d EXCEPTION (kAudioHardwareUnspecifiedError): \"Channels CFArray contained a non-UInt32 value.\""
- "%25s:%-5d EXCEPTION (std::logic_error): \"Product supports spatial capture, but does not have graph configuration\""
- "%25s:%-5d EXCEPTION (std::logic_error): \"Unknown value (%u) for Bluetooth property (%s)\""
- "%25s:%-5d EXCEPTION (std::runtime_error): \"Requested stream index is invalid: %u\""
- "%25s:%-5d EXCEPTION (std::runtime_error): \"Unable to create a valid UID for the aggregate device.\""
- "%25s:%-5d Headset could not be identified based on overridde identifier: \"%s\". Using default settings."
- "%25s:%-5d PlaybackDosimetry: invalid volume curve or sensitivity pointers"
- "%25s:%-5d SetPortSubType(MicrophoneWired) to b60f"
- "%25s:%-5d kAudioDevicePropertyPlayThruVolumeDecibels being set to %f"
- "%25s:%-5d kVirtualAudioPortPropertyBootChimeVolumeCurve is either not present or unsettable"
- "%25s:%-5d sidetone device does not support kAudioDevicePropertySidetoneEQData, could not update the sidetone device"
- "@@ Strips Jan 21 2026 00:24:12"
- "Invalid LoggingScope."
- "Product supports spatial capture, but does not have graph configuration"
- "Requested stream index is invalid: %u"
- "Unable to create a valid UID for the aggregate device."
- "Unknown value (%u) for Bluetooth property (%s)"
- "{ConnectionPropertiesMap={map<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties, std::less<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination>, std::allocator<std::pair<const va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties>>>={__tree<std::__value_type<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties>, std::__map_value_compare<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, std::__value_type<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties>, std::less<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination>>, std::allocator<std::__value_type<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}{map<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties, std::less<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination>, std::allocator<std::pair<const va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties>>>={__tree<std::__value_type<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties>, std::__map_value_compare<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, std::__value_type<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties>, std::less<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination>>, std::allocator<std::__value_type<va::ConnectionPropertiesMap::ModeAndSystemAudioEffectsSettingsCombination, va::ConnectionPropertiesMap::PortProperties>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}{map<unsigned int, va::ConnectionPropertiesMap::ConnectionProperties, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, va::ConnectionPropertiesMap::ConnectionProperties>>>={__tree<std::__value_type<unsigned int, va::ConnectionPropertiesMap::ConnectionProperties>, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, va::ConnectionPropertiesMap::ConnectionProperties>, std::less<unsigned int>>, std::allocator<std::__value_type<unsigned int, va::ConnectionPropertiesMap::ConnectionProperties>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}}8@?0"

```
