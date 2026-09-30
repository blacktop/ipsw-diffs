## HRTFEnrollmentService

> `/System/Library/PrivateFrameworks/HRTFEnrollment.framework/XPCServices/HRTFEnrollmentService.xpc/HRTFEnrollmentService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-40.41.1.1.7
-  __TEXT.__text: 0x78f4
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_stubs: 0x12c0
+40.41.1.1.10
+  __TEXT.__text: 0x7a40
+  __TEXT.__auth_stubs: 0x590
+  __TEXT.__objc_stubs: 0x1300
   __TEXT.__objc_methlist: 0x72c
-  __TEXT.__const: 0x98
+  __TEXT.__const: 0xb8
   __TEXT.__objc_classname: 0x187
-  __TEXT.__objc_methname: 0x1768
+  __TEXT.__objc_methname: 0x179c
   __TEXT.__objc_methtype: 0x6fa
-  __TEXT.__cstring: 0x57e
-  __TEXT.__oslogstring: 0x59d
-  __TEXT.__gcc_except_tab: 0x214
+  __TEXT.__cstring: 0x5af
+  __TEXT.__oslogstring: 0x58e
+  __TEXT.__gcc_except_tab: 0x22c
   __TEXT.__unwind_info: 0x1f8
   __DATA_CONST.__const: 0x328
   __DATA_CONST.__cfstring: 0x600

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
-  __DATA_CONST.__auth_got: 0x2d0
+  __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x1780
-  __DATA.__objc_selrefs: 0x680
+  __DATA.__objc_selrefs: 0x690
   __DATA.__objc_ivar: 0xbc
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x2a8

   - /System/Library/PrivateFrameworks/HRTFEnrollment.framework/HRTFEnrollment
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/Visage.framework/Visage
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 141
-  Symbols:   150
-  CStrings:  505
+  Symbols:   151
+  CStrings:  510
 
Symbols:
+ _MGIsDeviceOfType
CStrings:
+ "%s returned with %@"
+ "True"
+ "getAssetForEnrollmentMode"
+ "getAssetForEnrollmentMode:error:"
+ "getAssetWithError"
+ "setEnrollmentMode:"
- "getAssetWithError returned with %@"
```
