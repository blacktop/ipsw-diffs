## MMCS

> `/System/Library/PrivateFrameworks/MMCS.framework/MMCS`

```diff

-2700.109.0.0.0
-  __TEXT.__text: 0x7f620
+2700.112.0.0.0
+  __TEXT.__text: 0x7f478
   __TEXT.__objc_methlist: 0xbe0
   __TEXT.__const: 0x9ac
   __TEXT.__oslogstring: 0x442c
-  __TEXT.__cstring: 0x177ed
-  __TEXT.__gcc_except_tab: 0x63c
-  __TEXT.__unwind_info: 0x1598
+  __TEXT.__cstring: 0x178c2
+  __TEXT.__gcc_except_tab: 0x384
+  __TEXT.__unwind_info: 0x15a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x53d0
+  __DATA_CONST.__const: 0x5410
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x898
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__got: 0x2c8
-  __AUTH_CONST.__const: 0x2d10
-  __AUTH_CONST.__cfstring: 0xcee0
+  __AUTH_CONST.__const: 0x2d88
+  __AUTH_CONST.__cfstring: 0xce80
   __AUTH_CONST.__objc_const: 0x11f0
-  __AUTH_CONST.__auth_got: 0xe68
+  __AUTH_CONST.__auth_got: 0xe88
   __AUTH.__data: 0x420
   __DATA.__objc_ivar: 0xa0
   __DATA.__data: 0x460

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2401
-  Symbols:   3495
-  CStrings:  2988
+  Functions: 2418
+  Symbols:   3510
+  CStrings:  2990
 
Symbols:
+ GCC_except_table20
+ GCC_except_table27
+ GCC_except_table32
+ GCC_except_table36
+ _MMCSHTTPContextAssertCurrent
+ _MMCSHTTPContextPerformBlockAsync
+ _MMCSHTTPContextPerformBlockSync
+ ___MMCSHTTPContextPerformBlockAsync_block_invoke
+ ___MMCSHTTPContextPerformBlockSync_block_invoke
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___mmcs_perform_run_loop_target_sync_block_invoke
+ ___mmcs_report_close_block_invoke
+ __os_crash
+ _dispatch_assert_queue$V2
+ _dispatch_assert_queue_not$V2
+ _dispatch_sync
+ _mmcs_container_recorded_completion_info_count
+ _mmcs_get_complete_create_request_body
+ _mmcs_http_context_copy_perform_target
+ _mmcs_perform_dispatch_target_assert_current
+ _mmcs_perform_dispatch_target_assert_current_debug
+ _mmcs_perform_dispatch_target_assert_not_current
+ _mmcs_perform_dispatch_target_assert_not_current_debug
+ _mmcs_perform_dispatch_target_sync
+ _mmcs_perform_run_loop_target_assert_current
+ _mmcs_perform_run_loop_target_assert_current_debug
+ _mmcs_perform_run_loop_target_assert_not_current
+ _mmcs_perform_run_loop_target_assert_not_current_debug
+ _mmcs_perform_run_loop_target_sync
+ _mmcs_perform_target_assert_not_current
+ _mmcs_perform_target_sync
+ _mmcs_request_queue_set_max_requests_inflight
+ _mmcs_request_queue_set_requests_inflight
+ _objc_retain_x24
- GCC_except_table1
- GCC_except_table11
- GCC_except_table21
- GCC_except_table28
- GCC_except_table34
- GCC_except_table4
- GCC_except_table9
- _HttpContextPerformBlockAsync
- _HttpContextPerformBlockSync
- ___39-[MMCSHTTPContext invalidateStreamPair]_block_invoke
- ___Block_byref_object_copy_
- ___Block_byref_object_dispose_
- ___HttpContextPerformBlockAsync_block_invoke
- ___HttpContextPerformBlockSync_block_invoke
- ___block_descriptor_48_e8_32r40r_e5_v8?0lr32l8r40l8
- ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_64_e8_32s_e5_v8?0ls32l8
- _kMMCSEnginePropertyTestMaxInflightContainerRequests
- _mmcs_request_queue_set_test_max_requests_inflight
- _mmcs_request_queue_set_test_requests_inflight
- _objc_release_x9
CStrings:
+ "MMCSHTTPContextAssertCurrent"
+ "MMCSHTTPContextPerformBlockAsync"
+ "MMCSHTTPContextPerformBlockSync"
+ "mmcs runloop: %@ invalid: calling completionHandler with NSURLSessionResponseCancel"
+ "mmcs runloop: %@ invalid: calling completionHandler with nil"
+ "mmcs runloop: %@ invalid: calling completionHandler with nil request"
+ "mmcs runloop: %@ unknown task %@. Expected %@: ignoring delegate callback"
+ "mmcs_container_recorded_completion_info_count"
+ "mmcs_get_complete_create_request_body"
+ "mmcs_perform_target: current thread is not executing on the expected run loop"
+ "mmcs_perform_target: current thread is unexpectedly executing on the run loop it must not be confined to"
+ "mmcs_perform_target_sync"
- "%@ invalid: calling completionHandler with NSURLSessionResponseCancel"
- "%@ invalid: calling completionHandler with nil"
- "%@ invalid: calling completionHandler with nil request"
- "%@ invalid: ignoring delegate callback"
- "%@ unknown task %@. Expected %@: ignoring delegate callback"
- "HttpContextPerformBlockAsync"
- "HttpContextPerformBlockSync"
- "getCompleteRequestBodyCreate"
- "kMMCSEnginePropertyTestMaxInflightContainerRequests"
- "mmcs runloop: %@ invalid. Returning nil body stream"
```
