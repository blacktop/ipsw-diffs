## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-548.10.24.0.0
-  __TEXT.__text: 0x41fa0
+548.20.7.0.0
+  __TEXT.__text: 0x420a4
   __TEXT.__auth_stubs: 0x700
   __TEXT.__objc_methlist: 0x59dc
   __TEXT.__const: 0x230
   __TEXT.__gcc_except_tab: 0xbec
   __TEXT.__cstring: 0x2ff8
-  __TEXT.__oslogstring: 0x6a39
+  __TEXT.__oslogstring: 0x6aaa
   __TEXT.__unwind_info: 0x1000
   __TEXT.__objc_classname: 0x828
   __TEXT.__objc_methname: 0xc820
   __TEXT.__objc_methtype: 0x209c
-  __TEXT.__objc_stubs: 0x7f00
+  __TEXT.__objc_stubs: 0x7ee0
   __DATA_CONST.__got: 0x498
   __DATA_CONST.__const: 0x1390
   __DATA_CONST.__objc_classlist: 0x218

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 17DF191D-FBE4-3F57-9416-3C015C57CFB0
-  Functions: 1861
-  Symbols:   6334
-  CStrings:  4143
+  UUID: 2C0100C1-F2A8-3C82-BE14-EDE960437004
+  Functions: 1862
+  Symbols:   6335
+  CStrings:  4145
 
Symbols:
+ -[TVRCDevice _deviceUpdatedState:].cold.1
- _objc_msgSend$deviceUpdatedState:
Functions:
~ -[TVRCDevice _deviceUpdatedState:] : 3492 -> 3544
~ ___77-[TVRCRPCompanionLinkClientWrapper _invalidateAndResetWithCompletionHandler:]_block_invoke.114 : 184 -> 276
~ -[TVRCRPCompanionLinkClientWrapper _updateAttentionState:] : 368 -> 404
~ -[TVRCXPCClient deviceUpdatedState:] : 296 -> 308
+ -[TVRCDevice _deviceUpdatedState:].cold.1
CStrings:
+ "%s newState: %{public}@"
+ "Invalid disconnection reason. Possible state inconsistency detected"
+ "Invalidated all sessions. Invalidating CompanionLinkClient: %{public}@"
+ "[%{public}@] attention state updated to %{public}@ from %{public}@"
- "Invalidated all sessions. Invalidating CompanionLinkClient."
- "TV attention state updated to %{public}@ from %{public}@"

```
