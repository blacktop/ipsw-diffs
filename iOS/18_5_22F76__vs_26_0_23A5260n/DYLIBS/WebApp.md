## WebApp

> `/System/Library/PrivateFrameworks/WebApp.framework/WebApp`

```diff

-621.2.5.10.10
-  __TEXT.__text: 0x2990
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x7dc
+622.1.14.10.4
+  __TEXT.__text: 0x2aac
+  __TEXT.__auth_stubs: 0x3e0
+  __TEXT.__objc_methlist: 0x80c
   __TEXT.__cstring: 0x1b9
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x30
   __TEXT.__oslogstring: 0x156
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x160
-  __TEXT.__objc_classname: 0x138
-  __TEXT.__objc_methname: 0x1cef
-  __TEXT.__objc_methtype: 0xdcd
-  __TEXT.__objc_stubs: 0xea0
-  __DATA_CONST.__got: 0xd8
+  __TEXT.__unwind_info: 0x158
+  __TEXT.__objc_classname: 0x147
+  __TEXT.__objc_methname: 0x1dbe
+  __TEXT.__objc_methtype: 0xe39
+  __TEXT.__objc_stubs: 0xf40
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__const: 0x120
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x718
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__objc_selrefs: 0x758
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__auth_got: 0x200
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__objc_const: 0x1358
-  __AUTH.__objc_data: 0x230
+  __AUTH_CONST.__objc_const: 0x13f8
+  __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x74
   __DATA.__data: 0x240
   __DATA.__bss: 0x30

   - /System/Library/Frameworks/SafariServices.framework/SafariServices
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/SafariCore.framework/SafariCore
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 168A0E33-9850-37F4-A450-1570C94773FB
-  Functions: 74
-  Symbols:   499
-  CStrings:  431
+  UUID: 84D18C67-745A-3714-8EE9-E08D548548DC
+  Functions: 75
+  Symbols:   516
+  CStrings:  442
 
Symbols:
+ -[WebApplication buildMenuWithBuilder:]
+ _NSStringFromClass
+ _OBJC_CLASS_$_SFBrowserMenuProvider
+ _OBJC_CLASS_$_UIMenuSystem
+ _OBJC_CLASS_$_WebApplication
+ _OBJC_METACLASS_$_UIApplication
+ _OBJC_METACLASS_$_WebApplication
+ __OBJC_$_INSTANCE_METHODS_WebApplication
+ __OBJC_CLASS_RO_$_WebApplication
+ __OBJC_METACLASS_RO_$_WebApplication
+ _objc_msgSend$mainSystem
+ _objc_msgSend$rebuildMenuIfNeededForPersona:
+ _objc_msgSend$setMenusIfNecessaryForWebAppWithBuilder:
+ _objc_msgSend$sharedProvider
+ _objc_msgSend$system
+ _objc_opt_class
Functions:
~ -[AppDelegate applicationDidFinishLaunching:] : 4 -> 76
~ _WebAppMainEntry : 240 -> 276
+ -[WebApplication buildMenuWithBuilder:]
CStrings:
+ "@\"UISceneWindowingControlStyle\"24@0:8@\"UIWindowScene\"16"
+ "WebApplication"
+ "buildMenuWithBuilder:"
+ "mainSystem"
+ "preferredWindowingControlStyleForScene:"
+ "rebuildMenuIfNeededForPersona:"
+ "setMenusIfNecessaryForWebAppWithBuilder:"
+ "sharedProvider"
+ "system"
+ "v32@0:8@\"UIWindowScene\"16@\"UIWindowSceneGeometry\"24"
+ "windowScene:didUpdateEffectiveGeometry:"

```
