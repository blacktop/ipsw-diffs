## SpotlightResources

> `/System/Library/PrivateFrameworks/SpotlightResources.framework/Versions/A/SpotlightResources`

```diff

-2454.100.0.0.0
-  __TEXT.__text: 0x2dfd4
-  __TEXT.__objc_methlist: 0x1628
-  __TEXT.__const: 0x128
+2459.405.0.0.0
+  __TEXT.__text: 0x2e0b0
+  __TEXT.__objc_methlist: 0x1630
+  __TEXT.__const: 0x138
   __TEXT.__gcc_except_tab: 0xf58
-  __TEXT.__cstring: 0x2308
-  __TEXT.__oslogstring: 0x2517
-  __TEXT.__unwind_info: 0x8d8
+  __TEXT.__cstring: 0x2310
+  __TEXT.__oslogstring: 0x2531
+  __TEXT.__unwind_info: 0x8e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1118
+  __DATA_CONST.__objc_selrefs: 0x1120
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x930
   __DATA_CONST.__got: 0x280
   __AUTH_CONST.__const: 0x1300
-  __AUTH_CONST.__cfstring: 0x45a0
+  __AUTH_CONST.__cfstring: 0x45c0
   __AUTH_CONST.__objc_const: 0x2380
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x48

   - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/Versions/A/UnifiedAssetFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 886
-  Symbols:   1882
-  CStrings:  875
+  Functions: 887
+  Symbols:   1883
+  CStrings:  876
 
Symbols:
+ +[SRResourcesManager trialSpotlightUITreatmentID]
Functions:
+ +[SRResourcesManager trialSpotlightUITreatmentID]
~ ___SRShouldLoadFromUAF_block_invoke : 176 -> 216
~ -[SSTrialManager loadWithUpdateHandler:] : 1572 -> 1600
- _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
~ -[SSTrialManager loadWithUpdateHandler:].cold.2 : 156 -> 204
~ +[SSTrialManager didAllNamespacesLoadForClient:].cold.1 : 92 -> 100
~ +[SSTrialManager didAllNamespacesLoadForClient:].cold.2 : 92 -> 100
~ +[SSTrialManager didAllNamespacesLoadForClient:].cold.3 : 92 -> 100
~ +[SSTrialManager didAllNamespacesLoadForClient:].cold.4 : 92 -> 100
CStrings:
+ ".xctest"
+ "Before loading namespace %@: _hasActiveExperiment = %@ (treatmentID: %s), _hasRollout = %@, _hasOverride = %@"
+ "ns:%s, exp:%d, trt:%s, ro:%d, over:%d"
- "Before loading namespace %@: _hasActiveExperiment = %@, _hasRollout = %@, _hasOverride = %@"
- "ns:%s, exp:%d, ro:%d, over:%d"
```
