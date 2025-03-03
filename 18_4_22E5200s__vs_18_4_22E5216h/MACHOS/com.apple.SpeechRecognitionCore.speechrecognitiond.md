## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.3.30.5.0
-  __TEXT.__text: 0xbb2e0
+6.3.30.7.0
+  __TEXT.__text: 0xbb6fc
   __TEXT.__auth_stubs: 0x2710
   __TEXT.__objc_stubs: 0x3880
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x16d4
   __TEXT.__const: 0x599f
-  __TEXT.__gcc_except_tab: 0x81bc
+  __TEXT.__gcc_except_tab: 0x81c4
   __TEXT.__objc_methname: 0x4a85
   __TEXT.__cstring: 0x3be1
-  __TEXT.__oslogstring: 0x4cfb
+  __TEXT.__oslogstring: 0x4d7b
   __TEXT.__objc_classname: 0x307
   __TEXT.__objc_methtype: 0xf40
   __TEXT.__dlopen_cstrs: 0xc0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3499
-  Symbols:   1326
-  CStrings:  2176
+  Functions: 3501
+  Symbols:   1328
+  CStrings:  2178
 
Symbols:
+ __ZN9RDQSRPeer20GetCommandsInGrammarEPvP9__CFArray
+ __ZN9RDQSRPeer21CopyCommandsInGrammarEPv
CStrings:
+ "Activating Grammar  -> lmid = %llu, grammarID = %zu, %@"
+ "Deactivating Grammar  -> lmid = %llu, grammarID = %zu, %@"
+ "Deactivating Grammar after end of utterance -> lmid = %llu, grammarID = %zu, %@"
+ "Match Result:: isLive = %d isActive = %d lmid = %llu grammarID = %zu Commands = %@"
- "Activating Grammar  -> %zu, fClientActivated = %d, fCanListen = %d"
- "Deactivating Grammar  -> %zu, fClientActivated = %d, fCanListen = %d"

```
