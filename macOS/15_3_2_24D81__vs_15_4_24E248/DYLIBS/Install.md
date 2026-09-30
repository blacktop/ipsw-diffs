## Install

> `/System/Library/PrivateFrameworks/Install.framework/Versions/A/Install`

```diff

-1604.0.0.0.0
-  __TEXT.__text: 0x6eff0
+1611.0.0.0.0
+  __TEXT.__text: 0x6efa4
   __TEXT.__auth_stubs: 0x20a0
-  __TEXT.__objc_methlist: 0x736c
+  __TEXT.__objc_methlist: 0x7970
   __TEXT.__const: 0x440
-  __TEXT.__cstring: 0xd275
+  __TEXT.__cstring: 0xd272
   __TEXT.__gcc_except_tab: 0x7ec
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1ef8
+  __TEXT.__unwind_info: 0x1f00
   __TEXT.__objc_classname: 0x11e1
   __TEXT.__objc_methname: 0xe173
   __TEXT.__objc_methtype: 0x2212
   __TEXT.__objc_stubs: 0xd7a0
-  __DATA_CONST.__got: 0x880
+  __DATA_CONST.__got: 0x868
   __DATA_CONST.__const: 0x848
   __DATA_CONST.__objc_classlist: 0x470
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4228
+  __DATA_CONST.__objc_selrefs: 0x4360
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x3b0
   __AUTH_CONST.__auth_got: 0x1060
   __AUTH_CONST.__const: 0x3b8
   __AUTH_CONST.__cfstring: 0xafe0
-  __AUTH_CONST.__objc_const: 0xb588
+  __AUTH_CONST.__objc_const: 0xaa50
   __AUTH.__objc_data: 0x2c60
   __AUTH.__data: 0xd68
   __DATA.__objc_ivar: 0x7c8

   - /usr/lib/libxar.1.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 63C2E272-DD64-3975-9EA3-B3630F2C7E01
-  Functions: 2668
-  Symbols:   7018
-  CStrings:  6654
+  UUID: 7DFDC8FD-D435-38E5-A686-39A1067631E1
+  Functions: 2680
+  Symbols:   7040
+  CStrings:  6653
 
Symbols:
+ -[IFInstallPlan removeValueForAttribute:].cold.1
+ -[IFInstallPlan setAlternatePath:forNode:].cold.1
+ -[IFInstallPlan setValue:forAttribute:].cold.1
+ -[IFInstallPlan setValue:forAttribute:].cold.2
+ -[IFInstallPlan valueForAttribute:].cold.1
+ -[IFTaskElement run].cold.1
+ -[NSString(JRCNSStringRegEx) componentsMatchingByPattern:count:].cold.1
+ -[TreeNode(TreeNode_Attributes) removeValueForAttribute:].cold.1
+ -[TreeNode(TreeNode_Attributes) setValue:forAttribute:].cold.1
+ -[TreeNode(TreeNode_Attributes) setValue:forAttribute:].cold.2
+ -[TreeNode(TreeNode_Attributes) valueForAttribute:].cold.1
+ IFJS_IFDTargetGetProperty.cold.1
+ IFJS_SystemBootROMFeatureFlagsMakeGetProperty.cold.1
+ IFJS_SystemBootROMSupportsAPFSMakeGetProperty.cold.1
+ IFJS_SystemFilesCurrentPPDVersionCache.cold.1
+ IFJS_SystemFilesUsePPDVersionCacheIfCurrent.cold.1
+ IFJS_SystemPPDVersionAtPathFunction.cold.1
+ IFJS_SystemPlistAtPathFunction.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
CStrings:
- ".."

```
