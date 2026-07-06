## ScreenTime

> `/System/Library/Frameworks/ScreenTime.framework/Versions/A/ScreenTime`

```diff

-  __TEXT.__text: 0x534c
-  __TEXT.__objc_methlist: 0x72c
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x3ba
-  __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__oslogstring: 0x544
-  __TEXT.__unwind_info: 0x278
+  __TEXT.__text: 0x6204
+  __TEXT.__objc_methlist: 0x7bc
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x424
+  __TEXT.__gcc_except_tab: 0xf4
+  __TEXT.__oslogstring: 0x626
+  __TEXT.__unwind_info: 0x2a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f0
+  __DATA_CONST.__objc_selrefs: 0x660
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__got: 0x158
   __AUTH_CONST.__const: 0x450
-  __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0xf28
+  __AUTH_CONST.__cfstring: 0x2c0
+  __AUTH_CONST.__objc_const: 0xfe8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x54
+  __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x240
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 181
-  Symbols:   577
-  CStrings:  71
+  Functions: 201
+  Symbols:   627
+  CStrings:  79
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[STScreenTimeConfigurationObserver _effectiveEnforcesChildRestrictions]
+ -[STScreenTimeConfigurationObserver _stScreenTimeConfigurationObserverCommonInitWithUpdateQueue:webBrowserSettingsObserver:]
+ -[STScreenTimeConfigurationObserver hasReceivedLegacyConfiguration]
+ -[STScreenTimeConfigurationObserver initWithUpdateQueue:webBrowserSettingsObserver:]
+ -[STScreenTimeConfigurationObserver legacyEnforcesChildRestrictions]
+ -[STScreenTimeConfigurationObserver observeValueForKeyPath:ofObject:change:context:]
+ -[STScreenTimeConfigurationObserver setHasReceivedLegacyConfiguration:]
+ -[STScreenTimeConfigurationObserver setLegacyEnforcesChildRestrictions:]
+ -[STScreenTimeConfigurationObserver webBrowserSettingsObserver]
+ -[STWebHistory dealloc]
+ -[STWebHistory initWithBundleIdentifier:profileIdentifier:screenTimeWebBrowserHistory:]
+ -[STWebHistory initWithBundleIdentifier:profileIdentifier:screenTimeWebBrowserHistory:error:]
+ -[STWebHistory screenTimeWebBrowserHistory]
+ GCC_except_table12
+ GCC_except_table18
+ GCC_except_table23
+ OBJC_IVAR_$_STScreenTimeConfigurationObserver._hasReceivedLegacyConfiguration
+ OBJC_IVAR_$_STScreenTimeConfigurationObserver._legacyEnforcesChildRestrictions
+ OBJC_IVAR_$_STScreenTimeConfigurationObserver._webBrowserSettingsObserver
+ OBJC_IVAR_$_STWebHistory._screenTimeWebBrowserHistory
+ _OBJC_CLASS_$_STScreenTimeWebBrowserHistory
+ _OBJC_CLASS_$_STScreenTimeWebBrowserSettingsObserver
+ __53-[STWebHistory fetchAllHistoryWithCompletionHandler:]_block_invoke_2
+ ___53-[STWebHistory fetchAllHistoryWithCompletionHandler:]_block_invoke_3
+ _objc_msgSend$_effectiveEnforcesChildRestrictions
+ _objc_msgSend$_stScreenTimeConfigurationObserverCommonInitWithUpdateQueue:webBrowserSettingsObserver:
+ _objc_msgSend$hasMigrated
+ _objc_msgSend$hasPasscode
+ _objc_msgSend$hasReceivedLegacyConfiguration
+ _objc_msgSend$initWithBundleIdentifier:profileIdentifier:screenTimeWebBrowserHistory:
+ _objc_msgSend$initWithBundleIdentifier:profileIdentifier:screenTimeWebBrowserHistory:error:
+ _objc_msgSend$initWithEnforcesChildRestrictions:
+ _objc_msgSend$initWithUpdateQueue:
+ _objc_msgSend$legacyEnforcesChildRestrictions
+ _objc_msgSend$removeObserver:forKeyPath:context:
+ _objc_msgSend$screenTimeWebBrowserHistory
+ _objc_msgSend$setHasReceivedLegacyConfiguration:
+ _objc_msgSend$setLegacyEnforcesChildRestrictions:
+ _objc_msgSend$startObserving
+ _objc_msgSend$stopObserving
+ _objc_msgSend$webBrowserSettings
+ _objc_msgSend$webBrowserSettingsObserver
- -[STScreenTimeConfigurationObserver _updateWithConfiguration:]
- GCC_except_table10
- GCC_except_table16
- __53-[STWebHistory fetchAllHistoryWithCompletionHandler:]_block_invoke
- _objc_msgSend$_updateWithConfiguration:
CStrings:
+ "Failed to delete all web history with ScreenTimeSettings: %{public}@"
+ "Failed to delete history during %{private}@ with ScreenTimeSettings: %{public}@"
+ "Failed to delete history for %{private}@ with ScreenTimeSettings: %{public}@"
+ "KVOContextSTScreenTimeConfigurationObserver"
+ "webBrowserSettings.hasMigrated"
+ "webBrowserSettings.hasPasscode"

```
