## MailSupport

> `/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport`

```diff

-3864.100.1.2.9
-  __TEXT.__text: 0x18be0
-  __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_methlist: 0x17d8
-  __TEXT.__gcc_except_tab: 0x2618
+3864.200.33.2.2
+  __TEXT.__text: 0x18e84
+  __TEXT.__auth_stubs: 0xb10
+  __TEXT.__objc_methlist: 0x17f0
+  __TEXT.__gcc_except_tab: 0x26b4
   __TEXT.__cstring: 0x481e
-  __TEXT.__const: 0x39c
+  __TEXT.__const: 0x37c
   __TEXT.__oslogstring: 0x4a6
   __TEXT.__dlopen_cstrs: 0xd4
   __TEXT.__ustring: 0x18
   __TEXT.__swift5_typeref: 0x242
   __TEXT.__constg_swiftt: 0x60
-  __TEXT.__swift5_reflstr: 0xf2
-  __TEXT.__swift5_fieldmd: 0xc8
+  __TEXT.__swift5_reflstr: 0xb2
+  __TEXT.__swift5_fieldmd: 0x8c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_capture: 0x48
   __TEXT.__unwind_info: 0xd50
-  __TEXT.__objc_classname: 0x62c
-  __TEXT.__objc_methname: 0x5467
-  __TEXT.__objc_methtype: 0x851
-  __TEXT.__objc_stubs: 0x3760
-  __DATA_CONST.__got: 0x4b0
-  __DATA_CONST.__const: 0x1290
-  __DATA_CONST.__objc_classlist: 0x198
+  __TEXT.__objc_classname: 0x650
+  __TEXT.__objc_methname: 0x5583
+  __TEXT.__objc_methtype: 0x865
+  __TEXT.__objc_stubs: 0x3880
+  __DATA_CONST.__got: 0x4c0
+  __DATA_CONST.__const: 0x1288
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1400
+  __DATA_CONST.__objc_selrefs: 0x1450
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x590
+  __AUTH_CONST.__auth_got: 0x598
   __AUTH_CONST.__const: 0x4d0
   __AUTH_CONST.__cfstring: 0x4520
-  __AUTH_CONST.__objc_const: 0x3f50
+  __AUTH_CONST.__objc_const: 0x3fe0
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x180
+  __AUTH.__objc_data: 0x1d0
   __DATA.__objc_ivar: 0x1a4
   __DATA.__data: 0x610
   __DATA.__bss: 0x468

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
+  - /System/Library/Frameworks/WebKit.framework/WebKit
   - /System/Library/PrivateFrameworks/Email.framework/Email
   - /System/Library/PrivateFrameworks/EmailCore.framework/EmailCore
   - /System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E09D2E8C-4C53-3119-83EA-DD4B3D794048
+  UUID: D181D742-97EB-36AD-9956-8DAADE535223
   Functions: 655
-  Symbols:   3012
-  CStrings:  2278
+  Symbols:   3030
+  CStrings:  2287
 
Symbols:
+ +[MSWebKitWebViewConfigurationFactory commonWebViewConfiguration]
+ -[MSParsecSearchSession reportMessageListResultsFetched:topHitResults:instantAnswerResult:isFinished:]
+ -[MSParsecSearchSession reportMessageResultEngaged:engagementAction:]
+ -[MSParsecSearchSession reportMessageResultsVisible:]
+ _OBJC_CLASS_$_MSWebKitWebViewConfigurationFactory
+ _OBJC_CLASS_$_WKWebViewConfiguration
+ _OBJC_CLASS_$_WKWebsiteDataStore
+ _OBJC_METACLASS_$_MSWebKitWebViewConfigurationFactory
+ __OBJC_$_CLASS_METHODS_MSWebKitWebViewConfigurationFactory
+ __OBJC_CLASS_RO_$_MSWebKitWebViewConfigurationFactory
+ __OBJC_METACLASS_RO_$_MSWebKitWebViewConfigurationFactory
+ __os_feature_enabled_impl
+ _objc_msgSend$_disableMediaPlaybackRelatedFeatures
+ _objc_msgSend$_disableRichJavaScriptFeatures
+ _objc_msgSend$_setAllowedNetworkHosts:
+ _objc_msgSend$_setAllowsJavaScriptMarkup:
+ _objc_msgSend$defaultWebpagePreferences
+ _objc_msgSend$nonPersistentDataStore
+ _objc_msgSend$preferences
+ _objc_msgSend$setAllowsContentJavaScript:
+ _objc_msgSend$setWebsiteDataStore:
- -[MSParsecSearchSession reportMessageListResultEngaged:engagementAction:]
- -[MSParsecSearchSession reportMessageListResultsFetched:isFinished:]
- -[MSParsecSearchSession reportMessageListResultsVisible:]
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_MailSupport
CStrings:
+ "MSWebKitWebViewConfigurationFactory"
+ "MinWebKitAdoptionMediaPlayback"
+ "MinWebKitAdoptionRichJS"
+ "_disableMediaPlaybackRelatedFeatures"
+ "_disableRichJavaScriptFeatures"
+ "_setAllowedNetworkHosts:"
+ "_setAllowsJavaScriptMarkup:"
+ "commonWebViewConfiguration"
+ "defaultWebpagePreferences"
+ "nonPersistentDataStore"
+ "preferences"
+ "reportMessageListResultsFetched:topHitResults:instantAnswerResult:isFinished:"
+ "reportMessageResultEngaged:engagementAction:"
+ "reportMessageResultsVisible:"
+ "setAllowsContentJavaScript:"
+ "setWebsiteDataStore:"
+ "v44@0:8@16@24@32B40"
- "FollowUp"
- "MessageSearch"
- "RemindMe"
- "Shoji"
- "SolariumAvatars"
- "reportMessageListResultEngaged:engagementAction:"
- "reportMessageListResultsFetched:isFinished:"
- "reportMessageListResultsVisible:"

```
