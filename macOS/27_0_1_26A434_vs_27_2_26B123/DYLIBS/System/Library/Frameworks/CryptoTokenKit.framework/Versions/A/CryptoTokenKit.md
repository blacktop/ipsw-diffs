## CryptoTokenKit

> `/System/Library/Frameworks/CryptoTokenKit.framework/Versions/A/CryptoTokenKit`

```diff

-878.0.13.0.0
-  __TEXT.__text: 0x73ae4
+878.40.5.0.0
+  __TEXT.__text: 0x74024
   __TEXT.__delay_helper: 0x1f0
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0x55b8
-  __TEXT.__const: 0x7d1
-  __TEXT.__cstring: 0x3bee
-  __TEXT.__oslogstring: 0x7433
+  __TEXT.__objc_methlist: 0x55c0
+  __TEXT.__const: 0x7e1
+  __TEXT.__cstring: 0x3bfe
+  __TEXT.__oslogstring: 0x75a3
   __TEXT.__gcc_except_tab: 0x1510
   __TEXT.__swift5_typeref: 0x2a9
   __TEXT.__swift5_capture: 0x310

   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x1e78
+  __TEXT.__unwind_info: 0x1e80
   __TEXT.__eh_frame: 0x738
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ac0
+  __DATA_CONST.__objc_selrefs: 0x2ad0
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x2b8
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x7d0
   __AUTH_CONST.__const: 0x2d88
-  __AUTH_CONST.__cfstring: 0x3d20
+  __AUTH_CONST.__cfstring: 0x3d40
   __AUTH_CONST.__objc_const: 0x9a80
   __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_intobj: 0x5e8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0xc10
   __AUTH_CONST.__auth_ptr: 0x168
-  __AUTH.__objc_data: 0x15a8
+  __AUTH.__objc_data: 0x978
   __AUTH.__data: 0x240
   __DATA.__objc_ivar: 0x5e8
   __DATA.__data: 0xf08
-  __DATA.__bss: 0x890
+  __DATA.__bss: 0x8a0
   __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0xd70
+  __DATA_DIRTY.__objc_data: 0x19a0
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0x2a8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2947
-  Symbols:   5408
-  CStrings:  1330
+  Functions: 2955
+  Symbols:   5412
+  CStrings:  1337
 
Symbols:
+ +[TKKeybagSupport keybagNeedsPairing:tokenID:]
+ _block_invoke.gsmakDataBytes
+ _gsmakData
+ _objc_msgSend$caseInsensitiveCompare:
CStrings:
+ "gsmak"
+ "gsmak not supported, attempt to read its public key failed, error %08x"
+ "keybagNeedsPairing: failed to get token info: %x"
+ "keybagNeedsPairing: token %{public}@ is not registered, pairing needed"
+ "keybagNeedsPairing: token %{public}@ is registered with flags %llu"
+ "keybagNeedsPairing: tokenID is required"
+ "pairKeybag: legacy registration found, migrating to PKI token protocol"
```
