## TelephonyPreferences

> `/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-401.100.1.0.0
-  __TEXT.__text: 0x30c4c
-  __TEXT.__objc_methlist: 0x4000
+405.100.1.0.0
+  __TEXT.__text: 0x30bf4
+  __TEXT.__objc_methlist: 0x3ff8
   __TEXT.__const: 0x516
   __TEXT.__cstring: 0x1eca
   __TEXT.__oslogstring: 0x24fa

   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2358
+  __DATA_CONST.__objc_selrefs: 0x2350
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__got: 0x5d0
   __AUTH_CONST.__const: 0x2f0
   __AUTH_CONST.__cfstring: 0x1b60
-  __AUTH_CONST.__objc_const: 0x75c8
+  __AUTH_CONST.__objc_const: 0x75b8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x728

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1428
-  Symbols:   3468
+  Functions: 1427
+  Symbols:   3466
   CStrings:  463
 
Symbols:
+ -[TPSWiFiCallingController canEnableThumperCalling]
+ _objc_msgSend$canEnableThumperCalling
- -[TPSCloudCallingThumperController supportsThumperCalling]
- -[TPSWiFiCallingController supportsThumperCalling]
- _objc_msgSend$isRelayCallingEnabled
- _objc_msgSend$supportsThumperCalling
Functions:
~ -[TPSCloudCallingThumperProvisioningURLController shouldShowUpgradeToThumperButton] : 152 -> 136
- -[TPSCloudCallingThumperController supportsThumperCalling]
~ -[TPSWiFiCallingController isThumperCallingEnabled] : 96 -> 80
```
