## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`

```diff

-2702.5.0.0.0
-  __TEXT.__text: 0x56a6c
-  __TEXT.__objc_methlist: 0x4a1c
-  __TEXT.__const: 0xaf8
-  __TEXT.__cstring: 0xaae3
+2702.8.0.0.0
+  __TEXT.__text: 0x585c0
+  __TEXT.__objc_methlist: 0x4ad4
+  __TEXT.__const: 0xbf8
+  __TEXT.__cstring: 0xacd3
   __TEXT.__gcc_except_tab: 0x1360
   __TEXT.__constg_swiftt: 0x3b8
   __TEXT.__swift5_typeref: 0x25a

   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0x1af8
+  __TEXT.__unwind_info: 0x1b30
   __TEXT.__eh_frame: 0x4d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xed8
+  __DATA_CONST.__const: 0xf78
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2108
+  __DATA_CONST.__objc_selrefs: 0x2180
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x550
   __AUTH_CONST.__const: 0x6f0
-  __AUTH_CONST.__cfstring: 0x3960
-  __AUTH_CONST.__objc_const: 0x8698
+  __AUTH_CONST.__cfstring: 0x3a40
+  __AUTH_CONST.__objc_const: 0x8768
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__auth_got: 0xc30
   __AUTH.__objc_data: 0x138
   __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x774
+  __DATA.__objc_ivar: 0x784
   __DATA.__data: 0xc68
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x12e8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2396
-  Symbols:   3476
-  CStrings:  1588
+  Functions: 2422
+  Symbols:   3504
+  CStrings:  1604
 
Symbols:
+ +[DADevice appServicesFromArchive:]
+ +[DADevice normalizedPersistentServices:]
+ +[DADevice persistentServiceInfos:deviceID:perApp:authorizations:]
+ -[DADevice accessoryServicesMapForBundleID:]
+ -[DADevice appServicesInternalMap]
+ -[DADevice appServicesMap]
+ -[DADevice encodeAppServices]
+ -[DADevice loadPersistentServices:authorizations:]
+ -[DADevice scopedToBundleID:]
+ -[DADevice setAppServicesInternalMap:]
+ -[DADevice setEncodeAppServices:]
+ -[DAEventExtension bundleID]
+ -[DAEventExtension setBundleID:]
+ -[DAExtensionCapability _terminateLaunchedProcess]
+ -[DAExtensionCapability invalidateRequested]
+ -[DAExtensionCapability setInvalidateRequested:]
+ GCC_except_table101
+ GCC_except_table19
+ GCC_except_table41
+ GCC_except_table46
+ GCC_except_table88
+ _OBJC_IVAR_$_DADevice._appServicesInternalMap
+ _OBJC_IVAR_$_DADevice._encodeAppServices
+ _OBJC_IVAR_$_DAEventExtension._bundleID
+ _OBJC_IVAR_$_DAExtensionCapability._invalidateRequested
+ ___25-[DADevice copyWithZone:]_block_invoke
+ ___33-[DADevice descriptionWithLevel:]_block_invoke_4
+ ___41+[DADevice normalizedPersistentServices:]_block_invoke
+ ___50-[DADevice loadPersistentServices:authorizations:]_block_invoke
+ ___block_descriptor_40_e8_32s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e46_v32?0"NSString"8"NSMutableDictionary"16^B24ls32l8
+ ___block_descriptor_52_e8_32r40r_e46_v32?0"NSString"8"NSMutableDictionary"16^B24lr32l8r40l8
+ ___block_descriptor_56_e8_32s40s48s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8s48l8
- GCC_except_table17
- GCC_except_table45
- GCC_except_table58
- GCC_except_table85
- GCC_except_table98
CStrings:
+ "### Failed to terminate PID %d: %@"
+ "+[DADevice persistentServiceInfos:deviceID:perApp:authorizations:]"
+ "-[DAExtensionCapability _terminateLaunchedProcess]"
+ "AppExtensionGeneralWorker"
+ "CapabilityInfoMap: no accessory services found for '%@' on %@"
+ "DAErrorCodeTaskInterrupted"
+ "DAErrorCodeTaskRejected"
+ "Invalidated while launching"
+ "Invalidated while launching, %s PID %d: %@"
+ "[ServiceInfo Decoding Error] %@"
+ "appServices"
+ "dApS"
+ "not starting"
+ "services"
+ "terminating"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSMutableDictionary\"16^B24"
- "CapabilityInfoMap: no accessory services found for %@"
```
