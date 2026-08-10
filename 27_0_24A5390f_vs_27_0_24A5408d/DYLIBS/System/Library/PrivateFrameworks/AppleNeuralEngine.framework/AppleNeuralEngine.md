## AppleNeuralEngine

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-382.12.0.0.0
-  __TEXT.__text: 0x57ec0
-  __TEXT.__objc_methlist: 0x2b94
+382.15.1.0.0
+  __TEXT.__text: 0x59574
+  __TEXT.__objc_methlist: 0x2c3c
   __TEXT.__const: 0x2b8
-  __TEXT.__oslogstring: 0xb883
-  __TEXT.__cstring: 0x3893
-  __TEXT.__gcc_except_tab: 0x67d0
-  __TEXT.__unwind_info: 0x1418
+  __TEXT.__oslogstring: 0xba7b
+  __TEXT.__cstring: 0x3a6d
+  __TEXT.__gcc_except_tab: 0x6b7c
+  __TEXT.__ustring: 0xb76
+  __TEXT.__unwind_info: 0x1620
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x978
-  __DATA_CONST.__objc_classlist: 0x130
+  __DATA_CONST.__const: 0xad0
+  __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1a28
+  __DATA_CONST.__objc_selrefs: 0x1a88
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd8
-  __DATA_CONST.__objc_arraydata: 0x120
+  __DATA_CONST.__objc_arraydata: 0x128
   __DATA_CONST.__got: 0x2f8
-  __AUTH_CONST.__const: 0x4d0
-  __AUTH_CONST.__cfstring: 0x4a80
-  __AUTH_CONST.__objc_const: 0x3cd0
+  __AUTH_CONST.__const: 0x4f0
+  __AUTH_CONST.__cfstring: 0x4fe0
+  __AUTH_CONST.__objc_const: 0x3d88
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0x680
-  __AUTH.__objc_data: 0x4b0
+  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__auth_got: 0x688
+  __AUTH.__objc_data: 0x500
   __DATA.__objc_ivar: 0x23c
-  __DATA.__data: 0x718
-  __DATA.__bss: 0x180
+  __DATA.__data: 0x720
+  __DATA.__bss: 0x190
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0xf8

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 1726
-  Symbols:   2899
-  CStrings:  1433
+  Functions: 1751
+  Symbols:   2945
+  CStrings:  1483
 
