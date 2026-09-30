## PerfPowerServicesReader

> `/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader`

```diff

-2964.0.107.502.1
-  __TEXT.__text: 0x1317e0
+2964.0.137.0.0
+  __TEXT.__text: 0x132028
   __TEXT.__auth_stubs: 0xf30
   __TEXT.__init_offsets: 0xdc
   __TEXT.__objc_methlist: 0x127d4
-  __TEXT.__const: 0x605e
-  __TEXT.__cstring: 0xc05c
+  __TEXT.__const: 0x5ffe
+  __TEXT.__cstring: 0xc037
   __TEXT.__gcc_except_tab: 0x4ad0
-  __TEXT.__oslogstring: 0xcf0
+  __TEXT.__oslogstring: 0xdc2
   __TEXT.__unwind_info: 0x4738
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_classname: 0x1963
-  __TEXT.__objc_methname: 0x1950c
+  __TEXT.__objc_methname: 0x19530
   __TEXT.__objc_methtype: 0x2748
-  __TEXT.__objc_stubs: 0x9780
+  __TEXT.__objc_stubs: 0x97e0
   __DATA_CONST.__got: 0xa80
-  __DATA_CONST.__const: 0x28d8
+  __DATA_CONST.__const: 0x28e0
   __DATA_CONST.__objc_classlist: 0x548
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d60
-  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_selrefs: 0x5d70
+  __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x110
   __AUTH_CONST.__auth_got: 0x7b0
   __AUTH_CONST.__const: 0x30d0
-  __AUTH_CONST.__cfstring: 0xdc80
+  __AUTH_CONST.__cfstring: 0xdca0
   __AUTH_CONST.__objc_const: 0x165a8
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x10ac
   __DATA.__data: 0x581
-  __DATA.__bss: 0x58
+  __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0xb40
   __DATA_DIRTY.__data: 0xad8
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 62A67A52-01C9-351A-9542-D23E32383E2B
-  Functions: 7736
-  Symbols:   20911
-  CStrings:  8154
+  UUID: 8FC5EC95-24DE-30A9-8FC4-E3893725280B
+  Functions: 7737
+  Symbols:   20917
+  CStrings:  8159
 
Symbols:
+ +[PPSRequestValidator _validatePredicateValue:metricDefinition:error:].cold.1
+ __OBJC_PROTOCOL_REFERENCE_$_NSFastEnumeration
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ _objc_msgSend$collection
+ _objc_msgSend$containsPredicateWithProperty:values:
+ _objc_msgSend$expressionForAggregate:
+ _objc_msgSend$getCategoriesForFilepath:subsystem:
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- _objc_msgSend$getMetadataByCategoryForSubsystem:
Functions:
~ -[NSComparisonPredicate(PPSSQLitePredicate) pps_sqlPredicateForSelect] : 392 -> 600
~ +[PPSPredicateUtilities constantValueForLeftExpression:inPredicate:] : 196 -> 248
~ +[PPSPredicateUtilities predicateByReplacingUint64bit:legalMetricNames:] : 1264 -> 1712
~ -[NSComparisonPredicate(PPSSQLitePredicate) _checkTypeForValue:inKeyPath:] : 308 -> 732
~ +[PPSRequestValidator _validatePredicateValue:metricDefinition:error:] : 692 -> 1468
~ _PerfPowerServicesGetLogLines : 704 -> 708
~ ___PerfPowerServicesGetLogLines_block_invoke : 348 -> 328
~ ___PerfPowerServicesGetLogLines_block_invoke_2 : 784 -> 764
+ +[PPSRequestValidator _validatePredicateValue:metricDefinition:error:].cold.1
CStrings:
+ "IN"
+ "Validation: Non-Constant value expression present in provided collection for '%@::%@::%@' -- %{public}@"
+ "Validation: Type mismatch for entry in provided array '%@::%@::%@' -- %{public}@ != %{public}@ (expected)"
+ "collection"
+ "expressionForAggregate:"
+ "getCategoriesForFilepath:subsystem:"
- "getMetadataByCategoryForSubsystem:"
- "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"

```
