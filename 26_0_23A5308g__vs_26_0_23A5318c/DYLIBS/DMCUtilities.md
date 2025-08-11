## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities`

```diff

-50.0.0.0.0
-  __TEXT.__text: 0x34af4
+52.0.0.0.0
+  __TEXT.__text: 0x34df0
   __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_methlist: 0x2db4
+  __TEXT.__objc_methlist: 0x2dd4
   __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x7b8
-  __TEXT.__cstring: 0x3737
-  __TEXT.__oslogstring: 0x520d
+  __TEXT.__gcc_except_tab: 0x7c4
+  __TEXT.__cstring: 0x3740
+  __TEXT.__oslogstring: 0x5280
   __TEXT.__dlopen_cstrs: 0x165
   __TEXT.__unwind_info: 0xe00
   __TEXT.__objc_classname: 0x4b7
-  __TEXT.__objc_methname: 0x9a25
-  __TEXT.__objc_methtype: 0x1335
-  __TEXT.__objc_stubs: 0x6240
+  __TEXT.__objc_methname: 0x9ae6
+  __TEXT.__objc_methtype: 0x1347
+  __TEXT.__objc_stubs: 0x6280
   __DATA_CONST.__got: 0x690
   __DATA_CONST.__const: 0x11e8
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2550
+  __DATA_CONST.__objc_selrefs: 0x2568
   __DATA_CONST.__objc_superrefs: 0xc8
   __AUTH_CONST.__auth_got: 0x778
   __AUTH_CONST.__const: 0xd20
   __AUTH_CONST.__cfstring: 0x40a0
-  __AUTH_CONST.__objc_const: 0x4350
+  __AUTH_CONST.__objc_const: 0x4380
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH.__objc_data: 0xf00
-  __DATA.__objc_ivar: 0x208
+  __DATA.__objc_ivar: 0x20c
   __DATA.__data: 0x300
   __DATA.__bss: 0x968
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B2658550-CDC7-347F-A765-470BA52FB09D
-  Functions: 1386
-  Symbols:   5077
-  CStrings:  3254
+  UUID: 0601B0D5-E405-3B11-B066-776C0289984B
+  Functions: 1391
+  Symbols:   5090
+  CStrings:  3262
 
Symbols:
+ -[DMCNetworkMonitor _deviceMightHaveNetworkStrict:]
+ -[DMCNetworkMonitor _notifyRegularClients]
+ -[DMCNetworkMonitor _notifyStrictClients]
+ -[DMCNetworkMonitor cachedStrictCompletionHandlers]
+ -[DMCNetworkMonitor setCachedStrictCompletionHandlers:]
+ -[DMCNetworkMonitor waitForNetworkWithTimeout:strict:completionHandler:]
+ _OBJC_IVAR_$_DMCNetworkMonitor._cachedStrictCompletionHandlers
+ ___72-[DMCNetworkMonitor waitForNetworkWithTimeout:strict:completionHandler:]_block_invoke
+ ___72-[DMCNetworkMonitor waitForNetworkWithTimeout:strict:completionHandler:]_block_invoke.5
+ ___72-[DMCNetworkMonitor waitForNetworkWithTimeout:strict:completionHandler:]_block_invoke.7
+ ___72-[DMCNetworkMonitor waitForNetworkWithTimeout:strict:completionHandler:]_block_invoke_2
+ ___72-[DMCNetworkMonitor waitForNetworkWithTimeout:strict:completionHandler:]_block_invoke_2.8
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32bs40r_e8_v12?0B8lr40l8s32l8
+ ___block_descriptor_57_e8_32s40bs_e5_v8?0ls32l8s40l8
+ _objc_msgSend$_deviceMightHaveNetworkStrict:
+ _objc_msgSend$_notifyRegularClients
+ _objc_msgSend$_notifyStrictClients
+ _objc_msgSend$cachedStrictCompletionHandlers
+ _objc_msgSend$waitForNetworkWithTimeout:strict:completionHandler:
- -[DMCNetworkMonitor _deviceMightHaveNetwork]
- -[DMCNetworkMonitor _notifyAllClients]
- -[DMCNetworkMonitor waitForNetworkWithCompletionHandler:timeout:]
- ___65-[DMCNetworkMonitor waitForNetworkWithCompletionHandler:timeout:]_block_invoke
- ___65-[DMCNetworkMonitor waitForNetworkWithCompletionHandler:timeout:]_block_invoke.5
- ___65-[DMCNetworkMonitor waitForNetworkWithCompletionHandler:timeout:]_block_invoke_2
- ___block_descriptor_48_e8_32bs40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_56_e8_32bs40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
- _objc_msgSend$_deviceMightHaveNetwork
- _objc_msgSend$_notifyAllClients
- _objc_msgSend$waitForNetworkWithCompletionHandler:timeout:
CStrings:
+ "DMCNetworkMonitor: Device might have network now. path status: %ld, interface type: %{public}@"
+ "DMCNetworkMonitor: Device should have network now. path status: %ld, interface type: %{public}@"
+ "T@\"NSMutableArray\",&,N,V_cachedStrictCompletionHandlers"
+ "_cachedStrictCompletionHandlers"
+ "_deviceMightHaveNetworkStrict:"
+ "_notifyRegularClients"
+ "_notifyStrictClients"
+ "cachedStrictCompletionHandlers"
+ "setCachedStrictCompletionHandlers:"
+ "v12@?0B8"
+ "v36@0:8d16B24@?28"
+ "waitForNetworkWithTimeout:strict:completionHandler:"
- "Device might have network now. path status: %ld, interface type: %{public}@"
- "_deviceMightHaveNetwork"
- "_notifyAllClients"
- "waitForNetworkWithCompletionHandler:timeout:"

```
