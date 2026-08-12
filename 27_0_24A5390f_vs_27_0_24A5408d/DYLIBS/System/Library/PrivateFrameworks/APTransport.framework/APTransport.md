## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-980.71.1.0.0
-  __TEXT.__text: 0xb5c2c
+980.75.1.0.0
+  __TEXT.__text: 0xb68a0
   __TEXT.__objc_methlist: 0x1cf4
-  __TEXT.__const: 0x418
-  __TEXT.__gcc_except_tab: 0x9fc
-  __TEXT.__cstring: 0x3089c
+  __TEXT.__const: 0x664
+  __TEXT.__gcc_except_tab: 0xa1c
+  __TEXT.__cstring: 0x30a92
   __TEXT.__dlopen_cstrs: 0x1f3
   __TEXT.__oslogstring: 0x31c
-  __TEXT.__unwind_info: 0x2d20
+  __TEXT.__unwind_info: 0x2d60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3db8
+  __DATA_CONST.__const: 0x3e08
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__got: 0x400
-  __AUTH_CONST.__const: 0x2db8
+  __AUTH_CONST.__const: 0x2dd8
   __AUTH_CONST.__cfstring: 0x6600
   __AUTH_CONST.__objc_const: 0x2498
   __AUTH_CONST.__objc_arrayobj: 0x48

   __AUTH.__data: 0x2c0
   __DATA.__objc_ivar: 0x18c
   __DATA.__data: 0x14a0
-  __DATA.__bss: 0x128
+  __DATA.__bss: 0x130
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__data: 0xcb0
   __DATA_DIRTY.__bss: 0x2c8

   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5352
-  Symbols:   5009
-  CStrings:  4563
+  Functions: 5368
+  Symbols:   5026
+  CStrings:  4574
 
Symbols:
+ GCC_except_table26
+ GCC_except_table31
+ GCC_except_table34
+ GCC_except_table43
+ GCC_except_table61
+ GCC_except_table62
+ GCC_except_table67
+ _APBrowserDeregisterDiscoveryQueryObserver
+ _APBrowserRegisterDiscoveryQueryObserver
+ _APTNANEndpointGetV5PairingStatus
+ ___APBrowserDeregisterDiscoveryQueryObserver_block_invoke
+ ___APBrowserDeregisterDiscoveryQueryObserver_block_invoke_2
+ ___block_descriptor_56_e8_32b_e15_v24?0r^v8r^v16ls32l8
+ ___block_descriptor_60_e15_v24?0r^v8r^v16l
+ ___browser_addPredicateObserver_block_invoke
+ ___browser_dispatchPredicateObserverNotification_block_invoke
+ ___browser_notifyDeviceObservers_block_invoke
+ ___browser_notifyPredicateObservers_block_invoke
+ ___browser_registerPredicateObserver_block_invoke
+ _browser_addPredicateObserver.sNextTokenCount
+ _browser_copyNANEndpointForDeviceIDInternal
+ _browser_dispatchPredicateObserverNotification
+ _browser_getDevicePredicate
- GCC_except_table57
- GCC_except_table58
- GCC_except_table60
- GCC_except_table63
- _OUTLINED_FUNCTION_61
- ___browser_notifyDiscoveryObservers_block_invoke
CStrings:
+ "980.75.1"
+ "APTNANDataSessionGetV5PairingStatus"
+ "H"
+ "HomePod"
+ "NANDS [%{ptr}] Infra 6GHz steer failed"
+ "NANDS [%{ptr}] Infra 6GHz steer found no candidates"
+ "NANDS [%{ptr}] Infra relay required"
+ "OSStatus _APTNANDataSessionTranslateKnownActivationError(APTNANDataSessionRef, OSStatus)"
+ "OSStatus _APTNANDataSessionTranslateKnownActivationPairingError(APTNANDataSessionRef, APTNANPairingDelegate *, OSStatus)"
+ "Predicate [ All: %{flags}, Any: %{flags} ] matched for device: %@ %{flags}"
+ "[%@:%@] %s device - name: %'@ model: %@ flags: %#ll{flags} relationship: %d systemPairingID: %@ serviceAvailable: %s\n"
+ "_APTNANDataSessionTranslateKnownActivationPairingError"
+ "browser_addPredicateObserver"
+ "browser_removePredicateObserver"
+ "void browser_notifyPredicateObservers(APBrowserRef, CFNumberRef)_block_invoke"
- "980.71.1"
- "OSStatus _APTNANDataSessionHandleUnifiedPairingIfNecessary(APTNANDataSessionRef, CUNANDataSession *, APTNANPairingDelegate *, OSStatus)"
- "[%@:%@] %s device - name: %'@ model: %@ flags: %llx relationship: %d systemPairingID: %@ serviceAvailable: %s\n"
- "fakeInfraRelayFailed"
```
