## com.apple.datadetectors.AddToRecentsService

> `/System/Library/PrivateFrameworks/DataDetectorsUI.framework/XPCServices/com.apple.datadetectors.AddToRecentsService.xpc/com.apple.datadetectors.AddToRecentsService`

```diff

-522.3.0.0.0
-  __TEXT.__text: 0x8c0
-  __TEXT.__auth_stubs: 0x220
-  __TEXT.__objc_stubs: 0x280
-  __TEXT.__objc_methlist: 0x44
+522.9.0.0.0
+  __TEXT.__text: 0xc98
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0x4a0
+  __TEXT.__objc_methlist: 0x68
   __TEXT.__const: 0x60
-  __TEXT.__objc_classname: 0x66
-  __TEXT.__objc_methname: 0x3bb
-  __TEXT.__objc_methtype: 0x185
+  __TEXT.__objc_classname: 0x7b
+  __TEXT.__objc_methname: 0x556
+  __TEXT.__objc_methtype: 0x1b0
+  __TEXT.__cstring: 0xf7
   __TEXT.__oslogstring: 0xbd
-  __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x118
+  __TEXT.__unwind_info: 0x78
+  __DATA_CONST.__auth_got: 0x178
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__cfstring: 0xa0
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x500
-  __DATA.__objc_selrefs: 0xc0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x48
-  __DATA.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA.__objc_const: 0x5b0
+  __DATA.__objc_selrefs: 0x148
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0xa0
+  __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/SafariServices.framework/SafariServices
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreRecents.framework/CoreRecents
   - /System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13
-  Symbols:   58
-  CStrings:  80
+  Functions: 18
+  Symbols:   78
+  CStrings:  108
 
Symbols:
+ _CFArrayContainsValue
+ _CFArrayGetCount
+ _CFArrayGetTypeID
+ _CFGetTypeID
+ _DDPerformWebSearchFromQuery
+ _NSLog
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$__SFSearchEngineController
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ __NSConcreteGlobalBlock
+ ___CFConstantStringClassReference
+ _dispatch_once
+ _objc_autoreleaseReturnValue
+ _objc_release
+ _objc_retain
+ _objc_retain_x19
CStrings:
+ "@24@0:8@16"
+ "AddToRecentsService couldn't get the default browser"
+ "DDUISearchWebHandler"
+ "T@\"NSString\",?,R,C"
+ "bundleIdentifier"
+ "com.apple.datadetectors.AddToRecentsService"
+ "com.apple.mobilesafarishared"
+ "com.apple.security.exception.shared-preference.read-only"
+ "com.apple.security.exception.shared-preference.read-write"
+ "defaultSearchEngine"
+ "defaultWorkspace"
+ "initWithServiceName:"
+ "invalidate"
+ "isEqualToString:"
+ "mainBundle"
+ "openURL:configuration:completionHandler:"
+ "performWebSearchFromQuery:"
+ "reloadSearchEngines"
+ "remoteObjectProxy"
+ "searchURLForUserTypedString:"
+ "setRemoteObjectInterface:"
+ "sharedInstance"
+ "stringByTrimmingCharactersInSet:"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8@16"
+ "v8@?0"
+ "webSearchURLForQueryString:"
+ "whitespaceAndNewlineCharacterSet"

```
