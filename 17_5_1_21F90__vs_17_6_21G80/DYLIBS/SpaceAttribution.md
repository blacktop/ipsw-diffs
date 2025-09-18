## SpaceAttribution

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution`

```diff

-180.122.2.0.0
-  __TEXT.__text: 0xda5c
+180.140.5.0.0
+  __TEXT.__text: 0xe154
   __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_methlist: 0xcac
+  __TEXT.__objc_methlist: 0xce8
   __TEXT.__const: 0xa0
   __TEXT.__cstring: 0xb92
-  __TEXT.__oslogstring: 0xce9
-  __TEXT.__gcc_except_tab: 0x500
-  __TEXT.__unwind_info: 0x458
+  __TEXT.__oslogstring: 0xd88
+  __TEXT.__gcc_except_tab: 0x520
+  __TEXT.__unwind_info: 0x474
   __TEXT.__objc_classname: 0x13a
-  __TEXT.__objc_methname: 0x20e8
-  __TEXT.__objc_methtype: 0x6fd
-  __TEXT.__objc_stubs: 0x15a0
+  __TEXT.__objc_methname: 0x2198
+  __TEXT.__objc_methtype: 0x742
+  __TEXT.__objc_stubs: 0x15e0
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x3d8
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1270
-  __DATA_CONST.__objc_selrefs: 0x918
+  __DATA_CONST.__objc_const: 0x1290
+  __DATA_CONST.__objc_selrefs: 0x948
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x58

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 686F8FDA-8F26-3F3E-B947-9FEBD713EFD2
-  Functions: 429
-  Symbols:   1435
-  CStrings:  834
+  UUID: 4ED6770C-9478-3686-A2D1-8AB00D30E354
+  Functions: 442
+  Symbols:   1464
+  CStrings:  844
 
Symbols:
+ +[SAInternalAPI setForceTelemetry:]
+ +[SASupport clearSpeculativeHierarchyForPath:]
+ +[SASupport clearSpeculativeHierarchyForPath:].cold.1
+ +[SASupport clearSpeculativeHierarchyForPath:].cold.2
+ +[SASupport getINodeForDirStatKey:ofMount:]
+ +[SASupport getINodeForDirStatKey:ofMount:].cold.1
+ +[SASupport getPathOfiNode:inVolume:]
+ +[SASupport setSpeculativeHierarchy:purgeable:]
+ +[SASupport setSpeculativeHierarchy:purgeable:].cold.1
+ +[SASupport setSpeculativeHierarchy:purgeable:].cold.2
+ +[SAUtilities breakCommaSeparatedStringToComponents:]
+ GCC_except_table36
+ GCC_except_table39
+ GCC_except_table42
+ GCC_except_table49
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ ___35+[SAInternalAPI setForceTelemetry:]_block_invoke
+ ___35+[SAInternalAPI setForceTelemetry:]_block_invoke_2
+ ___35+[SAInternalAPI setForceTelemetry:]_block_invoke_3
+ ___38-[SADaemonXPC setInvalidationHandler:]_block_invoke.85
+ ___38-[SADaemonXPC setInvalidationHandler:]_block_invoke.85.cold.1
+ ___block_literal_global.87
+ __unnamed_array_storage.54
+ _objc_msgSend$setForceTelemetry:
+ _objc_msgSend$stringWithCString:encoding:
- +[SASupport setSpeculativeHierarcy:purgeable:]
- +[SASupport setSpeculativeHierarcy:purgeable:].cold.1
- +[SASupport setSpeculativeHierarcy:purgeable:].cold.2
- GCC_except_table35
- GCC_except_table38
- GCC_except_table41
- GCC_except_table8
- ___38-[SADaemonXPC setInvalidationHandler:]_block_invoke.84
- ___38-[SADaemonXPC setInvalidationHandler:]_block_invoke.84.cold.1
- ___block_literal_global.86
- __unnamed_array_storage.53
CStrings:
+ "@32@0:8Q16^{statfs=IiQQQQQ{fsid=[2i]}IIII[16c][1024c][1024c]I[7I]}24"
+ "APFSIOC_SPEC_TELEM_OP (set) failed for %@ with %s"
+ "APFSIOC_SPEC_TELEM_OP (unset) failed for %@ with %s"
+ "INodeForDirStatKey: APFSIOC_DIR_STATS_OP for %llu returned errno %u"
+ "Un-Setting hierarchy on path %s."
+ "breakCommaSeparatedStringToComponents:"
+ "clearSpeculativeHierarchyForPath:"
+ "getINodeForDirStatKey:ofMount:"
+ "getPathOfiNode:inVolume:"
+ "setForceTelemetry:"
+ "setSpeculativeHierarchy:purgeable:"
+ "stringWithCString:encoding:"
- "APFSIOC_SPEC_TELEM_OP failed for %@ with %s"
- "setSpeculativeHierarcy:purgeable:"

```
