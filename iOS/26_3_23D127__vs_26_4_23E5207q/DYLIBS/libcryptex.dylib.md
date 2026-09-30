## libcryptex.dylib

> `/usr/lib/libcryptex.dylib`

```diff

-589.82.1.0.0
-  __TEXT.__text: 0x25d34
-  __TEXT.__auth_stubs: 0x13d0
+662.100.17.0.0
+  __TEXT.__text: 0x26014
+  __TEXT.__auth_stubs: 0x13c0
   __TEXT.__objc_methlist: 0x490
-  __TEXT.__const: 0x7c0
-  __TEXT.__gcc_except_tab: 0xf8c
-  __TEXT.__cstring: 0x1cde
-  __TEXT.__oslogstring: 0x402c
-  __TEXT.__unwind_info: 0x5c8
+  __TEXT.__const: 0x7c8
+  __TEXT.__gcc_except_tab: 0xf5c
+  __TEXT.__cstring: 0x1f62
+  __TEXT.__oslogstring: 0x40b0
+  __TEXT.__unwind_info: 0x638
   __TEXT.__objc_classname: 0x140
   __TEXT.__objc_methname: 0x9e0
   __TEXT.__objc_methtype: 0x360

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x9f8
+  __AUTH_CONST.__auth_got: 0x9f0
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0xe18

   - /usr/lib/libcryptex_interface.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F6C5421E-B112-35B2-8398-45D74E158A67
-  Functions: 490
-  Symbols:   1755
-  CStrings:  855
+  UUID: E2ABA1FE-3124-3E5D-870E-C24A1EEE61BF
+  Functions: 507
+  Symbols:   1792
+  CStrings:  857
 
Symbols:
+ _OUTLINED_FUNCTION_11
+ ___cryptex_server_lookup_endpoint_block_invoke
+ _cryptex_server_lookup_endpoint
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
+ _objc_retain_x26
- ___cryptex_inventory_lookup_endpoint_block_invoke
- __hdi_copy_device_nodes.cold.6
- _cryptex_inventory_lookup_endpoint
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
CStrings:
+ "%{public}s: Failed to compute digest for asset %{public}s: %{darwin.errno}d"
+ "%{public}s: Failed to create xpc data: %{darwin.errno}d"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Binaries/libcryptex/install/Symbols/libcryptex"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Sources/libcryptex/hlutil/img4_xpc.m"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Sources/libcryptex/src/bundle.c"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Sources/libcryptex/src/cryptex.c"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Sources/libcryptex/src/cryptex_mount.m"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Sources/libcryptex/src/cryptex_server.m"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Sources/libcryptex/src/event.m"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Sources/libcryptex/src/remote_service.m"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Sources/libcryptex/src/signing_service.c"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Sources/libcryptex/src/simple_session.m"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Sources/libcryptex/util/xpc.c"
+ "662.100.17"
+ "@(#)VERSION:Darwin Cryptex Interface Version 2.0.0: Thu Jan 29 21:17:19 PST 2026; root:libcryptex-662.100.17~18/libcryptex/RELEASE_ARM64E"
+ "Darwin Cryptex Interface Version 2.0.0: Thu Jan 29 21:17:19 PST 2026; root:libcryptex-662.100.17~18/libcryptex/RELEASE_ARM64E"
+ "HashMethod"
+ "cryptex_server_lookup_endpoint_block_invoke"
- "/Library/Caches/com.apple.xbs/Binaries/libcryptex/install/Symbols/libcryptex"
- "/Library/Caches/com.apple.xbs/Sources/libcryptex/hlutil/img4_xpc.m"
- "/Library/Caches/com.apple.xbs/Sources/libcryptex/src/bundle.c"
- "/Library/Caches/com.apple.xbs/Sources/libcryptex/src/cryptex.c"
- "/Library/Caches/com.apple.xbs/Sources/libcryptex/src/cryptex_mount.m"
- "/Library/Caches/com.apple.xbs/Sources/libcryptex/src/event.m"
- "/Library/Caches/com.apple.xbs/Sources/libcryptex/src/inventory.m"
- "/Library/Caches/com.apple.xbs/Sources/libcryptex/src/remote_service.m"
- "/Library/Caches/com.apple.xbs/Sources/libcryptex/src/signing_service.c"
- "/Library/Caches/com.apple.xbs/Sources/libcryptex/src/simple_session.m"
- "/Library/Caches/com.apple.xbs/Sources/libcryptex/util/xpc.c"
- "589.82.1"
- "@(#)VERSION:Darwin Cryptex Interface Version 2.0.0: Wed Jan 21 22:40:50 PST 2026; root:libcryptex-589.82.1~2/libcryptex/RELEASE_ARM64E"
- "Darwin Cryptex Interface Version 2.0.0: Wed Jan 21 22:40:50 PST 2026; root:libcryptex-589.82.1~2/libcryptex/RELEASE_ARM64E"
- "cryptex_inventory_lookup_endpoint_block_invoke"
- "unexpected failure: bsd name not present as string in whole disk node"

```
