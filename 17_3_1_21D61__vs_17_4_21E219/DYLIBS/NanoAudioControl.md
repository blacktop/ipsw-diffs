## NanoAudioControl

> `/System/Library/PrivateFrameworks/NanoAudioControl.framework/NanoAudioControl`

```diff

-2021.400.2.0.0
-  __TEXT.__text: 0x239f4
-  __TEXT.__auth_stubs: 0x780
+2021.500.5.0.0
+  __TEXT.__text: 0x23d58
+  __TEXT.__auth_stubs: 0x730
   __TEXT.__objc_methlist: 0x295c
-  __TEXT.__cstring: 0xed9
+  __TEXT.__cstring: 0xef5
   __TEXT.__const: 0x180
-  __TEXT.__oslogstring: 0x1c2c
-  __TEXT.__gcc_except_tab: 0x320
+  __TEXT.__oslogstring: 0x1d48
+  __TEXT.__gcc_except_tab: 0x358
   __TEXT.__unwind_info: 0xbb0
-  __TEXT.__objc_classname: 0x4b2
-  __TEXT.__objc_methname: 0x535d
-  __TEXT.__objc_methtype: 0x1868
-  __TEXT.__objc_stubs: 0x37a0
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__objc_classname: 0x4b3
+  __TEXT.__objc_methname: 0x53e5
+  __TEXT.__objc_methtype: 0x1876
+  __TEXT.__objc_stubs: 0x3800
+  __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x950
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4de8
-  __DATA_CONST.__objc_selrefs: 0x11e8
-  __AUTH_CONST.__cfstring: 0xf60
+  __DATA_CONST.__objc_selrefs: 0x1200
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x250
+  __DATA_CONST.__objc_superrefs: 0x108
+  __AUTH_CONST.__cfstring: 0xf80
   __AUTH_CONST.__objc_const: 0xe10
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x3d0
+  __AUTH_CONST.__auth_got: 0x3a8
   __AUTH.__objc_data: 0xcd0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x250
-  __DATA.__objc_superrefs: 0x108
   __DATA.__objc_ivar: 0x358
   __DATA.__data: 0x540
   __DATA.__bss: 0x108

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/Celestial.framework/Celestial
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
+  - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1106
-  Symbols:   3560
-  CStrings:  1424
+  Functions: 1109
+  Symbols:   3565
+  CStrings:  1433
 
Symbols:
+ -[NACIDSServer _beginObservingSystemMutedState].cold.1
+ GCC_except_table101
+ GCC_except_table79
+ GCC_except_table82
+ _AVSystemController_SilentModeEnabledDidChangeNotification
+ _OBJC_IVAR_$_NACIDSServer._systemSilentModeNotificationToken
+ _OUTLINED_FUNCTION_3
+ ___33-[NACXPCClient _createConnection]_block_invoke.105
+ ___38-[NACIDSServer _handlePickAudioRoute:]_block_invoke.174
+ ___38-[NACIDSServer _handlePickAudioRoute:]_block_invoke.174.cold.1
+ ___38-[NACIDSServer _handlePickAudioRoute:]_block_invoke.176
+ ___47-[NACIDSServer _beginObservingSystemMutedState]_block_invoke_2
+ ___51-[NACXPCServer listener:shouldAcceptNewConnection:]_block_invoke.211
+ ___58-[NACIDSServer routingControllerAvailableRoutesDidChange:]_block_invoke.200
+ ___Block_byref_object_copy_.171
+ ___Block_byref_object_dispose_.172
+ ___block_descriptor_40_e8_32w_e24_v16?0"NSNotification"8lw32l8
+ ___block_literal_global.108
+ ___block_literal_global.215
+ ___block_literal_global.218
+ ___block_literal_global.220
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$getSilentMode
+ _objc_msgSend$setSilentMode:untilTime:reason:clientType:
- GCC_except_table100
- GCC_except_table78
- GCC_except_table81
- _OBJC_IVAR_$_NACIDSServer._systemMuteToken
- ___33-[NACXPCClient _createConnection]_block_invoke.103
- ___38-[NACIDSServer _handlePickAudioRoute:]_block_invoke.171
- ___38-[NACIDSServer _handlePickAudioRoute:]_block_invoke.171.cold.1
- ___38-[NACIDSServer _handlePickAudioRoute:]_block_invoke.173
- ___51-[NACXPCServer listener:shouldAcceptNewConnection:]_block_invoke.209
- ___58-[NACIDSServer routingControllerAvailableRoutesDidChange:]_block_invoke.197
- ___Block_byref_object_copy_.168
- ___Block_byref_object_dispose_.169
- ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
- ___block_literal_global.107
- ___block_literal_global.214
- ___block_literal_global.217
- ___block_literal_global.219
- _notify_cancel
- _notify_get_state
- _notify_post
- _notify_register_dispatch
- _notify_set_state
CStrings:
+ "\t\x11!"
+ "@\"<NSObject>\""
+ "NanoAudioControl handling system mute setting"
+ "T@\"NSString\",?,R,C"
+ "[NACIDS] System mute state: %d"
+ "[NACIDS] Updating system mute value because we got a state change notification"
+ "[NACIDS] Updating system mute value because we started observing"
+ "[NACIDS] Updating system mute value because we were asked to send the current observing system volume values"
+ "_systemSilentModeNotificationToken"
+ "addObserverForName:object:queue:usingBlock:"
+ "getSilentMode"
+ "setSilentMode:untilTime:reason:clientType:"
+ "v16@?0@\"NSNotification\"8"
- "\t1"
- "_systemMuteToken"
- "com.apple.springboard.ringerstate"
- "v12@?0i8"

```
