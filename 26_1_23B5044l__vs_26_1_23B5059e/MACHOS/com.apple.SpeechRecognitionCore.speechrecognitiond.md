## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.3.67.0.0
-  __TEXT.__text: 0xc6a40
+6.3.68.1.0
+  __TEXT.__text: 0xc6b2c
   __TEXT.__auth_stubs: 0x2620
   __TEXT.__objc_stubs: 0x3440
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x18d4
   __TEXT.__const: 0x5d66
-  __TEXT.__gcc_except_tab: 0xa30c
-  __TEXT.__objc_methname: 0x49cd
-  __TEXT.__cstring: 0x4036
+  __TEXT.__gcc_except_tab: 0xa318
+  __TEXT.__objc_methname: 0x49e2
+  __TEXT.__cstring: 0x4076
   __TEXT.__oslogstring: 0x5664
   __TEXT.__objc_classname: 0x348
   __TEXT.__objc_methtype: 0x1012

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA.__objc_const: 0x2c38
-  __DATA.__objc_selrefs: 0x12b0
+  __DATA.__objc_selrefs: 0x12b8
   __DATA.__objc_ivar: 0x140
   __DATA.__objc_data: 0x1488
   __DATA.__data: 0xf60

   - /System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/SpeechRecognitionCore
   - /System/Library/PrivateFrameworks/SpeechRecognitionSharedSupport.framework/SpeechRecognitionSharedSupport
   - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech
   - /System/Library/PrivateFrameworks/VoiceActions.framework/VoiceActions

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0BB45B3F-BF0B-3278-9C80-78A25D5192C0
+  UUID: B2622287-5714-3495-A049-611E611F965D
   Functions: 3556
   Symbols:   1117
-  CStrings:  2483
+  CStrings:  2485
 
Functions:
~ __Z32speechrecognitiond_peer_is_aliveiP6RDPeer : 236 -> 304
~ sub_100051bdc -> sub_100051c70 : 1296 -> 1464
CStrings:
+ "com.apple.private.voicecontrol.speechrecognition.api"
+ "valueForEntitlement:"

```
