## biomesyncd

> `/usr/libexec/biomesyncd`

```diff

-153.5.0.2.0
-  __TEXT.__text: 0x43b08
+153.6.0.1.0
+  __TEXT.__text: 0x448c8
   __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_stubs: 0x76e0
-  __TEXT.__objc_methlist: 0x34f4
+  __TEXT.__objc_stubs: 0x7780
+  __TEXT.__objc_methlist: 0x354c
   __TEXT.__const: 0x10c8
-  __TEXT.__gcc_except_tab: 0x918
-  __TEXT.__objc_methname: 0x93e0
-  __TEXT.__cstring: 0x49cd
-  __TEXT.__objc_classname: 0x820
-  __TEXT.__objc_methtype: 0x1882
-  __TEXT.__oslogstring: 0x50f1
+  __TEXT.__gcc_except_tab: 0x988
+  __TEXT.__objc_methname: 0x954f
+  __TEXT.__cstring: 0x4a20
+  __TEXT.__objc_classname: 0x844
+  __TEXT.__objc_methtype: 0x18e7
+  __TEXT.__oslogstring: 0x520a
   __TEXT.__unwind_info: 0xed8
   __DATA_CONST.__auth_got: 0x698
-  __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0xf98
-  __DATA_CONST.__cfstring: 0x4080
+  __DATA_CONST.__got: 0x398
+  __DATA_CONST.__const: 0xff0
+  __DATA_CONST.__cfstring: 0x4100
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1a0
-  __DATA_CONST.__objc_arraydata: 0x4a0
-  __DATA_CONST.__objc_arrayobj: 0x708
-  __DATA_CONST.__objc_intobj: 0x228
+  __DATA_CONST.__objc_arraydata: 0x4e8
+  __DATA_CONST.__objc_arrayobj: 0x780
+  __DATA_CONST.__objc_intobj: 0x258
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x7c40
-  __DATA.__objc_selrefs: 0x2458
-  __DATA.__objc_ivar: 0x3c8
+  __DATA.__objc_const: 0x8000
+  __DATA.__objc_selrefs: 0x2490
+  __DATA.__objc_ivar: 0x3d0
   __DATA.__objc_data: 0x1130
-  __DATA.__data: 0x840
-  __DATA.__bss: 0xe8
+  __DATA.__data: 0x8a0
+  __DATA.__bss: 0xf0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1479
-  Symbols:   338
-  CStrings:  2875
+  Functions: 1493
+  Symbols:   342
+  CStrings:  2899
 
Symbols:
+ _OBJC_CLASS_$_NSMutableIndexSet
+ _BMUseCaseWriter
+ _OBJC_CLASS_$_BMAccessConnectionFactory
+ _BMUseCasePruner
CStrings:
+ "B40@0:8Q16Q24@32"
+ "activeLocationsInClockVector:inStream:enumerateWithBlock:"
+ "@\"BMRapportRequest\""
+ "rangeClockVectorForStreamsSupportingTransportType:direction:device:"
+ "chunker hit defined limit, returning and setting moreComing bit"
+ " AND NOT EXISTS (SELECT 1 FROM CKAtom WHERE stream = ? "
+ "atomBatchesForChangesSinceClockVector:targetPlatform:transportType:direction:ckFormatVersion:chunker:"
+ "BMAccessConnectionFactoryDelegate"
+ "countAtomMergeResultRecords"
+ "@\"BMMultiStreamTimestampClockVector\""
+ "T@\"BMMultiStreamTimestampClockVector\",&,N,V_rangeClockVectors"
+ "minusVector:"
+ "shouldCacheConnectionToMachService:domain:useCase:"
+ "exceeded max number of distinct range clauses in clock vector query, not processing additional timestamps"
+ "atomBatchesForChangesSinceClockVector:ckFormatVersion:chunker:transportType:"
+ "\x12"
+ "generating atom batch with timestamps to fill for clock: %!@(MISSING), version: %!l(MISSING)u, stream: %!@(MISSING)"
+ "DELETE FROM SyncSessionLog WHERE session_id NOT IN (SELECT session_id from SyncSessionLog ORDER BY start_timestamp DESC LIMIT 100)"
+ "addIndex:"
+ "rangeClockVectorForStreamName:"
+ "legacyTimestampClockVectorForStreamName:"
+ "_atomMergeResultsRecorded"
+ "Sync already in progress"
+ " AND location_id = id)"
+ "_currentRequest"
+ "currentRangeClockVector %!@(MISSING) minusVector clockVector %!@(MISSING)"
+ "exceeded limit for recording atom merge results"
+ "B40@0:8Q16Q24@\"NSString\"32"
+ "atomBatchesForChangesSinceClockVector platform: %!@(MISSING), version: %!@(MISSING), clock: %!@(MISSING)"
+ " AND location.state = ?"
+ "atomsForChangesSinceClockVector:ckFormatVersion:chunker:transportType:enumerateWithBlock:"
+ "rangeClockVector"
+ "_rangeClockVectors"
+ "CKAtomRowSiteIdentifiersForStreamIdentifier:"
+ "failed to unarchive BMMultiStreamTimestampClockVector with error %!@(MISSING)"
+ "rangeClockVectors"
+ "setRangeClockVectors:"
- "timestampClockVectorForStreamName:"
- "atomBatchesInClockVector:targetPlatform:transportType:direction:ckFormatVersion:chunker:"
- "timestampCountForSiteIdentifier:"
- "removeObjectForKey:"
- "atomsInClockVector: %!@(MISSING), stream: %!@(MISSING)"
- " AND NOT EXISTS (SELECT * FROM CKAtom WHERE location_id = id)"
- "Generating atom batch after clock: %!@(MISSING), version: %!l(MISSING)u"
- "locationsInClockVector:inStream:enumerateWithBlock:"
- "isBlockedOnCausalityViolationForSiteIdentifier:inStream:"
- "atomsInClockVector:ckFormatVersion:chunker:transportType:enumerateWithBlock:"
- "Expected only one value in indexSet of timestampClockVector, found %!l(MISSING)u"
- "DELETE FROM SyncSessionLog WHERE session_id NOT IN (SELECT session_id from SyncSessionLog ORDER BY start_timestamp DESC LIMIT 1000)"
- "atomBatchesInClockVector:ckFormatVersion:chunker:transportType:"
- "atomBatchesInClockVector platform: %!@(MISSING), version: %!@(MISSING), clock: %!@(MISSING)"

```
