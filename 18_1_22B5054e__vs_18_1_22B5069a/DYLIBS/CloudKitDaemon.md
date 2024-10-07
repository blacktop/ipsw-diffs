## CloudKitDaemon

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon`

```diff

-2220.11.0.0.0
-  __TEXT.__text: 0x32590c
+2220.14.0.0.0
+  __TEXT.__text: 0x3268fc
   __TEXT.__auth_stubs: 0x3550
-  __TEXT.__objc_methlist: 0x2ad84
+  __TEXT.__objc_methlist: 0x2ae04
   __TEXT.__const: 0x2480
   __TEXT.__swift5_typeref: 0xbbe
   __TEXT.__swift5_capture: 0x24c
-  __TEXT.__cstring: 0x23a05
-  __TEXT.__oslogstring: 0x28123
+  __TEXT.__cstring: 0x23bd3
+  __TEXT.__oslogstring: 0x28319
   __TEXT.__swift5_reflstr: 0x4d0
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__constg_swiftt: 0x82c

   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_proto: 0x1e4
   __TEXT.__swift5_types: 0xa4
-  __TEXT.__gcc_except_tab: 0xc2d8
+  __TEXT.__gcc_except_tab: 0xc404
   __TEXT.__ustring: 0x2c
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0xacc0
+  __TEXT.__unwind_info: 0xad18
   __TEXT.__eh_frame: 0x1668
   __TEXT.__objc_classname: 0x4dc0
-  __TEXT.__objc_methname: 0x5340b
+  __TEXT.__objc_methname: 0x536b8
   __TEXT.__objc_methtype: 0x7faa
-  __TEXT.__objc_stubs: 0x34680
-  __DATA_CONST.__got: 0x18d8
+  __TEXT.__objc_stubs: 0x34800
+  __DATA_CONST.__got: 0x18e0
   __DATA_CONST.__const: 0x8718
   __DATA_CONST.__objc_classlist: 0x1250
   __DATA_CONST.__objc_catlist: 0x130
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10b80
+  __DATA_CONST.__objc_selrefs: 0x10be0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x1180
   __DATA_CONST.__objc_arraydata: 0x13b8
   __AUTH_CONST.__auth_got: 0x1ab8
-  __AUTH_CONST.__auth_ptr: 0x320
+  __AUTH_CONST.__auth_ptr: 0x318
   __AUTH_CONST.__const: 0x3880
-  __AUTH_CONST.__cfstring: 0x1e880
-  __AUTH_CONST.__objc_const: 0x434e8
+  __AUTH_CONST.__cfstring: 0x1e920
+  __AUTH_CONST.__objc_const: 0x43558
   __AUTH_CONST.__objc_arrayobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0xaa0
   __AUTH_CONST.__objc_intobj: 0xa80
   __AUTH.__objc_data: 0x5bd0
   __AUTH.__data: 0x328
-  __DATA.__objc_ivar: 0x15d0
+  __DATA.__objc_ivar: 0x15d8
   __DATA.__data: 0x55a8
   __DATA.__bss: 0x2148
   __DATA.__common: 0x110

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 17770
-  Symbols:   2738
-  CStrings:  21778
+  Functions: 17785
+  Symbols:   2740
+  CStrings:  21808
 
Symbols:
+ _OBJC_CLASS_$_CKDPCSNotifier
+ _OBJC_METACLASS_$_CKDPCSNotifier
CStrings:
+ "Adding services: %!@(MISSING) to services needing DBR re-authentication set."
+ "CKNilIfEmpty"
+ "Fake DBR account key sync failure"
+ "FakeDBRAccountNeedsReauthenticationPCSError"
+ "Faking DBR account needs re-authentication error from PCS"
+ "Key sync tracker for service: %!@(MISSING) raced with guitarfish repair callback."
+ "Received DBR account became ready notification %!{(MISSING)public}@"
+ "Service blocked from performing key sync due to DBR account re-auth needed. Direct user to settings to re-auth their account."
+ "Service: %!@(MISSING) needs DBR re-authentication. Setting account status temporarily unavailable for container: %!@(MISSING)"
+ "Stingray service %!@(MISSING) requested key sync while other outstanding services require DBR re-auth. Adding service to services needing DBR re-auth."
+ "T@\"NSMutableSet\",&,N,V_mutableServicesNeedingDBRReauthentication"
+ "T@\"NSSet\",R,N"
+ "TB,N,V_racedWithGuitarfishRepairCallback"
+ "User key sync failed due to DBR account re-auth needed. Direct user to settings to re-auth their account."
+ "_guitarfishRepairCallback_block_invoke"
+ "_mutableServicesNeedingDBRReauthentication"
+ "_racedWithGuitarfishRepairCallback"
+ "addServicesNeedingDBRReauthentication:"
+ "clearServicesNeedingDBRReauthentication"
+ "com.apple.ProtectedCloudStorage.GuitarfishRepairCompleted"
+ "hasOutstandingServicesNeedingDBRReauthentication"
+ "mutableServicesNeedingDBRReauthentication"
+ "notifier.servicesNeedingDBRReauthentication.count == 0"
+ "racedWithGuitarfishRepairCallback"
+ "serviceNeedsDBRReauthentication:"
+ "servicesNeedingDBRReauthentication"
+ "setMutableServicesNeedingDBRReauthentication:"
+ "setRacedWithGuitarfishRepairCallback:"
+ "setRacedWithGuitarfishRepairCallbackOnAllOutstandingHandlersWithCompletion:"
+ "setupGuitarfishRepairNotificationHandling"

```
