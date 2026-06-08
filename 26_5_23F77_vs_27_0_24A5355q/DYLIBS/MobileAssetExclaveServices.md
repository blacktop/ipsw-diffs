## MobileAssetExclaveServices

> `/System/Library/PrivateFrameworks/MobileAssetExclaveServices.framework/MobileAssetExclaveServices`

```diff

-1837.122.1.0.0
-  __TEXT.__text: 0xad2c
-  __TEXT.__auth_stubs: 0x950
+2215.0.0.502.1
+  __TEXT.__text: 0xab68
   __TEXT.__objc_methlist: 0x1f4
-  __TEXT.__const: 0x5f8
+  __TEXT.__const: 0x5e8
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__cstring: 0x33e
   __TEXT.__oslogstring: 0x63e

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x34
-  __TEXT.__unwind_info: 0x2c8
-  __TEXT.__eh_frame: 0x778
-  __TEXT.__objc_classname: 0x198
-  __TEXT.__objc_methname: 0x2df
-  __TEXT.__objc_methtype: 0x248
-  __TEXT.__objc_stubs: 0xa0
-  __DATA_CONST.__got: 0x128
+  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__eh_frame: 0x6f0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x110
   __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__got: 0x120
   __AUTH_CONST.__const: 0x308
   __AUTH_CONST.__objc_const: 0x4a8
-  __AUTH.__data: 0x1e8
-  __DATA.__data: 0x200
-  __DATA.__bss: 0x680
+  __AUTH_CONST.__auth_got: 0x528
+  __AUTH.__data: 0x140
+  __DATA.__data: 0x170
+  __DATA.__bss: 0x600
   __DATA_DIRTY.__objc_data: 0x178
-  __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0x8
+  __DATA_DIRTY.__data: 0x1a8
+  __DATA_DIRTY.__bss: 0x90
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7C09395F-3225-3491-8786-1BC995F05ADB
-  Functions: 165
-  Symbols:   207
-  CStrings:  120
+  UUID: 688F4897-D176-35C4-826B-D0C458049456
+  Functions: 160
+  Symbols:   218
+  CStrings:  45
 
Symbols:
+ ___swift_destroy_boxed_opaque_existential_0
+ _objc_claimAutoreleasedReturnValue
+ _objc_release
+ _objc_retainAutoreleaseReturnValue
+ _swift_bridgeObjectRetain_n
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x27
- ___swift_destroy_boxed_opaque_existential_0Tm
- ___swift_project_boxed_opaque_existential_1
- _objc_release_x26
- _objc_retain_x19
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSDictionary\"24@0:8^@16"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B36@0:8I16@\"NSString\"20^@28"
- "B36@0:8I16@20^@28"
- "B40@0:8@\"NSArray\"16@\"NSArray\"24^@32"
- "B40@0:8@16@24^@32"
- "B60@0:8I16@\"NSString\"20@\"NSData\"28@\"NSData\"36@\"NSData\"44^@52"
- "B60@0:8I16@20@28@36@44^@52"
- "B72@0:8I16@\"NSString\"20I28@\"NSData\"32@\"NSData\"40@\"NSData\"48^B56^@64"
- "B72@0:8I16@20I28@32@40@48^B56^@64"
- "MAExclaveManifestStorageServiceBaseProtocol"
- "MAExclaveManifestStorageServiceProtocol2"
- "NSObject"
- "Q16@0:8"
- "SecureMobileAssetExclaveManager"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC24SecureMobileAssetExclave31MAExclaveManifestStorageService"
- "_TtC24SecureMobileAssetExclave33MobileAssetExclaveServicesManager"
- "_TtCC24SecureMobileAssetExclave31MAExclaveManifestStorageService6Server"
- "_TtCC24SecureMobileAssetExclave31MAExclaveManifestStorageService7Service"
- "activateCommittedManifestForFSTag:specifier:error:"
- "autorelease"
- "checkManifestForFSTag:specifier:state:manifest:infoPlist:catalog:isValid:error:"
- "class"
- "commitStagedManifestForFSTags:specifiers:error:"
- "conformsToProtocol:"
- "connection"
- "dealloc"
- "debugDescription"
- "description"
- "hash"
- "init"
- "initWithConclave:"
- "invalidateManifestForFSTag:specifier:error:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lock"
- "log"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "proposeNonce:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sharedInstance"
- "stageManifestForFSTag:specifier:manifest:infoPlist:catalog:error:"
- "superclass"
- "tbClient"
- "unlock"
- "unsignedIntValue"
- "v16@0:8"
- "zone"

```
