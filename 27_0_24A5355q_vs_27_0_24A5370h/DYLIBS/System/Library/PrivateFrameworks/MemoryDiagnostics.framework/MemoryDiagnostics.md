## MemoryDiagnostics

> `/System/Library/PrivateFrameworks/MemoryDiagnostics.framework/MemoryDiagnostics`

```diff

-356.0.0.0.0
-  __TEXT.__text: 0x1000 sha256:c28ac46daf7817ede97c8838dbb2fa072640fbf3bcbd2102c4a021fc9f5abd2b
+358.0.0.0.0
+  __TEXT.__text: 0x1000 sha256:0a3ea4f214fd41c00007e3ffd83987a76860aa12cdb7f2addea768d847c1ca9d
   __TEXT.__const: 0x88 sha256:72bee89575266cdfad8a5d2e03dfcd526565698476879096e19e8a97aac7a2ae
   __TEXT.__oslogstring: 0x14a sha256:edb415095947e1bbeef9306e8c17ff96dad314dbfcf47bab3c73da81b66e2dbd
   __TEXT.__cstring: 0x5f8 sha256:60166f57d09e1f845be35ab8a48a9ceae1384e72a464f3e88f17958568c1f462
   __TEXT.__gcc_except_tab: 0x60 sha256:8d5412b2a142d673d7c3bb723f20fd8a2d9a0318b95f232024283472313b89af
-  __TEXT.__unwind_info: 0x98 sha256:8273238fe539498959d7b8356207ed2ecac36eae530d73e49b863dea82857f2c
+  __TEXT.__unwind_info: 0x98 sha256:9a81f0c702f83e7208e1030d09da616f6f4161e5fd73fa09a53e010c262a6d4b
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0xb8 sha256:7790e27b69082281ea3ffebcc9192c6388ecd455aedd9e7c0fed85cbe7ad3dab
+  __DATA_CONST.__const: 0xb8 sha256:88819dd5b025c43401e011a8fa819f4208e50d97d87e1fdc2d8964d2cb3d755a
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x30 sha256:a882994c3c3baccd6e80b6ced4e7c8ea5c07b7d7d8dec53f891de58496811137
+  __DATA_CONST.__objc_selrefs: 0x30 sha256:d63a0cc6fa7d57196c047b4c32bb48fa464e4541ff6e3a1af826a4eb44d93cf3
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x40 sha256:e37e1c9d42b36e35aabf12ab447ca9cf1eb9125246dc6faac5f0d89e82c45e5f
-  __AUTH_CONST.__cfstring: 0x840 sha256:8f2fd2a971ab0c97ea3fa94832353cab3d4ff68bb8d28a3975672430029b15a3
+  __AUTH_CONST.__const: 0x40 sha256:f9005e7db97b9d7cf0991f207ee7471c89e4067b5b9f99b0c5c4876ebfcc1b1b
+  __AUTH_CONST.__cfstring: 0x840 sha256:deddcc67bc4fd8d4195e836d357f21624dda499f4efccbeeea3f6566749b757e
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__data: 0x208 sha256:03a26722efd0d4856456660d2620cc3f1d522b99ef820ee48d10b3de1c0448b8
+  __DATA.__data: 0x208 sha256:ba5160a84332cd81262a64e3fec8c1ba921f0447d339ccd73eebb55bbe281dae
   __DATA_DIRTY.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0C55A4B6-609E-301E-A6B0-6D5E85D1A42F
+  UUID: C3CC3944-BE41-3CDD-822E-48FD44DB7203
   Functions: 12
   Symbols:   171
   CStrings:  155
Functions:
~ _memgraph_from_task_save_immediate : sha256 21a6a734a870a3ec8e90c31a6c8ec18ad1d32ed594260f047bea809cbde71c3b -> 61b9b6cdebcf8398209ed7095ca1e63fb1842822461c0606e6890b3fbb60f653
~ _RMEGetXPCConnection : sha256 760af4e89e2566ee9025aae75d4b96e237b56bddfc6671b1db1b7fb54b250b0c -> 549dbb5d328de4b124e417f884af937d3227441500eaac32b9f6cd4427796077
~ ___RMEGetXPCConnection_block_invoke : sha256 539aa7c7bef2a83223c29540426588d0c41032f672eb04ac6759b9ba241de8ac -> 6e327117fede088ee428cd5f6e1f53448d2d6d3ca2cf60229a440aa096113216
~ ___RMEGetXPCConnection_block_invoke_2 : sha256 5800703ed3850009d40d10fd7a2403b255f3594fb08f62511b4cfb063905d82b -> b5f8af5ce0443673f50e1ddfdd9368974670140f48b249972216d99824776e74
~ _ReportMemoryExceptionFromTask : sha256 1865190205dcb019e5ba606e32f25fb56b176fdaf9ce7f64100cb3547d76e828 -> bc332c5420f6089133576547343383fed3351074ff40941c0b0fd41d1964b1bf
~ ___ReportMemoryExceptionFromTask_block_invoke : sha256 5fec8c7c6bc9fc52c484061c67c6965684d6f7763cea1ee5b4de00b17b4268ee -> f52f7242cdde62cfd05bdb49ad87f1b39ca73e6e8c7964db9676885c74b13db6
~ ___ReportMemoryExceptionFromTask_block_invoke.19 : sha256 213af1f277a0d20fa4501b0c38cd0165241949ce23fb83e40d363208e5ff2d48 -> 62421e1a52498ae6224bed2f9e4c781419a0062adc7cbf0349fce5c562b1339c
~ _RMEHandleAnalyzeReply : sha256 f6efffb095430be8dd3468f4070623210b89562a5add6397d714f0a5a9fa943d -> 64d582009c92cf59bdb113b8535349f662901099d174ac9aa28d2c626f986600
~ ___Block_byref_object_dispose_ : sha256 32288930e06587df1344491f8922af47896e0781f9bd8998b8254e14439e1cbf -> 910d81d06d7f9524e241cc2711f9c0d0c173dffb00205f60cdd220863d3ad29d
~ ___isNotCircularException_block_invoke : sha256 36dcad76c4c43ffce92186551ee2e41af35403b1cd8d2c0db404a8f61771e3eb -> 0eab6cda5f373f80fceb272561855a56dfd0b4e2006d393104b50aefcac56a39
~ _FPExtractCorpseInfoWithBlock : sha256 503161c0c3488a2d7df66021b64bfb03b7a12aee130d0c716c3394d8341a17c2 -> 5850b51e4911a342c3e34f4e1e32d21a4a2295953bffc90761b4505a9a9dd7c6

```
