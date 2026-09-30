## coreidvd

> `/usr/libexec/coreidvd`

```diff

-8.108.0.0.0
-  __TEXT.__text: 0x693b10
+8.109.0.0.0
+  __TEXT.__text: 0x6abf90
   __TEXT.__auth_stubs: 0xc540
   __TEXT.__objc_stubs: 0x6e0
   __TEXT.__objc_methlist: 0x1f44
-  __TEXT.__const: 0x2c890
+  __TEXT.__const: 0x2fe30
   __TEXT.__objc_classname: 0x2e8
-  __TEXT.__objc_methname: 0x8cce
-  __TEXT.__objc_methtype: 0x23b7
-  __TEXT.__cstring: 0x3144c
+  __TEXT.__objc_methname: 0x8cd6
+  __TEXT.__objc_methtype: 0x23c2
+  __TEXT.__cstring: 0x3148c
   __TEXT.__swift5_typeref: 0xbaf2
   __TEXT.__swift5_fieldmd: 0xded0
-  __TEXT.__constg_swiftt: 0xd710
+  __TEXT.__constg_swiftt: 0xd720
   __TEXT.__swift5_builtin: 0x2bc
   __TEXT.__swift5_reflstr: 0xb98d
   __TEXT.__swift5_assocty: 0xbf8
   __TEXT.__swift5_protos: 0x1b4
   __TEXT.__swift5_proto: 0x1d90
   __TEXT.__swift5_types: 0xbf8
-  __TEXT.__oslogstring: 0x293e5
-  __TEXT.__swift5_capture: 0x5758
+  __TEXT.__oslogstring: 0x29415
+  __TEXT.__swift5_capture: 0x57a4
   __TEXT.__swift5_mpenum: 0x90
-  __TEXT.__swift_as_entry: 0x1134
-  __TEXT.__swift_as_ret: 0x19b4
+  __TEXT.__swift_as_entry: 0x1138
+  __TEXT.__swift_as_ret: 0x19c4
   __TEXT.__swift5_acfuncs: 0x64
   __TEXT.__swift5_entry: 0x8
   __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__unwind_info: 0x14f70
-  __TEXT.__eh_frame: 0x42898
+  __TEXT.__unwind_info: 0x151a0
+  __TEXT.__eh_frame: 0x43058
   __DATA_CONST.__auth_got: 0x62b0
-  __DATA_CONST.__got: 0x3d88
+  __DATA_CONST.__got: 0x3d80
   __DATA_CONST.__auth_ptr: 0x2200
-  __DATA_CONST.__const: 0x21658
+  __DATA_CONST.__const: 0x21708
   __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x708
   __DATA_CONST.__objc_protolist: 0x228

   __DATA.__objc_const: 0x10cd0
   __DATA.__objc_selrefs: 0x2468
   __DATA.__objc_ivar: 0x3c
-  __DATA.__objc_data: 0x39b8
-  __DATA.__data: 0x17c18
+  __DATA.__objc_data: 0x39c0
+  __DATA.__data: 0x17c48
   __DATA.__bss: 0x376b0
   __DATA.__common: 0x748
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C09C113D-D1BA-3DB8-9BA1-6F4061D46C7E
-  Functions: 17993
-  Symbols:   5549
-  CStrings:  8128
+  UUID: C80A5B16-6F02-30C5-B647-512D387BF9ED
+  Functions: 18088
+  Symbols:   5550
+  CStrings:  8130
 
Symbols:
+ _$s13CoreIDVShared25IdentityProofingNFCConfigC24minimumReadTimeThreshold17readRetryInterval17readyCheckEnabled015isChipIntegrityN15FailureTerminal0p11DeviceCrossnO0ACSiSg_AISbSgA2Jtcfc
+ _$s13CoreIDVShared8DIPErrorV4CodeO70remoteSessionServiceUnavailableUnableToFetchProvisioningFailureReasonsyA2EmFWC
- _$s13CoreIDVShared25IdentityProofingNFCConfigC24minimumReadTimeThreshold17readRetryInterval17readyCheckEnabled015isChipIntegrityN15FailureTerminalACSiSg_AHSbSgAItcfc
CStrings:
+ "No provisioning failure reason fetched"
+ "No provisioning failure reason fetched with error: "
+ "notifyProvisionComplete(credentialIdentifier:status:target:)"
+ "remoteSessionService is nil unable to fetch provisioningFailureReasons"
+ "service:account:inviteDroppedForSessionID:fromID:context:error:"
+ "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSError\"56"
- "notifyProvisionComplete(credentialIdentifier:status:)"
- "service:account:inviteDroppedForSessionID:fromID:error:"
- "unable to notify provisioning completion, identity target doesn't exist"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"

```
