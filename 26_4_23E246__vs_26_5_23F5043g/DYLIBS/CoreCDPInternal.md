## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-416.475.12.0.0
-  __TEXT.__text: 0x95bc4
+416.575.3.0.0
+  __TEXT.__text: 0x95f3c
   __TEXT.__auth_stubs: 0x1160
-  __TEXT.__objc_methlist: 0x563c
+  __TEXT.__objc_methlist: 0x565c
   __TEXT.__const: 0x830
-  __TEXT.__oslogstring: 0x146fe
-  __TEXT.__cstring: 0xd5c5
+  __TEXT.__oslogstring: 0x1480e
+  __TEXT.__cstring: 0xd625
   __TEXT.__gcc_except_tab: 0xc70
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x385

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__unwind_info: 0x1f68
-  __TEXT.__eh_frame: 0x958
+  __TEXT.__eh_frame: 0x930
   __TEXT.__objc_classname: 0xdbd
-  __TEXT.__objc_methname: 0xf9ff
-  __TEXT.__objc_methtype: 0x2a77
-  __TEXT.__objc_stubs: 0xcc20
-  __DATA_CONST.__got: 0x1088
-  __DATA_CONST.__const: 0x2570
+  __TEXT.__objc_methname: 0xfa5f
+  __TEXT.__objc_methtype: 0x2aa7
+  __TEXT.__objc_stubs: 0xcc80
+  __DATA_CONST.__got: 0x1090
+  __DATA_CONST.__const: 0x2598
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38a8
+  __DATA_CONST.__objc_selrefs: 0x38c0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0xd8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 95EB0CAF-7DA7-3AFB-8D4E-60BA2C7F61F6
-  Functions: 3144
-  Symbols:   10373
-  CStrings:  6484
+  UUID: 106B9AE0-B406-3AFF-A154-B8DB55DB1334
+  Functions: 3150
+  Symbols:   10396
+  CStrings:  6495
 
Symbols:
+ -[CDPDAnalyticsTransport _deliverEvent:]
+ -[CDPDAnalyticsTransport _deliverEvent:].cold.1
+ -[CDPDAnalyticsTransport _deliverEvent:].cold.2
+ -[CDPDAnalyticsTransport _deliverEvent:].cold.3
+ -[CDPDAnalyticsTransport _enforcePrivacyComplianceIfRequired:]
+ -[CDPDPDPRecoveryController clearCDPPDPFollowUp]
+ -[CDPDPDPRecoveryController clearCDPPDPFollowUp].cold.1
+ -[CDPDPDPRecoveryController clearCDPPDPFollowUp].cold.2
+ GCC_except_table47
+ _CDP_FOLLOWUP_CDP_PDP_REPAIR
+ ___62-[CDPDAnalyticsTransport _enforcePrivacyComplianceIfRequired:]_block_invoke
+ ___70-[CDPDSecureChannelController _processAndReplyWithMessage:completion:]_block_invoke.87
+ ___70-[CDPDSecureChannelController _processAndReplyWithMessage:completion:]_block_invoke.cold.2
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16ls32l8
+ _objc_msgSend$_deliverEvent:
+ _objc_msgSend$_enforcePrivacyComplianceIfRequired:
+ _objc_msgSend$contextForCDPPDPStateRepair
- -[CDPDAnalyticsTransport _sendEvent:].cold.2
- -[CDPDAnalyticsTransport _sendEvent:].cold.3
- GCC_except_table46
- ___37-[CDPDAnalyticsTransport _sendEvent:]_block_invoke
CStrings:
+ "ActiveLRCWithFallbackStingray"
+ "ActiveServerLogging"
+ "CDPDStateMachine: Skipping PDP setup due to forced Manatee reset"
+ "Clearing the stale CDP+PDP repair CFU (rdar://171113289)"
+ "Eligible (DEPRECATED)"
+ "Experienced error while attempting to clear CDP+PDP repair CFU: %@"
+ "Generating PDP blob for PDP eligible user (state: %lu)..."
+ "PDP blob generation requires PDP eligible state, current state: %lu"
+ "Rerouting event %@ to transport with clientName: %@"
+ "_deliverEvent:"
+ "_enforcePrivacyComplianceIfRequired:"
+ "contextForCDPPDPStateRepair"
+ "v32@0:8@\"CDPContext\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "Generating PDP blob..."
- "PDP blob generation requires active PDP state, current state: %lu"

```
