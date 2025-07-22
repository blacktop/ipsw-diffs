## transparencyd

> `/usr/libexec/transparencyd`

```diff

-1547.0.24.0.0
-  __TEXT.__text: 0x256a78
+1547.0.28.0.0
+  __TEXT.__text: 0x256b94
   __TEXT.__auth_stubs: 0x3090
   __TEXT.__objc_stubs: 0x1c1e0
   __TEXT.__objc_methlist: 0x15060
-  __TEXT.__cstring: 0x129ec
+  __TEXT.__cstring: 0x129f4
   __TEXT.__objc_classname: 0x2c70
   __TEXT.__objc_methname: 0x2276b
   __TEXT.__objc_methtype: 0x7500
   __TEXT.__const: 0xaa04
-  __TEXT.__gcc_except_tab: 0x52cc
-  __TEXT.__oslogstring: 0x11485
+  __TEXT.__gcc_except_tab: 0x5310
+  __TEXT.__oslogstring: 0x1150c
   __TEXT.__swift5_typeref: 0x243a
   __TEXT.__swift5_reflstr: 0x1795
   __TEXT.__swift5_assocty: 0x4b0

   __DATA_CONST.__auth_got: 0x1858
   __DATA_CONST.__got: 0xee0
   __DATA_CONST.__auth_ptr: 0x5d8
-  __DATA_CONST.__const: 0x16198
+  __DATA_CONST.__const: 0x16158
   __DATA_CONST.__cfstring: 0xe160
   __DATA_CONST.__objc_classlist: 0xcb8
   __DATA_CONST.__objc_catlist: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A0877957-7092-3A88-973F-F5610EB27E9D
+  UUID: 41DF4D77-2156-3FF1-9C5F-C9E6499AA9CA
   Functions: 15835
-  Symbols:   1414
-  CStrings:  13462
+  Symbols:   1406
+  CStrings:  13463
 
Symbols:
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftMetal
- __swift_FORCE_LOAD_$_swiftQuartzCore
- __swift_FORCE_LOAD_$_swiftsimd
Functions:
~ sub_100054da8 -> sub_100054b78 : 660 -> 704
~ sub_10005508c -> sub_100054e88 : 1028 -> 1116
~ sub_1000554d4 -> sub_100055328 : 612 -> 648
~ sub_1001d783c -> sub_1001d76b4 : 248 -> 172
~ sub_1001d7f48 -> sub_1001d7d74 : 3508 -> 3700
CStrings:
+ "Can't get AltDSID: %{public}@"
+ "Can't get DSID: %{public}@"
+ "Getting signature request: %d: %{public}@"
+ "KTErrorDomainCheckIDS"
+ "New keys inserted. Waiting while we try to make signatures: %{public}@"
+ "Returning existing signatures: %d. insertedKeys [0]: %{public}@"
+ "Returning existing signatures: %d. insertedKeys [1]: %{public}@"
+ "TransparencyAccount level not HSA2: %d: %{public}@"
+ "TransparencyAccount no account: %{public}@"
- "Can't get AltDSID"
- "Can't get DSID"
- "Getting signature request: %d"
- "New keys inserted. Waiting while we try to make signatures."
- "Returning existing signatures: %d. insertedKeys [0]"
- "Returning existing signatures: %d. insertedKeys [1]"
- "TransparencyAccount no account"
- "checkIDSError"

```
