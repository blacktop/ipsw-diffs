## InputAnalytics

> `/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics`

```diff

-111.3.101.0.0
-  __TEXT.__text: 0x1e7d4
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0x2584
+111.3.103.0.0
+  __TEXT.__text: 0x1eaec
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_methlist: 0x257c
   __TEXT.__const: 0x322
-  __TEXT.__cstring: 0x4ca2
-  __TEXT.__oslogstring: 0x2890
-  __TEXT.__gcc_except_tab: 0x3a8
+  __TEXT.__cstring: 0x4cd2
+  __TEXT.__oslogstring: 0x28e0
+  __TEXT.__gcc_except_tab: 0x42c
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x8c
   __TEXT.__swift5_capture: 0x98

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x868
+  __TEXT.__unwind_info: 0x898
   __TEXT.__eh_frame: 0x310
-  __TEXT.__objc_classname: 0x707
-  __TEXT.__objc_methname: 0x4b31
-  __TEXT.__objc_methtype: 0xa65
-  __TEXT.__objc_stubs: 0x2f80
+  __TEXT.__objc_classname: 0x704
+  __TEXT.__objc_methname: 0x4b48
+  __TEXT.__objc_methtype: 0xa50
+  __TEXT.__objc_stubs: 0x2fc0
   __DATA_CONST.__got: 0x240
   __DATA_CONST.__const: 0x1918
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1190
+  __DATA_CONST.__objc_selrefs: 0x1198
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0xdb0
-  __AUTH_CONST.__auth_got: 0x430
-  __AUTH_CONST.__const: 0x568
+  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__const: 0x5a8
   __AUTH_CONST.__cfstring: 0x7a00
-  __AUTH_CONST.__objc_const: 0x3fb0
+  __AUTH_CONST.__objc_const: 0x3f90
   __AUTH_CONST.__objc_intobj: 0xc30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x930
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x228
+  __DATA.__objc_ivar: 0x224
   __DATA.__data: 0x300
-  __DATA.__bss: 0xf0
+  __DATA.__common: 0x8
+  __DATA.__bss: 0xf8
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0xd8
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: CBD73555-A93D-3BC9-9B6A-5B17A0E680EE
-  Functions: 973
-  Symbols:   836
+  UUID: A89B4F75-689C-3D71-BB29-8400D40892FE
+  Functions: 980
+  Symbols:   839
   CStrings:  3159
 
Symbols:
+ _dispatch_sync
+ _objc_sync_enter
+ _objc_sync_exit
CStrings:
+ "@\"<IASAnalyticsTestingDelegateProtocol>\""
+ "IASignalAnalytics: ...returning xpcClient 0x%lx"
+ "IASignalAnalytics: fetching xpcClient..."
+ "T@\"<IASAnalyticsTestingDelegateProtocol>\",W,N,V_testingDelegate"
+ "T@\"NSDate\",C,N,V_lastConsumedSignalTimestamp"
+ "_lastConsumedSignalTimestamp"
+ "_testingDelegate"
+ "com.apple.InputAnalytics.IAXPCClient.sync"
+ "lastConsumedSignalTimestamp"
+ "logMessage called but server is nil"
+ "server called after connection invalidated"
+ "server: returning server 0x%lx"
+ "setLastConsumedSignalTimestamp:"
+ "setTestingDelegate:"
+ "syncQueue"
+ "testingDelegate"
- "@\"<IASServerAnalyticsDelegate>\""
- "@\"IAXPCClient\""
- "@\"IAXPCObject\""
- "T@\"<IASServerAnalyticsDelegate>\",W,N,V_serverDelegate"
- "T@\"IAXPCObject\",&,N,V_lastConsumedAsyncSignal"
- "_lastConsumedAsyncSignal"
- "_serverDelegate"
- "_xpcClient"
- "initialized new %{private}@ xpc client 0x%lx with server 0x%lx"
- "invalidateConnection called"
- "invalidateConnection completed"
- "lastConsumedAsyncSignal"
- "serverDelegate"
- "setLastConsumedAsyncSignal:"
- "setServerDelegate:"

```
