## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary`

```diff

-750.5.104.0.0
-  __TEXT.__text: 0x188ee0
+750.11.101.0.0
+  __TEXT.__text: 0x18b1ec
   __TEXT.__auth_stubs: 0xef0
-  __TEXT.__objc_methlist: 0x12a34
+  __TEXT.__objc_methlist: 0x12b74
   __TEXT.__const: 0x2e8
-  __TEXT.__gcc_except_tab: 0x4178
-  __TEXT.__oslogstring: 0x13eff
-  __TEXT.__cstring: 0x1338d
-  __TEXT.__unwind_info: 0x5908
+  __TEXT.__gcc_except_tab: 0x41dc
+  __TEXT.__oslogstring: 0x14141
+  __TEXT.__cstring: 0x1353e
+  __TEXT.__unwind_info: 0x59a0
   __TEXT.__objc_classname: 0x1d77
-  __TEXT.__objc_methname: 0x29b92
-  __TEXT.__objc_methtype: 0x4506
-  __TEXT.__objc_stubs: 0x19620
+  __TEXT.__objc_methname: 0x29f06
+  __TEXT.__objc_methtype: 0x451e
+  __TEXT.__objc_stubs: 0x198c0
   __DATA_CONST.__got: 0xa28
-  __DATA_CONST.__const: 0x5dd0
+  __DATA_CONST.__const: 0x5df8
   __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x82d0
+  __DATA_CONST.__objc_selrefs: 0x8380
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x7f0
-  __DATA_CONST.__objc_arraydata: 0x12c0
+  __DATA_CONST.__objc_arraydata: 0x12d0
   __AUTH_CONST.__auth_got: 0x788
-  __AUTH_CONST.__const: 0x2560
-  __AUTH_CONST.__cfstring: 0x147a0
-  __AUTH_CONST.__objc_const: 0x1d410
+  __AUTH_CONST.__const: 0x25a0
+  __AUTH_CONST.__cfstring: 0x14a00
+  __AUTH_CONST.__objc_const: 0x1d528
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x40
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x1724
+  __DATA.__objc_ivar: 0x1734
   __DATA.__data: 0xf30
-  __DATA.__bss: 0x878
+  __DATA.__bss: 0x890
   __DATA.__common: 0x21
   __DATA_DIRTY.__objc_data: 0x5230
   __DATA_DIRTY.__data: 0x9

   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8232
-  Symbols:   9384
-  CStrings:  11847
+  Functions: 8272
+  Symbols:   9425
+  CStrings:  11906
 
Symbols:
+ _CPLAppBundleIdentifierForContainerIdentifier
+ _CPLFeatureNameEPP
CStrings:
+ "\f\x11\x15\x17("
+ "\x13\"1#"
+ "%@ is trying to begin a session twice"
+ "Account capability is %{public}@ (%{public}@) - switching EPP enabled to %@"
+ "B52@0:8@16B24#28@36^@44"
+ "Beginning change session for %@"
+ "Blocking change session for %@ until %@ is done"
+ "CPLAlwaysAutoEnableEPP"
+ "CPLDisableEPPCapabilityCheck"
+ "CPLEPPEnabled"
+ "CPLEPPEnabledSource"
+ "Change session for %@ has been ended before it even began"
+ "CloudPhotoLibrary-750.11.101"
+ "Derivative generation error is transient, will retry: %@"
+ "EPP"
+ "EPPAutoEnable"
+ "Ending change session for %@"
+ "Ending unknown change session for %@"
+ "Error trying to generate derivatives for unsupported input video from %@: %@"
+ "Refreshing boundary key for %{public}@"
+ "Requesting update of %@ for Account EPP capability"
+ "Resuming change session for %@"
+ "TB,R,N,V_shouldCheckEPPCapability"
+ "TB,R,V_usesMMCSv2AsDefault"
+ "Trying to refresh fingerprint context while the library is not open"
+ "_addQuarantinedRecordWithScopedIdentifier:related:recordClass:reason:error:"
+ "_currentChangeSessionToken"
+ "_fetchBoundaryKeyIfNecessaryWithSourceLocked:completionHandler:"
+ "_pendingChangeSessionCompletionHandler"
+ "_pendingChangeSessionToken"
+ "_requestUpdateOfMainScopeFromTransport"
+ "_shouldCheckEPPCapability"
+ "_updateFingerprintContext"
+ "accountEPPCapability"
+ "accountEPPCapabilityMaximum"
+ "addQuarantinedRecordWithScopedIdentifier:related:recordClass:reason:error:"
+ "beginChangeSessionWithSessionToken:completionHandler:"
+ "capable"
+ "deactivated-engine"
+ "defaultAccountEPPCapabilityInUniverseName:"
+ "defaults"
+ "descriptionForAccountEPPCapability:"
+ "disabled-features"
+ "endChangeSessionWithSessionToken:"
+ "epp.auto-enable"
+ "epp.capability-check"
+ "initWithFingerprintSchemeV1:fingerprintSchemeV2:"
+ "initWithSuiteName:"
+ "isEPPRecord"
+ "isTransientDerivativeGenerationError:"
+ "maximumAccountEPPCapability"
+ "not-capable"
+ "removeRelatedRecordsFromQuarantineWithError:"
+ "session has been superseded"
+ "setAccountEPPCapability:"
+ "setBool:forKey:"
+ "setHasUpdatedScope:fromTransportWithError:"
+ "shouldCheckEPPCapability"
+ "shouldDisableEPP"
+ "supportsEPPAutoEnable"
+ "unsupported"
+ "updateWithAccountEPPCapability:source:"
+ "updateWithStatus:configuration:"
+ "v36@?0@\"CPLScopedIdentifier\"8B16@\"NSString\"20#28"
+ "\xf0\xe1"
- "\t\x11\x15\x17("
- "\x13\x121#"
- "CloudPhotoLibrary-750.5.104"
- "Error trying to generate unsupported video derivatives from %@"
- "TB,R,N,V_usesMMCSv2AsDefault"
- "initWithBoundaryKey:usesMMCSv2AsDefault:"
- "initWithFingerprintSchemeV1:fingerprintSchemeV2:usesMMCSv2AsDefault:"
- "usesMMCSv2AsDefaultInUniverseName:"
- "v32@?0@\"CPLScopedIdentifier\"8@\"NSString\"16#24"
- "\xf0\xb1"

```
