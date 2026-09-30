## SystemAppMigrator

> `/System/Library/DataClassMigrators/SystemAppMigrator.migrator/SystemAppMigrator`

```diff

-1513.80.6.0.0
-  __TEXT.__text: 0x7904
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_stubs: 0x1620
-  __TEXT.__objc_methlist: 0x5fc
+1513.100.80.0.0
+  __TEXT.__text: 0x80c8
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_stubs: 0x1660
+  __TEXT.__objc_methlist: 0x614
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x2b08
+  __TEXT.__cstring: 0x2bac
   __TEXT.__gcc_except_tab: 0x240
-  __TEXT.__objc_methname: 0x1e03
+  __TEXT.__objc_methname: 0x1e81
   __TEXT.__objc_classname: 0xad
   __TEXT.__objc_methtype: 0x3cf
   __TEXT.__oslogstring: 0x142
-  __TEXT.__unwind_info: 0x1e8
-  __DATA_CONST.__auth_got: 0x2b8
+  __TEXT.__unwind_info: 0x240
+  __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__const: 0x328
-  __DATA_CONST.__cfstring: 0x15a0
+  __DATA_CONST.__cfstring: 0x1600
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x850
-  __DATA.__objc_selrefs: 0x730
-  __DATA.__objc_ivar: 0x4c
+  __DATA.__objc_const: 0x880
+  __DATA.__objc_selrefs: 0x740
+  __DATA.__objc_ivar: 0x50
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 65ECB6F4-02C0-3CA0-95D5-D6B3376FF604
-  Functions: 123
-  Symbols:   177
-  CStrings:  706
+  UUID: D4DCB853-61BF-3F34-A25F-684E10066CC7
+  Functions: 127
+  Symbols:   176
+  CStrings:  716
 
Symbols:
+ _MobileInstallationStoreListOfAppsRequiringPreInstallConsent
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "LSUpgradeInstallConsent"
+ "MISystemAppMigrator: %@ requires pre-install consent"
+ "MISystemAppMigrator: Failed to store list of apps requiring pre-install consent %@: %@"
+ "T@\"NSSet\",R,N,V_preInstallConsentSet"
+ "_preInstallConsentSet"
+ "preInstallConsentSet"
+ "pushPreInstallConsentDataUsingSystemAppState:"

```
