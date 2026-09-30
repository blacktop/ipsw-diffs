## parentalcontrolsd

> `/System/Library/PrivateFrameworks/FamilyControls.framework/Versions/A/Resources/parentalcontrolsd`

```diff

-127.0.0.0.0
-  __TEXT.__text: 0x2b474
-  __TEXT.__auth_stubs: 0xc70
+129.0.0.0.0
+  __TEXT.__text: 0x2bf08
+  __TEXT.__auth_stubs: 0xca0
   __TEXT.__objc_stubs: 0x2b40
-  __TEXT.__objc_methlist: 0xaa4
+  __TEXT.__objc_methlist: 0xc44
   __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x2140
-  __TEXT.__cstring: 0x3097
-  __TEXT.__oslogstring: 0x44c0
+  __TEXT.__gcc_except_tab: 0x2148
+  __TEXT.__cstring: 0x30ba
+  __TEXT.__oslogstring: 0x459a
   __TEXT.__objc_methname: 0x250b
   __TEXT.__objc_classname: 0x122
   __TEXT.__objc_methtype: 0x4ef
   __TEXT.__unwind_info: 0x760
-  __DATA_CONST.__auth_got: 0x648
-  __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__auth_got: 0x660
+  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x6f8
-  __DATA_CONST.__cfstring: 0x1f80
+  __DATA_CONST.__cfstring: 0x1fa0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0x16e8
-  __DATA.__objc_selrefs: 0xc30
+  __DATA.__objc_const: 0x13e0
+  __DATA.__objc_selrefs: 0xcf0
   __DATA.__objc_ivar: 0x148
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x128

   - /System/Library/PrivateFrameworks/SystemAdministration.framework/Versions/A/SystemAdministration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0424CCD0-81C2-35A0-8A11-8E5ABF78A3C6
-  Functions: 822
-  Symbols:   328
-  CStrings:  1792
+  UUID: B353E986-B827-305C-B8B3-3AD47D1717FF
+  Functions: 828
+  Symbols:   331
+  CStrings:  1797
 
Symbols:
+ _CFEqual
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
CStrings:
+ "%s -- failed to copy value for entitlement %@: Error: %@"
+ "%s -- must be properly entitled to request data. caller uid = %d. user uid = %d"
+ "%s -- unable to create the security task needed to check for proper entitlements"
+ "com.apple.private.parentalcontrols"

```
