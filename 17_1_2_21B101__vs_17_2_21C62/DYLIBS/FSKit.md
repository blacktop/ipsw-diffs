## FSKit

> `/System/Library/PrivateFrameworks/FSKit.framework/FSKit`

```diff

-208.42.1.0.0
-  __TEXT.__text: 0x13820
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x1cb4
+208.60.13.0.2
+  __TEXT.__text: 0x1450c
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__objc_methlist: 0x1d04
   __TEXT.__const: 0x72
-  __TEXT.__gcc_except_tab: 0x47c
-  __TEXT.__cstring: 0x1109
-  __TEXT.__oslogstring: 0xdad
+  __TEXT.__gcc_except_tab: 0x4c4
+  __TEXT.__cstring: 0x11e9
+  __TEXT.__oslogstring: 0xed9
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x34
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x734
-  __TEXT.__objc_classname: 0x446
-  __TEXT.__objc_methname: 0x3eb8
-  __TEXT.__objc_methtype: 0x1488
-  __TEXT.__objc_stubs: 0x20e0
-  __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0x550
-  __DATA_CONST.__objc_classlist: 0x130
+  __TEXT.__unwind_info: 0x764
+  __TEXT.__objc_classname: 0x475
+  __TEXT.__objc_methname: 0x4020
+  __TEXT.__objc_methtype: 0x149f
+  __TEXT.__objc_stubs: 0x2240
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__const: 0x578
+  __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3008
-  __DATA_CONST.__objc_selrefs: 0x1130
+  __DATA_CONST.__objc_const: 0x3050
+  __DATA_CONST.__objc_selrefs: 0x1198
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__objc_const: 0x1120
+  __AUTH_CONST.__objc_const: 0x11f8
   __AUTH_CONST.__const: 0x198
-  __AUTH_CONST.__cfstring: 0xe40
+  __AUTH_CONST.__cfstring: 0xf20
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x460
-  __AUTH.__objc_data: 0xa18
+  __AUTH_CONST.__auth_got: 0x478
+  __AUTH.__objc_data: 0xab8
   __AUTH.__data: 0x28
   __DATA.__objc_protorefs: 0x70
-  __DATA.__objc_classrefs: 0x1a8
+  __DATA.__objc_classrefs: 0x1b8
   __DATA.__objc_superrefs: 0xd8
   __DATA.__objc_ivar: 0x1c4
   __DATA.__data: 0x8e8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 807
-  Symbols:   2678
-  CStrings:  1317
+  Functions: 819
+  Symbols:   2734
+  CStrings:  1351
 
Symbols:
+ +[FSKitDiskArbHelper DAMountUserFSVolume:deviceName:mountPoint:volumeName:mountOptions:]
+ +[FSKitDiskArbHelper DAMountUserFSVolume:deviceName:mountPoint:volumeName:mountOptions:].cold.1
+ +[stolenUSBLocalStorageClient newManager]
+ -[stolenUSBLocalStorageClient addDisk:]
+ -[stolenUSBLocalStorageClient loadVolumes:ofType:withError:]
+ -[stolenUSBLocalStorageClient loadVolumes:ofType:withError:].cold.1
+ GCC_except_table6
+ OBJC_IVAR_$_LiveFSClient.conn
+ _OBJC_CLASS_$_FSKitDiskArbHelper
+ _OBJC_CLASS_$_LiveFSClient
+ _OBJC_CLASS_$_LiveFSMountClient
+ _OBJC_CLASS_$_stolenUSBLocalStorageClient
+ _OBJC_METACLASS_$_FSKitDiskArbHelper
+ _OBJC_METACLASS_$_LiveFSClient
+ _OBJC_METACLASS_$_stolenUSBLocalStorageClient
+ __OBJC_$_CLASS_METHODS_FSKitDiskArbHelper
+ __OBJC_$_CLASS_METHODS_stolenUSBLocalStorageClient
+ __OBJC_$_INSTANCE_METHODS_stolenUSBLocalStorageClient
+ __OBJC_CLASS_RO_$_FSKitDiskArbHelper
+ __OBJC_CLASS_RO_$_stolenUSBLocalStorageClient
+ __OBJC_METACLASS_RO_$_FSKitDiskArbHelper
+ __OBJC_METACLASS_RO_$_stolenUSBLocalStorageClient
+ ___39-[stolenUSBLocalStorageClient addDisk:]_block_invoke
+ ___39-[stolenUSBLocalStorageClient addDisk:]_block_invoke_2
+ ___60-[stolenUSBLocalStorageClient loadVolumes:ofType:withError:]_block_invoke
+ ___60-[stolenUSBLocalStorageClient loadVolumes:ofType:withError:]_block_invoke_2
+ ___block_descriptor_48_e8_32r40r_e29_v24?0"NSError"8"NSArray"16lr32l8r40l8
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_enumerationMutation
+ _objc_msgSend$addDisk:fileSystemType:reply:
+ _objc_msgSend$addDisk:reply:
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$forgetVolume:withFlags:
+ _objc_msgSend$intValue
+ _objc_msgSend$integerValue
+ _objc_msgSend$loadVolumes:ofType:withError:
+ _objc_msgSend$mountVolume:displayName:provider:domainError:on:how:
+ _objc_msgSend$newClientForProvider:
+ _objc_msgSend$newConnectionForService:
+ _objc_msgSend$newManager
CStrings:
+ "%@ loadVolumes failed with %@"
+ "%@ mount failed with %@"
+ "%@ mounting with name %@, error %@, and how 0x%x."
+ "%@: got 2 different names from probe and userfs: p->%@  u->%@"
+ "%s:finish:%@:%@:%@"
+ "%s:start:%@:%@"
+ "-[stolenUSBLocalStorageClient loadVolumes:ofType:withError:]"
+ "DAMountUserFSVolume:deviceName:mountPoint:volumeName:mountOptions:"
+ "FSKitDiskArbHelper"
+ "Mounted %@ successfully."
+ "UUID"
+ "Untitled"
+ "addDisk:"
+ "addDisk:fileSystemType:reply:"
+ "addDisk:reply:"
+ "com.apple.filesystems.UserFS.FileProvider"
+ "countByEnumeratingWithState:objects:count:"
+ "errorForDomain"
+ "forgetVolume:withFlags:"
+ "how"
+ "i56@0:8@16@24@32@40@48"
+ "intValue"
+ "integerValue"
+ "loadVolumes:ofType:withError:"
+ "machp://com.apple.filesystems.localLiveFiles"
+ "mountVolume:displayName:provider:domainError:on:how:"
+ "newClientForProvider:"
+ "newConnectionForService:"
+ "newManager"
+ "stolenUSBLocalStorageClient"
+ "unload for volume %@ failed with %@"
+ "unsupported error code for domain: %ld"
+ "v24@?0@\"NSError\"8@\"NSArray\"16"

```
