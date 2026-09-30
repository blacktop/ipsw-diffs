## iCloudNotification

> `/System/Library/PrivateFrameworks/iCloudNotification.framework/iCloudNotification`

```diff

-301.22.5.4.0
-  __TEXT.__text: 0x4f10
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0x53c
+301.23.0.16.0
+  __TEXT.__text: 0x50c4
+  __TEXT.__auth_stubs: 0x360
+  __TEXT.__objc_methlist: 0x564
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x298
-  __TEXT.__cstring: 0x598
+  __TEXT.__cstring: 0x5cb
   __TEXT.__oslogstring: 0x54a
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__unwind_info: 0x250
   __TEXT.__objc_classname: 0x87
-  __TEXT.__objc_methname: 0x106d
-  __TEXT.__objc_methtype: 0x85b
-  __TEXT.__objc_stubs: 0x8a0
-  __DATA_CONST.__got: 0x98
+  __TEXT.__objc_methname: 0x10ef
+  __TEXT.__objc_methtype: 0x8cd
+  __TEXT.__objc_stubs: 0x900
+  __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x2c8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x448
+  __DATA_CONST.__objc_selrefs: 0x460
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1b8
+  __AUTH_CONST.__auth_got: 0x1c0
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x3e0
-  __AUTH_CONST.__objc_const: 0x620
+  __AUTH_CONST.__cfstring: 0x420
+  __AUTH_CONST.__objc_const: 0x630
   __AUTH_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x180

   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 95D7AC44-877E-346B-B49A-6A11FC6E74EF
-  Functions: 132
-  Symbols:   532
-  CStrings:  346
+  UUID: D029EB84-B303-3013-8D76-C5FFA5E2D18E
+  Functions: 134
+  Symbols:   541
+  CStrings:  357
 
Symbols:
+ -[INDaemonConnection observeFPItem:notifyURL:completion:]
+ _OBJC_CLASS_$_FPItemID
+ ___57-[INDaemonConnection observeFPItem:notifyURL:completion:]_block_invoke
+ __os_feature_enabled_impl
+ _objc_msgSend$observeFPItem:notifyURL:completion:
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$synchronousDaemonWithErrorHandler:
CStrings:
+ "Solarium"
+ "SwiftUI"
+ "X-Apple-iCloudUI-Feature"
+ "observeFPItem:notifyURL:completion:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "solarium"
+ "syncFPItem:observeItemIDs:notifyURL:completion:"
+ "v40@0:8@\"FPItemID\"16@\"NSURL\"24@?<v@?B@\"NSError\">32"
+ "v48@0:8@\"FPItemID\"16@\"NSArray\"24@\"NSURL\"32@?<v@?B@\"NSError\">40"

```
