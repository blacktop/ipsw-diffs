## SafariServices

> `/System/Library/Frameworks/SafariServices.framework/SafariServices`

```diff

-625.2.7.1.0
-  __TEXT.__text: 0x17a94c
-  __TEXT.__objc_methlist: 0x1bdf4
+625.2.8.10.4
+  __TEXT.__text: 0x17ae5c
+  __TEXT.__objc_methlist: 0x1be24
   __TEXT.__const: 0x2ec4
-  __TEXT.__cstring: 0xd690
-  __TEXT.__gcc_except_tab: 0xfe60
+  __TEXT.__cstring: 0xd720
+  __TEXT.__gcc_except_tab: 0xfef4
   __TEXT.__dlopen_cstrs: 0xb7f
-  __TEXT.__oslogstring: 0x83a7
+  __TEXT.__oslogstring: 0x83f7
   __TEXT.__ustring: 0x3774
   __TEXT.__swift5_typeref: 0x6b0
   __TEXT.__swift5_capture: 0x49c

   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x7c
   __TEXT.__swift_as_cont: 0xfc
-  __TEXT.__unwind_info: 0xa640
+  __TEXT.__unwind_info: 0xa660
   __TEXT.__eh_frame: 0x1208
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x8e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x123e0
+  __DATA_CONST.__objc_selrefs: 0x12418
   __DATA_CONST.__objc_protorefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x858
   __DATA_CONST.__objc_arraydata: 0x5a8
-  __DATA_CONST.__got: 0x2728
+  __DATA_CONST.__got: 0x2740
   __AUTH_CONST.__const: 0x2270
-  __AUTH_CONST.__cfstring: 0xc640
-  __AUTH_CONST.__objc_const: 0x2c720
+  __AUTH_CONST.__cfstring: 0xc700
+  __AUTH_CONST.__objc_const: 0x2c748
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0xca8
   __AUTH_CONST.__objc_arrayobj: 0x4f8
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__auth_got: 0x14a8
+  __AUTH_CONST.__auth_got: 0x14b8
   __AUTH.__objc_data: 0x5ec0
   __AUTH.__data: 0x2b0
   __DATA.__objc_ivar: 0x1f34

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/Frameworks/WebKit.framework/WebKit
+  - /System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI
   - /System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9315
-  Symbols:   17552
-  CStrings:  2574
+  Functions: 9321
+  Symbols:   17560
+  CStrings:  2581
 
Symbols:
+ +[SFContentBlockerManager(SFPrivate) compiledBytecodeForEnabledContentBlockersInDefaultProfile]
+ +[_SFSearchEngineController postRemoteAppIntentsNotificationForSearchEngineChange]
+ -[_SFSearchEngineController defaultSearchEnginePlist]
+ _OBJC_CLASS_$_SFContentBlockerManagerProxy
+ _OBJC_CLASS_$_SFSearchEngineControllerWrapper
+ _OBJC_CLASS_$_WBSPair
+ __SFContentBlockerStateURL
+ __ZL49postContentBlockerExtensionsDidChangeNotificationv
CStrings:
+ "BrowserChoiceConfirmButton"
+ "BrowserChoiceListCell-"
+ "BrowserChoiceShowMoreButton"
+ "ChooseCurrentDefaultButton"
+ "ContentRuleList-%@"
+ "SetUpLaterButton"
+ "Unable to seralize search engine dictionary representation into a plist: %{public}@"
```
