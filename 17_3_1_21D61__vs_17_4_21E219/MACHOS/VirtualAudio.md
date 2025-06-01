## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1203.4.2.0.0
-  __TEXT.__text: 0x4430e4
-  __TEXT.__auth_stubs: 0x2150
-  __TEXT.__objc_stubs: 0x660
+1203.5.48.30.1
+  __TEXT.__text: 0x4522c4
+  __TEXT.__auth_stubs: 0x21b0
+  __TEXT.__objc_stubs: 0x6c0
   __TEXT.__init_offsets: 0x4a0
   __TEXT.__objc_methlist: 0x128
-  __TEXT.__const: 0xb0453
-  __TEXT.__gcc_except_tab: 0x4551c
-  __TEXT.__oslogstring: 0x4a644
-  __TEXT.__cstring: 0x270ff
-  __TEXT.__objc_methname: 0x76a
+  __TEXT.__const: 0xb04b3
+  __TEXT.__gcc_except_tab: 0x462d0
+  __TEXT.__oslogstring: 0x4ba4b
+  __TEXT.__cstring: 0x2734a
+  __TEXT.__objc_methname: 0x7b4
   __TEXT.__objc_classname: 0x4a
   __TEXT.__objc_methtype: 0x473
   __TEXT.__dof_VirtualAu: 0x303
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualAu0: 0x2aa
-  __TEXT.__unwind_info: 0xe4b8
+  __TEXT.__unwind_info: 0xe550
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x10b8
+  __DATA_CONST.__auth_got: 0x10e8
   __DATA_CONST.__got: 0x388
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x21188
-  __DATA_CONST.__cfstring: 0x3920
+  __DATA_CONST.__const: 0x21838
+  __DATA_CONST.__cfstring: 0x39c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x90
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA.__objc_const: 0x728
-  __DATA.__objc_selrefs: 0x238
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x88
-  __DATA.__objc_superrefs: 0x10
+  __DATA.__objc_selrefs: 0x250
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x4d8
-  __DATA.__bss: 0x1720c
+  __DATA.__bss: 0x1759c
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
+  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 114B6FAA-01CB-32CA-8D04-B757FE1C17C9
-  Functions: 9995
-  Symbols:   679
-  CStrings:  10806
+  UUID: F7A33A22-CC81-3610-B3AC-BF55498BD30C
+  Functions: 10076
+  Symbols:   686
+  CStrings:  10889
 
