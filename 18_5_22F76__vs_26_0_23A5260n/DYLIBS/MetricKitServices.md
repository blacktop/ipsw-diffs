## MetricKitServices

> `/System/Library/PrivateFrameworks/MetricKitServices.framework/MetricKitServices`

```diff

-261.0.0.0.0
-  __TEXT.__text: 0x4944
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x4fc
+291.0.0.0.1
+  __TEXT.__text: 0x5658
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_methlist: 0x5f4
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x2ba
-  __TEXT.__oslogstring: 0x5c1
+  __TEXT.__cstring: 0x333
+  __TEXT.__oslogstring: 0x663
   __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__unwind_info: 0x138
-  __TEXT.__objc_classname: 0x6a
-  __TEXT.__objc_methname: 0xcdf
+  __TEXT.__unwind_info: 0x160
+  __TEXT.__objc_classname: 0x84
+  __TEXT.__objc_methname: 0xee3
   __TEXT.__objc_methtype: 0xb2
-  __TEXT.__objc_stubs: 0x740
+  __TEXT.__objc_stubs: 0x760
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x338
-  __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_arraydata: 0x1b0
-  __AUTH_CONST.__auth_got: 0x1d0
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0x740
-  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __DATA_CONST.__objc_selrefs: 0x378
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_arraydata: 0x268
+  __AUTH_CONST.__auth_got: 0x1d8
+  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__cfstring: 0x2a0
+  __AUTH_CONST.__objc_const: 0x8a0
+  __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x18
-  __DATA.__objc_ivar: 0x4c
-  __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0x1e0
-  __DATA_DIRTY.__bss: 0x70
+  __DATA.__objc_ivar: 0x5c
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__objc_data: 0x230
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/MetricKitSource.framework/MetricKitSource
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0B91114D-532D-31F1-A5FD-BCFF34D2E271
-  Functions: 118
-  Symbols:   474
-  CStrings:  246
+  UUID: 75A111DE-A666-3268-A822-3D444086C541
+  Functions: 141
+  Symbols:   543
+  CStrings:  269
 
Symbols:
+ +[MXSpaceAttributionService sharedSpaceAttributionService]
+ +[MXUtilities getServicesDateFormatter]
+ +[MXUtilities getServicesDateFormatter].cold.1
+ -[MXSpaceAttributionService .cxx_destruct]
+ -[MXSpaceAttributionService MXSpaceAttributionServiceLogHandle]
+ -[MXSpaceAttributionService _updateService]
+ -[MXSpaceAttributionService _updateService].cold.1
+ -[MXSpaceAttributionService getMetricsForClient:]
+ -[MXSpaceAttributionService init]
+ -[MXSpaceAttributionService metricsAvailable]
+ -[MXSpaceAttributionService metricsSupported]
+ -[MXSpaceAttributionService requestQueue]
+ -[MXSpaceAttributionService setMXSpaceAttributionServiceLogHandle:]
+ -[MXSpaceAttributionService setRequestQueue:]
+ -[MXSpaceAttributionService setSpaceAttributionDataPaths:]
+ -[MXSpaceAttributionService setUnarchivedSpaceAttributionData:]
+ -[MXSpaceAttributionService spaceAttributionDataPaths]
+ -[MXSpaceAttributionService startService]
+ -[MXSpaceAttributionService startService].cold.1
+ -[MXSpaceAttributionService stopService]
+ -[MXSpaceAttributionService unarchiveSpaceAttributionData]
+ -[MXSpaceAttributionService unarchiveSpaceAttributionData].cold.1
+ -[MXSpaceAttributionService unarchivedSpaceAttributionData]
+ _MobileGestalt_copy_productTypeDescForPowerPerf_obj
+ _MobileGestalt_get_current_device
+ _OBJC_CLASS_$_MXSpaceAttributionService
+ _OBJC_IVAR_$_MXSpaceAttributionService._MXSpaceAttributionServiceLogHandle
+ _OBJC_IVAR_$_MXSpaceAttributionService._requestQueue
+ _OBJC_IVAR_$_MXSpaceAttributionService._spaceAttributionDataPaths
+ _OBJC_IVAR_$_MXSpaceAttributionService._unarchivedSpaceAttributionData
+ _OBJC_METACLASS_$_MXSpaceAttributionService
+ __OBJC_$_CLASS_METHODS_MXSpaceAttributionService
+ __OBJC_$_INSTANCE_METHODS_MXSpaceAttributionService
+ __OBJC_$_INSTANCE_VARIABLES_MXSpaceAttributionService
+ __OBJC_$_PROP_LIST_MXSpaceAttributionService
+ __OBJC_CLASS_RO_$_MXSpaceAttributionService
+ __OBJC_METACLASS_RO_$_MXSpaceAttributionService
+ ___39+[MXUtilities getServicesDateFormatter]_block_invoke
+ ___58+[MXSpaceAttributionService sharedSpaceAttributionService]_block_invoke
+ ___block_literal_global.38
+ _getServicesDateFormatter.once_token
+ _getServicesDateFormatter.servicesDateFormatter
+ _objc_msgSend$getServicesDateFormatter
+ _objc_msgSend$unarchiveSpaceAttributionData
+ _objc_retain_x24
+ _sharedSpaceAttributionService.onceToken
+ _sharedSpaceAttributionService.sharedSpaceAttributionService
- _objc_msgSend$initWithCString:encoding:
- _objc_retain_x26
- _sysctl
CStrings:
+ "Failed to start space attribution service."
+ "Failed to unarchive space attribution data: %@"
+ "MXSpaceAttributionService"
+ "MXSpaceAttributionServiceLogHandle"
+ "SpaceAttribution"
+ "Starting space attribution service."
+ "Stopping space attribution service."
+ "T@\"NSMutableArray\",&,V_spaceAttributionDataPaths"
+ "T@\"NSMutableArray\",&,V_unarchivedSpaceAttributionData"
+ "T@\"NSObject<OS_os_log>\",&,V_MXSpaceAttributionServiceLogHandle"
+ "_MXSpaceAttributionServiceLogHandle"
+ "_spaceAttributionDataPaths"
+ "_unarchivedSpaceAttributionData"
+ "com.apple.metrickit.service.spaceattribution"
+ "com.apple.metrickitd.service.spaceattribution.requestqueue"
+ "getServicesDateFormatter"
+ "setMXSpaceAttributionServiceLogHandle:"
+ "setSpaceAttributionDataPaths:"
+ "setUnarchivedSpaceAttributionData:"
+ "sharedSpaceAttributionService"
+ "spaceAttributionDataPaths"
+ "unarchiveSpaceAttributionData"
+ "unarchivedSpaceAttributionData"
- "initWithCString:encoding:"

```
