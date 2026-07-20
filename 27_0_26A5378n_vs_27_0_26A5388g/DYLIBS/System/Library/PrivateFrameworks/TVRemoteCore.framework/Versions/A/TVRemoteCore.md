## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/Versions/A/TVRemoteCore`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-627.0.14.0.0
-  __TEXT.__text: 0x4b980
-  __TEXT.__objc_methlist: 0x6398
+627.0.19.0.0
+  __TEXT.__text: 0x4bd8c
+  __TEXT.__objc_methlist: 0x63a8
   __TEXT.__const: 0x290
   __TEXT.__cstring: 0x367f
   __TEXT.__gcc_except_tab: 0xb04
-  __TEXT.__oslogstring: 0x6615
-  __TEXT.__unwind_info: 0x1210
+  __TEXT.__oslogstring: 0x6653
+  __TEXT.__unwind_info: 0x11f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f88
+  __DATA_CONST.__objc_selrefs: 0x2f90
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_arraydata: 0x108

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2152
-  Symbols:   4740
-  CStrings:  1267
+  Functions: 2153
+  Symbols:   4742
+  CStrings:  1268
 
Symbols:
+ -[TVRCMatchPointDeviceQuery _cachedHomeInManager:]
+ _objc_msgSend$_cachedHomeInManager:
Functions:
~ -[TVRCMatchPointDeviceQuery stop] : 316 -> 280
~ -[TVRCMatchPointDeviceQuery homeManagerDidUpdateHomes:] : 316 -> 332
~ -[TVRCMatchPointDeviceQuery homeManagerDidUpdateCurrentHome:] : 456 -> 480
+ -[TVRCMatchPointDeviceQuery _cachedHomeInManager:]
~ ___75-[TVRCRPCompanionLinkClientWrapper sendEvent:options:shouldRetry:response:]_block_invoke : 600 -> 656
~ ___82-[TVRCRPCompanionLinkClientWrapper fetchUpNextInfoWithPaginationToken:completion:]_block_invoke : 304 -> 368
~ ___80-[TVRCRPCompanionLinkClientWrapper markAsWatchedWithMediaIdentifier:completion:]_block_invoke : 220 -> 284
~ ___74-[TVRCRPCompanionLinkClientWrapper addItemWithMediaIdentifier:completion:]_block_invoke : 220 -> 284
~ ___77-[TVRCRPCompanionLinkClientWrapper removeItemWithMediaIdentifier:completion:]_block_invoke : 220 -> 284
~ ___56-[TVRCRPCompanionLinkClientWrapper playItem:completion:]_block_invoke : 220 -> 284
~ ___76-[TVRCRPCompanionLinkClientWrapper fetchLaunchableAppsWithRange:completion:]_block_invoke : 224 -> 288
~ ___69-[TVRCRPCompanionLinkClientWrapper launchAppWithBundleID:completion:]_block_invoke : 220 -> 284
CStrings:
+ "Received request response with ID %@, responseKeyCount %lu, keys %@, error %@"
+ "currentHome is nil, reusing cached home: %@"
- "Received request response with ID %@, response %@, error %@"
```
