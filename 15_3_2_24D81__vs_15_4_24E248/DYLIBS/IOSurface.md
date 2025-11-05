## IOSurface

> `/System/Library/Frameworks/IOSurface.framework/Versions/A/IOSurface`

```diff

-372.3.5.0.0
-  __TEXT.__text: 0x118cc
+372.5.2.0.0
+  __TEXT.__text: 0x11990
   __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__objc_methlist: 0x790
+  __TEXT.__objc_methlist: 0x7c8
   __TEXT.__cstring: 0x24df
   __TEXT.__const: 0x6b
   __TEXT.__oslogstring: 0x415

   __AUTH_CONST.__auth_got: 0x608
   __AUTH_CONST.__const: 0x258
   __AUTH_CONST.__cfstring: 0x1d00
-  __AUTH_CONST.__objc_const: 0xeb0
+  __AUTH_CONST.__objc_const: 0xe58
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x370

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9A10F15D-D321-3810-B726-57F9362B16D0
-  Functions: 574
-  Symbols:   1351
+  UUID: 6C3DA69E-3122-3BCF-8C7E-B9E375A65E8A
+  Functions: 581
+  Symbols:   1366
   CStrings:  899
 
Symbols:
+ +[IOSurfaceRemotePerSurfaceGlobalState globalStateForSurface:mappedAddress:mappedSize:extraData:].cold.1
+ -[IOSurfaceRemotePerSurfacePerClientState removeClientReferenceToSurface].cold.1
+ -[IOSurfaceRemoteRemoteClient _getClient:inboundExtradata:outboundExtraData:].cold.1
+ IOSurfaceSharedEventNotifyEventListener.cold.1
+ _copySniffKeyFromStruct.cold.1
+ _ensureKeySniffDictionaries.cold.1
+ _ioSurfaceDeserializedFromXPCDictionaryWithKey.cold.2
+ _ioSurfaceDeserializedFromXPCDictionaryWithKey.cold.3
+ _ioSurfaceSerializeToXPCDictionaryWithKey.cold.1
+ _ioSurfaceSerializeToXPCDictionaryWithKey.cold.2
+ _ioSurfaceSerializeToXPCDictionaryWithKey.cold.3
+ _sniffKeysToMask.cold.1
+ _sniffKeysToStruct.cold.1
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurface/IOSurfaceUser/IOSurfaceClient.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/IOSurface/IOSurfaceUser/IOSurfaceClient.m"

```
