## AADataclassEnableNotificationPlugin

> `/System/Library/Accounts/Notification/AADataclassEnableNotificationPlugin.bundle/AADataclassEnableNotificationPlugin`

```diff

-1002.0.0.0.0
-  __TEXT.__text: 0x43e8
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0x268
+1005.0.0.0.0
+  __TEXT.__text: 0x4488
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__objc_methlist: 0x280
   __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x506
-  __TEXT.__oslogstring: 0x686
-  __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__unwind_info: 0x148
+  __TEXT.__cstring: 0x529
+  __TEXT.__oslogstring: 0x6cd
+  __TEXT.__gcc_except_tab: 0xb0
+  __TEXT.__unwind_info: 0x150
   __TEXT.__objc_classname: 0x9a
-  __TEXT.__objc_methname: 0xdaf
-  __TEXT.__objc_methtype: 0x253
-  __TEXT.__objc_stubs: 0xbc0
-  __DATA_CONST.__got: 0x1e8
+  __TEXT.__objc_methname: 0xe08
+  __TEXT.__objc_methtype: 0x25e
+  __TEXT.__objc_stubs: 0xbe0
+  __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0x170
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x380
+  __DATA_CONST.__objc_selrefs: 0x398
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x190
+  __AUTH_CONST.__auth_got: 0x1b0
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x540
-  __AUTH_CONST.__objc_const: 0x798
+  __AUTH_CONST.__objc_const: 0x7b0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 80
-  Symbols:   123
-  CStrings:  268
+  Functions: 83
+  Symbols:   129
+  CStrings:  275
 
Symbols:
+ _AASignInErrorDomain
+ _OBJC_CLASS_$_NSError
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_release_x28
+ _objc_retain_x22
+ _objc_retain_x28
- _objc_release_x27
- _objc_retain_x25
- _objc_retain_x27
CStrings:
+ "AADataclassManager failed to maintain ref to self."
+ "Account save with dataclass actions had success (%!@(MISSING)) for account (%!@(MISSING)) with dataclass actions: %!@(MISSING)"
+ "Encountered error when saving with dataclass actions: %!@(MISSING)"
+ "T@\"ACAccountStore\",&,N,V_store"
+ "Unable to build list of dataclasses and actions for enablement %!@(MISSING)"
+ "_buildAutoEnableableDataclassesAndActionsForAccount:dataclassesForEnablement:completion:"
+ "errorWithDomain:code:userInfo:"
+ "setStore:"
+ "store"
+ "v24@0:8@16"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "Failed to save account with dataclasses enabled, error: %!@(MISSING)"
- "Successfully enabled dataclasses for account (%!@(MISSING)) with dataclass actions: %!@(MISSING)"
- "Unable to build list of dataclasses and actions for enablement."
- "_buildAutoEnableableDataclassesAndActionsForAccount:dataclassesForEnablement:"

```
