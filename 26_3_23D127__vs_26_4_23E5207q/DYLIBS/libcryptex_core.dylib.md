## libcryptex_core.dylib

> `/usr/lib/libcryptex_core.dylib`

```diff

-589.82.1.0.0
-  __TEXT.__text: 0x16190
-  __TEXT.__auth_stubs: 0xe00
+662.100.17.0.0
+  __TEXT.__text: 0x16cdc
+  __TEXT.__auth_stubs: 0xde0
   __TEXT.__objc_methlist: 0x444
   __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x18ca
-  __TEXT.__oslogstring: 0x2a4f
-  __TEXT.__gcc_except_tab: 0x2dc
-  __TEXT.__unwind_info: 0x4c0
+  __TEXT.__cstring: 0x1b92
+  __TEXT.__oslogstring: 0x2c29
+  __TEXT.__gcc_except_tab: 0x2cc
+  __TEXT.__unwind_info: 0x518
   __TEXT.__objc_classname: 0xcd
   __TEXT.__objc_methname: 0xab9
   __TEXT.__objc_methtype: 0x19e
   __TEXT.__objc_stubs: 0xa20
   __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0xb38
+  __DATA_CONST.__const: 0xfa0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_nlclslist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x328
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x710
+  __AUTH_CONST.__auth_got: 0x700
   __AUTH_CONST.__const: 0x258
   __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0xab0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x5c
-  __DATA.__data: 0x280
+  __DATA.__data: 0x298
   __DATA.__bss: 0x288
   __DATA_DIRTY.__objc_data: 0x280
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23F61AE1-DE58-3CDE-9CF4-0380B6647623
-  Functions: 420
-  Symbols:   1338
-  CStrings:  739
+  UUID: BCC45D9A-9B13-325B-B6A2-66C056046616
+  Functions: 429
+  Symbols:   1357
+  CStrings:  776
 
Symbols:
+ __chflags_flags
+ __cryptex_asset_type_asset_root
+ __cryptex_asset_type_content_root
+ _cryptex_asset_new_closed
+ _cryptex_asset_new_closed.cold.1
+ _cryptex_asset_new_closed.cold.2
+ _cryptex_asset_open_sealed
+ _cryptex_asset_open_sealed.cold.1
+ _cryptex_core_is_sealed
+ _fcntl
+ _objc_retainAutoreleasedReturnValue
+ _openat_authenticated_np
+ _os_flagset_copy_string
+ _xpc_dictionary_get_count
- _OUTLINED_FUNCTION_7
- __cryptex_asset_type_root
- _objc_claimAutoreleasedReturnValue
- _objc_release_x28
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x27
- _objc_retain_x3
CStrings:
+ "%s fd[%d] : [invalid descriptor]: %{darwin.errno}d"
+ "%s fd[%d]: type = %s, size = %lld, flags = %s, path = %s"
+ "%{public}s: Asset %s is not sealed: %{darwin.errno}d"
+ "%{public}s: FD for im4m is invalid. Cryptex is not personalized."
+ "%{public}s: FD for image is invalid %{darwin.errno}d"
+ "%{public}s: No image nor content asset was loaded from directory.: %{darwin.errno}d"
+ "%{public}s: cryptex type is not image: %lld %{darwin.errno}d"
+ "%{public}s: using provided SSO token"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Binaries/libcryptex/install/Symbols/libcryptex_core"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Sources/libcryptex/core/cryptex_core.c"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Sources/libcryptex/core/magister.c"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Sources/libcryptex/core/scrivener.c"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Sources/libcryptex/core/signature.c"
+ "/Library/Caches/com.apple.xbs/9F3B9D61-EB54-4E7B-B21D-A0A57311432A/TemporaryDirectory.R26HX9/Sources/libcryptex/core/tss.m"
+ "662.100.17"
+ "@(#)VERSION:Darwin Cryptex Core Interface Version 2.0.0: Thu Jan 29 21:17:11 PST 2026; root:libcryptex-662.100.17~18/libcryptex_core/RELEASE_ARM64E"
+ "Content"
+ "Darwin Cryptex Core Interface Version 2.0.0: Thu Jan 29 21:17:11 PST 2026; root:libcryptex-662.100.17~18/libcryptex_core/RELEASE_ARM64E"
+ "Ensuring same sealed volume as:"
+ "Opening sealed %{public}s asset at %{public}s"
+ "SF_APPEND"
+ "SF_ARCHIVED"
+ "SF_DATALESS"
+ "SF_FIRMLINK"
+ "SF_IMMUTABLE"
+ "SF_NOUNLINK"
+ "SF_RESTRICTED"
+ "S_IFBLK"
+ "S_IFCHR"
+ "S_IFDIR"
+ "S_IFIFO"
+ "S_IFLNK"
+ "S_IFREG"
+ "S_IFSOCK"
+ "Treating unsealed asset of type %{public}s as sealed (internal-only)."
+ "UF_APPEND"
+ "UF_COMPRESSED"
+ "UF_DATAVAULT"
+ "UF_HIDDEN"
+ "UF_IMMUTABLE"
+ "UF_NODUMP"
+ "UF_OPAQUE"
+ "UF_TRACKED"
+ "[%s]"
+ "[unknown]"
+ "cont"
+ "cryptex_core_set_assets_from_fds"
+ "openat: %{public}s: %{darwin.errno}d"
+ "openat_authenticated_np: %{public}s [no error]"
+ "openat_authenticated_np: %{public}s: %{darwin.errno}d"
- "%{public}s: FD for im4m is invalid: %{darwin.errno}d"
- "%{public}s: FD for image is invalid: %{darwin.errno}d"
- "%{public}s: No image asset was loaded from directory.: %{darwin.errno}d"
- "%{public}s: cryptex type is not image: %lld: %{darwin.errno}d"
- "/Library/Caches/com.apple.xbs/Binaries/libcryptex/install/Symbols/libcryptex_core"
- "/Library/Caches/com.apple.xbs/Sources/libcryptex/core/cryptex_core.c"
- "/Library/Caches/com.apple.xbs/Sources/libcryptex/core/magister.c"
- "/Library/Caches/com.apple.xbs/Sources/libcryptex/core/scrivener.c"
- "/Library/Caches/com.apple.xbs/Sources/libcryptex/core/signature.c"
- "/Library/Caches/com.apple.xbs/Sources/libcryptex/core/tss.m"
- "589.82.1"
- "@(#)VERSION:Darwin Cryptex Core Interface Version 2.0.0: Wed Jan 21 22:40:44 PST 2026; root:libcryptex-589.82.1~2/libcryptex_core/RELEASE_ARM64E"
- "Darwin Cryptex Core Interface Version 2.0.0: Wed Jan 21 22:40:44 PST 2026; root:libcryptex-589.82.1~2/libcryptex_core/RELEASE_ARM64E"

```
