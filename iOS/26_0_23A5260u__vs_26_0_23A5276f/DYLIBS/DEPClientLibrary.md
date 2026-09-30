## DEPClientLibrary

> `/System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary`

```diff

-43.0.0.0.0
-  __TEXT.__text: 0x4db4
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0x8c4
+46.0.0.0.0
+  __TEXT.__text: 0x4e50
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__objc_methlist: 0x8f4
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__cstring: 0xdab
   __TEXT.__oslogstring: 0x2b
-  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__unwind_info: 0x1d8
   __TEXT.__objc_classname: 0x12b
-  __TEXT.__objc_methname: 0x14b2
-  __TEXT.__objc_methtype: 0x500
-  __TEXT.__objc_stubs: 0xb60
+  __TEXT.__objc_methname: 0x15af
+  __TEXT.__objc_methtype: 0x526
+  __TEXT.__objc_stubs: 0xbe0
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x608
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f0
+  __DATA_CONST.__objc_selrefs: 0x510
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x1a8
+  __AUTH_CONST.__auth_got: 0x1b0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x17e0
-  __AUTH_CONST.__objc_const: 0x13c8
+  __AUTH_CONST.__objc_const: 0x1428
   __AUTH_CONST.__objc_intobj: 0x18
-  __DATA.__objc_ivar: 0x94
+  __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x180
   __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0x2d0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F3F79097-98C0-351B-BCFB-35807A52CA77
-  Functions: 159
-  Symbols:   843
-  CStrings:  686
+  UUID: 120174C1-F10F-38E9-AC5E-FB3A68BAAE74
+  Functions: 163
+  Symbols:   858
+  CStrings:  695
 
Symbols:
+ -[DEPClient eligibilityDescription]
+ -[DEPClient eligibleForMigration]
+ -[DEPClient setEligibilityDescription:]
+ -[DEPClient setEligibleForMigration:]
+ -[DEPClient syncDEPPushToken:pushTopic:eligibleForMigration:eligibilityDescription:completionBlock:]
+ _OBJC_IVAR_$_DEPClient._eligibilityDescription
+ _OBJC_IVAR_$_DEPClient._eligibleForMigration
+ ___100-[DEPClient syncDEPPushToken:pushTopic:eligibleForMigration:eligibilityDescription:completionBlock:]_block_invoke
+ _objc_msgSend$eligibilityDescription
+ _objc_msgSend$eligibleForMigration
+ _objc_msgSend$setEligibilityDescription:
+ _objc_msgSend$setEligibleForMigration:
+ _objc_msgSend$syncDEPPushToken:pushTopic:eligibleForMigration:eligibilityDescription:completionBlock:
+ _objc_retain_x6
- -[DEPClient registerForDEPPushForceUpdate:completionBlock:]
- ___56-[DEPClient syncDEPPushToken:pushTopic:completionBlock:]_block_invoke
- _objc_msgSend$syncDEPPushToken:pushTopic:completionBlock:
CStrings:
+ "B"
+ "T@\"NSString\",&,N,V_eligibilityDescription"
+ "TB,N,V_eligibleForMigration"
+ "_eligibilityDescription"
+ "_eligibleForMigration"
+ "eligibilityDescription"
+ "eligibleForMigration"
+ "setEligibilityDescription:"
+ "setEligibleForMigration:"
+ "syncDEPPushToken:pushTopic:eligibleForMigration:eligibilityDescription:completionBlock:"
+ "v20@0:8B16"
+ "v52@0:8@\"NSData\"16@\"NSString\"24B32@\"NSString\"36@?<v@?B@\"NSDictionary\"@\"NSError\">44"
+ "v52@0:8@16@24B32@36@?44"
- "\n"
- "registerForDEPPushForceUpdate:completionBlock:"
- "v28@0:8B16@?20"
- "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?B@\"NSDictionary\"@\"NSError\">32"

```
