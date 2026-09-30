## IntelligencePlatform

> `/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform`

```diff

-155.13.0.0.0
-  __TEXT.__text: 0x4a1cc8
-  __TEXT.__auth_stubs: 0x4ca0
-  __TEXT.__objc_methlist: 0xa9d4
-  __TEXT.__const: 0x4dc88
-  __TEXT.__cstring: 0x1bf22
-  __TEXT.__swift5_typeref: 0x137aa
-  __TEXT.__constg_swiftt: 0x140b8
-  __TEXT.__swift5_reflstr: 0xb204
-  __TEXT.__swift5_fieldmd: 0x13204
+165.5.0.0.0
+  __TEXT.__text: 0x491604
+  __TEXT.__auth_stubs: 0x4c70
+  __TEXT.__objc_methlist: 0xa9dc
+  __TEXT.__const: 0x4d8f0
+  __TEXT.__swift5_typeref: 0x13616
+  __TEXT.__cstring: 0x16ba3
+  __TEXT.__constg_swiftt: 0x14010
+  __TEXT.__swift5_reflstr: 0xb374
+  __TEXT.__swift5_fieldmd: 0x132a4
   __TEXT.__swift5_builtin: 0x668
-  __TEXT.__swift5_assocty: 0x2f48
-  __TEXT.__swift5_proto: 0x3e20
-  __TEXT.__swift5_types: 0x1548
-  __TEXT.__oslogstring: 0x848b
-  __TEXT.__swift5_capture: 0x5740
+  __TEXT.__swift5_assocty: 0x2f78
+  __TEXT.__swift5_proto: 0x3db4
+  __TEXT.__swift5_types: 0x1534
+  __TEXT.__oslogstring: 0x85fb
+  __TEXT.__swift5_capture: 0x57bc
   __TEXT.__swift_as_entry: 0x2f8
   __TEXT.__swift_as_ret: 0x2c4
   __TEXT.__swift5_protos: 0x204
   __TEXT.__swift5_mpenum: 0x23c
-  __TEXT.__gcc_except_tab: 0x1104
+  __TEXT.__gcc_except_tab: 0x111c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x14dd0
-  __TEXT.__eh_frame: 0x2cbd0
-  __TEXT.__objc_classname: 0x1f5d
-  __TEXT.__objc_methname: 0x18aa2
-  __TEXT.__objc_methtype: 0x342c
-  __TEXT.__objc_stubs: 0x51c0
-  __DATA_CONST.__got: 0x16d0
-  __DATA_CONST.__const: 0x1410
-  __DATA_CONST.__objc_classlist: 0xf10
+  __TEXT.__unwind_info: 0x15228
+  __TEXT.__eh_frame: 0x2e730
+  __TEXT.__objc_classname: 0x5752
+  __TEXT.__objc_methname: 0x1aceb
+  __TEXT.__objc_methtype: 0x3af4
+  __TEXT.__objc_stubs: 0x7ea0
+  __DATA_CONST.__got: 0x1700
+  __DATA_CONST.__const: 0x1440
+  __DATA_CONST.__objc_classlist: 0xf18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3508
+  __DATA_CONST.__objc_selrefs: 0x3510
   __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x608
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0x2660
-  __AUTH_CONST.__const: 0x2d570
+  __AUTH_CONST.__auth_got: 0x2648
+  __AUTH_CONST.__const: 0x2dae8
   __AUTH_CONST.__cfstring: 0x2ea0
-  __AUTH_CONST.__objc_const: 0x2a550
+  __AUTH_CONST.__objc_const: 0x2a678
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x34b8
-  __AUTH.__data: 0x71c0
-  __DATA.__objc_ivar: 0x1590
-  __DATA.__data: 0xee08
-  __DATA.__bss: 0x6bf60
-  __DATA.__common: 0x560
+  __AUTH.__data: 0x7310
+  __DATA.__objc_ivar: 0x1594
+  __DATA.__data: 0xe9e8
+  __DATA.__bss: 0x6b0e0
+  __DATA.__common: 0x2c0
   __DATA_DIRTY.__objc_data: 0x4c88
-  __DATA_DIRTY.__data: 0xbde0
-  __DATA_DIRTY.__bss: 0xa020
+  __DATA_DIRTY.__data: 0xbf58
+  __DATA_DIRTY.__bss: 0xa120
   __DATA_DIRTY.__common: 0x158
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 64496C82-6067-31F8-9B94-6602818E9255
-  Functions: 35995
-  Symbols:   1142
-  CStrings:  7508
+  UUID: 4D848D2C-8214-31D6-A3C1-ED30D7EC1190
+  Functions: 36321
+  Symbols:   1138
+  CStrings:  7443
 
Symbols:
+ _OBJC_CLASS_$_NSUnit
+ _memcmp
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _sqrtf
CStrings:
+ " \n matchingSignal: "
+ "    SELECT ev.occurredAt AS occurredAt,\n           ci.userAlignment AS userAlignment,\n           ci.parameterName AS parameterName,\n           ci.searchLikelihood AS searchLikelihood\n    FROM events ev\n    JOIN candidateInteractions ci ON ci.eventId = ev.id\n    WHERE ci.candidateId = ?\n    ORDER BY ev.occurredAt DESC"
+ "    SELECT id AS id FROM candidates WHERE uuid = ? AND bundleId = ?"
+ "    SELECT ti.occurredAt AS occurredAt,\n           ti.userAlignment AS userAlignment\n    FROM tupleInteractions ti\n    JOIN tuples t ON ti.tupleId = t.id\n    WHERE t.candidateIds = ?\n    ORDER BY ti.occurredAt DESC LIMIT ?"
+ "    SELECT ti.occurredAt AS occurredAt,\n           ti.userAlignment AS userAlignment,\n           ti.tupleData AS tupleData\n    FROM tupleInteractions ti\n    JOIN tupleCandidates tc1 ON ti.tupleId = tc1.tupleId\n    JOIN tupleCandidates tc2 ON ti.tupleId = tc2.tupleId\n    WHERE tc2.candidateId IN ("
+ "    WITH filteredTupleCandidates AS (\n        SELECT tc.tupleId\n        FROM tupleCandidates tc\n        WHERE tc.candidateId IN ("
+ ")\n        GROUP BY tc.tupleId\n        HAVING COUNT(DISTINCT tc.candidateId) >= 2\n    )\n    SELECT\n        ti.occurredAt AS occurredAt,\n        ti.userAlignment AS userAlignment,\n        ti.tupleData AS tupleData\n    FROM tupleInteractions ti\n    JOIN filteredTupleCandidates ftc ON ti.tupleId = ftc.tupleId\n    ORDER BY ti.occurredAt DESC\n    LIMIT ?;"
+ ") AND tc1.candidateId = ?\n    GROUP BY ti.tupleId, ti.eventId\n    ORDER BY ti.occurredAt DESC Limit ?"
+ "007: Support Flexible Tuple Query"
+ "008: Add isLocal and devicePlatform"
+ "009: Add tuple data blob for flexible tuple query"
+ "014: Add remoteDeviceId"
+ "015: Add persistent identifier mapping"
+ "<GDRankerItem: entityID: %@, sourceID: %@, score: %f, entityClass: %@, features: %@, nameScore: %f, contextualScore: %f, entityRelevance: %f, entityRelevanceInferenceEventId: %@, confirmationConfidence: %f, isRelationshipMatch: %d, matchingSignal: %@>, identifierInformation: %@"
+ "@116@0:8@16@24@32@40d48d56d64d72@80d88B96@100@108"
+ "DefaultResolverInteractionsView: getFlexibleQueryWithRequired: No parameter candidates found"
+ "DefaultResolverInteractionsView: getFlexibleQueryWithRequired: No required candidate found for category %d"
+ "DefaultResolverInteractionsView: getFlexibleQueryWithRequired: parameterId: %s, requiredCandidateId: %lld"
+ "PersistentEntityIdentifier"
+ "T@\"NSString\",R,C,N,V_matchingSignal"
+ "The candidateId for tuple candidate %s is nil."
+ "UPDATE events SET devicePlatform = ?"
+ "_TtCV20IntelligencePlatform13ContactFinderP33_64D4ABC625BF09549B5378474BE94F3911GuardedData"
+ "_matchingSignal"
+ "candidateSelectStatement"
+ "customType"
+ "events_occurredAt"
+ "hashedIdentifier"
+ "initWithEntityID:sourceID:entityClass:features:score:nameScore:contextualScore:entityRelevance:entityRelevanceInferenceEventId:confirmationConfidence:isRelationshipMatch:matchingSignal:identifierInformation:"
+ "initialized"
+ "matchingSignal"
+ "searchLikelihood"
+ "tinyLatency"
+ "tupleInteractionFastSelectStatement"
+ "tupleInteractions_occurredAt"
+ "tupleInteractions_tupleId_occurredAt"
- "    SELECT ev.occurredAt AS occurredAt,\n            t.userAlignment AS userAlignment\n    FROM events ev\n    JOIN tupleInteractions t ON t.eventId = ev.id\n    WHERE t.candidateIdsHash IN (?)\n    ORDER BY ev.occurredAt DESC"
- "    SELECT ev.occurredAt AS occurredAt,\n           ci.userAlignment AS userAlignment\n    FROM events ev\n    JOIN candidateInteractions ci ON ci.eventId = ev.id\n    JOIN candidates c ON c.id == ci.candidateId\n    WHERE (c.uuid = ?) AND (c.bundleId = ?)\n    ORDER BY ev.occurredAt DESC"
- "<GDRankerItem: entityID: %@, sourceID: %@, score: %f, entityClass: %@, features: %@, nameScore: %f, contextualScore: %f, entityRelevance: %f, entityRelevanceInferenceEventId: %@, confirmationConfidence: %f, isRelationshipMatch: %d>, identifierInformation: %@"
- "@108@0:8@16@24@32@40d48d56d64d72@80d88B96@100"
- "initWithEntityID:sourceID:entityClass:features:score:nameScore:contextualScore:entityRelevance:entityRelevanceInferenceEventId:confirmationConfidence:isRelationshipMatch:identifierInformation:"
- "tupleInteractionsSelectStatement"

```
