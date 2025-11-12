## StorageKit

> `/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit`

```diff

-1024.40.8.0.0
-  __TEXT.__text: 0x2bb68
+1024.60.3.0.0
+  __TEXT.__text: 0x2bf54
   __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x34fc
+  __TEXT.__objc_methlist: 0x352c
   __TEXT.__const: 0x10a
   __TEXT.__oslogstring: 0x142a
-  __TEXT.__cstring: 0x301c
+  __TEXT.__cstring: 0x309c
   __TEXT.__gcc_except_tab: 0x13b8
   __TEXT.__swift5_typeref: 0x56
   __TEXT.__swift5_fieldmd: 0x30
   __TEXT.__constg_swiftt: 0x74
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xc28
+  __TEXT.__unwind_info: 0xc38
   __TEXT.__objc_classname: 0x697
-  __TEXT.__objc_methname: 0x6bf5
-  __TEXT.__objc_methtype: 0xef9
-  __TEXT.__objc_stubs: 0x6280
+  __TEXT.__objc_methname: 0x6ca2
+  __TEXT.__objc_methtype: 0xfa1
+  __TEXT.__objc_stubs: 0x62c0
   __DATA_CONST.__got: 0x328
   __DATA_CONST.__const: 0x908
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d98
+  __DATA_CONST.__objc_selrefs: 0x1db0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x5b8
   __AUTH_CONST.__const: 0x588
   __AUTH_CONST.__cfstring: 0x35a0
-  __AUTH_CONST.__objc_const: 0x7b00
+  __AUTH_CONST.__objc_const: 0x7b10
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x60

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 607D28D6-47A4-3978-AAD1-BBD160763678
-  Functions: 1190
-  Symbols:   4548
-  CStrings:  2731
+  UUID: 846ED2B7-E0BA-37BD-B399-904135A3F34E
+  Functions: 1194
+  Symbols:   4558
+  CStrings:  2740
 
Symbols:
+ -[SKAPFSDisk removeVolumeWithProgress:completionBlock:]
+ -[SKHelperClient deleteAPFSVolume:progress:completionBlock:]
+ ___60-[SKHelperClient deleteAPFSVolume:progress:completionBlock:]_block_invoke
+ ___60-[SKHelperClient deleteAPFSVolume:progress:completionBlock:]_block_invoke_2
+ _objc_msgSend$deleteAPFSVolume:optionsDictionary:handlingProgressForOperationUUID:withCompletionUUID:
+ _objc_msgSend$deleteAPFSVolume:progress:completionBlock:
CStrings:
+ "-[SKHelperClient deleteAPFSVolume:progress:completionBlock:]"
+ "-[SKHelperClient deleteAPFSVolume:progress:completionBlock:]_block_invoke_2"
+ "deleteAPFSVolume:optionsDictionary:handlingProgressForOperationUUID:withCompletionUUID:"
+ "deleteAPFSVolume:progress:completionBlock:"
+ "removeVolumeWithProgress:completionBlock:"
+ "v32@0:8@?16@?24"
+ "v40@0:8@\"SKAPFSDisk\"16@?<v@?f@\"NSString\">24@?<v@?B@\"NSError\">32"
+ "v48@0:8@\"NSDictionary\"16@\"NSDictionary\"24@\"NSString\"32@\"NSString\"40"
+ "v48@0:8@16@24@32@40"

```
