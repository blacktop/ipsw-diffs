## NanoAudioControl

> `/System/Library/PrivateFrameworks/NanoAudioControl.framework/NanoAudioControl`

```diff

-2023.100.45.0.0
-  __TEXT.__text: 0x26538
+2023.100.49.0.0
+  __TEXT.__text: 0x26570
   __TEXT.__auth_stubs: 0x750
   __TEXT.__objc_methlist: 0x33ec
-  __TEXT.__cstring: 0xf7f
+  __TEXT.__cstring: 0xfa3
   __TEXT.__const: 0x1d0
   __TEXT.__oslogstring: 0x1e5d
-  __TEXT.__gcc_except_tab: 0x4a0
+  __TEXT.__gcc_except_tab: 0x4a8
   __TEXT.__unwind_info: 0xc10
   __TEXT.__objc_classname: 0x4c3
   __TEXT.__objc_methname: 0x577e

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 26E766BB-CEF7-3825-AE11-4F40718D46B7
+  UUID: A9DF48C6-B9F6-3A7D-B309-D49F8C84C091
   Functions: 1159
   Symbols:   3717
-  CStrings:  1617
+  CStrings:  1618
 
Symbols:
+ ___32-[NACIDSServer _handlePlayTone:]_block_invoke.166
+ ___38-[NACIDSServer _handlePickAudioRoute:]_block_invoke.186
+ ___38-[NACIDSServer _handlePickAudioRoute:]_block_invoke.186.cold.1
+ ___38-[NACIDSServer _handlePickAudioRoute:]_block_invoke.188
+ ___58-[NACIDSServer routingControllerAvailableRoutesDidChange:]_block_invoke.212
+ ___Block_byref_object_copy_.183
+ ___Block_byref_object_dispose_.184
+ ___block_descriptor_64_e8_32s40s48s56w_e20_v24?0q8"NSError"16ls32l8s40l8w56l8s48l8
- ___32-[NACIDSServer _handlePlayTone:]_block_invoke.165
- ___38-[NACIDSServer _handlePickAudioRoute:]_block_invoke.185
- ___38-[NACIDSServer _handlePickAudioRoute:]_block_invoke.185.cold.1
- ___38-[NACIDSServer _handlePickAudioRoute:]_block_invoke.187
- ___58-[NACIDSServer routingControllerAvailableRoutesDidChange:]_block_invoke.211
- ___Block_byref_object_copy_.182
- ___Block_byref_object_dispose_.183
- ___block_descriptor_56_e8_32s40s48w_e20_v24?0q8"NSError"16ls32l8w48l8s40l8
Functions:
~ -[NACIDSServer _handlePlayTone:] : 956 -> 996
~ ___32-[NACIDSServer _handlePlayTone:]_block_invoke : 428 -> 444
CStrings:
+ "com.apple.NanoAudioControl.PlayTone"

```
