## GSSCred

> `/System/Library/Frameworks/GSS.framework/Helpers/GSSCred`

```diff

-710.0.0.0.0
-  __TEXT.__text: 0x1aeb8
+710.0.1.0.0
+  __TEXT.__text: 0x1b8e0
   __TEXT.__auth_stubs: 0x1000
   __TEXT.__objc_stubs: 0xb00
   __TEXT.__objc_methlist: 0x2bc
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x260
   __TEXT.__cstring: 0x1398
-  __TEXT.__oslogstring: 0xfb7
+  __TEXT.__oslogstring: 0x12c2
   __TEXT.__objc_classname: 0x93
   __TEXT.__objc_methname: 0x8c3
   __TEXT.__objc_methtype: 0x25c
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x308
+  __TEXT.__unwind_info: 0x310
   __DATA_CONST.__auth_got: 0x810
   __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__const: 0xae0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 632CFA8F-E38B-3072-99D8-59DFBA3A396D
-  Functions: 280
+  UUID: 2A1EBBC4-5519-3381-94BB-4B7344683473
+  Functions: 282
   Symbols:   325
-  CStrings:  639
+  CStrings:  654
 
CStrings:
+ "Blob size calculation would overflow"
+ "Decryption failed: Blob too small for authentication tag"
+ "Decryption failed: Blob too small for wrapped key data (need %u bytes, have %zu)"
+ "Decryption failed: Blob too small for wrapped key size"
+ "Decryption failed: CCCryptorGCMOneshotDecrypt error: %d"
+ "Decryption failed: Error unwrapping key: %d"
+ "Decryption failed: Failed to allocate memory for plaintext"
+ "Decryption failed: Failed to allocate memory for tag"
+ "Decryption failed: Input blob is NULL"
+ "Decryption failed: Input is not NSData"
+ "Decryption failed: Invalid unwrapped key size: %d (expected 32)"
+ "Decryption failed: Invalid wrapped key size: %u (maximum allowed: %d)"
+ "Decryption failed: Not enough data for IV (need %zu bytes, have %zu)"
+ "Encryption error: %d"
+ "Failed to allocate memory for blob"
+ "Wrapped key size error: %d"
- "Error with unwrap key: %d"

```
