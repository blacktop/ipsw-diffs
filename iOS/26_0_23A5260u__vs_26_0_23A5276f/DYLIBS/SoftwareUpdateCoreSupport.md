## SoftwareUpdateCoreSupport

> `/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport`

```diff

-2422.0.15.0.2
-  __TEXT.__text: 0x33e20
-  __TEXT.__auth_stubs: 0x730
+2422.0.31.502.1
+  __TEXT.__text: 0x33d68
+  __TEXT.__auth_stubs: 0x710
   __TEXT.__objc_methlist: 0x332c
-  __TEXT.__cstring: 0x7d09
+  __TEXT.__cstring: 0x7d17
   __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x68c
-  __TEXT.__oslogstring: 0x5111
-  __TEXT.__unwind_info: 0xb38
+  __TEXT.__gcc_except_tab: 0x5b8
+  __TEXT.__oslogstring: 0x50fe
+  __TEXT.__unwind_info: 0xb28
   __TEXT.__objc_classname: 0x256
   __TEXT.__objc_methname: 0xb28f
   __TEXT.__objc_methtype: 0xcf8
   __TEXT.__objc_stubs: 0x7260
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x1280
+  __DATA_CONST.__got: 0x290
+  __DATA_CONST.__const: 0x1288
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2390
   __DATA_CONST.__objc_superrefs: 0xc0
-  __AUTH_CONST.__auth_got: 0x3a8
+  __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x7d00
+  __AUTH_CONST.__cfstring: 0x7d20
   __AUTH_CONST.__objc_const: 0x4668
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8860C874-6B41-37CB-9292-D88568C73459
+  UUID: D6B1FA65-C959-3233-B39B-60F5C1CE05EC
   Functions: 1216
-  Symbols:   4370
+  Symbols:   4366
   CStrings:  4146
 
Symbols:
+ _kSUCoreControllerUsersLoggedInKey
+ _objc_retain_x7
- GCC_except_table41
- __os_activity_create
- __os_activity_current
- _os_activity_scope_enter
- _os_activity_scope_leave
Functions:
~ -[SUCoreFSM _postEvent:withInfo:] : 1068 -> 964
~ -[SUCoreFSM _triggerAction:usingAttached:onEvent:inState:withInfo:nextState:] : 484 -> 404
CStrings:
+ "UsersLoggedIn"
- "SU:Action"
- "SU:Event"

```
