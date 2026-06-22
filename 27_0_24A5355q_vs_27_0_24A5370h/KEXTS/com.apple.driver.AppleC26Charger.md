## com.apple.driver.AppleC26Charger

> `com.apple.driver.AppleC26Charger`

```diff

-147.0.0.0.1
-  __TEXT.__cstring: 0x1e7e sha256:9b57d41411e7ad7189732806fc8f7ec2ae3436260c7b94b3a6ccfeed039703d3
+153.0.0.0.0
+  __TEXT.__cstring: 0x27a6 sha256:a58d7a77d9fb81945b6faa322c43a81456e5fd5e22811e1bcd1d3cf74a3e54bc
   __TEXT.__const: 0x157 sha256:3753e7b05be6567d2e3e1988f8f27ca58b1d9c843fc7b2aa3b2f402bf5c6caec
   __TEXT.__os_log: 0x51 sha256:772d9eb73d08c1d01e3908e6a57dda1f0d036196396eb5f159036c3c160732e4
-  __TEXT_EXEC.__text: 0x11de8 sha256:937b583eefd85659c64c8fd4111c1eb8f6f1712f4c37b31e51951c08158d1a63
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:53a355e19465064531794ecacf272c847d33c6c9dc2de367c9a2d52c47b15a9d
-  __DATA.__common: 0x348 sha256:16d0edc8b7ad7705b23a14058f366ff1c0dfa16a0ad14f741924c308754cf8d1
-  __DATA_CONST.__mod_init_func: 0x18 sha256:c07570bb9546f3eeb70fed1a924a4d3e51c0d491e4010bba69fbb0b8d687d5fa
-  __DATA_CONST.__mod_term_func: 0x18 sha256:aef78acb9e7f152e4c2f093f8faa7748665cbb1b8b2e79736626c707542713da
-  __DATA_CONST.__const: 0x58c8 sha256:6291cb8fd49e9cd017a7198bc26d36d6aa47b313141b74ed9bcdfaf541697b31
-  __DATA_CONST.__kalloc_type: 0x500 sha256:b10125817118d0f50aabb3bc6af4e2de0c014d8d19157772cdd14df127e32dec
-  __DATA_CONST.__auth_got: 0x228 sha256:09bc792392952fb372c74813a0ac8b587b65d49ffc9aa13814a987c068f97f9c
-  __DATA_CONST.__got: 0xe0 sha256:7c4de180dd3f989325e6cb79c056757ef2ea4ec564247597c36a10a7063725cf
-  __DATA_CONST.__auth_ptr: 0x8 sha256:b3010e5681c4f45e2edaabcdd57a80a3323489d6da94c0f83afb5660c0e0e920
-  UUID: 72D23092-0E30-347C-94C5-5B0B81969590
-  Functions: 543
+  __TEXT_EXEC.__text: 0x13df4 sha256:d2717aac41bc8484661aa32c7ba4782baadbf916c8140aac10d0e793a05cd646
+  __TEXT_EXEC.__auth_stubs: 0x450 sha256:5cc8a6be84648eaf418d68e37740aa9994b21ec4c637869a39bd9f2167297d4a
+  __DATA.__data: 0xc8 sha256:a607bf3860d489c9142b3fbb148a766d41ebe7483efa7662b44783fb3b637366
+  __DATA.__common: 0x3c0 sha256:3dc463a76fc170607c07b104c3cb531362ce7d6e10c1a34e0c0f370aeae08ce8
+  __DATA_CONST.__mod_init_func: 0x18 sha256:c6d239df6132dded1abf6792b48176fc2656c23c3963048c10c5dd1d69247ee0
+  __DATA_CONST.__mod_term_func: 0x18 sha256:040591b591984a861530f475b00d7237200831d3fa0e56889dea0c19e86c9639
+  __DATA_CONST.__const: 0x6250 sha256:8d3bfb3388930e07ecb0e05c9c42ef9e2952cce8bf3be368ffb080664576e6e0
+  __DATA_CONST.__kalloc_type: 0x5c0 sha256:2e7ea3eefd6406b3f93cf562567a5c57f0b7109486929850bcb6cf399e1dab6e
+  __DATA_CONST.__auth_got: 0x228 sha256:1a6a1edf80c52d4139b80e29ac0484e0063d754e0f8fb0fa188f1f67c8a32c1a
+  __DATA_CONST.__got: 0xe0 sha256:d022a8183df3697a588d86f1bdf6fc410f4b8d3cf735c2f0257810c449401d01
+  __DATA_CONST.__auth_ptr: 0x8 sha256:0d20854e1968fb09958e82c3a78b961322093637ccc5b6d18041a4169d7c9620
+  UUID: FC88C613-77A9-3FBA-AE89-137952CFAD81
+  Functions: 603
   Symbols:   0
-  CStrings:  221
+  CStrings:  270
 
CStrings:
+ "%s: ***** QiAuthProtocol RECEIVED AUTH DATA ***** (len=%lu bytes)\n"
+ "%s: ***** QiAuthProtocol SENDING AUTH DATA ***** (len=%d bytes)\n"
+ "%s: ===== AppleQiAuthProtocol::start() SUCCESS =====\n"
+ "%s: AppleC26AuthProtocol got device stream (number=%d, type=%d)\n"
+ "%s: AppleC26AuthProtocol is not AppleC26DeviceStream\n"
+ "%s: AppleC26AuthProtocol super::start() failed\n"
+ "%s: AppleC26AuthProtocol::sendData called with %d bytes\n"
+ "%s: AppleC26AuthProtocol::start() called\n"
+ "%s: AppleC26AuthProtocol::start() completed successfully\n"
+ "%s: AppleC26AuthProtocolWatch got device stream (number=%d, type=%d)\n"
+ "%s: AppleC26AuthProtocolWatch is not AppleC26DeviceStream\n"
+ "%s: AppleC26AuthProtocolWatch super::start() failed\n"
+ "%s: AppleC26AuthProtocolWatch::sendData called with %d bytes\n"
+ "%s: AppleC26AuthProtocolWatch::start() completed successfully\n"
+ "%s: AppleQiAuthProtocol got device stream (number=%d, type=%d, protocol=%d)\n"
+ "%s: AppleQiAuthProtocol provider is not AppleC26DeviceStream\n"
+ "%s: AppleQiAuthProtocol super::start() failed\n"
+ "%s: AuthProtocol attached to dock\n"
+ "%s: AuthProtocol registered service\n"
+ "%s: AuthProtocol stream created\n"
+ "%s: AuthProtocol stream enabled\n"
+ "%s: AuthProtocolWatch attached to dock\n"
+ "%s: AuthProtocolWatch registered service\n"
+ "%s: AuthProtocolWatch stream created\n"
+ "%s: AuthProtocolWatch stream enabled\n"
+ "%s: Config stream enabled, sending GetDevInfo command\n"
+ "%s: Config stream setup complete, registered service\n"
+ "%s: Processing RetConfig response - payloadDataLen=%zu\n"
+ "%s: Processing RetDevInfo response\n"
+ "%s: QiAuthProtocol attached to dock\n"
+ "%s: QiAuthProtocol auth data sent successfully\n"
+ "%s: QiAuthProtocol registered service\n"
+ "%s: QiAuthProtocol stream created successfully\n"
+ "%s: QiAuthProtocol stream enabled\n"
+ "%s: Received config data - cmdID=0x%02x, dataLen=%zu\n"
+ "%s: RetConfig: configVersion=0x%04x, numStreams=%zu\n"
+ "%s: Sending GetConfig command to enumerate streams\n"
+ "%s: Starting config stream setup\n"
+ "%s: calling _c26Stream->sendData\n"
+ "%s: could not open AuthProtocolWatch stream\n"
+ "%s: could not start device stream, detached; str:%d typ:%d prot:%d\n"
+ "%s: createDeviceStream: streamNumber=%d, streamType=%d, protocolType=%d, deferStart=%d\n"
+ "%s: device stream init or attach failed; str:%d typ:%d prot:%d\n"
+ "%s: device stream started successfully; str:%d typ:%d prot:%d deferStart:%d\n"
+ "%s: received AuthProtocolWatch telegram:%s\n"
+ "%s: sending AuthProtocolWatch telegram:%s\n"
+ "1222222222222222"
+ "AppleC26AuthProtocolWatch"
+ "AppleC26AuthProtocolWatch::start()\n"
+ "AppleC26FFBDataStream"
+ "AppleC26FFBPacket"
+ "site.AppleC26AuthProtocolWatch"
+ "site.AppleC26FFBDataStream"
+ "site.AppleC26FFBPacket"
- "%s: could not start device stream, detached; str:%d typ:%d prot%d\n"
- "%s: createDeviceStream: streamType=%d, protocolType=%d\n"
- "%s:AuthProtocol stream created\n"
- "%s:QiAuthProtocol stream created\n"
- "AppleQiAuthProtocol::start()\n"

```
