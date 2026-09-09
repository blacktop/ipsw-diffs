## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__dof_VirtualAu`
- `__TEXT.__dof_Aggregate`
- `__TEXT.__dof_VirtualA0`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

 1451.115.30.0.0
-  __TEXT.__text: 0x530ae8
-  __TEXT.__realtime: 0x14908
-  __TEXT.__auth_stubs: 0x28b0
-  __TEXT.__objc_stubs: 0xfa0
-  __TEXT.__init_offsets: 0x1034
+  __TEXT.__text: 0x5477f4
+  __TEXT.__realtime: 0x14ab0
+  __TEXT.__auth_stubs: 0x29b0
+  __TEXT.__objc_stubs: 0x12a0
+  __TEXT.__init_offsets: 0x1048
   __TEXT.__objc_methlist: 0x2c0
-  __TEXT.__const: 0xb1418
-  __TEXT.__cstring: 0x36bce
-  __TEXT.__gcc_except_tab: 0x5fbb0
+  __TEXT.__const: 0xb4918
+  __TEXT.__cstring: 0x375c2
+  __TEXT.__gcc_except_tab: 0x611d0
   __TEXT.__swift5_typeref: 0x12b
   __TEXT.__swift5_capture: 0x168
-  __TEXT.__oslogstring: 0x56cb8
-  __TEXT.__objc_methname: 0xdad
+  __TEXT.__oslogstring: 0x58164
+  __TEXT.__objc_methname: 0xf99
   __TEXT.__objc_classname: 0x9d
   __TEXT.__objc_methtype: 0x422
   __TEXT.__constg_swiftt: 0xf8

   __TEXT.__dof_VirtualAu: 0x340
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0x14480
+  __TEXT.__unwind_info: 0x14a20
   __TEXT.__eh_frame: 0x730
-  __DATA_CONST.__const: 0x28d10
-  __DATA_CONST.__cfstring: 0x2f40
+  __DATA_CONST.__const: 0x294d8
+  __DATA_CONST.__cfstring: 0x2fa0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x1470
-  __DATA_CONST.__got: 0x510
+  __DATA_CONST.__auth_got: 0x14f0
+  __DATA_CONST.__got: 0x530
   __DATA_CONST.__auth_ptr: 0x70
   __DATA.__objc_const: 0x630
-  __DATA.__objc_selrefs: 0x4c0
+  __DATA.__objc_selrefs: 0x580
   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0x2b8
-  __DATA.__data: 0x5a8
+  __DATA.__data: 0x5b0
   __DATA.__common: 0x18
   - /AppleInternal/Library/Frameworks/AudioCapture.framework/AudioCapture
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12180
-  Symbols:   806
-  CStrings:  12114
+  Functions: 12452
+  Symbols:   827
+  CStrings:  12292
 
