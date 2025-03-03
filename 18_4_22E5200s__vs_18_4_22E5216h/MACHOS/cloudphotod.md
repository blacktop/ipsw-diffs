## cloudphotod

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod`

```diff

-750.5.104.0.0
-  __TEXT.__text: 0x1bc314
-  __TEXT.__auth_stubs: 0x1a20
-  __TEXT.__objc_stubs: 0x1b0e0
-  __TEXT.__objc_methlist: 0xf8ac
-  __TEXT.__cstring: 0x1a9b4
+750.11.101.0.0
+  __TEXT.__text: 0x1be074
+  __TEXT.__auth_stubs: 0x1a30
+  __TEXT.__objc_stubs: 0x1b400
+  __TEXT.__objc_methlist: 0xf9d4
+  __TEXT.__cstring: 0x1abc2
   __TEXT.__objc_classname: 0x27f0
-  __TEXT.__objc_methname: 0x27883
-  __TEXT.__objc_methtype: 0x83a3
+  __TEXT.__objc_methname: 0x27c8f
+  __TEXT.__objc_methtype: 0x83a9
   __TEXT.__const: 0x7950
-  __TEXT.__gcc_except_tab: 0x322c
-  __TEXT.__oslogstring: 0x1037e
+  __TEXT.__gcc_except_tab: 0x32c8
+  __TEXT.__oslogstring: 0x10488
   __TEXT.__swift5_typeref: 0x182f
   __TEXT.__swift5_reflstr: 0x1ef7
   __TEXT.__swift5_assocty: 0x378

   __TEXT.__swift5_types: 0x158
   __TEXT.__swift5_capture: 0x348
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x6bf0
+  __TEXT.__unwind_info: 0x6ca8
   __TEXT.__eh_frame: 0x1668
-  __DATA_CONST.__auth_got: 0xd20
-  __DATA_CONST.__got: 0xc30
+  __DATA_CONST.__auth_got: 0xd28
+  __DATA_CONST.__got: 0xc48
   __DATA_CONST.__auth_ptr: 0x398
-  __DATA_CONST.__const: 0x9fd0
-  __DATA_CONST.__cfstring: 0x11300
+  __DATA_CONST.__const: 0xa108
+  __DATA_CONST.__cfstring: 0x114a0
   __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x180
   __DATA_CONST.__objc_protolist: 0x438

   __DATA_CONST.__objc_floatobj: 0x60
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x1bf98
-  __DATA.__objc_selrefs: 0x8410
-  __DATA.__objc_ivar: 0x1200
+  __DATA.__objc_const: 0x1c048
+  __DATA.__objc_selrefs: 0x84e0
+  __DATA.__objc_ivar: 0x120c
   __DATA.__objc_data: 0x4348
   __DATA.__data: 0x6a08
-  __DATA.__bss: 0xdda0
+  __DATA.__bss: 0xddb0
   __DATA.__common: 0x6f0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9788
-  Symbols:   948
-  CStrings:  11379
+  Functions: 9830
+  Symbols:   952
+  CStrings:  11429
 
Symbols:
+ _CPLFeatureNameEPP
+ _OBJC_CLASS_$_CKCheckSupportedDeviceCapabilitiesOperation
+ _OBJC_CLASS_$_CKDeviceCapabilityCheckOptions
+ ___CPLSupportedFeatureVersion
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "\x01\x14"
+ "  EPP auto-enable: YES"
+ "  EPP enabled: %@ (Walrus: %@)"
+ "<%@ %p for %@>"
+ "<%@ standalone>"
+ "ALTER TABLE %@ ADD COLUMN related INTEGER"
+ "B52@0:8@\"CPLScopedIdentifier\"16B24#28@\"NSString\"36^@44"
+ "B52@0:8@16B24#28@36^@44"
+ "CPLCheckEPPCapabilityAccessTimeInterval"
+ "Checked capabilities on %{public}@ returned: %{public}@"
+ "Container does not support capability check for %{public}@: %@"
+ "DELETE FROM %@ WHERE related = 1"
+ "EPP Capability check has been disabled"
+ "Failed to check account capability"
+ "Failed to check capability"
+ "Failed to check capability for %{public}@ (ignoring): %@"
+ "Failed to check capability for %{public}@: %@"
+ "INSERT OR IGNORE INTO %@ (scopeIndex, localIdentifier, quarantineDate, class, reason, related) VALUES (%ld, %@, %lu, %@, %@, %d)"
+ "Removed %lu related records from quarantine"
+ "_cancelActivityRequest"
+ "_cancelAllOperations"
+ "_checkAccountEPPCapabilityWithCompletionHandler:"
+ "_determineSharedScopeFromFetchedRecords:scopeChange:zoneIdentification:currentUserID:"
+ "_didStart"
+ "_isCapabilityCheckIgnorableError:"
+ "_libraryManager"
+ "_shouldCheckEPPCapability"
+ "addQuarantinedRecordWithScopedIdentifier:related:recordClass:reason:error:"
+ "beginChangeSessionWithSessionToken:completionHandler:"
+ "beginDirectSessionWithKnownLibraryVersion:context:completionHandler:"
+ "checkEPPCapabilityIfNecessaryForCloudKitScope:completionHandler:"
+ "cpl_isEPPRecord"
+ "cpl_markRecordAsEPP"
+ "custom"
+ "endChangeSessionWithSessionToken:"
+ "engine.transport.cloudkit.checkdevicecapabilities"
+ "eppRecord"
+ "getScopeInfoWithCurrentUserID:completionHandler:"
+ "initWithDesiredCapabilitySets:zoneIDs:options:"
+ "initWithExcludeDevicesWithoutCapabilityCheckingSupport:excludeZoneAccessBefore:"
+ "isEPPRecord"
+ "isMMCSv2Fingerprint:"
+ "isSupported"
+ "libraryInfoRecordID"
+ "related"
+ "removeRelatedRecordsFromQuarantineWithError:"
+ "scopeIndex INTEGER NOT NULL,localIdentifier TEXT NOT NULL,quarantineDate TIMESTAMP NOT NULL,class TEXT,related INTEGER,reason TEXT NOT NULL"
+ "setAccountEPPCapability:"
+ "setCheckSupportedDeviceCapabilitiesCompletionBlock:"
+ "setHasUpdatedScope:fromTransportWithError:"
+ "sharedCloudKitScopeFromLibraryInfoRecord:userRecordID:"
+ "shouldCheckEPPCapability"
+ "supportsEPPAutoEnable"
+ "updateAccountEPPCapability:"
+ "v24@?0q8@\"NSError\"16"
+ "v32@?0@\"CKRecordZoneID\"8@\"NSDictionary\"16^B24"
+ "v32@?0@\"NSArray\"8@\"CKDeviceCapabilityCheckResult\"16^B24"
- "\x01\x13"
- "B48@0:8@\"CPLScopedIdentifier\"16#24@\"NSString\"32^@40"
- "B48@0:8@16#24@32^@40"
- "INSERT OR IGNORE INTO %@ (scopeIndex, localIdentifier, quarantineDate, class, reason) VALUES (%ld, %@, %lu, %@, %@)"
- "addQuarantinedRecordWithScopedIdentifier:recordClass:reason:error:"
- "getScopeInfoWithCurrentUserID:"
- "scopeIndex INTEGER NOT NULL,localIdentifier TEXT NOT NULL,quarantineDate TIMESTAMP NOT NULL,class TEXT,reason TEXT NOT NULL"

```
