## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8150.RELEASE.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__chain_fixups`
- `__DATA.__mod_init_func`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__DATA.__thread_vars`
- `__PDATA.__auth_ptr`
- `__PDATA.__const`
- `__PDATA.__mod_init_func`
- `__PDATA.__data`
- `__PDATA.__shared_cache`
- `__PDATA.__common`

```diff

-1777.0.16.0.0
-  __TEXT.__text: 0xe7cebc
+1777.0.20.0.0
+  __TEXT.__text: 0xe8b20c
   __TEXT.__lcxx_override: 0xe4
-  __TEXT.__cstring: 0xadd11
-  __TEXT.__const: 0x1b3954
-  __TEXT.__swift5_typeref: 0x2fa38
-  __TEXT.__swift5_reflstr: 0x41ca8
-  __TEXT.__swift5_assocty: 0xf740
-  __TEXT.__swift5_fieldmd: 0x67e20
-  __TEXT.__constg_swiftt: 0x6c994
-  __TEXT.__swift5_protos: 0x146c
-  __TEXT.__swift5_proto: 0xae00
-  __TEXT.__swift5_types: 0x6cf4
+  __TEXT.__cstring: 0xae8a1
+  __TEXT.__const: 0x1b4764
+  __TEXT.__swift5_typeref: 0x2fe3c
+  __TEXT.__swift5_reflstr: 0x424e8
+  __TEXT.__swift5_assocty: 0xf800
+  __TEXT.__swift5_fieldmd: 0x68a98
+  __TEXT.__constg_swiftt: 0x6d6d8
+  __TEXT.__swift5_protos: 0x1488
+  __TEXT.__swift5_proto: 0xaef0
+  __TEXT.__swift5_types: 0x6dc4
   __TEXT.__swift5_types2: 0xc0
   __TEXT.__swift5_builtin: 0x2b5c
-  __TEXT.__swift5_capture: 0x69e0
+  __TEXT.__swift5_capture: 0x6a28
   __TEXT.__objc_methtype: 0x536
-  __TEXT.__swift5_mpenum: 0xdc0
-  __TEXT.__swift_as_entry: 0x1614
-  __TEXT.__swift_as_ret: 0x1804
+  __TEXT.__swift5_mpenum: 0xd90
+  __TEXT.__swift_as_entry: 0x1620
+  __TEXT.__swift_as_ret: 0x1818
   __TEXT.__swift_as_cont: 0x2e74
-  __TEXT.__oslogstring: 0x6f97
+  __TEXT.__oslogstring: 0x6fa7
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x140
-  __TEXT.__eh_frame: 0x7fd60
-  __DATA.__TIGHTBEAM_VT: 0x14a0
-  __DATA.__TIGHTBEAM: 0x578
-  __DATA.__const: 0x107238
-  __DATA.__data: 0x57e20
+  __TEXT.__eh_frame: 0x808cc
+  __DATA.__TIGHTBEAM_VT: 0x1500
+  __DATA.__TIGHTBEAM: 0x588
+  __DATA.__const: 0x10a488
+  __DATA.__data: 0x58b78
   __DATA.__mod_init_func: 0x40
   __DATA.__ENDPOINTS: 0x1b6ad
-  __DATA.__auth_ptr: 0x8d78
+  __DATA.__auth_ptr: 0x8e48
   __DATA.__DEVICETREE: 0x30
   __DATA.__shared_cache: 0x3b8
   __DATA.__DARTS: 0x93f

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x30
-  __DATA.__bss: 0x248d0
-  __DATA.__common: 0x3099
+  __DATA.__bss: 0x248f0
+  __DATA.__common: 0x30b9
   __PDATA.__auth_ptr: 0x280
   __PDATA.__const: 0x67b0
   __PDATA.__objc_imageinfo: 0x8

   __PDATA.__data: 0x2af0
   __PDATA.__ENDPOINTS: 0x838
   __PDATA.__shared_cache: 0x70
-  __PDATA.__bss: 0xc4a8
+  __PDATA.__bss: 0xc4b8
   __PDATA.__common: 0x2578
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 50133
+  Functions: 50310
   Symbols:   1
-  CStrings:  16213
+  CStrings:  16268
 
