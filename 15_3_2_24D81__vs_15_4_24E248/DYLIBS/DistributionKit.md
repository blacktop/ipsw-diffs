## DistributionKit

> `/System/Library/PrivateFrameworks/Install.framework/Frameworks/DistributionKit.framework/Versions/A/DistributionKit`

```diff

-1604.0.0.0.0
-  __TEXT.__text: 0x13934
-  __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_methlist: 0xd44
+1611.0.0.0.0
+  __TEXT.__text: 0x13d9c
+  __TEXT.__auth_stubs: 0xaf0
+  __TEXT.__objc_methlist: 0xed4
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x2f4d
-  __TEXT.__gcc_except_tab: 0x18c
+  __TEXT.__cstring: 0x3009
+  __TEXT.__gcc_except_tab: 0x198
   __TEXT.__unwind_info: 0x648
-  __TEXT.__objc_classname: 0x271
-  __TEXT.__objc_methname: 0x362c
-  __TEXT.__objc_methtype: 0x69a
-  __TEXT.__objc_stubs: 0x35e0
-  __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0x168
+  __TEXT.__objc_classname: 0x27e
+  __TEXT.__objc_methname: 0x36d1
+  __TEXT.__objc_methtype: 0x69e
+  __TEXT.__objc_stubs: 0x36c0
+  __DATA_CONST.__got: 0x380
+  __DATA_CONST.__const: 0x140
   __DATA_CONST.__objc_classlist: 0x78
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1008
+  __DATA_CONST.__objc_selrefs: 0x10c8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x580
-  __AUTH_CONST.__const: 0x490
-  __AUTH_CONST.__cfstring: 0x2180
-  __AUTH_CONST.__objc_const: 0x1af8
+  __AUTH_CONST.__auth_got: 0x588
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0x21a0
+  __AUTH_CONST.__objc_const: 0x18b0
   __AUTH.__objc_data: 0x4b0
   __AUTH.__data: 0xde8
   __DATA.__objc_ivar: 0x138

   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/Versions/A/RemoteServiceDiscovery
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 223FA1FA-FCD2-3A2A-A189-780197B604DD
-  Functions: 476
-  Symbols:   1498
-  CStrings:  1470
+  UUID: EFF4D221-878C-3D03-BF30-13B72058E6D3
+  Functions: 481
+  Symbols:   1524
+  CStrings:  1482
 
Symbols:
+ +[PKDistributionController _evaluationQueue].cold.1
+ -[NSPredicate(Sanitization) _pk_allExpressions]
+ -[NSPredicate(Sanitization) _pk_containsBlockOrFunctionPredicatesOrExpressions]
+ -[PKDistributionChoiceItem(BindingAdaptorAdditions) setButtonCellValue:].cold.1
+ -[PKDistributionChoiceTitleButtonCell setObjectValue:].cold.1
+ GCC_except_table10
+ IFJS_SystemBootROMFeatureFlagsMakeGetProperty.cold.1
+ IFJS_SystemBootROMSupportsAPFSMakeGetProperty.cold.1
+ IFJS_SystemFilesCurrentPPDVersionCache.cold.1
+ IFJS_SystemFilesUsePPDVersionCacheIfCurrent.cold.1
+ IFJS_SystemPPDVersionAtPathFunction.cold.1
+ IFJS_SystemPlistAtPathFunction.cold.1
+ IFJS_TargetGetProperty.cold.1
+ _NSPOSIXErrorDomain
+ _OBJC_CLASS_$_NSBlockPredicate
+ _OBJC_CLASS_$_NSComparisonPredicate
+ _OBJC_CLASS_$_NSCompoundPredicate
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_NSPredicate
+ __65-[PKDistributionHelperController fileAtPathOnTrustedGraft:error:]_block_invoke.13
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSPredicate_$_Sanitization
+ __OBJC_$_CATEGORY_NSPredicate_$_Sanitization
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8l
+ _objc_msgSend$_pk_allExpressions
+ _objc_msgSend$_pk_containsBlockOrFunctionPredicatesOrExpressions
+ _objc_msgSend$expressionType
+ _objc_msgSend$fileHandleIsOnGraft:reply:
+ _objc_msgSend$initWithFileDescriptor:closeOnDealloc:
+ _objc_msgSend$leftExpression
+ _objc_msgSend$rightExpression
+ _objc_msgSend$subpredicates
+ _open
- -[PKDistributionHelperController _synchronousProxy]
- GCC_except_table12
- ___51-[PKDistributionHelperController _synchronousProxy]_block_invoke
- ___block_descriptor_32_e17_v16?0"NSError"8l
- _objc_msgSend$fileAtPathExistsOnGraft:reply:
CStrings:
+ "%s: Object proxy returned an error. %s"
+ "- Failed to evaluate predicate: %@ (contains block or function)"
+ "-[PKDistributionHelperController fileAtPathOnTrustedGraft:error:]_block_invoke"
+ "Package Authoring Error: Failed to evaluate %s requirement \"%s\" (contains block or function)"
+ "Sanitization"
+ "_pk_allExpressions"
+ "_pk_containsBlockOrFunctionPredicatesOrExpressions"
+ "expressionType"
+ "fileHandleIsOnGraft:reply:"
+ "initWithFileDescriptor:closeOnDealloc:"
+ "leftExpression"
+ "rightExpression"
+ "subpredicates"
+ "v32@0:8@\"NSFileHandle\"16@?<v@?BB@\"NSError\">24"
- "PKDistributionHelperController: Synchronous service object proxy returned an error. %s"
- "fileAtPathExistsOnGraft:reply:"
- "v32@0:8@\"NSString\"16@?<v@?BB@\"NSError\">24"

```
