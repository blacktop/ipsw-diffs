## IntelligencePlatformCore

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore`

```diff

-155.13.0.0.0
-  __TEXT.__text: 0xaf7758
-  __TEXT.__auth_stubs: 0xae00
-  __TEXT.__objc_methlist: 0x2eac
-  __TEXT.__const: 0x7d441
+165.5.0.0.0
+  __TEXT.__text: 0xafbe84
+  __TEXT.__auth_stubs: 0xaed0
+  __TEXT.__objc_methlist: 0x2ebc
+  __TEXT.__const: 0x7dcc9
   __TEXT.__dlopen_cstrs: 0xc0
-  __TEXT.__cstring: 0x46c7c
-  __TEXT.__swift5_typeref: 0x1e74e
-  __TEXT.__constg_swiftt: 0x233ec
-  __TEXT.__swift5_reflstr: 0x2640f
-  __TEXT.__swift5_fieldmd: 0x29ed4
+  __TEXT.__swift5_typeref: 0x1e92a
+  __TEXT.__cstring: 0x3120b
+  __TEXT.__constg_swiftt: 0x235d4
+  __TEXT.__swift5_reflstr: 0x2662f
+  __TEXT.__swift5_fieldmd: 0x2a0fc
   __TEXT.__swift5_builtin: 0x4d8
   __TEXT.__swift5_mpenum: 0x170
-  __TEXT.__swift5_assocty: 0x2f20
-  __TEXT.__swift5_proto: 0x6534
-  __TEXT.__swift5_types: 0x21f0
-  __TEXT.__swift5_protos: 0x378
-  __TEXT.__swift_as_entry: 0x1214
-  __TEXT.__swift_as_ret: 0xfb4
-  __TEXT.__oslogstring: 0x1e9f3
-  __TEXT.__swift5_capture: 0x4520
+  __TEXT.__swift5_assocty: 0x3040
+  __TEXT.__swift5_proto: 0x6594
+  __TEXT.__swift5_types: 0x2224
+  __TEXT.__swift5_protos: 0x37c
+  __TEXT.__swift_as_entry: 0x1208
+  __TEXT.__swift_as_ret: 0xfa8
+  __TEXT.__oslogstring: 0x1fca3
+  __TEXT.__swift5_capture: 0x3fb0
   __TEXT.__gcc_except_tab: 0x1bc
-  __TEXT.__unwind_info: 0x28738
-  __TEXT.__eh_frame: 0x61728
-  __TEXT.__objc_classname: 0x4b3
-  __TEXT.__objc_methname: 0xa0b2
-  __TEXT.__objc_methtype: 0x2729
-  __TEXT.__objc_stubs: 0x1160
-  __DATA_CONST.__got: 0x4370
-  __DATA_CONST.__const: 0xa60
-  __DATA_CONST.__objc_classlist: 0x1210
+  __TEXT.__unwind_info: 0x284c8
+  __TEXT.__eh_frame: 0x61900
+  __TEXT.__objc_classname: 0xa83d
+  __TEXT.__objc_methname: 0x19395
+  __TEXT.__objc_methtype: 0x2f92
+  __TEXT.__objc_stubs: 0x7e20
+  __DATA_CONST.__got: 0x4488
+  __DATA_CONST.__const: 0xaa8
+  __DATA_CONST.__objc_classlist: 0x1218
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d10
+  __DATA_CONST.__objc_selrefs: 0x2e28
   __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x5710
-  __AUTH_CONST.__const: 0x451c0
+  __AUTH_CONST.__auth_got: 0x5778
+  __AUTH_CONST.__const: 0x442e8
   __AUTH_CONST.__cfstring: 0x360
-  __AUTH_CONST.__objc_const: 0x2c5b0
+  __AUTH_CONST.__objc_const: 0x2c748
   __AUTH.__objc_data: 0x36a8
-  __AUTH.__data: 0x18198
+  __AUTH.__data: 0x182a8
   __DATA.__objc_ivar: 0xc4
-  __DATA.__data: 0x14550
-  __DATA.__bss: 0x86d50
-  __DATA.__common: 0x1a40
+  __DATA.__data: 0x12c58
+  __DATA.__bss: 0x878d0
+  __DATA.__common: 0x1a48
   __DATA_DIRTY.__objc_data: 0x41e0
-  __DATA_DIRTY.__data: 0x24950
-  __DATA_DIRTY.__bss: 0x2cd10
-  __DATA_DIRTY.__common: 0x17c0
+  __DATA_DIRTY.__data: 0x25d58
+  __DATA_DIRTY.__bss: 0x2cf10
+  __DATA_DIRTY.__common: 0x17c8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 26864E49-2287-3DAA-BB7B-AC0A4124FBCD
-  Functions: 61249
-  Symbols:   888
-  CStrings:  10153
+  UUID: 98E5EA46-FCC3-30A0-A81D-BE21DDE55138
+  Functions: 63188
+  Symbols:   890
+  CStrings:  10511
 
