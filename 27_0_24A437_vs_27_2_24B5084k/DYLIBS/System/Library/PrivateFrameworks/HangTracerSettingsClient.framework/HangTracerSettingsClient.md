## HangTracerSettingsClient

> `/System/Library/PrivateFrameworks/HangTracerSettingsClient.framework/HangTracerSettingsClient`

```diff

-426.0.0.0.0
-  __TEXT.__text: 0x17d2c
-  __TEXT.__objc_methlist: 0xd8c
-  __TEXT.__const: 0x20e2
-  __TEXT.__cstring: 0x3372
-  __TEXT.__gcc_except_tab: 0x1a8
-  __TEXT.__oslogstring: 0xa2f
+430.0.0.0.0
+  __TEXT.__text: 0x1a068
+  __TEXT.__objc_methlist: 0xf34
+  __TEXT.__const: 0x20f2
+  __TEXT.__cstring: 0x3448
+  __TEXT.__gcc_except_tab: 0x230
+  __TEXT.__oslogstring: 0xcbc
   __TEXT.__dlopen_cstrs: 0xaf
   __TEXT.__ustring: 0x83c
   __TEXT.__swift5_typeref: 0x4c3

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x194
   __TEXT.__swift5_types: 0x3c
-  __TEXT.__unwind_info: 0xc00
+  __TEXT.__unwind_info: 0xcb8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xdc8
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__const: 0xe18
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbc8
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_selrefs: 0xc10
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x158
-  __DATA_CONST.__got: 0x3d8
-  __AUTH_CONST.__const: 0x608
-  __AUTH_CONST.__cfstring: 0x3900
-  __AUTH_CONST.__objc_const: 0x1960
+  __DATA_CONST.__got: 0x410
+  __AUTH_CONST.__const: 0x628
+  __AUTH_CONST.__cfstring: 0x3920
+  __AUTH_CONST.__objc_const: 0x1c00
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x4d0
-  __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x100
+  __AUTH_CONST.__auth_got: 0x4d8
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0x120
   __DATA.__data: 0x6f8
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 851
-  Symbols:   1513
-  CStrings:  617
+  Functions: 910
+  Symbols:   1600
+  CStrings:  629
 
Symbols:
+ +[HTPerformanceEventDataFinder groupEntriesByEventID:]
+ -[HTAppLaunchDataFinder creationDateForFileURL:]
+ -[HTAppLaunchDataFinder dataEntryForFileURL:cachedAppRecords:]
+ -[HTAppLaunchDataFinder dateFromString:]
+ -[HTAppLaunchDataFinder fileFilterPredicate]
+ -[HTAppLaunchDataFinder includesProcessingHang:]
+ -[HTHang eventType]
+ -[HTPerformanceEventDataFinder .cxx_destruct]
+ -[HTPerformanceEventDataFinder appRecordWithBundleId:cachedAppRecords:]
+ -[HTPerformanceEventDataFinder dataEntriesAtPath:cachedAppRecords:error:]
+ -[HTPerformanceEventDataFinder dataEntryForFileURL:cachedAppRecords:]
+ -[HTPerformanceEventDataFinder dealloc]
+ -[HTPerformanceEventDataFinder fileFilterPredicate]
+ -[HTPerformanceEventDataFinder findEventsFilteringDeveloperApps:completionHandler:]
+ -[HTPerformanceEventDataFinder findProcessingEventsFilteringDeveloperApps:completionHandler:]
+ -[HTPerformanceEventDataFinder folderWatchDispatchSrcs]
+ -[HTPerformanceEventDataFinder folderWatchTaskQueue]
+ -[HTPerformanceEventDataFinder getFilteredLogURLsForPath:error:]
+ -[HTPerformanceEventDataFinder hangReporterDidSaveTailspin:]
+ -[HTPerformanceEventDataFinder hangReporterDoneProcessingTailspin:]
+ -[HTPerformanceEventDataFinder includesProcessingHang:]
+ -[HTPerformanceEventDataFinder initWithLogUpdateCallback:tailspinSavedCallback:tailspinDoneCallback:]
+ -[HTPerformanceEventDataFinder logCountByPath]
+ -[HTPerformanceEventDataFinder logUpdateCallback]
+ -[HTPerformanceEventDataFinder scanDirectoryPaths]
+ -[HTPerformanceEventDataFinder setFolderWatchDispatchSrcs:]
+ -[HTPerformanceEventDataFinder setFolderWatchTaskQueue:]
+ -[HTPerformanceEventDataFinder setLogCountByPath:]
+ -[HTPerformanceEventDataFinder setLogUpdateCallback:]
+ -[HTPerformanceEventDataFinder setTailspinDoneCallback:]
+ -[HTPerformanceEventDataFinder setTailspinSavedCallback:]
+ -[HTPerformanceEventDataFinder tailspinDoneCallback]
+ -[HTPerformanceEventDataFinder tailspinSavedCallback]
+ _CFPreferencesCopyMultiple
+ _HTLevelForAppLaunchDuration
+ _HTUIInternalAppLaunchClientLabel
+ _HTUIInternalAppLaunchClientLabel.str
+ _HTUIInternalAvailableLogsSectionTitle
+ _HTUIInternalAvailableLogsSectionTitle.str
+ _HTUIInternalSystemConditionsNotSupportedForClient
+ _HTUIInternalSystemConditionsNotSupportedForClient.str
+ _NSURLContentModificationDateKey
+ _NSURLCreationDateKey
+ _OBJC_CLASS_$_HTAppLaunchDataFinder
+ _OBJC_CLASS_$_HTPerformanceEventDataFinder
+ _OBJC_IVAR_$_HTHang._eventType
+ _OBJC_IVAR_$_HTPerformanceEventDataFinder._folderWatchDispatchSrcs
+ _OBJC_IVAR_$_HTPerformanceEventDataFinder._folderWatchTaskQueue
+ _OBJC_IVAR_$_HTPerformanceEventDataFinder._hangReporterService
+ _OBJC_IVAR_$_HTPerformanceEventDataFinder._logCountByPath
+ _OBJC_IVAR_$_HTPerformanceEventDataFinder._logUpdateCallback
+ _OBJC_IVAR_$_HTPerformanceEventDataFinder._tailspinDoneCallback
+ _OBJC_IVAR_$_HTPerformanceEventDataFinder._tailspinSavedCallback
+ _OBJC_METACLASS_$_HTAppLaunchDataFinder
+ _OBJC_METACLASS_$_HTPerformanceEventDataFinder
+ __OBJC_$_CLASS_METHODS_HTPerformanceEventDataFinder
+ __OBJC_$_INSTANCE_METHODS_HTAppLaunchDataFinder
+ __OBJC_$_INSTANCE_METHODS_HTPerformanceEventDataFinder
+ __OBJC_$_INSTANCE_VARIABLES_HTPerformanceEventDataFinder
+ __OBJC_$_PROP_LIST_HTPerformanceEventDataFinder
+ __OBJC_CLASS_RO_$_HTAppLaunchDataFinder
+ __OBJC_CLASS_RO_$_HTPerformanceEventDataFinder
+ __OBJC_METACLASS_RO_$_HTAppLaunchDataFinder
+ __OBJC_METACLASS_RO_$_HTPerformanceEventDataFinder
+ ___101-[HTPerformanceEventDataFinder initWithLogUpdateCallback:tailspinSavedCallback:tailspinDoneCallback:]_block_invoke
+ ___73-[HTPerformanceEventDataFinder dataEntriesAtPath:cachedAppRecords:error:]_block_invoke
+ ___83-[HTPerformanceEventDataFinder findEventsFilteringDeveloperApps:completionHandler:]_block_invoke
+ ___83-[HTPerformanceEventDataFinder findEventsFilteringDeveloperApps:completionHandler:]_block_invoke_2
+ ___93-[HTPerformanceEventDataFinder findProcessingEventsFilteringDeveloperApps:completionHandler:]_block_invoke
+ ___93-[HTPerformanceEventDataFinder findProcessingEventsFilteringDeveloperApps:completionHandler:]_block_invoke_2
+ ___block_descriptor_56_e8_32s40s48s_e22_v32?0"NSURL"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56r_e25_v32?0"NSString"8Q16^B24ls32l8s40l8r56l8s48l8
+ _defaultsTextForDomain
+ _kHTEventTypeFence
+ _kHTEventTypeRunLoop
+ _kHTEventTypeSlowActLaunch
+ _kHTEventTypeSlowActResume
+ _kHTExtendedAttributeEventEnd
+ _kHTExtendedAttributeEventStart
+ _kHTExtendedAttributeEventType
+ _objc_msgSend$creationDateForFileURL:
+ _objc_msgSend$dataEntriesAtPath:cachedAppRecords:error:
+ _objc_msgSend$dataEntryForFileURL:cachedAppRecords:
+ _objc_msgSend$eventType
+ _objc_msgSend$fileFilterPredicate
+ _objc_msgSend$groupEntriesByEventID:
+ _objc_msgSend$includesProcessingHang:
+ _objc_msgSend$predicateWithValue:
+ _objc_msgSend$scanDirectoryPaths
- _kHTExtendedAttributeHangEnd
- _kHTExtendedAttributeHangStart
CStrings:
+ "HTPerformanceEventDataFinder: adding %lu entries to list of results"
+ "HTPerformanceEventDataFinder: error finding entries for type: %lu"
+ "HTPerformanceEventDataFinder: error looking for hang logs at path %{public}@ error: %{public}@"
+ "HTPerformanceEventDataFinder: finding events (filtering on developer apps: %d)"
+ "HTPerformanceEventDataFinder: found %lu pending event entries"
+ "HTPerformanceEventDataFinder: getting pending events list (filtering on developer apps: %d)"
+ "HTPerformanceEventDataFinder: looking for data entries at path %{public}@"
+ "HTPerformanceEventDataFinder: unable to retrieve information about app with bundle id %{public}@ (Error: %{public}@)"
+ "HTUIInternalAppLaunchClientLabel"
+ "HTUIInternalAvailableLogsSectionTitle"
+ "HTUIInternalSystemConditionsNotSupportedForClient"
+ "lastPathComponent BEGINSWITH[cd] 'Applaunch' OR lastPathComponent BEGINSWITH[cd] 'Sentry_'"
```
