## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1267.603.0.0.0
-  __TEXT.__text: 0x492804
+1267.609.0.0.0
+  __TEXT.__text: 0x496a60
   __TEXT.__auth_stubs: 0x2550
   __TEXT.__objc_stubs: 0x740
   __TEXT.__init_offsets: 0x4c8
   __TEXT.__objc_methlist: 0x134
   __TEXT.__const: 0xb0786
-  __TEXT.__gcc_except_tab: 0x558c8
-  __TEXT.__cstring: 0x27718
+  __TEXT.__gcc_except_tab: 0x55cb8
+  __TEXT.__cstring: 0x27827
   __TEXT.__objc_classname: 0x34
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_capture: 0x158
-  __TEXT.__oslogstring: 0x4c9a4
+  __TEXT.__oslogstring: 0x4d0d1
   __TEXT.__objc_methname: 0x5b9
   __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_reflstr: 0x4c

   __TEXT.__dof_VirtualAu: 0x303
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0xf5d0
+  __TEXT.__unwind_info: 0xf598
   __TEXT.__eh_frame: 0x780
   __DATA_CONST.__auth_got: 0x12c0
   __DATA_CONST.__got: 0x460
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x242e0
+  __DATA_CONST.__const: 0x24250
   __DATA_CONST.__cfstring: 0x39c0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9901
+  Functions: 9886
   Symbols:   735
-  CStrings:  10500
+  CStrings:  10526
 
CStrings:
+ "%25s:%-5d %u: %s."
+ "%25s:%-5d Already notified for property %s on id %u. Returning."
+ "%25s:%-5d AudioObjectGetPropertyData(kAudioDevicePropertyDataSources) return no input data sources for device %u."
+ "%25s:%-5d AudioObjectGetPropertyData(kAudioDevicePropertyDataSources) returned error %s for device %u."
+ "%25s:%-5d AudioObjectGetPropertyDataSize(kAudioDevicePropertyDataSources) returned error %s for device %u."
+ "%25s:%-5d EXCEPTION (status) [error status is an error]: \"AudioObjectGetPropertyDataSize(%s) returned error %s (%d).\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"AirPlay audio device returned control list size of 0\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Expected %u bytes, got %u bytes instead\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"The HAL returned a size of %u while we expected %lu\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"The HAL returned a size of %u while we expected %u\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"The HAL returned input stream size of %u\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"The HAL returned kAudioObjectUnknown for %s index %u.\""
+ "%25s:%-5d EXCEPTION (theResult) [error theResult is an error]: \"AudioObjectGetPropertyData(kAudioDevicePropertyStreams, '%s') failed.\""
+ "%25s:%-5d EXCEPTION (theResult) [error theResult is an error]: \"Error %d ('%s') determining the number of stream formats for stream %d\""
+ "%25s:%-5d EXCEPTION (theResult) [error theResult is an error]: \"Error %d ('%s') reading the stream formats for stream %d\""
+ "%25s:%-5d EXCEPTION (theResult) [error theResult is an error]: \"Error getting property %s on device %u.\""
+ "%25s:%-5d Error %d ('%s') determining the number of stream formats for stream %u"
+ "%25s:%-5d Property %s is not settable on id %lu."
+ "%25s:%-5d Stream Format %u: %s."
+ "%25s:%-5d The HAL returned a size of %u while we expected %lu"
+ "%25s:%-5d The HAL returned fewer stream formats (%u) than were expected (%u)"
+ "%25s:%-5d The HAL returned more stream formats (%u) than were expected (%u)"
+ "%25s:%-5d failed to read device UID for device %u (status = %d, propSize = %u, uid = %p)"
+ "%25s:%-5d getting %s formats for output stream ID %u on device ID %u (uid: \"%@\")."
+ "%25s:%-5d property %s is not supported on id %lu."
+ "@@ Strips Apr  4 2025 03:20:32"
+ "AirPlay audio device returned control list size of 0"
+ "DeviceSettings_D20Family.cpp"
+ "DeviceSettings_D40Family.cpp"
+ "Expected %u bytes, got %u bytes instead"
+ "The HAL returned a size of %u while we expected %lu"
+ "The HAL returned a size of %u while we expected %u"
+ "The HAL returned input stream size of %u"
+ "The HAL returned kAudioObjectUnknown for %s index %u."
- "%25s:%-5d %lu: %s."
- "%25s:%-5d AudioObjectGetPropertyData(kAudioDevicePropertyDataSources) returned error %s for device %lu."
- "%25s:%-5d EXCEPTION (std::runtime_error): \"The HAL returned kAudioObjectUnknown for %s index %lu.\""
- "%25s:%-5d Stream Format %lu: %s."
- "%25s:%-5d getting %s formats for output stream ID %u on device ID %lu (uid: \"%@\")."
- "@@ Strips Mar 21 2025 21:40:47"
- "HapticDebugIOMonitor.h"
- "The HAL returned kAudioObjectUnknown for %s index %lu."

```
