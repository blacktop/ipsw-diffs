## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

-376.60.3.0.0
-  __TEXT.__text: 0x4d3e0
-  __TEXT.__auth_stubs: 0x1250
-  __TEXT.__objc_methlist: 0x1e44
-  __TEXT.__const: 0x1178
-  __TEXT.__oslogstring: 0x61a5
-  __TEXT.__cstring: 0x2d79
-  __TEXT.__gcc_except_tab: 0xaa4
-  __TEXT.__unwind_info: 0x994
-  __TEXT.__objc_classname: 0x518
-  __TEXT.__objc_methname: 0x4bf9
-  __TEXT.__objc_methtype: 0xe2c
-  __TEXT.__objc_stubs: 0x3840
-  __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x12a0
-  __DATA_CONST.__objc_classlist: 0x1b8
+397.100.12.0.0
+  __TEXT.__text: 0x4e274
+  __TEXT.__auth_stubs: 0x12d0
+  __TEXT.__objc_methlist: 0x1fc4
+  __TEXT.__const: 0x1200
+  __TEXT.__oslogstring: 0x5daf
+  __TEXT.__cstring: 0x3064
+  __TEXT.__gcc_except_tab: 0xb38
+  __TEXT.__unwind_info: 0xa08
+  __TEXT.__objc_classname: 0x55e
+  __TEXT.__objc_methname: 0x4f88
+  __TEXT.__objc_methtype: 0xe61
+  __TEXT.__objc_stubs: 0x3be0
+  __DATA_CONST.__got: 0x1b8
+  __DATA_CONST.__const: 0x1480
+  __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x21f8
-  __DATA_CONST.__objc_selrefs: 0x11c8
-  __DATA_CONST.__objc_arraydata: 0x410
-  __AUTH_CONST.__cfstring: 0x3cc0
-  __AUTH_CONST.__const: 0x260
+  __DATA_CONST.__objc_const: 0x2358
+  __DATA_CONST.__objc_selrefs: 0x12f0
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x298
+  __DATA_CONST.__objc_superrefs: 0x150
+  __DATA_CONST.__objc_arraydata: 0x428
+  __AUTH_CONST.__cfstring: 0x3fc0
+  __AUTH_CONST.__objc_const: 0x1978
+  __AUTH_CONST.__const: 0x280
   __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH_CONST.__objc_const: 0x18a0
-  __AUTH_CONST.__objc_arrayobj: 0x228
+  __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__auth_ptr: 0x28
-  __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x938
-  __AUTH.__objc_data: 0x1040
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x280
-  __DATA.__objc_superrefs: 0x148
-  __DATA.__objc_ivar: 0x1b8
-  __DATA.__data: 0x420
+  __AUTH_CONST.__objc_dictobj: 0xa0
+  __AUTH_CONST.__auth_got: 0x978
+  __AUTH.__objc_data: 0x10e0
+  __DATA.__objc_ivar: 0x1c8
+  __DATA.__data: 0x480
   __DATA.__common: 0x8
-  __DATA.__bss: 0xa0
+  __DATA.__bss: 0xb0
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
-  - /usr/lib/libimg4.dylib
+  - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  Functions: 1523
-  Symbols:   424
-  CStrings:  2283
+  Functions: 1537
+  Symbols:   436
+  CStrings:  2359
 
