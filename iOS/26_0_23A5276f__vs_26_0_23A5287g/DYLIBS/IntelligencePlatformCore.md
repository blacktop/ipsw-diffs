## IntelligencePlatformCore

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore`

```diff

-149.0.4.0.0
-  __TEXT.__text: 0xabaff0
-  __TEXT.__auth_stubs: 0xade0
+151.0.3.0.0
+  __TEXT.__text: 0xab0784
+  __TEXT.__auth_stubs: 0xad70
   __TEXT.__objc_methlist: 0x2e64
-  __TEXT.__const: 0x74831
+  __TEXT.__const: 0x749e1
   __TEXT.__dlopen_cstrs: 0xc0
-  __TEXT.__cstring: 0x4710c
-  __TEXT.__swift5_typeref: 0x1e4e4
-  __TEXT.__constg_swiftt: 0x23304
-  __TEXT.__swift5_reflstr: 0x262bf
-  __TEXT.__swift5_fieldmd: 0x29d98
-  __TEXT.__swift5_builtin: 0x4d8
-  __TEXT.__swift5_mpenum: 0x164
+  __TEXT.__cstring: 0x4699c
+  __TEXT.__swift5_typeref: 0x1e62c
+  __TEXT.__constg_swiftt: 0x23404
+  __TEXT.__swift5_reflstr: 0x2630f
+  __TEXT.__swift5_fieldmd: 0x29dfc
+  __TEXT.__swift5_builtin: 0x4ec
+  __TEXT.__swift5_mpenum: 0x16c
   __TEXT.__swift5_assocty: 0x2f38
-  __TEXT.__swift5_proto: 0x6528
-  __TEXT.__swift5_types: 0x21f0
+  __TEXT.__swift5_proto: 0x6538
+  __TEXT.__swift5_types: 0x21f4
   __TEXT.__swift5_protos: 0x378
   __TEXT.__swift_as_entry: 0x1208
   __TEXT.__swift_as_ret: 0xfac
-  __TEXT.__oslogstring: 0x1f5f3
-  __TEXT.__swift5_capture: 0x4508
+  __TEXT.__oslogstring: 0x1e943
+  __TEXT.__swift5_capture: 0x4520
   __TEXT.__gcc_except_tab: 0x1c8
-  __TEXT.__unwind_info: 0x27f88
-  __TEXT.__eh_frame: 0x616f4
+  __TEXT.__unwind_info: 0x28400
+  __TEXT.__eh_frame: 0x61184
   __TEXT.__objc_classname: 0x4b3
-  __TEXT.__objc_methname: 0x9ff4
+  __TEXT.__objc_methname: 0x9f67
   __TEXT.__objc_methtype: 0x26ef
   __TEXT.__objc_stubs: 0x1160
-  __DATA_CONST.__got: 0x4440
-  __DATA_CONST.__const: 0xab0
-  __DATA_CONST.__objc_classlist: 0x1208
+  __DATA_CONST.__got: 0x4398
+  __DATA_CONST.__const: 0xa60
+  __DATA_CONST.__objc_classlist: 0x1210
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ce8
+  __DATA_CONST.__objc_selrefs: 0x2ca0
   __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x5700
-  __AUTH_CONST.__const: 0x447a0
+  __AUTH_CONST.__auth_got: 0x56c8
+  __AUTH_CONST.__const: 0x44800
   __AUTH_CONST.__cfstring: 0x360
-  __AUTH_CONST.__objc_const: 0x2c3e0
+  __AUTH_CONST.__objc_const: 0x2c558
   __AUTH.__objc_data: 0x36a8
-  __AUTH.__data: 0x18338
+  __AUTH.__data: 0x18518
   __DATA.__objc_ivar: 0xc4
-  __DATA.__data: 0x11340
-  __DATA.__bss: 0x86e50
-  __DATA.__common: 0x1a28
+  __DATA.__data: 0x113a0
+  __DATA.__bss: 0x87050
+  __DATA.__common: 0x1a40
   __DATA_DIRTY.__objc_data: 0x41e0
-  __DATA_DIRTY.__data: 0x27830
+  __DATA_DIRTY.__data: 0x27740
   __DATA_DIRTY.__bss: 0x2ca90
   __DATA_DIRTY.__common: 0x17c0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 18B01D02-1664-360F-AE47-B3B8AC315DD5
-  Functions: 60884
-  Symbols:   893
-  CStrings:  10182
+  UUID: B4AD53A4-20C0-3D99-A291-E92B021A4719
+  Functions: 60849
+  Symbols:   889
+  CStrings:  10114
 
