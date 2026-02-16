## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

```diff

-100222.80.4.0.0
-  __TEXT.__text: 0xa52c0
-  __TEXT.__auth_stubs: 0x2120
+100231.100.15.0.0
+  __TEXT.__text: 0xa2828
+  __TEXT.__auth_stubs: 0x2130
   __TEXT.__objc_methlist: 0x150
-  __TEXT.__const: 0x104cc
-  __TEXT.__oslogstring: 0x52d0
-  __TEXT.__cstring: 0xbc0e
-  __TEXT.__unwind_info: 0x2178
+  __TEXT.__const: 0x104a4
+  __TEXT.__oslogstring: 0x5302
+  __TEXT.__cstring: 0xbc64
+  __TEXT.__unwind_info: 0x21a0
   __TEXT.__objc_classname: 0x58
   __TEXT.__objc_methname: 0xa3
-  __TEXT.__objc_methtype: 0x19bc
+  __TEXT.__objc_methtype: 0x1ad5
   __TEXT.__objc_stubs: 0x60
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x2ab8
+  __DATA_CONST.__const: 0x2b50
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x1098
+  __AUTH_CONST.__auth_got: 0x10a0
   __AUTH_CONST.__const: 0x1df0
-  __AUTH_CONST.__cfstring: 0x7400
+  __AUTH_CONST.__cfstring: 0x7480
   __AUTH_CONST.__objc_const: 0x508
   __AUTH.__objc_data: 0x190
-  __AUTH.__data: 0x98
+  __AUTH.__data: 0x78
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x590
-  __DATA.__bss: 0x4a8
+  __DATA.__bss: 0x4b0
   __DATA.__common: 0x100
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0xe8
-  __DATA_DIRTY.__bss: 0x268
+  __DATA_DIRTY.__data: 0xc8
+  __DATA_DIRTY.__bss: 0x248
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 70D18D5F-008A-33AD-A866-4F61B4E0B637
-  Functions: 3462
-  Symbols:   6655
-  CStrings:  3501
+  UUID: 589A0BD7-A7A5-37F4-BF77-644B282E618D
+  Functions: 3530
+  Symbols:   6838
+  CStrings:  3508
 
Symbols:
+ _CC_SHA256
+ _IOHIDDeviceGetProperty.cold.1
+ _IOHIDManagerScheduleWithRunLoop.cold.1
+ _IOHIDTransactionCommitWithCallback.cold.1
+ _IOHIDTransactionCommitWithCallback.cold.2
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ __IOHIDTraverseDevicesFromParentService
+ __MergedGlobals.67
+ ___IOHIDDeviceAbortCommitCallback
+ ___IOHIDDeviceAbortPendingCallbacks
+ ___IOHIDDeviceAbortReportCallback
+ ___IOHIDDeviceCleanupCommitCallback
+ ___IOHIDDeviceCleanupReportCallback
+ ___IOHIDDeviceRegisterAsyncCommitCallback
+ ___IOHIDDeviceRegisterAsyncReportCallback
+ ___IOHIDDeviceUnregisterAsyncCommitCallback
+ ___IOHIDDeviceUnregisterAsyncReportCallback
+ _____IOHIDDeviceGetHIDRMHash_block_invoke
+ ___block_descriptor_tmp.29
+ ___hidrmHashKeys
- _RosettaLibrary.libLibrary
- __MergedGlobals.68
- ___vers_digit_for_char
- _dynLinkrosetta_convert_to_rosetta_absolute_time
- _dynLinkrosetta_convert_to_system_absolute_time
- _dynLinkrosetta_is_current_process_translated
- _initrosetta_convert_to_rosetta_absolute_time
- _initrosetta_convert_to_system_absolute_time
- _initrosetta_is_current_process_translated
CStrings:
+ "/Library/Caches/com.apple.xbs/32234330-7A05-4B9F-B557-C817F13CEA3F/TemporaryDirectory.Iqf3Zf/Sources/IOAVFamily_user/IOAV.cpp"
+ "AID"
+ "Bluetooth"
+ "HIDRMHash"
+ "IOAccessoryBulkDataEndpoint"
+ "IOAccessoryHSAIDBulkData"
+ "IOAccessoryIDBusBulkData"
+ "IOAccessoryIDBusBulkDataEndpoint"
+ "IOUSBHostDevice"
+ "IOUSBHostInterface"
+ "Loading symbol for principal class:%@ from bundle"
+ "OSKEXT_BUILD_DATE 08:41:38 Jan 26 2026"
+ "ReportDescriptor"
+ "assertion failure: Callback Function is Required"
+ "v12@?0I8"
+ "{?=\"service\"I\"regID\"Q\"deviceInterface\"^^{IOHIDDeviceDeviceInterface}\"deviceTimeStampedInterface\"^^{IOHIDDeviceTimeStampedDeviceInterface}\"plugInInterface\"^^{IOCFPlugInInterfaceStruct}\"deviceLock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"properties\"^{__CFDictionary}\"elements\"^{__CFSet}\"rootKey\"^{__CFString}\"UUIDKey\"^{__CFString}\"notificationPort\"^{IONotificationPort}\"notification\"I\"asyncEventSource\"^{__CFRunLoopSource}\"sourceContext\"{?=\"version\"q\"info\"^v\"retain\"^?\"release\"^?\"copyDescription\"^?\"equal\"^?\"hash\"^?\"getPort\"^?\"perform\"^?}\"queuePort\"^{__CFMachPort}\"runLoop\"^{__CFRunLoop}\"runLoopMode\"^{__CFString}\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"dispatchMach\"@\"NSObject<OS_dispatch_mach>\"\"dispatchStateMask\"AI\"cancelHandler\"@?\"queue\"^{__IOHIDQueue}\"inputMatchingMultiple\"^{__CFArray}\"loadProperties\"C\"isDirty\"C\"transaction\"^v\"callbackLock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"reportBuffer\"^{__CFData}\"batchElements\"^{__CFArray}\"removalCallbackSet\"^{__CFSet}\"inputReportCallbackSet\"^{__CFSet}\"inputValueCallbackSet\"^{__CFSet}\"asyncCommitCallbacks\"^{__CFDictionary}\"asyncElementCallbacks\"^{__CFDictionary}\"asyncReportCallbacks\"^{__CFDictionary}\"elementHandler\"A^v\"removalHandler\"A^v\"inputReportHandler\"A^v\"propertyNotificationHandler\"A^v\"propertyNotificationKeys\"^{__CFArray}\"previousPropertyValues\"^{__CFDictionary}\"propertyPort\"^{IONotificationPort}\"propertyNotify\"I}"
- "/Library/Caches/com.apple.xbs/Sources/IOAVFamily_user/IOAV.cpp"
- "/usr/lib/libRosetta.dylib"
- "ColorComponent0:"
- "ColorComponent1:"
- "ColorComponent2:"
- "ColorSpace:"
- "OSKEXT_BUILD_DATE 14:46:15 Jan 16 2026"
- "Undefined"
- "XYZ"
- "rosetta_convert_to_rosetta_absolute_time"
- "rosetta_convert_to_system_absolute_time"
- "rosetta_is_current_process_translated"
- "{?=\"service\"I\"regID\"Q\"deviceInterface\"^^{IOHIDDeviceDeviceInterface}\"deviceTimeStampedInterface\"^^{IOHIDDeviceTimeStampedDeviceInterface}\"plugInInterface\"^^{IOCFPlugInInterfaceStruct}\"deviceLock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"properties\"^{__CFDictionary}\"elements\"^{__CFSet}\"rootKey\"^{__CFString}\"UUIDKey\"^{__CFString}\"notificationPort\"^{IONotificationPort}\"notification\"I\"asyncEventSource\"^{__CFRunLoopSource}\"sourceContext\"{?=\"version\"q\"info\"^v\"retain\"^?\"release\"^?\"copyDescription\"^?\"equal\"^?\"hash\"^?\"getPort\"^?\"perform\"^?}\"queuePort\"^{__CFMachPort}\"runLoop\"^{__CFRunLoop}\"runLoopMode\"^{__CFString}\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"dispatchMach\"@\"NSObject<OS_dispatch_mach>\"\"dispatchStateMask\"AI\"cancelHandler\"@?\"queue\"^{__IOHIDQueue}\"inputMatchingMultiple\"^{__CFArray}\"loadProperties\"C\"isDirty\"C\"transaction\"^v\"callbackLock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"reportBuffer\"^{__CFData}\"batchElements\"^{__CFArray}\"removalCallbackSet\"^{__CFSet}\"inputReportCallbackSet\"^{__CFSet}\"inputValueCallbackSet\"^{__CFSet}\"elementHandler\"A^v\"removalHandler\"A^v\"inputReportHandler\"A^v}"

```
