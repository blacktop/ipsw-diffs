## SafariShared

> `/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared`

```diff

-625.2.5.10.1
-  __TEXT.__text: 0x2a442c
-  __TEXT.__objc_methlist: 0x1617c
-  __TEXT.__const: 0xa3854
-  __TEXT.__gcc_except_tab: 0x1ebe0
-  __TEXT.__cstring: 0x23827
+625.2.7.1.0
+  __TEXT.__text: 0x2a5328
+  __TEXT.__objc_methlist: 0x16184
+  __TEXT.__const: 0xa3a94
+  __TEXT.__gcc_except_tab: 0x1ec3c
+  __TEXT.__cstring: 0x23847
   __TEXT.__ustring: 0xcec0
-  __TEXT.__oslogstring: 0x15cc2
+  __TEXT.__oslogstring: 0x15cb2
   __TEXT.__dlopen_cstrs: 0x2b7
-  __TEXT.__swift5_typeref: 0x36ca
+  __TEXT.__swift5_typeref: 0x374a
   __TEXT.__swift5_fieldmd: 0x18c4
-  __TEXT.__constg_swiftt: 0x21c0
+  __TEXT.__constg_swiftt: 0x21c8
   __TEXT.__swift5_builtin: 0x190
-  __TEXT.__swift5_reflstr: 0x1668
+  __TEXT.__swift5_reflstr: 0x1648
   __TEXT.__swift5_assocty: 0x450
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_proto: 0x400

   __TEXT.__swift_as_entry: 0x184
   __TEXT.__swift_as_ret: 0x16c
   __TEXT.__swift_as_cont: 0x2f0
-  __TEXT.__unwind_info: 0x114c0
-  __TEXT.__eh_frame: 0x5590
+  __TEXT.__unwind_info: 0x114f0
+  __TEXT.__eh_frame: 0x55e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x2c8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc188
+  __DATA_CONST.__objc_selrefs: 0xc1a0
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x960
   __DATA_CONST.__objc_arraydata: 0xb00
   __DATA_CONST.__got: 0x2120
   __AUTH_CONST.__const: 0xb4f0
-  __AUTH_CONST.__cfstring: 0x1b0c0
-  __AUTH_CONST.__objc_const: 0x285f8
+  __AUTH_CONST.__cfstring: 0x1b0e0
+  __AUTH_CONST.__objc_const: 0x28638
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x768
   __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__auth_got: 0x2d70
+  __AUTH_CONST.__auth_got: 0x2d78
   __AUTH.__objc_data: 0x7c78
-  __AUTH.__data: 0x1798
-  __DATA.__objc_ivar: 0x1940
-  __DATA.__data: 0x57c8
+  __AUTH.__data: 0x17b0
+  __DATA.__objc_ivar: 0x1944
+  __DATA.__data: 0x5848
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x9

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14790
-  Symbols:   19354
-  CStrings:  6158
+  Functions: 14802
+  Symbols:   19359
+  CStrings:  6159
 
Symbols:
+ +[WBSTrialManager prepareLogDictionary:withExperimentId:withTreatmentId:withRolloutId:isCounterFactualSearch:withFactorData:]
+ -[WBSTabOrderManager _nextNonClosedTabAdjacentToIndex:inAscendingOrder:foundIndex:]
+ -[WBSTabOrderManager _nextTabSkippingCollapsedClustersFromIndex:inAscendingOrder:]
+ -[WBSTrialManager inExperimentOrRollout]
+ _OBJC_IVAR_$_WBSTrialManager._rolloutId
+ ___swift_closure_destructor.179Tm
+ _symbolic Say_____yxGG 12SafariShared25WBSBookmarksFolderClusterV
+ _symbolic _____7cluster_SDySSSiG13itemPositionst 12SafariShared17WBSClusterManagerC7ClusterV
+ _symbolic ___________7cluster_SDySSSiG13itemPositionstt 10Foundation4UUIDV 12SafariShared17WBSClusterManagerC7ClusterV
+ _symbolic _____y__________7cluster_SDySSSiG13itemPositionstG s18_DictionaryStorageC 10Foundation4UUIDV 12SafariShared17WBSClusterManagerC7ClusterV
- +[WBSTrialManager prepareLogDictionary:withExperimentId:withTreatmentId:isCounterFactualSearch:withFactorData:]
- -[WBSTabOrderManager _nextNonClosedTabAdjacentToIndex:inAscendingOrder:]
- -[WBSTabOrderManager _nextTabSkippingCollapsedClustersFromTab:inAscendingOrder:]
- ___swift_closure_destructor.178Tm
- _symbolic Say_____yxGGSg 12SafariShared25WBSBookmarksFolderClusterV
CStrings:
+ "8625.2.7.1"
+ "Factor \"%@\" has value of %@ from Trial"
+ "Not enrolled in a rollout"
+ "Not enrolled in an experiment or rollout"
+ "Rollout ID"
- "8625.2.5.10.1"
- "Factor \"%@\" has value of %@ from the experiment"
- "Unknown Experiment ID"
- "Unknown Treatment ID"
```
