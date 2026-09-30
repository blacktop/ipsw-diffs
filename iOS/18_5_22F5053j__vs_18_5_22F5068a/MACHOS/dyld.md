## dyld

> `/System/ExclaveKit/usr/lib/dyld`

```diff

 1285.17.0.0.0
-  __TEXT.__text: 0x502fc
+  __TEXT.__text: 0x50188
   __TEXT.__const: 0x1b951
-  __TEXT.__cstring: 0xcc24
-  __TEXT.__unwind_info: 0x7a8
+  __TEXT.__cstring: 0xcc47
+  __TEXT.__unwind_info: 0x7a0
   __DATA_CONST.__auth_ptr: 0x48
   __DATA_CONST.__const: 0x47a0
   __DATA.__data: 0x1160

   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
   __DATA.__common: 0x5b0
-  __DATA.__bss: 0xb0478
+  __DATA.__bss: 0xb09b8
   __DATA_DIRTY.__all_image_info: 0x170
-  Functions: 2389
-  Symbols:   2682
+  Functions: 2387
+  Symbols:   2678
   CStrings:  1363
 
Symbols:
+ __thread_local_ipc_buffer_payload_storage
+ _thread_local_ipc_buffer_payload_storage.cold.1
+ _thread_local_ipc_buffer_payload_storage_static.ek_dyld_bufs
- __tb_ipc_buffer_constructor
- __tb_ipc_buffer_destructor
- _init_tss_key_once.cold.1
- _init_tss_key_once.init_x
- _tb_ipc_buffer_constructor.cold.1
- _tb_local_msg_buffer_destruct.cold.5
- _xrt_thread_tss_set
- xrt_thread_tss_set.cold.1
CStrings:
+ "/AppleInternal/Library/BuildRoots/211c1991-1d94-11f0-9801-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.iPhoneOS.platform/Developer/SDKs/ExclaveKit.iPhoneOS18.5.Internal.sdk/System/ExclaveKit/usr/include/xrt/thread.h"
+ "_thread_local_ipc_buffer_payload(): too many static threads"
- "/AppleInternal/Library/BuildRoots/87b999e9-1354-11f0-8366-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.iPhoneOS.platform/Developer/SDKs/ExclaveKit.iPhoneOS18.5.Internal.sdk/System/ExclaveKit/usr/include/xrt/thread.h"
- "XRT_UNLIKELY(count != 0)"

```
