## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-416.475.12.0.0
-  __TEXT.__text: 0x51bb8
+416.575.3.0.0
+  __TEXT.__text: 0x51edc
   __TEXT.__auth_stubs: 0x1020
-  __TEXT.__objc_methlist: 0x39e4
+  __TEXT.__objc_methlist: 0x39ec
   __TEXT.__const: 0x139c
   __TEXT.__gcc_except_tab: 0x131c
-  __TEXT.__oslogstring: 0x9085
-  __TEXT.__cstring: 0x60f1
+  __TEXT.__oslogstring: 0x919a
+  __TEXT.__cstring: 0x6111
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x1688
+  __TEXT.__unwind_info: 0x1680
   __TEXT.__objc_classname: 0x71d
-  __TEXT.__objc_methname: 0x9156
-  __TEXT.__objc_methtype: 0x1bde
+  __TEXT.__objc_methname: 0x917c
+  __TEXT.__objc_methtype: 0x1c0f
   __TEXT.__objc_stubs: 0x4f60
   __DATA_CONST.__got: 0x4e0
-  __DATA_CONST.__const: 0x2f90
+  __DATA_CONST.__const: 0x2f98
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2180
+  __DATA_CONST.__objc_selrefs: 0x2188
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0x820
   __AUTH_CONST.__const: 0x610
-  __AUTH_CONST.__cfstring: 0x3bc0
+  __AUTH_CONST.__cfstring: 0x3c00
   __AUTH_CONST.__objc_const: 0x8778
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 599FAFA4-1602-38F7-95DD-71E0D9D1695E
-  Functions: 2341
-  Symbols:   7838
-  CStrings:  3802
+  UUID: A6FA851B-0F0F-3C32-91B3-46A3C4308920
+  Functions: 2346
+  Symbols:   7849
+  CStrings:  3812
 
Symbols:
+ +[CDPFollowUpContext contextForCDPPDPStateRepair]
+ +[CDPFollowUpContext contextForCDPPDPStateRepair].cold.1
+ -[CDPContext isPDPStateEligible].cold.2
+ -[CDPContext isPDPStateEligible].cold.3
+ -[CDPContext pdpHealth].cold.1
+ _CDP_FOLLOWUP_CDP_PDP_REPAIR
+ ___66-[CDPStateController startSilentEscrowRecordRepairWithCompletion:]_block_invoke.82
+ ___66-[CDPStateController validatePDPIdentitiesWithContext:completion:]_block_invoke.88
+ ___66-[CDPStateController validatePDPIdentitiesWithContext:completion:]_block_invoke.88.cold.1
+ ___67-[CDPStateController createPDPLivenessDictionaryWithContext:error:]_block_invoke.90
+ ___68-[CDPStateController performSilentEscrowRecordRepairWithCompletion:]_block_invoke.83
+ ___74-[CDPStateController updateLastSilentEscrowRecordRepairAttemptDate:error:]_block_invoke.84
+ ___76-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:error:]_block_invoke.80
+ ___81-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:completion:]_block_invoke.81
+ ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.92
+ ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.92.cold.1
+ ___block_descriptor_48_e8_32bs40r_e28_v24?0"NSData"8"NSError"16lr40l8s32l8
+ ___block_literal_global.86
+ _objc_msgSend$isPDPEligibleForAccount:
- ___66-[CDPStateController startSilentEscrowRecordRepairWithCompletion:]_block_invoke.81
- ___66-[CDPStateController validatePDPIdentitiesWithContext:completion:]_block_invoke.87
- ___66-[CDPStateController validatePDPIdentitiesWithContext:completion:]_block_invoke.87.cold.1
- ___67-[CDPStateController createPDPLivenessDictionaryWithContext:error:]_block_invoke.89
- ___68-[CDPStateController performSilentEscrowRecordRepairWithCompletion:]_block_invoke.82
- ___74-[CDPStateController updateLastSilentEscrowRecordRepairAttemptDate:error:]_block_invoke.83
- ___76-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:error:]_block_invoke.79
- ___81-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:completion:]_block_invoke.80
- ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.91
- ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.91.cold.1
- ___block_descriptor_48_e8_32bs40r_e30_v24?0"NSString"8"NSError"16lr40l8s32l8
- ___block_literal_global.85
- _objc_msgSend$base64Encoding
CStrings:
+ "%s: Rejecting out-of-range PDP state (%lu), treating as Unknown."
+ "CDPContext: Missing altDSID in pdpHealth, treating as unhealthy"
+ "CDPContext: Missing altDSID, treating as ineligible"
+ "CDPContext: PDP eligibility check: isEligible=%{BOOL}d"
+ "CDPContext: Unable to get authKit account for altDSID, treating as ineligible"
+ "Creating tombstone context for stale CDP+PDP repair CFU (rdar://171113289)"
+ "contextForCDPPDPStateRepair"
+ "isPDPEligibleForAccount:"
+ "kCDPPDPStateRepair"
+ "v32@0:8@\"CDPContext\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "%s: Rejecting out-of-range PDP state (%@)."
- "CDPContext: PDP eligibility check: pdpState=%ld, isEligible=%{BOOL}d"
- "base64Encoding"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSString\"@\"NSError\">24"

```
