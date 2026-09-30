## idcredd

> `/usr/libexec/idcredd`

```diff

-8.104.2.0.0
-  __TEXT.__text: 0x19b7bc
-  __TEXT.__auth_stubs: 0x3d70
+8.107.0.0.0
+  __TEXT.__text: 0x19e2c0
+  __TEXT.__auth_stubs: 0x3d90
   __TEXT.__objc_methlist: 0x8fc
   __TEXT.__const: 0x4730
-  __TEXT.__cstring: 0xe8f9
+  __TEXT.__cstring: 0xeae9
   __TEXT.__constg_swiftt: 0x21e0
-  __TEXT.__swift5_typeref: 0x263c
-  __TEXT.__swift5_reflstr: 0x16d7
-  __TEXT.__swift5_fieldmd: 0x1618
+  __TEXT.__swift5_typeref: 0x2634
+  __TEXT.__swift5_reflstr: 0x16f7
+  __TEXT.__swift5_fieldmd: 0x1624
   __TEXT.__swift5_builtin: 0x1b8
   __TEXT.__swift5_assocty: 0x1c8
   __TEXT.__swift5_capture: 0x1f80
-  __TEXT.__objc_methname: 0x274c
-  __TEXT.__oslogstring: 0xa428
+  __TEXT.__objc_methname: 0x2784
+  __TEXT.__oslogstring: 0xa658
   __TEXT.__swift5_proto: 0x144
   __TEXT.__swift5_types: 0x1dc
   __TEXT.__objc_classname: 0x7f
   __TEXT.__objc_methtype: 0xb81
-  __TEXT.__swift_as_entry: 0x5fc
-  __TEXT.__swift_as_ret: 0x710
+  __TEXT.__swift_as_entry: 0x600
+  __TEXT.__swift_as_ret: 0x714
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x51e0
-  __TEXT.__eh_frame: 0x133b0
-  __DATA_CONST.__auth_got: 0x1eb8
-  __DATA_CONST.__got: 0x1520
-  __DATA_CONST.__auth_ptr: 0x9c8
+  __TEXT.__unwind_info: 0x5208
+  __TEXT.__eh_frame: 0x134d8
+  __DATA_CONST.__auth_got: 0x1ec8
+  __DATA_CONST.__got: 0x1540
+  __DATA_CONST.__auth_ptr: 0x9c0
   __DATA_CONST.__const: 0x5a30
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__linkguard: 0x15
   __DATA.__objc_const: 0x27e0
-  __DATA.__objc_selrefs: 0xae8
+  __DATA.__objc_selrefs: 0xaf8
   __DATA.__objc_data: 0xcc8
-  __DATA.__data: 0x3fd8
+  __DATA.__data: 0x3fd0
   __DATA.__bss: 0x1cd0
   __DATA.__common: 0xf0
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B5F546F4-D482-306D-8FDD-5B31746FDC46
-  Functions: 3919
-  Symbols:   1802
-  CStrings:  2145
+  UUID: 7C73EFAD-00DB-3AA0-B456-C920D3C03004
+  Functions: 3926
+  Symbols:   1807
+  CStrings:  2161
 
Symbols:
+ _$s10Foundation14DateComponentsV4dateAA0B0VSgvg
+ _$s10Foundation4DataV13CoreIDVSharedE13base16EncodedACSgSS_tcfC
+ _$s13CoreIDVShared10AnyCodableO14birthDateValueAA8ISO23220O05BirthF0VSgvg
+ _$s13CoreIDVShared22PassportPIIHashUtilityV17generatePIIHashes8portrait6holder3dob3doe11nationality9docNumberSDyS2SGSS_S5StKFZ
+ _$s13CoreIDVShared8DIPErrorV4CodeO047deviceCrossCheckFailedHashMismatchForFieldBasedI0yA2EmFWC
+ _$s13CoreIDVShared8DIPErrorV4CodeO049deviceCrossCheckFailedToGenerateHashForFieldBasedK0yA2EmFWC
+ _$s13CoreIDVShared8DIPErrorV4CodeO22incorrectPIIHashFormatyA2EmFWC
+ _$s13CoreIDVShared8DIPErrorV4CodeO41deviceCrossCheckFailedCalculatedHashEmptyyA2EmFWC
- _$s13CoreIDVShared10AnyCodableO9dictValueAA0cD10DictionaryVSgvg
- _$s13CoreIDVShared20AnyCodableDictionaryV5valueSDySSAA0cD0OGvg
- _$s13CoreIDVShared20AnyCodableDictionaryVMn
CStrings:
+ "Concatenated hash comparison failed - failed to generate hash"
+ "Concatenated hash comparison failed - hash mismatch"
+ "CredentialStorage - Calculated PII Hash for %s is: %s"
+ "CredentialStore storePIITokenCredentialList called for credentialIdentifier %{public}s"
+ "Deleting credential with ID: %{public}s from credential identifier list"
+ "Failed to perform field based hash comparison performing concatenated hash comparison: %@"
+ "Field based hash comparison failed - calculated hash is empty"
+ "Field based hash comparison failed - failed to generate hash"
+ "Field based hash comparison failed - hash mismatch"
+ "PII hash is incorrectly formatted"
+ "Storing updated credental list: %{public}s"
+ "Token Credential list not empty, updating list with new list: %{public}s"
+ "Token credential list is empty attempting to clean token"
+ "decodePayload(payloadProcessorBuilder:encryptedPayload:format:decryptionKeyInfo:credentialIdentifier:context:)"
+ "isPIIHashMismatchTerminal"
+ "performConcatenatedHashComparison"
+ "performConcatenatedHashComparison(storedHashString:portrait:name:dob:doe:nationality:docNumber:)"
+ "performDeviceCrossCheck(of:credentialIdentifier:isPIIHashMismatchTerminal:)"
+ "performFieldBasedHashComparison"
+ "performFieldBasedHashComparison(storedHashString:portrait:name:dob:doe:nationality:docNumber:)"
+ "setIsPIIHashMismatchTerminal:"
- "CredentialStore storePIITokenCredentialList"
- "Device cross check - failed to generate hash"
- "Device cross check failed - hash mismatch"
- "decodePayload(payloadProcessorBuilder:encryptedPayload:format:decryptionKeyInfo:credentialIdentifier:)"
- "performDeviceCrossCheck(of:credentialIdentifier:)"

```
