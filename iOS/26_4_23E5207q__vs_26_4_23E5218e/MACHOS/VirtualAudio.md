## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1364.531.0.0.0
-  __TEXT.__text: 0x4fd8a8
-  __TEXT.__auth_stubs: 0x2720
+1364.536.0.0.0
+  __TEXT.__text: 0x4fdb1c
+  __TEXT.__auth_stubs: 0x27d0
   __TEXT.__objc_stubs: 0xb20
   __TEXT.__init_offsets: 0x4e8
   __TEXT.__objc_methlist: 0x124
-  __TEXT.__const: 0xb0baa
-  __TEXT.__gcc_except_tab: 0x5f538
-  __TEXT.__cstring: 0x288c0
+  __TEXT.__const: 0xb0bca
+  __TEXT.__gcc_except_tab: 0x5f2f8
+  __TEXT.__cstring: 0x28895
   __TEXT.__swift5_typeref: 0x131
   __TEXT.__swift5_capture: 0x178
-  __TEXT.__oslogstring: 0x4eea5
+  __TEXT.__oslogstring: 0x4f0a4
   __TEXT.__objc_methname: 0x858
   __TEXT.__objc_classname: 0x6b
   __TEXT.__objc_methtype: 0x2ba

   __TEXT.__dof_VirtualAu: 0x340
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0x11898
+  __TEXT.__unwind_info: 0x11860
   __TEXT.__eh_frame: 0x758
-  __DATA_CONST.__auth_got: 0x13a8
-  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__auth_got: 0x1400
+  __DATA_CONST.__got: 0x4e8
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x28240
+  __DATA_CONST.__const: 0x282c8
   __DATA_CONST.__cfstring: 0x2dc0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/AppleSauce.framework/AppleSauce
   - /System/Library/PrivateFrameworks/AudioDSPGraph.framework/AudioDSPGraph
   - /System/Library/PrivateFrameworks/AudioDataAnalysis.framework/AudioDataAnalysis
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard

   - /System/Library/PrivateFrameworks/CPMS.framework/CPMS
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/CiderAudioServer.framework/CiderAudioServer
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService
   - /System/Library/PrivateFrameworks/IAP.framework/IAP

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 44A7C3E3-2B4C-38F0-98F9-CAE1CF1C7283
-  Functions: 11704
-  Symbols:   776
-  CStrings:  11365
+  UUID: 92CE0F41-62E2-345B-B4AF-ADCF3D266F07
+  Functions: 11713
+  Symbols:   788
+  CStrings:  11367
 
Symbols:
+ __ZNK10applesauce3xpc6object9to_stringEv
+ __xpc_type_dictionary
+ _analytics_send_event
+ _xpc_dictionary_create
+ _xpc_dictionary_set_value
+ _xpc_double_create
+ _xpc_get_type
+ _xpc_int64_create
+ _xpc_null_create
+ _xpc_release
+ _xpc_retain
+ _xpc_string_create
CStrings:
+ "%25s:%-5d CoreAnalytics event '%s':\n%s"
+ "%25s:%-5d EXCEPTION (std::logic_error): \"No Valid Tap Stream Index Identified\""
+ "%25s:%-5d Finalize requested on analytics for DSPChain '%s' (%lu) on VAD %lu ('%s') with IO %s"
+ "%25s:%-5d New AnalyticsManager for DSPChain '%s' (%lu) on VAD %lu ('%s')"
+ "%25s:%-5d StartIO analytics event on DSPChain '%s' (%lu) on VAD %lu ('%s')"
+ "%25s:%-5d StartIO analytics event when IO was already running. Event may be ignored. DSPChain '%s' (%lu) on VAD %lu ('%s')"
+ "%25s:%-5d StopIO analytics event on DSPChain '%s' (%lu) on VAD %lu ('%s')"
+ "%25s:%-5d StopIO analytics event when IO was already stopped. Event may be ignored. DSPChain '%s' (%lu) on VAD %lu ('%s')"
+ "%25s:%-5d Unable to translate physical format to client format for virtual stream %p of aggregate device %p using cached available formats, but device could be pending available format notification. Temporarily translating %s to %s"
+ "%25s:%-5d Waiting for clock device's sample rate to update to %f Hz failed with result '%s'"
+ "@@ Strips Feb 15 2026 08:37:02"
+ "No Valid Tap Stream Index Identified"
+ "apd_count"
+ "com.apple.coreaudio.APD.IODetectionSummary"
+ "duration_seconds"
+ "vad"
- "%25s:%-5d DSPChain analytics event:\n%s"
- "%25s:%-5d Finalize requested on analytics for DSPChain '%s' (%lu) with IO %s"
- "%25s:%-5d New AnalyticsManager for DSPChain '%s' (%lu)"
- "%25s:%-5d StartIO analytics event on DSPChain '%s' (%lu)"
- "%25s:%-5d StartIO analytics event when IO was already running. Event may be ignored. DSPChain '%s' (%lu)"
- "%25s:%-5d StopIO analytics event on DSPChain '%s' (%lu)"
- "%25s:%-5d StopIO analytics event when IO was already stopped. Event may be ignored. DSPChain '%s' (%lu)"
- "@@ Strips Jan 29 2026 23:39:11"
- "APD_End_EventCount"
- "APD_Final_EventCount"
- "APD_Session_EventCount"
- "APD_Start_EventCount"
- "DSPChainAnalyticsEvent_ChainInstance"
- "DSPChainAnalyticsEvent_ChainName"

```
