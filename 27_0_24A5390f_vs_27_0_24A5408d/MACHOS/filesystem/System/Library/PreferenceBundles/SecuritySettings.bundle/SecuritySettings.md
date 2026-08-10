## SecuritySettings

> `/System/Library/PreferenceBundles/SecuritySettings.bundle/SecuritySettings`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1171.0.3.0.0
-  __TEXT.__text: 0x85b0
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_stubs: 0x1fe0
-  __TEXT.__objc_methlist: 0xa44
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x705
-  __TEXT.__oslogstring: 0x5d4
-  __TEXT.__objc_methname: 0x2504
+1171.0.12.0.0
+  __TEXT.__text: 0x92b4
+  __TEXT.__auth_stubs: 0x490
+  __TEXT.__objc_stubs: 0x21c0
+  __TEXT.__objc_methlist: 0xa74
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x747
+  __TEXT.__oslogstring: 0x63f
+  __TEXT.__objc_methname: 0x2634
   __TEXT.__objc_classname: 0x11f
   __TEXT.__objc_methtype: 0x59a
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x250
-  __DATA_CONST.__const: 0x310
-  __DATA_CONST.__cfstring: 0x7c0
+  __TEXT.__unwind_info: 0x270
+  __DATA_CONST.__const: 0x360
+  __DATA_CONST.__cfstring: 0x800
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x260
-  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0x2a8
   __DATA.__objc_const: 0x1080
-  __DATA.__objc_selrefs: 0xbc8
+  __DATA.__objc_selrefs: 0xc40
   __DATA.__objc_ivar: 0x94
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x2b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 166
+  Functions: 177
   Symbols:   192
-  CStrings:  628
+  CStrings:  649
 
Symbols:
+ _OBJC_CLASS_$_LAContext
+ _objc_retain_x9
- _objc_retain_x25
- _objc_retain_x26
CStrings:
+ "Developer Mode DPO error: %@"
+ "Refusing to unpair specifier with missing hostKey or identifiers; userInfo=%@"
+ "allRecordIdentifiers"
+ "animateWithDuration:animations:"
+ "backBarButtonItem"
+ "compare:"
+ "evaluatePolicy:options:reply:"
+ "hostKey"
+ "hostKeyForRecord:"
+ "mergedUserInfoForRecords:hostKey:"
+ "mutableCopy"
+ "performDPOCheckWithCallback:onCancel:"
+ "q"
+ "setAlpha:"
+ "setDeveloperModeUIEnabled:"
+ "setEnabled:"
+ "setHidesBackButton:"
+ "setUserInteractionEnabled:"
+ "setWithArray:"
+ "specifierForPairedHost:hostKey:withUserInfo:"
+ "table"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "specifierForPairedHost:identifier:withUserInfo:"
```
