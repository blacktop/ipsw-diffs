## CoreMediaIO

> `/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-5631.0.0.0.0
-  __TEXT.__text: 0x3ea8c
+5633.0.0.0.0
+  __TEXT.__text: 0x3eb2c
   __TEXT.__objc_methlist: 0x204c
   __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0x145c
   __TEXT.__cstring: 0x8795
   __TEXT.__oslogstring: 0x4266
   __TEXT.__dlopen_cstrs: 0xb8
-  __TEXT.__unwind_info: 0xc50
+  __TEXT.__unwind_info: 0xc58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1008
   __DATA_CONST.__objc_superrefs: 0xd8
-  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__got: 0x280
   __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__cfstring: 0x2140
   __AUTH_CONST.__objc_const: 0x3a20

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1369
-  Symbols:   2252
+  Symbols:   2253
   CStrings:  1035
 
Symbols:
+ ___block_descriptor_48_e8_32o40o_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8s40l8
+ ___block_descriptor_64_e8_32o40o48o56o_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s56l8
+ _objc_release_x24
- ___block_descriptor_40_e8_32o_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8
- ___block_descriptor_56_e8_32o40o48o_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8
Functions:
~ -[CMIOExtensionSessionStream updatePropertyStates:streamID:] : 380 -> 384
~ -[CMIOExtensionSessionStream delegate] : 8 -> 44
~ -[CMIOExtensionSessionDevice updateStreamIDs:] : 1016 -> 1028
~ ___46-[CMIOExtensionSessionDevice updateStreamIDs:]_block_invoke : 252 -> 244
~ -[CMIOExtensionSessionDevice delegate] : 8 -> 44
~ -[CMIOExtensionSessionProvider delegate] : 8 -> 44
~ -[CMIOExtensionSessionProvider extension:didFailWithError:] : 104 -> 108
~ -[CMIOExtensionSessionProvider extensionHasBeenInvalidated:] : 240 -> 244
~ -[CMIOExtensionSessionProvider extension:pluginPropertiesChanged:] : 328 -> 332
~ -[CMIOExtensionSessionProvider extension:availableDevicesChanged:] : 968 -> 988
~ ___66-[CMIOExtensionSessionProvider extension:availableDevicesChanged:]_block_invoke : 316 -> 304
~ ___41-[CMIOExtensionSession initWithDelegate:]_block_invoke : 720 -> 744
```
