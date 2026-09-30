## ISPExclaveKitServices

> `/System/Library/PrivateFrameworks/ISPExclaveKitServices.framework/ISPExclaveKitServices`

```diff

-5.301.5.0.0
-  __TEXT.__text: 0x29328
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__const: 0x280
-  __TEXT.__gcc_except_tab: 0x6d4
-  __TEXT.__oslogstring: 0x2c87
-  __TEXT.__cstring: 0x49f0
-  __TEXT.__unwind_info: 0x730
+5.305.1.0.0
+  __TEXT.__text: 0x2b4a8
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__const: 0x2c0
+  __TEXT.__gcc_except_tab: 0x7cc
+  __TEXT.__oslogstring: 0x3092
+  __TEXT.__cstring: 0x4c72
+  __TEXT.__unwind_info: 0x7e0
   __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0xeb0
-  __AUTH_CONST.__auth_got: 0x378
+  __DATA_CONST.__const: 0xed8
+  __AUTH_CONST.__auth_got: 0x3a0
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x340
-  __DATA.__data: 0x1163b9
-  __DATA.__common: 0x18
+  __AUTH_CONST.__cfstring: 0x380
+  __DATA.__data: 0x1165e8
+  __DATA.__common: 0x20
+  __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: F8036678-CC40-312B-A18B-C5390A5548EC
-  Functions: 840
-  Symbols:   1967
-  CStrings:  540
+  UUID: C0EDD260-5E11-3CC6-A9E8-C0A20C326FB0
+  Functions: 890
+  Symbols:   2054
+  CStrings:  569
 
Symbols:
+ GCC_except_table15
+ GCC_except_table17
+ GCC_except_table24
+ GCC_except_table28
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table36
+ GCC_except_table40
+ GCC_except_table44
+ GCC_except_table48
+ __Z20_getEkBufferInternalP20sExclaveKitIspCmdHdrP28ISPExclaveKitFileDumpService26FileServiceBufferNameIndex
+ __Z20_getEkBufferInternalP20sExclaveKitIspCmdHdrP28ISPExclaveKitFileDumpService26FileServiceBufferNameIndex.cold.1
+ __Z20_getEkBufferInternalP20sExclaveKitIspCmdHdrP28ISPExclaveKitFileDumpService26FileServiceBufferNameIndex.cold.2
+ __Z20ispExclaveKitCommandP20sExclaveKitIspCmdHdr.cold.56
+ __Z20ispExclaveKitCommandP20sExclaveKitIspCmdHdr.cold.57
+ __Z22exclaveKitDefaultsInitP21ISPExclaveKitDefaults.cold.3
+ __Z22exclaveKitDefaultsInitP21ISPExclaveKitDefaults.cold.4
+ __Z30isNewSharedMemoryReplayEnabledP21ISPExclaveKitDefaults
+ __Z32ispExclavePrivatePropertiesResetv.cold.4
+ __Z32ispExclavePrivatePropertiesResetv.cold.5
+ __Z32ispExclavePrivatePropertiesResetv.cold.6
+ __Z32ispExclavePrivatePropertiesResetv.cold.7
+ __Z33_configureEkPropertyWriteInternalP20sExclaveKitIspCmdHdrjj
+ __Z34ispExclaveKitCommandChSendMetadataP20sExclaveKitIspCmdHdr.cold.6
+ __Z34ispExclaveKitCommandChSendMetadataP20sExclaveKitIspCmdHdr.cold.7
+ __Z38isNewSharedMemoryReplaySkipCopyEnabledP21ISPExclaveKitDefaults
+ __Z40isNewSharedMemoryReplayBufferDumpEnabledP21ISPExclaveKitDefaults
+ __Z48isNewSharedMemoryReplayBufferDumpSkipCopyEnabledP21ISPExclaveKitDefaults
+ __ZL48_convertFrameworkSensorMetaToTightbeamSensorMetaPKN25ISPExclaveKitAutoExposure31sExclaveKitIspCmdChSendMetadataEP45ispexclavekitshared_ekchannelsensormetadata_s
+ __ZL48_convertFrameworkSensorMetaToTightbeamSensorMetaPKN25ISPExclaveKitAutoExposure31sExclaveKitIspCmdChSendMetadataEP45ispexclavekitshared_ekchannelsensormetadata_s.cold.1
+ __ZN28ISPExclaveKitFileServiceBase12_getFileSizeERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN28ISPExclaveKitFileServiceBase14_buildFilePathE30MemoryWriteOnlyRegionTypeIndex26FileServiceBufferNameIndexm
+ __ZN28ISPExclaveKitFileServiceBase16_checkFileExistsE30MemoryWriteOnlyRegionTypeIndex26FileServiceBufferNameIndexm
+ __ZN28ISPExclaveKitFileServiceBase17getTotalFileCountE30MemoryWriteOnlyRegionTypeIndex26FileServiceBufferNameIndex
+ __ZN28ISPExclaveKitHostMetaManager12resetCounterEv
+ __ZN28ISPExclaveKitHostMetaManager13parseHostMetaEPh18eCISPMetaDataField
+ __ZN28ISPExclaveKitHostMetaManager13setRegionTypeE18HostMetaRegionType
+ __ZN28ISPExclaveKitHostMetaManager16_regionNameShortE
+ __ZN28ISPExclaveKitHostMetaManager19parseHostMetaSensorEPhP18HostMetaSensorInfo
+ __ZN28ISPExclaveKitHostMetaManager20readHostMetaFromDiskERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEP18HostMetaBufferInfo
+ __ZN28ISPExclaveKitHostMetaManager20readNextMetadataFileEP18HostMetaBufferInfo
+ __ZN28ISPExclaveKitHostMetaManager26readNextAndParseSensorMetaEP18HostMetaSensorInfoPm
+ __ZN28ISPExclaveKitHostMetaManager26readNextAndParseSensorMetaEP18HostMetaSensorInfoPm.cold.1
+ __ZN28ISPExclaveKitHostMetaManagerC1E18HostMetaRegionType
+ __ZN28ISPExclaveKitHostMetaManagerC2E18HostMetaRegionType
+ __ZN28ISPExclaveKitHostMetaManagerD1Ev
+ __ZN28ISPExclaveKitHostMetaManagerD2Ev
+ __ZNK28ISPExclaveKitHostMetaManager11getFileSizeERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZNK28ISPExclaveKitHostMetaManager13buildFilePathEm
+ __ZNK28ISPExclaveKitHostMetaManager13getRegionTypeEv
+ __ZNK28ISPExclaveKitHostMetaManager15checkFileExistsEm
+ __ZNK28ISPExclaveKitHostMetaManager17getTotalFileCountEv
+ __ZNK28ISPExclaveKitHostMetaManager19getCurrentFileIndexEv
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
+ __ZZL20_sensorMetaInjectionPKN25ISPExclaveKitAutoExposure31sExclaveKitIspCmdChSendMetadataEP45ispexclavekitshared_ekchannelsensormetadata_sE17s_hostMetaManager
+ __ZdaPvSt19__type_descriptor_t
+ __ZnamSt19__type_descriptor_t
+ ___Block_byref_object_copy_.27
+ ___Block_byref_object_dispose_.28
+ ____Z20_getEkBufferInternalP20sExclaveKitIspCmdHdrP28ISPExclaveKitFileDumpService26FileServiceBufferNameIndex_block_invoke
+ ___block_descriptor_tmp.30
+ ___block_descriptor_tmp.655
+ ___block_descriptor_tmp.724
+ ___block_descriptor_tmp.725
+ _ispexclavekitdebugmodule_ekchannelnewsharedmemoryreplaybuffergetoutput__decode
+ _ispexclavekitdebugmodule_ekdebug_channelnewsharedmemoryreplaybufferget
+ _ispexclavekitdebugmodule_ekdebug_channelnewsharedmemoryreplaybufferget.cold.1
+ _pFileDumpServiceAsynced
+ _read
+ _stat
- GCC_except_table47
- ___block_descriptor_tmp.650
- ___block_descriptor_tmp.719
- ___block_descriptor_tmp.720
CStrings:
+ "%s:%d - Created ISPExclaveKitHostMetaManager for channel %d\n"
+ "%s:%d - Metadata Replay - Ch %d: Failed to inject metadata, falling back to user metadata\n"
+ "%s:%d - Metadata Replay - Ch %d: Failed to read/parse metadata file from disk\n"
+ "%s:%d - Metadata Replay - Ch %d: Incoming frameID=%u, Internal counter=%zu, Disk frameID=%u\n"
+ "%s:%d - Metadata Replay - Ch %d: Successfully replaced sensor metadata from disk (file index %zu)\n"
+ "%s:%d - hostMeta injection: frameid=0x%x, ispdg=%d, timestamp=%lld\n"
+ "%s:%d - invalid available count: %zu vs list count: %zu\n"
+ "%s:%d - invalid buffer status\n"
+ "%s:%d - invalid channel index=%d\n"
+ "%s:%d - isNewSharedMemoryReplayBufferDumpEnabled=%d\n"
+ "%s:%d - isNewSharedMemoryReplayBufferDumpSkipCopyEnabled=%d\n"
+ "%s:%d - isNewSharedMemoryReplayEnabled=%d\n"
+ "%s:%d - isNewSharedMemoryReplaySkipCopyEnabled=%d\n"
+ "%s:%d - loading %s from disk\n"
+ "%s:%d - newSharedMemoryBufferDumpEnabled=%d\n"
+ "%s:%d - newSharedMemoryReplayEnabled=%d\n"
+ "%s:%d - pFileDumpServiceAsynced is nil, skip image dumping\n"
+ "%s:%d - starts dumping image to disk\n"
+ "%s_hostmetadata_output_%zu.meta"
+ "ISPExclaveKitCmdHandlerChAe.cpp"
+ "_convertFrameworkSensorMetaToTightbeamSensorMeta"
+ "_getEkBufferInternal"
+ "_sensorMetaInjection"
+ "newSharedMemoryBufferDumpEnabled"
+ "newSharedMemoryReplayEnabled"
+ "readNextAndParseSensorMeta"
+ "v504@?0{ispexclavekitdebugmodule_ekdebug_channelnewsharedmemoryreplaybufferget__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{ispexclavekitdebugmodule_ekchannelnewsharedmemoryreplaybuffergetoutput_s=Q[10{ispexclavekitdebugmodule_debugbufferdescriptor_s={ispexclavekitdebugmodule_debugbufferdescriptorbuffername_s=Q}QQ{ispexclavekitdebugmodule_debugbufferdescriptorbufferstatus_s=Q}QQ}]})}8"

```
