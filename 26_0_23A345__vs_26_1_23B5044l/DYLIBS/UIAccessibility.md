## UIAccessibility

> `/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility`

```diff

-3190.6.0.1.0
-  __TEXT.__text: 0x661e0
-  __TEXT.__auth_stubs: 0x15a0
-  __TEXT.__objc_methlist: 0x6a1c
+3191.3.0.0.0
+  __TEXT.__text: 0x66620
+  __TEXT.__auth_stubs: 0x15c0
+  __TEXT.__objc_methlist: 0x6a44
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x6d01
-  __TEXT.__oslogstring: 0x2c1e
-  __TEXT.__gcc_except_tab: 0xdd4
+  __TEXT.__cstring: 0x6d0d
+  __TEXT.__oslogstring: 0x2c88
+  __TEXT.__gcc_except_tab: 0xddc
   __TEXT.__dlopen_cstrs: 0x266
   __TEXT.__ustring: 0x14
-  __TEXT.__unwind_info: 0x1bd8
+  __TEXT.__unwind_info: 0x1be0
   __TEXT.__objc_classname: 0xb74
-  __TEXT.__objc_methname: 0x16e9d
-  __TEXT.__objc_methtype: 0x1f0a
-  __TEXT.__objc_stubs: 0x108e0
-  __DATA_CONST.__got: 0xd08
+  __TEXT.__objc_methname: 0x16f4f
+  __TEXT.__objc_methtype: 0x1f3a
+  __TEXT.__objc_stubs: 0x10920
+  __DATA_CONST.__got: 0xd20
   __DATA_CONST.__const: 0x15f8
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5580
+  __DATA_CONST.__objc_selrefs: 0x55a0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__auth_got: 0xae0
+  __AUTH_CONST.__auth_got: 0xaf0
   __AUTH_CONST.__const: 0x1208
-  __AUTH_CONST.__cfstring: 0x62a0
+  __AUTH_CONST.__cfstring: 0x62c0
   __AUTH_CONST.__objc_const: 0x4970
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AEE4BE93-E5F5-32BB-8F51-9E852B160A9C
-  Functions: 2756
-  Symbols:   9626
-  CStrings:  5336
+  UUID: 130D031C-FB9D-3922-BB93-DE09DD840675
+  Functions: 2759
+  Symbols:   9639
+  CStrings:  5344
 
Symbols:
+ -[NSObject(AXPrivCategory) _accessibilityIsInMenuBar]
+ -[NSObject(AXPrivCategory) _accessibilityPostHoverTypingOnlyValueChangedNotificationWithInsertedText:inputFrame:isSecureText:]
+ -[NSObject(AXPrivCategory) _accessibilitySetIsInMenuBar:]
+ GCC_except_table1050
+ GCC_except_table1158
+ GCC_except_table1205
+ GCC_except_table1347
+ _AXDeviceSupportsHoverTextTyping
+ _AXProcessIsClarityBoard
+ ___block_literal_global.1933
+ ___block_literal_global.1952
+ ___block_literal_global.1963
+ ___block_literal_global.1973
+ ___block_literal_global.1978
+ ___block_literal_global.1980
+ ___block_literal_global.1984
+ ___block_literal_global.3064
+ ___block_literal_global.3270
+ ___block_literal_global.3272
+ ___block_literal_global.3274
+ ___block_literal_global.3282
+ ___block_literal_global.3290
+ ___block_literal_global.3293
+ ___block_literal_global.3295
+ _kAXValueChangeUserInfoKeyIsHoverTypingOnly
+ _kAXValueChangeUserInfoKeyIsSecureText
+ _kAXValueHoverTypingInputFrame
+ _objc_msgSend$_accessibilityIsInMenuBar
+ _objc_msgSend$hoverTextTypingEnabled
- GCC_except_table1049
- GCC_except_table1155
- GCC_except_table1202
- GCC_except_table1344
- ___block_literal_global.1930
- ___block_literal_global.1949
- ___block_literal_global.1960
- ___block_literal_global.1970
- ___block_literal_global.1972
- ___block_literal_global.1977
- ___block_literal_global.1981
- ___block_literal_global.3057
- ___block_literal_global.3263
- ___block_literal_global.3265
- ___block_literal_global.3267
- ___block_literal_global.3275
- ___block_literal_global.3283
- ___block_literal_global.3286
- ___block_literal_global.3288
CStrings:
+ "Did not post Hover Typing-only notification because the feature is not active (supports: %d, enabled: %d)"
+ "IsInMenuBar"
+ "_accessibilityIsInMenuBar"
+ "_accessibilityPostHoverTypingOnlyValueChangedNotificationWithInsertedText:inputFrame:isSecureText:"
+ "_accessibilitySetIsInMenuBar:"
+ "hoverTextTypingEnabled"
+ "v60@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24B56"

```