Symbols:
+ _AMFDRSealingMapCopyPropertyWithTag
+ _CRGenerateRepairReport
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_CRRepairReport
+ _OBJC_CLASS_$_NSMutableIndexSet
+ _dlopen
+ _dlsym
+ _xpc_array_create
+ _xpc_array_set_string
+ _xpc_dictionary_apply
+ _xpc_dictionary_create
+ _xpc_dictionary_get_count
+ _xpc_dictionary_get_dictionary
+ _xpc_dictionary_set_bool
+ _xpc_dictionary_set_uint64
+ _xpc_dictionary_set_value
+ _xpc_int64_get_value
- _AMFDRDiagnosticGenerateReport
- _SMCopyAllJobDictionaries
- _SMJobRemove
- _SMJobSubmit
- _os_variant_has_internal_content
CStrings:
+ "\x01\x12"
+ "\b\x1a\x15\x1f\a"
+ "%@-%@"
+ "%s service already %s"
+ "%s: error %lld"
+ "/usr/lib/system/libxpc.dylib"
+ "0.2"
+ "@\"NSError\""
+ "@24@0:8q16"
+ "ADCL"
+ "AMFDRDataAppendPermissionsString Claim failed"
+ "AMFDRSealingMapCopyMultiInstanceForClass failed, error: %@"
+ "Added non-make data to merged data: %@-%@"
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "BackGlass"
+ "CRRepairReport"
+ "CRRepairReportItem"
+ "CoreRepairCoreXPCServiceProtocol"
+ "Could not get Sealed Data Instance"
+ "Current serial number: %@ doesn't match SPC KGBSerialNumber: %@"
+ "Failed to decode sealing manifest: %@"
+ "Failed to find libxpc API"
+ "Failed to get local sealing manifest"
+ "Failed to request FDR permissions"
+ "Failed to request FDRSNMAP Permissions"
+ "Failed to request SEAL-SIK KBB Permissions"
+ "Generate report timeout"
+ "Get report timeout"
+ "Got error: %@"
+ "Got report"
+ "GpC3"
+ "Live instance missing for %@: %@"
+ "Live property missing for %@: %@"
+ "MTUB"
+ "Malformed dataClasses or dataInstances: %@ %@"
+ "Number of data classes and instances mismatches"
+ "Property %@ does not exist"
+ "RearSystem"
+ "Reason"
+ "RepairHistory"
+ "State"
+ "Status"
+ "System"
+ "T@\"NSDictionary\",&,N,V_claimDict"
+ "T@\"NSDictionary\",&,N,V_updateClassDict"
+ "T@\"NSError\",&,N,V_error"
+ "T@\"NSString\",&,N,V_date"
+ "T@\"NSString\",&,N,V_name"
+ "T@\"NSString\",?,R,C"
+ "Tq,N,V_statusCode"
+ "Unsealed: %@"
+ "UnsealedComponents"
+ "Version"
+ "^v24@0:8r*16"
+ "^{__AMFDR=}16@0:8"
+ "_addDataClassAndInstancesToMutableArray:dataClasses:dataInstances:withError:"
+ "_claimDict"
+ "_createFDRLocal"
+ "_date"
+ "_error"
+ "_name"
+ "_statusCode"
+ "_updateClassDict"
+ "_xpc_domain_routine"
+ "addIndex:"
+ "array"
+ "by-cli"
+ "com.apple.CoreRepairCoreXPCService"
+ "determineRepairStatus:repairHistory:"
+ "disable"
+ "dlopen failed"
+ "dlsym(%s) failed"
+ "enable"
+ "error"
+ "errors"
+ "findUnsealedDataWithError:"
+ "force"
+ "generateRepairReport:withReply:"
+ "generateReport:error:"
+ "getLibXPCInternalWithSymbol:"
+ "indexSet"
+ "initWithName:"
+ "initWithServiceName:"
+ "insertItem:item:"
+ "itemWithName:"
+ "legacy-load"
+ "loaded"
+ "localizedDescription"
+ "minusSet:"
+ "no-einprogress"
+ "paths"
+ "populateDCSignedComponents"
+ "populateFaultyComponents"
+ "populateRCHLHistory"
+ "populateUnsealedComponents"
+ "prefetchPermissionsForSealing:fdrRemote:fdrLocal:claimClassDict:makeClasses:makeInstances:patchClasses:patchInstances:get1Classes:get1Instances:"
+ "prefetchPermissionsWith:returnError:"
+ "q32@0:8^{__AMFDR=}16^@24"
+ "q96@0:8^@16^{__AMFDR=}24^{__AMFDR=}32@40@48@56@64@72@80@88"
+ "remoteObjectProxyWithErrorHandler:"
+ "removeObjectsAtIndexes:"
+ "setClaimDict:"
+ "setDate:"
+ "setError:"
+ "setName:"
+ "setStatusCode:"
+ "setUpdateClassDict:"
+ "setValue:forKey:"
+ "translateToExternalName:"
+ "type"
+ "unloaded"
+ "v16@?0@\"NSDictionary\"8"
+ "withDate:"
+ "withError:"
+ "withStatus:"
+ "xpc_release"
+ "\xf0\xa1"
- "\n\x1a\x15\x1f\x05"
- "%@ job found"
- "AMFDRAppendPermissionsString Claim 1.0 failed"
- "AMFDRMigrateCredentials for Sealing error: %@"
- "AMFDRPermisisonRequest for Sealing error: %@"
- "AMFDRSealingMapCopyManifestProperties failed:%@"
- "Cannot create options"
- "Cannot generate FDR diagnostic report"
- "Current Srnm:%@ doesn't match KGBSrnm:%@"
- "Current serial number %@ doesn't match SPC KGBSerialNumber %@"
- "DOFU of battery is in future"
- "Daemon already running"
- "Daemon not running"
- "FDRSNMAP Permissions request failed."
- "Failed to copy FDRSNMAP of KBBSrNM:%@"
- "Failed to parse plist: %@"
- "Failed to read file: %@"
- "Failed to remove launchd job. Error: %@"
- "Failed to submit launchd job. Error: %@"
- "Label"
- "SEAL-SIK KBB Permissions request failed."
- "Unable to Create Persmission String using KBB sealheaders"
- "getDiagnosticReport"
- "job: %@"
- "old SealingManifestCopyDataClassesInstancesAndProperties: %@"
- "prefetchPermissionsForSealing:fdrRemote:fdrLocal:makeClasses:makeInstances:patchClasses:patchInstances:get1Classes:get1Instances:"
- "prefetchPermissionsWith:claimClassDict:returnError:"
- "q40@0:8^{__AMFDR=}16@24^@32"
- "q88@0:8^@16^{__AMFDR=}24^{__AMFDR=}32@40@48@56@64@72@80"
- "\xf0\xc1"

```
