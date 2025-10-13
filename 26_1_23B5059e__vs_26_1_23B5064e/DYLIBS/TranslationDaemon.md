## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

-355.1.0.0.0
-  __TEXT.__text: 0x193944
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x19bd8
+355.2.0.0.0
+  __TEXT.__text: 0x19480c
+  __TEXT.__auth_stubs: 0xd40
+  __TEXT.__objc_methlist: 0x19c30
   __TEXT.__const: 0x450
-  __TEXT.__gcc_except_tab: 0x1b35c
-  __TEXT.__cstring: 0x5af4
-  __TEXT.__oslogstring: 0xc1d8
+  __TEXT.__gcc_except_tab: 0x1b370
+  __TEXT.__cstring: 0x5c47
+  __TEXT.__oslogstring: 0xc399
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__unwind_info: 0xf488
+  __TEXT.__unwind_info: 0xf4b8
   __TEXT.__objc_classname: 0x4748
-  __TEXT.__objc_methname: 0x1b1d7
+  __TEXT.__objc_methname: 0x1b2a0
   __TEXT.__objc_methtype: 0xdfac
-  __TEXT.__objc_stubs: 0x129c0
-  __DATA_CONST.__got: 0xca0
-  __DATA_CONST.__const: 0x3f50
+  __TEXT.__objc_stubs: 0x12aa0
+  __DATA_CONST.__got: 0xca8
+  __DATA_CONST.__const: 0x3ff8
   __DATA_CONST.__objc_classlist: 0x1198
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x67b0
+  __DATA_CONST.__objc_selrefs: 0x67e8
   __DATA_CONST.__objc_superrefs: 0x1108
   __DATA_CONST.__objc_arraydata: 0x2a0
-  __AUTH_CONST.__auth_got: 0x6a8
+  __AUTH_CONST.__auth_got: 0x6b8
   __AUTH_CONST.__const: 0xae0
-  __AUTH_CONST.__cfstring: 0x7700
-  __AUTH_CONST.__objc_const: 0x2c450
+  __AUTH_CONST.__cfstring: 0x77e0
+  __AUTH_CONST.__objc_const: 0x2c470
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH.__objc_data: 0xa398
-  __DATA.__objc_ivar: 0x1178
+  __DATA.__objc_ivar: 0x117c
   __DATA.__data: 0xa68
   __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0xc58

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B673A341-95EC-3BAE-8DA4-5A76B7A395A6
-  Functions: 9957
-  Symbols:   33817
-  CStrings:  9067
+  UUID: 390CBC89-DEC7-3F96-8766-9EFAD42A4BD0
+  Functions: 9976
+  Symbols:   33873
+  CStrings:  9103
 
