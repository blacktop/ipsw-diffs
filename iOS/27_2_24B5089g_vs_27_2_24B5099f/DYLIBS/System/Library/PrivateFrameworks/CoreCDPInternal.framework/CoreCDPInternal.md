## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-448.125.5.2.0
-  __TEXT.__text: 0x8de40
-  __TEXT.__objc_methlist: 0x57ec
+448.125.9.0.0
+  __TEXT.__text: 0x8e4e0
+  __TEXT.__objc_methlist: 0x5804
   __TEXT.__const: 0x888
-  __TEXT.__oslogstring: 0x1511e
-  __TEXT.__cstring: 0xe685
-  __TEXT.__gcc_except_tab: 0xb68
+  __TEXT.__oslogstring: 0x1510e
+  __TEXT.__cstring: 0xe6a5
+  __TEXT.__gcc_except_tab: 0xb94
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x3b7
   __TEXT.__swift5_fieldmd: 0x80

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift_as_cont: 0x68
-  __TEXT.__unwind_info: 0x2ef0
-  __TEXT.__eh_frame: 0x8f0
+  __TEXT.__unwind_info: 0x2f28
+  __TEXT.__eh_frame: 0x918
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2610
+  __DATA_CONST.__const: 0x26d8
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a00
+  __DATA_CONST.__objc_selrefs: 0x3a18
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x220
-  __DATA_CONST.__got: 0x1130
-  __AUTH_CONST.__const: 0xad0
+  __DATA_CONST.__got: 0x1148
+  __AUTH_CONST.__const: 0xb10
   __AUTH_CONST.__cfstring: 0x9940
   __AUTH_CONST.__objc_const: 0x10260
   __AUTH_CONST.__objc_intobj: 0x180

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3209
-  Symbols:   4217
-  CStrings:  2862
+  Functions: 3220
+  Symbols:   4235
+  CStrings:  2863
 
Symbols:
+ -[CDPDPCSController _sendGeneratePDPBlob:completion:]
+ -[CDPDPCSController _sendSetupPDPIdentities:completion:]
+ GCC_except_table29
+ GCC_except_table32
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table54
+ ___53-[CDPDPCSController _sendGeneratePDPBlob:completion:]_block_invoke
+ ___53-[CDPDPCSController _sendGeneratePDPBlob:completion:]_block_invoke_2
+ ___56-[CDPDPCSController _sendSetupPDPIdentities:completion:]_block_invoke
+ ___56-[CDPDPCSController _sendSetupPDPIdentities:completion:]_block_invoke_2
+ ___56-[CDPDPCSController _sendSetupPDPIdentities:completion:]_block_invoke_3
+ ___56-[CDPDPCSController _sendSetupPDPIdentities:completion:]_block_invoke_4
+ ___block_descriptor_48_e8_32bs40r_e20_v24?0q8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32bs40r_e28_v24?0"NSData"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32bs40r_e28_v24?0"NSData"8"NSError"16ls32l8r40l8
+ ___block_descriptor_48_e8_32bs40r_e30_v24?0"NSNumber"8"NSError"16lr40l8s32l8
+ ___block_descriptor_56_e8_32s40r48w_e35_v16?0?<v?"NSNumber""NSError">8lw48l8s32l8r40l8
+ ___block_descriptor_56_e8_32s40s48r_e33_v16?0?<v?"NSData""NSError">8ls32l8s40l8r48l8
+ _kAAAnalyticsEventCustodianHealthCheckOwnerCleanupOrphanedCustodian
+ _kDataAccessRecoveryContactSuggestionFamily
+ _kDataAccessRecoveryContactSuggestionMegadome
- GCC_except_table30
- GCC_except_table38
- GCC_except_table40
- ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16ls32l8
CStrings:
+ "%@: Renewed credentials, retrying PDP blob generation"
+ "v16@?0@?<v@?@\"NSData\"@\"NSError\">8"
- "Generate PDP Blob retry completed with blob length=%lu error=%@"
```
