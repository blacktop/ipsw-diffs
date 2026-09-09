## assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__data`

```diff

-912.0.234.0.0
-  __TEXT.__text: 0x18ecc
-  __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_stubs: 0x4ca0
-  __TEXT.__objc_methlist: 0xe74
+912.0.235.0.0
+  __TEXT.__text: 0x1b3c8
+  __TEXT.__auth_stubs: 0xbc0
+  __TEXT.__objc_stubs: 0x5380
+  __TEXT.__objc_methlist: 0xfe4
   __TEXT.__dlopen_cstrs: 0x11b
-  __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x624
-  __TEXT.__objc_classname: 0x70b
-  __TEXT.__objc_methname: 0x5851
-  __TEXT.__objc_methtype: 0x98d
-  __TEXT.__oslogstring: 0x4264
-  __TEXT.__cstring: 0x1776
-  __TEXT.__unwind_info: 0x568
-  __DATA_CONST.__const: 0xf38
-  __DATA_CONST.__cfstring: 0xb80
-  __DATA_CONST.__objc_classlist: 0x168
+  __TEXT.__const: 0x140
+  __TEXT.__gcc_except_tab: 0x780
+  __TEXT.__objc_classname: 0x74e
+  __TEXT.__objc_methname: 0x5fc3
+  __TEXT.__objc_methtype: 0xa06
+  __TEXT.__oslogstring: 0x46bb
+  __TEXT.__cstring: 0x1a89
+  __TEXT.__unwind_info: 0x5e8
+  __DATA_CONST.__const: 0xfd8
+  __DATA_CONST.__cfstring: 0xde0
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_intobj: 0xa8
-  __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__auth_got: 0x5b8
-  __DATA_CONST.__got: 0x720
-  __DATA.__objc_const: 0x2dc8
-  __DATA.__objc_selrefs: 0x1508
-  __DATA.__objc_ivar: 0x7c
-  __DATA.__objc_data: 0xe10
+  __DATA_CONST.__objc_intobj: 0xd8
+  __DATA_CONST.__objc_arraydata: 0x50
+  __DATA_CONST.__objc_arrayobj: 0x60
+  __DATA_CONST.__auth_got: 0x5f0
+  __DATA_CONST.__got: 0x790
+  __DATA.__objc_const: 0x3120
+  __DATA.__objc_selrefs: 0x16c0
+  __DATA.__objc_ivar: 0xa8
+  __DATA.__objc_data: 0xeb0
   __DATA.__data: 0x360
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 366
-  Symbols:   421
-  CStrings:  1283
+  Functions: 402
+  Symbols:   442
+  CStrings:  1398
 
Symbols:
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_NSManagedObjectID
+ _OBJC_CLASS_$_NSSortDescriptor
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_PAImageConversionServiceClient
+ _OBJC_CLASS_$_PAMediaConversionServiceResourceURLCollection
+ _OBJC_CLASS_$_PLDiagnostics
+ _OBJC_CLASS_$_PLResourceLocalAvailabilityRequestOptions
+ _PAMediaConversionIsProvenanceProcessingTimeoutError
+ _PAMediaConversionResourceRoleProvenanceUnprocessed
+ _PAMediaConversionServiceErrorDomain
+ _PAMediaConversionServiceJobIdentifierKey
+ _PAMediaConversionServiceOptionIsContentProvenanceDryRunKey
+ _PAMediaConversionServiceOptionRequestReasonKey
+ _PAMediaConversionServiceProvenanceDiagnosticsRequestedKey
+ _PLCoreAnalyticsProvenanceSummaryEvent
+ _dispatch_block_cancel
+ _objc_opt_new
+ _objc_setProperty_nonatomic_copy
+ _objc_sync_enter
+ _objc_sync_exit
CStrings:
+ "%K >= %@"
+ "@\"NSManagedObjectID\""
+ "@\"NSProgress\""
+ "@\"NSURL\""
+ "B40@0:8@16@24d32"
+ "B44@0:8@16@24@32B40"
+ "PLProvenanceMaintenanceAsset"
+ "PLProvenanceProcessingMaintenanceTask"
+ "PLProvenanceProcessingMaintenanceTask-%@"
+ "Provenance Maintenance: Asset %{public}@ cancelled; not advancing resume marker"
+ "Provenance Maintenance: Asset fetch failed: %@"
+ "Provenance Maintenance: Cancel requested"
+ "Provenance Maintenance: Download wait timed out for asset %{public}@"
+ "Provenance Maintenance: Downloading resource for asset %{public}@ (dedicatedProvenance=%@)"
+ "Provenance Maintenance: Failed to download resource for asset %{public}@: %@"
+ "Provenance Maintenance: Failed to write TTR resume marker: %@"
+ "Provenance Maintenance: Failed to write last-processed resume marker: %@"
+ "Provenance Maintenance: Library shutting down; stopping loop"
+ "Provenance Maintenance: No assets to process"
+ "Provenance Maintenance: Starting loop with %tu assets"
+ "Provenance Maintenance: Submitting asset %{public}@ (suppressTTR=%@, dedicatedProvenance=%@)"
+ "Provenance Maintenance: TTR filed for asset %{public}@ (outcome=%@); halting maintenance loop"
+ "Provenance Maintenance: Task cancelled; stopping loop"
+ "Provenance Maintenance: Timed out after %.0fs waiting for in-flight work; cancelling"
+ "Provenance Maintenance: Wall-time budget (%.0fs) exceeded; cancelling in-flight work"
+ "Provenance maintenance: CIP server returned diagnosticsRequested=YES for requestID=%@ (assetUUID=%@)."
+ "Provenance maintenance: requestID=%@ timed out after 6 minutes (assetUUID=%@)."
+ "ProvenanceMaintenance.ResumeMarkerForLastAssetWithCompletedServerDiagnosticsTTR"
+ "ProvenanceMaintenance.ResumeMarkerForLastProcessedAsset"
+ "Q60@0:8@16@24@32@40@48B56"
+ "T@\"NSManagedObjectID\",&,N,V_objectID"
+ "T@\"NSManagedObjectID\",&,N,V_resourceObjectID"
+ "T@\"NSString\",C,N,V_uuid"
+ "T@\"NSURL\",&,N,V_url"
+ "TB,N,V_hasDedicatedProvenanceResource"
+ "TB,N,V_suppressTTR"
+ "URIRepresentation"
+ "URLWithString:"
+ "UUID"
+ "UUIDString"
+ "[Provenance] PCC request exceeded 6 minute timeout"
+ "[Provenance] server requested diagnostics"
+ "_advanceResumeMarkersForAssetObjectID:serverDiagnosticsTTRFired:"
+ "_appPrivateData"
+ "_budgetWatchdog"
+ "_buildSourceCollectionForAsset:resourceURL:"
+ "_downloadResourceForAsset:"
+ "_fetchAssets"
+ "_fetchAssetsUsingAppPrivateData:managedObjectContext:"
+ "_fileTTRIfNeededForAsset:jobIdentifier:resourceURL:result:error:suppressTTR:"
+ "_flushPendingResumeMarkers"
+ "_hasDedicatedProvenanceResource"
+ "_inFlightProgress"
+ "_installBudgetWatchdog"
+ "_objectID"
+ "_pendingResumeMarkerForLastAssetWithCompletedServerDiagnosticsTTR"
+ "_pendingResumeMarkerForLastProcessedAsset"
+ "_processAsset:withClient:"
+ "_publishInFlightProgress:andWait:timeoutSeconds:"
+ "_removeBudgetWatchdog"
+ "_resourceObjectID"
+ "_runConversionForAsset:client:resourceURL:suppressTTR:"
+ "_stopped"
+ "_suppressTTR"
+ "_url"
+ "_uuid"
+ "absoluteString"
+ "arrayWithCapacity:"
+ "collectionWithMainResourceURL:"
+ "compare:"
+ "dateCreated"
+ "diagnosticsRequested"
+ "existingObjectWithID:error:"
+ "fileURL"
+ "fileURLWithPath:"
+ "hasDedicatedProvenanceResource"
+ "heic"
+ "isCancelled"
+ "isLocallyAvailable"
+ "libraryStatsCoreAnalyticsProvenanceKey"
+ "makeResourceLocallyAvailableWithOptions:completion:"
+ "managedObjectIDForURIRepresentation:"
+ "pathExtension"
+ "persistedOriginalImageResource"
+ "persistedProvenanceResource"
+ "powderState"
+ "predicateWithValue:"
+ "processContentProvenanceForSourceURLCollection:destinationURL:options:completionHandler:"
+ "provenance processing timed out"
+ "provenance-maintenance-%@.%@"
+ "resourceObjectID"
+ "self > %@"
+ "serverDiagnostics"
+ "setFetchLimit:"
+ "setHasDedicatedProvenanceResource:"
+ "setNetworkAccessAllowed:"
+ "setObjectID:"
+ "setResourceObjectID:"
+ "setResourceURL:forRole:"
+ "setSortDescriptors:"
+ "setSuppressTTR:"
+ "setTaskIdentifier:"
+ "setUrl:"
+ "setUuid:"
+ "setValue:forKey:error:"
+ "sortDescriptorWithKey:ascending:"
+ "stringByAppendingPathComponent:"
+ "suppressTTR"
+ "tapToRadarWithTitle:description:radarComponent:isUserInitiated:displayReason:attachments:"
+ "the provenance server requested diagnostics"
+ "timeout"
+ "url"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
+ "v24@?0@\"PAMediaConversionServiceContentProvenanceProcessingResult\"8@\"NSError\"16"
+ "v28@0:8@16B24"
```
