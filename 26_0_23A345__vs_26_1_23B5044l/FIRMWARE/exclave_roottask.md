## exclave_roottask

> `exclave_roottask`

```diff

-1195.0.38.0.0
-  __TEXT.__text: 0x4cc7ac
+1195.40.17.0.0
+  __TEXT.__text: 0x4cb070
   __TEXT.__lcxx_override: 0x34c
-  __TEXT.__const: 0xe6319
-  __TEXT.__cstring: 0x330ea
-  __TEXT.__swift5_typeref: 0xad82
-  __TEXT.__swift5_capture: 0x17cc
+  __TEXT.__const: 0xe6289
+  __TEXT.__cstring: 0x32eda
+  __TEXT.__swift5_typeref: 0xad72
+  __TEXT.__swift5_capture: 0x179c
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_reflstr: 0x974c
   __TEXT.__swift5_assocty: 0x6448

   __TEXT.__swift5_protos: 0x340
   __TEXT.__swift5_mpenum: 0x468
   __TEXT.__swift5_types2: 0x3c
-  __TEXT.__swift_as_entry: 0x21c
-  __TEXT.__swift_as_ret: 0x2a4
+  __TEXT.__swift_as_entry: 0x218
+  __TEXT.__swift_as_ret: 0x2a0
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__swift5_replace: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x24
-  __TEXT.__eh_frame: 0x1a5dc
+  __TEXT.__eh_frame: 0x1a4dc
   __DATA.__got: 0x198
   __DATA.__auth_ptr: 0x160
-  __DATA.__mod_init_func: 0x50
-  __DATA.__const: 0x2f518
+  __DATA.__mod_init_func: 0x58
+  __DATA.__const: 0x2f568
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__data: 0x9aa0
+  __DATA.__data: 0x9a70
   __DATA.__shared_cache: 0x70
   __DATA.__DEVICETREE: 0x30
   __DATA.__ENDPOINTS: 0x62a

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
-  __DATA.__common: 0x21fe8
-  __DATA.__bss: 0x129b0
+  __DATA.__common: 0x21ec8
+  __DATA.__bss: 0x12ad0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  UUID: 2712E9EA-9B08-316F-AC44-897C1A92D4EF
-  Functions: 17968
+  UUID: 9B47FC62-043D-3BFA-9938-A483FB8722B5
+  Functions: 17952
   Symbols:   26
-  CStrings:  5453
+  CStrings:  5446
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B9U2ugBanAody3ztRRE_IPMX8YeE-OMaU-_L52Q/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.1.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "Failed to take entropy for insecure rand seed\n"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_malloc.c:6810)"
+ "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_segment.c:2300)"
+ "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_segment.c:2402)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_malloc.c:6114)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_segment.c:829)"
+ "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_segment.c:855)"
+ "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_segment.c:895)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_malloc.c:5267)"
+ "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_segment.c:850)"
+ "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_segment.c:894)"
+ "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_segment.c:831)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_malloc.c:4189)"
+ "vas_core_shadow_space_destroy"
+ "vas_core_shadow_space_setup"
+ "vas_span_alloc( vas_self(), VAS_SPAN_BUMP_POPULATED | VAS_SPAN_WIRED | VAS_SPAN_NOSPLIT, &config, &_ipmm_state.freed_frames.span)"
+ "vas_span_alloc( vas_self(), VAS_SPAN_MANAGED | VAS_SPAN_NOSPLIT | VAS_SPAN_WRITE, &config, &_ipmm_state.ipmm_retype_span)"
+ "vcss == _shadow_self()->shadow_space && _shadow_self()->move_caps != 0"
- "(span->attrs & VAS_SPAN_OPTOUT_SPANMAP) != 0"
- "/AppleInternal/Library/BuildRoots/4~B6sXugAGX1vZCl_U045WvS-4sh7ycqOOnDHOU9M/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "Not enough entropy\n"
- "OPTOUT_SPANMAP"
- "[VAS abort in function %s at line %d] [%s] destroying span after failed prepopulate metadata\n"
- "[VAS abort in function %s at line %d] [true: %lx %s %lx]vas_core_heap_shadow_space_alloc() failed\n"
- "[VAS abort in function %s at line %d] [true: (%s)] spanmap cleanup function on a non-spanmap span\n"
- "[VAS abort in function %s at line %d] unable to populate frame cap %lx in vas %p for address %lx\n"
- "_Concurrency/Task+immediate.swift"
- "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_malloc.c:6807)"
- "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_segment.c:2290)"
- "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_segment.c:2392)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_malloc.c:6111)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_segment.c:819)"
- "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_segment.c:845)"
- "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_segment.c:885)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_malloc.c:5264)"
- "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_segment.c:840)"
- "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_segment.c:884)"
- "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_segment.c:821)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavecore/src/xzone/xzone_malloc.c:4186)"
- "vas_core_shadow_space_alloc"
- "vas_core_shadow_space_free"
- "vas_span_alloc( vas_self(), VAS_SPAN_BUMP_POPULATED | VAS_SPAN_WIRED | VAS_SPAN_NOSPLIT | VAS_SPAN_OPTOUT_SPANMAP, &config, &_ipmm_state.freed_frames.span)"
- "vas_span_alloc( vas_self(), VAS_SPAN_MANAGED | VAS_SPAN_NOSPLIT | VAS_SPAN_WRITE | VAS_SPAN_OPTOUT_SPANMAP, &config, &_ipmm_state.ipmm_retype_span)"
- "vcss == &_shadow_self()->shadow_space && _shadow_self()->move_caps != 0"

```
