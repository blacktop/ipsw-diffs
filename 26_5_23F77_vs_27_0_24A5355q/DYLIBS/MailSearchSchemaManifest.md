## MailSearchSchemaManifest

> `/System/Library/PrivateFrameworks/MailSearchSchemaManifest.framework/MailSearchSchemaManifest`

```diff

-1.4.20.0.0
-  __TEXT.__text: 0xb914
-  __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__const: 0x1ee2
-  __TEXT.__constg_swiftt: 0x59c
-  __TEXT.__swift5_typeref: 0x350
-  __TEXT.__swift5_fieldmd: 0x2c0
-  __TEXT.__swift5_reflstr: 0x17c
-  __TEXT.__swift5_assocty: 0x3f0
-  __TEXT.__cstring: 0x1fb2
-  __TEXT.__swift5_proto: 0x14c
-  __TEXT.__swift5_types: 0xac
+2.0.4.0.0
+  __TEXT.__text: 0xc4cc
+  __TEXT.__const: 0x215a
+  __TEXT.__constg_swiftt: 0x644
+  __TEXT.__swift5_typeref: 0x3d2
+  __TEXT.__swift5_fieldmd: 0x2f0
+  __TEXT.__swift5_reflstr: 0x1ce
+  __TEXT.__swift5_assocty: 0x450
+  __TEXT.__cstring: 0x1f32
+  __TEXT.__swift5_proto: 0x164
+  __TEXT.__swift5_types: 0xb8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x3d8
-  __DATA_CONST.__got: 0x58
+  __TEXT.__unwind_info: 0x408
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x158
-  __AUTH_CONST.__const: 0xfdc
-  __AUTH.__data: 0x20
-  __DATA.__data: 0x528
-  __DATA.__bss: 0x2980
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x100c
+  __AUTH_CONST.__auth_got: 0x168
+  __AUTH.__data: 0x50
+  __DATA.__data: 0x548
+  __DATA.__bss: 0x2c80
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/Dendrite.framework/Dendrite
   - /System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 5A38F947-AB75-370B-8678-B3B2FEDE37C6
-  Functions: 379
-  Symbols:   151
-  CStrings:  196
+  UUID: 9370F5C3-C76E-3B7A-BBE0-4057FB600C41
+  Functions: 401
+  Symbols:   160
+  CStrings:  200
 
Symbols:
+ _associated conformance 24MailSearchSchemaManifest0ab14SpanAttribute_D0V17PoirotSchematizer07MessageD12ConstructingAaD0cdJ0
+ _associated conformance 24MailSearchSchemaManifest0ab15TraceAttribute_D0V17PoirotSchematizer07MessageD12ConstructingAaD0cdJ0
+ _associated conformance 24MailSearchSchemaManifest0ab17SessionAttribute_D0V17PoirotSchematizer07MessageD12ConstructingAaD0cdJ0
+ _associated conformance 24MailSearchSchemaManifest0ab6ClientC8ProviderVAA0eC9ProvidingAA13SpanAttributeAaDP_17PoirotSchematizer07MessageD12Constructing
+ _associated conformance 24MailSearchSchemaManifest0ab6ClientC8ProviderVAA0eC9ProvidingAA14TraceAttributeAaDP_17PoirotSchematizer07MessageD12Constructing
+ _associated conformance 24MailSearchSchemaManifest0ab6ClientC8ProviderVAA0eC9ProvidingAA16SessionAttributeAaDP_17PoirotSchematizer07MessageD12Constructing
+ _swift_bridgeObjectRetain_n
+ _swift_release_x20
+ _swift_retain_x20
+ _symbolic 13SpanAttribute_____Qz 24MailSearchSchemaManifest06ClientC9ProvidingP
+ _symbolic 14TraceAttribute_____Qz 24MailSearchSchemaManifest06ClientC9ProvidingP
+ _symbolic 16SessionAttribute_____Qz 24MailSearchSchemaManifest06ClientC9ProvidingP
+ _symbolic _____ 24MailSearchSchemaManifest0ab14SpanAttribute_D0V
+ _symbolic _____ 24MailSearchSchemaManifest0ab15TraceAttribute_D0V
+ _symbolic _____ 24MailSearchSchemaManifest0ab17SessionAttribute_D0V
- ___swift_destroy_boxed_opaque_existential_1
- ___swift_project_boxed_opaque_existential_1
- _swift_release
- _symbolic Say_____G s5UInt8V
CStrings:
+ "apple.mail_search"
+ "apple.mail_search.LogPayload"
+ "apple.mail_search.common.SectionType"
+ "apple.mail_search.ranker.ResultComponent"
+ "apple.mail_search.ranker.ResultRankingAttribute"
+ "apple.mail_search.ranker.ResultsRanked"
+ "apple.mail_search.trace.SessionAttribute"
+ "apple.mail_search.trace.SpanAttribute"
+ "apple.mail_search.trace.TraceAttribute"
+ "apple.mail_search.ui.BucketizedToken"
+ "apple.mail_search.ui.BuildType"
+ "apple.mail_search.ui.CategorizationState"
+ "apple.mail_search.ui.CharCountBucket"
+ "apple.mail_search.ui.DimensionContext"
+ "apple.mail_search.ui.DisplayContext"
+ "apple.mail_search.ui.DisplayEnded"
+ "apple.mail_search.ui.DisplayEndedReason"
+ "apple.mail_search.ui.DisplayStarted"
+ "apple.mail_search.ui.DisplayStartedReason"
+ "apple.mail_search.ui.InputDetected"
+ "apple.mail_search.ui.InteractionType"
+ "apple.mail_search.ui.MailCategory"
+ "apple.mail_search.ui.MailCategorySubtype"
+ "apple.mail_search.ui.MailScope"
+ "apple.mail_search.ui.QueryComponent"
+ "apple.mail_search.ui.ResultAttribute"
+ "apple.mail_search.ui.ResultReceived"
+ "apple.mail_search.ui.ResultSection"
+ "apple.mail_search.ui.SearchViewAppeared"
+ "apple.mail_search.ui.SearchViewAppearedReason"
+ "apple.mail_search.ui.SearchViewContext"
+ "apple.mail_search.ui.SearchViewDisappeared"
+ "apple.mail_search.ui.SearchViewDisappearedReason"
+ "apple.mail_search.ui.SessionIdResetContext"
+ "apple.mail_search.ui.SessionIdResetEnded"
+ "apple.mail_search.ui.SessionIdResetStarted"
+ "apple.mail_search.ui.Token"
+ "apple.mail_search.ui.UserInteractionDetected"
+ "apple.mail_search.ui.WordCountBucket"
+ "sessionStartTimestampInSeconds"
- "apple.mailsearch"
- "apple.mailsearch.LogPayload"
- "apple.mailsearch.mail_search.common.SectionType"
- "apple.mailsearch.mail_search.ranker.ResultComponent"
- "apple.mailsearch.mail_search.ranker.ResultRankingAttribute"
- "apple.mailsearch.mail_search.ranker.ResultsRanked"
- "apple.mailsearch.mail_search.ui.BucketizedToken"
- "apple.mailsearch.mail_search.ui.BuildType"
- "apple.mailsearch.mail_search.ui.CategorizationState"
- "apple.mailsearch.mail_search.ui.CharCountBucket"
- "apple.mailsearch.mail_search.ui.DimensionContext"
- "apple.mailsearch.mail_search.ui.DisplayContext"
- "apple.mailsearch.mail_search.ui.DisplayEnded"
- "apple.mailsearch.mail_search.ui.DisplayEndedReason"
- "apple.mailsearch.mail_search.ui.DisplayStarted"
- "apple.mailsearch.mail_search.ui.DisplayStartedReason"
- "apple.mailsearch.mail_search.ui.InputDetected"
- "apple.mailsearch.mail_search.ui.InteractionType"
- "apple.mailsearch.mail_search.ui.MailCategory"
- "apple.mailsearch.mail_search.ui.MailCategorySubtype"
- "apple.mailsearch.mail_search.ui.MailScope"
- "apple.mailsearch.mail_search.ui.QueryComponent"
- "apple.mailsearch.mail_search.ui.ResultAttribute"
- "apple.mailsearch.mail_search.ui.ResultReceived"
- "apple.mailsearch.mail_search.ui.ResultSection"
- "apple.mailsearch.mail_search.ui.SearchViewAppeared"
- "apple.mailsearch.mail_search.ui.SearchViewAppearedReason"
- "apple.mailsearch.mail_search.ui.SearchViewContext"
- "apple.mailsearch.mail_search.ui.SearchViewDisappeared"
- "apple.mailsearch.mail_search.ui.SearchViewDisappearedReason"
- "apple.mailsearch.mail_search.ui.SessionIdResetContext"
- "apple.mailsearch.mail_search.ui.SessionIdResetEnded"
- "apple.mailsearch.mail_search.ui.SessionIdResetStarted"
- "apple.mailsearch.mail_search.ui.Token"
- "apple.mailsearch.mail_search.ui.UserInteractionDetected"
- "apple.mailsearch.mail_search.ui.WordCountBucket"

```
