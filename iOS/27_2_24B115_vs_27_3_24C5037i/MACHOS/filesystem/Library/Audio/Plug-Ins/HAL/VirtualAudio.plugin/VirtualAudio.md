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
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1451.212.0.0.0
-  __TEXT.__text: 0x556738
-  __TEXT.__realtime: 0x14a60
+1451.305.0.0.0
+  __TEXT.__text: 0x55b5c8
+  __TEXT.__realtime: 0x149a4
   __TEXT.__auth_stubs: 0x2a40
   __TEXT.__objc_stubs: 0x1280
-  __TEXT.__init_offsets: 0x104c
+  __TEXT.__init_offsets: 0x1050
   __TEXT.__objc_methlist: 0x2c0
-  __TEXT.__const: 0xb4930
-  __TEXT.__cstring: 0x37a3a
-  __TEXT.__gcc_except_tab: 0x661cc
+  __TEXT.__const: 0xb49f0
+  __TEXT.__cstring: 0x37aaa
+  __TEXT.__gcc_except_tab: 0x667c8
   __TEXT.__swift5_typeref: 0x12b
   __TEXT.__swift5_capture: 0x168
-  __TEXT.__oslogstring: 0x58fb2
+  __TEXT.__oslogstring: 0x590c5
   __TEXT.__objc_methname: 0xf89
   __TEXT.__objc_classname: 0x9d
   __TEXT.__objc_methtype: 0x422

   __TEXT.__dof_VirtualAu: 0x340
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0x15b70
+  __TEXT.__unwind_info: 0x15c98
   __TEXT.__eh_frame: 0x730
-  __DATA_CONST.__const: 0x29738
+  __DATA_CONST.__const: 0x299b0
   __DATA_CONST.__cfstring: 0x2ec0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12546
+  Functions: 12589
   Symbols:   834
-  CStrings:  12363
+  CStrings:  12369
 
CStrings:
+ "%25s:%-5d - Conversational session: %u"
+ "%25s:%-5d AirPlay duplex-speech device %s: %u output stream(s), %u input stream(s) (created output %d, input %d)"
+ "%25s:%-5d AngleStateManager: Subscriber registered (%zu total)"
+ "%25s:%-5d DeviceStateManager: StableState subscriber registered (%zu total)"
+ "%25s:%-5d HapticAttenuationIODelegate: Failed to subscribe for angle updates; retrying on the next IO start"
+ "%25s:%-5d HapticAttenuationIODelegate: Failed to subscribe for stable-state updates; retrying on the next IO start"
+ "%25s:%-5d PhysicalDevice with AudioObjectID %lu and UID \"%s\" does not support PebblePlay conversational-apps transport type %s."
+ "%25s:%-5d Using the routing manager's conversational session state: %u"
+ "@@ Strips Oct 23 2026 03:16:33"
+ "AirPlay Duplex Speech Input"
+ "AirPlay Duplex Speech Output"
+ "Device_AirPlayDuplexSpeech_Aspen.cpp"
+ "Precondition failure: iter->second != nullptr"
+ "VAD_AirPlayDuplexSpeechInput"
+ "VAD_AirPlayDuplexSpeechOutput"
+ "conversational session"
- "%25s:%-5d AngleStateManager: Callback cleared"
- "%25s:%-5d AngleStateManager: Callback registered"
- "%25s:%-5d DeviceStateManager: StableState callback %s"
- "%25s:%-5d HapticAttenuationIODelegate: Coordinator active (subscriptions set)"
- "%25s:%-5d HapticAttenuationIODelegate: Coordinator inactive (subscriptions cleared)"
- "%25s:%-5d HapticAttenuationIODelegate: haptics IO restarted before HandleIOWillStop's delayed clear, maintaining subscriptions"
- "@@ Strips Oct  3 2026 19:41:58"
- "Precondition failure: pair.second != nullptr"
- "registered"
- "removed"
```
