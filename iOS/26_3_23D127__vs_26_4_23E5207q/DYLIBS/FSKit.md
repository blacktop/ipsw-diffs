## FSKit

> `/System/Library/PrivateFrameworks/FSKit.framework/FSKit`

```diff

-737.80.2.0.0
-  __TEXT.__text: 0x40d48
-  __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_methlist: 0x4a54
-  __TEXT.__const: 0x3b8
-  __TEXT.__gcc_except_tab: 0xd54
-  __TEXT.__oslogstring: 0x3099
-  __TEXT.__cstring: 0x432f
+737.100.107.0.0
+  __TEXT.__text: 0x42b60
+  __TEXT.__auth_stubs: 0xd70
+  __TEXT.__objc_methlist: 0x4e9c
+  __TEXT.__const: 0x3f8
+  __TEXT.__gcc_except_tab: 0xd58
+  __TEXT.__oslogstring: 0x31ca
+  __TEXT.__cstring: 0x457f
   __TEXT.__swift5_typeref: 0x1d1
   __TEXT.__swift5_capture: 0x58
   __TEXT.__swift5_reflstr: 0x16

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x12f8
-  __TEXT.__eh_frame: 0x160
-  __TEXT.__objc_classname: 0x8e9
-  __TEXT.__objc_methname: 0x9af2
-  __TEXT.__objc_methtype: 0x32db
-  __TEXT.__objc_stubs: 0x57a0
-  __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x13a8
-  __DATA_CONST.__objc_classlist: 0x250
+  __TEXT.__unwind_info: 0x1378
+  __TEXT.__eh_frame: 0x1b0
+  __TEXT.__objc_classname: 0x9bd
+  __TEXT.__objc_methname: 0x9d8a
+  __TEXT.__objc_methtype: 0x3055
+  __TEXT.__objc_stubs: 0x5b20
+  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__const: 0x1328
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x140
+  __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24b0
-  __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x1c0
-  __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x6a8
-  __AUTH_CONST.__const: 0x4e8
-  __AUTH_CONST.__cfstring: 0x2340
-  __AUTH_CONST.__objc_const: 0x7f20
-  __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1040
+  __DATA_CONST.__objc_selrefs: 0x25b0
+  __DATA_CONST.__objc_protorefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x1f0
+  __DATA_CONST.__objc_arraydata: 0x2d8
+  __AUTH_CONST.__auth_got: 0x6c8
+  __AUTH_CONST.__const: 0x508
+  __AUTH_CONST.__cfstring: 0x2680
+  __AUTH_CONST.__objc_const: 0x8590
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__objc_dictobj: 0x2a8
+  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH.__objc_data: 0x10e0
   __AUTH.__data: 0x80
-  __DATA.__objc_ivar: 0x4a4
-  __DATA.__data: 0xf48
+  __DATA.__objc_ivar: 0x4e8
+  __DATA.__data: 0xef8
   __DATA.__bss: 0x320
-  __DATA_DIRTY.__objc_data: 0x820
+  __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BDC47B06-5423-3FF6-8A6F-2A8FD27CBFC1
-  Functions: 2011
-  Symbols:   6384
-  CStrings:  3339
+  UUID: F4DFB6E3-EB9E-3A12-B3C8-54B196F09FB9
+  Functions: 2133
+  Symbols:   6798
+  CStrings:  3471
 
Symbols:
+ +[FSActivationOption optionWithName:argumentType:defaultValue:]
+ +[FSActivationOptionSyntax allOptionNames:]
+ +[FSActivationOptionSyntax argTypeFromDictionary:]
+ +[FSActivationOptionSyntax parseOptionFromData:]
+ +[FSActivationOptionSyntax stringForOption:inOptions:]
+ +[FSActivationOptionSyntax stringFromDictionary:key:]
+ +[FSActivationOptionSyntax systemMountOptions]
+ +[FSItemAttributes requestWithFSAttributes:]
+ +[FSKitConstants(project) fskitdLiveFSMachServiceName]
+ +[FSKitConstants(project) fskitdMachServiceName]
+ +[FSMachPort newByCopyingPort:]
+ +[FSMachPort supportsSecureCoding]
+ +[FSMemoryMap newWithPort:address:andSize:]
+ +[FSModuleExtension(Project) fskitdIsClient:]
+ +[FSModuleExtension(Project) fskitdIsClient:].cold.1
+ +[FSSharedMutableBuffer bufferWithCapacity:]
+ +[FSSharedMutableBuffer bufferWithLength:]
+ +[FSSharedMutableBuffer dataWithCapacity:]
+ +[FSSharedMutableBuffer dataWithLength:]
+ +[FSSharedMutableBuffer newByCopyingPort:]
+ +[FSSharedMutableBuffer supportsSecureCoding]
+ +[FSUserClient defaultClient]
+ -[FSActivationOption .cxx_destruct]
+ -[FSActivationOption argumentType]
+ -[FSActivationOption defaultValue]
+ -[FSActivationOption name]
+ -[FSActivationOption setArgumentType:]
+ -[FSActivationOption setDefaultValue:]
+ -[FSActivationOption setName:]
+ -[FSActivationOptionSyntax .cxx_destruct]
+ -[FSActivationOptionSyntax initWithAttributeData:]
+ -[FSActivationOptionSyntax initWithOptions:]
+ -[FSActivationOptionSyntax optionWithName:]
+ -[FSActivationOptionSyntax options]
+ -[FSActivationOptionSyntax setOptions:]
+ -[FSActivationOptionSyntax validateOptions:]
+ -[FSActivationOptionSyntax validateOptions:].cold.1
+ -[FSActivationOptionSyntax validateOptions:].cold.2
+ -[FSActivationOptionSyntax validateOptions:].cold.3
+ -[FSBlockDeviceResource isSSD]
+ -[FSClient hasEntitlement]
+ -[FSClient(Project) currentContainers:]
+ -[FSClient(Project) currentContainersSync:]
+ -[FSClient(Project) currentResourceIDs:]
+ -[FSClient(Project) currentResourceIDsSync:]
+ -[FSClient(Project) currentTasks:]
+ -[FSClient(Project) currentTasksSync:]
+ -[FSItemAttributes _setInhibitKernelOffloadedIO:]
+ -[FSItemAttributes getFSAttributes:]
+ -[FSItemAttributes initWithFSAttributes:]
+ -[FSItemAttributes sequenceNumber]
+ -[FSItemAttributes setSequenceNumberIfNeeded]
+ -[FSItemGetAttributesRequest initWithWantedFSAttributes:]
+ -[FSMachPort classForCoder]
+ -[FSMachPort dealloc]
+ -[FSMachPort dealloc].cold.1
+ -[FSMachPort encodeWithCoder:]
+ -[FSMachPort initWithCoder:]
+ -[FSMachPort initWithCoder:].cold.1
+ -[FSMachPort initWithPort:]
+ -[FSMachPort machPort]
+ -[FSMemoryMap address]
+ -[FSMemoryMap dealloc]
+ -[FSMemoryMap dealloc].cold.1
+ -[FSMemoryMap initWithPort:address:andSize:]
+ -[FSMemoryMap port]
+ -[FSMemoryMap setPort:]
+ -[FSMemoryMap size]
+ -[FSMessageReceiver dealloc]
+ -[FSMessageReceiver dealloc].cold.1
+ -[FSModuleIdentity fsShortName]
+ -[FSModuleInstance description]
+ -[FSServiceUserClient clearMetaBlocks:ranges:rangesCount:wait:]
+ -[FSServiceUserClient clearMetaBlocks:ranges:rangesCount:wait:].cold.1
+ -[FSServiceUserClient clearMetaBlocks:ranges:rangesCount:wait:].cold.2
+ -[FSServiceUserClient closeFileDescriptorForKernel:]
+ -[FSServiceUserClient createVolumePort]
+ -[FSServiceUserClient flushMeta:wait:]
+ -[FSServiceUserClient flushMeta:wait:].cold.1
+ -[FSServiceUserClient flushMeta:wait:].cold.2
+ -[FSServiceUserClient getVolumePort]
+ -[FSServiceUserClient init]
+ -[FSServiceUserClient openFileDescriptorForKernel:flags:]
+ -[FSServiceUserClient purgeMetaBlocks:ranges:rangesCount:]
+ -[FSServiceUserClient purgeMetaBlocks:ranges:rangesCount:].cold.1
+ -[FSServiceUserClient purgeMetaBlocks:ranges:rangesCount:].cold.2
+ -[FSServiceUserClient readMeta:buffer:offset:length:]
+ -[FSServiceUserClient readMeta:buffer:offset:length:].cold.1
+ -[FSServiceUserClient readMeta:buffer:offset:length:].cold.2
+ -[FSServiceUserClient readMetaWithRA:buffer:offset:length:raList:raListCount:]
+ -[FSServiceUserClient readMetaWithRA:buffer:offset:length:raList:raListCount:].cold.1
+ -[FSServiceUserClient readMetaWithRA:buffer:offset:length:raList:raListCount:].cold.2
+ -[FSServiceUserClient writeMeta:buffer:offset:length:]
+ -[FSServiceUserClient writeMeta:buffer:offset:length:].cold.1
+ -[FSServiceUserClient writeMeta:buffer:offset:length:].cold.2
+ -[FSServiceUserClient writeMetaDelayed:buffer:offset:length:]
+ -[FSServiceUserClient writeMetaDelayed:buffer:offset:length:].cold.1
+ -[FSServiceUserClient writeMetaDelayed:buffer:offset:length:].cold.2
+ -[FSServiceUserClient writeMetaSubBlock:offset:length:subBlockBuffer:subBlockOffset:subBlockLength:]
+ -[FSServiceUserClient writeMetaSubBlock:offset:length:subBlockBuffer:subBlockOffset:subBlockLength:].cold.1
+ -[FSServiceUserClient writeMetaSubBlock:offset:length:subBlockBuffer:subBlockOffset:subBlockLength:].cold.2
+ -[FSServiceUserClient writeMetaSubBlock:offset:length:subBlockBuffer:subBlockOffset:subBlockLength:].cold.3
+ -[FSSharedMutableBuffer .cxx_destruct]
+ -[FSSharedMutableBuffer bytes]
+ -[FSSharedMutableBuffer capacity]
+ -[FSSharedMutableBuffer classForCoder]
+ -[FSSharedMutableBuffer createDispatchData]
+ -[FSSharedMutableBuffer createMappingAt:options:startingAtOffset:forLength:completionHandler:]
+ -[FSSharedMutableBuffer createMappingForVMAAt:options:startingAtOffset:forLength:completionHandler:]
+ -[FSSharedMutableBuffer dealloc]
+ -[FSSharedMutableBuffer dealloc].cold.1
+ -[FSSharedMutableBuffer detachBytes]
+ -[FSSharedMutableBuffer detachBytes].cold.1
+ -[FSSharedMutableBuffer encodeWithCoder:]
+ -[FSSharedMutableBuffer ensureMappedIOMD]
+ -[FSSharedMutableBuffer ensureMappedMB:]
+ -[FSSharedMutableBuffer ensureMappedMB:].cold.1
+ -[FSSharedMutableBuffer ensureMapped]
+ -[FSSharedMutableBuffer initWithCapacity:]
+ -[FSSharedMutableBuffer initWithCapacity:andLength:]
+ -[FSSharedMutableBuffer initWithCapacity:andLength:].cold.1
+ -[FSSharedMutableBuffer initWithCapacity:andLength:].cold.2
+ -[FSSharedMutableBuffer initWithCapacity:andLength:].cold.3
+ -[FSSharedMutableBuffer initWithCoder:]
+ -[FSSharedMutableBuffer initWithCoder:].cold.1
+ -[FSSharedMutableBuffer initWithCoder:].cold.2
+ -[FSSharedMutableBuffer initWithLength:]
+ -[FSSharedMutableBuffer initWithMachPort:capacity:length:wrapsIOWMD:]
+ -[FSSharedMutableBuffer isIOWMD]
+ -[FSSharedMutableBuffer length]
+ -[FSSharedMutableBuffer memMap]
+ -[FSSharedMutableBuffer mp]
+ -[FSSharedMutableBuffer mutableBytes]
+ -[FSSharedMutableBuffer setCapacity:]
+ -[FSSharedMutableBuffer setIsIOWMD:]
+ -[FSSharedMutableBuffer setLength:]
+ -[FSSharedMutableBuffer setMemMap:]
+ -[FSSharedMutableBuffer setMp:]
+ -[FSSharedMutableBuffer setVma:]
+ -[FSSharedMutableBuffer vma]
+ -[FSTaskOptionsBundle initWithOptionString:count:optionDictionary:operationType:errorHandler:]
+ -[FSTaskOptionsBundle parseAndValidateActivateOptions:activationSyntax:]
+ -[FSTaskOptionsBundle parseAndValidateActivateOptions:activationSyntax:].cold.1
+ -[FSTaskOptionsBundle parseAndValidateActivateOptions:activationSyntax:].cold.2
+ -[FSUserClient callStructMethod:inStruct:inSize:outStruct:outStructSize:]
+ -[FSUserClient checkUserClientPort]
+ -[FSUserClient configureUserClient:pid:pidversion:supportBlockResource:]
+ -[FSUserClient configureUserClient:pid:pidversion:supportBlockResource:].cold.1
+ -[FSUserClient dealloc]
+ -[FSUserClient getConnPort]
+ -[FSUserClient getUserClientPortForService:]
+ -[FSUserClient getUserClientPort]
+ -[FSUserClient init]
+ -[FSUserClient setMainMachPort:forDomain:]
+ -[FSVolumeConnector setVolumeRequestedMountOptions:]
+ -[FSVolumeConnector volumeRequestedMountOptions]
+ GCC_except_table26
+ GCC_except_table29
+ GCC_except_table37
+ GCC_except_table56
+ GCC_except_table71
+ GCC_except_table89
+ GCC_except_table92
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _IOConnectCallStructMethod
+ _IOConnectSetNotificationPort
+ _IOServiceClose
+ _IOServiceMatching
+ _IOServiceOpen
+ _OBJC_CLASS_$_FSActivationOption
+ _OBJC_CLASS_$_FSActivationOptionSyntax
+ _OBJC_CLASS_$_FSMachPort
+ _OBJC_CLASS_$_FSMemoryMap
+ _OBJC_CLASS_$_FSServiceUserClient
+ _OBJC_CLASS_$_FSSharedMutableBuffer
+ _OBJC_CLASS_$_FSUserClient
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_IVAR_$_FSActivationOption._argumentType
+ _OBJC_IVAR_$_FSActivationOption._defaultValue
+ _OBJC_IVAR_$_FSActivationOption._name
+ _OBJC_IVAR_$_FSActivationOptionSyntax._options
+ _OBJC_IVAR_$_FSBlockDeviceResource._isSSD
+ _OBJC_IVAR_$_FSMachPort._machPort
+ _OBJC_IVAR_$_FSMemoryMap._address
+ _OBJC_IVAR_$_FSMemoryMap._port
+ _OBJC_IVAR_$_FSMemoryMap._size
+ _OBJC_IVAR_$_FSServiceUserClient.volumePort
+ _OBJC_IVAR_$_FSSharedMutableBuffer._capacity
+ _OBJC_IVAR_$_FSSharedMutableBuffer._isIOWMD
+ _OBJC_IVAR_$_FSSharedMutableBuffer._length
+ _OBJC_IVAR_$_FSSharedMutableBuffer._memMap
+ _OBJC_IVAR_$_FSSharedMutableBuffer._mp
+ _OBJC_IVAR_$_FSSharedMutableBuffer._vma
+ _OBJC_IVAR_$_FSUserClient.ourPort
+ _OBJC_IVAR_$_FSVolumeConnector._volumeRequestedMountOptions
+ _OBJC_METACLASS_$_FSActivationOption
+ _OBJC_METACLASS_$_FSActivationOptionSyntax
+ _OBJC_METACLASS_$_FSMachPort
+ _OBJC_METACLASS_$_FSMemoryMap
+ _OBJC_METACLASS_$_FSServiceUserClient
+ _OBJC_METACLASS_$_FSSharedMutableBuffer
+ _OBJC_METACLASS_$_FSUserClient
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _SecTaskCreateFromSelf
+ __OBJC_$_CLASS_METHODS_FSActivationOption
+ __OBJC_$_CLASS_METHODS_FSActivationOptionSyntax
+ __OBJC_$_CLASS_METHODS_FSMachPort
+ __OBJC_$_CLASS_METHODS_FSMemoryMap
+ __OBJC_$_CLASS_METHODS_FSSharedMutableBuffer
+ __OBJC_$_CLASS_METHODS_FSUserClient
+ __OBJC_$_CLASS_PROP_LIST_FSMachPort
+ __OBJC_$_CLASS_PROP_LIST_FSSharedMutableBuffer
+ __OBJC_$_INSTANCE_METHODS_FSActivationOption
+ __OBJC_$_INSTANCE_METHODS_FSActivationOptionSyntax
+ __OBJC_$_INSTANCE_METHODS_FSMachPort
+ __OBJC_$_INSTANCE_METHODS_FSMemoryMap
+ __OBJC_$_INSTANCE_METHODS_FSServiceUserClient
+ __OBJC_$_INSTANCE_METHODS_FSSharedMutableBuffer
+ __OBJC_$_INSTANCE_METHODS_FSUserClient
+ __OBJC_$_INSTANCE_VARIABLES_FSActivationOption
+ __OBJC_$_INSTANCE_VARIABLES_FSActivationOptionSyntax
+ __OBJC_$_INSTANCE_VARIABLES_FSMachPort
+ __OBJC_$_INSTANCE_VARIABLES_FSMemoryMap
+ __OBJC_$_INSTANCE_VARIABLES_FSServiceUserClient
+ __OBJC_$_INSTANCE_VARIABLES_FSSharedMutableBuffer
+ __OBJC_$_INSTANCE_VARIABLES_FSUserClient
+ __OBJC_$_PROP_LIST_FSActivationOption
+ __OBJC_$_PROP_LIST_FSActivationOptionSyntax
+ __OBJC_$_PROP_LIST_FSMachPort
+ __OBJC_$_PROP_LIST_FSMemoryMap
+ __OBJC_$_PROP_LIST_FSSharedMutableBuffer
+ __OBJC_CLASS_PROTOCOLS_$_FSMachPort
+ __OBJC_CLASS_PROTOCOLS_$_FSSharedMutableBuffer
+ __OBJC_CLASS_RO_$_FSActivationOption
+ __OBJC_CLASS_RO_$_FSActivationOptionSyntax
+ __OBJC_CLASS_RO_$_FSMachPort
+ __OBJC_CLASS_RO_$_FSMemoryMap
+ __OBJC_CLASS_RO_$_FSServiceUserClient
+ __OBJC_CLASS_RO_$_FSSharedMutableBuffer
+ __OBJC_CLASS_RO_$_FSUserClient
+ __OBJC_METACLASS_RO_$_FSActivationOption
+ __OBJC_METACLASS_RO_$_FSActivationOptionSyntax
+ __OBJC_METACLASS_RO_$_FSMachPort
+ __OBJC_METACLASS_RO_$_FSMemoryMap
+ __OBJC_METACLASS_RO_$_FSServiceUserClient
+ __OBJC_METACLASS_RO_$_FSSharedMutableBuffer
+ __OBJC_METACLASS_RO_$_FSUserClient
+ ___106-[FSVolumeConnector renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:requestID:replyHandler:]_block_invoke.429
+ ___31-[FSBlockDeviceResource revoke]_block_invoke.80
+ ___31-[FSBlockDeviceResource revoke]_block_invoke.80.cold.1
+ ___34-[FSClient(Project) currentTasks:]_block_invoke
+ ___38-[FSClient(Project) currentTasksSync:]_block_invoke
+ ___39-[FSClient(Project) currentContainers:]_block_invoke
+ ___40-[FSClient(Project) currentResourceIDs:]_block_invoke
+ ___40-[FSClient(Project) currentResourceIDs:]_block_invoke_2
+ ___41-[FSSharedMutableBuffer ensureMappedIOMD]_block_invoke
+ ___43-[FSClient(Project) currentContainersSync:]_block_invoke
+ ___43-[FSSharedMutableBuffer createDispatchData]_block_invoke
+ ___44-[FSClient(Project) currentResourceIDsSync:]_block_invoke
+ ___44-[FSClient(Project) currentResourceIDsSync:]_block_invoke_2
+ ___46-[FSModuleHost(Project) extensionPointRecords]_block_invoke.148
+ ___73-[FSModuleHost(Project) _updateProviderListForFilteredFSModuleInstances:]_block_invoke.186
+ ___73-[FSModuleHost(Project) _updateProviderListForFilteredFSModuleInstances:]_block_invoke_2.188
+ ___74-[FSClient(Private) validateVolumeName:usingBundle:volumeID:replyHandler:]_block_invoke.90
+ ___78-[FSClient(Private) installedExtensionWithShortName:synchronous:replyHandler:]_block_invoke.58
+ ___78-[FSClient(Private) installedExtensionWithShortName:synchronous:replyHandler:]_block_invoke.58.cold.1
+ ___78-[FSClient(Private) installedExtensionWithShortName:synchronous:replyHandler:]_block_invoke_3.cold.1
+ ___83+[FSBlockDeviceResource(Project) openWithBSDName:writable:auditToken:replyHandler:]_block_invoke.216
+ ___83+[FSBlockDeviceResource(Project) openWithBSDName:writable:auditToken:replyHandler:]_block_invoke.216.cold.1
+ ___96-[FSVolumeConnector makeCloneOf:named:inDirectory:attributes:usingFlags:requestID:replyHandler:]_block_invoke.424
+ ___block_descriptor_32_e32_16?0"LSExtensionPointRecord"8l
+ ___block_descriptor_40_e8_32bs_e38_v24?0"FSItemAttributes"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e8_32bs40r_e38_v24?0"FSItemAttributes"8"NSError"16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e24_v20?0i8"FSMemoryMap"12lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e29_v24?0"NSArray"8"NSError"16lr40l8s32l8
+ ___block_literal_global.158
+ ___block_literal_global.180
+ ___block_literal_global.182
+ ___block_literal_global.313
+ ___block_literal_global.80
+ ___strlcpy_chk
+ __nextAttributeSeqno
+ __os_log_default
+ _dispatch_data_create
+ _gDefaultClient
+ _mach_port_mod_refs
+ _objc_msgSend$FSClientXPCProtocol
+ _objc_msgSend$_setInhibitKernelOffloadedIO:
+ _objc_msgSend$address
+ _objc_msgSend$allOptionNames:
+ _objc_msgSend$argTypeFromDictionary:
+ _objc_msgSend$argumentType
+ _objc_msgSend$callStructMethod:inStruct:inSize:outStruct:outStructSize:
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$checkUserClientPort
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$createMappingAt:options:startingAtOffset:forLength:completionHandler:
+ _objc_msgSend$createMappingForVMAAt:options:startingAtOffset:forLength:completionHandler:
+ _objc_msgSend$createVolumePort
+ _objc_msgSend$delayedMetadataWriteFrom:startingAt:length:error:
+ _objc_msgSend$ensureMappedIOMD
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$fskitdMachServiceName
+ _objc_msgSend$getConnPort
+ _objc_msgSend$getFSAttributes:
+ _objc_msgSend$getUserClientPort
+ _objc_msgSend$getUserClientPortForService:
+ _objc_msgSend$hasEntitlement
+ _objc_msgSend$initWithAttributeData:
+ _objc_msgSend$initWithFSAttributes:
+ _objc_msgSend$initWithMachPort:capacity:length:wrapsIOWMD:
+ _objc_msgSend$initWithOptionString:count:optionDictionary:operationType:errorHandler:
+ _objc_msgSend$initWithOptions:
+ _objc_msgSend$initWithPort:
+ _objc_msgSend$initWithPort:address:andSize:
+ _objc_msgSend$initWithWantedFSAttributes:
+ _objc_msgSend$isSSD
+ _objc_msgSend$metadataReadInto:startingAt:length:error:
+ _objc_msgSend$metadataWriteFrom:startingAt:length:error:
+ _objc_msgSend$moduleExtensionForAppex:
+ _objc_msgSend$newWithPort:address:andSize:
+ _objc_msgSend$optionWithName:
+ _objc_msgSend$optionWithName:argumentType:defaultValue:
+ _objc_msgSend$parseAndValidateActivateOptions:activationSyntax:
+ _objc_msgSend$parseOptionFromData:
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$readInto:startingAt:length:completionHandler:
+ _objc_msgSend$requestWithFSAttributes:
+ _objc_msgSend$requestedMountOptions
+ _objc_msgSend$sequenceNumber
+ _objc_msgSend$set
+ _objc_msgSend$setArgumentType:
+ _objc_msgSend$setDefaultValue:
+ _objc_msgSend$setOptions:
+ _objc_msgSend$setSequenceNumberIfNeeded
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$stringForOption:inOptions:
+ _objc_msgSend$stringFromDictionary:key:
+ _objc_msgSend$systemMountOptions
+ _objc_msgSend$validateOptions:
+ _objc_msgSend$whitespaceCharacterSet
+ _objc_msgSend$withMutableBytes:
+ _objc_msgSend$writeFrom:startingAt:length:completionHandler:
+ _objc_msgSend$writeFrom:startingAt:length:error:
- +[FSItemAttributes requestWithLIAttributes:]
- +[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]
- +[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:].cold.1
- +[FSKitDiskArbHelper DAMountUserFSVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]
- +[FSKitDiskArbHelper DAMountUserFSVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:].cold.1
- +[FSKitDiskArbHelper DAMountUserFSVolume:deviceName:mountPoint:volumeName:mountOptions:]
- +[FSKitDiskArbHelper getFileProviderID]
- +[FSKitDiskArbHelper waitForPreviousTasksToComplete:client:]
- +[stolenUSBLocalStorageClient newManager]
- -[FSClient setupConnection].cold.2
- -[FSClient(Private) currentContainers:]
- -[FSClient(Private) currentContainersSync:]
- -[FSClient(Private) currentResourceIDs:]
- -[FSClient(Private) currentResourceIDsSync:]
- -[FSClient(Private) currentTasks:]
- -[FSClient(Private) currentTasksSync:]
- -[FSClient(Private) installedExtensionWithBundleID:synchronous:replyHandler:]
- -[FSItemAttributes getLIAttributes:]
- -[FSItemAttributes initWithLIAttributes:]
- -[FSItemAttributes setAttributeSeqno:]
- -[FSItemGetAttributesRequest initWithWantedLIAttributes:]
- -[FSModuleExtension(Project) fskitdIsClient:]
- -[FSModuleExtension(Project) fskitdIsClient:].cold.1
- -[FSTaskMessageSTDIOWithProgress drawTwiddleBar]
- -[FSTaskOptionsBundle initWithOptionString:count:optionDictionary:errorHandler:]
- -[stolenUSBLocalStorageClient loadVolumes:ofType:withError:]
- -[stolenUSBLocalStorageClient loadVolumes:ofType:withError:].cold.1
- GCC_except_table105
- GCC_except_table109
- GCC_except_table28
- GCC_except_table4
- GCC_except_table55
- GCC_except_table60
- GCC_except_table79
- GCC_except_table80
- GCC_except_table82
- GCC_except_table88
- OBJC_IVAR_$_LiveFSClient.conn
- _NSLog
- _OBJC_CLASS_$_FSKitDiskArbHelper
- _OBJC_CLASS_$_LiveFSClient
- _OBJC_CLASS_$_LiveFSMachPort
- _OBJC_CLASS_$_LiveFSMountClient
- _OBJC_CLASS_$_LiveFSServiceUserClient
- _OBJC_CLASS_$_stolenUSBLocalStorageClient
- _OBJC_IVAR_$_FSVolumeConnector._nextAttributeSeqno
- _OBJC_METACLASS_$_FSKitDiskArbHelper
- _OBJC_METACLASS_$_LiveFSClient
- _OBJC_METACLASS_$_stolenUSBLocalStorageClient
- __OBJC_$_CLASS_METHODS_FSKitDiskArbHelper
- __OBJC_$_CLASS_METHODS_stolenUSBLocalStorageClient
- __OBJC_$_INSTANCE_METHODS_stolenUSBLocalStorageClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LiveFSMounter
- __OBJC_$_PROTOCOL_METHOD_TYPES_LiveFSMounter
- __OBJC_CLASS_RO_$_FSKitDiskArbHelper
- __OBJC_CLASS_RO_$_stolenUSBLocalStorageClient
- __OBJC_LABEL_PROTOCOL_$_LiveFSMounter
- __OBJC_METACLASS_RO_$_FSKitDiskArbHelper
- __OBJC_METACLASS_RO_$_stolenUSBLocalStorageClient
- __OBJC_PROTOCOL_$_LiveFSMounter
- __OBJC_PROTOCOL_REFERENCE_$_LiveFSMounter
- ___106-[FSVolumeConnector renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:requestID:replyHandler:]_block_invoke.427
- ___27-[FSClient setupConnection]_block_invoke
- ___27-[FSClient setupConnection]_block_invoke_2
- ___31-[FSBlockDeviceResource revoke]_block_invoke.77
- ___31-[FSBlockDeviceResource revoke]_block_invoke.77.cold.1
- ___34-[FSClient(Private) currentTasks:]_block_invoke
- ___38-[FSClient(Private) currentTasksSync:]_block_invoke
- ___39-[FSClient(Private) currentContainers:]_block_invoke
- ___40-[FSClient(Private) currentResourceIDs:]_block_invoke
- ___40-[FSClient(Private) currentResourceIDs:]_block_invoke_2
- ___43-[FSClient(Private) currentContainersSync:]_block_invoke
- ___44-[FSClient(Private) currentResourceIDsSync:]_block_invoke
- ___44-[FSClient(Private) currentResourceIDsSync:]_block_invoke_2
- ___60+[FSKitDiskArbHelper waitForPreviousTasksToComplete:client:]_block_invoke
- ___60+[FSKitDiskArbHelper waitForPreviousTasksToComplete:client:]_block_invoke_2
- ___60+[FSKitDiskArbHelper waitForPreviousTasksToComplete:client:]_block_invoke_3
- ___60+[FSKitDiskArbHelper waitForPreviousTasksToComplete:client:]_block_invoke_4
- ___60+[FSKitDiskArbHelper waitForPreviousTasksToComplete:client:]_block_invoke_5
- ___60+[FSKitDiskArbHelper waitForPreviousTasksToComplete:client:]_block_invoke_6
- ___60-[stolenUSBLocalStorageClient loadVolumes:ofType:withError:]_block_invoke
- ___60-[stolenUSBLocalStorageClient loadVolumes:ofType:withError:]_block_invoke_2
- ___73-[FSModuleHost(Project) _updateProviderListForFilteredFSModuleInstances:]_block_invoke.179
- ___73-[FSModuleHost(Project) _updateProviderListForFilteredFSModuleInstances:]_block_invoke_2.181
- ___77-[FSClient(Private) installedExtensionWithBundleID:synchronous:replyHandler:]_block_invoke
- ___77-[FSClient(Private) installedExtensionWithBundleID:synchronous:replyHandler:]_block_invoke_2
- ___77-[FSClient(Private) installedExtensionWithBundleID:synchronous:replyHandler:]_block_invoke_3
- ___83+[FSBlockDeviceResource(Project) openWithBSDName:writable:auditToken:replyHandler:]_block_invoke.209
- ___83+[FSBlockDeviceResource(Project) openWithBSDName:writable:auditToken:replyHandler:]_block_invoke.209.cold.1
- ___96-[FSVolumeConnector makeCloneOf:named:inDirectory:attributes:usingFlags:requestID:replyHandler:]_block_invoke.422
- ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke
- ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.24
- ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.24.cold.1
- ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.24.cold.2
- ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.24.cold.3
- ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.29
- ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.29.cold.1
- ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.29.cold.2
- ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.30
- ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.30.cold.1
- ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.30.cold.2
- ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.32
- ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.32.cold.1
- ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.cold.1
- ___block_descriptor_148_e8_32s40s48s56s64s72s80s88s96r104r_e36_v32?0"FSVolumeDescription"8Q16^B24ls32l8s40l8s48l8r96l8s56l8s64l8s72l8s80l8s88l8r104l8
- ___block_descriptor_40_e8_32bs_e38_v24?0"FSModuleIdentity"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32r_e38_v24?0"FSModuleIdentity"8"NSError"16lr32l8
- ___block_descriptor_48_e8_32r40r_e29_v24?0"NSError"8"NSArray"16lr32l8r40l8
- ___block_descriptor_48_e8_32s40bs_e38_v24?0"FSItemAttributes"8"NSError"16ls40l8s32l8
- ___block_descriptor_48_e8_32s40r_e34_v32?0"FSTaskDescription"8Q16^B24ls32l8r40l8
- ___block_descriptor_56_e8_32s40bs48r_e38_v24?0"FSItemAttributes"8"NSError"16ls40l8s32l8r48l8
- ___block_descriptor_56_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48r56r_e39_v24?0"FSTaskDescription"8"NSError"16ls32l8r48l8r56l8s40l8
- ___block_literal_global.173
- ___block_literal_global.175
- ___block_literal_global.309
- ___block_literal_global.78
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:
- _objc_msgSend$DAMountUserFSVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:
- _objc_msgSend$addDisk:fileSystemType:reply:
- _objc_msgSend$audit_token
- _objc_msgSend$currentTasksSync:
- _objc_msgSend$forgetVolume:withFlags:
- _objc_msgSend$getFileProviderID
- _objc_msgSend$getLIAttributes:
- _objc_msgSend$initWithLIAttributes:
- _objc_msgSend$initWithOptionString:count:optionDictionary:errorHandler:
- _objc_msgSend$initWithWantedLIAttributes:
- _objc_msgSend$installedExtensionWithBundleID:replyHandler:
- _objc_msgSend$installedExtensionWithBundleID:synchronous:replyHandler:
- _objc_msgSend$installedExtensionWithShortName:replyHandler:
- _objc_msgSend$isIndeterminate
- _objc_msgSend$loadVolumes:ofType:withError:
- _objc_msgSend$mountVolume:fileSystem:displayName:provider:domainError:on:how:options:auditToken:
- _objc_msgSend$newClientForProvider:
- _objc_msgSend$newConnectionForService:
- _objc_msgSend$newManager
- _objc_msgSend$requestWithLIAttributes:
- _objc_msgSend$secureResourceWithURL:readonly:
- _objc_msgSend$setAttributeSeqno:
- _objc_msgSend$setInhibitKernelOffloadedIO:
- _objc_msgSend$setTaskUpdateHandler:replyHandler:
- _objc_msgSend$switchToFSKit:
- _objc_msgSend$taskResource
- _objc_msgSend$token
- _objc_msgSend$volumeName
- _objc_msgSend$waitForPreviousTasksToComplete:client:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
CStrings:
+ "%@=%@"
+ "%s: Couldn't create a new XPC connection to fskitd using %@"
+ "%s: Found extension with fsShortName (%@)"
+ "%s: Mount option validation failed: %@"
+ "%s: Negated option: no%@"
+ "%s: No extension with fsShortName (%@) found."
+ "%s: Option '%@' does not accept arguments"
+ "%s: Option '%@' requires an argument"
+ "%s: Parsed mount option: %@ (flag)"
+ "%s: Parsed mount option: %@ = %@"
+ "%s: Parsing mount options: %@"
+ "%s: Unknown option: %@"
+ "%s: default client of isn't from type FSServiceUserClient"
+ "%s: invalid argument given"
+ "%s: invalid subblock range"
+ "%s: invalidate our NSXPCListener (%p)"
+ "%s:start:theItem:%@:access:%lu:reqID:%llu"
+ "+[FSModuleExtension(Project) fskitdIsClient:]"
+ ","
+ "-[FSActivationOptionSyntax validateOptions:]"
+ "-[FSClient(Private) installedExtensionWithShortName:synchronous:replyHandler:]_block_invoke"
+ "-[FSMachPort initWithCoder:]"
+ "-[FSMessageReceiver dealloc]"
+ "-[FSServiceUserClient clearMetaBlocks:ranges:rangesCount:wait:]"
+ "-[FSServiceUserClient flushMeta:wait:]"
+ "-[FSServiceUserClient purgeMetaBlocks:ranges:rangesCount:]"
+ "-[FSServiceUserClient readMeta:buffer:offset:length:]"
+ "-[FSServiceUserClient readMetaWithRA:buffer:offset:length:raList:raListCount:]"
+ "-[FSServiceUserClient writeMeta:buffer:offset:length:]"
+ "-[FSServiceUserClient writeMetaDelayed:buffer:offset:length:]"
+ "-[FSServiceUserClient writeMetaSubBlock:offset:length:subBlockBuffer:subBlockOffset:subBlockLength:]"
+ "-[FSSharedMutableBuffer ensureMappedMB:]"
+ "-[FSSharedMutableBuffer initWithCapacity:andLength:]"
+ "-[FSSharedMutableBuffer initWithCoder:]"
+ "-[FSTaskOptionsBundle parseAndValidateActivateOptions:activationSyntax:]"
+ "="
+ "@\"FSMachPort\""
+ "@\"FSMemoryMap\""
+ "@\"FSSharedMutableBuffer\""
+ "@16@?0@\"LSExtensionPointRecord\"8"
+ "@24@0:8r^{_FSFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}16"
+ "@36@0:8I16Q20Q28"
+ "@40@0:8@16q24@32"
+ "@40@0:8I16Q20Q28B36"
+ "Didn't find matching client"
+ "FSActivationOption"
+ "FSActivationOptionSyntax"
+ "FSClient setting up %@ connection to fskitd"
+ "FSMachPort"
+ "FSMachPort: dealloc: error %d"
+ "FSMemoryMap"
+ "FSMemoryMap: dealloc: error %d"
+ "FSOptionArgumentTypeBoolean"
+ "FSOptionArgumentTypeHasArg"
+ "FSOptionArgumentTypeNoArg"
+ "FSResource.isSSD"
+ "FSSMBuff.cap"
+ "FSSMBuff.isIOWMD"
+ "FSSMBuff.len"
+ "FSSMBuff.mp"
+ "FSServiceUserClient"
+ "FSSharedMutableBuffer"
+ "FSSharedMutableBuffer: dealloc: error %d"
+ "FSUserClient"
+ "FSmp.mp"
+ "Instance %p ID '%@' UUID %@"
+ "LSExtensionPointRecord %p identifier '%@' name %@"
+ "No matching dict"
+ "T@\"FSMachPort\",&,V_fsMachPort"
+ "T@\"FSMemoryMap\",&,V_memMap"
+ "T@\"FSSharedMutableBuffer\",&,V_proxyOfBuffer"
+ "T@\"NSArray\",&,V_options"
+ "T@\"NSArray\",C,V_moduleOrder"
+ "T@\"NSString\",&,V_defaultValue"
+ "T@\"NSString\",&,V_name"
+ "T@\"NSString\",R,&"
+ "TB,R,V_isSSD"
+ "TB,V_isIOWMD"
+ "TI,R,V_machPort"
+ "TI,V_mp"
+ "TI,V_port"
+ "TQ"
+ "TQ,R,V_address"
+ "TQ,R,V_size"
+ "TQ,V_capacity"
+ "TQ,V_vma"
+ "TQ,V_volumeRequestedMountOptions"
+ "Tq,V_argumentType"
+ "_address"
+ "_argumentType"
+ "_capacity"
+ "_defaultValue"
+ "_isIOWMD"
+ "_isSSD"
+ "_machPort"
+ "_memMap"
+ "_setInhibitKernelOffloadedIO:"
+ "_volumeRequestedMountOptions"
+ "actimeo"
+ "address"
+ "allOptionNames:"
+ "argTypeFromDictionary:"
+ "argumentType"
+ "async"
+ "bufferWithCapacity:"
+ "bufferWithLength:"
+ "callStructMethod:inStruct:inSize:outStruct:outStructSize:"
+ "caseInsensitiveCompare:"
+ "checkUserClientPort"
+ "clear_meta_blocks returned %d"
+ "close_kernel_fd returned %d"
+ "com.apple.filesystems.fskitd.livefs"
+ "com.apple.private.LiveFS.connection"
+ "com_apple_filesystems_lifs"
+ "componentsSeparatedByString:"
+ "configureUserClient returned %d"
+ "configureUserClient:pid:pidversion:supportBlockResource:"
+ "createDispatchData"
+ "createMappingAt:options:startingAtOffset:forLength:completionHandler:"
+ "createMappingForVMAAt:options:startingAtOffset:forLength:completionHandler:"
+ "createVolumePort"
+ "create_volume_port returned %d"
+ "dashOOptions"
+ "defaultValue"
+ "detachBytes"
+ "detatchBytes called on FSSharedMutableBuffer wrapping an IOMD, which won't work well"
+ "dev"
+ "dsize"
+ "ensureMappedIOMD"
+ "exec"
+ "fileURLWithPath:isDirectory:"
+ "flush_meta returned %d"
+ "fsShortName"
+ "fskitdLiveFSMachServiceName"
+ "fskitdMachServiceName"
+ "get client returned %x"
+ "getConnPort"
+ "getFSAttributes:"
+ "getUserClientPort"
+ "getUserClientPortForService:"
+ "hasEntitlement"
+ "i20@0:8i16"
+ "i24@0:8i16i20"
+ "i28@0:8I16@20"
+ "i32@0:8I16i20i24i28"
+ "i32@0:8i16^{FSKit_Meta_BlockRange_s=qII}20i28"
+ "i36@0:8i16^{FSKit_Meta_BlockRange_s=qII}20i28i32"
+ "i44@0:8i16^v20q28Q36"
+ "i44@0:8i16r^v20q28Q36"
+ "i52@0:8I16r^v20Q28^v36^Q44"
+ "i56@0:8i16^v20q28Q36^{FSKit_Meta_Readahead_s=qQ}44i52"
+ "i60@0:8i16q20Q28r^v36q44Q52"
+ "initWithAttributeData:"
+ "initWithFSAttributes:"
+ "initWithMachPort:capacity:length:wrapsIOWMD:"
+ "initWithOptionString:count:optionDictionary:operationType:errorHandler:"
+ "initWithPort:"
+ "initWithPort:address:andSize:"
+ "initWithWantedFSAttributes:"
+ "isIOWMD"
+ "isSSD"
+ "locallocks"
+ "machPortForKernelMountUse"
+ "mach_port_mod_refs failed, returned %d"
+ "memMap"
+ "newWithPort:address:andSize:"
+ "no"
+ "open_kernel_fd returned %d"
+ "optionWithName:"
+ "optionWithName:argumentType:defaultValue:"
+ "ourPort"
+ "parseAndValidateActivateOptions:activationSyntax:"
+ "parseOptionFromData:"
+ "privileged"
+ "purge_meta_blocks returned %d"
+ "quota"
+ "r^v16@0:8"
+ "rangeOfString:"
+ "read_meta returned %d"
+ "read_meta_with_ra returned %d"
+ "readahead"
+ "requestWithFSAttributes:"
+ "requestedMountOptions"
+ "ro"
+ "rsize"
+ "rw"
+ "sequenceNumber"
+ "set"
+ "set client domain returned %x"
+ "set notification port returned %x"
+ "setArgumentType:"
+ "setCapacity:"
+ "setDefaultValue:"
+ "setIsIOWMD:"
+ "setLength:"
+ "setMainMachPort:forDomain:"
+ "setMemMap:"
+ "setMp:"
+ "setSequenceNumberIfNeeded"
+ "setVma:"
+ "setVolumeRequestedMountOptions:"
+ "strictatime"
+ "stringByTrimmingCharactersInSet:"
+ "stringForOption:inOptions:"
+ "stringFromDictionary:key:"
+ "suid"
+ "sync"
+ "systemMountOptions"
+ "union"
+ "v20@?0i8@\"FSMemoryMap\"12"
+ "v24@0:8^{_FSFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}16"
+ "v32@0:8@\"FSMachPort\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"NSString\"16Q24@?<v@?i@\"FSMachPort\">32"
+ "v52@0:8Q16I24Q28Q36@?44"
+ "validateOptions:"
+ "volumePort"
+ "volumeRequestedMountOptions"
+ "whitespaceCharacterSet"
+ "writeMetaSubBlock:offset:length:subBlockBuffer:subBlockOffset:subBlockLength:"
+ "write_meta returned %d"
+ "write_meta_delayed returned %d"
+ "write_meta_subblock returned %d"
+ "wsize"
+ "{_FSFileAttributes=\"__fa_rsvd0\"Q\"fa_validmask\"Q\"fa_seqno\"Q\"fa_type\"I\"fa_mode\"I\"fa_nlink\"I\"fa_uid\"I\"fa_gid\"I\"fa_bsd_flags\"I\"fa_size\"Q\"fa_allocsize\"Q\"fa_fileid\"Q\"fa_parentid\"Q\"fa_atime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_mtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_ctime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_birthtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_backuptime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_addedtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_int_flags\"I\"_pad0\"I}"
- "%@ loadVolumes failed with %@"
- "%@ mount failed with %@"
- "%@ mounting with name %@, error %@, and how 0x%x."
- "%@: got 2 different names from probe and userfs: p->%@  u->%@"
- "%s: %@ failed to activate volume (%@)"
- "%s: %@ failed to deactivateVolume (%@) error (%@)"
- "%s: %@ failed to load resource (%@)"
- "%s: %@ failed to unloadResource (%@) error (%@)"
- "%s: %@ mount failed with %@"
- "%s: Activating volumeName (%@) volumeID (%@) with activateOptions (%@)"
- "%s: Couldn't create a new XPC connection to com.apple.filesystems.fskitd"
- "%s: Mounted %@ successfully."
- "%s: default client of isn't from type LiveFSServiceUserClient"
- "%s:done activating volume (%@)"
- "%s:done deactivating volume (%@)"
- "%s:finish:%@:%@:%@"
- "%s:start:%@:%@"
- "%s:start:fsShortName(%@):deviceName(%@):mountPoint(%@):volumeName(%@):mountOptionString(%@)"
- "%s:start:theItem:%@:access:%ld:reqID:%llu"
- "+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]"
- "+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke"
- "-[FSModuleExtension(Project) fskitdIsClient:]"
- "-[stolenUSBLocalStorageClient loadVolumes:ofType:withError:]"
- "@\"LiveFSMachPort\""
- "@\"LiveFSSharedMutableBuffer\""
- "@24@0:8r^{_LIFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}16"
- "DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:"
- "DAMountUserFSVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:"
- "DAMountUserFSVolume:deviceName:mountPoint:volumeName:mountOptions:"
- "Error connecting to fskitd: %@"
- "Error setting up update handler: '%s'"
- "FSClient setting up connection to fskitd"
- "FSKitDiskArbHelper"
- "LiveFSMounter"
- "Mod %p ID '%@' UUID %@"
- "Mounted %@ successfully."
- "Setting remote protocol to all XPC"
- "T@\"LiveFSMachPort\",&,V_fsMachPort"
- "T@\"LiveFSSharedMutableBuffer\",&,V_proxyOfBuffer"
- "T@\"NSArray\",&,V_moduleOrder"
- "Untitled"
- "_"
- "_fskit"
- "_nextAttributeSeqno"
- "addDisk:fileSystemType:reply:"
- "com.apple.filesystems.UserFS.FileProvider"
- "drawTwiddleBar"
- "errorForDomain"
- "forgetVolume:withFlags:"
- "getFileProviderID"
- "getLIAttributes:"
- "how"
- "i56@0:8@16@24@32@40@48"
- "i88@0:8@16@24@32@40{?=[8I]}48@80"
- "initWithLIAttributes:"
- "initWithOptionString:count:optionDictionary:errorHandler:"
- "initWithWantedLIAttributes:"
- "installedExtensionWithBundleID:replyHandler:"
- "installedExtensionWithBundleID:synchronous:replyHandler:"
- "installedExtensionWithShortName:replyHandler:"
- "isIndeterminate"
- "listMounts:reply:"
- "loadVolumes:ofType:withError:"
- "machp://com.apple.filesystems.localLiveFiles"
- "mountVolume:displayName:provider:domainError:on:how:options:reply:"
- "mountVolume:displayName:provider:domainError:on:how:reply:"
- "mountVolume:fileSystem:displayName:provider:domainError:on:how:options:auditToken:"
- "mountVolume:fileSystem:displayName:provider:domainError:on:how:options:auditToken:reply:"
- "mountVolume:fileSystem:displayName:provider:domainError:on:how:options:reply:"
- "newClientForProvider:"
- "newConnectionForService:"
- "newManager"
- "o"
- "passthroughfs"
- "requestWithLIAttributes:"
- "setAttributeSeqno:"
- "setVerboseLevel:reply:"
- "stolenUSBLocalStorageClient"
- "switchToFSKit:"
- "unload for volume %@ failed with %@"
- "unmountVolume:how:reply:"
- "unmountVolume:provider:how:domainError:reply:"
- "unmountVolumeByID:how:reply:"
- "unsupported error code for domain: %ld"
- "updateErrorStateForVolume:provider:domainError:reply:"
- "v116@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48@\"NSString\"56i64@\"NSString\"68{?=[8I]}76@?<v@?@\"NSError\">108"
- "v116@0:8@16@24@32@40@48@56i64@68{?=[8I]}76@?108"
- "v24@0:8@?<v@?i>16"
- "v24@0:8^{_LIFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}16"
- "v24@?0@\"FSModuleIdentity\"8@\"NSError\"16"
- "v24@?0@\"FSTaskDescription\"8@\"NSError\"16"
- "v24@?0@\"NSError\"8@\"NSArray\"16"
- "v28@0:8B16@?<v@?@\"NSArray\">20"
- "v28@0:8i16@?20"
- "v28@0:8i16@?<v@?@\"NSError\">20"
- "v32@0:8@\"LiveFSMachPort\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"FSModuleIdentity\"@\"NSError\">24"
- "v32@0:8I16i20@?24"
- "v32@0:8I16i20@?<v@?@\"NSError\"@\"NSString\">24"
- "v32@?0@\"FSTaskDescription\"8Q16^B24"
- "v32@?0@\"FSVolumeDescription\"8Q16^B24"
- "v36@0:8@\"NSString\"16i24@?<v@?@\"NSError\"@\"NSString\">28"
- "v36@0:8@16i24@?28"
- "v40@0:8@\"NSString\"16Q24@?<v@?i@\"LiveFSMachPort\">32"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSError\"32@?<v@?@\"NSError\">40"
- "v52@0:8@\"NSString\"16@\"NSString\"24i32@\"NSError\"36@?<v@?@\"NSError\"@\"NSString\">44"
- "v68@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSError\"40@\"NSString\"48i56@?<v@?@\"NSError\">60"
- "v68@0:8@16@24@32@40@48i56@?60"
- "v76@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSError\"40@\"NSString\"48i56@\"NSString\"60@?<v@?@\"NSError\">68"
- "v76@0:8@16@24@32@40@48i56@60@?68"
- "v84@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48@\"NSString\"56i64@\"NSString\"68@?<v@?@\"NSError\">76"
- "v84@0:8@16@24@32@40@48@56i64@68@?76"
- "verboseLevel:"
- "waitForPreviousTasksToComplete:client:"
- "{_LIFileAttributes=\"__fa_rsvd0\"Q\"fa_validmask\"Q\"fa_seqno\"Q\"fa_type\"I\"fa_mode\"I\"fa_nlink\"I\"fa_uid\"I\"fa_gid\"I\"fa_bsd_flags\"I\"fa_size\"Q\"fa_allocsize\"Q\"fa_fileid\"Q\"fa_parentid\"Q\"fa_atime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_mtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_ctime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_birthtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_backuptime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_addedtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_int_flags\"I\"_pad0\"I}"
- "|/-\\"

```
