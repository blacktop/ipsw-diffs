## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary`

```diff

-742.0.141.0.0
-  __TEXT.__text: 0x187bb8
-  __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x11a68
-  __TEXT.__const: 0x2e0
-  __TEXT.__gcc_except_tab: 0x408c
-  __TEXT.__oslogstring: 0x13dae
-  __TEXT.__cstring: 0x131f3
-  __TEXT.__unwind_info: 0x58e8
-  __TEXT.__objc_classname: 0x1d72
-  __TEXT.__objc_methname: 0x29806
-  __TEXT.__objc_methtype: 0x44ee
-  __TEXT.__objc_stubs: 0x19360
-  __DATA_CONST.__got: 0xa18
-  __DATA_CONST.__const: 0x5cb8
+750.5.104.0.0
+  __TEXT.__text: 0x188ee0
+  __TEXT.__auth_stubs: 0xef0
+  __TEXT.__objc_methlist: 0x12a34
+  __TEXT.__const: 0x2e8
+  __TEXT.__gcc_except_tab: 0x4178
+  __TEXT.__oslogstring: 0x13eff
+  __TEXT.__cstring: 0x1338d
+  __TEXT.__unwind_info: 0x5908
+  __TEXT.__objc_classname: 0x1d77
+  __TEXT.__objc_methname: 0x29b92
+  __TEXT.__objc_methtype: 0x4506
+  __TEXT.__objc_stubs: 0x19620
+  __DATA_CONST.__got: 0xa28
+  __DATA_CONST.__const: 0x5dd0
   __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8188
+  __DATA_CONST.__objc_selrefs: 0x82d0
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x7e8
-  __DATA_CONST.__objc_arraydata: 0x12b0
-  __AUTH_CONST.__auth_got: 0x790
-  __AUTH_CONST.__const: 0x2500
-  __AUTH_CONST.__cfstring: 0x14480
-  __AUTH_CONST.__objc_const: 0x1ed90
+  __DATA_CONST.__objc_superrefs: 0x7f0
+  __DATA_CONST.__objc_arraydata: 0x12c0
+  __AUTH_CONST.__auth_got: 0x788
+  __AUTH_CONST.__const: 0x2560
+  __AUTH_CONST.__cfstring: 0x147a0
+  __AUTH_CONST.__objc_const: 0x1d410
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x1704
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x1724
   __DATA.__data: 0xf30
-  __DATA.__bss: 0x970
+  __DATA.__bss: 0x878
   __DATA.__common: 0x21
-  __DATA_DIRTY.__objc_data: 0x51e0
+  __DATA_DIRTY.__objc_data: 0x5230
   __DATA_DIRTY.__data: 0x9
-  __DATA_DIRTY.__bss: 0x480
+  __DATA_DIRTY.__bss: 0x580
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/MMCS.framework/MMCS
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
+  - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libCTGreenTeaLogger.dylib
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8069
-  Symbols:   9167
-  CStrings:  11778
+  Functions: 8232
+  Symbols:   9384
+  CStrings:  11847
 
Symbols:
+ OBJC_IVAR_$_CPLMemoryAsset._masterIdentifier
+ OBJC_IVAR_$_CPLSuggestionAsset._masterIdentifier
+ _PCSGetAppBoundaryKey
+ __os_feature_enabled_impl
+ _kPCSSetupDSID
+ _kPCSSetupDSIDAny
- OBJC_IVAR_$_CPLMemoryAsset._masterFingerprint
- OBJC_IVAR_$_CPLSuggestionAsset._masterFingerprint
- _MMCSSignatureIsValid
- _MMCSSignatureIsValidV2
- _fmod
CStrings:
+ "\x01A\x11\x12"
+ "\x02\x112"
+ "\b\x14!"
+ "!\x11\x15"
+ "%@ has an invalid fingerprint scheme"
+ "%@ saving CPLStatus %p (changed keys: %{public}@) to %@: %@"
+ "%@()"
+ "%ld (%@ + 0x%lx)"
+ "%ld (%@)"
+ "%s[%@ %@]"
+ "%{public}@ completed in %.3fs"
+ "%{public}@ has not completed after %.0fs"
+ ".icloud.com"
+ "/%@"
+ "/%@/%@"
+ "<%@ %ld/%ld/%ld>"
+ "@\"CPLFingerprintContext\""
+ "@\"CPLFingerprintContext\"16@0:8"
+ "@40@0:8@16:24@32"
+ "@64@0:8@16@24q32Q40@48@56"
+ "Asset for %@ has been stashed - stashing changes"
+ "BeforePushSession"
+ "CPLDisableInvalidFingerprintScheme"
+ "CPLForceEPPSupport"
+ "CPLUseRealBoundaryKey"
+ "Client pushed %@ changing from %@ to %@"
+ "Client pushed a record with mismatched fingerprint scheme resources %@: %@"
+ "CloudPhotoLibrary-750.5.104"
+ "EPPCapable"
+ "Failed to refresh boundary key for %{public}@: %@"
+ "Invalid fingerprint scheme"
+ "Invalid fingerprint scheme for %@ (related identifier '%{public}@')"
+ "Open"
+ "PCSGetAppBoundaryKey"
+ "Photos"
+ "PullSession"
+ "PushSession"
+ "Rejecting %@ as it changes from %@ to %@"
+ "Successfully refreshed boundary key for %{public}@"
+ "T@\"CPLFingerprintContext\",R,N"
+ "T@\"CPLFingerprintContext\",R,N,V_fingerprintContext"
+ "T@\"CPLFingerprintSchemeV1\",R,V_mmcsv1FingerprintScheme"
+ "T@\"CPLFingerprintSchemeV2\",R,V_mmcsv2FingerprintScheme"
+ "T@\"NSData\",C"
+ "T@\"NSDate\",C,N,V_userModificationDate"
+ "T@\"NSString\",&,N,V_masterIdentifier"
+ "Trying to use %@ with an invalid fingerprint scheme"
+ "Unable to find master %@ to stash"
+ "_beginPullChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:"
+ "_beginPushChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:"
+ "_callDescription"
+ "_concreteScopeMapping"
+ "_doesScopeContributeToGlobalStatus:"
+ "_fetchBoundaryKeyIfNecessaryWithSource:completionHandler:"
+ "_fingerprintContext"
+ "_fixGlobalStatus"
+ "_forManagement"
+ "_functionName"
+ "_hasFetchedBoundaryKey"
+ "_isMMCSv2"
+ "_scopeMapping"
+ "_serverFeatureCompatibleVersionToUpdate"
+ "_shouldUpdateGlobalStatusAtEndOfTransaction"
+ "_updateGlobalStatusWithScopeChange:forScope:"
+ "_userModificationDate"
+ "_willNeedToAccessScopeWithIdentifier:error:"
+ "addConcreteScope:forScope:"
+ "addTransportScope:forScope:"
+ "changing asset from %@ to %@"
+ "clientFeatureCompatibleVersion = %@"
+ "com.apple.photos.client-side-encryption-manager"
+ "descriptionForSupportedFeatureCompatibleVersion:"
+ "disableBoundaryKeyFetching"
+ "epp-assets"
+ "fingerprintContextIfKnown"
+ "getBytes:length:"
+ "getCloudCacheRecordsWithLocalScopedIdentifiers:desiredProperties:completionHandler:"
+ "hasMasterIdentifier"
+ "https"
+ "initForMMCSv2:"
+ "initWithBatch:targetMapping:ruleGroups:pushRepositoryPriority:fingerprintContext:provider:"
+ "initWithObject:selector:functionName:"
+ "initWithURL:resolvingAgainstBaseURL:"
+ "isCompatibleWithFingerprintScheme:"
+ "isStableHash:"
+ "isValidFingerprint:"
+ "observeAsyncCallWithFunction:block:"
+ "observeSyncCallWithFunction:block:"
+ "pathComponents"
+ "performUpgradeWithError:"
+ "providesEnhancedPrivacy"
+ "realStableHash"
+ "record %@ is not known to cloud cache"
+ "redacted."
+ "refreshBoundaryKeyWithSource:completionHandler:"
+ "requestClientToPullAllChangesInScopeIdentifiers:completionHandler:"
+ "scheme"
+ "scopeForScopeIdentifier:"
+ "setBoundaryKey:"
+ "setHost:"
+ "setPath:"
+ "setScheme:"
+ "setUserModificationDate:"
+ "setupFingerprintContextForTests"
+ "share.icloud.com"
+ "shared-library"
+ "storeVersionHasChanged"
+ "supportedFeatureCompatibleVersion"
+ "umod"
+ "userModificationDate"
+ "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "willBeginPushSession"
+ "www.icloud.com"
- "\x01A\x13"
- "\b\x13!"
- "!\x11\x14"
- "%@ saving CPLStatus %p (changed keys: %@) to %@: %@"
- "%s[%{public}@ %{public}@] completed in %.3fs"
- "%s[%{public}@ %{public}@] has not completed after %.0fs"
- "<%@ %@ %ld/%ld/%ld>"
- "@32@0:8@16:24"
- "@56@0:8@16@24q32Q40@48"
- "B24@0:8r^v16"
- "CPLForceMMCSv2Support"
- "CloudPhotoLibrary-742.0.141"
- "No error but no transport scope available for %@"
- "T@\"CPLFingerprintSchemeV1\",R,N,V_mmcsv1FingerprintScheme"
- "T@\"CPLFingerprintSchemeV2\",R,N,V_mmcsv2FingerprintScheme"
- "T@\"NSString\",&,N,V_masterFingerprint"
- "Trying to user %@ with an invalid fingerprint scheme"
- "^{os_unfair_lock_s=I}"
- "_doesScopeContributeToAssetCounts:"
- "_isUsingFingerprintSchemeSubclasses"
- "_masterFingerprint"
- "_sharedScopeIdentifierMapping"
- "_shouldUpdateAssetCountsAtEndOfTransaction"
- "_updateAssetCountsWithScopeChange:forScope:"
- "addConcreteScope:forScopeWithIdentifier:"
- "addTransportScope:forScopeWithIdentifier:"
- "clientFeatureCompatibleVersion = %ld"
- "defaultFingerprintSchemeForUnknownRecord"
- "hasMasterFingerprint"
- "https://redacted.icloud.com/photos"
- "initWithBatch:targetMapping:ruleGroups:pushRepositoryPriority:provider:"
- "initWithObject:selector:"
- "isMMCSv1SignatureBytes:"
- "isMMCSv1SignatureBytesKnownNotMMCSv2:"
- "isMMCSv2SignatureBytes:"
- "isValidSignatureBytes:"
- "masterFingerprint"
- "requestClientToPullAllChangesInScopeIdentifier:completionHandler:"
- "setMasterFingerprint:"
- "setSharedScopeIdentifier:forScopeWithIdentifier:"
- "sharedScopeIdentifierForScopeWithIdentifier:"
- "shouldSetSharedScopeIdentifierForScopeWithIdentifier:"
- "stableHashForMasterWithManager:"
- "v32@0:8@\"CPLScopedIdentifier\"16@?<v@?@\"CPLRecordChange\"@\"NSError\">24"

```
