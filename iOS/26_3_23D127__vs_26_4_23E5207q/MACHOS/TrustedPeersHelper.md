## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

-61901.80.25.0.0
-  __TEXT.__text: 0x2154cc
-  __TEXT.__auth_stubs: 0x1ff0
-  __TEXT.__objc_stubs: 0x2500
-  __TEXT.__objc_methlist: 0x276c
-  __TEXT.__const: 0xab00
-  __TEXT.__cstring: 0x18dbd
-  __TEXT.__objc_methname: 0x75c5
-  __TEXT.__oslogstring: 0xa7fa
+61901.100.267.0.2
+  __TEXT.__text: 0x2528a8
+  __TEXT.__auth_stubs: 0x1f90
+  __TEXT.__objc_stubs: 0x5aa0
+  __TEXT.__objc_methlist: 0x27fc
+  __TEXT.__const: 0xb300
+  __TEXT.__cstring: 0x1689b
+  __TEXT.__oslogstring: 0xac9a
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x3790
-  __TEXT.__swift5_typeref: 0x3838
-  __TEXT.__swift5_fieldmd: 0x27a4
-  __TEXT.__swift5_reflstr: 0x2377
+  __TEXT.__objc_classname: 0x142f
+  __TEXT.__objc_methname: 0x86b1
+  __TEXT.__objc_methtype: 0x246c
+  __TEXT.__constg_swiftt: 0x3998
+  __TEXT.__swift5_typeref: 0x39f6
+  __TEXT.__swift5_fieldmd: 0x291c
+  __TEXT.__swift5_reflstr: 0x2387
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x3f0
-  __TEXT.__swift5_proto: 0x8c8
-  __TEXT.__swift5_types: 0x290
-  __TEXT.__objc_classname: 0x42b
-  __TEXT.__objc_methtype: 0x21a8
+  __TEXT.__swift5_proto: 0x940
+  __TEXT.__swift5_types: 0x2ac
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_capture: 0x4458
   __TEXT.__gcc_except_tab: 0x160
+  __TEXT.__swift5_capture: 0x4708
   __TEXT.__dlopen_cstrs: 0x1c2
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x4ab8
-  __TEXT.__eh_frame: 0x7780
-  __DATA_CONST.__auth_got: 0x1008
-  __DATA_CONST.__got: 0x928
-  __DATA_CONST.__auth_ptr: 0x698
-  __DATA_CONST.__const: 0x131a8
-  __DATA_CONST.__cfstring: 0x1780
-  __DATA_CONST.__objc_classlist: 0x250
+  __TEXT.__unwind_info: 0x4cf0
+  __TEXT.__eh_frame: 0x7a70
+  __DATA_CONST.__auth_got: 0xfd8
+  __DATA_CONST.__got: 0x940
+  __DATA_CONST.__auth_ptr: 0x6c0
+  __DATA_CONST.__const: 0x13808
+  __DATA_CONST.__cfstring: 0x17c0
+  __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA.__objc_const: 0x6920
-  __DATA.__objc_selrefs: 0x1ce0
-  __DATA.__objc_ivar: 0x1e8
-  __DATA.__objc_data: 0x2a20
-  __DATA.__data: 0x7ab0
-  __DATA.__objc_stublist: 0x98
-  __DATA.__bss: 0x11598
-  __DATA.__common: 0x918
+  __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA.__objc_const: 0x6ac0
+  __DATA.__objc_selrefs: 0x1d18
+  __DATA.__objc_ivar: 0x1ec
+  __DATA.__objc_data: 0x2b20
+  __DATA.__data: 0x80a0
+  __DATA.__objc_stublist: 0xa8
+  __DATA.__bss: 0x12498
+  __DATA.__common: 0x9b0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 18CA4E65-C5FB-3AA6-829D-C5706957122F
-  Functions: 8126
-  Symbols:   512
-  CStrings:  3446
+  UUID: C853F852-F726-3294-AC79-F0CD5FD71EFB
+  Functions: 8452
+  Symbols:   509
+  CStrings:  3389
 
Symbols:
+ _OBJC_CLASS_$_OTSerializedPlistEscrowRecord
+ _OBJC_METACLASS_$__TtCO18TrustedPeersHelper13CuttlefishAPI21EnableWalrusOperation
+ _OBJC_METACLASS_$__TtCO18TrustedPeersHelper13CuttlefishAPI22DisableWalrusOperation
- _malloc
- _memset
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "<TPWalrusExtraArguments(isDBRv2:%@)>"
+ "BottleMO"
+ "ContainerMO"
+ "Could not attempt to enable walrus: %@"
+ "CustodianRecoveryKeyMO"
+ "DisableWalrus returned changes, but they can't be serialized"
+ "DisableWalrus returned changes: %{public}s"
+ "EnableWalrus returned changes, but they can't be serialized"
+ "EnableWalrus returned changes: %{public}s"
+ "EscrowClientMetadataMO"
+ "EscrowMetadataMO"
+ "EscrowRecordMO"
+ "MachineMO"
+ "PasscodeGen"
+ "PeerMO"
+ "PolicyMO"
+ "RecoveryVoucherMO"
+ "SetValueTransformer"
+ "TB,V_isDBRv2"
+ "TPWalrusExtraArguments"
+ "TrustedPeersHelper.DisableWalrusOperation"
+ "TrustedPeersHelper.EnableWalrusOperation"
+ "VoucherMO"
+ "_TtCO18TrustedPeersHelper13CuttlefishAPI21EnableWalrusOperation"
+ "_TtCO18TrustedPeersHelper13CuttlefishAPI22DisableWalrusOperation"
+ "_isDBRv2"
+ "blob"
+ "device indicates walrus is already disabled, aborting"
+ "device indicates walrus is already enabled, aborting"
+ "disableWalrus complete %{public}s"
+ "disableWalrus failed for %{public}s: %{public}s"
+ "disableWalrus failed: %{public}s"
+ "disableWalrus for %{public}s"
+ "disableWalrus handling failed: %{public}s"
+ "disableWalrus success"
+ "disableWalrus(_:completion:)"
+ "disableWalrus(preRecords:extraArgs:flowID:deviceSessionID:reply:)"
+ "disableWalrusWithSpecificUser:preRecords:extraArgs:flowID:deviceSessionID:reply:"
+ "enableWalrus complete %{public}s"
+ "enableWalrus failed for %{public}s: %{public}s"
+ "enableWalrus failed: %{public}s"
+ "enableWalrus for %{public}s"
+ "enableWalrus handling failed: %{public}s"
+ "enableWalrus success"
+ "enableWalrus(_:completion:)"
+ "enableWalrus(preRecords:extraArgs:flowID:deviceSessionID:reply:)"
+ "enableWalrusWithSpecificUser:preRecords:extraArgs:flowID:deviceSessionID:reply:"
+ "escrowRecords"
+ "fetch-after-walrus-state-change failed: %{public}s"
+ "fetch-after-walrus-state-change succeeded"
+ "no prepared identity, cannot disable walrus"
+ "no prepared identity, cannot enable walrus"
+ "setClock:"
+ "setIsDBRv2:"
+ "v64@0:8@\"TPSpecificUser\"16@\"NSArray\"24@\"TPWalrusExtraArguments\"32@\"NSString\"40@\"NSString\"48@?<v@?@\"NSError\">56"
+ "v64@0:8@16@24@32@40@48@?56"
+ "walrus state change succeeded, but more changes need fetching..."
- "escrow_proxy_error"

```
