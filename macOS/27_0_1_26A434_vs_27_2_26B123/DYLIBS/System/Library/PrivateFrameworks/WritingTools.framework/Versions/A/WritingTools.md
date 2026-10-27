## WritingTools

> `/System/Library/PrivateFrameworks/WritingTools.framework/Versions/A/WritingTools`

```diff

-149.503.0.0.0
-  __TEXT.__text: 0x6094
-  __TEXT.__objc_methlist: 0x8a4
+151.1.11.500.0
+  __TEXT.__text: 0x66bc
+  __TEXT.__objc_methlist: 0x98c
   __TEXT.__const: 0x306
-  __TEXT.__cstring: 0x7b2
-  __TEXT.__gcc_except_tab: 0x58
+  __TEXT.__cstring: 0x872
+  __TEXT.__gcc_except_tab: 0x88
   __TEXT.__oslogstring: 0x147
   __TEXT.__swift5_typeref: 0x67
   __TEXT.__constg_swiftt: 0x90

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__unwind_info: 0x2d8
   __TEXT.__eh_frame: 0xf8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x128
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x500
-  __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__got: 0x128
-  __AUTH_CONST.__const: 0x2f9
-  __AUTH_CONST.__cfstring: 0x5c0
-  __AUTH_CONST.__objc_const: 0x11e8
-  __AUTH_CONST.__auth_got: 0x248
+  __DATA_CONST.__objc_selrefs: 0x568
+  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__got: 0x138
+  __AUTH_CONST.__const: 0x329
+  __AUTH_CONST.__cfstring: 0x640
+  __AUTH_CONST.__objc_const: 0x1408
+  __AUTH_CONST.__auth_got: 0x268
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x78
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x88
   __DATA.__data: 0x280
   __DATA.__bss: 0x430
-  __DATA_DIRTY.__objc_data: 0x308
+  __DATA_DIRTY.__objc_data: 0x448
   __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 231
-  Symbols:   539
-  CStrings:  79
+  Functions: 250
+  Symbols:   595
+  CStrings:  84
 
Symbols:
+ +[WTPrecomputedData supportsBSXPCSecureCoding]
+ +[WTPrecomputedData supportsSecureCoding]
+ -[NSUndoManager(WTTurnTracking) wt_registerTurnWithHandler:]
+ -[NSUndoManager(WTTurnTracking) wt_registerUndoIfPossibleWithTarget:handler:]
+ -[WTPrecomputedData .cxx_destruct]
+ -[WTPrecomputedData copyWithZone:]
+ -[WTPrecomputedData encodeWithBSXPCCoder:]
+ -[WTPrecomputedData encodeWithCoder:]
+ -[WTPrecomputedData encodeWithGeneralCoder:]
+ -[WTPrecomputedData initWithBSXPCCoder:]
+ -[WTPrecomputedData initWithCoder:]
+ -[WTPrecomputedData initWithGeneralCoder:]
+ -[WTPrecomputedData initWithPrecomputedResultText:precomputedCitationsJSON:precomputedContentAdvisoriesJSON:precomputedResultReplacesExisting:]
+ -[WTPrecomputedData precomputedCitationsJSON]
+ -[WTPrecomputedData precomputedContentAdvisoriesJSON]
+ -[WTPrecomputedData precomputedResultReplacesExisting]
+ -[WTPrecomputedData precomputedResultText]
+ GCC_except_table4
+ OBJC_IVAR_$_WTPrecomputedData._precomputedCitationsJSON
+ OBJC_IVAR_$_WTPrecomputedData._precomputedContentAdvisoriesJSON
+ OBJC_IVAR_$_WTPrecomputedData._precomputedResultReplacesExisting
+ OBJC_IVAR_$_WTPrecomputedData._precomputedResultText
+ _NSInternalInconsistencyException
+ _OBJC_CLASS_$_NSUndoManager
+ _OBJC_CLASS_$_WTPrecomputedData
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_METACLASS_$_WTPrecomputedData
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSUndoManager_$_WTTurnTracking
+ __OBJC_$_CATEGORY_NSUndoManager_$_WTTurnTracking
+ __OBJC_$_CLASS_METHODS_WTPrecomputedData
+ __OBJC_$_CLASS_PROP_LIST_WTPrecomputedData
+ __OBJC_$_INSTANCE_METHODS_WTPrecomputedData
+ __OBJC_$_INSTANCE_VARIABLES_WTPrecomputedData
+ __OBJC_$_PROP_LIST_WTPrecomputedData
+ __OBJC_CLASS_PROTOCOLS_$_WTPrecomputedData
+ __OBJC_CLASS_RO_$_WTPrecomputedData
+ __OBJC_METACLASS_RO_$_WTPrecomputedData
+ ___60-[NSUndoManager(WTTurnTracking) wt_registerTurnWithHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e23_v16?0"NSUndoManager"8l
+ ___copy_helper_block_e8_32b
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_msgSend$groupingLevel
+ _objc_msgSend$groupsByEvent
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isUndoing
+ _objc_msgSend$name
+ _objc_msgSend$precomputedCitationsJSON
+ _objc_msgSend$precomputedContentAdvisoriesJSON
+ _objc_msgSend$precomputedResultReplacesExisting
+ _objc_msgSend$precomputedResultText
+ _objc_msgSend$registerUndoWithTarget:handler:
+ _objc_msgSend$wt_registerTurnWithHandler:
+ _objc_msgSend$wt_registerUndoIfPossibleWithTarget:handler:
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "WTPrecomputedDataCodingKeyCitationsJSON"
+ "WTPrecomputedDataCodingKeyContentAdvisoriesJSON"
+ "WTPrecomputedDataCodingKeyResultReplacesExisting"
+ "WTPrecomputedDataCodingKeyResultText"
+ "v16@?0@\"NSUndoManager\"8"
```
