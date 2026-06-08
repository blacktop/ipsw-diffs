## milod

> `/usr/libexec/milod`

```diff

-62.0.3.0.0
-  __TEXT.__text: 0x120 sha256:5e11dff6304b1f850fdc28fd8aa992e8b0e72c2157c5214dc9c2cba695717300
-  __TEXT.__auth_stubs: 0xb0 sha256:738e9cc2f1e4be6856b2a5ab59f0a9e0a884089394ada3bd1fb61879d231fdec
-  __TEXT.__objc_stubs: 0x60 sha256:a40e6729c913886836837feeeadc85ac0007bcc5515280c53d20239d400d4257
+106.0.2.0.0
+  __TEXT.__text: 0x11c sha256:76905a782f52805ee7f84f85b4f74a49acab20e88b840c306c7c0ac139a136f2
+  __TEXT.__auth_stubs: 0xb0 sha256:3bb8c42c285a74f9285bbd2d17857251555c3b5d1f84f30c5e4067d00dbafee3
+  __TEXT.__objc_stubs: 0x60 sha256:e8d5c41cdcdcacf8828b281224431ce80dfd635560b1f4fb39f1c53293b7c73c
   __TEXT.__oslogstring: 0xe sha256:81ca2c4a48687751ba462ca226de2a1cbef8eca443b3c70d2cdc8e9461f29a6d
   __TEXT.__cstring: 0x2c sha256:25cbc17279a690f0ad64c0fde11bf76b1cafa8ccd3ceb576c4b113c17cf67fd6
+  __TEXT.__const: 0x2 sha256:9b4fb24edd6d1d8830e272398263cdbf026b97392cc35387b991dc0248a628f9
   __TEXT.__objc_methname: 0x16 sha256:3148aff922fc35cca4931acb8d5b6d0d377cac72f2cdc07b29a36647179b993b
-  __TEXT.__unwind_info: 0x68 sha256:aa2354ebb3cb92c18a033c08fb1d7359f737d538fea1f9bfb355df2a1af68be0
-  __DATA_CONST.__auth_got: 0x60 sha256:75443b2d7eb304af704e135ce779b1582e40b4e112f49dba1aedc8490c781a2a
-  __DATA_CONST.__got: 0x10 sha256:a0cfdfff873c3eced2228c273ecd17c7491c7e6df8c1cdbaf4e01694537e798c
-  __DATA_CONST.__const: 0x40 sha256:e323d6cf090fb92742205712052bbe11a7463ff9361d45f8400bf06f691ee02b
-  __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA.__objc_selrefs: 0x18 sha256:293538496e98b572c44d3c2326840a01e6e36ff112bc1e29190b7614a9985c8f
+  __TEXT.__unwind_info: 0x68 sha256:c720ebff6766ac7a887e9d0f996c8f5014ae73f55f57ad914bde95db76cdc6e7
+  __DATA_CONST.__const: 0x78 sha256:48d347ffcc9d15a5bf557b6059d3cfcf660f096bbcd33f3307a3adb58ea15f7b
+  __DATA_CONST.__objc_imageinfo: 0x8 sha256:885ce8037a15de89b0ceb0054c31fc3de725513307f685be388961916dadcdb0
+  __DATA_CONST.__auth_got: 0x60 sha256:474749eb7756093469940bf6ae067a887fc02845e9e1f2b293719db761fd0ab3
+  __DATA_CONST.__got: 0x10 sha256:8c5a01cb362a19bcfb80c6c5b93439f1fce2b739adcd2be1e5756beb93b5e5cb
+  __DATA.__objc_selrefs: 0x18 sha256:fbcc0bb0c150cba56033ec7c5b1d5a59c48490fdf83c89b9b545ea3050f8356c
   __DATA.__data: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/MicroLocationUtilities.framework/MicroLocationUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 93EEC25C-E7EC-370E-9A83-FFFD2BCC9B9D
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 1413FFC8-EB04-3940-BC42-B7E8E5D62CEB
   Functions: 3
-  Symbols:   17
+  Symbols:   24
   CStrings:  7
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swiftos
+ _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_1000008f0 -> sub_100000ae0 : 200 -> 196
~ sub_1000009b8 -> sub_100000ba4 : sha256 b99a5b5348c2602aee16e0204b0646df2a61ed8d559fa3dedfc463df80d2bc70 -> e165569de44aca501b87dede625132b702374447731fe0afca9a2972b3a265e4
~ sub_1000009fc -> sub_100000be8 : sha256 ae77fa8c716474b5eb565c511d9a5183020f0615123814ede411ad902ef348b1 -> 0cd93b652b8eedad75557cd98f658a3d9eb253f8853ccbf11b503cfe57088e54

```
