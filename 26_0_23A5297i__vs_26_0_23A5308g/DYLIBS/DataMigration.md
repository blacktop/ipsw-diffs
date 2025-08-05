## DataMigration

> `/System/Library/PrivateFrameworks/DataMigration.framework/DataMigration`

```diff

-2835.0.0.0.0
-  __TEXT.__text: 0x6d4c
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x888
-  __TEXT.__cstring: 0x1596
+2836.0.0.0.0
+  __TEXT.__text: 0x7200
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__objc_methlist: 0x920
+  __TEXT.__cstring: 0x161a
   __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__unwind_info: 0x280
-  __TEXT.__objc_classname: 0x146
-  __TEXT.__objc_methname: 0x174b
-  __TEXT.__objc_methtype: 0x236
-  __TEXT.__objc_stubs: 0xf00
+  __TEXT.__gcc_except_tab: 0x74
+  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__objc_classname: 0x164
+  __TEXT.__objc_methname: 0x1898
+  __TEXT.__objc_methtype: 0x255
+  __TEXT.__objc_stubs: 0x1040
   __DATA_CONST.__got: 0x168
   __DATA_CONST.__const: 0x1a8
-  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f0
-  __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x468
+  __DATA_CONST.__objc_selrefs: 0x660
+  __DATA_CONST.__objc_superrefs: 0x40
+  __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0xe60
-  __AUTH_CONST.__objc_const: 0xcf8
+  __AUTH_CONST.__cfstring: 0xee0
+  __AUTH_CONST.__objc_const: 0xdc8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x74
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x78
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__bss: 0x20

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 170DD13F-FAE6-395D-BC6A-3AF2766535CB
-  Functions: 222
-  Symbols:   889
-  CStrings:  568
+  UUID: D132EED5-52F4-32DF-9258-8339C205A843
+  Functions: 234
+  Symbols:   934
+  CStrings:  595
 
Symbols:
+ -[DMEnvironment inducedPluginFailures]
+ -[DMEnvironment setInducedPluginFailures:]
+ -[DMInducedPluginFailureManager .cxx_destruct]
+ -[DMInducedPluginFailureManager _crash]
+ -[DMInducedPluginFailureManager _hang]
+ -[DMInducedPluginFailureManager _isInternalBuild]
+ -[DMInducedPluginFailureManager addInducedFailure:forPluginIdentifier:]
+ -[DMInducedPluginFailureManager allInducedFailures]
+ -[DMInducedPluginFailureManager environment]
+ -[DMInducedPluginFailureManager initWithEnvironment:]
+ -[DMInducedPluginFailureManager setEnvironment:]
+ -[DMInducedPluginFailureManager shouldInduceFailureForPluginIdentifier:]
+ GCC_except_table2
+ _OBJC_CLASS_$_DMInducedPluginFailureManager
+ _OBJC_IVAR_$_DMInducedPluginFailureManager._environment
+ _OBJC_METACLASS_$_DMInducedPluginFailureManager
+ __OBJC_$_INSTANCE_METHODS_DMInducedPluginFailureManager
+ __OBJC_$_INSTANCE_VARIABLES_DMInducedPluginFailureManager
+ __OBJC_$_PROP_LIST_DMInducedPluginFailureManager
+ __OBJC_CLASS_RO_$_DMInducedPluginFailureManager
+ __OBJC_METACLASS_RO_$_DMInducedPluginFailureManager
+ _abort
+ _objc_msgSend$_crash
+ _objc_msgSend$_hang
+ _objc_msgSend$_isInternalBuild
+ _objc_msgSend$environment
+ _objc_msgSend$inducedPluginFailures
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$setEnvironment:
+ _objc_msgSend$setInducedPluginFailures:
+ _sleep
CStrings:
+ "@\"DMEnvironment\""
+ "DMInducedPluginFailureManager"
+ "DMInducedPluginFailures"
+ "Inducing failure (crash) for plugin %@"
+ "Inducing failure (hang) for plugin %@"
+ "Inducing failure for plugin %@"
+ "T@\"DMEnvironment\",&,N,V_environment"
+ "_crash"
+ "_environment"
+ "_hang"
+ "_isInternalBuild"
+ "addInducedFailure:forPluginIdentifier:"
+ "allInducedFailures"
+ "environment"
+ "inducedPluginFailures"
+ "initWithEnvironment:"
+ "mutableCopy"
+ "objectAtIndexedSubscript:"
+ "removeObjectAtIndex:"
+ "setEnvironment:"
+ "setInducedPluginFailures:"
+ "shouldInduceFailureForPluginIdentifier:"
+ "v32@0:8Q16@24"

```
