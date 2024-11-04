## securityd

> `/usr/libexec/securityd`

```diff

-61439.60.91.502.1
-  __TEXT.__text: 0x22fcec
+61439.60.107.0.0
+  __TEXT.__text: 0x230408
   __TEXT.__auth_stubs: 0x38c0
-  __TEXT.__objc_stubs: 0x1a460
-  __TEXT.__objc_methlist: 0x128c4
-  __TEXT.__const: 0x8d5
-  __TEXT.__cstring: 0x1f896
-  __TEXT.__oslogstring: 0x28ee9
+  __TEXT.__objc_stubs: 0x1a4a0
+  __TEXT.__objc_methlist: 0x128dc
+  __TEXT.__const: 0x8cd
+  __TEXT.__cstring: 0x1f8fc
+  __TEXT.__oslogstring: 0x29028
   __TEXT.__gcc_except_tab: 0xac90
-  __TEXT.__objc_classname: 0x2283
-  __TEXT.__objc_methname: 0x291e5
-  __TEXT.__objc_methtype: 0x995f
+  __TEXT.__objc_classname: 0x2284
+  __TEXT.__objc_methname: 0x29279
+  __TEXT.__objc_methtype: 0x99a9
   __TEXT.__dlopen_cstrs: 0x1c8
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6200
+  __TEXT.__unwind_info: 0x6208
   __DATA_CONST.__auth_got: 0x1c70
   __DATA_CONST.__got: 0x1040
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x13080
-  __DATA_CONST.__cfstring: 0x1a580
+  __DATA_CONST.__cfstring: 0x1a5c0
   __DATA_CONST.__objc_classlist: 0x870
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x210

   __DATA_CONST.__objc_arraydata: 0x3d8
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x234a8
-  __DATA.__objc_selrefs: 0x8738
-  __DATA.__objc_ivar: 0x1854
+  __DATA.__objc_const: 0x234f8
+  __DATA.__objc_selrefs: 0x8750
+  __DATA.__objc_ivar: 0x185c
   __DATA.__objc_data: 0x5460
   __DATA.__data: 0x20b8
   __DATA.__thread_vars: 0xd8

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9062
+  Functions: 9064
   Symbols:   1451
-  CStrings:  15132
+  CStrings:  15145
 
CStrings:
+ "\x02\x12\x15"
+ "\x03\x12\x11?\x0f\r"
+ "-[CuttlefishXPCWrapper performCKServerUnreadableDataRemovalWithSpecificUser:isGuitarfish:internalAccount:demoAccount:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper resetWithSpecificUser:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:internalAccount:demoAccount:isGuitarfish:accountType:reply:]_block_invoke"
+ "@104@0:8@16@24q32@40@48B56B60q64@72@80@88@96"
+ "AuthKit Account Manager is nil"
+ "Have incoming classA items needing processing, but device is locked"
+ "Primary Authkit Account is nil"
+ "Requesting incoming processing for %!@(MISSING)"
+ "Tq,V_accountType"
+ "_accountType"
+ "accountType"
+ "init:contextID:reason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:isGuitarfish:accountType:intendedState:dependencies:errorState:cuttlefishXPCWrapper:"
+ "octagon-perform-ckserver-unreadable-data-removal, AuthKit Account Manager is nil"
+ "octagon-perform-ckserver-unreadable-data-removal, Primary Authkit Account is nil"
+ "octagon-perform-ckserver-unreadable-data-removal: failed to fetch demo account flag: %!@(MISSING)"
+ "performCKServerUnreadableDataRemoval:altDSID:reply:"
+ "performCKServerUnreadableDataRemoval:isGuitarfish:altDSID:reply:"
+ "performCKServerUnreadableDataRemovalWithSpecificUser:isGuitarfish:internalAccount:demoAccount:reply:"
+ "primaryAuthKitAccount"
+ "resetWithSpecificUser:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:internalAccount:demoAccount:isGuitarfish:accountType:reply:"
+ "setAccountType:"
+ "v44@0:8@\"OTControlArguments\"16B24@\"NSString\"28@?<v@?@\"NSError\">36"
+ "v44@0:8@\"TPSpecificUser\"16B24B28B32@?<v@?@\"NSError\">36"
+ "v44@0:8@16B24@28@?36"
+ "v44@0:8@16B24B28B32@?36"
+ "v80@0:8@\"TPSpecificUser\"16q24@\"NSString\"32@\"NSString\"40B48B52B56B60q64@?<v@?@\"NSError\">72"
+ "v80@0:8@16q24@32@40B48B52B56B60q64@?72"
- "\x02\x17"
- "\x03\x12\x11\x1f\x0f\r"
- "-[CuttlefishXPCWrapper performCKServerUnreadableDataRemovalWithSpecificUser:isGuitarfish:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper resetWithSpecificUser:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:internalAccount:demoAccount:isGuitarfish:reply:]_block_invoke"
- "@96@0:8@16@24q32@40@48B56B60@64@72@80@88"
- "Beginning incoming processing for %!@(MISSING)"
- "init:contextID:reason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:isGuitarfish:intendedState:dependencies:errorState:cuttlefishXPCWrapper:"
- "performCKServerUnreadableDataRemoval:isGuitarfish:reply:"
- "performCKServerUnreadableDataRemoval:reply:"
- "performCKServerUnreadableDataRemovalWithSpecificUser:isGuitarfish:reply:"
- "resetWithSpecificUser:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:internalAccount:demoAccount:isGuitarfish:reply:"
- "v36@0:8@\"OTControlArguments\"16B24@?<v@?@\"NSError\">28"
- "v36@0:8@\"TPSpecificUser\"16B24@?<v@?@\"NSError\">28"
- "v72@0:8@\"TPSpecificUser\"16q24@\"NSString\"32@\"NSString\"40B48B52B56B60@?<v@?@\"NSError\">64"
- "v72@0:8@16q24@32@40B48B52B56B60@?64"

```
