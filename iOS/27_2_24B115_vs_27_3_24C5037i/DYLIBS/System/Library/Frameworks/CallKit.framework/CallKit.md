## CallKit

> `/System/Library/Frameworks/CallKit.framework/CallKit`

```diff

-1406.200.91.0.0
-  __TEXT.__text: 0x665d0
-  __TEXT.__objc_methlist: 0x9324
+1406.300.51.0.0
+  __TEXT.__text: 0x668f8
+  __TEXT.__objc_methlist: 0x938c
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x6557
-  __TEXT.__oslogstring: 0x3e91
-  __TEXT.__gcc_except_tab: 0x784
-  __TEXT.__unwind_info: 0x2968
+  __TEXT.__cstring: 0x656a
+  __TEXT.__oslogstring: 0x3ebe
+  __TEXT.__gcc_except_tab: 0x8a8
+  __TEXT.__unwind_info: 0x2988
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xe08
-  __DATA_CONST.__objc_classlist: 0x410
+  __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3530
+  __DATA_CONST.__objc_selrefs: 0x3548
   __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0x390
+  __DATA_CONST.__objc_superrefs: 0x398
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x4f0
+  __DATA_CONST.__got: 0x4f8
   __AUTH_CONST.__const: 0x560
-  __AUTH_CONST.__cfstring: 0x4440
-  __AUTH_CONST.__objc_const: 0xf138
+  __AUTH_CONST.__cfstring: 0x4460
+  __AUTH_CONST.__objc_const: 0xf210
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1c20
-  __DATA.__objc_ivar: 0x950
+  __AUTH.__objc_data: 0x1c70
+  __DATA.__objc_ivar: 0x954
   __DATA.__data: 0x1740
   __DATA_DIRTY.__objc_data: 0xc80
   __DATA_DIRTY.__bss: 0x80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3269
-  Symbols:   5473
-  CStrings:  1031
+  Functions: 3275
+  Symbols:   5489
+  CStrings:  1032
 
Symbols:
+ +[CXSetPrimaryVideoPausedCallAction supportsSecureCoding]
+ -[CXSetPrimaryVideoPausedCallAction copyWithZone:]
+ -[CXSetPrimaryVideoPausedCallAction encodeWithCoder:]
+ -[CXSetPrimaryVideoPausedCallAction initWithCallUUID:primaryVideoPaused:]
+ -[CXSetPrimaryVideoPausedCallAction initWithCoder:]
+ -[CXSetPrimaryVideoPausedCallAction isPrimaryVideoPaused]
+ GCC_except_table99
+ _OBJC_CLASS_$_CXSetPrimaryVideoPausedCallAction
+ _OBJC_IVAR_$_CXSetPrimaryVideoPausedCallAction._primaryVideoPaused
+ _OBJC_METACLASS_$_CXSetPrimaryVideoPausedCallAction
+ __OBJC_$_CLASS_METHODS_CXSetPrimaryVideoPausedCallAction
+ __OBJC_$_INSTANCE_METHODS_CXSetPrimaryVideoPausedCallAction
+ __OBJC_$_INSTANCE_VARIABLES_CXSetPrimaryVideoPausedCallAction
+ __OBJC_$_PROP_LIST_CXSetPrimaryVideoPausedCallAction
+ __OBJC_CLASS_RO_$_CXSetPrimaryVideoPausedCallAction
+ __OBJC_METACLASS_RO_$_CXSetPrimaryVideoPausedCallAction
+ ___block_descriptor_64_e8_32s40s48s56r_e20_B24?0?<B?^>8^16ls32l8s40l8r56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e20_B24?0?<B?^>8^16ls32l8r56l8r64l8s40l8s48l8
CStrings:
+ "Failed to create new extension: %@"
+ "New extension's unique id not found; creating"
+ "Old extension not found; nothing to migrate"
+ "primaryVideoPaused"
- "Executing migration"
- "New extension's unique id not found"
- "Old extension not found"
```
