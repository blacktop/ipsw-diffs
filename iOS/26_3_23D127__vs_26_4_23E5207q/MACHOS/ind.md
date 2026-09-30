## ind

> `/System/Library/PrivateFrameworks/iCloudNotification.framework/ind`

```diff

-301.23.3.2.0
-  __TEXT.__text: 0x385e4
-  __TEXT.__auth_stubs: 0x1360
-  __TEXT.__objc_stubs: 0x43a0
-  __TEXT.__objc_methlist: 0x1c1c
-  __TEXT.__cstring: 0x237f
-  __TEXT.__objc_methname: 0x4e9d
-  __TEXT.__oslogstring: 0x4c62
-  __TEXT.__objc_classname: 0x50a
-  __TEXT.__objc_methtype: 0x10f2
-  __TEXT.__const: 0xc60
-  __TEXT.__gcc_except_tab: 0x4e4
-  __TEXT.__dlopen_cstrs: 0x56
+301.23.4.7.0
+  __TEXT.__text: 0x39010
+  __TEXT.__auth_stubs: 0x12f0
+  __TEXT.__objc_stubs: 0x4800
+  __TEXT.__objc_methlist: 0x1cb4
+  __TEXT.__cstring: 0x20b4
+  __TEXT.__objc_methname: 0x5295
+  __TEXT.__oslogstring: 0x4e62
+  __TEXT.__objc_classname: 0x5ea
+  __TEXT.__objc_methtype: 0x12c7
+  __TEXT.__const: 0xc64
+  __TEXT.__gcc_except_tab: 0x45c
+  __TEXT.__dlopen_cstrs: 0xbc
   __TEXT.__swift5_typeref: 0x50c
   __TEXT.__swift5_fieldmd: 0x254
   __TEXT.__constg_swiftt: 0x494
-  __TEXT.__swift5_reflstr: 0x164
+  __TEXT.__swift5_reflstr: 0x163
   __TEXT.__swift5_capture: 0x228
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x78

   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0xf90
-  __TEXT.__eh_frame: 0xef0
-  __DATA_CONST.__auth_got: 0x9c0
-  __DATA_CONST.__got: 0x5b0
+  __TEXT.__unwind_info: 0x1030
+  __TEXT.__eh_frame: 0xe90
+  __DATA_CONST.__auth_got: 0x988
+  __DATA_CONST.__got: 0x5b8
   __DATA_CONST.__auth_ptr: 0x1b0
-  __DATA_CONST.__const: 0x17e0
-  __DATA_CONST.__cfstring: 0x2200
-  __DATA_CONST.__objc_classlist: 0x198
+  __DATA_CONST.__const: 0x18b0
+  __DATA_CONST.__cfstring: 0x2260
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0x4838
-  __DATA.__objc_selrefs: 0x1530
+  __DATA.__objc_const: 0x48e8
+  __DATA.__objc_selrefs: 0x15a0
   __DATA.__objc_ivar: 0x1a8
-  __DATA.__objc_data: 0x1418
-  __DATA.__data: 0x630
-  __DATA.__bss: 0xef0
+  __DATA.__objc_data: 0x1468
+  __DATA.__data: 0x638
+  __DATA.__bss: 0xf00
   __DATA.__common: 0x60
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 89256AF3-9A9E-3FE2-9325-4BE6060AEBF1
-  Functions: 1292
-  Symbols:   581
-  CStrings:  2077
+  UUID: 1BEDE188-2146-3B28-95E9-5EB95498FE6C
+  Functions: 1318
+  Symbols:   577
+  CStrings:  2104
 
Symbols:
+ _NSClassFromString
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$__LSOpenConfiguration
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ "-[INDaemon notifyAMSEngagementAppDidBecomeActiveWithCompletion:]"
+ "-[INDaemon performAMSEngagementWithParameters:completion:]"
+ "-[INDaemon performPostPurchaseTeardownWithCompletion:]"
+ "Attempting to resolve chatterbox URL %@"
+ "Chatterbox URL resolved to itself! %@"
+ "Chatterbox URL resolved to unexpected URL! %@"
+ "Could not resolve chatterbox URL, falling back to browser: %@"
+ "Failed to open URL in browser: %@"
+ "Failed to resolve chatterbox URL %@ with error: %@."
+ "Failed to resolve chatterbox URL %@ with unknown error."
+ "Handling chatterbox URL: %@"
+ "ICQAMSEngagementPresenter"
+ "ICQAMSEngagementPresenter class not available."
+ "ICQAMSEngagementPresenter not available"
+ "INRedirectResolver"
+ "Launching URL: %@"
+ "Opening URL in browser (bypassing universal links): %@"
+ "Successfully opened URL in browser"
+ "_SWCChatterboxResolver"
+ "_openURLInBrowser:"
+ "_processResolvedURL:originalURL:resolutionError:completion:"
+ "_resolveURL:completion:"
+ "defaultWorkspace"
+ "handleChatterboxURL:completion:"
+ "host"
+ "icq.icloud.com"
+ "ind"
+ "notifyAMSEngagementAppDidBecomeActiveWithCompletion:"
+ "openURL:configuration:completionHandler:"
+ "performAMSEngagementWithParameters:completion:"
+ "performPostPurchaseTeardownWithCompletion:"
+ "reactivatePendingEngagementWithCompletion:"
+ "resolveWithCompletionHandler:"
+ "setAllowURLOverrides:"
+ "sharedPresenter"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SharedWebCredentials.framework/SharedWebCredentials"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
+ "v32@0:8@\"NSDictionary\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?B@\"NSError\">24"

```
