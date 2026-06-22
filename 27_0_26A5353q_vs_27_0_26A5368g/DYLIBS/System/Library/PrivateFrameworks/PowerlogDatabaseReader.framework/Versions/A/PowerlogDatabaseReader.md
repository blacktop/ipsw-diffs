## PowerlogDatabaseReader

> `/System/Library/PrivateFrameworks/PowerlogDatabaseReader.framework/Versions/A/PowerlogDatabaseReader`

```diff

-3468.0.0.0.0
-  __TEXT.__text: 0xa94 sha256:95ccca2a86899c74fc5d283d043b631bda74f7d0b5893c8eaa10724b53bebe4b
-  __TEXT.__objc_methlist: 0x74 sha256:d28d43c5c6e46b73e3775e507c767a22d0f8394baa6a0f27fc7493dbb41f8a95
+3486.0.21.501.2
+  __TEXT.__text: 0xa90 sha256:77e3070311a62726cbb2774d853eaee88457bf4746ef4db7e900b70ad8089bc8
+  __TEXT.__objc_methlist: 0x74 sha256:f8489fdae465feb7f79cbabab66b74ecede9a154381f68e0aafa66f38fa78799
   __TEXT.__const: 0x40 sha256:31e787a269e977bbc60d359a7d64df58eff877cd2b2fe2c853aa311fbe487ab0
   __TEXT.__cstring: 0x251 sha256:c3cd5399f3f9bfaaf385c11cde568dffa45a0e815053b12d1410399fe9fb10c9
-  __TEXT.__unwind_info: 0x88 sha256:8ad76a553c56e737c37266b2c0d4a4461f8b17d81dc9cde4051b00f7ff03b9b1
+  __TEXT.__unwind_info: 0x88 sha256:71d7e3bea38baf60bc939306fa2e6bf121557e539878799cd52312d942a944eb
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__objc_classlist: 0x8 sha256:73f4a5421ac32e2d8d100fc5f92275405ce4d68dc75743241deba72b81bc74ac
+  __DATA_CONST.__objc_classlist: 0x8 sha256:cce6f20db25bdd38b43b2ded0d5768f34eef2c17a2a888ffbc61cfaff5734252
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0xc8 sha256:f62445592a65ac7109584050c6d45b2355b719fa65e02fca0a4f60e5e1df7ce3
-  __DATA_CONST.__objc_superrefs: 0x8 sha256:36fe46d655aa87535c83d6110dabb014126a950e947d29bf062e978d01bab602
+  __DATA_CONST.__objc_selrefs: 0xc8 sha256:599ce82b59da37138ea2f2f877f82e5a10f1be725e9792c1d352dd65745491e9
+  __DATA_CONST.__objc_superrefs: 0x8 sha256:f7b58ade6440385d008ea2a545520cb3822f2a1c9737cfa68ab2193b8fa66e57
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__cfstring: 0x260 sha256:7a0b81fa9d462d612dbbd3e8aebe0c5610b9b7cc261429d105880ea65f7c7793
-  __AUTH_CONST.__objc_const: 0xd0 sha256:5919f2d17bea35b5ea3be61188e66d3b79e81a9c85fdaee91b99dd4750e63a5f
+  __AUTH_CONST.__cfstring: 0x260 sha256:a06c74025511169b3c9a4619369374bbabcf4fb779101c4bd3d89c48714d9d1a
+  __AUTH_CONST.__objc_const: 0xd0 sha256:31e105cd1cc036570d4f5d63856872f8152fddc1af00eb202edbdcd647f7972f
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x50 sha256:e69f780873dc114c0e64dad230cbe19eebf3cca4d2e91d69b7736de898c5e32d
+  __AUTH.__objc_data: 0x50 sha256:1d2a9ce6965273545034ec8c07afdd5220396dde4ef6e72bd17f77bb7d97c4ea
   __DATA.__objc_ivar: 0x4 sha256:dc765660b06ee03dd16fd7ca5b957e8c805161ac2c4af28c5a100ab2ab432ca1
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: C2FE1A14-1BD6-3D5F-A861-401A732F086A
+  UUID: AB71827A-A373-3784-8997-4FDC8C9E260E
   Functions: 9
   Symbols:   75
   CStrings:  41
Functions:
~ -[PLDatabaseReader openDatabaseFile:] : sha256 3dd6dfd5dcd91abd5bf9060c0dc2f20425a126cf658a3e7d69e359c3242c6fda -> f398af0143ea9e2e10e9b798a16054b503f511719ea9694e224151d5f2c7bdd1
~ -[PLDatabaseReader initWithDatabaseFile:] : sha256 a55bde41c31648afe5647e2ce685a5059c3dcac97357b4a379323f6163ce1682 -> 976ba4ef0e193844faf62ce04138e52c531665bf9283dcda1f722054db4bd660
~ -[PLDatabaseReader dealloc] : sha256 683df705228ef4239b3a4f1bbf6c622d051254a6220f9e3c93aef1ea0a4e7a3e -> 288b2a3156e10c12fde6497ec94e074b6c00400f4db6fe88210ae3d67c8947d6
~ -[PLDatabaseReader prepareStatementAndPerformWithString:] : sha256 a0138c110849fef7f2ce6953c44243b3029d99cd4e3b95bf8eefd9e5890509dc -> def9e261d83bc5fdca4481129fb9b81c53530b443237a381bed7622e14c4d386
~ -[PLDatabaseReader performStatement:] : sha256 f0d990436fb3e35e4340c62af4cfe6735e725bae9385485a8ac585469ac4c1ab -> 0ce88391abf5c830b03f36cfc6ccba42cbe0a90237cc4de07cbae9d0e2c2323c
~ -[PLDatabaseReader tableNamesFromDatabase] : sha256 199952cd463f5d87e6b88c2de787aee79c30f30da2bfd7f2d41211eff1d2d33c -> 3ec3b65415fbd7b29637e6191985689eec87d5d0232f4386cf7fb133367462d9
~ -[PLDatabaseReader stringValueOfTable:] : 968 -> 964

```
