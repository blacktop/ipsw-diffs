## MemoryDiagnostics

> `/System/Library/PrivateFrameworks/MemoryDiagnostics.framework/MemoryDiagnostics`

```diff

-314.120.5.0.0
-  __TEXT.__text: 0x109c sha256:ae2569589398111d3d9ab0202b7d443be0e1f44afc19e61029e2a902758e85d5
-  __TEXT.__auth_stubs: 0x300 sha256:66ed38797b6ee21c952556a3ee9f762d3dbf9124eb0cb6f18c49a92880eef7ff
+356.0.0.0.0
+  __TEXT.__text: 0x1000 sha256:c28ac46daf7817ede97c8838dbb2fa072640fbf3bcbd2102c4a021fc9f5abd2b
   __TEXT.__const: 0x88 sha256:72bee89575266cdfad8a5d2e03dfcd526565698476879096e19e8a97aac7a2ae
   __TEXT.__oslogstring: 0x14a sha256:edb415095947e1bbeef9306e8c17ff96dad314dbfcf47bab3c73da81b66e2dbd
   __TEXT.__cstring: 0x5f8 sha256:60166f57d09e1f845be35ab8a48a9ceae1384e72a464f3e88f17958568c1f462
-  __TEXT.__gcc_except_tab: 0x60 sha256:76856c2eb91061b81138d1f2bebdd8b5e7a82df542feb74c9b44a69d27506b74
-  __TEXT.__unwind_info: 0x90 sha256:3e036d61ee3d930c48b2e22a84940f67e42efea00fe9b6a7864393e25570335d
-  __TEXT.__objc_methname: 0x86 sha256:46767106edb5ba6424b98399b6584fdb2772ae40ffa19bf742d16424a33c6a35
-  __TEXT.__objc_stubs: 0xc0 sha256:23a166b45915e51a877e228806d5fe0cce06f322eafc9e45e9379fedf95abb19
-  __DATA_CONST.__got: 0x68 sha256:39f37f8d1931b3bdf767e7510dd69509fbf23af1f7654933d0a4d291cbdd4418
-  __DATA_CONST.__const: 0xb8 sha256:86aac2504f3cfad3a914896945260d2ef0beea01013cae5127fc7c0a677f5dfe
+  __TEXT.__gcc_except_tab: 0x60 sha256:8d5412b2a142d673d7c3bb723f20fd8a2d9a0318b95f232024283472313b89af
+  __TEXT.__unwind_info: 0x98 sha256:8273238fe539498959d7b8356207ed2ecac36eae530d73e49b863dea82857f2c
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
+  __DATA_CONST.__const: 0xb8 sha256:7790e27b69082281ea3ffebcc9192c6388ecd455aedd9e7c0fed85cbe7ad3dab
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x30 sha256:f836c05fecca704f58ef10286d2c9b2462b4f046ae5fe2cf8c28e30316fa2928
-  __AUTH_CONST.__auth_got: 0x190 sha256:7a12e561363385e9dfeeab326368731c030ed4b374e7f5897ac819159d2884c5
-  __AUTH_CONST.__const: 0x40 sha256:b46e6df324a1064716ccf8c44445b496ac3fd6b46096a968a3c9cb94ed82c9a0
-  __AUTH_CONST.__cfstring: 0x840 sha256:08836c7cf3ffcacb2054411b937c34f94696851fd3914ac1b0e1edd10f8ade71
-  __DATA.__data: 0x208 sha256:edab3b6ac8268a9d8006766b083fad6b5a2c88fda6cef11f5b612ecaa747a66b
-  __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
+  __DATA_CONST.__objc_selrefs: 0x30 sha256:a882994c3c3baccd6e80b6ced4e7c8ea5c07b7d7d8dec53f891de58496811137
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x40 sha256:e37e1c9d42b36e35aabf12ab447ca9cf1eb9125246dc6faac5f0d89e82c45e5f
+  __AUTH_CONST.__cfstring: 0x840 sha256:8f2fd2a971ab0c97ea3fa94832353cab3d4ff68bb8d28a3975672430029b15a3
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__data: 0x208 sha256:03a26722efd0d4856456660d2620cc3f1d522b99ef820ee48d10b3de1c0448b8
+  __DATA_DIRTY.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE3B0F2A-6CED-3255-A84E-EBBFEBC75ED9
+  UUID: 0C55A4B6-609E-301E-A6B0-6D5E85D1A42F
   Functions: 12
-  Symbols:   167
-  CStrings:  161
+  Symbols:   171
+  CStrings:  155
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retain_x21
- _objc_retain_x24
Functions:
~ _memgraph_from_task_save_immediate : 1056 -> 1008
~ _RMEGetXPCConnection : 100 -> 84
~ ___RMEGetXPCConnection_block_invoke : sha256 161ecdd107dae78f3d6b79c35165a7346d7d13d9c7c61bbba1792dc9cc626736 -> 539aa7c7bef2a83223c29540426588d0c41032f672eb04ac6759b9ba241de8ac
~ ___RMEGetXPCConnection_block_invoke_2 : 228 -> 180
~ _ReportMemoryExceptionFromTask : 1308 -> 1288
~ ___ReportMemoryExceptionFromTask_block_invoke : 612 -> 600
~ ___ReportMemoryExceptionFromTask_block_invoke.19 : 100 -> 96
~ _RMEHandleAnalyzeReply : 264 -> 256
~ ___Block_byref_object_dispose_ : sha256 60d0bf8dd9787f31f76490fd38dd6911201506cf5be00d2e0aa0446883f345e7 -> 32288930e06587df1344491f8922af47896e0781f9bd8998b8254e14439e1cbf
~ ___isNotCircularException_block_invoke : sha256 8e763037d4661d3e7eb28281f813ba046724c22c533f5d42d63afe319bc1907c -> 36dcad76c4c43ffce92186551ee2e41af35403b1cd8d2c0db404a8f61771e3eb
~ _FPExtractCorpseInfoWithBlock : sha256 4fd36382e06c8c575e3afd80e8a076c56168cad252b6591660c69eed6a190fda -> 503161c0c3488a2d7df66021b64bfb03b7a12aee130d0c716c3394d8341a17c2
CStrings:
- "UTF8String"
- "dictionaryWithObjects:forKeys:count:"
- "errorWithDomain:code:userInfo:"
- "initWithUTF8String:"
- "isEqualToString:"
- "stringWithFormat:"

```
