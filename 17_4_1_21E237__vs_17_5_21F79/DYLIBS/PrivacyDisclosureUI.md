## PrivacyDisclosureUI

> `/System/Library/PrivateFrameworks/PrivacyDisclosureUI.framework/PrivacyDisclosureUI`

```diff

-42.0.0.0.0
-  __TEXT.__text: 0x49a0
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x2c4
+45.0.0.0.0
+  __TEXT.__text: 0x4d94
+  __TEXT.__auth_stubs: 0x400
+  __TEXT.__objc_methlist: 0x324
   __TEXT.__const: 0x70
   __TEXT.__cstring: 0x434
   __TEXT.__oslogstring: 0x94
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x18c
-  __TEXT.__objc_classname: 0x117
-  __TEXT.__objc_methname: 0x2154
-  __TEXT.__objc_methtype: 0xb30
-  __TEXT.__objc_stubs: 0x15e0
-  __DATA_CONST.__got: 0x58
+  __TEXT.__unwind_info: 0x19c
+  __TEXT.__objc_classname: 0x11c
+  __TEXT.__objc_methname: 0x236e
+  __TEXT.__objc_methtype: 0xb40
+  __TEXT.__objc_stubs: 0x1820
+  __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x17b8
-  __DATA_CONST.__objc_selrefs: 0x618
+  __DATA_CONST.__objc_const: 0x1818
+  __DATA_CONST.__objc_selrefs: 0x6b0
   __DATA_CONST.__objc_classrefs: 0x130
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x80

   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_const: 0x230
-  __AUTH_CONST.__auth_got: 0x1f0
+  __AUTH_CONST.__auth_got: 0x210
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x44
+  __DATA.__objc_ivar: 0x4c
   __DATA.__data: 0x240
   __DATA.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 93
-  Symbols:   573
-  CStrings:  495
+  Functions: 100
+  Symbols:   613
+  CStrings:  520
 
Symbols:
+ -[PDUWelcomeViewController_iOS _updateContinueButtonConfiguration]
+ -[PDUWelcomeViewController_iOS continueButtonOriginalTextColor]
+ -[PDUWelcomeViewController_iOS continueButton]
+ -[PDUWelcomeViewController_iOS setContinueButton:]
+ -[PDUWelcomeViewController_iOS setContinueButtonOriginalTextColor:]
+ -[PDUWelcomeViewController_iOS traitCollectionDidChange:]
+ -[UIColor(PDUExtras) convertedToRGB]
+ _CGColorCreateCopyByMatchingToColorSpace
+ _CGColorRelease
+ _CGColorSpaceCreateWithName
+ _CGColorSpaceRelease
+ _OBJC_IVAR_$_PDUWelcomeViewController_iOS._continueButton
+ _OBJC_IVAR_$_PDUWelcomeViewController_iOS._continueButtonOriginalTextColor
+ __OBJC_$_INSTANCE_METHODS_UIColor(PDUExtras)
+ _kCGColorSpaceGenericRGB
+ _objc_msgSend$CGColor
+ _objc_msgSend$_updateContinueButtonConfiguration
+ _objc_msgSend$baseForegroundColor
+ _objc_msgSend$blackColor
+ _objc_msgSend$configuration
+ _objc_msgSend$continueButton
+ _objc_msgSend$continueButtonOriginalTextColor
+ _objc_msgSend$convertedToRGB
+ _objc_msgSend$hasDifferentColorAppearanceComparedToTraitCollection:
+ _objc_msgSend$initWithCGColor:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$setBaseForegroundColor:
+ _objc_msgSend$setConfiguration:
+ _objc_msgSend$setContinueButton:
+ _objc_msgSend$setContinueButtonOriginalTextColor:
+ _objc_msgSend$setNeedsUpdateConfiguration
+ _objc_msgSend$textColor
+ _objc_msgSend$traitCollection
CStrings:
+ "\x03!"
+ "2"
+ "@\"OBTrayButton\""
+ "CGColor"
+ "T@\"OBTrayButton\",W,N,V_continueButton"
+ "T@\"UIColor\",&,N,V_continueButtonOriginalTextColor"
+ "_continueButton"
+ "_continueButtonOriginalTextColor"
+ "_updateContinueButtonConfiguration"
+ "baseForegroundColor"
+ "blackColor"
+ "configuration"
+ "continueButton"
+ "continueButtonOriginalTextColor"
+ "convertedToRGB"
+ "hasDifferentColorAppearanceComparedToTraitCollection:"
+ "initWithCGColor:"
+ "setBaseForegroundColor:"
+ "setConfiguration:"
+ "setContinueButton:"
+ "setContinueButtonOriginalTextColor:"
+ "setNeedsUpdateConfiguration"
+ "textColor"
+ "traitCollection"
+ "traitCollectionDidChange:"

```
