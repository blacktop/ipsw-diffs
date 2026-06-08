## libsystem_darwin.dylib

> `/usr/lib/system/libsystem_darwin.dylib`

```diff

-1752.120.2.0.0
-  __TEXT.__text: 0x64c8 sha256:0779d339f12e497feac484b6d78c9e4aa086e46271eb819e551cbde70d54f5a6
-  __TEXT.__auth_stubs: 0x550 sha256:90b0cd8fc1f7777e93a1e8b92e10b1f54f7be05a547cf4866229c35750d990a5
-  __TEXT.__const: 0xa0 sha256:1e998b314b754ee6aba4298b84f2838f07ac4a2b598fe994263c929276fd1a41
-  __TEXT.__cstring: 0x1e58 sha256:df00161aad6e2c20e56152ae19d306a18dfca9036c65730a1d6e14ac48a17cfa
+1782.0.0.0.0
+  __TEXT.__text: 0x65ac sha256:3e352f76c673eb02bb35b2a7bbb1b3cbff191909eba3a6130c6a958ec1534ba2
+  __TEXT.__const: 0x90 sha256:87a3cf8cc3e21ea864b1dc64b203f155350d42a7d2f6a16b525c7c3407f1405a
+  __TEXT.__cstring: 0x1ebc sha256:6324bc3dfb63ce6701051e7017e6279f83d57901c798a12f3995f3de4dcf28cf
   __TEXT.__oslogstring: 0x8d4 sha256:13772c1d5eed1d9158d31ae71b9e428aa7110ae84e75c41a40cd196707c02b57
-  __TEXT.__unwind_info: 0x1d0 sha256:170313d2b97734e0bd34d378881dffa2cb70ecc98129d4b3ca20712f6f3d7cf7
-  __DATA_CONST.__got: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
-  __DATA_CONST.__const: 0x2930 sha256:e51f8b3ea7362334758eed1ace23e0fab8d81dbc80f0c44b60c4756ee0e5c8e7
-  __AUTH_CONST.__auth_got: 0x2a8 sha256:3893c122a235d76ac34b7853ae88aae7b72c2785f12e0e5ba05506aa89f4cf6c
-  __AUTH_CONST.__const: 0x180 sha256:2947777228c607280ed339d8e4f1ecc79b9c2afdde8b6e2e95a87fd9d526462d
-  __DATA.__data: 0x10 sha256:af8197cfd558b57d8bd6c7117a3be97466ff1725c1aa232ebe729b89082e5e4b
+  __TEXT.__unwind_info: 0x1d8 sha256:0cab1b5104bce9433d75ef5ed54b2d64c6d56eb76b7c01a55c1a6dd20db9070d
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x2950 sha256:966b2bbd06a41b30da7a53e47ce1726be1b133ad5b27adb6a58f44da67d91168
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x1a0 sha256:6f0333ae59e9d73935d273a3d807a247293108e9c0999ee6b8381e717e26eee3
+  __AUTH_CONST.__auth_got: 0x2b0 sha256:334e61fade598d87a35822d34aaa6adec70d9edb5a441ea134552eeb2afd813e
+  __DATA.__data: 0x10 sha256:376d5652833904085aaed2c1256e0d0a4c886166c48d9f0825eb657effc49829
+  __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA_DIRTY.__bss: 0x48 sha256:834a709ba2534ebe3ee1397fd4f7bd288b2acc1d20a08d6c862dcd99b6f04400
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: AF4F1CB1-72DD-32B7-8A3F-32369CD3DE39
-  Functions: 171
-  Symbols:   452
-  CStrings:  483
+  UUID: 164C9B77-94A4-378C-A122-26290CA39E73
+  Functions: 174
+  Symbols:   462
+  CStrings:  487
 
Symbols:
+ ___os_lockdown_mode_enabled_block_invoke
+ ___os_lockdown_mode_enabled_block_invoke.cold.1
+ _abort_report_np
+ _os_lockdown_mode_enabled
+ _os_lockdown_mode_enabled.cold.1
+ _os_lockdown_mode_enabled.lockdown_mode_enabled
+ _os_lockdown_mode_enabled.once
- _OUTLINED_FUNCTION_24
CStrings:
+ "%s:%s:%u: %s"
+ "lockdown_mode.c"
+ "os_lockdown_mode_enabled_block_invoke"
+ "security.mac.lockdown_mode_state"

```
