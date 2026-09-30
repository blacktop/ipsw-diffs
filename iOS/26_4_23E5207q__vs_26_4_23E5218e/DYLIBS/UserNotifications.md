## UserNotifications

> `/System/Library/Frameworks/UserNotifications.framework/UserNotifications`

```diff

-640.4.31.100.0
-  __TEXT.__text: 0x314f8
+640.4.40.0.0
+  __TEXT.__text: 0x315d8
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x36a8
-  __TEXT.__cstring: 0x33fc
+  __TEXT.__objc_methlist: 0x36c0
+  __TEXT.__cstring: 0x340c
   __TEXT.__const: 0xd0
   __TEXT.__oslogstring: 0x2092
   __TEXT.__gcc_except_tab: 0x248
   __TEXT.__dlopen_cstrs: 0x8a
   __TEXT.__unwind_info: 0xdb8
   __TEXT.__objc_classname: 0x9ad
-  __TEXT.__objc_methname: 0x967d
+  __TEXT.__objc_methname: 0x96a3
   __TEXT.__objc_methtype: 0x1279
   __TEXT.__objc_stubs: 0x5000
   __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__const: 0xb08
+  __DATA_CONST.__const: 0xb18
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c08
+  __DATA_CONST.__objc_selrefs: 0x1c18
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x130
   __AUTH_CONST.__auth_got: 0x318
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x3440
+  __AUTH_CONST.__cfstring: 0x3460
   __AUTH_CONST.__objc_const: 0xa4c8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x2d0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0B95D802-B106-3280-A57C-224326FE8CB7
-  Functions: 1343
-  Symbols:   4678
-  CStrings:  2609
+  UUID: BB048E40-D7E4-36BA-9E19-F28D61384C37
+  Functions: 1345
+  Symbols:   4682
+  CStrings:  2613
 
Symbols:
+ +[UNNotificationIcon iconForApplicationURL:]
+ -[UNNotificationIcon applicationURL]
Functions:
~ -[UNNotificationCategory _initWithIdentifier:actions:minimalActions:alternateAction:intentIdentifiers:hiddenPreviewsBodyPlaceholder:categorySummaryFormat:actionsMenuTitle:options:backgroundStyle:listPriority:] : 392 -> 396
~ -[UNNotificationIcon initWithCoder:] : 820 -> 840
+ +[UNNotificationIcon iconForSystemImageNamed:]
+ -[UNNotificationIcon dateComponents]
CStrings:
+ "Application URL"
+ "applicationURL"
+ "iconForApplicationURL:"

```
