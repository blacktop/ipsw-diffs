## ContainerMigrator

> `/System/Library/DataClassMigrators/ContainerMigrator.migrator/ContainerMigrator`

```diff

-725.120.2.0.0
-  __TEXT.__text: 0x1b4 sha256:67c1e740be6d094bdb60fbbc89caa7cf158848e301661572af7588194e2d1ff8
-  __TEXT.__auth_stubs: 0x70 sha256:ae4564976eea6d2bf2a056e9399ff5113d5bc8559866d3aa106bc11e70a081d9
-  __TEXT.__objc_methlist: 0x38 sha256:a83d104764d75a468f585b1b360dc9c61d353b82da7d5b69bf8e96afec0ac777
-  __TEXT.__const: 0x60 sha256:45b0ba1dfd27b1cfc060e84ce12d5e81cd94b913545f9b29c7974c6ee567cdc8
+826.0.0.0.1
+  __TEXT.__text: 0x138 sha256:37df58180d507fda1f34466f8196f8f87cd973224578979169cd675b75c6e4f7
+  __TEXT.__auth_stubs: 0x10 sha256:8a207f0d771971e82bc80599c84032591e6d43a0578c4124a8a9f593cb838644
+  __TEXT.__objc_methlist: 0x38 sha256:ba73d8972548e5bf82b54ceb7cc69123e949ffd33259bbaa0e1b7abc361627cb
+  __TEXT.__const: 0x5c sha256:fb22ec2ed2227991acdfc7728c60e434118e321f9933e8212581b6a1a5c66ba7
   __TEXT.__cstring: 0x19 sha256:b8c7ee2ad69863b43a78460c99fb46d76936bbf14fa155b44128970561b3d57c
-  __TEXT.__oslogstring: 0x71 sha256:69c66c4b32f127d5db9978e2195ecc8d4550a938ad2c82f70764e70f6cbc11e1
   __TEXT.__objc_classname: 0x19 sha256:b8c7ee2ad69863b43a78460c99fb46d76936bbf14fa155b44128970561b3d57c
   __TEXT.__objc_methname: 0x43 sha256:a3c541449edcd458901150a14a3c0c96944f11c314abe746b2dd0c9f242b16b6
   __TEXT.__objc_methtype: 0x18 sha256:6404870a6dbab538b4bdad51c08745b53e39f57fc4e93f7b87c1fbbc52729c46
-  __TEXT.__unwind_info: 0x60 sha256:0bb3934e53c22f7c16f2321eabe33dbda56f2aeebc7db34738c8e9accd470a42
-  __DATA_CONST.__auth_got: 0x38 sha256:c64f604af69e89d20227b8d936c3d0a50ceaa156663427d7a57463c70460dc89
-  __DATA_CONST.__got: 0x8 sha256:d8091ef279148e1d296cd6e05b0e112b36864ba9df0a6e2458fa1eb82e27090f
-  __DATA_CONST.__cfstring: 0x20 sha256:f4eb799cb588ea2a496858bad9eb5bfa59a3047d0f085f57dd9ace21a988a437
-  __DATA_CONST.__objc_classlist: 0x8 sha256:a4265e0d6d02153c7111b77ffc290a8f86239be963e5a1d0b9c86af78b122256
+  __TEXT.__unwind_info: 0x58 sha256:630de9ca0ac04fa8ce7e03a4333c76750609e8e924611f9fb17e76b60b72434b
+  __DATA_CONST.__cfstring: 0x20 sha256:93890a87d3a10b569af0883c145faa818a0e85b58cb9b2919519199bcaec72a6
+  __DATA_CONST.__objc_classlist: 0x8 sha256:3f6fa8d6e65e730bfea79fd38576269044a66d3966e7a755ecbe5288c5704a82
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA.__objc_const: 0x90 sha256:d556212ec5bf3ddf3c30456b477268ab4dea2ad1fa8229690c25dcf2a5529a1d
-  __DATA.__objc_selrefs: 0x20 sha256:e69f8727dfb45352bc794bb493b5c078aea0020897caf28a092ae97caac4e387
-  __DATA.__objc_data: 0x50 sha256:c96d10459110ce7e4544afbcb96b54292814667880b28c8c06a6a1f878d0863b
+  __DATA_CONST.__auth_got: 0x8 sha256:113aa6c7b6611bba072def7adb986af5df2f421f447afd9fda654c2c89e527ee
+  __DATA_CONST.__got: 0x8 sha256:7bec1c4a60b65f8ec319bade4d385885b5f64eaa9f87d3ccae7e1c9c6d63aaef
+  __DATA.__objc_const: 0x90 sha256:839caa28c210d60e6f10b610113995864ea6ffe555c86ccc1c964763e3201b94
+  __DATA.__objc_selrefs: 0x20 sha256:2103d95ceab580b1fe50f8d59716e965b30e1c172a0a031851c771ef019ba3ea
+  __DATA.__objc_data: 0x50 sha256:1a894aad905921d25079133b23cfc49a1cc879e5958b4f3f6f732ed622449e1d
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6C77057D-D89B-3A31-A3EC-A689379F2886
+  UUID: 6B38B37E-85D9-3515-A042-08CD0629B119
   Functions: 4
-  Symbols:   14
-  CStrings:  11
+  Symbols:   8
+  CStrings:  10
 
Symbols:
- __os_log_fault_impl
- _container_log_handle_for_category
- _container_perform_data_migration
- _objc_release_x20
- _objc_retainAutoreleasedReturnValue
- _os_log_type_enabled
Functions:
~ sub_980 -> sub_930 : 76 -> 80
~ sub_9cc -> sub_980 : sha256 5d76b06531d89662ec7d2db8853262f6b19711dd323c7f2b505f40d88a5a0cac -> 288b4daf6923fccfc0aa268028717548b0344a3c5416a5fe9c5f37b4311d4e97
~ sub_a18 -> sub_9cc : 204 -> 80
~ sub_ae4 -> sub_a1c : 80 -> 76
CStrings:
- "Migration failed with error %llu. Please include a sysdiagnose in a bug report for MobileContainerManager | all."

```
