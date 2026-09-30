## SiriFoundation

> `/System/Library/PrivateFrameworks/SiriFoundation.framework/Versions/A/SiriFoundation`

```diff

-3403.4.1.14.2
-  __TEXT.__text: 0xfd88
+3404.72.1.14.4
+  __TEXT.__text: 0xfed4
   __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0xf18
+  __TEXT.__objc_methlist: 0x10cc
   __TEXT.__const: 0x7c
-  __TEXT.__cstring: 0x2719
+  __TEXT.__cstring: 0x2734
   __TEXT.__oslogstring: 0x19b1
   __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__unwind_info: 0x3a8
+  __TEXT.__unwind_info: 0x3c8
   __TEXT.__objc_classname: 0x1f2
-  __TEXT.__objc_methname: 0x3450
-  __TEXT.__objc_methtype: 0x466
-  __TEXT.__objc_stubs: 0x2240
+  __TEXT.__objc_methname: 0x3529
+  __TEXT.__objc_methtype: 0x48d
+  __TEXT.__objc_stubs: 0x22c0
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__const: 0x2b0
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd38
+  __DATA_CONST.__objc_selrefs: 0xdf0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0x3d0
   __AUTH_CONST.__cfstring: 0x1820
-  __AUTH_CONST.__objc_const: 0x1aa8
+  __AUTH_CONST.__objc_const: 0x17e0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28

   - /System/Library/PrivateFrameworks/login.framework/Versions/A/login
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9B2F8355-EE58-3963-BCDB-88FEA8248379
-  Functions: 382
-  Symbols:   1177
-  CStrings:  1207
+  UUID: FFF264AD-6853-3D8B-B222-960458EF0496
+  Functions: 400
+  Symbols:   1199
+  CStrings:  1214
 
Symbols:
+ +[SRFBugReporter sharedReporter].cold.1
+ +[SRFClamshellStateNotifier sharedInstance].cold.1
+ +[SRFLauncher sharedInstance].cold.1
+ +[SRFLockStateNotifier sharedInstance].cold.1
+ +[SRFLoggingDefaults _sharedAssistantLoggingUserDefaults].cold.1
+ +[SRFLoggingDefaults sharedDefaults].cold.1
+ +[SRFPreferences sharedPreferences].cold.1
+ +[SRFSetupAssistantPreferences sharedPreferences].cold.1
+ +[SRFSignpostLog sharedInstance].cold.1
+ +[SRFStateNotifier sharedNotifier].cold.1
+ +[SRFUserDefaultsController _canAccessUserDefaults].cold.1
+ +[SRFUserDefaultsController sharedUserDefaultsController].cold.1
+ +[SRFVoiceTriggerDevices sharedVoiceTriggerDevices].cold.1
+ +[SiriSymbolicHotKeysDefaultsController sharedSiriSymbolicHotKeysDefaultsController].cold.1
+ -[SRFUserDefaultsController _isInternal].cold.1
+ -[SRFUserDefaultsController keyboardShortcutDictionaryWithSAEEnabled:]
+ -[SRFUserDefaultsController mostRecentCustomizedKeyboardShorcutDictionaryWithSAEEnabled:]
+ -[SRFUserDefaultsController setKeyboardShortcutDictionary:saeEnabled:]
+ -[SRFUserDefaultsController setMostRecentCustomizedKeyboardShorcutDictionary:saeEnabled:]
+ -[SiriSymbolicHotKeysDefaultsController disableHotKey:]
+ -[SiriSymbolicHotKeysDefaultsController hotKeyMigrationIfNeeded:saeEnabled:]
+ -[SiriSymbolicHotKeysDefaultsController hotKeyValue:]
+ _AFDeviceSupportsSAEDeprecated
+ __block_literal_global.166
+ __block_literal_global.177
+ __block_literal_global.207
+ _objc_msgSend$disableHotKey:
+ _objc_msgSend$hotKeyMigrationIfNeeded:saeEnabled:
+ _objc_msgSend$hotKeyValue:
+ _objc_msgSend$keyboardShortcutDictionaryWithSAEEnabled:
+ _objc_msgSend$mostRecentCustomizedKeyboardShorcutDictionaryWithSAEEnabled:
+ _objc_msgSend$setKeyboardShortcutDictionary:saeEnabled:
+ _objc_msgSend$setMostRecentCustomizedKeyboardShorcutDictionary:saeEnabled:
- -[SiriSymbolicHotKeysDefaultsController disableHotKey]
- -[SiriSymbolicHotKeysDefaultsController hotKeyMigrationIfNeeded:]
- -[SiriSymbolicHotKeysDefaultsController hotKeyValue]
- _AFDeviceSupportsSystemAssistantExperience
- _OUTLINED_FUNCTION_5
- __block_literal_global.165
- __block_literal_global.176
- __block_literal_global.206
- _objc_msgSend$disableHotKey
- _objc_msgSend$hotKeyMigrationIfNeeded:
- _objc_msgSend$hotKeyValue
CStrings:
+ "-[SRFUserDefaultsController mostRecentCustomizedKeyboardShorcutDictionaryWithSAEEnabled:]"
+ "-[SiriSymbolicHotKeysDefaultsController hotKeyMigrationIfNeeded:saeEnabled:]"
+ "-[SiriSymbolicHotKeysDefaultsController hotKeyValue:]"
+ "/AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SiriFoundation/SiriFoundation/SRFEnablementFlowConfigurationProvider.m"
+ "/AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SiriFoundation/SiriFoundation/SRFFoundationAdditions.m"
+ "/AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SiriFoundation/SiriFoundation/SRFPreferences.m"
+ "/AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SiriFoundation/SiriFoundation/SRFUserDefaultsController.m"
+ "@20@0:8B16"
+ "@28@0:8@16B24"
+ "T@\"NSDictionary\""
+ "disableHotKey:"
+ "hotKeyMigrationIfNeeded:saeEnabled:"
+ "hotKeyValue:"
+ "keyboardShortcutDictionaryWithSAEEnabled:"
+ "mostRecentCustomizedKeyboardShorcutDictionaryWithSAEEnabled:"
+ "setKeyboardShortcutDictionary:saeEnabled:"
+ "setMostRecentCustomizedKeyboardShorcutDictionary:saeEnabled:"
+ "v28@0:8@16B24"
- "-[SRFUserDefaultsController mostRecentCustomizedKeyboardShorcutDictionary]"
- "-[SiriSymbolicHotKeysDefaultsController hotKeyMigrationIfNeeded:]"
- "-[SiriSymbolicHotKeysDefaultsController hotKeyValue]"
- "/AppleInternal/Library/BuildRoots/5d7f20e9-d19f-11ef-9955-d285688f7a47/Library/Caches/com.apple.xbs/Sources/SiriFoundation/SiriFoundation/SRFEnablementFlowConfigurationProvider.m"
- "/AppleInternal/Library/BuildRoots/5d7f20e9-d19f-11ef-9955-d285688f7a47/Library/Caches/com.apple.xbs/Sources/SiriFoundation/SiriFoundation/SRFFoundationAdditions.m"
- "/AppleInternal/Library/BuildRoots/5d7f20e9-d19f-11ef-9955-d285688f7a47/Library/Caches/com.apple.xbs/Sources/SiriFoundation/SiriFoundation/SRFPreferences.m"
- "/AppleInternal/Library/BuildRoots/5d7f20e9-d19f-11ef-9955-d285688f7a47/Library/Caches/com.apple.xbs/Sources/SiriFoundation/SiriFoundation/SRFUserDefaultsController.m"
- "T@\"NSDictionary\",D"
- "disableHotKey"
- "hotKeyMigrationIfNeeded:"
- "hotKeyValue"

```
