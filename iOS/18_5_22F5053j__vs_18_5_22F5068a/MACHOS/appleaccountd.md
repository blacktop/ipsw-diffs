## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-1007.476.0.0.0
-  __TEXT.__text: 0x30800c
+1007.477.0.0.0
+  __TEXT.__text: 0x30a508
   __TEXT.__auth_stubs: 0x2740
   __TEXT.__objc_methlist: 0xe10
   __TEXT.__objc_methname: 0x44e7
   __TEXT.__objc_classname: 0x20a
   __TEXT.__objc_methtype: 0x1525
-  __TEXT.__cstring: 0x8534
-  __TEXT.__swift5_typeref: 0x6135
+  __TEXT.__cstring: 0x8544
+  __TEXT.__swift5_typeref: 0x6133
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xc70c
-  __TEXT.__constg_swiftt: 0xa650
-  __TEXT.__swift5_reflstr: 0x5414
-  __TEXT.__swift5_fieldmd: 0x52d0
+  __TEXT.__const: 0xc87c
+  __TEXT.__constg_swiftt: 0xa6dc
+  __TEXT.__swift5_reflstr: 0x5434
+  __TEXT.__swift5_fieldmd: 0x537c
   __TEXT.__swift5_builtin: 0x1e0
-  __TEXT.__swift5_assocty: 0x698
-  __TEXT.__swift5_proto: 0x998
-  __TEXT.__swift5_types: 0x4dc
-  __TEXT.__oslogstring: 0x19006
+  __TEXT.__swift5_assocty: 0x6b0
+  __TEXT.__swift5_proto: 0x9ac
+  __TEXT.__swift5_types: 0x4e0
+  __TEXT.__oslogstring: 0x19556
   __TEXT.__swift_as_entry: 0x280
   __TEXT.__swift_as_ret: 0x328
   __TEXT.__swift5_protos: 0x1e0
-  __TEXT.__swift5_capture: 0x5810
+  __TEXT.__swift5_capture: 0x580c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5b78
-  __TEXT.__eh_frame: 0x9a10
+  __TEXT.__unwind_info: 0x5bb8
+  __TEXT.__eh_frame: 0x9bf8
   __DATA_CONST.__auth_got: 0x13a0
   __DATA_CONST.__got: 0xe80
-  __DATA_CONST.__auth_ptr: 0x1fa8
-  __DATA_CONST.__const: 0x10bf8
+  __DATA_CONST.__auth_ptr: 0x2150
+  __DATA_CONST.__const: 0x10c60
   __DATA_CONST.__objc_classlist: 0x500
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x187c0
+  __DATA.__objc_const: 0x18860
   __DATA.__objc_selrefs: 0x1400
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x2ba8
-  __DATA.__data: 0x10dc0
+  __DATA.__data: 0x10e70
   __DATA.__objc_stublist: 0x68
-  __DATA.__bss: 0xe800
-  __DATA.__common: 0x3b0
+  __DATA.__bss: 0xea80
+  __DATA.__common: 0x3d8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7996
+  Functions: 8011
   Symbols:   1280
-  CStrings:  3471
+  CStrings:  3487
 
CStrings:
+ "CustodianRecord found on the local disk, after fetching from cloud"
+ "CustodianRecord found on the local disk, no need to fetch from cloud"
+ "CustodianRecord not found on the local disk, Fetching the record from cloud"
+ "CustodianRecoveryInfoRecord found on the local disk, after fetching from cloud"
+ "CustodianRecoveryInfoRecord found on the local disk, no need to fetch from cloud"
+ "CustodianRecoveryInfoRecord not found on the local disk, fetching the record from cloud"
+ "CustodianshipInfoRecord found on the local disk, after fetching from cloud"
+ "CustodianshipInfoRecord found on the local disk, no need to fetch from cloud"
+ "CustodianshipInfoRecord not found on the local disk, Fetching the record from cloud"
+ "Error fetching CustodianRecord from the local disk, after fetching from cloud: %@"
+ "Error fetching CustodianRecoveryInfoRecord from the local disk, after fetching from cloud: %@"
+ "Error fetching CustodianshipInfoRecord from the local disk, after fetching from cloud: %@"
+ "Error occured fetching CustodianRecoveryInfoRecord from local disk %@"
+ "Fetching CustodianRecord from local disk"
+ "Fetching CustodianRecord from local disk after fetching from cloud"
+ "Fetching CustodianRecoveryInfoRecord from local disk"
+ "Fetching CustodianRecoveryInfoRecord from local disk after fetching from cloud"
+ "Fetching CustodianshipInfoRecord from local disk"
+ "Fetching CustodianshipInfoRecord from local disk after fetching from cloud"
+ "contextType"
+ "flow"
+ "process(_:originalStatus:postCFU:telemetryFlowID:flow:)"
+ "🚨 CustodianRecord still not found on the local disk, even after fetching from cloud"
+ "🚨 CustodianRecoveryInfoRecord not found on the local disk, even after fetching from cloud"
+ "🚨 CustodianshipInfoRecord found on the local disk, even after fetching from cloud"
- "Custodian record not found. Fetching the record from cloud."
- "CustodianshipInfo record not found. Fetching the record from cloud."
- "Error fetching recovery info from cloud %@"
- "Fetching custodian record from local disk"
- "Fetching custodian record from local disk after cloud pull"
- "Fetching custodianinfo record from local disk"
- "Fetching custodianinfo record from local disk after cloud pull"
- "Recovery Info record not found. Fetching the record from cloud."
- "process(_:originalStatus:postCFU:telemetryFlowID:)"

```
