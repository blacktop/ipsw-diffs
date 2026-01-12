## transparencyd

> `/usr/libexec/transparencyd`

```diff

-1547.80.7.0.0
-  __TEXT.__text: 0x276da0
+1547.80.8.0.0
+  __TEXT.__text: 0x276ff0
   __TEXT.__auth_stubs: 0x33f0
-  __TEXT.__objc_stubs: 0x1c880
-  __TEXT.__objc_methlist: 0x154a8
-  __TEXT.__cstring: 0x131e3
-  __TEXT.__objc_classname: 0x2c9a
-  __TEXT.__objc_methname: 0x231d4
-  __TEXT.__objc_methtype: 0x7805
+  __TEXT.__objc_stubs: 0x1c980
+  __TEXT.__objc_methlist: 0x154c8
+  __TEXT.__cstring: 0x131a7
+  __TEXT.__objc_classname: 0x2c9b
+  __TEXT.__objc_methname: 0x23229
+  __TEXT.__objc_methtype: 0x76f8
   __TEXT.__const: 0xba8c
-  __TEXT.__gcc_except_tab: 0x54fc
+  __TEXT.__gcc_except_tab: 0x552c
   __TEXT.__oslogstring: 0x11aa6
   __TEXT.__swift5_typeref: 0x2a98
   __TEXT.__swift5_capture: 0x14a8

   __TEXT.__swift_as_entry: 0x118
   __TEXT.__swift_as_ret: 0xc0
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0xa4b0
+  __TEXT.__unwind_info: 0xa4c0
   __TEXT.__eh_frame: 0x55b0
   __DATA_CONST.__auth_got: 0x1a08
   __DATA_CONST.__got: 0xfe8
   __DATA_CONST.__auth_ptr: 0x748
-  __DATA_CONST.__const: 0x170b0
-  __DATA_CONST.__cfstring: 0xe320
+  __DATA_CONST.__const: 0x17060
+  __DATA_CONST.__cfstring: 0xe280
   __DATA_CONST.__objc_classlist: 0xce8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x3d8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x6f0
-  __DATA_CONST.__objc_intobj: 0x6c0
+  __DATA_CONST.__objc_intobj: 0x660
   __DATA_CONST.__objc_arraydata: 0x1b8
   __DATA_CONST.__objc_dictobj: 0xf0
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA.__objc_const: 0x2fd40
-  __DATA.__objc_selrefs: 0x8758
-  __DATA.__objc_ivar: 0x10f0
+  __DATA.__objc_const: 0x2fd98
+  __DATA.__objc_selrefs: 0x8780
+  __DATA.__objc_ivar: 0x10f8
   __DATA.__objc_data: 0x9a18
   __DATA.__data: 0xa940
   __DATA.__thread_vars: 0x48

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: F29490FF-8DEC-39D3-A14E-1ED00FDBB10D
-  Functions: 16437
+  UUID: 195A8FF6-03E4-30B1-8036-3848311489E9
+  Functions: 16443
   Symbols:   1527
-  CStrings:  13697
+  CStrings:  13687
 
CStrings:
+ "@\"KTSelfValidationDiagnostics\""
+ "@\"KTSelfValidationResult\""
+ "@48@0:8Q16@24@32@40"
+ "KTSelfValidationResult"
+ "T@\"KTSelfValidationDiagnostics\",&,V_diagnostics"
+ "T@\"KTSelfValidationResult\",&,V_lastValidateSelfOptInResults"
+ "T@\"KTSelfValidationResult\",&,V_lastValidateSelfResults"
+ "T@\"KTSelfValidationResult\",&,V_selfValidationResult"
+ "T@\"NSString\",&,V_lastCheckIDSRegistration"
+ "T@\"NSString\",&,V_lastDutyCycle"
+ "T@\"NSString\",&,V_lastFetchCK"
+ "T@\"NSString\",&,V_lastFetchIDMS"
+ "T@\"NSString\",&,V_lastFetchIDSSelf"
+ "T@\"NSString\",&,V_lastFetchKTSelf"
+ "T@\"NSString\",&,V_lastForceSyncKVS"
+ "T@\"NSString\",&,V_lastPublicKeyRefresh"
+ "T@\"NSString\",&,V_lastRegistration"
+ "T@\"NSString\",&,V_lastSignalIDS"
+ "T@\"NSString\",&,V_lastValidateSelf"
+ "T@\"NSString\",&,V_lastValidateSelfOptIn"
+ "T@\"QueryRequest\",&,V_ktQueryRequest"
+ "T@\"QueryResponse\",&,V_ktQueryResponse"
+ "_diagnostics"
+ "_ktQueryRequest"
+ "_ktQueryResponse"
+ "_lastFetchCK"
+ "_lastValidateSelfOptInResults"
+ "_lastValidateSelfResults"
+ "handleOperationResults"
+ "initWithResult:loggableData:application:resultError:"
+ "ktQueryRequest"
+ "ktQueryResponse"
+ "lastFetchCK"
+ "lastValidateSelfOptInResults"
+ "lastValidateSelfResults"
+ "resultPendingForApplication:"
+ "self validation is pending"
+ "setDiagnostics:"
+ "setKtQueryRequest:"
+ "setKtQueryResponse:"
+ "setLastFetchCK:"
+ "setLastValidateSelfOptInResults:"
+ "setLastValidateSelfResults:"
+ "v40@0:8@\"NSString\"16@\"KTSelfValidationResult\"24@?<v@?BB@\"NSError\">32"
- "@\"KTBackgroundSystemValidationOperation\""
- "@\"KTCheckIDSRegistrationOperation\""
- "@\"KTEnrollmentRegistrationSignature\""
- "@\"KTFetchIDMSOperation\""
- "@\"KTFetchIDSSelfOperation\""
- "@\"KTFetchKTSelfOperation\""
- "@\"KTForceSyncKVSOperation\""
- "@\"KTPublicKeyStoreRefresh\""
- "@\"KTSMSelfValidationResult\""
- "@\"KTSignalIDSOperation\""
- "@\"KTTransparentData\""
- "@\"KTValidateSelfOperation\""
- "FetchIDSSelf"
- "FetchKTSelf"
- "FetchSelf"
- "KTSMSelfValidationResult"
- "T@\"KTBackgroundSystemValidationOperation\",&,V_lastDutyCycle"
- "T@\"KTCheckIDSRegistrationOperation\",&,V_lastCheckIDSRegistration"
- "T@\"KTEnrollmentRegistrationSignature\",&,V_lastRegistration"
- "T@\"KTFetchIDMSOperation\",&,V_lastFetchIDMS"
- "T@\"KTFetchIDSSelfOperation\",&,V_lastFetchIDSSelf"
- "T@\"KTFetchKTSelfOperation\",&,V_lastFetchKTSelf"
- "T@\"KTForceSyncKVSOperation\",&,V_lastForceSyncKVS"
- "T@\"KTPublicKeyStoreRefresh\",&,V_lastPublicKeyRefresh"
- "T@\"KTSMSelfValidationResult\",&,V_selfValidationResult"
- "T@\"KTSignalIDSOperation\",&,V_lastSignalIDS"
- "T@\"KTTransparentData\",&,V_transparentData"
- "T@\"KTValidateSelfOperation\",&,V_lastValidateSelf"
- "T@\"KTValidateSelfOperation\",&,V_lastValidateSelfOptIn"
- "T@\"NSError\",&,V_resultError"
- "T@\"NSOperation\",&,V_lastCKFetch"
- "T@\"QueryRequest\",&,V_queryRequest"
- "T@\"QueryResponse\",&,V_queryResponse"
- "ValidateFetchIDSSelf"
- "ValidateFetchKTSelf"
- "_lastCKFetch"
- "_resultError"
- "_transparentData"
- "fetch-ids-self"
- "handleOperationResults:"
- "initWithResult:transparentData:loggableData:application:resultError:"
- "lastCKFetch"
- "resultError"
- "setLastCKFetch:"
- "setResultError:"
- "setTransparentData:"
- "transparencyTriggerFetchSelf:"
- "triggerFetchSelf:"
- "v40@0:8@\"NSString\"16@\"KTSMSelfValidationResult\"24@?<v@?BB@\"NSError\">32"

```
