## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-871.2.0.0.0
-  __TEXT.__text: 0xb3b14
+871.3.0.0.0
+  __TEXT.__text: 0xb3bc0
   __TEXT.__auth_stubs: 0x840
   __TEXT.__objc_methlist: 0xa00c
   __TEXT.__const: 0x1b8
   __TEXT.__gcc_except_tab: 0x1ca0
-  __TEXT.__cstring: 0xfb3e
+  __TEXT.__cstring: 0xfb5d
   __TEXT.__oslogstring: 0x65f6
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa

   __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__auth_got: 0x430
   __AUTH_CONST.__const: 0x840
-  __AUTH_CONST.__cfstring: 0x74c0
+  __AUTH_CONST.__cfstring: 0x74e0
   __AUTH_CONST.__objc_const: 0x3d2a8
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F5436B68-F928-3922-A988-CFC0F28717FE
+  UUID: B0C456A9-6B2D-300B-955A-CA5C4DFF4FCD
   Functions: 3874
   Symbols:   14035
-  CStrings:  7374
+  CStrings:  7376
 
Symbols:
+ ___block_literal_global.300
+ ___block_literal_global.316
- ___block_literal_global.297
- ___block_literal_global.313
Functions:
~ +[TSNoPlanForTransferViewController getTitleAndDetailsForTransferCapability:carrier:phoneNumber:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:] : 2848 -> 2912
~ +[TSSinglePlanTransferViewController getTitleAndDetailsForPlanType:transferCapability:isShowingFilteredPlans:carrier:] : 1860 -> 1968
CStrings:
+ "CONTACT_CARRIER_TO_SETUP_ESIM"
+ "TRANSFER_UNSUPPORTED_PLAN_DETAIL_%@"
- "TRANSFER_INELIGIBLE_PLAN_DETAIL_%@"

```
