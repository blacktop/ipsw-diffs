## exclave_pmm_exclave

> `exclave_pmm_exclave`

```diff

-1195.0.10.0.0
-  __TEXT.__text: 0x3d6c4
-  __TEXT.__const: 0x1cb80
-  __TEXT.__cstring: 0xe41d
+1195.0.22.0.0
+  __TEXT.__text: 0x3e720
+  __TEXT.__const: 0x1cb90
+  __TEXT.__cstring: 0xe942
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x18
   __DATA.__auth_ptr: 0x10
   __DATA.__mod_init_func: 0x18
-  __DATA.__const: 0xe70
-  __DATA.__data: 0x1be1
+  __DATA.__const: 0xe90
+  __DATA.__data: 0x1bf1
   __DATA.__ENDPOINTS: 0x838
   __DATA.__shared_cache: 0x70
   __DATA.__mod_term_func: 0x0
   __DATA.__thread_vars: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
-  __DATA.__bss: 0x44c30
-  __DATA.__common: 0x7560
+  __DATA.__bss: 0x45e70
+  __DATA.__common: 0x75a0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  UUID: D5011D7A-FA02-3B68-AE9F-18E1B35E907E
-  Functions: 1047
+  UUID: 64E0FCB7-5E4D-3951-BB6F-C3C118D9068A
+  Functions: 1059
   Symbols:   4
-  CStrings:  1294
+  CStrings:  1318
 
CStrings:
+ "!VAS_SPANFAULT_CBRESULT_VALID_COW(fault_frame_res)"
+ "!bitmap_is_null(bitmap)"
+ "!canexec && !VAS_SPANFAULT_CBRESULT_VALID_MANAGED_RO(fault_frame_res)"
+ "/AppleInternal/Library/BuildRoots/4~B3EGugCtUzRfeXifvn_RbLkC7aGOUgbKyItT_Xo/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/bitmap.c"
+ "PREPOPULATE_METADATA"
+ "Unexpected L4_Error: %s(%zu) err='_map_this_frame(span, address, fault->rotmpcap)'"
+ "[PMM] Don't know how to allocate %lu, only %llx"
+ "[VAS abort in function %s at line %d] Prepopulated metadata was not prepopulated!!\n"
+ "[VAS abort in function %s at line %d] [%s] destroying span after failed prepopulate metadata\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] could not prepopulate span, giving up\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] logic error 0x%lx != 0x%lx\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] read-exec span received a fault but callback returned crazy %#x\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] read-only span received a fault but callback returned crazy %#x\n"
+ "__PMM_EXTRA_FRAMES"
+ "_span_populate_metadata"
+ "_startfault_impl_managed"
+ "bitmap_bit_cap"
+ "canexec && !VAS_SPANFAULT_CBRESULT_VALID_MANAGED_RX(fault_frame_res)"
+ "created == frame_cap(reserved_frame)"
+ "frame_address != address && frame_address != end_address"
+ "pmm: \"%s\" set to %zu\n"
+ "pmm: bundle metadata for \"%s\" %zu clamped to max %zd\n"
+ "pmm: bundle metadata for \"%s\" is too long (%zd >= %zd)"
+ "pmm: bundle metadata for \"%s\" not a valid number (\"%s\")\n"
+ "ret.cap == L4_Nil"
+ "v24@?0Q8Q16"
- "!VAS_SPANFAULT_CBRESULT_VALID(fault_frame_res)"
- "/AppleInternal/Library/BuildRoots/4~B1gjugDsddWwV53lEm2VsrI55-hGcddtlhG1mJw/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "raw_frame_create(paddr, cap, type, requestor) == frame_cap(reserved_frame)"

```
