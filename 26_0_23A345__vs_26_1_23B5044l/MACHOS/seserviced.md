## seserviced

> `/usr/libexec/seserviced`

```diff

-60.35.0.0.0
-  __TEXT.__text: 0x3e3e3c
-  __TEXT.__auth_stubs: 0x4a20
+61.3.0.0.0
+  __TEXT.__text: 0x3e6ffc
+  __TEXT.__auth_stubs: 0x4a30
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0x2c4
-  __TEXT.__objc_stubs: 0x9c60
-  __TEXT.__objc_methlist: 0x64dc
-  __TEXT.__const: 0xec88
-  __TEXT.__gcc_except_tab: 0x3598
-  __TEXT.__objc_methname: 0x12f21
-  __TEXT.__oslogstring: 0x2a2cc
-  __TEXT.__cstring: 0x23454
-  __TEXT.__objc_classname: 0x11be
-  __TEXT.__objc_methtype: 0x668b
-  __TEXT.__swift5_typeref: 0x4bc8
+  __TEXT.__objc_stubs: 0x9ca0
+  __TEXT.__objc_methlist: 0x651c
+  __TEXT.__const: 0xec98
+  __TEXT.__gcc_except_tab: 0x368c
+  __TEXT.__objc_methname: 0x12f70
+  __TEXT.__oslogstring: 0x2a55c
+  __TEXT.__cstring: 0x23544
+  __TEXT.__objc_classname: 0x11d4
+  __TEXT.__objc_methtype: 0x6673
+  __TEXT.__swift5_typeref: 0x4bda
   __TEXT.__constg_swiftt: 0x4d60
   __TEXT.__swift5_reflstr: 0x544a
   __TEXT.__swift5_fieldmd: 0x5298
   __TEXT.__swift5_builtin: 0x2bc
   __TEXT.__swift5_assocty: 0x6c0
-  __TEXT.__swift5_capture: 0x22c4
+  __TEXT.__swift5_capture: 0x22f4
   __TEXT.__swift5_proto: 0x80c
   __TEXT.__swift5_types: 0x51c
   __TEXT.__swift_as_entry: 0x380
   __TEXT.__swift_as_ret: 0x518
   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_mpenum: 0x90
-  __TEXT.__unwind_info: 0x97d0
-  __TEXT.__eh_frame: 0x1312c
-  __DATA_CONST.__auth_got: 0x2528
-  __DATA_CONST.__got: 0x15d0
+  __TEXT.__unwind_info: 0x97c8
+  __TEXT.__eh_frame: 0x13194
+  __DATA_CONST.__auth_got: 0x2530
+  __DATA_CONST.__got: 0x15d8
   __DATA_CONST.__auth_ptr: 0xdd0
-  __DATA_CONST.__const: 0x11800
-  __DATA_CONST.__cfstring: 0x8e40
-  __DATA_CONST.__objc_classlist: 0x768
+  __DATA_CONST.__const: 0x11b78
+  __DATA_CONST.__cfstring: 0x8e80
+  __DATA_CONST.__objc_classlist: 0x770
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x420
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_intobj: 0x810
-  __DATA.__objc_const: 0x15aa8
-  __DATA.__objc_selrefs: 0x4400
-  __DATA.__objc_ivar: 0xb34
-  __DATA.__objc_data: 0x62e0
-  __DATA.__data: 0xbb34
+  __DATA.__objc_const: 0x15ba8
+  __DATA.__objc_selrefs: 0x4410
+  __DATA.__objc_ivar: 0xb3c
+  __DATA.__objc_data: 0x6330
+  __DATA.__data: 0xbcb4
   __DATA.__bss: 0xe480
   __DATA.__common: 0x700
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 81B48020-A09A-3816-97B4-8AD91E6D802F
-  Functions: 11460
-  Symbols:   2104
-  CStrings:  11827
+  UUID: 8B78C8A2-F2AF-33E9-8C0F-4B90A0A9AFEA
+  Functions: 11493
+  Symbols:   2105
+  CStrings:  11854
 
Symbols:
+ _objc_retain_x10
CStrings:
+ "%s -- error %s encountered"
+ "%s deleting credential config %s"
+ "?3A"
+ "@48@0:8@16@24q32@40"
+ "BSXPCConnection is unexpectedly not setup"
+ "BSXPCConnection setup failed"
+ "Couldn't load ECID from MG %@"
+ "Deleting credential configs due to absence of instance %s"
+ "Device does not support a database"
+ "ECID length isn't uint64? %d"
+ "ECID mismatched attestation %{private}lld != local %{private}lld"
+ "Error encountered while setting up BSXPCConnection"
+ "Failed to initialize database"
+ "Failed to parse attestation applet data? %d %@"
+ "Failed to parse attestation data? %d %@"
+ "Failed to parse attestation? %d %@"
+ "Initializing debug server"
+ "No aux keys found for endpoint with primary reader ID %s"
+ "No ecp2info with key %s found for endpoint"
+ "No free slot available, adding %s to queue"
+ "No keys fetched for %s"
+ "One or more endpoints did not perform the rebind successfully"
+ "Q48@0:8@16@24@32^@40"
+ "Received RSSI update %s"
+ "SESDatabaseReadHandle"
+ "T@\"NSManagedObjectContext\",R,N,V_context"
+ "T@\"SESEndpointDatabase\",R,N,V_database"
+ "Unable to attest imported key on SN200V"
+ "Unexpected BSXPCConnection not setup"
+ "UniqueChipID"
+ "_cleanupAppletsWithNoEndpoints:handle:"
+ "_createEndPointCA:handle:clientName:identifier:subjectIdentifier:forEndPointType:error:"
+ "_ensureCAExistsAndValid:clientName:secureElement:handle:forEndPointType:error:"
+ "_existsDuplicateInDatabase:withIdentifier:orReaderIdentifier:outError:"
+ "_preWarmAlishaInternal:handle:proximityChipInfo:manufactuer:clientName:error:"
+ "_renewEndPointCAIfExpired:secureElement:forEndPointType:handle:"
+ "deleteCredentialConfigs(_:)"
+ "fixEndpointSignatureCertificatePK:"
+ "iOS (26.1) - SecureElementService-61.3"
+ "reconcileCredentialConfigDatabase()"
+ "revokeRemoteTerminationRequestEndPoints:handle:identifier:taskID:clientInfo:outError:"
+ "stageEndPointEntityWithIdentifier:endPointCAEntity:airInstanceEntity:clientName:handle:error:"
+ "startTransaction:"
+ "updatePreArmState:for:"
+ "v16@?0@\"SESDatabaseReadHandle\"8"
+ "v24@?0@\"SESDatabaseReadHandle\"8@\"NSError\"16"
+ "v28@0:8B16@20"
+ "v32@?0@\"SecureElement\"8@\"SESDatabaseReadHandle\"16@\"NSError\"24"
+ "v40@?0@\"SESDatabaseReadHandle\"8@\"SEEndPointEntity\"16@\"SEEndPoint\"24@\"NSError\"32"
+ "v40@?0@\"SecureElement\"8@\"SESDatabaseReadHandle\"16@\"SESProximityChip\"24@\"NSError\"32"
+ "v48@?0@\"SecureElement\"8@\"SESDatabaseReadHandle\"16@\"SEEndPointEntity\"24@\"SEEndPoint\"32@\"NSError\"40"
+ "wiredTransactionWithAuthDuration"
- "?2A"
- "@40@0:8@16@24q32"
- "B36@0:8B16@20^@28"
- "Connection is nil, setting up"
- "Database not initialized"
- "No aux keys found for endpoint %s"
- "No free slot available, adding to queue"
- "One ore more endpoints did not perform the rebind successfully"
- "Q56@0:8@16@24@32@40^@48"
- "_cleanupAppletsWithNoEndpoints:secureElement:"
- "_createEndPointCA:database:clientName:identifier:subjectIdentifier:forEndPointType:error:"
- "_ensureCAExistsAndValid:clientName:secureElement:database:forEndPointType:error:"
- "_existsDuplicateInDatabase:airInstanceEntity:withIdentifier:orReaderIdentifier:outError:"
- "_preWarmAlishaInternal:database:proximityChipInfo:manufactuer:clientName:error:"
- "_renewEndPointCAIfExpired:secureElement:forEndPointType:"
- "fixEndpointSignatureCertificatePK"
- "iOS (26.0) - SecureElementService-60.35"
- "revokeRemoteTerminationRequestEndPoints:sesDatabase:identifier:taskID:clientInfo:outError:"
- "stageEndPointEntityWithIdentifier:endPointCAEntity:airInstanceEntity:clientName:error:"
- "updatePreArmState:for:error:"
- "v16@?0@\"NSManagedObjectContext\"8"
- "v24@?0@\"SESEndpointDatabase\"8@\"NSError\"16"
- "v32@?0@\"SecureElement\"8@\"SESEndpointDatabase\"16@\"NSError\"24"
- "v40@?0@\"SESEndpointDatabase\"8@\"SEEndPointEntity\"16@\"SEEndPoint\"24@\"NSError\"32"
- "v40@?0@\"SecureElement\"8@\"SESEndpointDatabase\"16@\"SESProximityChip\"24@\"NSError\"32"
- "v48@?0@\"SecureElement\"8@\"SESEndpointDatabase\"16@\"SEEndPointEntity\"24@\"SEEndPoint\"32@\"NSError\"40"
- "wiredTransactionWithAuthTotalDuration"

```
