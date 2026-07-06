## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

```diff

-  __TEXT.__text: 0x5a190
+  __TEXT.__text: 0x5a8a4
   __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_stubs: 0x6780
-  __TEXT.__objc_methlist: 0x2f24
+  __TEXT.__objc_stubs: 0x6880
+  __TEXT.__objc_methlist: 0x2fcc
   __TEXT.__const: 0x190
-  __TEXT.__gcc_except_tab: 0x28fc
-  __TEXT.__cstring: 0x48da
-  __TEXT.__objc_methname: 0x7c09
-  __TEXT.__oslogstring: 0xab5b
-  __TEXT.__objc_classname: 0x3f1
-  __TEXT.__objc_methtype: 0xe73
-  __TEXT.__unwind_info: 0xdd8
-  __DATA_CONST.__const: 0x1ce8
-  __DATA_CONST.__cfstring: 0x4ae0
-  __DATA_CONST.__objc_classlist: 0x120
+  __TEXT.__gcc_except_tab: 0x2910
+  __TEXT.__cstring: 0x493b
+  __TEXT.__objc_methname: 0x7d7f
+  __TEXT.__oslogstring: 0xabe3
+  __TEXT.__objc_classname: 0x407
+  __TEXT.__objc_methtype: 0xe7b
+  __TEXT.__unwind_info: 0xe00
+  __DATA_CONST.__const: 0x1d08
+  __DATA_CONST.__cfstring: 0x4b40
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_arraydata: 0x568
-  __DATA_CONST.__objc_arrayobj: 0x1c8
+  __DATA_CONST.__objc_arraydata: 0x578
+  __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_intobj: 0x1e0
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x320
   __DATA_CONST.__auth_got: 0x7a0
-  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__got: 0x268
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x48a8
-  __DATA.__objc_selrefs: 0x1e90
-  __DATA.__objc_ivar: 0x384
-  __DATA.__objc_data: 0xb40
+  __DATA.__objc_const: 0x4a68
+  __DATA.__objc_selrefs: 0x1ee0
+  __DATA.__objc_ivar: 0x39c
+  __DATA.__objc_data: 0xb90
   __DATA.__data: 0x4f0
   __DATA.__common: 0x1
-  __DATA.__bss: 0x1f8
+  __DATA.__bss: 0x230
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1222
-  Symbols:   3156
-  CStrings:  3773
+  Functions: 1236
+  Symbols:   3191
+  CStrings:  3802
 
Sections:
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
Symbols:
+ +[AppContainerCaches deleteAppCaches:options:]
+ -[AppCacheDeleteOptions .cxx_destruct]
+ -[AppCacheDeleteOptions bytesNeeded]
+ -[AppCacheDeleteOptions fairPurgeMode]
+ -[AppCacheDeleteOptions group]
+ -[AppCacheDeleteOptions setBytesNeeded:]
+ -[AppCacheDeleteOptions setFairPurgeMode:]
+ -[AppCacheDeleteOptions setGroup:]
+ -[AppCacheDeleteOptions setTelemetry:]
+ -[AppCacheDeleteOptions setUrgency:]
+ -[AppCacheDeleteOptions telemetry]
+ -[AppCacheDeleteOptions urgency]
+ -[CDAppClassifier allHiddenAppBundleGroups]
+ -[CDAppClassifier allVisibleAppBundleGroups]
+ -[CDAppClassifier buildAppInfoForBundleGroups:]
+ -[CacheDeleteFairPurgeOperation cloneCorrectionByVolume]
+ -[CacheDeleteFairPurgeOperation setCloneCorrectionByVolume:]
+ GCC_except_table31
+ OBJC_IVAR_$_AppCacheDeleteOptions._bytesNeeded
+ OBJC_IVAR_$_AppCacheDeleteOptions._fairPurgeMode
+ OBJC_IVAR_$_AppCacheDeleteOptions._group
+ OBJC_IVAR_$_AppCacheDeleteOptions._telemetry
+ OBJC_IVAR_$_AppCacheDeleteOptions._urgency
+ _OBJC_CLASS_$_AppCacheDeleteOptions
+ _OBJC_METACLASS_$_AppCacheDeleteOptions
+ __OBJC_$_INSTANCE_METHODS_AppCacheDeleteOptions
+ __OBJC_$_INSTANCE_VARIABLES_AppCacheDeleteOptions
+ __OBJC_$_PROP_LIST_AppCacheDeleteOptions
+ __OBJC_CLASS_RO_$_AppCacheDeleteOptions
+ __OBJC_METACLASS_RO_$_AppCacheDeleteOptions
+ ___43-[CDAppClassifier allHiddenAppBundleGroups]_block_invoke
+ ___44-[CDAppClassifier allVisibleAppBundleGroups]_block_invoke
+ ___47-[CDAppClassifier buildAppInfoForBundleGroups:]_block_invoke
+ ___47-[CDAppClassifier buildAppInfoForBundleGroups:]_block_invoke_2
+ ___FairPurgeSkippedBundleIDs_block_invoke
+ ___block_descriptor_64_e8_32s40bs48r_e5_v8?0ls32l8s40l8r48l8
+ _objc_msgSend$allHiddenAppBundleGroups
+ _objc_msgSend$allVisibleAppBundleGroups
+ _objc_msgSend$buildAppInfoForBundleGroups:
+ _objc_msgSend$bytesNeeded
+ _objc_msgSend$cloneCorrectionByVolume
+ _objc_msgSend$deleteAppCaches:options:
+ _objc_msgSend$fairPurgeMode
+ _objc_msgSend$group
+ _objc_msgSend$setBytesNeeded:
+ _objc_msgSend$setFairPurgeMode:
+ _objc_msgSend$setGroup:
+ _objc_msgSend$setTelemetry:
+ _objc_msgSend$telemetry
- +[AppContainerCaches deleteAppCaches:urgency:telemetry:group:fairPurgeMode:]
- -[CDAppClassifier allHiddenAppBundleIDs]
- -[CDAppClassifier allVisibleAppBundleIDs]
- -[CDAppClassifier buildAppInfoForBundleIDs:]
- ___40-[CDAppClassifier allHiddenAppBundleIDs]_block_invoke
- ___41-[CDAppClassifier allVisibleAppBundleIDs]_block_invoke
- ___44-[CDAppClassifier buildAppInfoForBundleIDs:]_block_invoke
- ___44-[CDAppClassifier buildAppInfoForBundleIDs:]_block_invoke_2
- ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8s40l8r48l8
- _objc_msgSend$allHiddenAppBundleIDs
- _objc_msgSend$allVisibleAppBundleIDs
- _objc_msgSend$buildAppInfoForBundleIDs:
- _objc_msgSend$deleteAppCaches:urgency:telemetry:group:
- _objc_msgSend$deleteAppCaches:urgency:telemetry:group:fairPurgeMode:
CStrings:
+ "@\"NSObject<OS_dispatch_group>\""
+ "AppCacheDeleteOptions"
+ "CLONE_CORRECTION"
+ "T@\"NSMutableDictionary\",&,N,V_cloneCorrectionByVolume"
+ "T@\"NSObject<OS_dispatch_group>\",&,N,V_group"
+ "T@\"TestTelemetry\",&,N,V_telemetry"
+ "TB,N,V_fairPurgeMode"
+ "TQ,N,V_bytesNeeded"
+ "_bytesNeeded"
+ "_cloneCorrectionByVolume"
+ "_fairPurgeMode"
+ "_group"
+ "_telemetry"
+ "allHiddenAppBundleGroups"
+ "allVisibleAppBundleGroups"
+ "buildAppInfoForBundleGroups:"
+ "bytesNeeded"
+ "cloneCorrectionByVolume"
+ "com.apple.CloudDocs.iCloudDriveFileProvider"
+ "com.apple.FileProvider.LocalStorage"
+ "deleteAppCaches: reached goal (%llu >= %llu bytes), stopping early"
+ "deleteAppCaches:options:"
+ "fairPurgeMode"
+ "group"
+ "plugin updateBlock skipped for urgency %d: refresh already in flight"
+ "setBytesNeeded:"
+ "setCloneCorrectionByVolume:"
+ "setFairPurgeMode:"
+ "setGroup:"
+ "setTelemetry:"
+ "telemetry"
- "@48@0:8@16i24@28@36B44"
- "allHiddenAppBundleIDs"
- "allVisibleAppBundleIDs"
- "buildAppInfoForBundleIDs:"
- "deleteAppCaches:urgency:telemetry:group:fairPurgeMode:"

```
