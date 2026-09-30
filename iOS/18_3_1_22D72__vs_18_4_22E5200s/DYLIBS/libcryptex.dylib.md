## libcryptex.dylib

> `/usr/lib/libcryptex.dylib`

```diff

-475.80.3.0.0
-  __TEXT.__text: 0x25414
+493.100.42.0.0
+  __TEXT.__text: 0x25c1c
   __TEXT.__auth_stubs: 0x1370
   __TEXT.__objc_methlist: 0x490
-  __TEXT.__const: 0x7bd
+  __TEXT.__const: 0x7c5
   __TEXT.__gcc_except_tab: 0xf78
-  __TEXT.__oslogstring: 0x3d0b
-  __TEXT.__cstring: 0x1b99
-  __TEXT.__unwind_info: 0x5c0
+  __TEXT.__oslogstring: 0x3f36
+  __TEXT.__cstring: 0x1bb7
+  __TEXT.__unwind_info: 0x5d0
   __TEXT.__objc_classname: 0x140
   __TEXT.__objc_methname: 0x9da
   __TEXT.__objc_methtype: 0x360
   __TEXT.__objc_stubs: 0xa40
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x6a8
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x718
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_nlclslist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x78
   __AUTH_CONST.__auth_got: 0x9c8
-  __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__auth_ptr: 0x10
+  __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0xe18
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x30
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x1e0
-  __DATA_DIRTY.__data: 0x68
+  __DATA_DIRTY.__data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libcryptex_interface.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 477
-  Symbols:   978
-  CStrings:  824
+  Functions: 491
+  Symbols:   1014
+  CStrings:  836
 
Symbols:
+ __cryptex_get_core
+ _codex_interface_create_uninstall_request
+ _cryptex_attr_set_uninstall_flags
+ _cryptex_core_close
+ _cryptex_core_get_num_assets
+ _cryptex_core_open
+ _cryptex_remote_service_nonce_attr_set_ndom_handle
- __cryptex_actor_init_invoke_cstr
- __cryptex_uninstall_by_name
- _cryptex_subsystem_cryptex
- _cryptex_uninstall_pack
- _cryptex_uninstall_reply_unpack
- _memmove
CStrings:
+ "%{public}s: Build identity %lu (%{public}s) is not a cryptex. Skipping."
+ "%{public}s: Failed to open all cryptex assets"
+ "%{public}s: Performing nonce domain workaround, 0x5 mapped to 0x3"
+ "%{public}s: setting uninstall flags: %#llx"
+ "493.100.42"
+ "@(#)VERSION:Darwin Cryptex Interface Version 2.0.0: Sun Feb 16 10:33:32 PST 2025; root:libcryptex-493.100.42~129/libcryptex/RELEASE_ARM64E"
+ "B16@?0^{__CFError=}8"
+ "Darwin Cryptex Interface Version 2.0.0: Sun Feb 16 10:33:32 PST 2025; root:libcryptex-493.100.42~129/libcryptex/RELEASE_ARM64E"
+ "Error in response to uninstall request: %{public}@"
+ "Error unpacking uninstall response: %{darwin.errno}d"
+ "Failed to create uninstall request"
+ "Failed to get response to uninstall request."
+ "RemoteXPC error: %{public}s"
+ "UNINSTALL:ERROR_DICT"
+ "Unexpected response to uninstall request: %s"
+ "XPC error in response to uninstall request: %s"
+ "assertion failure: \"dict != ((void *)0)\" -> %llu"
+ "assertion failure: \"matches.count <= 1\" -> %llu"
+ "assertion failure: \"self->service\" -> %llu"
+ "canceling RXPC connection '%{public}@'"
+ "cryptex_uninstall"
+ "establish RXPC connection '%{public}@'"
+ "failed to copy cryptex from bundle [no error]"
+ "failed to copy cryptex from bundle: %@"
+ "got reply: %{public}s"
+ "remote device %{public}s disconnected"
+ "remote service install response doesn't have key '%{public}s'"
+ "sending request: %{public}s"
- "%{public}s: uninstall rpc: %{darwin.errno}d"
- "475.80.3"
- "@(#)VERSION:Darwin Cryptex Interface Version 2.0.0: Thu Jan 16 05:18:55 PST 2025; root:libcryptex-475.80.3~402/libcryptex/RELEASE_ARM64E"
- "Darwin Cryptex Interface Version 2.0.0: Thu Jan 16 05:18:55 PST 2025; root:libcryptex-475.80.3~402/libcryptex/RELEASE_ARM64E"
- "RemoteXPC error: %s"
- "assertion failure: \"dict != ((void *)0)\" -> %lld"
- "assertion failure: \"matches.count <= 1\" -> %lld"
- "assertion failure: \"self->service\" -> %lld"
- "canceling RXPC connection %{public}@"
- "establish RXPC connection %{public}@"
- "failed to copy cryptex from bundle"
- "got reply: %s"
- "remote device %s disconnected"
- "remote service install response doesn't have key %s"
- "sending request: %s"
- "unexpected failure: not implemented"

```
