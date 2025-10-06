## Messages

> `/System/Library/Frameworks/Messages.framework/Messages`

```diff

-1261.100.4.2.35
-  __TEXT.__text: 0x254c8
+1261.200.71.2.16
+  __TEXT.__text: 0x25a20
   __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x3394
+  __TEXT.__objc_methlist: 0x33c4
   __TEXT.__const: 0x338
   __TEXT.__gcc_except_tab: 0x158
   __TEXT.__cstring: 0x1add
-  __TEXT.__oslogstring: 0xab7
+  __TEXT.__oslogstring: 0xb72
   __TEXT.__dlopen_cstrs: 0x262
-  __TEXT.__unwind_info: 0xb38
+  __TEXT.__unwind_info: 0xb50
   __TEXT.__objc_classname: 0x6ca
-  __TEXT.__objc_methname: 0x9b6f
-  __TEXT.__objc_methtype: 0x28a0
-  __TEXT.__objc_stubs: 0x65e0
+  __TEXT.__objc_methname: 0x9ba7
+  __TEXT.__objc_methtype: 0x28d5
+  __TEXT.__objc_stubs: 0x6600
   __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__const: 0x5f0
+  __DATA_CONST.__const: 0x618
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8

   __AUTH_CONST.__auth_got: 0x468
   __AUTH.__objc_data: 0x820
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x2e8
+  __DATA.__objc_classrefs: 0x2e0
   __DATA.__objc_superrefs: 0xf0
-  __DATA.__objc_ivar: 0x340
+  __DATA.__objc_ivar: 0x33c
   __DATA.__data: 0xa70
   __DATA.__bss: 0x128
   __DATA_DIRTY.__objc_data: 0x230

   - /System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BE636B6D-DF11-393A-AE3C-90C25E342D61
-  Functions: 1288
-  Symbols:   4468
-  CStrings:  2295
+  UUID: CA007AC4-1348-384A-A872-BD6A0149F895
+  Functions: 1292
+  Symbols:   4474
+  CStrings:  2294
 
Symbols:
+ -[MSMessagesAppViewController _presentAlertSheetWithTitle:message:buttonTitles:styles:completion:]
+ -[_MSMessageAppBundleContext presentAlertSheetWithTitle:message:buttonTitles:styles:completion:]
+ -[_MSMessageAppBundleHostContext _presentAlertSheetWithTitle:message:buttonTitles:styles:completion:]
+ -[_MSMessageAppContext presentAlertSheetWithTitle:message:buttonTitles:styles:completion:]
+ -[_MSMessageAppExtensionContext presentAlertSheetWithTitle:message:buttonTitles:styles:completion:]
+ -[_MSMessageAppExtensionHostContext _presentAlertSheetWithTitle:message:buttonTitles:styles:completion:]
+ ___block_descriptor_64_e8_32s40s48s56s_e63_v32?0?<v?"<NSSecureCoding>""NSError">8#16"NSDictionary"24ls32l8s40l8s48l8s56l8
+ ___block_literal_global.126
+ _objc_msgSend$_presentAlertSheetWithTitle:message:buttonTitles:styles:completion:
+ _objc_msgSend$presentAlertSheetWithTitle:message:buttonTitles:styles:completion:
- -[_MSTempFileManager .cxx_destruct]
- -[_MSTempFileManager registry]
- _OBJC_CLASS_$_NSHashTable
- _OBJC_IVAR_$__MSTempFileManager._registry
- __OBJC_$_INSTANCE_VARIABLES__MSTempFileManager
- __OBJC_$_PROP_LIST__MSTempFileManager
- ___block_literal_global.124
- _objc_msgSend$weakObjectsHashTable
CStrings:
+ "_MSMessageMediaPayload: Cannot copy sticker file: %@ to %@, because either the source or destination file URL is nil. This may be expected if the original sticker did not have a file URL"
+ "_presentAlertSheetWithTitle:message:buttonTitles:styles:completion:"
+ "presentAlertSheetWithTitle:message:buttonTitles:styles:completion:"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32@\"NSArray\"40@?<v@?i>48"
- "@\"NSHashTable\""
- "T@\"NSHashTable\",R,N,V_registry"
- "_registry"
- "registry"
- "weakObjectsHashTable"

```
