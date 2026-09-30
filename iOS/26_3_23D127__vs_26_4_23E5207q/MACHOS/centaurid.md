## centaurid

> `/usr/libexec/centaurid`

```diff

-70.1.0.0.0
-  __TEXT.__text: 0x3057c
-  __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_stubs: 0x30c0
-  __TEXT.__objc_methlist: 0x106c
+89.0.0.0.0
+  __TEXT.__text: 0x335d4
+  __TEXT.__auth_stubs: 0x9c0
+  __TEXT.__objc_stubs: 0x31a0
+  __TEXT.__objc_methlist: 0x10dc
   __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x19555
-  __TEXT.__oslogstring: 0x5652
-  __TEXT.__objc_methname: 0x2eeb
+  __TEXT.__gcc_except_tab: 0x18f8
+  __TEXT.__cstring: 0x19655
+  __TEXT.__oslogstring: 0x58e0
+  __TEXT.__objc_methname: 0x3020
   __TEXT.__objc_classname: 0x1bc
-  __TEXT.__objc_methtype: 0x95b
-  __TEXT.__gcc_except_tab: 0x168c
-  __TEXT.__unwind_info: 0x770
-  __DATA_CONST.__auth_got: 0x508
-  __DATA_CONST.__got: 0x198
+  __TEXT.__objc_methtype: 0x960
+  __TEXT.__unwind_info: 0x7d0
+  __DATA_CONST.__auth_got: 0x4f8
+  __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x750
-  __DATA_CONST.__cfstring: 0x109a0
+  __DATA_CONST.__const: 0x7a0
+  __DATA_CONST.__cfstring: 0x109c0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__objc_arraydata: 0xa188
+  __DATA_CONST.__objc_arrayobj: 0x558
   __DATA_CONST.__objc_intobj: 0x9480
-  __DATA_CONST.__objc_arraydata: 0xa0e8
-  __DATA_CONST.__objc_arrayobj: 0x540
   __DATA_CONST.__objc_dictobj: 0x1c48
-  __DATA.__objc_const: 0x1b50
-  __DATA.__objc_selrefs: 0xd38
-  __DATA.__objc_ivar: 0x1a4
+  __DATA.__objc_const: 0x1be0
+  __DATA.__objc_selrefs: 0xd80
+  __DATA.__objc_ivar: 0x1b0
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x2a8
   __DATA.__bss: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5882BDB7-9D85-351D-9F9E-B258188F2433
-  Functions: 571
-  Symbols:   222
-  CStrings:  5514
+  UUID: F815FC7C-A555-36A0-A2FF-C1B6A0E73C46
+  Functions: 616
+  Symbols:   226
+  CStrings:  5543
 
Symbols:
+ _CFDictionaryGetTypeID
+ _CentauriBooterCopyBootError
+ _CentauriControllerGetProperty
+ _CentauriControllerSetProperty
+ _CentauriControllerSetWakeOnROM
+ __dispatch_source_type_signal
+ __os_log_debug_impl
+ _dispatch_activate
+ _kCentauriControllerPropertyBootTimestamps
+ _kCentauriControllerPropertyFirmwareBootArgs
+ _kCentauriControllerPropertyFirmwareBootTimestamps
+ _kCentauriControllerPropertyFusingConfig
+ _kCentauriControllerPropertyModuleVendor
+ _kCentauriControllerPropertyPowerTableVersions
+ _signal
- _CentauriControllerGetBootTimestamps
- _CentauriControllerSendFirmwareBootTimestamps
- ___kCFBooleanFalse
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
- _sigaction
CStrings:
+ "%{public}@::%{public}@: HW %u, transaction %u, power assertion %u, activated %u, LPM %u, halted %u, PMU error %u, activate retries %lu, previous activate retry %@, boot retries %lu, previous boot retry %@"
+ "%{public}@::%{public}@: SIGTERM"
+ "%{public}@::%{public}@: activated %u, boot retry count %lu, has firmware %u"
+ "%{public}@::%{public}@: active power table versions: %{public}@"
+ "%{public}@::%{public}@: assertion failure: _sigtermSource -- failed to create SIGTERM source"
+ "%{public}@::%{public}@: assertion failure: _sigusr1Source -- failed to create SIGUSR1 source"
+ "%{public}@::%{public}@: assertion failure: _sigusr2Source -- failed to create SIGUSR2 source"
+ "%{public}@::%{public}@: assertion failure: globalQueue -- failed to get global queue"
+ "%{public}@::%{public}@: fusing config: %{public}@"
+ "%{public}@::%{public}@: invalid boot args property"
+ "%{public}@::%{public}@: invalid fusing config property"
+ "%{public}@::%{public}@: invalid power table versions property"
+ "%{public}@::%{public}@: override out of range: %lu"
+ "%{public}@::%{public}@: wakeOnROM: %d"
+ "@\"NSDictionary\""
+ "T@\"NSDictionary\",R"
+ "T@\"NSDictionary\",R,V_activePowerTableVersions"
+ "T@\"NSString\",R,V_activeBootArgs"
+ "T@\"NSString\",R,V_fusingConfig"
+ "_activePowerTableVersions"
+ "_fusingConfig"
+ "_sigtermSource"
+ "_sigusr1Source"
+ "_sigusr2Source"
+ "activeBootArgs"
+ "activePowerTableVersions"
+ "assertion failure: _sigtermSource -- failed to create SIGTERM source"
+ "assertion failure: _sigusr1Source -- failed to create SIGUSR1 source"
+ "assertion failure: _sigusr2Source -- failed to create SIGUSR2 source"
+ "assertion failure: globalQueue -- failed to get global queue"
+ "booterBootFailure:%@"
+ "date"
+ "fusingConfig"
+ "getModuleVendor"
+ "getPropertyFailure:%s"
+ "logPreferences"
+ "noFirmware"
+ "prepareForExit"
+ "refreshProperties:"
+ "setWakeOnROM:"
+ "storeModuleVendor:"
- "%{public}@::%{public}@: HW %u, transaction %u, power assertion %u, activated %u, LPM %u, halted %u, PMU error %u, activate retries %lu, boot retries %lu"
- "%{public}@::%{public}@: activated %u, boot retry count %lu"
- "%{public}@::%{public}@: active power table paths: %{public}@"
- "%{public}@::%{public}@: assertion failure: NO -- unexpected signal %d"
- "%{public}@::%{public}@: override out of range: %ld"
- "T@\"NSArray\",R"
- "_activePowerTablePaths"
- "_booted"
- "assertion failure: NO -- unexpected signal %d"
- "bootFailure"
- "handleSignal:"
- "unknown"
- "v20@0:8i16"

```
