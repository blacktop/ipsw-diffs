## libtailspin.dylib

> `/usr/lib/libtailspin.dylib`

```diff

-234.0.0.0.0
-  __TEXT.__text: 0x2713c
-  __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_methlist: 0x1dc
+237.0.0.0.0
+  __TEXT.__text: 0x27824
+  __TEXT.__auth_stubs: 0x1090
+  __TEXT.__objc_methlist: 0x1f4
   __TEXT.__const: 0x189
-  __TEXT.__cstring: 0x2f22
-  __TEXT.__oslogstring: 0x2a59
-  __TEXT.__gcc_except_tab: 0x1ad8
+  __TEXT.__cstring: 0x2f0f
+  __TEXT.__oslogstring: 0x2bda
+  __TEXT.__gcc_except_tab: 0x1b60
   __TEXT.__ustring: 0x6
   __TEXT.__dlopen_cstrs: 0x48
-  __TEXT.__unwind_info: 0x9e8
-  __TEXT.__objc_classname: 0x18
-  __TEXT.__objc_methname: 0x1155
+  __TEXT.__unwind_info: 0xa10
+  __TEXT.__objc_classname: 0x19
+  __TEXT.__objc_methname: 0x1191
   __TEXT.__objc_methtype: 0xfb
   __TEXT.__objc_stubs: 0x1200
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0xa40
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__const: 0xa48
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x518
+  __DATA_CONST.__objc_selrefs: 0x528
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x850
+  __AUTH_CONST.__auth_got: 0x860
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x1ba0
-  __AUTH_CONST.__objc_const: 0x2d0
+  __AUTH_CONST.__cfstring: 0x1be0
+  __AUTH_CONST.__objc_const: 0x300
   __AUTH.__objc_data: 0x28
-  __DATA.__objc_ivar: 0x30
+  __DATA.__objc_ivar: 0x34
   __DATA.__data: 0x10
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x6a8

   - /System/Library/PrivateFrameworks/kperfdata.framework/kperfdata
   - /System/Library/PrivateFrameworks/ktrace.framework/ktrace
   - /usr/lib/libIOReport.dylib
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 931964AB-EBE1-3AD6-A0FB-3AA6F3660E54
-  Functions: 649
-  Symbols:   538
-  CStrings:  1025
+  UUID: 7DBF74CB-6A0D-320A-AAFD-3C01F136FF1E
+  Functions: 661
+  Symbols:   542
+  CStrings:  1037
 
Symbols:
+ _MGCopyAnswer
+ _MGGetStringAnswer
+ _MobileGestalt_copy_hwModelDescriptionForPowerPerf_obj
+ _MobileGestalt_copy_productTypeDescForPowerPerf_obj
+ _MobileGestalt_get_current_device
+ _TSPMetadata_SubProductTypeKey
+ __os_log_default
- _dlclose
- _dlopen
- _pthread_threadid_np
CStrings:
+ "FAILED due to reason: %{public}@.\nFile path: %{public}@"
+ "Failed to get current device from MobileGestalt: %{darwin.errno}d"
+ "Failed to get hwModel from MobileGestalt: %{darwin.errno}d"
+ "Failed to get productType from MobileGestalt: %{darwin.errno}d"
+ "Got an empty hwModel string from MobileGestalt"
+ "Got an empty productType string from MobileGestalt"
+ "HWModelStr"
+ "Looking up kMGQHWModelStr"
+ "Looking up kMGQProductType"
+ "SubProductType"
+ "Succeeded.\nFile path: %{public}@"
+ "T@\"NSString\",&,N,V_filePath"
+ "_filePath"
+ "filePath"
+ "setFilePath:"
- "/usr/lib/libMobileGestalt.dylib"
- "11"
- "FAILED due to reason: %{public}@"
- "MGCopyAnswer"

```
