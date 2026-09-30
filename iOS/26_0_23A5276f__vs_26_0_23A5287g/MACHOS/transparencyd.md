## transparencyd

> `/usr/libexec/transparencyd`

```diff

-1547.0.12.0.0
-  __TEXT.__text: 0x2555dc
-  __TEXT.__auth_stubs: 0x3080
-  __TEXT.__objc_stubs: 0x1c000
-  __TEXT.__objc_methlist: 0x15020
-  __TEXT.__cstring: 0x1298c
+1547.0.24.0.0
+  __TEXT.__text: 0x256a78
+  __TEXT.__auth_stubs: 0x3090
+  __TEXT.__objc_stubs: 0x1c1e0
+  __TEXT.__objc_methlist: 0x15060
+  __TEXT.__cstring: 0x129ec
   __TEXT.__objc_classname: 0x2c70
-  __TEXT.__objc_methname: 0x22646
-  __TEXT.__objc_methtype: 0x74b2
-  __TEXT.__const: 0xa9e4
-  __TEXT.__gcc_except_tab: 0x5254
-  __TEXT.__oslogstring: 0x113e5
+  __TEXT.__objc_methname: 0x2276b
+  __TEXT.__objc_methtype: 0x7500
+  __TEXT.__const: 0xaa04
+  __TEXT.__gcc_except_tab: 0x52cc
+  __TEXT.__oslogstring: 0x11485
   __TEXT.__swift5_typeref: 0x243a
   __TEXT.__swift5_reflstr: 0x1795
   __TEXT.__swift5_assocty: 0x4b0

   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_proto: 0x80c
   __TEXT.__swift5_types: 0x274
-  __TEXT.__swift5_capture: 0x10e4
+  __TEXT.__swift5_capture: 0x1124
   __TEXT.__swift_as_entry: 0x118
   __TEXT.__swift_as_ret: 0xc0
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x9df8
-  __TEXT.__eh_frame: 0x4f30
-  __DATA_CONST.__auth_got: 0x1850
-  __DATA_CONST.__got: 0xed0
+  __TEXT.__unwind_info: 0x9e98
+  __TEXT.__eh_frame: 0x4f80
+  __DATA_CONST.__auth_got: 0x1858
+  __DATA_CONST.__got: 0xee0
   __DATA_CONST.__auth_ptr: 0x5d8
-  __DATA_CONST.__const: 0x15fe0
-  __DATA_CONST.__cfstring: 0xe120
+  __DATA_CONST.__const: 0x16198
+  __DATA_CONST.__cfstring: 0xe160
   __DATA_CONST.__objc_classlist: 0xcb8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x3c8

   __DATA_CONST.__objc_arraydata: 0x1b8
   __DATA_CONST.__objc_dictobj: 0xf0
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA.__objc_const: 0x2e4c8
-  __DATA.__objc_selrefs: 0x8470
+  __DATA.__objc_const: 0x2e4d8
+  __DATA.__objc_selrefs: 0x84e8
   __DATA.__objc_ivar: 0x10cc
   __DATA.__objc_data: 0x9458
   __DATA.__data: 0xa2b0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3ECB4446-FB84-3431-9553-79852C455BF5
-  Functions: 15812
-  Symbols:   1411
-  CStrings:  13434
+  UUID: A0877957-7092-3A88-973F-F5610EB27E9D
+  Functions: 15835
+  Symbols:   1414
+  CStrings:  13462
 
Symbols:
+ _$sSS11utf8CStrings15ContiguousArrayVys4Int8VGvg
+ _OBJC_CLASS_$_KTURI
+ _OBJC_CLASS_$_KTValidatePeersResponse
CStrings:
+ " imHandle %{mask.hash}@ not found"
+ " updating handle %{mask.hash}@ with %d"
+ "%@ "
+ "KTPrimaryAccount"
+ "ValidateSelf: failed to find request for requestId %{public}@ for %@"
+ "calling IDS with %lu results for %{mask.hash}.@"
+ "clearKTSignaturePolicy"
+ "drainContextStore"
+ "fetchNow"
+ "fillUploadedRdata:withRegistrationData:"
+ "initWithApplication:results:"
+ "initWithIDSURL:application:"
+ "ktSignaturePolicy"
+ "ktURI"
+ "privacyURI:"
+ "public"
+ "redactedDescription"
+ "setKtURIVRF:"
+ "setTraceUUID:"
+ "signaturePolicy: clearing signature policy: %d"
+ "signaturePolicy: corrupt public key"
+ "signaturePolicy: corrupt signature"
+ "signaturePolicy: empty public key"
+ "signaturePolicy: empty signature"
+ "signaturePolicy: leaving policy in place: %d"
+ "uriToVerificationInfo"
+ "uris failed: "
+ "v32@0:8@\"KTValidatePeersQuery\"16@?<v@?@\"KTValidatePeersResponse\"@\"NSError\">24"
+ "v32@?0@\"KTVerifierResult\"8Q16^B24"
+ "v32@?0@\"NSString\"8@\"NSError\"16^B24"
+ "validatePeers: returning %lu results for %{mask.hash}@: %@"
+ "validatePeers:completionBlock:"
+ "validateStoreEntry looking for handles: %{mask.hash}@"
- " imHandle %@ not found"
- " updating handle %@ with %d"
- "ValidateSelf: failed to find request for requestId %{public}@ for %{mask.hash}@"
- "calling IDS with %lu results for %@"
- "fetchDeviceSignature callback: Skipping rdata for application %{public}@ because it has not been uploaded to CloudKit"
- "uris failed: %@"
- "validatePeers: returning %lu results for %@: %@"
- "validateStoreEntry looking for handles: %@"

```
