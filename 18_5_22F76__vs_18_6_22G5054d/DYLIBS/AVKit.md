## AVKit

> `/System/Library/Frameworks/AVKit.framework/AVKit`

```diff

-1250.7.1.0.0
-  __TEXT.__text: 0x14a1a0
+1260.4.1.0.0
+  __TEXT.__text: 0x14a23c
   __TEXT.__auth_stubs: 0x2400
   __TEXT.__objc_methlist: 0x16dec
   __TEXT.__swift5_typeref: 0x3598
   __TEXT.__swift5_fieldmd: 0x7a8
-  __TEXT.__const: 0x2258
+  __TEXT.__const: 0x2328
   __TEXT.__constg_swiftt: 0x9d4
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_reflstr: 0x631

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x104
   __TEXT.__swift5_types: 0xa8
-  __TEXT.__cstring: 0xf1c9
+  __TEXT.__cstring: 0xf1c7
   __TEXT.__swift5_capture: 0x1a0
   __TEXT.__oslogstring: 0x7561
   __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift_as_ret: 0x98
-  __TEXT.__gcc_except_tab: 0x2cd0
+  __TEXT.__gcc_except_tab: 0x2ce8
   __TEXT.__dlopen_cstrs: 0x1ef
   __TEXT.__ustring: 0x7a
-  __TEXT.__unwind_info: 0x5890
+  __TEXT.__unwind_info: 0x5898
   __TEXT.__eh_frame: 0x1408
   __TEXT.__objc_classname: 0x2f3e
   __TEXT.__objc_methname: 0x410d9
   __TEXT.__objc_methtype: 0x79ab
   __TEXT.__objc_stubs: 0x25980
-  __DATA_CONST.__got: 0x11b0
+  __DATA_CONST.__got: 0x11b8
   __DATA_CONST.__const: 0x2c78
   __DATA_CONST.__objc_classlist: 0x7e8
   __DATA_CONST.__objc_catlist: 0xd0

   __AUTH.__objc_data: 0x3d60
   __AUTH.__data: 0x5c8
   __DATA.__objc_ivar: 0x223c
-  __DATA.__data: 0x39f0
+  __DATA.__data: 0x3918
   __DATA.__bss: 0x2518
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x13b0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: DD89995E-8D92-3508-B340-43DA3EDCAE3B
+  UUID: 0A3FC3C2-DD4C-369E-A042-FC3E0E578AC0
   Functions: 8786
-  Symbols:   27799
+  Symbols:   27801
   CStrings:  13952
 
Symbols:
+ GCC_except_table6983
+ _AVNowPlayingInfoSkipCommandInterval_block_invoke.createSharedControllerOnceToken
+ _AVNowPlayingInfoSkipCommandInterval_block_invoke.nowPlayingInfoController
+ _kMRMediaRemoteOptionSkipInterval
- _AVNowPlayingInfoPreferredIntervalsKey_block_invoke.createSharedControllerOnceToken
- _AVNowPlayingInfoPreferredIntervalsKey_block_invoke.nowPlayingInfoController
Functions:
~ -[AVNowPlayingInfoController _handleRemoteCommand:options:] : 2996 -> 3012
~ ___61-[AVMobileChromelessControlsViewController _observationSetup]_block_invoke_26 : 308 -> 376
~ -[AVPlayerController seekOrStepByFrameCount:] : 1000 -> 1012
~ -[AVPlayerController currentEnabledAssetTrackForMediaType:completionHandler:] : 532 -> 592
CStrings:
+ "AVNowPlayingInfoSkipCommandInterval"
- "AVNowPlayingInfoPreferredIntervalsKey"

```
