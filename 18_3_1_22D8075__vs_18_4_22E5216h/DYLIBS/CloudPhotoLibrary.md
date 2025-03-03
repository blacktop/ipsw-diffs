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
+750.11.101.0.0
+  __TEXT.__text: 0x18b1ec
+  __TEXT.__auth_stubs: 0xef0
+  __TEXT.__objc_methlist: 0x12b74
+  __TEXT.__const: 0x2e8
+  __TEXT.__gcc_except_tab: 0x41dc
+  __TEXT.__oslogstring: 0x14141
+  __TEXT.__cstring: 0x1353e
+  __TEXT.__unwind_info: 0x59a0
+  __TEXT.__objc_classname: 0x1d77
+  __TEXT.__objc_methname: 0x29f06
+  __TEXT.__objc_methtype: 0x451e
+  __TEXT.__objc_stubs: 0x198c0
+  __DATA_CONST.__got: 0xa28
+  __DATA_CONST.__const: 0x5df8
   __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8188
+  __DATA_CONST.__objc_selrefs: 0x8380
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x7e8
-  __DATA_CONST.__objc_arraydata: 0x12b0
-  __AUTH_CONST.__auth_got: 0x790
-  __AUTH_CONST.__const: 0x2500
-  __AUTH_CONST.__cfstring: 0x14480
-  __AUTH_CONST.__objc_const: 0x1ed90
+  __DATA_CONST.__objc_superrefs: 0x7f0
+  __DATA_CONST.__objc_arraydata: 0x12d0
+  __AUTH_CONST.__auth_got: 0x788
+  __AUTH_CONST.__const: 0x25a0
+  __AUTH_CONST.__cfstring: 0x14a00
+  __AUTH_CONST.__objc_const: 0x1d528
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x1704
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x1734
   __DATA.__data: 0xf30
-  __DATA.__bss: 0x970
+  __DATA.__bss: 0x890
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
+  Functions: 8272
+  Symbols:   9425
+  CStrings:  11906
 
