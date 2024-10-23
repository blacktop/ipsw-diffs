## CoreAudio

> `/System/Library/Frameworks/CoreAudio.framework/CoreAudio`

```diff

-328.204.30.1.0
-  __TEXT.__text: 0x50dc60
-  __TEXT.__auth_stubs: 0x2b00
+328.328.0.0.0
+  __TEXT.__text: 0x521b70
+  __TEXT.__auth_stubs: 0x2b30
   __TEXT.__objc_methlist: 0xf94
-  __TEXT.__gcc_except_tab: 0x55250
-  __TEXT.__const: 0x4c918
-  __TEXT.__oslogstring: 0x3bca6
-  __TEXT.__cstring: 0x2ac8f
-  __TEXT.__unwind_info: 0x17f40
+  __TEXT.__gcc_except_tab: 0x57f94
+  __TEXT.__const: 0x4cc38
+  __TEXT.__oslogstring: 0x3c3a6
+  __TEXT.__cstring: 0x2adaa
+  __TEXT.__unwind_info: 0x18098
   __TEXT.__objc_classname: 0x353
   __TEXT.__objc_methname: 0x38ca
   __TEXT.__objc_methtype: 0x3cee
   __TEXT.__objc_stubs: 0x1e60
   __DATA_CONST.__got: 0x460
-  __DATA_CONST.__const: 0x6328
+  __DATA_CONST.__const: 0x63b8
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_selrefs: 0x9c0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x1590
+  __AUTH_CONST.__auth_got: 0x15a8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x2efe8
-  __AUTH_CONST.__cfstring: 0x3800
+  __AUTH_CONST.__const: 0x2f140
+  __AUTH_CONST.__cfstring: 0x3860
   __AUTH_CONST.__objc_const: 0x2738
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x118
-  __DATA.__data: 0x758
-  __DATA.__bss: 0x1e78
+  __DATA.__data: 0x770
+  __DATA.__bss: 0x1eb8
   __DATA_DIRTY.__objc_data: 0x5a0
   __DATA_DIRTY.__data: 0x228
-  __DATA_DIRTY.__bss: 0x14a8
+  __DATA_DIRTY.__bss: 0x1478
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 17583
-  Symbols:   19002
-  CStrings:  7165
+  Functions: 17624
+  Symbols:   19046
+  CStrings:  7199
 
Symbols:
+ __ZN4AMCP13Feature_Flags36allow_unified_device_engine_replacerEv
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEb
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEf
+ _objc_sync_enter
+ _objc_sync_exit
- _fputs
CStrings:
+ " Out: "
+ "%!s(MISSING):%!d(MISSING)  \nHALS_ObjectMap::_Dump: ->"
+ "%!s(MISSING):%!d(MISSING)    %!d(MISSING) Objects"
+ "%!s(MISSING):%!d(MISSING)    No Object List"
+ "%!s(MISSING):%!d(MISSING)    No Objects"
+ "%!s(MISSING):%!d(MISSING)    Object ID: %!d(MISSING) | Class: '%!s(MISSING)' | Base Class: '%!s(MISSING)' | Ref: %!l(MISSING)ld"
+ "%!s(MISSING):%!d(MISSING)  ADS::Device::Device_GetPropertyData: not enough space for the return value of kAudioFakeDevicePropertyIOThreadStateChangeCallback for the device"
+ "%!s(MISSING):%!d(MISSING)  ADS::Device::Device_SetPropertyData: wrong size for the data for kAudioFakeDevicePropertyIOThreadStateChangeCallback"
+ "%!s(MISSING):%!d(MISSING)  HALB_TailspinImpl::dumpTailspin: Looking back %!l(MISSING)ld ms to time %!l(MISSING)lu"
+ "%!s(MISSING):%!d(MISSING)  HALB_TailspinImpl::dumpTailspin: Looking forward %!l(MISSING)ld ms to time %!l(MISSING)lu"
+ "%!s(MISSING):%!d(MISSING)  HALS_ObjectMap::_Dump: <-\n"
+ "%!s(MISSING):%!d(MISSING)  HALS_PlugInDevice::GetPropertyData: bad property data size for kAudioDeviceEngineReplacerIsEnabled"
+ "%!s(MISSING):%!d(MISSING)  HALS_PlugInDevice::GetPropertyData: bad property data size for kAudioDeviceEngineReplacerUID"
+ "%!s(MISSING):%!d(MISSING)  HALS_PlugInDevice::GetPropertyData: does not support property kAudioDeviceEngineReplacerIsEnabled"
+ "%!s(MISSING):%!d(MISSING)  HALS_PlugInDevice::GetPropertyData: does not support property kAudioDeviceEngineReplacerUID"
+ "%!s(MISSING):%!d(MISSING)  Simulator_AddRef: out of isolated references"
+ "%!u(MISSING) %!s(MISSING):%!d(MISSING) Allow unified device engine replacer"
+ "%!u(MISSING) %!s(MISSING):%!d(MISSING) Disallow unified device engine replacer"
+ "%!u(MISSING) %!s(MISSING):%!d(MISSING) Failed to reassses the composition when engine replacer changed"
+ "%!u(MISSING) %!s(MISSING):%!d(MISSING) The engine replacer input format differs from this device"
+ "%!u(MISSING) %!s(MISSING):%!d(MISSING) The engine replacer number of streams differs from this device"
+ "%!u(MISSING) %!s(MISSING):%!d(MISSING) The engine replacer output format differs from this device"
+ "%!u(MISSING) %!s(MISSING):%!d(MISSING) Throwing Exception: %!s(MISSING) Failed to find IOThread, io ipc info not found, context id %!l(MISSING)u"
+ "%!u(MISSING) %!s(MISSING):%!d(MISSING) Throwing Exception: %!s(MISSING) Invalid nominal sample rate"
+ "%!u(MISSING) %!s(MISSING):%!d(MISSING) Throwing Exception: %!s(MISSING) Setting priveleged property failed"
+ "%!u(MISSING) %!s(MISSING):%!d(MISSING) [hal_dsp] Adding reference candidate with (Device ID: %!u(MISSING))"
+ "%!u(MISSING) %!s(MISSING):%!d(MISSING) _WriteToStream_CommitTrailingSilence: the context (%!u(MISSING)) cannot commit trailing silence, max size is 0, wants to commit %!d(MISSING), rb size is %!d(MISSING)"
+ "%!u(MISSING) %!s(MISSING):%!d(MISSING) _WriteToStream_CommitTrailingSilence: the context (%!u(MISSING)), context is too far behind, updating write position by %!d(MISSING) frames, max size %!d(MISSING), rb size %!d(MISSING)"
+ "Allow unified device engine replacer: %!d(MISSING)"
+ "AudioAccessoryFeatures"
+ "Base Class:             "
+ "Box "
+ "Bundle ID: "
+ "Bundle ID:               "
+ "Class:                  "
+ "Client "
+ "Client ID:      "
+ "Client: "
+ "Clock Device "
+ "Clock Domain:        "
+ "Clock Domain:          "
+ "Codec Device: "
+ "Context ID"
+ "Control "
+ "Current Physical Format: "
+ "Current Virtual Format:  "
+ "Device "
+ "Device %!u(MISSING), Context %!u(MISSING)\n%!s(MISSING)"
+ "Device Description"
+ "Device Manager "
+ "Device: "
+ "Direction:               "
+ "Element:                "
+ "Error encountered while reading register data for register address "
+ "Event"
+ "Failed to find IOThread, io ipc info not found"
+ "Has Audio:            "
+ "Has MIDI:             "
+ "Has Video:            "
+ "IO Context "
+ "IO Thread Name: "
+ "Invalid nominal sample rate"
+ "Is Acquired:          "
+ "Is Active:               "
+ "Is Hidden:           "
+ "Is Hidden:             "
+ "Is Protected:         "
+ "Is Running:     "
+ "Isolated Use Case"
+ "Latency                In: "
+ "Latency              In: "
+ "Left Channel:           "
+ "Max Value:              "
+ "Max dB Value:           "
+ "Min Value:              "
+ "Min dB Value:           "
+ "Name:                "
+ "Name:                 "
+ "Name:                  "
+ "Nominal Sample Rate: "
+ "Nominal Sample Rate:   "
+ "Number "
+ "Number Clock Devices: "
+ "Number Controls:       "
+ "Number Devices:       "
+ "Number Selector Values: "
+ "Number of Boxes:         "
+ "Number of Clients: "
+ "Number of Clock Devices: "
+ "Number of Device Managers: "
+ "Number of Devices:       "
+ "Number of IO Contexts: "
+ "Opted Out: "
+ "PID:       "
+ "Right Channel:          "
+ "Safety Offset          In: "
+ "Scalar Value:           "
+ "Scope:                  "
+ "Setting priveleged property failed"
+ "Starting Channel:        "
+ "Stream "
+ "Time: "
+ "Transport Type:      "
+ "Transport Type:       "
+ "Transport Type:        "
+ "UID:                 "
+ "UID:                  "
+ "UID:                   "
+ "USBCUnifiedDevice"
+ "Unified Device Engine Replacer"
+ "Value:                  "
+ "Volume Scalar: "
+ "dB Value:               "
+ "inNominalSampleRate <= 0.0"
+ "policy != SettabilityPolicy::IgnoreSettability"
+ "virtual int HALS_IOUAEngine::_WriteToStream_Write(AudioObjectID, HALS_IOEngine2_StreamInfo &, const AudioServerPlugInIOCycleInfo &, UInt32, const HALS_BufferInfo &)"
+ "virtual void HALS_IOUAEngine::_ReadFromStream_Read(AudioObjectID, HALS_IOEngine2_StreamInfo &, const AudioServerPlugInIOCycleInfo &, UInt32, const HALS_BufferInfo &)"
+ "void ADS::Device::Device_SetPropertyData(AudioObjectID, pid_t, const AudioObjectPropertyAddress &, UInt32, const void *, UInt32, const void *, UInt32 &, std::vector<AudioObjectPropertyAddress> &, SettabilityPolicy)"
- " %!u(MISSING)->%!s(MISSING)"
- "%!s(MISSING):%!d(MISSING)  HALB_TailspinImpl::dumpTailspin: Looking back %!l(MISSING)lu ms to time %!l(MISSING)lu"
- "%!s(MISSING):%!d(MISSING)  HALB_TailspinImpl::dumpTailspin: Looking forward %!l(MISSING)lu ms to time %!l(MISSING)lu"
- "%!s(MISSING):%!d(MISSING)  Simulator_Release: bad driver reference"
- "%!s(MISSING):%!d(MISSING)  Simulator_Release: out of references"
- "%!u(MISSING) %!s(MISSING):%!d(MISSING) Throwing Exception: %!s(MISSING) Failed to unregister IOThread, io ipc info not found, context id %!l(MISSING)u"
- "%!u(MISSING) %!s(MISSING):%!d(MISSING) _WriteToStream_CommitTrailingSilence: the context (%!u(MISSING)), context is too far behind, updating write position by %!d(MISSING) frames"
- "Base Class:             '%!s(MISSING)'\n"
- "Box %!u(MISSING)\n"
- "Bundle ID:               %!s(MISSING)\n"
- "Bundle ID: %!s(MISSING)\n"
- "Class:                  '%!s(MISSING)'\n"
- "Client %!u(MISSING)\n"
- "Client ID:      %!u(MISSING)\n"
- "Client: %!u(MISSING)l\n"
- "Clock Device %!u(MISSING)\n"
- "Clock Domain:          %!u(MISSING)\n"
- "Clock Domain:        %!u(MISSING)\n"
- "Codec Device: %!s(MISSING)\n"
- "Control %!u(MISSING)\n"
- "Current Physical Format: %!s(MISSING)\n"
- "Current Virtual Format:  %!s(MISSING)\n"
- "Device %!u(MISSING)\n"
- "Device Manager %!u(MISSING)\n"
- "Device: %!u(MISSING)\n"
- "Direction:               %!s(MISSING)\n"
- "Element:                %!d(MISSING)\n"
- "Error encountered while reading register data for register address %!x(MISSING)\n"
- "Has Audio:            %!s(MISSING)\n"
- "Has MIDI:             %!s(MISSING)\n"
- "Has Video:            %!s(MISSING)\n"
- "IO Context %!u(MISSING)\n"
- "IO Thread Name: %!s(MISSING)\n"
- "Is Acquired:          %!s(MISSING)\n"
- "Is Active:               %!s(MISSING)\n"
- "Is Hidden:             %!s(MISSING)\n"
- "Is Hidden:           %!s(MISSING)\n"
- "Is Protected:         %!s(MISSING)\n"
- "Is Running:     %!s(MISSING)\n"
- "Latency                In: %!u(MISSING) Out: %!u(MISSING)\n"
- "Latency              In: %!u(MISSING) Out: %!u(MISSING)\n"
- "Left Channel:           %!u(MISSING)\n"
- "Max Value:              %!u(MISSING)\n"
- "Max dB Value:           %!f(MISSING)\n"
- "Min Value:              %!u(MISSING)\n"
- "Min dB Value:           %!f(MISSING)\n"
- "Name:                  %!s(MISSING)\n"
- "Name:                 %!s(MISSING)\n"
- "Name:                %!s(MISSING)\n"
- "Nominal Sample Rate:   %!f(MISSING)\n"
- "Nominal Sample Rate: %!f(MISSING)\n"
- "Number %!s(MISSING) %!l(MISSING)u\n"
- "Number Clock Devices: %!u(MISSING)\n"
- "Number Controls:       %!l(MISSING)u\n"
- "Number Devices:       %!u(MISSING)\n"
- "Number Selector Values: %!u(MISSING)\n"
- "Number of Boxes:         %!l(MISSING)u\n"
- "Number of Clients: %!l(MISSING)u\n"
- "Number of Clock Devices: %!l(MISSING)u\n"
- "Number of Device Managers: %!l(MISSING)u\n"
- "Number of Devices:       %!l(MISSING)u\n"
- "Number of IO Contexts: %!l(MISSING)u\n"
- "Opted Out: %!u(MISSING)\n"
- "PID:       %!u(MISSING)\n"
- "Right Channel:          %!u(MISSING)\n"
- "Safety Offset          In: %!u(MISSING) Out: %!u(MISSING)\n"
- "Scalar Value:           %!f(MISSING)\n"
- "Scope:                  '%!s(MISSING)'\n"
- "Starting Channel:        %!u(MISSING)\n"
- "Stream %!u(MISSING)\n"
- "Time: %!s(MISSING)\n"
- "Transport Type:        '%!s(MISSING)'\n"
- "Transport Type:       '%!s(MISSING)'\n"
- "Transport Type:      '%!s(MISSING)'\n"
- "UID:                   %!s(MISSING)\n"
- "UID:                  %!s(MISSING)\n"
- "UID:                 %!s(MISSING)\n"
- "Value:                  %!f(MISSING)\n"
- "Value:                  %!s(MISSING)\n"
- "Value:                  %!u(MISSING)\n"
- "Volume Scalar: %!l(MISSING)f\n"
- "dB Value:               %!f(MISSING)\n"
- "virtual int HALS_IOUAEngine::_BeginReading(AudioObjectID, UInt32, const HALS_IOEngineInfo &)"
- "virtual int HALS_IOUAEngine::_EndWriting(AudioObjectID, UInt32, const HALS_IOEngineInfo &)"

```
