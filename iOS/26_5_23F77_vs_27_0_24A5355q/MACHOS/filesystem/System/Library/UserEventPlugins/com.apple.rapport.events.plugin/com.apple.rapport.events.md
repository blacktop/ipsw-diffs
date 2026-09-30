## com.apple.rapport.events

> `/System/Library/UserEventPlugins/com.apple.rapport.events.plugin/com.apple.rapport.events`

```diff

-716.600.13.0.0
-  __TEXT.__text: 0x39c sha256:a5668caf4a69e33164876057fbd7c94bb2d5fd30f9eb10057cf5d2738e4280ae
-  __TEXT.__auth_stubs: 0xb0 sha256:4d485924e9a8f177cc4813254bb32bf2b548ad40af961b933be0d44b77cf8ec0
-  __TEXT.__objc_stubs: 0x60 sha256:ac2ec8d2d38eb15679cdbd1094444f0ea433a50470ab9f20dcc33e06926efe62
+740.100.2.0.0
+  __TEXT.__text: 0x398 sha256:257ca319b7e4d67e382cef581ba688a42a175bf2f10b6524d0c0c0e8146acd92
+  __TEXT.__auth_stubs: 0xb0 sha256:03aa1b22ca66ab6f2ebcb80841a642a2b4993f0261b8c52a7b830805818618cc
+  __TEXT.__objc_stubs: 0x60 sha256:16b00726808a413eff29dbdaea5e1c67396922f4ed773f1f6ed8f2adeeac6513
   __TEXT.__cstring: 0x162 sha256:605a666c55a7943d9b067c808aa56ba86cf50f7ca208d8c3a486f6becc8ddf18
   __TEXT.__objc_methname: 0x3e sha256:1deb225ef279fe38c0cbf46cec08660b64d3d50d01ef64370d6fcf05feb42bc4
-  __TEXT.__unwind_info: 0x70 sha256:248392eebfe24d6488e586a435c5e238352776fe2e8918aea8768be9d042fc42
-  __DATA.__auth_got: 0x60 sha256:75443b2d7eb304af704e135ce779b1582e40b4e112f49dba1aedc8490c781a2a
-  __DATA.__got: 0x10 sha256:a0cfdfff873c3eced2228c273ecd17c7491c7e6df8c1cdbaf4e01694537e798c
-  __DATA.__const: 0x40 sha256:043905ca82ad900fcc0958b8e8e1b7f4d8888c769f5b5153357f4e0e90d19ad5
-  __DATA.__cfstring: 0xa0 sha256:5e28b338b8832aed7c32c7911f46e0e8d23af4297406d89a68ef3fc3ac739fd0
+  __TEXT.__unwind_info: 0x70 sha256:ef1fe38b83bad67996116b975bdedc31e97997320b4fa4134d0cb967b0dc024a
+  __DATA.__const: 0x40 sha256:3bb50c80000f9829c1f03c00edde97239db9fde793e8785caa7efb7b7bec8010
+  __DATA.__cfstring: 0xa0 sha256:fa676651091bcb5ae4cdcbe0b3803aa043d94ae94d6d0713ba81bda0b4ae25d8
   __DATA.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
   __DATA.__objc_selrefs: 0x18 sha256:3c60f1cfa9c36414f5ab433f6700f2fe7fc7385721cf3e657d98e6c43088b2ab
-  __DATA.__data: 0x74 sha256:b7f8e266901a0e0f897ba7a637b2ca6b9c1e65719ed131176b25f5adbe8e249b
+  __DATA.__data: 0x74 sha256:bb762ab0344afb45eaa4f34320c03934ed1c3b2944068849a6b5239444fdaf36
+  __DATA.__auth_got: 0x60 sha256:54a9222a83a1b52c94be2fec9c477d4fec494c871fc1750a8f9c5cb0c12ed78c
+  __DATA.__got: 0x10 sha256:a626504318ec285fd87e2c1cfc3dd242e92e84d7ff8f38bd9f6207106268a1d4
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DCB7DAA5-1845-3F82-91B5-69E509A9001E
+  UUID: 164A0513-ECA1-38E6-8004-BDF5704FE7CE
   Functions: 9
   Symbols:   18
   CStrings:  23
Symbols:
+ _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleasedReturnValue
Functions:
~ _RPUserEventPluginInit : 192 -> 188
~ sub_908 -> sub_904 : sha256 dead79f761ed7d65307546d8ebf50cb9f56e6084a626d4b04746e118a9cf485f -> 5d08b9513ae4ffd20de4c7a700f778d4fefd70475f8909b367d47302805ab4ae
~ sub_960 -> sub_95c : sha256 f7fb7c8a9bcededd8f4d2914799848e50ac294379f9c4c37dcd162e14e703f6c -> 954081b17186c18f6b4e4bb73d9d5bdad964a455402c79305e80f05237244eaf
~ sub_b48 -> sub_b44 : sha256 1c2b910613f5e95940bfabc72b344babfb0721fb8c79c17c5ca564617178412c -> 495ee5157b7c39c318189cf6a3f97f02296debb47cfad872e89f2ee5c30a1361
~ sub_b5c -> sub_b58 : sha256 d857bde9102df171f85f96b2fa0d72f1117759c147a2b76382641fe8e6951b5f -> 66fdd5efe1bf84d856d46be21828e092183410f37b537b4f3d4f9dcdb9a811a4
~ sub_b78 -> sub_b74 : sha256 65fcb0c4926d25a1b852ca885ce70820db50b6165e37ceabbe5ef0112854c539 -> a7680663b2d53cc0e2d868074f8d32c093383a3298e22f08d6186da3052241a9

```
