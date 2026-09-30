## libspindump.dylib

> `/usr/lib/libspindump.dylib`

```diff

-448.0.0.0.0
-  __TEXT.__text: 0x442c
+451.0.0.0.0
+  __TEXT.__text: 0x4500
   __TEXT.__const: 0xc0
   __TEXT.__cstring: 0x500
   __TEXT.__oslogstring: 0xd72

   __TEXT.__objc_methname: 0x0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38
+  __DATA_CONST.__objc_selrefs: 0x40
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x190
   __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__auth_got: 0x1f8
+  __AUTH_CONST.__auth_got: 0x210
   __DATA.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0x128
+  __DATA_DIRTY.__bss: 0x328
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 98
-  Symbols:   207
+  Functions: 99
+  Symbols:   213
   CStrings:  124
 
Symbols:
+ _OBJC_CLASS_$_NSNumber
+ _SPStringFromInfoDictionaryValue
+ _objc_autoreleaseReturnValue
+ _objc_msgSend$stringValue
+ _objc_opt_class
+ _objc_opt_isKindOfClass
Functions:
~ ___SPNotifyLeavingFullWake_block_invoke : 40 -> 44
~ ___SPSubmitHIDTelemetry_block_invoke : 804 -> 868
+ _SPStringFromInfoDictionaryValue
```
