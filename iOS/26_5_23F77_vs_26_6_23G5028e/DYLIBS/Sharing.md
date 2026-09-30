## Sharing

> `/System/Library/PrivateFrameworks/Sharing.framework/Sharing`

```diff

-2094.60.51.0.0
-  __TEXT.__text: 0x34bc3c
+2094.70.31.0.0
+  __TEXT.__text: 0x34bc78
   __TEXT.__auth_stubs: 0x4c90
-  __TEXT.__objc_methlist: 0x147f4
+  __TEXT.__objc_methlist: 0x1480c
   __TEXT.__const: 0x213b4
-  __TEXT.__cstring: 0x39ee5
+  __TEXT.__cstring: 0x39f15
   __TEXT.__gcc_except_tab: 0x3434
   __TEXT.__oslogstring: 0x9fde
   __TEXT.__dlopen_cstrs: 0x640

   __TEXT.__unwind_info: 0xdf58
   __TEXT.__eh_frame: 0xd61c
   __TEXT.__objc_classname: 0x2f56
-  __TEXT.__objc_methname: 0x2ea07
+  __TEXT.__objc_methname: 0x2ea37
   __TEXT.__objc_methtype: 0x6840
   __TEXT.__objc_stubs: 0x19a40
   __DATA_CONST.__got: 0x1208
-  __DATA_CONST.__const: 0x76e0
+  __DATA_CONST.__const: 0x76e8
   __DATA_CONST.__objc_classlist: 0x8b0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x3d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9868
+  __DATA_CONST.__objc_selrefs: 0x9878
   __DATA_CONST.__objc_protorefs: 0x1f0
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x540
   __DATA_CONST.__objc_arraydata: 0x448
   __AUTH_CONST.__auth_got: 0x2660
   __AUTH_CONST.__const: 0x15c40
-  __AUTH_CONST.__cfstring: 0x13c20
-  __AUTH_CONST.__objc_const: 0x398f0
+  __AUTH_CONST.__cfstring: 0x13c60
+  __AUTH_CONST.__objc_const: 0x39920
   __AUTH_CONST.__objc_intobj: 0x660
   __AUTH_CONST.__objc_dictobj: 0x5c8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH.__objc_data: 0x3228
   __AUTH.__data: 0x2b98
-  __DATA.__objc_ivar: 0x25ac
+  __DATA.__objc_ivar: 0x25b0
   __DATA.__data: 0xc4f8
   __DATA.__bss: 0x398e0
   __DATA.__common: 0xc8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 038DE752-5F8F-3BAD-AEF6-C2B113642841
-  Functions: 22396
-  Symbols:   39700
-  CStrings:  20178
+  UUID: 09356778-D014-3DC6-9947-196E1832136E
+  Functions: 22398
+  Symbols:   39705
+  CStrings:  20186
 
Symbols:
+ -[SFNFCTagReaderUIController accessMode]
+ -[SFNFCTagReaderUIController setAccessMode:]
+ _OBJC_IVAR_$_SFNFCTagReaderUIController._accessMode
+ ___44-[SFAuthenticationManager isEnabledForType:]_block_invoke.473
+ ___55-[SFAuthenticationManager _handleEnabledDevicesChanged]_block_invoke.467
+ ___67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke.543
+ ___67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_2.544
+ ___67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_2.544.cold.1
+ ___67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_3.545
+ ___67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_3.545.cold.1
+ ___72-[SFAuthenticationManager listEligibleDevicesForType:completionHandler:]_block_invoke.487
+ ___73-[SFAuthenticationManager listCandidateDevicesForType:completionHandler:]_block_invoke.490
+ ___block_literal_global.472
+ ___block_literal_global.502
+ ___block_literal_global.504
+ ___block_literal_global.509
+ ___block_literal_global.511
+ ___block_literal_global.513
+ ___block_literal_global.518
+ ___block_literal_global.520
+ ___block_literal_global.539
+ ___block_literal_global.547
- ___44-[SFAuthenticationManager isEnabledForType:]_block_invoke.470
- ___55-[SFAuthenticationManager _handleEnabledDevicesChanged]_block_invoke.464
- ___67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke.540
- ___67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_2.541
- ___67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_2.541.cold.1
- ___67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_3.542
- ___67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_3.542.cold.1
- ___72-[SFAuthenticationManager listEligibleDevicesForType:completionHandler:]_block_invoke.484
- ___73-[SFAuthenticationManager listCandidateDevicesForType:completionHandler:]_block_invoke.487
- ___block_literal_global.469
- ___block_literal_global.499
- ___block_literal_global.501
- ___block_literal_global.508
- ___block_literal_global.510
- ___block_literal_global.517
- ___block_literal_global.536
- ___block_literal_global.544
CStrings:
+ "SFAuthenticationTypePAURangeOnlySilently"
+ "Tq,N,V_accessMode"
+ "Unimplemented at /Library/Caches/com.apple.xbs/4F2EE7E3-F757-4AA6-8E50-592140E58240/TemporaryDirectory.SFRQ7B/Sources/Sharing/Framework/SFTokenBucket.m:142 : Don't use init on SFTokenBucketWithDups"
+ "Unimplemented at /Library/Caches/com.apple.xbs/4F2EE7E3-F757-4AA6-8E50-592140E58240/TemporaryDirectory.SFRQ7B/Sources/Sharing/Framework/SFTokenBucket.m:25 : Don't use init on SFTokenBucket"
+ "_accessMode"
+ "accessMode"
+ "setAccessMode:"
- "Unimplemented at /Library/Caches/com.apple.xbs/E41F33CD-1B2C-416D-9D12-0E1E840BBE7A/TemporaryDirectory.1P6g6T/Sources/Sharing/Framework/SFTokenBucket.m:142 : Don't use init on SFTokenBucketWithDups"
- "Unimplemented at /Library/Caches/com.apple.xbs/E41F33CD-1B2C-416D-9D12-0E1E840BBE7A/TemporaryDirectory.1P6g6T/Sources/Sharing/Framework/SFTokenBucket.m:25 : Don't use init on SFTokenBucket"

```
