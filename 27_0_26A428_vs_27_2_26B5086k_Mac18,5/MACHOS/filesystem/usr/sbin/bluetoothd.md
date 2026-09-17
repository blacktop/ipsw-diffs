## bluetoothd

> `/usr/sbin/bluetoothd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2700.51.0.0.0
-  __TEXT.__text: 0x8b1ac4
-  __TEXT.__auth_stubs: 0x45b0
-  __TEXT.__objc_stubs: 0x16520
+2701.3.0.0.0
+  __TEXT.__text: 0x8b283c
+  __TEXT.__auth_stubs: 0x4570
+  __TEXT.__objc_stubs: 0x16540
   __TEXT.__init_offsets: 0x68
-  __TEXT.__objc_methlist: 0x8c5c
-  __TEXT.__gcc_except_tab: 0x6b0a8
-  __TEXT.__const: 0x90bc
-  __TEXT.__cstring: 0xc2bd3
-  __TEXT.__oslogstring: 0xc0c99
-  __TEXT.__objc_methname: 0x1bcca
+  __TEXT.__objc_methlist: 0x8cec
+  __TEXT.__gcc_except_tab: 0x6b1cc
+  __TEXT.__const: 0x90cc
+  __TEXT.__cstring: 0xc2a2b
+  __TEXT.__oslogstring: 0xc0f07
+  __TEXT.__objc_methname: 0x1bda9
   __TEXT.__objc_classname: 0x7b9
   __TEXT.__objc_methtype: 0x4f61
   __TEXT.__ustring: 0x2c
   __TEXT.__dlopen_cstrs: 0x70
-  __TEXT.__unwind_info: 0x2c768
-  __DATA_CONST.__const: 0x31c58
-  __DATA_CONST.__cfstring: 0x24ea0
+  __TEXT.__unwind_info: 0x2c798
+  __DATA_CONST.__const: 0x31bc0
+  __DATA_CONST.__cfstring: 0x25000
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1c8
-  __DATA_CONST.__objc_intobj: 0x990
-  __DATA_CONST.__objc_arraydata: 0x3f8
-  __DATA_CONST.__objc_dictobj: 0x348
+  __DATA_CONST.__objc_intobj: 0x9a8
+  __DATA_CONST.__objc_arraydata: 0x3d8
+  __DATA_CONST.__objc_dictobj: 0x320
   __DATA_CONST.__objc_arrayobj: 0x180
-  __DATA_CONST.__auth_got: 0x22f0
-  __DATA_CONST.__got: 0x990
-  __DATA_CONST.__auth_ptr: 0x1f8
-  __DATA.__objc_const: 0xed30
-  __DATA.__objc_selrefs: 0x6818
-  __DATA.__objc_ivar: 0x109c
+  __DATA_CONST.__auth_got: 0x22d0
+  __DATA_CONST.__got: 0x988
+  __DATA_CONST.__auth_ptr: 0x200
+  __DATA.__objc_const: 0xee10
+  __DATA.__objc_selrefs: 0x6860
+  __DATA.__objc_ivar: 0x10b8
   __DATA.__objc_data: 0x18b0
   __DATA.__data: 0x4c40
   __DATA.__crash_info: 0x148

   - /usr/lib/libiconv.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 36207
-  Symbols:   1424
-  CStrings:  41479
+  Functions: 36228
+  Symbols:   1419
+  CStrings:  41491
 
Symbols:
- _IOObjectConformsTo
- _OBJC_CLASS_$_NSAssertionHandler
- _dlerror
- _localtime
- _proc_pidpath
CStrings:
+ "%s published ColorID with no reachable LocationID"
+ "%{public}s: dropping held pairing notification for “%s”"
+ "%{public}s: posting held pairing notification for “%s” with colorID %d"
+ "%{public}s: refusing to record unresolved colorID"
+ "%{public}s: “%s” has no ColorID yet, holding pairing notification until it is published"
+ "%{public}s: “%s” published colorID %d (stored color %d)"
+ "%{public}s: “%{public}s” USB-paired, notifying user with colorID %d"
+ "771783b8e832813b93b16f99a63281197d05bd7284b551bfd25ec6e004529191"
+ "AudioQualityOptimizer - isOptimizableLink:No(incomplete service discovery)"
+ "CSMainModeOverride"
+ "DaemonXPCToScanMgr"
+ "Freeing transient LeDevice %{public}@ read from cache for address %@ (returning identifier only, device not tracked)"
+ "Freeing transient LeDevice %{public}@ read from cache for address %s (inspection only, not tracked)"
+ "GapRxToObserver"
+ "GapToObserver"
+ "HCIToGap"
+ "IONotificationPortCreate for ColorID failed"
+ "IOServiceAddMatchingNotification for %s failed (%d)"
+ "Keeping IRK for \"%s\": still in use by OOB owner (slot %d), device %{public}s"
+ "LeChannelSoundingAgent initialize fEnableRTTMainMode set to %d"
+ "ObserverToPreNotify"
+ "PairingManager::leDevicePaired LK:%{private, mask.hash}.16P LKype:%d, isAppleWatch %d"
+ "PreNotifyToDaemonXPC"
+ "Registered for %s notifications for ColorID"
+ "ScanMgrToWPDClient"
+ "Shared memory reset"
+ "[LeAdvMetric] getAdvReportMetricCBv1 (ms) %@"
+ "[LeAdvMetric] inXPC not a dict"
+ "com.apple.icloud.findmydeviced"
+ "daemonXPCSendAt"
+ "ed3fd5388913b157ffcc58229cc4c1c1f705ecbace5746b51eaf8e49c1c7a17c"
+ "gapRxAt"
+ "getAdvReportDictFromXPC:"
+ "getAdvReportMetricCBv1"
+ "getAdvReportTimestamps"
+ "getAdvReportXPCRepresentation"
+ "hciRxAt"
+ "kCBAdvReportMetricHeySiri"
+ "observerRxAt"
+ "preNotifyAt"
+ "reject non-credit-based channel in reconfiguration REQ: cid:0x%x type:%d psm:0x%x"
+ "scanMgrRxAt"
+ "setAdvReportTimestamps:"
+ "setDaemonXPCSendAt"
+ "setGapRxAt:"
+ "setHciRxAt:"
+ "setObserverRxAt"
+ "setPreNotifyAt"
+ "setScanMgrRxAt"
+ "setWPDClientAt"
+ "void BT::USBPairingManager::forgetColorIDState(Device *)"
+ "void BT::USBPairingManager::handleColorIDServiceAvailable(io_service_t)"
+ "void BT::USBPairingManager::notifyPairingComplete(Device *, uint32_t)"
+ "void BT::USBPairingManager::notifyPairingCompleteWhenColorKnown(Device *)_block_invoke"
+ "void BT::USBPairingManager::recordResolvedColorID(Device *, uint32_t)"
+ "wpdClientAt"
- "%Y_%m_%d_%H:%M:%S"
- "%{public}s: “%{public}s” USB-paired while logged in as UID=%d, notify user"
- "/usr/lib/libtailspin.dylib"
- "/usr/local/lib/libtailspin.dylib"
- "A2DP Overwait detected"
- "A2DP Tailspin logging %{public}s"
- "AudioLinkManager.mm"
- "Captured tailspin %s at %s"
- "EnableTailspinLogging"
- "Failed to create filepath at %@ to capture tailspin"
- "Failed to open file descriptor to capture tailspin: %@"
- "Identification - Device ID unknown, not generating"
- "Overwait_A2DP_%s.tailspin"
- "PairingManager::leDevicePaired LK:%{private, mask.hash}.16P LKype:%d"
- "TCC exempt for pre-Catalina SDK app %@ (SDK 0x%08x)"
- "TSPDumpOptions_NoSymbolicate"
- "TSPDumpOptions_ReasonString"
- "Trying to be central for A2DP"
- "Trying to save tailspin %@"
- "Warning: Ignoring kCBManagerIsIOBluetoothShim from app %@ with SDK 0x%08x"
- "bool BT::soft_tailspin_config_apply_sync(const tailspin_config_t)"
- "currentHandler"
- "handleFailureInFunction:file:lineNumber:description:"
- "int BT::soft_tailspin_dump_output_with_options(int, NSDictionary * _Nullable __strong, dispatch_queue_t _Nullable, void (^ _Nullable __strong)(bool))"
- "kCBManagerIsIOBluetoothShim"
- "makeActiveModeAndCentral - invalid device"
- "not successfully"
- "setRequestHandler:"
- "successfully"
- "tailspin_config_apply_sync"
- "tailspin_config_create_with_current_state"
- "tailspin_config_create_with_default_config"
- "tailspin_config_free"
- "tailspin_config_t BT::soft_tailspin_config_create_with_current_state()"
- "tailspin_config_t BT::soft_tailspin_config_create_with_default_config()"
- "tailspin_dump_output_with_options"
- "tailspin_enabled_set"
- "tailspin_kdbg_filter_subclass_set"
- "v40@?0@\"NSString\"8@\"NSDictionary\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSError\">32"
- "void *BT::libtailspinLibrary()"
- "void BT::USBPairingManager::completeIncomingUSBDevice(Device *)"
- "void BT::soft_tailspin_config_free(tailspin_config_t)"
- "void BT::soft_tailspin_enabled_set(tailspin_config_t, bool)"
- "void BT::soft_tailspin_kdbg_filter_subclass_set(tailspin_config_t, uint8_t, uint8_t, bool)"
```
