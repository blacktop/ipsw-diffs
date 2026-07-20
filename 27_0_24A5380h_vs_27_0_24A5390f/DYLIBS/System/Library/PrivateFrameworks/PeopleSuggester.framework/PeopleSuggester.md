## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1962.0.1.0.0
-  __TEXT.__text: 0x127f88
-  __TEXT.__objc_methlist: 0xaeb4
+1967.0.0.0.0
+  __TEXT.__text: 0x128e34
+  __TEXT.__objc_methlist: 0xaed4
   __TEXT.__const: 0x988
   __TEXT.__gcc_except_tab: 0x49d8
-  __TEXT.__cstring: 0x31473
-  __TEXT.__oslogstring: 0x11218
+  __TEXT.__cstring: 0x315b4
+  __TEXT.__oslogstring: 0x11318
   __TEXT.__dlopen_cstrs: 0x19c8
   __TEXT.__ustring: 0xb22
-  __TEXT.__unwind_info: 0x35b8
+  __TEXT.__unwind_info: 0x35c8
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7110
+  __DATA_CONST.__objc_selrefs: 0x7148
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x39e80
-  __DATA_CONST.__got: 0xa30
+  __DATA_CONST.__got: 0xa50
   __AUTH_CONST.__const: 0x1cc0
-  __AUTH_CONST.__cfstring: 0x7f960
+  __AUTH_CONST.__cfstring: 0x7fc20
   __AUTH_CONST.__objc_const: 0x15978
   __AUTH_CONST.__objc_intobj: 0x11d0
   __AUTH_CONST.__objc_arrayobj: 0x11d60
   __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH_CONST.__objc_dictobj: 0x22858
-  __AUTH_CONST.__auth_got: 0x818
+  __AUTH_CONST.__auth_got: 0x820
   __AUTH.__objc_data: 0x1db0
   __DATA.__objc_ivar: 0xf34
   __DATA.__data: 0x4f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5357
-  Symbols:   10759
-  CStrings:  17914
+  Functions: 5363
+  Symbols:   10774
+  CStrings:  17939
 
Symbols:
+ +[_PSAppUsageUtilities _attachmentsContainWebURL:]
+ +[_PSAppUsageUtilities _defaultBrowserAppBundleID]
+ +[_PSAppUsageUtilities boostAppsForSourceBundleId:attachments:mapping:traceId:parentSpanId:]
+ +[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:]
+ -[_PSContactCatalog _attemptLoadContactCatalogCapturingAttributes:]
+ _NSFileSize
+ _UTTypeConformsTo
+ ___196+[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:]_block_invoke
+ _kUTTypeFileURL
+ _kUTTypePlainText
+ _kUTTypeURL
+ _objc_msgSend$URLOverrideForURL:
+ _objc_msgSend$_attachmentsContainWebURL:
+ _objc_msgSend$_attemptLoadContactCatalogCapturingAttributes:
+ _objc_msgSend$_defaultBrowserAppBundleID
+ _objc_msgSend$applicationsAvailableForOpeningURL:
+ _objc_msgSend$boostAppsForSourceBundleId:attachments:mapping:traceId:parentSpanId:
+ _objc_msgSend$mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$unsignedLongLongValue
- +[_PSAppUsageUtilities boostAppsForSourceBundleId:]
- +[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:]
- ___163+[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:]_block_invoke
- _objc_msgSend$boostAppsForSourceBundleId:
- _objc_msgSend$mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:
CStrings:
+ "(none)"
+ "Contact catalog root is not a dictionary; got %{public}@ (fileSize=%llu bytes)"
+ "Default browser lookup returned nil; LSApplicationWorkspace did not surface a handler for https URL"
+ "Default-browser boost: %{public}@ (browser %{public}@) for source %{public}@"
+ "attachmentSchemes"
+ "attachmentTexts"
+ "attachmentUTIs"
+ "boostFired"
+ "boostedExtensionCount"
+ "boostedExtensions"
+ "com.apple"
+ "defaultBrowser"
+ "defaultBrowserBoostEnd2End"
+ "fileNotFound"
+ "fileSizeBytes"
+ "hasWebURL"
+ "https://www.apple.com"
+ "isThirdParty"
+ "loadContactCatalog"
+ "nonDictionary"
+ "outcome"
+ "parseFailed"
+ "readFailed"
+ "rootClass"
+ "versionMismatch"
```
