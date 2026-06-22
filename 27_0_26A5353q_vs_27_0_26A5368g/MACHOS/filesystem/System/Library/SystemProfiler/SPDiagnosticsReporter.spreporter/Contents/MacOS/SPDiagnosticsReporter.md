## SPDiagnosticsReporter

> `/System/Library/SystemProfiler/SPDiagnosticsReporter.spreporter/Contents/MacOS/SPDiagnosticsReporter`

```diff

 122.0.0.0.0
-  __TEXT.__text: 0x1720 sha256:4194a9edaad2b3812c66886b11d4d5d8c9d1c1855528a3693e537d9857d443cb
+  __TEXT.__text: 0x1704 sha256:df887f6442bb0e9c719c03c3cf3b53a7bd95ef725b702f65c769757de2cd4b81
   __TEXT.__auth_stubs: 0x170 sha256:9605f550a305818e64072de493ef9f0c3935d7436b5c53d09916aa0463649cce
   __TEXT.__objc_stubs: 0x580 sha256:45e82c9ae1cb2cad97aaa78ef19474647d80889862be98d0f8472687f618527c
-  __TEXT.__objc_methlist: 0xf4 sha256:314add35fa32adbb18b0e719d7d898efccb07843cb749871c94acd971cea8c80
+  __TEXT.__objc_methlist: 0xf4 sha256:09893b955bfacac08f6e528dba2250349fc991bb0c1f8e86cde008e037aae157
   __TEXT.__const: 0x8 sha256:aae5da9a50bad414bd1e1de0e32c6bec00f35db06e63c6271d3687572e85f373
   __TEXT.__cstring: 0x25e sha256:2e2227aa89089f9e911054270f8e1e9cca064d258af656000586525643c620c3
   __TEXT.__objc_classname: 0x35 sha256:00b6b72b558790ffbd08a4061eebc9dcc6c6ed891b1d493bef97b9d82ff37866
   __TEXT.__objc_methname: 0x3e6 sha256:9361865b5a39239efbdf36b1a2fab9f22185e343c57fe082f93f9cdf5f6ee748
   __TEXT.__objc_methtype: 0x9f sha256:6b084baa365274590284fa1c5e5cdf18f5f7443cab3348ab17873cff52f316ad
-  __TEXT.__unwind_info: 0x98 sha256:6bd3ba1a9d8197c2534f30655eb0536b22896afe4a3fcd0df170d1d5d830a963
-  __DATA_CONST.__cfstring: 0x520 sha256:3c8033aa19d157e4b7a67f0f07033d97860a216f074a7aab40a343774e8f6392
+  __TEXT.__unwind_info: 0x98 sha256:a1284b7e0013a4d0765d0a4d86205f0187712e346bc4de8739abe6672497ea72
+  __DATA_CONST.__cfstring: 0x520 sha256:e16988523bd70bc553db5c535862b910a358b71503b1feb13bed50672236a61e
   __DATA_CONST.__objc_classlist: 0x18 sha256:127a884f384b833e2c6688556c0de6dd042a481017176534b3a81a4f5c20da5e
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
   __DATA_CONST.__objc_superrefs: 0x8 sha256:fada7cee5503c8a21aa66872e345395738842ebaf6e65603924fc178cdd25562
   __DATA_CONST.__auth_got: 0xc0 sha256:57faf070a9884cb6742d7fd788b2bb6c7d2f0da31db6324d46e0912ea4cb397d
   __DATA_CONST.__got: 0x48 sha256:e6cb332e93e87f0a97f61240e5fbc1d8c7a5401f2d2aaaa630c5e3bb48dd4c16
-  __DATA.__objc_const: 0x278 sha256:7f134d660e45decedf4f1fcc57d991d2216260663226bf093a05ad9e7b00de60
-  __DATA.__objc_selrefs: 0x198 sha256:c387576f3938a4e370c53355a1cef79f6c9879d4b20dd5aecf40657f5311fad8
+  __DATA.__objc_const: 0x278 sha256:f74b6a7b8d0fc63edba25fd9612ce488a52ab7a9cc3ec5cb2bb89dc99f925821
+  __DATA.__objc_selrefs: 0x198 sha256:0b53198aa11204cbfd20639c9e6e269775456c30ff1fe275e920e413069ae48b
   __DATA.__objc_ivar: 0x18 sha256:52a93e9644306479e2f67ec8319798d1a40b93e480878399afe3e8355dcdc8df
   __DATA.__objc_data: 0xf0 sha256:cc70766568f340fc3f7d9083dcfaed37368493749c4eb593eba1f2411ec78896
   __DATA.__bss: 0x5 sha256:8855508aade16ec573d21e6a485dfd0a7624085c1a14b5ecdd6485de0c6839a4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A405D632-95A0-38F0-A9E8-563F03C0DF82
+  UUID: 706E6445-23AA-3171-BB67-98F4B2CA3CBE
   Functions: 19
   Symbols:   128
   CStrings:  164
Functions:
~ -[SPDiagnosticsPOST memoryDictionary] : 3212 -> 3148
~ -[SPDiagnosticsPOST postDictionary] : sha256 305d97f9fe2598e466cf1fbdd6a37f2f3e26618d6716782b3fa8209d706391d2 -> ae9688a12e56cdf96c5ba21e23d24d17eb1e011e0a52454a451ac8b788a0538d
~ -[SPDiagnosticsPOST smbiosPostDictionary] : sha256 bdc8d3e294d2d7096f8067c5c3e591bc72f1ada19af3324eb37b39b9adfba42a -> c52f23862b32f0157d4380a67ed07bda19934f028a4ffb5318e5018b0992213c
~ -[SmbiosParser getTheSmbiosTable] : sha256 7ca8bfd2cf145398d83dff1f46babc7cbc6aa13a2b486dc5d2dad5941f399485 -> b4872f30f42be32194c1d2837f65a9c26b7459c9781ca74609f5ac0679335b05
~ -[SmbiosParser initialize] : 188 -> 204
~ -[SmbiosParser getSmbiosByType:occurence:] : 72 -> 80
~ -[SmbiosParser getSmbiosByHand:] : 52 -> 60
~ -[SmbiosParser getSmbiosStr:number:] : 72 -> 76
~ -[SmbiosParser getAttribute:forRecord:] : sha256 81d5167882b7e5aae53a127c60abbcc85d819c3073662122aedd37d1ba2e305f -> 9d81aace7b0feb7f53d4bc02c296a7db75dc547cb573aaf42d471b7b00a3e53a
~ -[SmbiosParser getAttribute:forHandle:] : sha256 db07ab4fae7b7e24cebc4a0b8fd0c906a66386b385df6f119bb04e1d661d2cc7 -> 2c9a2517c331905b36537cc54edb3e1b6a67a847b12bffdb8c9d3f24aba55658
~ -[SmbiosParser getAttribute:forType:occurence:] : sha256 4ee9c9aa5e6ea377cf4caf2cf51de64e1479aec182275238c7e1850908664a82 -> 59cde815b753352326e60b67979e8e3e4af572da94d4824d28fb9eafff753a86
~ -[SPDiagnosticsReporter diagsDictionary:] : sha256 055425fd420575f1e8748a933e1310abeda1769f673fc4e144702475901dab68 -> 08e8f9de8b2e376b327ce1e7cd7355c346dcd15622296ed7be240b78cc513f11
~ -[SPDiagnosticsReporter updateDictionary:] : sha256 69cccb26ac4bb8dbc177bfb8b5a4a106b7838eacb6cbe8eb7302e8566b6d9534 -> 9d79769a85a7fdcc0eda2aec8a1f69fb0ae39866bea2d8b35f4653f082ec25d4

```
