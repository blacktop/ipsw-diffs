## securityd

> `/usr/libexec/securityd`

```diff

-61439.40.54.0.0
-  __TEXT.__text: 0x22f4fc
+61439.42.1.0.1
+  __TEXT.__text: 0x22f5f0
   __TEXT.__auth_stubs: 0x38c0
-  __TEXT.__objc_stubs: 0x1a520
-  __TEXT.__objc_methlist: 0x1295c
+  __TEXT.__objc_stubs: 0x1a540
+  __TEXT.__objc_methlist: 0x12974
   __TEXT.__const: 0x8cd
-  __TEXT.__cstring: 0x203d8
+  __TEXT.__cstring: 0x203f2
   __TEXT.__oslogstring: 0x28d78
   __TEXT.__gcc_except_tab: 0xac5c
   __TEXT.__objc_classname: 0x22ba
-  __TEXT.__objc_methname: 0x292b6
-  __TEXT.__objc_methtype: 0x9885
+  __TEXT.__objc_methname: 0x2937c
+  __TEXT.__objc_methtype: 0x9927
   __TEXT.__dlopen_cstrs: 0x2c4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6280
+  __TEXT.__unwind_info: 0x6288
   __DATA_CONST.__auth_got: 0x1c70
   __DATA_CONST.__got: 0xdd0
   __DATA_CONST.__auth_ptr: 0x20

   __DATA_CONST.__objc_arraydata: 0x3d8
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x23648
-  __DATA.__objc_selrefs: 0x8790
-  __DATA.__objc_ivar: 0x1864
+  __DATA.__objc_const: 0x23698
+  __DATA.__objc_selrefs: 0x87a0
+  __DATA.__objc_ivar: 0x186c
   __DATA.__objc_data: 0x5500
   __DATA.__data: 0x20b8
   __DATA.__thread_vars: 0xd8

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9094
+  Functions: 9096
   Symbols:   1373
-  CStrings:  15240
+  CStrings:  15248
 
CStrings:
+ "-[CuttlefishXPCWrapper performCKServerUnreadableDataRemovalWithSpecificUser:isGuitarfish:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper resetWithSpecificUser:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:internalAccount:demoAccount:isGuitarfish:reply:]_block_invoke"
+ "@96@0:8@16@24q32@40@48B56B60@64@72@80@88"
+ "TB,V_isGuitarfish"
+ "_isGuitarfish"
+ "clearCliqueFromAccount:resetReason:isGuitarfish:reply:"
+ "init:contextID:reason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:isGuitarfish:intendedState:dependencies:errorState:cuttlefishXPCWrapper:"
+ "isGuitarfish"
+ "performCKServerUnreadableDataRemoval:isGuitarfish:reply:"
+ "performCKServerUnreadableDataRemovalWithSpecificUser:isGuitarfish:reply:"
+ "resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:reply:"
+ "resetAndEstablish:resetReason:isGuitarfish:reply:"
+ "resetWithSpecificUser:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:internalAccount:demoAccount:isGuitarfish:reply:"
+ "rpcReset:isGuitarfish:reply:"
+ "rpcResetAndEstablish:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:reply:"
+ "rpcResetAndEstablish:isGuitarfish:reply:"
+ "setIsGuitarfish:"
+ "v36@0:8@\"OTControlArguments\"16B24@?<v@?@\"NSError\">28"
+ "v36@0:8@\"TPSpecificUser\"16B24@?<v@?@\"NSError\">28"
+ "v36@0:8q16B24@?28"
+ "v44@0:8@\"OTControlArguments\"16q24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@16q24B32@?36"
+ "v64@0:8q16@24@32B40@44B52@?56"
+ "v72@0:8@\"OTControlArguments\"16q24@\"NSString\"32@\"NSString\"40B48@\"OTAccountSettings\"52B60@?<v@?@\"NSError\">64"
+ "v72@0:8@\"TPSpecificUser\"16q24@\"NSString\"32@\"NSString\"40B48B52B56B60@?<v@?@\"NSError\">64"
+ "v72@0:8@16q24@32@40B48@52B60@?64"
+ "v72@0:8@16q24@32@40B48B52B56B60@?64"
- "-[CuttlefishXPCWrapper performCKServerUnreadableDataRemovalWithSpecificUser:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper resetWithSpecificUser:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:internalAccount:demoAccount:reply:]_block_invoke"
- "@92@0:8@16@24q32@40@48B56@60@68@76@84"
- "clearCliqueFromAccount:resetReason:reply:"
- "init:contextID:reason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:intendedState:dependencies:errorState:cuttlefishXPCWrapper:"
- "performCKServerUnreadableDataRemoval:"
- "performCKServerUnreadableDataRemovalWithSpecificUser:reply:"
- "resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:reply:"
- "resetAndEstablish:resetReason:reply:"
- "resetWithSpecificUser:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:internalAccount:demoAccount:reply:"
- "rpcReset:reply:"
- "rpcResetAndEstablish:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:reply:"
- "rpcResetAndEstablish:reply:"
- "v40@0:8@\"OTControlArguments\"16q24@?<v@?@\"NSError\">32"
- "v60@0:8q16@24@32B40@44@?52"
- "v68@0:8@\"OTControlArguments\"16q24@\"NSString\"32@\"NSString\"40B48@\"OTAccountSettings\"52@?<v@?@\"NSError\">60"
- "v68@0:8@\"TPSpecificUser\"16q24@\"NSString\"32@\"NSString\"40B48B52B56@?<v@?@\"NSError\">60"
- "v68@0:8@16q24@32@40B48@52@?60"
- "v68@0:8@16q24@32@40B48B52B56@?60"

```
