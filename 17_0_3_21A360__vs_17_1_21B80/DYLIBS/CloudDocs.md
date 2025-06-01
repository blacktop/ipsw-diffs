## CloudDocs

> `/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs`

```diff

-2461.2.1.0.0
-  __TEXT.__text: 0x8ba80
+2461.40.47.0.0
+  __TEXT.__text: 0x8bd94
   __TEXT.__auth_stubs: 0x1390
-  __TEXT.__objc_methlist: 0x4f30
+  __TEXT.__objc_methlist: 0x4f78
   __TEXT.__const: 0x108
-  __TEXT.__gcc_except_tab: 0x421c
-  __TEXT.__cstring: 0xaf80
-  __TEXT.__oslogstring: 0x9493
+  __TEXT.__gcc_except_tab: 0x4238
+  __TEXT.__cstring: 0xb01d
+  __TEXT.__oslogstring: 0x94c6
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2374
-  __TEXT.__objc_classname: 0xd1f
-  __TEXT.__objc_methname: 0x10247
+  __TEXT.__unwind_info: 0x2380
+  __TEXT.__objc_classname: 0xd44
+  __TEXT.__objc_methname: 0x1026d
   __TEXT.__objc_methtype: 0x3f07
   __TEXT.__objc_stubs: 0xacc0
   __DATA_CONST.__got: 0x510
-  __DATA_CONST.__const: 0x2670
-  __DATA_CONST.__objc_classlist: 0x2b0
+  __DATA_CONST.__const: 0x2678
+  __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xdf40
-  __DATA_CONST.__objc_selrefs: 0x39f8
+  __DATA_CONST.__objc_const: 0xdff8
+  __DATA_CONST.__objc_selrefs: 0x3a08
   __DATA_CONST.__objc_arraydata: 0x58
+  __AUTH_CONST.__cfstring: 0x58c0
   __AUTH_CONST.__const: 0xfe0
-  __AUTH_CONST.__cfstring: 0x5860
-  __AUTH_CONST.__objc_const: 0x2648
+  __AUTH_CONST.__objc_const: 0x26d8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__auth_got: 0x9d8
-  __AUTH.__objc_data: 0x10e0
+  __AUTH.__objc_data: 0x1180
   __AUTH.__data: 0x98
   __DATA.__objc_protorefs: 0x90
   __DATA.__objc_classrefs: 0x408
-  __DATA.__objc_superrefs: 0x230
-  __DATA.__objc_ivar: 0x604
+  __DATA.__objc_superrefs: 0x238
+  __DATA.__objc_ivar: 0x608
   __DATA.__data: 0x1160
   __DATA.__bss: 0x200
   __DATA.__common: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: FADD1692-FE33-3CBF-9A60-5573016089C0
-  Functions: 3117
-  Symbols:   10384
-  CStrings:  6056
+  UUID: 897C7B4B-F835-3D20-961C-F23587DFEAE6
+  Functions: 3122
+  Symbols:   10407
+  CStrings:  6069
 
Symbols:
+ +[BRPosixOperationsWrapper exitProcess:]
+ +[NSError(BRAdditions) brc_errorItemBusy]
+ +[NSFileProviderManager(BRAdditions) br_getDomainForCurrentPersonaWithError:].cold.1
+ -[BRStopwatch init]
+ -[BRStopwatch stop]
+ _BRDomainMigrationIDKey
+ _OBJC_CLASS_$_BRPosixOperationsWrapper
+ _OBJC_CLASS_$_BRStopwatch
+ _OBJC_IVAR_$_BRStopwatch._start
+ _OBJC_METACLASS_$_BRPosixOperationsWrapper
+ _OBJC_METACLASS_$_BRStopwatch
+ __OBJC_$_CLASS_METHODS_BRPosixOperationsWrapper
+ __OBJC_$_INSTANCE_METHODS_BRStopwatch
+ __OBJC_$_INSTANCE_VARIABLES_BRStopwatch
+ __OBJC_CLASS_RO_$_BRPosixOperationsWrapper
+ __OBJC_CLASS_RO_$_BRStopwatch
+ __OBJC_METACLASS_RO_$_BRPosixOperationsWrapper
+ __OBJC_METACLASS_RO_$_BRStopwatch
+ ___40-[BRAccount containerWithPendingChanges]_block_invoke.31
+ ___48-[BRAccount(BRPrivate) getEvictableSpace:error:]_block_invoke.84
+ ___52-[BRAccount(BRPrivate) hasOptimizeStorageWithError:]_block_invoke.73
+ ___53-[BRAccount(BRPrivate) evictOldDocumentsWithHandler:]_block_invoke.88
+ ___56-[BRAccount(BRPrivate) setOptimizeStorageEnabled:error:]_block_invoke.79
+ ___62-[BRAccount iCloudDesktopSettingsChangedWithAttributes:error:]_block_invoke.35
+ ___block_literal_global.120
+ ___block_literal_global.122
+ ___block_literal_global.205
+ ___block_literal_global.34
+ ___block_literal_global.83
+ ___block_literal_global.87
- ___40-[BRAccount containerWithPendingChanges]_block_invoke.28
- ___48-[BRAccount(BRPrivate) getEvictableSpace:error:]_block_invoke.81
- ___52-[BRAccount(BRPrivate) hasOptimizeStorageWithError:]_block_invoke.70
- ___53-[BRAccount(BRPrivate) evictOldDocumentsWithHandler:]_block_invoke.85
- ___56-[BRAccount(BRPrivate) setOptimizeStorageEnabled:error:]_block_invoke.76
- ___62-[BRAccount iCloudDesktopSettingsChangedWithAttributes:error:]_block_invoke.32
- ___block_literal_global.202
- ___block_literal_global.31
- ___block_literal_global.63
- ___block_literal_global.69
- ___block_literal_global.75
CStrings:
+ "+[NSFileProviderManager(BRAdditions) br_getDomainForCurrentPersonaWithError:]"
+ "2461.40.47"
+ "BRPosixOperationsWrapper"
+ "BRStopwatch"
+ "[CRIT] UNREACHABLE: Could not compute providerID%@"
+ "_start"
+ "brc_errorItemBusy"
+ "domainID or providerID"
+ "exitProcess:"
+ "migrationID"
+ "unreachable: Could not compute providerID"
- "2461.2.1"

```
