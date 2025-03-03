## IFFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/IFFlowPlugin`

```diff

-3404.62.2.0.0
-  __TEXT.__text: 0x50478
-  __TEXT.__auth_stubs: 0x2a40
+3404.69.1.0.0
+  __TEXT.__text: 0x5cbe4
+  __TEXT.__auth_stubs: 0x2ac0
   __TEXT.__objc_methlist: 0x158
-  __TEXT.__cstring: 0x15d6
-  __TEXT.__const: 0xf10
+  __TEXT.__cstring: 0x16e6
+  __TEXT.__const: 0xef0
   __TEXT.__constg_swiftt: 0x478
-  __TEXT.__swift5_typeref: 0xabc
-  __TEXT.__swift5_reflstr: 0x705
+  __TEXT.__swift5_typeref: 0xa8c
+  __TEXT.__swift5_reflstr: 0x6e5
   __TEXT.__swift5_fieldmd: 0x5c8
   __TEXT.__swift5_proto: 0x64
   __TEXT.__swift5_types: 0x54
   __TEXT.__objc_classname: 0x24
   __TEXT.__objc_methname: 0x770
   __TEXT.__objc_methtype: 0x19e
-  __TEXT.__oslogstring: 0x31d2
+  __TEXT.__oslogstring: 0x3232
   __TEXT.__swift5_assocty: 0xb8
-  __TEXT.__swift_as_entry: 0xcc
+  __TEXT.__swift_as_entry: 0xd0
   __TEXT.__swift_as_ret: 0x104
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_capture: 0x178
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x9b8
-  __TEXT.__eh_frame: 0x1ab0
-  __DATA_CONST.__auth_got: 0x1520
-  __DATA_CONST.__got: 0xb38
-  __DATA_CONST.__auth_ptr: 0x728
-  __DATA_CONST.__const: 0x900
+  __TEXT.__unwind_info: 0xa40
+  __TEXT.__eh_frame: 0x1d18
+  __DATA_CONST.__auth_got: 0x1560
+  __DATA_CONST.__got: 0xb40
+  __DATA_CONST.__auth_ptr: 0x738
+  __DATA_CONST.__const: 0x9b0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0xd70
+  __DATA.__objc_const: 0xd10
   __DATA.__objc_selrefs: 0x320
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x1170
-  __DATA.__bss: 0xc70
-  __DATA.__common: 0x38
+  __DATA.__data: 0x1178
+  __DATA.__bss: 0xc60
+  __DATA.__common: 0x30
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 667
-  Symbols:   189
-  CStrings:  429
+  Functions: 693
+  Symbols:   191
+  CStrings:  437
 
Symbols:
+ __swiftEmptySetSingleton
+ _objc_release_x9
+ _objc_retain_x28
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
- _swift_willThrow
CStrings:
+ "%s Cancelling input due to user cancel signal"
+ "%s Execution should never reach here since we are providing implementation of onAsync function"
+ "%s Ignoring input as it does not contain NLRouter info"
+ ".gettingUserIdentity"
+ "IFFlow SearchTool invoked + ShowASR FF Enabled + PCS result(s). Sending Reveal ASR AceCommand"
+ "IFFlow received unsupported failure %s"
+ "IFFlowError.noSessionID: Session identifier fetching failed with error: "
+ "IFFlowError.noUserID: User identifier is not present for remote session"
+ "PCSCommon#CATFallback"
+ "PQACommon#CATDisambiguation"
+ "SearchAnswerEntity"
+ "Unable to retrieve currentSessionIdentifier with error: %s"
+ "Unexpected PrescribedPlan: .searchTool"
+ "Unexpected parse received: %s"
+ "actionForInput(_:)"
+ "nil execution source"
- "IFFlow SearchTool invoked + ShowASR FF Enabled. Appending Reveal ASR AceCommand"
- "IFFlow not accepting input. No supported utterance found."
- "IFFlow valid directInvocation detected."
- "IFFlow value prompt received direct SiriX input instead of NLRouterParse. Using observed utterance from environment (%s)"
- "Unable to retrieve currentSessionIdentifier. All messages will be dropped. %@"
- "_currentUtterance"
- "currentIFSessionId"
- "parseInterpreter"

```
