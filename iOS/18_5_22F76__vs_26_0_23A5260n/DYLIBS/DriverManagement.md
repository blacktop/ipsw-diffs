## DriverManagement

> `/System/Library/PrivateFrameworks/DriverManagement.framework/DriverManagement`

```diff

-463.100.7.0.0
-  __TEXT.__text: 0x1c368
-  __TEXT.__auth_stubs: 0xda0
+487.0.1.0.0
+  __TEXT.__text: 0x1bbb0
+  __TEXT.__auth_stubs: 0xdf0
   __TEXT.__objc_methlist: 0x298
   __TEXT.__const: 0x194a
-  __TEXT.__swift5_typeref: 0x656
+  __TEXT.__swift5_typeref: 0x66e
   __TEXT.__constg_swiftt: 0x420
   __TEXT.__swift5_reflstr: 0x387
   __TEXT.__swift5_fieldmd: 0x504

   __TEXT.__swift5_types: 0x70
   __TEXT.__cstring: 0xc5b
   __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_capture: 0x168
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_capture: 0x148
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x7c8
-  __TEXT.__eh_frame: 0x8c8
+  __TEXT.__unwind_info: 0x770
+  __TEXT.__eh_frame: 0x848
   __TEXT.__objc_classname: 0x5d
   __TEXT.__objc_methname: 0x450
   __TEXT.__objc_methtype: 0xbb
   __TEXT.__objc_stubs: 0x320
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__const: 0x80
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x198
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x6d8
-  __AUTH_CONST.__const: 0xf10
+  __AUTH_CONST.__auth_got: 0x700
+  __AUTH_CONST.__const: 0xee8
   __AUTH_CONST.__objc_const: 0x6c0
   __DATA.__objc_ivar: 0x10
-  __DATA.__data: 0x280
-  __DATA.__bss: 0x1c50
+  __DATA.__data: 0x270
+  __DATA.__bss: 0x1a50
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x300
-  __DATA_DIRTY.__data: 0x640
-  __DATA_DIRTY.__bss: 0xe00
+  __DATA_DIRTY.__data: 0x660
+  __DATA_DIRTY.__bss: 0x1000
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 60E1689A-1892-3E3E-9C7C-BC61A88B988B
-  Functions: 745
-  Symbols:   553
+  UUID: 9796274D-B656-36AC-B3B9-6529F68171C7
+  Functions: 738
+  Symbols:   543
   CStrings:  165
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_DriverManagement
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_DriverManagement
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_DriverManagement
+ _block_copy_helper.20
+ _block_copy_helper.29
+ _block_copy_helper.38
+ _block_copy_helper.50
+ _block_descriptor.22
+ _block_descriptor.31
+ _block_descriptor.40
+ _block_descriptor.52
+ _block_destroy_helper.21
+ _block_destroy_helper.30
+ _block_destroy_helper.39
+ _block_destroy_helper.51
+ _swift_coroFrameAlloc
+ _symbolic SS______t 16DriverManagement13ApprovalStateO
+ _symbolic Si6offset______7elementtSg 16DriverManagement26ApprovalSettingsStateEntryV
+ _symbolic _____y___________pGIegg_ s6ResultOsRi_zRi0_zrlE 16DriverManagement21ApprovalSettingsStateV s5ErrorP
+ _symbolic _____yyt______pG s6ResultOsRi_zRi0_zrlE s5ErrorP
+ _symbolic y_____yyt______pGc s6ResultOsRi_zRi0_zrlE s5ErrorP
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_DriverManagement
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_DriverManagement
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_DriverManagement
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_DriverManagement
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_DriverManagement
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_DriverManagement
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_DriverManagement
- _block_copy_helper.22
- _block_copy_helper.40
- _block_copy_helper.52
- _block_descriptor.24
- _block_descriptor.42
- _block_descriptor.54
- _block_destroy_helper.23
- _block_destroy_helper.41
- _block_destroy_helper.53
- _swift_bridgeObjectRetain_n
- _symbolic SaySsG
- _symbolic _____ SS5IndexV
- _symbolic _____y___________pGIegg_ s6ResultOsRi_zrlE 16DriverManagement21ApprovalSettingsStateV s5ErrorP
- _symbolic _____yyt______pG s6ResultOsRi_zrlE s5ErrorP
- _symbolic y_____yyt______pGc s6ResultOsRi_zrlE s5ErrorP

```
