## libcryptex_core.dylib

> `/usr/lib/libcryptex_core.dylib`

```diff

-475.80.3.0.0
-  __TEXT.__text: 0x151b4
-  __TEXT.__auth_stubs: 0xd70
+493.100.42.0.0
+  __TEXT.__text: 0x15e60
+  __TEXT.__auth_stubs: 0xdf0
   __TEXT.__objc_methlist: 0x444
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x16b4
-  __TEXT.__oslogstring: 0x286a
-  __TEXT.__gcc_except_tab: 0x264
-  __TEXT.__unwind_info: 0x470
+  __TEXT.__const: 0x140
+  __TEXT.__cstring: 0x18bd
+  __TEXT.__oslogstring: 0x29a6
+  __TEXT.__gcc_except_tab: 0x2dc
+  __TEXT.__unwind_info: 0x4b8
   __TEXT.__objc_classname: 0xcd
   __TEXT.__objc_methname: 0xaa0
   __TEXT.__objc_methtype: 0x19b
   __TEXT.__objc_stubs: 0xa20
-  __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0xb20
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__const: 0xb38
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_nlclslist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x320
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x6c8
-  __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x238
-  __AUTH_CONST.__cfstring: 0x520
+  __AUTH_CONST.__auth_got: 0x708
+  __AUTH_CONST.__auth_ptr: 0x20
+  __AUTH_CONST.__const: 0x258
+  __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0xab0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x280
-  __DATA.__bss: 0x278
+  __DATA.__bss: 0x288
   __DATA_DIRTY.__objc_data: 0x280
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 402
-  Symbols:   787
-  CStrings:  682
+  Functions: 416
+  Symbols:   809
+  CStrings:  695
 
Symbols:
+ __Block_copy
+ __Block_release
+ _cryptex_asset_close
+ _cryptex_asset_is_open
+ _cryptex_asset_open
+ _cryptex_core_close
+ _cryptex_core_get_num_assets
+ _cryptex_core_metadata_matches
+ _cryptex_core_metadata_matches_xattrs
+ _cryptex_core_open
+ _cryptex_core_select_chip
+ _cryptex_core_write_metadata_to_xattrs
+ _cryptex_magister_authenticate_f
+ _cryptex_metadata_read_from_cryptex
+ _cryptex_metadata_read_from_file_xattrs
+ _cryptex_metadata_write_to_file_xattrs
+ _image4_trust_destroy
+ _kAMAuthInstallApParameterSiKA
+ _objc_release_x1
+ _objc_release_x28
+ _objc_retain_x27
+ _open
+ _xpc_equal
- _signature_metadata_read_from_cryptex
- _signature_metadata_read_from_file
CStrings:
+ "%{public}s: Closed all assets from cryptex"
+ "%{public}s: Failed to open asset '%{public}s': %{darwin.errno}d"
+ "%{public}s: Opened all assets from cryptex"
+ "%{public}s: failed to get cryptex metadata %{darwin.errno}d"
+ "%{public}s: failed to read cryptex metadata from %s %{darwin.errno}d"
+ "%{public}s: failed to write cryptex metadata to %s %{darwin.errno}d"
+ "%{public}s: realpath %{darwin.errno}d"
+ "/Library/Caches/com.apple.xbs/Sources/libcryptex/core/cryptex_core.c"
+ "493.100.42"
+ "@(#)VERSION:Darwin Cryptex Core Interface Version 2.0.0: Sun Feb 16 10:33:21 PST 2025; root:libcryptex-493.100.42~129/libcryptex_core/RELEASE_ARM64E"
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "Darwin Cryptex Core Interface Version 2.0.0: Sun Feb 16 10:33:21 PST 2025; root:libcryptex-493.100.42~129/libcryptex_core/RELEASE_ARM64E"
+ "Failed to apply xattr '%s'.: %{darwin.errno}d"
+ "Invalid metadata.: %{darwin.errno}d"
+ "Unexpected value for cryptex_metadata key '%s': %{darwin.errno}d"
+ "com.apple.security.cryptex.tatsu"
+ "cryptex_core_metadata_matches"
+ "cryptex_core_metadata_matches_xattrs"
+ "cryptex_core_write_metadata_to_xattrs"
+ "failed to map file into memory: %{darwin.errno}d"
+ "failed to stat file: %{darwin.errno}d"
+ "metadata"
+ "realpath_np failed: %{darwin.errno}d"
+ "tss request failed: [%d] %{public}s"
+ "v40@?0^{_cryptex_magister={_cryptex_base={_os_object_header=^vii}Q^{dispatch_queue_s}^{dispatch_queue_s}^?i}{_object_proto=**^{os_log_s}}Q^{_cryptex_core}^{_cryptex_signature}^{_cryptex_host}^{_img4_chip}{_img4_nonce=S[48C]I}}8r^{_cryptex_asset_type=Q^?^?qI**}16^{_buff=(?=**^v^v)(?=Qq)^vQ^v^?^?}24^{__CFError=}32"
- "%{public}s: Failed to apply xattr '%s'.: %{darwin.errno}d"
- "%{public}s: Signature has invalid metadata.: %{darwin.errno}d"
- "%{public}s: Unexpected value for metadata key '%s': %{darwin.errno}d"
- "%{public}s: failed to map asset into memory: %s: %{darwin.errno}d"
- "%{public}s: failed to stat object: %s: %{darwin.errno}d"
- "%{public}s: tss request failed: [%d] %{public}s %{darwin.errno}d"
- "475.80.3"
- "@(#)VERSION:Darwin Cryptex Core Interface Version 2.0.0: Thu Jan 16 05:18:42 PST 2025; root:libcryptex-475.80.3~402/libcryptex_core/RELEASE_ARM64E"
- "B24@?0r*8^v16"
- "Darwin Cryptex Core Interface Version 2.0.0: Thu Jan 16 05:18:42 PST 2025; root:libcryptex-475.80.3~402/libcryptex_core/RELEASE_ARM64E"
- "http://gs.apple.com"
- "signature_metadata"

```