CStrings:
+ "  %s:"
+ "  frame permissions: read%s%s\n"
+ "  removed permissions: %#06lx\n"
+ " %s"
+ " MobileAsset loaders)"
+ " bytes) does not fit in one frame ("
+ " execute"
+ " write"
+ "$JgAneEngineComponent.AneEngine.init(_:_:oslog:IsoId1SegAccess:IsoId2SegAccess:)"
+ "$JgEXDisplayPipeDriverH18PComponent.EXDisplayPipeComponent.init(device:driverUpcalls:exbrightSILHealthOpt:seg0Opt:seg0BackingOpt:companionDebugInterface:osLog:upnotification:context:displayTelemetryAggregatorOpt:)"
+ "$JgExclaveKeyStoreComponent.ExclaveKeyStoreController.init(sksClient:sharedOOLBufferIn:sharedOOLBufferOut:)"
+ "%s untyped { ftid=%#03x; base=%#018llx; size=%#018llx; types=%#08llx; perms=%#06lx }\n"
+ "(invalid type)"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Protogen_exclavecore/EXMobileAssetLoader/EXMobileAssetLoader.swift"
+ "1"
+ "430.0.5"
+ "<MobileAssetLoader "
+ "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Wed Jul 15 23:43:44 PDT 2026; root:AppleImage4_exclavecore-374~12685/ExclaveImage4/RELEASE_ARM64E"
+ "ANEExclave version: ANEExclave_exclavecore-13.17.1"
+ "ANST_512x512.*.hwx"
+ "Boot-args string ("
+ "Build Date: Wed Jul 15 22:52:19 PDT 2026"
+ "Cannot start Exclave Mobile Asset Loader Service "
+ "EXDisplayPipeComponentImpl: init(device:driverUpcalls:exbrightSILHealthOpt:seg0Opt:seg0BackingOpt:companionDebugInterface:osLog:upnotification:context:displayTelemetryAggregatorOpt:)"
+ "EXMobileAssetLoader/EXMobileAssetLoader.swift"
+ "EXMobileAssetLoader/EXMobileAssetLoader_Swift.swift"
+ "EXMobileAssetLoader/StorageExclaveSharedMem.swift"
+ "Empty-VLA endpoint marker missing argument position: "
+ "Empty-VLA marker collides with another argument at position "
+ "ExclaveOS Image4 Framework Version 7.0.0: Wed Jul 15 23:43:44 PDT 2026; root:AppleImage4_exclavecore-374~12685/ExclaveImage4/RELEASE_ARM64E"
+ "ExclaveSNE init with OSLog"
+ "Failed to start MobileAsset loader for FSTag "
+ "Failed to vas_slot_alloc() for boot-args"
+ "Initialized ANEExclaveStorageHelper from system service and segAccess ("
+ "InternalExclaveLauncher/BootArgs.swift"
+ "Invalid key value while decoding result type for malDropSKRefID"
+ "Invalid key value while decoding result type for malGetInfo"
+ "Invalid key value while decoding result type for malGetSize"
+ "Invalid key value while decoding result type for malGrabSKRefID"
+ "Invalid key value while decoding result type for malRead"
+ "Invalid key value while decoding result type for malReaddir"
+ "Invalid key value while decoding result type for malStart"
+ "Invalid key value while decoding result type for malStop"
+ "L4_BootInfo_GetType(untyped_entry) == L4_Type_Untyped"
+ "L4_Type_"
+ "Make MobileAssetLoader from "
+ "OWNERINFO"
+ "PMMInstance could not create Frame of "
+ "Started MobileAsset loader for FSTag "
+ "Stop prox policy (reset)"
+ "System/ExclaveKit/System/Library/PrivateFrameworks/AppleCameraSISP_EK_AlgoModels.framework/Networks.bundle/ANST_512x512.bundle/*.bundle"
+ "Thu Jul 16 00:30:01 PDT 2026"
+ "Unable to copy boot-args frame cap="
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy( _boot_info.normal_untyped.rw_cap, frame_cap_parent )'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy( frame_cap_parent, frame_cap_child )'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy(_boot_info.normal_untyped.rx_cap, slot)'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(temp_slot)'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Mint_Untyped( source_cap, dest_slot, (((L4_Word_t) 1) << (2)) | (((L4_Word_t) 1) << (1)), L4_BootInfo_Untyped_GetBase(untyped_entry), L4_BootInfo_Untyped_GetSize(untyped_entry), type_bitmap, permissions )'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Move(entry_slot, temp_slot)'"
+ "Unsupported configuration. CachedProcedures are only supported for RTGraph programs"
+ "[AppleKeyStoreManager] apfsIntegrityGetPublicKey: unexpected nil derOut"
+ "[AppleKeyStoreManager] apfsIntegrityKeySign: unexpected nil derOut"
+ "[AppleKeyStoreManager] performKDFOperation: unexpected nil derivedKeyOut"
+ "[AppleKeyStoreManager] refKeyPerformOperation: unexpected nil derOut"
+ "[B] Stop prox policy (reset)"
+ "[DMKSClient] init: Failed to map buffer: "
+ "[EXDisplayPipe] Disabled Checks = 0x"
+ "[EXDisplayPipe] Disabled Checks = 0x%llx"
+ "_mint_reduced_untyped"
+ "_sanitize_untyped_entry"
+ "attempted to copy non-existant normal r/x untyped"
+ "cannot sanitize untypeds before bootinfo initialized"
+ "cbinfo_copy_normal_rx_untyped"
+ "com.apple.aneengine"
+ "created"
+ "derived"
+ "dyld_enable_stdio"
+ "ensureDeviceTreeMapped()"
+ "exbright_mot_enable"
+ "exclave_disable_serial"
+ "exclaves_ec_initial_stack_frames"
+ "failed to mint boot-args cap"
+ "failed to shutdown host with exit code: %d"
+ "freed slot was not most recently allocated"
+ "init(allocateUntypedSize:with:rwFrames:)"
+ "integer value bound to non-value generic parameter"
+ "integer value where a type is required"
+ "policy-override-chill-pill"
+ "policy-override-chill-pill exceeds MOT, setting back to default to "
+ "received single-type untyped in roottask for type: %s"
+ "removed types"
+ "sanitized"
+ "types"
+ "x untyped must only be used to create r/x frame objects from normal managed memory, got (ftid: "
+ "yes"
- "$JgExclaveKeyStoreComponent.ExclaveKeyStoreController.init(_:sharedOOLBufferIn:sharedOOLBufferOut:)"
- "%s(%zu): Failed to copy frame parent cap to child cap"
- "%s(%zu): Failed to mint frame parent cap"
- "430.0.2"
- "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Sat Jun 27 01:25:50 PDT 2026; root:AppleImage4_exclavecore-374~6589/ExclaveImage4/RELEASE_ARM64E"
- "ANEExclave version: ANEExclave_exclavecore-13.16.4"
- "Build Date: Sat Jun 27 00:53:12 PDT 2026"
- "ConclaveLauncherEntry()"
- "ExclaveOS Image4 Framework Version 7.0.0: Sat Jun 27 01:25:50 PDT 2026; root:AppleImage4_exclavecore-374~6589/ExclaveImage4/RELEASE_ARM64E"
- "Initialized ANEExclaveStorageHelper from system service and segAccess"
- "InternalExclaveLauncher/RunFlags.swift"
- "Roottask slide is 0x%llx\n"
- "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy( frame_cap_parent, frame_cap_child)'"
- "Unexpected L4_Error: %s(%zu) err='L4_Cap_Mint_Untyped( L4_BootInfo_GetSlot(entry), frame_cap_parent, (((L4_Word_t) 1) << (2)) | (((L4_Word_t) 1) << (1)), 0, 0, (((L4_TypeBitmap_t) 1) << (L4_Type_Arm64_FrameLevel0)), ((L4_Word_t) (0)) | (((L4_Word_t) 1) << (0)))'"
- "Unsupported configuration"
- "Wed Jul  1 23:32:17 PDT 2026"
- "[CONCLAVE LAUNCHER "
- "[DMKSClient] init: Failed to create SegmentMap: "
- "[DMKSClient] init: Failed to get region: "
- "[DMKSClient] init: Failed to set map range: "
- "[DMKSClient] performDeviceMemoryKDFOperation: bad protection class ("
- "[EXDisplayPipe] Disabled Checks"
- "[EXDisplayPipe] Disabled Checks = "
- "[SCHED] Scheduling %s 0x%04hx (%zu/%zu)\n"
- "[StackshotConclaveSupport] discard_address_space_info no shared memory available"
- "[runflags warning] Couldn't get bootargs. Using metadata defaults only"
- "__   _______ _______\n\\ \\ / /  __ \\__   __|\n \\ V /| |__) | | |\n  > < |  _  /  | |\n / . \\| | \\ \\  | |\n/_/ \\_\\_|  \\_\\ |_|___Conclavelauncher "
- "handleException(tag:badge:exception:)"
- "handlePanic()"
- "init(allocateUntypedSize:with:)"
- "init(state:easmServers:upcalls:attachCaps:detachCaps:delegatedDetachCaps:myConclaveId:)"
- "isEarlyCrashLoop()"
- "launchFromStorage(storage:)"
- "mapDeviceTree()"
- "no fixup data for faultable range [%#lx, %#lx) found"
- "non-zero exit return: %d"
- "resume(graph:)"
- "start()"
- "suspend(graph:)"
- "suspendAndKill(graph:stackshotSupportHandle:)"
```
