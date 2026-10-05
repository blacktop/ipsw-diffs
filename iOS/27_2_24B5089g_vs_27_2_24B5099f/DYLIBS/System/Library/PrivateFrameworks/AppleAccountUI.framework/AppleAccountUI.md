## AppleAccountUI

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI`

```diff

-589.125.4.0.0
-  __TEXT.__text: 0x3883fc
+589.125.7.0.0
+  __TEXT.__text: 0x38876c
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0x2d0
-  __TEXT.__objc_methlist: 0xc3cc
+  __TEXT.__objc_methlist: 0xc3d4
   __TEXT.__cstring: 0xbb61
-  __TEXT.__const: 0x143a4
+  __TEXT.__const: 0x143b4
   __TEXT.__gcc_except_tab: 0x14f4
-  __TEXT.__oslogstring: 0x1205c
+  __TEXT.__oslogstring: 0x1209c
   __TEXT.__dlopen_cstrs: 0x582
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x156ea
+  __TEXT.__swift5_typeref: 0x156fa
   __TEXT.__swift5_capture: 0x6560
   __TEXT.__swift5_reflstr: 0x40e6
   __TEXT.__swift5_assocty: 0x1308

   __TEXT.__swift_as_cont: 0x460
   __TEXT.__swift5_protos: 0x58
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x10e30
+  __TEXT.__unwind_info: 0x10e20
   __TEXT.__eh_frame: 0x3248
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3658
+  __DATA_CONST.__const: 0x3680
   __DATA_CONST.__objc_classlist: 0x928
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x3d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7050
+  __DATA_CONST.__objc_selrefs: 0x7070
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x498
   __DATA_CONST.__objc_arraydata: 0xd0
-  __DATA_CONST.__got: 0x1e48
+  __DATA_CONST.__got: 0x1e50
   __AUTH_CONST.__const: 0x14f48
   __AUTH_CONST.__cfstring: 0x5260
   __AUTH_CONST.__objc_const: 0x43fe8

   __AUTH.__objc_data: 0x80c8
   __AUTH.__data: 0x5048
   __DATA.__objc_ivar: 0xce4
-  __DATA.__data: 0x7620
+  __DATA.__data: 0x7630
   __DATA.__common: 0x5e0
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x48

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17531
-  Symbols:   10522
-  CStrings:  2872
+  Functions: 17528
+  Symbols:   10525
+  CStrings:  2873
 
Symbols:
+ -[AAUISignOutUtilities _signoutFromAuthKitForAltDSID:telemetryFlowID:completion:]
+ -[AAUISignOutUtilities signOutServiceAccountsWithServiceOwnersManager:forAltDSID:DSID:telemetryFlowID:context:completion:]
+ _OBJC_CLASS_$_AKSignoutInfo
+ ___122-[AAUISignOutUtilities signOutServiceAccountsWithServiceOwnersManager:forAltDSID:DSID:telemetryFlowID:context:completion:]_block_invoke
+ ___81-[AAUISignOutUtilities _signoutFromAuthKitForAltDSID:telemetryFlowID:completion:]_block_invoke
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ _get_witness_table 7SwiftUI15ModifiedContentVy012AppleAccountB028AddRecoveryContactControllerVAA30_SafeAreaRegionsIgnoringLayoutVGAA4ViewHPAfaJHPyHC_AhA0P8ModifierHPyHCHC
+ _symbolic _____y__________G 7SwiftUI15ModifiedContentV 012AppleAccountB028AddRecoveryContactControllerV AA30_SafeAreaRegionsIgnoringLayoutV
- -[AAUISignOutUtilities _signoutFromAuthKitForAltDSID:completion:]
- -[AAUISignOutUtilities signOutServiceAccountsWithServiceOwnersManager:forAltDSID:DSID:context:completion:]
- ___106-[AAUISignOutUtilities signOutServiceAccountsWithServiceOwnersManager:forAltDSID:DSID:context:completion:]_block_invoke
- ___65-[AAUISignOutUtilities _signoutFromAuthKitForAltDSID:completion:]_block_invoke
- _get_witness_table 14AppleAccountUI28AddRecoveryContactControllerV05SwiftC04ViewHPyHC
CStrings:
+ "Fetching avatar from primary source"
+ "Got avatar from primary source"
+ "No avatar from primary source"
+ "No avatar from primary source, falling back to monogram"
+ "Skipping profile picture update, managed by primary source"
- "Got avatar from IdentityStore"
- "No avatar from IdentityStore"
- "No avatar from IdentityStore, falling back to monogram"
- "Using IdentityStore to fetch avatar"
```
