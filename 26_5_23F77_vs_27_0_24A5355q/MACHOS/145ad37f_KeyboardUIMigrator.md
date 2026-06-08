## KeyboardUIMigrator

> `/System/Library/DataClassMigrators/KeyboardUIMigrator.migrator/KeyboardUIMigrator`

```diff

-9126.5.5.2.102
-  __TEXT.__text: 0x280 sha256:df0f4f319bcaa0055bdbc783e29988d53469751c5e7b42f410cd69e857ebe002
-  __TEXT.__auth_stubs: 0x60 sha256:e3c7ab4163b026dae39974dcc7f2684d9419202cc48f1e35072d0e4f03256821
-  __TEXT.__objc_stubs: 0x100 sha256:c72ad79e53462034bbc134985feedf9bc4b504f263f3c8ff690017cded4ef31c
-  __TEXT.__objc_methlist: 0x44 sha256:c3a626b4005d2303e46e8eec9af09eb4206d6578fd4b9fc96cdbbab1fbb31ef9
+9127.0.66.1.102
+  __TEXT.__text: 0x288 sha256:2f9d0fd33201bd62c961ac2dc940ffeb22493ef5341f39bd42b7e153cfabe8cd
+  __TEXT.__auth_stubs: 0x60 sha256:4ff02f36cd7655e7e522d304a3a64bdab29ddb2652734fabb12c58bfc891ea5b
+  __TEXT.__objc_stubs: 0x100 sha256:e69fa831b768852fadda0075cdd4c6ce3e68d2b1a2a5011f4a28bdbb08f095d2
+  __TEXT.__objc_methlist: 0x44 sha256:f4ae812db13cb67720326de027e52985e270ae18775074ab50d01b2bf9b4ab32
   __TEXT.__const: 0x18 sha256:fa2902b3a8ca8a7d1b1aa3503b77df4fc3e87bc11e029686af129a318d6830bc
   __TEXT.__objc_methname: 0xb6 sha256:96ca81cf869d044f2d61983a2c9267c02b87f7eae5ef419e92e5bc4f4f2570fc
   __TEXT.__cstring: 0x49 sha256:f89d2e8db413315ea15118faa19f1af6b169738100cd3814ff2f4a79b827d601
   __TEXT.__objc_classname: 0x13 sha256:395f12bea31257275c2bd0b6537ffbcb80776fcbf023fa500196eb43299d8ea8
   __TEXT.__objc_methtype: 0x31 sha256:9d4bfbb0add90637541dfd410fe32c0cbe060a27c6dde6cd3c7f69ca21907165
-  __TEXT.__unwind_info: 0x78 sha256:975c317d3b22c7b33c201312517bb900d9dc23a44df20dcb478c4d3d8e2671c5
-  __DATA_CONST.__auth_got: 0x38 sha256:c64f604af69e89d20227b8d936c3d0a50ceaa156663427d7a57463c70460dc89
-  __DATA_CONST.__got: 0x18 sha256:34362124caf31a353be2cfae8c5c03e13750543a38ae6ab67d22f6649ba5b0e8
-  __DATA_CONST.__const: 0x40 sha256:5e2804fcc51313aedb21a2d55e63cc472b26c9b8c4190b47ea1c8cefd4e6902a
-  __DATA_CONST.__cfstring: 0xa0 sha256:5adcc363bdf8e643668bfff8d4fa80cd71ffd5a80935928c561338f2d9e1cb81
+  __TEXT.__unwind_info: 0x78 sha256:6fbe8e1a88269f249906730c9cc240cc34965075fc946ba348745545be4d83db
+  __DATA_CONST.__const: 0x40 sha256:df93a92941affa9094df40ddad7cb99f2370b08bf0763f49832412bae4b9d3b9
+  __DATA_CONST.__cfstring: 0xa0 sha256:2750e8d82506cb3dccf37b447d53b84a959dcf04213d9b386dd3adc86b86b922
   __DATA_CONST.__objc_classlist: 0x8 sha256:d057f81a3ccff70b608a82a0a6ad8d9fb132d34be2baeee74176263fae8c7532
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA_CONST.__objc_superrefs: 0x8 sha256:ba9d0ae48bac03620646c161fe276b995050623044a830c08c9c227b06851cd0
+  __DATA_CONST.__objc_superrefs: 0x8 sha256:a854cd916bb114d159a05917f45bd8d4826b5bb07cf5cd3c42a6ce28f1656441
+  __DATA_CONST.__auth_got: 0x38 sha256:80045245b744eb0f2b2f3c23d9caff0a4ecfbd513d0d540e6810b87eed5aa204
+  __DATA_CONST.__got: 0x18 sha256:7a5032b2e73fa6ff00a94b48abc51a39142e38d75e5ea8acc58834826474b233
   __DATA.__objc_const: 0xd0 sha256:afbececc8a9a53d41a1908e73d1cd554f791d4ecbacc6d7f0e0779ae988f2606
   __DATA.__objc_selrefs: 0x60 sha256:454a3ea11411cd3736ce2e07ac7f0981129c6cfd8bb1a8b4054e3b51cafcca2a
   __DATA.__objc_ivar: 0x4 sha256:097328e8c957de2428283954f6a1ee8ff7ad7def12e100a600178407f5decf24

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F4DD3935-2153-3991-A27A-44231559C8C4
+  UUID: 26A8C5A1-A487-3FC0-A24B-63483FD13E0D
   Functions: 8
   Symbols:   20
   CStrings:  31
Functions:
~ sub_c28 : 88 -> 92
~ sub_c80 -> sub_c84 : 204 -> 208
~ sub_d4c -> sub_d54 : sha256 1fa36799b71b70896c13eb8b4df12ddcc7cf87666e17cb2723ee6c8210109bc0 -> 4e3e70373010be4a5260ce4ede8276c1ae55fd7d2e7a20196a9327f88a19535f
~ sub_de0 -> sub_de8 : sha256 5c1121c348a1e311e8c268c879f8f089edabd81df0d2a57a322b77d25fc5037c -> 7738d9e5ac4a0bc061f941a33a55e1cc8838feee869cdb7c86398610f615258b
~ sub_e44 -> sub_e4c : sha256 0bb194242bef5aec85b50c7e7a2cd1c705e7a809ca0924766a4b627204cc24c9 -> d59c0f415137ceb8b78f6e90ba0a8e99107c2ade3fe8502b5eb957f18502a8be
~ sub_e50 -> sub_e58 : sha256 01efc9cc554270c8d7736146d52a4d6687e79b9037ca8fda8e0e4e979bbb36f8 -> cbad68cb08e1964da43192c35b89e787154cadd3f11ad460ea05580e8dd380e1
~ sub_e90 -> sub_e98 : sha256 8e139236c78e5f75693470aee99c90a6c3654d76e0ea69625724af39abfebee6 -> e1de88035b33b4d8a55e921020cc52026f81eb781ee8bddfc775b83ec9fa2483

```
