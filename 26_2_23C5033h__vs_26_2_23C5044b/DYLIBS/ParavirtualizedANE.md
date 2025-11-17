## ParavirtualizedANE

> `/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/ParavirtualizedANE`

```diff

-380.100.0.0.0
-  __TEXT.__text: 0x1a23c
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0x638
+380.200.3.0.0
+  __TEXT.__text: 0x1a598
+  __TEXT.__auth_stubs: 0x610
+  __TEXT.__objc_methlist: 0x644
   __TEXT.__const: 0x190
-  __TEXT.__cstring: 0xe08
-  __TEXT.__oslogstring: 0x4e9c
-  __TEXT.__gcc_except_tab: 0x36e8
-  __TEXT.__unwind_info: 0x5c8
+  __TEXT.__cstring: 0xe14
+  __TEXT.__oslogstring: 0x4ea7
+  __TEXT.__gcc_except_tab: 0x36f8
+  __TEXT.__unwind_info: 0x600
   __TEXT.__objc_classname: 0x2f
-  __TEXT.__objc_methname: 0x1eb7
-  __TEXT.__objc_methtype: 0x902
-  __TEXT.__objc_stubs: 0x1f20
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x50
+  __TEXT.__objc_methname: 0x1f12
+  __TEXT.__objc_methtype: 0x916
+  __TEXT.__objc_stubs: 0x1f80
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x868
+  __DATA_CONST.__objc_selrefs: 0x880
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x300
-  __AUTH_CONST.__const: 0x50
+  __AUTH_CONST.__auth_got: 0x318
+  __AUTH_CONST.__const: 0xd0
   __AUTH_CONST.__cfstring: 0xfc0
   __AUTH_CONST.__objc_const: 0x380
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x30
   __DATA.__data: 0x10
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5E5A4083-D001-339C-ABC7-84CDC2F3B4CC
-  Functions: 429
-  Symbols:   1418
-  CStrings:  954
+  UUID: DF3525E2-04F2-3B4D-9FE1-79FB1889A505
+  Functions: 440
+  Symbols:   1457
+  CStrings:  959
 
Symbols:
+ -[_ANEVirtualPlatformClient doModelAttributeUpdateDictionary:dictionary:].cold.3
+ -[_ANEVirtualPlatformClient getObjectFromIOSurfaceID:classes:topLevelClass:length:]
+ -[_ANEVirtualPlatformClient getObjectFromIOSurfaceID:classes:topLevelClass:length:].cold.1
+ -[_ANEVirtualPlatformClient getObjectFromIOSurfaceID:classes:topLevelClass:length:].cold.2
+ -[_ANEVirtualPlatformClient getObjectFromIOSurfaceID:classes:topLevelClass:length:].cold.3
+ -[_ANEVirtualPlatformClient getObjectFromIOSurfaceID:classes:topLevelClass:length:].cold.4
+ -[_ANEVirtualPlatformClient getOptionsDictFromInputDict:]
+ -[_ANEVirtualPlatformClient getOptionsDictFromInputDict:].cold.1
+ -[_ANEVirtualPlatformClient getOptionsDictFromInputDict:].cold.2
+ -[_ANEVirtualPlatformClient getOptionsDictFromInputDict:].cold.3
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.17
+ -[_ANEVirtualPlatformClient validateNetworkCreateMLIR:].cold.4
+ GCC_except_table103
+ GCC_except_table104
+ GCC_except_table105
+ GCC_except_table106
+ GCC_except_table107
+ GCC_except_table122
+ GCC_except_table129
+ GCC_except_table131
+ GCC_except_table135
+ GCC_except_table32
+ GCC_except_table43
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table62
+ GCC_except_table67
+ GCC_except_table77
+ GCC_except_table85
+ _CFDataGetTypeID
+ _NSStringFromClass
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSSet
+ __NSConcreteGlobalBlock
+ __ZZ55-[_ANEVirtualPlatformClient validateNetworkCreateMLIR:]E22validationParamClasses
+ __ZZ55-[_ANEVirtualPlatformClient validateNetworkCreateMLIR:]E9onceToken
+ __ZZ57-[_ANEVirtualPlatformClient getOptionsDictFromInputDict:]E18optionsDictClasses
+ __ZZ57-[_ANEVirtualPlatformClient getOptionsDictFromInputDict:]E9onceToken
+ __ZZ71-[_ANEVirtualPlatformClient getObjectFromIOSurfaceID:classType:length:]E9dictTypes
+ __ZZ71-[_ANEVirtualPlatformClient getObjectFromIOSurfaceID:classType:length:]E9onceToken
+ __ZZ73-[_ANEVirtualPlatformClient doModelAttributeUpdateDictionary:dictionary:]E16modelAttrClasses
+ __ZZ73-[_ANEVirtualPlatformClient doModelAttributeUpdateDictionary:dictionary:]E9onceToken
+ ___55-[_ANEVirtualPlatformClient validateNetworkCreateMLIR:]_block_invoke
+ ___57-[_ANEVirtualPlatformClient getOptionsDictFromInputDict:]_block_invoke
+ ___71-[_ANEVirtualPlatformClient getObjectFromIOSurfaceID:classType:length:]_block_invoke
+ ___73-[_ANEVirtualPlatformClient doModelAttributeUpdateDictionary:dictionary:]_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_literal_global
+ ___block_literal_global.253
+ ___block_literal_global.265
+ ___block_literal_global.360
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$getObjectFromIOSurfaceID:classes:topLevelClass:length:
+ _objc_msgSend$getOptionsDictFromInputDict:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$setWithObjects:
+ _objc_opt_isKindOfClass
- -[_ANEVirtualPlatformClient compileModelDictionary:].cold.4
- -[_ANEVirtualPlatformClient evaluateWithModelDictionary:].cold.8
- -[_ANEVirtualPlatformClient getObjectFromIOSurfaceID:classType:length:].cold.2
- -[_ANEVirtualPlatformClient getObjectFromIOSurfaceID:classType:length:].cold.3
- -[_ANEVirtualPlatformClient getOptionsFromDictionary:]
- -[_ANEVirtualPlatformClient getOptionsFromDictionary:].cold.1
- -[_ANEVirtualPlatformClient getOptionsFromDictionary:].cold.2
- -[_ANEVirtualPlatformClient sessionHintWithModel:].cold.2
- GCC_except_table117
- GCC_except_table124
- GCC_except_table125
- GCC_except_table126
- GCC_except_table19
- GCC_except_table33
- GCC_except_table45
- GCC_except_table53
- GCC_except_table56
- GCC_except_table57
- GCC_except_table61
- GCC_except_table66
- GCC_except_table75
- GCC_except_table81
- GCC_except_table94
- GCC_except_table95
- _objc_msgSend$decodeObjectOfClass:forKey:
- _objc_msgSend$getOptionsFromDictionary:
CStrings:
+ "%@: ANEVirtualPlatformClient failed to extract options dictionary!"
+ "%@: ERROR : Failed to extract options dictionary of length %d but optionsIOSID is 0!"
+ "%@: ERROR failed to extract options dictionary!"
+ "%@: No options dictionary found"
+ "%@: No options found"
+ "%@: Options length is 0 or kVirtANEOptionsLength key not found. Nothing to extract!"
+ "%s: unarchived object does not match topLevelClass : decoded to %@ instead of %@"
+ "-[_ANEVirtualPlatformClient getObjectFromIOSurfaceID:classes:topLevelClass:length:]"
+ "@44@0:8I16@20#28Q36"
+ "decodeObjectOfClasses:forKey:"
+ "getObjectFromIOSurfaceID:classes:topLevelClass:length:"
+ "getOptionsDictFromInputDict:"
+ "setWithObject:"
+ "setWithObjects:"
- "%@: ANEVirtualPlatformClient kVirtANEIOSIDOptions not found!"
- "%@: ANEVirtualPlatformClient kVirtANEOptionsLength not found!"
- "%@: ANEVirtualPlatformClient unLoadModelDictionary could not extract options dictionary from input dictionary"
- "%@: ERROR failed to extract options dictionary from IOSurface with optionsIOSID=%u optionsDataSize=%llu!"
- "%@: No optionsIOSID found"
- "%@: optionsLength is 0 for optionsIOSID=%u"
- "-[_ANEVirtualPlatformClient getObjectFromIOSurfaceID:classType:length:]"
- "decodeObjectOfClass:forKey:"
- "getOptionsFromDictionary:"

```
