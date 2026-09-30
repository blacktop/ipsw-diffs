## IncomingCallFilter

> `/System/Library/PrivateFrameworks/IncomingCallFilter.framework/Versions/A/IncomingCallFilter`

```diff

 170.300.101.0.0
-  __TEXT.__text: 0x3480
+  __TEXT.__text: 0x34c0
   __TEXT.__auth_stubs: 0x350
   __TEXT.__objc_methlist: 0x80
   __TEXT.__const: 0x60
   __TEXT.__oslogstring: 0x921
   __TEXT.__cstring: 0x266
-  __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__unwind_info: 0x120
+  __TEXT.__gcc_except_tab: 0xd0
+  __TEXT.__unwind_info: 0x128
   __TEXT.__objc_classname: 0xe
   __TEXT.__objc_methname: 0x1cf
   __TEXT.__objc_methtype: 0x71

   - /System/Library/PrivateFrameworks/IMFoundation.framework/Versions/A/IMFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0DD33519-5958-3661-8E35-99343B0A7ABB
-  Functions: 62
-  Symbols:   208
+  UUID: 660343A7-6CF0-3E07-A147-A9749DEB1D86
+  Functions: 66
+  Symbols:   212
   CStrings:  140
 
Symbols:
+ +[ICFCallServer sharedInstance].cold.1
+ ICFCallProviderShouldAllowIncomingCallWithQueue.cold.2
+ ICFDefaultLog.cold.1
+ _ICFConfigureGlobals.cold.1
Functions:
~ __ICFConfigureGlobals : 136 -> 120
~ _____ICFXPCServer_peer_event_handler_block_invoke : 120 -> 112
~ +[ICFCallServer sharedInstance] : 68 -> 56
~ __21-[ICFCallServer init]_block_invoke.8 : 404 -> 408
~ -[ICFCallServer _clientConnected] : 116 -> 120
~ -[ICFCallServer _cleanup] : 108 -> 116
~ _ICFCallProviderShouldAllowIncomingCallWithQueue : 936 -> 912
~ _ICFDefaultLog : 68 -> 56
+ _ICFConfigureGlobals.cold.1
+ +[ICFCallServer sharedInstance].cold.1
~ ICFCallProviderShouldAllowIncomingCallWithQueue.cold.1 : 68 -> 40
+ ICFCallProviderShouldAllowIncomingCallWithQueue.cold.2

```
