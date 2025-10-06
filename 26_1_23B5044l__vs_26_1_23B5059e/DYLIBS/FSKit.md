## FSKit

> `/System/Library/PrivateFrameworks/FSKit.framework/FSKit`

```diff

-737.40.5.0.0
-  __TEXT.__text: 0x40d90
+737.40.13.0.0
+  __TEXT.__text: 0x40cf4
   __TEXT.__auth_stubs: 0xd30
   __TEXT.__objc_methlist: 0x4a54
   __TEXT.__const: 0x390
-  __TEXT.__gcc_except_tab: 0xd74
-  __TEXT.__oslogstring: 0x30db
+  __TEXT.__gcc_except_tab: 0xd54
+  __TEXT.__oslogstring: 0x3099
   __TEXT.__cstring: 0x432f
   __TEXT.__swift5_typeref: 0x1d1
   __TEXT.__swift5_capture: 0x58

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7412DEC7-CB67-3D5F-9361-3C0E1589987E
-  Functions: 2012
+  UUID: B6D691FB-E6A8-35C9-958D-DADD02E043A2
+  Functions: 2011
   Symbols:   6384
-  CStrings:  3341
+  CStrings:  3339
 
Symbols:
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.273.cold.1
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.274
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.274.cold.1
+ ___57-[FSModuleConnector unloadResource:options:replyHandler:]_block_invoke.278
+ ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke.280
+ ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.283
+ ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.283.cold.1
+ ___block_descriptor_88_e8_32s40s48s56s64bs72r80r_e29_v24?0"NSArray"8"NSError"16ls32l8r72l8s40l8s64l8r80l8s48l8s56l8
+ ___block_literal_global.282
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.cold.3
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.cold.4
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.cold.5
- ___57-[FSModuleConnector unloadResource:options:replyHandler:]_block_invoke.277
- ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke.279
- ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.282
- ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.282.cold.1
- ___block_descriptor_88_e8_32s40s48s56s64bs72r80r_e29_v24?0"NSArray"8"NSError"16ls32l8r72l8s64l8r80l8s40l8s48l8s56l8
- ___block_literal_global.281
CStrings:
+ "%s: Volume implements neither maxFileSizeInBits nor maxFileSize. One of them must be implemented."
+ "%s: delegate load resource returned (nil, nil) updating error to EPROTONOSUPPORT"
+ "%s: load error %@, container status %@"
- "%s: Volume does not implement both maxFileSizeInBits and maxFileSize, while one of them must be implemented."
- "%s: forced-load error %@, container status %@"
- "%s: load reply(nil,nil), container status %@"
- "%s: non forced-load error %@, container status %@"
- "%s: unexpected container error %@"

```
