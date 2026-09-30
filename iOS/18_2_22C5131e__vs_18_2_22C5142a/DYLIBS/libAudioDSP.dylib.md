## libAudioDSP.dylib

> `/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib`

```diff

-747.339.0.0.0
-  __TEXT.__text: 0x743e0c
-  __TEXT.__auth_stubs: 0x47d0
+747.340.0.0.0
+  __TEXT.__text: 0x744f40
+  __TEXT.__auth_stubs: 0x47e0
   __TEXT.__objc_methlist: 0x314
-  __TEXT.__gcc_except_tab: 0x57444
+  __TEXT.__gcc_except_tab: 0x5753c
   __TEXT.__const: 0x7cbe0
-  __TEXT.__oslogstring: 0x37151
-  __TEXT.__cstring: 0x6e50a
+  __TEXT.__oslogstring: 0x371d8
+  __TEXT.__cstring: 0x6e56a
   __TEXT.__swift5_typeref: 0xd9
   __TEXT.__swift5_capture: 0xd4
   __TEXT.__constg_swiftt: 0xc4

   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x4
   __TEXT.__dlopen_cstrs: 0xf3
-  __TEXT.__unwind_info: 0x20438
+  __TEXT.__unwind_info: 0x20450
   __TEXT.__eh_frame: 0x5b0
   __TEXT.__objc_classname: 0x15a
   __TEXT.__objc_methname: 0x15e2

   __DATA_CONST.__objc_classrefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x3f0
-  __AUTH_CONST.__auth_got: 0x2400
+  __AUTH_CONST.__auth_got: 0x2408
   __AUTH_CONST.__auth_ptr: 0x270
   __AUTH_CONST.__const: 0x35978
   __AUTH_CONST.__cfstring: 0x21d20

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 25037
-  Symbols:   27193
-  CStrings:  16333
+  Functions: 25040
+  Symbols:   27197
+  CStrings:  16338
 
Symbols:
+ __ZN2IR13IRCoordinates17equalWithAccuracyERKS0_S2_f
CStrings:
+ ", {:.{}f}"
+ "/AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
+ "/AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
+ "00:10:06"
+ "00:10:10"
+ "00:10:21"
+ "@@ Strips Nov 10 2024 23:59:54"
+ "Gains dB: direct={:.1f}, tuning={:.1f}, dry={:.1f}, reverb={:.1f}, wet={:.1f}, ppReverb={:.1f}, ppWet={:.1f}"
+ "Nov 11 2024"
+ "PostProcDRRLin"
+ "TuningGainLin"
+ "[%s|%s] AUSM_VERBOSE|CombinedReverbIRWeights[%u]={%s}"
+ "[%s|%s] AUSM_VERBOSE|CombinedReverbSendGains=%s"
+ "[%s|%s] AUSM_VERBOSE|DirectIRWeights[%u]={%s}"
+ "[%s|%s] AUSM_VERBOSE|PostProcReverbIRWeights[%u]={%s}"
+ "[%s|%s] AUSM_VERBOSE|PostProcReverbSendGains=%s"
+ "[%s|%s] AUSM_VERBOSE|ReverbIRWeights[%u]={%s}"
+ "[%s|%s] AUSM_VERBOSE|ReverbSendGains=%s"
+ "[%s|%s] AUSM_VERBOSE|TGrid #%u: %s"
+ "[%s|%s] Forced update failed because of a mutex. This should not happen."
+ "az={:.1f}, el={:.1f}, r={:.2f}, tuningGaindB={:.1f}, rGaindB={:.1f}, ppDRRdB={:.1f}, internalized={:.1f}"
+ "{:.{}f}"
- "/AppleInternal/Library/BuildRoots/38565290-993f-11ef-b290-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
- "/AppleInternal/Library/BuildRoots/38565290-993f-11ef-b290-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
- "17:54:00"
- "17:54:05"
- "17:54:15"
- "@@ Strips Nov  2 2024 17:44:12"
- "DRRLin"
- "GainLin"
- "Nov  2 2024"
- "PostProcReverb"
- "SceneReverb"
- "[%s|%s] AUSM_VERBOSE: %s wetGaindB=%.1f, dryGaindB=%.1f"
- "[%s|%s] AUSM_VERBOSE: directGaindB=%.1f, sceneReverbGaindB=%.1f, postProcReverbGaindB=%.1f, sceneDRRdB=%.1f, sceneBlend=%.2f, postProcBlend=%.2f"
- "[%s|%s] AUSM_VERBOSE|Channel #%u: %s"
- "[%s|%s] AUSM_VERBOSE|Channel #%u: directGaindB=%.1f, reverbGaindB=%.1f"
- "az={:.1f}, el={:.1f}, r={:.2f}, gaindB={:.1f}, distGaindB={:.1f}, DRRdB={:.1f}, internalized={:.1f}"
- "calculateWetDryGains"

```
