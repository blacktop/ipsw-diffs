## coreidvd

> `/usr/libexec/coreidvd`

```diff

-8.415.0.0.0
-  __TEXT.__text: 0x674ea8
-  __TEXT.__auth_stubs: 0xc7b0
-  __TEXT.__objc_stubs: 0x6d20
+8.417.0.0.0
+  __TEXT.__text: 0x67aea4
+  __TEXT.__auth_stubs: 0xc800
+  __TEXT.__objc_stubs: 0x6e80
   __TEXT.__objc_methlist: 0x1fac
-  __TEXT.__const: 0x30240
-  __TEXT.__cstring: 0x2824c
+  __TEXT.__const: 0x30270
+  __TEXT.__cstring: 0x28426
   __TEXT.__objc_classname: 0x35e3
-  __TEXT.__objc_methname: 0xd436
+  __TEXT.__objc_methname: 0xd546
   __TEXT.__objc_methtype: 0x47db
-  __TEXT.__swift5_typeref: 0xb9d0
-  __TEXT.__swift5_fieldmd: 0xdea0
-  __TEXT.__constg_swiftt: 0xd6fc
+  __TEXT.__swift5_typeref: 0xba0c
+  __TEXT.__swift5_fieldmd: 0xdeac
+  __TEXT.__constg_swiftt: 0xd70c
   __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_reflstr: 0xba1e
+  __TEXT.__swift5_reflstr: 0xba3e
   __TEXT.__swift5_assocty: 0xbc8
   __TEXT.__swift5_protos: 0x1b8
   __TEXT.__swift5_proto: 0x1d70
   __TEXT.__swift5_types: 0xbe4
-  __TEXT.__oslogstring: 0x29545
-  __TEXT.__swift5_capture: 0x56a4
+  __TEXT.__oslogstring: 0x29681
+  __TEXT.__swift5_capture: 0x5708
   __TEXT.__swift5_mpenum: 0x98
-  __TEXT.__swift_as_entry: 0x118c
-  __TEXT.__swift_as_ret: 0x19e0
+  __TEXT.__swift_as_entry: 0x1194
+  __TEXT.__swift_as_ret: 0x1a0c
   __TEXT.__swift5_acfuncs: 0x64
   __TEXT.__swift5_entry: 0x8
   __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__unwind_info: 0x14f78
-  __TEXT.__eh_frame: 0x42378
-  __DATA_CONST.__auth_got: 0x63e8
-  __DATA_CONST.__got: 0x3f80
-  __DATA_CONST.__auth_ptr: 0x2250
-  __DATA_CONST.__const: 0x21420
+  __TEXT.__unwind_info: 0x15020
+  __TEXT.__eh_frame: 0x428c0
+  __DATA_CONST.__auth_got: 0x6410
+  __DATA_CONST.__got: 0x3fb0
+  __DATA_CONST.__auth_ptr: 0x2258
+  __DATA_CONST.__const: 0x21540
   __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x708
   __DATA_CONST.__objc_protolist: 0x228

   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__linkguard: 0xe
-  __DATA.__objc_const: 0x10cc0
-  __DATA.__objc_selrefs: 0x2460
+  __DATA.__objc_const: 0x10ce0
+  __DATA.__objc_selrefs: 0x24b8
   __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0x39a8
-  __DATA.__data: 0x178f0
+  __DATA.__data: 0x17910
   __DATA.__bss: 0x37230
-  __DATA.__common: 0x74a
+  __DATA.__common: 0x752
+  - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F6E7272C-3618-304C-B6ED-5E59C31FA658
-  Functions: 17820
-  Symbols:   5667
-  CStrings:  8160
+  UUID: 7D5C8FB9-4557-3593-AF7A-DBF7786BADF9
+  Functions: 17875
+  Symbols:   5677
+  CStrings:  8183
 
Symbols:
+ _$s13CoreIDVShared16IdentityDocumentC16encryptedNFCData10Foundation4DataVSgvg
+ _$s13CoreIDVShared18AlertConfigurationV5title7message18defaultButtonTitle09alternatehI0ACSS_S3SSgtcfC
+ _$s13TapToRadarKit0abC7ServiceC11createDraft_11processName13displayReasonySo0cG0C_SSSgAItKF
+ _$s13TapToRadarKit0abC7ServiceC6sharedACvgZ
+ _$s13TapToRadarKit0abC7ServiceCMa
+ _$s13TapToRadarKit0abC7ServiceCMn
+ _$s13TapToRadarKit0abC7ServiceCMo
+ _$s13TapToRadarKit0abC7ServiceCN
+ _OBJC_CLASS_$_RadarComponent
+ _OBJC_CLASS_$_RadarDraft
CStrings:
+ "Allow CoreIDV To Collect Privacy Sensitive Logs"
+ "Calculated hash and stored hash mismatch. Uploaded PII data with proofingSessionID: "
+ "Collected logs includes name, date of birth, date of expiry, portrait, nationality, documentNumber and will be retained for up to 30 days."
+ "Failed to draft Tap-to-Radar: %@"
+ "Failed to show TTR alert error: %@"
+ "Failed to show TTR alert unable to find proofing session id"
+ "Second edition request without deviceRequestInfo must have exactly one doc request"
+ "[Cransport] PII Hash Mismatch"
+ "a consistency check failed"
+ "encryptedCredentialPII"
+ "encryptedNFCData"
+ "initWithName:version:identifier:"
+ "received an error while updating the encrypted nfc data"
+ "setAutoDiagnostics:"
+ "setClassification:"
+ "setComponent:"
+ "setEncryptedNFCData:"
+ "setProblemDescription:"
+ "setReproducibility:"
+ "setTimeOfIssue:"
+ "updateEncryptedNFCData(proofingSessionID:encryptedNFCData:)"
+ "uploadEncryptedIntegrityCheckDataForIdentifier:data:completion:"
- "Received a second edition request that does not contain use cases"

```
