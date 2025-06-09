## MessageLegacy

> `/System/Library/PrivateFrameworks/MessageLegacy.framework/MessageLegacy`

```diff

-22.0.0.0.0
-  __TEXT.__text: 0x64d10
-  __TEXT.__auth_stubs: 0x1b60
+24.0.0.0.0
+  __TEXT.__text: 0x64e74
+  __TEXT.__auth_stubs: 0x1b30
   __TEXT.__objc_methlist: 0x8c64
   __TEXT.__const: 0x2a0
-  __TEXT.__gcc_except_tab: 0x788
-  __TEXT.__cstring: 0x6d57
+  __TEXT.__gcc_except_tab: 0x7ac
+  __TEXT.__cstring: 0x6c86
   __TEXT.__oslogstring: 0x32eb
   __TEXT.__ustring: 0x1cba
-  __TEXT.__unwind_info: 0x20b0
+  __TEXT.__dlopen_cstrs: 0x4e
+  __TEXT.__unwind_info: 0x2070
   __TEXT.__objc_classname: 0xbda
   __TEXT.__objc_methname: 0x13f52
   __TEXT.__objc_methtype: 0x21e1
   __TEXT.__objc_stubs: 0xf600
-  __DATA_CONST.__got: 0xbd8
-  __DATA_CONST.__const: 0x1bb8
+  __DATA_CONST.__got: 0xbe8
+  __DATA_CONST.__const: 0x1bf8
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x56f8
   __DATA_CONST.__objc_superrefs: 0x300
-  __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0xdc0
-  __AUTH_CONST.__const: 0x690
-  __AUTH_CONST.__cfstring: 0x92a0
+  __DATA_CONST.__objc_arraydata: 0x60
+  __AUTH_CONST.__auth_got: 0xda8
+  __AUTH_CONST.__const: 0x610
+  __AUTH_CONST.__cfstring: 0x9260
   __AUTH_CONST.__objc_const: 0xee00
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0x1450
-  __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x8dc
   __DATA.__data: 0x6d8
-  __DATA.__bss: 0x22c
+  __DATA.__bss: 0x1f4
   __DATA_DIRTY.__objc_data: 0xe10
-  __DATA_DIRTY.__data: 0x68
-  __DATA_DIRTY.__bss: 0x188
+  __DATA_DIRTY.__data: 0x58
+  __DATA_DIRTY.__bss: 0x178
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 02419FF6-D6AB-3E19-9469-9680872C62F0
-  Functions: 3268
-  Symbols:   11380
-  CStrings:  6796
+  UUID: 7EA6E7E0-6A3B-3F63-B4E8-08DD41334D4B
+  Functions: 3260
+  Symbols:   11350
+  CStrings:  6792
 
Symbols:
+ +[MFPowerController powerlog:eventData:].cold.1
+ +[MFPowerController powerlog:eventData:].cold.2
+ _CSAccountTypeLocal
+ _CSAccountTypeUnknown
+ _PowerLogLibrary
+ _PowerLogLibrary.cold.1
+ _PowerLogLibraryCore.frameworkLibrary
+ ___PowerLogLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___getPLLogRegisteredEventSymbolLoc_block_invoke
+ ___getPLShouldLogRegisteredEventSymbolLoc_block_invoke
+ __sl_dlopen
+ _audit_stringPowerLog
+ _getPLLogRegisteredEventSymbolLoc.ptr
+ _getPLShouldLogRegisteredEventSymbolLoc.ptr
- _CFMakeCollectable
- _CSAccountTypeLocalFunction
- _CSAccountTypeUnknownFunction
- _LoadCoreSpotlight.frameworkLibrary
- _LoadCoreSpotlight.loadPredicate
- _LoadPowerLog.frameworkLibrary
- _LoadPowerLog.loadPredicate
- _MFHasAccountsEntitlement
- _MFHasAccountsEntitlement.__hasAccountsEntitlement
- _MFHasAccountsEntitlement.cold.1
- _MFHasAccountsEntitlement.once
- _NSLog
- _SecTaskCopyValuesForEntitlements
- _SecTaskCreateFromSelf
- ___LoadCoreSpotlight_block_invoke
- ___LoadPowerLog_block_invoke
- ___MFHasAccountsEntitlement_block_invoke
- ___block_literal_global.209
- ___block_literal_global.769
- _constantCSAccountTypeLocal
- _constantCSAccountTypeUnknown
- _getCSAccountTypeLocal
- _getCSAccountTypeUnknown
- _initCSAccountTypeLocal
- _initCSAccountTypeLocal.cold.1
- _initCSAccountTypeUnknown
- _initCSAccountTypeUnknown.cold.1
- _initPLLogRegisteredEvent
- _initPLLogRegisteredEvent.cold.1
- _initPLShouldLogRegisteredEvent
- _initPLShouldLogRegisteredEvent.cold.1
- _softLinkPLLogRegisteredEvent
- _softLinkPLShouldLogRegisteredEvent
CStrings:
+ "%s"
+ "BOOL soft_PLShouldLogRegisteredEvent(PLClientID, CFStringRef)"
+ "softlink:r:path:/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog"
+ "void *PowerLogLibrary(void)"
+ "void soft_PLLogRegisteredEvent(PLClientID, CFStringRef, CFDictionaryRef, CFArrayRef)"
- "### Failed to Soft Linked: /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight"
- "### Failed to Soft Linked: /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog"
- "/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight"
- "/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog"
- "CSAccountTypeLocal"
- "CSAccountTypeUnknown"
- "com.apple.private.accounts.allaccounts"

```
