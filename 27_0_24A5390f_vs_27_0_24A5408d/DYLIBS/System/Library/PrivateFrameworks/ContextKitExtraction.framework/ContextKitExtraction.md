## ContextKitExtraction

> `/System/Library/PrivateFrameworks/ContextKitExtraction.framework/ContextKitExtraction`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

   __TEXT.__gcc_except_tab: 0x270
   __TEXT.__oslogstring: 0x653
   __TEXT.__dlopen_cstrs: 0x11b
-  __TEXT.__unwind_info: 0x3e8
+  __TEXT.__unwind_info: 0x3e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
Functions:
~ -[CKContextContentProviderUIScene _setScene:] -> +[CKContextContentProviderManager isSpringBoard] : 20 -> 12
~ -[CKContextContentProviderManager userActivityWasCreated:] -> -[CKContextContentProviderUIScene _setScene:] : 180 -> 20
~ +[CKContextContentProviderManager isSpringBoard] -> -[CKContextContentProviderManager userActivityWasCreated:] : 12 -> 180
~ -[CKContextContentProviderManager scheduleUserActivityRecordingWithUserActivity:] -> -[CKContextContentProviderManager _hasForegroundActiveContentWithReply:] : 480 -> 204
~ -[CKContextContentProviderManager _isActivityReportingAllowedForCurrentBundleIdentifier:] -> -[CKContextContentProviderUIScene _scene] : 264 -> 52
~ -[CKContextContentProviderManager _loadContextKitIfNecessaryWithExecutor:] -> -[CKContextContentProviderManager scheduleUserActivityRecordingWithUserActivity:] : 192 -> 480
~ -[CKContextContentProviderManager _queueActivityForReporting:] -> -[CKContextContentProviderManager _isActivityReportingAllowedForCurrentBundleIdentifier:] : 148 -> 264
~ -[CKContextContentProviderUIScene _scene] -> -[CKContextContentProviderManager _loadContextKitIfNecessaryWithExecutor:] : 52 -> 192
~ -[CKContextContentProviderManager _prepareDonationWithNonce:options:isRecentsCapture:requiringMainQueue:andReply:] -> -[CKContextContentProviderManager _queueActivityForReporting:] : 264 -> 148
~ -[CKContextContentProviderManager _hasForegroundActiveContentWithReply:] -> -[CKContextContentProviderManager _prepareDonationWithNonce:options:isRecentsCapture:requiringMainQueue:andReply:] : 204 -> 264
```
