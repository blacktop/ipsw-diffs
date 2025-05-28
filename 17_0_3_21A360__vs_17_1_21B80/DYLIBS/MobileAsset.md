## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

```diff

-936.2.1.0.0
-  __TEXT.__text: 0x6a200
+936.42.1.0.0
+  __TEXT.__text: 0x6c4d0
   __TEXT.__auth_stubs: 0x8e0
-  __TEXT.__objc_methlist: 0x5410
+  __TEXT.__objc_methlist: 0x5488
   __TEXT.__const: 0x1b8
-  __TEXT.__gcc_except_tab: 0x71c
-  __TEXT.__cstring: 0x12766
-  __TEXT.__oslogstring: 0x3eef
-  __TEXT.__unwind_info: 0x16e8
+  __TEXT.__gcc_except_tab: 0x74c
+  __TEXT.__cstring: 0x12987
+  __TEXT.__oslogstring: 0x4132
+  __TEXT.__unwind_info: 0x174c
   __TEXT.__objc_classname: 0x5f1
-  __TEXT.__objc_methname: 0x10107
-  __TEXT.__objc_methtype: 0x107c
-  __TEXT.__objc_stubs: 0x6b80
+  __TEXT.__objc_methname: 0x102c3
+  __TEXT.__objc_methtype: 0x108f
+  __TEXT.__objc_stubs: 0x6c60
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x1bb0
   __DATA_CONST.__objc_classlist: 0x1e8

   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x6bc0
-  __DATA_CONST.__objc_selrefs: 0x27e0
+  __DATA_CONST.__objc_selrefs: 0x2830
   __DATA_CONST.__objc_arraydata: 0x250
-  __AUTH_CONST.__cfstring: 0xd3e0
+  __AUTH_CONST.__cfstring: 0xd600
   __AUTH_CONST.__const: 0x5e0
   __AUTH_CONST.__objc_const: 0x2010
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /System/Library/PrivateFrameworks/StreamingZip.framework/StreamingZip
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2555
-  Symbols:   7505
-  CStrings:  4400
+  Functions: 2589
+  Symbols:   7582
+  CStrings:  4436
 
Symbols:
+ +[MAAutoAsset cancelActivityForSelector:completion:]
+ +[MAAutoAsset cancelActivityForSelector:completion:].cold.1
+ +[MAAutoAsset cancelActivityForSelectorSync:]
+ +[MAAutoAsset stageDetermineAllAvailableForUpdate:completion:]
+ +[MAAutoAsset stageDetermineAllAvailableForUpdate:completion:].cold.1
+ +[MAAutoAsset stageDetermineAllAvailableForUpdateSync:totalExpectedBytes:error:]
+ -[MAAutoAsset _cancelActivityForSelector:]
+ -[MAAutoAsset _cancelActivityForSelector:].cold.1
+ -[MAAutoAsset _cancelActivityForSelectorSync]
+ -[MAAutoAsset _failedCancelActivity:withResponseError:description:completion:]
+ -[MAAutoAsset _failedCancelActivity:withResponseError:description:completion:].cold.1
+ -[MAAutoAsset _stageDetermineAllAvailableForUpdate:completion:]
+ -[MAAutoAsset _stageDetermineAllAvailableForUpdate:completion:].cold.1
+ -[MAAutoAsset _stageDetermineAllAvailableForUpdateSync:totalExpectedBytes:error:]
+ -[MAAutoAsset _successCancelActivity:]
+ GCC_except_table159
+ GCC_except_table172
+ GCC_except_table190
+ GCC_except_table201
+ GCC_except_table212
+ GCC_except_table223
+ GCC_except_table234
+ GCC_except_table245
+ GCC_except_table256
+ GCC_except_table267
+ ___33-[MAAutoAsset _successEliminate:]_block_invoke.568
+ ___38-[MAAutoAsset _successCancelActivity:]_block_invoke
+ ___38-[MAAutoAsset _successCancelActivity:]_block_invoke.561
+ ___38-[MAAutoAsset _successCancelActivity:]_block_invoke.cold.1
+ ___42-[MAAutoAsset _cancelActivityForSelector:]_block_invoke
+ ___42-[MAAutoAsset _cancelActivityForSelector:]_block_invoke_2
+ ___45-[MAAutoAsset _cancelActivityForSelectorSync]_block_invoke
+ ___45-[MAAutoAsset _cancelActivityForSelectorSync]_block_invoke_2
+ ___45-[MAAutoAsset _cancelActivityForSelectorSync]_block_invoke_3
+ ___47-[MAAutoAsset _successEndLockUsage:completion:]_block_invoke.557
+ ___52+[MAAutoAsset cancelActivityForSelector:completion:]_block_invoke
+ ___52+[MAAutoAsset cancelActivityForSelector:completion:]_block_invoke_2
+ ___58-[MAAutoAsset _successLockContent:dueToDesire:completion:]_block_invoke.550
+ ___62+[MAAutoAsset stageDetermineAllAvailableForUpdate:completion:]_block_invoke
+ ___62+[MAAutoAsset stageDetermineAllAvailableForUpdate:completion:]_block_invoke_2
+ ___63-[MAAutoAsset _stageDetermineAllAvailableForUpdate:completion:]_block_invoke
+ ___63-[MAAutoAsset _stageDetermineAllAvailableForUpdate:completion:]_block_invoke_2
+ ___78-[MAAutoAsset _failedCancelActivity:withResponseError:description:completion:]_block_invoke
+ ___78-[MAAutoAsset _failedCancelActivity:withResponseError:description:completion:]_block_invoke.cold.1
+ ___81-[MAAutoAsset _stageDetermineAllAvailableForUpdateSync:totalExpectedBytes:error:]_block_invoke
+ ___81-[MAAutoAsset _stageDetermineAllAvailableForUpdateSync:totalExpectedBytes:error:]_block_invoke_2
+ ___81-[MAAutoAsset _stageDetermineAllAvailableForUpdateSync:totalExpectedBytes:error:]_block_invoke_3
+ ___Block_byref_object_copy_.528
+ ___Block_byref_object_copy_.930
+ ___Block_byref_object_dispose_.529
+ ___Block_byref_object_dispose_.931
+ ___block_literal_global.1049
+ ___block_literal_global.2250
+ ___block_literal_global.2252
+ ___block_literal_global.2254
+ ___block_literal_global.2256
+ ___block_literal_global.634
+ ___block_literal_global.645
+ ___block_literal_global.683
+ ___block_literal_global.686
+ ___block_literal_global.689
+ ___block_literal_global.699
+ ___block_literal_global.704
+ ___block_literal_global.783
+ ___block_literal_global.785
+ ___block_literal_global.787
+ ___block_literal_global.808
+ __unnamed_array_storage.725
+ __unnamed_array_storage.726
+ __unnamed_array_storage.742
+ __unnamed_array_storage.945
+ __unnamed_array_storage.953
+ __unnamed_array_storage.968
+ _objc_msgSend$_cancelActivityForSelector:
+ _objc_msgSend$_cancelActivityForSelectorSync
+ _objc_msgSend$_failedCancelActivity:withResponseError:description:completion:
+ _objc_msgSend$_stageDetermineAllAvailableForUpdate:completion:
+ _objc_msgSend$_stageDetermineAllAvailableForUpdateSync:totalExpectedBytes:error:
+ _objc_msgSend$_successCancelActivity:
+ _objc_msgSend$initWithAvailableForStaging:withTotalExpectedBytes:
- GCC_except_table154
- GCC_except_table167
- GCC_except_table185
- GCC_except_table196
- GCC_except_table207
- GCC_except_table218
- GCC_except_table229
- GCC_except_table240
- ___33-[MAAutoAsset _successEliminate:]_block_invoke.546
- ___47-[MAAutoAsset _successEndLockUsage:completion:]_block_invoke.542
- ___58-[MAAutoAsset _successLockContent:dueToDesire:completion:]_block_invoke.535
- ___Block_byref_object_copy_.513
- ___Block_byref_object_copy_.921
- ___Block_byref_object_dispose_.514
- ___Block_byref_object_dispose_.922
- ___block_literal_global.1040
- ___block_literal_global.2247
- ___block_literal_global.2249
- ___block_literal_global.2251
- ___block_literal_global.2253
- ___block_literal_global.625
- ___block_literal_global.636
- ___block_literal_global.674
- ___block_literal_global.677
- ___block_literal_global.680
- ___block_literal_global.690
- ___block_literal_global.695
- ___block_literal_global.728
- ___block_literal_global.730
- ___block_literal_global.732
- ___block_literal_global.799
- __unnamed_array_storage.716
- __unnamed_array_storage.717
- __unnamed_array_storage.733
- __unnamed_array_storage.942
- __unnamed_array_storage.950
- __unnamed_array_storage.965
CStrings:
+ "+cancelActivityForSelector"
+ "+stageDetermineAllAvailableForUpdate"
+ "@40@0:8@16^Q24^@32"
+ "MA-AUTO(REPLY):CANCEL_ACTIVITY_FOR_SELECTOR"
+ "MA-AUTO-STAGE:DETERMINE_ALL_AVAILABLE_FOR_UPDATE"
+ "MA-AUTO:CANCEL_ACTIVITY_FOR_SELECTOR"
+ "MA-auto(staging-client){+stageDetermineAllAvailableForUpdate} | no client completion block | %{public}@"
+ "MA-auto{+cancelActivityForSelectorSync}"
+ "MA-auto{+cancelActivityForSelector}"
+ "MA-auto{+cancelActivityForSelector} | no client completion block | %{public}@"
+ "MA-auto{_cancelActivityForSelector} | no client completion block | %{public}@"
+ "MA-auto{_failedCancelActivity} | %{public}@ | SUCCESS"
+ "MA-auto{_failedCancelActivity} | %{public}@ | error:%{public}@"
+ "MA-auto{_failedCancelActivity} | no client completion block | %{public}@"
+ "MA-auto{_successCancelActivity} | %{public}@ | SUCCESS"
+ "MA-auto{_successCancelActivity} | no client completion block | %{public}@"
+ "OSVersion"
+ "STAGE_GENERAL"
+ "TargetBuildVersion"
+ "TargetOSVersion"
+ "_cancelActivityForSelector"
+ "_cancelActivityForSelector:"
+ "_cancelActivityForSelectorSync"
+ "_failedCancelActivity:withResponseError:description:completion:"
+ "_stageDetermineAllAvailableForUpdate:completion:"
+ "_stageDetermineAllAvailableForUpdateSync:totalExpectedBytes:error:"
+ "_successCancelActivity:"
+ "auto(cancelActivity)"
+ "auto(cancelActivityForSelectorSync)"
+ "auto(stageDetermineAllAvailableForUpdate)"
+ "cancelActivity"
+ "cancelActivityForSelector:completion:"
+ "cancelActivityForSelectorSync:"
+ "stageDetermineAllAvailableForUpdate:completion:"
+ "stageDetermineAllAvailableForUpdateSync:totalExpectedBytes:error:"
+ "timeout (at framework layer) while waiting for cancel-activity to complete"

```
