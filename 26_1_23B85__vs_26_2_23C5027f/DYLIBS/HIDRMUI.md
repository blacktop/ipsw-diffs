## HIDRMUI

> `/System/Library/PrivateFrameworks/HIDRMUI.framework/HIDRMUI`

```diff

-71.40.3.0.0
-  __TEXT.__text: 0x6c8c
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0x824
+71.60.6.0.0
+  __TEXT.__text: 0x7260
+  __TEXT.__auth_stubs: 0x490
+  __TEXT.__objc_methlist: 0x874
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0x494
-  __TEXT.__cstring: 0x58e
+  __TEXT.__cstring: 0x5c0
   __TEXT.__ustring: 0x110
   __TEXT.__oslogstring: 0x75e
-  __TEXT.__unwind_info: 0x278
-  __TEXT.__objc_classname: 0xcf
-  __TEXT.__objc_methname: 0x16b5
-  __TEXT.__objc_methtype: 0x22f
-  __TEXT.__objc_stubs: 0x1360
+  __TEXT.__unwind_info: 0x290
+  __TEXT.__objc_classname: 0xd1
+  __TEXT.__objc_methname: 0x1784
+  __TEXT.__objc_methtype: 0x23d
+  __TEXT.__objc_stubs: 0x13c0
   __DATA_CONST.__got: 0x170
   __DATA_CONST.__const: 0x270
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x618
+  __DATA_CONST.__objc_selrefs: 0x648
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x250
+  __AUTH_CONST.__auth_got: 0x258
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x440
-  __AUTH_CONST.__objc_const: 0xdd8
+  __AUTH_CONST.__cfstring: 0x460
+  __AUTH_CONST.__objc_const: 0xe08
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0xb0
+  __DATA.__objc_ivar: 0xb4
   __DATA.__data: 0x120
   __DATA.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 58DB309E-5978-398C-8695-521B705830AB
-  Functions: 219
-  Symbols:   887
-  CStrings:  454
+  UUID: D52A90C7-3A9D-314F-A587-463BAAFBD1F0
+  Functions: 226
+  Symbols:   906
+  CStrings:  465
 
Symbols:
+ +[IOUserNotificationButton buttonWithTitle:andIdentifier:]
+ -[IOUserNotification addButtonWithTitle:andIdentifier:]
+ -[IOUserNotification hasSelectedButtonWithIdentifier:]
+ -[IOUserNotificationButton hash]
+ -[IOUserNotificationButton identifier]
+ -[IOUserNotificationButton initWithTitle:andIdentifier:]
+ -[IOUserNotificationButton isEqual:]
+ -[IOUserNotificationButton setIdentifier:]
+ GCC_except_table17
+ GCC_except_table28
+ _OBJC_IVAR_$_IOUserNotificationButton._identifier
+ _objc_msgSend$buttonWithTitle:andIdentifier:
+ _objc_msgSend$identifier
+ _objc_msgSend$initWithTitle:andIdentifier:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_release_x28
- -[IOUserNotificationButton initWithTitle:]
- GCC_except_table10
- _objc_msgSend$initWithTitle:
CStrings:
+ "<%@: %p, title: %@, identifier: %@, selected: %d>"
+ "B32@0:8@16@24"
+ "T@\"NSString\",C,N,V_identifier"
+ "_identifier"
+ "addButtonWithTitle:andIdentifier:"
+ "buttonWithTitle:andIdentifier:"
+ "hasSelectedButtonWithIdentifier:"
+ "identifier"
+ "initWithTitle:andIdentifier:"
+ "numberWithUnsignedInteger:"
+ "setIdentifier:"
- "initWithTitle:"

```
