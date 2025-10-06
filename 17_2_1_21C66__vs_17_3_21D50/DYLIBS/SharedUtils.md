## SharedUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils`

```diff

-1394.62.1.0.0
-  __TEXT.__text: 0x1da40
+1394.82.1.0.0
+  __TEXT.__text: 0x1e0ac
   __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_methlist: 0xcd0
+  __TEXT.__objc_methlist: 0xd10
   __TEXT.__const: 0x190
-  __TEXT.__cstring: 0x251d
-  __TEXT.__gcc_except_tab: 0x1d0
-  __TEXT.__oslogstring: 0xa82
-  __TEXT.__unwind_info: 0x780
+  __TEXT.__cstring: 0x261f
+  __TEXT.__gcc_except_tab: 0x1e8
+  __TEXT.__oslogstring: 0xa97
+  __TEXT.__unwind_info: 0x798
   __TEXT.__objc_classname: 0x41c
-  __TEXT.__objc_methname: 0x28ed
-  __TEXT.__objc_methtype: 0xff3
-  __TEXT.__objc_stubs: 0x17c0
+  __TEXT.__objc_methname: 0x295f
+  __TEXT.__objc_methtype: 0xffe
+  __TEXT.__objc_stubs: 0x1800
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x5b8
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1f60
-  __DATA_CONST.__objc_selrefs: 0x9d8
-  __AUTH_CONST.__cfstring: 0xd80
+  __DATA_CONST.__objc_selrefs: 0xa00
+  __AUTH_CONST.__cfstring: 0xe00
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__objc_intobj: 0x768
+  __AUTH_CONST.__objc_intobj: 0x8a0
   __AUTH_CONST.__auth_got: 0x350
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_protorefs: 0x78

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9A63A432-C598-3D2B-A380-1C881216531F
-  Functions: 623
-  Symbols:   1846
-  CStrings:  1178
+  UUID: 28F0FDFD-5DAD-315F-8E05-EE5D412CDE03
+  Functions: 629
+  Symbols:   1861
+  CStrings:  1196
 
Symbols:
+ +[LAACMHelper _errorFromACMStatus:]
+ +[LAACMHelper ratchetStatusWithConfig:]
+ +[LAACMHelper resetRatchet:]
+ +[LAManagedACMParameters acmParameterDoNotStartDTOTimers]
+ +[LAUtils isLocationBasedPolicy:]
+ GCC_except_table35
+ GCC_except_table49
+ GCC_except_table51
+ ___31+[LAParamChecker checkOptions:]_block_invoke.153
+ ___39+[LAACMHelper ratchetStatusWithConfig:]_block_invoke
+ ___block_literal_global.156
+ ___block_literal_global.164
+ ___block_literal_global.171
+ ___block_literal_global.186
+ ___block_literal_global.204
+ ___block_literal_global.221
+ ___block_literal_global.33
+ _objc_msgSend$_errorFromACMStatus:
+ _objc_msgSend$notifyBiometricMatchOperationStartAttempted
- GCC_except_table37
- GCC_except_table39
- ___31+[LAParamChecker checkOptions:]_block_invoke.126
- ___block_literal_global.129
- ___block_literal_global.137
- ___block_literal_global.144
- ___block_literal_global.159
- ___block_literal_global.177
- ___block_literal_global.194
- ___block_literal_global.32
CStrings:
+ "ACMRequirement - ACMRequirementDataRatchet"
+ "BiometricRatchetAuthentication"
+ "DoNotStartDTOTimers"
+ "Failed to fetch ratchet state and config (stat: %d)"
+ "Failed to reset ACM Ratchet: %d"
+ "LBDeviceOwnerAuthentication"
+ "Reseting ACM Ratchet"
+ "_errorFromACMStatus:"
+ "acmParameterDoNotStartDTOTimers"
+ "com.apple.BiometricKit.matchOperationStartAttempted"
+ "isLocationBasedPolicy:"
+ "q20@0:8i16"
+ "ratchetStatusWithConfig:"
+ "resetRatchet:"

```
