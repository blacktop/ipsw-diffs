## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-64.0.4.0.1
-  __TEXT.__text: 0xaae78
-  __TEXT.__auth_stubs: 0xe90
-  __TEXT.__objc_stubs: 0x2340
+57.0.2.0.0
+  __TEXT.__text: 0xaabc4
+  __TEXT.__auth_stubs: 0xec0
+  __TEXT.__objc_stubs: 0x2360
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x2f0
-  __TEXT.__const: 0x842f
-  __TEXT.__gcc_except_tab: 0xa2e4
-  __TEXT.__cstring: 0x4346
-  __TEXT.__oslogstring: 0x251d9
+  __TEXT.__objc_methlist: 0x84c
+  __TEXT.__const: 0x8577
+  __TEXT.__gcc_except_tab: 0xa47c
+  __TEXT.__cstring: 0x440f
+  __TEXT.__oslogstring: 0x25ae2
   __TEXT.__objc_classname: 0x1b7
-  __TEXT.__objc_methname: 0x28b0
+  __TEXT.__objc_methname: 0x28f7
   __TEXT.__objc_methtype: 0x111e
-  __TEXT.__unwind_info: 0x3398
-  __DATA_CONST.__auth_got: 0x758
-  __DATA_CONST.__got: 0x450
+  __TEXT.__unwind_info: 0x3378
+  __DATA_CONST.__auth_got: 0x770
+  __DATA_CONST.__got: 0x470
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x6bd8
-  __DATA_CONST.__cfstring: 0x47c0
+  __DATA_CONST.__const: 0x6c78
+  __DATA_CONST.__cfstring: 0x4880
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x1828
-  __DATA.__objc_selrefs: 0x980
+  __DATA.__objc_const: 0xe08
+  __DATA.__objc_selrefs: 0xc58
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x3d8
-  __DATA.__bss: 0x598
+  __DATA.__bss: 0x5d8
   __DATA.__common: 0x48
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2736
-  Symbols:   391
-  CStrings:  3037
+  Functions: 2728
+  Symbols:   396
+  CStrings:  3073
 
Symbols:
+ _XPC_ACTIVITY_CHECK_IN
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ _container_system_group_path_for_identifier
+ _xpc_activity_copy_criteria
+ _xpc_activity_set_criteria
+ _xpc_equal
- __ZNKSt9exception4whatEv
- __ZNSt9exceptionD2Ev
- __ZTISt9exception
CStrings:
+ "EQ_HISTORY_MANIFEST_DOWNLOAD_PERIOD_SECONDS"
+ "EQ_HISTORY_MANIFEST_FILE_NAME"
+ "com.apple.safetyalerts.ehmd"
+ "eqSensing"
+ "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
+ "manifestDownloadPeriod"
+ "manifestFileName"
+ "stringByAppendingPathComponent:"
+ "systemgroup.com.apple.safetyalerts"
+ "v20@?0r^v8B16"
+ "{\"msg%{public}.0s\":\"#assetConfig,getEarthquakeSensingConfig\"}"
+ "{\"msg%{public}.0s\":\"#assetConfig,readEqSensingAsset\", \"asset\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#assetConfig,readEqSensingAsset,nil asset dictionary\"}"
+ "{\"msg%{public}.0s\":\"#assetConfig,readEqSensingAsset,nil config\"}"
+ "{\"msg%{public}.0s\":\"#assetConfig,readEqSensingAsset,nil eqSensing dictionary\"}"
+ "{\"msg%{public}.0s\":\"#ehmd,download completed\", \"filePath\":%{private, location:escape_only}s, \"result\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#ehmd,init\"}"
+ "{\"msg%{public}.0s\":\"#ehmd,invalid file downloader\"}"
+ "{\"msg%{public}.0s\":\"#ehmd,released\"}"
+ "{\"msg%{public}.0s\":\"#md,downloadManifest,download completed\", \"result\":%{private}hhd, \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,downloadManifest,downloader not available\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,downloadManifest,downloading\"}"
+ "{\"msg%{public}.0s\":\"#md,downloadManifest,igneous group container not available\"}"
+ "{\"msg%{public}.0s\":\"#md,downloadManifest,pull channel name unavailable\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,empty file name\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,empty identifier\"}"
+ "{\"msg%{public}.0s\":\"#md,init\"}"
+ "{\"msg%{public}.0s\":\"#md,invalid file downloader\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,negative download period\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,onXPCActivityTriggered\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,processXPCActivity,activity is nil\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,processXPCActivity,failed to set state\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,processXPCActivity,unexpected xpcActivity\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,processXPCActivity,xpcActivity checkin\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,processXpcActivity\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,released\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,scheduleXPCActivity,updating xpc criteria\", \"existingCriteria\":%{private, location:escape_only}@, \"criteria\":%{private, location:escape_only}@, \"id\":%{private, location:escape_only}s}"
- "setSafetyAlertsVersion:"

```
