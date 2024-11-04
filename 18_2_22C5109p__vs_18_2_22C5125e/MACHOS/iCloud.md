## iCloud

> `/Applications/iCloud.app/iCloud`

```diff

-2230.20.1.0.0
-  __TEXT.__text: 0x13b70
+2230.23.0.0.0
+  __TEXT.__text: 0x13de8
   __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_stubs: 0x2c80
-  __TEXT.__objc_methlist: 0xa1c
+  __TEXT.__objc_stubs: 0x2d00
+  __TEXT.__objc_methlist: 0xa2c
   __TEXT.__const: 0xc8
   __TEXT.__gcc_except_tab: 0x6d0
-  __TEXT.__objc_methname: 0x3c73
-  __TEXT.__cstring: 0x25f3
-  __TEXT.__oslogstring: 0x1921
+  __TEXT.__objc_methname: 0x3cd6
+  __TEXT.__cstring: 0x2621
+  __TEXT.__oslogstring: 0x19ac
   __TEXT.__objc_classname: 0xc9
   __TEXT.__objc_methtype: 0xd51
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x3e8
   __DATA_CONST.__auth_got: 0x2e0
-  __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0x648
+  __DATA_CONST.__got: 0x388
+  __DATA_CONST.__const: 0x650
   __DATA_CONST.__cfstring: 0x1e20
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x1728
-  __DATA.__objc_selrefs: 0xbf0
+  __DATA.__objc_selrefs: 0xc10
   __DATA.__objc_ivar: 0xac
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x180

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 266
-  Symbols:   214
-  CStrings:  1058
+  Functions: 267
+  Symbols:   216
+  CStrings:  1065
 
Symbols:
+ _OBJC_CLASS_$_APApplication
+ _OBJC_CLASS_$_APGuard
CStrings:
+ "Failed to authenticate user for bundle %!@(MISSING). Error: %!@(MISSING)"
+ "Failed to initialize App Protection Subject for some reason. Skipping authentication."
+ "ShareAcceptorStatePromptingForApplicationAuth"
+ "_authenticateUsers:"
+ "applicationWithBundleIdentifier:"
+ "authenticateSyncForSubject:error:"
+ "sharedGuard"

```
