## IntelligenceSimulation

> `/System/Library/PrivateFrameworks/IntelligenceSimulation.framework/IntelligenceSimulation`

```diff

-3610.11.1.0.0
-  __TEXT.__text: 0x20b24
+3610.17.2.0.0
+  __TEXT.__text: 0x2cb90
   __TEXT.__objc_methlist: 0x14
-  __TEXT.__const: 0x23d2
-  __TEXT.__oslogstring: 0x595
-  __TEXT.__cstring: 0x694
-  __TEXT.__swift5_typeref: 0x89c
-  __TEXT.__constg_swiftt: 0x7d8
-  __TEXT.__swift5_reflstr: 0x576
-  __TEXT.__swift5_fieldmd: 0x8a8
+  __TEXT.__const: 0x2562
+  __TEXT.__oslogstring: 0x645
+  __TEXT.__cstring: 0x8f4
+  __TEXT.__swift5_typeref: 0x950
+  __TEXT.__constg_swiftt: 0x844
+  __TEXT.__swift5_reflstr: 0x666
+  __TEXT.__swift5_fieldmd: 0x940
   __TEXT.__swift5_proto: 0x164
   __TEXT.__swift5_types: 0x9c
-  __TEXT.__swift5_capture: 0x124
+  __TEXT.__swift5_capture: 0x1b0
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift_as_entry: 0x11c
-  __TEXT.__swift_as_ret: 0x10c
-  __TEXT.__swift_as_cont: 0x200
-  __TEXT.__swift5_protos: 0x20
+  __TEXT.__swift5_protos: 0x24
+  __TEXT.__swift_as_entry: 0x160
+  __TEXT.__swift_as_ret: 0x1b8
+  __TEXT.__swift_as_cont: 0x2a8
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__unwind_info: 0xed0
-  __TEXT.__eh_frame: 0x2418
+  __TEXT.__unwind_info: 0x11a0
+  __TEXT.__eh_frame: 0x30a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x90
-  __DATA_CONST.__got: 0x200
-  __AUTH_CONST.__const: 0x14d8
-  __AUTH_CONST.__objc_const: 0x338
-  __AUTH_CONST.__auth_got: 0x820
+  __DATA_CONST.__objc_selrefs: 0xc0
+  __DATA_CONST.__got: 0x258
+  __AUTH_CONST.__const: 0x1618
+  __AUTH_CONST.__objc_const: 0x378
+  __AUTH_CONST.__auth_got: 0x950
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x578
-  __DATA.__data: 0x498
+  __AUTH.__data: 0x5b0
+  __DATA.__data: 0x4e0
   __DATA.__common: 0x50
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AgentSessionKit.framework/AgentSessionKit
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/CampoServices.framework/CampoServices
   - /System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore
   - /System/Library/PrivateFrameworks/IntelligenceFlowProto.framework/IntelligenceFlowProto
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
+  - /System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata
   - /System/Library/PrivateFrameworks/SiriActivationFoundation.framework/SiriActivationFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 909
-  Symbols:   407
-  CStrings:  54
+  Functions: 1027
+  Symbols:   428
+  CStrings:  66
 
Symbols:
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_SAFCampoPresentationDescriptor
+ _SAFCampoPresentationTypeGetName
+ ___swift_memcpy33_8
+ _objc_release_x27
+ _objc_release_x28
+ _swift_bridgeObjectRetain_n
+ _swift_deletedAsyncMethodErrorTu
+ _swift_release_x22
+ _swift_release_x28
+ _swift_retain_x25
+ _symbolic $s22IntelligenceSimulation19CampoAudioInjectingP
+ _symbolic SS8expected_SSSg7currentt
+ _symbolic Say_____G 10Foundation3URLV
+ _symbolic Sb
+ _symbolic _____ 22IntelligenceSimulation24CampoAttachmentTransport33_3AD9493B4CBA514B9F6A3CD05CB1C3FFLLO
+ _symbolic _____Sg 10Foundation3URLV
+ _symbolic _____Sg_ABt 10Foundation3URLV
+ _symbolic _____XMT 22IntelligenceSimulation17CampoSiriReplayerC
+ _symbolic ______SS5statet s8DurationV
+ _symbolic ______pSg 22IntelligenceSimulation19CampoAudioInjectingP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation3URLV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 13CampoServices0D14TestAttachmentO
- ___swift_memcpy17_8
- _swift_release_x25
CStrings:
+ " after dismissal, so a new request would resume it; Campo state: "
+ ", not the turn's chat "
+ "; listening would put the spoken turn in the wrong chat"
+ "A spoken Campo turn can't carry an attachment; attach on a typed turn instead"
+ "Campo chat opened for a spoken turn: chatID=%s"
+ "Campo island torn down %s after dismissal"
+ "Campo request sent: chatID=%s attachments=%ld transport=%s"
+ "Campo spoken request sent: chatID=%s audio=%s"
+ "Campo still presented the dismissed chat's island "
+ "Campo's current chat is "
+ "The request carried audio, but this replayer was made without an audio injector; use makeCampoReplayer(audioInjector:)"
+ "The request's audio content has neither a contentPath nor contentData"
+ "The request's audio file isn't readable: "
+ "startSiriRequestWithPayload requires a text, attachment or audio content payload; the request carried none"
- "Campo request sent: chatID=%s"
- "startSiriRequestWithPayload requires a text content payload; Campo chat only accepts text utterances"
```
