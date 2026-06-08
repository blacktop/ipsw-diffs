## com.apple.iokit.IOPAudioDriverFamily

> `com.apple.iokit.IOPAudioDriverFamily`

```diff

-340.1.0.0.0
-  __TEXT.__cstring: 0x3739
-  __TEXT.__const: 0x50
-  __TEXT.__os_log: 0x2232
-  __TEXT_EXEC.__text: 0x12024
+400.11.0.0.0
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0x3b50
+  __TEXT.__os_log: 0x2654
+  __TEXT_EXEC.__text: 0x13e70
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x308
-  __DATA.__common: 0x128
-  __DATA_CONST.__auth_got: 0x260
+  __DATA.__common: 0x150
+  __DATA_CONST.__mod_init_func: 0x40
+  __DATA_CONST.__mod_term_func: 0x40
+  __DATA_CONST.__const: 0x22e0
+  __DATA_CONST.__kalloc_type: 0x340
+  __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__mod_init_func: 0x38
-  __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x21a0
-  __DATA_CONST.__kalloc_type: 0x300
-  UUID: B27FEC1D-8E09-348A-BE93-7C3FC7C0763E
-  Functions: 581
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
