## AssistiveTouch-iOS

> `/System/Library/CoreAccessories/PlugIns/Features/AssistiveTouch-iOS.feature/AssistiveTouch-iOS`

```diff

-1139.82.1.0.0
-  __TEXT.__text: 0x13a4
-  __TEXT.__auth_stubs: 0x270
+1147.100.12.0.0
+  __TEXT.__text: 0x1334
+  __TEXT.__auth_stubs: 0x250
   __TEXT.__objc_methlist: 0x22c
   __TEXT.__const: 0x28
   __TEXT.__cstring: 0xae

   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x148
-  __AUTH_CONST.__auth_got: 0x140
+  __AUTH_CONST.__auth_got: 0x130
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x330

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B0D2EDE3-5856-3972-9955-B07647B22829
-  Functions: 39
+  UUID: F25007DB-FFAB-394B-9AFA-4CBD7E573A6A
+  Functions: 40
   Symbols:   195
   CStrings:  109
 
Symbols:
+ _OUTLINED_FUNCTION_4
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ -[ACCAssistiveTouchFeaturePlugin description] : 168 -> 176
~ -[ACCAssistiveTouchFeaturePlugin startPlugin] : 504 -> 480
~ -[ACCAssistiveTouchFeaturePlugin stopPlugin] : 420 -> 396
~ -[ACCAssistiveTouchFeaturePlugin assistiveTouch:setEnabled:] : 304 -> 288
~ ___57-[ACCAssistiveTouchFeaturePlugin _assistiveTouchToggled:]_block_invoke : 204 -> 196
~ ___55-[ACCAssistiveTouchFeaturePlugin _startAssistiveTouch:]_block_invoke : 276 -> 260
~ ___54-[ACCAssistiveTouchFeaturePlugin _stopAssistiveTouch:]_block_invoke : 276 -> 260
~ _OUTLINED_FUNCTION_0 : 24 -> 72
~ _OUTLINED_FUNCTION_1 : 28 -> 24
~ _OUTLINED_FUNCTION_2 : 28 -> 20
~ _OUTLINED_FUNCTION_3 : 12 -> 20
+ _OUTLINED_FUNCTION_4
~ ___57-[ACCAssistiveTouchFeaturePlugin _assistiveTouchToggled:]_block_invoke.cold.1 : 112 -> 56
~ ___55-[ACCAssistiveTouchFeaturePlugin _startAssistiveTouch:]_block_invoke.cold.2 : 52 -> 44
~ ___55-[ACCAssistiveTouchFeaturePlugin _startAssistiveTouch:]_block_invoke.cold.4 : 52 -> 44
~ ___54-[ACCAssistiveTouchFeaturePlugin _stopAssistiveTouch:]_block_invoke.cold.2 : 52 -> 44
~ ___54-[ACCAssistiveTouchFeaturePlugin _stopAssistiveTouch:]_block_invoke.cold.4 : 52 -> 44

```
