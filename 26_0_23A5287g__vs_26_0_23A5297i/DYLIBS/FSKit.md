## FSKit

> `/System/Library/PrivateFrameworks/FSKit.framework/FSKit`

```diff

-737.0.14.0.1
-  __TEXT.__text: 0x403f0
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x49c4
+737.0.17.0.2
+  __TEXT.__text: 0x40958
+  __TEXT.__auth_stubs: 0xd30
+  __TEXT.__objc_methlist: 0x4a24
   __TEXT.__const: 0x390
-  __TEXT.__gcc_except_tab: 0xdd8
+  __TEXT.__gcc_except_tab: 0xde0
   __TEXT.__oslogstring: 0x3092
-  __TEXT.__cstring: 0x42df
+  __TEXT.__cstring: 0x42ef
   __TEXT.__swift5_typeref: 0x1d1
   __TEXT.__swift5_capture: 0x58
   __TEXT.__swift5_reflstr: 0x16

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x12f0
+  __TEXT.__unwind_info: 0x1320
   __TEXT.__eh_frame: 0x160
   __TEXT.__objc_classname: 0x8e7
-  __TEXT.__objc_methname: 0x99ba
+  __TEXT.__objc_methname: 0x9a6c
   __TEXT.__objc_methtype: 0x32db
-  __TEXT.__objc_stubs: 0x56c0
+  __TEXT.__objc_stubs: 0x5720
   __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__const: 0x1360
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2478
+  __DATA_CONST.__objc_selrefs: 0x2490
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH_CONST.__auth_got: 0x6a8
   __AUTH_CONST.__const: 0x4e8
   __AUTH_CONST.__cfstring: 0x2300
-  __AUTH_CONST.__objc_const: 0x7e70
+  __AUTH_CONST.__objc_const: 0x7e90
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1040
   __AUTH.__data: 0x80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9EC86963-8B12-310F-9619-5FDCC5D0EC4D
-  Functions: 1993
-  Symbols:   6339
-  CStrings:  3324
+  UUID: 114AC186-A5EB-3F7F-876F-C4AC79259104
+  Functions: 2001
+  Symbols:   6360
+  CStrings:  3327
 
Symbols:
+ +[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]
+ +[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:].cold.1
+ -[FSClient(Private) activateVolume:shortName:options:auditToken:replyHandler:]
+ -[FSClient(Private) deactivateVolume:shortName:numericOptions:auditToken:replyHandler:]
+ -[FSClient(Private) loadResource:shortName:options:auditToken:replyHandler:]
+ -[FSClient(Private) unloadResource:shortName:options:auditToken:replyHandler:]
+ GCC_except_table106
+ GCC_except_table109
+ GCC_except_table70
+ GCC_except_table88
+ ___76-[FSClient(Private) loadResource:shortName:options:auditToken:replyHandler:]_block_invoke
+ ___78-[FSClient(Private) activateVolume:shortName:options:auditToken:replyHandler:]_block_invoke
+ ___78-[FSClient(Private) unloadResource:shortName:options:auditToken:replyHandler:]_block_invoke
+ ___87-[FSClient(Private) deactivateVolume:shortName:numericOptions:auditToken:replyHandler:]_block_invoke
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.24
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.24.cold.1
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.24.cold.2
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.24.cold.3
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.29
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.29.cold.1
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.29.cold.2
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.30
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.30.cold.1
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.30.cold.2
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.32
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.32.cold.1
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.cold.1
+ ___block_descriptor_148_e8_32s40s48s56s64s72s80s88s96r104r_e36_v32?0"FSVolumeDescription"8Q16^B24ls32l8s40l8s48l8r96l8s56l8s64l8s72l8s80l8s88l8r104l8
+ ___block_literal_global.309
+ _objc_msgSend$DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:
+ _objc_msgSend$activateVolume:shortName:options:auditToken:replyHandler:
+ _objc_msgSend$deactivateVolume:shortName:numericOptions:auditToken:replyHandler:
+ _objc_msgSend$loadResource:shortName:options:auditToken:replyHandler:
+ _objc_msgSend$unloadResource:shortName:options:auditToken:replyHandler:
+ _objc_release_x10
- +[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]
- +[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:].cold.1
- GCC_except_table101
- GCC_except_table86
- GCC_except_table98
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.24
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.24.cold.1
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.24.cold.2
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.24.cold.3
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.29
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.29.cold.1
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.29.cold.2
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.30
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.30.cold.1
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.30.cold.2
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.32
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.32.cold.1
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.cold.1
- ___block_descriptor_116_e8_32s40s48s56s64s72s80s88s96r104r_e36_v32?0"FSVolumeDescription"8Q16^B24ls32l8s40l8s48l8r96l8s56l8s64l8s72l8s80l8s88l8r104l8
- ___block_literal_global.304
- _objc_msgSend$DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:
- _objc_msgSend$mountVolume:fileSystem:displayName:provider:domainError:on:how:options:
CStrings:
+ "+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]"
+ "+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke"
+ "DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:"
+ "activateVolume:shortName:options:auditToken:replyHandler:"
+ "deactivateVolume:shortName:numericOptions:auditToken:replyHandler:"
+ "loadResource:shortName:options:auditToken:replyHandler:"
+ "unloadResource:shortName:options:auditToken:replyHandler:"
- "+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]"
- "+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke"
- "DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:"
- "mountVolume:fileSystem:displayName:provider:domainError:on:how:options:"

```
