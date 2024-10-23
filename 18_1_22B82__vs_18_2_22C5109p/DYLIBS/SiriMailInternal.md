## SiriMailInternal

> `/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal`

```diff

-3401.21.2.11.1
-  __TEXT.__text: 0xe6154
-  __TEXT.__auth_stubs: 0x3fd0
-  __TEXT.__const: 0x5fe0
-  __TEXT.__cstring: 0x2424
-  __TEXT.__constg_swiftt: 0x21bc
-  __TEXT.__swift5_typeref: 0x3738
-  __TEXT.__swift5_fieldmd: 0x1a68
-  __TEXT.__oslogstring: 0x6557
-  __TEXT.__swift5_types: 0x198
-  __TEXT.__swift5_proto: 0x28c
-  __TEXT.__swift5_reflstr: 0x19d3
-  __TEXT.__swift5_assocty: 0x460
+3402.22.1.0.0
+  __TEXT.__text: 0xebd38
+  __TEXT.__auth_stubs: 0x41e0
+  __TEXT.__const: 0x65b0
+  __TEXT.__cstring: 0x2534
+  __TEXT.__constg_swiftt: 0x22f0
+  __TEXT.__swift5_typeref: 0x38a0
+  __TEXT.__swift5_fieldmd: 0x1b90
+  __TEXT.__oslogstring: 0x67f7
+  __TEXT.__swift5_builtin: 0xf0
+  __TEXT.__swift5_reflstr: 0x1b23
+  __TEXT.__swift5_assocty: 0x4f0
+  __TEXT.__swift5_proto: 0x2d0
+  __TEXT.__swift5_types: 0x1ac
   __TEXT.__swift5_protos: 0x2c
-  __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_mpenum: 0x6c
-  __TEXT.__swift5_capture: 0x5c8
-  __TEXT.__unwind_info: 0x2cd8
-  __TEXT.__eh_frame: 0x6000
+  __TEXT.__swift5_mpenum: 0x80
+  __TEXT.__swift5_capture: 0x5e8
+  __TEXT.__unwind_info: 0x2df0
+  __TEXT.__eh_frame: 0x60b8
   __TEXT.__objc_classname: 0xb8
-  __TEXT.__objc_methname: 0x9ec
+  __TEXT.__objc_methname: 0xa1b
   __TEXT.__objc_methtype: 0x1d1
-  __DATA_CONST.__got: 0x1158
+  __DATA_CONST.__got: 0x11a8
   __DATA_CONST.__const: 0x140
-  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f0
+  __DATA_CONST.__objc_selrefs: 0x300
   __DATA_CONST.__objc_protorefs: 0x60
-  __AUTH_CONST.__auth_got: 0x1fe8
-  __AUTH_CONST.__auth_ptr: 0x1760
-  __AUTH_CONST.__const: 0x2470
-  __AUTH_CONST.__objc_const: 0x2658
-  __AUTH.__objc_data: 0x750
-  __AUTH.__data: 0x2eb8
-  __DATA.__data: 0x26e0
-  __DATA.__bss: 0x51d0
-  __DATA.__common: 0x228
+  __AUTH_CONST.__auth_got: 0x20f0
+  __AUTH_CONST.__auth_ptr: 0x1878
+  __AUTH_CONST.__const: 0x2640
+  __AUTH_CONST.__objc_const: 0x2788
+  __AUTH.__objc_data: 0x7a0
+  __AUTH.__data: 0x2fd8
+  __DATA.__data: 0x27e0
+  __DATA.__bss: 0x5a80
+  __DATA.__common: 0x248
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/SiriReferenceResolutionDataModel.framework/SiriReferenceResolutionDataModel
   - /System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities
   - /System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit
+  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4309
-  Symbols:   2302
-  CStrings:  836
+  Functions: 4439
+  Symbols:   2351
+  CStrings:  858
 
Symbols:
+ _NSDocumentTypeDocumentAttribute
+ _NSHTMLTextDocumentType
+ _OBJC_CLASS_$_NSAttributedString
+ _swift_getForeignTypeMetadata
- _LNConnectionOperationRequestTimeout
CStrings:
+ "#MailFlowFactory found DynamicTask<Common.Message.Send>, pushing SendMailFlow"
+ "#ReferenceResolution calling SRR for resolving FormattedString entity"
+ "#ReferenceResolution calling SRR for resolving SiriContentTopic entity"
+ "#ReferenceResolution entity appBundleId %!s(MISSING)"
+ "#ResolveSRREntity invoked, Montara FF enabled."
+ "#ResolveSRREntity invoked, but Montara FF disabled. Returning nil."
+ "#ResolveSRREntity on iOS, converting Markdown to HTML."
+ "#ResolveSRREntity returning HTML string"
+ "#ResolveSRREntity returning raw Markdown, if populated"
+ "#SendMessageFlow accept(input: Input) returning .yes() for input %!s(MISSING)"
+ "#SendMessageFlow change state from: %!s(MISSING) to %!s(MISSING)"
+ "#SendMessageFlow executing action"
+ "#SendMessageFlow pushing SendMailPlan"
+ "#SendMessageFlow pushing SendMailSceneHostPlan"
+ "GenerativeAssistantTools"
+ "MontaraTools"
+ "ReferenceResolution# Found %!l(MISSING)d candidates"
+ "_TtC16SiriMailInternal12SendMailFlow"
+ "com.apple.generativeassistanttools"
+ "com.apple.intelligenceflowd"
+ "dataFromRange:documentAttributes:error:"
+ "length"
+ "referenceResolver"
+ "resolveContextualEntities"
+ "sendMessage(message body: "
- "#MailFlowFactory found DynamicTask<Common.Message.Send>, pushing SendMailPlan"
- "#MailFlowFactory found DynamicTask<Common.Message.Send>, pushing SendMailSceneHostPlan"
- "ReferenceResolution# Found %!l(MISSING)d candidates. Using the first one"

```
