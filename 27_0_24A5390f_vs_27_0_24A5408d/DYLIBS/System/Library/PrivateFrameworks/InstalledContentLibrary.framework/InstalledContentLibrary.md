## InstalledContentLibrary

> `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-1673.0.0.0.0
-  __TEXT.__text: 0xce76c
-  __TEXT.__objc_methlist: 0x5b94
+1674.2.1.0.0
+  __TEXT.__text: 0xcee78
+  __TEXT.__objc_methlist: 0x5be4
   __TEXT.__const: 0xdb30
   __TEXT.__cstring: 0x183ee
-  __TEXT.__gcc_except_tab: 0xde0
+  __TEXT.__gcc_except_tab: 0xde8
   __TEXT.__dlopen_cstrs: 0x111
   __TEXT.__oslogstring: 0x8c1
   __TEXT.__swift5_typeref: 0x30
-  __TEXT.__unwind_info: 0x19c8
+  __TEXT.__unwind_info: 0x19f0
   __TEXT.__eh_frame: 0x398
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x30a8
+  __DATA_CONST.__objc_selrefs: 0x30c0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0xb10
   __DATA_CONST.__got: 0x4f0
   __AUTH_CONST.__const: 0x4d88
-  __AUTH_CONST.__cfstring: 0xd460
-  __AUTH_CONST.__objc_const: 0xa740
+  __AUTH_CONST.__cfstring: 0xd4a0
+  __AUTH_CONST.__objc_const: 0xa7d0
   __AUTH_CONST.__objc_dictobj: 0x1248
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x180
-  __AUTH_CONST.__auth_got: 0xc08
+  __AUTH_CONST.__auth_got: 0xc10
   __AUTH.__objc_data: 0x1180
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x5c0
+  __DATA.__objc_ivar: 0x5cc
   __DATA.__data: 0xf38
   __DATA.__bss: 0x2d0
   __DATA.__common: 0xaa4

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 2402
-  Symbols:   5034
-  CStrings:  2260
+  Functions: 2412
+  Symbols:   5051
+  CStrings:  2262
 
Symbols:
+ -[ICLPlaceholderRecord installBuildVersion]
+ -[ICLPlaceholderRecord originalInstallDate]
+ -[ICLPlaceholderRecord setInstallBuildVersion:]
+ -[ICLPlaceholderRecord setOriginalInstallDate:]
+ -[MIExecutableBundle getHasExecutableSliceForArchSupportingPAC:withError:]
+ -[MIMachOImageSlice initWithCPUType:cpuSubtype:platform:sdkVersion:minOSVersion:supportsPAC:]
+ -[MIMachOImageSlice setSupportsPAC:]
+ -[MIMachOImageSlice supportsPAC]
+ GCC_except_table22
+ GCC_except_table76
+ GCC_except_table95
+ _MIMachOHasRunnableSliceSupportingPAC
+ _OBJC_IVAR_$_ICLPlaceholderRecord._installBuildVersion
+ _OBJC_IVAR_$_ICLPlaceholderRecord._originalInstallDate
+ _OBJC_IVAR_$_MIMachOImageSlice._supportsPAC
+ __CopyRunnableArchNames
+ __CopyRunnablePlatforms
+ ___block_descriptor_40_e8_32s_e23_B32?0i8i12I16I20I24B28ls32l8
+ ___block_descriptor_57_e8_32bs40r_e14_v20?0I8I12I16lr40l8s32l8
+ _macho_supports_pointer_authentication
+ _objc_msgSend$initWithCPUType:cpuSubtype:platform:sdkVersion:minOSVersion:supportsPAC:
+ _objc_msgSend$setSupportsPAC:
+ _objc_msgSend$supportsPAC
- -[MIMachOImageSlice initWithCPUType:cpuSubtype:platform:sdkVersion:minOSVersion:]
- GCC_except_table75
- GCC_except_table94
- ___block_descriptor_40_e8_32s_e20_B28?0i8i12I16I20I24ls32l8
- ___block_descriptor_56_e8_32bs40r_e14_v20?0I8I12I16lr40l8s32l8
- _objc_msgSend$initWithCPUType:cpuSubtype:platform:sdkVersion:minOSVersion:
CStrings:
+ "#)"
+ "B32@?0i8i12I16I20I24B28"
+ "InstallBuildVersion"
+ "OriginalInstallDate"
+ "The executable at \"%s\" does not contain code for any platform and CPU architecture combination that is runnable on this device. The executable has code for these platforms and architectures: %@. This device can run code for these platforms: %@"
- "#'"
- "B28@?0i8i12I16I20I24"
- "The executable at \"%s\" does not contain code for any platform and CPU architecture combination that is runnable on this device. The executable has code for these platforms and architectures: %@. This device can run code for these architectures: %@. This device can run code for these platforms: %@"
```
