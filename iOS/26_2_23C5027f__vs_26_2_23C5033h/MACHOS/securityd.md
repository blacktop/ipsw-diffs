## securityd

> `/usr/libexec/securityd`

```diff

-61901.60.29.0.0
-  __TEXT.__text: 0x25cd6c
+61901.60.37.0.0
+  __TEXT.__text: 0x25df00
   __TEXT.__auth_stubs: 0x42b0
-  __TEXT.__objc_stubs: 0x1c800
-  __TEXT.__objc_methlist: 0x15368
+  __TEXT.__objc_stubs: 0x1c900
+  __TEXT.__objc_methlist: 0x153f8
   __TEXT.__const: 0x919
-  __TEXT.__objc_methname: 0x2c6d3
-  __TEXT.__cstring: 0x21130
-  __TEXT.__oslogstring: 0x2d547
+  __TEXT.__objc_methname: 0x2c8c7
+  __TEXT.__cstring: 0x211b8
+  __TEXT.__oslogstring: 0x2d61c
   __TEXT.__swift5_typeref: 0x37a
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__constg_swiftt: 0x274

   __TEXT.__swift5_types: 0x20
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__gcc_except_tab: 0xb654
-  __TEXT.__objc_classname: 0x238d
-  __TEXT.__objc_methtype: 0xa5b6
+  __TEXT.__gcc_except_tab: 0xb698
+  __TEXT.__objc_classname: 0x2394
+  __TEXT.__objc_methtype: 0xa5fc
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x67e8
+  __TEXT.__unwind_info: 0x6800
   __TEXT.__eh_frame: 0xa58
   __DATA_CONST.__auth_got: 0x2168
   __DATA_CONST.__got: 0x1360
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x141d0
-  __DATA_CONST.__cfstring: 0x1b520
+  __DATA_CONST.__const: 0x141f8
+  __DATA_CONST.__cfstring: 0x1b5c0
   __DATA_CONST.__objc_classlist: 0x8c0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x250

   __DATA_CONST.__objc_arraydata: 0x3f8
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA.__objc_const: 0x22a38
-  __DATA.__objc_selrefs: 0x9378
-  __DATA.__objc_ivar: 0x1a10
+  __DATA.__objc_const: 0x22b50
+  __DATA.__objc_selrefs: 0x93b8
+  __DATA.__objc_ivar: 0x1a28
   __DATA.__objc_data: 0x5a78
   __DATA.__data: 0x2380
   __DATA.__thread_vars: 0xc0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D77E6C6B-77DF-31A3-A49E-D0BFAA571EC9
-  Functions: 9639
+  UUID: 924A9284-8832-3E02-9738-FCF3DBA1D8FA
+  Functions: 9652
   Symbols:   1778
-  CStrings:  19634
+  CStrings:  19666
 
CStrings:
+ "-[CuttlefishXPCWrapper requestEscrowCheckWithSpecificUser:requiresEscrowCheck:passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:rateLimit:reply:]_block_invoke"
+ "@80@0:8@16@24@32@40q48@56@64@72"
+ "B56@0:8@16@24@32^q40^@48"
+ "B64@0:8@16@24^@32^@40^@48^@56"
+ "Failed to fetch escrow content"
+ "Failed to get escrow contents: %@"
+ "Received bottle entropy for ID %@"
+ "SecureBackupNetworkReachedHint"
+ "Successfully enabled backup"
+ "T@\"NSData\",C,N,V_entropy"
+ "T@\"NSData\",C,N,V_escrowSigningSPKI"
+ "T@\"NSString\",C,N,V_bottleID"
+ "Tq,V_daysLeftOnRateLimit"
+ "_daysLeftOnRateLimit"
+ "_escrowSigningSPKI"
+ "daysLeftOnRateLimit"
+ "device reached the network: %@"
+ "enableAndReturnNetworkReachedHint:"
+ "enableWithPasscodeStashSecret:existingRecord:account:reachedNetwork:error:"
+ "enableWithSecureBackupAndReturnHint:error:"
+ "escrowSigningPublicKey"
+ "escrowSigningSPKI"
+ "failed to reach network"
+ "fetchEscrowContentWithActiveAccount:cuttlefishXPCWrapper:entropy:bottleID:escrowSigningSPKI:error:"
+ "initWithDependencies:intendedState:errorState:followupHandler:contextType:entropy:bottleID:escrowSigningSPKI:"
+ "octagon: failed to fetch escrow content, %@"
+ "rate limited, days left on rate limit %ld"
+ "reached network"
+ "reached network unknown"
+ "requestEscrowCheckWithSpecificUser:requiresEscrowCheck:passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:rateLimit:reply:"
+ "setEscrowSigningPublicKey:"
+ "setEscrowSigningSPKI:"
+ "v80@0:8@\"TPSpecificUser\"16B24Q28@\"NSArray\"36B44@\"NSString\"48@\"NSString\"56q64@?<v@?@\"OTEscrowCheckCallResult\"@\"NSError\">72"
+ "v80@0:8@16B24Q28@36B44@48@56q64@?72"
- "-[CuttlefishXPCWrapper requestEscrowCheckWithSpecificUser:requiresEscrowCheck:passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:reply:]_block_invoke"
- "@56@0:8@16@24@32@40q48"
- "enableWithPasscodeStashSecret:existingRecord:account:error:"
- "initWithDependencies:intendedState:errorState:followupHandler:contextType:"
- "requestEscrowCheckWithSpecificUser:requiresEscrowCheck:passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:reply:"
- "v72@0:8@\"TPSpecificUser\"16B24Q28@\"NSArray\"36B44@\"NSString\"48@\"NSString\"56@?<v@?@\"OTEscrowCheckCallResult\"@\"NSError\">64"
- "v72@0:8@16B24Q28@36B44@48@56@?64"

```
