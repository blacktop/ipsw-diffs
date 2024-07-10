## SystemExtensions

> `/System/Library/Frameworks/SystemExtensions.framework/Versions/A/SystemExtensions`

```diff

-187.0.1.0.0
-  __TEXT.__text: 0xa500
+187.0.2.0.1
+  __TEXT.__text: 0xa53c
   __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0xb5c
-  __TEXT.__const: 0x88
+  __TEXT.__objc_methlist: 0xb84
+  __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0x1e0
-  __TEXT.__cstring: 0x90c
+  __TEXT.__cstring: 0x916
   __TEXT.__oslogstring: 0x3db
   __TEXT.__unwind_info: 0x328
   __TEXT.__objc_classname: 0x331
-  __TEXT.__objc_methname: 0x21bf
+  __TEXT.__objc_methname: 0x225c
   __TEXT.__objc_methtype: 0x7f0
-  __TEXT.__objc_stubs: 0x18e0
+  __TEXT.__objc_stubs: 0x1900
   __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x818
+  __DATA_CONST.__objc_selrefs: 0x830
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x38
   __AUTH_CONST.__auth_got: 0x2a8
   __AUTH_CONST.__const: 0x580
   __AUTH_CONST.__cfstring: 0x640
-  __AUTH_CONST.__objc_const: 0x1ea8
+  __AUTH_CONST.__objc_const: 0x1f08
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0xd4
+  __DATA.__objc_ivar: 0xdc
   __DATA.__data: 0x440
   __DATA.__common: 0x10
   __DATA.__bss: 0x40

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 308
-  Symbols:   909
-  CStrings:  98
+  Functions: 311
+  Symbols:   915
+  CStrings:  99
 
Symbols:
+ -[OSSystemExtensionInfo disallowDisablingAndUninstalling]
+ -[OSSystemExtensionInfo removable]
+ -[OSSystemExtensionInfo setRemovable:]
+ GCC_except_table117
+ GCC_except_table123
+ GCC_except_table130
+ GCC_except_table143
+ GCC_except_table147
+ GCC_except_table189
+ GCC_except_table65
+ GCC_except_table97
+ OBJC_IVAR_$_OSSystemExtensionInfo._disallowDisablingAndUninstalling
+ OBJC_IVAR_$_OSSystemExtensionInfo._removable
+ __69-[OSSystemExtensionPointListener listener:shouldAcceptNewConnection:]_block_invoke.352
+ __70-[SystemExtensionsWorkspace cleanupOrphanedSystemExtensionsWithError:]_block_invoke.591
+ __block_literal_global.522
+ __block_literal_global.526
+ __block_literal_global.528
+ __block_literal_global.586
+ __block_literal_global.629
+ _objc_msgSend$setRemovable:
- GCC_except_table114
- GCC_except_table120
- GCC_except_table124
- GCC_except_table140
- GCC_except_table144
- GCC_except_table186
- GCC_except_table62
- GCC_except_table94
- __69-[OSSystemExtensionPointListener listener:shouldAcceptNewConnection:]_block_invoke.342
- __70-[SystemExtensionsWorkspace cleanupOrphanedSystemExtensionsWithError:]_block_invoke.581
- __block_literal_global.512
- __block_literal_global.516
- __block_literal_global.518
- __block_literal_global.576
- __block_literal_global.619
CStrings:
+ "Removable"

```
