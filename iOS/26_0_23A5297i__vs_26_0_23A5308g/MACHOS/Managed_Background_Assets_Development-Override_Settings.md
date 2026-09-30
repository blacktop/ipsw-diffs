## Managed Background Assets Development-Override Settings

> `/System/Library/PreferenceBundles/Managed Background Assets Development-Override Settings.bundle/Managed Background Assets Development-Override Settings`

```diff

-1.0.52.0.0
-  __TEXT.__text: 0x1bc4
-  __TEXT.__auth_stubs: 0x450
+1.0.55.0.0
+  __TEXT.__text: 0x1adc
+  __TEXT.__auth_stubs: 0x430
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__cstring: 0x1f4
+  __TEXT.__cstring: 0x1fa
   __TEXT.__objc_methname: 0xc6
   __TEXT.__const: 0xb2
   __TEXT.__constg_swiftt: 0x7c

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
   __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x228
+  __DATA_CONST.__auth_got: 0x218
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0xd0
   __DATA_CONST.__const: 0x100

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B0DB7081-A8CC-31F7-905E-27B55C4FDF40
+  UUID: 532CE42E-D40F-3A9A-8E89-2C0BA3F85A29
   Functions: 25
   Symbols:   53
   CStrings:  23
Functions:
~ sub_1c94 : 2836 -> 2604
CStrings:
+ "The URL of the mock server from which development apps on this device should download asset packs. Include the URL’s HTTPS scheme and port but omit its path."
+ "https://example.com:49152"
- "The URL of the mock server from which development apps on this device should download asset packs. Include the URL’s HTTPS scheme but omit its path."
- "https://example.com"

```
