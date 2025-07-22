## AccessoryFirmwareUpdate

> `/System/Library/PrivateFrameworks/AccessoryFirmwareUpdate.framework/AccessoryFirmwareUpdate`

```diff

-16.0.0.0.0
-  __TEXT.__text: 0x1992c
-  __TEXT.__auth_stubs: 0x9c0
+17.0.0.0.0
+  __TEXT.__text: 0x1a2a4
+  __TEXT.__auth_stubs: 0x9e0
   __TEXT.__objc_methlist: 0x1d4
   __TEXT.__const: 0xc60
-  __TEXT.__constg_swiftt: 0x79c
+  __TEXT.__constg_swiftt: 0x7b4
   __TEXT.__swift5_typeref: 0x4d7
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__swift5_reflstr: 0x66c
-  __TEXT.__swift5_fieldmd: 0x4d4
+  __TEXT.__swift5_reflstr: 0x69c
+  __TEXT.__swift5_fieldmd: 0x4e0
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_proto: 0x68
   __TEXT.__swift5_types: 0x38
-  __TEXT.__cstring: 0xd4d
-  __TEXT.__oslogstring: 0x12d3
+  __TEXT.__cstring: 0xd7d
+  __TEXT.__oslogstring: 0x1313
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_capture: 0x368
-  __TEXT.__unwind_info: 0x420
+  __TEXT.__unwind_info: 0x418
   __TEXT.__eh_frame: 0x180
   __TEXT.__objc_classname: 0x50
   __TEXT.__objc_methname: 0x2e8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0x4e0
+  __AUTH_CONST.__auth_got: 0x4f0
   __AUTH_CONST.__const: 0xa10
-  __AUTH_CONST.__objc_const: 0x930
+  __AUTH_CONST.__objc_const: 0x950
   __AUTH.__objc_data: 0x1a8
   __AUTH.__data: 0x208
   __DATA.__data: 0x3b0
   __DATA.__bss: 0xa80
-  __DATA.__common: 0x20
+  __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x1c0
-  __DATA_DIRTY.__data: 0x340
+  __DATA_DIRTY.__data: 0x360
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 4B81D1AC-053A-3EA3-B573-AE235AFD1C84
-  Functions: 475
-  Symbols:   379
-  CStrings:  206
+  UUID: 564F11AE-2A88-375B-98E7-6E8FD89C87D7
+  Functions: 477
+  Symbols:   378
+  CStrings:  207
 
Symbols:
+ _block_copy_helper.100
+ _block_copy_helper.107
+ _block_copy_helper.114
+ _block_copy_helper.121
+ _block_copy_helper.125
+ _block_copy_helper.129
+ _block_copy_helper.133
+ _block_copy_helper.137
+ _block_copy_helper.141
+ _block_copy_helper.148
+ _block_copy_helper.152
+ _block_copy_helper.156
+ _block_copy_helper.160
+ _block_copy_helper.56
+ _block_copy_helper.93
+ _block_descriptor.102
+ _block_descriptor.109
+ _block_descriptor.116
+ _block_descriptor.123
+ _block_descriptor.127
+ _block_descriptor.131
+ _block_descriptor.135
+ _block_descriptor.139
+ _block_descriptor.143
+ _block_descriptor.150
+ _block_descriptor.154
+ _block_descriptor.158
+ _block_descriptor.162
+ _block_descriptor.58
+ _block_descriptor.95
+ _block_destroy_helper.101
+ _block_destroy_helper.108
+ _block_destroy_helper.115
+ _block_destroy_helper.122
+ _block_destroy_helper.126
+ _block_destroy_helper.130
+ _block_destroy_helper.134
+ _block_destroy_helper.138
+ _block_destroy_helper.142
+ _block_destroy_helper.149
+ _block_destroy_helper.153
+ _block_destroy_helper.157
+ _block_destroy_helper.161
+ _block_destroy_helper.57
+ _block_destroy_helper.94
+ _objectdestroy.119Tm
+ _swift_getErrorValue
- _block_copy_helper.106
- _block_copy_helper.113
- _block_copy_helper.120
- _block_copy_helper.124
- _block_copy_helper.128
- _block_copy_helper.132
- _block_copy_helper.136
- _block_copy_helper.140
- _block_copy_helper.147
- _block_copy_helper.151
- _block_copy_helper.155
- _block_copy_helper.159
- _block_copy_helper.55
- _block_copy_helper.92
- _block_copy_helper.99
- _block_descriptor.101
- _block_descriptor.108
- _block_descriptor.115
- _block_descriptor.122
- _block_descriptor.126
- _block_descriptor.130
- _block_descriptor.134
- _block_descriptor.138
- _block_descriptor.142
- _block_descriptor.149
- _block_descriptor.153
- _block_descriptor.157
- _block_descriptor.161
- _block_descriptor.57
- _block_descriptor.94
- _block_destroy_helper.100
- _block_destroy_helper.107
- _block_destroy_helper.114
- _block_destroy_helper.121
- _block_destroy_helper.125
- _block_destroy_helper.129
- _block_destroy_helper.133
- _block_destroy_helper.137
- _block_destroy_helper.141
- _block_destroy_helper.148
- _block_destroy_helper.152
- _block_destroy_helper.156
- _block_destroy_helper.160
- _block_destroy_helper.56
- _block_destroy_helper.93
- _objectdestroy.118Tm
CStrings:
+ "#AccessoryUarpDeviceBridge -%s - No active firmware version found - exiting with completionReason: %s"
+ "#AccessoryUarpDeviceBridge -%s - activeFirmwareVersion: %s, stagedFirmwareVersion: %s with completionReason: %s"
+ "#AccessoryUarpDeviceBridge -%s - only activeFirmwareVersion: %s retrieved -- reporting to delegate with completionReason: %s"
+ "accessoryConnectionStateUpdateError"
- "#AccessoryUarpDeviceBridge -%s - No active firmware version found - exiting"
- "#AccessoryUarpDeviceBridge -%s - activeFirmwareVersion: %s, stagedFirmwareVersion: %s"
- "#AccessoryUarpDeviceBridge -%s - only activeFirmwareVersion: %s retrieved -- reporting to delegate"

```
