## MobileDeviceLink

> `/System/Library/PrivateFrameworks/MobileDeviceLink.framework/MobileDeviceLink`

```diff

-303.0.0.0.0
-  __TEXT.__text: 0xcd78
-  __TEXT.__auth_stubs: 0xb50
+305.0.0.0.0
+  __TEXT.__text: 0xccec
   __TEXT.__cstring: 0x4a02
   __TEXT.__const: 0x50
   __TEXT.__oslogstring: 0x108
   __TEXT.__unwind_info: 0x2c8
-  __DATA_CONST.__got: 0x88
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x1c8
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x3040
   __AUTH_CONST.__auth_got: 0x5a8
-  __AUTH_CONST.__cfstring: 0x3020
   __AUTH.__data: 0x58
   __DATA.__data: 0xc
   __DATA.__bss: 0x71

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
-  UUID: 614DC4A1-74B3-31E4-ACBA-DB7817ECAE89
-  Functions: 242
-  Symbols:   625
-  CStrings:  924
+  UUID: D4F24354-38DA-342E-8688-D2701BAD88BC
+  Functions: 241
+  Symbols:   623
+  CStrings:  925
 
Symbols:
- _OUTLINED_FUNCTION_1
Functions:
~ __DLHandlerThreadMessagePortCallback : 5120 -> 5124
~ _DLLockdownXPCCheckin : 532 -> 488
~ ___DLLockdownXPCCheckin_block_invoke : 536 -> 492
- _OUTLINED_FUNCTION_1
~ __DLLog : 436 -> 456
~ _DLGetListenerSocketFromLaunchd : 720 -> 724
~ _SocketConnect : 696 -> 700
~ _DLLockdownXPCCheckin.cold.1 : 104 -> 72
~ _DLLockdownXPCCheckin.cold.2 : 108 -> 76

```
