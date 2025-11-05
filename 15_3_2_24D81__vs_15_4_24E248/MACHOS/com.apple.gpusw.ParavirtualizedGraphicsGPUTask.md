## com.apple.gpusw.ParavirtualizedGraphicsGPUTask

> `/System/Library/Frameworks/ParavirtualizedGraphics.framework/Versions/A/XPCServices/com.apple.gpusw.ParavirtualizedGraphicsGPUTask.xpc/Contents/MacOS/com.apple.gpusw.ParavirtualizedGraphicsGPUTask`

```diff

-40.3.2.0.0
-  __TEXT.__text: 0x27734
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_stubs: 0x5ea0
-  __TEXT.__objc_methlist: 0x2124
-  __TEXT.__const: 0xf0
-  __TEXT.__objc_classname: 0x47f
-  __TEXT.__objc_methname: 0x764d
-  __TEXT.__objc_methtype: 0x88a0
-  __TEXT.__cstring: 0x2d52
-  __TEXT.__oslogstring: 0xf1f
-  __TEXT.__gcc_except_tab: 0x1134
-  __TEXT.__unwind_info: 0xd98
-  __DATA_CONST.__auth_got: 0x330
-  __DATA_CONST.__got: 0x1a0
+40.5.10.0.0
+  __TEXT.__text: 0x401ec
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_stubs: 0x5800
+  __TEXT.__objc_methlist: 0x2420
+  __TEXT.__objc_classname: 0x50e
+  __TEXT.__objc_methname: 0x6b86
+  __TEXT.__objc_methtype: 0x31df
+  __TEXT.__cstring: 0x371c
+  __TEXT.__gcc_except_tab: 0x30ec
+  __TEXT.__const: 0x2fa8
+  __TEXT.__oslogstring: 0xfa2
+  __TEXT.__unwind_info: 0x1748
+  __DATA_CONST.__auth_got: 0x420
+  __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x630
-  __DATA_CONST.__cfstring: 0x1820
-  __DATA_CONST.__objc_classlist: 0x138
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__const: 0x7e8
+  __DATA_CONST.__cfstring: 0x1180
+  __DATA_CONST.__objc_classlist: 0x148
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x118
-  __DATA.__objc_const: 0x4518
-  __DATA.__objc_selrefs: 0x1978
-  __DATA.__objc_ivar: 0x2b0
-  __DATA.__objc_data: 0xc30
-  __DATA.__data: 0x4e0
+  __DATA.__objc_const: 0x3760
+  __DATA.__objc_selrefs: 0x1868
+  __DATA.__objc_ivar: 0x248
+  __DATA.__objc_data: 0xcd0
+  __DATA.__data: 0x5a0
   __DATA.__common: 0x810
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0F5F16F6-ABA5-3316-BFA9-4C528C0F1EEC
-  Functions: 1051
-  Symbols:   286
-  CStrings:  1883
+  UUID: 529B7598-2699-390D-8A7C-0640256AB40F
+  Functions: 1332
+  Symbols:   394
+  CStrings:  1834
 
Symbols:
+ OBJC_IVAR_$_PGBaseTask._objectListManager
+ OBJC_IVAR_$_PGBaseTask._resourceManager
+ _OBJC_CLASS_$_PGDiscardableHeapBufferResource
+ _OBJC_CLASS_$_PGDiscardableSerializerTextureResource
+ _OBJC_CLASS_$_PGResourceManagerDelegate
+ _OBJC_CLASS_$_PGResourceManagerDeserializationContext
+ _OBJC_METACLASS_$_PGDiscardableHeapBufferResource
+ _OBJC_METACLASS_$_PGDiscardableSerializerTextureResource
+ _OBJC_METACLASS_$_PGResourceManagerDelegate
+ _OBJC_METACLASS_$_PGResourceManagerDeserializationContext
+ __Z17newFunctionWithIRPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEE5PGPtrIP6NSDataE
+ __Z19newIOSurfaceTextureP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectP9IOSurfaceNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z20newTextureDescriptorPK29PGSerializedTextureDescriptory
+ __Z20newTextureDescriptorPK30PGSerializedTextureDescriptor2y
+ __Z24newTextureWithDescriptorP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z25newTextureWithDescriptor2P17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z28newSerializerTextureWithHeapP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z29newSamplerStateWithDescriptorPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __Z30newSharedTextureWithDescriptorP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z31newIOSurfaceTextureWithRotationP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectP9IOSurfaceNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z31newSharedTextureWithDescriptor2P17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z33newRasterizationRateMapDescriptorP41PGOperationRasterizationRateMapDescriptorNSt3__110shared_ptrI21PGVirtualMemoryCursorEE
+ __Z34newDepthStencilStateWithDescriptorPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __Z34newSerializerTextureViewWithBufferP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z34newSerializerTextureWithDescriptorP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z35newSerializerTextureViewWithSwizzleP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z35newSerializerTextureWithDescriptor2P17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z36newRenderPipelineStateWithDescriptorPU19objcproto9MTLDevice11objc_objectPU36objcproto25MTLDeserializationContext11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __Z37newComputePipelineStateWithDescriptorPU19objcproto9MTLDevice11objc_objectPU36objcproto25MTLDeserializationContext11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __Z37newRasterizationRateMapWithDescriptorPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __Z39newSerializerTextureViewWithPixelFormatP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z39newSerializerTextureViewWithTextureTypeP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z40newRenderPipelineStateWithTileDescriptorPU19objcproto9MTLDevice11objc_objectPU36objcproto25MTLDeserializationContext11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN14PGByteIteratorC1EPKvy
+ __ZN17PGResourceManager10createHeapERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createBufferERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createObjectIP10PGResourceEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEERK14APVObjectEntryNS3_10shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createObjectIPU18objcproto8MTLFence11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEERK14APVObjectEntryNS3_10shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createObjectIPU22objcproto11MTLFunction11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEERK14APVObjectEntryNS3_10shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createObjectIPU26objcproto15MTLSamplerState11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEERK14APVObjectEntryNS3_10shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createObjectIPU31objcproto20MTLDepthStencilState11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEERK14APVObjectEntryNS3_10shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createObjectIPU33objcproto22MTLRenderPipelineState11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEERK14APVObjectEntryNS3_10shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createObjectIPU34objcproto23MTLComputePipelineState11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEERK14APVObjectEntryNS3_10shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createObjectIPU34objcproto23MTLRasterizationRateMap11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEERK14APVObjectEntryNS3_10shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12deleteObjectEPKvm
+ __ZN17PGResourceManager13createBackingERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager13reserveObjectEjRK14APVObjectEntryRK18APVObjectPlacementRNS_16ReservationTableE
+ __ZN17PGResourceManager14flushResourcesEv
+ __ZN17PGResourceManager14getObjectEntryEj
+ __ZN17PGResourceManager14objectDelegateEv
+ __ZN17PGResourceManager14reserveObjectsEv
+ __ZN17PGResourceManager15newMemoryCursorEym
+ __ZN17PGResourceManager16createHeapBufferERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager17getExistingObjectIP10PGResourceEENSt3__18optionalIT_EEj
+ __ZN17PGResourceManager17getExistingObjectIPU34objcproto23MTLRasterizationRateMap11objc_objectEENSt3__18optionalIT_EEj
+ __ZN17PGResourceManager19createNormalTextureERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager19createSharedTextureERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager20finalizeReservationsERNS_16ReservationTableE
+ __ZN17PGResourceManager21createMapperRefBufferERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager22createMapperRefTextureERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager23clearPlacementListEntryEj
+ __ZN17PGResourceManager23createBackingRefTextureERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager23createSerializerTextureERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager23heapTextureSizeAndAlignEPKvm
+ __ZN17PGResourceManager26createSharedTextureBackingERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager30textureDescriptorForDescriptorEPK29PGSerializedTextureDescriptor
+ __ZN17PGResourceManager32newWritableMemoryCursorForBufferEj
+ __ZN17PGResourceManager7getDataEym
+ __ZN17PGResourceManager9getObjectIPU17objcproto7MTLHeap11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9getObjectIPU19objcproto9MTLBuffer11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9getObjectIPU21objcproto10MTLTexture11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9getObjectIPU22objcproto11MTLResource11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManagerC1EPU19objcproto9MTLDevice11objc_objectPU50objcproto15PGTask_Resource22PGTask_ResourceManager11objc_objectNSt3__110shared_ptrI19PGObjectListManagerEE
+ __ZN17PGResourceManagerC2EPU19objcproto9MTLDevice11objc_objectPU50objcproto15PGTask_Resource22PGTask_ResourceManager11objc_objectNSt3__110shared_ptrI19PGObjectListManagerEE
+ __ZN17PGResourceManagerD1Ev
+ __ZN17PGResourceManagerD2Ev
+ __ZN19PGObjectListManager13setObjectListEyjyjP12APVTaskRoot2
+ __ZN21PGVirtualMemoryCursor16cursorWithRangesERNSt3__16vectorINS_5RangeENS0_9allocatorIS2_EEEE
+ __ZN21PGVirtualMemoryCursor7advanceEm
+ __ZN21PGVirtualMemoryCursor9readBytesEmPv
+ __ZN21PGVirtualMemoryCursorC2ENSt3__16vectorINS_5RangeENS0_9allocatorIS2_EEEE
+ __ZN28PGMemoryMapObjectListManager10newMappingEyyb
+ __ZN28PGMemoryMapObjectListManager13mapObjectListEv
+ __ZN28PGMemoryMapObjectListManager15unmapObjectListEv
+ __ZN28PGMemoryMapObjectListManager16mapPlacementListEv
+ __ZN28PGMemoryMapObjectListManager18unmapPlacementListEv
+ __ZN29PGWritableVirtualMemoryCursor10writeBytesEmPKv
+ __ZN29PGWritableVirtualMemoryCursor16cursorWithRangesERNSt3__16vectorIN21PGVirtualMemoryCursor5RangeENS0_9allocatorIS3_EEEE
+ __ZN29PGWritableVirtualMemoryCursorC2ENSt3__16vectorIN21PGVirtualMemoryCursor5RangeENS0_9allocatorIS3_EEEE
+ __ZNKSt13runtime_error4whatEv
+ __ZNKSt3__119__shared_weak_count13__get_deleterERKSt9type_info
+ __ZNKSt3__16locale9use_facetERNS0_2idE
+ __ZNSt12out_of_rangeD1Ev
+ __ZNSt13runtime_errorC2EPKc
+ __ZNSt13runtime_errorD2Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc
+ __ZNSt3__119__shared_weak_count14__release_weakEv
+ __ZNSt3__119__shared_weak_countD2Ev
+ __ZNSt3__16localeC1ERKS0_
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16localeD1Ev
+ __ZNSt3__16localeaSERKS0_
+ __ZNSt3__18numpunctIcE2idE
+ __ZNSt3__18to_charsEPcS0_d
+ __ZNSt3__18to_charsEPcS0_dNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_dNS_12chars_formatEi
+ __ZNSt3__18to_charsEPcS0_e
+ __ZNSt3__18to_charsEPcS0_eNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_eNS_12chars_formatEi
+ __ZNSt3__18to_charsEPcS0_f
+ __ZNSt3__18to_charsEPcS0_fNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_fNS_12chars_formatEi
+ __ZTV28PGMemoryMapObjectListManager
+ __ZTVSt12out_of_range
+ __ZdlPvSt19__type_descriptor_t
+ __ZnwmSt19__type_descriptor_t
+ ___cxa_end_catch
+ ___cxa_pure_virtual
+ ___cxa_rethrow
+ ___udivti3
+ ___umodti3
+ __dispatch_data_destructor_free
+ _memchr
+ _memset
+ _strlen
- OBJC_IVAR_$_PGBaseTask._computePipelines
- OBJC_IVAR_$_PGBaseTask._depthStencils
- OBJC_IVAR_$_PGBaseTask._fences
- OBJC_IVAR_$_PGBaseTask._functions
- OBJC_IVAR_$_PGBaseTask._objectListMutex
- OBJC_IVAR_$_PGBaseTask._rasterizationRateMaps
- OBJC_IVAR_$_PGBaseTask._renderPipelines
- OBJC_IVAR_$_PGBaseTask._reservedSerializerTextures
- OBJC_IVAR_$_PGBaseTask._resources
- OBJC_IVAR_$_PGBaseTask._samplers
- _OBJC_CLASS_$_PGRangeBufferResource
- _OBJC_CLASS_$_PGRangeHeapResource
- _OBJC_METACLASS_$_PGRangeBufferResource
- _OBJC_METACLASS_$_PGRangeHeapResource
- __Z17validateCommandID13PGOperationIDS_
- __ZN14PGByteIteratorC1EPvy
- __os_log_debug_impl
- __os_log_default
- __os_log_impl
CStrings:
+ " does not allow the "
+ " formatting argument"
+ " option"
+ "-[PGDeserializerInfoDecoder decodeHeapTextureDescriptorSizeAndAlignWithIterator:]"
+ "-[ParavirtualizedGraphicsGPUTask cursorFromVirtualOffsetInternal:length:needWritable:]_block_invoke"
+ "0"
+ "01"
+ "01234567"
+ "0123456789abcdef"
+ "0123456789abcdefghijklmnopqrstuvwxyz"
+ "0B"
+ "0X"
+ "0b"
+ "0x"
+ "@\"<MTLCommandQueue>\"16@0:8"
+ "@\"MTLSharedTextureHandle\"20@0:8I16"
+ "@\"MTLTextureDescriptor\"24@0:8r^{?=b4b1b1b1b1b8b16IIISSSSQ}16"
+ "@\"NSData\"32@0:8Q16Q24"
+ "@\"PGMapping\"36@0:8Q16Q24B32"
+ "@24@0:8^v16"
+ "@24@0:8r^{?=b4b1b1b1b1b8b16IIISSSSQ}16"
+ "@36@0:8Q16Q24B32"
+ "@44@0:8@16^{?=QIIC}24^{?=IIIb24b8}32I40"
+ "@56@0:8@16r^{?=IQ}24r^{?=b14b1b1SQQCCCC[0{?=QQQIII}]}32Q40@48"
+ "@60@0:8@16I24r^{?=IQ}28r^{?=b14b1b1SQQCCCC[0{?=QQQIII}]}36Q44@52"
+ "An argument index may not have a negative value"
+ "Attempting to create mapper ref against invalid surface ({})"
+ "Attempting to create shared texture backing from a non shared texture resource"
+ "Attempting to fetch invalid object: {}"
+ "Attempting to use unsupported dual-plane textures"
+ "B52@0:8^{?=QIIC}16r^{?=IIIb24b8}24^{?=IIIb24b8}32I40Q44"
+ "Cannot get backing from a non-zero task ID"
+ "End of input while parsing an argument index"
+ "End of input while parsing format specifier precision"
+ "Failed copy cursor"
+ "Failed to alloc descriptor"
+ "Failed to alloc dimension"
+ "Failed to correctly place texture"
+ "Failed to create Buffer"
+ "Failed to create Function"
+ "Failed to create Heap"
+ "Failed to create Texture"
+ "Failed to create buffer host resource"
+ "Failed to create child resource"
+ "Failed to create compute pipeline: %@"
+ "Failed to create compute pipeline: {}"
+ "Failed to create cursor"
+ "Failed to create depth stencil state"
+ "Failed to create descriptor"
+ "Failed to create descriptor: {}"
+ "Failed to create dispatch data"
+ "Failed to create fence"
+ "Failed to create heap buffer"
+ "Failed to create heap buffer host resource"
+ "Failed to create heap host resource"
+ "Failed to create host resource"
+ "Failed to create host resource for shared texture backing"
+ "Failed to create library: {}"
+ "Failed to create mapper ref buffer host resource"
+ "Failed to create memory cursor"
+ "Failed to create rasterization rate map"
+ "Failed to create render pipeline: %@"
+ "Failed to create render pipeline: {}"
+ "Failed to create resource"
+ "Failed to create sampler state"
+ "Failed to create sampler state with correct resourceID"
+ "Failed to create shared texture"
+ "Failed to create texture"
+ "Failed to get %s (%s)"
+ "Failed to get backing for ioSurfaceID ({})"
+ "Failed to get base buffer: {}"
+ "Failed to get base heap {}"
+ "Failed to get base heap: {}"
+ "Failed to get base texture: {}"
+ "Failed to get compute pipeline: %s"
+ "Failed to get cursor for buffer"
+ "Failed to get function data"
+ "Failed to get function with ref %u: %s"
+ "Failed to get handle for shared texture"
+ "Failed to get placement: {}"
+ "Failed to get resource: %s"
+ "Failed to get shared texture handle for handle ({})"
+ "Failed to iterate: %@"
+ "Failed to read buffer descriptor: {}"
+ "Failed to read command: {}"
+ "Failed to read descriptor: {}"
+ "Failed to read dimension: {}"
+ "Failed to read function header: {}"
+ "Failed to read guest coordinate"
+ "Failed to read heap buffer descriptor: {}"
+ "Failed to read heap descriptor: {}"
+ "Failed to read height samples at index ({}): {}"
+ "Failed to read layer at index ({}): {}"
+ "Failed to read mapper ref buffer descriptor: {}"
+ "Failed to read mapper ref texture descriptor: {}"
+ "Failed to read normal texture descriptor: {}"
+ "Failed to read planes: {}"
+ "Failed to read rest of dimension: {}"
+ "Failed to read serializer header: {}"
+ "Failed to read shared texture backing header: {}"
+ "Failed to read shared texture descriptor: {}"
+ "Failed to read texture dimension: {}"
+ "Failed to read width samples at index ({}): {}"
+ "Failed to register object"
+ "Failed to reserve objects: %s"
+ "Failed to validate IOSurface descriptor"
+ "Failed to write to cursor: %s"
+ "Failed: %s"
+ "Insufficient data in command"
+ "Integral value outside the range of the char type"
+ "Invalid command for deletion"
+ "Invalid mip level count for shared texture backing"
+ "Invalid object type ({}) for compute pipeline state"
+ "Invalid object type ({}) for depthstencil state"
+ "Invalid object type ({}) for fence"
+ "Invalid object type ({}) for function"
+ "Invalid object type ({}) for rasterization rate map"
+ "Invalid object type ({}) for render pipeline state"
+ "Invalid object type ({}) for sampler state"
+ "Invalid object type {} for buffer cursor"
+ "Invalid placement of non-placeable render pipeline state"
+ "Invalid serializer command type ({})"
+ "Invalid storage mode"
+ "Invalid storage mode ({})"
+ "ObjectRef ref({}) out of range({})"
+ "Out of range cursor request"
+ "PGDiscardableHeapBufferResource"
+ "PGDiscardableSerializerTextureResource"
+ "PGResourceManager.mm"
+ "PGResourceManagerDelegate"
+ "PGResourceManagerDeserializationContext"
+ "PGResourceManager_RasterizationRate.mm"
+ "PGResourceManager_Texture.mm"
+ "PGResource_Buffer.mm"
+ "PGResource_Heap.mm"
+ "PGResource_Texture.mm"
+ "PGTask_ObjectListManager"
+ "PGTask_ResourceManager"
+ "Placement list not mapped"
+ "Read from offset ({}) length ({}) > cursorLength ({})"
+ "Replacement argument isn't a standard signed or unsigned integer type"
+ "T@\"<MTLCommandQueue>\",R"
+ "TQ,R,V_objectListCount"
+ "Task not wired"
+ "The argument index is invalid"
+ "The argument index should end with a ':' or a '}'"
+ "The argument index starts with an invalid character"
+ "The argument index value is too large for the number of arguments supplied"
+ "The fill option contains an invalid value"
+ "The format specifier contains malformed Unicode characters"
+ "The format specifier for "
+ "The format specifier should consume the input or end with a '}'"
+ "The format string contains an invalid escape sequence"
+ "The format string terminates at a '{'"
+ "The numeric value of the format specifier is too large"
+ "The precision option does not contain a value or an argument index"
+ "The replacement field misses a terminating '}'"
+ "The type does not fit in the mask"
+ "The type option contains an invalid value for "
+ "The type option contains an invalid value for a string formatting argument"
+ "The value of the argument index exceeds its maximum value"
+ "The width option should not have a leading zero"
+ "Too many planes ({}) in backing resource"
+ "Unable to do placement list copy"
+ "Unexpected function count in library ({})"
+ "Unexpected object type ({}) for resource"
+ "Unexpected serializer command type ({}) for backing ref texture"
+ "Unexpected serializer command type ({}) for mapper backed texture"
+ "Unexpected serializer command type ({}) for normal texture"
+ "Unexpected serializer command type ({}) for serializer texture"
+ "Unexpected serializer command type ({}) for shared ref texture"
+ "Unexpected serializer command type ({}) for shared texture backing resource"
+ "Using automatic argument numbering in manual argument numbering mode"
+ "Using manual argument numbering in automatic argument numbering mode"
+ "Write offset ({}) length ({}) > cursorLength ({})"
+ "Zero length cursor request"
+ "\\\""
+ "\\'"
+ "\\\\"
+ "\\n"
+ "\\r"
+ "\\t"
+ "\\u{"
+ "\\x{"
+ "_objectListManager"
+ "_resourceManager"
+ "a bool"
+ "a character"
+ "a floating-point"
+ "a pointer"
+ "alternate form"
+ "an integer"
+ "basic_string"
+ "command->rotation == (__typeof__(command->rotation))(*descriptor).rotation"
+ "computePipeline"
+ "createSharedTextureResourceWithTask:objectType:pagingInfo:dimension:dimensionLength:texture:"
+ "createTextureResourceWithTask:objectType:pagingInfo:dimension:dimensionLength:texture:"
+ "cursorFromVirtualOffset:length:"
+ "cursorFromVirtualOffsetInternal:length:needWritable:"
+ "decodeHeapTextureDescriptorSizeAndAlignWithIterator:"
+ "depthStencil"
+ "false"
+ "fence"
+ "from must be non-null"
+ "function"
+ "heapTextureSizeAndAlign"
+ "infnanINFNAN"
+ "initWithBuffer:"
+ "initWithResourceManager:"
+ "initWithTask:descriptor:planes:planeCount:"
+ "initWithTexture:"
+ "into must be non-null"
+ "lengthRemaining != 0"
+ "lengthRemaining >= lengthInPage"
+ "locale-specific form"
+ "newChildBufferResourceWithBuffer:"
+ "newChildTextureResourceWithTexture:"
+ "newIOSurfaceTextureWithRotation"
+ "newMemoryCursorForBuffer:"
+ "newRasterizationRateMapDescriptor"
+ "newSharedTextureWithHandle:withResourceIndex:"
+ "newVirtualMapping:length:needWritable:"
+ "object"
+ "pagingQueue"
+ "precision"
+ "rasterizationRateMap"
+ "rateMapDescriptor.layerCount == desc->layerCount"
+ "registerObject"
+ "renderPipeline"
+ "sampler"
+ "sign"
+ "texture"
+ "textureDescriptorForDescriptor:"
+ "true"
+ "v116@0:8I16Q20I28{?=QB}32{APVFeatures=BBBBBBBBBBBBBBBBBIIBBBBBBBBBBBBBBBBBBBBBBBB}48@\"PGMemoryMap\"100@?<v@?Ii>108"
+ "v116@0:8I16Q20I28{?=QB}32{APVFeatures=BBBBBBBBBBBBBBBBBIIBBBBBBBBBBBBBBBBBBBBBBBB}48@100@?108"
+ "validateBackingDescriptor:srcPlanes:destPlanes:planeCount:backingAllocationLength:"
+ "writableCursorFromVirtualOffset:length:"
+ "zero-padding"
+ "{shared_ptr<PGObjectListManager>=\"__ptr_\"^{PGObjectListManager}\"__cntrl_\"^{__shared_weak_count}}"
+ "{shared_ptr<PGVirtualMemoryCursor>=^{PGVirtualMemoryCursor}^{__shared_weak_count}}32@0:8Q16Q24"
+ "{shared_ptr<PGVirtualMemoryCursor>=^{PGVirtualMemoryCursor}^{__shared_weak_count}}36@0:8Q16Q24B32"
+ "{shared_ptr<PGWritableVirtualMemoryCursor>=^{PGWritableVirtualMemoryCursor}^{__shared_weak_count}}20@0:8I16"
+ "{shared_ptr<PGWritableVirtualMemoryCursor>=^{PGWritableVirtualMemoryCursor}^{__shared_weak_count}}32@0:8Q16Q24"
+ "{unique_ptr<PGResourceManager, std::default_delete<PGResourceManager>>=\"__ptr_\"{__compressed_pair<PGResourceManager *, std::default_delete<PGResourceManager>>=\"__value_\"^{PGResourceManager}}}"
+ "\xf0\xf0\xf0a"
- "!os_add_overflow(_objectListOffset, _objectListLength, &end)"
- "-[PGBaseTask newBackingRefTextureWithEntry:forReference:]"
- "-[PGBaseTask newNormalTextureWithEntry:forReference:]"
- "-[PGBaseTask newSerializerTextureWithEntry:forReference:]"
- "-[PGBaseTask newSharedTextureWithEntry:forReference:]"
- "-[PGBaseTask reserveObjects]"
- "-[PGBaseTask reservePlacedOtherSerializerReference:]"
- "-[PGDeserializerInfoDecoder decodeHeapTexturDescriptorSizeAndAlignWithIterator:]"
- "-[ParavirtualizedGraphicsGPUTask ensureObjectListMapped]"
- "-[ParavirtualizedGraphicsGPUTask rebuildTask]"
- "-[_PGDeserializer heapTextureSizeAndAlignWithSerializedData:serializedDataSize:]"
- "-[_PGDeserializer newTextureForSerializedData:serializedDataSize:ioSurface:resourceIndex:resourceID:]"
- "-[_PGDeserializer newTextureWithHeap:resourceIndex:resourceID:]"
- "-[_PGDeserializer reserveObjectWithSerializedData:serializedDataSize:placement:]"
- "@\"<MTLComputePipelineState>\"40@0:8r*16Q24^(PGDeserializerPlacement=Q{?=QQ})32"
- "@\"<MTLDepthStencilState>\"40@0:8r*16Q24^(PGDeserializerPlacement=Q{?=QQ})32"
- "@\"<MTLFence>\"40@0:8r*16Q24^(PGDeserializerPlacement=Q{?=QQ})32"
- "@\"<MTLFunction>\"40@0:8r*16Q24@\"NSObject<OS_dispatch_data>\"32"
- "@\"<MTLRasterizationRateMap>\"40@0:8r*16Q24^(PGDeserializerPlacement=Q{?=QQ})32"
- "@\"<MTLRenderPipelineState>\"40@0:8r*16Q24^(PGDeserializerPlacement=Q{?=QQ})32"
- "@\"<MTLSamplerState>\"40@0:8r*16Q24^(PGDeserializerPlacement=Q{?=QQ})32"
- "@\"<MTLTexture>\"40@0:8r*16Q24@\"MTLSharedTextureHandle\"32"
- "@\"<MTLTexture>\"48@0:8r*16Q24Q32Q40"
- "@\"<MTLTexture>\"56@0:8r*16Q24^{__IOSurface=}32Q40Q48"
- "@24@0:8r^{?=I{?=b3b1b1b1b26{?=b3b3b3b3b20II}{?=b3b3b3b3b20II}}}16"
- "@24@0:8r^{?=I}16"
- "@28@0:8^{?=b8b24Q}16I24"
- "@32@0:8^{?=II}16Q24"
- "@32@0:8^{?=I{?={?=SS}IIf[0{?={?=SS}}]}}16Q24"
- "@32@0:8r^{?=II}16Q24"
- "@32@0:8r^{?=I{?=b2b2b1b3b4b4b4b4b2b5b1b1b3b28ffQ}}16^(PGDeserializerPlacement=Q{?=QQ})24"
- "@32@0:8r^{?=b4b1b1b1b1b16IIIISSSSQCCCC}16Q24"
- "@32@0:8r^{?=b4b1b1b1b1b8b16IIISSSSQ}16Q24"
- "@36@0:8@16r^v24I32"
- "@40@0:8@16r^{?=IQQ}24^(?=Q{?=QQ})32"
- "@40@0:8^{?=IIQQ{?=b4b1b1b1b1b8b16IIISSSSQ}}16Q24Q32"
- "@40@0:8^{?=IISS{?=QQ}{?=QQ}CCCC}16Q24Q32"
- "@40@0:8^{?=IISS{?=QQ}{?=QQ}}16Q24Q32"
- "@40@0:8^{?=IIS}16Q24Q32"
- "@40@0:8^{?=II{?=b4b1b1b1b1b8b16IIISSSSQ}b1b31Q}16Q24Q32"
- "@40@0:8^{?=I{?=b4b1b1b1b1b16IIIISSSSQCCCC}}16Q24Q32"
- "@40@0:8^{?=I{?=b4b1b1b1b1b8b16IIISSSSQ}}16Q24Q32"
- "@40@0:8r*16Q24@32"
- "@40@0:8r*16Q24^(PGDeserializerPlacement=Q{?=QQ})32"
- "@48@0:8r*16Q24Q32Q40"
- "@52@0:8@16r^{?=IQ}24r^{?=b14b1b1SQQCCCC[0{?=QQQIII}]}32I40@44"
- "@56@0:8@16I24r^{?=IQ}28r^{?=b14b1b1SQQCCCC[0{?=QQQIII}]}36I44@48"
- "@56@0:8r*16Q24^{__IOSurface=}32Q40Q48"
- "Attempting to create reference texture from mapper with invalid device"
- "Attempting to use unsupported multi-plane texture"
- "B44@0:8^{?=QIIC}16^{?=IIIb24b8}24I32Q36"
- "Expected Cmd ID %u but received Cmd Id %u"
- "Failed allocate copy"
- "Failed at Metal level"
- "Failed to create backing ref texture"
- "Failed to create function"
- "Failed to create heap"
- "Failed to create host resource for mapperRef texture"
- "Failed to create host resource for ref texture"
- "Failed to create host resource for shared texture"
- "Failed to create mapper ref texture"
- "Failed to create normal texture"
- "Failed to create serializer texture"
- "Failed to create shared texture with handle"
- "Failed to get shared texture handle"
- "Failed to make mapping: %@"
- "Forcing address range resources"
- "Got invalid compute pipeline for ref(%d)"
- "Got invalid heap for ref(%d)"
- "Got invalid rate map for ref (%d)"
- "Got invalid render pipeline for ref(%d)"
- "Got invalid sampler state for ref(%d)"
- "Got invalid texture for ref(%d)"
- "Heap buffer size out of range"
- "Heap support not enabled"
- "IOSurface validation failed"
- "Invalid ComputePipelineState reference, %d"
- "Invalid ComputePipelineState reference, %d, object already exists"
- "Invalid DepthStencilState reference, %d"
- "Invalid DepthStencilState reference, %d, object already exists"
- "Invalid Fence reference, %d"
- "Invalid Fence reference, %d, object already exists"
- "Invalid RasterizationRateMap reference, %d"
- "Invalid RasterizationRateMap reference, %d, object already exists"
- "Invalid RenderPipelineState reference, %d"
- "Invalid RenderPipelineState reference, %d, object already exists"
- "Invalid SamplerState reference, %d"
- "Invalid SamplerState reference, %d, object already exists"
- "Invalid argument, entry isn't a buffer (%u)"
- "Invalid command"
- "Invalid function reference, %d"
- "Invalid function reference, %d, object already exists"
- "Invalid index for placement"
- "Invalid mip level count"
- "Invalid object ID"
- "Invalid reply size"
- "Invalid swizzle"
- "InvalidReference"
- "Non-kernel IOSurface backing task"
- "PGBaseTask.mm"
- "PGBufferResource.m"
- "PGHeapResource.m"
- "PGRangeBufferResource"
- "PGRangeHeapResource"
- "PGResource.m"
- "Placing compute pipeline states is not supported"
- "Placing depth stencil states is not supported"
- "Placing fences is not supported"
- "Placing rasterization rate maps is not supported"
- "Placing render pipeline states is not supported"
- "Placing texture"
- "Placing view"
- "Q24@0:8Q16"
- "Resource %d already exists"
- "TQ,R,D"
- "Trying to delete non-buffer resource from buffer path"
- "Trying to delete non-heap resource from heap path"
- "Trying to delete non-texture resource from texture path"
- "Unexpected function count: %u"
- "Unexpected object type (%d) for heap ref(%d)"
- "Unexpected object type (%d) for resource ref(%d)"
- "Unexpected object type (%d) for serializer ref(%d)"
- "Unexpected object type (%d) for texture ref(%d)"
- "Zero length object list"
- "^(?=Q{?=QQ})"
- "^(?=Q{?=QQ})20@0:8I16"
- "^{?=b8b24Q}"
- "_computePipelines"
- "_depthStencils"
- "_fences"
- "_functions"
- "_handShakeDone"
- "_objectList"
- "_objectListLength"
- "_objectListMapping"
- "_objectListOffset"
- "_placementList"
- "_placementListAlignedLength"
- "_placementListLength"
- "_placementListMapping"
- "_placementListOffset"
- "_rasterizationRateMaps"
- "_renderPipelines"
- "_reservedSerializerTextures"
- "_resources"
- "_samplers"
- "clearPlacementEntry:"
- "command->rotation == (__typeof__(command->rotation))descriptor.rotation"
- "decodeHeapTexturDescriptorSizeAndAlignWithIterator:"
- "deleteResourceForReference:"
- "deleteResourceLocked:clearPlacementListEntry:"
- "getPlacementEntry:"
- "heapTextureSizeAndAlignWithSerializedData:serializedDataSize:"
- "initWithTask:descriptor:descriptorLength:"
- "initWithTask:texture:"
- "listEntry->objectType == APVObjRefTexture"
- "listEntry->objectType == APVObjSerializerResource || listEntry->objectType == APVObjMemorylessTexture"
- "listEntry->objectType == APVObjSharedTexture"
- "listEntry->objectType == APVObjTexture || listEntry->objectType == APVObjClientStorageTexture || listEntry->objectType == APVObjDualPlaneTexture"
- "newBackingForReference:"
- "newBackingRefTextureWithEntry:forReference:"
- "newBufferForReference:"
- "newComputePipelineStateForReference:"
- "newComputePipelineStateWithDescriptor:serializedDataSize:"
- "newComputePipelineStateWithSerializedData:serializedDataSize:placement:"
- "newDepthStencilStateForReference:"
- "newDepthStencilStateWithSerializedData:serializedDataSize:placement:"
- "newFence:"
- "newFenceForReference:"
- "newFenceWithSerializedData:serializedDataSize:placement:"
- "newFunctionForReference:"
- "newFunctionWithSerializedData:serializedDataSize:metalLibData:"
- "newHeapBufferWithTask:descriptor:descriptorLength:placement:"
- "newHeapForReference:"
- "newMapperRefTextureWithEntry:forReference:"
- "newNormalTextureWithEntry:forReference:"
- "newRasterizationRateMapForReference:"
- "newRasterizationRateMapWithDescriptor:serializedDataSize:"
- "newRasterizationRateMapWithSerializedData:serializedDataSize:placement:"
- "newRenderPipelineStateForReference:"
- "newRenderPipelineStateWithDescriptor:serializedDataSize:"
- "newRenderPipelineStateWithSerializedData:serializedDataSize:placement:"
- "newRenderPipelineStateWithTileDescriptor:serializedDataSize:"
- "newResourceForReference:"
- "newSamplerStateForReference:"
- "newSamplerStateWithDescriptor:placement:"
- "newSamplerStateWithSerializedData:serializedDataSize:placement:"
- "newSerializerTextureWithEntry:forReference:"
- "newSharedTextureForSerializedData:serializedDataSize:sharedTextureHandle:"
- "newSharedTextureWithDescriptor2:resourceIndex:resourceID:"
- "newSharedTextureWithDescriptor:resourceIndex:resourceID:"
- "newSharedTextureWithEntry:forReference:"
- "newSharedTextureWithHandle:"
- "newTextureDescriptor2:resourceIndex:"
- "newTextureDescriptor:resourceIndex:"
- "newTextureForReference:"
- "newTextureForSerializedData:serializedDataSize:ioSurface:resourceIndex:resourceID:"
- "newTextureResourceWithTask:objectType:pagingInfo:dimension:dimensionLength:texture:"
- "newTextureViewWithBuffer:resourceIndex:resourceID:"
- "newTextureViewWithPixelFormat:resourceIndex:resourceID:"
- "newTextureViewWithSwizzle:resourceIndex:resourceID:"
- "newTextureViewWithTextureType:resourceIndex:resourceID:"
- "newTextureWithDescriptor2:resourceIndex:resourceID:"
- "newTextureWithDescriptor:resourceIndex:resourceID:"
- "newTextureWithHeap:resourceIndex:resourceID:"
- "newTextureWithSerializedData:serializedDataSize:resourceIndex:resourceID:"
- "newVirtualMapping:length:"
- "placement"
- "rasterizationRateMapInfoReplySizeForLayerCount:"
- "registerComputePipelineStateForReference:computePipeline:"
- "registerDepthStencilStateForReference:depthStencil:"
- "registerFenceForReference:fence:"
- "registerFunctionForReference:function:"
- "registerHostResource:forReference:"
- "registerRasterizationRateMapForReference:rasterizationRateMap:"
- "registerRenderPipelineStateForReference:renderPipeline:"
- "registerSamplerStateForReference:sampler:"
- "reserveObjectWithSerializedData:serializedDataSize:placement:"
- "reserveObjects"
- "reservePlacedOtherSerializerReference:"
- "reservePlacedTextureForReference:indices:"
- "self.features->supportsArgumentBuffers"
- "setReductionMode:"
- "supportsSharedTextureHandles"
- "v116@0:8I16Q20I28{?=QBB}32{APVFeatures=BBBBBBBBBBBBBBBBBIIBBBBBBBBBBBBBBBBBBBBBBBB}48@\"PGMemoryMap\"100@?<v@?Ii>108"
- "v116@0:8I16Q20I28{?=QBB}32{APVFeatures=BBBBBBBBBBBBBBBBBIIBBBBBBBBBBBBBBBBBBBBBBBB}48@100@?108"
- "v24@0:8I16B20"
- "v28@0:8I16@20"
- "v28@0:8I16^v20"
- "v32@0:8r*16Q24"
- "v40@0:8r*16Q24^(PGDeserializerPlacement=Q{?=QQ})32"
- "validateBackingDescriptor:dest:planeCount:backingAllocationLength:"
- "{?=QQ}32@0:8r*16Q24"
- "{unordered_map<unsigned int, PGPtr<PGResource *>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, PGPtr<PGResource *>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, PGPtr<id<MTLComputePipelineState>>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, PGPtr<id<MTLComputePipelineState>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, PGPtr<id<MTLDepthStencilState>>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, PGPtr<id<MTLDepthStencilState>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, PGPtr<id<MTLFence>>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, PGPtr<id<MTLFence>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, PGPtr<id<MTLFunction>>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, PGPtr<id<MTLFunction>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, PGPtr<id<MTLRasterizationRateMap>>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, PGPtr<id<MTLRasterizationRateMap>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, PGPtr<id<MTLRenderPipelineState>>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, PGPtr<id<MTLRenderPipelineState>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, PGPtr<id<MTLSamplerState>>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, PGPtr<id<MTLSamplerState>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_set<unsigned int, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<unsigned int>>=\"__table_\"{__hash_table<unsigned int, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<unsigned int>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<unsigned int, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned int, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<unsigned int, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned int, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned int, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<unsigned int, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<unsigned int, void *> *>, std::allocator<std::__hash_node<unsigned int, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<unsigned int, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::hash<unsigned int>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::equal_to<unsigned int>>=\"__value_\"f}}}"
- "\xf0\xf0\xf0\x81"

```
