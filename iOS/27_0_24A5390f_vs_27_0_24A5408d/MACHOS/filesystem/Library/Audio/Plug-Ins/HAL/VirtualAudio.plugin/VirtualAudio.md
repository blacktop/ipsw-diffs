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
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-1451.108.1.0.0
-  __TEXT.__text: 0x52efb8
-  __TEXT.__realtime: 0x145e4
-  __TEXT.__auth_stubs: 0x2890
+1451.115.0.0.0
+  __TEXT.__text: 0x52ee30
+  __TEXT.__realtime: 0x14908
+  __TEXT.__auth_stubs: 0x28b0
   __TEXT.__objc_stubs: 0xfa0
-  __TEXT.__init_offsets: 0x102c
+  __TEXT.__init_offsets: 0x1034
   __TEXT.__objc_methlist: 0x2c0
-  __TEXT.__const: 0xb13e0
-  __TEXT.__cstring: 0x36be6
-  __TEXT.__gcc_except_tab: 0x5f834
+  __TEXT.__const: 0xb1418
+  __TEXT.__cstring: 0x36b5e
+  __TEXT.__gcc_except_tab: 0x5f90c
   __TEXT.__swift5_typeref: 0x12b
   __TEXT.__swift5_capture: 0x168
-  __TEXT.__oslogstring: 0x56013
+  __TEXT.__oslogstring: 0x56a41
   __TEXT.__objc_methname: 0xdad
   __TEXT.__objc_classname: 0x9d
   __TEXT.__objc_methtype: 0x422

   __TEXT.__dof_VirtualAu: 0x340
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0x14520
+  __TEXT.__unwind_info: 0x14430
   __TEXT.__eh_frame: 0x730
-  __DATA_CONST.__const: 0x294c8
-  __DATA_CONST.__cfstring: 0x2f60
+  __DATA_CONST.__const: 0x28c80
+  __DATA_CONST.__cfstring: 0x2f40
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x1460
+  __DATA_CONST.__auth_got: 0x1470
   __DATA_CONST.__got: 0x510
   __DATA_CONST.__auth_ptr: 0x70
   __DATA.__objc_const: 0x630
   __DATA.__objc_selrefs: 0x4c0
   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0x2b8
-  __DATA.__data: 0x5b0
-  __DATA.__bss: 0x25678
+  __DATA.__data: 0x5a8
+  __DATA.__bss: 0x25628
   __DATA.__common: 0x18
   - /AppleInternal/Library/Frameworks/AudioCapture.framework/AudioCapture
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12360
-  Symbols:   804
-  CStrings:  12081
+  Functions: 12158
+  Symbols:   806
+  CStrings:  12105
 
