## com.apple.health.records.legacy-ingestion

> `/System/Library/PrivateFrameworks/HealthRecordServices.framework/XPCServices/com.apple.health.records.legacy-ingestion.xpc/com.apple.health.records.legacy-ingestion`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0xb500
+6074.1.2.4.0
+  __TEXT.__text: 0xb974
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_stubs: 0x22e0
-  __TEXT.__objc_methlist: 0xef4
-  __TEXT.__objc_methname: 0x2b1f
-  __TEXT.__cstring: 0xe35
-  __TEXT.__objc_classname: 0x32d
-  __TEXT.__objc_methtype: 0x784
-  __TEXT.__const: 0x40
-  __TEXT.__oslogstring: 0x402
-  __TEXT.__unwind_info: 0x3a8
+  __TEXT.__objc_methlist: 0xe94
+  __TEXT.__cstring: 0xd09
+  __TEXT.__objc_methname: 0x2a4e
+  __TEXT.__objc_classname: 0x2f8
+  __TEXT.__objc_methtype: 0x83c
+  __TEXT.__const: 0x38
+  __TEXT.__oslogstring: 0x5d8
+  __TEXT.__unwind_info: 0x398
   __DATA_CONST.__auth_got: 0x280
-  __DATA_CONST.__got: 0x160
-  __DATA_CONST.__const: 0x3e8
-  __DATA_CONST.__cfstring: 0x10a0
-  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__const: 0x388
+  __DATA_CONST.__cfstring: 0xe60
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_intobj: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x1d10
-  __DATA.__objc_selrefs: 0xa98
-  __DATA.__objc_ivar: 0xf4
-  __DATA.__objc_data: 0x780
+  __DATA.__objc_const: 0x1b20
+  __DATA.__objc_selrefs: 0xa48
+  __DATA.__objc_ivar: 0xe4
+  __DATA.__objc_data: 0x6e0
   __DATA.__data: 0x240
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3D84A9AC-BC30-3132-93B4-94579F6339EF
-  Functions: 330
-  Symbols:   200
-  CStrings:  866
+  UUID: 0E26DE4E-9909-3C17-AFF7-8EE597A4059A
+  Functions: 321
+  Symbols:   199
+  CStrings:  816
 
Symbols:
+ _HKFHIRAuthorizationSchemaParameterNamePKCEChallenge
+ _HKFHIRAuthorizationSchemaParameterNamePKCEMethod
+ _HKFHIRAuthorizationSchemaParameterNamePKCEVerifier
+ _HKFHIREndpointSchemaVariableClientID
+ _HKFHIREndpointSchemaVariableClientSecret
+ _HKFHIREndpointSchemaVariableCode
+ _HKFHIREndpointSchemaVariableGreaterEqualLastFetchDate
+ _HKFHIREndpointSchemaVariableGreaterEqualLastFetchDateTime
+ _HKFHIREndpointSchemaVariablePKCEChallenge
+ _HKFHIREndpointSchemaVariablePKCEVerifier
+ _HKFHIREndpointSchemaVariablePatient
+ _HKFHIREndpointSchemaVariableRefreshToken
+ _HKFHIREndpointSchemaVariableState
+ _NSStringFromHKFHIRResourceQueryMode
- _HDFHIREndpointSchemaVariableClientID
- _HDFHIREndpointSchemaVariableClientSecret
- _HDFHIREndpointSchemaVariableCode
- _HDFHIREndpointSchemaVariableGreaterEqualLastFetchDate
- _HDFHIREndpointSchemaVariableGreaterEqualLastFetchDateTime
- _HDFHIREndpointSchemaVariablePKCEChallenge
- _HDFHIREndpointSchemaVariablePKCEVerifier
- _HDFHIREndpointSchemaVariableRefreshToken
- _HDFHIREndpointSchemaVariableState
- _HDFHIRQueryModeFromHKFHIRResourceQueryMode
- _OBJC_CLASS_$_HDFHIRResourceDocument
- _OBJC_CLASS_$_HDFHIRResourceExtractionBatch
- _OBJC_METACLASS_$_HDFHIRResourceDocument
- _OBJC_METACLASS_$_HDFHIRResourceExtractionBatch
- _objc_release_x1
CStrings:
+ "%{public}@ completed refresh token task with %{public}@"
+ "%{public}@ done with fetchOrRefreshCredential for account %{public}@ with result %{public}@"
+ "%{public}@ failed to fetch access token for %{public}@: %{public}@"
+ "%{public}@ failed to init FHIR specification: %{public}@"
+ "%{public}@ is starting %{public}@"
+ "%{public}@ starting fetchOrRefreshCredential for account %{public}@"
+ "%{public}@ successfully finished fetching access token for %{public}@"
+ "%{public}@ will start fetching access token for %{public}@"
+ "Error instantiating auth schema: %@"
+ "_credentialedSessionSuitableForConnectionInformation:"
+ "authSchemas"
+ "fetchAccessTokenForTokenSession:connectionInformation:completion:"
+ "fetchOrRefreshCredentialForAccount:completion:"
+ "remote_fetchAccessTokenForTokenSession:connectionInformation:completion:"
+ "remote_fetchOrRefreshCredentialForAccount:completion:"
+ "requestedScope"
+ "v32@0:8@\"HKClinicalAccountConnectionInformation\"16@?<v@?@\"HKFHIRCredentialRefreshResult\">24"
+ "v40@0:8@\"HKOAuth2TokenSession\"16@\"HKClinicalAccountConnectionInformation\"24@?<v@?@\"HKFHIRCredential\"@\"HKFHIRRequestTaskEndState\"@\"NSError\">32"
- "@\"HDFHIRResourceDocument\""
- "@\"NSDictionary\"16@?0@\"HDOriginalFHIRResourceObject\"8"
- "@\"NSNumber\""
- "@24@0:8@?16"
- "HDFHIRResourceDocument"
- "HDFHIRResourceExtractionBatch"
- "HDFHIRResourceExtractionBatch.m"
- "JSONObject"
- "PKCEChallenge"
- "PKCEVerifier"
- "T@\"HDFHIRResourceDocument\",R,N,V_document"
- "T@\"NSNumber\",R,C,N,V_highestRowID"
- "T@\"NSNumber\",R,C,N,V_rulesVersion"
- "Unknown HKFHIRResourceQueryMode %lu, returning \"all\" HDFHIRQueryMode"
- "_credentialedSessionSuitableForRequest:"
- "_dictionaryRepresentationWithResourceHandler:"
- "_document"
- "_highestRowID"
- "_resourceObjects"
- "_rulesVersion"
- "addObjectsFromArray:"
- "addResourceObjects:"
- "array"
- "authSchemaDefinitions"
- "code_challenge"
- "code_challenge_method"
- "code_verifier"
- "dictionary"
- "dictionaryRepresentation"
- "document"
- "full"
- "geLastFetchedDate"
- "geLastFetchedDateTime"
- "highestRowID"
- "i"
- "identifier"
- "initWithDocument:rulesVersion:"
- "initWithDocument:rulesVersion:highestRowID:"
- "patient"
- "resourceObjects"
- "resourceSchemaDefinitions"
- "rulesVersion"
- "rulesVersion != nil"
- "update"

```
