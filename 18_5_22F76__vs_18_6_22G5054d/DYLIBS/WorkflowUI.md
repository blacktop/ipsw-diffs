## WorkflowUI

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI`

```diff

-3607.0.2.0.0
-  __TEXT.__text: 0x2a906c
+3609.0.0.0.0
+  __TEXT.__text: 0x2a9344
   __TEXT.__auth_stubs: 0x6240
-  __TEXT.__objc_methlist: 0xc324
-  __TEXT.__const: 0x183a8
+  __TEXT.__objc_methlist: 0xc33c
+  __TEXT.__const: 0x187b8
   __TEXT.__dlopen_cstrs: 0x22e
-  __TEXT.__cstring: 0xf5fc
+  __TEXT.__cstring: 0xf64d
   __TEXT.__constg_swiftt: 0x97a0
   __TEXT.__swift5_typeref: 0x2719a
   __TEXT.__swift5_reflstr: 0x5673

   __TEXT.__swift5_proto: 0xbf8
   __TEXT.__swift5_types: 0x7a4
   __TEXT.__swift_as_entry: 0x13c
-  __TEXT.__oslogstring: 0x240e
+  __TEXT.__oslogstring: 0x2480
   __TEXT.__swift5_protos: 0x88
   __TEXT.__swift_as_ret: 0x11c
   __TEXT.__swift5_mpenum: 0x258
-  __TEXT.__gcc_except_tab: 0xc34
+  __TEXT.__gcc_except_tab: 0xc38
   __TEXT.__ustring: 0x30c
   __TEXT.__unwind_info: 0xab90
   __TEXT.__eh_frame: 0x629c
   __TEXT.__objc_classname: 0x203e
-  __TEXT.__objc_methname: 0x1fa78
+  __TEXT.__objc_methname: 0x1fae8
   __TEXT.__objc_methtype: 0x7389
-  __TEXT.__objc_stubs: 0x11c80
+  __TEXT.__objc_stubs: 0x11cc0
   __DATA_CONST.__got: 0x2690
-  __DATA_CONST.__const: 0x2158
+  __DATA_CONST.__const: 0x2180
   __DATA_CONST.__objc_classlist: 0x910
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x558
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7ab8
+  __DATA_CONST.__objc_selrefs: 0x7ac8
   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x440
   __DATA_CONST.__objc_arraydata: 0x1d0
   __AUTH_CONST.__auth_got: 0x3130
-  __AUTH_CONST.__const: 0x102d8
+  __AUTH_CONST.__const: 0x102f8
   __AUTH_CONST.__cfstring: 0x3c00
   __AUTH_CONST.__objc_const: 0x19908
   __AUTH_CONST.__objc_intobj: 0x5a0

   __AUTH.__objc_data: 0x7c38
   __AUTH.__data: 0x55a0
   __DATA.__objc_ivar: 0x838
-  __DATA.__data: 0xbad8
+  __DATA.__data: 0xb6a8
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x16808
   __DATA.__common: 0x1f0
   __DATA_DIRTY.__objc_data: 0x1110
-  __DATA_DIRTY.__data: 0x30e8
+  __DATA_DIRTY.__data: 0x30f8
   __DATA_DIRTY.__bss: 0x1d60
   __DATA_DIRTY.__common: 0xc8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: AEF094E6-8AB0-3481-8F5D-1336FDB872E9
-  Functions: 18000
-  Symbols:   22823
-  CStrings:  8505
+  UUID: A4DDB2D8-9C0B-3124-A518-1209BFE48B7C
+  Functions: 18003
+  Symbols:   22833
+  CStrings:  8511
 
Symbols:
+ -[WFCreateAutomationCoordinator cleanUpAbandonedTriggerIfNecessary]
+ -[WFCreateAutomationCoordinator dealloc]
+ -[WFCreateAutomationCoordinator setUnfinishedTriggerIdentifier:]
+ -[WFCreateAutomationCoordinator unfinishedTriggerIdentifier]
+ GCC_except_table2548
+ GCC_except_table2555
+ GCC_except_table2559
+ GCC_except_table2592
+ GCC_except_table2712
+ GCC_except_table2729
+ GCC_except_table2818
+ _HomeLibrary.sLib.15661
+ _HomeLibrary.sOnce.15658
+ _HomeUILibrary.sLib.15657
+ _HomeUILibrary.sOnce.15653
+ _OBJC_IVAR_$_WFCreateAutomationCoordinator._unfinishedTriggerIdentifier
+ _PassKitUILibraryCore.frameworkLibrary.18059
+ ___39-[WFCreateAutomationCoordinator cancel]_block_invoke.243
+ ___57-[WFCreateAutomationCoordinator finishWithTriggerRecord:]_block_invoke.240
+ ___67-[WFCreateAutomationCoordinator cleanUpAbandonedTriggerIfNecessary]_block_invoke
+ ___Block_byref_object_copy_.17179
+ ___Block_byref_object_dispose_.17180
+ ___HomeLibrary_block_invoke.15660
+ ___HomeUILibrary_block_invoke.15655
+ ___PassKitUILibraryCore_block_invoke.18060
+ ___block_descriptor_48_e8_32s40w_e20_v20?0B8"NSError"12lw40l8s32l8
+ ___block_literal_global.15622
+ ___block_literal_global.15864
+ ___block_literal_global.251
+ ___block_literal_global.428
+ ___block_literal_global.432
+ _audit_stringPassKitUI.18065
+ _objc_msgSend$cleanUpAbandonedTriggerIfNecessary
+ _objc_msgSend$setUnfinishedTriggerIdentifier:
+ _objc_msgSend$unfinishedTriggerIdentifier
- -[WFCreateAutomationCoordinator setTriggerIdentifier:]
- -[WFCreateAutomationCoordinator triggerIdentifier]
- GCC_except_table2546
- GCC_except_table2553
- GCC_except_table2557
- GCC_except_table2589
- GCC_except_table2709
- GCC_except_table2726
- GCC_except_table2815
- _HomeLibrary.sLib.15659
- _HomeLibrary.sOnce.15656
- _HomeUILibrary.sLib.15655
- _HomeUILibrary.sOnce.15652
- _OBJC_IVAR_$_WFCreateAutomationCoordinator._triggerIdentifier
- _PassKitUILibraryCore.frameworkLibrary.18055
- ___39-[WFCreateAutomationCoordinator cancel]_block_invoke.241
- ___57-[WFCreateAutomationCoordinator finishWithTriggerRecord:]_block_invoke.238
- ___Block_byref_object_copy_.17178
- ___Block_byref_object_dispose_.17179
- ___HomeLibrary_block_invoke.15658
- ___HomeUILibrary_block_invoke.15654
- ___PassKitUILibraryCore_block_invoke.18056
- ___block_literal_global.15623
- ___block_literal_global.15862
- ___block_literal_global.423
- ___block_literal_global.427
- _audit_stringPassKitUI.18061
- _objc_msgSend$setTriggerIdentifier:
CStrings:
+ "%s Attempted to finish trigger creation but trigger identifier was nil"
+ "%s Failed to delete configured trigger: %@"
+ "-[WFCreateAutomationCoordinator cleanUpAbandonedTriggerIfNecessary]_block_invoke"
+ "T@\"NSString\",&,N,V_unfinishedTriggerIdentifier"
+ "_unfinishedTriggerIdentifier"
+ "cleanUpAbandonedTriggerIfNecessary"
+ "setUnfinishedTriggerIdentifier:"
+ "unfinishedTriggerIdentifier"
- "T@\"NSString\",&,N,V_triggerIdentifier"
- "setTriggerIdentifier:"

```
