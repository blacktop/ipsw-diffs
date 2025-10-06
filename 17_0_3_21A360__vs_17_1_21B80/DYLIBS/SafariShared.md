## SafariShared

> `/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared`

```diff

-616.1.27.10.16
-  __TEXT.__text: 0x1621f8
+616.2.9.10.10
+  __TEXT.__text: 0x16157c
   __TEXT.__auth_stubs: 0x1b20
-  __TEXT.__objc_methlist: 0xeea0
-  __TEXT.__gcc_except_tab: 0x1908c
-  __TEXT.__cstring: 0x18e6f
-  __TEXT.__const: 0x54ca8
-  __TEXT.__oslogstring: 0xebc3
+  __TEXT.__objc_methlist: 0xee10
+  __TEXT.__gcc_except_tab: 0x19088
+  __TEXT.__cstring: 0x18d7e
+  __TEXT.__const: 0x54cc8
+  __TEXT.__oslogstring: 0xeb21
   __TEXT.__ustring: 0xd9be
-  __TEXT.__dlopen_cstrs: 0x25f
-  __TEXT.__unwind_info: 0xa3cc
+  __TEXT.__dlopen_cstrs: 0x209
+  __TEXT.__unwind_info: 0xa388
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x2d12
-  __TEXT.__objc_methname: 0x2e08c
-  __TEXT.__objc_methtype: 0xb76d
-  __TEXT.__objc_stubs: 0x19340
+  __TEXT.__objc_classname: 0x2ccb
+  __TEXT.__objc_methname: 0x2dec8
+  __TEXT.__objc_methtype: 0xb741
+  __TEXT.__objc_stubs: 0x192a0
   __DATA_CONST.__got: 0x4b0
-  __DATA_CONST.__const: 0x134c8
-  __DATA_CONST.__objc_classlist: 0x9f0
+  __DATA_CONST.__const: 0x134a8
+  __DATA_CONST.__objc_classlist: 0x9e8
   __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x220
+  __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x17cc0
-  __DATA_CONST.__objc_selrefs: 0x89c8
+  __DATA_CONST.__objc_const: 0x17b20
+  __DATA_CONST.__objc_selrefs: 0x8978
   __DATA_CONST.__objc_arraydata: 0x2d20
-  __AUTH_CONST.__const: 0x2880
-  __AUTH_CONST.__objc_const: 0x7c18
-  __AUTH_CONST.__cfstring: 0x1d880
+  __AUTH_CONST.__const: 0x2860
+  __AUTH_CONST.__objc_const: 0x7b88
+  __AUTH_CONST.__cfstring: 0x1d800
   __AUTH_CONST.__objc_arrayobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_doubleobj: 0xa0

   __AUTH_CONST.__auth_got: 0xda8
   __AUTH.__objc_data: 0x3200
   __DATA.__objc_protorefs: 0x80
-  __DATA.__objc_classrefs: 0xbe0
-  __DATA.__objc_superrefs: 0x7f8
-  __DATA.__objc_ivar: 0x128c
-  __DATA.__data: 0x2c80
-  __DATA.__bss: 0x738
+  __DATA.__objc_classrefs: 0xbd0
+  __DATA.__objc_superrefs: 0x7f0
+  __DATA.__objc_ivar: 0x127c
+  __DATA.__data: 0x2c20
+  __DATA.__bss: 0x730
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x3160
+  __DATA_DIRTY.__objc_data: 0x3110
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x600
+  __DATA_DIRTY.__bss: 0x5e8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 4478CA14-B0FE-386C-BF8B-2BE609D3B5AD
-  Functions: 8459
-  Symbols:   28961
-  CStrings:  16299
+  UUID: 18A613E1-71BA-3CDB-A0F8-D44895B6209D
+  Functions: 8435
+  Symbols:   28881
+  CStrings:  16265
 
Symbols:
+ +[NSString(SafariSharedExtras) safari_detailStringWithTitleString:prompt:]
+ +[WBSURLCompletionDatabase _shouldPreloadTopHit:forTypedString:withSearchParameters:]
+ -[WBSEncryptedCloudKeyValueStore prewarm]
+ ___85+[WBSURLCompletionDatabase _shouldPreloadTopHit:forTypedString:withSearchParameters:]_block_invoke
+ ___block_descriptor_56_ea8_32s40s_e5_B8?0ls32l8s40l8
+ _objc_msgSend$_shouldPreloadTopHit:forTypedString:withSearchParameters:
- +[NSString(SafariSharedExtras) safari_localizedStringFromComponents:usingConjunctionForFinalJoiner:]
- +[WBSPrimaryAppleAccountObserver sharedObserver]
- -[WBSPrimaryAppleAccountObserver .cxx_destruct]
- -[WBSPrimaryAppleAccountObserver _registerForUpdates]
- -[WBSPrimaryAppleAccountObserver _registerForUpdates].cold.1
- -[WBSPrimaryAppleAccountObserver _setAccountIfPrimary:]
- -[WBSPrimaryAppleAccountObserver _setAccountOnInternalQueue:]
- -[WBSPrimaryAppleAccountObserver accountWasAdded:]
- -[WBSPrimaryAppleAccountObserver accountWasModified:]
- -[WBSPrimaryAppleAccountObserver accountWasRemoved:]
- -[WBSPrimaryAppleAccountObserver getPrimaryAppleAccountAltDSIDWithCompletionHandler:]
- -[WBSPrimaryAppleAccountObserver getPrimaryAppleAccountHasSafariSyncEnabledWithCompletionHandler:]
- -[WBSPrimaryAppleAccountObserver getPrimaryAppleAccountWithCompletionHandler:]
- -[WBSPrimaryAppleAccountObserver init]
- _AppleAccountLibraryCore
- _AppleAccountLibraryCore.frameworkLibrary
- _OBJC_CLASS_$_ACMonitoredAccountStore
- _OBJC_CLASS_$_WBSPrimaryAppleAccountObserver
- _OBJC_IVAR_$_WBSPrimaryAppleAccountObserver._accountStore
- _OBJC_IVAR_$_WBSPrimaryAppleAccountObserver._primaryAccountAltDSID
- _OBJC_IVAR_$_WBSPrimaryAppleAccountObserver._primaryAppleAccount
- _OBJC_IVAR_$_WBSPrimaryAppleAccountObserver._queue
- _OBJC_METACLASS_$_WBSPrimaryAppleAccountObserver
- _WBSPrimaryAppleAccountDidChangeNotification
- __OBJC_$_CLASS_METHODS_WBSPrimaryAppleAccountObserver
- __OBJC_$_CLASS_PROP_LIST_WBSPrimaryAppleAccountObserver
- __OBJC_$_INSTANCE_METHODS_WBSPrimaryAppleAccountObserver
- __OBJC_$_INSTANCE_VARIABLES_WBSPrimaryAppleAccountObserver
- __OBJC_$_PROP_LIST_WBSPrimaryAppleAccountObserver
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ACMonitoredAccountStoreDelegateProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_ACMonitoredAccountStoreDelegateProtocol
- __OBJC_$_PROTOCOL_REFS_ACMonitoredAccountStoreDelegateProtocol
- __OBJC_CLASS_PROTOCOLS_$_WBSPrimaryAppleAccountObserver
- __OBJC_CLASS_RO_$_WBSPrimaryAppleAccountObserver
- __OBJC_LABEL_PROTOCOL_$_ACMonitoredAccountStoreDelegateProtocol
- __OBJC_METACLASS_RO_$_WBSPrimaryAppleAccountObserver
- __OBJC_PROTOCOL_$_ACMonitoredAccountStoreDelegateProtocol
- ___100+[NSString(SafariSharedExtras) safari_localizedStringFromComponents:usingConjunctionForFinalJoiner:]_block_invoke
- ___38-[WBSPrimaryAppleAccountObserver init]_block_invoke
- ___48+[WBSPrimaryAppleAccountObserver sharedObserver]_block_invoke
- ___52-[WBSPrimaryAppleAccountObserver accountWasRemoved:]_block_invoke
- ___55-[WBSPrimaryAppleAccountObserver _setAccountIfPrimary:]_block_invoke
- ___78-[WBSPrimaryAppleAccountObserver getPrimaryAppleAccountWithCompletionHandler:]_block_invoke
- ___85-[WBSPrimaryAppleAccountObserver getPrimaryAppleAccountAltDSIDWithCompletionHandler:]_block_invoke
- ___98-[WBSPrimaryAppleAccountObserver getPrimaryAppleAccountHasSafariSyncEnabledWithCompletionHandler:]_block_invoke
- ___AppleAccountLibraryCore_block_invoke
- ___block_descriptor_64_ea8_32s40s48s56r_e25_v32?0"NSString"8Q16^B24lr56l8s32l8s40l8s48l8
- ___getAAAccountClassPrimarySymbolLoc_block_invoke
- ___getAAAccountClassPrimarySymbolLoc_block_invoke.cold.1
- _audit_stringAppleAccount
- _getAAAccountClassPrimary
- _getAAAccountClassPrimary.cold.1
- _getAAAccountClassPrimarySymbolLoc.ptr
- _objc_msgSend$_registerForUpdates
- _objc_msgSend$_setAccountIfPrimary:
- _objc_msgSend$_setAccountOnInternalQueue:
- _objc_msgSend$aa_isAccountClass:
- _objc_msgSend$initWithAccountTypes:delegate:
- _objc_msgSend$registerSynchronouslyWithError:
- _sharedObserver.onceToken
- _sharedObserver.sharedObserver
CStrings:
+ "%@ %@"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__hash_table"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/deque"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/vector"
+ "B40@0:8^v16@24@32"
+ "_shouldPreloadTopHit:forTypedString:withSearchParameters:"
+ "prewarm"
+ "safari_detailStringWithTitleString:prompt:"
- "%@ %@ %@"
- "%@%@ %@"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__hash_table"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/deque"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/vector"
- "@\"ACAccount\""
- "@\"ACMonitoredAccountStore\""
- "AAAccountClassPrimary"
- "ACMonitoredAccountStoreDelegateProtocol"
- "Failed to register for account updates: %{public}@"
- "NSString *getAAAccountClassPrimary(void)"
- "Running in an environment where AppleAccount framework is not available. Refusing to connect to account store."
- "T@\"WBSPrimaryAppleAccountObserver\",R,N"
- "WBSPrimaryAppleAccountDidChangeNotification"
- "WBSPrimaryAppleAccountObserver"
- "WBSPrimaryAppleAccountObserver.m"
- "_accountStore"
- "_primaryAccountAltDSID"
- "_primaryAppleAccount"
- "_registerForUpdates"
- "_setAccountIfPrimary:"
- "_setAccountOnInternalQueue:"
- "aa_isAccountClass:"
- "accountCredentialChanged:"
- "accountWasAdded:"
- "accountWasModified:"
- "accountWasRemoved:"
- "and"
- "com.apple.SafariShared.WBSPrimaryAppleAccountObserver"
- "getPrimaryAppleAccountAltDSIDWithCompletionHandler:"
- "getPrimaryAppleAccountHasSafariSyncEnabledWithCompletionHandler:"
- "getPrimaryAppleAccountWithCompletionHandler:"
- "initWithAccountTypes:delegate:"
- "registerSynchronouslyWithError:"
- "safari_localizedStringFromComponents:usingConjunctionForFinalJoiner:"
- "softlink:o:path:/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount"
- "v24@0:8@\"ACAccount\"16"
- "void *AppleAccountLibrary(void)"

```
