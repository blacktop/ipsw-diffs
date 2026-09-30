## exclave_roottask

> `exclave_roottask`

```diff

-1195.0.10.0.0
-  __TEXT.__text: 0x4c1d60
+1195.0.22.0.0
+  __TEXT.__text: 0x4c1e90
   __TEXT.__lcxx_override: 0x34c
-  __TEXT.__const: 0xe6349
-  __TEXT.__cstring: 0x326fa
+  __TEXT.__const: 0xe62e9
+  __TEXT.__cstring: 0x32ada
   __TEXT.__swift5_typeref: 0xad62
-  __TEXT.__swift5_capture: 0x1814
+  __TEXT.__swift5_capture: 0x181c
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_reflstr: 0x970c
-  __TEXT.__swift5_assocty: 0x64a8
-  __TEXT.__constg_swiftt: 0x11f58
-  __TEXT.__swift5_fieldmd: 0xf0c8
-  __TEXT.__swift5_builtin: 0xd34
-  __TEXT.__swift5_proto: 0x2454
-  __TEXT.__swift5_types: 0x1090
+  __TEXT.__swift5_assocty: 0x6490
+  __TEXT.__constg_swiftt: 0x11f1c
+  __TEXT.__swift5_fieldmd: 0xf0b8
+  __TEXT.__swift5_builtin: 0xd20
+  __TEXT.__swift5_proto: 0x2448
+  __TEXT.__swift5_types: 0x1088
   __TEXT.__swift5_protos: 0x340
   __TEXT.__swift5_mpenum: 0x460
   __TEXT.__swift5_types2: 0x38

   __DATA.__got: 0x198
   __DATA.__auth_ptr: 0x158
   __DATA.__mod_init_func: 0x50
-  __DATA.__const: 0x2f5b8
+  __DATA.__const: 0x2f490
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__data: 0x9690
+  __DATA.__data: 0x96a0
   __DATA.__shared_cache: 0x70
   __DATA.__DEVICETREE: 0x30
   __DATA.__ENDPOINTS: 0x62a

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
-  __DATA.__common: 0x2208b
-  __DATA.__bss: 0x12980
+  __DATA.__common: 0x220d8
+  __DATA.__bss: 0x12990
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  UUID: 64F02BC4-8141-3ABE-B04B-FCACA0107B76
-  Functions: 17944
+  UUID: BA23F398-7603-3B85-AF7A-513DC293CD30
+  Functions: 17938
   Symbols:   26
-  CStrings:  5396
+  CStrings:  5411
 
CStrings:
+ " fault-on-demand, but "
+ "!VAS_SPANFAULT_CBRESULT_VALID_COW(fault_frame_res)"
+ "!canexec && !VAS_SPANFAULT_CBRESULT_VALID_MANAGED_RO(fault_frame_res)"
+ "/AppleInternal/Library/BuildRoots/4~B3EGugCtUzRfeXifvn_RbLkC7aGOUgbKyItT_Xo/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "Claimed NULL waitingTask!"
+ "PREPOPULATE_METADATA"
+ "Unexpected IsIsolatingCurrentContextDecision value"
+ "Unexpected L4_Error: %s(%zu) err='_map_this_frame(span, address, fault->rotmpcap)'"
+ "[VAS abort in function %s at line %d] Prepopulated metadata was not prepopulated!!\n"
+ "[VAS abort in function %s at line %d] [%s] destroying span after failed prepopulate metadata\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] could not prepopulate span, giving up\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] logic error 0x%lx != 0x%lx\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] read-exec span received a fault but callback returned crazy %#x\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] read-only span received a fault but callback returned crazy %#x\n"
+ "_span_populate_metadata"
+ "_startfault_impl_managed"
+ "canexec && !VAS_SPANFAULT_CBRESULT_VALID_MANAGED_RX(fault_frame_res)"
+ "frame_address != address && frame_address != end_address"
+ "free to empty or invalid chunk detected (likely double-free)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_malloc.c:6116)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_malloc.c:5269)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_malloc.c:4207)"
+ "ret.cap == L4_Nil"
- "!VAS_SPANFAULT_CBRESULT_VALID(fault_frame_res)"
- "/AppleInternal/Library/BuildRoots/4~B1gjugDsddWwV53lEm2VsrI55-hGcddtlhG1mJw/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "A SwiftSetting should never actually be constructed"
- "Failed to claim waitingTask!"
- "Swift/SwiftSettings.swift"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_malloc.c:6100)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_malloc.c:5253)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_malloc.c:4191)"

```
