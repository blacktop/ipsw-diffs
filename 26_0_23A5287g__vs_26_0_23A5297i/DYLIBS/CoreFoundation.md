## CoreFoundation

> `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

```diff

-4034.1.101.0.0
-  __TEXT.__text: 0x1bdd40
+4037.0.0.0.0
+  __TEXT.__text: 0x1be528
   __TEXT.__auth_stubs: 0x31e0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x7a34
-  __TEXT.__const: 0x1a1718
-  __TEXT.__oslogstring: 0x5819
-  __TEXT.__cstring: 0x14b20d
-  __TEXT.__gcc_except_tab: 0x44c8
+  __TEXT.__objc_methlist: 0x7a5c
+  __TEXT.__const: 0x1a1728
+  __TEXT.__oslogstring: 0x58d8
+  __TEXT.__cstring: 0x14b29f
+  __TEXT.__gcc_except_tab: 0x454c
   __TEXT.__ustring: 0x484
   __TEXT.__dof_CFRunLoop: 0x964
   __TEXT.__dof_Cocoa_Aut: 0x486
-  __TEXT.__unwind_info: 0x5c90
+  __TEXT.__unwind_info: 0x5ca0
   __TEXT.__eh_frame: 0x588
   __TEXT.__objc_classname: 0xa9a
-  __TEXT.__objc_methname: 0x8323
-  __TEXT.__objc_methtype: 0xb399d
-  __TEXT.__objc_stubs: 0x6060
+  __TEXT.__objc_methname: 0x8370
+  __TEXT.__objc_methtype: 0xb399f
+  __TEXT.__objc_stubs: 0x60c0
   __DATA_CONST.__got: 0x490
-  __DATA_CONST.__const: 0x37d6a0
+  __DATA_CONST.__const: 0x37d6c0
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_nlclslist: 0x58
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2738
+  __DATA_CONST.__objc_selrefs: 0x2750
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x16e0
   __AUTH_CONST.__auth_got: 0x1908
   __AUTH_CONST.__const: 0x4d68
-  __AUTH_CONST.__cfstring: 0x141420
-  __AUTH_CONST.__objc_const: 0x9ac8
+  __AUTH_CONST.__cfstring: 0x1414c0
+  __AUTH_CONST.__objc_const: 0x9ad8
   __AUTH_CONST.__const_cfobj2: 0x40
   __AUTH_CONST.__objc_dictobj: 0x7f8
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 44CF748C-19F2-31C4-A0F1-143E32768AF1
-  Functions: 7991
-  Symbols:   20450
-  CStrings:  100955
+  UUID: 27A19959-D869-369B-8D48-616914C3AE25
+  Functions: 7997
+  Symbols:   20468
+  CStrings:  100973
 
Symbols:
+ -[CFPrefsSource validateValue:forKey:inDict:forWriting:]
+ -[NSDateComponents isRepeatedDaySet]
+ -[NSDateComponents isRepeatedDay]
+ -[NSDateComponents setRepeatedDay:]
+ GCC_except_table83
+ GCC_except_table95
+ _CFDateComponentsIsRepeatedDay
+ _CFDateComponentsIsRepeatedDaySet
+ ___CFRunLoopObserverWithHandlerPerform
+ ___block_descriptor_tmp.376
+ ___block_literal_global.191
+ __kCFURLDirectoryHasVisibleContentKey
+ __kCFURLIconEmojiKey
+ __kCFURLIconSymbolNameKey
+ __kCFURLTagColorIndexKey
+ _objc_msgSend$isRepeatedDay
+ _objc_msgSend$isRepeatedDaySet
+ _objc_msgSend$setRepeatedDay:
- GCC_except_table70
- GCC_except_table74
- ___block_descriptor_tmp.375
- ___block_literal_global.187
- __runLoopObserverWithBlockContext
CStrings:
+ "\n    Repeated Day: %ld"
+ "@24@0:8^{__CFDateComponents={__CFRuntimeBase=QAQ}^{__CFCalendar}^{__CFTimeZone}qqqqqqqqqqqqqqqqqq}16"
+ "TB,GisRepeatedDay"
+ "UCAL_IS_REPEATED_DAY"
+ "^{__CFDateComponents={__CFRuntimeBase=QAQ}^{__CFCalendar}^{__CFTimeZone}qqqqqqqqqqqqqqqqqq}16@0:8"
+ "_NSURLDirectoryHasVisibleContentKey"
+ "_NSURLIconEmojiKey"
+ "_NSURLIconSymbolNameKey"
+ "_NSURLTagColorIndexKey"
+ "attempted to write invalid value %{private}@ for key %{public}@ in %{public}@. Replacing with NULL."
+ "isRepeatedDay"
+ "isRepeatedDaySet"
+ "looked up invalid value %{private}@ for key %{public}@ in %{public}@. Replacing with NULL."
+ "repeatedDay"
+ "setRepeatedDay:"
- "@24@0:8^{__CFDateComponents={__CFRuntimeBase=QAQ}^{__CFCalendar}^{__CFTimeZone}qqqqqqqqqqqqqqqqq}16"
- "^{__CFDateComponents={__CFRuntimeBase=QAQ}^{__CFCalendar}^{__CFTimeZone}qqqqqqqqqqqqqqqqq}16@0:8"

```
