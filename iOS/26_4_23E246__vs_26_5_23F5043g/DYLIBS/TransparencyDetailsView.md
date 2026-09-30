## TransparencyDetailsView

> `/System/Library/PrivateFrameworks/TransparencyDetailsView.framework/TransparencyDetailsView`

```diff

-637.4.7.0.0
-  __TEXT.__text: 0x8ff8
+637.5.1.0.0
+  __TEXT.__text: 0x91bc
   __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_methlist: 0x884
+  __TEXT.__objc_methlist: 0x8ac
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0xb91
+  __TEXT.__cstring: 0xbef
   __TEXT.__ustring: 0x88
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__unwind_info: 0x238
+  __TEXT.__unwind_info: 0x240
   __TEXT.__objc_classname: 0xb9
-  __TEXT.__objc_methname: 0x2371
+  __TEXT.__objc_methname: 0x23a4
   __TEXT.__objc_methtype: 0x559
-  __TEXT.__objc_stubs: 0x1e00
-  __DATA_CONST.__got: 0x1c8
+  __TEXT.__objc_stubs: 0x1e40
+  __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__const: 0x178
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x980
+  __DATA_CONST.__objc_selrefs: 0x990
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x198

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 624932CE-E61E-331B-B03D-463AE6389238
-  Functions: 158
-  Symbols:   800
-  CStrings:  587
+  UUID: 95B25659-107B-3CD8-B109-09B0DBE232F4
+  Functions: 161
+  Symbols:   809
+  CStrings:  589
 
Symbols:
+ -[ADTransparencyViewController _currentTextSizeValue]
+ -[NewsTransparencyViewController _currentTextSizeValue]
+ -[UserTransparencyViewController _currentTextSizeValue]
+ GCC_except_table18
+ GCC_except_table3
+ _UIContentSizeCategoryMedium
+ _objc_msgSend$_currentTextSizeValue
+ _objc_msgSend$preferredContentSizeCategory
- GCC_except_table17
- GCC_except_table2
Functions:
+ -[UserTransparencyViewController _currentTextSizeValue]
~ -[UserTransparencyViewController immediatelyLoadViewControllerBeforeNetworkRequest] : 2832 -> 2868
+ -[NewsTransparencyViewController _currentTextSizeValue]
~ -[NewsTransparencyViewController _commonInit] : 1564 -> 1592
+ -[ADTransparencyViewController _currentTextSizeValue]
~ -[ADTransparencyViewController configureWebView] : 1588 -> 1616
CStrings:
+ "        window.transparency = {            isLocationPermissionGranted: () => { return %@ },            isPAEnabled: () => { return %@ },            userTextSize: () => { return '%@' }        }    "
+ "        window.transparency = {            isLocationPermissionGranted: () => { return 0 },            isPAEnabled: () => { return %@ },            userTextSize: () => { return '%@' }        }    "
+ "_currentTextSizeValue"
+ "preferredContentSizeCategory"
- "        window.transparency = {            isLocationPermissionGranted: () => { return %@ },            isPAEnabled: () => { return %@ }         }    "
- "        window.transparency = {            isLocationPermissionGranted: () => { return 0 },            isPAEnabled: () => { return %@ }         }    "

```
