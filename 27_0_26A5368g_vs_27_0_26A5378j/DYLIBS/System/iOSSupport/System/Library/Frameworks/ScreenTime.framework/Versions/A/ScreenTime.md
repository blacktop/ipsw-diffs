## ScreenTime

> `/System/iOSSupport/System/Library/Frameworks/ScreenTime.framework/Versions/A/ScreenTime`

```diff

-  __TEXT.__text: 0x48cc
-  __TEXT.__objc_methlist: 0x724
-  __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x32c
-  __TEXT.__gcc_except_tab: 0xa8
-  __TEXT.__oslogstring: 0x540
-  __TEXT.__unwind_info: 0x250
+  __TEXT.__text: 0x565c
+  __TEXT.__objc_methlist: 0x7b4
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x396
+  __TEXT.__gcc_except_tab: 0xf0
+  __TEXT.__oslogstring: 0x622
+  __TEXT.__unwind_info: 0x280
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d0
+  __DATA_CONST.__objc_selrefs: 0x640
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__got: 0x150
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x220
-  __AUTH_CONST.__objc_const: 0xeb8
+  __AUTH_CONST.__cfstring: 0x260
+  __AUTH_CONST.__objc_const: 0xf78
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x58
+  __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x240
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x10

   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 165
-  Symbols:   571
-  CStrings:  65
+  Functions: 185
+  Symbols:   621
+  CStrings:  73
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
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
+ GCC_except_table16
+ GCC_except_table19
+ OBJC_IVAR_$_STScreenTimeConfigurationObserver._hasReceivedLegacyConfiguration
+ OBJC_IVAR_$_STScreenTimeConfigurationObserver._legacyEnforcesChildRestrictions
+ OBJC_IVAR_$_STScreenTimeConfigurationObserver._webBrowserSettingsObserver
+ OBJC_IVAR_$_STWebHistory._screenTimeWebBrowserHistory
+ _OBJC_CLASS_$_STScreenTimeWebBrowserHistory
+ _OBJC_CLASS_$_STScreenTimeWebBrowserSettingsObserver
+ __53-[STWebHistory fetchAllHistoryWithCompletionHandler:]_block_invoke_2
+ __61-[STWebHistory fetchHistoryDuringInterval:completionHandler:]_block_invoke_2
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
- GCC_except_table10
- GCC_except_table14
- __53-[STWebHistory fetchAllHistoryWithCompletionHandler:]_block_invoke
- __61-[STWebHistory fetchHistoryDuringInterval:completionHandler:]_block_invoke
- _objc_msgSend$_updateWithConfiguration:
CStrings:
+ "Failed to delete all web history with ScreenTimeSettings: %{public}@"
+ "Failed to delete history during %{private}@ with ScreenTimeSettings: %{public}@"
+ "Failed to delete history for %{private}@ with ScreenTimeSettings: %{public}@"
+ "KVOContextSTScreenTimeConfigurationObserver"
+ "webBrowserSettings.hasMigrated"
+ "webBrowserSettings.hasPasscode"

```