Symbols:
+ _NSClassFromString
+ _OBJC_CLASS_$_CMDeviceStateEvent
+ _OBJC_CLASS_$_CMDeviceStateManager
+ _OBJC_CLASS_$_NSOperationQueue
+ __ZNKSt13runtime_error4whatEv
+ __ZNSt3__123__cxx_atomic_notify_allEPVKv
+ __ZNSt3__16localeC1ERKS0_
+ __ZNSt3__16localeaSERKS0_
+ __ZNSt3__18numpunctIcE2idE
+ __ZNSt3__18to_charsEPcS0_d
+ __ZNSt3__18to_charsEPcS0_dNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_dNS_12chars_formatEi
+ __ZNSt3__18to_charsEPcS0_e
+ __ZNSt3__18to_charsEPcS0_eNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_eNS_12chars_formatEi
+ __ZNSt3__18to_charsEPcS0_f
+ __ZNSt3__18to_charsEPcS0_fNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_fNS_12chars_formatEi
+ ___atomic_load
+ ___atomic_store
+ ___umodti3
CStrings:
+ " does not allow the "
+ " formatting argument"
+ " option"
+ "%25s:%-5d ASSERTION FAILURE: \"AngleStateManager::TheInstance() called before Create()\""
+ "%25s:%-5d ASSERTION FAILURE: \"DeviceStateManager::TheInstance() called before SetInstance()\""
+ "%25s:%-5d ASSERTION FAILURE: \"Expected HapticAttenuationIODelegate to be non-null!\""
+ "%25s:%-5d ASSERTION FAILURE: \"Expected at most one HapticAttenuationIODelegate!\""
+ "%25s:%-5d AngleStateManager created"
+ "%25s:%-5d AngleStateManager destroyed"
+ "%25s:%-5d AngleStateManager: CMAngleManager is not available on this device"
+ "%25s:%-5d AngleStateManager: Callback cleared"
+ "%25s:%-5d AngleStateManager: Callback registered"
+ "%25s:%-5d AngleStateManager: Close trigger at %.1f degrees — serializing close route change"
+ "%25s:%-5d AngleStateManager: Open trigger at %.1f degrees (velocity=%.1f deg/s%s) — serializing open route change"
+ "%25s:%-5d AngleStateManager: Started monitoring (interval=%.2fs)"
+ "%25s:%-5d AngleStateManager: Stopped monitoring"
+ "%25s:%-5d AngleStateManager::Impl created"
+ "%25s:%-5d AngleStateManager::Impl destroyed"
+ "%25s:%-5d Applying device state tuning for device '%s' with state: %s"
+ "%25s:%-5d Bad event sent from CMDeviceStateEvent!"
+ "%25s:%-5d Close transition — suppressing Speaker override (panic-close window active or no audio since route became Receiver-capable)"
+ "%25s:%-5d DSPChain '%s': attached HapticAttenuationIODelegate"
+ "%25s:%-5d Device state changed"
+ "%25s:%-5d DeviceStateHandler: New Receiver-capable route while device open — starting rapid transition timer"
+ "%25s:%-5d DeviceStateHandler: Rapid transition timer started (3s window)"
+ "%25s:%-5d DeviceStateManager created"
+ "%25s:%-5d DeviceStateManager destroyed"
+ "%25s:%-5d DeviceStateManager: BookMicBlocked transition %s -> %s (pose held at %s)"
+ "%25s:%-5d DeviceStateManager: CMDeviceStateManager is not available on this device"
+ "%25s:%-5d DeviceStateManager: Callback registered"
+ "%25s:%-5d DeviceStateManager: Callback removed"
+ "%25s:%-5d DeviceStateManager: Error in device state update: %@"
+ "%25s:%-5d DeviceStateManager: StablePose transition %s -> %s"
+ "%25s:%-5d DeviceStateManager: StableState callback %s"
+ "%25s:%-5d DeviceStateManager: Started monitoring"
+ "%25s:%-5d DeviceStateManager: Stopped monitoring"
+ "%25s:%-5d DeviceStateManager: Tuning transition %s -> %s (bookMicBlocked=%s)"
+ "%25s:%-5d DeviceStateManager: propertyA=%@ propertyB=%@ propertyC=%@ propertyD=%@"
+ "%25s:%-5d DeviceStateManager::Impl created"
+ "%25s:%-5d DeviceStateManager::Impl destroyed"
+ "%25s:%-5d EXCEPTION (std::logic_error) [%s is true]: \"sAngleStateManager is not nullptr!\""
+ "%25s:%-5d EXCEPTION (std::logic_error) [sAngleStateManager is NULL]: \"sAngleStateManager is nullptr!\""
+ "%25s:%-5d EXCEPTION (std::logic_error): \"Invalid ActuatorDatabaseType in platform attributes\""
+ "%25s:%-5d Failed to set 'tmgp' to %u (%s) on %s chain '%s': %s"
+ "%25s:%-5d HandleDeviceStateUpdate invoked"
+ "%25s:%-5d HapticAttenuationIODelegate created for Actuator VAD"
+ "%25s:%-5d HapticAttenuationIODelegate: Applying %s%s attenuation (dB=%.2f, upSmooth=%.3fs, downSmooth=%.3fs)"
+ "%25s:%-5d HapticAttenuationIODelegate: Applying %s%s attenuation (dB=%.2f, upSmooth=%.3fs, downSmooth=%.3fs, new source)"
+ "%25s:%-5d HapticAttenuationIODelegate: Bootstrap Angle=%s"
+ "%25s:%-5d HapticAttenuationIODelegate: Bootstrap ChargingPad state=%s attenuation=%.2f dB"
+ "%25s:%-5d HapticAttenuationIODelegate: Bootstrap StablePose state=%s"
+ "%25s:%-5d HapticAttenuationIODelegate: Coordinator active (subscriptions set)"
+ "%25s:%-5d HapticAttenuationIODelegate: Coordinator inactive (subscriptions cleared)"
+ "%25s:%-5d HapticAttenuationIODelegate: Error %u setting UserGainDecibels DSP parameter"
+ "%25s:%-5d HapticAttenuationIODelegate: Error %u setting VolumeDecaySmoothTime DSP parameter"
+ "%25s:%-5d HapticAttenuationIODelegate: Error %u setting VolumeSmoothTime DSP parameter"
+ "%25s:%-5d HapticAttenuationIODelegate: Maximum attenuation applied in this session was for %s%s (dB=%.2f)"
+ "%25s:%-5d HapticAttenuationIODelegate: No attenuation applied in this session"
+ "%25s:%-5d HapticAttenuationIODelegate: SetChargingPadAttenuation %s (attenuation=%.2f dB)"
+ "%25s:%-5d HapticAttenuationIODelegate: VolumeDecaySmoothTime is now %.3f sec (winner change)"
+ "%25s:%-5d HapticAttenuationIODelegate: VolumeSmoothTime is now %.3f sec (winner change)"
+ "%25s:%-5d HapticAttenuationIODelegate: haptics IO restarted before HandleIOWillStop's delayed clear, maintaining subscriptions"
+ "%25s:%-5d Non-NULL IO start on Default VAD — restarting rapid transition timer from IO start"
+ "%25s:%-5d Open transition while routed to Receiver — starting rapid transition timer"
+ "%25s:%-5d PV_ExecuteHingeStateChange: Unhandled hinge state for latch unwind"
+ "%25s:%-5d Port_MicrophoneBuiltIn_Aspen: DSP reported mic channel %u but no built-in SubPortDescription resolves for it — falling through to routing default"
+ "%25s:%-5d Port_MicrophoneBuiltIn_Aspen::GetActiveSubPort: returning DSP-selected SubPort '%s' (channel %u)"
+ "%25s:%-5d SelectedMicDSPUpdateCommand: dispatching route update (mic swap detected via 'chnl')"
+ "%25s:%-5d SelectedMicUpdater::Arm - baseline=%u, window=%llu ms, poll=%llu ms"
+ "%25s:%-5d Set 'tmgp' to %u (%s) on %s chain '%s'"
+ "%25s:%-5d Setting internal overridden port(s): %s"
+ "%25s:%-5d UpdateHapticsPower: deferring to HapticAttenuationIODelegate (active=%d attenuation=%.2f dB)"
+ "%25s:%-5d VirtualAudio_PlugIn::HandlePoseStateChange: New state: %s, bookMicBlocked: %s"
+ ", predicted"
+ "01"
+ "01234567"
+ "0123456789abcdef"
+ "0123456789abcdefghijklmnopqrstuvwxyz"
+ "0B"
+ "0X"
+ "0b"
+ "0x"
+ "={:.1f}°"
+ "@@ Strips Aug  8 2026 18:42:51"
+ "An argument index may not have a negative value"
+ "AngleStateManager.mm"
+ "CMAngleManager"
+ "DeviceStateCommands.cpp"
+ "DeviceStateHandler.cpp"
+ "DeviceStateManager.mm"
+ "End of input while parsing an argument index"
+ "End of input while parsing format specifier precision"
+ "HapticAttenuationIODelegate.mm"
+ "Hinge state route change"
+ "Integral value outside the range of the char type"
+ "Invalid ActuatorDatabaseType in platform attributes"
+ "Invariant failure: CategoryHasReceiverRoute(mCurrentCategoryMode.mCategory)"
+ "Replacement argument isn't a standard signed or unsigned integer type"
+ "Selected input mic (DSP swap) route update"
+ "The argument index is invalid"
+ "The argument index should end with a ':' or a '}'"
+ "The argument index starts with an invalid character"
+ "The argument index value is too large for the number of arguments supplied"
+ "The fill option contains an invalid value"
+ "The format specifier contains malformed Unicode characters"
+ "The format specifier for "
+ "The format specifier should consume the input or end with a '}'"
+ "The format string contains an invalid escape sequence"
+ "The format string terminates at a '{'"
+ "The numeric value of the format specifier is too large"
+ "The precision option does not contain a value or an argument index"
+ "The replacement field misses a terminating '}'"
+ "The type does not fit in the mask"
+ "The type option contains an invalid value for "
+ "The type option contains an invalid value for a string formatting argument"
+ "The value of the argument index exceeds its maximum value"
+ "The width option should not have a leading zero"
+ "Using automatic argument numbering in manual argument numbering mode"
+ "Using manual argument numbering in automatic argument numbering mode"
+ "\\'"
+ "\\u{"
+ "\\x{"
+ "a bool"
+ "a character"
+ "a floating-point"
+ "a pointer"
+ "alternate form"
+ "an integer"
+ "angleDegrees"
+ "com.apple.virtualaudio.anglestate"
+ "com.apple.virtualaudio.devicestate"
+ "com.apple.virtualaudio.hapticattenuationiodelegate"
+ "device_hinge_extra_angle_degrees"
+ "device_hinge_extra_angular_velocity"
+ "device_hinge_extra_predicted_action"
+ "device_hinge_state"
+ "device_hinge_state_action"
+ "device_mp_extra_angle_degrees"
+ "device_mp_extra_derived_open_state"
+ "device_mp_extra_derived_stable"
+ "device_mp_state"
+ "device_mp_state_book_mic_blocked"
+ "device_mp_state_stable"
+ "inactive"
+ "infnanINFNAN"
+ "isAngleValid"
+ "isAvailable"
+ "isVelocityValid"
+ "localizedDescription"
+ "mechanicalAngleDegrees"
+ "nullptr != sAngleStateManager"
+ "precision"
+ "propertyA"
+ "propertyB"
+ "propertyC"
+ "propertyD"
+ "registered"
+ "removed"
+ "sAngleStateManager is not nullptr!"
+ "sAngleStateManager is nullptr!"
+ "setAngleUpdateInterval:"
+ "setName:"
+ "setQualityOfService:"
+ "sign"
+ "startAngleUpdatesToQueue:handler:"
+ "startUpdatesToQueue:withHandler:"
+ "state"
+ "stopAngleUpdates"
+ "stopUpdates"
+ "stringForDeviceStatePropertyAType:"
+ "stringForDeviceStatePropertyBType:"
+ "stringForDeviceStatePropertyCType:"
+ "stringForDeviceStatePropertyDType:"
+ "v16@?0@\"CMAngle\"8"
+ "v24@?0@\"CMDeviceStateEvent\"8@\"NSError\"16"
+ "velocityDegreesPerSeconds"
+ "waitUntilAllOperationsAreFinished"
+ "zero-padding"
+ "{:.1f}°"
- "@@ Strips Aug  9 2026 03:26:56"
```
