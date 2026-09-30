## MobileIdentityServiceUI

> `/System/Library/PrivateFrameworks/MobileIdentityServiceUI.framework/MobileIdentityServiceUI`

```diff

-463.0.0.0.0
-  __TEXT.__text: 0x7754
-  __TEXT.__auth_stubs: 0x710
+463.0.4.0.0
+  __TEXT.__text: 0x76a0
+  __TEXT.__auth_stubs: 0x700
   __TEXT.__objc_methlist: 0xc8
   __TEXT.__const: 0x2ea
   __TEXT.__swift5_typeref: 0x129

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x8
-  __TEXT.__oslogstring: 0x2a1
+  __TEXT.__oslogstring: 0x246
   __TEXT.__cstring: 0x743
   __TEXT.__swift5_capture: 0x144
   __TEXT.__swift_as_entry: 0x30

   __TEXT.__eh_frame: 0x5a8
   __TEXT.__objc_methname: 0x265
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0xb0
+  __DATA_CONST.__const: 0x90
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xd8
-  __AUTH_CONST.__auth_got: 0x388
+  __AUTH_CONST.__auth_got: 0x380
   __AUTH_CONST.__const: 0x458
   __AUTH_CONST.__objc_const: 0xd0
   __AUTH.__objc_data: 0x70

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 60B14E69-2F0B-34EF-8BC3-313E0B761A28
+  UUID: 2FBC16AA-41CC-3652-845F-0BFFE1082100
   Functions: 160
-  Symbols:   114
+  Symbols:   109
   CStrings:  79
 
Symbols:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _objc_release_x28
Functions:
~ sub_265bf7858 -> sub_26699c728 : 960 -> 940
~ sub_265bf7f30 -> sub_26699cdec : 1004 -> 984
~ sub_265bf9ac0 -> sub_26699e968 : 656 -> 636
~ sub_265bfa814 -> sub_26699f6a8 : 740 -> 700
~ sub_265bfaaf8 -> sub_26699f964 : 1024 -> 1004
~ sub_265bfb974 -> sub_2669a07cc : 656 -> 636
~ sub_265bfc85c -> sub_2669a16a0 : 2044 -> 2004
CStrings:
+ "Deleted app %{public}s"
+ "Did not delete app %{public}s. Uninstall disposition is %{public}lu"
+ "Error setting removability of %{public}s with error '%{public}s'"
+ "Error uninstalling %{public}s with error '%{public}s'"
+ "Failed to query launch warning database for %{public}s, error: '%{public}s'."
+ "Failed to request update for %{public}s, error: '%{public}s'."
+ "Failed to retrieve LSApplicationRecord for %{public}s with error '%{public}s'"
+ "Fetched %s update metadata for %{public}s"
- "Deleted app %{private,mask.hash}s"
- "Did not delete app %{private,mask.hash}s. Uninstall disposition is %{public}lu"
- "Error setting removability of %{private,mask.hash}s with error '%{public}s'"
- "Error uninstalling %{private,mask.hash}s with error '%{public}s'"
- "Failed to query launch warning database for %{private,mask.hash}s, error: '%{public}s'."
- "Failed to request update for %{private,mask.hash}s, error: '%{public}s'."
- "Failed to retrieve LSApplicationRecord for %{private,mask.hash}s with error '%{public}s'"
- "Fetched %s update metadata for %{private,mask.hash}s"

```
