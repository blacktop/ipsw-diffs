## RemotePairingDevice

> `/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice`

```diff

-199.100.20.0.0
-  __TEXT.__text: 0xcbbec
-  __TEXT.__auth_stubs: 0x2b40
-  __TEXT.__objc_methlist: 0x4ac
-  __TEXT.__const: 0xed08
-  __TEXT.__cstring: 0x6a3c
-  __TEXT.__oslogstring: 0x3bcc
+199.120.5.0.0
+  __TEXT.__text: 0xccf2c
+  __TEXT.__auth_stubs: 0x2b60
+  __TEXT.__objc_methlist: 0x4bc
+  __TEXT.__const: 0xeef8
+  __TEXT.__cstring: 0x6b3c
+  __TEXT.__oslogstring: 0x3cbc
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__constg_swiftt: 0x3abc
-  __TEXT.__swift5_typeref: 0x3856
-  __TEXT.__swift5_reflstr: 0x2960
-  __TEXT.__swift5_fieldmd: 0x343c
+  __TEXT.__constg_swiftt: 0x3b18
+  __TEXT.__swift5_typeref: 0x389e
+  __TEXT.__swift5_reflstr: 0x29f0
+  __TEXT.__swift5_fieldmd: 0x34c0
   __TEXT.__swift5_builtin: 0x21c
-  __TEXT.__swift5_assocty: 0x258
-  __TEXT.__swift5_proto: 0xaf8
-  __TEXT.__swift5_types: 0x400
-  __TEXT.__swift5_capture: 0x1c1c
+  __TEXT.__swift5_assocty: 0x270
+  __TEXT.__swift5_proto: 0xb14
+  __TEXT.__swift5_types: 0x40c
+  __TEXT.__swift5_capture: 0x1c28
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x188
-  __TEXT.__unwind_info: 0x3fa0
+  __TEXT.__unwind_info: 0x3ff0
   __TEXT.__eh_frame: 0x37f0
   __TEXT.__objc_classname: 0x13c
-  __TEXT.__objc_methname: 0xb60
+  __TEXT.__objc_methname: 0xbb4
   __TEXT.__objc_methtype: 0x127
-  __TEXT.__objc_stubs: 0x260
+  __TEXT.__objc_stubs: 0x2c0
   __DATA_CONST.__got: 0x6f8
-  __DATA_CONST.__const: 0x7f8
+  __DATA_CONST.__const: 0x800
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x448
+  __DATA_CONST.__objc_selrefs: 0x460
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x15b0
+  __AUTH_CONST.__auth_got: 0x15c0
   __AUTH_CONST.__auth_ptr: 0x8e8
-  __AUTH_CONST.__const: 0xb238
-  __AUTH_CONST.__cfstring: 0x180
+  __AUTH_CONST.__const: 0xb3e8
+  __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x46e0
   __AUTH.__objc_data: 0x590
-  __AUTH.__data: 0x1a98
+  __AUTH.__data: 0x1a88
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x2748
-  __DATA.__bss: 0xd890
+  __DATA.__data: 0x27a8
+  __DATA.__bss: 0xdb90
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x290
   __DATA_DIRTY.__data: 0x1ad8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7578
-  Symbols:   1964
-  CStrings:  1062
+  Functions: 7625
+  Symbols:   1976
+  CStrings:  1073
 
Symbols:
+ _kRemotePairingOptPreserveAutomationPairRecords
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _remotepairing_delete_pair_records_with_options
CStrings:
+ "%{public}s: Out-of-band PairSetup handler accepted ownership of pairing attempt"
+ "%{public}s: Out-of-band PairSetup handler declined ownership of pairing attempt. Will handle attempt using standard pairing flow"
+ "%{public}s: Will attempt to use out-of-band PairSetup handler to complete pairing"
+ "Only unauthenticated connections can initiate pairing. Current state is "
+ "boolValue"
+ "createNewPairingsThroughLockdown"
+ "deleteNonAutomationPairingRecordsAndReturnError:"
+ "hostPairingViaLockdownPreference"
+ "never"
+ "nonAutomationHosts"
+ "objectForKeyedSubscript:"
+ "preserveAutomationPairRecords"
+ "upgradeExistingPairingsOnly"
- "%{public}s: Using configured out-of-band PairSetup handler to complete pairing"
- "hostPreferPairingViaLockdown"

```
