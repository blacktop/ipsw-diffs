## teslad

> `/usr/libexec/teslad`

```diff

-43.0.0.0.0
-  __TEXT.__text: 0xe7fc
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_stubs: 0x2580
-  __TEXT.__objc_methlist: 0x1694
+46.0.0.0.0
+  __TEXT.__text: 0xe8f0
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_stubs: 0x25e0
+  __TEXT.__objc_methlist: 0x16f4
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0x6c
-  __TEXT.__oslogstring: 0xc92
-  __TEXT.__cstring: 0x1357
-  __TEXT.__objc_classname: 0x6ac
-  __TEXT.__objc_methtype: 0xb8e
+  __TEXT.__oslogstring: 0xc63
+  __TEXT.__cstring: 0x137c
+  __TEXT.__objc_classname: 0x6ae
+  __TEXT.__objc_methtype: 0xbb6
   __TEXT.__dlopen_cstrs: 0xaa
-  __TEXT.__objc_methname: 0x2d43
+  __TEXT.__objc_methname: 0x2e32
   __TEXT.__unwind_info: 0x3d0
-  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0x808
-  __DATA_CONST.__cfstring: 0x1da0
+  __DATA_CONST.__const: 0x810
+  __DATA_CONST.__cfstring: 0x1dc0
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0xf0
-  __DATA.__objc_const: 0x3a08
-  __DATA.__objc_selrefs: 0xb98
-  __DATA.__objc_ivar: 0xf4
+  __DATA.__objc_const: 0x3ac8
+  __DATA.__objc_selrefs: 0xbb0
+  __DATA.__objc_ivar: 0x104
   __DATA.__objc_data: 0x1040
   __DATA.__data: 0x240
   __DATA.__bss: 0xc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F38126C7-DA10-3BA3-ABA8-947F5699714F
-  Functions: 410
-  Symbols:   187
-  CStrings:  1192
+  UUID: 738146CA-FE00-3A42-BCCA-59F943971E1C
+  Functions: 418
+  Symbols:   188
+  CStrings:  1201
 
Symbols:
+ _objc_retain_x6
CStrings:
+ "T@\"NSString\",&,N,V_eligibilityDescription"
+ "TB,N,V_eligibleForMigration"
+ "_eligibilityDescription"
+ "_eligibleForMigration"
+ "eligibilityDescription"
+ "eligibleForMigration"
+ "mdm_migration_capability_description"
+ "setEligibilityDescription:"
+ "setEligibleForMigration:"
+ "syncDEPPushToken:pushTopic:eligibleForMigration:eligibilityDescription:completionBlock:"
+ "v52@0:8@\"NSData\"16@\"NSString\"24B32@\"NSString\"36@?<v@?B@\"NSDictionary\"@\"NSError\">44"
+ "v52@0:8@16@24B32@36@?44"
- "DEPPush feature flag is not enabled. Return..."
- "isDEPPushEnabled"
- "syncDEPPushToken:pushTopic:completionBlock:"
- "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?B@\"NSDictionary\"@\"NSError\">32"

```
