## LinkServices

> `/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices`

```diff

-300.0.2.0.0
-  __TEXT.__text: 0x1076e4
+300.0.4.102.0
+  __TEXT.__text: 0x1077e0
   __TEXT.__auth_stubs: 0x2410
   __TEXT.__objc_methlist: 0x9130
   __TEXT.__const: 0x58c8

   __TEXT.__swift5_capture: 0x870
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__oslogstring: 0x5abb
+  __TEXT.__oslogstring: 0x5aeb
   __TEXT.__gcc_except_tab: 0x1f8c
-  __TEXT.__unwind_info: 0x4b10
+  __TEXT.__unwind_info: 0x4b18
   __TEXT.__eh_frame: 0x4ea0
   __TEXT.__objc_classname: 0x1b68
   __TEXT.__objc_methname: 0x149a7

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3682CB0E-3964-33D6-B414-43C04F568DF4
-  Functions: 7399
-  Symbols:   14247
+  UUID: 175B77CC-61B9-3EAA-ACAE-E1240E042309
+  Functions: 7400
+  Symbols:   14249
   CStrings:  6502
 
Symbols:
+ -[LNActionDefaultValueProvider _loadActionMetadataWithProvider:retry:error:]
+ GCC_except_table2786
+ GCC_except_table2790
+ GCC_except_table2824
+ GCC_except_table2828
+ GCC_except_table2830
+ GCC_except_table2840
+ GCC_except_table2891
+ GCC_except_table2903
+ GCC_except_table2908
+ GCC_except_table2938
+ _DialogEngineLibraryCore.frameworkLibrary.12695
+ ___Block_byref_object_copy_.10567
+ ___Block_byref_object_copy_.12772
+ ___Block_byref_object_copy_.14184
+ ___Block_byref_object_copy_.14824
+ ___Block_byref_object_copy_.8763
+ ___Block_byref_object_dispose_.10568
+ ___Block_byref_object_dispose_.12773
+ ___Block_byref_object_dispose_.14185
+ ___Block_byref_object_dispose_.14825
+ ___Block_byref_object_dispose_.8764
+ ___DialogEngineLibraryCore_block_invoke.12696
+ ___block_literal_global.10078
+ ___block_literal_global.10556
+ ___block_literal_global.11000
+ ___block_literal_global.11081
+ ___block_literal_global.12103
+ ___block_literal_global.12223
+ ___block_literal_global.12294
+ ___block_literal_global.12350
+ ___block_literal_global.12779
+ ___block_literal_global.12814
+ ___block_literal_global.13324
+ ___block_literal_global.14155
+ ___block_literal_global.14442
+ ___block_literal_global.14775
+ ___block_literal_global.15047
+ ___block_literal_global.27.9509
+ ___block_literal_global.8805
+ ___block_literal_global.8956
+ ___block_literal_global.9185
+ ___block_literal_global.9251
+ ___block_literal_global.9412
+ ___block_literal_global.9508
+ ___block_literal_global.9736
+ ___block_literal_global.9929
+ _audit_stringDialogEngine.12700
- GCC_except_table2785
- GCC_except_table2789
- GCC_except_table2823
- GCC_except_table2827
- GCC_except_table2829
- GCC_except_table2839
- GCC_except_table2890
- GCC_except_table2902
- GCC_except_table2907
- GCC_except_table2937
- _DialogEngineLibraryCore.frameworkLibrary.12696
- ___Block_byref_object_copy_.10569
- ___Block_byref_object_copy_.12773
- ___Block_byref_object_copy_.14183
- ___Block_byref_object_copy_.14823
- ___Block_byref_object_copy_.8764
- ___Block_byref_object_dispose_.10570
- ___Block_byref_object_dispose_.12774
- ___Block_byref_object_dispose_.14184
- ___Block_byref_object_dispose_.14824
- ___Block_byref_object_dispose_.8765
- ___DialogEngineLibraryCore_block_invoke.12697
- ___block_literal_global.10079
- ___block_literal_global.10558
- ___block_literal_global.11002
- ___block_literal_global.11083
- ___block_literal_global.12104
- ___block_literal_global.12224
- ___block_literal_global.12295
- ___block_literal_global.12351
- ___block_literal_global.12780
- ___block_literal_global.12815
- ___block_literal_global.13325
- ___block_literal_global.14154
- ___block_literal_global.14441
- ___block_literal_global.14774
- ___block_literal_global.15046
- ___block_literal_global.27.9510
- ___block_literal_global.8806
- ___block_literal_global.8957
- ___block_literal_global.9186
- ___block_literal_global.9252
- ___block_literal_global.9413
- ___block_literal_global.9509
- ___block_literal_global.9737
- ___block_literal_global.9930
- _audit_stringDialogEngine.12701
Functions:
~ -[LNActionDefaultValueProvider loadActionMetadataWithRetry:error:] : 1180 -> 244
+ -[LNActionDefaultValueProvider _loadActionMetadataWithProvider:retry:error:]
CStrings:
+ "Forced registration completed for %{public}@, retry metadata fetch"
+ "Retrying metadata fetch for actionIdentifier %{public}@"
- "%{public}@ is registered, skipping forced indexing"
- "Failed to fetch bundles"

```