Symbols:
+ _GDSearchLog
- _OBJC_CLASS_$_BMIntelligenceEngineInteraction
- _OBJC_CLASS_$_BMIntelligenceEngineInteractionCandidateID
- _OBJC_CLASS_$_BMIntelligenceEngineInteractionCandidateInteraction
- _OBJC_CLASS_$_PPNamedEntityQuery
- _OBJC_CLASS_$_PPNamedEntityStore
CStrings:
+ "\nSelect columns: "
+ "AutonamingMessagesAggregationHandler: Person id %s, could not find a most occurring name or contact: max name count is %ld, max contact count is %ld over a total of %ld inferences."
+ "AutonamingMessagesAggregationHandler: Person id %s, found most occurring inference contact %s with count %ld over %ld inferences."
+ "AutonamingMessagesAggregationHandler: Person id %s, found most occurring inference name %s with count %ld over %ld inferences."
+ "CREATE VIRTUAL TABLE search USING ipsearch("
+ "Commands: %s"
+ "DefaultResolverInteractionsViewGenerator: performUpdate: it is unsupported."
+ "EntityQuery(\nTable: "
+ "Need to either materialize results or pass a block that uses the cursor"
+ "ORDER BY search_rank DESC"
+ "Processing deletion events. Calling processBiomeEvent as \"shouldProcess\": %{bool}d and \"advance\": %{bool}d"
+ "Search clause is already defined on query. At most one search can be conducted on a query."
+ "_TtC24IntelligencePlatformCore11EntityQuery"
+ "groupBy"
+ "having"
+ "initWithURL:isEmbedded:"
+ "iterTopicRecordsWithQuery:error:block:"
+ "orderBy"
+ "s.rank AS search_rank"
+ "search"
+ "selectColumns"
+ "setMatchingAlgorithms:"
+ "sharedService"
+ "useCase"
+ "v24@?0@\"PPTopicRecord\"8^B16"
- "    SELECT\n        \""
- "    SELECT\n        id\n    FROM\n        interactions"
- "    SELECT ent.id AS entityId\n    FROM entities ent\n    JOIN interactionEntities ie\n    ON ie.entityRowid = ent.rowid\n    WHERE ( ie.interactionRowid = ? )\n    AND ie.parameter IN ('recipientHandles', 'senderHandle', 'contactHandles')"
- "    SELECT startDate AS occurredAt,\n    type AS type,\n    durationSeconds AS durationSeconds,\n    bundleId AS bundleId,\n    rowId AS interactionRowid\n    FROM interactions\n    WHERE (id = ?)"
- " (timestamp DOUBLE PRIMARY KEY)"
- " WHERE originId = "
- "\"\n    WHERE\n        updated > ?\n    AND\n        id IS NOT NULL"
- "\" AS id,\n        \""
- "\" AS updated\n    FROM\n        \""
- "$__lazy_storage_$_photoLibrary"
- "AutonamingMessagesAggregationHandler: Person id %s, could not find a most occuring name or contact: max name count is %ld, max contact count is %ld over a total of %ld inferences."
- "AutonamingMessagesAggregationHandler: Person id %s, found most occuring inference contact %s with count %ld over %ld inferences."
- "AutonamingMessagesAggregationHandler: Person id %s, found most occuring inference name %s with count %ld over %ld inferences."
- "CREATE TEMPORARY TABLE "
- "Calling processBiomeEvent as \"shouldProcess\": %{bool}d and \"advance\": %{bool}d"
- "DELETE FROM candidateInteractions WHERE eventId IN (SELECT id FROM events WHERE source = 0)"
- "DELETE FROM events WHERE source = 0"
- "DELETE FROM tupleInteractions WHERE eventId IN (SELECT id FROM events WHERE source = 0)"
- "DefaultResolver: %{public}s got final bookmark: %f, %f"
- "DefaultResolver: %{public}s is a required source but unavailable"
- "DefaultResolver: Completed the deletion of the orphaned data"
- "DefaultResolver: Reading from the view %{public}s "
- "DefaultResolver: deleting all siriRemembers data"
- "DefaultResolver: deleting orphaned data"
- "DefaultResolver: siriRemembers changed interaction: %s"
- "DefaultResolver: skip the siriRemembers interaction without entities: %s"
- "DefaultResolver: skip the siriRemembers interaction: %s"
- "DefaultResolver: truncate the intelligenceEngine candidates with first %ld: %ld"
- "DefaultResolver: truncate the siriRemembers candidates with first %ld: %ld"
- "DefaultResolverInteractionsViewGenerator Inserting candidate interaction: %s"
- "DefaultResolverInteractionsViewGenerator Inserting tuple interaction: %s"
- "DefaultResolverInteractionsViewGenerator: %s has been pruned, new first timestamp is %f"
- "DefaultResolverInteractionsViewGenerator: %s: timestamps: %f , %f"
- "DefaultResolverInteractionsViewGenerator: Update the Event table"
- "DefaultResolverInteractionsViewGenerator: Update the internal event tables with RowId: %lld"
- "DefaultResolverInteractionsViewGenerator: checking for any stream pruning"
- "DefaultResolverInteractionsViewGenerator: deleteAllEvents: from %ld%s"
- "DefaultResolverInteractionsViewGenerator: deleteEvents: from %ld harvested at %ld different times"
- "DefaultResolverInteractionsViewGenerator: failed to update from %s. Error: %@"
- "DefaultResolverInteractionsViewGenerator: finished update from %s"
- "DefaultResolverInteractionsViewGenerator: performUpdate: clear required"
- "DefaultResolverInteractionsViewGenerator: performUpdate: control source full rebuild"
- "DefaultResolverInteractionsViewGenerator: performUpdate: incremental update"
- "DefaultResolverInteractionsViewGenerator: performUpdate: priority at end current = %s."
- "DefaultResolverInteractionsViewGenerator: performUpdate: priority at start current = %s."
- "DefaultResolverInteractionsViewGenerator: performUpdate: truncation required"
- "DefaultResolverInteractionsViewGenerator: performUpdate: weekly schedule full rebuild"
- "DefaultResolverInteractionsViewGenerator: processStream %s: controlSourceFullRebuild"
- "DefaultResolverInteractionsViewGenerator: processStream %s: ignore bookmark: %{bool}d"
- "DefaultResolverInteractionsViewGenerator: processStream %s: processing tombstones"
- "DefaultResolverInteractionsViewGenerator: processStream %s: processing tombstones failed: %@, deleting all interactions"
- "DefaultResolverInteractionsViewGenerator: receiveInput error: processing: %s: %s"
- "DefaultResolverInteractionsViewGenerator: receiveInput error: unknown event body in %s: %s"
- "DefaultResolverInteractionsViewGenerator: received IE InteractionStore input"
- "DefaultResolverInteractionsViewGenerator: received IE InteractionStore input with eventId: %lld"
- "DefaultResolverInteractionsViewGenerator: received input from stream %s"
- "Empty RowId for the events table"
- "Expected siriRemembers view source"
- "INSERT INTO events (originId, trigger, occurredAt, source, biomeEventTimestamp) VALUES (?,?,?,?,?)"
- "INSERT OR IGNORE INTO "
- "INSERT OR REPLACE INTO candidateInteractions (eventId, candidateId, userAlignment) VALUES (?,?,?)"
- "INSERT OR REPLACE INTO candidates (uuid, bundleId) VALUES (?,?)"
- "INSERT OR REPLACE INTO tupleInteractions (eventId, candidateIdsHash, userAlignment) VALUES (?,?,?)"
- "INStartCallIntent"
- "IntelligenceEngine.Interaction.Donation"
- "Invalid bookmark type"
- "Invalid identifier in the biome events"
- "Invalid sessionId and statementIndex for biome events"
- "LanguageCounter: failed to retrieve named entities for messages language detection"
- "SELECT * FROM candidates WHERE (uuid = ?) AND (bundleId = ?)"
- "SELECT * FROM events WHERE (originId = ?)"
- "The occurredAt is unknown for IntelligenceEngine events"
- "UPDATE events SET source = source & ~"
- "UPDATE events SET source = source & ~?"
- "UPDATE events SET source = source & ~? WHERE biomeEventTimestamp < ?"
- "UPDATE events SET source = source & ~? WHERE biomeEventTimestamp IN (SELECT timestamp FROM "
- "ViewUpdate.BiomeSource: DefaultResolverInteractionsSourceStream: unexpected stream: %s"
- "appIntentInvocationUUID"
- "candidateId"
- "candidateIds"
- "defaultResolverInteractionsView"
- "initWithRequested:"
- "interactionRowid"
- "iterNamedEntityRecordsWithQuery:error:block:"
- "sessionId"
- "sirikitIntentItemId"
- "statementIndex"
- "tmp_deleteAllInteractions_"
- "transcriptStatementId"
- "trigger"
- "tupleInteraction"
- "userAlignment"
- "v24@?0@\"PPNamedEntityRecord\"8^B16"

```
