## ZhuGeService

> `/System/Library/PrivateFrameworks/ZhuGeSupport.framework/XPCServices/ZhuGeService.xpc/ZhuGeService`

```diff

-267.60.2.0.0
-  __TEXT.__text: 0x7100
+280.100.9.0.0
+  __TEXT.__text: 0x8708
   __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_stubs: 0x1080
-  __TEXT.__objc_methlist: 0x418
+  __TEXT.__objc_stubs: 0x1140
+  __TEXT.__objc_methlist: 0x468
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x39bf
+  __TEXT.__cstring: 0x3e63
   __TEXT.__objc_classname: 0xfc
-  __TEXT.__objc_methname: 0xfc0
-  __TEXT.__objc_methtype: 0x321
+  __TEXT.__objc_methname: 0x1118
+  __TEXT.__objc_methtype: 0x392
   __TEXT.__oslogstring: 0xe
-  __TEXT.__gcc_except_tab: 0xa4
+  __TEXT.__gcc_except_tab: 0x14c
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x20c
+  __TEXT.__unwind_info: 0x24c
   __DATA_CONST.__auth_got: 0x2b8
   __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x398
-  __DATA_CONST.__cfstring: 0x29e0
+  __DATA_CONST.__const: 0x3c0
+  __DATA_CONST.__cfstring: 0x2d00
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0xf0
-  __DATA.__objc_const: 0xbd0
-  __DATA.__objc_selrefs: 0x4c0
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0xd0
-  __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x28
+  __DATA.__objc_const: 0xce0
+  __DATA.__objc_selrefs: 0x508
+  __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x230
   __DATA.__data: 0xbc0
   __DATA.__bss: 0x270

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7B8B7253-2BFF-3FA2-8B49-E5D0EAA72208
-  Functions: 138
-  Symbols:   163
-  CStrings:  994
+  UUID: 7016ACB9-6008-330D-A043-E3FDA145EA64
+  Functions: 149
+  Symbols:   168
+  CStrings:  1064
 
Symbols:
+ OBJC_IVAR_$_ZhuGeService._domainString
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_NSOrderedSet
+ _OBJC_CLASS_$_NSSet
CStrings:
+ "\x01\x12"
+ "-[ZhuGeService setBulkInternalKeys:getValuesAndError:]"
+ "-[ZhuGeService setBulkInternalMGKeys:getValuesAndError:]"
+ "-[ZhuGeService setBulkKeys:getValuesAndError:]"
+ "-[ZhuGeService setBulkMGKeys:getValuesAndError:]"
+ "-[ZhuGeService setInternalMGKey:getValueAndError:]"
+ "Begin: bulk query MG keys"
+ "Begin: bulk query internal MG keys"
+ "Begin: bulk query internal keys"
+ "Begin: bulk query keys"
+ "End: bulk query MG keys"
+ "End: bulk query internal MG keys"
+ "End: bulk query internal keys"
+ "End: bulk query keys"
+ "Error"
+ "Failed to get internal service proxy for internal MG key \"%@\"!"
+ "Failed to get internal service proxy for internal key \"%@\"!"
+ "In bulk query, MG Key \"%@\" failed! Error: %@"
+ "In bulk query, failed to get internal service proxy for internal MG keys!"
+ "In bulk query, failed to get internal service proxy for internal keys!"
+ "In bulk query, failed to query internal MG keys!"
+ "In bulk query, failed to query internal keys!"
+ "In bulk query, key \"%@\" failed! Error: %@"
+ "In bulk query, query key: \"%@\" from %@entrusted MG"
+ "In bulk query, query key: \"%@\" in %@entrusted way"
+ "Options"
+ "Preferences"
+ "Received internal key: \"%@\""
+ "Received key: \"%@\""
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,V_domainString"
+ "The caller is not entitled for internal key \"%@\"!"
+ "The caller is not entitled for key \"%@\"!"
+ "Trying internal MG key \"%@\""
+ "Value"
+ "_domainString"
+ "activate"
+ "domainString"
+ "keysDict pointer is nil!"
+ "keysList pointer is nil!"
+ "remoteObjectInterface"
+ "setBulkInternalKeys:getValuesAndError:"
+ "setBulkInternalMGKeys:getValuesAndError:"
+ "setBulkKeys:getValuesAndError:"
+ "setBulkMGKeys:getValuesAndError:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setInternalMGKey:getValueAndError:"
+ "setWithObjects:"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "\x01\x11"
- "Failed to get internal service proxy for \"%@\"!"
- "Received internal key \"%@\""
- "Received key \"%@\""
- "The caller is not entitled for \"%@\"!"
- "resume"

```
