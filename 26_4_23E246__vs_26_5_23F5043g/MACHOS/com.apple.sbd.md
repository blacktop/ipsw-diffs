## com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

-694.100.38.0.0
-  __TEXT.__text: 0x52f88
+694.120.12.0.0
+  __TEXT.__text: 0x53e3c
   __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_stubs: 0x6f80
-  __TEXT.__objc_methlist: 0x2fa0
+  __TEXT.__objc_stubs: 0x7020
+  __TEXT.__objc_methlist: 0x304c
   __TEXT.__const: 0x150
-  __TEXT.__gcc_except_tab: 0x1d04
-  __TEXT.__cstring: 0x4256
-  __TEXT.__objc_methname: 0x7964
-  __TEXT.__oslogstring: 0x811d
-  __TEXT.__objc_classname: 0x74c
+  __TEXT.__gcc_except_tab: 0x1d10
+  __TEXT.__cstring: 0x432d
+  __TEXT.__objc_methname: 0x7a31
+  __TEXT.__oslogstring: 0x828d
+  __TEXT.__objc_classname: 0x77d
   __TEXT.__objc_methtype: 0x1128
-  __TEXT.__unwind_info: 0xe40
+  __TEXT.__unwind_info: 0xe70
   __DATA_CONST.__auth_got: 0x7e8
   __DATA_CONST.__got: 0x780
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x14e8
-  __DATA_CONST.__cfstring: 0x3c60
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __DATA_CONST.__const: 0x1538
+  __DATA_CONST.__cfstring: 0x3ce0
+  __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x138
+  __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x1a0
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x5250
-  __DATA.__objc_selrefs: 0x1fd8
+  __DATA.__objc_const: 0x53a8
+  __DATA.__objc_selrefs: 0x2008
   __DATA.__objc_ivar: 0x2c0
-  __DATA.__objc_data: 0x1180
+  __DATA.__objc_data: 0x1220
   __DATA.__data: 0x5a8
   __DATA.__bss: 0x130
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: D055FF67-61F8-3C59-99EB-9040EA1AC65E
-  Functions: 1404
+  UUID: 96A16B43-EF13-357C-9CC6-896A31438C0D
+  Functions: 1421
   Symbols:   504
-  CStrings:  3427
+  CStrings:  3454
 
CStrings:
+ "-[SecureBackupDaemon getFedCertificateWithRequest:reply:]"
+ "/escrowproxy/api/get_lrc_fed_type"
+ "<%@: %p>{clubType = %@}"
+ "Bailing on creating data wrapped to fed key due to no cert request: %@"
+ "Bailing on fetching fed certificate due to no cert request: %@"
+ "Empty escrowRecord"
+ "EscrowFederationRequest"
+ "EscrowFederationResponse"
+ "Fetched fed certificate with result: %@ %@"
+ "GETLRCFEDTYPE"
+ "Requesting federation cert for label: %@"
+ "Requesting federation cert for versions: %@"
+ "_fetchFedCertificateWithRequest:reply:"
+ "annotateProtectedData:request:timestamp:digest:"
+ "clubType"
+ "createDataWrappedToFedKeyWithRequest:reply:"
+ "fedCertificateWithTarget:altDSID:inEnvironment:"
+ "federationRequest:error:"
+ "fetchFedCertificateWithRequest:reply:"
+ "getFedCertificateWithRequest:reply:"
+ "unable to fetch fed certificate (lakitu error): %@"
+ "unable to fetch fed certificate: %@"
+ "v24@?0@\"EscrowFederationResponse\"8@\"NSError\"16"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
- "createDataWrappedToFedKeyWithRequest:error:"
- "fedCertificate:altDSID:inEnvironment:"

```
