## exclave_scheduler

> `exclave_scheduler`

```diff

-1195.0.10.0.0
-  __TEXT.__text: 0x310010
+1195.0.22.0.0
+  __TEXT.__text: 0x310180
   __TEXT.__lcxx_override: 0x34c
-  __TEXT.__cstring: 0x21c40
-  __TEXT.__const: 0xd90d2
-  __TEXT.__constg_swiftt: 0xa86c
-  __TEXT.__swift5_typeref: 0x5db2
-  __TEXT.__swift5_builtin: 0xab4
-  __TEXT.__swift5_reflstr: 0x2615
-  __TEXT.__swift5_fieldmd: 0x6500
-  __TEXT.__swift5_assocty: 0x4a10
-  __TEXT.__swift5_proto: 0x1540
-  __TEXT.__swift5_types: 0x930
+  __TEXT.__cstring: 0x21fc0
+  __TEXT.__const: 0xd9070
+  __TEXT.__constg_swiftt: 0xa830
+  __TEXT.__swift5_typeref: 0x5daa
+  __TEXT.__swift5_builtin: 0xaa0
+  __TEXT.__swift5_reflstr: 0x260c
+  __TEXT.__swift5_fieldmd: 0x64f0
+  __TEXT.__swift5_assocty: 0x49f8
+  __TEXT.__swift5_proto: 0x1534
+  __TEXT.__swift5_types: 0x928
   __TEXT.__swift5_protos: 0x238
   __TEXT.__swift5_types2: 0x2c
   __TEXT.__swift5_mpenum: 0x14c

   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x24
-  __TEXT.__eh_frame: 0xfd48
+  __TEXT.__eh_frame: 0xfd40
   __DATA.__got: 0x8
   __DATA.__auth_ptr: 0x58
   __DATA.__mod_init_func: 0x48
-  __DATA.__const: 0x1a4a8
+  __DATA.__const: 0x1a390
   __DATA.__objc_imageinfo: 0x8
   __DATA.__ENDPOINTS: 0xc54
   __DATA.__data: 0x4330

   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x38
   __DATA.__bss: 0x498c0
-  __DATA.__common: 0x1f7b
+  __DATA.__common: 0x1fb8
   __PDATA.__shared_cache: 0x0
   __PDATA.__mod_init_func: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  UUID: 9F131903-116C-30B4-BAD7-76BCCF6B9B17
-  Functions: 11744
+  UUID: 7A07AAB2-4F4C-31D8-934B-5961DC5835F4
+  Functions: 11742
   Symbols:   27
-  CStrings:  3964
+  CStrings:  3977
 
CStrings:
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
+ "ret.cap == L4_Nil"
- "!VAS_SPANFAULT_CBRESULT_VALID(fault_frame_res)"
- "/AppleInternal/Library/BuildRoots/4~B1gjugDsddWwV53lEm2VsrI55-hGcddtlhG1mJw/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "A SwiftSetting should never actually be constructed"
- "Failed to claim waitingTask!"
- "Swift/SwiftSettings.swift"

```
