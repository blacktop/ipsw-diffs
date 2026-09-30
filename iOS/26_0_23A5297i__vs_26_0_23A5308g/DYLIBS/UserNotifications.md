## UserNotifications

> `/System/Library/Frameworks/UserNotifications.framework/UserNotifications`

```diff

-634.0.0.0.0
-  __TEXT.__text: 0x2fc34
+640.0.0.0.0
+  __TEXT.__text: 0x2fd4c
   __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0x3698
-  __TEXT.__cstring: 0x33c6
+  __TEXT.__objc_methlist: 0x36a8
+  __TEXT.__cstring: 0x33e3
   __TEXT.__const: 0xd0
   __TEXT.__oslogstring: 0x2092
   __TEXT.__gcc_except_tab: 0x26c
   __TEXT.__dlopen_cstrs: 0x8a
   __TEXT.__unwind_info: 0xd28
   __TEXT.__objc_classname: 0x9ad
-  __TEXT.__objc_methname: 0x9637
+  __TEXT.__objc_methname: 0x967d
   __TEXT.__objc_methtype: 0x1279
-  __TEXT.__objc_stubs: 0x4fe0
+  __TEXT.__objc_stubs: 0x5000
   __DATA_CONST.__got: 0x3b0
   __DATA_CONST.__const: 0xb08
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c00
+  __DATA_CONST.__objc_selrefs: 0x1c08
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x130
   __AUTH_CONST.__auth_got: 0x348
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x3420
-  __AUTH_CONST.__objc_const: 0xa498
+  __AUTH_CONST.__cfstring: 0x3440
+  __AUTH_CONST.__objc_const: 0xa4c8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x33c
+  __DATA.__objc_ivar: 0x340
   __DATA.__data: 0x848
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0xd70

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EC9962D1-5897-34B3-8617-67A934340817
-  Functions: 1332
-  Symbols:   4656
-  CStrings:  2602
+  UUID: F1A3427C-80FC-34E7-A086-C49094A845A4
+  Functions: 1333
+  Symbols:   4660
+  CStrings:  2607
 
Symbols:
+ -[UNOneTimeCode displayCode]
+ -[UNOneTimeCode initWithCode:displayCode:applicationIdentifier:notificationIdentifier:timestamp:]
+ _OBJC_IVAR_$_UNOneTimeCode._displayCode
+ _objc_msgSend$displayCode
+ _objc_msgSend$initWithCode:displayCode:applicationIdentifier:notificationIdentifier:timestamp:
- -[UNOneTimeCode initWithCode:applicationIdentifier:notificationIdentifier:timestamp:]
- _objc_msgSend$initWithCode:applicationIdentifier:notificationIdentifier:timestamp:
CStrings:
+ "<%@: %p; code: %@; displayCode: %@; applicationIdentifier: %@; notificationIdentifier: %@; timestamp: %@>"
+ "T@\"NSString\",R,C,N,V_displayCode"
+ "_displayCode"
+ "displayCode"
+ "initWithCode:displayCode:applicationIdentifier:notificationIdentifier:timestamp:"
- "<%@: %p; code: %@; applicationIdentifier: %@; notificationIdentifier: %@; timestamp: %@>"
- "initWithCode:applicationIdentifier:notificationIdentifier:timestamp:"

```
