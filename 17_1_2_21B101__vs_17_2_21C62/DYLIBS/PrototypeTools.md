## PrototypeTools

> `/System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools`

```diff

-148.0.0.0.0
-  __TEXT.__text: 0x16ef8
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0x1eb0
-  __TEXT.__cstring: 0x1187
+148.1.0.0.0
+  __TEXT.__text: 0x175f4
+  __TEXT.__auth_stubs: 0x610
+  __TEXT.__objc_methlist: 0x1ee8
+  __TEXT.__cstring: 0x11ee
   __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0x130
-  __TEXT.__oslogstring: 0xbbc
+  __TEXT.__oslogstring: 0xc5c
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x78c
-  __TEXT.__objc_classname: 0x3c0
-  __TEXT.__objc_methname: 0x441a
-  __TEXT.__objc_methtype: 0xa3f
-  __TEXT.__objc_stubs: 0x3ae0
-  __DATA_CONST.__got: 0x88
+  __TEXT.__unwind_info: 0x7a8
+  __TEXT.__objc_classname: 0x3e9
+  __TEXT.__objc_methname: 0x44e0
+  __TEXT.__objc_methtype: 0xaab
+  __TEXT.__objc_stubs: 0x3b60
+  __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x488
-  __DATA_CONST.__objc_classlist: 0x148
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x80
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x54c0
-  __DATA_CONST.__objc_selrefs: 0x12e8
+  __DATA_CONST.__objc_const: 0x55f8
+  __DATA_CONST.__objc_selrefs: 0x1320
   __DATA_CONST.__objc_arraydata: 0x170
-  __AUTH_CONST.__cfstring: 0x1760
-  __AUTH_CONST.__objc_const: 0xfb8
+  __AUTH_CONST.__cfstring: 0x17a0
+  __AUTH_CONST.__objc_const: 0x1000
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__auth_got: 0x2e0
-  __AUTH.__objc_data: 0xa50
+  __AUTH_CONST.__auth_got: 0x318
+  __AUTH.__objc_data: 0xaa0
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x1b8
+  __DATA.__objc_classrefs: 0x1c0
   __DATA.__objc_superrefs: 0xa0
-  __DATA.__objc_ivar: 0x200
-  __DATA.__data: 0x600
-  __DATA.__bss: 0xa0
+  __DATA.__objc_ivar: 0x208
+  __DATA.__data: 0x660
+  __DATA.__bss: 0xb0
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0AE50FDF-65D1-3323-A6A7-15BA3FB04E22
-  Functions: 741
-  Symbols:   2799
-  CStrings:  1498
+  UUID: 0E5F159C-D1B8-38FA-93E3-79E05D86B39A
+  Functions: 755
+  Symbols:   2854
+  CStrings:  1522
 
Symbols:
+ +[_PTPredicateValidator validatorWithPredicate:]
+ -[_PTPredicateValidator .cxx_destruct]
+ -[_PTPredicateValidator evaluate]
+ -[_PTPredicateValidator evaluate].cold.1
+ -[_PTPredicateValidator evaluate].cold.2
+ -[_PTPredicateValidator visitPredicate:]
+ -[_PTPredicateValidator visitPredicateExpression:]
+ -[_PTPredicateValidator visitPredicateExpression:].cold.1
+ -[_PTPredicateValidator visitPredicateOperator:]
+ -[_PTPredicateValidator visitPredicateOperator:].cold.1
+ _NSStringFromSelector
+ _OBJC_CLASS_$__PTPredicateValidator
+ _OBJC_IVAR_$__PTPredicateValidator._predicate
+ _OBJC_IVAR_$__PTPredicateValidator._valid
+ _OBJC_METACLASS_$__PTPredicateValidator
+ _OUTLINED_FUNCTION_1
+ _PTValidatePredicate
+ _PTValidatePredicate.cold.1
+ __OBJC_$_INSTANCE_METHODS__PTPredicateValidator
+ __OBJC_$_INSTANCE_VARIABLES__PTPredicateValidator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSPredicateVisitor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSPredicateVisitor
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSPredicateVisitor
+ __OBJC_CLASS_PROTOCOLS_$__PTPredicateValidator
+ __OBJC_CLASS_RO_$__PTPredicateValidator
+ __OBJC_LABEL_PROTOCOL_$_NSPredicateVisitor
+ __OBJC_METACLASS_RO_$__PTPredicateValidator
+ __OBJC_PROTOCOL_$_NSPredicateVisitor
+ ___block_literal_global.28
+ ___block_literal_global.49
+ ___block_literal_global.58
+ __bs_set_crash_log_message
+ __os_log_debug_impl
+ __os_log_default
+ __os_log_error_impl
+ __sharedInstance.__lock
+ _objc_msgSend$_allowsEvaluation
+ _objc_msgSend$acceptVisitor:flags:
+ _objc_msgSend$expressionType
+ _objc_msgSend$operatorType
+ _objc_opt_new
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _structureForSettingsClass:.__lock
- ___block_literal_global.25
- ___block_literal_global.34
CStrings:
+ "BOOL PTValidatePredicate(NSPredicate *__strong)"
+ "NSPredicateVisitor"
+ "PTUtilities.m"
+ "Predicate failed validation: %{public}@"
+ "Predicate passed validation: %{public}@"
+ "[PTPredicate] %@ %@ (%lu) %@"
+ "_PTPredicateValidator"
+ "_allowsEvaluation"
+ "_predicate"
+ "_valid"
+ "acceptVisitor:flags:"
+ "expressionType"
+ "failure in %{public}@ (%{public}@:%i) : %{public}@"
+ "operatorType"
+ "predicate has already enabled evaluation"
+ "v24@0:8@\"NSExpression\"16"
+ "v24@0:8@\"NSPredicateOperator\"16"
+ "v40@0:8@\"NSExpression\"16@\"NSString\"24@\"NSString\"32"
+ "visitPredicate:"
+ "visitPredicateExpression:"
+ "visitPredicateExpression:keyPathScope:key:"
+ "visitPredicateOperator:"

```