Symbols:
+ _CFNullGetTypeID
+ _OBJC_CLASS_$_CBProductInfo
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5eraseEmm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignERKS5_mm
+ __ZNSt3__15stoulERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
+ _objc_retain_x24
+ _objc_retain_x27
+ _objc_retain_x28
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE
- ___toupper
CStrings:
+ " does not "
+ "\" : \""
+ "\" }"
+ "%25s:%-5d AOP device is expected but not available."
+ "%25s:%-5d ASSERTION FAILURE: \"Mismatched Policy Values\""
+ "%25s:%-5d Bluetooth profile: %s, active count: %u"
+ "%25s:%-5d Cannot persist VAD; NonShareable ports in route : %s"
+ "%25s:%-5d Changing %s route, active count: %u"
+ "%25s:%-5d ConfigureSecureSpeechDetectionDSP inMode=%u inInitiationContext=%u\n"
+ "%25s:%-5d Configuring silence reset prevention is deprecated. This is now done by default for graphs"
+ "%25s:%-5d Connections are incompatible: %s"
+ "%25s:%-5d Creating a LPMic-Injector output port with UID \"%@\""
+ "%25s:%-5d Default Volume taper command for port %s."
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectCategoryNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForCategory.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectCategoryNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForRouteConfiguration.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectCategoryNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectCategoryNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyActivePortsForCategory.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectCategoryNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyActivePortsForRouteConfiguration.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectCategoryNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyBuiltInPortsForCategory.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectCategoryNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyCategoryInfo.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectCategoryNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyConnectedPortsForCategory.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectCategoryNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyRouteConfigurationIsDisruptive.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectCategoryNotSupportedError): (\"Error setting route configuration via HandlePortUpdate.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectCategoryNotSupportedError): (\"Routing category info lookup failed.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectRoutingNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForCategory.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectRoutingNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyActiveNonQuiesceablePortsForRouteConfiguration.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectRoutingNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectRoutingNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyActivePortsForCategory.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectRoutingNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyActivePortsForRouteConfiguration.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectRoutingNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyBuiltInPortsForCategory.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectRoutingNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyCategoryInfo.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectRoutingNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyConnectedPortsForCategory.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectRoutingNotSupportedError): (\"Error processing kVirtualAudioPlugInPropertyRouteConfigurationIsDisruptive.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectRoutingNotSupportedError): (\"Error setting route configuration via HandlePortUpdate.\")"
+ "%25s:%-5d EXCEPTION (kVirtualAudioObjectRoutingNotSupportedError): (\"Routing category info lookup failed.\")"
+ "%25s:%-5d EXCEPTION (std::logic_error): \"Unsupported Bluetooth profile for %s\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"LPMic-Injector output device has no output streams.\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"SoftwareVolumeCommand does not supports dB to Scalar convertion\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"mCalculatedAPC2Power not initialized; Sending a zero value to AHS!\""
+ "%25s:%-5d Encountered a null stream in AggregateDevice_CommonBase::GetDSPConfigurationUseCases() for device '%@'. Direction: %s, stream index: %u"
+ "%25s:%-5d Get on queue to get initialization state"
+ "%25s:%-5d Headset type for port '%s': %s"
+ "%25s:%-5d No sessions IDs found for context ID %u"
+ "%25s:%-5d No volume command supports Scalar to dB convertion."
+ "%25s:%-5d No volume command supports dB to Scalar convertion."
+ "%25s:%-5d PlugIn initialized ? %d"
+ "%25s:%-5d Port %@ supports PME: %s"
+ "%25s:%-5d Profile %s not found"
+ "%25s:%-5d Reference stream port ? in %s"
+ "%25s:%-5d Request to convert %f dB to scalar."
+ "%25s:%-5d Request to convert %f scalar to dB."
+ "%25s:%-5d Setting BTLE content type %u on device %s"
+ "%25s:%-5d Setting profile for %u to %s (%s)"
+ "%25s:%-5d Software volume mode is not supported on device %s"
+ "%25s:%-5d Software volume supported for Bluetooth device \"%u\": %s"
+ "%25s:%-5d SoftwareVolumeCommand_VolumeTaper_Graph::CancelVolumeRamp()."
+ "%25s:%-5d SoftwareVolumeCommand_VolumeTaper_Graph::EnableWritableSoftwareVolumeProcessors() - %s."
+ "%25s:%-5d SoftwareVolumeCommand_VolumeTaper_Graph::GetMute() - %s."
+ "%25s:%-5d SoftwareVolumeCommand_VolumeTaper_Graph::SetMute() - %s."
+ "%25s:%-5d SoftwareVolumeCommand_VolumeTaper_Graph::SetVolume() - setting volume to %.2f."
+ "%25s:%-5d SoftwareVolumeCommand_VolumeTaper_Graph::SetVolumeRampListener() - callback is %s."
+ "%25s:%-5d SoftwareVolumeCommand_VolumeTaper_Graph::SoftwareVolumeCommand_VolumeTaper_Graph() - creating volume taper command for chain '%s'. Volume command%ssupports volume ramping. Volume command%ssupports unit convertion"
+ "%25s:%-5d SoftwareVolumeCommand_VolumeTaper_Graph::StartVolumeRamp() - target: %.2f upward rate: %.2fms downward rate: %.2fms category: '%s'."
+ "%25s:%-5d SoftwareVolumeCommand_VolumeTaper_Graph::VolumeRampUpdated() - ramp state %s slider position %.2f callback is %s."
+ "%25s:%-5d SoftwareVolumeCommand_VolumeTaper_Graph::convertScalarTodB() Failed to convert %f Scalar to dB. Output value: %f Scalar"
+ "%25s:%-5d SoftwareVolumeCommand_VolumeTaper_Graph::convertScalarTodB() Successfully converted %f scalar to %f dB"
+ "%25s:%-5d SoftwareVolumeCommand_VolumeTaper_Graph::convertdBToScalar() Failed to convert %f dB to scalar. Output value: %f dB"
+ "%25s:%-5d SoftwareVolumeCommand_VolumeTaper_Graph::convertdBToScalar() Successfully converted %f dB to %f scalar."
+ "%25s:%-5d SupportsSoftwareVolume: %d"
+ "%25s:%-5d Unsupported Bluetooth profile %s"
+ "%25s:%-5d VA Init Status: %u"
+ "%25s:%-5d VolumeCommand: Failed to get parameter '%s' to %f on processor type '%s' index %u, err: %s on chain '%s'."
+ "%25s:%-5d VolumeCommand: Failed to get property '%s' on processor type '%s' index %u, err: %s on chain '%s'."
+ "%25s:%-5d VolumeCommand: Failed to set property '%s' on processor type '%s' index %u, err: %s on chain '%s'."
+ "%25s:%-5d creating a USB tap input port with name \"%s\" and UID \"%s\""
+ "@@ Strips Feb 16 2024 22:25:15"
+ "DSPChain.mm"
+ "Device_LPMic_Injector_Aspen.cpp"
+ "EchoCancellationVoice"
+ "ExclaveCapability"
+ "LPMic-Injector"
+ "LPMic-Injector output device has no output streams."
+ "Penrose"
+ "ProfileChangeQueueKey"
+ "RouteUtilities.h"
+ "Secure Muted Talker Detection"
+ "Secure Sound Analysis"
+ "SoftwareVolumeCommand does not supports dB to Scalar convertion"
+ "T@\"NSString\",?,R,C"
+ "Unsupported Bluetooth profile for %s"
+ "VA Initialization Queue"
+ "VirtualAudioDevice_LPMicInjector"
+ "VirtualAudioDevice_SecureMutedTalkerDetection"
+ "VirtualAudioDevice_SecureSoundAnalysis"
+ "dlit"
+ "hlit"
+ "mCalculatedAPC2Power not initialized; Sending a zero value to AHS!"
+ "prefer independent route"
+ "prefer independent route: "
+ "productInfoWithProductID:"
+ "productName"
+ "secure_mtd"
+ "secure_sa"
+ "startup_sequence_change"
+ "stringWithString:"
+ "unkn"
+ "use corrected reference stream offset"
+ "{ \""
- "%25s:%-5d ASSERTION FAILURE: \"Profile %s not found\""
- "%25s:%-5d DeviceActivationReason: %s. Setting BTLE content type %u on device %s"
- "%25s:%-5d EXCEPTION (std::logic_error): \"Unsupported Bluetooth profile %s\""
- "%25s:%-5d EXCEPTION (std::runtime_error): \"mCalculatedAPC2Powe4r not initialized; Sending a zero value to AHS!\""
- "%25s:%-5d Encountered a null stream in %@"
- "%25s:%-5d HasProperty(swsp): %d HasProperty(swen): %d SupportsSoftwareVolume: %d"
- "%25s:%-5d Minimum value for Haptics is %u"
- "%25s:%-5d No NonShareable ports. Route/VAD can persist. (Shared porttypes : %s)"
- "%25s:%-5d Resetting %s route, active count: %u"
- "%25s:%-5d Setting %s active, active count: %u"
- "%25s:%-5d Setting %s inactive, active count: %u"
- "%25s:%-5d Setting %u to %s (%s)"
- "%25s:%-5d Software volume mode (%s) is not supported on device %s"
- "%25s:%-5d SoftwareVolumeCommand_HeadsetVolumeRamping_Graph::CancelVolumeRamp()."
- "%25s:%-5d SoftwareVolumeCommand_HeadsetVolumeRamping_Graph::EnableWritableSoftwareVolumeProcessors() - %s."
- "%25s:%-5d SoftwareVolumeCommand_HeadsetVolumeRamping_Graph::GetMute() - %s."
- "%25s:%-5d SoftwareVolumeCommand_HeadsetVolumeRamping_Graph::SetMute() - %s."
- "%25s:%-5d SoftwareVolumeCommand_HeadsetVolumeRamping_Graph::SetVolume() - setting volume to %.2f."
- "%25s:%-5d SoftwareVolumeCommand_HeadsetVolumeRamping_Graph::SetVolumeRampListener() - callback is %s."
- "%25s:%-5d SoftwareVolumeCommand_HeadsetVolumeRamping_Graph::SoftwareVolumeCommand_HeadsetVolumeRamping_Graph() - creating ramped volume command for chain '%s'."
- "%25s:%-5d SoftwareVolumeCommand_HeadsetVolumeRamping_Graph::StartVolumeRamp() - target: %.2f upward rate: %.2fms downward rate: %.2fms category: '%s'."
- "%25s:%-5d SoftwareVolumeCommand_HeadsetVolumeRamping_Graph::VolumeRampUpdated() - ramp state %s slider position %.2f callback is %s."
- "%25s:%-5d Unknown Bluetooth productID : %u."
- "@@ Strips Dec 20 2023 19:47:54"
- "C"
- "DSPChain.cpp"
- "DeviceInfo Listener Queue"
- "Unsupported Bluetooth profile %s"
- "_b204"
- "mCalculatedAPC2Powe4r not initialized; Sending a zero value to AHS!"

```
