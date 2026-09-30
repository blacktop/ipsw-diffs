## SymptomAnalytics

> `/System/Library/PrivateFrameworks/Symptoms.framework/Versions/A/Frameworks/SymptomAnalytics.framework/Versions/A/SymptomAnalytics`

```diff

-2001.80.5.0.0
-  __TEXT.__text: 0xa258
+2022.100.26.0.0
+  __TEXT.__text: 0xa254
   __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_methlist: 0x8f8
+  __TEXT.__objc_methlist: 0xaa8
   __TEXT.__cstring: 0xeee
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x384
+  __TEXT.__gcc_except_tab: 0x390
   __TEXT.__oslogstring: 0xe61
   __TEXT.__unwind_info: 0x298
   __TEXT.__objc_classname: 0x21e
-  __TEXT.__objc_methname: 0x2c1c
-  __TEXT.__objc_methtype: 0x997
+  __TEXT.__objc_methname: 0x2c4d
+  __TEXT.__objc_methtype: 0x9bb
   __TEXT.__objc_stubs: 0x1a00
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__const: 0x4d0
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8b0
+  __DATA_CONST.__objc_selrefs: 0x980
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x138
   __AUTH_CONST.__const: 0x1d0
   __AUTH_CONST.__cfstring: 0x19a0
-  __AUTH_CONST.__objc_const: 0x29d0
+  __AUTH_CONST.__objc_const: 0x26f8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x8c

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 39D9BD85-1F1B-3CA0-8F63-24AE357CDF90
-  Functions: 202
-  Symbols:   911
-  CStrings:  1166
+  UUID: 3CA65152-0D86-31C2-98A3-D99F53940640
+  Functions: 203
+  Symbols:   912
+  CStrings:  1171
 
Symbols:
+ __22-[NWActivityXPC start]_block_invoke.50
+ objectanalyticsHandle.cold.1
- __22-[NWActivityXPC start]_block_invoke.49
Functions:
~ _objectanalyticsHandle : 84 -> 68
~ +[AnalyticsWorkspace retrieveWorkspaceWithName:atPath:queue:resultCallback:] : 844 -> 840
~ -[AnalyticsWorkspace initWorkspaceWithName:atPath:objectModelName:objectModelBundle:useReadOnly:] : 228 -> 232
~ -[AnalyticsWorkspace persistentStoreCoordinator] : 3568 -> 3584
~ -[AnalyticsWorkspace mainObjectContext] : 228 -> 232
~ -[AnalyticsWorkspace createNewContext] : 180 -> 184
~ -[AnalyticsWorkspace reset] : 132 -> 136
~ -[AnalyticsWorkspace save] : 496 -> 500
~ -[AnalyticsWorkspace canCloneObjectsOfType:] : 308 -> 312
~ -[AnalyticsWorkspace _cloneInternal:intoWorkspace:ancestry:iteration:mustFail:] : 1484 -> 1476
~ -[AnalyticsWorkspace _primePath:] : 960 -> 952
~ -[AnalyticsWorkspace _migrateDBFile:] : 2048 -> 2044
~ -[NWActivityXPC retrieveMetricsForActivity:completion:] : 1560 -> 1552
~ ___55-[NWActivityXPC retrieveMetricsForActivity:completion:]_block_invoke : 380 -> 364
CStrings:
+ "btIN"
+ "btIN_exp"
+ "btOUT"
+ "btOUT_exp"
+ "donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:latitude:longitude:reply:"
+ "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40d48d56@?<v@?@\"NSDictionary\"@\"NSError\">64"
+ "v72@0:8@16@24@32@40d48d56@?64"
- "donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:reply:"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"

```
