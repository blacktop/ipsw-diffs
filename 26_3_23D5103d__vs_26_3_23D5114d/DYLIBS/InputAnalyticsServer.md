## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-111.3.104.1.0
-  __TEXT.__text: 0x56a24
-  __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_methlist: 0x47ac
-  __TEXT.__const: 0x440
-  __TEXT.__cstring: 0x42d9
-  __TEXT.__oslogstring: 0x5ab3
-  __TEXT.__gcc_except_tab: 0xb38
+111.3.104.2.0
+  __TEXT.__text: 0x5723c
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_methlist: 0x482c
+  __TEXT.__const: 0x450
+  __TEXT.__cstring: 0x4369
+  __TEXT.__oslogstring: 0x5bb3
+  __TEXT.__gcc_except_tab: 0xbb0
   __TEXT.__swift5_typeref: 0x10d
   __TEXT.__swift5_capture: 0x98
   __TEXT.__constg_swiftt: 0x4c

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x10b8
+  __TEXT.__unwind_info: 0x10e0
   __TEXT.__eh_frame: 0x310
-  __TEXT.__objc_classname: 0xab7
-  __TEXT.__objc_methname: 0xa3e4
-  __TEXT.__objc_methtype: 0xeac
-  __TEXT.__objc_stubs: 0x8320
-  __DATA_CONST.__got: 0x1028
-  __DATA_CONST.__const: 0x10b8
+  __TEXT.__objc_classname: 0xab9
+  __TEXT.__objc_methname: 0xa591
+  __TEXT.__objc_methtype: 0xedc
+  __TEXT.__objc_stubs: 0x8460
+  __DATA_CONST.__got: 0x1030
+  __DATA_CONST.__const: 0x10e0
   __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23e8
+  __DATA_CONST.__objc_selrefs: 0x2430
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0x1b8
-  __AUTH_CONST.__auth_got: 0x778
+  __AUTH_CONST.__auth_got: 0x790
   __AUTH_CONST.__const: 0xf38
-  __AUTH_CONST.__cfstring: 0x4b00
-  __AUTH_CONST.__objc_const: 0x7cc0
+  __AUTH_CONST.__cfstring: 0x4b40
+  __AUTH_CONST.__objc_const: 0x7d80
   __AUTH_CONST.__objc_intobj: 0xe40
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH.__objc_data: 0xd38
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x564
+  __DATA.__objc_ivar: 0x574
   __DATA.__data: 0x490
   __DATA.__bss: 0x208
   __DATA_DIRTY.__objc_data: 0xfc8

   - /System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog
   - /System/Library/PrivateFrameworks/TextInput.framework/TextInput
   - /System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AB28C72D-7A76-3235-8B8E-51CF58095B19
-  Functions: 1969
-  Symbols:   674
-  CStrings:  3647
+  UUID: EC53138F-7E37-3A54-8662-C2CFE4AA939A
+  Functions: 1985
+  Symbols:   678
+  CStrings:  3678
 
Symbols:
+ _MKBDeviceUnlockedSinceBoot
+ _kMobileKeyBagLockStatusNotifyToken
+ _notify_cancel
+ _notify_register_dispatch
CStrings:
+ "@\"IASDataStoreSystemTable\""
+ "ERROR: Tried to schedule signal processing when a timer already exists."
+ "ERROR: Tried to schedule signal processing when it is disabled"
+ "ERROR: Unexpected %lu signals remaining in buffer after flush"
+ "Error cleaning system table"
+ "Failed to register listening for first unlock"
+ "Pausing signal processing on Session Manager: %{private}@"
+ "Processing action %{sensitive}@ from buffer on Session Manager: %{private}@"
+ "Running buffer processing loop with shouldFlush=%{private}d on Session Manager: %{private}@"
+ "T@\"IASDataStoreSystemTable\",&,N,V_systemTable"
+ "TB,N,V_hasFinalizedInitialization"
+ "TB,N,V_signalProcessingEnabled"
+ "Ti,N,V_unlockStatusToken"
+ "Unpausing signal processing on Session Manager: %{private}@"
+ "_hasFinalizedInitialization"
+ "_signalProcessingEnabled"
+ "_systemTable"
+ "_unlockStatusToken"
+ "deviceUnlockedSinceBoot"
+ "finalizeInitialization"
+ "hasFinalizedInitialization"
+ "i16@0:8"
+ "processBufferWithFlush:"
+ "setHasFinalizedInitialization:"
+ "setSignalProcessingEnabled:"
+ "setSystemTable:"
+ "setUnlockStatusToken:"
+ "signalProcessingEnabled"
+ "unlockStatusToken"
+ "v12@?0i8"
+ "v20@0:8i16"
+ "\x81"
- "ERROR: Tried to schedule a new timer when one already exists."
- "Processing action %{sensitive}@ from buffer"
- "Running buffer processing loop with finalFlush: %{private}d"
- "processBufferWithFinalFlush:"

```
