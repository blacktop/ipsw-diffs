## ManagedEvent

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/ManagedEvent.framework/ManagedEvent`

```diff

-2357.0.0.0.2
-  __TEXT.__text: 0xa64 sha256:1e6041dd5eecdd51c80821e4349ec61c820e89a584e9975c3dee8303ad29f80b
+2374.0.0.0.0
+  __TEXT.__text: 0xa70 sha256:6508db065757c98d52d11e872f669dd5ae249e5c4d8cae93f69b296fe7846032
   __TEXT.__const: 0x18 sha256:97d6c6ba80894cc6faffb874e0966524a9825921997bb75ddd81bec11be4cd0c
   __TEXT.__oslogstring: 0x184 sha256:692985ddaba61134e971e24fb67a016eb4ef0976bba0e93200002ae7236647c1
-  __TEXT.__cstring: 0x858 sha256:a5e258cb4780ae4a45d3c1d6cbd17e414b50feabc40abd5980290dc1b2340d73
-  __TEXT.__unwind_info: 0x88 sha256:51b9540733c0932c058a135f27cfd28f84cbf0956bd137cd234e40f8659e5ebc
+  __TEXT.__cstring: 0x86a sha256:5bb9a8e04b7b5d7d01b190484aeeb8e5e385b0d4b0e6a48b4b2819083669e93d
+  __TEXT.__unwind_info: 0x88 sha256:81b0ad3e746977a001ed28af3d41675b3326decd91ac7a488a66d63f57099f32
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0xe0 sha256:59b8db687dabe2718d71f2e326d075ca1beda0607f6303a3780985a495b38174
+  __DATA_CONST.__const: 0xe0 sha256:a7ee5cc51bd1017f8d0f8437a6d7d0481adc528dd87549d7ab23afec6f4a242c
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x40 sha256:e13cc1cce32fb49b38dedb94105624685ace4d31f81a926cd7e83360e2c27972
+  __AUTH_CONST.__const: 0x40 sha256:cbefea07d7162ff96f97f669bb043501ee29ae5620662bc453a8df8e702faa7d
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__data: 0x310 sha256:6a5cba22b65e7a0f4749cec6ef6d0477792ab760a103add68e3c6ade82521db1
+  __DATA.__data: 0x318 sha256:8819738ed1962a9d302ac3f10e2e01c469852fbc857717561a29d5312f807ba1
   __DATA_DIRTY.__bss: 0x18 sha256:9d908ecfb6b256def8b49a7c504e6c889c4b0e41fe6ce3e01863dd7b61a20aa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
-  UUID: 5D1E3365-F4BE-31EF-B55A-5242145D4703
+  UUID: 1466C430-012E-34ED-815D-5F7941833A4F
   Functions: 17
-  Symbols:   178
-  CStrings:  109
+  Symbols:   179
+  CStrings:  110
 
Symbols:
+ _kSymptomManagedEventKeyCensusNoForegroundApp
Functions:
~ _managed_event_fetch_completion : 224 -> 236
~ ___managed_event_fetch_helper_block_invoke : sha256 e3d399c24f61ea6b64bae25de72d345d5724f52ceeec6b0e35eabe3146f7152b -> c8bde875f080ad65af87a09293a214590a09191faf519c86f65b85cf764da8df
~ ___managed_event_compose_from_xpc_object_block_invoke : sha256 f1121d7a972001ede6fe89e3f4d4603952a3f4ba5a5acbcbb7603a58a5756a4e -> 113ef6265ec579cdedfad0421394a09bf390e02a51a73a37cb7a38f256a0bc73
~ _managed_event_fetch : sha256 7eb6456f52f561f0c3f07fefc247bfc4f944a800886e30dd92cea9021a2da16d -> 82655374f9abbfbaa016416f0241ba68c999e2536cc504c9ba2eff461b3f2446
~ _msg_requesting : sha256 8ed2e9ab5b62c5ebc7a0f9d4028705beec129127d2bf0384cd95ef07b460cbda -> 899822407378eb40fd194b0d2dccfff5bd34ef240c855643647f32e5c43df42a
~ _managed_event_send_with_reply : sha256 f17e3cbf2bfd2d166a263156b7f8f5438ffe7430568617798d52e33aa4e02deb -> 08e350d607ee3554d5091d8373f08d5e6d1ab3e1fa414e0711b9502b22bd3b2d
~ ___managed_event_send_with_reply_block_invoke : sha256 85db15bca2d167604f4796904443765e1fb49dcec0271405a17d3c80594c3d8c -> 31bbd47b3a8dbca49de8c1f3aacfddb5679d63387fdbe668f323c7f44f7dc89e
~ _managed_event_fetch_series : sha256 814a8be0877cef9e29d8ca8015c5731e514a2128b9d24238c6f94c663b203301 -> fb87f2a7ddb1fddc0ffa0fb4046f17c188667918dae8cc8d5cef9724862c42a7
~ ___managed_event_get_queue_block_invoke : sha256 b2695e2361531e4bc941b48639095bb6ac5b055517b2ef409109172e8cf211fc -> 9148428a2dea3a0b129b33d5544d5153a0377f7abfffa8f9ee408f67706fa43d
~ ___managed_event_get_connection_block_invoke : sha256 30068868dc38a585661b9515be67f3a612fb4bba5b4aa4370269d192c4a28f6d -> 0f8230257ac3ad04749958ed882fa286077753228255c9db43b33b46f0d9de6b
~ _OUTLINED_FUNCTION_0 : sha256 902a28da609d5e09e803be22da6be77255745fe6489e0fd9d9e916a5eb755e0c -> 9ca19c11d36498928bc7b659a2ffd0e29ba5d093644163e91369e6aaa44b4235
CStrings:
+ "no-foreground-app"

```