Symbols:
+ +[_LTDLanguageAssetService _cacheInstalledLanguages]
+ +[_LTDLanguageAssetService _cacheInstalledLanguages].cold.1
+ +[_LTDLanguageAssetService _offlineStateFromString:]
+ +[_LTDLanguageAssetService _resetSymlinkDirectory]
+ +[_LTDLanguageAssetService _resetSymlinkDirectory].cold.1
+ +[_LTDLanguageAssetService _resetSymlinkDirectory].cold.2
+ +[_LTDLanguageAssetService _resetSymlinkDirectory].cold.3
+ +[_LTDLanguageAssetService _stringForOfflineState:]
+ +[_LTDLanguageAssetService _synthesizeInitialObservationsFromDefaults]
+ -[_LTDDaemon _setupNotifyHandlers]
+ -[_LTTranslationServer ensureSelectedLocalesDownload]
+ GCC_except_table100
+ _OBJC_IVAR_$__LTDDaemon._notifyHandlerQueue
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ __LTPreferencesOfflineLanguageInstallationStatus
+ __LTPreferencesSetOfflineLanguageInstallationStatus
+ ___34-[_LTDDaemon _setupNotifyHandlers]_block_invoke
+ ___44+[_LTDLanguageAssetService removeLanguages:]_block_invoke
+ ___52+[_LTDLanguageAssetService _cacheInstalledLanguages]_block_invoke
+ ___52+[_LTDLanguageAssetService _cacheInstalledLanguages]_block_invoke_2
+ ___53-[_LTTranslationServer ensureSelectedLocalesDownload]_block_invoke
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.51
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.52
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.43
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.43.cold.1
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.43.cold.2
+ ___61+[_LTDLanguageAssetService syncInstalledLocalesOnAssetUpdate]_block_invoke.40
+ ___61+[_LTDLanguageAssetService syncInstalledLocalesOnAssetUpdate]_block_invoke.40.cold.1
+ ___64+[_LTDLanguageAssetService _syncInstalledLocalesWithCompletion:]_block_invoke.33
+ ___64+[_LTDLanguageAssetService _syncInstalledLocalesWithCompletion:]_block_invoke.36
+ ___66+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:gateID:]_block_invoke.37
+ ___66+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:gateID:]_block_invoke.37.cold.1
+ ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.24
+ ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.24.cold.1
+ ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.25
+ ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.30
+ ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.30.cold.1
+ ___97+[_LTDLanguageAssetService startLanguageStatusSession:taskHint:progress:observations:completion:]_block_invoke.cold.1
+ ___block_descriptor_32_e41_"NSString"16?0"_LTLanguageAssetModel"8l
+ ___block_descriptor_40_e15_v16?0?<v?B>8l
+ ___block_descriptor_40_e8_32w_e33_v16?0"NSObject<OS_xpc_object>"8lw32l8
+ ___block_descriptor_56_e8_32bs40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_96_e8_32s40s48s56bs64bs72bs_e29_v24?0"NSArray"8"NSError"16ls56l8s64l8s32l8s40l8s48l8s72l8
+ ___block_literal_global.214
+ ___block_literal_global.35
+ ___block_literal_global.47
+ ___block_literal_global.65
+ ___block_literal_global.68
+ ___block_literal_global.71
+ __xpc_event_key_name
+ _objc_msgSend$_cacheInstalledLanguages
+ _objc_msgSend$_offlineStateFromString:
+ _objc_msgSend$_resetSymlinkDirectory
+ _objc_msgSend$_setupNotifyHandlers
+ _objc_msgSend$_stringForOfflineState:
+ _objc_msgSend$_synthesizeInitialObservationsFromDefaults
+ _objc_msgSend$ensureSelectedLocalesDownload
+ _objc_msgSend$initWithUTF8String:
+ _xpc_dictionary_get_string
+ _xpc_set_event_stream_handler
- +[_LTDAssetService registerAssetSetUpdateHandler]
- ___49+[_LTDAssetService registerAssetSetUpdateHandler]_block_invoke
- ___49+[_LTDAssetService registerAssetSetUpdateHandler]_block_invoke.396
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.47
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.48
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.41
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.41.cold.1
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.41.cold.2
- ___61+[_LTDLanguageAssetService syncInstalledLocalesOnAssetUpdate]_block_invoke.38
- ___61+[_LTDLanguageAssetService syncInstalledLocalesOnAssetUpdate]_block_invoke.38.cold.1
- ___64+[_LTDLanguageAssetService _syncInstalledLocalesWithCompletion:]_block_invoke.31
- ___64+[_LTDLanguageAssetService _syncInstalledLocalesWithCompletion:]_block_invoke.34
- ___66+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:gateID:]_block_invoke.35
- ___66+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:gateID:]_block_invoke.35.cold.1
- ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.22
- ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.27
- ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.27.cold.1
- ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.cold.1
- ___block_descriptor_88_e8_32s40s48s56bs64bs_e29_v24?0"NSArray"8"NSError"16ls56l8s32l8s40l8s48l8s64l8
- ___block_literal_global.211
- ___block_literal_global.33
- ___block_literal_global.395
- ___block_literal_global.398
- ___block_literal_global.43
- _objc_msgSend$registerAssetSetUpdateHandler
CStrings:
+ "/Translation/Assets"
+ "@\"NSString\"16@?0@\"_LTLanguageAssetModel\"8"
+ "Cache is not ready, returning immediate data from Defaults"
+ "Creation of symlink folder %@ failed: %@"
+ "Got xpc event for notification %{public}s"
+ "OfflineLanguageInstallationStatus"
+ "Removal of symlink folder %@ aborted due to failed sanity check"
+ "Removal of symlink folder %@ failed: %@"
+ "Removal of symlink folder aborted due to locale selections prior to dequeue"
+ "Removing symlink folder %@"
+ "There are no lastObservations"
+ "Using lastObservations"
+ "Using synthesized observations %@"
+ "Writing to UserDefaults: %{public}@"
+ "_cacheInstalledLanguages"
+ "_notifyHandlerQueue"
+ "_offlineStateFromString:"
+ "_resetSymlinkDirectory"
+ "_setupNotifyHandlers"
+ "_stringForOfflineState:"
+ "_synthesizeInitialObservationsFromDefaults"
+ "com.apple.notifyd.matching"
+ "com.apple.siri.uaf.com.apple.sequoia.asset"
+ "com.apple.siri.uaf.com.apple.speech.automaticspeechrecognition"
+ "com.apple.translation.daemon.notifyHander"
+ "ensureSelectedLocalesDownload"
+ "initWithUTF8String:"
+ "installed"
+ "unavailable"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
- "ASR asset update event"
- "registerAssetSetUpdateHandler"

```
