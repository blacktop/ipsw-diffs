## SocialConversationFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin`

```diff

-3500.18.2.0.0
-  __TEXT.__text: 0xbfb5c
-  __TEXT.__auth_stubs: 0x2890
+3520.24.1.1.2
+  __TEXT.__text: 0xcdb00
+  __TEXT.__auth_stubs: 0x29d0
+  __TEXT.__objc_stubs: 0x4c0
   __TEXT.__objc_methlist: 0x26c
-  __TEXT.__swift5_typeref: 0xc1a
-  __TEXT.__const: 0x2d52
-  __TEXT.__swift5_capture: 0x2e74
-  __TEXT.__oslogstring: 0x187d
-  __TEXT.__cstring: 0xaed8
-  __TEXT.__constg_swiftt: 0x1324
-  __TEXT.__swift5_reflstr: 0x8f2
-  __TEXT.__swift5_fieldmd: 0xbe0
+  __TEXT.__const: 0x30f2
+  __TEXT.__constg_swiftt: 0x1448
+  __TEXT.__swift5_typeref: 0xcd4
+  __TEXT.__swift5_fieldmd: 0xca0
   __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_reflstr: 0x9a2
   __TEXT.__swift5_assocty: 0x240
-  __TEXT.__swift5_proto: 0x13c
-  __TEXT.__swift5_types: 0x124
-  __TEXT.__objc_classname: 0x9e
-  __TEXT.__objc_methname: 0x520
-  __TEXT.__objc_methtype: 0x1a8
-  __TEXT.__swift_as_entry: 0xa4
-  __TEXT.__swift_as_ret: 0x90
-  __TEXT.__swift5_protos: 0xc
+  __TEXT.__swift5_proto: 0x154
+  __TEXT.__swift5_types: 0x138
+  __TEXT.__objc_classname: 0x878
+  __TEXT.__objc_methname: 0xae9
+  __TEXT.__objc_methtype: 0x1af
+  __TEXT.__swift5_capture: 0x3374
+  __TEXT.__oslogstring: 0x1a6d
+  __TEXT.__cstring: 0xa653
+  __TEXT.__swift_as_entry: 0xb4
+  __TEXT.__swift_as_ret: 0xa4
+  __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xc60
-  __TEXT.__eh_frame: 0xdc8
-  __DATA_CONST.__auth_got: 0x1448
-  __DATA_CONST.__got: 0x4d8
-  __DATA_CONST.__auth_ptr: 0x728
-  __DATA_CONST.__const: 0x83a0
-  __DATA_CONST.__objc_classlist: 0xc0
+  __TEXT.__unwind_info: 0xd40
+  __TEXT.__eh_frame: 0xf80
+  __DATA_CONST.__auth_got: 0x14f0
+  __DATA_CONST.__got: 0x508
+  __DATA_CONST.__auth_ptr: 0x778
+  __DATA_CONST.__const: 0x9100
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA.__objc_const: 0x1fe8
+  __DATA.__objc_const: 0x21d8
   __DATA.__objc_selrefs: 0x260
   __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0x2b08
+  __DATA.__data: 0x2d18
+  __DATA.__bss: 0x2810
   __DATA.__common: 0x5e8
-  __DATA.__bss: 0x2590
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents

   - /System/Library/Frameworks/StoreKit.framework/StoreKit
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation
   - /System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/IntelligenceEngine.framework/IntelligenceEngine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 962EBC47-8DD6-3D04-907F-E53860B3DF01
-  Functions: 2483
-  Symbols:   132
-  CStrings:  2206
+  UUID: 74E3097F-85C5-3194-A3F4-33B5AB132DFD
+  Functions: 2651
+  Symbols:   134
+  CStrings:  2249
 
Symbols:
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
- _malloc
CStrings:
+ "$defaultActor"
+ "%{public}s"
+ ": "
+ "CAT execution failed: %s"
+ "CAT file missing: catID=%{public}s expectedPath=%{public}s"
+ "Error executing dialog for "
+ "Error processing intent name': %s"
+ "Invalid CAT ID format: catID=%{public}s"
+ "Invalid parse format from CDM NLU response"
+ "Missing NLv4ToCat mapping for intent: '%{public}s' - social conversation cannot handle this request"
+ "NLv4 supported intent: %s -> %s"
+ "NLv4ToCat mapping fallback used: intent=%{public}s fallback=%{public}s reason=holiday_parse"
+ "New Siri Intent: %s"
+ "No dialog sections found for "
+ "No mapping found in NLv4ToCat.dictionary for intent: '"
+ "No parse available from CDM NLU response"
+ "Sorry, I couldn't process your request"
+ "StaticString should have Unicode scalar representation"
+ "Template directory not found for catGlobals: "
+ "USO parse failed: dialogAct=%{public}s error=%{public}s"
+ "Voice trigger dialog response"
+ "_TtC36SocialConversationFlowDelegatePlugin29SocialConversationCoordinator"
+ "_TtC36SocialConversationFlowDelegatePlugin33SocialConversationFlowServiceImpl"
+ "checkExistenceSiriNewsiri"
+ "checkExistenceSiriOldsiri"
+ "flow"
+ "isSetup"
+ "localeIdentifier"
+ "newSiri"
+ "nlu"
+ "oldSiri"
+ "summariseSiriNewsiri"
+ "summariseSiriSirisname"
- "NLv4 supported intent: %s"
- "self must be a properly aligned pointer for types Pointee and T"

```
