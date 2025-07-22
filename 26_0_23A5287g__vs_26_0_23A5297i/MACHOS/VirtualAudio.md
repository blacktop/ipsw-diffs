## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1364.110.0.0.0
-  __TEXT.__text: 0x4fa19c
-  __TEXT.__auth_stubs: 0x26e0
+1364.115.30.0.0
+  __TEXT.__text: 0x503a88
+  __TEXT.__auth_stubs: 0x26f0
   __TEXT.__objc_stubs: 0x9e0
-  __TEXT.__init_offsets: 0x4d8
+  __TEXT.__init_offsets: 0x4dc
   __TEXT.__objc_methlist: 0x124
-  __TEXT.__const: 0xb0afa
-  __TEXT.__gcc_except_tab: 0x5cb68
-  __TEXT.__cstring: 0x285f6
+  __TEXT.__const: 0xb0b02
+  __TEXT.__gcc_except_tab: 0x5da38
+  __TEXT.__cstring: 0x286d9
   __TEXT.__objc_classname: 0x34
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_capture: 0x178
-  __TEXT.__oslogstring: 0x4dc66
+  __TEXT.__oslogstring: 0x4e15b
   __TEXT.__objc_methname: 0x710
   __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_reflstr: 0x4c

   __TEXT.__dof_VirtualAu: 0x340
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0x11098
+  __TEXT.__unwind_info: 0x11340
   __TEXT.__eh_frame: 0x7a0
-  __DATA_CONST.__auth_got: 0x1388
+  __DATA_CONST.__auth_got: 0x1390
   __DATA_CONST.__got: 0x4d8
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x27678
+  __DATA_CONST.__const: 0x27b30
   __DATA_CONST.__cfstring: 0x2de0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x268
   __DATA.__data: 0x340
-  __DATA.__bss: 0x242d0
+  __DATA.__bss: 0x24bc0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A1F6CE5C-A924-39FB-B524-ABA20B7AC4E5
-  Functions: 11351
-  Symbols:   772
-  CStrings:  11243
+  UUID: A4A8F017-2BDD-3A84-A9EC-866ED65236A5
+  Functions: 11494
+  Symbols:   773
+  CStrings:  11270
 
Symbols:
+ _AVAUVoiceIOSetVoiceProcessingBypassedForBundleID
CStrings:
+ "%25s:%-5d Adding config change listener for CarPlay device ID: %lu"
+ "%25s:%-5d Already notified for config change property on CarPlay device ID: %lu. Returning."
+ "%25s:%-5d Config change listener fired for CarPlay device ID: %lu"
+ "%25s:%-5d Config change listener fired for CarPlay device ID: %lu for different addresses %s"
+ "%25s:%-5d Config change listener fired for device ID: %lu not CarPlay device ID: %lu"
+ "%25s:%-5d DSPChain analytics event:\n%s"
+ "%25s:%-5d Device with UID \"%s\" is Apple Display"
+ "%25s:%-5d Error %d registering CarPlay property listener on id %u."
+ "%25s:%-5d Error %d unregistering CarPlay property listener on id %u."
+ "%25s:%-5d Failed to find a valid route for port update. Attempting to activate for normal as a fallback"
+ "%25s:%-5d Finalize requested on analytics for DSPChain '%s' (%lu) with IO %s"
+ "%25s:%-5d New AnalyticsManager for DSPChain '%s' (%lu)"
+ "%25s:%-5d Removing config change listener for CarPlay device ID: %lu"
+ "%25s:%-5d StartIO analytics event on DSPChain '%s' (%lu)"
+ "%25s:%-5d StartIO analytics event when IO was already running. Event may be ignored. DSPChain '%s' (%lu)"
+ "%25s:%-5d StopIO analytics event on DSPChain '%s' (%lu)"
+ "%25s:%-5d StopIO analytics event when IO was already stopped. Event may be ignored. DSPChain '%s' (%lu)"
+ "%25s:%-5d Studio mic enabled, allowing PV in HW volume mode for device %s."
+ "%25s:%-5d Unable to read password detection count for analytics on DSPChain %s (status %ld)"
+ "%25s:%-5d oldPropertyValue: %u; shouldPrioritizeThisPort: %u, newValue: %u."
+ "@@ Strips Jul 15 2025 21:48:10"
+ "APD_End_EventCount"
+ "APD_Final_EventCount"
+ "APD_Session_EventCount"
+ "APD_Start_EventCount"
+ "AnalyticsManager.cpp"
+ "AudioObjectPropertyListenerManagerQueueKey"
+ "DSPChainAnalyticsEvent_ChainInstance"
+ "DSPChainAnalyticsEvent_ChainName"
+ "Require Studio Mic Enabled"
+ "Studio Mic Active"
+ "firFilterIDs"
+ "stopped"
- "%25s:%-5d Device has Apple Display UID"
- "%25s:%-5d Device has Apple Display VID_PID"
- "%25s:%-5d EXCEPTION (std::logic_error): \"unsupported method GetDSPProcessorInstanceIDAtChainIndex\""
- "%25s:%-5d oldPropertyValue: %u; newValue: %u."
- "@@ Strips Jun 28 2025 20:14:58"
- "unsupported method GetDSPProcessorInstanceIDAtChainIndex"

```
