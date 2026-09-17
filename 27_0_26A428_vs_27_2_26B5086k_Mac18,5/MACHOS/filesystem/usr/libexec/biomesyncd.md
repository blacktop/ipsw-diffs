## biomesyncd

> `/usr/libexec/biomesyncd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__linkguard`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-250.0.0.3.0
-  __TEXT.__text: 0x4eb14
-  __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_stubs: 0x8980
-  __TEXT.__objc_methlist: 0x3c5c
-  __TEXT.__const: 0x1360
-  __TEXT.__gcc_except_tab: 0x8a4
-  __TEXT.__objc_methname: 0xa45c
-  __TEXT.__cstring: 0x5aec
+255.0.2.0.0
+  __TEXT.__text: 0x50bcc
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__objc_stubs: 0x8c40
+  __TEXT.__objc_methlist: 0x3d1c
+  __TEXT.__const: 0x1368
+  __TEXT.__gcc_except_tab: 0x908
+  __TEXT.__objc_methname: 0xa819
+  __TEXT.__cstring: 0x5b96
   __TEXT.__objc_classname: 0x7f2
-  __TEXT.__objc_methtype: 0x1733
-  __TEXT.__oslogstring: 0x661d
-  __TEXT.__unwind_info: 0x1728
-  __DATA_CONST.__const: 0x1320
-  __DATA_CONST.__cfstring: 0x4780
+  __TEXT.__objc_methtype: 0x1760
+  __TEXT.__oslogstring: 0x6cb5
+  __TEXT.__unwind_info: 0x17b8
+  __DATA_CONST.__const: 0x1340
+  __DATA_CONST.__cfstring: 0x47e0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1a0
-  __DATA_CONST.__objc_arraydata: 0x5a0
-  __DATA_CONST.__objc_arrayobj: 0x8a0
+  __DATA_CONST.__objc_arraydata: 0x5c0
+  __DATA_CONST.__objc_arrayobj: 0x8d0
   __DATA_CONST.__objc_intobj: 0x2e8
+  __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__linkguard: 0xf
-  __DATA_CONST.__objc_dictobj: 0x78
-  __DATA_CONST.__auth_got: 0x5d0
+  __DATA_CONST.__auth_got: 0x5d8
   __DATA_CONST.__got: 0x450
   __DATA.__objc_const: 0x7718
-  __DATA.__objc_selrefs: 0x2900
+  __DATA.__objc_selrefs: 0x29b0
   __DATA.__objc_ivar: 0x3ec
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0x840

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1682
-  Symbols:   334
-  CStrings:  3095
+  Functions: 1713
+  Symbols:   335
+  CStrings:  3145
 
Symbols:
+ __os_feature_enabled_impl
CStrings:
+ "%@%@_%@"
+ "-[BMSyncServiceServer cascadeRapportSyncWithReply:]"
+ "B32@0:8d16@24"
+ "Biome"
+ "Dropping malformed deleted location from peer for stream %{public}@"
+ "Failed to clear the local device flag for %@: %@"
+ "HighestPostedEventTimestamp_"
+ "RetiredLocalSiteIdentifiers"
+ "TimeTravelDeviceRotation"
+ "TimeTravelPoolCleanup"
+ "Tombstone segment %@ in stream %@ is already gone; assuming the store's configured version %u for bookmark ordering"
+ "addRetiredLocalSiteIdentifier:"
+ "anySyncStreamHoldsFutureDatedEvents"
+ "anySyncStreamIsFrozenForSiteIdentifier:database:"
+ "arrayByAddingObject:"
+ "cascadeRapportSync called"
+ "clearLocalDeviceFlagForDeviceWithIdentifier:"
+ "configDatastoreVersion"
+ "could not open a transaction to rotate the local device identifier"
+ "d32@0:8@16@24"
+ "failed to retire site %@ in stream %{public}@"
+ "failed to rotate the local device identifier while sync was frozen"
+ "handleHighestDeletedLocationDidFetchRecord: can't build location from stream:%{public}@ site:%{public}@ day:%ld"
+ "handleHighestDeletedLocationDidFetchRecord: no location row for stream:%{public}@ site:%{public}@ day:%ld; not recording it as the highest deleted location"
+ "hasElapsed:sinceDate:"
+ "highestLocationForSiteIdentifier:inStream:"
+ "highestPostedEventTimestampForSiteIdentifier:inStream:"
+ "highestPostedEventTimestampKeyForSiteIdentifier:inStream:"
+ "isTimeTravelStreamResetEnabledForConfig:"
+ "newEnumeratorFromStartTime:endTime:maxEvents:options:"
+ "newEnumeratorStartingAfterBookmark:reader:notBefore:"
+ "newestEventTimestampForStreamConfiguration:"
+ "not rotating the local device identifier: stream %{public}@ still holds future dated events"
+ "not rotating the local device identifier: there is no identified local device to retire"
+ "populateAtomBatch could not open a reader for bookmark %@, adding a placeholder append: %@"
+ "refusing to record an unusable retired local site identifier %@"
+ "resetImmediateSyncBudget"
+ "retireLocationsForRetiredLocalSiteIdentifiersInManagers:database:"
+ "retireSiteIdentifier:"
+ "retiredLocalSiteIdentifiers"
+ "retiring site %@ in stream %{public}@ up to and including %@; peers will prune everything that site contributed"
+ "rolling back a failed local device identifier rotation"
+ "rotateLocalDeviceIdentifier"
+ "rotateLocalDeviceIdentifierIfFrozenAndEveryStreamRecovered:database:"
+ "rotated the local device identifier because sync was frozen and every sync stream is free of future dated events"
+ "seedHighestPostedEventTimestampIfLastPostedEventIsGone:reader:"
+ "setHighestPostedEventTimestamp:forSiteIdentifier:inStream:"
+ "stream %{public}@ has posted atoms whose events are gone from disk; seeding the highest posted timestamp to %f so no earlier event is posted to peers"
+ "stream %{public}@ retracted %lu atoms in %@ whose events are no longer on disk; peers will prune their copies"
+ "stream %{public}@ withheld %lu events at or below the highest already posted timestamp %f; sync for this stream stays frozen until the clock passes it"
+ "syncAllPersonasNowWithReason:activity:completionHandler:"
+ "v40@0:8d16@24@32"
- "activity \"%s\" not supported on this platform"
- "newEnumeratorFromBookmark:options:"
```
