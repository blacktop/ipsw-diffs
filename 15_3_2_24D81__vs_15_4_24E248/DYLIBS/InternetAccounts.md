## InternetAccounts

> `/System/Library/PrivateFrameworks/InternetAccounts.framework/Versions/A/InternetAccounts`

```diff

 300.0.0.0.0
-  __TEXT.__text: 0x3e924
+  __TEXT.__text: 0x3e240
   __TEXT.__auth_stubs: 0x880
-  __TEXT.__objc_methlist: 0x3884
+  __TEXT.__objc_methlist: 0x3c6c
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x11d0
+  __TEXT.__gcc_except_tab: 0x11d4
   __TEXT.__cstring: 0x7211
   __TEXT.__oslogstring: 0x3d
-  __TEXT.__unwind_info: 0xe98
+  __TEXT.__unwind_info: 0xe80
   __TEXT.__objc_classname: 0x796
   __TEXT.__objc_methname: 0x8768
   __TEXT.__objc_methtype: 0xeee
   __TEXT.__objc_stubs: 0x70e0
   __DATA_CONST.__got: 0x570
-  __DATA_CONST.__const: 0x788
+  __DATA_CONST.__const: 0x850
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26e0
+  __DATA_CONST.__objc_selrefs: 0x2768
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x170
   __AUTH_CONST.__auth_got: 0x450
   __AUTH_CONST.__const: 0xdc0
   __AUTH_CONST.__cfstring: 0x6c00
-  __AUTH_CONST.__objc_const: 0x7fe0
+  __AUTH_CONST.__objc_const: 0x78d0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x1680

   __DATA.__data: 0x45c
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x240
-  __DATA.__common: 0x38
+  __DATA.__common: 0x33
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2919997A-5BBC-304D-BBFD-5A7B5C6223D1
-  Functions: 1363
-  Symbols:   3943
+  UUID: EB7B5D8A-908F-3A52-8C77-52CB09B61DC0
+  Functions: 1379
+  Symbols:   3965
   CStrings:  3861
 
Symbols:
+ +[ACAccountsHelper storeQueue].cold.1
+ +[ACAccountsHelper store].cold.1
+ +[IAAccountCollector shared].cold.1
+ +[IADNSCache shared].cold.1
+ +[IAExtensionManager shared].cold.1
+ +[IAPluginManager shared].cold.1
+ +[IAProvider aListProviderIDs].cold.1
+ +[IAProvider dataProviderIDs].cold.1
+ -[IAAListPlugin displayTypeForRegion:].cold.1
+ -[IAAccountCollector parentGoogleAccountForChildAccountWithUID:].cold.1
+ -[IAAccountCreator _exchangeAutodiscoverForSettings:].cold.1
+ -[IADataPluginController plugin:performBlock:withTimeOut:].cold.1
+ -[IAGoogleAuthTokenManager displayGoogleWebLoginAlertInWindow:withWebLoginURL:completion:].cold.1
+ -[IAGoogleAuthTokenManager displayGoogleWebLoginAlertInWindow:withWebLoginURL:completion:].cold.2
+ -[IAPlugin isSocial].cold.1
+ -[IAPluginManager pluginIDForDomain:].cold.1
+ IADebugLog.cold.1
+ IADebugLoggingPath.cold.1
+ IAKeyboardRegionEquivalents.cold.1
+ IAPluginIDCompare.cold.1
+ __IADebugLog_block_invoke.cold.1
+ iaMigratorLog.cold.1

```
