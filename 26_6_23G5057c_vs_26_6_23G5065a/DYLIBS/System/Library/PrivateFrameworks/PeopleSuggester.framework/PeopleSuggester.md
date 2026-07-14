## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
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

-  __TEXT.__text: 0x1084f8
-  __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_methlist: 0xa224
+  __TEXT.__text: 0x108ff0
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_methlist: 0xa23c
   __TEXT.__const: 0x8d0
   __TEXT.__gcc_except_tab: 0x2f84
-  __TEXT.__cstring: 0xc245
-  __TEXT.__oslogstring: 0xcafe
+  __TEXT.__cstring: 0xc317
+  __TEXT.__oslogstring: 0xcbaf
   __TEXT.__dlopen_cstrs: 0x189d
   __TEXT.__ustring: 0x33e
   __TEXT.__unwind_info: 0x31c0
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x12b5
-  __TEXT.__objc_methname: 0x23018
+  __TEXT.__objc_methname: 0x230cf
   __TEXT.__objc_methtype: 0x283b
-  __TEXT.__objc_stubs: 0x13bc0
-  __DATA_CONST.__got: 0x9a8
+  __TEXT.__objc_stubs: 0x13c40
+  __DATA_CONST.__got: 0x9c0
   __DATA_CONST.__const: 0x3970
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68b0
+  __DATA_CONST.__objc_selrefs: 0x68d0
   __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0xd88
-  __AUTH_CONST.__auth_got: 0x7c0
+  __AUTH_CONST.__auth_got: 0x7c8
   __AUTH_CONST.__const: 0x1a80
-  __AUTH_CONST.__cfstring: 0xe7c0
+  __AUTH_CONST.__cfstring: 0xe980
   __AUTH_CONST.__objc_const: 0x144e8
   __AUTH_CONST.__objc_intobj: 0x1140
   __AUTH_CONST.__objc_arrayobj: 0x828

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4825
-  Symbols:   9793
-  CStrings:  8007
+  Functions: 4828
+  Symbols:   9803
+  CStrings:  8027
 
Symbols:
+ +[_PSAppUsageUtilities _attachmentsContainWebURL:]
+ +[_PSAppUsageUtilities _defaultBrowserAppBundleID]
+ +[_PSAppUsageUtilities boostAppsForSourceBundleId:attachments:mapping:traceId:parentSpanId:]
+ +[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:]
+ _UTTypeConformsTo
+ ___196+[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:]_block_invoke
+ _kUTTypeFileURL
+ _kUTTypePlainText
+ _kUTTypeURL
+ _objc_msgSend$URLOverrideForURL:
+ _objc_msgSend$_attachmentsContainWebURL:
+ _objc_msgSend$_defaultBrowserAppBundleID
+ _objc_msgSend$applicationsAvailableForOpeningURL:
+ _objc_msgSend$boostAppsForSourceBundleId:attachments:mapping:traceId:parentSpanId:
+ _objc_msgSend$mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:
- +[_PSAppUsageUtilities boostAppsForSourceBundleId:]
- +[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:]
- ___163+[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:]_block_invoke
- _objc_msgSend$boostAppsForSourceBundleId:
- _objc_msgSend$mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:
CStrings:
+ "(nil)"
+ "(none)"
+ "Default browser lookup returned nil; LSApplicationWorkspace did not surface a handler for https URL"
+ "Default-browser boost: %{public}@ (browser %{public}@) for source %{public}@"
+ "URLOverrideForURL:"
+ "_attachmentsContainWebURL:"
+ "_defaultBrowserAppBundleID"
+ "applicationsAvailableForOpeningURL:"
+ "attachmentSchemes"
+ "attachmentTexts"
+ "attachmentUTIs"
+ "boostAppsForSourceBundleId:attachments:mapping:traceId:parentSpanId:"
+ "boostFired"
+ "boostedExtensionCount"
+ "boostedExtensions"
+ "com.apple"
+ "defaultBrowser"
+ "defaultBrowserBoostEnd2End"
+ "hasWebURL"
+ "https://www.apple.com"
+ "isThirdParty"
+ "mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:attachments:traceId:parentSpanId:sharesFromSourceToTargetBundle:appUsageDurations:"
- "boostAppsForSourceBundleId:"
- "mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:"
```
