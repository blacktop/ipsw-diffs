## seserviced

> `/usr/libexec/seserviced`

```diff

-60.31.0.0.0
-  __TEXT.__text: 0x3ebe4c
-  __TEXT.__auth_stubs: 0x49f0
+60.32.0.0.0
+  __TEXT.__text: 0x3ec554
+  __TEXT.__auth_stubs: 0x4a00
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0x2c4
-  __TEXT.__objc_stubs: 0x9c40
-  __TEXT.__objc_methlist: 0x64cc
-  __TEXT.__const: 0xeca8
-  __TEXT.__gcc_except_tab: 0x34c8
-  __TEXT.__objc_methname: 0x12eed
-  __TEXT.__oslogstring: 0x2a189
-  __TEXT.__cstring: 0x233a0
+  __TEXT.__objc_stubs: 0x9c60
+  __TEXT.__objc_methlist: 0x64dc
+  __TEXT.__const: 0xece8
+  __TEXT.__gcc_except_tab: 0x34cc
+  __TEXT.__objc_methname: 0x12f21
+  __TEXT.__oslogstring: 0x2a269
+  __TEXT.__cstring: 0x233d0
   __TEXT.__objc_classname: 0x11be
-  __TEXT.__objc_methtype: 0x6623
-  __TEXT.__swift5_typeref: 0x4b8a
+  __TEXT.__objc_methtype: 0x668b
+  __TEXT.__swift5_typeref: 0x4bac
   __TEXT.__constg_swiftt: 0x4d40
-  __TEXT.__swift5_reflstr: 0x542a
-  __TEXT.__swift5_fieldmd: 0x5280
+  __TEXT.__swift5_reflstr: 0x543a
+  __TEXT.__swift5_fieldmd: 0x528c
   __TEXT.__swift5_builtin: 0x2bc
   __TEXT.__swift5_assocty: 0x6c0
-  __TEXT.__swift5_capture: 0x2478
-  __TEXT.__swift5_proto: 0x808
+  __TEXT.__swift5_capture: 0x2488
+  __TEXT.__swift5_proto: 0x80c
   __TEXT.__swift5_types: 0x51c
-  __TEXT.__swift_as_entry: 0x3a4
+  __TEXT.__swift_as_entry: 0x3a8
   __TEXT.__swift_as_ret: 0x5a8
   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_mpenum: 0x90
-  __TEXT.__unwind_info: 0x9958
-  __TEXT.__eh_frame: 0x13a64
-  __DATA_CONST.__auth_got: 0x2510
-  __DATA_CONST.__got: 0x15b8
+  __TEXT.__unwind_info: 0x9988
+  __TEXT.__eh_frame: 0x13acc
+  __DATA_CONST.__auth_got: 0x2518
+  __DATA_CONST.__got: 0x15c0
   __DATA_CONST.__auth_ptr: 0xdd8
-  __DATA_CONST.__const: 0x11958
-  __DATA_CONST.__cfstring: 0x8dc0
+  __DATA_CONST.__const: 0x119f8
+  __DATA_CONST.__cfstring: 0x8de0
   __DATA_CONST.__objc_classlist: 0x768
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x420

   __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_intobj: 0x810
-  __DATA.__objc_const: 0x15a68
-  __DATA.__objc_selrefs: 0x43f8
+  __DATA.__objc_const: 0x15a88
+  __DATA.__objc_selrefs: 0x4400
   __DATA.__objc_ivar: 0xb34
   __DATA.__objc_data: 0x62e0
-  __DATA.__data: 0xbb3c
-  __DATA.__bss: 0xe410
-  __DATA.__common: 0x6f8
+  __DATA.__data: 0xbb0c
+  __DATA.__bss: 0xe490
+  __DATA.__common: 0x700
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4ACDF5EC-A712-37CE-9177-8EC188F17203
-  Functions: 11526
-  Symbols:   2098
-  CStrings:  11816
+  UUID: 513609FA-8574-3D4A-AE03-7494DBBDC516
+  Functions: 11540
+  Symbols:   2100
+  CStrings:  11819
 
Symbols:
+ _$s10Foundation4DateVSLAAMc
+ _$sSL1loiySbx_xtFZTj
CStrings:
+ "-[SESEndpointAndKeyXPCServer(SEKeyXPC) findAndAttest:challenge:usingProxy:callback:]"
+ "Biolockout prompt triggered, scanning disabled"
+ "Disabling scanning when biolock is active and no geofence entry exception"
+ "Processing pass %s named %s, user deletable: %{bool}d, instance AIDs: %s"
+ "Setting scanning to %{bool}d with low power mode %{bool}d, Uwb suspended %{bool}d, biolockout backoff %{bool}d, express reader group identifiers %s, adaptive connection rssi threshold %hhd, device stationary %{bool}d, biolock %{bool}d, and geofence entry state %{bool}d"
+ "Vv48@0:8@\"SEFidoKeySearchParameters\"16@\"NSData\"24@\"<SEProxyInterface>\"32@?<v@?@\"SEFidoKey\"@\"NSError\">40"
+ "findAndAttest:challenge:usingProxy:callback:"
+ "findAndLoadKey:secureElement:error:"
+ "iOS (26.0) - SecureElementService-60.32"
+ "wiredVisibility"
- "Ending biolockout backoff for %f seconds for Lyon"
- "Processing pass %s named %s, user deletable: %{bool}d"
- "Scanning disabled till device exits biolockout"
- "Starting biolockout backoff for %f seconds for Lyon"
- "biolockoutBackoffDuration"
- "debug.lyon.biolockoutBackoff.durationInSeconds"
- "home:didEnableNotifications:"
- "iOS (26.0) - SecureElementService-60.31"

```
