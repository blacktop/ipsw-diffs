## RemoteManagementModel

> `/System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel`

```diff

-500.25.3.7.0
-  __TEXT.__text: 0x4068c
+500.25.5.10.0
+  __TEXT.__text: 0x4239c
   __TEXT.__auth_stubs: 0x330
   __TEXT.__objc_methlist: 0x63dc
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x347b
+  __TEXT.__cstring: 0x3473
   __TEXT.__unwind_info: 0xfc0
   __TEXT.__objc_classname: 0x13e0
-  __TEXT.__objc_methname: 0xa633
+  __TEXT.__objc_methname: 0xa62b
   __TEXT.__objc_methtype: 0xadb
   __TEXT.__objc_stubs: 0x4dc0
   __DATA_CONST.__got: 0x38

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x7d40
   __DATA_CONST.__objc_selrefs: 0x18c8
-  __DATA_CONST.__objc_arraydata: 0x22c8
+  __DATA_CONST.__objc_classrefs: 0x478
+  __DATA_CONST.__objc_superrefs: 0x320
+  __DATA_CONST.__objc_arraydata: 0x2e48
   __AUTH_CONST.__cfstring: 0x5660
-  __AUTH_CONST.__objc_arrayobj: 0x3df8
-  __AUTH_CONST.__objc_intobj: 0x1f38
+  __AUTH_CONST.__objc_arrayobj: 0x4998
+  __AUTH_CONST.__objc_intobj: 0x2850
   __AUTH_CONST.__objc_const: 0x120
-  __AUTH_CONST.__const: 0x1a0
+  __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__auth_got: 0x1a0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_classrefs: 0x478
-  __DATA.__objc_superrefs: 0x320
   __DATA.__objc_ivar: 0x69c
   __DATA.__data: 0x1e8
   __DATA.__bss: 0x88
-  __DATA_DIRTY.__const: 0x620
+  __DATA_DIRTY.__const: 0x380
   __DATA_DIRTY.__objc_const: 0x40e8
   __DATA_DIRTY.__objc_data: 0x2850
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2051
-  Symbols:   7277
-  CStrings:  2291
+  Symbols:   7401
+  CStrings:  2292
 
Symbols:
+ +[RMModelConfigurationBase combineEnumFirst:other:enums:]
+ +[RMModelConfigurationBase combineEnumLast:other:enums:]
+ +[RMModelExampleCombineDeclaration buildWithIdentifier:booleanOr:booleanAnd:numberMin:numberMax:enumFirst:enumLast:firstString:arrayAppend:setUnion:setIntersection:dictionaryFirst:dictionaryCombine:]
+ +[RMModelExampleCombineDeclaration_DictionaryCombine buildWithNumberMin:enumLast:]
+ -[RMModelExampleCombineDeclaration payloadEnumFirst]
+ -[RMModelExampleCombineDeclaration payloadEnumLast]
+ -[RMModelExampleCombineDeclaration setPayloadEnumFirst:]
+ -[RMModelExampleCombineDeclaration setPayloadEnumLast:]
+ -[RMModelExampleCombineDeclaration_DictionaryCombine payloadEnumLast]
+ -[RMModelExampleCombineDeclaration_DictionaryCombine setPayloadEnumLast:]
+ _OBJC_IVAR_$_RMModelExampleCombineDeclaration._payloadEnumFirst
+ _OBJC_IVAR_$_RMModelExampleCombineDeclaration._payloadEnumLast
+ _OBJC_IVAR_$_RMModelExampleCombineDeclaration_DictionaryCombine._payloadEnumLast
+ _RMModelExampleCombineDeclaration_DictionaryCombine_EnumLast_high1
+ _RMModelExampleCombineDeclaration_DictionaryCombine_EnumLast_high2
+ _RMModelExampleCombineDeclaration_DictionaryCombine_EnumLast_high3
+ _RMModelExampleCombineDeclaration_EnumFirst_low1
+ _RMModelExampleCombineDeclaration_EnumFirst_low2
+ _RMModelExampleCombineDeclaration_EnumFirst_low3
+ _RMModelExampleCombineDeclaration_EnumLast_high1
+ _RMModelExampleCombineDeclaration_EnumLast_high2
+ _RMModelExampleCombineDeclaration_EnumLast_high3
+ ___block_literal_global.127
+ ___block_literal_global.137
+ ___block_literal_global.142
+ ___block_literal_global.154
+ ___block_literal_global.156
+ ___block_literal_global.166
+ ___block_literal_global.171
+ ___block_literal_global.183
+ ___block_literal_global.184
+ ___block_literal_global.185
+ ___block_literal_global.187
+ ___block_literal_global.189
+ ___block_literal_global.219
+ ___block_literal_global.287
+ ___block_literal_global.359
+ ___block_literal_global.375
+ ___block_literal_global.377
+ ___block_literal_global.379
+ ___block_literal_global.38
+ ___block_literal_global.381
+ ___block_literal_global.439
+ ___block_literal_global.44
+ ___block_literal_global.447
+ ___block_literal_global.63
+ ___block_literal_global.70
+ ___block_literal_global.74
+ __unnamed_array_storage.100
+ __unnamed_array_storage.103
+ __unnamed_array_storage.107
+ __unnamed_array_storage.122
+ __unnamed_array_storage.125
+ __unnamed_array_storage.128
+ __unnamed_array_storage.131
+ __unnamed_array_storage.136
+ __unnamed_array_storage.139
+ __unnamed_array_storage.58
+ __unnamed_array_storage.61
+ __unnamed_array_storage.65
+ __unnamed_array_storage.78
+ __unnamed_array_storage.81
+ _objc_msgSend$combineEnumFirst:other:enums:
+ _objc_msgSend$combineEnumLast:other:enums:
+ _objc_msgSend$payloadEnumFirst
+ _objc_msgSend$payloadEnumLast
+ _objc_msgSend$setPayloadEnumFirst:
+ _objc_msgSend$setPayloadEnumLast:
- +[RMModelConfigurationBase combineEnumHighest:other:enums:]
- +[RMModelConfigurationBase combineEnumLowest:other:enums:]
- +[RMModelExampleCombineDeclaration buildWithIdentifier:booleanOr:booleanAnd:numberMin:numberMax:enumLowest:enumHighest:firstString:arrayAppend:setUnion:setIntersection:dictionaryFirst:dictionaryCombine:]
- +[RMModelExampleCombineDeclaration_DictionaryCombine buildWithNumberMin:enumHighest:]
- -[RMModelExampleCombineDeclaration payloadEnumHighest]
- -[RMModelExampleCombineDeclaration payloadEnumLowest]
- -[RMModelExampleCombineDeclaration setPayloadEnumHighest:]
- -[RMModelExampleCombineDeclaration setPayloadEnumLowest:]
- -[RMModelExampleCombineDeclaration_DictionaryCombine payloadEnumHighest]
- -[RMModelExampleCombineDeclaration_DictionaryCombine setPayloadEnumHighest:]
- _OBJC_IVAR_$_RMModelExampleCombineDeclaration._payloadEnumHighest
- _OBJC_IVAR_$_RMModelExampleCombineDeclaration._payloadEnumLowest
- _OBJC_IVAR_$_RMModelExampleCombineDeclaration_DictionaryCombine._payloadEnumHighest
- _RMModelExampleCombineDeclaration_DictionaryCombine_EnumHighest_high1
- _RMModelExampleCombineDeclaration_DictionaryCombine_EnumHighest_high2
- _RMModelExampleCombineDeclaration_DictionaryCombine_EnumHighest_high3
- _RMModelExampleCombineDeclaration_EnumHighest_high1
- _RMModelExampleCombineDeclaration_EnumHighest_high2
- _RMModelExampleCombineDeclaration_EnumHighest_high3
- _RMModelExampleCombineDeclaration_EnumLowest_low1
- _RMModelExampleCombineDeclaration_EnumLowest_low2
- _RMModelExampleCombineDeclaration_EnumLowest_low3
- ___block_literal_global.119
- ___block_literal_global.121
- ___block_literal_global.134
- ___block_literal_global.146
- ___block_literal_global.148
- ___block_literal_global.150
- ___block_literal_global.163
- ___block_literal_global.168
- ___block_literal_global.173
- ___block_literal_global.175
- ___block_literal_global.177
- ___block_literal_global.179
- ___block_literal_global.182
- ___block_literal_global.209
- ___block_literal_global.284
- ___block_literal_global.350
- ___block_literal_global.36
- ___block_literal_global.361
- ___block_literal_global.366
- ___block_literal_global.368
- ___block_literal_global.372
- ___block_literal_global.40
- ___block_literal_global.41
- ___block_literal_global.430
- ___block_literal_global.438
- ___block_literal_global.61
- ___block_literal_global.62
- ___block_literal_global.66
- __unnamed_array_storage.102
- __unnamed_array_storage.105
- __unnamed_array_storage.12
- __unnamed_array_storage.123
- __unnamed_array_storage.5
- __unnamed_array_storage.66
- __unnamed_array_storage.76
- __unnamed_array_storage.79
- __unnamed_array_storage.93
- __unnamed_array_storage.96
- __unnamed_array_storage.99
- _objc_msgSend$combineEnumHighest:other:enums:
- _objc_msgSend$combineEnumLowest:other:enums:
- _objc_msgSend$payloadEnumHighest
- _objc_msgSend$payloadEnumLowest
- _objc_msgSend$setPayloadEnumHighest:
- _objc_msgSend$setPayloadEnumLowest:
CStrings:
+ "EnumFirst"
+ "EnumLast"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_payloadEnumFirst"
+ "T@\"NSString\",C,N,V_payloadEnumLast"
+ "_payloadEnumFirst"
+ "_payloadEnumLast"
+ "buildWithIdentifier:booleanOr:booleanAnd:numberMin:numberMax:enumFirst:enumLast:firstString:arrayAppend:setUnion:setIntersection:dictionaryFirst:dictionaryCombine:"
+ "buildWithNumberMin:enumLast:"
+ "combineEnumFirst:other:enums:"
+ "combineEnumLast:other:enums:"
+ "payloadEnumFirst"
+ "payloadEnumLast"
+ "setPayloadEnumFirst:"
+ "setPayloadEnumLast:"
- "EnumHighest"
- "EnumLowest"
- "T@\"NSString\",C,N,V_payloadEnumHighest"
- "T@\"NSString\",C,N,V_payloadEnumLowest"
- "_payloadEnumHighest"
- "_payloadEnumLowest"
- "buildWithIdentifier:booleanOr:booleanAnd:numberMin:numberMax:enumLowest:enumHighest:firstString:arrayAppend:setUnion:setIntersection:dictionaryFirst:dictionaryCombine:"
- "buildWithNumberMin:enumHighest:"
- "combineEnumHighest:other:enums:"
- "combineEnumLowest:other:enums:"
- "payloadEnumHighest"
- "payloadEnumLowest"
- "setPayloadEnumHighest:"
- "setPayloadEnumLowest:"

```
