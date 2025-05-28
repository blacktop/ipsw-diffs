## CarCommandsFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin`

```diff

-3301.7.1.0.0
-  __TEXT.__text: 0x1143f8
-  __TEXT.__auth_stubs: 0x2cc0
+3302.6.1.0.0
+  __TEXT.__text: 0x112a08
+  __TEXT.__auth_stubs: 0x2dc0
   __TEXT.__objc_stubs: 0x8a0
   __TEXT.__objc_methlist: 0x5fc
   __TEXT.__oslogstring: 0x10aa
-  __TEXT.__cstring: 0xcecd
+  __TEXT.__cstring: 0xcead
   __TEXT.__objc_classname: 0x19b
-  __TEXT.__objc_methname: 0x19a4
+  __TEXT.__objc_methname: 0x19ac
   __TEXT.__objc_methtype: 0x62a
-  __TEXT.__const: 0x8014
+  __TEXT.__const: 0x7fc4
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__constg_swiftt: 0x51cc
-  __TEXT.__swift5_typeref: 0x36ee
-  __TEXT.__swift5_fieldmd: 0x2778
+  __TEXT.__constg_swiftt: 0x51b4
+  __TEXT.__swift5_typeref: 0x376e
+  __TEXT.__swift5_fieldmd: 0x27c0
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0x2af3
+  __TEXT.__swift5_reflstr: 0x2b53
   __TEXT.__swift5_assocty: 0xce8
-  __TEXT.__swift5_proto: 0x6e0
-  __TEXT.__swift5_types: 0x2d0
+  __TEXT.__swift5_proto: 0x6d0
+  __TEXT.__swift5_types: 0x2cc
   __TEXT.__swift5_capture: 0x624
-  __TEXT.__swift5_protos: 0xd0
+  __TEXT.__swift5_protos: 0xd4
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x61d0
-  __TEXT.__eh_frame: 0x11148
-  __DATA_CONST.__auth_got: 0x1670
-  __DATA_CONST.__got: 0x650
-  __DATA_CONST.__auth_ptr: 0x2d8
-  __DATA_CONST.__const: 0x7b78
+  __TEXT.__unwind_info: 0x62f0
+  __TEXT.__eh_frame: 0x112a0
+  __DATA_CONST.__auth_got: 0x16f0
+  __DATA_CONST.__got: 0x670
+  __DATA_CONST.__auth_ptr: 0x2d0
+  __DATA_CONST.__const: 0x7b80
   __DATA_CONST.__cfstring: 0x60
-  __DATA_CONST.__objc_classlist: 0x230
+  __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA.__objc_const: 0x5280
+  __DATA.__objc_const: 0x5328
   __DATA.__objc_selrefs: 0x780
   __DATA.__objc_protorefs: 0xb0
-  __DATA.__objc_classrefs: 0x1f8
+  __DATA.__objc_classrefs: 0x200
   __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x20
-  __DATA.__objc_data: 0x1f78
-  __DATA.__data: 0xa840
-  __DATA.__common: 0x2d0
+  __DATA.__objc_data: 0x1ee8
+  __DATA.__data: 0xa9c8
+  __DATA.__common: 0x2b0
   __DATA.__bss: 0x9c00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/SiriKitInvocation.framework/SiriKitInvocation
   - /System/Library/PrivateFrameworks/SiriNLUTypes.framework/SiriNLUTypes
   - /System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology
+  - /System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation
   - /System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8746
-  Symbols:   308
-  CStrings:  1396
+  Functions: 8727
+  Symbols:   309
+  CStrings:  1401
 
Symbols:
+ _OBJC_CLASS_$_SRUIFInstrumentationManager
CStrings:
+ "$__lazy_storage_$_cachedRadioEntitySpans"
+ "$__lazy_storage_$_hasCarCommandsUserVocabExactMatch"
+ "$__lazy_storage_$_hasUserVocabExactMatchForOtherDomain"
+ "/Library/Caches/com.apple.xbs/Sources/SiriCarCommands/CarCommandsFlowDelegatePlugin/Flow/Common/CarCommandsSimpleFlow.swift"
+ "Error executing CarCommandActionable:"
+ "Error making generic error dialog:"
+ "Missing NL Parse"
+ "The current Siri turnID is: "
+ "The event metadata is nil. Will not emit the metrics event"
+ "The turnID is nil. Failing early because we need this for the events to be joinable."
+ "This parse has an exact user vocab match for another domain, but does not have an exact user vocab match for CarCommands. Rejecting parse."
+ "_TtC29CarCommandsFlowDelegatePlugin21CarCommandsSimpleFlow"
+ "action"
+ "carCommands#genericErrorResponse"
+ "carCommandsSetDefroster#intentHandledResponse"
+ "generateEventMetaData()"
+ "instrumentationManager"
+ "latestStoredTurn"
+ "makeGenericErrorResponse()"
+ "nlIntent"
+ "sharedManager"
- "$__lazy_storage_$_cachedRadioEntityIdentifiers"
- "$__lazy_storage_$_hasCarCommandsUserVocab"
- "$__lazy_storage_$_hasCarNounEntityWithUserVocabForOtherDomain"
- "$__lazy_storage_$_hasUserVocabForOtherDomain"
- "/Library/Caches/com.apple.xbs/Sources/SiriCarCommands/CarCommandsFlowDelegatePlugin/Flow/Protocols/CarCommandsIntent/SetCarDefrosterIntent+CarCommandsIntent.swift"
- "/Library/Caches/com.apple.xbs/Sources/SiriCarCommands/CarCommandsFlowDelegatePlugin/NL/NLv4/Extensions/UsoTask+CarCommands.swift"
- "Found radio identifier: "
- "No USO identifiers found on radio parse (that's bad)"
- "The userEntity being acted on is likely not a car even though the term \"car\" or a brand name may be present in the utterance."
- "_TtC29CarCommandsFlowDelegatePlugin31CarCommandsControlDefrosterCATs"
- "_TtC29CarCommandsFlowDelegatePlugin37CarCommandsControlDefrosterCATsSimple"
- "carCommandsControlDefroster#needsConfirmationResponse"
- "carCommandsControlDefroster#needsValueResponse"
- "setDefroster:"
- "usoIdentifiersForRadioEntity()"

```