Symbols:
+ +[_ANECompileFlavorPolicy nonBondedCsIdentities]
+ +[_ANECompileFlavorPolicy shouldDisableBondedForCsIdentity:]
+ +[_ANEErrors errorForCode:method:]
+ +[_ANEErrors errorForCode:method:underlyingCode:]
+ +[_ANEErrors errorForCode:method:underlyingCode:additionalUserInfo:]
+ +[_ANEErrors inferenceErrorForStatus:method:]
+ +[_ANEErrors stringForCode:]
+ +[_ANEModelToken appGroupIdentifiersFor:processIdentifier:]
+ +[_ANEStrings modelSourceContainerName]
+ -[_ANEClient compiledModelExistsInCacheFor:limitToCurrentProcess:]
+ -[_ANEClient updateCachedModelLocationForModelTrackedByHash:toAppGroup:error:]
+ -[_ANEDaemonConnection compiledModelExistsInCacheFor:limitToCurrentProcess:withReply:]
+ -[_ANEDaemonConnection updateCachedModelLocationForModelTrackedByHash:toAppGroup:withReply:]
+ GCC_except_table0
+ GCC_except_table20
+ GCC_except_table21
+ GCC_except_table22
+ GCC_except_table23
+ GCC_except_table24
+ GCC_except_table27
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table52
+ GCC_except_table68
+ GCC_except_table71
+ _CFArrayGetTypeID
+ _OBJC_CLASS_$__ANECompileFlavorPolicy
+ _OBJC_METACLASS_$__ANECompileFlavorPolicy
+ __OBJC_$_CLASS_METHODS__ANECompileFlavorPolicy
+ __OBJC_CLASS_RO_$__ANECompileFlavorPolicy
+ __OBJC_METACLASS_RO_$__ANECompileFlavorPolicy
+ ___48+[_ANECompileFlavorPolicy nonBondedCsIdentities]_block_invoke
+ ___66-[_ANEClient compiledModelExistsInCacheFor:limitToCurrentProcess:]_block_invoke
+ ___66-[_ANEClient compiledModelExistsInCacheFor:limitToCurrentProcess:]_block_invoke_2
+ ___78-[_ANEClient updateCachedModelLocationForModelTrackedByHash:toAppGroup:error:]_block_invoke
+ ___78-[_ANEClient updateCachedModelLocationForModelTrackedByHash:toAppGroup:error:]_block_invoke_2
+ ___86-[_ANEDaemonConnection compiledModelExistsInCacheFor:limitToCurrentProcess:withReply:]_block_invoke
+ ___92-[_ANEDaemonConnection updateCachedModelLocationForModelTrackedByHash:toAppGroup:withReply:]_block_invoke
+ ___block_descriptor_65_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_72_e8_32s40s48r56r_e20_v20?0B8"NSError"12lr48l8s32l8s40l8r56l8
+ ___block_descriptor_80_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8
+ ___block_descriptor_88_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8
+ _kANEErrorLoadStageKey
+ _kANEErrorUnderlyingStatusKey
+ _kANEFDisableBondedNetworksKey
+ _nonBondedCsIdentities.list
+ _nonBondedCsIdentities.once
+ _objc_msgSend$compiledModelExistsInCacheFor:limitToCurrentProcess:
+ _objc_msgSend$compiledModelExistsInCacheFor:limitToCurrentProcess:withReply:
+ _objc_msgSend$errorForCode:method:underlyingCode:
+ _objc_msgSend$errorForCode:method:underlyingCode:additionalUserInfo:
+ _objc_msgSend$inferenceErrorForStatus:method:
+ _objc_msgSend$nonBondedCsIdentities
+ _objc_msgSend$notSupportedErrorForMethod:
+ _objc_msgSend$programTooLargeErrorForMethod:
+ _objc_msgSend$stringForCode:
+ _objc_msgSend$updateCachedModelLocationForModelTrackedByHash:toAppGroup:withReply:
- -[_ANEDaemonConnection compiledModelExistsInCacheFor:withReply:]
- GCC_except_table64
- GCC_except_table67
- ___44-[_ANEClient compiledModelExistsInCacheFor:]_block_invoke
- ___44-[_ANEClient compiledModelExistsInCacheFor:]_block_invoke_2
- ___64-[_ANEDaemonConnection compiledModelExistsInCacheFor:withReply:]_block_invoke
- ___block_descriptor_64_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- ___block_descriptor_96_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8s48l8r64l8
- _objc_msgSend$compiledModelExistsInCacheFor:withReply:
- _objc_msgSend$programIOSurfacesMapErrorForMethod:code:
- _objc_msgSend$programIOSurfacesUnmapErrorForMethod:code:
CStrings:
+ "%@: %@"
+ "%@: %@ (underlying=0x%lX)"
+ "%@: ANE error (code=%lu)"
+ "%@: ANE error (code=%lu, underlying=0x%lX)"
+ "%@: SecTaskCopyValueForEntitlement() returned app-groups:=\"%@\""
+ "%@: appGroupIdentifiersFor ignoring inelligible app-group (found %@)"
+ "%@: client(%d) : does not belong to an app-group"
+ "../"
+ "Error: %@ encountered during updateCachedModelLocationForModelTrackedByHash:%@ toAppGroup:%@"
+ "Inference failed — ANE firmware failure"
+ "Inference failed — ANE hardware failure"
+ "Inference failed — IOSurface smaller than the model expects (re-check inputBufferSize/outputBufferSize from the load reply)"
+ "Inference failed — ISO too old (transient; retry)"
+ "Inference failed — bad program image (model may be corrupt or incompatible)"
+ "Inference failed — device not ready (transient; retry)"
+ "Inference failed — device power-on failed (transient; retry)"
+ "Inference failed — device still open (lifecycle issue)"
+ "Inference failed — exclusive-access contention with another client"
+ "Inference failed — generic ANE error"
+ "Inference failed — invalid argument or state"
+ "Inference failed — no ANE resources (transient; retry)"
+ "Inference failed — no memory (transient; retry under lower memory pressure)"
+ "Inference failed — operation not permitted (check entitlements)"
+ "Inference failed — referenced resource not found"
+ "Inference failed — request aborted"
+ "Inference failed — shared intermediate buffer alloc/lock failure"
+ "Inference preempted by higher-priority request (transient; retry)"
+ "Mutable weights map failed"
+ "Mutable weights unmap failed"
+ "Program IOSurfaces map failed"
+ "Program IOSurfaces unmap failed"
+ "Program load failed — ANE firmware failure"
+ "Program load failed — ANE hardware failure"
+ "Program load failed — bad program image (model may be corrupt or incompatible)"
+ "Program load failed — device power-on failed (transient; retry)"
+ "Program load failed — generic ANE error"
+ "Program load failed — no ANE resources (transient; retry)"
+ "Program load failed — no memory (transient; retry under lower memory pressure)"
+ "Program load failed — operation not permitted (check entitlements)"
+ "Session hint request failed"
+ "[proxy updateCachedModelLocationForModelTrackedByHash:%@ toAppGroup:%@...] returned success = %d with error = %@"
+ "_"
+ "_ANEErrorLoadStage"
+ "_ANEErrorUnderlyingStatus"
+ "com.apple.security.application-groups"
+ "com.topazlabs.TopazPhotoAI"
+ "kANEFDisableBondedNetworksKey"
+ "model.src_cont"
+ "updateCachedModelLocationForModelTrackedByHash:%@ toAppGroup:%@"
+ "updateLocationForModelTrackedByHash:%@ toAppGroup:%@"
```