Symbols:
+ __ZNSt3__120__libcpp_atomic_waitEPVKvx
+ __ZNSt3__123__libcpp_atomic_monitorEPVKv
CStrings:
+ "%25s:%-5d ASSERTION FAILURE: \"DestroyObjects: RoutingMutex must not be held when acquiring the object mutex\""
+ "%25s:%-5d ASSERTION FAILURE: \"UnregisterObject: RoutingMutex must not be held when acquiring the object mutex\""
+ "%25s:%-5d Bluetooth device %u: set %s=1 at publish returned %s (VA will drive SW volume)"
+ "%25s:%-5d EXCEPTION (kAudioHardwareBadObjectError) [!objectAndMutex is true]: \"ExecuteSynchronized: no object with given ID\""
+ "%25s:%-5d EXCEPTION (kAudioHardwareBadObjectError) [!objectAndMutex is true]: \"TryExecuteSynchronized: no object with given ID\""
+ "%25s:%-5d EXCEPTION (std::logic_error) [%s is true]: \"GetVPMicID failed to resolve internal id '%s' (%u)\""
+ "%25s:%-5d FDR data (%lu bytes) is smaller than its header; returning empty ascf::ArrayRef"
+ "%25s:%-5d FDR data (%lu bytes) too small for %u entries of %u bytes; returning empty ascf::ArrayRef"
+ "%25s:%-5d HardwareVolumeControl::GetDefaultVolumeRangeDecibels: mPhysicalDeviceVolumeControl expired; returning empty range."
+ "%25s:%-5d HardwareVolumeControl::GetHardwareVolumeRangeDecibels: mPhysicalDeviceVolumeControl expired; returning empty range."
+ "%25s:%-5d HardwareVolumeControl::GetPropertyData: mPhysicalDeviceVolumeControl expired; skipping."
+ "%25s:%-5d HardwareVolumeControl::GetPropertyDataSize: mPhysicalDeviceVolumeControl expired; returning 0."
+ "%25s:%-5d HardwareVolumeControl::IsMuted: mPhysicalDeviceVolumeControl expired; returning false."
+ "%25s:%-5d HardwareVolumeControl::Mute: mPhysicalDeviceVolumeControl expired; skipping."
+ "%25s:%-5d HardwareVolumeControl::Reconfigure: mPhysicalDeviceVolumeControl expired; skipping."
+ "%25s:%-5d HardwareVolumeControl::SetPropertyData: mPhysicalDeviceVolumeControl expired; skipping."
+ "%25s:%-5d HardwareVolumeControl::Unmute: mPhysicalDeviceVolumeControl expired; skipping."
+ "%25s:%-5d Port_MicrophoneBuiltIn_Aspen::GetPropertyData: owning device expired; skipping."
+ "%25s:%-5d Port_MicrophoneBuiltIn_Aspen::GetPropertyDataSize: owning device expired; returning 0."
+ "%25s:%-5d Port_MicrophoneBuiltIn_Aspen::HasProperty: owning device expired; returning false."
+ "%25s:%-5d Port_MicrophoneBuiltIn_Aspen::IsPropertySettable: owning device expired; returning false."
+ "%25s:%-5d Port_MicrophoneBuiltIn_Aspen::RegisterRelayedListener: owning device expired; returning false."
+ "%25s:%-5d Port_MicrophoneBuiltIn_Aspen::UnregisterRelayedListener: owning device expired; returning false."
+ "%25s:%-5d Removing %s for %s"
+ "%25s:%-5d Route activation failed with %lu optional alternate-VAD route(s) present; retrying activation with them dropped."
+ "%25s:%-5d Route activation failed; optional alternate-VAD route %s was present and will be dropped before retry."
+ "%25s:%-5d SelectedMicUpdater: 'chnl' changed %u -> %u; dispatching change callback"
+ "%25s:%-5d SelectedMicUpdater: observation window expired with no 'chnl' change from baseline=%u"
+ "%25s:%-5d Skipping forwarding volume due to client override."
+ "%25s:%-5d Unpublished VA port %u whose backing core port had already expired (async teardown race)."
+ "%25s:%-5d WeakObjectAdapter::GetPropertyData: wrapped object expired"
+ "%25s:%-5d WeakObjectAdapter::GetPropertyDataSize: wrapped object expired"
+ "%25s:%-5d WeakObjectAdapter::GetUpdatedDescription: wrapped object expired"
+ "%25s:%-5d WeakObjectAdapter::HasProperty: wrapped object expired"
+ "%25s:%-5d WeakObjectAdapter::IsPropertySettable: wrapped object expired"
+ "%25s:%-5d WeakObjectAdapter::RegisterRelayedListener: wrapped object expired"
+ "%25s:%-5d WeakObjectAdapter::SetPropertyData: wrapped object expired"
+ "%25s:%-5d WeakObjectAdapter::UnregisterRelayedListener: wrapped object expired"
+ "@@ Strips Aug  4 2026 11:01:42"
+ "ADAMCallbackQueueKey"
+ "GetVPMicID failed to resolve internal id '%s' (%u)"
+ "HardwareMuteControl.h"
+ "Precondition failure: iter != mContextAttributesMap.cend()"
- "!driverDataSourceID"
- "%25s:%-5d Bluetooth device %u: set %s=1 at publish (VA will drive SW volume)"
- "%25s:%-5d Bluetooth device %u: set %s=1 at publish failed with %s (BT side may not have adopted yet)"
- "%25s:%-5d EXCEPTION (kAudioHardwareBadObjectError) [!hasLock is true]: \"TryExecuteSynchronized: unable to lock object map mutex\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadObjectError) [iter == mObjectMap.cend() is true]: \"ExecuteSynchronized: no object with given ID\""
- "%25s:%-5d EXCEPTION (std::logic_error) [%s is true]: \"Could not find data source %s within ordered data sources\""
- "%25s:%-5d EXCEPTION (std::logic_error) [%s is true]: \"Did not find vp mic id for internal id '%s' (%u)\""
- "%25s:%-5d EXCEPTION (std::logic_error) [%s is true]: \"More than one data source for virtual ID %u\""
- "%25s:%-5d EXCEPTION (std::logic_error) [%s is true]: \"More than one mic for virtual ID %u\""
- "%25s:%-5d Resolved Internal Mic ID:%u to Data Source: %s"
- "%25s:%-5d Using defaults haptic override"
- "@@ Strips Jul 13 2026 21:40:16"
- "Could not find data source %s within ordered data sources"
- "Did not find vp mic id for internal id '%s' (%u)"
- "HapticsExternalPowerAttenuation"
- "More than one data source for virtual ID %u"
- "More than one mic for virtual ID %u"
- "config.mDataSources.size() > 1"
- "driverDataSourceID"
```
