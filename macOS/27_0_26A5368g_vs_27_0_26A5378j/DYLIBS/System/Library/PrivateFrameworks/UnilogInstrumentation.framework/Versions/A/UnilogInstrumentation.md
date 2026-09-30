## UnilogInstrumentation

> `/System/Library/PrivateFrameworks/UnilogInstrumentation.framework/Versions/A/UnilogInstrumentation`

```diff

-  __TEXT.__text: 0xc370
+  __TEXT.__text: 0x18e4c
   __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x9f0
-  __TEXT.__swift5_typeref: 0x376
-  __TEXT.__constg_swiftt: 0x3d4
-  __TEXT.__swift5_fieldmd: 0x284
-  __TEXT.__swift5_reflstr: 0xec
+  __TEXT.__const: 0x1010
+  __TEXT.__constg_swiftt: 0x69c
+  __TEXT.__swift5_typeref: 0x5f8
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_types: 0x40
-  __TEXT.__cstring: 0x1c1
-  __TEXT.__oslogstring: 0x101
-  __TEXT.__swift5_capture: 0x38
-  __TEXT.__swift5_protos: 0x8
-  __TEXT.__swift5_proto: 0x5c
-  __TEXT.__swift_as_entry: 0xc
-  __TEXT.__swift_as_ret: 0x8
-  __TEXT.__swift_as_cont: 0x8
+  __TEXT.__swift5_reflstr: 0x215
+  __TEXT.__swift5_fieldmd: 0x47c
+  __TEXT.__swift5_types: 0x68
+  __TEXT.__swift5_proto: 0x8c
+  __TEXT.__swift_as_entry: 0x50
+  __TEXT.__swift_as_ret: 0x30
+  __TEXT.__swift_as_cont: 0x34
+  __TEXT.__oslogstring: 0x2f1
+  __TEXT.__cstring: 0x1f1
+  __TEXT.__swift5_protos: 0x10
+  __TEXT.__swift5_capture: 0xe4
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x398
-  __TEXT.__eh_frame: 0x398
+  __TEXT.__unwind_info: 0x688
+  __TEXT.__eh_frame: 0xa70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x60
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x30
-  __DATA_CONST.__got: 0x148
-  __AUTH_CONST.__const: 0x5e8
-  __AUTH_CONST.__objc_const: 0x600
-  __AUTH_CONST.__auth_got: 0x568
-  __AUTH.__objc_data: 0x160
-  __AUTH.__data: 0x4f8
-  __DATA.__data: 0x320
-  __DATA.__bss: 0x990
+  __DATA_CONST.__objc_selrefs: 0x38
+  __DATA_CONST.__got: 0x230
+  __AUTH_CONST.__const: 0x908
+  __AUTH_CONST.__objc_const: 0x710
+  __AUTH_CONST.__auth_got: 0x7d0
+  __AUTH.__objc_data: 0x1b0
+  __AUTH.__data: 0x8a8
+  __DATA.__data: 0x640
+  __DATA.__bss: 0xe90
   __DATA.__common: 0x20
+  - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
   - /System/Library/PrivateFrameworks/Dendrite.framework/Versions/A/Dendrite
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/Versions/A/IntelligencePlatformLibrary
   - /System/Library/PrivateFrameworks/UnilogCommonLibrary.framework/Versions/A/UnilogCommonLibrary
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 269
-  Symbols:   241
-  CStrings:  23
+  Functions: 474
+  Symbols:   336
+  CStrings:  36
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __DATA_CONST.__const : content changed
Symbols:
+ _MobileGestalt_copy_buildVersion_obj
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_internalBuild
+ _OBJC_CLASS_$_BMPublisherOptions
+ __DATA__TtC21UnilogInstrumentation18IdentifierProvider
+ __IVARS__TtC21UnilogInstrumentation18IdentifierProvider
+ __METACLASS_DATA__TtC21UnilogInstrumentation18IdentifierProvider
+ ___swift_closure_destructorTm
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___unnamed_7
+ __swift_closure_destructor.29Tm
+ __swift_implicitisolationactor_to_executor_cast
+ _associated conformance 21UnilogInstrumentation10PruneScopeOSHAASQ
+ _associated conformance 21UnilogInstrumentation15IdentifierSpaceOSHAASQ
+ _associated conformance 21UnilogInstrumentation18IdentifierProviderC8CacheKey33_D2E5F6091AAE096B04697F2BAAC6CCFFLLVSHAASQ
+ _associated conformance 21UnilogInstrumentation19LongLivedIdentifierVSHAASQ
+ _objc_msgSend$initWithStartDate:endDate:maxEvents:lastN:reversed:
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_checkMetadataState
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initEnumMetadataSingleCaseWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithTake
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_endAccess
+ _swift_getAssociatedTypeWitness
+ _swift_getEnumCaseMultiPayload
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getTupleTypeLayout2
+ _swift_getTupleTypeMetadata2
+ _swift_storeEnumTagSinglePayloadGeneric
+ _symbolic $s21UnilogInstrumentation14PrunableStream33_551DDB4CD3A161A961E50635C079D2CELLP
+ _symbolic $s21UnilogInstrumentation17IdentifierStorageP
+ _symbolic SDy__________G 21UnilogInstrumentation18IdentifierProviderC8CacheKey33_D2E5F6091AAE096B04697F2BAAC6CCFFLLV AA09LongLivedC0V
+ _symbolic _____ 10Foundation4DateV
+ _symbolic _____ 19UnilogCommonLibrary6ClientO
+ _symbolic _____ 21UnilogInstrumentation10PruneRangeO
+ _symbolic _____ 21UnilogInstrumentation10PruneScopeO
+ _symbolic _____ 21UnilogInstrumentation15IdentifierSpaceO
+ _symbolic _____ 21UnilogInstrumentation15InMemoryStorageC16TimestampedEvent33_5DFF3211C0598BF1CE1398156B8971E3LLV
+ _symbolic _____ 21UnilogInstrumentation17PrunableStreamFor33_551DDB4CD3A161A961E50635C079D2CELLO
+ _symbolic _____ 21UnilogInstrumentation18IdentifierProviderC
+ _symbolic _____ 21UnilogInstrumentation18IdentifierProviderC8CacheKey33_D2E5F6091AAE096B04697F2BAAC6CCFFLLV
+ _symbolic _____ 21UnilogInstrumentation19LongLivedIdentifierV
+ _symbolic _____ 21UnilogInstrumentation21IdentifierStreamErrorO
+ _symbolic _____ 21UnilogInstrumentation21IdentifierStreamStoreV
+ _symbolic _____6client______5spacet 19UnilogCommonLibrary6ClientO 0A15Instrumentation15IdentifierSpaceO
+ _symbolic _____Sg 10Foundation8CalendarV
+ _symbolic _____Sg 10Foundation8TimeZoneV
+ _symbolic _____Sg 19UnilogCommonLibrary13DeviceContextV
+ _symbolic _____Sg 19UnilogCommonLibrary21LongTermAggregationIdV
+ _symbolic _____Sg 21UnilogInstrumentation11BiomeWriter33_551DDB4CD3A161A961E50635C079D2CELLC
+ _symbolic _____Sg 21UnilogInstrumentation19LongLivedIdentifierV
+ _symbolic _____Sg 27IntelligencePlatformLibrary24ExternalSchemaStreamDataV
+ _symbolic _____Sg_ABt 19UnilogCommonLibrary21LongTermAggregationIdV
+ _symbolic _____XDXMT 21UnilogInstrumentation12BiomeStorageC
+ _symbolic ______AAt 10Foundation4DateV
+ _symbolic ___________t 19UnilogCommonLibrary6ClientO 0A15Instrumentation15IdentifierSpaceO
+ _symbolic ______p 19UnilogCommonLibrary18AggregationPayloadP
+ _symbolic ______pXmT 21UnilogInstrumentation14PrunableStream33_551DDB4CD3A161A961E50635C079D2CELLP
+ _symbolic ______pXp 19UnilogCommonLibrary18AggregationPayloadP
+ _symbolic ______p___________tYbc 21UnilogInstrumentation17IdentifierStorageP 0A13CommonLibrary6ClientO AA0C5SpaceO
+ _symbolic _____ySay_____y______GGG 2os21OSAllocatedUnfairLockV 21UnilogInstrumentation15InMemoryStorageC16TimestampedEvent33_5DFF3211C0598BF1CE1398156B8971E3LLV 0E13CommonLibrary07StagingK0V
+ _symbolic _____ySay_____y______GGG 2os21OSAllocatedUnfairLockV 21UnilogInstrumentation15InMemoryStorageC16TimestampedEvent33_5DFF3211C0598BF1CE1398156B8971E3LLV 10Foundation4DataV
+ _symbolic _____y_____G 21UnilogInstrumentation13SourceWrapper33_551DDB4CD3A161A961E50635C079D2CELLV 27IntelligencePlatformLibrary0O0O7StreamsO0A0O12SafariSearchO11AggregationO
+ _symbolic _____y_____G 21UnilogInstrumentation13SourceWrapper33_551DDB4CD3A161A961E50635C079D2CELLV 27IntelligencePlatformLibrary0O0O7StreamsO0A0O12SafariSearchO5StageO
+ _symbolic _____y_____G 21UnilogInstrumentation17PrunableStreamFor33_551DDB4CD3A161A961E50635C079D2CELLO 27IntelligencePlatformLibrary0P0O7StreamsO0A0O12SafariSearchO11AggregationO
+ _symbolic _____y_____G 21UnilogInstrumentation17PrunableStreamFor33_551DDB4CD3A161A961E50635C079D2CELLO 27IntelligencePlatformLibrary0P0O7StreamsO0A0O12SafariSearchO5StageO
+ _symbolic _____y_____G 21UnilogInstrumentation17PrunableStreamFor33_551DDB4CD3A161A961E50635C079D2CELLO 27IntelligencePlatformLibrary0P0O7StreamsO0A0O4SiriO5StageO
+ _symbolic _____y_____G 21UnilogInstrumentation17PrunableStreamFor33_551DDB4CD3A161A961E50635C079D2CELLO 27IntelligencePlatformLibrary0P0O7StreamsO0A0O4SiriO9ProcessedO
+ _symbolic _____y______G 21UnilogInstrumentation15InMemoryStorageC16TimestampedEvent33_5DFF3211C0598BF1CE1398156B8971E3LLV 0A13CommonLibrary07StagingG0V
+ _symbolic _____y______G 21UnilogInstrumentation15InMemoryStorageC16TimestampedEvent33_5DFF3211C0598BF1CE1398156B8971E3LLV 10Foundation4DataV
+ _symbolic _____y__________G s18_DictionaryStorageC 21UnilogInstrumentation18IdentifierProviderC8CacheKey33_D2E5F6091AAE096B04697F2BAAC6CCFFLLV AC09LongLivedE0V
+ _symbolic _____y_____y______GG s23_ContiguousArrayStorageC 21UnilogInstrumentation08InMemoryC0C16TimestampedEvent33_5DFF3211C0598BF1CE1398156B8971E3LLV 0D13CommonLibrary07StagingI0V
+ _symbolic _____y_____y______GG s23_ContiguousArrayStorageC 21UnilogInstrumentation08InMemoryC0C16TimestampedEvent33_5DFF3211C0598BF1CE1398156B8971E3LLV 10Foundation4DataV
- ___swift_destroy_boxed_opaque_existential_0
- ___unnamed_4
- _symbolic _____y_____G s23_ContiguousArrayStorageC 19UnilogCommonLibrary12StagingEventV
CStrings:
+ "Aggregate event dropped: client has no aggregation stream"
+ "Aggregate event: %s"
+ "Aggregation prune skipped: client %d has no aggregation stream"
+ "Error serializing aggregate event: %@"
+ "Failed to prune identifier stream: %@"
+ "Failed to read identifier stream: %@"
+ "Failed to write identifier: %@"
+ "Processed prune skipped: client %d has no processed stream"
+ "Prune failed for %s: %@"
+ "Prune requested (scope: %s, range: %s) — no-op for LogStorage"
+ "Safari client"
+ "UnilogInstrumentation.IdentifierProvider"
+ "client space "

```
