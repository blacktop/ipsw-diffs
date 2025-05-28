## IntlPreferencesUI

> `/System/Library/PrivateFrameworks/IntlPreferencesUI.framework/IntlPreferencesUI`

```diff

-435.201.0.0.0
-  __TEXT.__text: 0x57a4
-  __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_methlist: 0x610
+435.305.0.0.0
+  __TEXT.__text: 0x5954
+  __TEXT.__auth_stubs: 0x270
+  __TEXT.__objc_methlist: 0x630
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x269
+  __TEXT.__cstring: 0x297
   __TEXT.__unwind_info: 0x170
   __TEXT.__objc_classname: 0xc7
-  __TEXT.__objc_methname: 0x205d
+  __TEXT.__objc_methname: 0x20df
   __TEXT.__objc_methtype: 0x3f2
-  __TEXT.__objc_stubs: 0x1e80
+  __TEXT.__objc_stubs: 0x1ee0
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xac0
-  __DATA_CONST.__objc_selrefs: 0x888
+  __DATA_CONST.__objc_const: 0xaf0
+  __DATA_CONST.__objc_selrefs: 0x8a8
+  __DATA_CONST.__objc_classrefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x170
-  __AUTH_CONST.__cfstring: 0x7e0
+  __AUTH_CONST.__cfstring: 0x800
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_const: 0x280
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x138
+  __AUTH_CONST.__auth_got: 0x140
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_classrefs: 0x128
-  __DATA.__objc_superrefs: 0x20
-  __DATA.__objc_ivar: 0x68
+  __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 125
-  Symbols:   689
-  CStrings:  488
+  Functions: 128
+  Symbols:   700
+  CStrings:  498
 
Symbols:
+ -[IPPronounValidator _clearUserEntries]
+ -[IPPronounValidator autofillPronouns:]
+ -[IPPronounValidator knownPronouns]
+ -[IPPronounValidator setKnownPronouns:]
+ _OBJC_IVAR_$_IPPronounValidator._knownPronouns
+ __os_feature_enabled_impl
+ __unnamed_array_storage.170
+ __unnamed_array_storage.58
+ __unnamed_array_storage.66
+ __unnamed_array_storage.67
+ __unnamed_array_storage.79
+ __unnamed_array_storage.80
+ _objc_msgSend$autofillPronouns:
+ _objc_msgSend$knownPronouns
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$setKnownPronouns:
- -[IPPronounValidator fillInRememberedPronouns:]
- __unnamed_array_storage.165
- __unnamed_array_storage.55
- __unnamed_array_storage.63
- __unnamed_array_storage.64
- __unnamed_array_storage.76
- __unnamed_array_storage.77
- _objc_msgSend$fillInRememberedPronouns:
CStrings:
+ "\x01\x17"
+ "IntlPreferences"
+ "KnownPronouns"
+ "PronounAutofill"
+ "T@\"NSArray\",&,N,V_knownPronouns"
+ "T@\"NSString\",?,R,C"
+ "_clearUserEntries"
+ "_knownPronouns"
+ "autofillPronouns:"
+ "knownPronouns"
+ "removeObjectForKey:"
+ "setKnownPronouns:"
- "\x01\x16"
- "fillInRememberedPronouns:"

```
