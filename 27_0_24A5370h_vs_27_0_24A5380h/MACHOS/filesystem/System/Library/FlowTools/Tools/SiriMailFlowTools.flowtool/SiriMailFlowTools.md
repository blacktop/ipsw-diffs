## SiriMailFlowTools

> `/System/Library/FlowTools/Tools/SiriMailFlowTools.flowtool/SiriMailFlowTools`

```diff

-  __TEXT.__text: 0x46c0c
-  __TEXT.__auth_stubs: 0x1350
-  __TEXT.__objc_stubs: 0x240
-  __TEXT.__const: 0x14c0
-  __TEXT.__constg_swiftt: 0x36c
-  __TEXT.__swift5_typeref: 0x616
-  __TEXT.__swift5_reflstr: 0x503
-  __TEXT.__swift5_fieldmd: 0x590
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__cstring: 0x254
-  __TEXT.__oslogstring: 0xffd
-  __TEXT.__swift5_proto: 0xa8
-  __TEXT.__swift5_types: 0x34
+  __TEXT.__text: 0x49aa0
+  __TEXT.__auth_stubs: 0x1410
+  __TEXT.__objc_stubs: 0x460
+  __TEXT.__const: 0x16c0
+  __TEXT.__constg_swiftt: 0x3d4
+  __TEXT.__swift5_typeref: 0x6c4
+  __TEXT.__swift5_reflstr: 0x5a9
+  __TEXT.__swift5_fieldmd: 0x5fc
+  __TEXT.__swift5_assocty: 0x78
+  __TEXT.__cstring: 0x2a4
+  __TEXT.__oslogstring: 0x13da
+  __TEXT.__swift5_proto: 0xb0
+  __TEXT.__swift5_types: 0x3c
   __TEXT.__swift_as_entry: 0xe4
   __TEXT.__swift_as_ret: 0x218
   __TEXT.__swift_as_cont: 0x3c8
   __TEXT.__swift5_capture: 0xf0
   __TEXT.__objc_classname: 0xed
-  __TEXT.__objc_methname: 0x282
+  __TEXT.__objc_methname: 0x411
   __TEXT.__objc_methtype: 0x1
-  __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x1398
-  __TEXT.__eh_frame: 0x3e10
-  __DATA_CONST.__const: 0xa60
+  __TEXT.__swift5_protos: 0x14
+  __TEXT.__unwind_info: 0x13e8
+  __TEXT.__eh_frame: 0x3cc0
+  __DATA_CONST.__const: 0xba8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x9b0
-  __DATA_CONST.__got: 0x2f0
-  __DATA_CONST.__auth_ptr: 0x740
-  __DATA.__objc_const: 0xa38
-  __DATA.__objc_selrefs: 0x90
-  __DATA.__data: 0xa30
-  __DATA.__bss: 0x1450
+  __DATA_CONST.__auth_got: 0xa10
+  __DATA_CONST.__got: 0x360
+  __DATA_CONST.__auth_ptr: 0x778
+  __DATA.__objc_const: 0xad8
+  __DATA.__objc_selrefs: 0x118
+  __DATA.__data: 0xa90
+  __DATA.__bss: 0x1520
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Speech.framework/Speech

   - /System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition
   - /System/Library/PrivateFrameworks/FlowToolTypes.framework/FlowToolTypes
   - /System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow
+  - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
+  - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI
   - /System/Library/PrivateFrameworks/SiriMailUIModel.framework/SiriMailUIModel
   - /System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1471
-  Symbols:   142
-  CStrings:  102
+  Functions: 1543
+  Symbols:   157
+  CStrings:  132
 
Sections:
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_capture : content changed
~ __DATA_CONST.__objc_classlist : content changed
Symbols:
+ _OBJC_CLASS_$_AssistantSiriAnalytics
+ _OBJC_CLASS_$_FTDMailSchemaFTDMailApplicationInfo
+ _OBJC_CLASS_$_FTDMailSchemaFTDMailCreateOrUpdateDraftInvoked
+ _OBJC_CLASS_$_FTDMailSchemaFTDMailRecipientsInfo
+ _OBJC_CLASS_$_FTDMailSchemaFTDMailSendDraftInvoked
+ _OBJC_CLASS_$_FTDSchemaFTDClientEvent
+ _OBJC_CLASS_$_FTDSchemaFTDClientEventMetadata
+ _OBJC_CLASS_$_SISchemaUUID
+ _objc_release
+ _objc_release_x25
+ _objc_release_x26
+ _objc_retain
+ _objc_retain_x23
+ _swift_conformsToProtocol2
+ _swift_unknownObjectRelease
CStrings:
+ "#ComposeMailFlowTool - foreground Mail compose detected, suppressing Siri response to avoid blank auto-snippet over the compose sheet"
+ "#FTDMailMetricsSubmitter %s"
+ "#FTDMailMetricsSubmitter Failed to create FTDMailSchemaFTDMailApplicationInfo"
+ "#FTDMailMetricsSubmitter Failed to create FTDMailSchemaFTDMailCreateOrUpdateDraftInvoked"
+ "#FTDMailMetricsSubmitter Failed to create FTDMailSchemaFTDMailRecipientsInfo"
+ "#FTDMailMetricsSubmitter Failed to create FTDMailSchemaFTDMailSendDraftInvoked"
+ "#FTDMailMetricsSubmitter Failed to create FTDSchemaFTDClientEvent"
+ "#FTDMailMetricsSubmitter Failed to create FTDSchemaFTDClientEventMetadata"
+ "#FTDMailMetricsSubmitter Unmapped FlowToolInvocationContext.ResponseMode case %s — reporting UNKNOWN"
+ "#MailFlowTool foregrounded app %s differs from executing app %s, but composing with attachments in display mode — letting AppIntent execute in foreground so the user can see the attachment in the full UI"
+ "_metricsSubmitter"
+ "emitMessage:"
+ "initWithNSUUID:"
+ "setAppBundleId:"
+ "setContactRecipients:"
+ "setEventMetadata:"
+ "setFlowToolClientInteractionId:"
+ "setHasForcedBackgroundMode:"
+ "setHasSpecifiedMailAccount:"
+ "setHasVendedSnippet:"
+ "setIsForegrounded:"
+ "setMailApplication:"
+ "setMailCreateOrUpdateDraftInvoked:"
+ "setMailSendDraftInvoked:"
+ "setNonContactRecipients:"
+ "setRecipients:"
+ "setUserResponseMode:"
+ "sharedStream"
+ "submitCreateOrUpdateDraftInvoked"
+ "submitSendDraftInvoked"

```
