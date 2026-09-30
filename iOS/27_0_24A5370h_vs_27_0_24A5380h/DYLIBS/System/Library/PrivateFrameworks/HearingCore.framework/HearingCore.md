## HearingCore

> `/System/Library/PrivateFrameworks/HearingCore.framework/HearingCore`

```diff

-  __TEXT.__text: 0x7f90
-  __TEXT.__objc_methlist: 0x988
+  __TEXT.__text: 0x844c
+  __TEXT.__objc_methlist: 0x9a0
   __TEXT.__const: 0xd4
-  __TEXT.__gcc_except_tab: 0x108
-  __TEXT.__cstring: 0xb5b
-  __TEXT.__oslogstring: 0x707
-  __TEXT.__unwind_info: 0x308
+  __TEXT.__dlopen_cstrs: 0x5a
+  __TEXT.__gcc_except_tab: 0x120
+  __TEXT.__cstring: 0xb79
+  __TEXT.__oslogstring: 0x7f0
+  __TEXT.__unwind_info: 0x320
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x398
+  __DATA_CONST.__const: 0x3f8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x838
+  __DATA_CONST.__objc_selrefs: 0x848
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__got: 0x1b0
   __AUTH_CONST.__const: 0x480
   __AUTH_CONST.__cfstring: 0xda0
   __AUTH_CONST.__objc_const: 0xb60

   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x68
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x149
+  __DATA.__bss: 0x160
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 247
-  Symbols:   1087
-  CStrings:  277
+  Functions: 251
+  Symbols:   1110
+  CStrings:  283
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[HCDatabaseManager excludeStoreFromCloudBackupIfNeeded:]
+ -[HCDatabaseManager shouldExcludeStoreFromCloudBackup]
+ GCC_except_table235
+ GCC_except_table249
+ _CFURLSetResourcePropertyForKey
+ _SetupAssistantLibraryCore.frameworkLibrary
+ ___SetupAssistantLibraryCore_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e8_32s40s_e50_v24?0"NSPersistentStoreDescription"8"NSError"16ls32l8s40l8
+ ___getBYSetupAssistantNeedsToRunSymbolLoc_block_invoke
+ __kCFURLIsExcludedFromCloudBackupKey
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringSetupAssistant
+ _dlerror
+ _dlsym
+ _getBYSetupAssistantNeedsToRunSymbolLoc.ptr
+ _kCFBooleanTrue
+ _objc_msgSend$excludeStoreFromCloudBackupIfNeeded:
+ _objc_msgSend$shouldExcludeStoreFromCloudBackup
- GCC_except_table245
- ___block_descriptor_40_e8_32s_e50_v24?0"NSPersistentStoreDescription"8"NSError"16ls32l8
CStrings:
+ "%s"
+ "BYSetupAssistantNeedsToRun"
+ "Database Manager: Excluded store from iCloud Backup: %@"
+ "Database Manager: Failed to exclude store from iCloud Backup: %@ error: %@"
+ "Database Manager: Setup Assistant still needs to run, deferring iCloud Backup exclusion for store: %@"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant"

```
