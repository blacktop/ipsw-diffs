## com.apple.driver.AppleMesaSEPDriver

> `com.apple.driver.AppleMesaSEPDriver`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-10312.0.0.0.0
+10314.0.0.0.0
   __TEXT.__const: 0x150
   __TEXT.__cstring: 0x6b3d
   __TEXT.__os_log: 0x36f7
-  __TEXT_EXEC.__text: 0x31e68
+  __TEXT_EXEC.__text: 0x31e24
   __TEXT_EXEC.__auth_stubs: 0x760
   __DATA.__data: 0xc4
   __DATA.__common: 0x2b0

   __DATA_CONST.__kalloc_var: 0x140
   __DATA_CONST.__auth_got: 0x3b0
   __DATA_CONST.__got: 0xc8
-  Functions: 627
-  Symbols:   1595
+  Functions: 630
+  Symbols:   1598
   CStrings:  1057
 
Symbols:
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_8810
+ __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_9124
+ __ZZN18AppleMesaSEPDriver16sendEnrollResultEP16enroll_result_v2E21kalloc_type_view_7340
+ __ZZN18AppleMesaSEPDriver16sendEnrollResultEP16enroll_result_v2E21kalloc_type_view_7349
+ __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE22kalloc_type_view_10819
+ __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE22kalloc_type_view_10871
+ __ZZN18AppleMesaSEPDriver26sendTemplateListUpdatedMsgEP25template_update_info_v2_tE21kalloc_type_view_7410
+ __ZZN18AppleMesaSEPDriver26sendTemplateListUpdatedMsgEP25template_update_info_v2_tE21kalloc_type_view_7419
+ __ZZN18AppleMesaSEPDriver29sendTemplateListNotUpdatedMsgEP17bgops_result_v2_tE21kalloc_type_view_7442
+ __ZZN18AppleMesaSEPDriver29sendTemplateListNotUpdatedMsgEP17bgops_result_v2_tE21kalloc_type_view_7451
+ __ZZN18AppleMesaSEPDriver31sendEnrollProgresWithEnrollInfoEhP20enrollment_info_v2_tE21kalloc_type_view_7310
+ __ZZN18AppleMesaSEPDriver31sendEnrollProgresWithEnrollInfoEhP20enrollment_info_v2_tE21kalloc_type_view_7319
- __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_8794
- __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_9107
- __ZZN18AppleMesaSEPDriver16sendEnrollResultEP16enroll_result_v2E21kalloc_type_view_7344
- __ZZN18AppleMesaSEPDriver16sendEnrollResultEP16enroll_result_v2E21kalloc_type_view_7353
- __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE22kalloc_type_view_10798
- __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE22kalloc_type_view_10850
- __ZZN18AppleMesaSEPDriver26sendTemplateListUpdatedMsgEP25template_update_info_v2_tE21kalloc_type_view_7414
- __ZZN18AppleMesaSEPDriver26sendTemplateListUpdatedMsgEP25template_update_info_v2_tE21kalloc_type_view_7423
- __ZZN18AppleMesaSEPDriver29sendTemplateListNotUpdatedMsgEP17bgops_result_v2_tE21kalloc_type_view_7446
- __ZZN18AppleMesaSEPDriver29sendTemplateListNotUpdatedMsgEP17bgops_result_v2_tE21kalloc_type_view_7455
- __ZZN18AppleMesaSEPDriver31sendEnrollProgresWithEnrollInfoEhP20enrollment_info_v2_tE21kalloc_type_view_7314
- __ZZN18AppleMesaSEPDriver31sendEnrollProgresWithEnrollInfoEhP20enrollment_info_v2_tE21kalloc_type_view_7323
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Xh418E/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/AppleMesaAccessory.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Xh418E/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/MesaAccessoryManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Xh418E/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaSEPDriver.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Xh418E/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/IOMesaLogging.cpp"
+ "AssertMacros: %s (value = 0x%lx), version: Mesa-10314~989, %s file: %s, line: %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.q4Tq0M/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/AppleMesaAccessory.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.q4Tq0M/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/MesaAccessoryManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.q4Tq0M/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaSEPDriver.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.q4Tq0M/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/IOMesaLogging.cpp"
- "AssertMacros: %s (value = 0x%lx), version: Mesa-10312~482, %s file: %s, line: %d\n"
```
