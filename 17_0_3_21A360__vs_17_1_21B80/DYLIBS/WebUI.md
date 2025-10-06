## WebUI

> `/System/Library/PrivateFrameworks/WebUI.framework/WebUI`

```diff

-616.1.27.10.16
-  __TEXT.__text: 0xff6c
+616.2.9.10.10
+  __TEXT.__text: 0xf98c
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0xb74
+  __TEXT.__objc_methlist: 0xb2c
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x418
-  __TEXT.__cstring: 0xc1e
-  __TEXT.__oslogstring: 0x4f6
+  __TEXT.__gcc_except_tab: 0x3fc
+  __TEXT.__cstring: 0xc29
+  __TEXT.__oslogstring: 0x4bb
   __TEXT.__ustring: 0x746
-  __TEXT.__unwind_info: 0x484
-  __TEXT.__objc_classname: 0x269
-  __TEXT.__objc_methname: 0x5e14
-  __TEXT.__objc_methtype: 0x10c9
-  __TEXT.__objc_stubs: 0x3620
-  __DATA_CONST.__got: 0x180
+  __TEXT.__unwind_info: 0x468
+  __TEXT.__objc_classname: 0x241
+  __TEXT.__objc_methname: 0x5cc6
+  __TEXT.__objc_methtype: 0x108c
+  __TEXT.__objc_stubs: 0x3520
+  __DATA_CONST.__got: 0x170
   __DATA_CONST.__const: 0xa10
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1d60
-  __DATA_CONST.__objc_selrefs: 0x1050
+  __DATA_CONST.__objc_const: 0x1bf8
+  __DATA_CONST.__objc_selrefs: 0xff8
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__cfstring: 0xac0
+  __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_got: 0x2e8
-  __DATA.__objc_classrefs: 0x268
+  __DATA.__objc_classrefs: 0x258
   __DATA.__objc_superrefs: 0x50
-  __DATA.__objc_ivar: 0xe8
-  __DATA.__data: 0x3d0
-  __DATA.__bss: 0x98
-  __DATA_DIRTY.__const: 0x1a0
+  __DATA.__objc_ivar: 0xdc
+  __DATA.__data: 0x370
+  __DATA.__bss: 0x88
+  __DATA_DIRTY.__const: 0x160
   __DATA_DIRTY.__objc_const: 0x780
   __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A6B4EC59-0CA1-3A95-92D2-B5059DD0B94F
-  Functions: 341
-  Symbols:   1683
-  CStrings:  1133
+  UUID: AA57DE83-9897-3D09-B9A4-97D8D36E706C
+  Functions: 329
+  Symbols:   1634
+  CStrings:  1112
 
Symbols:
+ -[WBUFeatureManager _primaryAppleAccountChanged]
+ GCC_except_table20
+ _OBJC_CLASS_$_WBSKeychainSyncingMonitor
+ _OBJC_CLASS_$_WBSPrimaryAppleAccountObserver
+ _OBJC_IVAR_$_WBUFeatureManager._primaryAppleAccount
+ _WBSPrimaryAppleAccountDidChangeNotification
+ ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke.192
+ ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_2.193
+ ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_3.195
+ ___48-[WBUFeatureManager _primaryAppleAccountChanged]_block_invoke
+ ___48-[WBUFeatureManager _primaryAppleAccountChanged]_block_invoke_2
+ ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke.255
+ ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke.267
+ ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke_2.272
+ ___block_descriptor_40_e8_32s_e19_v16?0"ACAccount"8ls32l8
+ ___block_literal_global.520
+ __unnamed_array_storage.224
+ __unnamed_array_storage.227
+ __unnamed_array_storage.230
+ __unnamed_array_storage.250
+ _objc_msgSend$_primaryAppleAccountChanged
+ _objc_msgSend$getPrimaryAppleAccountWithCompletionHandler:
+ _objc_msgSend$sharedMonitor
+ _objc_msgSend$sharedObserver
- -[WBUFeatureManager _setAccount:]
- -[WBUFeatureManager _updateKeychainSyncingStatus]
- -[WBUFeatureManager accountWasAdded:]
- -[WBUFeatureManager accountWasModified:]
- -[WBUFeatureManager accountWasRemoved:]
- -[WBUFeatureManager dealloc]
- -[WBUFeatureManager isKeychainSyncEnabled]
- -[WBUFeatureManager isKeychainSyncEnabled].cold.1
- GCC_except_table22
- GCC_except_table26
- _AAAccountClassPrimary
- _ACAccountTypeIdentifierAppleAccount
- _OBJC_CLASS_$_ACMonitoredAccountStore
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_OTClique
- _OBJC_CLASS_$_OTConfigurationContext
- _OBJC_IVAR_$_WBUFeatureManager._account
- _OBJC_IVAR_$_WBUFeatureManager._accountStore
- _OBJC_IVAR_$_WBUFeatureManager._keychainClique
- _OBJC_IVAR_$_WBUFeatureManager._primaryAccountAltDSID
- _OTDefaultContext
- _WBS_LOG_CHANNEL_PREFIXKeychain
- _WBS_LOG_CHANNEL_PREFIXKeychain.log
- _WBS_LOG_CHANNEL_PREFIXKeychain.onceToken
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ACMonitoredAccountStoreDelegateProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_ACMonitoredAccountStoreDelegateProtocol
- __OBJC_$_PROTOCOL_REFS_ACMonitoredAccountStoreDelegateProtocol
- __OBJC_CLASS_PROTOCOLS_$_WBUFeatureManager
- __OBJC_LABEL_PROTOCOL_$_ACMonitoredAccountStoreDelegateProtocol
- __OBJC_PROTOCOL_$_ACMonitoredAccountStoreDelegateProtocol
- ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke.191
- ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_2.192
- ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_3.194
- ___25-[WBUFeatureManager init]_block_invoke
- ___33-[WBUFeatureManager _setAccount:]_block_invoke
- ___42-[WBUFeatureManager isKeychainSyncEnabled]_block_invoke
- ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke.254
- ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke.266
- ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke_2.271
- ___WBS_LOG_CHANNEL_PREFIXKeychain_block_invoke
- ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
- ___block_literal_global.10
- ___block_literal_global.519
- __unnamed_array_storage.223
- __unnamed_array_storage.226
- __unnamed_array_storage.229
- __unnamed_array_storage.249
- _objc_msgSend$_setAccount:
- _objc_msgSend$_updateKeychainSyncingStatus
- _objc_msgSend$aa_altDSID
- _objc_msgSend$aa_isAccountClass:
- _objc_msgSend$aa_primaryAppleAccount
- _objc_msgSend$fetchUserControllableViewsSyncingEnabled:
- _objc_msgSend$initWithAccountTypes:delegate:
- _objc_msgSend$initWithContextData:
- _objc_msgSend$registerSynchronouslyWithError:
- _objc_msgSend$removeObserver:name:object:
- _objc_msgSend$setAltDSID:
- _objc_msgSend$setWithObject:
CStrings:
+ "\x05"
+ "_primaryAppleAccount"
+ "_primaryAppleAccountChanged"
+ "getPrimaryAppleAccountWithCompletionHandler:"
+ "sharedMonitor"
+ "sharedObserver"
+ "v16@?0@\"ACAccount\"8"
- "\b"
- "@\"ACMonitoredAccountStore\""
- "@\"OTClique\""
- "ACMonitoredAccountStoreDelegateProtocol"
- "Failed to read keychain sync status with error: %{public}@"
- "Keychain"
- "TB,R,N,GisKeychainSyncEnabled"
- "_account"
- "_accountStore"
- "_keychainClique"
- "_primaryAccountAltDSID"
- "_setAccount:"
- "_updateKeychainSyncingStatus"
- "aa_altDSID"
- "aa_isAccountClass:"
- "aa_primaryAppleAccount"
- "accountCredentialChanged:"
- "accountWasAdded:"
- "accountWasModified:"
- "accountWasRemoved:"
- "fetchUserControllableViewsSyncingEnabled:"
- "initWithAccountTypes:delegate:"
- "initWithContextData:"
- "registerSynchronouslyWithError:"
- "removeObserver:name:object:"
- "setAltDSID:"
- "setWithObject:"
- "v24@0:8@\"ACAccount\"16"

```
