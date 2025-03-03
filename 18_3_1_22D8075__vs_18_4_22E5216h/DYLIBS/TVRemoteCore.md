## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-496.30.3.0.0
-  __TEXT.__text: 0xb9bcc
-  __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_methlist: 0x89c4
+496.40.29.0.0
+  __TEXT.__text: 0xbad10
+  __TEXT.__auth_stubs: 0xce0
+  __TEXT.__objc_methlist: 0xa160
   __TEXT.__const: 0x23c40
   __TEXT.__gcc_except_tab: 0xf68
-  __TEXT.__cstring: 0x57df
-  __TEXT.__oslogstring: 0x8765
-  __TEXT.__unwind_info: 0x1d50
+  __TEXT.__cstring: 0x58aa
+  __TEXT.__oslogstring: 0x8813
+  __TEXT.__unwind_info: 0x1d80
   __TEXT.__eh_frame: 0x7f8
-  __TEXT.__objc_classname: 0x10f9
-  __TEXT.__objc_methname: 0x12883
-  __TEXT.__objc_methtype: 0x3d89
-  __TEXT.__objc_stubs: 0xbf00
-  __DATA_CONST.__got: 0x7c8
-  __DATA_CONST.__const: 0x1b58
-  __DATA_CONST.__objc_classlist: 0x438
+  __TEXT.__objc_classname: 0x1105
+  __TEXT.__objc_methname: 0x12b01
+  __TEXT.__objc_methtype: 0x3e4f
+  __TEXT.__objc_stubs: 0xc020
+  __DATA_CONST.__got: 0x7d0
+  __DATA_CONST.__const: 0x1bb0
+  __DATA_CONST.__objc_classlist: 0x440
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3eb0
+  __DATA_CONST.__objc_selrefs: 0x4560
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x368
+  __DATA_CONST.__objc_superrefs: 0x370
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x688
+  __AUTH_CONST.__auth_got: 0x680
   __AUTH_CONST.__const: 0x3c18
-  __AUTH_CONST.__cfstring: 0x7860
-  __AUTH_CONST.__objc_const: 0x12160
+  __AUTH_CONST.__cfstring: 0x7a00
+  __AUTH_CONST.__objc_const: 0xfa38
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x28f0
-  __DATA.__objc_ivar: 0xa78
+  __AUTH.__objc_data: 0x2940
+  __DATA.__objc_ivar: 0xa90
   __DATA.__data: 0x1220
   __DATA.__bss: 0x150
   __DATA.__common: 0x9f8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3326
-  Symbols:   4061
-  CStrings:  5641
+  Functions: 3360
+  Symbols:   4122
+  CStrings:  5685
 
Symbols:
+ _OBJC_CLASS_$_TVRCAppInfo
+ _OBJC_METACLASS_$_TVRCAppInfo
+ _TVRCApplicationGenreKey
+ _TVRCApplicationTypeKey
+ _TVRCBundleIDKey
+ _TVRCImageKey
+ _TVRCIncludeAppMetadataKey
+ _TVRCLaunchAppEvent
+ _TVRCLocalizedAppNameKey
- _fmod
CStrings:
+ "82"
+ "<%@ %p: name=%@; bundleID=%@; appType=%@; appGenre=%@; mruCount=%@>"
+ "@64@0:8@16@24@32Q40Q48q56"
+ "ApplicationGenreKey"
+ "ApplicationTypeKey"
+ "Asking tvremoted for launchable apps for %{public}@"
+ "Asking tvremoted to launch app %{public}@ for %{public}@"
+ "BundleIDKey"
+ "ImageKey"
+ "IncludeAppMetadataKey"
+ "Invalid bundleID sent to %@"
+ "LaunchApp"
+ "LocalizedAppName"
+ "MRUCount"
+ "Sending companion request with ID %@"
+ "T@\"NSData\",R,N,V_imageData"
+ "T@\"NSString\",R,N,V_bundleID"
+ "T@\"NSString\",R,N,V_localizedName"
+ "TQ,R,N,V_MRUCount"
+ "TQ,R,N,V_appGenre"
+ "TVRCAppInfo"
+ "Tq,R,N,V_appType"
+ "_MRUCount"
+ "_appGenre"
+ "_appType"
+ "_localizedName"
+ "appGenre"
+ "appInfoWithBundleID:dictionary:"
+ "appInfoWithLocalizedName:bundleID:imageData:MRUCount:appGenre:appType:"
+ "appInfoWithMRUCount:"
+ "appType"
+ "fetchLaunchableAppsForDeviceWithIdentifier:completion:"
+ "fetchLaunchableAppsWithCompletion:"
+ "initWithLocalizedName:bundleID:imageData:MRUCount:appGenre:appType:"
+ "inputSession:documentStateDidChange:withMergeResult:"
+ "isTVApp"
+ "launchAppForDeviceWithIdentifier:bundleID:completion:"
+ "launchAppWithBundleID:completion:"
+ "localizedName"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v40@0:8@\"RTIInputSystemSession\"16@\"RTIDocumentState\"24Q32"
+ "v40@0:8@16@24Q32"
- "TVApp"
- "testarossa"
- "testarossaEnabled"

```
