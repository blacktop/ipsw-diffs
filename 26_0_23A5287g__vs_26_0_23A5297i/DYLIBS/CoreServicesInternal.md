## CoreServicesInternal

> `/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal`

```diff

-576.0.0.0.0
-  __TEXT.__text: 0x2db50
+578.0.0.0.0
+  __TEXT.__text: 0x2dcd0
   __TEXT.__auth_stubs: 0x1480
-  __TEXT.__delay_stubs: 0x160
-  __TEXT.__delay_helper: 0x3b0
-  __TEXT.__cstring: 0x1b91
+  __TEXT.__delay_stubs: 0x1b8
+  __TEXT.__delay_helper: 0x49c
+  __TEXT.__cstring: 0x1c37
   __TEXT.__const: 0x5e0
   __TEXT.__oslogstring: 0x2009
   __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__got: 0x728
+  __DATA_CONST.__got: 0x740
   __DATA_CONST.__const: 0x288
-  __AUTH_CONST.__auth_got: 0xa80
+  __AUTH_CONST.__auth_got: 0xa90
   __AUTH_CONST.__const: 0x328
-  __AUTH_CONST.__cfstring: 0x1020
-  __DATA.__data: 0x94
-  __DATA.__bss: 0x4a
+  __AUTH_CONST.__cfstring: 0x1080
+  __DATA.__data: 0x98
+  __DATA.__bss: 0x100a
   __DATA_DIRTY.__data: 0x250
-  __DATA_DIRTY.__bss: 0x1e78
+  __DATA_DIRTY.__bss: 0xf80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
+  - /System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 7EC5A83F-A572-3AB6-A3C4-2436D0FCE462
-  Functions: 612
-  Symbols:   1865
-  CStrings:  597
+  UUID: 92EDBE0B-9A0B-337F-9DBC-A4E3600474B2
+  Functions: 616
+  Symbols:   1882
+  CStrings:  604
 
Symbols:
+ _FPCreateBookmarkableStringFromDocumentURLWithOptions
+ _FPCreateBookmarkableStringFromDocumentURLWithOptions$delayInitStub
+ __DS_CFURLGetPropertyForKey
+ __DS_CFURLGetPropertyForKey$delayInitStub
+ __DS_CFURLSetPropertyForKey
+ __DS_CFURLSetPropertyForKey$delayInitStub
+ __MergedGlobals.59
+ __ZL22GetFromDesktopServicesPK7__CFURLPKvPS3_PP9__CFError
+ __ZL22SetWithDesktopServicesPK7__CFURLPK10__CFStringPKvPP9__CFError
+ ___block_descriptor_tmp.23
+ ___block_literal_global.25
+ _dlopenHelper$DesktopServicesPriv
+ _dlopenHelperFlag$DesktopServicesPriv
+ _gotLoadHelper_x8$__DS_CFURLGetPropertyForKey
+ _gotLoadHelper_x8$__DS_CFURLSetPropertyForKey
+ _gotLoadHelper_x9$_FPCreateBookmarkableStringFromDocumentURLWithOptions
+ _kCFURLDirectoryEntryCountKey
+ _registerExternalProviderProperties.cold.3
- _FPCreateBookmarkableStringFromDocumentURL
- _FPCreateBookmarkableStringFromDocumentURL$delayInitStub
- __MergedGlobals.62
- ___block_descriptor_tmp.26
- ___block_literal_global.28
- _gotLoadHelper_x9$_FPCreateBookmarkableStringFromDocumentURL
CStrings:
+ "/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv"
+ "__kCFURLDirectoryHasVisibleContentKey"
+ "__kCFURLIconEmojiKey"
+ "__kCFURLIconSymbolNameKey"
+ "__kCFURLTagColorIndexKey"
- "NSURLDirectoryEntryCountKey"

```
