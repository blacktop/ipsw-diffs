## UniversalAccessCore

> `/System/Library/PrivateFrameworks/UniversalAccess.framework/Versions/A/Frameworks/UniversalAccessCore.framework/Versions/A/UniversalAccessCore`

```diff

-696.3.1.0.0
-  __TEXT.__text: 0x2992c
+696.5.5.0.0
+  __TEXT.__text: 0x29cac
   __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_methlist: 0x1e00
+  __TEXT.__objc_methlist: 0x1fc8
   __TEXT.__const: 0x358
   __TEXT.__cstring: 0x2756
   __TEXT.__oslogstring: 0x1202
   __TEXT.__gcc_except_tab: 0xe4
   __TEXT.__dlopen_cstrs: 0x1c0
-  __TEXT.__unwind_info: 0xbc8
+  __TEXT.__unwind_info: 0xc08
   __TEXT.__objc_classname: 0x20d
   __TEXT.__objc_methname: 0x6554
   __TEXT.__objc_methtype: 0x54e
   __TEXT.__objc_stubs: 0x45c0
-  __DATA_CONST.__got: 0xc50
+  __DATA_CONST.__got: 0xc18
   __DATA_CONST.__const: 0x270
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1920
+  __DATA_CONST.__objc_selrefs: 0x19b0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x1d8
   __AUTH_CONST.__auth_got: 0x648
   __AUTH_CONST.__const: 0x9b0
   __AUTH_CONST.__cfstring: 0x1f80
-  __AUTH_CONST.__objc_const: 0x2788
+  __AUTH_CONST.__objc_const: 0x2450
   __AUTH_CONST.__objc_intobj: 0x720
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libUniversalAccess.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B4E9E9CA-0042-3729-A61D-AECCA8F6BEE2
-  Functions: 1351
-  Symbols:   2968
+  UUID: FFB23021-5BF6-36C9-B1FF-3DCDA7626A6D
+  Functions: 1386
+  Symbols:   2999
   CStrings:  1840
 
Symbols:
+ +[NSDictionary(SwitchInput) _hidDictionaryDeviceKeysToCompare].cold.1
+ +[UABaseSystem shared].cold.1
+ +[UALoginWindowFeatureManager _orderedAvailableFeatureTypes].cold.2
+ +[UANVRAM availableLoginWindowFeatures].cold.1
+ +[UANVRAM shared].cold.1
+ +[UASettingsTransaction _commitRootTransaction].cold.2
+ +[UASettingsTransaction _rootTransactionBlocks].cold.1
+ +[UASettingsTransaction _transactionIdentifiers].cold.1
+ +[UASettingsTransaction beginTransaction:].cold.3
+ +[UASettingsTransaction beginTransaction:].cold.4
+ +[UASettingsTransaction endTransaction:].cold.4
+ +[UASettingsTransaction endTransaction:].cold.5
+ +[UASettingsTransaction hasCurrentTransaction].cold.1
+ +[UASettingsTransaction performOnFinalTransactionCommit:].cold.1
+ +[UASettingsTransaction performOnFinalTransactionCommit:].cold.2
+ +[UASettingsTransaction performWithTransaction:work:].cold.1
+ +[UASettingsTransaction performWithTransaction:work:].cold.2
+ +[UASwitchUtilities _hidDictionaryDeviceKeysToCompare].cold.1
+ +[UASystemSettings shared].cold.1
+ +[_UAPMouseAlertEventHandler defaultHandler].cold.1
+ -[UAShortcutManager init].cold.1
+ UAAlternateMouseButtonsDefaultActions.cold.1
+ UAAlternateMouseButtonsOrderedActions.cold.1
+ UADaemonLog.cold.1
+ UADisplayLog.cold.1
+ UAIsRunningOutsideLoginWindowSession.cold.1
+ UAKeyboardAccessAvailableCommands.cold.1
+ UAKeyboardLog.cold.1
+ UALiveSpeechLog.cold.1
+ UAMouseLog.cold.1
+ UAOptionsLog.cold.1
+ UAPointerControlLog.cold.1
+ UAShortcutsLog.cold.1
+ UASymbolNameForFeature.cold.1
+ UAUserSwitchActionTypes.cold.1
+ UAZoomLog.cold.1
+ _UAFeatureIDFromFeatureName.cold.1
- _OUTLINED_FUNCTION_6

```
