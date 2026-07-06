## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

```diff

-  __TEXT.__text: 0x5b860
+  __TEXT.__text: 0x5c004
   __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_stubs: 0x65e0
-  __TEXT.__objc_methlist: 0x2e94
+  __TEXT.__objc_stubs: 0x66e0
+  __TEXT.__objc_methlist: 0x2f3c
   __TEXT.__const: 0x180
-  __TEXT.__gcc_except_tab: 0x2724
-  __TEXT.__cstring: 0x4564
-  __TEXT.__objc_methname: 0x7a26
-  __TEXT.__oslogstring: 0x9fb8
-  __TEXT.__objc_classname: 0x3e5
-  __TEXT.__objc_methtype: 0xe92
-  __TEXT.__unwind_info: 0xdb8
-  __DATA_CONST.__const: 0x1e98
-  __DATA_CONST.__cfstring: 0x4720
-  __DATA_CONST.__objc_classlist: 0x118
+  __TEXT.__gcc_except_tab: 0x2738
+  __TEXT.__cstring: 0x45c5
+  __TEXT.__objc_methname: 0x7b9c
+  __TEXT.__oslogstring: 0xa040
+  __TEXT.__objc_classname: 0x3fb
+  __TEXT.__objc_methtype: 0xe9a
+  __TEXT.__unwind_info: 0xdc0
+  __DATA_CONST.__const: 0x1eb8
+  __DATA_CONST.__cfstring: 0x4780
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xe0
-  __DATA_CONST.__objc_arraydata: 0x5a8
-  __DATA_CONST.__objc_arrayobj: 0x1c8
+  __DATA_CONST.__objc_arraydata: 0x5b8
+  __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_intobj: 0x120
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x348
   __DATA_CONST.__auth_got: 0x728
-  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__got: 0x2a0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x4750
-  __DATA.__objc_selrefs: 0x1e68
-  __DATA.__objc_ivar: 0x374
-  __DATA.__objc_data: 0xaf0
+  __DATA.__objc_const: 0x4910
+  __DATA.__objc_selrefs: 0x1eb8
+  __DATA.__objc_ivar: 0x38c
+  __DATA.__objc_data: 0xb40
   __DATA.__data: 0x4e8
-  __DATA.__bss: 0x1b8
+  __DATA.__bss: 0x1f8
   __DATA.__common: 0x1
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1289
-  Symbols:   3178
-  CStrings:  3675
+  Functions: 1303
+  Symbols:   3213
+  CStrings:  3704
 
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
+ GCC_except_table33
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
+ ___block_descriptor_64_e8_32s40bs48r_e5_v8?0l
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
- ___block_descriptor_56_e8_32s40bs48r_e5_v8?0l
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
