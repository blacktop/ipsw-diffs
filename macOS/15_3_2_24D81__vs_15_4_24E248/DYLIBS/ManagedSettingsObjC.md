## ManagedSettingsObjC

> `/System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/Versions/A/ManagedSettingsObjC`

```diff

-242.2.2.0.0
-  __TEXT.__text: 0x2512c
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0x2e50
+242.4.10.0.0
+  __TEXT.__text: 0x26a0c
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_methlist: 0x336c
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x51c
-  __TEXT.__cstring: 0xd89
-  __TEXT.__oslogstring: 0x1663
-  __TEXT.__unwind_info: 0xc88
+  __TEXT.__gcc_except_tab: 0x518
+  __TEXT.__cstring: 0xea3
+  __TEXT.__oslogstring: 0x17b2
+  __TEXT.__unwind_info: 0xd20
   __TEXT.__objc_classname: 0xa40
-  __TEXT.__objc_methname: 0x5c81
-  __TEXT.__objc_methtype: 0xed2
-  __TEXT.__objc_stubs: 0x1fc0
-  __DATA_CONST.__got: 0x368
-  __DATA_CONST.__const: 0x420
+  __TEXT.__objc_methname: 0x6034
+  __TEXT.__objc_methtype: 0xf44
+  __TEXT.__objc_stubs: 0x2080
+  __DATA_CONST.__got: 0x378
+  __DATA_CONST.__const: 0x428
   __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1488
+  __DATA_CONST.__objc_selrefs: 0x1610
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1b0
-  __AUTH_CONST.__auth_got: 0x1c8
+  __AUTH_CONST.__auth_got: 0x1d0
   __AUTH_CONST.__const: 0x710
-  __AUTH_CONST.__cfstring: 0x1840
-  __AUTH_CONST.__objc_const: 0x7500
+  __AUTH_CONST.__cfstring: 0x19c0
+  __AUTH_CONST.__objc_const: 0x7060
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH.__objc_data: 0x1d10
   __DATA.__objc_ivar: 0x294
   __DATA.__data: 0x600
-  __DATA.__bss: 0x650
+  __DATA.__bss: 0x6d0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DC50F34F-51C3-3C48-9D8B-7B6530C74D2F
-  Functions: 1123
-  Symbols:   2841
-  CStrings:  1722
+  UUID: 90FC068F-F620-395C-A27D-4C6126C2AA3A
+  Functions: 1182
+  Symbols:   2928
+  CStrings:  1791
 
Symbols:
+ +[MOCalculatorSettingsGroup denyInputModeRPNMetadata]
+ +[MOCalculatorSettingsGroup denyInputModeUnitConversionMetadata]
+ +[MOCalculatorSettingsGroup denyModeMathPaperMetadata]
+ +[MOCalculatorSettingsGroup denyModeProgrammerMetadata]
+ +[MOCalculatorSettingsGroup denyModeScientificMetadata]
+ +[MOCalculatorSettingsGroup forceSquareRootOnBasicCalculatorMetadata]
+ +[MOLogger blame].cold.1
+ +[MOLogger effective].cold.1
+ +[MOLogger sandboxing].cold.1
+ +[MOLogger store].cold.1
+ +[MOLogger subscription].cold.1
+ +[MOLogger xpc].cold.1
+ +[MOSafariSettingsGroup denyHistoryClearingMetadata]
+ +[MOSafariSettingsGroup denyPrivateBrowsingMetadata]
+ +[MOSandboxExtensionIssuer sharedIssuer].cold.1
+ +[MOSettingsStore createSettingsStoreErrorWithCode:]
+ +[MOSettingsStore directoryAttributes].cold.1
+ +[MOSettingsStore fileAttributes].cold.1
+ +[MOSettingsStore loadEffectiveSettingsAtURL:]
+ +[MOSettingsStore loadEffectiveSettingsAtURL:].cold.1
+ +[MOSettingsStore loadEffectiveSettingsAtURL:].cold.2
+ +[MOSettingsStore settingAndGroupStringsFromSettingKey:outGroup:outSetting:]
+ +[MOSettingsStore settingAndGroupStringsFromSettingKey:outGroup:outSetting:].cold.1
+ +[MOSettingsStore settingKeyFromSetting:group:]
+ +[MOSubscriptionCenter sharedCenter].cold.1
+ -[MOBatchSettingsStore persistableValueForSetting:inGroup:]
+ -[MOBatchSettingsStore persistableValueForSettingKey:]
+ -[MOBatchSettingsStore removePersistableValueForSetting:inGroup:]
+ -[MOBatchSettingsStore removePersistableValueForSettingKey:]
+ -[MOBatchSettingsStore setPersistableValue:forSetting:inGroup:]
+ -[MOBatchSettingsStore setPersistableValue:forSettingKey:]
+ -[MOBatchSettingsStore settingsReader]
+ -[MOBatchSettingsStore settingsWriter]
+ -[MOCalculatorSettingsGroup denyInputModeRPN]
+ -[MOCalculatorSettingsGroup denyInputModeUnitConversion]
+ -[MOCalculatorSettingsGroup denyModeMathPaper]
+ -[MOCalculatorSettingsGroup denyModeProgrammer]
+ -[MOCalculatorSettingsGroup denyModeScientific]
+ -[MOCalculatorSettingsGroup forceSquareRootOnBasicCalculator]
+ -[MOCalculatorSettingsGroup setDenyInputModeRPN:]
+ -[MOCalculatorSettingsGroup setDenyInputModeUnitConversion:]
+ -[MOCalculatorSettingsGroup setDenyModeMathPaper:]
+ -[MOCalculatorSettingsGroup setDenyModeProgrammer:]
+ -[MOCalculatorSettingsGroup setDenyModeScientific:]
+ -[MOCalculatorSettingsGroup setForceSquareRootOnBasicCalculator:]
+ -[MOEffectiveSettingsStore persistableValueForSetting:inGroup:]
+ -[MOEffectiveSettingsStore persistableValueForSettingKey:]
+ -[MOEffectiveSettingsStore persistableValueForSettingKey:].cold.1
+ -[MOEffectiveSettingsStore settingsReader]
+ -[MOLocalSettingsStore persistableValueForSetting:inGroup:]
+ -[MOLocalSettingsStore persistableValueForSettingKey:]
+ -[MOLocalSettingsStore removePersistableValueForSetting:inGroup:]
+ -[MOLocalSettingsStore removePersistableValueForSettingKey:]
+ -[MOLocalSettingsStore setPersistableValue:forSetting:inGroup:]
+ -[MOLocalSettingsStore setPersistableValue:forSettingKey:]
+ -[MOLocalSettingsStore settingsReader]
+ -[MOLocalSettingsStore settingsWriter]
+ -[MOSafariSettingsGroup denyHistoryClearing]
+ -[MOSafariSettingsGroup denyPrivateBrowsing]
+ -[MOSafariSettingsGroup setDenyHistoryClearing:]
+ -[MOSafariSettingsGroup setDenyPrivateBrowsing:]
+ -[MOSettingsStore metadataForSettingKey:].cold.1
+ -[MOSettingsStore setValue:forSettingKey:outError:]
+ -[MOSettingsStore setValue:forSettingKey:outError:].cold.1
+ -[MOSettingsStore setValue:forSettingKey:outError:].cold.2
+ -[MOSettingsStore setValue:forSettingKey:outError:].cold.3
+ -[MOSettingsStore settingsReader]
+ -[MOSettingsStore settingsWriter]
+ -[MOSettingsStore valueForSettingKey:]
+ -[MOSettingsStore valueForSettingKey:].cold.1
+ -[MOSettingsStore valueForSettingKey:].cold.2
+ -[MOSettingsStore valueForUndefinedKey:]
+ -[MOSettingsStore valueForUndefinedKey:].cold.1
+ GCC_except_table30
+ GCC_except_table33
+ GCC_except_table35
+ GCC_except_table50
+ _MOSettingsStoreErrorDomain
+ _OBJC_CLASS_$_NSError
+ __54-[MOLocalSettingsStore persistableValueForSettingKey:]_block_invoke.32
+ __54-[MOLocalSettingsStore persistableValueForSettingKey:]_block_invoke.32.cold.1
+ __54-[MOLocalSettingsStore persistableValueForSettingKey:]_block_invoke.cold.1
+ __58-[MOLocalSettingsStore setPersistableValue:forSettingKey:]_block_invoke.35
+ __58-[MOLocalSettingsStore setPersistableValue:forSettingKey:]_block_invoke.35.cold.1
+ __58-[MOLocalSettingsStore setPersistableValue:forSettingKey:]_block_invoke.cold.1
+ __60-[MOLocalSettingsStore removePersistableValueForSettingKey:]_block_invoke.40
+ __60-[MOLocalSettingsStore removePersistableValueForSettingKey:]_block_invoke.40.cold.1
+ __60-[MOLocalSettingsStore removePersistableValueForSettingKey:]_block_invoke.cold.1
+ ___52+[MOSafariSettingsGroup denyHistoryClearingMetadata]_block_invoke
+ ___52+[MOSafariSettingsGroup denyPrivateBrowsingMetadata]_block_invoke
+ ___53+[MOCalculatorSettingsGroup denyInputModeRPNMetadata]_block_invoke
+ ___54+[MOCalculatorSettingsGroup denyModeMathPaperMetadata]_block_invoke
+ ___54-[MOLocalSettingsStore persistableValueForSettingKey:]_block_invoke
+ ___55+[MOCalculatorSettingsGroup denyModeProgrammerMetadata]_block_invoke
+ ___55+[MOCalculatorSettingsGroup denyModeScientificMetadata]_block_invoke
+ ___58-[MOLocalSettingsStore setPersistableValue:forSettingKey:]_block_invoke
+ ___60-[MOLocalSettingsStore removePersistableValueForSettingKey:]_block_invoke
+ ___64+[MOCalculatorSettingsGroup denyInputModeUnitConversionMetadata]_block_invoke
+ ___69+[MOCalculatorSettingsGroup forceSquareRootOnBasicCalculatorMetadata]_block_invoke
+ __block_literal_global.49
+ _objc_autorelease
+ _objc_msgSend$createSettingsStoreErrorWithCode:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$loadEffectiveSettingsAtURL:
+ _objc_msgSend$persistableValueForSetting:inGroup:
+ _objc_msgSend$persistableValueForSettingKey:
+ _objc_msgSend$removePersistableValueForSetting:inGroup:
+ _objc_msgSend$removePersistableValueForSettingKey:
+ _objc_msgSend$setPersistableValue:forSetting:inGroup:
+ _objc_msgSend$setPersistableValue:forSettingKey:
+ _objc_msgSend$settingAndGroupStringsFromSettingKey:outGroup:outSetting:
+ _objc_msgSend$settingsReader
+ _objc_msgSend$settingsWriter
+ denyHistoryClearingMetadata.metadata
+ denyHistoryClearingMetadata.onceToken
+ denyInputModeRPNMetadata.metadata
+ denyInputModeRPNMetadata.onceToken
+ denyInputModeUnitConversionMetadata.metadata
+ denyInputModeUnitConversionMetadata.onceToken
+ denyModeMathPaperMetadata.metadata
+ denyModeMathPaperMetadata.onceToken
+ denyModeProgrammerMetadata.metadata
+ denyModeProgrammerMetadata.onceToken
+ denyModeScientificMetadata.metadata
+ denyModeScientificMetadata.onceToken
+ denyPrivateBrowsingMetadata.metadata
+ denyPrivateBrowsingMetadata.onceToken
+ forceSquareRootOnBasicCalculatorMetadata.metadata
+ forceSquareRootOnBasicCalculatorMetadata.onceToken
- +[MOSettingsStore loadSettingsAtURL:]
- +[MOSettingsStore loadSettingsAtURL:].cold.1
- +[MOSettingsStore loadSettingsAtURL:].cold.2
- -[MOBatchSettingsStore reader]
- -[MOBatchSettingsStore removeValueForSetting:inGroup:]
- -[MOBatchSettingsStore setValue:forSetting:inGroup:]
- -[MOBatchSettingsStore valueForSetting:inGroup:]
- -[MOBatchSettingsStore writer]
- -[MOEffectiveSettingsStore reader]
- -[MOEffectiveSettingsStore valueForSetting:inGroup:]
- -[MOLocalSettingsStore reader]
- -[MOLocalSettingsStore removeValueForSetting:inGroup:]
- -[MOLocalSettingsStore setValue:forSetting:inGroup:]
- -[MOLocalSettingsStore valueForSetting:inGroup:]
- -[MOLocalSettingsStore writer]
- -[MOSettingsStore reader]
- -[MOSettingsStore settingKeyFromSetting:group:]
- -[MOSettingsStore writer]
- GCC_except_table29
- GCC_except_table31
- GCC_except_table32
- GCC_except_table49
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- __48-[MOLocalSettingsStore valueForSetting:inGroup:]_block_invoke.31
- __48-[MOLocalSettingsStore valueForSetting:inGroup:]_block_invoke.31.cold.1
- __48-[MOLocalSettingsStore valueForSetting:inGroup:]_block_invoke.cold.1
- __52-[MOLocalSettingsStore setValue:forSetting:inGroup:]_block_invoke.34
- __52-[MOLocalSettingsStore setValue:forSetting:inGroup:]_block_invoke.34.cold.1
- __52-[MOLocalSettingsStore setValue:forSetting:inGroup:]_block_invoke.cold.1
- __54-[MOLocalSettingsStore removeValueForSetting:inGroup:]_block_invoke.39
- __54-[MOLocalSettingsStore removeValueForSetting:inGroup:]_block_invoke.39.cold.1
- __54-[MOLocalSettingsStore removeValueForSetting:inGroup:]_block_invoke.cold.1
- ___48-[MOLocalSettingsStore valueForSetting:inGroup:]_block_invoke
- ___52-[MOLocalSettingsStore setValue:forSetting:inGroup:]_block_invoke
- ___54-[MOLocalSettingsStore removeValueForSetting:inGroup:]_block_invoke
- __block_literal_global.41
- _objc_msgSend$loadSettingsAtURL:
- _objc_msgSend$reader
- _objc_msgSend$removeValueForSetting:inGroup:
- _objc_msgSend$setValue:forSetting:inGroup:
- _objc_msgSend$valueForSetting:inGroup:
- _objc_msgSend$writer
CStrings:
+ "@24@0:8@\"NSString\"16"
+ "@24@0:8q16"
+ "B40@0:8@16@24^@32"
+ "B40@0:8@16^@24^@32"
+ "Cannot read value for %{public}@"
+ "Cannot write value for %{public}@"
+ "Invalid effective setting %{public}@"
+ "Invalid setting key: %{public}@"
+ "MOSettingsStoreErrorDomain"
+ "Missing metadata when reading value for %{public}@"
+ "Missing metadata when setting value for %{public}@"
+ "Missing persistable value when setting value for %{public}@"
+ "Unable to find group name %{public}@"
+ "createSettingsStoreErrorWithCode:"
+ "denyHistoryClearing"
+ "denyHistoryClearingMetadata"
+ "denyInputModeRPN"
+ "denyInputModeRPNMetadata"
+ "denyInputModeUnitConversion"
+ "denyInputModeUnitConversionMetadata"
+ "denyModeMathPaper"
+ "denyModeMathPaperMetadata"
+ "denyModeProgrammer"
+ "denyModeProgrammerMetadata"
+ "denyModeScientific"
+ "denyModeScientificMetadata"
+ "denyPrivateBrowsing"
+ "denyPrivateBrowsingMetadata"
+ "errorWithDomain:code:userInfo:"
+ "forceSquareRootOnBasicCalculator"
+ "forceSquareRootOnBasicCalculatorMetadata"
+ "loadEffectiveSettingsAtURL:"
+ "persistableValueForSetting:inGroup:"
+ "persistableValueForSettingKey:"
+ "removePersistableValueForSetting:inGroup:"
+ "removePersistableValueForSettingKey:"
+ "safari.denyHistoryClearing"
+ "safari.denyPrivateBrowsing"
+ "setDenyHistoryClearing:"
+ "setDenyInputModeRPN:"
+ "setDenyInputModeUnitConversion:"
+ "setDenyModeMathPaper:"
+ "setDenyModeProgrammer:"
+ "setDenyModeScientific:"
+ "setDenyPrivateBrowsing:"
+ "setForceSquareRootOnBasicCalculator:"
+ "setPersistableValue:forSetting:inGroup:"
+ "setPersistableValue:forSettingKey:"
+ "setValue:forSettingKey:outError:"
+ "settingAndGroupStringsFromSettingKey:outGroup:outSetting:"
+ "v24@0:8@\"NSString\"16"
+ "v32@0:8@16@\"NSString\"24"
+ "valueForSettingKey:"
+ "valueForUndefinedKey:"
+ "webContent.blockedByFilter"
- "loadSettingsAtURL:"
- "reader"
- "removeValueForSetting:inGroup:"
- "setValue:forSetting:inGroup:"
- "valueForSetting:inGroup:"
- "writer"

```
