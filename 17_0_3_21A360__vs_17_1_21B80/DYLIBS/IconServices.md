## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

```diff

-597.1.0.0.0
-  __TEXT.__text: 0x3874c
-  __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0x40dc
+597.5.2.1.0
+  __TEXT.__text: 0x38fdc
+  __TEXT.__auth_stubs: 0xa50
+  __TEXT.__objc_methlist: 0x4144
   __TEXT.__const: 0x3e4
   __TEXT.__gcc_except_tab: 0x384
-  __TEXT.__cstring: 0x3056
-  __TEXT.__oslogstring: 0x2312
-  __TEXT.__unwind_info: 0xfa4
+  __TEXT.__cstring: 0x30eb
+  __TEXT.__oslogstring: 0x234e
+  __TEXT.__unwind_info: 0xfbc
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0xb3e
-  __TEXT.__objc_methname: 0x7e84
-  __TEXT.__objc_methtype: 0x1057
-  __TEXT.__objc_stubs: 0x69a0
+  __TEXT.__objc_classname: 0xb48
+  __TEXT.__objc_methname: 0x7f78
+  __TEXT.__objc_methtype: 0x107a
+  __TEXT.__objc_stubs: 0x6ae0
   __DATA_CONST.__got: 0x208
   __DATA_CONST.__const: 0x7b0
-  __DATA_CONST.__objc_classlist: 0x358
+  __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9c68
-  __DATA_CONST.__objc_selrefs: 0x21e8
+  __DATA_CONST.__objc_const: 0x9d40
+  __DATA_CONST.__objc_selrefs: 0x2238
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__cfstring: 0x2e60
-  __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__cfstring: 0x2ee0
+  __AUTH_CONST.__objc_const: 0x48
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x530
+  __AUTH_CONST.__auth_got: 0x540
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x4b0
-  __DATA.__objc_superrefs: 0x260
-  __DATA.__objc_ivar: 0x3dc
+  __DATA.__objc_classrefs: 0x4b8
+  __DATA.__objc_superrefs: 0x268
+  __DATA.__objc_ivar: 0x3e4
   __DATA.__data: 0x1828
   __DATA.__bss: 0x4b0
-  __DATA_DIRTY.__const: 0xde0
+  __DATA_DIRTY.__const: 0xdc0
   __DATA_DIRTY.__objc_const: 0x2f58
   __DATA_DIRTY.__objc_data: 0x2170
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1574
-  Symbols:   6136
-  CStrings:  2601
+  Functions: 1584
+  Symbols:   6177
+  CStrings:  2624
 
Symbols:
+ -[ISDefaults enableBadgeOverhange]
+ -[ISDefaults enableInstanceIDBasedTwoAppModel]
+ -[ISPersona .cxx_destruct]
+ -[ISPersona initWithRecord:]
+ -[ISPersona isEnterprisePersona]
+ -[ISPersona personaType]
+ -[ISPersona record]
+ -[ISPersona resourceBadge]
+ -[ISResourceProvider _findBadgeResourceWithIconDictionary:bundle:record:]
+ GCC_except_table28
+ _OBJC_CLASS_$_ISPersona
+ _OBJC_IVAR_$_ISPersona._personaType
+ _OBJC_IVAR_$_ISPersona._record
+ _OBJC_METACLASS_$_ISPersona
+ __OBJC_$_INSTANCE_METHODS_ISPersona
+ __OBJC_$_INSTANCE_VARIABLES_ISPersona
+ __OBJC_$_PROP_LIST_ISPersona
+ __OBJC_CLASS_RO_$_ISPersona
+ __OBJC_METACLASS_RO_$_ISPersona
+ ___block_descriptor_76_ea8_32r40r_e55_v24?0r^{?=[16C]{?=dd}dI[16C][16C]{?=[16C]Q[16C]}}8^B16lr32l8r40l8
+ ___block_literal_global.83
+ _dispatch_get_global_queue
+ _dispatch_queue_create_with_target$V2
+ _objc_msgSend$_findBadgeResourceWithIconDictionary:bundle:record:
+ _objc_msgSend$_setQueue:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$enableBadgeOverhange
+ _objc_msgSend$enableInstanceIDBasedTwoAppModel
+ _objc_msgSend$floatValue
+ _objc_msgSend$identities
+ _objc_msgSend$initWithRecord:
+ _objc_msgSend$isEnterprisePersona
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$resourceBadge
- -[ISResourceProvider _findBadgeResourceWithIconDictionary:bundle:]
- GCC_except_table26
- ___block_descriptor_68_ea8_32r_e55_v24?0r^{?=[16C]{?=dd}dI[16C][16C]{?=[16C]Q[16C]}}8^B16lr32l8
- ___block_literal_global.69
- ___block_literal_global.77
- _objc_msgSend$_findBadgeResourceWithIconDictionary:bundle:
CStrings:
+ ","
+ "14:00:56"
+ "@\"LSBundleRecord\""
+ "B40@0:8@16@24@32"
+ "ISPersona"
+ "Invalid color component`%@`. Values must be between 0 and 1"
+ "LaunchServices"
+ "T@\"LSBundleRecord\",R,N,V_record"
+ "Tq,R,N,V_personaType"
+ "_findBadgeResourceWithIconDictionary:bundle:record:"
+ "_setQueue:"
+ "com.apple.fileprovider-actionsui"
+ "com.apple.fileprovider-nonui"
+ "componentsSeparatedByString:"
+ "enableBadgeOverhange"
+ "enableInstanceIDBasedTwoAppModel"
+ "enable_badge_overhang"
+ "floatValue"
+ "frying.pan.fill"
+ "identities"
+ "initWithRecord:"
+ "instance_id_based_two_app_model"
+ "isEnterprisePersona"
+ "objectAtIndex:"
+ "resourceBadge"
- "20:36:48"
- "_findBadgeResourceWithIconDictionary:bundle:"

```
