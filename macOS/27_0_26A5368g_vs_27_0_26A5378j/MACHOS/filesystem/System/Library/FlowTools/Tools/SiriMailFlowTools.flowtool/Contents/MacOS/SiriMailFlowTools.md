## SiriMailFlowTools

> `/System/Library/FlowTools/Tools/SiriMailFlowTools.flowtool/Contents/MacOS/SiriMailFlowTools`

```diff

-  __TEXT.__text: 0x3e7c8
-  __TEXT.__auth_stubs: 0x10c0
-  __TEXT.__objc_stubs: 0x240
-  __TEXT.__const: 0x14a0
-  __TEXT.__constg_swiftt: 0x36c
-  __TEXT.__swift5_typeref: 0x5f6
-  __TEXT.__swift5_reflstr: 0x503
-  __TEXT.__swift5_fieldmd: 0x590
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__cstring: 0x234
-  __TEXT.__oslogstring: 0xd9d
-  __TEXT.__swift5_proto: 0xa8
-  __TEXT.__swift5_types: 0x34
+  __TEXT.__text: 0x41388
+  __TEXT.__auth_stubs: 0x1130
+  __TEXT.__objc_stubs: 0x460
+  __TEXT.__const: 0x1690
+  __TEXT.__constg_swiftt: 0x3d4
+  __TEXT.__swift5_typeref: 0x698
+  __TEXT.__swift5_reflstr: 0x5a9
+  __TEXT.__swift5_fieldmd: 0x5fc
+  __TEXT.__swift5_assocty: 0x78
+  __TEXT.__cstring: 0x284
+  __TEXT.__oslogstring: 0x101a
+  __TEXT.__swift5_proto: 0xb0
+  __TEXT.__swift5_types: 0x3c
   __TEXT.__swift_as_entry: 0xe0
   __TEXT.__swift_as_ret: 0x1f8
   __TEXT.__swift_as_cont: 0x384
   __TEXT.__swift5_capture: 0xf0
   __TEXT.__objc_classname: 0xed
-  __TEXT.__objc_methname: 0x282
+  __TEXT.__objc_methname: 0x411
   __TEXT.__objc_methtype: 0x1
-  __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x1270
-  __TEXT.__eh_frame: 0x39a0
-  __DATA_CONST.__const: 0xa50
+  __TEXT.__swift5_protos: 0x14
+  __TEXT.__unwind_info: 0x1320
+  __TEXT.__eh_frame: 0x39a8
+  __DATA_CONST.__const: 0xb98
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x868
-  __DATA_CONST.__got: 0x2a8
-  __DATA_CONST.__auth_ptr: 0x718
-  __DATA.__objc_const: 0xa38
-  __DATA.__objc_selrefs: 0x90
-  __DATA.__data: 0xa08
-  __DATA.__bss: 0x1450
+  __DATA_CONST.__auth_got: 0x8a0
+  __DATA_CONST.__got: 0x318
+  __DATA_CONST.__auth_ptr: 0x750
+  __DATA.__objc_const: 0xad8
+  __DATA.__objc_selrefs: 0x118
+  __DATA.__data: 0xa58
+  __DATA.__bss: 0x1520
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Speech.framework/Versions/A/Speech

   - /System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/Versions/A/CoreEmbeddedSpeechRecognition
   - /System/Library/PrivateFrameworks/FlowToolTypes.framework/Versions/A/FlowToolTypes
   - /System/Library/PrivateFrameworks/IntelligenceFlow.framework/Versions/A/IntelligenceFlow
+  - /System/Library/PrivateFrameworks/SiriAnalytics.framework/Versions/A/SiriAnalytics
+  - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/Versions/A/SiriInstrumentation
   - /System/Library/PrivateFrameworks/SiriMailUI.framework/Versions/A/SiriMailUI
   - /System/Library/PrivateFrameworks/SiriMailUIModel.framework/Versions/A/SiriMailUIModel
   - /System/Library/PrivateFrameworks/ToolKit.framework/Versions/A/ToolKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1339
-  Symbols:   111
-  CStrings:  95
+  Functions: 1406
+  Symbols:   120
+  CStrings:  123
 
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
+ _swift_unknownObjectRelease
CStrings:
+ "#FTDMailMetricsSubmitter %s"
+ "#FTDMailMetricsSubmitter Failed to create FTDMailSchemaFTDMailApplicationInfo"
+ "#FTDMailMetricsSubmitter Failed to create FTDMailSchemaFTDMailCreateOrUpdateDraftInvoked"
+ "#FTDMailMetricsSubmitter Failed to create FTDMailSchemaFTDMailRecipientsInfo"
+ "#FTDMailMetricsSubmitter Failed to create FTDMailSchemaFTDMailSendDraftInvoked"
+ "#FTDMailMetricsSubmitter Failed to create FTDSchemaFTDClientEvent"
+ "#FTDMailMetricsSubmitter Failed to create FTDSchemaFTDClientEventMetadata"
+ "#FTDMailMetricsSubmitter Unmapped FlowToolInvocationContext.ResponseMode case %s — reporting UNKNOWN"
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
