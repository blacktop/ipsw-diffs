## MobileGestaltEvents

> `/System/Library/UserEventPlugins/MobileGestaltEvents.plugin/MobileGestaltEvents`

```diff

-1484.120.3.0.0
-  __TEXT.__text: 0x558 sha256:ee4c6ebcfd24f86a3048adf0e3ef831852c10b45a2dd2d10276363622f06837c
-  __TEXT.__auth_stubs: 0x1c0 sha256:ac15e39d87031f3b5182142fc844e44747d40830f7c6ea3b7a849bd121a06c7c
-  __TEXT.__objc_stubs: 0x160 sha256:15cc3e0e445dd190ab54e0f4673e92ccbcc8bbe7b4cafe7956415672cb166426
+1608.0.0.0.0
+  __TEXT.__text: 0x4c8 sha256:93045c5e2c01d828efacd230d29a59a4c78fc9e83b6ccd071ea1a47dfb9de7fe
+  __TEXT.__auth_stubs: 0x1b0 sha256:8139704958356ef90e5ea47c6a9d18d7f34b2d72889ef934e5fdf71b35531dfc
+  __TEXT.__objc_stubs: 0x160 sha256:513aba3af87d4164785e90761e29e0fd6f84a33f66f582bb9a6d74e6658f8a90
   __TEXT.__const: 0x8 sha256:61ea6d291f51bed018bdd7fb80d20685e7773ed7872222c6648a8ecfbe680f88
-  __TEXT.__cstring: 0x1f1 sha256:1f1efb793cc99947a6a61b60d2fabd91de286204019257f699c29b5c7e352b4e
-  __TEXT.__objc_classname: 0x1 sha256:6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d
+  __TEXT.__cstring: 0x164 sha256:e8b3109c2a1edb8b323635ee2118d10a2fecc265d587f863b4029c59e2672590
   __TEXT.__objc_methname: 0xc0 sha256:f5abaee82377315be1239f17858985173b2ed845bfc5c19f70a6ba1c98d57035
-  __TEXT.__unwind_info: 0x78 sha256:300f8f03b466f13be4191dc49c98b3c21f50705360562efe5fd77d09ab21ee0c
-  __DATA.__auth_got: 0xe8 sha256:e7de95c408e140d992dfc04937f67503f0b1e5bb145f7ebdbb6d0fa7ed3fabde
-  __DATA.__got: 0x40 sha256:d476ce255262529725eec1ef6e9887b50e4b01567360e11a8dcfd6094e659465
-  __DATA.__const: 0x60 sha256:ad6db28a9f292bf90639a0ce73f3b9c1a73751be2dca97410c3e002705b826ac
-  __DATA.__cfstring: 0xe0 sha256:ba215d1778efdbe034c5b1c615654855cb2c8c63b07739a5fd201b74543ddbb8
+  __TEXT.__unwind_info: 0x78 sha256:5158d572bab97281f0bcb8d113fe66aa3ef665a7e08bb623b7c0d934778bb270
+  __DATA.__const: 0x60 sha256:19f344862a5e671e8ad30e9d1bc0655753c6b271328d3173f067b6123b77c05d
+  __DATA.__cfstring: 0xe0 sha256:8508f2ec76713f47a19e920322ce17deb81f465a1fa4f29c6a2ef3f890f91465
   __DATA.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA.__objc_selrefs: 0x58 sha256:a6e20244af51d9fc53f75a14523546bb4c96bf038698871f437df9e450fc9c90
+  __DATA.__objc_selrefs: 0x58 sha256:0fa42e542628bef984dfcac63b7cb088adee9dfc0ed33e0d8364ac1ec668b93a
+  __DATA.__auth_got: 0xe0 sha256:466dc36c9f9470545cbadbd356e8e8a9934aaf7450665881a14547dd3ead5363
+  __DATA.__got: 0x40 sha256:a2e84d9ac2b4a9fdfec5e41fb65eea5fa1f021bc26d6efb7851e6292b8f0f118
   __DATA.__common: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E90773F-B4F3-36FF-A1FC-26CEC31C16AA
+  UUID: 3066171C-8166-3A21-B7E8-1BE89519F9AB
   Functions: 6
-  Symbols:   43
+  Symbols:   42
   CStrings:  31
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x26
+ _objc_retain_x2
- _objc_release_x27
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _rindex
Functions:
~ _init_gestalt_plugin : sha256 b3a9874e3e6bc7ffe17b7d83291ba67f155eb2ef36dcfdf3a15ba0bdfb857619 -> 22d4b9a38762b0bcd0c2249e0966b2d88e05391ec6ddfd853388bc913a34bcc8
~ sub_8f4 -> sub_8a4 : 956 -> 816
~ sub_cb0 -> sub_bd4 : sha256 c2896d1fce74abbd533c91def881e12e01ff912fc1c07979d080ba4841e67db5 -> b753643e7e4d170865c7fccc0d7b92c4caf2a94d80cc30d2a2d9d343f525d580
~ sub_cbc -> sub_be0 : sha256 12c6f1d550f94e06d8340a5fa59b7e43d128e61260a7146ed5aed31e6a109bcc -> 96a5806f9a971802899618e5c94067a293e84399e3e1eb74a9a384239b4f78e1
~ sub_cf8 -> sub_c1c : 188 -> 184
~ sub_db4 -> sub_cd4 : sha256 765351ea80e385e3d9eaa53ea1467a35af7cdb9c23dda6f71d15bf201a14b4ed -> 4fc87eec3493de7ddf52aad0b62de9af70b4e4ecc8d847f7a4d16bdb63b09ee0
CStrings:
+ "MobileGestaltEvents.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MobileGestaltSupport/MobileGestaltEvents/MobileGestaltEvents.m"

```
