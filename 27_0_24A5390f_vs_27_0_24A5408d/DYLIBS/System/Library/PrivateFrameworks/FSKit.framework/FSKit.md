## FSKit

> `/System/Library/PrivateFrameworks/FSKit.framework/FSKit`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__constg_swiftt`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-974.0.11.0.0
-  __TEXT.__text: 0x536b4
-  __TEXT.__objc_methlist: 0x6288
+974.0.13.0.2
+  __TEXT.__text: 0x53b8c
+  __TEXT.__objc_methlist: 0x6348
   __TEXT.__const: 0x498
   __TEXT.__gcc_except_tab: 0xe5c
   __TEXT.__oslogstring: 0x3f76

   __TEXT.__constg_swiftt: 0x210
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1828
+  __TEXT.__unwind_info: 0x1848
   __TEXT.__eh_frame: 0x478
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x18f0
   __DATA_CONST.__objc_classlist: 0x398
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x1b0
+  __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c08
+  __DATA_CONST.__objc_selrefs: 0x2c18
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x488
   __DATA_CONST.__got: 0x488
   __AUTH_CONST.__const: 0x6f0
   __AUTH_CONST.__cfstring: 0x2ae0
-  __AUTH_CONST.__objc_const: 0xb258
+  __AUTH_CONST.__objc_const: 0xb2b8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__objc_arrayobj: 0x288

   __AUTH.__objc_data: 0x1bd8
   __AUTH.__data: 0x58
   __DATA.__objc_ivar: 0x640
-  __DATA.__data: 0x14d8
+  __DATA.__data: 0x1538
   __DATA.__bss: 0x2d0
   __DATA_DIRTY.__objc_data: 0x958
   __DATA_DIRTY.__data: 0x80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2695
-  Symbols:   5122
+  Functions: 2705
+  Symbols:   5139
   CStrings:  1099
 
Symbols:
+ -[FSBlockDeviceResource hash]
+ -[FSFileName isEqual:]
+ -[FSGenericURLResource hash]
+ -[FSModuleInstance hash]
+ -[FSPathURLResource hash]
+ -[FSServerURLResource hash]
+ -[FSTaskOption hash]
+ -[FSVolumeDescription isEqual:]
+ -[FSVolumeSupportedCapabilities hash]
+ GCC_except_table62
+ GCC_except_table72
+ GCC_except_table82
+ __OBJC_$_PROP_LIST_FSVolumeCommonOperations
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FSVolumeCommonOperations
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FSVolumeCommonOperations
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FSVolumeCommonOperations
+ __OBJC_LABEL_PROTOCOL_$_FSVolumeCommonOperations
+ __OBJC_PROTOCOL_$_FSVolumeCommonOperations
+ _objc_msgSend$activateVolumeWithOptions:replyHandler:
+ _objc_msgSend$deactivateVolumeWithOptions:replyHandler:
+ _objc_msgSend$volumeName
+ _objc_msgSend$volumeState
- GCC_except_table23
- GCC_except_table61
- GCC_except_table70
- GCC_except_table81
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FSVolumeHandler
Functions:
+ -[FSFileName isEqual:]
~ -[FSModuleConnector deactivateVolume:numericOptions:replyHandler:] : 488 -> 556
+ -[FSModuleInstance hash]
+ -[FSServerURLResource hash]
+ -[FSTaskOption hash]
+ -[FSVolumeDescription isEqual:]
+ -[FSVolumeSupportedCapabilities hash]
+ -[FSBlockDeviceResource hash]
+ -[FSGenericURLResource hash]
+ -[FSPathURLResource hash]
~ -[FSClient handleInvalidated] : 256 -> 264
~ -[FSVolumeConnector otherAttributeOf:named:requestID:replyHandler:] : 4064 -> 4076
+ sub_2618f5d38
```
