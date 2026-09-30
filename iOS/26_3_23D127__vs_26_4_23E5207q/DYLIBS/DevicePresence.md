## DevicePresence

> `/System/Library/PrivateFrameworks/DevicePresence.framework/DevicePresence`

```diff

 29.0.0.0.0
-  __TEXT.__text: 0xdcc
-  __TEXT.__auth_stubs: 0x1b0
+  __TEXT.__text: 0xe1c
+  __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_methlist: 0x2fc
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x28

   __DATA_CONST.__objc_selrefs: 0x1f8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xe8
+  __AUTH_CONST.__auth_got: 0xe0
   __AUTH_CONST.__cfstring: 0x1e0
   __AUTH_CONST.__objc_const: 0x738
   __DATA.__objc_ivar: 0x18

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3A9A933E-EE80-3284-81DD-6A48B158A7E2
-  Functions: 36
-  Symbols:   195
+  UUID: 462B54B8-ED67-3565-98E8-6C878182DE69
+  Functions: 37
+  Symbols:   196
   CStrings:  151
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
Functions:
~ -[DPCManager stopWatchPresenceUpdate] : 76 -> 80
~ __DPCLoggingFacility : 160 -> 176
~ -[DPCManager dealloc] : 200 -> 208
~ -[DPCManager dealloc].cold.1 : 68 -> 56
~ -[DPCManager dealloc].cold.2 : 68 -> 56
~ ___32-[DPCManager setupXPCConnection]_block_invoke : 184 -> 188
~ -[DPCManager setupXPCConnection] : 504 -> 512
~ ___32-[DPCManager setupXPCConnection]_block_invoke.61 : 184 -> 188
~ -[DPCManager updateWatchPresenceStatus] : 76 -> 80
~ -[DPCManager setupWatchPresenceDetection] : 76 -> 80
~ -[DPCManager startWatchPresenceUpdate] : 76 -> 80
~ -[DPCManager setWatchNewEvent:] : 92 -> 96
~ -[DPCManager setStreamingMode:] : 92 -> 96
+ _OUTLINED_FUNCTION_0
~ -[DPCDaemonClient informDelegateWithLatestEvent] : 264 -> 268
~ -[DPCDaemonClient informDelegateWithError:] : 292 -> 300
~ -[DPCDaemonClient informDelegateWithWatchStatusEvent:] : 336 -> 344

```
