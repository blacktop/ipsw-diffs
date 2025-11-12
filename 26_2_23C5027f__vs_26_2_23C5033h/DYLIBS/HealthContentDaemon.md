## HealthContentDaemon

> `/System/Library/PrivateFrameworks/HealthContentDaemon.framework/HealthContentDaemon`

```diff

-6200.3.4.0.0
-  __TEXT.__text: 0x2d928
+6200.3.8.0.0
+  __TEXT.__text: 0x2d960
   __TEXT.__auth_stubs: 0x9c0
   __TEXT.__objc_methlist: 0x2124
   __TEXT.__const: 0x268

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4A49B357-FA10-3A7E-A4BC-F4F7A2D45024
+  UUID: 1A28B9B8-AECA-346C-B444-CCA0068151A2
   Functions: 1060
   Symbols:   3847
   CStrings:  1951
Symbols:
+ ___66-[HDOntologyUpdateCoordinator performPeriodicActivity:completion:]_block_invoke.353
+ ___block_literal_global.326
+ ___block_literal_global.331
+ ___block_literal_global.332
+ ___block_literal_global.337
+ ___block_literal_global.338
+ ___block_literal_global.343
+ ___block_literal_global.348
+ ___block_literal_global.349
+ ___block_literal_global.353
+ ___block_literal_global.359
+ ___block_literal_global.364
+ ___block_literal_global.375
- ___66-[HDOntologyUpdateCoordinator performPeriodicActivity:completion:]_block_invoke.344
- ___block_literal_global.317
- ___block_literal_global.322
- ___block_literal_global.323
- ___block_literal_global.328
- ___block_literal_global.329
- ___block_literal_global.334
- ___block_literal_global.335
- ___block_literal_global.339
- ___block_literal_global.340
- ___block_literal_global.350
- ___block_literal_global.355
- ___block_literal_global.366
Functions:
~ -[HDOntologyBackingStore _queue_flushDatabaseConnectionsIfNecessary] : 112 -> 108
~ -[HDOntologyBackingStore _updateAvailability] : 92 -> 88
~ -[HDOntologyFeatureCoordinator _observationQueue_isPrimaryProfileReady] : 148 -> 144
~ -[HDOntologyUpdateCoordinator _invalidatePreparedAssertions] : 108 -> 116
~ -[HDOntologyUpdateCoordinator _prepareAssertions] : 112 -> 124
~ -[HDOntologyUpdateCoordinator _callWillTriggerGatedActivityTestHookWithMaximumDelay:] : 116 -> 132
~ -[HDSimpleGraphDatabase _openAndCreateDatabaseIfNeededWithError:] : 208 -> 204
~ -[HDSimpleGraphDatabase _createDatabaseConnectionWithURL:] : 184 -> 200
~ -[HDOntologyConceptManager _resetAttributeIdentifierMap] : 132 -> 144
~ -[HDOntologyFeatureCoordinator _persistedEntryWithIdentifier:entryOut:transaction:error:] : 196 -> 192
~ -[HDOntologyFeatureCoordinator _insertEntry:transaction:error:] : 124 -> 120
~ -[HDOntologyFeatureCoordinator _performOrJournalFeatureCoordinatorRequireOperationForItems:error:] : 196 -> 192
~ -[HDOntologyShardDownloader _downloadFilesForEntries:session:completion:] : 180 -> 200
~ -[HDOntologyShardRegistry _assertionQueue_openFileHandlesWithError:] : 156 -> 152
~ -[HDOntologyMercuryZipTSVPruner _setPruneDateMetadataWithTransaction:error:] : 156 -> 152
~ -[HDOntologyBackingStore _flushConnectionsAndWait] : 80 -> 88
~ -[HDOntologyBackingStore _queue_contentProtectionStateChanged:previousState:] : 84 -> 92
~ -[HDOntologyBackingStore _allowedToOpenDatabaseWithError:] : 236 -> 232
~ -[HDOntologyBackingStore _availabilityLock_handleNewAvailability:] : 160 -> 156

```
