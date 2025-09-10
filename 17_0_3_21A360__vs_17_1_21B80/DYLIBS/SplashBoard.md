## SplashBoard

> `/System/Library/PrivateFrameworks/SplashBoard.framework/SplashBoard`

```diff

-296.101.0.0.0
-  __TEXT.__text: 0x27bf8
-  __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_methlist: 0x2254
+297.1.0.0.0
+  __TEXT.__text: 0x27964
+  __TEXT.__auth_stubs: 0xc80
+  __TEXT.__objc_methlist: 0x220c
   __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x2643
+  __TEXT.__cstring: 0x25ed
   __TEXT.__gcc_except_tab: 0x938
-  __TEXT.__oslogstring: 0x2e3f
+  __TEXT.__oslogstring: 0x2e1b
   __TEXT.__ustring: 0x2a
-  __TEXT.__unwind_info: 0xbd0
-  __TEXT.__objc_classname: 0x4ee
-  __TEXT.__objc_methname: 0x62ab
-  __TEXT.__objc_methtype: 0xea4
-  __TEXT.__objc_stubs: 0x4d80
-  __DATA_CONST.__got: 0x158
+  __TEXT.__unwind_info: 0xbc0
+  __TEXT.__objc_classname: 0x4e5
+  __TEXT.__objc_methname: 0x6235
+  __TEXT.__objc_methtype: 0xe77
+  __TEXT.__objc_stubs: 0x4ce0
+  __DATA_CONST.__got: 0x180
   __DATA_CONST.__const: 0xde8
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6290
-  __DATA_CONST.__objc_selrefs: 0x1688
-  __AUTH_CONST.__cfstring: 0x2ce0
+  __DATA_CONST.__objc_const: 0x6230
+  __DATA_CONST.__objc_selrefs: 0x1668
+  __AUTH_CONST.__cfstring: 0x2ca0
   __AUTH_CONST.__objc_const: 0xee0
-  __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__auth_got: 0x648
-  __AUTH.__objc_data: 0x140
+  __AUTH_CONST.__const: 0x420
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__auth_got: 0x650
+  __AUTH.__objc_data: 0x190
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x2b0
-  __DATA.__objc_superrefs: 0xd8
-  __DATA.__objc_ivar: 0x28c
+  __DATA.__objc_superrefs: 0xd0
+  __DATA.__objc_ivar: 0x284
   __DATA.__data: 0x4e8
   __DATA.__bss: 0x38
-  __DATA_DIRTY.__objc_data: 0x910
+  __DATA_DIRTY.__objc_data: 0x8c0
   __DATA_DIRTY.__bss: 0x138
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CCB49E4A-F760-3DFB-B758-107945F83BD3
-  Functions: 1005
-  Symbols:   3751
-  CStrings:  2200
+  UUID: DB2645FA-5E7A-3AE4-B8AA-CA3C8B3773B1
+  Functions: 998
+  Symbols:   3733
+  CStrings:  2186
 
Symbols:
+ +[XBVolumeMaintainer configure:]
+ -[XBApplicationController initWithMainDisplayConfiguration:applicationProvider:launchRequestProvider:configureVolumeMaintenance:]
+ _OBJC_CLASS_$_XBVolumeMaintainer
+ _OBJC_METACLASS_$_XBVolumeMaintainer
+ _XPC_ACTIVITY_INTERVAL
+ _XPC_ACTIVITY_INTERVAL_1_DAY
+ _XPC_ACTIVITY_PRIORITY
+ _XPC_ACTIVITY_PRIORITY_MAINTENANCE
+ _XPC_ACTIVITY_REPEATING
+ __OBJC_$_CLASS_METHODS_XBVolumeMaintainer
+ __OBJC_CLASS_RO_$_XBVolumeMaintainer
+ __OBJC_METACLASS_RO_$_XBVolumeMaintainer
+ ___133-[XBApplicationController _captureOrUpdateLaunchImagesForApplications:firstImageIsReady:createCaptureInfo:completionWithCaptureInfo:]_block_invoke.87
+ ___32+[XBVolumeMaintainer configure:]_block_invoke
+ ___32+[XBVolumeMaintainer configure:]_block_invoke_2
+ ___32+[XBVolumeMaintainer configure:]_block_invoke_3
+ ___68-[XBApplicationController performPostMigrationLaunchImageGeneration]_block_invoke.81
+ ___block_descriptor_40_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
+ _objc_msgSend$configure:
+ _objc_msgSend$initWithMainDisplayConfiguration:applicationProvider:launchRequestProvider:configureVolumeMaintenance:
+ _xpc_activity_register
+ _xpc_dictionary_set_string
- -[XBApplicationController _configureCacheDelete]
- -[XBCacheDeleteRequestHandler .cxx_destruct]
- -[XBCacheDeleteRequestHandler amountPurgeable:urgency:]
- -[XBCacheDeleteRequestHandler applicationProvider]
- -[XBCacheDeleteRequestHandler initWithApplicationProvider:]
- -[XBCacheDeleteRequestHandler performPeriodic:urgency:]
- -[XBCacheDeleteRequestHandler performPurge:urgency:]
- -[XBCacheDeleteRequestHandler setApplicationProvider:]
- _CacheDeleteRegisterInfoCallbacksForProcess
- _OBJC_CLASS_$_XBCacheDeleteRequestHandler
- _OBJC_IVAR_$_XBApplicationController._snapshotCacheDeleteRequestHandler
- _OBJC_IVAR_$_XBCacheDeleteRequestHandler._applicationProvider
- _OBJC_METACLASS_$_XBCacheDeleteRequestHandler
- __OBJC_$_INSTANCE_METHODS_XBCacheDeleteRequestHandler
- __OBJC_$_INSTANCE_VARIABLES_XBCacheDeleteRequestHandler
- __OBJC_$_PROP_LIST_XBCacheDeleteRequestHandler
- __OBJC_CLASS_RO_$_XBCacheDeleteRequestHandler
- __OBJC_METACLASS_RO_$_XBCacheDeleteRequestHandler
- ___133-[XBApplicationController _captureOrUpdateLaunchImagesForApplications:firstImageIsReady:createCaptureInfo:completionWithCaptureInfo:]_block_invoke.93
- ___48-[XBApplicationController _configureCacheDelete]_block_invoke
- ___48-[XBApplicationController _configureCacheDelete]_block_invoke_2
- ___48-[XBApplicationController _configureCacheDelete]_block_invoke_3
- ___48-[XBApplicationController _configureCacheDelete]_block_invoke_4
- ___68-[XBApplicationController performPostMigrationLaunchImageGeneration]_block_invoke.86
- ___block_descriptor_40_e8_32s_e45_^{__CFDictionary=}20?0i8^{__CFDictionary=}12ls32l8
- ___block_literal_global.89
- _objc_msgSend$_configureCacheDelete
- _objc_msgSend$amountPurgeable:urgency:
- _objc_msgSend$applicationProvider
- _objc_msgSend$initWithApplicationProvider:
- _objc_msgSend$initWithMainDisplayConfiguration:applicationProvider:launchRequestProvider:configureCacheDelete:
- _objc_msgSend$performPeriodic:urgency:
- _objc_msgSend$performPurge:urgency:
CStrings:
+ "\x13"
+ "XBVolumeMaintainer"
+ "configure:"
+ "initWithMainDisplayConfiguration:applicationProvider:launchRequestProvider:configureVolumeMaintenance:"
- "\x14"
- "@\"XBCacheDeleteRequestHandler\""
- "@28@0:8@16i24"
- "CACHE_DELETE_AMOUNT"
- "CACHE_DELETE_VOLUME"
- "Failed to register with CacheDelete"
- "T@\"<XBApplicationProviding>\",&,N,V_applicationProvider"
- "XBCacheDeleteRequestHandler"
- "^{__CFDictionary=}20@?0i8^{__CFDictionary=}12"
- "_configureCacheDelete"
- "_snapshotCacheDeleteRequestHandler"
- "amountPurgeable:urgency:"
- "initWithApplicationProvider:"
- "performPeriodic:urgency:"
- "performPurge:urgency:"
- "setApplicationProvider:"

```
