## WebContentRestrictionsUI

> `/Applications/WebContentRestrictionsUI.app/WebContentRestrictionsUI`

```diff

-  __TEXT.__text: 0xc18
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_stubs: 0x4c0
-  __TEXT.__objc_methlist: 0x260
-  __TEXT.__const: 0x50
+  __TEXT.__text: 0xdb4
+  __TEXT.__auth_stubs: 0x1d0
+  __TEXT.__objc_stubs: 0x540
+  __TEXT.__objc_methlist: 0x270
+  __TEXT.__const: 0x58
   __TEXT.__objc_classname: 0x93
-  __TEXT.__objc_methname: 0x4e7
+  __TEXT.__objc_methname: 0x522
   __TEXT.__objc_methtype: 0x14a
-  __TEXT.__cstring: 0x125
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x80
-  __DATA_CONST.__cfstring: 0x160
+  __TEXT.__cstring: 0x1d6
+  __TEXT.__unwind_info: 0xc0
+  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0xa8
+  __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x270
-  __DATA.__objc_selrefs: 0x208
+  __DATA.__objc_selrefs: 0x220
   __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 40
-  Symbols:   55
-  CStrings:  117
+  Functions: 42
+  Symbols:   60
+  CStrings:  133
 
Sections:
~ __TEXT.__objc_methtype : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _OBJC_CLASS_$_OSEligibilityQuery
+ __NSConcreteStackBlock
+ _objc_opt_class
+ _objc_retain_x2
+ _objc_retain_x21
CStrings:
+ "Checking OSE criteria"
+ "Failed to open Screen Time Settings for age verification: %@"
+ "Launching ST Settings"
+ "OSE Error: %@"
+ "OSE Response: %s"
+ "_isAgeVerificationCriteriaMet"
+ "answer"
+ "eligible"
+ "ineligible"
+ "initWithDomain:error:"
+ "v20@?0B8@\"NSError\"12"

```
