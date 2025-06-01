## TranslationUIServices

> `/System/Library/PrivateFrameworks/TranslationUIServices.framework/TranslationUIServices`

```diff

-249.2.0.0.0
-  __TEXT.__text: 0x35dc
+252.2.1.0.0
+  __TEXT.__text: 0x3730
   __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_methlist: 0x458
+  __TEXT.__objc_methlist: 0x478
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x204
   __TEXT.__oslogstring: 0x306
   __TEXT.__gcc_except_tab: 0x4c
   __TEXT.__unwind_info: 0x13c
   __TEXT.__objc_classname: 0xee
-  __TEXT.__objc_methname: 0x12ce
-  __TEXT.__objc_methtype: 0x20e
-  __TEXT.__objc_stubs: 0x1060
+  __TEXT.__objc_methname: 0x1384
+  __TEXT.__objc_methtype: 0x222
+  __TEXT.__objc_stubs: 0x1140
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x940
-  __DATA_CONST.__objc_selrefs: 0x538
+  __DATA_CONST.__objc_const: 0x970
+  __DATA_CONST.__objc_selrefs: 0x560
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x1f0
   __AUTH_CONST.__const: 0xc0

   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0xd0
   __DATA.__objc_superrefs: 0x18
-  __DATA.__objc_ivar: 0x4c
+  __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x188
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/Translation.framework/Translation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 32C2B8A4-3A9C-3731-AB9C-423E0E7CD882
-  Functions: 122
-  Symbols:   588
-  CStrings:  340
+  UUID: 82792871-CEB3-31EF-82FE-0BA6AEFB8F22
+  Functions: 125
+  Symbols:   602
+  CStrings:  348
 
Symbols:
+ -[LTUITranslationViewController _cleanUpExtension]
+ -[LTUITranslationViewController currentExtension]
+ -[LTUITranslationViewController setCurrentExtension:]
+ _OBJC_IVAR_$_LTUITranslationViewController._currentExtension
+ _objc_msgSend$_cleanUpExtension
+ _objc_msgSend$cancelExtensionRequestWithIdentifier:
+ _objc_msgSend$currentExtension
+ _objc_msgSend$endMatchingExtensions:
+ _objc_msgSend$matchingToken
+ _objc_msgSend$requestID
+ _objc_msgSend$setCurrentExtension:
CStrings:
+ ";"
+ "@\"<NSCopying>\""
+ "@\"NSExtension\""
+ "T@\"<NSCopying>\",&,N,V_requestID"
+ "T@\"NSExtension\",&,N,V_currentExtension"
+ "_cleanUpExtension"
+ "_currentExtension"
+ "cancelExtensionRequestWithIdentifier:"
+ "currentExtension"
+ "endMatchingExtensions:"
+ "setCurrentExtension:"
- ":"
- "@\"NSUUID\""
- "T@\"NSUUID\",&,N,V_requestID"

```
