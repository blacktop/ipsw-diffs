## com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

-638.40.26.0.0
-  __TEXT.__text: 0x4a45c
-  __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_stubs: 0x64c0
-  __TEXT.__objc_methlist: 0x25fc
+638.42.1.0.0
+  __TEXT.__text: 0x4c29c
+  __TEXT.__auth_stubs: 0xfc0
+  __TEXT.__objc_stubs: 0x67a0
+  __TEXT.__objc_methlist: 0x270c
   __TEXT.__const: 0x148
-  __TEXT.__gcc_except_tab: 0x1b44
-  __TEXT.__cstring: 0x3b81
-  __TEXT.__objc_methname: 0x6d68
-  __TEXT.__oslogstring: 0x7b36
+  __TEXT.__gcc_except_tab: 0x1b64
+  __TEXT.__cstring: 0x3d34
+  __TEXT.__objc_methname: 0x7037
+  __TEXT.__oslogstring: 0x7d87
   __TEXT.__objc_classname: 0x70d
-  __TEXT.__objc_methtype: 0xf6f
-  __TEXT.__unwind_info: 0xbd0
-  __DATA_CONST.__auth_got: 0x7e0
-  __DATA_CONST.__got: 0x688
+  __TEXT.__objc_methtype: 0xfab
+  __TEXT.__unwind_info: 0xc10
+  __DATA_CONST.__auth_got: 0x7f0
+  __DATA_CONST.__got: 0x6b0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1430
-  __DATA_CONST.__cfstring: 0x36e0
+  __DATA_CONST.__cfstring: 0x3800
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x1a0
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x5888
-  __DATA.__objc_selrefs: 0x1c50
-  __DATA.__objc_ivar: 0x288
+  __DATA.__objc_const: 0x59c8
+  __DATA.__objc_selrefs: 0x1d00
+  __DATA.__objc_ivar: 0x294
   __DATA.__objc_data: 0x10e0
   __DATA.__data: 0x5a8
   __DATA.__bss: 0x120

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1270
-  Symbols:   472
-  CStrings:  2739
+  Functions: 1300
+  Symbols:   479
+  CStrings:  2793
 
Symbols:
+ _OBJC_CLASS_$_AppleIDPasswordMetadata
+ _OBJC_CLASS_$_NSUserDefaults
+ _SecureBackupIsGuitarfishEnabled
+ __os_log_fault_impl
+ _kEscrowServiceGuitarfishLabel
+ _kEscrowServiceGuitarfishTokenLabel
+ _kSecureBackupGuitarfishRecoveryTokenMetadataKey
CStrings:
+ "-[SecureBackupDaemon enableGuitarfishTokenWithRequest:reply:]"
+ "-[SecureBackupDaemon recoverGuitarfishTokenWithRequest:reply:]"
+ "/\x0f\x03"
+ "@\"AppleIDPasswordMetadata\""
+ "@\"AppleIDPasswordMetadata\"16@0:8"
+ "DEMO: parsing srp init: %!@(MISSING), %!@(MISSING)"
+ "DEMO: proto %!@(MISSING), salt %!@(MISSING), iterations %!d(MISSING)"
+ "Disallowing %!@(MISSING) operation for label %!@(MISSING) (due to com.apple.cloudservices/PCS-NoRecord)"
+ "Disallowing %!@(MISSING) operation for label %!@(MISSING) (due to com.apple.cloudservices/PCS-UpdateDisabled)"
+ "Filtering PCS record label %!@(MISSING) (due to com.apple.cloudservices/PCS-NoRecord)"
+ "Guitarfish token recovery returned: %!@(MISSING)"
+ "GuitarfishDemo"
+ "No passphrase provided"
+ "No passphrase provided; skipping SRPInit before it fails later"
+ "PCS-NoRecord"
+ "PCS-UpdateDisabled"
+ "Performing Guitarfish token recovery"
+ "T@\"AppleIDPasswordMetadata\",R,N"
+ "T@\"AppleIDPasswordMetadata\",R,N,V_appleIDPasswordMetadata"
+ "TB,R,N,V_guitarfish"
+ "TB,R,N,V_guitarfishToken"
+ "_appleIDPasswordMetadata"
+ "_checkFetchOperationWithHandler:"
+ "_checkReadOperationWithHandler:"
+ "_checkUpdateOperationWithHandler:"
+ "_guitarfish"
+ "_guitarfishToken"
+ "appleIDPasswordMetadata"
+ "artificial error injected (com.apple.cloudservices/PCS-NoRecord)"
+ "artificial error injected (com.apple.cloudservices/PCS-UpdateDisabled)"
+ "com.apple.cloudservices"
+ "enableGuitarfishTokenWithRequest:reply:"
+ "error parsing Guitarfish record: %!@(MISSING)"
+ "falling back from recover_request v1 to v0 (%!@(MISSING))"
+ "falling back from recover_request v2 to v0 (%!@(MISSING))"
+ "guitarfish"
+ "guitarfish token data version does not match version in escrow"
+ "guitarfishToken"
+ "initFromResponseFilterPCS:"
+ "initWithProto:salt:iterations:"
+ "initWithRequest:validate:reqVersion:"
+ "initWithSuiteName:"
+ "isPcsRecord"
+ "iterations"
+ "pcsNoRecord"
+ "pcsUpdateDisabled"
+ "proto"
+ "rawPassword not provided"
+ "recoverGuitarfishTokenWithRequest:reply:"
+ "salt"
+ "setAppleIDPasswordMetadata:"
+ "setGfRecord:"
+ "setPasswordMetadataWithRequest:response:ses:"
+ "validatePassphrasePresentOrPending"
- "/\x0f\x02"
- "falling back from recover_request v1 to v0"
- "falling back from recover_request v2 to v0"

```
