## AppServerSupport

> `/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-3298.2.1.0.0
-  __TEXT.__text: 0x7aec
-  __TEXT.__objc_methlist: 0xb2c
-  __TEXT.__const: 0x80
+3298.40.20.0.0
+  __TEXT.__text: 0x7bac
+  __TEXT.__objc_methlist: 0xb54
+  __TEXT.__const: 0x88
   __TEXT.__cstring: 0x63c
   __TEXT.__oslogstring: 0xdd6
   __TEXT.__unwind_info: 0x240

   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x680
+  __DATA_CONST.__objc_selrefs: 0x690
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__got: 0xc8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x580
-  __AUTH_CONST.__objc_const: 0x1840
+  __AUTH_CONST.__objc_const: 0x1870
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x120
+  __DATA.__objc_ivar: 0x124
   __DATA.__data: 0x1e0
   __DATA.__crash_info: 0x148
   __DATA_DIRTY.__objc_data: 0x2d0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 200
-  Symbols:   604
+  Functions: 203
+  Symbols:   610
   CStrings:  177
 
Symbols:
+ +[OSLaunchdJob _createSubmitExtensionRequest:overlay:domain:properties:]
+ +[OSLaunchdJob _submitExtension:overlay:domain:properties:error:]
+ -[OSLaunchdJobProperties label]
+ -[OSLaunchdJobProperties setLabel:]
+ _OBJC_IVAR_$_OSLaunchdJobProperties._label
+ _objc_msgSend$_createSubmitExtensionRequest:overlay:domain:properties:
+ _objc_msgSend$_submitExtension:overlay:domain:properties:error:
+ _objc_msgSend$label
- +[OSLaunchdJob _submitExtension:overlay:domain:error:]
- _objc_msgSend$_submitExtension:overlay:domain:error:
```
