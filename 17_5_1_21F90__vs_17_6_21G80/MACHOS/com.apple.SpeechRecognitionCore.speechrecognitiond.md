## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.2.83.5.0
-  __TEXT.__text: 0xa9798
-  __TEXT.__auth_stubs: 0x18c0
-  __TEXT.__objc_stubs: 0x2f00
+6.2.83.7.1
+  __TEXT.__text: 0xa9a6c
+  __TEXT.__auth_stubs: 0x18d0
+  __TEXT.__objc_stubs: 0x2f80
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xc18
-  __TEXT.__cstring: 0x2f19
-  __TEXT.__objc_methname: 0x3756
+  __TEXT.__cstring: 0x2f42
+  __TEXT.__objc_methname: 0x37d0
   __TEXT.__objc_classname: 0x1ce
   __TEXT.__objc_methtype: 0xb6d
   __TEXT.__const: 0x5605
   __TEXT.__oslogstring: 0x3ccf
   __TEXT.__gcc_except_tab: 0x6d60
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x3e58
+  __TEXT.__unwind_info: 0x3e80
   __TEXT.__eh_frame: 0x1a0
-  __DATA_CONST.__auth_got: 0xc78
+  __DATA_CONST.__auth_got: 0xc80
   __DATA_CONST.__got: 0x3a0
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x63a0
+  __DATA_CONST.__const: 0x63e8
   __DATA_CONST.__cfstring: 0x1b40
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x1f8
+  __DATA_CONST.__objc_classrefs: 0x208
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA.__objc_const: 0x2428
-  __DATA.__objc_selrefs: 0xdb0
+  __DATA.__objc_selrefs: 0xdd0
   __DATA.__objc_ivar: 0xdc
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x790
-  __DATA.__bss: 0x9e0
+  __DATA.__bss: 0x9f0
   __DATA.__common: 0x20
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/SpeechRecognitionCore
   - /System/Library/PrivateFrameworks/SpeechRecognitionSharedSupport.framework/SpeechRecognitionSharedSupport
+  - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5CC684C7-CB05-3964-851A-C4501D12E1EE
-  Functions: 3258
-  Symbols:   1116
-  CStrings:  1986
+  UUID: 6F3FFC5C-5A73-3561-82DA-40D7146872B1
+  Functions: 3263
+  Symbols:   1121
+  CStrings:  1991
 
Symbols:
+ _OBJC_CLASS_$_STActivityAttribution
+ _OBJC_CLASS_$_STMediaStatusDomainPublisher
+ _RDAddSTActivityAttributionForAuditToken
+ _RDRemoveSTActivityAttributionForAuditToken
+ _xpc_connection_get_audit_token
CStrings:
+ "addAudioRecordingAttribution:"
+ "attributionWithAuditToken:"
+ "removeAudioRecordingAttribution:"
+ "updateVolatileDataWithBlock:"
+ "v16@?0@\"STMutableMediaStatusDomainData\"8"

```
