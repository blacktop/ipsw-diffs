## RunningBoardServices

> `/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices`

```diff

-1008.80.2.0.0
-  __TEXT.__text: 0x42424
-  __TEXT.__auth_stubs: 0xe20
-  __TEXT.__objc_methlist: 0x5a68
+1015.100.15.0.0
+  __TEXT.__text: 0x44034
+  __TEXT.__auth_stubs: 0xdc0
+  __TEXT.__objc_methlist: 0x5b70
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x481a
+  __TEXT.__cstring: 0x48bb
   __TEXT.__oslogstring: 0x2768
-  __TEXT.__gcc_except_tab: 0x92c
+  __TEXT.__gcc_except_tab: 0x8d4
   __TEXT.__dlopen_cstrs: 0x76
-  __TEXT.__unwind_info: 0x1650
-  __TEXT.__objc_classname: 0xf04
-  __TEXT.__objc_methname: 0x80cf
+  __TEXT.__unwind_info: 0x1898
+  __TEXT.__objc_classname: 0xf3c
+  __TEXT.__objc_methname: 0x81a3
   __TEXT.__objc_methtype: 0x1595
-  __TEXT.__objc_stubs: 0x4ae0
-  __DATA_CONST.__got: 0x4d8
+  __TEXT.__objc_stubs: 0x4b60
+  __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__const: 0xcf0
-  __DATA_CONST.__objc_classlist: 0x440
+  __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d00
+  __DATA_CONST.__objc_selrefs: 0x1d30
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2d8
-  __AUTH_CONST.__auth_got: 0x720
+  __DATA_CONST.__objc_superrefs: 0x2e8
+  __AUTH_CONST.__auth_got: 0x6f0
   __AUTH_CONST.__const: 0x660
-  __AUTH_CONST.__cfstring: 0x5ee0
-  __AUTH_CONST.__objc_const: 0xad18
+  __AUTH_CONST.__cfstring: 0x5fc0
+  __AUTH_CONST.__objc_const: 0xaf78
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x1680
-  __DATA.__objc_ivar: 0x5c4
+  __AUTH.__objc_data: 0x1720
+  __DATA.__objc_ivar: 0x5d4
   __DATA.__data: 0x620
   __DATA.__bss: 0x260
   __DATA_DIRTY.__objc_data: 0x1400

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED9E8ED5-E812-3138-986D-7B73FCE93985
-  Functions: 2257
-  Symbols:   7106
-  CStrings:  3691
+  UUID: D82AA987-9B3E-3F47-AC87-55AA1C1B8CC2
+  Functions: 2332
+  Symbols:   7309
+  CStrings:  3719
 
Symbols:
+ +[RBSPrefetchPageAttribute initWithScenario:]
+ +[RBSPrefetchPageAttribute initWithScenario:].cold.1
+ +[RBSProcessPrefetchPageScenario initWithScenario:]
+ +[RBSProcessPrefetchPageScenario supportsRBSXPCSecureCoding]
+ -[RBSLaunchContext psPageIn]
+ -[RBSLaunchContext setPsPageIn:]
+ -[RBSPrefetchPageAttribute description]
+ -[RBSPrefetchPageAttribute hash]
+ -[RBSPrefetchPageAttribute isEqual:]
+ -[RBSPrefetchPageAttribute scenario]
+ -[RBSProcessPrefetchPageScenario copyWithZone:]
+ -[RBSProcessPrefetchPageScenario description]
+ -[RBSProcessPrefetchPageScenario encodeWithRBSXPCCoder:]
+ -[RBSProcessPrefetchPageScenario hash]
+ -[RBSProcessPrefetchPageScenario initWithRBSXPCCoder:]
+ -[RBSProcessPrefetchPageScenario initWithScenario:]
+ -[RBSProcessPrefetchPageScenario isEqual:]
+ -[RBSProcessPrefetchPageScenario scenario]
+ -[RBSProcessState prefetchPageScenarios]
+ -[RBSProcessState setPrefetchPageScenarios:]
+ _OBJC_CLASS_$_RBSPrefetchPageAttribute
+ _OBJC_CLASS_$_RBSProcessPrefetchPageScenario
+ _OBJC_IVAR_$_RBSLaunchContext._psPageIn
+ _OBJC_IVAR_$_RBSPrefetchPageAttribute._scenario
+ _OBJC_IVAR_$_RBSProcessPrefetchPageScenario._scenario
+ _OBJC_IVAR_$_RBSProcessState._prefetchPageScenarios
+ _OBJC_METACLASS_$_RBSPrefetchPageAttribute
+ _OBJC_METACLASS_$_RBSProcessPrefetchPageScenario
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ __OBJC_$_CLASS_METHODS_RBSPrefetchPageAttribute
+ __OBJC_$_CLASS_METHODS_RBSProcessPrefetchPageScenario
+ __OBJC_$_INSTANCE_METHODS_RBSPrefetchPageAttribute
+ __OBJC_$_INSTANCE_METHODS_RBSProcessPrefetchPageScenario
+ __OBJC_$_INSTANCE_VARIABLES_RBSPrefetchPageAttribute
+ __OBJC_$_INSTANCE_VARIABLES_RBSProcessPrefetchPageScenario
+ __OBJC_$_PROP_LIST_RBSPrefetchPageAttribute
+ __OBJC_$_PROP_LIST_RBSProcessPrefetchPageScenario
+ __OBJC_CLASS_PROTOCOLS_$_RBSProcessPrefetchPageScenario
+ __OBJC_CLASS_RO_$_RBSPrefetchPageAttribute
+ __OBJC_CLASS_RO_$_RBSProcessPrefetchPageScenario
+ __OBJC_METACLASS_RO_$_RBSPrefetchPageAttribute
+ __OBJC_METACLASS_RO_$_RBSProcessPrefetchPageScenario
+ _objc_msgSend$initWithScenario:
+ _objc_msgSend$psPageIn
+ _objc_msgSend$setPrefetchPageScenarios:
+ _objc_msgSend$setPsPageIn:
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
CStrings:
+ " prefetchPageScenarios:[\n\t"
+ "<%@| scenario:%llu>"
+ "<%@| task:%@ debug:%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@>"
+ "RBSPrefetchPageAttribute"
+ "RBSPrefetchPageAttribute.m"
+ "RBSProcessPrefetchPageScenario"
+ "T@\"NSSet\",C,N,V_prefetchPageScenarios"
+ "TB,N,V_psPageIn"
+ "TQ,R,N,V_scenario"
+ "_prefetchPageScenarios"
+ "_psPageIn"
+ "_scenario"
+ "initWithScenario:"
+ "initialized with invalid scenario: %llu"
+ "prefetchPageScenarios"
+ "psPageIn"
+ "scenario"
+ "setPrefetchPageScenarios:"
+ "setPsPageIn:"
- "<%@| task:%@ debug:%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@>"

```
