## cupsd

> `/usr/sbin/cupsd`

```diff

-522.5.0.0.0
-  __TEXT.__text: 0x42e7c sha256:10ae49d90a9a57285d6d1bfc9e912b5271b0b3a9a76b44a04b49596c46d6bb3a
-  __TEXT.__auth_stubs: 0x1f10 sha256:1a7b47092c2af274536110ceb7d88b0269743d563f468c83572524e62c84b994
-  __TEXT.__cstring: 0x11612 sha256:02e62cb015aae7373241b6a8272751ad53ca2fe145c4f8dce0dc8520cd9b996b
+522.7.0.0.0
+  __TEXT.__text: 0x4314c sha256:0d0df5654faa9afb2528df4f64751d068b4cacf9018da3056d15b3f3a95d03fd
+  __TEXT.__auth_stubs: 0x1f20 sha256:ed25ee70c54b4c57dc8a4b396dad926d44591fab9a9166ba6f23f1867d6f9619
+  __TEXT.__cstring: 0x1178f sha256:252a928fa2315cde09b1094495bd45ecc3ace60adc685962e30529f3b6b42be3
   __TEXT.__const: 0x340 sha256:b194a63b925361f4678b8e64680ccebcee6898a0682632f9753e581d85829edd
   __TEXT.__oslogstring: 0x24 sha256:0e8b82d4db1e716b8381bec23fa8b1600e809840545b1ba4153471c3c1556604
-  __TEXT.__unwind_info: 0x568 sha256:e8a5d34bd53ac0cac0e151753adb7835c728682a2a5d3ecf297d34e6a40e780e
-  __DATA_CONST.__auth_got: 0xf88 sha256:ddf59c17b75c7a76bd27fdbb8014ac1feb5701eb82c85fcb571ee74222404e30
-  __DATA_CONST.__got: 0x120 sha256:2b8ec34e17063f63e138c6c47cb1ed3d1aded2927db8cd7dea0c36286d94f7af
-  __DATA_CONST.__auth_ptr: 0x78 sha256:05244e7c471d9447c368742234783fc9cef9a880b3fdb6aa9b539d410045cd2d
-  __DATA_CONST.__const: 0xdc0 sha256:51aba38f9fecdcab30a074466bc2bc1f1a9523487f8a3aabf5fb073c291dbd1c
-  __DATA_CONST.__cfstring: 0xc0 sha256:e66ac1586122e9fc0f528fb23b3486d03dbb260f3f002228d8a8b855d5751f0d
+  __TEXT.__unwind_info: 0x588 sha256:e97314a79e5cd40f91d69b85d58ead422730f6ab9a1f73c22647137e18797885
+  __DATA_CONST.__auth_got: 0xf90 sha256:a92a810d260ced5e5b0c79bb02c5caa78f5d1e4119af33559ecc386cb3697425
+  __DATA_CONST.__got: 0x120 sha256:9a230d416724e6f11705f6756693cb950a11195f21cd4bf76c474b8e697be3df
+  __DATA_CONST.__auth_ptr: 0x78 sha256:e5c90df1f98a77d1525b6f26fc8c5d8aa70e6e30f37e09623aedf478a335e47b
+  __DATA_CONST.__const: 0xdc0 sha256:3ff0231e86d3d24467fa10c3ba221ae7b35d1902d9b0a582ce2ddb5e727d67ee
+  __DATA_CONST.__cfstring: 0xc0 sha256:d3f86d464d3d9f6b0526009d784ff600d29997eaba47bc18a25f98276d0b944c
   __DATA.__data: 0x224 sha256:c44e7f7dffaa01fd2a0d68aaef3b198c2b2efd05ec72e1c1dfd877b1d0ba001e
   __DATA.__bss: 0x891 sha256:9fe14829d6952967d55af5fc7e22c02a4b003e9907fcef5187985226ef50d72d
   __DATA.__common: 0x4a0 sha256:7081ba3d8887be22551f56b5f50da675bda7dd02f40e9fcb150ac84fccbe387f

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 16E1FDD4-09A7-3AC5-9FBD-A07EF2CF42CB
-  Functions: 404
-  Symbols:   531
-  CStrings:  2704
+  UUID: E68A66D6-21C6-3004-850B-6120F122D0D6
+  Functions: 413
+  Symbols:   532
+  CStrings:  2710
 
Symbols:
+ _httpSchemeFromURI
CStrings:
+ "Empty or NULL printer name rejected."
+ "Invalid character (0x%02x) in printer name \"%s\""
+ "Printer name too long (%zu chars, max 127): \"%s\""
+ "Skipping keyword with invalid name \"%s\" and/or value \"%s\" for %s"
+ "Stopping job because support for device URIs with the file: scheme is not enabled."
+ "Unable to add printer \"%s\" - skipping entry in printers.conf"
+ "Unable to print due to a bad device URI scheme"
- "%254[^:]"

```
