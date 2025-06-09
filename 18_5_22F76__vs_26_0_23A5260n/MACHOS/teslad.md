## teslad

> `/usr/libexec/teslad`

```diff

-20.5.1.2.0
-  __TEXT.__text: 0xdcf8
+43.0.0.0.0
+  __TEXT.__text: 0xe7fc
   __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_stubs: 0x24a0
-  __TEXT.__objc_methlist: 0x1504
+  __TEXT.__objc_stubs: 0x2580
+  __TEXT.__objc_methlist: 0x1694
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0x6c
-  __TEXT.__oslogstring: 0xc14
-  __TEXT.__cstring: 0x132a
-  __TEXT.__objc_classname: 0x5d0
-  __TEXT.__objc_methtype: 0xb46
+  __TEXT.__oslogstring: 0xc92
+  __TEXT.__cstring: 0x1357
+  __TEXT.__objc_classname: 0x6ac
+  __TEXT.__objc_methtype: 0xb8e
   __TEXT.__dlopen_cstrs: 0xaa
-  __TEXT.__objc_methname: 0x2c4f
-  __TEXT.__unwind_info: 0x388
+  __TEXT.__objc_methname: 0x2d43
+  __TEXT.__unwind_info: 0x3d0
   __DATA_CONST.__auth_got: 0x2a8
-  __DATA_CONST.__got: 0x350
-  __DATA_CONST.__const: 0x7a0
-  __DATA_CONST.__cfstring: 0x1ca0
-  __DATA_CONST.__objc_classlist: 0x170
+  __DATA_CONST.__got: 0x358
+  __DATA_CONST.__const: 0x808
+  __DATA_CONST.__cfstring: 0x1da0
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0xf0
-  __DATA.__objc_const: 0x3538
-  __DATA.__objc_selrefs: 0xb60
-  __DATA.__objc_ivar: 0xe4
-  __DATA.__objc_data: 0xe60
+  __DATA.__objc_const: 0x3a08
+  __DATA.__objc_selrefs: 0xb98
+  __DATA.__objc_ivar: 0xf4
+  __DATA.__objc_data: 0x1040
   __DATA.__data: 0x240
   __DATA.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3C9184A8-58FE-36D2-A3E8-545254D6EBA6
-  Functions: 384
-  Symbols:   188
-  CStrings:  1155
+  UUID: F38126C7-DA10-3BA3-ABA8-947F5699714F
+  Functions: 410
+  Symbols:   187
+  CStrings:  1192
 
Symbols:
- ___NSDictionary0__struct
CStrings:
+ "/deviceRegister"
+ "/endMdmMigration"
+ "/startMdmMigration"
+ "/v2/profile"
+ "/v2/unenroll"
+ "@56@0:8@16q24@32@40@48"
+ "CCDEndMDMMigrationRequestPayload"
+ "CCDEnrollmentEndMDMMigrationOperation"
+ "CCDEnrollmentEndMDMMigrationRequest"
+ "CCDEnrollmentStartMDMMigrationOperation"
+ "CCDEnrollmentStartMDMMigrationRequest"
+ "CCDStartMDMMigrationRequestPayload"
+ "End MDM Migration Response: %{public}@"
+ "EndMdmMigration"
+ "HasUndergoneMigration"
+ "IgnoreMDMFromBackup"
+ "IsReturnToService"
+ "MDMMigration feature flag is not enabled. Return..."
+ "Start MDM Migration Response: %{public}@"
+ "StartMdmMigration"
+ "T@\"NSString\",&,N,V_serverUID"
+ "T@\"NSString\",&,N,V_status"
+ "_serverUID"
+ "_status"
+ "depBaseURLStringWithURLString:"
+ "dmc_jsonDictionaryFromData:"
+ "do-not-use-profile-from-backup"
+ "errorWithDomain:code:description:underlyingError:errorType:"
+ "has-undergone-migration"
+ "https://iprofiles.apple.com"
+ "internalErrorWithCode:underlyingError:"
+ "is-multi-user & is-return-to-service is mutual exclusive."
+ "is-return-to-service"
+ "makeEndMDMMigrationRequestWithServerUID:status:completionBlock:"
+ "makeStartMDMMigrationRequestWithCompletionBlock:"
+ "serverUID"
+ "server_uid"
+ "setServerUID:"
+ "setStatus:"
+ "status"
+ "stringByAppendingPathComponent:"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B@\"NSDictionary\"@\"NSError\">32"
- "@48@0:8@16q24@32@40"
- "AllowInvalidNetworkCertificates"
- "IsRapidReturnToService"
- "MCTeslaDeviceRegisterURL"
- "MCTeslaUnenrollURL"
- "depConfigurationEnrollmentURLStringWithURLString:"
- "depRemoveEnrollmentURLStringWithURLString:"
- "deviceRegisterURLStringWithURLString:"
- "errorWithDomain:code:description:errorType:"
- "https://iprofiles.apple.com/deviceRegister"
- "https://iprofiles.apple.com/v2/profile"
- "https://iprofiles.apple.com/v2/unenroll"
- "is-multi-user & is-rapid-return-to-service is mutual exclusive."
- "is-rapid-return-to-service"

```
