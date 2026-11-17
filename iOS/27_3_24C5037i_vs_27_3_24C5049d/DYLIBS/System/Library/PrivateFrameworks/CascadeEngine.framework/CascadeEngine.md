## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`

```diff

-259.2.0.2.0
-  __TEXT.__text: 0x7a9f8
-  __TEXT.__objc_methlist: 0x21f4
+259.5.0.0.0
+  __TEXT.__text: 0x7b7e0
+  __TEXT.__objc_methlist: 0x226c
   __TEXT.__const: 0x1b9c
   __TEXT.__gcc_except_tab: 0x738
-  __TEXT.__cstring: 0x321f
+  __TEXT.__cstring: 0x325f
   __TEXT.__ustring: 0x84
-  __TEXT.__oslogstring: 0x754e
+  __TEXT.__oslogstring: 0x772e
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__swift5_typeref: 0x11af
   __TEXT.__swift5_reflstr: 0x4bc

   __TEXT.__swift_as_cont: 0xd0
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1f60
+  __TEXT.__unwind_info: 0x1fa0
   __TEXT.__eh_frame: 0x1ee8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xfc0
+  __DATA_CONST.__const: 0x1040
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d08
+  __DATA_CONST.__objc_selrefs: 0x1d58
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xf8
-  __DATA_CONST.__objc_arraydata: 0x50
+  __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__got: 0x748
   __AUTH_CONST.__const: 0x3038
-  __AUTH_CONST.__cfstring: 0x1c80
-  __AUTH_CONST.__objc_const: 0x5670
+  __AUTH_CONST.__cfstring: 0x1ce0
+  __AUTH_CONST.__objc_const: 0x5700
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x1030
   __AUTH.__objc_data: 0x8b0
   __AUTH.__data: 0x138
-  __DATA.__objc_ivar: 0x2ec
+  __DATA.__objc_ivar: 0x2fc
   __DATA.__data: 0x1040
   __DATA_DIRTY.__objc_data: 0xb00
   __DATA_DIRTY.__data: 0x4f8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2794
-  Symbols:   2296
-  CStrings:  893
+  Functions: 2817
+  Symbols:   2324
+  CStrings:  905
 
Symbols:
+ -[CCImmediateSyncBudgetTracker _globalBudgetAllowsImmediateSyncAt:description:windowWasReset:]
+ -[CCImmediateSyncBudgetTracker shouldAllowImmediateSync]
+ -[CCSyncManager _finishDeviceAddedSync:]
+ -[CCSyncManager _handleCompanionLinkDeviceAddedWithCompletionHandler:]
+ -[CCSyncManager _isDeviceAddedSyncFeatureEnabled]
+ -[CCSyncManager _runDeviceAddedSync]
+ -[CCSyncManager _startDeviceAddedSync]
+ -[CCSyncManager deviceAddedSyncDebounceInterval]
+ -[CCSyncManager handleCompanionLinkDeviceAddedWithCompletionHandler:]
+ -[CCSyncManager setDeviceAddedSyncDebounceInterval:]
+ GCC_except_table47
+ _OBJC_IVAR_$_CCSyncManager._deviceAddedSyncCompletionHandlers
+ _OBJC_IVAR_$_CCSyncManager._deviceAddedSyncDebounceInterval
+ _OBJC_IVAR_$_CCSyncManager._deviceAddedSyncScheduled
+ _OBJC_IVAR_$_CCSyncManager._setChangeListenerQueue
+ _OUTLINED_FUNCTION_185
+ _OUTLINED_FUNCTION_186
+ _OUTLINED_FUNCTION_187
+ _OUTLINED_FUNCTION_188
+ ___36-[CCSyncManager _runDeviceAddedSync]_block_invoke
+ ___36-[CCSyncManager _runDeviceAddedSync]_block_invoke_2
+ ___38-[CCSyncManager _startDeviceAddedSync]_block_invoke
+ ___38-[CCSyncManager _startDeviceAddedSync]_block_invoke_2
+ ___69-[CCSyncManager handleCompanionLinkDeviceAddedWithCompletionHandler:]_block_invoke
+ ___70-[CCSyncManager _handleCompanionLinkDeviceAddedWithCompletionHandler:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_58_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
CStrings:
+ "App.BlockedApp"
+ "DeviceAdded"
+ "Failed to record immediate sync budget, skipping sync on device added: %@"
+ "Ignoring Rapport device added: sync on device added is not enabled"
+ "Immediate sync budget denies sync on device added"
+ "Immediate sync budget tracker unavailable, skipping sync on device added: %@"
+ "Rapport device added, coalescing with pending sync"
+ "Rapport device added, scheduling sync in %.0fs"
+ "Sync on device added finished with %lu completed interaction(s), errors: %@"
+ "Triggering Rapport sync on device added"
+ "rapportSyncOnDeviceAdded"
+ "set-agnostic trigger"
```
