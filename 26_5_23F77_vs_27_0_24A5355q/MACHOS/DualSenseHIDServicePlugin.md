## DualSenseHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/DualSenseHIDServicePlugin.plugin/DualSenseHIDServicePlugin`

```diff

-13.5.1.0.0
-  __TEXT.__text: 0x5e84
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_stubs: 0x860
-  __TEXT.__objc_methlist: 0x474
-  __TEXT.__const: 0x4c0
-  __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__cstring: 0x3d9
-  __TEXT.__objc_methname: 0xf0b
-  __TEXT.__oslogstring: 0x815
-  __TEXT.__objc_classname: 0xa0
-  __TEXT.__objc_methtype: 0xa1d
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__auth_got: 0x1b8
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x1f0
-  __DATA_CONST.__cfstring: 0x780
+14.0.14.0.0
+  __TEXT.__text: 0x74f0
+  __TEXT.__auth_stubs: 0x400
+  __TEXT.__objc_stubs: 0x900
+  __TEXT.__objc_methlist: 0x494
+  __TEXT.__const: 0x4e0
+  __TEXT.__gcc_except_tab: 0x16c
+  __TEXT.__cstring: 0x553
+  __TEXT.__objc_methname: 0xf4c
+  __TEXT.__oslogstring: 0x9ef
+  __TEXT.__objc_classname: 0x9a
+  __TEXT.__objc_methtype: 0xb15
+  __TEXT.__unwind_info: 0x238
+  __DATA_CONST.__const: 0x308
+  __DATA_CONST.__cfstring: 0x880
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x720
-  __DATA.__objc_selrefs: 0x3c0
-  __DATA.__objc_ivar: 0x88
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0x78
+  __DATA.__objc_const: 0x740
+  __DATA.__objc_selrefs: 0x3e8
+  __DATA.__objc_ivar: 0x8c
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 549BB280-6D45-37D2-8619-9C10F52B6306
-  Functions: 98
-  Symbols:   75
-  CStrings:  410
+  UUID: BE446C11-F0DF-3503-9486-374A8210B8C5
+  Functions: 128
+  Symbols:   90
+  CStrings:  449
 
Symbols:
+ _NSLocalizedFailureErrorKey
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSMutableArray
+ __os_activity_create
+ __os_activity_current
+ __os_log_debug_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_opt_new
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainBlock
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _os_activity_scope_enter
+ _os_activity_scope_leave
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
CStrings:
+ "Activate"
+ "Cancel"
+ "DualSenseError"
+ "Failed to retrieve multi-pairing info. %{public}@"
+ "Failed to retrieve pairing info. %{public}@"
+ "Get feature report %#0.2x error: %{public}@"
+ "Get feature report %#0.2x failed: %{public}@"
+ "I/O Error %#0.8x"
+ "MultiPairingInfo"
+ "PairingInfo"
+ "Read Device Info"
+ "Ready"
+ "Recent"
+ "Refresh Multi-Pairing Info"
+ "Refresh Pairing Info"
+ "Report [%#0.2x] response has length [%zu bytes], which is less than the expected length [%zu bytes]."
+ "Report [%#0.2x] response is empty.  Expected at least %zu bytes."
+ "Request Multi-Pairing Info"
+ "Request Multi-Pairing Info Error: %{public}@"
+ "Request Pairing Info"
+ "Request Pairing Info Error: %{public}@"
+ "Retrieved Device Multi-Pairing Info: %@"
+ "Retrieved Device Pairing Info: {\n\t localBDAddress = %{public}.*P\n\t hostBDAddress = %{public}.*P\n}"
+ "Set feature report failed."
+ "Slots"
+ "_multiPairingInfo"
+ "addObject:"
+ "copy"
+ "initGameControllerDaemonXPC"
+ "initWithDomain:code:userInfo:"
+ "initWithFormat:"
+ "localizedDescription"
+ "ready"
+ "refreshDeviceInfo"
+ "v24@?0r^{?=[6C][3C][4{?=C[6C]}]}8@\"NSError\"16"
+ "v24@?0r^{?=[6C][3C][6C]}8@\"NSError\"16"
+ "v32@?0r^v8Q16@\"NSError\"24"
+ "{?=\"properties\"{?=\"localBDAddress\"[6C]\"categoryOfDevice\"[3C]\"hostBDAddress\"[6C]}\"fetchRequested\"b1\"fetchInProgress\"b1\"hasFetchedAtLeastOnce\"b1\"valid\"b1}"
+ "{?=\"properties\"{?=\"localBDAddress\"[6C]\"categoryOfDevice\"[3C]\"slot\"[4{?=\"recentUse\"C\"hostBDAddress\"[6C]}]}\"fetchRequested\"b1\"fetchInProgress\"b1\"hasFetchedAtLeastOnce\"b1\"valid\"b1}"
- "!\xf0\xf0D"
- "CRC"
- "Pairing Info = %@"
- "Unable to retreive pairing info from DualSense."
- "getReport:reportLength:withIdentifier:forType:error:"
- "propertyForKey:"
- "requestPairingInfo"
- "{?=\"reportID\"C\"localBDAddress\"[6C]\"categoryOfDevice\"[3C]\"hostBDAddress\"[6C]\"crc\"I}"

```
