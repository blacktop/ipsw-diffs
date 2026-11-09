## DigitalSeparation

> `/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`

```diff

-653.0.10.0.0
-  __TEXT.__text: 0x3a090
-  __TEXT.__objc_methlist: 0x202c
+653.0.10.0.2
+  __TEXT.__text: 0x3a21c
+  __TEXT.__objc_methlist: 0x203c
   __TEXT.__cstring: 0x1927
   __TEXT.__const: 0xbc8
   __TEXT.__gcc_except_tab: 0xb8c
-  __TEXT.__oslogstring: 0x2844
+  __TEXT.__oslogstring: 0x28d4
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__swift5_typeref: 0x51c
   __TEXT.__swift5_capture: 0x1c8

   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift_as_cont: 0x90
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__unwind_info: 0x1170
+  __TEXT.__unwind_info: 0x1190
   __TEXT.__eh_frame: 0xd10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15c0
+  __DATA_CONST.__objc_selrefs: 0x15c8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__got: 0x550

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1275
-  Symbols:   1843
-  CStrings:  477
+  Functions: 1277
+  Symbols:   1844
+  CStrings:  479
 
Symbols:
+ -[DSAppSharing isThirdPartyApp:]
Functions:
~ -[DSAppSharing resetFileAccessPermissionsForApp:withCompletionHandler:] : 196 -> 320
+ -[DSAppSharing isThirdPartyApp:]
+ -[DSAppSharing isThirdPartyApp:].cold.1
CStrings:
+ "Error determining whether %@ is a third party app: %@"
+ "Not resetting file access for %@ because it is a first party app and doing so would cause a crash"
```
