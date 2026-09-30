## CPAnalytics

> `/System/Library/PrivateFrameworks/CPAnalytics.framework/CPAnalytics`

```diff

-840.2.120.0.0
-  __TEXT.__text: 0x13158
+842.0.102.0.0
+  __TEXT.__text: 0x138c8
   __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x13d4
+  __TEXT.__objc_methlist: 0x141c
   __TEXT.__const: 0x180
   __TEXT.__gcc_except_tab: 0x160
-  __TEXT.__cstring: 0x1fd6
+  __TEXT.__cstring: 0x21e9
   __TEXT.__oslogstring: 0x1004
-  __TEXT.__unwind_info: 0x550
+  __TEXT.__unwind_info: 0x560
   __TEXT.__objc_classname: 0x3c1
-  __TEXT.__objc_methname: 0x36c8
+  __TEXT.__objc_methname: 0x37ab
   __TEXT.__objc_methtype: 0x4c0
-  __TEXT.__objc_stubs: 0x3080
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x8b8
+  __TEXT.__objc_stubs: 0x3140
+  __DATA_CONST.__got: 0x2a0
+  __DATA_CONST.__const: 0x8d0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd58
+  __DATA_CONST.__objc_selrefs: 0xd98
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__auth_got: 0x2d8
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x2740
-  __AUTH_CONST.__objc_const: 0x25c0
-  __AUTH_CONST.__objc_intobj: 0x2a0
+  __AUTH_CONST.__cfstring: 0x2aa0
+  __AUTH_CONST.__objc_const: 0x2620
+  __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_ivar: 0x120
+  __DATA.__objc_ivar: 0x128
   __DATA.__data: 0x248
   __DATA.__bss: 0x19
   __DATA_DIRTY.__objc_data: 0x870

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftDemangle.dylib
-  UUID: BE494D7B-AC3F-3F5F-85CC-8E2E63BC5FE3
-  Functions: 385
-  Symbols:   1887
-  CStrings:  1394
+  UUID: 1B8D82AB-318E-30B4-9E2C-0EC0F0AADF49
+  Functions: 391
+  Symbols:   1911
+  CStrings:  1460
 
Symbols:
+ +[CPAnalyticsCoreAnalyticsHelper _mediaAgeEnum:]
+ -[CPAnalyticsAppStateDestination appLaunchSource]
+ -[CPAnalyticsAppStateDestination launchSource]
+ -[CPAnalyticsAppStateDestination setAppLaunchSource:]
+ -[CPAnalyticsAppStateDestination setLaunchSource:]
+ -[PhotosAnalyticsSystemPropertyProvider appLaunchSource]
+ GCC_except_table373
+ _CPAnalyticsAppLaunchSource
+ _CPAnalyticsAppLaunchSourceEvent
+ _CPAnalyticsSystemPropertyAppLaunchSource
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_IVAR_$_CPAnalyticsAppStateDestination._appLaunchSource
+ _OBJC_IVAR_$_CPAnalyticsAppStateDestination._launchSource
+ ___51-[CPAnalyticsAppStateDestination updateWithConfig:]_block_invoke.55
+ ___51-[CPAnalyticsAppStateDestination updateWithConfig:]_block_invoke.56
+ ___51-[CPAnalyticsAppStateDestination updateWithConfig:]_block_invoke.57
+ _objc_msgSend$_mediaAgeEnum:
+ _objc_msgSend$appLaunchSource
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$setAppLaunchSource:
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$synchronize
- GCC_except_table367
- ___51-[CPAnalyticsAppStateDestination updateWithConfig:]_block_invoke.49
- ___51-[CPAnalyticsAppStateDestination updateWithConfig:]_block_invoke.50
- ___51-[CPAnalyticsAppStateDestination updateWithConfig:]_block_invoke.51
CStrings:
+ "CPAnalyticsCurrentAppLaunchSource"
+ "MediaAge10Years"
+ "MediaAge1Year"
+ "MediaAge20Years"
+ "MediaAge2Years"
+ "MediaAge30Years"
+ "MediaAge3Years"
+ "MediaAge40PlusYears"
+ "MediaAge40Years"
+ "MediaAge4Years"
+ "MediaAge5Years"
+ "MediaAgeFuture"
+ "MediaAgeJustNow"
+ "MediaAgeLast180Days"
+ "MediaAgeLast30Days"
+ "MediaAgeLast60Days"
+ "MediaAgeLast90Days"
+ "MediaAgeLastYear"
+ "MediaAgeNew"
+ "MediaAgeThisWeek"
+ "MediaAgeToday"
+ "MediaAgeVeryNew"
+ "MediaAgeYesterday"
+ "T@\"NSObject\",&,N,V_appLaunchSource"
+ "T@\"NSString\",&,N,V_launchSource"
+ "_appLaunchSource"
+ "_launchSource"
+ "_mediaAgeEnum:"
+ "appLaunchSource"
+ "com.apple.photos.CPAnalytics.appLaunchSource"
+ "com.apple.photos.CPAnalytics.sharedAlbumsEngaged"
+ "cpa_common_appLaunchSource"
+ "integerForKey:"
+ "launchSource"
+ "setAppLaunchSource:"
+ "setLaunchSource:"
+ "standardUserDefaults"
+ "synchronize"

```
