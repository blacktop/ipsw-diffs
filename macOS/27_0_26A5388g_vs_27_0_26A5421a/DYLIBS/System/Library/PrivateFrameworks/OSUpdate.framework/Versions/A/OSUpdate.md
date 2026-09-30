## OSUpdate

> `/System/Library/PrivateFrameworks/OSUpdate.framework/Versions/A/OSUpdate`

```diff

-2412.0.5.0.0
-  __TEXT.__text: 0x92b08
-  __TEXT.__objc_methlist: 0x7b9c
-  __TEXT.__const: 0x1f1
-  __TEXT.__cstring: 0x8102
-  __TEXT.__oslogstring: 0xdc19
-  __TEXT.__gcc_except_tab: 0x1b54
+2412.1.1.0.0
+  __TEXT.__text: 0x92abc
+  __TEXT.__objc_methlist: 0x7b94
+  __TEXT.__const: 0x201
+  __TEXT.__cstring: 0x813d
+  __TEXT.__oslogstring: 0xdc6b
+  __TEXT.__gcc_except_tab: 0x1b34
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x2018
+  __TEXT.__unwind_info: 0x2020
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x6f8
   __DATA_CONST.__got: 0xa58
-  __AUTH_CONST.__const: 0x2d00
-  __AUTH_CONST.__cfstring: 0x6100
-  __AUTH_CONST.__objc_const: 0xa100
+  __AUTH_CONST.__const: 0x2ca0
+  __AUTH_CONST.__cfstring: 0x6140
+  __AUTH_CONST.__objc_const: 0xa098
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__auth_got: 0x5e0
-  __AUTH.__objc_data: 0xc30
-  __DATA.__objc_ivar: 0x788
+  __AUTH.__objc_data: 0xc80
+  __DATA.__objc_ivar: 0x784
   __DATA.__data: 0x612
   __DATA.__bss: 0x48
-  __DATA_DIRTY.__objc_data: 0xcd0
+  __DATA_DIRTY.__objc_data: 0xc80
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 3350
-  Symbols:   7226
-  CStrings:  2239
+  Symbols:   7225
+  CStrings:  2241
 
Symbols:
+ -[SUOSUClient refreshAvailableUpdates]
+ -[SUOSUClient startScanningForUpdates]
+ -[SUOSUScanPolicy .cxx_destruct]
+ -[SUOSUScanPolicy clientManager]
+ -[SUOSUScanPolicy initWithSharedPrefs:clientManager:msuController:installTonightManager:]
+ -[SUOSUScanPolicy installTonightManager]
+ -[SUOSUScanPolicy invalidateLastSuccessfulMSUScan]
+ -[SUOSUScanPolicy isBackgroundActivityScanAllowed:]
+ -[SUOSUScanPolicy msuController]
+ -[SUOSUScanPolicy recordSuccessfulBackgroundAction]
+ -[SUOSUScanPolicy recordSuccessfulMSUScan]
+ -[SUOSUScanPolicy sharedPrefs]
+ -[SUOSUScanPolicy shouldClientScanOnLaunchForClientType:availableMSUUpdates:]
+ -[SUOSUServiceDaemon scanPolicy]
+ -[SUOSUServiceDaemon setScanPolicy:]
+ -[SUOSUServiceDaemon shouldClientScanOnLaunchForClientType:completion:]
+ -[SUOSUShimController _startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:]
+ -[SUOSUShimController _startScanningForUpdatesWithBackground:]
+ -[SUOSUShimController refreshAvailableUpdates]
+ -[SUOSUShimController startScanningForUpdates]
+ -[SUOSUUpdateController shouldClientScanOnLaunchForClientType:]
+ GCC_except_table153
+ GCC_except_table155
+ GCC_except_table156
+ GCC_except_table179
+ GCC_except_table188
+ GCC_except_table192
+ GCC_except_table198
+ GCC_except_table201
+ GCC_except_table204
+ GCC_except_table205
+ GCC_except_table210
+ GCC_except_table211
+ GCC_except_table221
+ GCC_except_table225
+ GCC_except_table228
+ GCC_except_table233
+ GCC_except_table239
+ GCC_except_table242
+ GCC_except_table247
+ GCC_except_table251
+ GCC_except_table258
+ GCC_except_table263
+ GCC_except_table264
+ GCC_except_table289
+ GCC_except_table290
+ GCC_except_table298
+ GCC_except_table308
+ GCC_except_table74
+ OBJC_IVAR_$_SUOSUScanPolicy._clientManager
+ OBJC_IVAR_$_SUOSUScanPolicy._installTonightManager
+ OBJC_IVAR_$_SUOSUScanPolicy._msuController
+ OBJC_IVAR_$_SUOSUScanPolicy._sharedPrefs
+ OBJC_IVAR_$_SUOSUServiceDaemon._scanPolicy
+ _OBJC_CLASS_$_SUOSUScanPolicy
+ _OBJC_METACLASS_$_SUOSUScanPolicy
+ __106-[SUOSUShimController _startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:]_block_invoke
+ __106-[SUOSUShimController _startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:]_block_invoke_4
+ __62-[SUOSUShimController _startScanningForUpdatesWithBackground:]_block_invoke
+ __62-[SUOSUShimController _startScanningForUpdatesWithBackground:]_block_invoke_2
+ __OBJC_$_INSTANCE_METHODS_SUOSUScanPolicy
+ __OBJC_$_INSTANCE_VARIABLES_SUOSUScanPolicy
+ __OBJC_$_PROP_LIST_SUOSUScanPolicy
+ __OBJC_CLASS_RO_$_SUOSUScanPolicy
+ __OBJC_METACLASS_RO_$_SUOSUScanPolicy
+ ___106-[SUOSUShimController _startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:]_block_invoke
+ ___106-[SUOSUShimController _startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:]_block_invoke_2
+ ___106-[SUOSUShimController _startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:]_block_invoke_3
+ ___106-[SUOSUShimController _startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:]_block_invoke_4
+ ___46-[SUOSUShimController refreshAvailableUpdates]_block_invoke
+ ___51-[SUOSUScanPolicy isBackgroundActivityScanAllowed:]_block_invoke
+ ___62-[SUOSUShimController _startScanningForUpdatesWithBackground:]_block_invoke
+ ___62-[SUOSUShimController _startScanningForUpdatesWithBackground:]_block_invoke_2
+ ___63-[SUOSUUpdateController shouldClientScanOnLaunchForClientType:]_block_invoke
+ ___71-[SUOSUServiceDaemon shouldClientScanOnLaunchForClientType:completion:]_block_invoke
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0l
+ _kSUOSUScanOnLaunchIntervalWithAvailableUpdates
+ _kSUOSUScanOnLaunchIntervalWithoutAvailableUpdates
+ _objc_msgSend$_startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:
+ _objc_msgSend$_startScanningForUpdatesWithBackground:
+ _objc_msgSend$invalidateLastSuccessfulMSUScan
+ _objc_msgSend$isBackgroundActivityScanAllowed:
+ _objc_msgSend$lastCatalogChangeDate
+ _objc_msgSend$lastSuccessfulMSUBackgroundActionDate
+ _objc_msgSend$lastSuccessfulMSUScanDate
+ _objc_msgSend$recordSuccessfulBackgroundAction
+ _objc_msgSend$recordSuccessfulMSUScan
+ _objc_msgSend$refreshAvailableUpdates
+ _objc_msgSend$scanPolicy
+ _objc_msgSend$setLastSuccessfulMSUBackgroundActionDate:
+ _objc_msgSend$setLastSuccessfulMSUScanDate:
+ _objc_msgSend$shouldClientScanOnLaunchForClientType:
+ _objc_msgSend$shouldClientScanOnLaunchForClientType:availableMSUUpdates:
+ _objc_msgSend$shouldClientScanOnLaunchForClientType:completion:
+ _objc_msgSend$startScanningForUpdates
- -[SUOSUBackgroundScanPolicy .cxx_destruct]
- -[SUOSUBackgroundScanPolicy clientManager]
- -[SUOSUBackgroundScanPolicy initWithSharedPrefs:clientManager:msuController:installTonightManager:]
- -[SUOSUBackgroundScanPolicy installTonightManager]
- -[SUOSUBackgroundScanPolicy isBackgroundScanAllowed:]
- -[SUOSUBackgroundScanPolicy msuController]
- -[SUOSUBackgroundScanPolicy recordSuccessfulBackgroundScan]
- -[SUOSUBackgroundScanPolicy sharedPrefs]
- -[SUOSUClient latestSuccessfulScanDate]
- -[SUOSUClient startScanningForLegacyUpdatesEvenIfUnchanged:]
- -[SUOSUClient startScanningForUpdatesEvenIfUnchanged:]
- -[SUOSUClient startScanningForUpdatesEvenIfUnchanged:withCompletionHandler:]
- -[SUOSUServiceDaemon backgroundScanPolicy]
- -[SUOSUServiceDaemon setBackgroundScanPolicy:]
- -[SUOSUShimController _shouldRescan]
- -[SUOSUShimController latestCatalogModifiedDate]
- -[SUOSUShimController latestSuccessfulScanDate]
- -[SUOSUShimController setLatestCatalogModifiedDate:]
- -[SUOSUShimController startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:]
- -[SUOSUShimController startScanningForUpdatesEvenIfUnchanged:background:withCompletionHandler:]
- -[SUOSUShimController startScanningForUpdatesEvenIfUnchanged:withCompletionHandler:]
- GCC_except_table154
- GCC_except_table157
- GCC_except_table16
- GCC_except_table171
- GCC_except_table181
- GCC_except_table182
- GCC_except_table190
- GCC_except_table194
- GCC_except_table199
- GCC_except_table203
- GCC_except_table206
- GCC_except_table207
- GCC_except_table209
- GCC_except_table213
- GCC_except_table218
- GCC_except_table223
- GCC_except_table229
- GCC_except_table237
- GCC_except_table240
- GCC_except_table245
- GCC_except_table249
- GCC_except_table254
- GCC_except_table259
- GCC_except_table262
- GCC_except_table285
- GCC_except_table288
- GCC_except_table294
- GCC_except_table306
- GCC_except_table72
- GCC_except_table80
- GCC_except_table83
- OBJC_IVAR_$_SUOSUBackgroundScanPolicy._clientManager
- OBJC_IVAR_$_SUOSUBackgroundScanPolicy._installTonightManager
- OBJC_IVAR_$_SUOSUBackgroundScanPolicy._msuController
- OBJC_IVAR_$_SUOSUBackgroundScanPolicy._sharedPrefs
- OBJC_IVAR_$_SUOSUServiceDaemon._backgroundScanPolicy
- OBJC_IVAR_$_SUOSUShimController._latestCatalogModifiedDate
- _OBJC_CLASS_$_SUOSUBackgroundScanPolicy
- _OBJC_METACLASS_$_SUOSUBackgroundScanPolicy
- __105-[SUOSUShimController startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:]_block_invoke
- __105-[SUOSUShimController startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:]_block_invoke_4
- __95-[SUOSUShimController startScanningForUpdatesEvenIfUnchanged:background:withCompletionHandler:]_block_invoke
- __95-[SUOSUShimController startScanningForUpdatesEvenIfUnchanged:background:withCompletionHandler:]_block_invoke_2
- __OBJC_$_INSTANCE_METHODS_SUOSUBackgroundScanPolicy
- __OBJC_$_INSTANCE_VARIABLES_SUOSUBackgroundScanPolicy
- __OBJC_$_PROP_LIST_SUOSUBackgroundScanPolicy
- __OBJC_CLASS_RO_$_SUOSUBackgroundScanPolicy
- __OBJC_METACLASS_RO_$_SUOSUBackgroundScanPolicy
- ___105-[SUOSUShimController startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:]_block_invoke
- ___105-[SUOSUShimController startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:]_block_invoke_2
- ___105-[SUOSUShimController startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:]_block_invoke_3
- ___105-[SUOSUShimController startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:]_block_invoke_4
- ___53-[SUOSUBackgroundScanPolicy isBackgroundScanAllowed:]_block_invoke
- ___95-[SUOSUShimController startScanningForUpdatesEvenIfUnchanged:background:withCompletionHandler:]_block_invoke
- ___95-[SUOSUShimController startScanningForUpdatesEvenIfUnchanged:background:withCompletionHandler:]_block_invoke_2
- ___block_descriptor_50_e8_32s40bs_e5_v8?0l
- ___block_descriptor_64_e8_32s40bs48r56r_e17_v16?0"NSError"8l
- ___block_descriptor_72_e8_32s40s48bs56r64r_e5_v8?0l
- ___copy_helper_block_e8_32s40b48r56r
- ___copy_helper_block_e8_32s40s48b56r64r
- ___destroy_helper_block_e8_32s40s48s56r64r
- _objc_msgSend$_shouldRescan
- _objc_msgSend$backgroundScanPolicy
- _objc_msgSend$isBackgroundScanAllowed:
- _objc_msgSend$lastCatalogChangedDate
- _objc_msgSend$lastScanSuccessfulDate
- _objc_msgSend$lastSuccessfulMSUBackgroundScanDate
- _objc_msgSend$latestCatalogModifiedDate
- _objc_msgSend$latestSuccessfulScanDate
- _objc_msgSend$recordSuccessfulBackgroundScan
- _objc_msgSend$setLastSuccessfulMSUBackgroundScanDate:
- _objc_msgSend$setLastSuccessfulScanDate:
- _objc_msgSend$startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:
- _objc_msgSend$startScanningForUpdatesEvenIfUnchanged:background:withCompletionHandler:
- _objc_msgSend$startScanningForUpdatesEvenIfUnchanged:withCompletionHandler:
CStrings:
+ "%@: Client should scan on launch: catalog changed since last successful MSU scan"
+ "%@: Client should scan on launch: last successful MSU scan was %0.1fs ago (interval %0.1fs, updates available: %i)"
+ "%@: Client shouldn't scan on launch: recent successful MSU scan (%0.1fs ago)"
+ "26A350"
+ "Controller: currentPallasAudience - %@, shouldScan - %d, productKeysInActiveForegroundTransactions - %lu, client = %lu, foregroundScan: %hhd"
+ "[MAJOR] macOS Golden Gate 27.0"
+ "[MINOR] macOS Tahoe 26.6"
+ "[SPLAT COMBO] macOS Tahoe 26.6 (b)"
+ "[internal only] last successful background action was %@"
+ "https://www.apple.com/macos/"
- "%@: Catalog has been modified since last scan, should re-scan"
- "%@: Skipping re-scanning for updates"
- "%@: Time interval since last scan: %0.1f (updates available: %i)"
- "Controller: currentPallasAudience - %@, shouldScan - %d, productKeysInActiveForegroundTransactions - %lu, client = %lu, shouldScanForClient: %hhd, foregroundScan: %hhd"
- "[MAJOR] macOS Sequoia"
- "[MINOR] macOS Sonoma"
- "[SPLAT COMBO] macOS Sonoma"
- "[internal only] last successful background scan was %@"
```
