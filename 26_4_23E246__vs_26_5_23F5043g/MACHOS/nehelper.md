## nehelper

> `/usr/libexec/nehelper`

```diff

-2226.102.1.0.0
-  __TEXT.__text: 0x2672c
+2226.120.12.0.0
+  __TEXT.__text: 0x268e0
   __TEXT.__auth_stubs: 0x1070
   __TEXT.__objc_stubs: 0x2980
   __TEXT.__objc_methlist: 0x44c
   __TEXT.__const: 0x11c
   __TEXT.__gcc_except_tab: 0xa24
   __TEXT.__objc_methname: 0x1f39
-  __TEXT.__oslogstring: 0x496b
-  __TEXT.__cstring: 0x5e3f
+  __TEXT.__cstring: 0x5e70
+  __TEXT.__oslogstring: 0x4a05
   __TEXT.__objc_classname: 0x1a4
   __TEXT.__objc_methtype: 0x26e
   __TEXT.__unwind_info: 0x420
   __DATA_CONST.__auth_got: 0x848
-  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__got: 0x398
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xc98
+  __DATA_CONST.__const: 0xcb0
   __DATA_CONST.__cfstring: 0x5120
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F8207F94-1CB5-350C-9485-FB88272C7561
+  UUID: E00B1896-E329-3FC7-BAF6-43C775B4CA13
   Functions: 245
-  Symbols:   376
-  CStrings:  2340
+  Symbols:   377
+  CStrings:  2346
 
Symbols:
+ _kSecUseSystemKeychainAlways
Functions:
~ sub_100002ce4 : 1628 -> 1684
~ sub_100003340 -> sub_100003378 : 2228 -> 2608
CStrings:
+ "%@ GetCertificateData: persistentRef length=%lu"
+ "%@ SecItemCopyMatching failed for certificate, status=%d"
+ "%@ processing Relay Manager message: %s (command=%llu)"
+ "%@ system keychain lookup failed (%d), trying default keychain"
+ "GetCertificateData"
+ "GetIdentityProxy"
+ "Ping"
+ "Unknown"
- "%@ SecItemCopyMatching failed %d"
- "%@ processing Relay Manager message"

```
