## Coordination

> `/System/Library/PrivateFrameworks/Coordination.framework/Versions/A/Coordination`

```diff

-234.30.1.0.0
-  __TEXT.__text: 0x3eaf8
+234.40.2.0.0
+  __TEXT.__text: 0x3eaf4
   __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_methlist: 0x27f0
+  __TEXT.__objc_methlist: 0x2cfc
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0xfa0
+  __TEXT.__gcc_except_tab: 0xf9c
   __TEXT.__cstring: 0x15a2
   __TEXT.__oslogstring: 0x3058
-  __TEXT.__unwind_info: 0x1068
+  __TEXT.__unwind_info: 0x1088
   __TEXT.__objc_classname: 0x91e
   __TEXT.__objc_methname: 0x60fa
   __TEXT.__objc_methtype: 0x1118

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15a8
+  __DATA_CONST.__objc_selrefs: 0x1630
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x168
   __AUTH_CONST.__auth_got: 0x1e8
   __AUTH_CONST.__const: 0x14e0
   __AUTH_CONST.__cfstring: 0x15c0
-  __AUTH_CONST.__objc_const: 0x5d58
+  __AUTH_CONST.__objc_const: 0x54a8
   __AUTH.__objc_data: 0x1180
   __DATA.__objc_ivar: 0x2fc
   __DATA.__data: 0x960

   - /System/Library/PrivateFrameworks/Rapport.framework/Versions/A/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F38382F5-76AE-36BE-9765-9A871B9B4EFB
-  Functions: 1348
-  Symbols:   3200
+  UUID: E053D79C-D6CA-3A28-BFBC-8222915A8D30
+  Functions: 1354
+  Symbols:   3203
   CStrings:  1904
 
Symbols:
+ +[COCluster _allowedClusterClasses].cold.1
+ +[COClusterConfiguration domainPermittedCharacterSet].cold.1
+ +[COFeatureStatus isFastFoldEnabled].cold.1
+ +[COFeatureStatus isIPDiscoveryDiffingEnabled].cold.1
+ +[COKeyPath allowedCharacterSet].cold.1
+ -[COStateManager _onqueue_setDictionary:clusters:cacheLocally:completionHandler:].cold.2
+ COLogForCategory.cold.1
+ GCC_except_table132
- GCC_except_table136
- GCC_except_table144
- _OUTLINED_FUNCTION_10

```
