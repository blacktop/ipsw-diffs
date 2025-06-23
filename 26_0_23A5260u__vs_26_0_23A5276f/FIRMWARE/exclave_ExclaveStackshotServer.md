## exclave_ExclaveStackshotServer

> `exclave_ExclaveStackshotServer`

```diff

 68.0.0.0.0
-  __TEXT.__text: 0x343738
+  __TEXT.__text: 0x343cf0
   __TEXT.__lcxx_override: 0x34c
-  __TEXT.__const: 0xd9030
-  __TEXT.__cstring: 0x24a9b
-  __TEXT.__swift5_typeref: 0x6004
-  __TEXT.__swift5_fieldmd: 0x5c9c
-  __TEXT.__constg_swiftt: 0xa794
-  __TEXT.__swift5_reflstr: 0x2000
-  __TEXT.__swift5_assocty: 0x4998
+  __TEXT.__const: 0xd8fe0
+  __TEXT.__cstring: 0x2513b
+  __TEXT.__swift5_typeref: 0x5ffc
+  __TEXT.__swift5_fieldmd: 0x5c8c
+  __TEXT.__constg_swiftt: 0xa758
+  __TEXT.__swift5_reflstr: 0x1ff0
+  __TEXT.__swift5_assocty: 0x4980
   __TEXT.__swift5_protos: 0x258
-  __TEXT.__swift5_proto: 0x1500
-  __TEXT.__swift5_types: 0x898
+  __TEXT.__swift5_proto: 0x14f4
+  __TEXT.__swift5_types: 0x890
   __TEXT.__swift5_capture: 0x408
-  __TEXT.__swift5_builtin: 0x5a0
+  __TEXT.__swift5_builtin: 0x58c
   __TEXT.__swift5_mpenum: 0xbc
   __TEXT.__swift5_types2: 0x24
   __TEXT.__swift_as_entry: 0x224

   __TEXT.__swift5_acfuncs: 0x0
   __TEXT.__swift5_replace: 0x0
   __TEXT.__thread_starts: 0x2c
-  __TEXT.__eh_frame: 0x10388
+  __TEXT.__eh_frame: 0x10380
   __DATA.__got: 0x8
   __DATA.__auth_ptr: 0x70
   __DATA.__mod_init_func: 0x48
-  __DATA.__const: 0x1b398
+  __DATA.__const: 0x1b288
   __DATA.__objc_imageinfo: 0x8
   __DATA.__TIGHTBEAM_VT: 0x60
   __DATA.__TIGHTBEAM: 0x20
-  __DATA.__data: 0x47c0
+  __DATA.__data: 0x47b0
   __DATA.__shared_cache: 0x38
   __DATA.__ENDPOINTS: 0x838
   __DATA.__thread_vars: 0x60

   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
   __DATA.__bss: 0x45650
-  __DATA.__common: 0x27e3
+  __DATA.__common: 0x2820
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  UUID: F289DFED-F65A-3F42-BCBD-BD64DE66D78E
-  Functions: 12788
+  UUID: EDE199D1-E1FD-335F-9CD2-4F9792582FA8
+  Functions: 12793
   Symbols:   0
-  CStrings:  4019
+  CStrings:  4048
 
CStrings:
+ "!VAS_SPANFAULT_CBRESULT_VALID_COW(fault_frame_res)"
+ "!canexec && !VAS_SPANFAULT_CBRESULT_VALID_MANAGED_RO(fault_frame_res)"
+ "/AppleInternal/Library/BuildRoots/4~B3EGugCtUzRfeXifvn_RbLkC7aGOUgbKyItT_Xo/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "Claimed NULL waitingTask!"
+ "NotIsolated"
+ "PREPOPULATE_METADATA"
+ "Unexpected IsIsolatingCurrentContextDecision value"
+ "Unexpected L4_Error: %s(%zu) err='_map_this_frame(span, address, fault->rotmpcap)'"
+ "[%s:%llx]"
+ "[VAS abort in function %s at line %d] Prepopulated metadata was not prepopulated!!\n"
+ "[VAS abort in function %s at line %d] [%s] destroying span after failed prepopulate metadata\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] PT out of range\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] could not prepopulate span, giving up\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] logic error 0x%lx != 0x%lx\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] missing prepopulated page table\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] prepopulated cap missing for address 0x%lx\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] prepopulated page table missing\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] read-exec span received a fault but callback returned crazy %#x\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] read-only span received a fault but callback returned crazy %#x\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] span map mutated on a no-alloc path\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] spanmap changed while we were using it unlocked\n"
+ "_span_populate_metadata"
+ "_startfault_impl_managed"
+ "canexec && !VAS_SPANFAULT_CBRESULT_VALID_MANAGED_RX(fault_frame_res)"
+ "frame_address != address && frame_address != end_address"
+ "pt == L4_Nil"
+ "pt_index >= ptr->num_page_tables"
+ "ptr->page_tables[i] == L4_Nil"
+ "ret.cap == L4_Nil"
+ "span->spanmap.pointer != ret.spanmap.pointer"
+ "spanmap_count(span->spanmap) != count"
+ "vascore__noalloc_mapper_map"
+ "vascore__noalloc_mapper_setup"
+ "vascore__noalloc_mapper_unmap"
- "!VAS_SPANFAULT_CBRESULT_VALID(fault_frame_res)"
- "/AppleInternal/Library/BuildRoots/4~B1gjugDsddWwV53lEm2VsrI55-hGcddtlhG1mJw/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "A SwiftSetting should never actually be constructed"
- "Failed to claim waitingTask!"
- "Swift/SwiftSettings.swift"

```
