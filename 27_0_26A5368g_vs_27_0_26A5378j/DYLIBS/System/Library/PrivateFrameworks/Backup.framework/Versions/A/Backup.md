## Backup

> `/System/Library/PrivateFrameworks/Backup.framework/Versions/A/Backup`

```diff

-  __TEXT.__text: 0x824d8
-  __TEXT.__objc_methlist: 0x1c00
+  __TEXT.__text: 0x82404
+  __TEXT.__objc_methlist: 0x1c10
   __TEXT.__const: 0x3c3e
-  __TEXT.__gcc_except_tab: 0xb524
-  __TEXT.__cstring: 0x3b34
+  __TEXT.__gcc_except_tab: 0xb51c
+  __TEXT.__cstring: 0x3b42
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x48e0
+  __TEXT.__unwind_info: 0x48e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1938
+  __DATA_CONST.__objc_selrefs: 0x1940
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__got: 0x0
+  __DATA_CONST.__got: 0x598
   __AUTH_CONST.__const: 0x46f8
-  __AUTH_CONST.__cfstring: 0x3fa0
+  __AUTH_CONST.__cfstring: 0x3fc0
   __AUTH_CONST.__objc_const: 0x2aa8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x78

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3089
-  Symbols:   7012
-  CStrings:  1171
+  Functions: 3090
+  Symbols:   7013
+  CStrings:  1173
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ +[BU_TUserDefaults sendSmartNamingEnablementTelemetry]
Functions:
~ __ZNSt3__135__uninitialized_allocator_copy_implB9nqe220106INS_9allocatorI7TStringEEPS2_S4_S4_EET2_RT_T0_T1_S5_ : 184 -> 168
~ __ZN17TBackupController20ResetSnapshotTargetsERKNSt3__16vectorINS0_10shared_ptrI18TTimeMachineTargetEENS0_9allocatorIS4_EEEEbb : 496 -> 504
~ __ZN17TBackupController19FindNextValidTargetERKNSt3__110shared_ptrI18TTimeMachineTargetEE : 300 -> 304
~ __ZN16TTimelineControl12SetSnapshotsERKNSt3__16vectorINS0_10shared_ptrI18TTimeMachineTargetEENS0_9allocatorIS4_EEEE : 460 -> 448
~ __ZN16TTimelineControl14GenerateLayoutEv : 2404 -> 2392
~ __ZN16algorithm_extras11erase_firstI13TFENodeVector7TFENodeEENT_8iteratorERS3_RKT0_ : 212 -> 204
~ __ZNSt3__116__insertion_sortB9nqe220106INS_17_ClassicAlgPolicyERPFbRKNS_10shared_ptrI18TTimeMachineTargetEES6_EPS4_EEvT1_SB_T0_ : 320 -> 276
~ __ZNSt3__126__insertion_sort_unguardedB9nqe220106INS_17_ClassicAlgPolicyERPFbRKNS_10shared_ptrI18TTimeMachineTargetEES6_EPS4_EEvT1_SB_T0_ : 276 -> 256
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERPFbRKNS_10shared_ptrI18TTimeMachineTargetEES6_EPS4_EEbT1_SB_T0_ : 932 -> 884
~ -[BUStarfieldTimelineLayer handleReloadData] : 536 -> 544
~ __ZNSt3__15dequeIfNS_9allocatorIfEEE19__add_back_capacityEv : 480 -> 468
~ __ZNSt3__135__uninitialized_allocator_copy_implB9nqe220106INS_9allocatorI7TStringEEPKS2_S5_PS2_EET2_RT_T0_T1_S7_ : 152 -> 136
~ __ZNSt3__111basic_regexIcNS_12regex_traitsIcEEE25__parse_equivalence_classIPKcEET_S7_S7_PNS_20__bracket_expressionIcS2_EE : 524 -> 500
~ __ZNSt3__111basic_regexIcNS_12regex_traitsIcEEE23__parse_character_classIPKcEET_S7_S7_PNS_20__bracket_expressionIcS2_EE : 176 -> 152
~ __ZNSt3__111basic_regexIcNS_12regex_traitsIcEEE24__parse_collating_symbolIPKcEET_S7_S7_RNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE : 228 -> 204
~ __ZNSt3__15dequeINS_7__stateIcEENS_9allocatorIS2_EEE19__add_back_capacityEv : 480 -> 468
~ __Z11ParseFormatRKNSt3__117basic_string_viewIcNS_11char_traitsIcEEEE : 3216 -> 3224
+ +[BU_TUserDefaults sendSmartNamingEnablementTelemetry]
~ __ZNK15TFIFOQueueStyleINSt3__14pairIyP17TWorkerThreadDataEEE7EnqueueERNS0_6vectorIS4_NS0_9allocatorIS4_EEEEOS9_ : 144 -> 152
~ __ZNK15TFIFOQueueStyleINSt3__14pairIyP17TWorkerThreadDataEEE7DequeueERNS0_6vectorIS4_NS0_9allocatorIS4_EEEESA_ : 104 -> 112
~ __ZNK15TFILOQueueStyleINSt3__14pairIyP17TWorkerThreadDataEEE7DequeueERNS0_6vectorIS4_NS0_9allocatorIS4_EEEESA_ : 104 -> 112
~ __ZN23TCoalescingNodeObserver19RunDeferredHandlersEv : 1344 -> 1340
~ __ZNSt3__16vectorI18TBrowseDestinationNS_9allocatorIS1_EEE22__base_destruct_at_endB9nqe220106EPS1_ : 96 -> 84
~ __ZZL8RegistryvENK3$_0clEv : 3284 -> 3304
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oi86ul/Sources/Finder_Backup/BackupFramework/Browser/BUBackup.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oi86ul/Sources/Finder_Backup/BackupFramework/Public/BackupPrivNew.cp"
+ "icloud.dashed"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iU52xa/Sources/Finder_Backup/BackupFramework/Browser/BUBackup.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iU52xa/Sources/Finder_Backup/BackupFramework/Public/BackupPrivNew.cp"

```
