## CloudDocs

> `/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs`

```diff

-2461.40.47.0.0
-  __TEXT.__text: 0x8bd94
+2461.62.1.0.0
+  __TEXT.__text: 0x8c34c
   __TEXT.__auth_stubs: 0x1390
-  __TEXT.__objc_methlist: 0x4f78
+  __TEXT.__objc_methlist: 0x4fc0
   __TEXT.__const: 0x108
-  __TEXT.__gcc_except_tab: 0x4238
-  __TEXT.__cstring: 0xb01d
+  __TEXT.__gcc_except_tab: 0x4244
+  __TEXT.__cstring: 0xb071
   __TEXT.__oslogstring: 0x94c6
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2380
-  __TEXT.__objc_classname: 0xd44
-  __TEXT.__objc_methname: 0x1026d
+  __TEXT.__unwind_info: 0x2390
+  __TEXT.__objc_classname: 0xd5a
+  __TEXT.__objc_methname: 0x10361
   __TEXT.__objc_methtype: 0x3f07
-  __TEXT.__objc_stubs: 0xacc0
+  __TEXT.__objc_stubs: 0xad00
   __DATA_CONST.__got: 0x510
-  __DATA_CONST.__const: 0x2678
-  __DATA_CONST.__objc_classlist: 0x2c0
+  __DATA_CONST.__const: 0x26a8
+  __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xdff8
-  __DATA_CONST.__objc_selrefs: 0x3a08
+  __DATA_CONST.__objc_const: 0xe0a0
+  __DATA_CONST.__objc_selrefs: 0x3a30
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__cfstring: 0x58c0
+  __AUTH_CONST.__cfstring: 0x5a00
   __AUTH_CONST.__const: 0xfe0
-  __AUTH_CONST.__objc_const: 0x26d8
+  __AUTH_CONST.__objc_const: 0x2720
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__auth_got: 0x9d8
-  __AUTH.__objc_data: 0x1180
+  __AUTH.__objc_data: 0x11d0
   __AUTH.__data: 0x98
   __DATA.__objc_protorefs: 0x90
   __DATA.__objc_classrefs: 0x408
-  __DATA.__objc_superrefs: 0x238
-  __DATA.__objc_ivar: 0x608
+  __DATA.__objc_superrefs: 0x240
+  __DATA.__objc_ivar: 0x610
   __DATA.__data: 0x1160
   __DATA.__bss: 0x200
   __DATA.__common: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3122
-  Symbols:   10407
-  CStrings:  5359
+  Functions: 3128
+  Symbols:   10432
+  CStrings:  5379
 
Symbols:
+ -[BRDeviceConfiguration .cxx_destruct]
+ -[BRDeviceConfiguration configuration]
+ -[BRDeviceConfiguration getDeviceConfigurationString]
+ -[BRDeviceConfiguration initForTestingDevice:]
+ -[NSError(BRAdditions) br_isFileProviderErrorCode:]
+ OBJC_IVAR_$_BRQueryItem._equivalentContentVersions
+ _BRDomainDatabaseIDKey
+ _OBJC_CLASS_$_BRDeviceConfiguration
+ _OBJC_IVAR_$_BRDeviceConfiguration._configuration
+ _OBJC_METACLASS_$_BRDeviceConfiguration
+ __OBJC_$_INSTANCE_METHODS_BRDeviceConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_BRDeviceConfiguration
+ __OBJC_$_PROP_LIST_BRDeviceConfiguration
+ __OBJC_CLASS_RO_$_BRDeviceConfiguration
+ __OBJC_METACLASS_RO_$_BRDeviceConfiguration
+ ___40-[BRAccount containerWithPendingChanges]_block_invoke.34
+ ___48-[BRAccount(BRPrivate) getEvictableSpace:error:]_block_invoke.87
+ ___52-[BRAccount(BRPrivate) hasOptimizeStorageWithError:]_block_invoke.76
+ ___53-[BRAccount(BRPrivate) evictOldDocumentsWithHandler:]_block_invoke.91
+ ___53-[BRDeviceConfiguration getDeviceConfigurationString]_block_invoke
+ ___56-[BRAccount(BRPrivate) setOptimizeStorageEnabled:error:]_block_invoke.82
+ ___62-[BRAccount iCloudDesktopSettingsChangedWithAttributes:error:]_block_invoke.38
+ ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSString"16^B24ls32l8
+ ___block_literal_global.208
+ ___block_literal_global.318
+ ___block_literal_global.37
+ ___block_literal_global.69
+ ___block_literal_global.75
+ ___block_literal_global.81
+ ___block_literal_global.90
+ _objc_msgSend$br_isFileProviderErrorCode:
+ _objc_msgSend$initWithMainContentVersion:equivalentContentVersions:mainMetadataVersion:equivalentMetadataVersions:lastEditorDeviceName:
+ _objc_msgSend$setUnbounded:
- ___40-[BRAccount containerWithPendingChanges]_block_invoke.31
- ___48-[BRAccount(BRPrivate) getEvictableSpace:error:]_block_invoke.84
- ___52-[BRAccount(BRPrivate) hasOptimizeStorageWithError:]_block_invoke.73
- ___53-[BRAccount(BRPrivate) evictOldDocumentsWithHandler:]_block_invoke.88
- ___56-[BRAccount(BRPrivate) setOptimizeStorageEnabled:error:]_block_invoke.79
- ___62-[BRAccount iCloudDesktopSettingsChangedWithAttributes:error:]_block_invoke.35
- ___block_literal_global.120
- ___block_literal_global.122
- ___block_literal_global.205
- ___block_literal_global.315
- ___block_literal_global.34
- ___block_literal_global.83
- ___block_literal_global.87
- _objc_msgSend$initWithContentVersion:metadataVersion:lastEditorDeviceName:
CStrings:
+ "\x0f\t\x14A"
+ "%@:%@;"
+ "%@::"
+ "0"
+ "1"
+ "1.1"
+ "2461.62.1"
+ "BRDeviceConfiguration"
+ "EDS"
+ "FPFS"
+ "T@\"NSDictionary\",R,N,V_configuration"
+ "TESTING"
+ "_configuration"
+ "_equivalentContentVersions"
+ "br_isFileProviderErrorCode:"
+ "configuration"
+ "dbID"
+ "eqCver"
+ "getDeviceConfigurationString"
+ "initForTestingDevice:"
+ "initWithMainContentVersion:equivalentContentVersions:mainMetadataVersion:equivalentMetadataVersions:lastEditorDeviceName:"
+ "setUnbounded:"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
- "\x0f\b\x14A"
- "2461.40.47"
- "initWithContentVersion:metadataVersion:lastEditorDeviceName:"

```
