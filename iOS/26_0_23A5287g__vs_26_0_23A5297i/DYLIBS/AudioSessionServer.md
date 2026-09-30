## AudioSessionServer

> `/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`

```diff

-398.104.0.0.0
-  __TEXT.__text: 0x72850
+398.106.0.0.0
+  __TEXT.__text: 0x72868
   __TEXT.__auth_stubs: 0x1110
   __TEXT.__objc_methlist: 0xc28
   __TEXT.__gcc_except_tab: 0xac98

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4E63FF69-F781-3B12-B64F-F4BE8A285E13
+  UUID: CE0733CB-1C3D-379E-B2D7-FBBAFAC90A41
   Functions: 1661
   Symbols:   5752
   CStrings:  1582
Symbols:
+ __ZN4avas12WorkloopPool10DispatchIDC1ENS_21WorkLoopOperationTypeERK13audit_token_tNSt3__18optionalIjEE
- __ZN4avas12WorkloopPool10DispatchIDC1ERK13audit_token_tNSt3__18optionalIjEE
Functions:
~ -[AVAudioSessionRemoteXPCClient setProperties:values:MXProperties:batchStrategy:genericMXPipe:reply:] : 452 -> 456
~ -[AVAudioSessionRemoteXPCClient getProperty:propertyName:MXProperty:reply:] : 436 -> 440
~ -[AVAudioSessionRemoteXPCClient getMXPropertyGenericPipe:propertyName:reply:] : 428 -> 432
~ -[AVAudioSessionRemoteXPCClient getProperties:properties:reply:] : 428 -> 432
~ -[AVAudioSessionRemoteXPCClient getPropertiesForCache:reply:] : 460 -> 464
~ -[AVAudioSessionRemoteXPCClient getDeferredMessages:reply:] : 372 -> 376

```
