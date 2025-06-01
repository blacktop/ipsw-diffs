## SharedUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils`

```diff

-1391.2.1.0.0
-  __TEXT.__text: 0x1d32c
+1394.40.33.0.0
+  __TEXT.__text: 0x1d8dc
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0xc80
+  __TEXT.__objc_methlist: 0xc98
   __TEXT.__const: 0x248
-  __TEXT.__cstring: 0x2555
+  __TEXT.__cstring: 0x2598
   __TEXT.__gcc_except_tab: 0x1d0
   __TEXT.__oslogstring: 0xa49
-  __TEXT.__unwind_info: 0x754
+  __TEXT.__unwind_info: 0x760
   __TEXT.__objc_classname: 0x3d7
-  __TEXT.__objc_methname: 0x27cf
-  __TEXT.__objc_methtype: 0xf55
-  __TEXT.__objc_stubs: 0x1780
+  __TEXT.__objc_methname: 0x282b
+  __TEXT.__objc_methtype: 0xf94
+  __TEXT.__objc_stubs: 0x17a0
   __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x5d8
+  __DATA_CONST.__const: 0x5c0
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1e08
-  __DATA_CONST.__objc_selrefs: 0x9a8
-  __AUTH_CONST.__cfstring: 0xde0
+  __DATA_CONST.__objc_selrefs: 0x9b8
+  __AUTH_CONST.__cfstring: 0xe00
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_intobj: 0x750
+  __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__auth_got: 0x358
   __DATA.__objc_protorefs: 0x78
   __DATA.__objc_classrefs: 0x158
   __DATA.__objc_superrefs: 0x68
   __DATA.__objc_ivar: 0xac
   __DATA.__data: 0x9e1
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0xe0
   __DATA.__common: 0x0
-  __DATA_DIRTY.__const: 0x3a0
+  __DATA_DIRTY.__const: 0x320
   __DATA_DIRTY.__objc_const: 0x900
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__data: 0x4

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E79C5C6D-0386-3CD2-B185-87A4D7F30FE5
-  Functions: 610
-  Symbols:   1825
-  CStrings:  1168
+  UUID: 8AE54CBB-5587-3390-A13F-9C7F4B8F14BF
+  Functions: 618
+  Symbols:   1824
+  CStrings:  1177
 
Symbols:
+ -[LAACMHelper clear]
+ -[LAAssertionsProxy dropTouchIdAssertionWithReason:reply:]
+ -[LAAssertionsProxy takeTouchIdAssertionWithReason:reply:]
+ -[LAPasscodeHelper _verifyPasswordUsingMKB:acmContext:userId:options:log:]
+ GCC_except_table20
+ GCC_except_table23
+ GCC_except_table27
+ GCC_except_table29
+ GCC_except_table37
+ GCC_except_table39
+ GCC_except_table41
+ GCC_except_table43
+ GCC_except_table45
+ GCC_except_table47
+ _ACMSEPControl
+ _ACMSEPControlEx
+ _LibCall_ACMSEPControl
+ _LibCall_ACMSEPControl_Block
+ _LibSer_SEPControlResponse_Deserialize
+ _LibSer_SEPControlResponse_GetSize
+ _LibSer_SEPControlResponse_Serialize
+ _LibSer_SEPControl_Deserialize
+ _LibSer_SEPControl_GetSize
+ _LibSer_SEPControl_Serialize
+ _MKBUnlockDevice
+ _MKBVerifyPasswordWithContext
+ _Util_getSubrequirement
+ _Util_getSubrequirement.cold.1
+ _Util_getSubrequirementOfType
+ _Util_getSubrequirementOfType.cold.1
+ ___58-[LAAssertionsProxy dropTouchIdAssertionWithReason:reply:]_block_invoke
+ ___58-[LAAssertionsProxy dropTouchIdAssertionWithReason:reply:]_block_invoke_2
+ ___58-[LAAssertionsProxy dropTouchIdAssertionWithReason:reply:]_block_invoke_2.cold.1
+ ___58-[LAAssertionsProxy takeTouchIdAssertionWithReason:reply:]_block_invoke
+ ___58-[LAAssertionsProxy takeTouchIdAssertionWithReason:reply:]_block_invoke_2
+ ___58-[LAAssertionsProxy takeTouchIdAssertionWithReason:reply:]_block_invoke_2.cold.1
+ ___76-[LAPasscodeHelper verifyPasswordUsingAKS:acmContext:userId:policy:options:]_block_invoke
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_i8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.78
+ ___block_literal_global.80
+ _objc_msgSend$_verifyPasswordUsingMKB:acmContext:userId:options:log:
+ _objc_msgSend$dropTouchIdAssertionWithReason:reply:
+ _objc_msgSend$takeTouchIdAssertionWithReason:reply:
+ _objc_retain_x27
+ _objc_retain_x28
- -[LAAssertionsProxy dropTouchIdAssertion:]
- -[LAAssertionsProxy takeTouchIdAssertion:]
- GCC_except_table19
- GCC_except_table22
- GCC_except_table25
- GCC_except_table28
- GCC_except_table36
- GCC_except_table38
- GCC_except_table40
- GCC_except_table42
- GCC_except_table44
- GCC_except_table46
- _IOConnectCallMethod
- _IORegistryEntryFromPath
- _IOServiceClose
- ___42-[LAAssertionsProxy dropTouchIdAssertion:]_block_invoke
- ___42-[LAAssertionsProxy dropTouchIdAssertion:]_block_invoke_2
- ___42-[LAAssertionsProxy dropTouchIdAssertion:]_block_invoke_2.cold.1
- ___42-[LAAssertionsProxy takeTouchIdAssertion:]_block_invoke
- ___42-[LAAssertionsProxy takeTouchIdAssertion:]_block_invoke_2
- ___42-[LAAssertionsProxy takeTouchIdAssertion:]_block_invoke_2.cold.1
- ___block_descriptor_tmp.149
- ___block_descriptor_tmp.170
- ___block_literal_global.151
- ___block_literal_global.172
- ___block_literal_global.71
- ___block_literal_global.73
- ___get_aks_client_connection_block_invoke
- ___get_aks_client_dispatch_queue_block_invoke
- __aks_verify_password
- __copy_aks_client_connection
- _aks_copy_packed_data
- _aks_pack_data
- _aks_unlock_device
- _aks_verify_password
- _get_aks_client_connection
- _get_aks_client_connection.connection
- _get_aks_client_dispatch_queue.connection_queue
- _get_aks_client_dispatch_queue.onceToken
- _objc_msgSend$dropTouchIdAssertion:
- _objc_msgSend$takeTouchIdAssertion:
- _syslog
CStrings:
+ "ACMRequirement - ACMRequirementDataRatchet"
+ "DeviceHandle"
+ "LibCall_ACMSEPControl"
+ "LibCall_ACMSEPControl_Block"
+ "MKB device unlock for keybag %d returned %d"
+ "MKB password verification for keybag %d returned %d"
+ "Util_getSubrequirement"
+ "Util_getSubrequirementOfType"
+ "_verifyPasswordUsingMKB:acmContext:userId:options:log:"
+ "clear"
+ "dropTouchIdAssertionWithReason:reply:"
+ "i56@0:8@16@24@32@40@48"
+ "i8@?0"
+ "req"
+ "takeTouchIdAssertionWithReason:reply:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "AKS device unlock for keybag %d returned %x"
- "AKS password verification for keybag %d returned %x"
- "AppleKeyStore"
- "IOService:/IOResources/AppleKeyStore"
- "aks-client-queue"
- "dropTouchIdAssertion:"
- "failed to open connection to %s\n"
- "takeTouchIdAssertion:"

```
