## modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

-502.0.0.0.0
-  __TEXT.__text: 0x158aac
-  __TEXT.__auth_stubs: 0x37b0
+513.0.0.0.0
+  __TEXT.__text: 0x159470
+  __TEXT.__auth_stubs: 0x37a0
   __TEXT.__objc_methlist: 0x158
-  __TEXT.__const: 0x5046
-  __TEXT.__cstring: 0x3270
-  __TEXT.__swift5_typeref: 0x234d
+  __TEXT.__const: 0x5056
+  __TEXT.__cstring: 0x3280
+  __TEXT.__swift5_typeref: 0x2359
   __TEXT.__swift5_capture: 0xbc8
   __TEXT.__objc_methname: 0x492
-  __TEXT.__oslogstring: 0x8419
+  __TEXT.__oslogstring: 0x8409
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x2778
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_reflstr: 0x1ec3
-  __TEXT.__swift5_fieldmd: 0x1c54
+  __TEXT.__swift5_fieldmd: 0x1c60
   __TEXT.__swift5_types: 0x198
   __TEXT.__objc_classname: 0x78
   __TEXT.__objc_methtype: 0x191

   __TEXT.__swift5_proto: 0x2d8
   __TEXT.__swift5_assocty: 0x1a0
   __TEXT.__swift5_protos: 0x80
-  __TEXT.__unwind_info: 0x5cd0
-  __TEXT.__eh_frame: 0x14540
-  __DATA_CONST.__auth_got: 0x1bd8
+  __TEXT.__unwind_info: 0x5cd8
+  __TEXT.__eh_frame: 0x145a0
+  __DATA_CONST.__auth_got: 0x1bd0
   __DATA_CONST.__got: 0xe98
   __DATA_CONST.__auth_ptr: 0xc70
-  __DATA_CONST.__const: 0x3d10
+  __DATA_CONST.__const: 0x3cf0
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA.__objc_const: 0x3b68
+  __DATA.__objc_const: 0x3b88
   __DATA.__objc_selrefs: 0x220
   __DATA.__objc_data: 0x550
-  __DATA.__data: 0x5870
+  __DATA.__data: 0x5878
   __DATA.__common: 0x568
   __DATA.__bss: 0x4d40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5DDF8E4A-66CC-3D62-8E0A-66BBE8B701E4
-  Functions: 6434
-  Symbols:   1564
+  UUID: 7AE217DD-3F06-308C-991A-8B0FF5071100
+  Functions: 6429
+  Symbols:   1559
   CStrings:  1004
 
Symbols:
+ _$s20ModelManagerServices0A10XPCRequestO25StartMonitoringInferencesV8endpoint3XPC11XPCEndpointVvg
+ _$s20ModelManagerServices30InferenceProviderRequestResultV06directdE8Endpoint3XPC11XPCEndpointVSgvg
+ _$s3XPC10XPCSessionC8endpoint11targetQueue7options19cancellationHandlerAcA11XPCEndpointV_So17OS_dispatch_queueCSgAC21InitializationOptionsVyAA12XPCRichErrorVcSgtKcfC
+ _$s3XPC11XPCEndpointVMa
+ _$s3XPC11XPCEndpointVMn
- _$s20ModelManagerServices0A10XPCRequestO25StartMonitoringInferencesV8endpoint3XPC11XPCListenerC8EndpointVvg
- _$s20ModelManagerServices14InferenceErrorO8wrappingACs0E0_p_tcfC
- _$s20ModelManagerServices30InferenceProviderRequestResultV06directdE8Endpoint3XPC11XPCListenerC0I0VSgvg
- _$s3XPC10XPCSessionC8endpoint11targetQueue7options19cancellationHandlerAcA11XPCListenerC8EndpointV_So17OS_dispatch_queueCSgAC21InitializationOptionsVyAA12XPCRichErrorVcSgtKcfC
- _$s3XPC11XPCListenerC8EndpointVMa
- _$s3XPC11XPCListenerC8EndpointVMn
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "isFallback"
+ "loadAsset attempting to load %s, but waiting for it to finish moving to %s"
- "Client %d has entitlement %s set to false"
- "Could not find secTask for client %d"

```
