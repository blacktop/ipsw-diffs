## ScreenTime

> `/System/Library/Frameworks/ScreenTime.framework/ScreenTime`

```diff

-  __TEXT.__text: 0x471c
-  __TEXT.__objc_methlist: 0x71c
-  __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x2f3
-  __TEXT.__gcc_except_tab: 0xa8
-  __TEXT.__oslogstring: 0x4a6
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__text: 0x54ac
+  __TEXT.__objc_methlist: 0x7ac
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x35d
+  __TEXT.__gcc_except_tab: 0xf0
+  __TEXT.__oslogstring: 0x588
+  __TEXT.__unwind_info: 0x270
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5c0
+  __DATA_CONST.__objc_selrefs: 0x630
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__got: 0x168
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x1e0
-  __AUTH_CONST.__objc_const: 0xe80
+  __AUTH_CONST.__cfstring: 0x220
+  __AUTH_CONST.__objc_const: 0xf40
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x54
+  __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x240
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 165
-  Symbols:   746
-  CStrings:  60
+  Functions: 185
+  Symbols:   821
+  CStrings:  68
 
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
+ GCC_except_table16
+ GCC_except_table19
+ _OBJC_CLASS_$_STScreenTimeWebBrowserHistory
+ _OBJC_CLASS_$_STScreenTimeWebBrowserSettingsObserver
+ _OBJC_IVAR_$_STScreenTimeConfigurationObserver._hasReceivedLegacyConfiguration
+ _OBJC_IVAR_$_STScreenTimeConfigurationObserver._legacyEnforcesChildRestrictions
+ _OBJC_IVAR_$_STScreenTimeConfigurationObserver._webBrowserSettingsObserver
+ _OBJC_IVAR_$_STWebHistory._screenTimeWebBrowserHistory
+ ___53-[STWebHistory fetchAllHistoryWithCompletionHandler:]_block_invoke_3
+ ___61-[STWebHistory fetchHistoryDuringInterval:completionHandler:]_block_invoke_3
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
+ _objc_release_x27
- -[STScreenTimeConfigurationObserver _updateWithConfiguration:]
- GCC_except_table14
- _objc_msgSend$_updateWithConfiguration:
CStrings:
+ "Failed to delete all web history with ScreenTimeSettings: %{public}@"
+ "Failed to delete history during %{private}@ with ScreenTimeSettings: %{public}@"
+ "Failed to delete history for %{private}@ with ScreenTimeSettings: %{public}@"
+ "KVOContextSTScreenTimeConfigurationObserver"
+ "webBrowserSettings.hasMigrated"
+ "webBrowserSettings.hasPasscode"

```
