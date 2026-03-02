## coreidvd

> `/usr/libexec/coreidvd`

```diff

-8.417.0.0.0
-  __TEXT.__text: 0x67aea4
+8.418.2.0.0
+  __TEXT.__text: 0x67827c
   __TEXT.__auth_stubs: 0xc800
-  __TEXT.__objc_stubs: 0x6e80
+  __TEXT.__objc_stubs: 0x6e60
   __TEXT.__objc_methlist: 0x1fac
-  __TEXT.__const: 0x30270
-  __TEXT.__cstring: 0x28426
+  __TEXT.__const: 0x30260
+  __TEXT.__cstring: 0x284f6
   __TEXT.__objc_classname: 0x35e3
-  __TEXT.__objc_methname: 0xd546
-  __TEXT.__objc_methtype: 0x47db
+  __TEXT.__objc_methname: 0xd526
+  __TEXT.__objc_methtype: 0x470b
   __TEXT.__swift5_typeref: 0xba0c
-  __TEXT.__swift5_fieldmd: 0xdeac
-  __TEXT.__constg_swiftt: 0xd70c
+  __TEXT.__swift5_fieldmd: 0xde64
+  __TEXT.__constg_swiftt: 0xd6fc
   __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_reflstr: 0xba3e
+  __TEXT.__swift5_reflstr: 0xb9ce
   __TEXT.__swift5_assocty: 0xbc8
   __TEXT.__swift5_protos: 0x1b8
   __TEXT.__swift5_proto: 0x1d70
   __TEXT.__swift5_types: 0xbe4
-  __TEXT.__oslogstring: 0x29681
-  __TEXT.__swift5_capture: 0x5708
+  __TEXT.__oslogstring: 0x29791
+  __TEXT.__swift5_capture: 0x5758
   __TEXT.__swift5_mpenum: 0x98
   __TEXT.__swift_as_entry: 0x1194
-  __TEXT.__swift_as_ret: 0x1a0c
+  __TEXT.__swift_as_ret: 0x1a00
   __TEXT.__swift5_acfuncs: 0x64
   __TEXT.__swift5_entry: 0x8
   __TEXT.__gcc_except_tab: 0xac
   __TEXT.__unwind_info: 0x15020
-  __TEXT.__eh_frame: 0x428c0
+  __TEXT.__eh_frame: 0x428e8
   __DATA_CONST.__auth_got: 0x6410
   __DATA_CONST.__got: 0x3fb0
-  __DATA_CONST.__auth_ptr: 0x2258
-  __DATA_CONST.__const: 0x21540
+  __DATA_CONST.__auth_ptr: 0x2250
+  __DATA_CONST.__const: 0x21550
   __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x708
   __DATA_CONST.__objc_protolist: 0x228

   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__linkguard: 0xe
   __DATA.__objc_const: 0x10ce0
-  __DATA.__objc_selrefs: 0x24b8
+  __DATA.__objc_selrefs: 0x24b0
   __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0x39a8
-  __DATA.__data: 0x17910
+  __DATA.__data: 0x17900
   __DATA.__bss: 0x37230
   __DATA.__common: 0x752
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7D5C8FB9-4557-3593-AF7A-DBF7786BADF9
-  Functions: 17875
-  Symbols:   5677
-  CStrings:  8183
+  UUID: 46EEBCAD-F68F-373F-8524-7D8F769076B1
+  Functions: 17876
+  Symbols:   5676
+  CStrings:  8185
 
Symbols:
+ _$s13CoreIDVShared25IdentityProofingNFCConfigC24minimumReadTimeThreshold17readRetryInterval17readyCheckEnabledACSiSg_AGSbSgtcfc
+ _$s13CoreIDVShared8DIPErrorV4CodeO38failedToShowTTRInsufficientInformationyA2EmFWC
- _$s13CoreIDVShared25IdentityProofingNFCConfigC24minimumReadTimeThreshold17readRetryInterval17readyCheckEnabled015isChipIntegrityN15FailureTerminal0p11DeviceCrossnO0ACSiSg_AISbSgA2Jtcfc
- _$s13CoreIDVShared25IdentityProofingNFCConfigCMn
- _$s13CoreIDVShared8DIPErrorV4CodeO70remoteSessionServiceUnavailableUnableToFetchProvisioningFailureReasonsyA2EmFWC
CStrings:
+ ", encryptedNFCPII is empty: "
+ "Failed to show TTR alert insufficient data encryptedCredentialPII is empty: "
+ "Ignoring error due to internal setting"
+ "Non fatal - unable to fetch credential properties for server action notification: %@"
+ "Non fatal - unable to notify server of terminal state with error: %@"
+ "Non fatal error - failed to fetch encryptedNFCPII with error: %@"
+ "Unable to find PII hash in producedAssetManager - fail to store hash in idcredd"
+ "Unable to notifyServerOfTerminalState no proofing session"
+ "Updated the proofing status to readyToAddID as provisioning has failed"
+ "non terminal - remoteSessionService is nil unable to fetch provisioningFailureReasons"
+ "showTTRAlert(proofingSessionID:encryptedCredentialPII:encryptedNFCPII:)"
+ "unable to fetch credential properties for provisionFailureReason and encryptedPII with error: "
+ "updateProofing(proofingSessionId:target:)"
- "Failed to store pii hash in keychain"
- "Failed to store pii token in keychain"
- "No provisioning failure reason fetched with error: "
- "Unable to storePIIHash - unable to find PII Hash"
- "Updated the proofing status to readyToAddID as provisioning as failed"
- "isChipIntegrityCheckFailureTerminal"
- "isDeviceCrossCheckEnabled"
- "isPIIMismatchTerminal"
- "remoteSessionService is nil unable to fetch provisioningFailureReasons"
- "setIsPIIHashMismatchTerminal:"
- "v48@0:8@\"_TtC13CoreIDVShared29IdentityProofingConfiguration\"16@\"_TtC13CoreIDVShared25IdentityProofingDocuments\"24@\"NSString\"32@?<v@?@\"_TtC13CoreIDVShared25IdentityProofingNFCConfig\"@\"NSError\">40"

```
