## DataMigration

> `/System/Library/PrivateFrameworks/DataMigration.framework/DataMigration`

```diff

-2830.1.0.0.0
-  __TEXT.__text: 0x64e4
-  __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_methlist: 0x840
-  __TEXT.__cstring: 0x1525
+2834.0.0.0.0
+  __TEXT.__text: 0x6d4c
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_methlist: 0x888
+  __TEXT.__cstring: 0x1596
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__unwind_info: 0x278
-  __TEXT.__objc_classname: 0x135
-  __TEXT.__objc_methname: 0x168e
-  __TEXT.__objc_methtype: 0x20b
-  __TEXT.__objc_stubs: 0xe60
-  __DATA_CONST.__got: 0x148
+  __TEXT.__unwind_info: 0x298
+  __TEXT.__objc_classname: 0x146
+  __TEXT.__objc_methname: 0x174b
+  __TEXT.__objc_methtype: 0x236
+  __TEXT.__objc_stubs: 0xf00
+  __DATA_CONST.__got: 0x168
   __DATA_CONST.__const: 0x1a8
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b8
+  __DATA_CONST.__objc_selrefs: 0x5f0
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x458
+  __AUTH_CONST.__auth_got: 0x468
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0xe40
-  __AUTH_CONST.__objc_const: 0xc68
+  __AUTH_CONST.__cfstring: 0xe60
+  __AUTH_CONST.__objc_const: 0xcf8
   __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x74
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0x370

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C25FCC63-7D14-3855-B16C-B7C02E3B2202
-  Functions: 217
-  Symbols:   864
-  CStrings:  553
+  UUID: 94F1CF08-CA8A-3E72-826E-D90D4567FF61
+  Functions: 222
+  Symbols:   889
+  CStrings:  568
 
Symbols:
+ -[DMConnection forceMigrationOnNextRebootWithUserDataDisposition:context:]
+ -[DMContextManager _entriesHavingBoolValue]
+ -[DMContextManager _entriesHavingStringValue]
+ -[DMContextManager addContext:toXPCDictionary:]
+ -[DMContextManager contextFromArguments:withCount:]
+ -[DMContextManager contextFromXPCDictionary:]
+ _OBJC_CLASS_$_DMContextManager
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_METACLASS_$_DMContextManager
+ __OBJC_$_INSTANCE_METHODS_DMContextManager
+ __OBJC_CLASS_RO_$_DMContextManager
+ __OBJC_METACLASS_RO_$_DMContextManager
+ ___kCFBooleanTrue
+ ___stderrp
+ _fprintf
+ _objc_msgSend$_entriesHavingBoolValue
+ _objc_msgSend$_entriesHavingStringValue
+ _objc_msgSend$addContext:toXPCDictionary:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$forceMigrationOnNextRebootWithUserDataDisposition:context:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _xpc_init_services
- -[DMConnection forceMigrationOnNextRebootWithUserDataDisposition:]
- _objc_msgSend$forceMigrationOnNextRebootWithUserDataDisposition:
CStrings:
+ "@28@0:8^*16i24"
+ "Context argument '%s' lacks value\n"
+ "Context argument '%s' unrecognized\n"
+ "DMContextManager"
+ "DMXPCConnection calling xpc_init_services"
+ "_entriesHavingBoolValue"
+ "_entriesHavingStringValue"
+ "addContext:toXPCDictionary:"
+ "containsObject:"
+ "contextFromArguments:withCount:"
+ "contextFromXPCDictionary:"
+ "forceMigrationOnNextRebootWithUserDataDisposition:context:"
+ "setObject:forKeyedSubscript:"
+ "v28@0:8I16@20"
+ "v32@0:8@16@24"
- "forceMigrationOnNextRebootWithUserDataDisposition:"

```