Symbols:
+ OBJC_IVAR_$_CPLMemoryAsset._masterIdentifier
+ OBJC_IVAR_$_CPLSuggestionAsset._masterIdentifier
+ _CPLAppBundleIdentifierForContainerIdentifier
+ _CPLFeatureNameEPP
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
+ "\f\x11\x15\x17("
+ "\x13\"1#"
+ "!\x11\x15"
+ "%@ has an invalid fingerprint scheme"
+ "%@ is trying to begin a session twice"
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
+ "Account capability is %{public}@ (%{public}@) - switching EPP enabled to %@"
+ "Asset for %@ has been stashed - stashing changes"
+ "B52@0:8@16B24#28@36^@44"
+ "BeforePushSession"
+ "Beginning change session for %@"
+ "Blocking change session for %@ until %@ is done"
+ "CPLAlwaysAutoEnableEPP"
+ "CPLDisableEPPCapabilityCheck"
+ "CPLDisableInvalidFingerprintScheme"
+ "CPLEPPEnabled"
+ "CPLEPPEnabledSource"
+ "CPLForceEPPSupport"
+ "CPLUseRealBoundaryKey"
+ "Change session for %@ has been ended before it even began"
+ "Client pushed %@ changing from %@ to %@"
+ "Client pushed a record with mismatched fingerprint scheme resources %@: %@"
+ "CloudPhotoLibrary-750.11.101"
+ "Derivative generation error is transient, will retry: %@"
+ "EPP"
+ "EPPAutoEnable"
+ "EPPCapable"
+ "Ending change session for %@"
+ "Ending unknown change session for %@"
+ "Error trying to generate derivatives for unsupported input video from %@: %@"
+ "Failed to refresh boundary key for %{public}@: %@"
+ "Invalid fingerprint scheme"
+ "Invalid fingerprint scheme for %@ (related identifier '%{public}@')"
+ "Open"
+ "PCSGetAppBoundaryKey"
+ "Photos"
+ "PullSession"
+ "PushSession"
+ "Refreshing boundary key for %{public}@"
+ "Rejecting %@ as it changes from %@ to %@"
+ "Requesting update of %@ for Account EPP capability"
+ "Resuming change session for %@"
+ "Successfully refreshed boundary key for %{public}@"
+ "T@\"CPLFingerprintContext\",R,N"
+ "T@\"CPLFingerprintContext\",R,N,V_fingerprintContext"
+ "T@\"CPLFingerprintSchemeV1\",R,V_mmcsv1FingerprintScheme"
+ "T@\"CPLFingerprintSchemeV2\",R,V_mmcsv2FingerprintScheme"
+ "T@\"NSData\",C"
+ "T@\"NSDate\",C,N,V_userModificationDate"
+ "T@\"NSString\",&,N,V_masterIdentifier"
+ "TB,R,N,V_shouldCheckEPPCapability"
+ "TB,R,V_usesMMCSv2AsDefault"
+ "Trying to refresh fingerprint context while the library is not open"
+ "Trying to use %@ with an invalid fingerprint scheme"
+ "Unable to find master %@ to stash"
+ "_addQuarantinedRecordWithScopedIdentifier:related:recordClass:reason:error:"
+ "_beginPullChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:"
+ "_beginPushChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:"
+ "_callDescription"
+ "_concreteScopeMapping"
+ "_currentChangeSessionToken"
+ "_doesScopeContributeToGlobalStatus:"
+ "_fetchBoundaryKeyIfNecessaryWithSource:completionHandler:"
+ "_fetchBoundaryKeyIfNecessaryWithSourceLocked:completionHandler:"
+ "_fingerprintContext"
+ "_fixGlobalStatus"
+ "_forManagement"
+ "_functionName"
+ "_hasFetchedBoundaryKey"
+ "_isMMCSv2"
+ "_pendingChangeSessionCompletionHandler"
+ "_pendingChangeSessionToken"
+ "_requestUpdateOfMainScopeFromTransport"
+ "_scopeMapping"
+ "_serverFeatureCompatibleVersionToUpdate"
+ "_shouldCheckEPPCapability"
+ "_shouldUpdateGlobalStatusAtEndOfTransaction"
+ "_updateFingerprintContext"
+ "_updateGlobalStatusWithScopeChange:forScope:"
+ "_userModificationDate"
+ "_willNeedToAccessScopeWithIdentifier:error:"
+ "accountEPPCapability"
+ "accountEPPCapabilityMaximum"
+ "addConcreteScope:forScope:"
+ "addQuarantinedRecordWithScopedIdentifier:related:recordClass:reason:error:"
+ "addTransportScope:forScope:"
+ "beginChangeSessionWithSessionToken:completionHandler:"
+ "capable"
+ "changing asset from %@ to %@"
+ "clientFeatureCompatibleVersion = %@"
+ "com.apple.photos.client-side-encryption-manager"
+ "deactivated-engine"
+ "defaultAccountEPPCapabilityInUniverseName:"
+ "defaults"
+ "descriptionForAccountEPPCapability:"
+ "descriptionForSupportedFeatureCompatibleVersion:"
+ "disableBoundaryKeyFetching"
+ "disabled-features"
+ "endChangeSessionWithSessionToken:"
+ "epp-assets"
+ "epp.auto-enable"
+ "epp.capability-check"
+ "fingerprintContextIfKnown"
+ "getBytes:length:"
+ "getCloudCacheRecordsWithLocalScopedIdentifiers:desiredProperties:completionHandler:"
+ "hasMasterIdentifier"
+ "https"
+ "initForMMCSv2:"
+ "initWithBatch:targetMapping:ruleGroups:pushRepositoryPriority:fingerprintContext:provider:"
+ "initWithFingerprintSchemeV1:fingerprintSchemeV2:"
+ "initWithObject:selector:functionName:"
+ "initWithSuiteName:"
+ "initWithURL:resolvingAgainstBaseURL:"
+ "isCompatibleWithFingerprintScheme:"
+ "isEPPRecord"
+ "isStableHash:"
+ "isTransientDerivativeGenerationError:"
+ "isValidFingerprint:"
+ "maximumAccountEPPCapability"
+ "not-capable"
+ "observeAsyncCallWithFunction:block:"
+ "observeSyncCallWithFunction:block:"
+ "pathComponents"
+ "performUpgradeWithError:"
+ "providesEnhancedPrivacy"
+ "realStableHash"
+ "record %@ is not known to cloud cache"
+ "redacted."
+ "refreshBoundaryKeyWithSource:completionHandler:"
+ "removeRelatedRecordsFromQuarantineWithError:"
+ "requestClientToPullAllChangesInScopeIdentifiers:completionHandler:"
+ "scheme"
+ "scopeForScopeIdentifier:"
+ "session has been superseded"
+ "setAccountEPPCapability:"
+ "setBool:forKey:"
+ "setBoundaryKey:"
+ "setHasUpdatedScope:fromTransportWithError:"
+ "setHost:"
+ "setPath:"
+ "setScheme:"
+ "setUserModificationDate:"
+ "setupFingerprintContextForTests"
+ "share.icloud.com"
+ "shared-library"
+ "shouldCheckEPPCapability"
+ "shouldDisableEPP"
+ "storeVersionHasChanged"
+ "supportedFeatureCompatibleVersion"
+ "supportsEPPAutoEnable"
+ "umod"
+ "unsupported"
+ "updateWithAccountEPPCapability:source:"
+ "updateWithStatus:configuration:"
+ "userModificationDate"
+ "v36@?0@\"CPLScopedIdentifier\"8B16@\"NSString\"20#28"
+ "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "willBeginPushSession"
+ "www.icloud.com"
+ "\xf0\xe1"
- "\x01A\x13"
- "\b\x13!"
- "\t\x11\x15\x17("
- "\x13\x121#"
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
- "Error trying to generate unsupported video derivatives from %@"
- "No error but no transport scope available for %@"
- "T@\"CPLFingerprintSchemeV1\",R,N,V_mmcsv1FingerprintScheme"
- "T@\"CPLFingerprintSchemeV2\",R,N,V_mmcsv2FingerprintScheme"
- "T@\"NSString\",&,N,V_masterFingerprint"
- "TB,R,N,V_usesMMCSv2AsDefault"
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
- "initWithBoundaryKey:usesMMCSv2AsDefault:"
- "initWithFingerprintSchemeV1:fingerprintSchemeV2:usesMMCSv2AsDefault:"
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
- "usesMMCSv2AsDefaultInUniverseName:"
- "v32@0:8@\"CPLScopedIdentifier\"16@?<v@?@\"CPLRecordChange\"@\"NSError\">24"
- "v32@?0@\"CPLScopedIdentifier\"8@\"NSString\"16#24"
- "\xf0\xb1"

```