Symbols:
+ _CNContactExternalUUIDKey
+ _OBJC_CLASS_$_BMAppIntent
+ _OBJC_CLASS_$_BMIntelligenceEngineInteraction
+ _OBJC_CLASS_$_BMIntelligenceEngineInteractionCandidateID
+ _OBJC_CLASS_$_BMIntelligenceEngineInteractionCandidateInteraction
+ _OBJC_CLASS_$_CNMutableContact
+ _OBJC_CLASS_$_NSCompoundPredicate
+ _memcmp
- _OBJC_CLASS_$_BMLocationHashedCoordinates
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _sqrt
CStrings:
+ "    SELECT\n        \""
+ "    SELECT\n        id\n    FROM\n        interactions"
+ "    SELECT ent.id AS entityId\n    FROM entities ent\n    JOIN interactionEntities ie\n    ON ie.entityRowid = ent.rowid\n    WHERE ( ie.interactionRowid = ? )\n    AND ie.parameter IN ('recipients', 'sender', 'contacts')"
+ "    SELECT startDate AS occurredAt,\n    type AS type,\n    durationSeconds AS durationSeconds,\n    bundleId AS bundleId,\n    rowId AS interactionRowid,\n    isLocal AS isLocal,\n    devicePlatform AS devicePlatform,\n    remoteDeviceId AS remoteDeviceId\n    FROM interactions\n    WHERE (id = ?)"
+ " (timestamp DOUBLE PRIMARY KEY)"
+ " WHERE originId = "
+ "\"\n    WHERE\n        updated > ?\n    AND\n        id IS NOT NULL"
+ "\" AS id,\n        \""
+ "\" AS updated\n    FROM\n        \""
+ "%s: Entity lookup result for %s: %s"
+ "%s: Found valid cached mapping for hashed ID %s"
+ "%s: Found valid cached negative result for hashed ID %s"
+ "%s: Performing fresh entity lookup for %s"
+ "/Library/Caches/com.apple.xbs/E8139D47-9946-4B2D-A71F-AF282D3FE206/TemporaryDirectory.bheNfX/Sources/GRDB/GRDB/GRDB/Core/Row.swift"
+ "@\"<BMSpotlightLibrary>\"16@0:8"
+ "AlgorithmicStationSiriEntity"
+ "ArtistSiriEntity"
+ "AudioCapableDeviceSiriEntity"
+ "CREATE TEMPORARY TABLE "
+ "ContactLabeledDateEntity"
+ "ContactLabeledPostalAddressEntity"
+ "ContactLabeledValueEntity"
+ "ContactStoreProvider: No person info available for contact matching"
+ "ContactStoreProvider: Stored mapping - hashedId: %s, localId: %s"
+ "Could not convert event of type %s to BMAppIntent"
+ "CurrentLocationEntity"
+ "DELETE FROM candidateInteractions WHERE eventId IN (SELECT id FROM events WHERE source = 0)"
+ "DELETE FROM events WHERE source = 0"
+ "DELETE FROM tupleInteractions WHERE eventId IN (SELECT id FROM events WHERE source = 0)"
+ "DefaultResolver: %{public}s got final bookmark: %f, %f"
+ "DefaultResolver: %{public}s is a required source but unavailable"
+ "DefaultResolver: Completed the deletion of the orphaned data"
+ "DefaultResolver: Reading from the view %{public}s "
+ "DefaultResolver: deleting all siriRemembers data"
+ "DefaultResolver: deleting orphaned data"
+ "DefaultResolver: siriRemembers changed interaction: %s"
+ "DefaultResolver: skip the siriRemembers interaction without entities: %s"
+ "DefaultResolver: skip the siriRemembers interaction: %s"
+ "DefaultResolver: truncate the intelligenceEngine candidates with first %ld: %ld"
+ "DefaultResolver: truncate the siriRemembers candidates with first %ld: %ld"
+ "DefaultResolverInteractionsViewGenerator Inserting candidate interaction: %s"
+ "DefaultResolverInteractionsViewGenerator Inserting tuple interaction: %s"
+ "DefaultResolverInteractionsViewGenerator: %s has been pruned, new first timestamp is %f"
+ "DefaultResolverInteractionsViewGenerator: %s: timestamps: %f , %f"
+ "DefaultResolverInteractionsViewGenerator: Update the Event table"
+ "DefaultResolverInteractionsViewGenerator: Update the internal event tables with RowId: %lld"
+ "DefaultResolverInteractionsViewGenerator: checking for any stream pruning"
+ "DefaultResolverInteractionsViewGenerator: deleteAllEvents: from %ld%s"
+ "DefaultResolverInteractionsViewGenerator: deleteEvents: from %ld harvested at %ld different times"
+ "DefaultResolverInteractionsViewGenerator: event.absoluteTimestamp is nil"
+ "DefaultResolverInteractionsViewGenerator: failed to update from %s. Error: %@"
+ "DefaultResolverInteractionsViewGenerator: finished update from %s"
+ "DefaultResolverInteractionsViewGenerator: performUpdate: clear required"
+ "DefaultResolverInteractionsViewGenerator: performUpdate: control source full rebuild"
+ "DefaultResolverInteractionsViewGenerator: performUpdate: feature flag is disabled."
+ "DefaultResolverInteractionsViewGenerator: performUpdate: incremental update"
+ "DefaultResolverInteractionsViewGenerator: performUpdate: priority at end current = %s."
+ "DefaultResolverInteractionsViewGenerator: performUpdate: priority at start current = %s."
+ "DefaultResolverInteractionsViewGenerator: performUpdate: truncation required"
+ "DefaultResolverInteractionsViewGenerator: performUpdate: weekly schedule full rebuild"
+ "DefaultResolverInteractionsViewGenerator: processStream %s: controlSourceFullRebuild"
+ "DefaultResolverInteractionsViewGenerator: processStream %s: ignore bookmark: %{bool}d"
+ "DefaultResolverInteractionsViewGenerator: processStream %s: processing tombstones"
+ "DefaultResolverInteractionsViewGenerator: processStream %s: processing tombstones failed: %@, deleting all interactions"
+ "DefaultResolverInteractionsViewGenerator: receiveInput error: processing: %s: %s"
+ "DefaultResolverInteractionsViewGenerator: receiveInput error: unknown event body in %s: %s"
+ "DefaultResolverInteractionsViewGenerator: received IE InteractionStore input"
+ "DefaultResolverInteractionsViewGenerator: received IE InteractionStore input with eventId: %lld"
+ "DefaultResolverInteractionsViewGenerator: received input from stream %s"
+ "Empty RowId for the events table"
+ "EntityMappingStore: No store provider registered for entity type: %s"
+ "Expected siriRemembers view source"
+ "Failed to map entity identifier: "
+ "HierarchicalClustering.PopulateCollections"
+ "HierarchicalClustering: Entity count %ld exceeds maximum %ld. Skipping clustering."
+ "HierarchicalClustering: No entities to cluster"
+ "HierarchicalClustering: Processing large entity count: %ld"
+ "INSERT INTO events (originId, trigger, occurredAt, source, biomeEventTimestamp, isLocal, devicePlatform, remoteDeviceId) VALUES (?,?,?,?,?,?,?,?)"
+ "INSERT INTO interactions (id, domain, type, bundleId, isDonatedBySiri, donorStream, direction, handlingStatus, startDate, durationSeconds, fields, contentHash, biomeEventTimestamp, isLocal, devicePlatform, remoteDeviceId, userDonatorType, sourceStreams) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
+ "INSERT OR IGNORE INTO "
+ "INSERT OR IGNORE INTO tupleCandidates (tupleId, candidateId) VALUES (?,?)"
+ "INSERT OR IGNORE INTO tuples (candidateIds) VALUES (?)"
+ "INSERT OR REPLACE INTO candidateInteractions (eventId, candidateId, userAlignment, parameterName, searchLikelihood) VALUES (?,?,?,?,?)"
+ "INSERT OR REPLACE INTO candidates (uuid, bundleId, type) VALUES (?,?,?)"
+ "INSERT OR REPLACE INTO entityIdMapping (hashedIdentifier, localIdentifier, updatedTimestamp) VALUES (?, ?, ?)"
+ "INSERT OR REPLACE INTO tupleInteractions (eventId, tupleId, userAlignment, tupleData, occurredAt) VALUES (?,?,?,?,?)"
+ "INStartAudioCallIntent"
+ "INStartCallIntent"
+ "INStartVideoCallIntent"
+ "IntelligenceEngine.Interaction.Donation"
+ "Invalid bookmark type"
+ "Invalid identifier in the biome events"
+ "Invalid sessionId and statementIndex for biome events"
+ "KNDocumentEntity"
+ "LiveStationSiriEntity"
+ "LiveTVChannelEntity"
+ "LocationSearchEntity"
+ "MediaControlsDevice"
+ "NewsProviderEntity"
+ "No external identifier or valid hash info provided"
+ "No identifying information available in hash info"
+ "No store provider registered for entity type: "
+ "PlaylistSiriEntity"
+ "PodcastCollectionEntity"
+ "RCRecordingEntity"
+ "RadioShowEpisodeSiriEntity"
+ "RadioShowSiriEntity"
+ "SELECT * FROM candidates WHERE (uuid = ?) AND (bundleId = ?)"
+ "SELECT * FROM events WHERE (originId = ?)"
+ "SELECT * FROM tuples WHERE (candidateIds = ?)"
+ "SELECT localIdentifier, updatedTimestamp FROM entityIdMapping WHERE hashedIdentifier = ?"
+ "SendMessageIntent"
+ "ShazamSongEntity"
+ "SiriRemembersViewGenerator: No entity mapping available, returning nil for entity identifier: %s"
+ "SiriRemembersViewGenerator: No hash info available for remote entity mapping, originalIdentifier: %s"
+ "SiriRemembersViewGenerator: mapped originalIdentifier: %s to localIdentifier: %s with hashInfo: %s"
+ "SiriRemembersViewGenerator: persistentEntityIdentifier feature flag is false, skipping entity store provider registration"
+ "SiriRemembersViewGenerator: persistentEntityIdentifier feature flag is true, attempting to map remote entity: %s"
+ "SiriRemembersViewGenerator: persistentEntityIdentifier feature flag is true, registering default entity store providers"
+ "Skipping candidate interaction: %{private}s of type %s"
+ "SongCollectionSiriEntity"
+ "SportsEventEntity"
+ "SportsTeamAppEntity"
+ "Spotlight"
+ "StartFaceTimeCallIntent"
+ "StartTelephonyCallIntent"
+ "TB,R,N,G_isCoordinateDerived"
+ "TPDocumentEntity"
+ "The occurredAt is unknown for IntelligenceEngine events"
+ "UPDATE events SET source = source & ~"
+ "UPDATE events SET source = source & ~?"
+ "UPDATE events SET source = source & ~? WHERE biomeEventTimestamp < ?"
+ "UPDATE events SET source = source & ~? WHERE biomeEventTimestamp < ? AND remoteDeviceId = ?"
+ "UPDATE events SET source = source & ~? WHERE biomeEventTimestamp IN (SELECT timestamp FROM "
+ "UPDATE events SET source = source & ~? WHERE remoteDeviceId = ?"
+ "ViewUpdate.BiomeSource: DefaultResolverInteractionsSourceStream: unexpected stream: %s"
+ "WarmupMusicQueueResultSiriEntity"
+ "_TtC24IntelligencePlatformCore18EntityMappingStore"
+ "_TtC24IntelligencePlatformCore20ContactStoreProvider"
+ "_isCoordinateDerived"
+ "andPredicateWithSubpredicates:"
+ "appIntentInvocationUUID"
+ "cachedStatements"
+ "candidateId"
+ "candidateIds"
+ "compressionRatio"
+ "countryCode"
+ "defaultResolverInteractionsView"
+ "digits"
+ "entityHashInfo"
+ "entityMappingGetStatement"
+ "entityMappingUpdateStatement"
+ "event.absoluteTimestamp is nil"
+ "externalIdentifier"
+ "familyName ==[cd] %@"
+ "file"
+ "givenName ==[cd] %@"
+ "hasSearchLikelihood"
+ "hashInfo"
+ "interactionRowid"
+ "isCoordinateDerived"
+ "mutableCopy"
+ "parameterName"
+ "predicateForContactMatchingPhoneNumberWithDigits:countryCode:"
+ "predicateForContactsMatchingEmailAddress:"
+ "predicateForContactsMatchingExternalUUIDs:"
+ "primitive"
+ "sameEmailDomain"
+ "schema"
+ "searchLikelihood"
+ "sessionId"
+ "sirikitIntentItemId"
+ "statementIndex"
+ "storeProviders"
+ "tmp_deleteAllInteractions_"
+ "tool"
+ "transcriptStatementId"
+ "trigger"
+ "tupleCandidatesInsertStatement"
+ "tupleInsertStatement"
+ "tupleInteraction"
+ "tupleSelectStatement"
+ "typeName"
+ "userAlignment"
- "/Library/Caches/com.apple.xbs/Sources/GRDB/GRDB/Core/Row.swift"
- "Could not create a BMLocationHashedCoordinates event from the provided event - %s"
- "DefaultResolverInteractionsViewGenerator: performUpdate: it is unsupported."
- "INSERT INTO interactions (id, domain, type, bundleId, isDonatedBySiri, donorStream, direction, handlingStatus, startDate, durationSeconds, fields, contentHash, biomeEventTimestamp, isLocal, devicePlatform, userDonatorType, sourceStreams) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
- "INSERT OR REPLACE INTO processedInteractions (id, date) VALUES (?,?)"
- "ViewBiomeDeleteDebounce"
- "_TtCOO24IntelligencePlatformCore12OneShotTasks9ViewTasksP33_AD948141065DF512D4334E10387519D433ViewBiomeDeleteDebounceTaskRunner"
- "biomeDeleteDebounce"
- "processedInteractionsInsertStatement"
- "viewBiomeDeleteDebounce"

```
