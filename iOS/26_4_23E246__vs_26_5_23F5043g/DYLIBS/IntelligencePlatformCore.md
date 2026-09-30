## IntelligencePlatformCore

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore`

```diff

-165.6.3.0.0
-  __TEXT.__text: 0xaff9d0
-  __TEXT.__auth_stubs: 0xaeb0
-  __TEXT.__objc_methlist: 0x2ebc
-  __TEXT.__const: 0x7dcb9
+165.9.0.0.0
+  __TEXT.__text: 0xaf526c
+  __TEXT.__auth_stubs: 0xad80
+  __TEXT.__objc_methlist: 0x2ecc
+  __TEXT.__const: 0x7dbb9
   __TEXT.__dlopen_cstrs: 0xc0
-  __TEXT.__swift5_typeref: 0x1e92a
-  __TEXT.__cstring: 0x3120b
-  __TEXT.__constg_swiftt: 0x235d4
-  __TEXT.__swift5_reflstr: 0x2661f
-  __TEXT.__swift5_fieldmd: 0x2a0fc
+  __TEXT.__swift5_typeref: 0x1e894
+  __TEXT.__cstring: 0x3030b
+  __TEXT.__constg_swiftt: 0x23574
+  __TEXT.__swift5_reflstr: 0x265bf
+  __TEXT.__swift5_fieldmd: 0x2a06c
   __TEXT.__swift5_builtin: 0x4d8
   __TEXT.__swift5_mpenum: 0x170
   __TEXT.__swift5_assocty: 0x3040
   __TEXT.__swift5_proto: 0x6594
-  __TEXT.__swift5_types: 0x2224
+  __TEXT.__swift5_types: 0x2218
   __TEXT.__swift5_protos: 0x37c
   __TEXT.__swift_as_entry: 0x1208
   __TEXT.__swift_as_ret: 0xfa8
-  __TEXT.__oslogstring: 0x1fca3
-  __TEXT.__swift5_capture: 0x3fb0
+  __TEXT.__oslogstring: 0x1ef33
+  __TEXT.__swift5_capture: 0x3f34
   __TEXT.__gcc_except_tab: 0x1bc
-  __TEXT.__unwind_info: 0x284e8
-  __TEXT.__eh_frame: 0x61a5c
-  __TEXT.__objc_classname: 0xa83d
-  __TEXT.__objc_methname: 0x19395
+  __TEXT.__unwind_info: 0x28388
+  __TEXT.__eh_frame: 0x61404
+  __TEXT.__objc_classname: 0xa82d
+  __TEXT.__objc_methname: 0x19265
   __TEXT.__objc_methtype: 0x2f92
-  __TEXT.__objc_stubs: 0x7e20
-  __DATA_CONST.__got: 0x4488
-  __DATA_CONST.__const: 0xaa8
+  __TEXT.__objc_stubs: 0x7b60
+  __DATA_CONST.__got: 0x43a8
+  __DATA_CONST.__const: 0xa60
   __DATA_CONST.__objc_classlist: 0x1218
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e28
+  __DATA_CONST.__objc_selrefs: 0x2d80
   __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x5768
-  __AUTH_CONST.__const: 0x442e8
+  __AUTH_CONST.__auth_got: 0x56d0
+  __AUTH_CONST.__const: 0x440a8
   __AUTH_CONST.__cfstring: 0x360
-  __AUTH_CONST.__objc_const: 0x2c748
+  __AUTH_CONST.__objc_const: 0x2c760
   __AUTH.__objc_data: 0x36a8
   __AUTH.__data: 0x182a8
   __DATA.__objc_ivar: 0xc4
-  __DATA.__data: 0x12c58
+  __DATA.__data: 0x12c08
   __DATA.__bss: 0x878d0
-  __DATA.__common: 0x1a48
+  __DATA.__common: 0x1a40
   __DATA_DIRTY.__objc_data: 0x41e0
-  __DATA_DIRTY.__data: 0x25d58
+  __DATA_DIRTY.__data: 0x25c58
   __DATA_DIRTY.__bss: 0x2cf10
-  __DATA_DIRTY.__common: 0x17c8
+  __DATA_DIRTY.__common: 0x17c0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0DDD5325-1351-3C4D-8CFA-081900E62622
-  Functions: 63212
-  Symbols:   890
-  CStrings:  10511
+  UUID: F2300EA1-16E1-3597-AA87-7C680374B048
+  Functions: 63138
+  Symbols:   887
+  CStrings:  10382
 
