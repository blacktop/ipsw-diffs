## biomesyncd

> `/usr/libexec/biomesyncd`

```diff

-153.10.0.0.0
-  __TEXT.__text: 0x44d30
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_stubs: 0x77e0
+165.2.0.2.0
+  __TEXT.__text: 0x44ee0
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_stubs: 0x7820
   __TEXT.__objc_methlist: 0x356c
   __TEXT.__const: 0x10c8
   __TEXT.__gcc_except_tab: 0x9a4
-  __TEXT.__objc_methname: 0x95b0
-  __TEXT.__cstring: 0x4a62
+  __TEXT.__objc_methname: 0x9630
+  __TEXT.__cstring: 0x4a52
   __TEXT.__objc_classname: 0x844
-  __TEXT.__objc_methtype: 0x18e7
-  __TEXT.__oslogstring: 0x534b
-  __TEXT.__unwind_info: 0xee8
-  __DATA_CONST.__auth_got: 0x698
-  __DATA_CONST.__got: 0x3a8
-  __DATA_CONST.__const: 0xff8
+  __TEXT.__objc_methtype: 0x18ff
+  __TEXT.__oslogstring: 0x532a
+  __TEXT.__unwind_info: 0xef0
+  __DATA_CONST.__auth_got: 0x690
+  __DATA_CONST.__got: 0x3b0
+  __DATA_CONST.__const: 0x1048
   __DATA_CONST.__cfstring: 0x4140
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_intobj: 0x258
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x8010
-  __DATA.__objc_selrefs: 0x24a0
-  __DATA.__objc_ivar: 0x3d0
+  __DATA.__objc_const: 0x8030
+  __DATA.__objc_selrefs: 0x24b8
+  __DATA.__objc_ivar: 0x3d4
   __DATA.__objc_data: 0x1130
   __DATA.__data: 0x8a0
   __DATA.__bss: 0xf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1496
+  Functions: 1497
   Symbols:   344
-  CStrings:  2908
+  CStrings:  2911
 
Symbols:
+ _OBJC_CLASS_$_BMPersonaUtilities
+ _OBJC_CLASS_$_CCPersonaSyncManager
- _OBJC_CLASS_$_CCRapportSyncEngine
- __os_feature_enabled_impl
CStrings:
+ "@\"CCPersonaSyncManager\""
+ "_cascadeSyncManager"
+ "currentPersonaIdentifierLoggingDescription"
+ "direction == BMResourceSyncDirectionOutbound"
+ "initWithQueue:biomeSyncCore:cascadeSyncManager:"
+ "rapportSyncWithError persona is %!@(MISSING)"
+ "syncEngineForCurrentPersona"
+ "teardown"
- "Biome"
- "CascadeSync"
- "cascade sync feature flag not enabled, returning from periodic sync"
- "direction == BMStreamSyncDirectionOutbound"
- "initWithQueue:core:"

```
