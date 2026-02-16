## PowerExperience

> `/System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience`

```diff

-118.80.3.0.0
-  __TEXT.__text: 0x3c44
-  __TEXT.__auth_stubs: 0x2c0
-  __TEXT.__objc_methlist: 0x4ec
+136.100.8.0.0
+  __TEXT.__text: 0x430c
+  __TEXT.__auth_stubs: 0x2b0
+  __TEXT.__objc_methlist: 0x4fc
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x230
-  __TEXT.__cstring: 0x387
-  __TEXT.__oslogstring: 0x3de
-  __TEXT.__unwind_info: 0x230
+  __TEXT.__gcc_except_tab: 0x234
+  __TEXT.__cstring: 0x393
+  __TEXT.__oslogstring: 0x4c0
+  __TEXT.__unwind_info: 0x290
   __TEXT.__objc_classname: 0x190
-  __TEXT.__objc_methname: 0x841
-  __TEXT.__objc_methtype: 0x318
-  __TEXT.__objc_stubs: 0x6a0
+  __TEXT.__objc_methname: 0x8b2
+  __TEXT.__objc_methtype: 0x32d
+  __TEXT.__objc_stubs: 0x700
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x268
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x258
+  __DATA_CONST.__objc_selrefs: 0x278
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x170
-  __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x420
+  __AUTH_CONST.__auth_got: 0x168
+  __AUTH_CONST.__const: 0x220
+  __AUTH_CONST.__cfstring: 0x440
   __AUTH_CONST.__objc_const: 0x868
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x4c
   __DATA.__data: 0x360
-  __DATA.__bss: 0x8
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D8CAE36D-56BB-32AF-8181-2C565AC17B8F
-  Functions: 146
-  Symbols:   606
-  CStrings:  266
+  UUID: FEA460AC-C94D-3DEF-B799-C84E9D246953
+  Functions: 155
+  Symbols:   656
+  CStrings:  276
 
Symbols:
+ -[ContextualPowerModesClient registerWithIdentifier:forModes:queue:callback:]
+ -[ContextualPowerModesClient registerWithIdentifier:forModes:queue:callback:].cold.1
+ -[ContextualPowerModesClient registerWithIdentifier:forModes:queue:callback:].cold.2
+ -[ContextualPowerModesClient registerWithIdentifier:forModes:queue:callback:].cold.3
+ -[ContextualPowerModesClient registerWithIdentifier:forModes:queue:callback:].cold.4
+ GCC_except_table13
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ ___34-[ContextualPowerModesClient init]_block_invoke.43
+ ___34-[ContextualPowerModesClient init]_block_invoke.43.cold.1
+ ___34-[ContextualPowerModesClient init]_block_invoke.45
+ ___77-[ContextualPowerModesClient registerWithIdentifier:forModes:queue:callback:]_block_invoke
+ ___77-[ContextualPowerModesClient registerWithIdentifier:forModes:queue:callback:]_block_invoke.27
+ ___77-[ContextualPowerModesClient registerWithIdentifier:forModes:queue:callback:]_block_invoke.27.cold.1
+ ___block_literal_global.29
+ ___block_literal_global.31
+ _objc_autoreleaseReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend$containsObject:
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_release_x24
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
+ _registerWithIdentifier:forModes:queue:callback:.onceToken
+ _registerWithIdentifier:forModes:queue:callback:.validModes
- GCC_except_table10
- ___34-[ContextualPowerModesClient init]_block_invoke.38
- ___34-[ContextualPowerModesClient init]_block_invoke.38.cold.1
- ___34-[ContextualPowerModesClient init]_block_invoke.40
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "B48@0:8@16@24@32@?40"
+ "DefaultMode"
+ "Invalid count of power modes. Exiting without registering client"
+ "Invalid power mode '%@' not found in ContextualPowerModesList. Exiting without registering client."
+ "Modes set is nil or empty. Exiting without registering client"
+ "containsObject:"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "registerWithIdentifier:forModes:queue:callback:"

```
