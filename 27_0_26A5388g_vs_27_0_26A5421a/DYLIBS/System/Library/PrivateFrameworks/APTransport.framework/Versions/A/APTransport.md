## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/Versions/A/APTransport`

```diff

-980.71.1.0.0
-  __TEXT.__text: 0x8defc
-  __TEXT.__objc_methlist: 0x1a54
-  __TEXT.__const: 0x3f0
-  __TEXT.__gcc_except_tab: 0x830
-  __TEXT.__cstring: 0x24bf6
+980.77.5.3.0
+  __TEXT.__text: 0x8ea70
+  __TEXT.__objc_methlist: 0x1a64
+  __TEXT.__const: 0x63c
+  __TEXT.__gcc_except_tab: 0x850
+  __TEXT.__cstring: 0x24dee
   __TEXT.__dlopen_cstrs: 0xfe
   __TEXT.__oslogstring: 0x1af
-  __TEXT.__unwind_info: 0x2370
+  __TEXT.__unwind_info: 0x23a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1ae0
+  __DATA_CONST.__const: 0x1b08
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16e8
+  __DATA_CONST.__objc_selrefs: 0x16f0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__got: 0x360
-  __AUTH_CONST.__const: 0x3860
+  __AUTH_CONST.__const: 0x38e0
   __AUTH_CONST.__cfstring: 0x5800
-  __AUTH_CONST.__objc_const: 0x20c0
+  __AUTH_CONST.__objc_const: 0x20c8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x0

   __AUTH.__data: 0x2c0
   __DATA.__objc_ivar: 0x174
   __DATA.__data: 0xeb0
-  __DATA.__bss: 0xc8
+  __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0xaf0
   __DATA_DIRTY.__bss: 0x240

   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4217
-  Symbols:   4646
-  CStrings:  3621
+  Functions: 4234
+  Symbols:   4663
+  CStrings:  3632
 
Symbols:
+ APTNANDataSessionGetV5PairingStatus
+ GCC_except_table30
+ GCC_except_table35
+ GCC_except_table49
+ GCC_except_table72
+ GCC_except_table77
+ _APBrowserDeregisterDiscoveryQueryObserver
+ _APBrowserRegisterDiscoveryQueryObserver
+ _APTNANEndpointGetV5PairingStatus
+ ___APBrowserDeregisterDiscoveryQueryObserver_block_invoke
+ ___APBrowserDeregisterDiscoveryQueryObserver_block_invoke_2
+ ___block_descriptor_52_e8_32b_e5_v8?0l
+ ___block_descriptor_56_e8_32b_e15_v24?0r^v8r^v16l
+ ___block_descriptor_60_e15_v24?0r^v8r^v16l
+ ___browser_addPredicateObserver_block_invoke
+ ___browser_dispatchPredicateObserverNotification_block_invoke
+ ___browser_notifyDeviceObservers_block_invoke
+ ___browser_notifyPredicateObservers_block_invoke
+ ___browser_registerPredicateObserver_block_invoke
+ _browser_copyNANEndpointForDeviceIDInternal
+ _browser_dispatchPredicateObserverNotification
+ _browser_getDevicePredicate
+ browser_addPredicateObserver.sNextTokenCount
- GCC_except_table63
- GCC_except_table64
- GCC_except_table69
- _OUTLINED_FUNCTION_58
- _OUTLINED_FUNCTION_59
- ___browser_notifyDiscoveryObservers_block_invoke
CStrings:
+ "980.77.5.3"
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