Symbols:
- _OBJC_CLASS_$_BMIntelligenceEngineInteraction
- _OBJC_CLASS_$_BMIntelligenceEngineInteractionCandidateID
- _OBJC_CLASS_$_BMIntelligenceEngineInteractionCandidateInteraction
CStrings:
+ "DefaultResolverInteractionsViewGenerator: performUpdate: it is unsupported."
+ "T@\"NSArray\",R,N,G_enrichmentPhotos"
+ "_enrichmentPhotos"
+ "enrichmentPhotos"
- "    SELECT\n        \""
- "    SELECT\n        id\n    FROM\n        interactions"
- "    SELECT ent.id AS entityId\n    FROM entities ent\n    JOIN interactionEntities ie\n    ON ie.entityRowid = ent.rowid\n    WHERE ( ie.interactionRowid = ? )\n    AND ie.parameter IN ('recipients', 'sender', 'contacts')"
- "    SELECT startDate AS occurredAt,\n    type AS type,\n    durationSeconds AS durationSeconds,\n    bundleId AS bundleId,\n    rowId AS interactionRowid,\n    isLocal AS isLocal,\n    devicePlatform AS devicePlatform,\n    remoteDeviceId AS remoteDeviceId\n    FROM interactions\n    WHERE (id = ?)"
- " (timestamp DOUBLE PRIMARY KEY)"
- " WHERE originId = "
- "\"\n    WHERE\n        updated > ?\n    AND\n        id IS NOT NULL"
- "\" AS id,\n        \""
- "\" AS updated\n    FROM\n        \""
- "AlgorithmicStationSiriEntity"
- "ArtistSiriEntity"
- "AudioCapableDeviceSiriEntity"
- "CREATE TEMPORARY TABLE "
- "ContactLabeledDateEntity"
- "ContactLabeledPostalAddressEntity"
- "ContactLabeledValueEntity"
- "CurrentLocationEntity"
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
- "DefaultResolverInteractionsViewGenerator: event.absoluteTimestamp is nil"
- "DefaultResolverInteractionsViewGenerator: failed to update from %s. Error: %@"
- "DefaultResolverInteractionsViewGenerator: finished update from %s"
- "DefaultResolverInteractionsViewGenerator: performUpdate: clear required"
- "DefaultResolverInteractionsViewGenerator: performUpdate: control source full rebuild"
- "DefaultResolverInteractionsViewGenerator: performUpdate: feature flag is disabled."
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
- "INSERT INTO events (originId, trigger, occurredAt, source, biomeEventTimestamp, isLocal, devicePlatform, remoteDeviceId) VALUES (?,?,?,?,?,?,?,?)"
- "INSERT OR IGNORE INTO "
- "INSERT OR IGNORE INTO tupleCandidates (tupleId, candidateId) VALUES (?,?)"
- "INSERT OR IGNORE INTO tuples (candidateIds) VALUES (?)"
- "INSERT OR REPLACE INTO candidateInteractions (eventId, candidateId, userAlignment, parameterName, searchLikelihood) VALUES (?,?,?,?,?)"
- "INSERT OR REPLACE INTO candidates (uuid, bundleId, type) VALUES (?,?,?)"
- "INSERT OR REPLACE INTO tupleInteractions (eventId, tupleId, userAlignment, tupleData, occurredAt) VALUES (?,?,?,?,?)"
- "INStartAudioCallIntent"
- "INStartCallIntent"
- "INStartVideoCallIntent"
- "IntelligenceEngine.Interaction.Donation"
- "Invalid bookmark type"
- "Invalid identifier in the biome events"
- "Invalid sessionId and statementIndex for biome events"
- "KNDocumentEntity"
- "LiveStationSiriEntity"
- "LiveTVChannelEntity"
- "LocationSearchEntity"
- "MediaControlsDevice"
- "NewsProviderEntity"
- "PlaylistSiriEntity"
- "PodcastCollectionEntity"
- "RCRecordingEntity"
- "RadioShowEpisodeSiriEntity"
- "RadioShowSiriEntity"
- "SELECT * FROM candidates WHERE (uuid = ?) AND (bundleId = ?)"
- "SELECT * FROM events WHERE (originId = ?)"
- "SELECT * FROM tuples WHERE (candidateIds = ?)"
- "SendMessageIntent"
- "ShazamSongEntity"
- "Skipping candidate interaction: %{private}s of type %s"
- "SongCollectionSiriEntity"
- "SportsEventEntity"
- "SportsTeamAppEntity"
- "StartFaceTimeCallIntent"
- "StartTelephonyCallIntent"
- "TPDocumentEntity"
- "The occurredAt is unknown for IntelligenceEngine events"
- "UPDATE events SET source = source & ~"
- "UPDATE events SET source = source & ~?"
- "UPDATE events SET source = source & ~? WHERE biomeEventTimestamp < ?"
- "UPDATE events SET source = source & ~? WHERE biomeEventTimestamp < ? AND remoteDeviceId = ?"
- "UPDATE events SET source = source & ~? WHERE biomeEventTimestamp IN (SELECT timestamp FROM "
- "UPDATE events SET source = source & ~? WHERE remoteDeviceId = ?"
- "ViewUpdate.BiomeSource: DefaultResolverInteractionsSourceStream: unexpected stream: %s"
- "WarmupMusicQueueResultSiriEntity"
- "appIntentInvocationUUID"
- "candidateId"
- "candidateIds"
- "defaultResolverInteractionsView"
- "event.absoluteTimestamp is nil"
- "file"
- "hasSearchLikelihood"
- "interactionRowid"
- "parameterName"
- "primitive"
- "schema"
- "searchLikelihood"
- "sessionId"
- "sirikitIntentItemId"
- "statementIndex"
- "tmp_deleteAllInteractions_"
- "tool"
- "transcriptStatementId"
- "trigger"
- "tupleInteraction"
- "typeName"
- "userAlignment"

```
