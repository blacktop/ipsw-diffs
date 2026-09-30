## com.apple.driver.AppleMesaSEPDriver

> `com.apple.driver.AppleMesaSEPDriver`

```diff

-10317.0.0.0.0
+10321.40.5.0.0
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x6dbc
+  __TEXT.__cstring: 0x6df6
   __TEXT.__os_log: 0x3728
-  __TEXT_EXEC.__text: 0x320cc
+  __TEXT_EXEC.__text: 0x3225c
   __TEXT_EXEC.__auth_stubs: 0x780
   __DATA.__data: 0xc4
   __DATA.__common: 0x2b0

   __DATA_CONST.__kalloc_type: 0x5c0
   __DATA_CONST.__kalloc_var: 0x140
   __DATA_CONST.__auth_got: 0x3c0
-  __DATA_CONST.__got: 0xc8
-  Functions: 633
-  Symbols:   1608
-  CStrings:  1071
+  __DATA_CONST.__got: 0xd8
+  Functions: 635
+  Symbols:   1612
+  CStrings:  1074
 
Symbols:
+ _OUTLINED_FUNCTION_36
+ __ZN18AppleMesaSEPDriver23reRegisterChildServicesEv
+ __ZN9IOService9metaClassE
+ __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_8842
+ __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_9156
+ __ZZN18AppleMesaSEPDriver16sendEnrollResultEP16enroll_result_v2E21kalloc_type_view_7372
+ __ZZN18AppleMesaSEPDriver16sendEnrollResultEP16enroll_result_v2E21kalloc_type_view_7381
+ __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE22kalloc_type_view_10851
+ __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE22kalloc_type_view_10903
+ __ZZN18AppleMesaSEPDriver26sendTemplateListUpdatedMsgEP25template_update_info_v3_tE21kalloc_type_view_7442
+ __ZZN18AppleMesaSEPDriver26sendTemplateListUpdatedMsgEP25template_update_info_v3_tE21kalloc_type_view_7451
+ __ZZN18AppleMesaSEPDriver29sendTemplateListNotUpdatedMsgEP17bgops_result_v3_tE21kalloc_type_view_7474
+ __ZZN18AppleMesaSEPDriver29sendTemplateListNotUpdatedMsgEP17bgops_result_v3_tE21kalloc_type_view_7483
+ __ZZN18AppleMesaSEPDriver31sendEnrollProgresWithEnrollInfoEhP20enrollment_info_v2_tE21kalloc_type_view_7342
+ __ZZN18AppleMesaSEPDriver31sendEnrollProgresWithEnrollInfoEhP20enrollment_info_v2_tE21kalloc_type_view_7351
+ _gIOServicePlane
- __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_8815
- __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_9129
- __ZZN18AppleMesaSEPDriver16sendEnrollResultEP16enroll_result_v2E21kalloc_type_view_7345
- __ZZN18AppleMesaSEPDriver16sendEnrollResultEP16enroll_result_v2E21kalloc_type_view_7354
- __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE22kalloc_type_view_10824
- __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE22kalloc_type_view_10876
- __ZZN18AppleMesaSEPDriver26sendTemplateListUpdatedMsgEP25template_update_info_v3_tE21kalloc_type_view_7415
- __ZZN18AppleMesaSEPDriver26sendTemplateListUpdatedMsgEP25template_update_info_v3_tE21kalloc_type_view_7424
- __ZZN18AppleMesaSEPDriver29sendTemplateListNotUpdatedMsgEP17bgops_result_v3_tE21kalloc_type_view_7447
- __ZZN18AppleMesaSEPDriver29sendTemplateListNotUpdatedMsgEP17bgops_result_v3_tE21kalloc_type_view_7456
- __ZZN18AppleMesaSEPDriver31sendEnrollProgresWithEnrollInfoEhP20enrollment_info_v2_tE21kalloc_type_view_7315
- __ZZN18AppleMesaSEPDriver31sendEnrollProgresWithEnrollInfoEhP20enrollment_info_v2_tE21kalloc_type_view_7324
Functions:
~ __ZN18AppleMesaSEPDriver18setPowerStateGatedEPm : 416 -> 420
+ __ZN18AppleMesaSEPDriver23reRegisterChildServicesEv
~ _OUTLINED_FUNCTION_33 : 12 -> 20
~ _OUTLINED_FUNCTION_35 : 20 -> 12
+ _OUTLINED_FUNCTION_36
~ _ZN18AppleMesaSEPDriver18setPowerStateGatedEPm.cold.1 : 764 -> 788
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/IOKit/biometric/IOBiometricSynchronization.h"
+ "AssertMacros: %s (value = 0x%lx), version: Mesa-10321.40.5~31, %s file: %s, line: %d\n"
+ "iter"
+ "reRegisterChildServices"
+ "reRegisterChildServices()"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/IOKit/biometric/IOBiometricSynchronization.h"
- "AssertMacros: %s (value = 0x%lx), version: Mesa-10317~1293, %s file: %s, line: %d\n"
```
