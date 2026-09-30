## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1364.536.0.0.0
-  __TEXT.__text: 0x4fdb1c
+1364.539.0.0.0
+  __TEXT.__text: 0x501930
   __TEXT.__auth_stubs: 0x27d0
   __TEXT.__objc_stubs: 0xb20
   __TEXT.__init_offsets: 0x4e8
   __TEXT.__objc_methlist: 0x124
   __TEXT.__const: 0xb0bca
-  __TEXT.__gcc_except_tab: 0x5f2f8
+  __TEXT.__gcc_except_tab: 0x5f5d8
   __TEXT.__cstring: 0x28895
   __TEXT.__swift5_typeref: 0x131
   __TEXT.__swift5_capture: 0x178
-  __TEXT.__oslogstring: 0x4f0a4
+  __TEXT.__oslogstring: 0x4e676
   __TEXT.__objc_methname: 0x858
   __TEXT.__objc_classname: 0x6b
   __TEXT.__objc_methtype: 0x2ba

   __TEXT.__dof_VirtualAu: 0x340
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0x11860
+  __TEXT.__unwind_info: 0x119a8
   __TEXT.__eh_frame: 0x758
   __DATA_CONST.__auth_got: 0x1400
   __DATA_CONST.__got: 0x4e8
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x282c8
+  __DATA_CONST.__const: 0x28988
   __DATA_CONST.__cfstring: 0x2dc0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 92CE0F41-62E2-345B-B4AF-ADCF3D266F07
-  Functions: 11713
+  UUID: 9ADD10FC-C201-3CFB-AE39-D9B22B6DB5F4
+  Functions: 11882
   Symbols:   788
-  CStrings:  11367
+  CStrings:  11350
 
CStrings:
+ "%25s:%-5d Attempting to set clock %@ sampling rate to %f prior to configuring aggregate"
+ "%25s:%-5d Could not update clock %@ sample rate to %f Hz. Error code '%s'"
+ "%25s:%-5d Error %s setting fixed buffer frame size to %u"
+ "%25s:%-5d Setting device %@ sample rate to %f after format update"
+ "%25s:%-5d Stream is configured for Atmos, fixing buffer frame size to %u"
+ "@@ Strips Feb 23 2026 03:02:03"
- "%25s:%-5d EXCEPTION (kAudioHardwareBadDeviceError) [theDevice is NULL]: \"HP_HardwarePlugIn_DeviceAddIOProc: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadDeviceError) [theDevice is NULL]: \"HP_HardwarePlugIn_DeviceCreateIOProcID: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadDeviceError) [theDevice is NULL]: \"HP_HardwarePlugIn_DeviceCreateIOProcIDWithBlock: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadDeviceError) [theDevice is NULL]: \"HP_HardwarePlugIn_DeviceCreateIOProcIDWithClockedProc: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadDeviceError) [theDevice is NULL]: \"HP_HardwarePlugIn_DeviceGetCurrentTime: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadDeviceError) [theDevice is NULL]: \"HP_HardwarePlugIn_DeviceGetNearestStartTime: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadDeviceError) [theDevice is NULL]: \"HP_HardwarePlugIn_DeviceRead: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadDeviceError) [theDevice is NULL]: \"HP_HardwarePlugIn_DeviceRemoveIOProc: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadDeviceError) [theDevice is NULL]: \"HP_HardwarePlugIn_DeviceStart: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadDeviceError) [theDevice is NULL]: \"HP_HardwarePlugIn_DeviceStartAtTime: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadDeviceError) [theDevice is NULL]: \"HP_HardwarePlugIn_DeviceStop: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadDeviceError) [theDevice is NULL]: \"HP_HardwarePlugIn_DeviceTranslateTime: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadObjectError) [theDevice is NULL]: \"HP_HardwarePlugIn_DeviceGetProperty: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadObjectError) [theDevice is NULL]: \"HP_HardwarePlugIn_DeviceGetPropertyInfo: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadObjectError) [theDevice is NULL]: \"HP_HardwarePlugIn_DeviceSetProperty: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadObjectError) [theObject is NULL]: \"HP_HardwarePlugIn_ObjectIsPropertySettable: no object with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadObjectError) [theObject is NULL]: \"HP_HardwarePlugIn_ObjectSetPropertyData: no object with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadObjectError) [theObject is NULL]: \"HP_HardwarePlugIn_ObjectShow: no object with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadObjectError) [theStream is NULL]: \"HP_HardwarePlugIn_StreamGetProperty: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadObjectError) [theStream is NULL]: \"HP_HardwarePlugIn_StreamGetPropertyInfo: no device with given ID\""
- "%25s:%-5d EXCEPTION (kAudioHardwareBadObjectError) [theStream is NULL]: \"HP_HardwarePlugIn_StreamSetProperty: no device with given ID\""
- "%25s:%-5d Waiting for clock device's sample rate to update to %f Hz failed with result '%s'"
- "@@ Strips Feb 15 2026 08:37:02"

```
