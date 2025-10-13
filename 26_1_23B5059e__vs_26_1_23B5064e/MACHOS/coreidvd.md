## coreidvd

> `/usr/libexec/coreidvd`

```diff

-8.107.0.0.0
-  __TEXT.__text: 0x68f8b4
+8.108.0.0.0
+  __TEXT.__text: 0x693b10
   __TEXT.__auth_stubs: 0xc540
   __TEXT.__objc_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x1f3c
-  __TEXT.__const: 0x2c820
+  __TEXT.__objc_methlist: 0x1f44
+  __TEXT.__const: 0x2c890
   __TEXT.__objc_classname: 0x2e8
-  __TEXT.__objc_methname: 0x8c7e
-  __TEXT.__objc_methtype: 0x236b
-  __TEXT.__cstring: 0x3126c
-  __TEXT.__swift5_typeref: 0xbacc
-  __TEXT.__swift5_fieldmd: 0xde60
-  __TEXT.__constg_swiftt: 0xd6ec
+  __TEXT.__objc_methname: 0x8cce
+  __TEXT.__objc_methtype: 0x23b7
+  __TEXT.__cstring: 0x3144c
+  __TEXT.__swift5_typeref: 0xbaf2
+  __TEXT.__swift5_fieldmd: 0xded0
+  __TEXT.__constg_swiftt: 0xd710
   __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_reflstr: 0xb91d
+  __TEXT.__swift5_reflstr: 0xb98d
   __TEXT.__swift5_assocty: 0xbf8
   __TEXT.__swift5_protos: 0x1b4
   __TEXT.__swift5_proto: 0x1d90
   __TEXT.__swift5_types: 0xbf8
-  __TEXT.__oslogstring: 0x29335
-  __TEXT.__swift5_capture: 0x5750
+  __TEXT.__oslogstring: 0x293e5
+  __TEXT.__swift5_capture: 0x5758
   __TEXT.__swift5_mpenum: 0x90
-  __TEXT.__swift_as_entry: 0x1128
-  __TEXT.__swift_as_ret: 0x1978
+  __TEXT.__swift_as_entry: 0x1134
+  __TEXT.__swift_as_ret: 0x19b4
   __TEXT.__swift5_acfuncs: 0x64
   __TEXT.__swift5_entry: 0x8
   __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__unwind_info: 0x14ed0
-  __TEXT.__eh_frame: 0x42460
+  __TEXT.__unwind_info: 0x14f70
+  __TEXT.__eh_frame: 0x42898
   __DATA_CONST.__auth_got: 0x62b0
-  __DATA_CONST.__got: 0x3d78
-  __DATA_CONST.__auth_ptr: 0x21f8
-  __DATA_CONST.__const: 0x215f8
+  __DATA_CONST.__got: 0x3d88
+  __DATA_CONST.__auth_ptr: 0x2200
+  __DATA_CONST.__const: 0x21658
   __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x708
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x10cc8
-  __DATA.__objc_selrefs: 0x2450
+  __DATA.__objc_const: 0x10cd0
+  __DATA.__objc_selrefs: 0x2468
   __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0x39b8
-  __DATA.__data: 0x17c08
+  __DATA.__data: 0x17c18
   __DATA.__bss: 0x376b0
   __DATA.__common: 0x748
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 051F8449-7EE8-3BA7-AA2C-99713C469169
-  Functions: 17956
-  Symbols:   5546
-  CStrings:  8117
+  UUID: C09C113D-D1BA-3DB8-9BA1-6F4061D46C7E
+  Functions: 17993
+  Symbols:   5549
+  CStrings:  8128
 
Symbols:
+ _$s13CoreIDVShared25IdentityProofingNFCConfigC24minimumReadTimeThreshold17readRetryInterval17readyCheckEnabled015isChipIntegrityN15FailureTerminalACSiSg_AHSbSgAItcfc
+ _$s13CoreIDVShared25IdentityProofingNFCConfigCMn
+ _$s13CoreIDVShared8DIPErrorV4CodeO30failedToMakeActionNotificationyA2EmFWC
+ _$s13CoreIDVShared8DIPErrorV4CodeO34failedToDeletePIITokenNoIdentifieryA2EmFWC
- _$s13CoreIDVShared25IdentityProofingNFCConfigC24minimumReadTimeThreshold17readRetryInterval17readyCheckEnabledACSiSg_AGSbSgtcfc
CStrings:
+ "Failed to make actioin notification request"
+ "Failed to notify server provisioningComplete: %@"
+ "No credentialID for proofing session with proofingSessionID: %s"
+ "Provisioning has failed with error: %s"
+ "Unable to delete PII token no proofingSessionID/ piiTokenIdentifier available"
+ "globalAuthACLInfo"
+ "globalAuthACLInfo()"
+ "globalAuthACLInfoWithCompletionHandler:"
+ "isChipIntegrityCheckFailureTerminal"
+ "notifyProvisionComplete - documentTypeString doesn't exist to derive the documentType"
+ "notifyProvisionComplete(credentialIdentifier:status:)"
+ "provisioningFailureReasons"
+ "service:account:inviteDroppedForSessionID:fromID:error:"
+ "unable to notify provisioning completion, identity target doesn't exist"
+ "v24@0:8@?<v@?@\"NSArray\"qq@\"NSError\">16"
+ "v40@?0@\"NSArray\"8q16q24@\"NSError\"32"
+ "v48@0:8@\"_TtC13CoreIDVShared29IdentityProofingConfiguration\"16@\"_TtC13CoreIDVShared25IdentityProofingDocuments\"24@\"NSString\"32@?<v@?@\"_TtC13CoreIDVShared25IdentityProofingNFCConfig\"@\"NSError\">40"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"
- "Identity target doesn't exist"
- "Provisioning has failed"
- "documentTypeString doesn't exist to derive the documentType"
- "globalAuthACLTemplateUUIDs"
- "globalAuthACLTemplateUUIDs()"
- "globalAuthACLTemplateUUIDsWithCompletionHandler:"
- "notifyProvisionComplete(credentialIdentifier:)"
- "v24@0:8@?<v@?@\"NSArray\"q@\"NSError\">16"
- "v32@?0@\"NSArray\"8q16@\"NSError\"24"

```
