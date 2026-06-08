## com.apple.iokit.IOPAudioDriverFamily

> `com.apple.iokit.IOPAudioDriverFamily`

```diff

-340.1.0.0.0
-  __TEXT.__cstring: 0x3739 sha256:541eba9d25bcc752efda7206e9beeb56adc9965b946c05fd9a04d95ed4e335e4
-  __TEXT.__const: 0x50 sha256:ad9065dc90eefe171742b488a48172c5aaa6ff6df41a74b1273d0e769a088e55
-  __TEXT.__os_log: 0x2232 sha256:02729c9b091f7b37116b1e2ed9a4ea93484d71ea70a3662251b6b4bbaa2a17d5
-  __TEXT_EXEC.__text: 0x12024 sha256:1a83465d1caf7973b6207f35c9ded3e7b52041282da8785b499864263929b79c
+400.11.0.0.0
+  __TEXT.__const: 0x60 sha256:6fd30f710a8b05a759e1d145a51f102e0f24b24bb8c2c5a26b1ca39a5e069854
+  __TEXT.__cstring: 0x3b50 sha256:17035b5a43ce83d063810f4e80f539f65991d573f6832acdccf6fa1182500faa
+  __TEXT.__os_log: 0x2654 sha256:7bd2b6efe145dfbd5749b4f5d4bbbb3d9544f2444070dd367d9ca9af2f313689
+  __TEXT_EXEC.__text: 0x13e70 sha256:a7332ae0b2adc56d9a65fd983405e2fb0e7461a31ef726e2d0496d4b524adff4
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x308 sha256:5d83c66302ee5ba4babbb08b0a5ab35847bd51bf1ae690a13a0ccba014d91804
-  __DATA.__common: 0x128 sha256:250f52cb2d6f1966a29f6ac771fa1cd185b8f8531396c8a4026c0fe635617e0c
-  __DATA_CONST.__auth_got: 0x260 sha256:a6b2bcdc231b0d73bc4d96cd863f3a81460eaebe4477a4feb31e8863d9c8f57b
-  __DATA_CONST.__got: 0xa0 sha256:a0b8fbf57d8b59df54fa1d357942114cad1a23848453db175e95f2ca08bb6389
-  __DATA_CONST.__mod_init_func: 0x38 sha256:5a29f67a632c08f8109e45b18adc3c97206332584f9484cc4f80010ebd132986
-  __DATA_CONST.__mod_term_func: 0x38 sha256:b5fdbd3f869504045f648393d866d135a5370c729f9d92bda1392ad0e7892624
-  __DATA_CONST.__const: 0x21a0 sha256:9d5079752e4dd590e9b21f99abc616bb05cfa0304374e7a4f87082fa203e2059
-  __DATA_CONST.__kalloc_type: 0x300 sha256:1bd301f58daac77da1216fcac406eadc17d87aabc56b67f9c45a1fbd48355425
-  UUID: B27FEC1D-8E09-348A-BE93-7C3FC7C0763E
-  Functions: 581
+  __DATA.__data: 0x308 sha256:73ca80f663e1bea34d4b7a852c0702d1126489e46e9a479145ad6d70b3d8559c
+  __DATA.__common: 0x150 sha256:52a3e0804d93dc525ec3c67ef8ac5b01756ecf0513e36f3c19435e4c82cb5d29
+  __DATA_CONST.__mod_init_func: 0x40 sha256:683e91bc497e0f1ff78a6b076956b692f2ea527f6505d5fafc3800165509c3a4
+  __DATA_CONST.__mod_term_func: 0x40 sha256:5b0aa1d8eba319cbdc2f4117c5b2ed89f646174663872d00c60a575bb1b34f8a
+  __DATA_CONST.__const: 0x22e0 sha256:be1f7a94d941b57e41f7ef7fd327903b61ad7ce874c400493573e83fdbf2542c
+  __DATA_CONST.__kalloc_type: 0x340 sha256:6f3d44953c7b8a5f3a53e101952a07b67ac9b08f409e9624c047388c21df8881
+  __DATA_CONST.__auth_got: 0x288 sha256:02c4b29c35b6a8ca20fc611f5996d11bff18a43f925d277f30d1fed84c31d655
+  __DATA_CONST.__got: 0xa0 sha256:6b587d4d131df38721a0918e4f69532f91c9e9001bf8a46c5e846973777ea3e1
+  UUID: 24E0797F-27FA-39A2-8DCC-3E05C989E159
+  Functions: 635
   Symbols:   0
-  CStrings:  293
+  CStrings:  319
 
CStrings:
+ "!((clientConfig->messageAction) == nullptr)"
+ "!((dispatcher) == nullptr)"
+ "!((domainID) == nullptr)"
+ "!((inCallback) == nullptr)"
+ "!((mAggregateMessageDispatcher) == nullptr)"
+ "!((mMessageDispatchers) == nullptr)"
+ "!(inDomainID == IOPAudio::DomainID::kInvalid)"
+ "!(static_cast<bool>(mMessageDispatchers->getObject(domainID.get())))"
+ "%s::%s() Final domain configuration applied: domainID='%c%c%c%c', iopDomainID='%c%c%c%c'"
+ "%s::%s() Found domain-id property: '%c%c%c%c'"
+ "%s::%s() Found iop-domain-id property: '%c%c%c%c'"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/IOPAudioDriverFamily/src/kext/IOPAudioDriverFamily/core/IOPAudioAggregateMessageDispatcher/IOPAudioAggregateMessageDispatcher.cpp"
+ "11212"
+ "1121212"
+ "112121211222"
+ "1121222"
+ "121111121222121211111112112222"
+ "121112"
+ "IOPAudioAggregateMessageDispatcher"
+ "IOPAudioAggregateMessageDispatcher: Default domain ID set to 0x%x"
+ "IOPAudioAggregateMessageDispatcher: Deregistered message dispatcher for domain %s"
+ "IOPAudioAggregateMessageDispatcher: Registered message dispatcher for domain 0x%x (default domain: 0x%x)"
+ "external-service-name-delimiter"
+ "mMessageDispatchers->setObject(domainID.get(), dispatcher.get())"
+ "name-override"
+ "nameOverride[nameOverrideData->getLength() - 1] == 0"
+ "ret = dispatcher->enable() == 0 "
+ "ret = dispatcher->registerClient(inClient, inCallback) == 0 "
+ "ret = mAggregateMessageDispatcher->registerClient( clientConfig->domainID, inClient, clientConfig->messageAction) == 0 "
+ "retrieveDomainInfoFromDeviceTree"
+ "site.IOPAudioAggregateMessageDispatcher"
- "12111112122212121111111211222"
- "1212"
- "121212"
- "12121211222"
- "121222"

```
