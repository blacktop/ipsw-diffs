## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xb8f38
+881.0.0.0.0
+  __TEXT.__text: 0xb9024
   __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0xa38c
+  __TEXT.__objc_methlist: 0xa3a4
   __TEXT.__const: 0x1d0
   __TEXT.__gcc_except_tab: 0x1db8
   __TEXT.__cstring: 0x1074d
   __TEXT.__oslogstring: 0x6aa3
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x2638
+  __TEXT.__unwind_info: 0x2640
   __TEXT.__objc_classname: 0x15e4
-  __TEXT.__objc_methname: 0x16e64
+  __TEXT.__objc_methname: 0x16eb9
   __TEXT.__objc_methtype: 0x356e
-  __TEXT.__objc_stubs: 0xe600
+  __TEXT.__objc_stubs: 0xe660
   __DATA_CONST.__got: 0xa78
   __DATA_CONST.__const: 0x1db0
   __DATA_CONST.__objc_classlist: 0x488
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x52a0
+  __DATA_CONST.__objc_selrefs: 0x52b8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_arraydata: 0x1a8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F720217-6060-3856-BABC-DDBE5B7964D7
-  Functions: 3969
-  Symbols:   14323
-  CStrings:  7562
+  UUID: C752D3B8-B4A8-362C-B8C7-CDC5CEB87E21
+  Functions: 3971
+  Symbols:   14330
+  CStrings:  7565
 
Symbols:
+ +[TSUtilities getStringWithFirstCharacterUppercase:]
+ -[CTDisplayPlan(SimSetup) transferCapabilityForMessage]
+ GCC_except_table56
+ ___block_literal_global.681
+ ___block_literal_global.710
+ ___block_literal_global.770
+ _objc_msgSend$getStringWithFirstCharacterUppercase:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$transferCapabilityForMessage
- GCC_except_table53
- ___block_literal_global.680
- ___block_literal_global.709
- ___block_literal_global.769
Functions:
~ -[NSArray(CTDisplayPlan) getCombinedFooterForNonTransferablePlans] : 1332 -> 1400
~ -[NSArray(CTDisplayPlan) getCombinedTitleAndDetailsForNonTransferablePlans:details:] : 676 -> 748
+ -[CTDisplayPlan(SimSetup) transferCapabilityForMessage]
~ +[NSMutableDictionary(CategorizedPlans) dictionaryWithPlansByGroupByTransferCapability:] : 512 -> 428
~ -[TSNoPlanForTransferViewController initWithCarrier:phoneNumber:transferCapability:showOtherOptions:entryPoint:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:isStartOverNeeded:] : 448 -> 380
~ -[TSNoPlanForTransferViewController initWithPlans:showOtherOptions:isStartOverNeeded:] : 1040 -> 908
~ +[TSNoPlanForTransferViewController getTitleAndDetailsForTransferCapability:carrier:phoneNumber:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:isVisitStoreRequired:] : 3032 -> 3036
+ +[TSUtilities getStringWithFirstCharacterUppercase:]
CStrings:
+ "getStringWithFirstCharacterUppercase:"
+ "stringWithString:"
+ "transferCapabilityForMessage"

```
