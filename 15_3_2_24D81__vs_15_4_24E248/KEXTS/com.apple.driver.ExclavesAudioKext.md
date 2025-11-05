## com.apple.driver.ExclavesAudioKext

> `com.apple.driver.ExclavesAudioKext`

```diff

-220.24.0.0.0
+240.34.0.0.0
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x2fa4
   __TEXT.__os_log: 0x55a
-  __TEXT_EXEC.__text: 0xa4fc
+  __TEXT_EXEC.__text: 0xa904
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8
-  __DATA_CONST.__auth_got: 0x158
+  __DATA_CONST.__auth_got: 0x190
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
   __DATA_CONST.__const: 0x1148
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: 3059A63F-75C1-398B-AC6A-8AD6F063376E
-  Functions: 323
-  Symbols:   527
+  UUID: 5C8A24D6-D23A-3F8C-A5B8-91D1E7AD72FD
+  Functions: 321
+  Symbols:   577
   CStrings:  111
 
Symbols:
+ _ZN26ExclavesAudioProxyEndpoint12initForProxyEP9IOServiceS1_.cold.1
+ _ZN26ExclavesAudioProxyEndpoint23createTightbeamEndpointERP13tb_endpoint_s.cold.1
+ _ZN26ExclavesAudioProxyEndpoint23createTightbeamEndpointERP13tb_endpoint_s.cold.2
+ _ZN32ExclavesAudioProxyDebugInterface16initWithEndpointEP9IOServiceP26ExclavesAudioProxyEndpoint.cold.1
+ _ZN32ExclavesAudioProxyDebugInterface16initWithEndpointEP9IOServiceP26ExclavesAudioProxyEndpoint.cold.2
+ _ZN32ExclavesAudioProxyDebugTightbeam15enableInjectionEb.cold.1
+ _ZN32ExclavesAudioProxyDebugTightbeam15enableInjectionEb.cold.2
+ _ZN32ExclavesAudioProxyDebugTightbeam16initWithEndpointEP9IOServiceP26ExclavesAudioProxyEndpoint.cold.1
+ _ZN32ExclavesAudioProxyDebugTightbeam16initWithEndpointEP9IOServiceP26ExclavesAudioProxyEndpoint.cold.2
+ _ZN32ExclavesAudioProxyDebugTightbeam16initWithEndpointEP9IOServiceP26ExclavesAudioProxyEndpoint.cold.3
+ _ZN33ExclavesAudioProxyDriverInterface16initWithEndpointEP9IOServiceP26ExclavesAudioProxyEndpoint.cold.1
+ _ZN33ExclavesAudioProxyDriverInterface16initWithEndpointEP9IOServiceP26ExclavesAudioProxyEndpoint.cold.2
+ _ZN33ExclavesAudioProxyDriverInterface34findMatchingStreamDescriptionIndexERK30IOAudio2StreamBasicDescriptionjRh.cold.1
+ _ZN33ExclavesAudioProxyDriverInterface34findMatchingStreamDescriptionIndexERK30IOAudio2StreamBasicDescriptionjRh.cold.2
+ _ZN33ExclavesAudioProxyDriverInterface34findMatchingStreamDescriptionIndexERK30IOAudio2StreamBasicDescriptionjRh.cold.3
+ _ZN33ExclavesAudioProxyDriverTightbeam10teardownIOEv.cold.1
+ _ZN33ExclavesAudioProxyDriverTightbeam10teardownIOEv.cold.2
+ _ZN33ExclavesAudioProxyDriverTightbeam12mapDMABufferEv.cold.1
+ _ZN33ExclavesAudioProxyDriverTightbeam12mapDMABufferEv.cold.2
+ _ZN33ExclavesAudioProxyDriverTightbeam13setupClientIOEy.cold.1
+ _ZN33ExclavesAudioProxyDriverTightbeam13setupClientIOEy.cold.2
+ _ZN33ExclavesAudioProxyDriverTightbeam13setupClientIOEy.cold.3
+ _ZN33ExclavesAudioProxyDriverTightbeam16initWithEndpointEP9IOServiceP26ExclavesAudioProxyEndpoint.cold.1
+ _ZN33ExclavesAudioProxyDriverTightbeam16initWithEndpointEP9IOServiceP26ExclavesAudioProxyEndpoint.cold.2
+ _ZN33ExclavesAudioProxyDriverTightbeam16initWithEndpointEP9IOServiceP26ExclavesAudioProxyEndpoint.cold.3
+ _ZN33ExclavesAudioProxyDriverTightbeam16teardownClientIOEy.cold.1
+ _ZN33ExclavesAudioProxyDriverTightbeam16teardownClientIOEy.cold.2
+ _ZN33ExclavesAudioProxyDriverTightbeam16teardownClientIOEy.cold.3
+ _ZN33ExclavesAudioProxyDriverTightbeam20getStreamDescriptionER30IOAudio2StreamBasicDescription.cold.1
+ _ZN33ExclavesAudioProxyDriverTightbeam20getStreamDescriptionER30IOAudio2StreamBasicDescription.cold.2
+ _ZN33ExclavesAudioProxyDriverTightbeam20setStreamDescriptionERK30IOAudio2StreamBasicDescriptionj.cold.1
+ _ZN33ExclavesAudioProxyDriverTightbeam20setStreamDescriptionERK30IOAudio2StreamBasicDescriptionj.cold.2
+ _ZN33ExclavesAudioProxyDriverTightbeam31selectPhysicalStreamDescriptionEh.cold.1
+ _ZN33ExclavesAudioProxyDriverTightbeam31selectPhysicalStreamDescriptionEh.cold.2
+ _ZN33ExclavesAudioProxyDriverTightbeam4wakeEv.cold.1
+ _ZN33ExclavesAudioProxyDriverTightbeam4wakeEv.cold.2
+ _ZN33ExclavesAudioProxyDriverTightbeam5sleepEv.cold.1
+ _ZN33ExclavesAudioProxyDriverTightbeam5sleepEv.cold.2
+ _ZN33ExclavesAudioProxyDriverTightbeam7setupIOEv.cold.1
+ _ZN33ExclavesAudioProxyDriverTightbeam7setupIOEv.cold.2
+ _ZN33ExclavesAudioProxyDriverTightbeam9readInputEyyj.cold.1
+ _ZN33ExclavesAudioProxyDriverTightbeam9readInputEyyj.cold.2
+ _ZN33ExclavesAudioProxyDriverTightbeam9readInputEyyj.cold.3
+ _tb_message_precheck_decoding
+ _tb_message_precheck_encoding
+ _tb_message_raw_decode_u32
+ _tb_message_raw_decode_u64
+ _tb_message_raw_decode_u8
+ _tb_message_raw_encode_bool
+ _tb_message_raw_encode_u32
+ _tb_message_raw_encode_u64
+ _tb_message_raw_encode_u8
- _tb_message_encode_bool
- _tb_message_encode_u32
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/ExclavesAudioProxyDebugInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/ExclavesAudioProxyDebugTightbeam.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/ExclavesAudioProxyDriverInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/ExclavesAudioProxyDriverTightbeam.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Endpoint/ExclavesAudioProxyEndpoint.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/ExclavesAudioProxyDebugInterface.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/ExclavesAudioProxyDebugTightbeam.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/ExclavesAudioProxyDriverInterface.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/ExclavesAudioProxyDriverTightbeam.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Endpoint/ExclavesAudioProxyEndpoint.cpp"

```
