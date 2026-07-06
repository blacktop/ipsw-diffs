## com.apple.driver.AppleMesaSEPDriver

> `com.apple.driver.AppleMesaSEPDriver`

```diff

   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x6b1c
+  __TEXT.__cstring: 0x6b3d
   __TEXT.__os_log: 0x36f7
-  __TEXT_EXEC.__text: 0x31ca0
-  __TEXT_EXEC.__auth_stubs: 0x740
+  __TEXT_EXEC.__text: 0x31e68
+  __TEXT_EXEC.__auth_stubs: 0x760
   __DATA.__data: 0xc4
   __DATA.__common: 0x2b0
   __DATA.__bss: 0x21

   __DATA_CONST.__const: 0x46d8
   __DATA_CONST.__kalloc_type: 0x5c0
   __DATA_CONST.__kalloc_var: 0x140
-  __DATA_CONST.__auth_got: 0x3a0
+  __DATA_CONST.__auth_got: 0x3b0
   __DATA_CONST.__got: 0xc8
-  Functions: 626
-  Symbols:   1657
-  CStrings:  1054
+  Functions: 627
+  Symbols:   1660
+  CStrings:  1057
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ __ZNK18AppleMesaSEPDriver12isRecoveryOSEv
+ __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_8794
+ __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_9107
+ __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE22kalloc_type_view_10798
+ __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE22kalloc_type_view_10850
+ _strlen
+ _strncmp
- __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_8760
- __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_9073
- __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE22kalloc_type_view_10764
- __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE22kalloc_type_view_10816
Functions:
+ __ZNK18AppleMesaSEPDriver12isRecoveryOSEv
~ __ZN18AppleMesaSEPDriver23getOperationDeviceStateEPK8OSObject : 392 -> 408
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.q4Tq0M/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/AppleMesaAccessory.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.q4Tq0M/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/MesaAccessoryManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.q4Tq0M/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaSEPDriver.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.q4Tq0M/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/IOMesaLogging.cpp"
+ "AssertMacros: %s (value = 0x%lx), version: Mesa-10312~482, %s file: %s, line: %d\n"
+ "osenvironment"
+ "recovery"
+ "recoveryos"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.actPQQ/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/AppleMesaAccessory.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.actPQQ/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/MesaAccessoryManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.actPQQ/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaSEPDriver.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.actPQQ/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/IOMesaLogging.cpp"
- "AssertMacros: %s (value = 0x%lx), version: Mesa-10308~3331, %s file: %s, line: %d\n"

```
