## MediaControlReceiver

> `/System/Library/PrivateFrameworks/MediaControlReceiver.framework/MediaControlReceiver`

```diff

-890.73.1.11.1
-  __TEXT.__text: 0x4aa4
-  __TEXT.__auth_stubs: 0x630
+890.77.2.0.0
+  __TEXT.__text: 0x4cdc
+  __TEXT.__auth_stubs: 0x640
   __TEXT.__objc_methlist: 0x68
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x198
-  __TEXT.__cstring: 0x1637
+  __TEXT.__cstring: 0x176a
   __TEXT.__unwind_info: 0x150
   __TEXT.__objc_classname: 0x5d
-  __TEXT.__objc_methname: 0x38c
+  __TEXT.__objc_methname: 0x3b1
   __TEXT.__objc_methtype: 0x79
-  __TEXT.__objc_stubs: 0x420
-  __DATA_CONST.__got: 0x90
+  __TEXT.__objc_stubs: 0x440
+  __DATA_CONST.__got: 0x98
   __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x130
+  __DATA_CONST.__objc_selrefs: 0x138
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x328
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x340
+  __AUTH_CONST.__cfstring: 0x380
   __AUTH_CONST.__objc_const: 0x1c8
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x10

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 01C36A19-391E-35F5-8E17-085F94D4E1F0
-  Functions: 54
-  Symbols:   298
-  CStrings:  246
+  UUID: A348C424-81D6-311C-9A04-0DFD069A63CF
+  Functions: 55
+  Symbols:   303
+  CStrings:  257
 
Symbols:
+ _APSXPCServerAddCommandHandler
+ _APSXPCServerStart
+ __HandleReceiverProcessConnect
+ ___block_literal_global.89
+ _kAPSXPCServerOption_EntitlementName
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
- ___block_literal_global.93
- _sleep
CStrings:
+ "Agent server received %'@ from the receiver process\n"
+ "Connect to %@ failed with error: %#m\n"
+ "Failed to add command handler for %@ command with err: %d"
+ "Failed to start %@ with err: %d"
+ "OSStatus _HandleReceiverProcessConnect(CFStringRef, CFDictionaryRef, CFDictionaryRef *)"
+ "Sending %'@ to %@\n"
+ "Starting %@ server"
+ "com.apple.airplay.receiver.mediaremote.agent.services"
+ "com.apple.airplay.receiver.mediaremote.agent.services.allow"
+ "dictionaryWithObjects:forKeys:count:"
+ "void _StartAgentService(void)"
- "Connect failed with error: %#m\n"
- "void APReceiverMediaRemoteXPCClient_SetDelegate(id<APReceiverMediaRemoteCommunicationChannelDelegate> _Nonnull)"

```
